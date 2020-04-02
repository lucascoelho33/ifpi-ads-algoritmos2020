#13. Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#    a) "Telefonou para a vítima ?"
#    b) "Esteve no local do crime ?"
#    c) "Mora perto da vítima ?"
#    d) "Devia para a vítima ?"
#    e) "Já trabalhou com a vítima ?"
#O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
#e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

def main():

    pergunta1 = input('Telefonou para a vítima? ')
    pergunta2 = input('Esteve no local do crime? ')
    pergunta3 = input('Mora perto da vítima? ')
    pergunta4 = input('Devia para a vítima? ')
    pergunta5 = input('Já trabalhou com a vítima? ')

    resp = input()

    if resp == 2:
        print('Suspeita')
    elif resp == 3 or resp == 4:
        print('Cúmplice')
    elif resp == 5:
        print('Assassino')
    else:
        print('Inocente')


main()
