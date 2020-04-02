def main():

    litros_vendidos = int(input('Digite o número de litros vendidos: '))
    tipo = str(input('A - álcool, G - gasolina: ' ))

    preco_gas = 2.50
    preco_alc = 1.90

    if tipo == 'A' or tipo == 'a':
        if litros_vendidos <= 20:
            valor_alc = (1.90 * 3) / 100
            print('Valor a pagar : R$ %.2f'% valor_alc)
        else:
            valor_alc2 = (1.90 * 5) / 100
            print('Valor a pagar: R$ %.2f'% valor_alc2)
    elif tipo == 'G' or tipo == 'g':
        if litros_vendidos <= 20:
            valor_gas = (2.50 * 4) / 100
            print('Valor a pagar: R$ %.2f'% valor_gas)
        else:
            valor_gas2 = (2.50 * 6) / 100
            print('Valor a pagar: R$ %.2f'% valor_gas2)
    else:
        print('Tipo de combustível inválido')

if __name__=='__main__':
    main()

