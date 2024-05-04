from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

##@##
description = 'Create a scene with a red rectangle to the right'
##@##


# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1000, 700), bg_color=cream_white)

# Create a red rectangle, place it to the right, and add it to the scene
rectangle = Rectangle(200, 100, color='red')
rectangle.place_shape_global((800, 400))
scene.add_shape(rectangle)