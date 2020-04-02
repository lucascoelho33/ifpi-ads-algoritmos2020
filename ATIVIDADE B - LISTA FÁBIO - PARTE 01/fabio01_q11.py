#11. Leia um número inteiro (3 dígitos) e escreva o inverso do número.
#(Ex.: número = 532 ; inverso = 235).


def main():


    num = int(input('Digite um número inteiro: '))

    centena = num // 100
    dezena = (num % 100) // 10
    unidade = num % 10


    print(unidade,dezena,centena)



main()


    
