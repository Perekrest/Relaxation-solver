import numpy as np
from Relaxation import Relaxation
a = np.random.randint(-5,high=10,size = [3,3])
A = np.transpose(np.triu(a,0))+np.triu(a,1)
X_exact = [2,3,4]
b = np.matmul(A,X_exact)
omega = 1
eps = 0.0001
x_solution = Relaxation(A,b,omega,eps)
print(x_solution)