#25. Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
#uma mensagem de permissão de acesso ou não.

def main():

    senha = int(input('Senha: '))

    if senha == 1234:
        print('Acesso permitido')
    else:
        print('Acesso negado')


main()
    
