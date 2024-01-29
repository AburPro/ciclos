import math
list=[]
x=0
e1=0
e2=0
d=0
n1=0
n2=0
while d>0.0001 or d==0:
    e1=e2
    n1=n2
    e2=1/math.factorial(x)
    list.append(e2)
    x+=1
    n2=sum(list)-e1
    d=abs(n2-n1)
print(n2)