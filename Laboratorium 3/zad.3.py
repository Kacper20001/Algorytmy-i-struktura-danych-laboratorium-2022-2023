def funkcja(n):
    if n==1:
        return 4
    elif n>1:
        return 1/(1-funkcja(n-1))

print(funkcja(8))
print(funkcja(9))
print(funkcja(10))
print(funkcja(100))