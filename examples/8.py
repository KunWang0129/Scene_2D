##@##
description = 'Create a scene with a rainbow arching over a cloudy sky.'
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the cloudy sky
sky_height = 400
sky = Rectangle(width=800, height=sky_height, color='lightblue')
sky.place_shape_global((400, sky_height/2))
scene.add_shape(sky)

# Create the clouds
cloud_width = 500
cloud_height = 200
cloud = Rectangle(width=cloud_width, height=cloud_height, color='white')
cloud.place_shape_global((400, 400))
scene.add_shape(cloud)

# Create the rainbow
rainbow_width = 600
rainbow_height = 300
rainbow_y = 150
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
for i, color in enumerate(rainbow_colors):
    rainbow_rect = Rectangle(width=rainbow_width, height=rainbow_height/7, color=color)
    rainbow_rect.place_shape_global((100, rainbow_y + i * rainbow_height/7))
    scene.add_shape(rainbow_rect)

# Create the sun
sun_radius = 50
sun = Circle(radius=sun_radius, color='yellow')
sun.place_shape_global((600, 200))
scene.add_shape(sun)

# Render the scene
scene.render('rainbow_cloud.png')
scene.render(filename='output.png')
scene.render(filename='output.png')