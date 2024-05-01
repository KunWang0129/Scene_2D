from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

#@# Prompt
prompt = 'Create a scene with a green triangle, a red triangle, and a blue triangle.'
#@#

# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1024, 768), bg_color=cream_white)


# Create an green Triangle, place it, and add it to the scene
triangle_1 = Triangle(100, color='green')
triangle_1.place_shape_global((600, 400))
scene.add_shape(triangle_1)

# Create a red Triangle, place it, and add it to the scene
triangle_2 = Triangle(100, color='red')
triangle_2.place_shape_global((400, 400))
scene.add_shape(triangle_2)

# Create a blue Triangle, place it, and add it to the scene
triangle_3 = Triangle(100, color='blue')
triangle_3.place_shape_global((500, 300))
scene.add_shape(triangle_3)

# Render the scene and save it to an image file
scene.render("examples/2.png")