def main():
    palavra = input()
    tamanho_linha = int(input('Tamanho da linha: '))

    resposta = right_justify(palavra, tamanho_linha)

    print(f'Linhas formatadas:\n{resposta}')


def right_justify(s, tamanho_linha):
    tam_palavra = len(s)

    qtd_espaco = tamanho_linha - tam_palavra
    espacos = qtd_espaco * ' '
    linha = espacos + s

    return linha


main()
