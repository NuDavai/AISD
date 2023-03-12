n = int(input("Wczytaj n: "))
if n>0:
    ile_u=0
    i=0
    while i<n:
        a=int(input("Wczytaj element: "))
        if a<0:
            ile_u=ile_u+1
        i=i+1
    print(ile_u)
