# 7. Leia um número N, some todos os números inteiros
# entre 1 e N e escreva o resultado obtido.

def main():

    n = int(input('N: '))
    cont = 2
    soma = 0

    while cont < n:
        soma = soma + cont
        cont = cont + 1
    print('SOMA = {}'.format(soma))


main()
