# 10. Leia LimiteSuperior e LimiteInferior e
# escreva todos os números ímpares entre os limites lidos.

def main():

    lim_inf = int(input('Limite Inferior: '))
    lim_sup = int(input('Limite Superior: '))

    for i in range(lim_inf, lim_sup):
        if i % 2 != 0:
            print(i)


main()

