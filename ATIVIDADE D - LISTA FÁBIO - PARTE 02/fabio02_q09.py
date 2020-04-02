#9. Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.

num = int(input('Digite um número inteiro de 3 dígitos: '))

numero_centena = num // 100
resto_centena = num % 100
numero_dezena = resto_centena // 10
numero_unidade = resto_centena % 10

diferenca = num - ((numero_unidade * 100) + (numero_dezena * 10) + (numero_centena * 1))

print('Diferença = ', diferenca)
