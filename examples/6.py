from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

##@##
description = 'Create a scene with four rectangles, each with a different color.'
##@##

# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1000, 700), bg_color=cream_white)

# Create a red rectangle, place it at the top left, and add it to the scene
rectangle_1 = Rectangle(200, 100, color='red')
rectangle_1.place_shape_global((300, 200))
scene.add_shape(rectangle_1)

# Create a green rectangle, place it at the top right, and add it to the scene
rectangle_2 = Rectangle(200, 100, color='green')
rectangle_2.place_shape_global((700, 200))
scene.add_shape(rectangle_2)

# Create a blue rectangle, place it at the bottom left, and add it to the scene
rectangle_3 = Rectangle(200, 100, color='blue')
rectangle_3.place_shape_global((300, 500))
scene.add_shape(rectangle_3)


# Create a yellow rectangle, place it at the bottom right, and add it to the scene
rectangle_4 = Rectangle(200, 100, color='yellow')
rectangle_4.place_shape_global((700, 500))
scene.add_shape(rectangle_4)