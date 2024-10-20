import numpy as np
def Relaxation(A,b,omega,eps):
    x_0 = np.ones(len(b))
    eps1 = 1
    x_solution = np.ones(len(b))

    while eps1 > eps:
        for i in range(len(b)):
            sum1 = 0
            for j in range(i):
                sum1 = sum1 + A[i][j]*x_solution[j]
            sum2 = 0
            for j in range(i+1,len(b)):
                sum2 = sum2 +  A[i][j]*x_0[j]
            x_solution[i] = (1-omega)*x_0[i]+omega*(b[i]-sum1-sum2)/A[i][i]
        eps1 = np.linalg.norm(x_solution-x_0,ord = np.inf)
        x_0 = np.copy(x_solution)

    return(x_solution)

  






