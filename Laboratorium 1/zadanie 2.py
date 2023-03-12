"""Implementacja algorytm wczytywania ciągu n liczb całkowitych (N>0) i wyznaczania ilości liczb
ujemnych w tym ciągu. """


while True:
    n = int(input("Podaj 'n'"))
    if n>0:
        ile_u=0
        i=0
        while i<n:
            ai=int(input("podaj a(i)"))
            if ai<0:
                ile_u+=1
                i+=1
            else:
                i+=1
        else:
            print(f"Ilość liczb ujemnych wynosi {ile_u}")
            break
    else:
        continue




