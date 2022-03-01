from fei.ppds import Thread, Semaphore
from random import randint
from time import sleep


class Adt:
    def __init__(self):
        self.counter = 0
        self.S = Semaphore()

    def do_the_trick(self, t_id):
        while True:
            if t_id == self.counter:
                self.S.wait()
                break
        self.counter += 1
        self.S.signal()


def compute_fibonacci(a, i):
    sleep(randint(1, 10) / 10)
    a.do_the_trick(i)
    fib_seq[i + 2] = fib_seq[i] + fib_seq[i + 1]


THREADS = 10

fib_seq = [0] * (THREADS + 2)
fib_seq[1] = 1

adt = Adt()
threads = [Thread(compute_fibonacci, adt, i) for i in range(THREADS)]
[t.join() for t in threads]

print(fib_seq)
