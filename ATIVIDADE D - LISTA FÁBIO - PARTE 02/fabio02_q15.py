#15. Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o resultado em forma de fração.

numerador1 = int(input('Digite o numerador: '))
denominador1 = int(input('Digite o denominador: '))
numerador2 = int(input('Digite o segundo numerador: '))
denominador2 = int(input('Digite o segundo denominador: '))

denominador_comum = denominador1 * denominador2

soma = ((denominador_comum / denominador1) * numerador1) + ((denominador_comum / denominador2) * numerador2)

print('A soma das frações é {:.0f}/{}'.format(soma, denominador_comum))
