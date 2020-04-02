#24. Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o
#coeficiente A deve ser diferente de 0 (zero).

from math import sqrt

def main():

    a = int(input())
    b = int(input())
    c = int(input())

    if a < 0 or b < c:
        print('Não é possível calcular as raízes')
    else:
        x1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
        x2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
        print('X1: %.1f'% x1)
        print('X2: %.1f'% x2)


main()
