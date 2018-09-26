import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1);#generates x coordinates from 0 to 5 with interval of 0.1
y = np.sin(x)#generates corresponding y values
plt.plot(x, y)
plt.show()