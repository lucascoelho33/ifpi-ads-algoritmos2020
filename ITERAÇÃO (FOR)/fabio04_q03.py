# 3. Leia as variáveis A0, Limite e R e escreva os
# valores menores que Limite gerados pela Progressão
# Aritmética que tem por valor inicial A0 e razão R.

def main():

    a = int(input('A0: '))
    limite = int(input('Limite: '))
    r = int(input('Razão: '))

    for i in range(a, limite+1, r):
        a = a + r
        print(i)


main()
