def main():

    n = int(input('N: '))
    cont = 1
    soma = 0

    while n >= 1:
        soma = soma + cont/n
        n = n - 1
        cont = cont + 1


    print('SOMA: %.2f'% soma)


main()

    
