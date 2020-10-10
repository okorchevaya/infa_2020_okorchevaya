import turtle as tur
import numpy as np
tur.shape('turtle')



def arch(halfr):                #функция
    ag=6
    n=(np.pi*halfr**2/180*ag)
    for i in range(180//ag):
        tur.left(ag)
        tur.forward(n)
    
        
        
tur.goto(-30,40)
tur.left(90)       #рот
tur.pendown()
tur.width(5)
tur.pencolor('coral')
arch(10)
tur.right(180)
