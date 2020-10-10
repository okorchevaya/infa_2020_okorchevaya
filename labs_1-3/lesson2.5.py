import turtle as tur
tur.shape('turtle')
tur.speed(6)

n=10
x=6
step=5

for i in range(n):
     
    for l in range(4):
        tur.forward(x)
        tur.left(90)
   
    tur.penup()
    tur.right(90)   
    tur.forward(step)
    tur.right(90)
    tur.forward(step)
    tur.right(180)
    tur.pendown()

    x=x+2*step
