def silnia(n):
    if n==0:
        return 1
    else:
        return n*silnia(n-1)
print(silnia(5))

def nwdIter(a,b):
    if a>0 and b>0:
        if a!=b:
            if a>b:
                a=a-b
            else:
                b=b-a
        else:
            return a
    else:
        return("a i b nie są większe od zera!")
print(nwdIter(18,12))

def nwdRek(a,b):
    if a!=b:
        if a>b: return nwdRek(a-b,b)
        else: return nwdRek(a,b-a)
    return a
print(nwdRek(18,12))

def nwdInterII(a,b):
    while b!=0:
        temp = b
        b=a%b
        a = temp
    return a
print(nwdInterII(18,12))

def nwdRekII(a,b):
    if b!=0:
        return nwdRekII(b,a%b)
    return a
print(nwdRekII(18,12))

