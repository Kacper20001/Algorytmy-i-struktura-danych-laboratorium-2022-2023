
def NWD(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a
print(NWD(12,18))
print(NWD(28,24))


def NWDrek(a,b):
    if a!=b:
        if a>b:
            return NWDrek(a-b,b)
        else:
            return NWDrek(a,b-a)
    return a

print(NWDrek(12,18))
print(NWDrek(28,24))