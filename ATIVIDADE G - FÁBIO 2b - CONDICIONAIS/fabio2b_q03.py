#3. Leia uma letra e verifique se a letra digitada é vogal ou consoante.

def main():

    letra = input()

    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        print('Vogal Maiúscula')
    elif letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('Vogal Minúscula')
    else:
        print('Consoante')



main()
