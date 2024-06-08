##@##
description = 'Create a scene with a car driving down a winding road.'
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the road
road_width = 800
road_height = 200
road = Rectangle(width=road_width, height=road_height, color='grey')
road.place_shape_global((400, 500))
scene.add_shape(road)

# Create the winding road curves
curve_width = 100
curve_height = 50
curve_spacing = 50
for i in range(10):
    curve = Rectangle(width=curve_width, height=curve_height, color='grey')
    curve.place_shape_global((i * curve_width + curve_spacing, 500 - curve_height/2))
    scene.add_shape(curve)

# Create the car
car_width = 200
car_height = 100
car_body = Rectangle(width=car_width, height=car_height, color='brown')
car_body.place_shape_global((400, 400))
scene.add_shape(car_body)

# Create the wheels
wheel_radius = car_height/4
front_wheel = Circle(radius=wheel_radius, color='black')
front_wheel.place_shape_local(car_body, 'below', offset=(-car_width/3, 0))
scene.add_shape(front_wheel)

rear_wheel = Circle(radius=wheel_radius, color='black')
rear_wheel.place_shape_local(car_body, 'below', offset=(car_width/3, 0))
scene.add_shape(rear_wheel)

# Create the front and rear bumpers
bumper_width = 50
bumper_height = 20
front_bumper = Rectangle(width=bumper_width, height=bumper_height, color='black')
front_bumper.place_shape_local(car_body, 'left')
scene.add_shape(front_bumper)

rear_bumper = Rectangle(width=bumper_width, height=bumper_height, color='black')
rear_bumper.place_shape_local(car_body, 'right')
scene.add_shape(rear_bumper)

# Create the windshield and rear window
window_width = 100
window_height = 50
windshield = Rectangle(width=window_width, height=window_height, color='lightblue')
windshield.place_shape_local(car_body, 'above', offset=(0, -car_height/4))
scene.add_shape(windshield)

rear_window = Rectangle(width=window_width, height=window_height, color='lightblue')
rear_window.place_shape_local(car_body, 'above', offset=(0, car_height/4))
scene.add_shape(rear_window)

# Create the roof
roof_width = 150
roof_height = 30
roof = Rectangle(width=roof_width, height=roof_height, color='brown')
roof.place_shape_local(car_body, 'above')
scene.add_shape(roof)

# Create the headlight and taillight
headlight_radius = 10
headlight = Circle(radius=headlight_radius, color='yellow')
headlight.place_shape_local(car_body, 'left', offset=(-bumper_width, 0))
scene.add_shape(headlight)

taillight_radius = 10
taillight = Circle(radius=taillight_radius, color='red')
taillight.place_shape_local(car_body, 'right', offset=(bumper_width, 0))
scene.add_shape(taillight)

# Create the landscape
landscape_height = 100
landscape_spacing = 50
for i in range(10):
    landscape = Triangle(size=landscape_height, color='green')
    landscape.place_shape_global((i * landscape_height + landscape_spacing, 600))
    scene.add_shape(landscape)

# Create the sky
sky = Rectangle(width=800, height=300, color='lightblue')
sky.place_shape_global((400, 150))
scene.add_shape(sky)

# Render the scene
scene.render('car_on_road.png')
scene.render(filename='output.png')