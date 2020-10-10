import turtle as tur
tur.shape('turtle')

func_=input('Сколько лучей?: ')
y=eval(func_)

fun_=input('Длина лучей (в пикселях): ')
x=eval(fun_)

for i in range(y):
    tur.forward(x)
    tur.left(180)
    tur.forward(x)
    tur.left(180)
    tur.right(360/y)