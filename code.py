
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene
import math

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the sea
sea = Rectangle(width=800, height=400, color='blue')
sea.place_shape_global((400, 300))
scene.add_shape(sea)

# Create the sky
sky = Rectangle(width=800, height=200, color='lightblue')
sky.place_shape_global((400, 100))
scene.add_shape(sky)

# Create the sailing boat
boat = Rectangle(width=200, height=100, color='white')
boat.place_shape_global((400, 400))
scene.add_shape(boat)

# Create the sail
sail = Triangle(size=150, color='gray')
sail.place_shape_local(boat, 'above', offset=(0, -50))
scene.add_shape(sail)

# Create the hull
hull1 = Rectangle(width=50, height=30, color='brown')
hull1.place_shape_local(boat, 'below', offset=(-50, 20))
scene.add_shape(hull1)

hull2 = Rectangle(width=50, height=30, color='brown')
hull2.place_shape_local(boat, 'below', offset=(50, 20))
scene.add_shape(hull2)

# Create the sun
sun = Circle(radius=50, color='yellow')
sun.place_shape_global((700, 100))
scene.add_shape(sun)

# Create the waves
for i in range(10):
    wave = Rectangle(width=80, height=20, color='white')
    wave.place_shape_global((i * 80 + 40, 500 + 20 * math.sin(i * 0.5)))
    scene.add_shape(wave)

# Create the mast
mast = Rectangle(width=10, height=100, color='brown')
mast.place_shape_local(boat, 'above', offset=(0, -50))
scene.add_shape(mast)

# Render the scene
scene.render('scene.png')
