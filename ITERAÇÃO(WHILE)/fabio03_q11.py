# 11. Leia LimiteSuperior e LimiteInferior e
# escreva todos os números primos entre os limites lidos.

def main():

    lim_sup = int(input('Limite Superior: '))
    lim_inf = int(input('Limite Inferior: '))

    while lim_inf <= lim_sup:
        if lim_inf % 2 == 1:
            print(lim_inf)
        lim_inf = lim_inf + 1


main()
