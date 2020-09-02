# 12. Leia N e uma lista de N números e
# escreva a soma e a média de todos os números da lista.

def main():

    n = int(input('N: '))
    soma = 0

    for i in range(n):
        num = int(input('Digite um número: '))
        soma += num
        media = soma / n
    print(f'SOMA = {soma}')
    print(f'MÉDIA = {media}')


main()

