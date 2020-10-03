def main():

    menu = '**** TREINO LISTAS ****\n' 
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar valor da posição'
    menu += '\n 3 - Mostrar todos os valores'
    menu += '\n 4 - Remover valor'
    menu += '\n 5 - Atualizar vetor'
    menu += '\n 6 - Quantidade de Pares'
    menu += '\n 7 - Quantidade de Ímpares'
    menu += '\n 8 - Quantidade de Primos'
    menu += '\n 9 - Quantidade de Positivos'
    menu += '\n 10 - Quantidade de zerados'
    menu += '\n 11 - Média dos valores' 
    menu += '\n 0 -  Sair'   
    menu += '\n\n Opção ->-> '


    lista = []

    while True:
        opcao = int(input(menu))
        if opcao == 1:
            inserir_valores(lista)
        elif opcao == 2:
            mostra_valor_pos(lista)
        elif opcao == 3:
            mostra_todos(lista)
        elif opcao == 4:
            remover_valor(lista)
        elif opcao == 5:
            atualizar_valor(lista)
        elif opcao == 6:
            qtd_pares = contar_qtd_pares(lista)
            print(f'São {qtd_pares} números pares')
        elif opcao == 7:
            qtd_impares = contar_qtd_impares(lista)
            print(f'São {qtd_impares} números ímpares')
        elif opcao == 8:
            qtd_primos = contar_qtd_primos(lista)
            print(f'São {qtd_primos} números primos')
        elif opcao == 9:
            qtd_positivos = contar_qtd_positivos(lista)
            print(f'São {qtd_positivos} números positivos')
        elif opcao == 10:
            qtd_zerados = contar_qtd_zerados(lista)
            print(f'São {qtd_zerados} numeros zerados')
        elif opcao == 11:
            media = calcular_media(lista)
            print(f'Media: {media}')
        elif opcao == 0:
            break
        else:
            print('Valor inválido.')


def inserir_valores(lista):
    qtd = int(input('Qtd de números: '))

    for i in range(qtd):
        num = int(input('Digite um número: '))
        lista.append(num)

    print(lista)
    print('<enter> para continuar')
    print()



def mostra_valor_pos(lista):
    posicao = int(input('Posição: '))
    print('Valor buscado...')
    print(lista[posicao])

    print('<enter> para continuar')
    print()


def mostra_todos(lista):
    tamanho = len(lista)
    print(f'>>>> Mostrando a lista <<<<')
    for i in lista:
        print(i)


def remover_valor(lista):
    pos = int(input('Qual posição quer remover? '))

    removido = lista.pop(pos)
    print(f'O valor {removido} foi removido da posição {pos}')
    print(lista)


def atualizar_valor(lista):
    pos = int(input('Qual posição quer atualizar? '))

    valor = lista[pos]
    print(f'Na posição {pos} existe o valor {valor}')

    novo_valor = int(input('Digite o novo valor: '))
    lista[pos] = novo_valor
    print('Valor atualizado!')
    print(lista)


def contar_qtd_pares(lista):
    qtd = 0

    for numero in lista:
        if eh_par(numero):
            qtd += 1

    return qtd

def eh_par(numero):
    if numero % 2 == 0:
        return numero


def contar_qtd_impares(lista):
    qtd = 0
    for numero in lista:
        if eh_impar(numero):
            qtd += 1

    return qtd

def eh_impar(numero):
    if numero % 2 != 0:
        return numero


def contar_qtd_primos(lista):
    qtd = 0
    for numero in lista:
        if eh_primo(numero):
            qtd += 1

    return qtd

def eh_primo(numero):
    if numero % 2 == 1:
        return numero


def contar_qtd_positivos(lista):
    qtd = 0
    for numero in lista:
        if eh_positivo(numero):
            qtd += 1

    return qtd

def eh_positivo(numero):
    if numero > 0:
        return numero



def contar_qtd_zerados(lista):
    qtd = 0
    for numero in lista:
        if eh_zerado(numero):
            qtd += 1

    return qtd

def eh_zerado(numero):
    if numero == 0:
        return numero


def calcular_media(lista):
    somatorio = 0
    for numero in lista:
        somatorio += numero

    media = somatorio / len(lista)

    return media
  

main()

            
            
