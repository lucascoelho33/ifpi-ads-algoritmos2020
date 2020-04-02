#5. Leia um número inteiro (3 dígitos),
#calcule e escreva a soma de seus elementos (C + D +  U).


def main():

    num = int(input('Digite um número inteiro de tres dígitos: '))


    C = num // 100
    D = (num % 100) // 10
    U = num % 10
    soma = C + D + U


    print('A soma dos elementos foi ', soma)


main()
