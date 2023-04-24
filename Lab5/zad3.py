def SumaC(n):
    if n==0: return 1
    if n==1: return 1
    if n>1:
        return 2*SumaC(n-1)-SumaC(n-2)

x=SumaC(2)
print(x)