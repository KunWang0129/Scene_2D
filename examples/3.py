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