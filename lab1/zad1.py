import math
def funk(a,b,c):
    if a!=0:
        delta=b*b-4*a*c
        if delta>0:
            x1=(-b-math.sqrt(delta))/2*a
            x2=(-b+math.sqrt(delta))/2*a
            return(x1,x2)
        elif delta==0:
            x1=-b/(2*a)
            return(x1)
        else:
            return("Brak rozwiązań rzeczywistych")
    else:
        return("To nie jest równanie kwadratowe")

print(funk(1,2,-3)) #test