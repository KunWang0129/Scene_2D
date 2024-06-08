##@##
description = 'Create a scene with a cloud and a sun.'
##@##

from utils.Shape import Circle, Rectangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the sky
sky = Rectangle(width=800, height=400, color='lightblue')
sky.place_shape_global((400, 200))
scene.add_shape(sky)

# Create the cloud
cloud_radius = 150
cloud = Circle(radius=cloud_radius, color='white')
cloud.place_shape_global((600, 200))
scene.add_shape(cloud)

# Create the sun
sun_radius = 75
sun = Circle(radius=sun_radius, color='yellow')
sun.place_shape_global((200, 150))
scene.add_shape(sun)

# Render the scene
scene.render('cloud_and_sun.png')
scene.render(filename='output.png')