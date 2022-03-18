"""
Author: Daniel Janci
This program is a modification of a problem of savages from:
https://uim.fei.stuba.sk/i-ppds/5-cvicenie-problem-fajciarov-problem-divochov-%f0%9f%9a%ac/
"""
from time import sleep
from random import randint
from fei.ppds import Thread, Mutex, Semaphore, print

# number of savages
S = 10
# number of cooks
C = 5
# number of meals
M = 7


class SimpleBarrier:
    """
    Contains variables: n with value from parameter n, count with default value 0, mutex is an instance of Mutex,
    barrier is an instance of Semaphore.
    """
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)

    def wait(self, shared, each=None, last=None):
        """
        This implementation of a barrier additionally, when count is equal to n, sets value servings in shared to M and
        signalizes to savages that pot is full.
        :param shared: instance of class Shared
        :param each: string
        :param last: string
        :return: None
        """
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
    """
    Contains variables: servings with value from parameter m, mutex is an instance of Mutex, full_pot and empty_pot is
    an instance of Semaphore, barrier is an instance of SimpleBarrier
    """
    def __init__(self, m):
        self.servings = m
        self.mutex = Mutex()
        self.full_pot = Semaphore(0)
        self.empty_pot = Semaphore(0)
        self.barrier = SimpleBarrier(C)


def eating():
    """
    Simulates eating of savages with sleep function.
    :return: None
    """
    sleep(randint(20, 50) / 100)


def cooking():
    """
    Simulates cooking of cooks with sleep function.
    :return: None
    """
    sleep(randint(50, 200) / 100)


def savage(i, shared):
    """
    Function decrements variable servings in shared by one when savage eats a meal. If there is no more meals (servings)
    one savage signalizes all cooks so they can start cooking.
    :param i: identificator of a savage
    :param shared: instance of class Shared
    :return: None
    """
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
    """
    Function allows cook to start cooking after he was signalized. Then every cook stops at barrier where they wait each
    other.
    :param i: identificator of a cook
    :param shared: instance of class Shared
    :return: None
    """
    while True:
        shared.empty_pot.wait()
        cooking()
        shared.barrier.wait(shared, each=f'cook {i}: is cooking', last=f'cook {i}: dinner is ready')


def main():
    """
    Creates an instance of class Shared with value 0, S number of threads for savages and C number of threads fo cooks.
    :return: None
    """
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
