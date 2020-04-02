#2. Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.

def main():

    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo número: '))

    if num1 > num2:
        print('O primeiro número é o maior')
    elif num1 < num2:
        print('O segundo número é o maior')
    else:
        print('Os números são iguais')


main()
