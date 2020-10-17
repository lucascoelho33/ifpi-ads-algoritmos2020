# 8. Leia um vetor com N elementos, encontre e escreva o maior e o
# menor elemento e suas respectivas posições no vetor.

def main():

    n = int(input('N: '))
    vetor = []

    for i in range(n):
        elemento = int(input(f'{i} > '))
        vetor.append(elemento)

    maior = vetor[0]
    pos_maior = 0
    menor = vetor[0]
    pos_menor = 0


    for i in range(n):
        if vetor[i] > maior:
            maior = vetor[i]
            pos_maior = i
        if vetor[i] < menor:
            menor = vetor[i]
            pos_menor = i


    print(f'Maior = {maior} na posição {pos_maior}')
    print(f'Menor = {menor} na posição {pos_menor}')


main()


            
