# 5. Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele
# corresponde.

horas = int(input('Horas: '))

semanas = horas // 168
dias = (horas % 168) // 24
horas2 = (horas % 168) % 24

print('Corresponde a %d semanas, %d dias e %d horas'%(semanas,dias,horas2))
