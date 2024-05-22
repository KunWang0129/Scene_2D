
# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='white')

# Create the flower petals
flower_petals = Circle(radius=100, color='green')
flower_petals.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(flower_petals)

# Create the flower center
flower_center = Circle(radius=30, color='yellow')
flower_center.place_shape_local(flower_petals, 'center')
scene.add_shape(flower_center)

# Create the leaves
leaf1 = Triangle(size=50, color='green')
leaf1.place_shape_local(flower_center, 'above', offset=(0, -50))
scene.add_shape(leaf1)

leaf2 = Triangle(size=50, color='green')
leaf2.place_shape_local(flower_center, 'right', offset=(50, 0))
scene.add_shape(leaf2)

leaf3 = Triangle(size=50, color='green')
leaf3.place_shape_local(flower_center, 'below', offset=(0, 50))
scene.add_shape(leaf3)

# Create the flower stem
flower_stem = Rectangle(width=10, height=150, color='brown')
flower_stem.place_shape_local(flower_center, 'below', offset=(0, 50))
scene.add_shape(flower_stem)

# Create the leaves at the bottom of the stem
leaf4 = Rectangle(width=30, height=20, color='brown')
leaf4.place_shape_local(flower_stem, 'left', offset=(-20, 0))
scene.add_shape(leaf4)

leaf5 = Rectangle(width=30, height=20, color='brown')
leaf5.place_shape_local(flower_stem, 'right', offset=(20, 0))
scene.add_shape(leaf5)

# Render the scene to an image file
scene.render(filename='flower_scene.png')
