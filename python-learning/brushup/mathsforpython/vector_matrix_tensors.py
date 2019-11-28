import sys
import numpy as np

print(f"Python: {sys.version}")
print(f"NumPy: {np.__version__}")

# defining a scalar
x = 6
print(f"scalar x: {x}")

# defining a vector
y = np.array((1, 2, 3))
print(f"vector y: {y}")
print(f"vector dimension is: {y.shape} and vector size is : {y.size}")
# vector dimension is: (3,)--> this is read as Length and vector size is : 3

# defining a matrix
m = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"the 3X3 matrix is: {m}")
print(m)
print(f"Matrix dimension {m.shape} and matrix size is {m.size}")

# define a matrix of a given dimension
matrix = np.ones((3, 3))
print(matrix)

print(f"Matrix dimension is {matrix.shape} and matrix size is {matrix.size}")
# create a 3 dimensional tensor
_tensor = np.ones((3, 3, 3,))
print(_tensor)
print(f"Tensor dimension: {_tensor.shape} and the size of the tensor is {_tensor.size}")

# Indexing
A = np.ones((5, 5), dtype=np.int)
print(A)
# Indexing starts at 0
A[0, 1] = 2
print(f"adding 2 at 0,1 index \n {A}")

# for higher dimensions let's add an index
A = np.ones((5, 5, 5,), dtype=int)
print(f"The tensor is \n {A}")
# assigning the first row a new value

A[:, 0, 0] = 6
print(f"adding 6 at 0,0,0 index of every column, now the tesnor  is \n {A}")
