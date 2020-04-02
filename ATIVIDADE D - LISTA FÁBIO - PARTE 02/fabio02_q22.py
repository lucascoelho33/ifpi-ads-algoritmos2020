valor = int(input('Digite o valor a ser retirado: '))

nota_50 = valor // 50
resto = valor % 50
nota_10 = resto // 10
resto2 = resto % 10
nota_5 = resto2 // 5
nota_1 = resto % 5

print('%d notas de 50, %d notas de 10, %d notas de 5 e %d notas de 1'% (nota_50, nota_10, nota_5, nota_1))
