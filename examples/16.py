##@##
description =Create a scene with three cars parked under a large tree.
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='white')

# Create the ground
ground = Rectangle(width=800, height=300, color='#00b300')
ground.place_shape_global((400, 450))
scene.add_shape(ground)

# Create the tree
tree_canopy = Circle(radius=150, color='#006600')
tree_canopy.place_shape_global((400, 200))
scene.add_shape(tree_canopy)

tree_trunk = Rectangle(width=100, height=250, color='#663300')
tree_trunk.place_shape_local(tree_canopy, 'below')
scene.add_shape(tree_trunk)

tree_root1 = Rectangle(width=120, height=30, color='#663300')
tree_root1.place_shape_local(tree_trunk, 'below', offset=(-50, 0))
scene.add_shape(tree_root1)

tree_root2 = Rectangle(width=120, height=30, color='#663300')
tree_root2.place_shape_local(tree_trunk, 'below', offset=(50, 0))
scene.add_shape(tree_root2)

# Create the cars
# Car 1
car1_body = Rectangle(width=150, height=70, color='#808080')
car1_body.place_shape_global((200, 500))
scene.add_shape(car1_body)

car1_window = Rectangle(width=100, height=20, color='#000000')
car1_window.place_shape_local(car1_body, 'above')
scene.add_shape(car1_window)

car1_wheel1 = Circle(radius=20, color='#000000')
car1_wheel1.place_shape_local(car1_body, 'below', offset=(-40, 0))
scene.add_shape(car1_wheel1)

car1_wheel2 = Circle(radius=20, color='#000000')
car1_wheel2.place_shape_local(car1_body, 'below', offset=(40, 0))
scene.add_shape(car1_wheel2)

# Car 2
car2_body = Rectangle(width=150, height=70, color='#808080')
car2_body.place_shape_global((400, 520))
scene.add_shape(car2_body)

car2_window = Rectangle(width=100, height=20, color='#000000')
car2_window.place_shape_local(car2_body, 'above')
scene.add_shape(car2_window)

car2_wheel1 = Circle(radius=20, color='#000000')
car2_wheel1.place_shape_local(car2_body, 'below', offset=(-40, 0))
scene.add_shape(car2_wheel1)

car2_wheel2 = Circle(radius=20, color='#000000')
car2_wheel2.place_shape_local(car2_body, 'below', offset=(40, 0))
scene.add_shape(car2_wheel2)

# Car 3
car3_body = Rectangle(width=150, height=70, color='#808080')
car3_body.place_shape_global((600, 500))
scene.add_shape(car3_body)

car3_window = Rectangle(width=100, height=20, color='#000000')
car3_window.place_shape_local(car3_body, 'above')
scene.add_shape(car3_window)

car3_wheel1 = Circle(radius=20, color='#000000')
car3_wheel1.place_shape_local(car3_body, 'below', offset=(-40, 0))
scene.add_shape(car3_wheel1)

car3_wheel2 = Circle(radius=20, color='#000000')
car3_wheel2.place_shape_local(car3_body, 'below', offset=(40, 0))
scene.add_shape(car3_wheel2)

# Render the scene
scene.render(filename='output.png')
scene.render(filename='output.png')