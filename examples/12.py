##@##
description =Create a scene with a group of three trees in a grassy field.
##@##

# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the grassy field
field = Rectangle(width=800, height=300, color='green')
field.place_shape_global((400, 450))
scene.add_shape(field)

# Create the first tree
# Tree canopy
tree1_canopy = Circle(radius=100, color='green')
tree1_canopy.place_shape_global((200, 300))
scene.add_shape(tree1_canopy)

# Tree trunk
tree1_trunk = Rectangle(width=30, height=200, color='brown')
tree1_trunk.place_shape_local(tree1_canopy, 'below')
scene.add_shape(tree1_trunk)

# Tree branches
tree1_branch1 = Circle(radius=30, color='green')
tree1_branch1.place_shape_local(tree1_trunk, 'above', offset=(0, -50))
scene.add_shape(tree1_branch1)

tree1_branch2 = Circle(radius=30, color='green')
tree1_branch2.place_shape_local(tree1_trunk, 'above', offset=(-50, -25))
scene.add_shape(tree1_branch2)

tree1_branch3 = Circle(radius=30, color='green')
tree1_branch3.place_shape_local(tree1_trunk, 'above', offset=(50, -25))
scene.add_shape(tree1_branch3)

# Create the second tree
# Tree canopy
tree2_canopy = Circle(radius=100, color='green')
tree2_canopy.place_shape_global((600, 300))
scene.add_shape(tree2_canopy)

# Tree trunk
tree2_trunk = Rectangle(width=30, height=200, color='brown')
tree2_trunk.place_shape_local(tree2_canopy, 'below')
scene.add_shape(tree2_trunk)

# Tree branches
tree2_branch1 = Circle(radius=30, color='green')
tree2_branch1.place_shape_local(tree2_trunk, 'above', offset=(0, -50))
scene.add_shape(tree2_branch1)

tree2_branch2 = Circle(radius=30, color='green')
tree2_branch2.place_shape_local(tree2_trunk, 'above', offset=(-50, -25))
scene.add_shape(tree2_branch2)

tree2_branch3 = Circle(radius=30, color='green')
tree2_branch3.place_shape_local(tree2_trunk, 'above', offset=(50, -25))
scene.add_shape(tree2_branch3)

# Create the third tree
# Tree canopy
tree3_canopy = Circle(radius=100, color='green')
tree3_canopy.place_shape_global((400, 300))
scene.add_shape(tree3_canopy)

# Tree trunk
tree3_trunk = Rectangle(width=30, height=200, color='brown')
tree3_trunk.place_shape_local(tree3_canopy, 'below')
scene.add_shape(tree3_trunk)

# Tree branches
tree3_branch1 = Circle(radius=30, color='green')
tree3_branch1.place_shape_local(tree3_trunk, 'above', offset=(0, -50))
scene.add_shape(tree3_branch1)

tree3_branch2 = Circle(radius=30, color='green')
tree3_branch2.place_shape_local(tree3_trunk, 'above', offset=(-50, -25))
scene.add_shape(tree3_branch2)

tree3_branch3 = Circle(radius=30, color='green')
tree3_branch3.place_shape_local(tree3_trunk, 'above', offset=(50, -25))
scene.add_shape(tree3_branch3)

# Create the grass tufts
grass_tuft1 = Triangle(size=50, color='green')
grass_tuft1.place_shape_global((150, 550))
scene.add_shape(grass_tuft1)

grass_tuft2 = Triangle(size=50, color='green')
grass_tuft2.place_shape_global((650, 550))
scene.add_shape(grass_tuft2)

# Render the scene
scene.render('scene.png')
scene.render(filename='output.png')