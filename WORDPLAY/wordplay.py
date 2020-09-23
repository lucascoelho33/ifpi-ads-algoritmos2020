def main():

    menu = '**** WORDPLAY ****\n' \
        + '1 - Palavras com mais de 20 letras\n' \
        + '2 - Palavras sem "e"\n' \
        + '3 - Palavras sem letras proibidas\n' \
        + '4 - Palavras com letras permitidas\n' \
        + '0 - Sair\n' \
        + '\Digite uma opção: '

    opcao = int(input(menu))


    while opcao != 0:
        if opcao == 1:
            palavras_com_mais_de_20_letras()
        elif opcao == 2:
            palavras_sem_e()
        elif opcao == 3:
            letras_proibidas()
        else:
            print('Opção Inválida!')

        input('continuar <enter>')
        opcao = int(input(menu))


    print('FIM WORDPLAY....')



def palavras_com_mais_de_20_letras():
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) > 20:
            print(palavra)

    arquivo.close()


def palavras_sem_e():
    arquivo = open('words.txt')
    total = 0
    palavras_sem_e = 0

    for linha in arquivo:
        palavra.strip()
        total += 1
        if has_no_e(palavra):
            palavras_sem_e += 1
            print(palavra)


    perc = (palavras_sem_e / total) * 100
    print(f'Total de Palavras: {total}')
    print(f'Palavras sem "e": {palavras_sem_e}')
    print(f'Percentual: {perc} %')
    arquivo.close()

def has_no_e(palavra):
    for letra in palavra:
        if letra == 'e':
            return False

    return True


def avoids():
    arquivo = open('words.txt')
    total = 0
    letras_proibidas = 0

    for linha in arquivo:
        palavra.strip()
        total += 1
        if letras_proibidas(palavra):
            letras_proibidas += 1
            print(palavra)

    arquivo.close()

def letras_proibidas():
    palavra = input('Palavra: ')
    letras_proibidas = input('Letras: ')
    for letras_proibidas not in palavra:
        return True


def uses_only():
    arquivo = open('words.txt')
    letras_permitidas = input('Digite somente as letras permitidas: ')


    for linha in arquivo:
        palavra = linha.strip()
        contem_letras(letras_permitidas, palavra)

    arquivo.close()


def contem_letras(letras_permitidas, palavra):
    cont = 0

    for letra in range(len(palavra)):
        if palavra[letra] not in letras_permitidas:
            cont += 1
    if cont == 0:
        print(palavra)
            


main()

    
        
            
