import matplotlib.pyplot as plt
import numpy as np


plt.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
plt.plot([1,2,3,4], [0,0,0,0])
a=[1,2,3,4]
b=[1,4,6,3]
plt.plot(a,b)
plt.set_xlabel('x label')  # Add an x-label to the axes.
plt.set_ylabel('y label')  # Add a y-label to the axes.
plt.set_title("Simple Plot")  # Add a title to the axes.
plt.legend()  # Add a legend.
plt.show()