#20. Leia uma temperatura em °C, calcule e escreva a equivalente em °F.
#(t°F = (9 * t°C + 160) / 5).



def main():


    temperatura = int(input('Digite uma temperatura em C°: '))

    temperatura_f = (9 * temperatura + 160) / 5


    print('Temperatura em °F: ', temperatura_f,'°F')



main()


    
