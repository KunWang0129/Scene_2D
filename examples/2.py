##@##
description = 'Create a scene with a chair.'
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='white')

# Create the seat of the chair
seat = Rectangle(width=200, height=30, color='brown')
seat.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(seat)

# Set chair leg dimensions
leg_width = 10
leg_height = 100

# Create the left leg of the chair
left_leg = Rectangle(width=leg_width, height=leg_height, color='brown')
left_leg.place_shape_local(seat, 'left', offset=(0, leg_height/2))  # Positioned at the left edge of the seat
scene.add_shape(left_leg)

# Create the right leg of the chair
right_leg = Rectangle(width=leg_width, height=leg_height, color='brown')
right_leg.place_shape_local(seat, 'right', offset=(0, leg_height/2))  # Positioned at the right edge of the seat
scene.add_shape(right_leg)

# Create the backrest of the chair
backrest = Rectangle(width=10, height=200, color='brown')
backrest.place_shape_local(left_leg, 'above')  # Positioned on top of the left leg
scene.add_shape(backrest)