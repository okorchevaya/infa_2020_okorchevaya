import turtle as tur
tur.shape('turtle')

#func_=input('Количество стоон правильного многоугольника: ')
#n=eval(func_)

n=3
angle=180*(n-2)/n

for i in range(3):
    tur.forward(50)
    tur.left(180-angle)