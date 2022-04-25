"""
Author: Daniel Janci
This program creates a random matrix and transposes this matrix using cuda calculations.
"""
from numba import cuda
import numpy as np
import math


@cuda.jit
def my_kernel_2D(i_array, o_array):
    """
    Fills out the output array as a transposed input array.
    :param i_array: input array
    :param o_array: output array
    :return: None
    """
    x, y = cuda.grid(2)
    o_array[y][x] = i_array[x][y]


def main():
    """
    Creates a matrix with size 8, 4 and fills it with random numbers from 0 to 9. Creates another matrix with size 4, 8
    and fills it with zeros. Sets up a grid values, calls the function "my_kernel_2D" with these values and the two
    matrices. Lastly prints the first (original) matrix and the second (transposed) one.
    :return: None
    """
    x_dim, y_dim = 8, 4
    i_array = np.random.randint(0, 10, size=(x_dim, y_dim), dtype=int)
    o_array = np.zeros((y_dim, x_dim), dtype=int)

    threads_per_block = (4, 2)
    blocks_per_grid_x = math.ceil(i_array.shape[0] / threads_per_block[0])
    blocks_per_grid_y = math.ceil(i_array.shape[1] / threads_per_block[1])
    blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)

    my_kernel_2D[blocks_per_grid, threads_per_block](i_array, o_array)

    print('Input matrix:')
    print(i_array)
    print('\nTransposed matrix:')
    print(o_array)


if __name__ == '__main__':
    main()
