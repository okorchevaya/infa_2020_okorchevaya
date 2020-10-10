import turtle as tur
import numpy as np
tur.shape('turtle')

r=15
ag=6
n=np.pi*r**2/360*ag


for i in range(360//ag):
    tur.left(ag)
    tur.forward(n)





