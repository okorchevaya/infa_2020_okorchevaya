#import numpy as np
#import matplotlib.pyplot as plt
#y=eval(input("Create function"))
#print(y)
#plt.show()
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10, 10.01, 0.01)
func_=input('give me func: ')
print(func_)
y=eval(func_)
with plt.xkcd():
    plt.plot(x,y)
    plt.show()
