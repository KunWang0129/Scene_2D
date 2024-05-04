from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

##@##
description = 'Create a scene with blue triangle at the top'
##@##


# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1000, 700), bg_color=cream_white)

# Create a blue triangle, place it at the top, and add it to the scene
triangle = Triangle(200, color='blue')
triangle.place_shape_global((500, 200))
scene.add_shape(triangle)