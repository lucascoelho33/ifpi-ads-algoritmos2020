def main():

    n = int(input('N: '))

    for i in range(n):
        codigo = int(input('Código: '))
        num_horas = int(input('N° de horas: '))
        num_dependentes = int(input('N° de dependentes: '))

        salario = (12 * num_horas) + (40 * num_dependentes)
        inss = salario - (8.5 / 100)
        ir = salario - (5 / 100)

        salario_liquido = salario + inss + ir

        print('INSS: R$ %.2f'% inss)
        print('IR: R$ % .2f'% ir)
        print('Salário líquido: R$ %.2f'% salario_liquido)


main()

