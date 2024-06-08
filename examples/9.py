##@##
description = 'Create a scene with a tree and a field of flowers.'
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the sky
sky = Rectangle(width=800, height=300, color='lightblue')
sky.place_shape_global((400, 150))
scene.add_shape(sky)

# Create the field
field = Rectangle(width=800, height=300, color='green')
field.place_shape_global((400, 450))
scene.add_shape(field)

# Create the tree trunk
trunk_width = 100
trunk_height = 300
trunk = Rectangle(width=trunk_width, height=trunk_height, color='brown')
trunk.place_shape_global((400, 450))
scene.add_shape(trunk)

# Create the tree canopy
canopy_size = 300
canopy = Triangle(size=canopy_size, color='green')
canopy.place_shape_local(trunk, 'above')
scene.add_shape(canopy)

# Create the flowers
flower_radius = 20
for i in range(20):
    flower = Circle(radius=flower_radius, color='yellow')
    flower.place_shape_global((
        400 + (i - 10) * 50,
        450 + (i - 10) * 30
    ))
    scene.add_shape(flower)

# Render the scene
scene.render('tree_and_flowers.png')
scene.render(filename='output.png')