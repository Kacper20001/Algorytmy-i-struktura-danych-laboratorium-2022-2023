def funkcja(A,p=0,k=None):
    if k is None:
        k=len(A)-1
    if p==k:
        return A[p]
    else:
        s=(p+k)//2
        max_l=funkcja(A,p,s)
        max_r=funkcja(A,s+1,k)
        if max_l>max_r:
            return max_l
        else:
            return max_r

print(funkcja([5,9,2,8,3]))