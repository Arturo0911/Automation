#!/usr/bin/python3


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(0,5,11)
y = x ** 2
figure = plt.figure()
axes_1 = figure.add_axes([0.1,0.1,0.8,0.8])
#axes_1.plot(x,y)

fig, axes = plt.subplots(nrows=3, ncols=3)
#axes.plot(x,y)
plt.show()