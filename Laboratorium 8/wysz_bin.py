# wyszukiwanie binarne z sortowaniem listy za pomocą insert sort
def wysz_bin(lista, x, p=0, k=None):
    if k is None:
        k = len(lista)
    for i in range(1, len(lista)):
        element = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > element:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = element
    print(lista)
    s = len(lista) // 2
    if len(lista) == 0:
        return None
    else:
        if x == lista[s]:
            return s
        elif x > lista[s]:
            return wysz_bin(lista,x, s + 1, k)
        else:
            return wysz_bin(lista,x, p, s - 1,)

lista = [-2, 0, 4, -3, 2, 7]
print(wysz_bin(lista, 2))



