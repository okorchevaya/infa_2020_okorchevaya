import turtle as tur
import numpy as np
tur.shape('turtle')

body=12                       #переменные 
eye=5
mouth=0.45

def circle(r):                  #функция
    ag=6
    n=np.pi*r**2/360*ag
    for i in range(360//ag):
        tur.left(ag)
        tur.forward(n)
        
def arch(halfr):                #функция
    ag=6
    n=(np.pi*halfr**2/180*ag)
    for i in range(180//ag):
        tur.left(ag)
        tur.forward(n)
            
tur.goto(0,0)
tur.begin_fill()        #тело
tur.color('gold')
circle(body)
tur.end_fill()
tur.penup()

tur.goto(25,70)         #правый глаз
tur.pendown()
tur.begin_fill()
tur.color('lavender')
circle(eye)
tur.end_fill()
tur.penup()

tur.goto(-25,70)        #левый глаз
tur.pendown()
tur.begin_fill()
tur.color('lavender')
circle(eye)
tur.end_fill()
tur.penup()

tur.goto(0,40)          #нос
tur.pendown()
tur.width(5)
tur.pencolor('black')
tur.left(90)
tur.forward(20)
tur.penup()

tur.goto(-25,40)
tur.right(180)       #рот
tur.pendown()
tur.width(5)
tur.pencolor('coral')
arch(5)
