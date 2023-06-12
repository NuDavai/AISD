print("Podaj ciąg znaków zakończony '*', a ja ci powiem ile razy wystąpiła litera 'c'")
suma=0
while True:
    znak=input("Podaj znak: ")
    if znak=='*':
        break
    if znak=='c':
        suma=suma+1
print(suma)