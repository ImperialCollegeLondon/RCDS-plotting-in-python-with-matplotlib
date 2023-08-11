# IMPORTANT NOTE: This file will not display an output in a Codespace environment

import matplotlib.pyplot as plt
import math

x = []
y = []

for i in range(1000):
  x.append(i * 100)
  y.append(math.sin(i * 0.01))

plt.plot(x,y)

# This command opens a new window showing the plot
plt.show()