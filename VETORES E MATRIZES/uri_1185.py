def main():

    operacao = input()
    soma = 0
    cont = 0

    for i in range(12):
        for j in range(12):
            valor = float(input())
            if (i + j <= 10):
                soma += valor
                cont += 1

    if operacao == 'S':
        print('%f'% soma)
    else:
        print('%f'% media)


main()


            
