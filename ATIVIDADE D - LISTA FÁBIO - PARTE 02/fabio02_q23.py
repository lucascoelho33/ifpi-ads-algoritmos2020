valor = float(input('Digite o valor: '))

entrada = (valor // 3) + (valor % 3)
prestacoes = valor // 3

print('A entrada vai ser de %.2fR$ e as duas prestações de %.2fR$'% (entrada, prestacoes))
