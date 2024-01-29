def entero ():
    num=int(input('n: '))
    while num!=1:
        print(num,end=' ')
        if num%2==0:
            num=int(num/2)
        else:
            num=(num*3)+1
    print(1)
entero()
def graf ():
    num=int(input('n: '))
    for i in range(1,num+1):
        n=i
        iterar=1
        while n!=1:
            if n%2==0:
                n=int(n/2)
            else:
                n=(n*3)+1
            iterar+=1
        print(f'{i} {iterar*"*"}')
graf()