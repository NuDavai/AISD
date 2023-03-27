def Hanoi(n, A, B, C):
    if n>0:
        Hanoi(n-1, A, B, C)
        print("Przenosimy krążek", n, "drążek", A, "na drążek", C)
        Hanoi(n-1, B, A, C)
print("Wieża Hanoi")
print(Hanoi(3,'początkowy','roboczy','docelowy'))
