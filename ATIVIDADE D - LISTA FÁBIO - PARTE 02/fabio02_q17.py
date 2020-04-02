#17. Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele fuma,
# o no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).

anos_que_fuma = int(input('Digite o número de anos que a pessoa fuma: '))
cigarros_dia = int(input('Digite o número de cigarros fumados por dia: '))
preco_carteira = float(input('Preço da carteira R$: '))

qtd_total = (anos_que_fuma * 365) * cigarros_dia
dinheiro_total = (qtd_total // 20) * preco_carteira

print('A quantidade de dinheiro gasta por um fumante é R$ %.2f'% dinheiro_total)
