##@##
description =Create a scene with a blue sky and scattered white clouds.
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the sky
sky = Rectangle(width=800, height=600, color='lightblue')
sky.place_shape_global((400, 300))
scene.add_shape(sky)

# Create the clouds
cloud1 = Circle(radius=80, color='white')
cloud1.place_shape_global((200, 200))
scene.add_shape(cloud1)

cloud2 = Circle(radius=100, color='white')
cloud2.place_shape_global((500, 150))
scene.add_shape(cloud2)

cloud3 = Circle(radius=90, color='white')
cloud3.place_shape_global((400, 250))
scene.add_shape(cloud3)

cloud4 = Circle(radius=70, color='white')
cloud4.place_shape_global((300, 350))
scene.add_shape(cloud4)

cloud5 = Circle(radius=60, color='white')
cloud5.place_shape_global((600, 300))
scene.add_shape(cloud5)

# Render the scene
scene.render('scene.png')
scene.render(filename='output.png')