# 13. Leia N e uma lista de N números e escreva o maior número da lista.

def main():

    n = int(input('N: '))
    maior = 0
    cont = 1

    while cont <= n:
        num = int(input('Digite um número: '))
        if num > maior:
            maior = num
        cont = cont + 1

    print('O maior número é {}'.format(maior))


main()


    
