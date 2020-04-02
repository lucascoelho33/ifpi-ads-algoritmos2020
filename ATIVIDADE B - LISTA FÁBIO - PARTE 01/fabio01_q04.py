#4. Leia o valor do dólar e um valor em dólar,
#calcule e escreva o equivalente em real (R$).


def main():

    dolar = float(input('Digite o valor do dólar: '))
    valor_dolar = float(input('Digite um valor em dólar: '))


    real = valor_dolar / dolar


    print('O valor em real é R$ %.2f'%real,'reais')


main()


    
