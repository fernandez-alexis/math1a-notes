import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

fig, ax1 = plt.subplots(figsize=(2, 2))

#Axis limits and grid
plt.ylim(0, 4)
ax1.set_xlim(0, 4) 
ax1.set_xticks(np.arange(0, 5, 1)) 
ax1.grid(True, which='major', color='lightgray', linestyle='-')
ax1.tick_params(axis='x', which='major', length=0, labelbottom=False) #Hides number ticks on xy-axis
ax1.tick_params(axis='y', which='major', length=0, labelleft=False)

#Add a,b to axis
tick_positions = [0.3, 3.4]
tick_labels = ['a', 'b']
ax1.set_xticks(tick_positions, minor=True)
ax1.set_xticklabels(tick_labels, minor=True)
ax1.tick_params(axis='x', which='minor', colors='blue', labelsize=12)

#Peak
h,k = 2.4, 3
y_end = 1.5 #f(a)=f(b) condition of Rolle's

# Mathematically calculate coefficients so they hit y_end at the boundaries
a_left = (y_end - k) / (tick_positions[0] - h)**2
a_right = (y_end - k) / (tick_positions[1] - h)**2

#Generate the curves over the strict interval
x_left = np.linspace(tick_positions[0], h, 100)
y_left = a_left * (x_left - h)**2 + k

x_right = np.linspace(h, tick_positions[1], 100)
y_right = a_right * (x_right - h)**2 + k
ax1.plot(x_left, y_left, color='blue', linewidth=2.5, label='Flat-End Uneven Parabola')
ax1.plot(x_right, y_right, color='blue', linewidth=2.5)

#Draw line
ax1.hlines(3.05, xmin=1.9, xmax=2.9, color="cyan", linewidth=1)

ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.axhline(0, color="black", linewidth=0.8)
ax1.axvline(0, color="black", linewidth=0.8)

#Save plot as pdf and show
plt.savefig("images/note16/rolles2.pdf", format="pdf", bbox_inches="tight")
plt.show()