def main():

    n = int(input('N: '))
    soma_salario = 0
    soma_filhos = 0
    perc = 0

    for i in range(n):
        salario = float(input('Salário: '))
        num_filhos = int(input('N° de filhos: '))

        soma_salario += salario
        soma_filhos += num_filhos

        if salario <= 1000:
            perc += 1

        media_salario = soma_salario / n
        media_filhos = soma_filhos / n


    print('A média de salário da população é R$ %.2f'% media_salario)
    print('A média de número de filhos é de %.2f'% media_filhos)
    print('O percentual de pessoas com salário até R$ 1000.00 é de {}%'.format((perc / n) * 100))


main()



        
        
