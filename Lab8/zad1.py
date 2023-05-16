class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext

temp=Node(93)
print(temp.getData())
print(temp.getNext())

class Unorderedlist:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head == None
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found  = True
            else:
                current = current.getNext()

        return found
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found  = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

mylist = Unorderedlist()
mylist.add(31)
mylist.add(12)
mylist.add(325)
mylist.add(123)
mylist.add(3121)
mylist.add(21)

print(mylist.size())
print(mylist.search(0))
print(mylist.search(123))

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
        print("Tablica wylosowana: ", tab)
    quicksort(0,n-1,tab)
    print("posortwoana lista: ", tab)
    z=int(input("Podaj liczbe szukaną: "))
    print("Szukana liczba znajduje sie pod indeksem: ", binarySearch(tab,0,n-1,z))
else:
    print("Podales n<0 uzytkowniku")

# przerobic to na funkcje, zrobic schemat, zabezbieczyc zeby podczas losowania nie bylo duplikatow (usuwanie duplikwatow jezeli sie jakies wylosowaly)