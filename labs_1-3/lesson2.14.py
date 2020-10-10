import turtle as tur
tur.shape('turtle')

tur.speed(1)

n=input('Сколько лучей звезды?: ')
y=eval(n)
 

for i in range(y): 
    tur.forward(50)
    tur.left(180)
    tur.left(180/y)
    tur.forward(50)
