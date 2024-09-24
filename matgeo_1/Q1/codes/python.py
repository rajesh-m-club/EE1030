import matplotlib.pyplot as plt

# Function to read the dividing point from the text file
def read_dividing_point(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Extract the coordinates from the first line
        coord_line = lines[0].strip().split(": ")[1]
        x, y = map(float, coord_line.strip("()").split(", "))
        return x, y

# Read the dividing point from the file
dividing_point_file = "dividing_point.txt"
x_div, y_div = read_dividing_point(dividing_point_file)

# Original points P and Q
x1, y1 = 7, -6  # Point P
x2, y2 = 3, 4   # Point Q

# Function to determine the quadrant of the point
def find_quadrant(x, y):
    if x > 0 and y > 0:
        return "First Quadrant"
    elif x < 0 and y > 0:
        return "Second Quadrant"
    elif x < 0 and y < 0:
        return "Third Quadrant"
    elif x > 0 and y < 0:
        return "Fourth Quadrant"
    elif x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "Y-Axis"
    else:
        return "X-Axis"

# Determine the quadrant of the dividing point
quadrant = find_quadrant(x_div, y_div)

# Plotting the points and the line segment
plt.figure(figsize=(8, 8))
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Plot points P and Q
plt.scatter([x1, x2], [y1, y2], color='blue', label='Points P and Q')

# Plot the dividing point
plt.scatter(x_div, y_div, color='red', label=f'Dividing Point ({x_div:.2f}, {y_div:.2f})', zorder=5)

# Draw line PQ
plt.plot([x1, x2], [y1, y2], color='gray', linestyle='--', label='Line PQ')

# Add labels to the points
plt.text(x1, y1, f'P({x1},{y1})', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(x2, y2, f'Q({x2},{y2})', fontsize=12, verticalalignment='top', horizontalalignment='right')
plt.text(x_div, y_div, f'({x_div:.2f}, {y_div:.2f})', fontsize=12, verticalalignment='top', horizontalalignment='left')

# Display the quadrant
plt.title(f"Dividing Point lies in the {quadrant}")

# Set the x and y limits
plt.xlim(min(x1, x2, x_div) - 2, max(x1, x2, x_div) + 2)
plt.ylim(min(y1, y2, y_div) - 2, max(y1, y2, y_div) + 2)

# Add grid, legend, and show the plot
plt.grid(True)
plt.legend()
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

