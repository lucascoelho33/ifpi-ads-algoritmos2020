def main():

    o = input()

    matriz = []
    tamanho = 12


    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(float(input()))
        matriz.append(linha)


    v = []

    for c in range(1, tamanho):
        for l in range(tamanho-c, tamanho):
            v.append(matriz[c][l])


    resultado = 0
    if o == 's':
        resultado = sum(v)
    else:
        resultado = sum(v) / len(v)


    print('%.1f'% resultado)


main()
