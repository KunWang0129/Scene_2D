##@##
description = 'Create a scene with a tree.'
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='white')

# Create the trunk of the tree
trunk = Rectangle(width=30, height=200, color='brown')
trunk.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(trunk)

# Create the crown of the tree
crown = Circle(radius=100, color='green')
crown.place_shape_local(trunk, 'above')  # Positioned above the trunk
scene.add_shape(crown)