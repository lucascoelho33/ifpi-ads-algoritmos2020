#4. Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente
#do algarismo da unidade.

def main():

    num = int(input('Digite um número de 2 dígitos: '))

    dezena = num // 10
    unidade = num % 10

    if dezena == unidade:
        print('Os dois dígitos são iguais')
    else:
        print('Os dois dígitos são diferentes')


main()
