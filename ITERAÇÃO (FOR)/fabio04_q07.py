# 7. Leia um número N, some todos os números
# inteiros entre 1 e N e escreva o resultado obtido.

def main():

    n = int(input('N: '))
    soma = 0

    for i in range(1, n):
        soma += i

    print(soma)



main()


        
