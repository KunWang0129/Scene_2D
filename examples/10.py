#@# Prompt
prompt = 'Create a scene with four grey circles aggregated together but not touching each other.'
#@#

# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1024, 768), bg_color=cream_white)

# Create four grey circles, place them together but not touching, and add them to the scene
circle_1 = Circle(50, color='grey')
circle_1.place_shape_global((400, 400))
scene.add_shape(circle_1)

circle_2 = Circle(50, color='grey')
circle_2.place_shape_global((520, 400))  # Increase the x-coordinate
scene.add_shape(circle_2)

circle_3 = Circle(50, color='grey')
circle_3.place_shape_global((400, 520))  # Increase the y-coordinate
scene.add_shape(circle_3)

circle_4 = Circle(50, color='grey')
circle_4.place_shape_global((520, 520))  # Increase both the x and y coordinates
scene.add_shape(circle_4)