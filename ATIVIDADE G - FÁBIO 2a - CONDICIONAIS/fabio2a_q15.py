#15. Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
#Escreva na tela qual dos professores tem salário total maior.

def main():

    qtd_horas1 = int(input('Quantidade de horas: '))
    valor_recebido1 = float(input('Valor recebido: R$ '))
    qtd_horas2 = int(input('Quantidade de horas: '))
    valor_recebido2 = float(input('Valor recebido: R$ '))

    salario1 = (qtd_horas1 * valor_recebido1)
    salario2 = (qtd_horas2 * valor_recebido2)

    if salario1 > salario2:
        print('O primeiro professor possui o salário maior')
    elif salario1 < salario2:
        print('O segundo professor possui o salário maior')
    else:
        print('Os dois professores possuem o mesmo salário')


main()
