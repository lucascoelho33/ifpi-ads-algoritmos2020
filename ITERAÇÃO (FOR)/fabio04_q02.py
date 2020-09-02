# 2. Leia N e escreva todos os números inteiros pares de 1 a N.

def main():

    n = int(input('N: '))

    for i  in range(1, n+1):
        if i % 2 == 0:
            print(i)


main()

