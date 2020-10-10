import turtle as tur
import numpy as np
tur.shape('turtle')
tur.speed(9)

tur.left(90)
        
def arch(halfr):              
    ag=6
    n=(np.pi*halfr**2/180*ag)
    for i in range(180//ag):
        tur.left(ag)
        tur.forward(n)
        
while 2>1:
    arch(10)
    arch(5)