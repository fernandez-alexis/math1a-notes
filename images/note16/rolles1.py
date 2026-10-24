import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

fig, ax1 = plt.subplots(figsize=(2, 2))

#Axis limits and grid
plt.ylim(0, 3)
ax1.set_xlim(0, 3) 
ax1.set_xticks(np.arange(0, 4, 1)) 
ax1.grid(True, which='major', color='lightgray', linestyle='-')
ax1.tick_params(axis='x', which='major', length=0, labelbottom=False) #Hides number ticks on xy-axis
ax1.tick_params(axis='y', which='major', length=0, labelleft=False)

#Add a,b to axis
tick_positions = [0.3, 2.4]
tick_labels = ['a', 'b']
ax1.set_xticks(tick_positions, minor=True)
ax1.set_xticklabels(tick_labels, minor=True)
ax1.tick_params(axis='x', which='minor', colors='blue', labelsize=12)

#Draw line
ax1.hlines(2, xmin=tick_positions[0], xmax=tick_positions[1], color="blue", linewidth=2.5)

ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.axhline(0, color="black", linewidth=0.8)
ax1.axvline(0, color="black", linewidth=0.8)

#Save plot as pdf and show
plt.savefig("images/note16/rolles1.pdf", format="pdf", bbox_inches="tight")
plt.show()