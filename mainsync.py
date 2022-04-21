"""
Author: Daniel Janci
Program creates and runs multiple generators until every yields for the last time.
"""
import time
from time import sleep


def task(n, ident):
    """
    A generator that yields string n times. String contains of generators id and the number of how many time it yielded.
    :param n: number of iterations
    :param ident: identificator of generator
    :return: yields a string
    """
    for i in range(n):
        sleep(0.3)
        yield f'task id: {ident}, times yielded: {i + 1}'


def create_tasks(arr):
    """
    Creates generators from list arr. For each element in arr a instance of "task" is created. The element is a number
    of iterations in the generator and the index of that element is an identificator of the generator.
    :param arr: list of integers
    :return: list of generators
    """
    tasks = []
    for i in range(len(arr)):
        tasks.append(task(arr[i], i))
    return tasks


def scheduler(arr):
    """
    Creates generators. Function calls next function for each generator and prints the yielded value. Functions runs
    until every generator has reached limit of it's iterations.
    :param arr: list of integers
    :return: None
    """
    tasks = create_tasks(arr)
    while True:
        for t in tasks:
            try:
                print(next(t))
            except StopIteration:
                tasks.remove(t)
        if len(tasks) == 0:
            break


def main():
    """
    Creates an list of itegers and calls function "scheduler" with that list as a parameter.
    :return: None
    """
    arr = [4, 4, 4, 5, 3]
    start = time.perf_counter()
    scheduler(arr)
    print(f'\nRunning time: {time.perf_counter() - start}')


if __name__ == '__main__':
    main()
