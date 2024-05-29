##@##
description = 'Create a scene with a table.'
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='white')

# Create the tabletop
tabletop = Rectangle(width=400, height=50, color='brown')
tabletop.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(tabletop)

# Create the left table leg
left_leg = Rectangle(width=20, height=200, color='brown')
left_leg.place_shape_local(tabletop, 'below', offset=(-190, 0))  # Positioned at the left edge of the tabletop
scene.add_shape(left_leg)

# Create the right table leg
right_leg = Rectangle(width=20, height=200, color='brown')
right_leg.place_shape_local(tabletop, 'below', offset=(190, 0))  # Positioned at the right edge of the tabletop
scene.add_shape(right_leg)