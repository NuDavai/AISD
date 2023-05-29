class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {} #lista sąsiedztwa z wagami
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    def getConnections(self):
        return self.connectedTo.keys()
    def getId(self):
        return self.id
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self,n):
        return n in self.vertList
    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())

print("Budowa grafu")
print("Zacznijmy budowę grafu od wybrania rodzaju grafu")
print("Rodzaje: skierowany, nieskierowany, ważony, inny możliwy")
rodzaj = input("Podaj rodzaj twojego grafu: ")
print("Kolejnym krokiem będzie podanie liczby wierzchołków w grafie")
n = int(input("Podaj liczbę wierzchołków w twoim grafie: "))

g = Graph()
for i in range(n):
    g.addVertex(i)
    g.vertList


print("Ostatnim krokiem w budowie grafu będzie podanie liczby krawędzi między wierzchołkami")
if rodzaj == 'ważony':
    print("Podaj, w odpowiedniej kolejności: początek krawędzi (jako numer wierchołka), koniec krawędzi (numer wierzchołka, waga")
    while True:
        x = int(input("Początek krawędzi: "))
        y = int(input("Koniec krawędzi: "))
        z = int(input("Waga: "))
        g.addEdge(x, y, z)
        flaga = input("Czy wprowadzamy kolejną krawędź (y/n)? ")
        if flaga == 'n':
            break

else:
    print("Podaj, w odpowiedniej kolejności: początek krawędzi (jako numer wierchołka) i koniec krawędzi (numer wierzchołka)")
    while True:
        x = int(input("Początek krawędzi: "))
        y = int(input("Koniec krawędzi: "))
        g.addEdge(x, y, 0)
        flaga = input("Czy wprowadzamy kolejną krawędź (y/n)? ")
        if flaga == 'n':
            break

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

## Macierz sąsiedztwa
#zerowanie macierzy
macierzS = [[0] * n for i in range(n)]
for row in macierzS:
    print(' '.join([str(elem) for elem in row]))

#Przypisywanie wartości macierzy sąsiedztwa
#for i in range(n):
# for j in lista wierzchołków, które sąsiadują z wierzchołkiem i
#   macierzS[i][j]=1


## Lista sąsiedztwa
listaS = []
#for i in range(n):
#   macierzS[i].append(lista wierzchołków, które sąsiadują z wierzchołkiem i)

## Reprezentacja grafu
# biblioteka planarity nie chce się zainstalować na przez Python Packages, instalacja przez terminal również nie wchodzi