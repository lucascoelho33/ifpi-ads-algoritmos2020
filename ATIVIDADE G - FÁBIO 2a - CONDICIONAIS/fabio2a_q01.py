#1. Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.

def main():

    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    num3 = int(input('Terceiro número: '))

    if num1 == num2 == num3:
        print('Todos os números são iguais')
    elif num1 == num2 and num1 != num3 and num2 != num3:
        print('O primeiro e o segundo número são iguais')
    elif num1 != num2 and num1 == num3 and num2 != num3:
        print('O primeiro e o terceiro número são iguais')
    elif num1 != num2 and num1 != num3 and num2 == num3:
        print('O segundo e o terceiro número sõa iguais')
    else:
        print('Todos os números são diferentes')


main()
