##@##
description =Create a scene with a field of three trees.
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the grassy field
field = Rectangle(width=800, height=300, color='green')
field.place_shape_global((400, 450))
scene.add_shape(field)

# Create the first tree
# Tree trunk
tree1_trunk = Rectangle(width=50, height=200, color='brown')
tree1_trunk.place_shape_global((200, 300))
scene.add_shape(tree1_trunk)

# Tree canopy
tree1_canopy = Triangle(size=150, color='green')
tree1_canopy.place_shape_local(tree1_trunk, 'above')
scene.add_shape(tree1_canopy)

# Inner foliage
tree1_inner = Triangle(size=100, color='#00b300')
tree1_inner.place_shape_local(tree1_canopy, 'center', offset=(0, -25))
scene.add_shape(tree1_inner)

# Create the second tree
# Tree trunk
tree2_trunk = Rectangle(width=50, height=200, color='brown')
tree2_trunk.place_shape_global((400, 300))
scene.add_shape(tree2_trunk)

# Tree canopy
tree2_canopy = Triangle(size=150, color='green')
tree2_canopy.place_shape_local(tree2_trunk, 'above')
scene.add_shape(tree2_canopy)

# Inner foliage
tree2_inner = Triangle(size=100, color='#00b300')
tree2_inner.place_shape_local(tree2_canopy, 'center', offset=(0, -25))
scene.add_shape(tree2_inner)

# Create the third tree
# Tree trunk
tree3_trunk = Rectangle(width=50, height=200, color='brown')
tree3_trunk.place_shape_global((600, 300))
scene.add_shape(tree3_trunk)

# Tree canopy
tree3_canopy = Triangle(size=150, color='green')
tree3_canopy.place_shape_local(tree3_trunk, 'above')
scene.add_shape(tree3_canopy)

# Inner foliage
tree3_inner = Triangle(size=100, color='#00b300')
tree3_inner.place_shape_local(tree3_canopy, 'center', offset=(0, -25))
scene.add_shape(tree3_inner)

# Add some flowers
flower1 = Circle(radius=10, color='yellow')
flower1.place_shape_global((150, 500))
scene.add_shape(flower1)

flower2 = Circle(radius=10, color='yellow')
flower2.place_shape_global((300, 550))
scene.add_shape(flower2)

flower3 = Circle(radius=10, color='yellow')
flower3.place_shape_global((550, 500))
scene.add_shape(flower3)

flower4 = Circle(radius=10, color='yellow')
flower4.place_shape_global((700, 550))
scene.add_shape(flower4)

# Render the scene
scene.render('scene.png')
scene.render(filename='output.png')