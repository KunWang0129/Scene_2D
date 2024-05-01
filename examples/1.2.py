from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

#@# Prompt
prompt = 'Create a scene with a red square, surrounded by four grey circles.'
#@#

# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1024, 768), bg_color=cream_white)


# Create an red Rectangle, place it, and add it to the scene
triangle_1 = Triangle(100, color='red')
triangle_1.place_shape_global((600, 400))
scene.add_shape(triangle_1)

# Create grey circles, place it around the rectangle, and add it to the scene
# The circles are placed to the left, right, above, and below the rectangle
circle_1 = Circle(50, color='grey')
circle_1.place_shape_local(triangle_1, 'left')
scene.add_shape(circle_1)

circle_2 = Circle(50, color='grey')
circle_2.place_shape_local(triangle_1, 'right')
scene.add_shape(circle_2)

circle_3 = Circle(50, color='grey')
circle_3.place_shape_local(triangle_1, 'above')
scene.add_shape(circle_3)

circle_4 = Circle(50, color='grey')
circle_4.place_shape_local(triangle_1, 'below')
scene.add_shape(circle_4)

# Render the scene and save it to an image file
scene.render("examples/1.2.png")
