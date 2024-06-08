##@##
description = 'Create a scene with multiple clouds and a large sun in the sky.'
##@##

from utils.Shape import Circle, Rectangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the sun
sun_radius = 150
sun = Circle(radius=sun_radius, color='yellow')
sun.place_shape_global((400, 150))
scene.add_shape(sun)

# Create the clouds
cloud_radius_1 = 100
cloud_1 = Circle(radius=cloud_radius_1, color='white')
cloud_1.place_shape_global((600, 250))
scene.add_shape(cloud_1)

cloud_radius_2 = 80
cloud_2 = Circle(radius=cloud_radius_2, color='white')
cloud_2.place_shape_local(cloud_1, 'left', offset=(-50, 50))
scene.add_shape(cloud_2)

cloud_radius_3 = 90
cloud_3 = Circle(radius=cloud_radius_3, color='white')
cloud_3.place_shape_local(cloud_1, 'right', offset=(50, 30))
scene.add_shape(cloud_3)

cloud_radius_4 = 70
cloud_4 = Circle(radius=cloud_radius_4, color='white')
cloud_4.place_shape_local(cloud_1, 'above', offset=(0, -50))
scene.add_shape(cloud_4)

cloud_radius_5 = 60
cloud_5 = Circle(radius=cloud_radius_5, color='white')
cloud_5.place_shape_local(cloud_4, 'right', offset=(50, 0))
scene.add_shape(cloud_5)

# Render the scene
scene.render('sky_with_clouds_and_sun.png')
scene.render(filename='output.png')
scene.render(filename='output.png')