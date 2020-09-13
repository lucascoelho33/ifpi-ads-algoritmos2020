def main():

    n = int(input())

    for i in range(n):
        texto = input('Texto: ')
        chave = int(input('Chave: '))
    

        texto_criptografado = cripto_texto(texto, chave)
        texto_invertido = inverso_texto(texto, chave)

        print(f'{texto_criptografado}')
        print(f'{texto_invertido}')


def cripto_texto(texto, chave):
    mensagem = ''
    for letra in texto:
        codigo = ord(letra)
        novo_codigo = chr(codigo + chave)
        mensagem += novo_codigo

    return mensagem


def rotacionar_caractere(texto, chave):
    codigo = ord(texto)
    novo_codigo = codigo + chave
    novo_caractere = chr(novo_codigo)

    return novo_caractere


def inverso_texto(texto, chave):
    nova_mensagem = ''

    for i in range(len(texto)-1, -1, -1):
        nova_mensagem += texto[i]

    return nova_mensagem


main()


    
    
    

    
