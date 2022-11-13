#!/bin/python3
# ./main.py  > dump.txt
import numpy as np
from numpy import array
from typing import Tuple
from numpy.linalg import norm


# with jacobi method
def split_matrix(a:np.ndarray)->Tuple[np.ndarray, np.ndarray]:

    m = np.zeros(a.shape)
    np.fill_diagonal(m, a.diagonal())
    n = m - a
    return m, n

def test1(xk:np.ndarray, xk1:np.ndarray, tau:float)->bool:
    val = norm(xk1 - xk) / norm(xk)  # change from previous iteration
    print('test1', val)
    return val <= tau

def test2(xk:np.ndarray, b:np.ndarray, a:np.ndarray, tau:float)->bool:
    val = norm(b - a.dot(xk)) / norm(b) # difference from real solution
    print('test2', val)
    return val <= tau

def solve(a:np.ndarray, b:np.ndarray, x:np.ndarray, tau:float):

    m,n = split_matrix(a)

    while True:

        print('x(k):')
        print(x)
        print('a matrix:')
        print(a)
        print('b vector:')
        print(b)
        print('m matrix:')
        print(m)
        print('n matrix:')
        print(n)
        xKplusOne = (b - n.dot(x)) / m.diagonal() # with Jacobi
        print('x(k+1):')
        print(xKplusOne)

        if test1(x, xKplusOne, tau) and test2(xKplusOne, b, a, tau):
            break
        else:
            x = xKplusOne
        
        print('-'*10)


a = np.array([[4, 2, 0],
              [0, 2, 1],
              [1, 1, 4]])

# a = np.array([[3, -2, 1],
#               [1, -3, 2],
#               [-1, 2, 4]])

b = np.array([0, 2, 0])
x0 = np.array([0,0,0])
tau = 10**-3

solve(a, b, x0, tau)