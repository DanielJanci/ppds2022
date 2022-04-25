# Homework 9
File main.py contains program that uses cuda calculations to create a transposed matrix.


Functions:

---

***my_kernel_2D(i_array, o_array)*** fills out the o_array matrix as a transposed i_array
matrix.

---

***main()*** Creates a matrix with size 8, 4 and fills it with random numbers from 0 to 9. 
Creates another matrix with size 4, 8 and fills it with zeros. Sets up a grid values, calls 
the function "my_kernel_2D" with the grid values and the two matrices. Lastly prints the 
first (original) matrix and the second (transposed) one.

---

Output:
```
Input matrix:
[[2 5 7 2]
 [5 4 0 8]
 [0 7 8 0]
 [8 8 5 9]
 [9 0 7 8]
 [7 8 8 7]
 [8 3 0 9]
 [7 2 4 5]]

Transposed matrix:
[[2 5 0 8 9 7 8 7]
 [5 4 7 8 0 8 3 2]
 [7 0 8 5 7 8 0 4]
 [2 8 0 9 8 7 9 5]]
```