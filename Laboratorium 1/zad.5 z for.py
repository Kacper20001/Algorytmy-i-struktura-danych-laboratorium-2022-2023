import numpy as np
T=np.array([[4,2,8,5,1,6,7], [9,6,2,7,1,5,8]])
N=len(T)
for i in range(N):
    M=len(T[i])
    min_wart=T[i][0]
    min_ind=0
    for j in range(M):
        if T[i][j]<min_wart:
            min_wart=T[i][j]
            min_ind=j
    T[i][0],T[i][min_ind]=T[i][min_ind],T[i][0]
print(T)