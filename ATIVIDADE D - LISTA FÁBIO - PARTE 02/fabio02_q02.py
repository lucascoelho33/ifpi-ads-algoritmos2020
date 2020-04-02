#2. Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

metros = int(input('Metros: '))

km = metros * 1000
m = (metros * 1000) + metros

print('Corresponde a %d km e %.1f metros'% (km, m))
