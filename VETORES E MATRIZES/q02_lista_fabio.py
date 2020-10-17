# Questão 02: Leia um vetor A com N elementos, verifique e escreva se
# existem ou não elementos iguais no vetor.


def main():

    # entrada
    n = int(input('N: '))
    a = criar(n)
    a = preencher(a)
    contem(a)
    
def contem(vetor):
    contador = 0
    for i in range(len(vetor)):
        for j in range(len(vetor)):
            if i != j:
                if vetor[i] == vetor[j]:
                    contador += 1
    if contador == 0:
        print('não contem elementos iguais')
    else:
        print('contém elementos iguais')


def criar(n):
    a = [0]*n
    return a

def preencher(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input('{} > '.format(i)))
    return vetor


main()
