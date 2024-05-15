#@# Prompt
prompt = 'Create a scene with four grey squares aggregated together but not touching each other.'
#@#

# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1024, 768), bg_color=cream_white)

# Create four grey squares, place them together but not touching, and add them to the scene
square_1 = Rectangle(100, 100, color='grey')
square_1.place_shape_global((400, 400))
scene.add_shape(square_1)

square_2 = Rectangle(100, 100, color='grey')
square_2.place_shape_global((510, 400))  # Increase the x-coordinate
scene.add_shape(square_2)

square_3 = Rectangle(100, 100, color='grey')
square_3.place_shape_global((400, 510))  # Increase the y-coordinate
scene.add_shape(square_3)

square_4 = Rectangle(100, 100, color='grey')
square_4.place_shape_global((510, 510))  # Increase both the x and y coordinates
scene.add_shape(square_4)