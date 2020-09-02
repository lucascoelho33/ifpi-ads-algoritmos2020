def main():

    soma = 0
    aux = 1

    for i in range(1, 51):
        soma += aux/i
        aux += 2

    print('SOMA: %.2f'% soma)


main()

