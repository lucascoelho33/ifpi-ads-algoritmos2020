#Questão 11: Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
#número. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplos:
#            o 326 = 3 centenas, 2 dezenas e 6 unidades
#            o 12 = 1 dezena e 2 unidades

def main():

    #entrada
    numero = int(input('número: '))

    #computacao
    if numero <= 99:
        dezena = numero // 10
        unidade = numero % 10
        print(f'{numero} = {dezena} dezena e {unidade} unidades')
    elif numero <= 999:
        centena = numero // 100
        resto = numero % 100
        dezena = resto // 10
        unidade = resto % 10
        print(f'{numero} = {centena} centenas, {dezena} dezenas e {unidade} unidades')


main()
