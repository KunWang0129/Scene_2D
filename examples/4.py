from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

##@##
description = 'Create a scene with two red circles'
##@##


# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1000, 700), bg_color=cream_white)


# Create red circles and place them in the scene
circle_1 = Circle(100, color='red')
circle_1.place_shape_global((300, 300))
scene.add_shape(circle_1)

circle_2 = Circle(100, color='red')
circle_2.place_shape_global((700, 300))
scene.add_shape(circle_2)