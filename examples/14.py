##@##
description = 'Create a scene with a full moon reflecting on a still lake.'
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene
import random

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='navy')

# Create the lake
lake = Rectangle(width=800, height=300, color='lightblue')
lake.place_shape_global((400, 450))
scene.add_shape(lake)

# Create the night sky
sky = Rectangle(width=800, height=300, color='navy')
sky.place_shape_global((400, 150))
scene.add_shape(sky)

# Create the full moon
moon_radius = 100
moon = Circle(radius=moon_radius, color='white')
moon.place_shape_global((700, 100))
scene.add_shape(moon)

# Create the moon's reflection
reflection_radius = 75
reflection = Circle(radius=reflection_radius, color='white')
reflection.place_shape_global((400, 450))
scene.add_shape(reflection)

# Create the ripples on the lake
num_ripples = 20
for _ in range(num_ripples):
    ripple_size = random.uniform(10, 30)
    ripple_x = random.uniform(50, 750)
    ripple_y = random.uniform(400, 600)
    ripple = Triangle(size=ripple_size, color='white')
    ripple.place_shape_global((ripple_x, ripple_y))
    scene.add_shape(ripple)

# Create the stars in the night sky
num_stars = 50
for _ in range(num_stars):
    star_size = random.uniform(5, 15)
    star_x = random.uniform(50, 750)
    star_y = random.uniform(50, 300)
    star = Triangle(size=star_size, color='white')
    star.place_shape_global((star_x, star_y))
    scene.add_shape(star)

# Render the scene
scene.render('full_moon_lake.png')
scene.render(filename='output.png')
scene.render(filename='output.png')