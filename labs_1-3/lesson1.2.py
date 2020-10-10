import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5, 5.01, 0.001)
plt.plot(x,x**2-x-6)
y=np.arange(-5, 5.01, 0.001)
plt.plot(y,y*0)
plt.show()
