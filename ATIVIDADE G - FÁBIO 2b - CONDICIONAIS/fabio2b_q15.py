#15. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                        Até 5 Kg           Acima de 5 Kg
#Morango             R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã                R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10%
#sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas
#e escreva o valor a ser pago pelo cliente.

def main():

    qtd_mor = float(input())
    qtd_mac = float(input())

    if qtd_mor <= 5:
        valor_pago1 = qtd_mor * 2.50
    else:
        valor_pago1 = qtd_mor * 2.20
    if qtd_mac <= 5:
        valor_pago2 = qtd_mac * 1.80
    else:
        valor_pago2 = qtd_mac * 1.50


    valor_total = valor_pago1 + valor_pago2

    if valor_total > 8 or valor_total > 25:
        valor_pago = valor_total - ((valor_total * 10) / 100)

    print('O valor a ser pago pelo cliente é R$ %.2f'% valor_pago)


main()
