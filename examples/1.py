##@##
description = 'Create a scene with a car.'
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='white')

# Set the car dimensions
car_width = 300
car_height = 100

# Create the car body
car_body = Rectangle(width=car_width, height=car_height, color='brown')
car_body.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(car_body)

# Create the wheels
front_wheel = Circle(radius=car_height/4, color='black')
front_wheel.place_shape_local(car_body, 'below', offset=(-car_width/3, 0))
scene.add_shape(front_wheel)

rear_wheel = Circle(radius=car_height/4, color='black')
rear_wheel.place_shape_local(car_body, 'below', offset=(car_width/3, 0))
scene.add_shape(rear_wheel)

# Create the roof
roof = Rectangle(width=car_width/2, height=car_height/2, color='brown')
roof.place_shape_local(car_body, 'above')
scene.add_shape(roof)

# Create the headlights
headlight_radius = car_height/10
headlight = Circle(radius=car_height/10, color='yellow')
headlight.place_shape_local(car_body, 'right', offset=(-headlight_radius,0))
scene.add_shape(headlight)