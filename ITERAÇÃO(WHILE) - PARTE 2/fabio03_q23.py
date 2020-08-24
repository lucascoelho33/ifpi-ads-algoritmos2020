def main():

    n = int(input('N° de funcionários: '))
    cont = 0

    while cont <= n:
        codigo = int(input('Código: '))
        num_horas = int(input('N° DE HORAS: '))
        num_dependentes = int(input('N° de dependentes: '))
        cont = cont + 1

        salario_bruto = num_horas * 12 + num_dependentes * 40
        inss = salario_bruto * (8.5 /100)
        ir = salario_bruto * (5/100)

        salario_liquido = salario_bruto - inss - ir

        print('Desconto do INSS: R$ %.2f'% inss)
        print('Desconto do IR: R$ %.2f'% ir)
        print('Salario liquido: R$ %.2f'% salario_liquido)


main()
