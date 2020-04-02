#3. Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

dias = int(input('Dias: '))

semanas = dias // 7
dias2 = (dias // 7) + dias

print('Corresponde a %d semanas e %d dias'%(semanas,dias2))
