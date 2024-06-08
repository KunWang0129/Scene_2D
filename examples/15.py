##@##
description = 'Create a scene with a rainbow arching over a bridge.'
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='lightblue')

# Create the sky
sky = Rectangle(width=800, height=400, color='lightblue')
sky.place_shape_global((400, 200))
scene.add_shape(sky)

# Create the grass
grass = Rectangle(width=800, height=200, color='green')
grass.place_shape_global((400, 500))
scene.add_shape(grass)

# Create the bridge
bridge_width = 400
bridge_height = 100
bridge = Rectangle(width=bridge_width, height=bridge_height, color='grey')
bridge.place_shape_global((400, 500))
scene.add_shape(bridge)

# Create the rainbow
rainbow_width = 600
rainbow_height = 300
rainbow_y = 150
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
for i, color in enumerate(rainbow_colors):
    rainbow_rect = Rectangle(width=rainbow_width, height=rainbow_height/7, color=color)
    rainbow_rect.place_shape_global((100, rainbow_y + i * rainbow_height/7))
    scene.add_shape(rainbow_rect)

# Create the bridge supports
support_width = 50
support_height = 200
support_left = Rectangle(width=support_width, height=support_height, color='grey')
support_left.place_shape_global((200, 500))
scene.add_shape(support_left)

support_right = Rectangle(width=support_width, height=support_height, color='grey')
support_right.place_shape_global((600, 500))
scene.add_shape(support_right)

# Create the bridge deck
deck_width = 350
deck_height = 50
deck = Rectangle(width=deck_width, height=deck_height, color='grey')
deck.place_shape_global((400, 450))
scene.add_shape(deck)

# Create the bridge railings
railing_width = 25
railing_height = 50
railing_left = Rectangle(width=railing_width, height=railing_height, color='grey')
railing_left.place_shape_global((175, 425))
scene.add_shape(railing_left)

railing_right = Rectangle(width=railing_width, height=railing_height, color='grey')
railing_right.place_shape_global((625, 425))
scene.add_shape(railing_right)

# Render the scene
scene.render('rainbow_bridge.png')
scene.render(filename='output.png')