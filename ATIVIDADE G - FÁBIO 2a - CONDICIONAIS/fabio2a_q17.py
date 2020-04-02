#17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
#escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
#são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
#divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
#escreva o quadrado dos números lidos.

def main():

    var1 = int(input('Variável 1: '))
    var2 = int(input('Variável 2: '))

    resto = var1 % var2

    if resto == 1:
        soma = (var1 + var2) + resto
        print(soma)
    elif resto == 2:
        if var1 % 2 == 0 and var2 % 2 == 0:
            print('Pares')
        else:
            print('Ímpares')
    elif resto == 3:
        prod = (var1 + var2) * var1
        print(prod)
    elif resto == 4:
        div = (var1 + var2) / var2
        print(div)
    else:
        quadrado1 = var1**2
        quadrado2 = var2**2
        print(quadrado1)
        print(quadrado2)


main()
