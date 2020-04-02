#5. Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é sempre pelo mais barato.

def main():

    p1 = float(input())
    p2 = float(input())
    p3 = float(input())

    if p1 < p2 and p1 < p3:
        print('O primeiro produto é o mais barato')
    elif p2 < p1 and p2 < p3:
        print('O segundo produto é o mais barato')
    else:
        print('O terceiro produto é o mais barato')



main()
