#21. Sabendo que latão é constituído de 70% de cobre e 30% de zinco,
# escreva um algoritmo que calcule a quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg),
# informada pelo usuário.

qtd_latao = int(input('Digite a quantidade de latão em kg: '))

qtd_cobre = qtd_latao * 0.70
qtd_zinco = qtd_latao * 0.30

print('A quantidade de cobre é %d kg e a quantidade de zinco é %d kg'%(qtd_cobre, qtd_zinco))
