import turtle as tur
import numpy as np
tur.shape('turtle')
tur.speed(8)
    
def circle(r):                  #функция
    ag=6
    n=np.pi*r**2/360*ag
    for i in range(360//ag):
        tur.left(ag)
        tur.forward(n)
m=1024
x=1 
while x<=m/2:
    circle(10)
    tur.left(180)
    circle(10)
    tur.right(360/m)
    x=x+1