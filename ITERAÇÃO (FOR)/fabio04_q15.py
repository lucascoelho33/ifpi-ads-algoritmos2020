# 15. Leia N, calcule e escreva os
# N primeiros termos de seqüência (1, 3, 6, 10, 15,...).

def main():

    n = int(input('N: '))
    valor = 1
    aux = 2

    for i in range(1, n+1):
        print(valor, end=' ')
        valor += aux
        aux += 1


main()


        
