#@# Prompt
# prompt = 'Create a scene with a chair.'
#@#

# Create the Scene object with desired dimensions and background color
scene = Scene(size=(800, 600), bg_color="lightgray")

# Create the chair using rectangles
chair_seat = Rectangle(width=100, height=20, color="darkgray")
chair_seat.place_shape_global((200, 350))  # Position the chair seat to the left of the table

chair_backrest = Rectangle(width=20, height=80, color="darkgray")
chair_backrest.place_shape_global((160, 310))  # Position the backrest to the left of the seat

chair_leg1 = Rectangle(width=10, height=40, color="darkgray")
chair_leg1.place_shape_global((180, 370))  # Front-left chair leg

chair_leg2 = Rectangle(width=10, height=40, color="darkgray")
chair_leg2.place_shape_global((220, 370))  # Front-right chair leg

chair_leg3 = Rectangle(width=10, height=40, color="darkgray")
chair_leg3.place_shape_global((180, 410))  # Back-left chair leg

chair_leg4 = Rectangle(width=10, height=40, color="darkgray")
chair_leg4.place_shape_global((220, 410))  # Back-right chair leg

# Add all shapes to the scene
scene.add_shape(chair_seat)
scene.add_shape(chair_backrest)
scene.add_shape(chair_leg1)
scene.add_shape(chair_leg2)
scene.add_shape(chair_leg3)
scene.add_shape(chair_leg4)
