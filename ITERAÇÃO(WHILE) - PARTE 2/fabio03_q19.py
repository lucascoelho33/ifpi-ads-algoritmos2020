def main():

    n = int(input('N: '))
    cont = 1
    soma = 0

    while cont <= n:
        if cont % 2 != 0:
            soma = soma + (1/n)
        else:
            soma = soma - (1/n)

        n = n-1
        cont = cont + 1

    print('SOMA: %.2f'% soma)


main()


        
