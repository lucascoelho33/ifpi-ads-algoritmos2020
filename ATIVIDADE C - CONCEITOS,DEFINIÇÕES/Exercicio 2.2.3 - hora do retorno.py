#Entrada

hora_saida = 6
minuto_saida = 52


#Calculo

volta3 = 3 * (7 + (12 / 60))
volta2 = 2 * (8 + (15 / 60))
soma_voltas = volta3 + volta2
hora_minutos = (minuto_saida + (soma_voltas % 60)) // 60
minuto_chegada = int((minuto_saida + (soma_voltas % 60)) % 60)
hora_chegada = int(hora_saida + (soma_voltas // 60) + hora_minutos)

#Saida

print('Para o café da manhã chego %d horas e %d minutos'%(hora_chegada, minuto_chegada))
