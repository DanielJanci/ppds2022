from fei.ppds import Thread, Mutex
from collections import Counter


class Shared:
    def __init__(self, size):
        self.counter = 0
        self.end = size
        # due to experiments, 10 is added to size so "out of index"
        # exception is solved temporarily
        self.elms = [0] * (size + 10)


mutex = Mutex()


def do_count(shared):
    mutex.lock()
    while True:
        if shared.counter >= shared.end:
            break
        shared.elms[shared.counter] += 1
        shared.counter += 1
    mutex.unlock()


shared = Shared(1_000_000)

t1 = Thread(do_count, shared)
t2 = Thread(do_count, shared)
t1.join()
t2.join()

counter = Counter(shared.elms)
print(counter.most_common())
