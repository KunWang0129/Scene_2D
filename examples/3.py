<<<<<<< HEAD
from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

##@##
description = 'Create a scene with blue triangle at the top'
##@##

=======
#@# Prompt
prompt = 'Create a scene with five circles, each with a different color.'
#@#
>>>>>>> origin/main

# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1000, 700), bg_color=cream_white)

<<<<<<< HEAD
# Create a blue triangle, place it at the top, and add it to the scene
triangle = Triangle(200, color='blue')
triangle.place_shape_global((500, 200))
scene.add_shape(triangle)
=======

# Create an blue circe, place it and add it to the scene
circle_1 = Circle(50, color='blue')
circle_1.place_shape_global((600, 400))
scene.add_shape(circle_1)

# Create a red circe, place it and add it to the scene
circle_2 = Circle(50, color='red')
circle_2.place_shape_global((400, 400))
scene.add_shape(circle_2)

# Create a green circe, place it and add it to the scene
circle_3 = Circle(50, color='green')
circle_3.place_shape_local(circle_1, 'left')
scene.add_shape(circle_3)

# Create a yellow circe, place it and add it to the scene
circle_4 = Circle(50, color='yellow')
circle_4.place_shape_local(circle_2, 'right')
scene.add_shape(circle_4)

# Create a purple circe, place it and add it to the scene
circle_5 = Circle(50, color='purple')
circle_5.place_shape_local(circle_3, 'above')
scene.add_shape(circle_5)


# Create a orange circe, place it and add it to the scene
circle_6 = Circle(50, color='orange')
circle_6.place_shape_local(circle_4, 'below')
scene.add_shape(circle_6)
>>>>>>> origin/main
