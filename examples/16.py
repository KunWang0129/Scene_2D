##@##
description = 'Create a scene with a lake and some fish swimming in it.'
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='lightblue')

# Create the lake
lake = Rectangle(width=800, height=400, color='blue')
lake.place_shape_global((400, 400))
scene.add_shape(lake)

# Create the sky
sky = Rectangle(width=800, height=200, color='lightblue')
sky.place_shape_global((400, 100))
scene.add_shape(sky)

# Create the fish
fish_size = 50
fish1 = Triangle(size=fish_size, color='orange')
fish1.place_shape_global((200, 500))
scene.add_shape(fish1)

fish2 = Triangle(size=fish_size, color='orange')
fish2.place_shape_global((300, 500))
scene.add_shape(fish2)

fish3 = Triangle(size=fish_size, color='orange')
fish3.place_shape_global((400, 500))
scene.add_shape(fish3)

fish4 = Triangle(size=fish_size, color='orange')
fish4.place_shape_global((500, 550))
scene.add_shape(fish4)

fish5 = Triangle(size=fish_size, color='orange')
fish5.place_shape_global((600, 550))
scene.add_shape(fish5)

# Create the tree
tree_width = 100
tree_height = 200
tree_trunk = Rectangle(width=50, height=tree_height, color='brown')
tree_trunk.place_shape_global((700, 400))
scene.add_shape(tree_trunk)

tree_canopy = Rectangle(width=tree_width, height=tree_height, color='green')
tree_canopy.place_shape_local(tree_trunk, 'above')
scene.add_shape(tree_canopy)

# Create the sun
sun = Circle(radius=50, color='yellow')
sun.place_shape_global((100, 100))
scene.add_shape(sun)

# Render the scene
scene.render('lake_with_fish.png')
scene.render(filename='output.png')