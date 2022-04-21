# Homework 8
File **mainsync.py** contains program from **main.py** from branch 07 which has been slightly changed. Now the
program runs until EVERY instance of generator has reached its max number of iterations.

---

File **mainasync** contains program which is an asynchronous implementation of the program in
**mainsync**. Sleep function in generator **task** in **mainsync** has been changed to an awaitable 
sleep using asyncio module. We expect that tasks in asynchronous implementation will finish sooner
than in synchronous.

---

Results:
Sleep functions in **task** in both programs were set to 0.3 seconds.
Both programs were run with same parameters.
Running time is in seconds.

---

Result for **mainsync.py**:
```
task id: 0, times yielded: 1
task id: 1, times yielded: 1
task id: 2, times yielded: 1
task id: 3, times yielded: 1
task id: 4, times yielded: 1
task id: 0, times yielded: 2
task id: 1, times yielded: 2
task id: 2, times yielded: 2
task id: 3, times yielded: 2
task id: 4, times yielded: 2
task id: 0, times yielded: 3
task id: 1, times yielded: 3
task id: 2, times yielded: 3
task id: 3, times yielded: 3
task id: 4, times yielded: 3
task id: 0, times yielded: 4
task id: 1, times yielded: 4
task id: 2, times yielded: 4
task id: 3, times yielded: 4
task id: 3, times yielded: 5

Running time: 6.2107254
```

---

Result for **mainasync**:
```
task id: 0, times called: 1
task id: 2, times called: 1
task id: 4, times called: 1
task id: 1, times called: 1
task id: 3, times called: 1
task id: 0, times called: 2
task id: 4, times called: 2
task id: 3, times called: 2
task id: 2, times called: 2
task id: 1, times called: 2
task id: 0, times called: 3
task id: 3, times called: 3
task id: 1, times called: 3
task id: 4, times called: 3
task id: 2, times called: 3
task id: 0, times called: 4
task id: 1, times called: 4
task id: 3, times called: 4
task id: 2, times called: 4
task id: 3, times called: 5

Running time: 1.5387314
```

---

From the results we can see that asynchronous implementation had much shorter run time, as expected.
This is caused by awaitable function sleep. While one of the tasks wait, the next task can immediately
start running. Unlike in synchronous implementation where the task waits, and after it yields a value, the
next task can start running.

