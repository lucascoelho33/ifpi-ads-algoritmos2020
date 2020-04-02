def main():

    salario = float(input('Digite o salário: '))

    
    ir = calcular_ir(salario)
    ir_atual = calcular_ir_atual(salario)
    
    print('Pela tabela atual o imposto custará R$ %.2f'% ir)
    print('Pela tabela ajustada o imposto deveria ser R$ %.2f'% ir_atual)


def calcular_ir(salario):

    imposto = 0

    if salario > 4664.68:
        renda_tributar = salario - 4664.68
        salario = 4664.68
        imposto += renda_tributar * (27.5 / 100)

    if salario >= 3751.05:
        renda_tributar = salario - 3751.05
        salario = 3751.05
        imposto += renda_tributar * (22,5 / 100)

    if salario >= 2826.66:
        renda_tributar = salario - 2826.66
        salario = 2826.66
        imposto += renda_tributar * (15 / 100)

    if salario >= 1903.99:
        renda_tributar = salario - 1903.99
        salario = 1903.99
        imposto += renda_tributar * (7,5 / 100)

    return imposto

def calcular_ir_atual(salario):

    imposto = 0

    if salario > 4664.68:
        renda_tributar = salario - 2826.65
        salario = 2826.65
        imposto += renda_tributar * (27,5 / 100)

    if salario >= 3751.05:
        renda_tributar = salario - 3751.05
        salario = 3751.05
        imposto += renda_tributar * (22,5 / 100)

    if salario >= 2826.66:
        renda_tributar = salario - 2826.66
        salario = 2826.66
        imposto += renda_tributar * (15 / 100)

    if salario >= 1903.99:
        renda_tributar = salario - 1903.99
        salario = 1903.99
        imposto += renda_tributar * (7,5 / 100)

    return imposto

if __name__== '__main__':
    main()
    

        
        
