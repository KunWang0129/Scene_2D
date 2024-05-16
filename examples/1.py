##@##
description = 'Create a scene with a car.'
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='white')

# Create the car body
car_body = Rectangle(width=300, height=100, color='brown')
car_body.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(car_body)

# Create the wheels
front_wheel = Circle(radius=25, color='black')
front_wheel.place_shape_local(car_body, 'below', offset=(-90, 0))
scene.add_shape(front_wheel)

rear_wheel = Circle(radius=25, color='black')
rear_wheel.place_shape_local(car_body, 'below', offset=(90, 0))
scene.add_shape(rear_wheel)

# Create the front bumper
front_bumper = Rectangle(width=10, height=50, color='black')
front_bumper.place_shape_local(car_body, 'right')
scene.add_shape(front_bumper)

# Create the rear bumper
rear_bumper = Rectangle(width=10, height=50, color='black')
rear_bumper.place_shape_local(car_body, 'left')
scene.add_shape(rear_bumper)

# Create the windshield
windshield = Rectangle(width=60, height=30, color='lightblue')
windshield.place_shape_local(car_body, 'above', offset=(50, 50))
scene.add_shape(windshield)

# Create the rear window
rear_window = Rectangle(width=60, height=30, color='lightblue')
rear_window.place_shape_local(car_body, 'above', offset=(-50, 50))
scene.add_shape(rear_window)

# Create the roof
roof = Rectangle(width=80, height=10, color='brown')
roof.place_shape_local(car_body, 'above')
scene.add_shape(roof)

# Create the headlight
headlight = Circle(radius=10, color='yellow')
headlight.place_shape_local(car_body, 'right')
scene.add_shape(headlight)

# Create the taillight
taillight = Circle(radius=10, color='red')
taillight.place_shape_local(car_body, 'left')
scene.add_shape(taillight)

# Render the scene to an image file
scene.render(filename='car_scene.png')
