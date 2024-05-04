from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

##@##
description = 'Create a scene with an orange circle in the middle'
##@##


# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1000, 700), bg_color=cream_white)


# Create an orange circle, place it, and add it to the scene
circle = Circle(100, color='orange')
circle.place_shape_global((500, 350))
scene.add_shape(circle)