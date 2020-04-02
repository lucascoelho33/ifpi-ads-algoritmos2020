#6. Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
#se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
#verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
#obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).

def main():

    num1 = int(input('1° número: '))
    num2 = int(input('2° número: '))
    num3 = int(input('3° número: '))

    soma = num1 + num2 + num3

    if soma == 180 and num1 > 0 and num2 > 0 and num3 > 0:
        print('Forma um triângulo')
        if num1 < 90 and num2 < 90 and num3 < 90:
            print('Triângulo Acutângulo')
        elif num1 == 90 or num2 == 90 or num3 == 90:
            print('Triângulo Retângulo')
        elif num1 > 90 or num2 > 90 or num3 > 90:
            print('Triângulo Obtusângulo')
        elif num1 == 0 and num2 == 0 and num3 == 0:
            print('Não existe ângulo com tamanho 0°')
    else:
        print('Não forma um triângulo')


main()
