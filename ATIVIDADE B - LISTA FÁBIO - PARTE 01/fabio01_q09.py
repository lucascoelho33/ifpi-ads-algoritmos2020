#9. Leia 2 números (A, B) e escreva-os em ordem inversa (B, A).


def main():

    a = int(input('Digite o primeiro numero: '))
    b = int(input('Digite o segundo número: '))

    receptor = a
    a = b
    b = receptor


    print('A ordem inversa é ',a,'',b)



main()


    
