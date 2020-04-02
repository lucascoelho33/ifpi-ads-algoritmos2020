#3. Leia 3 (três) números, verifique e escreva o maior entre os números lidos.

def main():

    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))
    num3 = int(input('Terceiro número: '))

    if num1 > num2 and num1 > num3:
        print('O primeiro número é maior')
    elif num2 > num1 and num2 > num3:
        print('O segundo número é maior')
    elif num3 > num1 and num3 > num2:
        print('O terceiro número é maior')
    else:
        print('Os números são iguais')


main()
