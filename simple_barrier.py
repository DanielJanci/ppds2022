from fei.ppds import Thread, Mutex, Event, print


class SimpleBarrier:
    def __init__(self, N):
        self.N = N
        self.C = 0
        self.M = Mutex()
        self.T = Event()

    def wait(self):
        self.M.lock()
        self.C += 1
        if self.C == self.N:
            self.C = 0
            self.T.signal()
        self.M.unlock()
        self.T.wait()
        self.T.clear()


def before_barrier(thread_id):
    print(f"before barrier {thread_id}")


def after_barrier(thread_id):
    print(f"after barrier {thread_id}")


def barrier_cycle(b1, b2, thread_id):
    while True:
        before_barrier(thread_id)
        b1.wait()
        after_barrier(thread_id)
        b2.wait()


THREADS = 5
sb1 = SimpleBarrier(THREADS)
sb2 = SimpleBarrier(THREADS)

threads = [Thread(barrier_cycle, sb1, sb2, i) for i in range(THREADS)]
[t.join() for t in threads]
