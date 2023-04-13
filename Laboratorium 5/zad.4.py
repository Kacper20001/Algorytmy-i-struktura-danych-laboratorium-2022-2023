def funkcja(n,m):
    T = []
    for i in range(n + 1):
        r=[0]*(m + 1)
        T.append(r)
    for i in range(n+1):
        if m>i:
            z=i
        else:
            z=m
        for j in range(z+1):
            if j==0 or j==i:
                T[i][j]=1
            else:
                T[i][j]=T[i-1][j-1]+T[i-1][j]
    return T[n][m]

print(funkcja(6,4))
