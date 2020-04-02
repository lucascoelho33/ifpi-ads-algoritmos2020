#19. Leia o valor do raio de uma esfera, calcule e escreva seu volume.
#(v = (4 * p * r3) / 3) (p = 3,14).



def main():


    raio = float(input('Raio: '))
    pi = 3.14

    v = (4 * pi * raio**3) / 3


    print('Volume: %.2f'% v)



main()


    
