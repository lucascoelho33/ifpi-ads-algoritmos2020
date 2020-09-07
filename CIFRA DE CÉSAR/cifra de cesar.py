def main():

    mensagem = input('Mensagem: ')
    chave = int(input('Chave: '))
    n = 128   # tamanho da tabela ascii
    texto = ''

    
    for letra in mensagem:
        codigo = ord(letra)
        novo_codigo = chr((codigo + chave) % n)
        texto = texto + novo_codigo

    print(mensagem)
    print(texto)


main()

