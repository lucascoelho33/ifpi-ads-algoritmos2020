def main():

    n = int(input('N: '))

    matriz = [0] * n

    for i in range(n):
        matriz[i] = [0] * n
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input('Valor %d%d: '%(i, j)))

    for i in range(len(matriz)):
        print(matriz[i])


    print('Soma da diagonal principal: ',soma_diagonal_principal(matriz))
    print('Soma da diagonal secundaria: ',soma_diagonal_secundaria(matriz))


def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j:
                soma += matriz[i][j]

    return soma


def soma_diagonal_secundaria(matriz):
    soma = 0
    for i in range(len(matriz)-1,-1,-1):
        for j in range(len(matriz)):
            if i + j == len(matriz) - 1:
                soma += matriz[i][j]

    return soma


main()

