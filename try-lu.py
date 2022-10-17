import numpy as np
from scipy.linalg import lu

A = np.array([ [2, 7, 5], [14, 50, 36], [2, 8, 8]  ])

print(A)

p, l, u = lu(A)

# print(p, l, u)

print(l)
print(u)
