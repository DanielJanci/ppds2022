from time import sleep


def task(n, ident):
    for i in range(n):
        sleep(0.3)
        yield f'task id: {ident}, times yielded: {i + 1}'


def create_tasks(arr):
    tasks = []
    for i in range(len(arr)):
        tasks.append(task(arr[i], i))
    return tasks


def scheduler(arr):
    tasks = create_tasks(arr)
    while True:
        try:
            for t in tasks:
                print(next(t))
        except StopIteration:
            break


def main():
    arr = [4, 4, 4, 5, 3]
    scheduler(arr)


if __name__ == '__main__':
    main()
