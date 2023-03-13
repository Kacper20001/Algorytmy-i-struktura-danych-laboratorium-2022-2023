import numpy as np
T=np.array([[4,2,8,5,1,6,7], [9,6,2,7,1,5,8]])
print(T)
N=len(T)
i=0
while i<N:
    M=len(T[i])
    min_wart=T[i][0]
    min_ind=0
    j=0
    while j<M:
        if T[i][j]<min_wart:
            min_wart=T[i][j]
            min_ind=j
        j+=1
    T[i][0],T[i][min_ind]=T[i][min_ind],T[i][0]
    i+=1
print(T)