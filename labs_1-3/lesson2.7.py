import turtle as tur
tur.shape('turtle')
tur.speed(0)

n=0.001

for i in range(360*10):
    tur.right(1)
    tur.forward(n)
    n=n+0.001
    

