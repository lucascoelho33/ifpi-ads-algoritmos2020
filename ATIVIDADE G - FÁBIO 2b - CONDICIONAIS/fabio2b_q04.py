#4. Leia 2 (duas)  notas parciais de um aluno, calcule a média e escreva a mensagem:
#o "Aprovado", se a média alcançada for maior ou igual a sete;
#o "Reprovado", se a média for menor do que sete;
#o "Aprovado com Distinção", se a média for igual a dez.

def main():

    n1 = float(input())
    n2 = float(input())

    media = (n1 + n2) / 2

    if media == 10:
        print('Aprovado com Distinção')
    elif media >= 7:
        print('Aprovado')
    else:
        print('Reprovado')


main()
