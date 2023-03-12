"""Implementacja algorytmu, który sprawdza czy podana przez użytkownika wartość
występuje w tablicy jednowymiarowej."""
import numpy as np
T=np.array([1,2,3,5,6,10,20])
n=len(T)
x=float(input("podaj x"))
i=0
while i<n:
    if T[i]==x:
        print("Podana wartość występuje w tablicy")
        break
    else:
        i+=1
else:
    print("Podana wartość nie występuje w tablicy")
