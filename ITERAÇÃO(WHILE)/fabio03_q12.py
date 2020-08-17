# 12. Leia N e uma lista de N números e
# escreva a soma e a média de todos os números da lista.

def main():

    n = int(input())
    soma = 0
    cont = 1

    while cont <= n:
        num = int(input())
        soma = soma + num
        cont = cont + 1
    media = soma / n
    
    print('A soma é igual a {} e a média é igual a {}'.format(soma, media))


main()

        
