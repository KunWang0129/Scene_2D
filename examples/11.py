##@##
description = 'Create a scene with a crescent moon in the night sky.'
##@##

from utils.Shape import Circle, Rectangle
from utils.Scene import Scene
import random

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='navy')

# Create the night sky
sky = Rectangle(width=800, height=600, color='navy')
sky.place_shape_global((400, 300))
scene.add_shape(sky)

# Create the crescent moon
moon_radius = 100
moon_x = 650
moon_y = 150
moon = Circle(radius=moon_radius, color='lightgrey')
moon.place_shape_global((moon_x, moon_y))
scene.add_shape(moon)

# Create the stars
num_stars = 100
for _ in range(num_stars):
    star_radius = random.uniform(2, 5)
    star_x = random.uniform(50, 750)
    star_y = random.uniform(50, 550)
    star = Circle(radius=star_radius, color='white')
    star.place_shape_global((star_x, star_y))
    scene.add_shape(star)

# Render the scene
scene.render('crescent_moon.png')
scene.render(filename='output.png')