#18. Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 –
#Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação
#sobre os dois valores lidos.

def main():

    num1 = int(input('Num 1: '))
    num2 = int(input('Num 2: '))
    print('1 - Adição, 2 - Subtração, 3 - Multiplicação, 4 - Divisão')
    operacao = int(input('Operação? '))

    if operacao == 1:
        soma = (num1 + num2)
        print(soma)
    elif operacao == 2:
        diferenca = (num1 - num2)
        print(diferenca)
    elif operacao == 3:
        produto = (num1 * num2)
        print(produto)
    elif operacao == 4:
        divisao = (num1 / num2)
        print(divisao)
    else:
        print('Operação inválida')


main()
