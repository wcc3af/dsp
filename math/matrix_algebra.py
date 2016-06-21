# Matrix Algebra

import numpy as np
from numpy import linalg as LA

A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5])[:,None]


#######
# 1. Matrix Dimensions
#######
print A.shape
    # (2,3)
print B.shape
    # (2,2)
print C.shape
    # (3,2)
print D.shape
    # (2,3)
print u.shape
    # (4,) ((really 1,4 but numpy reports vectors as 1-dimensional arrays))
print w.shape
    # (4,1) ((same kind of thing as with u, but I forced this to be a 2-d array for the column))


#######
# 2. Vector operations
#######
a = 6
print u + v
    # [9 7 -4 9]
print u - v
    # [ 3 -3 -2  1]
print a * u
    # [ 36  12 -18  30]
print np.dot(u,v)
    # 51
print LA.norm(u)
    # 8.60232526704


#######
# 3. Matrix Operations
########
# A + C cannot be done because of dimension mismatch...they must have the same dimensionality
print A - C.transpose()
    # [[-4 -7 -3]
    #  [ 3  6  4]]
print C.transpose() + 3*D
    # [[14  3  3]
    #  [ 2  7  9]]
print B*A
    # [[-1 -5 -1]
    #  [ 2  7  4]]
# B*A.transpose() cannot be done because of dimension mis-alignment B=(2,2), A^T=(3x2)


#######
# Optional
#######
# B*C cannot be done because of dimension mis-alignment B=(2,2), C=(3x2)
print C*B
    # [[ 5 -6]
    #  [ 9 -8]
    #  [ 6 -6]]
print B**4
    # [[ 1 -4]
    #  [ 0  1]]
print A*A.transpose()
    # [[14 28]
    #  [28 69]]
print D.transpose() * D
    # [[10 -4  0]
    #  [-4  8  8]
    #  [ 0  8 10]]
