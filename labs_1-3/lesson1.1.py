import numpy as np

for x in [1, 10, 1000]:
    a=(np.e**1)/(np.sin(x)+ 1)
    b=(5/4+1/((x**1)*5)) 
    print(np.log(a/b)/np.log(1+x**2))
    