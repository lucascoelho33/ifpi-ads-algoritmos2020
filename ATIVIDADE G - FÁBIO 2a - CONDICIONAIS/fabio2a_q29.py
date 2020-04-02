#29. Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
#formadas pelos seus dois primeiros e dois últimos dígitos.
#Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
#Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.

from math import sqrt

def main():

    num = int(input('Digite um número: '))

    dezena1 = num // 100
    dezena2 = num % 100

    raiz = sqrt(num)
    soma_dezenas = dezena1 + dezena2

    if raiz == soma_dezenas:
        print('O número {} é um quadrado perfeito'.format(num))
    else:
        print('O número {} não é um quadrado perfeito'.format(num))


main()
