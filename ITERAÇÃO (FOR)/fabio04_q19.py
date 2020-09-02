def main():

    n = int(input('N: '))
    soma = 0
    numerador = 1
    denominador = n

    for i in range(1, n+1):
        if i % 2 != 0:
            soma += i / n
        else:
            soma -= n / i

    n -= 1

    print('SOMA: %.2f'% soma)


main()

