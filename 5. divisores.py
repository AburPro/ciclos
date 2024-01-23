num=int(input('ingrese numero: '))
for i in range(1,num+1):
    divisores=num%i
    if divisores==0:
        print(i,end= ' ')