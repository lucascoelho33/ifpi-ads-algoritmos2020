#13. Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

anos = int(input('Anos: '))
meses = int(input('Meses: '))
dias = int(input('Dias: '))

anos_dias = anos * 365
meses_dias = meses * 30
dias_ao_todo = anos_dias + meses_dias + dias

print('A idade da pessoa em dias é %d'% dias_ao_todo,'dias')
