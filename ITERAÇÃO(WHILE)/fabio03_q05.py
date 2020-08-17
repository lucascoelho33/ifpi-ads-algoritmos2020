# 5. Leia um número, calcule e escreva seu fatorial.

def main():

    num = int(input('Num: '))
    fatorial = 1

    while num > 1:
        fatorial = fatorial * num
        num = num - 1

    print(f'O fatorial é {fatorial}')


main()

        
