#8. Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.

num = int(input('Digite um número inteiro com 4 dígitos: '))

posicao4 = num // 1000
resto = num % 1000
posicao3 = resto // 100
resto2 = resto % 100
posicao2 = resto2 // 10
posicao1 = resto2 % 10
decimal = (posicao1 * 1) + (posicao2 * 2) + (posicao3 * 4) + (posicao4 * 8)

print('O número binário %d é equivalente ao decimal %d'% (num, decimal))

