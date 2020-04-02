def main():

    print('F - Filé, A - Alcatra, P - Picanha')
    print('---------------------------------------')
    tipo = input()
    qtd_carne = float(input())
    cartao = input()

    if tipo == 'F' or tipo == 'f':
        if qtd_carne <= 5:
            valor_pago = qtd_carne * 4.90
        else:
            valor_pago = qtd_carne * 5.80
        tipo = 'FILÉ'
    elif tipo == 'A' or tipo == 'a':
        if qtd_carne <= 5:
            valor_pago = qtd_carne * 5.90
        else:
            valor_pago = qtd_carne * 6.80
        tipo = 'ALCATRA'
    elif tipo == 'P' or tipo == 'p':
        if qtd_carne <= 5:
            valor_pago = qtd_carne * 6.90
        else:
            valor_pago = qtd_carne * 7.80
    else:
        print('Tipo de carne inválido')

    if cartao == 'SIM' or cartao == 'sim' or cartao == 'Sim':
        valor_car = valor_pago - ((valor_pago * 5) / 100)
        desconto = 5
        pagamento = 'CARTÃO TABAJARA'
    else:
        valor_car = valor_pago
        desconto = 0
        pagamento = 'DINHEIRO'


    print('CUPOM FISCAL')
    print('------------------')
    print('Tipo de carne: ', tipo)
    print('Quantidade de carne: %.2f'% qtd_carne)
    print('Preço total: %.2f'% valor_pago)
    print('TIPO DE PAGAMENTO: %s'% pagamento)
    print('Valor do desconto: %d'% desconto, '%')
    print('Valor a pagar: %.2f'% valor_car)

if __name__=='__main__':
    main()







