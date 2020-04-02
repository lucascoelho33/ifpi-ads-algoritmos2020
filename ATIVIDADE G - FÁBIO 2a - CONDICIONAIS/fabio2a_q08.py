#8. Leia data atual (dia, mês e ano) e data de nascimento (dia, mês e ano) de uma pessoa, calcule e escreva
#sua idade exata (em anos).

def main():

    dia_atual = int(input())
    mes_atual = int(input())
    ano_atual = int(input())
    print('')
    dia_nasc = int(input())
    mes_nasc = int(input())
    ano_nasc = int(input())

    dias_hoje = (ano_atual * 365) + (mes_atual * 30) + dia_atual
    dias_nascimento = (ano_nasc * 365) + (mes_nasc * 30) + dia_nasc
    dias_vida = dias_hoje - dias_nascimento
    anos_vida = dias_vida // 365

    print('Sua idade exata em anos é %d'% anos_vida)


main()
