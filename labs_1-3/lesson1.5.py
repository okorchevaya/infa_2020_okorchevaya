#import matplotlib.pyplot as plt
#x = [1, 2, 3, 4, 5]
#y = [0.99, 0.49, 0.35, 0.253, 0.18]
#plt.errorbar(x, y, xerr=0.05, yerr=0.1)
#plt.grid()
#plt.show()
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.01)
plt.plot(x, x**2, label=r'$f = x^2$')
plt.scatter(x, x**2 + np.random.randn(len(x))*x, s=0.3)
plt.fill_between(x, 1.3*x**2, 0.7*x**2, alpha=0.3)
plt.legend(loc='best')
plt.savefig('figure_fill_between.png')
 x = [1, 2, 3, 4, 5, 6]
 y = [1, 1.42, 1.76, 2, 2.24, 2.5]
 p, v = np.polyfit(x, y, deg=1, cov=True)

 >>> p
 array([0.28517032, 0.80720757])
 >>> v
 array([[0.00063242, -0.00221348],
[-0.00221348, 0.00959173]])
plt.show()
