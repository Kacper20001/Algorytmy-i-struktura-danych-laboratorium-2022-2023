"""Implementacja algorytmu wyszukiwania w tablicy jednowymiarowej minimalnej wartości. """
import numpy as np
T=np.array([1,2,3,5,6,10,20])
N=len(T)
i=0
min=T[0]
while i<N:
    if min>T[i]:
        min=T[i]
        i+=1
    else:
        i+=1
print(min)
