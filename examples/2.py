<<<<<<< HEAD
from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

##@##
description = 'Create a scene with a red rectangle to the right'
##@##

=======
#@# Prompt
prompt = 'Create a scene with a green triangle, a red triangle, and a blue triangle.'
#@#
>>>>>>> origin/main

# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1000, 700), bg_color=cream_white)

<<<<<<< HEAD
# Create a red rectangle, place it to the right, and add it to the scene
rectangle = Rectangle(200, 100, color='red')
rectangle.place_shape_global((800, 400))
scene.add_shape(rectangle)
=======

# Create an green Triangle, place it, and add it to the scene
triangle_1 = Triangle(100, color='green')
triangle_1.place_shape_global((600, 400))
scene.add_shape(triangle_1)

# Create a red Triangle, place it, and add it to the scene
triangle_2 = Triangle(100, color='red')
triangle_2.place_shape_global((400, 400))
scene.add_shape(triangle_2)

# Create a blue Triangle, place it, and add it to the scene
triangle_3 = Triangle(100, color='blue')
triangle_3.place_shape_global((500, 300))
scene.add_shape(triangle_3)
>>>>>>> origin/main
