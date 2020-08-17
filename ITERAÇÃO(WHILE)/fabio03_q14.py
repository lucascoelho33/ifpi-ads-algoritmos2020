# 14. Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo,
# se N for igual a 38,o maior quadrado menor que 38 é 36 (quadrado de 6).

def main():

    n = int(input('N: '))
    cont = 1
    maior = 0

    while cont <= n:
        quadrado = 6** cont
        if quadrado <= n:
            maior = quadrado
        cont = cont + 1

    print('Maior: {}'.format(maior))


main()
