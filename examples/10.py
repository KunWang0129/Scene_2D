from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

##@##
description = 'Create a dark scene with a pair of rectangle.'
##@##


# Create a scene with a dark background
scene = Scene(size=(1000, 700), bg_color='grey')

# Create a pair of rectangles, place them, and add them to the scene
rectangle_1 = Rectangle(200, 100, color='blue')
rectangle_1.place_shape_global((300, 400))
scene.add_shape(rectangle_1)

rectangle_2 = Rectangle(200, 100, color='blue')
rectangle_2.place_shape_global((700, 400))
scene.add_shape(rectangle_2)