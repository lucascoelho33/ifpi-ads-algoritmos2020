#12. Leia um número e escreva se o número é inteiro ou decimal.

def main():

    num = float(input())

    parte_decimal = (num * 100) % 100

    if parte_decimal == 0:
        print('É um número inteiro')
    else:
        print('É um número decimal')



main()
