print("Podaj dwie liczby, ktore beda przedzialem liczbowym sposrod ktorego wypisze wszystkie liczby podziene przez 3")
x=int(input("Podaj x: "))
y=int(input("Podaj y: "))
while x<=y:
    if x%3==0:
        print(x)
    x=x+1
