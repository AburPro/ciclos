p=1
d=1
a=0
print('Potencia     Fraccion      Suma')
while d>0.000001:
    d=1/2**p
    a+=d
    print(f'{str(p).center(10)}  {str(round(d,4)).center(10)}  {str(round(a,4)).center(10)}')
    p+=1