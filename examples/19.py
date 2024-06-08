##@##
description = 'Create a scene with a grassy field and several fluffy white clouds in the sky.'
##@##

from utils.Shape import Circle, Rectangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the grassy field
field = Rectangle(width=800, height=300, color='green')
field.place_shape_global((400, 450))
scene.add_shape(field)

# Create the fluffy white clouds
cloud_radius = 100
# Top left cloud
cloud1 = Circle(radius=cloud_radius, color='white')
cloud1.place_shape_global((200, 150))
scene.add_shape(cloud1)

# Top center cloud
cloud2 = Circle(radius=cloud_radius, color='white')
cloud2.place_shape_global((400, 100))
scene.add_shape(cloud2)

# Top right cloud
cloud3 = Circle(radius=cloud_radius, color='white')
cloud3.place_shape_global((600, 150))
scene.add_shape(cloud3)

# Render the scene
scene.render('grassy_field_with_clouds.png')
scene.render(filename='output.png')
scene.render(filename='output.png')