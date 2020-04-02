#30. Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
#o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
#milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
#terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
#2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.

def main():

    num = int(input('Digite um número de 4 dígitos: '))

    milhar_centena = num // 100
    dezena_unidade = num % 100
    soma = milhar_centena + dezena_unidade
    quadrado = soma**2

    if num == quadrado:
        print('O quadrado do terceiro número formado é igual ao número original')
    elif num != quadrado:
        print('O quadrado do terceiro número formado não é igual ao número original')


main()
