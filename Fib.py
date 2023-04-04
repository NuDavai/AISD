print("Obliczanie sumy ciągu Fibonacciego")
def Fib(n):
    if n==0: return 0
    if n==1: return 1
    else: return(Fib(n-1)+Fib(n-2))
n = int(input("Podaj n dla ciągu Fibonacciego: "))
print(Fib(n))

print("Obliczanie elementów tablicy ciągu Fibonacciego")
fibTab = []
n = int(input("Podaj rozmiar ciągu Fibonacciego: "))
for i in range(n):
    if i == 0:
        fibTab.append(i)
    elif i == 1:
        fibTab.append(i)
    else:
        fibTab.append(fibTab[i-1]+fibTab[i-2])
print(fibTab)