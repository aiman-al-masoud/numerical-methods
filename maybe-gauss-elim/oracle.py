import numpy as np
from scipy.linalg import lu

a = np.array([[2, 7, 5], 
             [14, 50, 36], 
             [2, 8, 8]])

print(a)

p, l, u = lu(a)


print('Permutation Matrix\n\n', p,  '\n'*3, 'Lower Triangular Matrix\n\n', l,'\n'*3, 'Upper Triangular\n\n', u)


# k = 0
# def nome(r):
#     return abs(r[k])
