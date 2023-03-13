tab = []
n = int(input("Podaj wielkość tablicy: "))
for i in range(n):
    x=int(input("Wczytaj element tablicy: "))
    tab.append(x)
mini = tab[0]
for i in range(1,n):
    if tab[i]<mini:
        mini=tab[i]
print("Minimalny element tablicy wynosi: ", mini)