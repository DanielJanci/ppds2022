"""
Author: Daniel Janci
Async version of mainsync.py
"""
import asyncio
import time


async def task(n, ident):
    for i in range(n):
        await asyncio.sleep(0.3)
        print(f'task id: {ident}, times called: {i + 1}')


def create_tasks(arr):
    tasks = []
    for i in range(len(arr)):
        tasks.append(task(arr[i], i))
    return tasks


async def scheduler(arr):
    tasks = create_tasks(arr)
    await asyncio.gather(*tasks)


def main():
    arr = [4, 4, 4, 5, 3]
    start = time.perf_counter()
    asyncio.run(scheduler(arr))
    print(f'\nRunning time: {time.perf_counter() - start}')


if __name__ == '__main__':
    main()
