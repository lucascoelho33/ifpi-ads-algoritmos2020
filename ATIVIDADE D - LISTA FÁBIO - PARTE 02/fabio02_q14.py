#14. Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

idade_dias = int(input('Idade: '))

anos = idade_dias // 365
resto = idade_dias % 365
meses = resto // 30
dias = resto % 30

print('Sua idade corresponde a %d anos, %d meses e %d dias'%(anos,meses,dias))
