#11. Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
#valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
#possíveis para a variável opção são 1, 2 e 3.

def main():

    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    opcao = int(input('Opção: '))

    if opcao == 1:
        print(num1)
    elif opcao == 2:
        print(num2)
    elif opcao == 3:
        print(num3)
    else:
        print('Número inválido')


main()
