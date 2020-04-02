#22. Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:
#hora e minuto). Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
#máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia
#seguinte.

def main():

    hora_inicio = int(input())
    minuto_inicio = int(input())
    hora_fim = int(input())
    minuto_fim = int(input())

    if minuto_inicio <= minuto_fim:
        minutos = minuto_inicio - minuto_fim
    if hora_fim < hora_inicio:
        horas = (hora_fim + 24) - hora_inicio
        if minuto_inicio > minuto_fim:
            horas = horas - 1
            minutos = (minuto_fim + 60) - minuto_inicio
        elif minuto_inicio <= minuto_fim:
            minutos = minuto_fim - minuto_inicio
    elif hora_inicio < hora_fim:
        horas = hora_fim - hora_inicio
        if minuto_inicio > minuto_fim:
            horas = horas - 1
            minutos = (minuto_fim + 60) - minuto_inicio
        elif minuto_inicio <= minuto_fim:
            horas = horas + 1
            minutos = minuto_fim - minuto_inicio
    print('O jogo teve a duração de %d horas e %d minutos'% (horas, minutos))



main()
        
