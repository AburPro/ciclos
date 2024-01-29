while True:
    h=int(input('Altura: '))
    b=int(input('Ancho: '))
    if h !=0:
        for i in range (1,h+1):
            print('*'*b)
    break
while True:
    h=int(input('Altura: '))
    if h !=0:
        for i in range (1,h+1):
            print('*'*i)
    break
while True:
    h=int(input('Lado: '))
    if h !=0:
        for i in range (h):
            ast='*'
            esp=' '
            print(f'{esp*(h-i)}', end=f'{ast*(h+(i*2))}\n')
            k=h+(i*2)
        for j in range(1,h):
            print(f'{esp*(j+1)}', end=f'{ast*(k-(j*2))}\n')
            # print(('*'*(k-(j*2))))
    break
