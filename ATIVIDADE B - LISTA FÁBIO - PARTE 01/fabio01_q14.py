#14. Leia 3 notas de um aluno e o peso de cada nota,
#calcule e escreva média ponderada.


def main():


    nota1 = float(input('1° nota: '))
    nota2 = float(input('2° nota: '))
    nota3 = float(input('3° nota: '))

    peso1 = int(input('1° peso: '))
    peso2 = int(input('2° peso: '))
    peso3 = int(input('3° peso: '))


    media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1+peso2+peso3)


    print('A média ponderada dos 3 alunos é %.2f'% media)



main()



    

    
