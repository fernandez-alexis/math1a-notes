import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

#Linear Function
fig, ax1 = plt.subplots(figsize=(2, 2))

x1 = np.linspace(-3, 3, 100)

m = 3
b = 2
y1 = m*x1 + b

ax1.plot(x1, y1, label="y = 3x + 2", color="black", linewidth=2)
plt.plot(0, 2, 'ro')
plt.plot([2, 2], [5, 8], color="blue", linestyle='-', label="m")
plt.plot([1, 2], [5, 5], color="blue", linestyle='-')

ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))

ax1.set_title("Linear Function")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid(True, alpha=0.3)
ax1.axhline(0, color="black", linewidth=0.8)
ax1.axvline(0, color="black", linewidth=0.8)

plt.show()