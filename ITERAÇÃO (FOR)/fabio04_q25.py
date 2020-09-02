def main():

    n = int(input('N: '))
    cand_a = 0
    cand_b = 0
    cand_c = 0
    tot_nulo = 0
    tot_branco = 0

    for i in range(1, n+1):
        codigo = int(input('Código: '))

        if codigo == '1':
            cand_a += 1
        elif codigo == '2':
            cand_b += 1
        elif codigo == '3':
            cand_c += 1
        elif codigo == '9':
            tot_nulo += 1
        elif codigo == '0':
            tot_branco += 1


    print('Candidato A: ',cand_a)
    print('Candidato B: ',cand_b)
    print('Candidato C: ',cand_c)
    print('Total de votos nulos: ',tot_nulo)
    print('Total de votos brancos: ',tot_branco)

    if cand_a > cand_b and cand_a > cand_c:
        print('Candidato A venceu')
    elif cand_b > cand_a and cand_b > cand_c:
        print('Candidato B venceu')
    elif cand_c > cand_a and cand_c > cand_b:
        print('Candidato C venceu')

main()



    
        
