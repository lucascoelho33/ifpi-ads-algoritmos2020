import turtle
bob = turtle.Turtle()
from math import pi



def main():
    bob = turtle.Turtle(shape='turtle')
    raio = 100
    angulo= 90


    #quadrado(bob, 100)
    #triangulo(bob, 120)
    #circulo(bob, 140)
    #arco(bob, raio, angulo)
    #petala(bob, 100, angulo)
    flor(bob, 300, qtd_petalas=25)

print(bob)
turtle.mainloop()
