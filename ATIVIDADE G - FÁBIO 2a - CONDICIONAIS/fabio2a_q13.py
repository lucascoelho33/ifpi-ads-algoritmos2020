#13. Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são
#diferentes.

def main():

    n1 = int(input())
    n2 = int(input())
    n3 = int(input())
    n4 = int(input())
    n5 = int(input())

    maior = 0
    menor = 0

    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        maior = n1
    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        maior = n2
    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        maior = n3
    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        maior = n4
    elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        maior = n5


    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        menor = n1
    elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
        menor = n2
    elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
        menor = n3
    elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
        menor = n4
    elif n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
        menor = n5

    print('%d é o maior número'% maior)
    print('%d é o menor número'% menor)

main()


    
