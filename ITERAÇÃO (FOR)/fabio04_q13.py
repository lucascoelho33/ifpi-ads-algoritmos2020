# 13. Leia N e uma lista de N números e escreva o maior número da lista.

def main():

    n = int(input('N: '))
    maior = 0

    for i in range(n):
        num = int(input('Digite um número: '))
        if num > maior:
            maior = num
    print(f'Maior: {maior}')


main()

