def main():

    n = int(input('N: '))
    soma = 0
    cont = 1

    while cont <= n:
        soma = soma + 1/cont
        cont = cont + 1

    print('SOMA: %.2f'% soma)


main()
