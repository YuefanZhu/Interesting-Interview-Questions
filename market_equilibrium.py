#Solve the system of equations 3 * x0 + x1 = 9 and x0 + 2 * x1 = 8:
#>>> a = np.array([[3,1], [1,2]])
#>>> b = np.array([9,8])
#>>> x = np.linalg.solve(a, b)

import numpy as np
def market_equil(prob_matrix):
    a=[[1]*len(prob_matrix)]
    b=[1]+[0]*(len(prob_matrix)-1)
    for i in list(range(0,len(prob_matrix)-1)):
        l=[]
        for j in list(range(0,len(prob_matrix))):
            if(j==i):
                l.append(prob_matrix[j][i]-1)
            else:
                l.append(prob_matrix[j][i])
        a.append(l)
    return np.linalg.solve(np.array(a),np.array(b))

prob_matrix=[[0.8,0.2],[0.1,0.9]]
print([round(float(elem),4) for elem in market_equil(prob_matrix)])