"""
Author: Daniel Janci
Async version of mainsync.py
"""
import asyncio
import time


async def task(n, ident):
    """
    Waits for 0.3 seconds and then prints this tasks' id and hom many times it has been called.
    :param n: number of iterations
    :param ident: identificator of task
    :return: None
    """
    for i in range(n):
        await asyncio.sleep(0.3)
        print(f'task id: {ident}, times called: {i + 1}')


def create_tasks(arr):
    """
    Creates instance of function task for each integer in list.
    :param arr: list of integers
    :return: list of tasks
    """
    tasks = []
    for i in range(len(arr)):
        tasks.append(task(arr[i], i))
    return tasks


async def scheduler(arr):
    """
    Creates tasks from list. Runs multiple tasks using asyncio.gather.
    :param arr: list of integers
    :return: None
    """
    tasks = create_tasks(arr)
    await asyncio.gather(*tasks)


def main():
    """
    Creates an list of itegers and calls asyncio.run on function "scheduler" with that list as a parameter.
    :return:
    """
    arr = [4, 4, 4, 5, 3]
    start = time.perf_counter()
    asyncio.run(scheduler(arr))
    print(f'\nRunning time: {time.perf_counter() - start}')


if __name__ == '__main__':
    main()
