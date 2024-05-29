##@##
description =Create a scene with a grassy field and a blue sky with fluffy clouds.
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the grassy field
grass = Rectangle(width=800, height=300, color='green')
grass.place_shape_global((400, 450))
scene.add_shape(grass)

# Create the sky
sky = Rectangle(width=800, height=300, color='lightblue')
sky.place_shape_global((400, 150))
scene.add_shape(sky)

# Create the clouds
cloud1 = Circle(radius=50, color='white')
cloud1.place_shape_global((100, 100))
scene.add_shape(cloud1)

cloud2 = Circle(radius=70, color='white')
cloud2.place_shape_global((300, 150))
scene.add_shape(cloud2)

cloud3 = Circle(radius=60, color='white')
cloud3.place_shape_global((500, 120))
scene.add_shape(cloud3)

cloud4 = Circle(radius=40, color='white')
cloud4.place_shape_global((650, 180))
scene.add_shape(cloud4)

cloud5 = Circle(radius=45, color='white')
cloud5.place_shape_global((200, 200))
scene.add_shape(cloud5)

cloud6 = Circle(radius=55, color='white')
cloud6.place_shape_global((400, 250))
scene.add_shape(cloud6)

# Render the scene
scene.render('scene.png')
scene.render(filename='output.png')
scene.render(filename='output.png')