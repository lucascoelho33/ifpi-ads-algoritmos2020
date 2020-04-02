#10. Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

def main():

    dia = int(input('Dia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))
    valido = False

    if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if dia <= 31:
            valido = True
    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
        if dia <= 30:
            valido = True
    elif mes == 2:
        if (ano % 4 == 0 and ano % 400 != 0) or (ano % 400 == 0):
            if dia <= 29:
                valido = True
            elif dia <= 28:
                valido = True
    if valido:
        print('Data Válida')
    else:
        print('Data inválida')


main()


            
