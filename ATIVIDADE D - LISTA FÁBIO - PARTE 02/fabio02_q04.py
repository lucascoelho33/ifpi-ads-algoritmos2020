#4. Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos
# segundos ele corresponde.

segundos = int(input('Segundos: '))

horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos2 = (segundos % 3600) % 60

print('Corresponde a %d horas, %d minutos e %d segundos'%(horas, minutos,segundos2))
