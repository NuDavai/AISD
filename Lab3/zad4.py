def decToBin(n):
    wynik = ""
    if n == 0:
        return "0"
    while n>0:
        wynik = str(n % 2) + wynik
        n = n//2
    return wynik
print(decToBin(10))