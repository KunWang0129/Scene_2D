from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

##@##
description = 'Create a scene with a green circle, with a red circle to the left, and a blue circle to the right.'
##@##

# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1000, 700), bg_color=cream_white)

# Create a green circle, place it at the center, and add it to the scene
green_circle = Circle(200, color='green')
green_circle.place_shape_global((500, 350))
scene.add_shape(green_circle)

# Create a red circle, place it to the left, and add it to the scene
red_circle = Circle(100, color='red')
red_circle.place_shape_local(green_circle, 'left')
scene.add_shape(red_circle)

# Create a blue circle, place it to the right, and add it to the scene
blue_circle = Circle(100, color='blue')
blue_circle.place_shape_local(green_circle, 'right')
scene.add_shape(blue_circle)