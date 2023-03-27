def wynik(i):
    if i<3:
        return 1
    elif i%2==0:
        #licznik = 0
        #licznik +=2
        #print(f"licznik = {licznik}")
        return wynik(i-3)+wynik(i-1)+1
    else:
        #licznik = 0
        #licznik+=1
        #print(f"licznik = {licznik}")
        return wynik(i-1)%7

print(wynik(2))
