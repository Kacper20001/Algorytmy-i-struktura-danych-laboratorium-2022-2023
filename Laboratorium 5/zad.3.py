def S(n):
    T=[0]*(n+1)
    T[0]=1
    T[1]=1
    for i in range(2,n+1):
        T[i]=2*T[i-1]-T[i-2]
    return T[n]

print(S(5))