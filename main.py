from time import sleep
from random import randint
from fei.ppds import Thread, Mutex, Semaphore, print

N = 10
M = 3


class SimpleBarrier:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)

    def wait(self, each=None, last=None):
        self.mutex.lock()
        self.count += 1
        if each:
            print(each)
        if self.count == self.n:
            if last:
                print(last)
            self.count = 0
            self.barrier.signal(self.n)
        self.mutex.unlock()
        self.barrier.wait()


class Shared:
    def __init__(self, m):
        self.servings = m
        self.mutex = Mutex()
        self.empty_pot = Semaphore(0)
        self.full_pot = Semaphore(0)
        self.b1 = SimpleBarrier(N)
        self.b2 = SimpleBarrier(N)


def eat():
    # print(f'savage {i}: eat start')
    sleep(randint(20, 50) / 100)
    # print(f'savage {i}: eat end')


def savage(i, shared):
    sleep(randint(1, 100) / 100)
    while True:
        shared.b1.wait()
        shared.b2.wait(each=f'savage {i}: before dinner', last=f'savage {i}: everyone is done eating')
        shared.mutex.lock()
        if shared.servings == 0:
            shared.empty_pot.signal()
            shared.full_pot.wait()
        print(f'savage {i}: take from pot')
        shared.servings -= 1
        shared.mutex.unlock()
        eat()


def cook(shared):
    while True:
        shared.empty_pot.wait()
        print(f'cook: cooking')
        sleep(randint(50, 200) / 100)
        print(f'cook: {M} servings --> pot')
        shared.servings += M
        shared.full_pot.signal()


def main():
    shared = Shared(0)
    threads = []
    for i in range(N):
        threads.append(Thread(savage, i, shared))
    threads.append(Thread(cook, shared))

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
