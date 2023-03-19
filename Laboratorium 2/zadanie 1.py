T=[-2,0,4,-3,2,7]
n=len(T)
for i in range(0,n):
    min=i
    for j in range(i+1,n):
        if T[j]<T[min]:
            min=j
    t=T[min]
    T[min]=T[i]
    T[i]=t
print(T)