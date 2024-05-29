##@##
description =Create a scene with three cars parked on a road.
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='white')

# Create the road
road = Rectangle(width=600, height=300, color='gray')
road.place_shape_global((400, 300))
scene.add_shape(road)

# Create the cars
# Red car
red_car_body = Rectangle(width=150, height=70, color='red')
red_car_body.place_shape_global((200, 400))
scene.add_shape(red_car_body)

red_car_wheel1 = Circle(radius=20, color='black')
red_car_wheel1.place_shape_local(red_car_body, 'below', offset=(-40, 0))
scene.add_shape(red_car_wheel1)

red_car_wheel2 = Circle(radius=20, color='black')
red_car_wheel2.place_shape_local(red_car_body, 'below', offset=(40, 0))
scene.add_shape(red_car_wheel2)

red_car_headlight = Rectangle(width=20, height=10, color='black')
red_car_headlight.place_shape_local(red_car_body, 'right')
scene.add_shape(red_car_headlight)

red_car_taillight = Rectangle(width=20, height=10, color='red')
red_car_taillight.place_shape_local(red_car_body, 'left')
scene.add_shape(red_car_taillight)

red_car_roof = Rectangle(width=50, height=10, color='white')
red_car_roof.place_shape_local(red_car_body, 'above')
scene.add_shape(red_car_roof)

red_car_door1 = Rectangle(width=30, height=40, color='white')
red_car_door1.place_shape_local(red_car_body, 'left', offset=(0, -10))
scene.add_shape(red_car_door1)

red_car_door2 = Rectangle(width=30, height=40, color='white')
red_car_door2.place_shape_local(red_car_body, 'right', offset=(0, -10))
scene.add_shape(red_car_door2)

# Blue car
blue_car_body = Rectangle(width=150, height=70, color='blue')
blue_car_body.place_shape_global((400, 400))
scene.add_shape(blue_car_body)

blue_car_wheel1 = Circle(radius=20, color='black')
blue_car_wheel1.place_shape_local(blue_car_body, 'below', offset=(-40, 0))
scene.add_shape(blue_car_wheel1)

blue_car_wheel2 = Circle(radius=20, color='black')
blue_car_wheel2.place_shape_local(blue_car_body, 'below', offset=(40, 0))
scene.add_shape(blue_car_wheel2)

blue_car_headlight = Rectangle(width=20, height=10, color='black')
blue_car_headlight.place_shape_local(blue_car_body, 'right')
scene.add_shape(blue_car_headlight)

blue_car_taillight = Rectangle(width=20, height=10, color='blue')
blue_car_taillight.place_shape_local(blue_car_body, 'left')
scene.add_shape(blue_car_taillight)

blue_car_roof = Rectangle(width=50, height=10, color='white')
blue_car_roof.place_shape_local(blue_car_body, 'above')
scene.add_shape(blue_car_roof)

blue_car_door1 = Rectangle(width=30, height=40, color='white')
blue_car_door1.place_shape_local(blue_car_body, 'left', offset=(0, -10))
scene.add_shape(blue_car_door1)

blue_car_door2 = Rectangle(width=30, height=40, color='white')
blue_car_door2.place_shape_local(blue_car_body, 'right', offset=(0, -10))
scene.add_shape(blue_car_door2)

# Green car
green_car_body = Rectangle(width=150, height=70, color='green')
green_car_body.place_shape_global((600, 400))
scene.add_shape(green_car_body)

green_car_wheel1 = Circle(radius=20, color='black')
green_car_wheel1.place_shape_local(green_car_body, 'below', offset=(-40, 0))
scene.add_shape(green_car_wheel1)

green_car_wheel2 = Circle(radius=20, color='black')
green_car_wheel2.place_shape_local(green_car_body, 'below', offset=(40, 0))
scene.add_shape(green_car_wheel2)

green_car_headlight = Rectangle(width=20, height=10, color='black')
green_car_headlight.place_shape_local(green_car_body, 'right')
scene.add_shape(green_car_headlight)

green_car_taillight = Rectangle(width=20, height=10, color='green')
green_car_taillight.place_shape_local(green_car_body, 'left')
scene.add_shape(green_car_taillight)

green_car_roof = Rectangle(width=50, height=10, color='white')
green_car_roof.place_shape_local(green_car_body, 'above')
scene.add_shape(green_car_roof)

green_car_door1 = Rectangle(width=30, height=40, color='white')
green_car_door1.place_shape_local(green_car_body, 'left', offset=(0, -10))
scene.add_shape(green_car_door1)

green_car_door2 = Rectangle(width=30, height=40, color='white')
green_car_door2.place_shape_local(green_car_body, 'right', offset=(0, -10))
scene.add_shape(green_car_door2)

# Render the scene
scene.render(filename='output.png')
scene.render(filename='output.png')