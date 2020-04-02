#5. Leia 3 (três) números e escreva-os em ordem crescente.

def main():

    num1 = int(input('1° número: '))
    num2 = int(input('2° número: '))
    num3 = int(input('3° número: '))

    if num1 < num2 and num2 < num3:
        print('%d < %d < %d'%(num1,num2,num3))
    elif num1 < num2 and num1 < num3 and num3 < num2:
        print('%d < %d < %d'%(num1,num3,num2))
    elif num2 < num1 and num2 < num3 and num1 < num3:
        print('%d < %d < %d'%(num2,num1,num3))
    elif num2 < num1 and num2 < num3 and num3 < num1:
        print('%d < %d < %d'%(num2,num3,num1))
    elif num3 < num2 and num3 < num1 and num1 < num2:
        print('%d < %d < %d'%(num3,num1,num2))
    elif num3 < num2 and num3 < num1 and num2 < num1:
        print('%d < %d < %d'%(num3,num2,num1))
    else:
        print('Os números são iguais')


main()
