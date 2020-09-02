# 14. Leia N, calcule e escreva o maior quadrado menor ou igual a N.
# Por exemplo, se N for igual a 38, o maior quadrado menor
# que 38 é 36 (quadrado de 6).

def main():

    n = int(input('N: '))
    maior = 0

    for i in range(n):
        if (i**2) <= n:
            maior = i

    print(f'Maior quadrado = {maior}')


main()

