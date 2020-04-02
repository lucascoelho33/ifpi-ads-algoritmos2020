#3. Leia um valor em minutos, calcule e escreva o equivalente em
#horas e minutos.


def main():

    minutos = int(input('Digite um valor em minutos: '))


    horas = minutos // 60
    minutos2 = minutos % 60


    print(minutos, 'min é igual a',horas,'h',minutos2,'min')


main()

    
