def main():

    salario = float(input())

    if salario <= 280:
        aumento = (salario * 20) / 100
        novo_salario = salario + aumento
        print('O salário antes do reajuste era de R$ {:2}'.format(salario))
        print('O percentual de aumento aplicado foi de 20%')
        print('O valor do aumento foi de R$ {:2}'.format(aumento))
        print('O novo salário após o aumento é de R$ {:2}'.format(novo_salario))
    elif salario > 280 and salario < 700:
        aumento = (salario * 15) / 100
        novo_salario = salario + aumento
        print('O salário antes do reajuste era de R$ {:2}'.format(salario))
        print('O percentual de aumento aplicado foi de 15%')
        print('O valor do aumento foi de R$ {:2}'.format(aumento))
        print('O novo salário após o aumento é de R$ {:2}'.format(novo_salario))
    elif salario > 700 and salario < 1500:
        aumento = (salario * 10) / 100
        novo_salario = salario + aumento
        print('O salário antes do reajuste era de R$ {:2}'.format(salario))
        print('O percentual de aumento aplicado foi de 10%')
        print('O valor do aumento foi de R$ {:2}'.format(aumento))
        print('O novo salário após o aumento é de R$ {:2}'.format(novo_salario))
    elif salario > 1500:
        aumento = (salario * 5) / 100
        novo_salario = salario + aumento
        print('O salário antes do reajuste era de R$ {:2}'.format(salario))
        print('O percentual de aumento aplicado foi de 5%')
        print('O valor do aumento foi de R$ {:2}'.format(aumento))
        print('O novo salário após o aumento é de R$ {:2}'.format(novo_salario))

if __name__=='__main__':
    main()

