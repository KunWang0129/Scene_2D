from utils.Scene import Scene
from utils.Shape import Circle, Rectangle

#@# Prompt
prompt = 'Create a scene with a purple square, an orange circle, and a yellow rectangle.'
#@#

# Light gray background color can be represented as a hex color code
light_gray = '#d3d3d3'  # This is a common representation for light gray

# Create a scene with a light gray background
scene = Scene(size=(1024, 768), bg_color=light_gray)

# Create a purple Square, place it, and add it to the scene
square_1 = Rectangle(150, 100, color='purple')
square_1.place_shape_global((250, 400))
scene.add_shape(square_1)

# Create an orange Circle, place it, and add it to the scene
circle_1 = Circle(50, color='orange')
circle_1.place_shape_global((700, 400))
scene.add_shape(circle_1)

# Create a yellow Rectangle, place it, and add it to the scene
rectangle_1 = Rectangle(150, 100, color='yellow')
rectangle_1.place_shape_global((475, 300))
scene.add_shape(rectangle_1)

scene.render("examples/4.png")
