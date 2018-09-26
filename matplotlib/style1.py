import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(0,2*np.pi,0.1)
x = np.linspace(0,2*np.pi,100)

y=np.sin(x)
fig,(ax1,ax2)=plt.subplots(1,2)
ax1.set_ylabel("sin")
ax1.plot(x,y)

ax2.set_title("cos")
ax2.plot(x,np.cos(x))

plt.show()