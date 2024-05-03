from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

##@##
description = 'Create a scene with an orange circle, and arrange four blue rectangles.'
##@##


# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1024, 768), bg_color=cream_white)


# Create an orange circle, place it, and add it to the scene
circle = Circle(100, color='orange')
circle.place_shape_global((600, 400))
scene.add_shape(circle)

# Create blue rectangles, place it around the circle, and add it to the scene
# The rectangles are placed to the left, right, above, and below the circle
rectangle_1 = Rectangle(160, 80, color='blue', rotation=90)
rectangle_1.place_shape_local(circle, 'left')
scene.add_shape(rectangle_1)

rectangle_3 = Rectangle(160, 80, color='blue', rotation=90)
rectangle_3.place_shape_local(circle, 'right')
scene.add_shape(rectangle_3)

rectangle_2 = Rectangle(160, 80, color='blue', rotation=0)
rectangle_2.place_shape_local(circle, 'above')
scene.add_shape(rectangle_2)

rectangle_4 = Rectangle(160, 80, color='blue', rotation=0)
rectangle_4.place_shape_local(circle, 'below')
scene.add_shape(rectangle_4)