#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


"""
x = np.linspace(0,5,11)
y = x ** 2
figure = plt.figure()
axes_1 = figure.add_axes([0.1,0.1,0.8,0.8])

fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x,y)
axes[0].set_title("plotting zero position")


axes[1].plot(y,x)
axes[1].set_title("plotting one position")
plt.show()
"""


# using numpy
x = np.arange(0,100)
y = x*2
z = x**2
"""
figure = plt.figure()
axes  = figure.add_axes([0,0,1,1])
axes.plot(x,y)
axes.set_title("plotting")
axes.set_xlabel("axis")
axes.set_ylabel("ordenate")
plt.show()
"""

# solutions part

#figure = plt.figure()
#axes = figure.add_axes([0,0,1,1])
#axes.plot(x,y)


figure = plt.figure()
ax1 = figure.add_axes([0,0,1,1])
ax2 = figure.add_axes([0.2,.5,.2,.5])
ax1.plot(x,y)
ax2.plot(x,y)
plt.show()


































