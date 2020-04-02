#6. Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

meses = int(input('Meses: '))

anos = meses // 12
meses2 = meses % 12

print('Corresponde a %d anos e %d meses'%(anos, meses2))
