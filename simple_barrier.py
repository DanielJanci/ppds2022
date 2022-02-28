from fei.ppds import Thread, Mutex, Event, print


class SimpleBarrier:
    """This class contains variables N which represents the number of threads, C is a counter with default value of 0,
    M is a instance of Mutex and T is an instance of Event. Class contains one function called wait.
    :parameter N: the number of threads

    """
    def __init__(self, N):
        self.N = N
        self.C = 0
        self.M = Mutex()
        self.T = Event()

    def wait(self):
        """Counts how many threads finished their task and Event.wait() "holds" them. If the count is N an
        Event.Signal() a signal to "release" the threads. Lastly, clear() "resets" the Event() for further usage.
        :return: None
        """
        self.M.lock()
        self.C += 1
        if self.C == self.N:
            self.C = 0
            self.T.signal()
        self.M.unlock()
        self.T.wait()
        self.T.clear()


def before_barrier(thread_id):
    """Prints identificators of threads that are being "held" before an event sends a signal.

    :param thread_id: indentificator of thread
    :return: None
    """
    print(f"before barrier {thread_id}")


def after_barrier(thread_id):
    """Prints identificators of threads that are being "released" after an event sends a signal.

    :param thread_id: indentificator of thread
    :return: None
    """
    print(f"after barrier {thread_id}")


def barrier_cycle(b1, b2, thread_id):
    """Prints identificators of threads that are before and after barrier in a never-ending cycle.

    :param b1: instance of SimpleBarrier
    :param b2: instance of SimpleBarrier
    :param thread_id: indentificator of thread
    :return: None
    """
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
