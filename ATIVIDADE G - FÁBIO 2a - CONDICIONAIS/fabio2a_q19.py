#19. Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
#(IMC = peso / altura2
#). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso
#(IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).

def main():

    altura = float(input())
    peso = float(input())

    imc = peso / altura**2

    if imc < 25:
        print('Peso normal')
    elif imc > 25 and imc < 30:
        print('Obeso')
    elif imc > 30:
        print('Obesidade mórbida')


main()

    
