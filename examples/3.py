##@##
description = 'Create a scene with a cloud.'
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the main cloud body
main_cloud = Circle(radius=100, color='white')
main_cloud.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(main_cloud)

# Create the cloud details (smaller circles around the main cloud)
small_cloud1 = Circle(radius=80, color='white')
small_cloud1.place_shape_local(main_cloud, 'left', offset=(40, -30))
scene.add_shape(small_cloud1)

small_cloud2 = Circle(radius=80, color='white')
small_cloud2.place_shape_local(main_cloud, 'right', offset=(-40, -30))
scene.add_shape(small_cloud2)

small_cloud3 = Circle(radius=80, color='white')
small_cloud3.place_shape_local(main_cloud, 'above', offset=(0, 70))
scene.add_shape(small_cloud3)

# Render the scene to an image file
scene.render(filename='cloud_scene.png')
