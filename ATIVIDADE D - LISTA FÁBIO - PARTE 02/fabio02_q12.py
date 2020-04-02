#12. Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.:
# número = 9534 ; soma = 9+5+3+4 = 21.

num = int(input('Digite um número de 4 dígitos: '))

numero_milhar = num // 1000
resto_milhar = num % 1000
numero_centena = resto_milhar // 100
resto_centena = resto_milhar % 100
numero_dezena = resto_centena // 10
numero_unidade = resto_centena % 10

soma_algarismos = numero_milhar + numero_centena + numero_dezena + numero_unidade

print('SOMA = ', soma_algarismos)
