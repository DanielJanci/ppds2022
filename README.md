# Homework 01
The code consists of class called Shared which 
contains a counter with default value of 0, size 
which is passed as a parameter and an array with 
elements of value 0 and the size from parameter. It 
also contains a do_count function with parameter 
of type Shared. The function increments an element 
of an array in Shared by one and then increments a
index of that array by one. 

The code is run paralelly with two threads which 
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





