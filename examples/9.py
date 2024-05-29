##@##
description =Create a scene with three fluffy clouds floating in a clear sky.
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='lightblue')

# Create the clouds
cloud1 = Circle(radius=100, color='white')
cloud1.place_shape_global((200, 150))
scene.add_shape(cloud1)

cloud2 = Circle(radius=120, color='white')
cloud2.place_shape_global((400, 250))
scene.add_shape(cloud2)

cloud3 = Circle(radius=90, color='white')
cloud3.place_shape_global((600, 300))
scene.add_shape(cloud3)

# Render the scene
scene.render('scene.png')
scene.render(filename='output.png')