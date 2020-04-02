#2. Leia uma letra, verifique se  letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.

def main():

    letra = input()

    if letra == 'F' or letra == 'f':
        print('Feminino')
    elif letra == 'M' or letra == 'm':
        print('Masculino')
    else:
        print('Sexo Inválido')


main()
