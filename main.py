"""
Author: Daniel Janci
This program implements the problem of the barbershop.
"""
from fei.ppds import Semaphore, Mutex, Thread, print
from time import sleep
from random import randint


class Shared:
    """
    Contains variables: roomCapacity with value from parameter n, customers with default value 0, room is an empty
    array. Variables: customer, barber, customerDone, barberDone are instances of Semaphore and mutex is an instance of
    Mutex. Variable room holds indetificators of customers inside the waiting room, its only used for printing.
    """
    def __init__(self, n):
        self.roomCapacity = n
        self.customers = 0
        self.room = []
        self.customer = Semaphore(0)
        self.barber = Semaphore(0)
        self.customerDone = Semaphore(0)
        self.barberDone = Semaphore(0)
        self.mutex = Mutex()


def customer(i, s):
    """
    When customer comes to a waiting room the number of customers is incremented and the indentificator af that customer
    is put into s.room. Function gives signal to barber that customer is ready and waits until he is done. After that
    the number of customers is decremented and the indentificator of the cutomer is removed from s.room.
    :param i: indentificator of a customer
    :param s: instance of Shared
    :return: None
    """
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
    """
    Barber waits for customers signal then proceeds to make a haircut and then gives signal to customers that he has
    finished.
    :param s: instance of Shared
    :return: None
    """
    while True:
        s.customer.wait()
        s.barber.signal()
        cut_hair()
        s.customerDone.wait()
        s.barberDone.signal()


def cut_hair():
    """
    Simulates cutting hair with a sleep function.
    :return: None
    """
    print('Barber is working.')
    sleep(randint(20, 50) / 100)


def main():
    """
    Creates threads for c number of customers and one thread for the barber which share an object s (class Shared) with
    roomCapacity of value room.
    :return: None
    """
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
