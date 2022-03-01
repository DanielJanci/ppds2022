from fei.ppds import Thread, Semaphore
from random import randint
from time import sleep


class Adt:
    """This class contains variables: counter with default value of 0 and S which is an instance of a Semaphore

    """
    def __init__(self):
        self.counter = 0
        self.S = Semaphore()

    def do_the_trick(self, t_id):
        """Parameter t_id  is compared to the counter and if the two values are equal, semaphore releases the next
        thread. If not the counter is incremented by one and semaphore puts out a signal.
        :param t_id: identificator of a thread
        :return: None
        """
        while True:
            if t_id == self.counter:
                self.S.wait()
                break
        self.counter += 1
        self.S.signal()


def compute_fibonacci(a, i):
    """Computes the fibonacci sequence of length THREADS+2 with THREADS number of threads.

    :param a: instance of Ads
    :param i: indentificator of a thread
    :return:
    """
    sleep(randint(1, 10) / 10)
    a.do_the_trick(i)
    fib_seq[i + 2] = fib_seq[i] + fib_seq[i + 1]


THREADS = 20

fib_seq = [0] * (THREADS + 2)
fib_seq[1] = 1

adt = Adt()
threads = [Thread(compute_fibonacci, adt, i) for i in range(THREADS)]
[t.join() for t in threads]

print(fib_seq)
