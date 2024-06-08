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

# Set table leg dimensions
leg_width = 20
leg_height = 200

# Create the left table leg
left_leg = Rectangle(width=leg_width, height=leg_height, color='brown')
left_leg.place_shape_local(tabletop, 'left', offset=(0, leg_height/2))  # Positioned at the left edge of the tabletop
scene.add_shape(left_leg)

# Create the right table leg
right_leg = Rectangle(width=leg_width, height=leg_height, color='brown')
right_leg.place_shape_local(tabletop, 'right', offset=(0, leg_height/2))  # Positioned at the right edge of the tabletop
scene.add_shape(right_leg)