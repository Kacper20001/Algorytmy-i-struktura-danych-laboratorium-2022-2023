def funkcja (n,a,b,c):
    if n==1:
        print(f" z patyka {a} na patyk {b} przełóż {n}")
    else:
        funkcja(n-1,a,c,b)
        print(f"z patyka {a} na patyk {b} przełóż {n}")
        funkcja(n-1,c,b,a)
print(funkcja(5,"A","B","C"))