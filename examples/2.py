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

# Create the left leg of the chair
left_leg = Rectangle(width=10, height=100, color='brown')
left_leg.place_shape_local(seat, 'below', offset=(-95, 0))  # Positioned at the left edge of the seat
scene.add_shape(left_leg)

# Create the right leg of the chair
right_leg = Rectangle(width=10, height=100, color='brown')
right_leg.place_shape_local(seat, 'below', offset=(95, 0))  # Positioned at the right edge of the seat
scene.add_shape(right_leg)

# Create the backrest of the chair
backrest = Rectangle(width=10, height=200, color='brown')
backrest.place_shape_local(seat, 'above', offset=(-95, 0))  # Positioned on top of the seat
scene.add_shape(backrest)

# Render the scene to an image file
scene.render(filename='chair_scene.png')
