
# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='navy')

# Create the star body
star_body = Circle(radius=100, color='yellow')
star_body.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(star_body)

# Create the star points
for i in range(5):
    angle = i * 72  # 72 degrees between each point (360 / 5)
    star_point = Triangle(size=80, color='white', rotation=angle)
    star_point.place_shape_local(star_body, 'above')
    scene.add_shape(star_point)

# Create the star center
star_center = Circle(radius=30, color='yellow')
star_center.place_shape_local(star_body, 'above')
scene.add_shape(star_center)

# Render the scene to an image file
scene.render(filename='star_scene.png')
