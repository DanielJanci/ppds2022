# Homework 01
The code consists of class called Shared which 
contains a counter with default value of 0, size 
which is passed as a parameter and an array with 
elements of value 0 and the size from parameter. It 
also contains a do_count function with parameter 
of type Shared. The function increments an element 
of an array in Shared by one and then increments an
index of that array by one. 

The code is run parallelly with two threads which 
share the same index. At the end, the amounts of
different elements in the array are printed. 

If we run this code without using lock, the values of
the array in the Shared object are incremented 
differently. For example after running this code
without lock with 1 000 000 as parameter, 
we get the following output:
[(1, 891853), (2, 108144), (0, 13)]. It tells us that
in the array, 891853 elements had been incremented 
by one, 108144 elements had been incremented by 2 and 
13 elements haven't been incremented at all.

Experiments were run in Python 3.8.


The code in main01.py contains first implementation of
Mutex.lock() function. Lock is put inside the funtion
do_count right before incrementing value of an element.
And unlock is put right after the incrementation. This
causes that when incrementing the value, only one thread
has access to the index of the array. Thus the value 
is incremented only once. The following output is after 
this implementation of the lock: [(1, 1000001), (0, 9)].
We can see that 1 000 000 values have been incremented correctly.
The last 10 values come from updating the size value
in class Shared for avoiding an out of index exception.


The code in main02.py contains second implementation of
Mutex.lock() function. Lock is put before the while
loop inside the do_count function and unlock after 
the while loop. This defeats the purpose of parallel 
programming since only one thread has
access to the index of the array during the whole 
while loop, and it's not distributed parallelly, but
it is an example of how lock can work. As expected, 
the following output of this implementation is correct: 
[(1, 1000000), (0, 10)]. Again, 1 000 000 of the values
have been incremented correctly and the last 10 values
are explained in the first implementation.

