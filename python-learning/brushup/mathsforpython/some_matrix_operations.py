import sys
import numpy as np

print(f"Python version : {sys.version}")
print(f"NumPy version is {np.__version__}")

# Now let's do some matrix operations
A = np.matrix([[1, 2], [3, 4]])
B = np.ones((2, 2), dtype=int)
print(f"Matrix A = \n {A}")
print(f"Matrix B is = \n{B}")

# Now let's do an element wise sum A + B = C
C = A + B
print(f"sum of A + B = C \n{C}")

# Let's do element wise subtraction
C = A - B
print(f"Subtraction A - B = C \n {C}")

# Let's do multiplication as well
C = A * B
print(f"the multiplication of A * B = C \n {C}")

# Matrix transpose
A = np.array(range(9))
print(f"A = \n {A}")
A = A.reshape(3, 3)
print(f"After reshape A = \n {A}")
# transpose
A = A.T
print(f"Transpose of matrix A is = \n {A}")
# Create a transpose
A = np.ones((3,3,3,3,3,3,3,3,3,3))
print(A.shape)
print(len(A.shape))
print(A.size)
