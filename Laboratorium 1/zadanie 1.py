"""Implementacja  algorytmu wyznaczającego pierwiastki równania kwadratowego"""
import math
a=float(input('podaj współczynnik "a" funkcji kwadratowej'))
b=float(input('podaj współczynnik "b" funkcji kwadratowej'))
c=float(input('podaj wspołczynnik "c"funkcji kwadratowej'))
if a!=0:
    delta=b**2-4*a*c
    if delta>0:
        x1=(-b-math.sqrt(delta))/2*a
        x2=(-b+math.sqrt(delta))/2*a
        print(f"Pierwiastkami równania są: x1={x1}, x2={x2}")
    else:
        if delta==0:
            x1=-b/(2*a)
            print(f"Funkcja ma tylko jeden pierwistek x1={x1}")
        else:
            print("Brak rozwiązań rzeczywistych")
else:
    print("To nie jest równanie kwadratowe")



