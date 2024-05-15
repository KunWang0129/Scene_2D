#@# Prompt
prompt = 'Create a scene with four grey triangles aggregated together but not touching each other.'
#@#

# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1024, 768), bg_color=cream_white)

# Create four grey triangles, place them together but not touching, and add them to the scene
triangle_1 = Triangle(100, color='grey')
triangle_1.place_shape_global((400, 400))
scene.add_shape(triangle_1)

triangle_2 = Triangle(100, color='grey')
triangle_2.place_shape_global((510, 400))  # Increase the x-coordinate
scene.add_shape(triangle_2)

triangle_3 = Triangle(100, color='grey')
triangle_3.place_shape_global((400, 510))  # Increase the y-coordinate
scene.add_shape(triangle_3)

triangle_4 = Triangle(100, color='grey')
triangle_4.place_shape_global((510, 510))  # Increase both the x and y coordinates
scene.add_shape(triangle_4)