print("Algorytm Eulidesa Iteracyjnie")
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
if a > 0 and b > 0:
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    else:
        print(a)
else:
    print("Zostały podane nie właściwe wartości")
    a = int(input("Podaj a: "))
    b = int(input("Podaj b: "))

def NWDrek(a,b):
    if a!=b:
        if a>b: return NWDrek(a-b,b)
        else: return NWDrek(a,b-a)
    return a
print("Algorytm Eulidesa rekurencyjnie")
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
print(NWDrek(a,b))