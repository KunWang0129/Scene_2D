##@##
description = 'Create a scene with two chairs and a table in a grassy field.'
##@##

from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the grassy field
field = Rectangle(width=800, height=400, color='green')
field.place_shape_global((400, 400))
scene.add_shape(field)

# Create the table
table_width = 200
table_height = 100
table = Rectangle(width=table_width, height=table_height, color='brown')
table.place_shape_global((400, 400))
scene.add_shape(table)

# Create the chair seats
chair_seat_width = 100
chair_seat_height = 50
chair_seat_left = Rectangle(width=chair_seat_width, height=chair_seat_height, color='grey')
chair_seat_left.place_shape_local(table, 'left', offset=(-50, 0))
scene.add_shape(chair_seat_left)

chair_seat_right = Rectangle(width=chair_seat_width, height=chair_seat_height, color='grey')
chair_seat_right.place_shape_local(table, 'right', offset=(50, 0))
scene.add_shape(chair_seat_right)

# Create the chair backs
chair_back_width = 80
chair_back_height = 80
chair_back_left = Rectangle(width=chair_back_width, height=chair_back_height, color='grey')
chair_back_left.place_shape_local(chair_seat_left, 'above', offset=(0, 20))
scene.add_shape(chair_back_left)

chair_back_right = Rectangle(width=chair_back_width, height=chair_back_height, color='grey')
chair_back_right.place_shape_local(chair_seat_right, 'above', offset=(0, 20))
scene.add_shape(chair_back_right)

# Create the chair legs
chair_leg_width = 20
chair_leg_height = 150
chair_leg_left_1 = Rectangle(width=chair_leg_width, height=chair_leg_height, color='brown')
chair_leg_left_1.place_shape_local(chair_seat_left, 'below', offset=(-25, 0))
scene.add_shape(chair_leg_left_1)

chair_leg_left_2 = Rectangle(width=chair_leg_width, height=chair_leg_height, color='brown')
chair_leg_left_2.place_shape_local(chair_seat_left, 'below', offset=(25, 0))
scene.add_shape(chair_leg_left_2)

chair_leg_right_1 = Rectangle(width=chair_leg_width, height=chair_leg_height, color='brown')
chair_leg_right_1.place_shape_local(chair_seat_right, 'below', offset=(-25, 0))
scene.add_shape(chair_leg_right_1)

chair_leg_right_2 = Rectangle(width=chair_leg_width, height=chair_leg_height, color='brown')
chair_leg_right_2.place_shape_local(chair_seat_right, 'below', offset=(25, 0))
scene.add_shape(chair_leg_right_2)

# Create the tabletop
tabletop_width = 150
tabletop_height = 20
tabletop = Rectangle(width=tabletop_width, height=tabletop_height, color='brown')
tabletop.place_shape_local(table, 'above', offset=(0, 20))
scene.add_shape(tabletop)

# Render the scene
scene.render('table_and_chairs.png')
scene.render(filename='output.png')