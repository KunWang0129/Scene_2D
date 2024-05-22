
# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the sun
sun = Circle(radius=100, color='yellow')
sun.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(sun)

# Create the sun rays
for i in range(12):
    angle = i * 30  # 12 rays, each 30 degrees apart
    ray = Circle(radius=150, color='yellow')
    ray.place_shape_local(sun, 'above', offset=(0, 0), rotation=angle)
    scene.add_shape(ray)

# Create the sun core
sun_core = Circle(radius=50, color='orange')
sun_core.place_shape_local(sun, 'center')
scene.add_shape(sun_core)

# Create the sun outline
sun_outline = Circle(radius=101, color='black')
sun_outline.place_shape_local(sun, 'center')
scene.add_shape(sun_outline)

# Render the scene to an image file
scene.render(filename='sun_scene.png')
