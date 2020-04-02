#23. Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais
#recente.

def main():
    

    dia1 = int(input())
    mes1 = int(input())
    ano1 = int(input())

    dia2 = int(input())
    mes2 = int(input())
    ano2 = int(input())

    if ano1 == ano2:
        if mes1 == mes2:
            if dia1 > dia2:
                print('A primeira data é mais recente')
            elif dia2 > dia1:
                print('A segunda data é mais recente')
        elif mes1 > mes2:
            print('A primeira data é mais recente')
        elif mes2 > mes1:
            print('A segunda data é mais recente')
    elif ano1 > ano2:
        print('A primeira data é mais recente')
    elif ano2 > ano1:
        print('A segunda data é mais recente')


main()
