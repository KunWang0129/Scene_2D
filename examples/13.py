##@##
description =Create a scene with a tree next to several parked cars.
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='white')

# Create the tree
tree_canopy = Circle(radius=100, color='green')
tree_canopy.place_shape_global((400, 300))
scene.add_shape(tree_canopy)

tree_trunk = Rectangle(width=50, height=150, color='brown')
tree_trunk.place_shape_local(tree_canopy, 'below')
scene.add_shape(tree_trunk)

tree_root1 = Rectangle(width=80, height=20, color='brown')
tree_root1.place_shape_local(tree_trunk, 'below', offset=(-40, 0))
scene.add_shape(tree_root1)

tree_root2 = Rectangle(width=80, height=20, color='brown')
tree_root2.place_shape_local(tree_trunk, 'below', offset=(0, 0))
scene.add_shape(tree_root2)

tree_root3 = Rectangle(width=80, height=20, color='brown')
tree_root3.place_shape_local(tree_trunk, 'below', offset=(40, 0))
scene.add_shape(tree_root3)

# Create the parked cars
# Car 1
car1_body = Rectangle(width=150, height=70, color='gray')
car1_body.place_shape_global((200, 500))
scene.add_shape(car1_body)

car1_window = Rectangle(width=100, height=20, color='black')
car1_window.place_shape_local(car1_body, 'above')
scene.add_shape(car1_window)

car1_headlight = Rectangle(width=20, height=10, color='black')
car1_headlight.place_shape_local(car1_body, 'right')
scene.add_shape(car1_headlight)

car1_wheel = Circle(radius=20, color='black')
car1_wheel.place_shape_local(car1_body, 'below', offset=(-40, 0))
scene.add_shape(car1_wheel)

car1_wheel2 = Circle(radius=20, color='black')
car1_wheel2.place_shape_local(car1_body, 'below', offset=(40, 0))
scene.add_shape(car1_wheel2)

# Car 2
car2_body = Rectangle(width=150, height=70, color='gray')
car2_body.place_shape_global((600, 500))
scene.add_shape(car2_body)

car2_window = Rectangle(width=100, height=20, color='black')
car2_window.place_shape_local(car2_body, 'above')
scene.add_shape(car2_window)

car2_headlight = Rectangle(width=20, height=10, color='black')
car2_headlight.place_shape_local(car2_body, 'right')
scene.add_shape(car2_headlight)

car2_wheel = Circle(radius=20, color='black')
car2_wheel.place_shape_local(car2_body, 'below', offset=(-40, 0))
scene.add_shape(car2_wheel)

car2_wheel2 = Circle(radius=20, color='black')
car2_wheel2.place_shape_local(car2_body, 'below', offset=(40, 0))
scene.add_shape(car2_wheel2)

# Render the scene
scene.render(filename='output.png')
scene.render(filename='output.png')