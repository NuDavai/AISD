n = int(input("Podaj n: "))
P = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i > 0 and j == 0:
            P[i][j]=0
        elif i == 0 and j>0:
            P[i][j]=1
        elif i > 0 and j > 0:
            P[i][j]=(P[i-1][j] + P[i][j-1])/2

for row in P:
    print('   '.join([str(elem) for elem in row]))