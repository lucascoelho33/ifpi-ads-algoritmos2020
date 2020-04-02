#20. Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
#quarto) em que o ângulo se localiza.

def main():

    angulo = int(input())

    if angulo <= 90:
        print('1° quadrante')
    elif angulo > 90 and angulo <= 180:
        print('2° quadrante')
    elif angulo > 180 and angulo <= 270:
        print('3° quadrante')
    elif angulo > 270 and angulo <= 360:
        print('4° quadrante')
    else:
        print('Quadrante inválido')

main()
