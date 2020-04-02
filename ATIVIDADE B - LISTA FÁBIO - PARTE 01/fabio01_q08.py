#8. Leia 2 números, calcule e escreva a divisão da
#soma pela subtraçãodos números lidos.


def main():

    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))


    soma = num1 + num2
    subtracao = num1 - num2

    divisao = soma / subtracao


    print('O resultado da divisão é %.2f'%divisao)



main()


    
