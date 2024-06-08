##@##
description = 'Create a scene with a rainbow arching over a cloud.'
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the cloud
cloud_width = 500
cloud_height = 200
cloud = Circle(radius=cloud_height/2, color='white')
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

# Create the ground
ground_height = 150
ground = Rectangle(width=800, height=ground_height, color='grey')
ground.place_shape_global((400, 600 - ground_height/2))
scene.add_shape(ground)

# Render the scene
scene.render('rainbow_cloud.png')
scene.render(filename='output.png')