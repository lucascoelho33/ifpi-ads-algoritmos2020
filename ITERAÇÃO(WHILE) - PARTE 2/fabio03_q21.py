def main():

    denominador = 1
    numerador = 1
    somatorio = 0

    while denominador <= 50:
        somatorio += numerador/denominador
        denominador += 1
        numerador += 1

    print('SOMA: %.f'% somatorio)

main()
