#27. Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
#nascimento e a data (dia, mês e ano) atual.

def main():

    dia_nasc = int(input('Dia: '))
    mes_nasc = int(input('Mês: '))
    ano_nasc = int(input('Ano: '))
    print('')
    dia_atual = int(input('Dia: '))
    mes_atual = int(input('Mês: '))
    ano_atual = int(input('Ano: '))


    ano = ano_atual - ano_nasc
    dia = dia_atual
    if mes_nasc >= mes_atual:
        ano = ano - 1
        mes = (mes_atual + 12) - mes_nasc
        if mes_nasc == mes_atual:
            mes = 0
            if dia_nasc >= dia_atual:
                ano = ano + 1
                dia = dia_atual - dia_nasc
    elif mes_atual > mes_nasc:
        mes = mes_atual - mes_nasc

    print('{} anos,{} meses e {} dias'.format(ano, mes, dia))


main()
    
