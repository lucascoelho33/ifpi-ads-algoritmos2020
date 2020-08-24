def main():

    n = int(input('N: '))
    cont = 0
    maior = 0
    menor = 0

    while cont < n:
        num_id = int(input('ID: '))
        peso = float(input('Peso: '))

        if peso > maior:
            maior = peso
        elif peso < maior:
            menor = peso
        cont = cont + 1

    print('ID: {} e o peso do boi mais magro é {} kg'.format(num_id, menor))
    print('ID: {} e o peso do boi mais gordo é {} kg'.format(num_id, maior))


main()

            
