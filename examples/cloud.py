#@# Prompt
prompt = 'Create a scene with five aggregated circles to form the shape of a cloud.'
#@#

# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1024, 768), bg_color=cream_white)

# Create five light blue circles, arrange them to form a cloud-like shape, and add them to the scene
circle_1 = Circle(80, color='#87CEEB')  # Light blue color
circle_1.place_shape_global((300, 350))  # Adjust coordinates to form cloud-like shape
scene.add_shape(circle_1)

circle_2 = Circle(90, color='#87CEEB')  # Light blue color
circle_2.place_shape_global((420, 350))  # Adjust coordinates to form cloud-like shape
scene.add_shape(circle_2)

circle_3 = Circle(100, color='#87CEEB')  # Light blue color
circle_3.place_shape_global((550, 350))  # Adjust coordinates to form cloud-like shape
scene.add_shape(circle_3)

circle_4 = Circle(90, color='#87CEEB')  # Light blue color
circle_4.place_shape_global((380, 280))  # Adjust coordinates to form cloud-like shape
scene.add_shape(circle_4)

circle_5 = Circle(80, color='#87CEEB')  # Light blue color
circle_5.place_shape_global((500, 280))  # Adjust coordinates to form cloud-like shape
scene.add_shape(circle_5)
