def funkcja(n):
    if n==0:
        return '0'
    elif n==1:
        return '1'
    else:
        return funkcja(n//2)+str(n%2)

print(funkcja(10))