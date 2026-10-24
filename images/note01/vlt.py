import matplotlib.pyplot as plt
import numpy as np

#Font to match LaTeX
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "axes.labelsize": 10,    
    "font.size": 10,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9
})

#Creates two side-by-side plots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(4, 2))

#Plot 1: Parabola - Function
x1 = np.linspace(0, 4, 100)
y1 = (x1-2)**2

ax1.plot(x1, y1, label="y = x^2 (Parabola)", color="blue", linewidth=2)

#Vertical line
test_x = 3
ax1.axvline(
    x=test_x, color="red", linestyle="--", label=f"Vertical Line at x = {test_x}"
)

ax1.set_title("This is a function.")
ax1.set_ylim(0,4)
ax1.set_xlim(0, 4) 
ax1.set_xticks(np.arange(0, 4, 1)) 
ax1.set_yticks(np.arange(0, 4, 1))
ax1.grid(True, which='major', color='lightgray', linestyle='-')
ax1.axhline(0, color="black", linewidth=0.8)
ax1.tick_params(axis='x', which='major', length=0, labelbottom=False) #Hides number ticks on xy-axis
ax1.tick_params(axis='y', which='major', length=0, labelleft=False)

#Plot 2: Sideways Parabola - Not a Function
y2 = np.linspace(-3, 3, 100)
x2 = y2**2

ax2.plot(x2, y2, label="x = y^2 (Parabola)", color="blue", linewidth=2)

#Vertical line
test_x = 1.5
ax2.axvline(
    x=test_x, color="red", linestyle="--", label=f"Vertical Line at x = {test_x}"
)

ax2.set_title("This is not a function.")
ax2.set_ylim(-2,2)
ax2.set_xlim(0, 4) 
ax2.set_xticks(np.arange(0, 4, 1)) 
ax2.set_yticks(np.arange(-2, 2, 1))
ax2.grid(True, which='major', color='lightgray', linestyle='-')
ax2.axhline(0, color="black", linewidth=0.8)
ax2.tick_params(axis='x', which='major', length=0, labelbottom=False) #Hides number ticks on xy-axis
ax2.tick_params(axis='y', which='major', length=0, labelleft=False)
ax2.axvline(0, color="black", linewidth=0.8)

#Save figure as pdf and show
plt.savefig("images/note01/vlt.pdf", format="pdf", bbox_inches="tight")
plt.show()