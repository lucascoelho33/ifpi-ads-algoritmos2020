# 9. Leia LimiteSuperior e LimiteInferior e
# escreva todos os números pares entre os limites lidos.

def main():

    lim_inf = int(input('Limite Inferior: '))
    lim_sup = int(input('Limite Superior: '))

    for i in range(lim_inf, lim_sup+1):
        if i % 2 == 0:
            print(i)


main()

