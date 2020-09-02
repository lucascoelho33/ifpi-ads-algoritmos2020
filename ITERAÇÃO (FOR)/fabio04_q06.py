# 6. Escreva a tabuada dos números de 1 a 10.

def main():

    for i in range(1, 10+1):
        for j in range(10+1):
            prod = i * j
            print(f'{i} x {j} = {prod}')


main()

        
