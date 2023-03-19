A=[-2,0,4,-3,2,7]
n=len(A)
for i in range(1,n-1):
    element=A[i]
    j=i-1
    while j>=0 and A[j]>element:
        A[j+1],A[j]=A[j],A[j+1]
        j=j-1
print(A)

