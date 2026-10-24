import matplotlib.pyplot as plt
import numpy as np

fig, ax1 = plt.subplots(figsize=(3, 3))

x1 = np.linspace(-3, 3, 100)
y1 = x1**2

ax1.plot(x1, y1, label="y = x^2 (Parabola)", color="blue", linewidth=2)

ax1.set_title("Quadratic Function")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid(True, alpha=0.3)
ax1.axhline(0, color="black", linewidth=0.8)
ax1.axvline(0, color="black", linewidth=0.8)

plt.savefig("images/note2/quadratic.pdf", format="pdf", bbox_inches="tight")
plt.show()