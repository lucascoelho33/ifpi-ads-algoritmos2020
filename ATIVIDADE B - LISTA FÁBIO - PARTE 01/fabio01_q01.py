#1. Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h.
#(Vkm/h = Vm/s * 3.6).

def main():

    vel_ms = float(input('Digite um velocidade em m/s: '))

    vel_kmh = vel_ms * 3.6

    print('A velocidade em km/h é equivalente a %.1f' % vel_kmh,'km/h')


main()
