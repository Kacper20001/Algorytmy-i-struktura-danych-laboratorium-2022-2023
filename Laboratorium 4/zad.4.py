def funkcja(A):
    k=len(A)
    if k==0:
        return 0
    if k==1:
        return A[0]
    s=k//2
    l=A[:s]
    r=A[s:]
    suma_l=funkcja(l)
    suma_p=funkcja(r)
    return suma_l+suma_p

print(funkcja([4, 8, 2, 1, 5, 9, 6, 7]))