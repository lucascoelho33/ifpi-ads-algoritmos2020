#21. Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
#maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
#contrario, é arredondado para o inteiro imediatamente inferior.

def main():

    num = float(input())

    resto = num % 2

    if resto >= 0.5:
        soma = num + 1
    else:
        diferenca = num - 1

main()
