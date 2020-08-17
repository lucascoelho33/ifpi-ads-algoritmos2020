# 2. Leia N e escreva todos os números inteiros pares de 1 a N.

def main():

    n = int(input('N: '))
    cont = 1
    alvo = n

    while cont <= alvo:
        if cont % 2 == 0:
            print(cont)

        cont = cont + 1


main()
