import turtle
import random
ventana = turtle.Screen()
ventana.title("proyecto")
ventana.bgcolor("gray")

jugador1= turtle.Turtle()
jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("green","green")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)


jugador2= turtle.Turtle()
jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("red","red")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)



jugador1.penup()
jugador1.goto(200,200)
jugador1.pendown()
jugador1.circle(40)
jugador1.penup()
jugador1.goto(-200,200)
jugador1.showturtle()


jugador2.penup()
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)
jugador2.penup()
jugador2.goto(-200,-200)
jugador2.showturtle()

dado = [1,2,3,4,5,6]

for i in range(20):
    if jugador1.pos() >= (200,200):
        print("La tortuga verde ha ganado")
        break
    elif jugador2.pos() >= (200,-200):
     print("el jugador rojo ha ganado")
     break
    else: 
        turno = input("PRESIONA LA TECLA ENTER PARA AVANZAR")
        turno = random.choice(dado)
        print("tu numero es: ", turno, "\nAvanzas: ", turno*20)
        jugador1.pendown()
        jugador1.forward(20*turno)

        turno2 = input("PRESIONA LA TECLA ENTER PARA AVANZAR")
        turno2 = random.choice(dado)
        print("tu numero es: ", turno, "\nAvanzas: ", turno*20)
        jugador2.pendown()
        jugador2.forward(20*turno)

turtle.done()
