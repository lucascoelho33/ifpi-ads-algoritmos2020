def main():

    n = int(input('N: '))
    id_maior = 0
    id_menor = 0
    maior = 0
    menor = 0

    for i in range(n):
        num_id = int(input('ID: '))
        nome = input('Nome: ')
        peso = float(input('Peso: '))

        if peso > maior:
            maior = peso
            id_maior = num_id
        else:
            menor = peso
            id_menor = num_id

    print('O ID do boi mais magro é {} e o peso é igual a {}'.format(id_menor, menor))
    print('O ID do boi mais gordo é {} e o peso é igual a {}'.format(id_maior, maior))


main()
