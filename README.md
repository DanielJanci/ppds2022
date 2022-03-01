# Homework 02
The code in simple_barrier.py contains one class called
SimpleBarrier. This class has one parameter which represents
the number of threads. Class contains variables N where is 
stored the value from parameter, C is a counter with default value of 0,
M is an instance of Mutex and T is an instance of Event. 
Class contains one function called wait.

Function wait() counts threads that finished their task and
waits (creates so-called "barrier") until the number of these 
threads is equal to N. If it is, event sends a signal to 
"release" these threads and "resets" the event, so it can 
be used again.

After executing this code, there will be printed the identificators
of threads before and after the barrier in function wait().

The code in fibonacci01.py contains a class called Adc with variables 
counter with default value of 0 and an instance of Semaphore.
It also contains function called do_the_trick with parameter t_id
which represents id of a thread. This id is compared to the counter
and if the two values are equal, semaphore releases the next thread.
If not the counter is incremented by one and semaphore puts out 
a signal.

This code computes the fibonacci sequence using multiple threads. 
Threads are released in series one by one, only after one element 
of the sequence is calculated. The number of threads is stored in
variable THREADS. The sequence has length of THREADS+2. 