#10. Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.
# (Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).

num = int(input('Digite um número com 3 dígitos: '))

numero_centena = num // 100
resto_centena = num % 100
numero_dezena = resto_centena // 10
numero_unidade = resto_centena % 10

soma = num + ((numero_unidade * 100) + (numero_dezena * 10) + (numero_centena * 1))

print('SOMA = ', soma)
