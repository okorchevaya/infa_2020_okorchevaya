import turtle as tur
import mathtur.shape("turtle")

m=3
n=0
x=0
l=10
tur.goto(0,0)
while x<10:
    tur.left(90+180/m)
    tur.forward(10+10*n)
    
    for i in range (m-1):
        tur.left(360/m)
        tur.forward(10+10*n)
    tur.right(90-180/m)
    tur.penup()
    tur.goto(l,0)
    tur.pendown()
    n=n+1
    m=m+1
    x=x+1
    l=l+10