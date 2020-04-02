#26. Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.

def main():

    lado1 = int(input())
    lado2 = int(input())
    lado3 = int(input())

    if lado1 > lado2 and lado1 > lado3:
        print('Hipotenusa: {} e os catetos são {},{}'.format(lado1,lado2,lado3))
    elif lado2 > lado1 and lado2 > lado3:
        print('Hipotenusa: {} e os catetos são {},{}'.format(lado2,lado1,lado3))
    else:
        print('Hipotenusa: {} e os catetos são: {},{}'.format(lado3,lado1,lado2))


main()
        
