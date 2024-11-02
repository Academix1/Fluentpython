import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation

# Load Excalidraw JSON data
file_path = 'asdf.json'
with open(file_path, 'r') as f:
    data = json.load(f)

# Parse the JSON data
elements = data['elements']
rectangles = [el for el in elements if el['type'] == 'rectangle']
arrow = next(el for el in elements if el['type'] == 'arrow')

# Set up figure and axis with adjusted limits
fig, ax = plt.subplots()
ax.set_xlim(10000, 10600)
ax.set_ylim(108800, 109200)
ax.set_aspect('equal')
ax.set_facecolor(data['appState']['viewBackgroundColor'])

# Initialize elements for animation
rect_patches = []
for rect in rectangles:
    patch = patches.FancyBboxPatch(
        (rect['x'], rect['y']), 
        rect['width'], 
        rect['height'], 
        linewidth=rect['strokeWidth'], 
        edgecolor=rect['strokeColor'], 
        facecolor=rect['backgroundColor'],
        boxstyle="round,pad=0.1"  # Rounded corners
    )
    rect_patches.append(patch)
    ax.add_patch(patch)

# Initialize arrow line
arrow_line, = ax.plot([], [], color=arrow['strokeColor'], linewidth=arrow['strokeWidth'])

# Function to update frames
def animate(i):
    if i < len(rect_patches):
        rect_patches[i].set_visible(True)
    else:
        # Animate the arrow line segment by segment
        start_x, start_y = arrow['x'], arrow['y']
        end_x = start_x + arrow['points'][i - len(rect_patches)][0]
        end_y = start_y + arrow['points'][i - len(rect_patches)][1]
        arrow_line.set_data([start_x, end_x], [start_y, end_y])

# Hide rectangles initially
for rect_patch in rect_patches:
    rect_patch.set_visible(False)

# Animate
ani = FuncAnimation(fig, animate, frames=len(rect_patches) + len(arrow['points']), interval=200, repeat=False)

# Display animation
plt.show()
