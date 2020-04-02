#28. Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
#um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
#não pode ser negativo.

def main():

    x = float(input('X: '))
    y = float(input('Y: '))

    area = x * y

    if area <= 0:
        print('Valor inválido')
    else:
        print('O valor da área do retângulo é %d'% area)


main()
