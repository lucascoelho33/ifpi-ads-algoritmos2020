# 8. Leia N , LimiteSuperior e LimiteInferior e
# escreva todos os múltiplos de N entre os limites lidos.

def main():

    n = int(input('N: '))
    lim_sup = int(input('Limite Superior: '))
    lim_inf = int(input('Limite Inferior: '))

    while lim_inf <= lim_sup:
        if lim_inf % n == 0:
            print(lim_inf)
        lim_inf = lim_inf + 1


main()

    
    
