from time import sleep
from random import randint
from fei.ppds import Thread, Mutex, Semaphore, print

S = 10
C = 5
M = 7


class SimpleBarrier:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)

    def wait(self, shared, each=None, last=None):
        self.mutex.lock()
        self.count += 1
        if each:
            print(each)
        if self.count == self.n:
            if last:
                print(last)
            self.count = 0
            shared.servings = M
            shared.full_pot.signal()
            self.barrier.signal(self.n)
        self.mutex.unlock()
        self.barrier.wait()


class Shared:
    def __init__(self, m):
        self.servings = m
        self.mutex = Mutex()
        self.full_pot = Semaphore(0)
        self.empty_pot = Semaphore(0)
        self.barrier = SimpleBarrier(C)


def eating():
    sleep(randint(20, 50) / 100)


def cooking():
    sleep(randint(50, 200) / 100)


def savage(i, shared):
    sleep(randint(1, 100) / 100)
    while True:
        shared.mutex.lock()
        if shared.servings == 0:
            print(f'savage {i} wakes up cooks')
            shared.empty_pot.signal(C)
            shared.full_pot.wait()
        eating()
        print(f'savage {i} eats')
        shared.servings -= 1
        shared.mutex.unlock()


def cook(i, shared):
    while True:
        shared.empty_pot.wait()
        cooking()
        shared.barrier.wait(shared, each=f'cook {i}: is cooking', last=f'cook {i}: dinner is ready')


def main():
    shared = Shared(0)
    threads = []
    for i in range(S):
        threads.append(Thread(savage, i, shared))
    for j in range(C):
        threads.append(Thread(cook, j, shared))

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
