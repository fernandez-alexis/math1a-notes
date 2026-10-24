import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "axes.labelsize": 11,     # Match your LaTeX font size (e.g., 10pt, 11pt, 12pt)
    "font.size": 11,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9
})

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(8, 2), sharex=True, sharey=True)

#Example 1
#Axis limits and grid
ax1.set_ylim(0,4)
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

#Draw line
ax1.hlines(2.3, xmin=tick_positions[0], xmax=tick_positions[1], color="blue", linewidth=2.5)

ax1.axhline(0, color="black", linewidth=0.8)
ax1.axvline(0, color="black", linewidth=0.8)


#Example 2 
#Axis limits and grid
ax2.grid(True, which='major', color='lightgray', linestyle='-')
ax2.tick_params(axis='x', which='major', length=0, labelbottom=False) #Hides number ticks on xy-axis
ax2.tick_params(axis='y', which='major', length=0, labelleft=False)

# #Add a,b to axis
ax2.tick_params(axis='x', which='minor', colors='blue', labelsize=12)

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
ax2.plot(x_left, y_left, color='blue', linewidth=2.5, label='Flat-End Uneven Parabola')
ax2.plot(x_right, y_right, color='blue', linewidth=2.5)

#Draw tangent line
ax2.hlines(3.05, xmin=1.9, xmax=2.9, color="cyan", linewidth=1)

ax2.axhline(0, color="black", linewidth=0.8)
ax2.axvline(0, color="black", linewidth=0.8)


#Example 3
#Axis limits and grid
plt.ylim(0, 4)
ax3.set_xlim(0, 4) 
ax3.set_xticks(np.arange(0, 5, 1)) 
ax3.grid(True, which='major', color='lightgray', linestyle='-')
ax3.tick_params(axis='x', which='major', length=0, labelbottom=False) #Hides number ticks on xy-axis
ax3.tick_params(axis='y', which='major', length=0, labelleft=False)

#Add a,b to axis
ax3.tick_params(axis='x', which='minor', colors='blue', labelsize=12)

a_pos, b_pos = tick_positions[0], tick_positions[1]
 
h1, k1 = 1.4, 3.6  # Peak
h2, k2 = 2.7, 0.6  # Valley
y_end = 2.5        # Height where the function starts at 'a' and ends at 'b'

# Midpoint between peak and valley
mid_x = (h1 + h2) / 2
mid_y = (k1 + k2) / 2

#Calculate Coefficients for Smooth Connections
a1 = (y_end - k1) / (a_pos - h1)**2       # Rises from 'a' to Peak
a2 = (mid_y - k1) / (mid_x - h1)**2       # Falls from Peak to Midpoint
a3 = (mid_y - k2) / (mid_x - h2)**2       # Falls from Midpoint to Valley
a4 = (y_end - k2) / (b_pos - h2)**2       # Rises from Valley to 'b'

#Generate the 4 Continuous Data Streams
x1 = np.linspace(a_pos, h1, 50)
y1 = a1 * (x1 - h1)**2 + k1

x2 = np.linspace(h1, mid_x, 50)
y2 = a2 * (x2 - h1)**2 + k1  

x3 = np.linspace(mid_x, h2, 50)
y3 = a3 * (x3 - h2)**2 + k2

x4 = np.linspace(h2, b_pos, 50)
y4 = a4 * (x4 - h2)**2 + k2

# Plot the complete curve segments seamlessly
for x_part, y_part in [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]:
    ax3.plot(x_part, y_part, color='blue', linewidth=2.5)

# Tangent lines
ax3.hlines(3.65, xmin=0.9, xmax=1.9, color="cyan", linewidth=1)
ax3.hlines(0.55, xmin=2.2, xmax=3.2, color="cyan", linewidth=1)


#Example 4
#Axis limits and grid
plt.ylim(0, 4)
ax4.set_xlim(0, 4) 
ax4.set_xticks(np.arange(0, 5, 1)) 
ax4.grid(True, which='major', color='lightgray', linestyle='-')
ax4.tick_params(axis='x', which='major', length=0, labelbottom=False) #Hides number ticks on xy-axis
ax4.tick_params(axis='y', which='major', length=0, labelleft=False)

#Add a,b to axis
ax4.tick_params(axis='x', which='minor', colors='blue', labelsize=12)

#Peak
h,k = 1.8, 1.3
y_end = 2.4 #f(a)=f(b) condition of Rolle's

# Mathematically calculate coefficients so they hit y_end at the boundaries
a_left = (y_end - k) / (tick_positions[0] - h)**2
a_right = (y_end - k) / (tick_positions[1] - h)**2

#Generate the curves over the strict interval
x_left = np.linspace(tick_positions[0], h, 100)
y_left = a_left * (x_left - h)**2 + k

x_right = np.linspace(h, tick_positions[1], 100)
y_right = a_right * (x_right - h)**2 + k
ax4.plot(x_left, y_left, color='blue', linewidth=2.5, label='Flat-End Uneven Parabola')
ax4.plot(x_right, y_right, color='blue', linewidth=2.5)

#Draw tangent line
ax4.hlines(1.25, xmin=1.3, xmax=2.3, color="cyan", linewidth=1)

#Save plot as pdf and show
plt.savefig("images/note16/rolles.pdf", format="pdf", bbox_inches="tight")
plt.show()