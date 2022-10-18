import numpy as np
from scipy.linalg import lu

a = np.array([[2, 7, 5], 
             [14, 50, 36], 
             [2, 8, 8]])

print(a)

pl, u = lu(a, permute_l=True)


# print(p, l, u)

print(pl)
print(u)
