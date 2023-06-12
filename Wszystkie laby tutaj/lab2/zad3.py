tabX = []
tabY = []
n = int(input("Podaj rozmiar tablicy: "))
for i in range(n):
    x = int(input("Podaj element tablicy: "))
    tabX.append(x)
    for j in range(size(x)):
        y = x//(size(x)-j)*10
        tabY.append(y)
#...