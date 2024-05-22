
# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the mountain
mountain = Triangle(size=400, color='gray')
mountain.place_shape_global((400, 400))
scene.add_shape(mountain)

# Create the mountain peak
peak = Triangle(size=200, color='lightgray')
peak.place_shape_local(mountain, 'above')
scene.add_shape(peak)

# Create the mountain ridges
ridge1 = Triangle(size=200, color='darkgray')
ridge1.place_shape_local(mountain, 'below', offset=(0, 50))
scene.add_shape(ridge1)

ridge2 = Triangle(size=200, color='darkgray')
ridge2.place_shape_local(ridge1, 'below', offset=(0, 50))
scene.add_shape(ridge2)

ridge3 = Triangle(size=200, color='darkgray')
ridge3.place_shape_local(ridge2, 'below', offset=(0, 50))
scene.add_shape(ridge3)

# Create the sky
sky = Circle(radius=300, color='lightblue')
sky.place_shape_local(peak, 'above', offset=(0, 50))
scene.add_shape(sky)

# Create the ground
ground = Rectangle(width=800, height=200, color='green')
ground.place_shape_global((400, 550))
scene.add_shape(ground)

# Create the rocks
rock1 = Circle(radius=10, color='brown')
rock1.place_shape_local(ground, 'right', offset=(-100, -50))
scene.add_shape(rock1)

rock2 = Circle(radius=15, color='brown')
rock2.place_shape_local(ground, 'left', offset=(100, -70))
scene.add_shape(rock2)

rock3 = Circle(radius=12, color='brown')
rock3.place_shape_local(ground, 'above', offset=(0, -30))
scene.add_shape(rock3)

# Render the scene to an image file
scene.render(filename='mountain_scene.png')
