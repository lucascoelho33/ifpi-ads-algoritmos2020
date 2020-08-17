# 15. Leia N, calcule e escreva os N primeiros
# termos de seqüência (1, 3, 6, 10, 15,...).

def main():

    n = int(input('N: '))
    lista = 1
    cont = 0

    while cont < n:
        print(lista, end=' ')
        lista = lista + 2 + cont
        cont = cont + 1
        n = n - 1

main()

