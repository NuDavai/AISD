# 1. n - liczba elementow na liscie, n>0
# 2. losujemy przedzial (x,y), elementy podaje uzytkownik
# 3. nalezy wyswietlic liste wylosowana i posortowana
# 4. uzytkownik podaje liczbe szukana x
# 5. jesli program znajdzie liczbe to wyswietlic komunikat i jej pozycje, jesli nie, to tylko komunikat

def quicksort(l, r, list):
    if l >= r:
        return

    v = list[r]
    p = l

    for j in range(l, r):
        if list[j] < v:
            list[p], list[j] = list[j], list[p]
            p += 1

    list[p], list[r] = list[r], list[p]

    quicksort(l, p - 1, list)
    quicksort(p + 1, r, list)
    return list

def binarySearch(lista,l,r,szukana):
    l=0
    r=n-1
    srodek=(l+r)//2
    while l<=r:
        srodek=(l+r)//2
        if lista[srodek] == szukana:
            return srodek
        elif lista[srodek] > szukana:
            r=srodek-1
        else:
            l=srodek+1
    return -1

import random
tab = []
n = int(input("Podaj n uzytkowniku: "))
if n > 0:
    print("Podaj przedzialy liczbowe uzytkowniku")
    x = int(input("x: "))
    y = int(input("y: "))
    if y>=x:
        for i in range(n):
            a = random.randint(x,y)
            tab.append(a)
        # zabezpieczenie przed losowaniem duplikatow
        licznikDuplikatow = 0
        for i in range(n):
            for j in range(i+1, n):
                if tab[i] == tab[j]:
                    licznikDuplikatow = licznikDuplikatow + 1
        if licznikDuplikatow > 0:
            while True:
                tab.clear()
                licznikDuplikatow=0
                for i in range(n):
                    a = random.randint(x, y)
                    tab.append(a)
                for i in range(n):
                    for j in range(i + 1, n):
                        if tab[i] == tab[j]:
                            licznikDuplikatow = licznikDuplikatow + 1
                if licznikDuplikatow == 0:
                    break
        #
        print("Tablica wylosowana: ", tab)
    quicksort(0,n-1,tab)
    print("posortwoana lista: ", tab)
    z=int(input("Podaj liczbe szukaną: "))
    print("Szukana liczba znajduje sie pod indeksem: ", binarySearch(tab,0,n-1,z))
else:
    print("Podales n<0 uzytkowniku")