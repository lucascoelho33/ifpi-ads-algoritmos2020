# 11. Leia LimiteSuperior e LimiteInferior e
# escreva todos os números primos entre os limites lidos.

def main():

    lim_inf = int(input('Limite Inferior: '))
    lim_sup = int(input('Limite Superior: '))

    for i in range(lim_inf, lim_sup):
        if i % 2 == 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            print(i)


main()

