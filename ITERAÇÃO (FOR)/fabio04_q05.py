# 5. Leia um número, calcule e escreva seu fatorial.

def main():

    n = int(input('N: '))
    prod = 1

    for i in range(n):
        prod = prod * n
        n -= 1
    print(prod)


main()
