#7. Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele
# corresponde.

minutos = int(input('Minutos: '))

dias = minutos // 1440
horas = (minutos // 1440) % 24
minutos2 = (minutos % 1440) % 24

print('Corresponde a %d dias,%d horas e %d minutos'%(dias,horas,minutos2))
