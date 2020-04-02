#21. Leia uma temperatura em °F, calcule e escreva a equivalente em °C.
#(t°C = (5 * t°F - 160) / 9).



def main():


    temperatura_f = float(input('Temperatura em °F: '))

    temperatura_c = (5 * temperatura_f - 160) / 9


    print('A temperatura em °C é %.1f °C'% temperatura_c)



main()


    
