import turtle as tur
import numpy as np
tur.shape('turtle')
tur.speed(0)

r=8    
def circle(r):                  #функция
    ag=6
    n=np.pi*r**2/360*ag
    for i in range(360//ag):
        tur.left(ag)
        tur.forward(n)
while 2>1:      
    circle(r)
    tur.left(180)
    circle(r)
    r=r+2