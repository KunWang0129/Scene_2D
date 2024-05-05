from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

##@##
description = 'Create a scene with a pair of rectangle and circle shapes, with circle placed above the rectangle.'
##@##


# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1000, 700), bg_color=cream_white)

# Create a rectangle, place it, and add it to the scene
rectangle = Rectangle(300, 100, color='blue')
rectangle.place_shape_global((500, 400))
scene.add_shape(rectangle)

# Create a circle, place it above the rectangle, and add it to the scene
circle = Circle(50, color='orange')
circle.place_shape_local(rectangle, 'above')
scene.add_shape(circle)