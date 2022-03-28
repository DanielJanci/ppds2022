"""
Author: Daniel Janci
This program implements the problem of the barbershop.
"""
from fei.ppds import Semaphore, Mutex, Thread, print
from time import sleep
from random import randint


class Shared:
    def __init__(self, n):
        self.roomCapacity = n
        self.customers = 0
        self.room = []
        self.queue = []
        self.customer = Semaphore(0)
        self.barber = Semaphore(0)
        self.customerDone = Semaphore(0)
        self.barberDone = Semaphore(0)
        self.mutex = Mutex()


def customer(i, s):
    while True:
        sleep(randint(5, 10) / 10)
        s.mutex.lock()
        if s.customers == s.roomCapacity:
            print(f'The waiting room is full. Customers in the waiting room: {s.room}')
            s.mutex.unlock()
            continue
        s.room.append(i)
        s.customers += 1
        print(f'Customer {i} entered the waiting room. Customers in the waiting room: {s.room}')
        s.mutex.unlock()

        s.customer.signal()
        s.barber.wait()
        s.customerDone.signal()
        s.barberDone.wait()

        s.mutex.lock()
        s.room.remove(i)
        s.customers -= 1
        print(f'Customer {i} got a haircut. Customers in the waiting room: {s.room}')
        s.mutex.unlock()


def barber(s):
    while True:
        s.customer.wait()
        s.barber.signal()
        cut_hair()
        s.customerDone.wait()
        s.barberDone.signal()


def cut_hair():
    print('Barber is working.')
    sleep(randint(20, 50) / 100)


def main():
    c = 10
    room = 5
    s = Shared(room)
    threads = []
    for i in range(c):
        threads.append(Thread(customer, i, s))
    threads.append(Thread(barber, s))

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
