import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))

x1 = np.linspace(-3, 3, 100)
y1 = x1**2

ax1.plot(x1, y1, label="y = x^2 (Parabola)", color="blue", linewidth=2)

test_x = 1.5
ax1.axvline(
    x=test_x, color="red", linestyle="--", label=f"Vertical Line at x = {test_x}"
)

ax1.set_title("This is a function.")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid(True, alpha=0.3)
ax1.axhline(0, color="black", linewidth=0.8)
ax1.axvline(0, color="black", linewidth=0.8)

y2 = np.linspace(-3, 3, 100)
x2 = y2**2

ax2.plot(x2, y2, label="x = y^2 (Parabola)", color="blue", linewidth=2)

test_x = 1.5
ax2.axvline(
    x=test_x, color="red", linestyle="--", label=f"Vertical Line at x = {test_x}"
)

ax2.set_title("This is not a function.")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.grid(True, alpha=0.3)
ax2.axhline(0, color="black", linewidth=0.8)
ax2.axvline(0, color="black", linewidth=0.8)

plt.savefig("vlt.pdf", format="pdf", bbox_inches="tight")
plt.show()