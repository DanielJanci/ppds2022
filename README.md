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