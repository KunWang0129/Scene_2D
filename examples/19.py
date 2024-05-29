##@##
description =Create a scene with a sun in the sky and three cars parked on a road.
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the sun
sun = Circle(radius=50, color='yellow')
sun.place_shape_global((100, 100))
scene.add_shape(sun)

# Create the road
road = Rectangle(width=800, height=200, color='gray')
road.place_shape_global((400, 400))
scene.add_shape(road)

# Create the cars
# Red car
red_car_body = Rectangle(width=150, height=70, color='red')
red_car_body.place_shape_global((200, 450))
scene.add_shape(red_car_body)

red_car_headlight = Rectangle(width=20, height=10, color='black')
red_car_headlight.place_shape_local(red_car_body, 'right', offset=(-20, 0))
scene.add_shape(red_car_headlight)

red_car_grille = Rectangle(width=20, height=10, color='black')
red_car_grille.place_shape_local(red_car_body, 'right', offset=(20, 0))
scene.add_shape(red_car_grille)

red_car_wheel = Circle(radius=20, color='black')
red_car_wheel.place_shape_local(red_car_body, 'below', offset=(-40, 0))
scene.add_shape(red_car_wheel)

red_car_wheel2 = Circle(radius=20, color='black')
red_car_wheel2.place_shape_local(red_car_body, 'below', offset=(40, 0))
scene.add_shape(red_car_wheel2)

red_car_roof = Rectangle(width=50, height=10, color='white')
red_car_roof.place_shape_local(red_car_body, 'above')
scene.add_shape(red_car_roof)

# Blue car
blue_car_body = Rectangle(width=150, height=70, color='blue')
blue_car_body.place_shape_global((400, 450))
scene.add_shape(blue_car_body)

blue_car_headlight = Rectangle(width=20, height=10, color='black')
blue_car_headlight.place_shape_local(blue_car_body, 'right', offset=(-20, 0))
scene.add_shape(blue_car_headlight)

blue_car_grille = Rectangle(width=20, height=10, color='black')
blue_car_grille.place_shape_local(blue_car_body, 'right', offset=(20, 0))
scene.add_shape(blue_car_grille)

blue_car_wheel = Circle(radius=20, color='black')
blue_car_wheel.place_shape_local(blue_car_body, 'below', offset=(-40, 0))
scene.add_shape(blue_car_wheel)

blue_car_wheel2 = Circle(radius=20, color='black')
blue_car_wheel2.place_shape_local(blue_car_body, 'below', offset=(40, 0))
scene.add_shape(blue_car_wheel2)

blue_car_roof = Rectangle(width=50, height=10, color='white')
blue_car_roof.place_shape_local(blue_car_body, 'above')
scene.add_shape(blue_car_roof)

# Green car
green_car_body = Rectangle(width=150, height=70, color='green')
green_car_body.place_shape_global((600, 450))
scene.add_shape(green_car_body)

green_car_headlight = Rectangle(width=20, height=10, color='black')
green_car_headlight.place_shape_local(green_car_body, 'right', offset=(-20, 0))
scene.add_shape(green_car_headlight)

green_car_grille = Rectangle(width=20, height=10, color='black')
green_car_grille.place_shape_local(green_car_body, 'right', offset=(20, 0))
scene.add_shape(green_car_grille)

green_car_wheel = Circle(radius=20, color='black')
green_car_wheel.place_shape_local(green_car_body, 'below', offset=(-40, 0))
scene.add_shape(green_car_wheel)

green_car_wheel2 = Circle(radius=20, color='black')
green_car_wheel2.place_shape_local(green_car_body, 'below', offset=(40, 0))
scene.add_shape(green_car_wheel2)

green_car_roof = Rectangle(width=50, height=10, color='white')
green_car_roof.place_shape_local(green_car_body, 'above')
scene.add_shape(green_car_roof)

# Render the scene
scene.render(filename='output.png')
scene.render(filename='output.png')