def main():

    n = int(input('N° de eleitores: '))
    candidato_a = 0
    candidato_b = 0
    candidato_c = 0
    tot_nulo = 0
    tot_branco = 0
    cont = 1

    while n > 0:
        voto = int(input('Digite o código do candidato: '))
        if voto == 1:
            candidato_a += 1
        elif voto == 2:
            candidato_b += 1
        elif voto == 3:
            candidato_c += 1
        elif voto == 9:
            tot_nulo += 1
        n = n - 1

    print('Total de votos do candidato A: ',candidato_a)
    print('Total de votos do candidato B: ',candidato_b)
    print('Total de votos do candidato C: ',candidato_c)
    print('Total de votos nulos: ',tot_nulo)

    if candidato_a >= candidato_b and candidato_a >= candidato_c:
        print('Candidato A venceu')
    elif candidato_b >= candidato_a and candidato_b >= candidato_c:
        print('Candidato B venceu')
    elif candidato_c >= candidato_a and candidato_c >= candidato_b:
        print('Candidato C venceu')

main()

        
