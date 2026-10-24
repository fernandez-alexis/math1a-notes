import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

#Linear Function
fig, ax1 = plt.subplots(figsize=(2, 2))

ax1.axhline(2, color="blue")

# x1 = np.linspace(-3, 3, 100)
# y1 = 2

# ax1.plot(x1, y1, label="y = x + 2", color="black", linewidth=2)

ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))

ax1.set_title("Constant Function")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid(True, alpha=0.3)
ax1.axhline(0, color="black", linewidth=0.8)
ax1.axvline(0, color="black", linewidth=0.8)

plt.savefig("images/note2/constant.pdf", format="pdf", bbox_inches="tight")
plt.show()