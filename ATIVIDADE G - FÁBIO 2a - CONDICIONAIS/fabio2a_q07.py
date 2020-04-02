#7. Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
#(três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
#formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
#escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).

def main():

    n1 = int(input('Lado 1: '))
    n2 = int(input('Lado 2: '))
    n3 = int(input('Lado 3: '))

    if n1 < n2 + n3 or n2 < n1 + n3 or n3 < n1 + n2:
        print('Forma um triângulo')
        if n1 == n2 == n3:
            print('Triângulo Equilátero')
        elif n1 == n2 != n3 or n1 == n3 != n2 or n1!= n2 == n3:
            print('Triângulo Isósceles')
        elif n1 != n2 and n1 != n3 and n2 != n3:
            print('Triângulo Escaleno')
        else:
            print('Não existe lado com tamanho 0')
    else:
        print('Não forma um triângulo')


main()
