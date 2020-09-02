# 16. Leia um número N, calcule e escreva os N primeiros termos
# de seqüência de Fibonacci(0,1,1,2,3,5,8,...). O valor lido para
# N sempre será maior ou igual a 2.

def main():

    n = int(input('N: '))
    a = 0
    b = 1

    if n == 1:
        print('0', end=' ')
    elif n >= 2:
        print('0 1', end=' ')
    for i in range(n-2):
        c = a + b
        a = b
        b = c
        print(c, end=' ')


main()


        
