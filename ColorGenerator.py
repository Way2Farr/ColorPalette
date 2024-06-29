import colorsys

import matplotlib.pyplot as plt

# Create a color wheel
color_wheel = [colorsys.hsv_to_rgb(hue / 360, 1, 1) for hue in range(360)]

def get_color(hue):
    return color_wheel[hue % 360]

# Relationship functions
def get_complementary(hue):
    return [(hue + 180) % 360]

def get_split_complementary(hue):
    return [(hue + 150) % 360, (hue + 210) % 360]

def get_analogous(hue):
    return [(hue + 30) % 360, (hue - 30) % 360]

def get_triadic(hue):
    return [(hue + 120) % 360, (hue + 240) % 360]

def get_square(hue):
    return [(hue + 90) % 360, (hue + 180) % 360, (hue + 270) % 360]

def get_tetradic(hue):
    return [(hue + 90) % 360, (hue + 180) % 360, (hue + 270) % 360]

# DFS implementation
def dfs(start_color, relationship_func, max_depth):
    visited = set()
    stack = [(start_color, 0)]
    palette = []

    while stack:
        current_color, depth = stack.pop()
        if current_color not in visited and depth <= max_depth:
            visited.add(current_color)
            palette.append(get_color(current_color))
            for neighbor in relationship_func(current_color):
                stack.append((neighbor, depth + 1))
    return palette

# Prompt user for inputs
try:
    start_color = int(input("Enter the starting color (0-359): "))
    relationship = input("Enter the relationship (complementary, split_complementary, analogous, triadic, square, tetradic): ")
    max_depth = int(input("Enter the maximum depth: "))

    # Determine the relationship function based on user input
    relationship_funcs = {
        "complementary": get_complementary,
        "split_complementary": get_split_complementary,
        "analogous": get_analogous,
        "triadic": get_triadic,
        "square": get_square,
        "tetradic": get_tetradic,
    }

    relationship_func = relationship_funcs.get(relationship)
    if relationship_func is None:
        print("Invalid relationship input. Please try again.")
        exit()

    # Generate the palette using DFS
    palette = dfs(start_color, relationship_func, max_depth)

    # Output palette using imshow
    plt.figure(figsize=(8, 2))
    plt.imshow([palette], aspect='auto')
    plt.axis('off')
    plt.show()

except ValueError:
    print("Invalid input. Please enter integer values for color and depth.")
