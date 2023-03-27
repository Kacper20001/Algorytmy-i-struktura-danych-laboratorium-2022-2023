
def NWDII(a,b):
    while b!=0:
        temp = b
        b = a % b
        a = temp
    return a


def NWDIIrek(a,b):
    if b!=0:
        return NWDIIrek(b,a % b)
    return a


print(NWDIIrek(12,18))
print(NWDIIrek(28,24))
