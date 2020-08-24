def main():

    n = int(input('N: '))
    soma = 0
    media_salario = 0
    num_filhos = 0
    perc = 0
    cont = 1


    while cont <= n:
        salario = float(input('Salário: R$ '))
        num_dependentes = int(input('N° de dependentes: '))
        cont = cont + 1

        soma = soma + salario
        num_filhos = num_filhos + num_dependentes

        if salario <= 1000:
            perc = perc + 1

        media_salario = soma / n
        media_filhos = num_filhos / n
        percentual = ((perc / n) * 100)


    print('Média de salário da população: R$%.2f'% media_salario)
    print('Média de número de filhos: ', media_filhos)
    print('Percentual de pessoas com salário até R$ 1000: ', percentual)


main()



        
