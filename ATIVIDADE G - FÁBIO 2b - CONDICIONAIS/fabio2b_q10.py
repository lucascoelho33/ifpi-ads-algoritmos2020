#10. Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
#A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
#Entre 9.0 e 10.0          A
#Entre 7.5 e 9.0           B
#Entre 6.0 e 7.5           C
#Entre 4.0 e 6.0           D
#Entre 4.0 e zero          E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e
#a  mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

def main():

    n1 = float(input())
    n2 = float(input())
    print('Nota 1: %.2f'% n1)
    print('Nota 2: %.2f'% n2)

    media = (n1 + n2) / 2
    print('Média: %.2f'% media)

    if 9 < media < 10:
        print('Conceito A')
    elif 7.5 < media < 9:
        print('Conceito B')
    elif 6 < media < 7.5:
        print('Conceito C')
    elif 4 < media < 6:
        print('Conceito D')
    elif 0 < media < 4:
        print('Conceito E')

    conceito = input()

    if conceito == A or conceito == B or conceito == C:
        print('APROVADO')
    else:
        print('REPROVADO')


main()
