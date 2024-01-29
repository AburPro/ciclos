num=int(input('n: '))
a=[]
for i in range(num):
    x=((-1)**i)/((2*i)+1)
    a.append(x)
suma=sum(a)*4
print(suma)