n = int(input("Podaj n: "))
S = []
for i in range(n):
    for j in range(n):
        if n == 0:
            S.append(1)
        elif n == 1:
            S.append(1)
        elif n > 1:
            S.append(2*S[i-1] - S[i-2])
print(S)