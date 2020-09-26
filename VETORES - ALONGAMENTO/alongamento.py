def main():

    numero = int(input('Quantos números? '))


    vetor = gerar_vetor(numero, -1)

    print(vetor)
    for pos in range(len(vetor)):
        vetor[pos] = int(input('Num: '))
        

    print(vetor)

    qtd_pares = contar_pares(vetor)
    qtd_impares = contar_impares(vetor)
    qtd_positivo = contar_positivo(vetor)
    qtd_negativo = contar_negativo(vetor)

    print(f'Pares: {qtd_pares}')
    print(f'Ímpares: {qtd_impares}')
    print(f'Positivos: {qtd_positivo}')
    print(f'Negativos: {qtd_negativo}')
    print('')

    
    vetor_transformado = transformar(vetor)
    print('>> Vetor Transformado <<')
    print(vetor)

    qtd_pares = contar_pares(vetor_transformado)
    qtd_impares = contar_impares(vetor_transformado)
    qtd_positivo = contar_positivo(vetor_transformado)
    qtd_negativo = contar_negativo(vetor_transformado)

    print(f'Pares: {qtd_pares}')
    print(f'Ímpares: {qtd_impares}')
    print(f'Positivos: {qtd_positivo}')
    print(f'Negativos: {qtd_negativo}')
    print('')


    media = calcular_media(vetor_transformado)

    print(f'Média: {media}')
   

def gerar_vetor(num, valor):
    return [valor] * num


def contar_pares(vetor):
    qtd = 0
    for numero in vetor:
        if eh_par(numero):
            qtd += 1
            
    return qtd

def eh_par(numero):
    if numero % 2 == 0:
        return numero

    
def contar_impares(vetor):
    qtd = 0
    for numero in vetor:
        if eh_impar(numero):
            qtd += 1

    return qtd

def eh_impar(numero):
    if numero % 2 != 0:
        return numero


def contar_positivo(vetor):
    qtd = 0
    for numero in vetor:
        if eh_positivo(numero):
            qtd += 1

    return qtd

def eh_positivo(numero):
    if numero > 0:
        return numero


def contar_negativo(vetor):
    qtd = 0
    for numero in vetor:
        if eh_negativo(numero):
            qtd += 1

    return qtd

def eh_negativo(numero):
    if numero < 0:
        return numero


def transformar(vetor):
    for i in range(len(vetor)):
        if vetor[i] > 0:
            vetor[i] = vetor[i] * 2
        else:
            vetor[i] = vetor[i] / 2

    return vetor



def calcular_media(vetor):
    somatorio = 0
    for valor in vetor:
        somatorio += valor


    media = somatorio / len(vetor)


    return media

          
    

main()

