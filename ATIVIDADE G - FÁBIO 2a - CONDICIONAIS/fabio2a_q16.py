#16. Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
#ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
#final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
#escreva “Reprovado”.

def main():

    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))

    media = (n1 + n2) / 2

    if media >= 7:
        print('Aprovado')
    else:
        nota_exame = float(input('Nota do exame: '))
        media_final = (media + nota_exame) / 2

        if media_final >= 5:
            print('Aprovado')
        else:
            print('Reprovado')


main()
