##@##
description =Create a scene with a sun in the sky and several clouds.
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the sun
sun = Circle(radius=100, color='yellow')
sun.place_shape_global((650, 150))
scene.add_shape(sun)

# Create the clouds
# Large cloud in the upper-left
cloud1 = Circle(radius=120, color='white')
cloud1.place_shape_global((200, 150))
scene.add_shape(cloud1)

# Medium cloud in the upper-center
cloud2 = Circle(radius=100, color='white')
cloud2.place_shape_global((400, 200))
scene.add_shape(cloud2)

# Small cloud in the upper-right, to the left of the sun
cloud3 = Circle(radius=80, color='white')
cloud3.place_shape_global((550, 150))
scene.add_shape(cloud3)

# Medium cloud in the center-left
cloud4 = Circle(radius=90, color='white')
cloud4.place_shape_global((200, 300))
scene.add_shape(cloud4)

# Two small clouds in the lower-right
cloud5 = Circle(radius=70, color='white')
cloud5.place_shape_global((600, 450))
scene.add_shape(cloud5)

cloud6 = Circle(radius=60, color='white')
cloud6.place_shape_global((700, 500))
scene.add_shape(cloud6)

# Render the scene
scene.render('scene.png')
scene.render(filename='output.png')
scene.render(filename='output.png')