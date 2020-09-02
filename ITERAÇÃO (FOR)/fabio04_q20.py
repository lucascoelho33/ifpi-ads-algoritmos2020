def main():

    n = int(input('N: '))
    soma = 0

    for i in range(1, n+1):
        if i % 2 == 0:
            soma += 1/i
        else:
            soma -= 1/i

    print('SOMA: %.2f'% soma)


main()

