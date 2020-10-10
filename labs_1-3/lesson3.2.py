import turtle as tur
tur.shape('turtle')
#cords or dots 
A=(0,0)
B=(0,-30)
C=(0,-60)
D=(30,-60)
E=(30,-30)
M=(30,0)
zero=[A, M, D, C, A]
one=[B, M, D]
two=[A, M, E, C, D]
three=[A, M, B, E, C]
four=[A, B, E, M, D]
five=[M, A, B, E, D,C]
six=[M, A, C, D, E, B]
seven=[A, M, C]
eight=[A, M, D, C, A, B, E]
nine=[E, B, A, M, D, C]
#writing function
def draw(Cords,delta_x, delta_y):
    tur.penup()
    tur.goto(delta_x, delta_y)
    tur.pendown()
    for i in Cords:
        tur.goto(i[0]+delta_x, i[1]) 
    tur.penup()


draw(one,0,-30)
draw(four, 40, 0)
draw(one,80,-30)
draw(seven,120,0)
draw(zero, 160, 0)
draw(zero, 200, 0)
