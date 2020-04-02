#9. Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.

def main():

    num = int(input('Digite um número entre 0 e 100: '))

    if num % 2 != 0:
        print('Número primo')
    else:
        print('Não é primo')

main()
