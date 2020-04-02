#Entrada

preco_capa = 24.95

#Calculo

desconto_da_livraria = (preco_capa / 100) * 40
transporte_primeiro = desconto_da_livraria + 3
transporte_resto = desconto_da_livraria + 0.75
custo_total = transporte_resto * 60 + transporte_primeiro


#Saida

print('O custo total é de R$ %.2f'% custo_total)
