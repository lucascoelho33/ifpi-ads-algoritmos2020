# 6. Escreva a tabuada dos números de 1 a 10.

def main():

    valor = int(input('Tabuada de: '))
    cont = 0

    while cont <= 10:
        prod = cont * valor
        print('{} x {} = {}'.format(cont,valor,prod))
        cont = cont + 1


main()
