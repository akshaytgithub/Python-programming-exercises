import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,10)
y = x

fig , ax = plt.subplots()
ax.plot(x,y,'bs')
ax.set_xlabel("x-axis")
ax.set_ylabel("y-axis")
ax.set_title("line plot")

plt.show()