#Questão 08: Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
#depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
#11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde
#ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
#quantidade de horas trabalhadas no mês.
#Desconto do IR:
#            o Salário Bruto até R$ 900,00 (inclusive) - isento
#            o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
#            o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
#            o Salário Bruto acima de R$ 2.500,00 - desconto de 20%
#Escreva na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e
#a quantidade de hora é 220.
# Salário Bruto: (5 * 220) : R$ 1100,00
# (-) IR (5%) : R$ 55,00
# (-) INSS ( 10%) : R$ 110,00
# FGTS (11%) : R$ 121,00
# Total de descontos : R$ 165,00
# Salário Liquido : R$ 935,00

def main():

    #entrada
    valor_hora = float(input('valor p/hora: '))
    horas = int(input('horas: '))

    #computacao
    salario_bruto = valor_hora * horas
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    inss_porcet = '10%'
    fgts_porcet = '11%'
    ir = 0
    if salario_bruto <= 900:
        ir = 0
        ir_percentual = 'inseto'
    elif salario_bruto <=1500:
        ir = salario_bruto * 0.05
        ir_percentual = '5%'
    elif salario_bruto <= 2500:
        ir = salario_bruto * 0.1
        ir_percentual = '10%'
    elif salario_bruto > 2500:
        ir = salario_bruto * 0.2
        ir_percentual = '20%'
    total_desconto = ir + inss
    salario_liquido = salario_bruto - total_desconto

    #saida
    print(f"Salário Bruto: ({valor_hora} * {horas}) : R$ %.2f" %salario_bruto)
    print(f"(-) IR ({ir_percentual}) : R$ ",ir)
    print(f"(-) INSS ({inss_porcet}) : R$ ",inss)
    print(f"FGTS ({fgts_porcet}) : R$ ",fgts)
    print("Total de descontos : R$ %.2f" % total_desconto)
    print('Salário Liquido : R$ %.2f' %salario_liquido)


main()
