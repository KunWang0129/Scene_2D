from utils.Scene import Scene
from utils.Shape import Rectangle, Triangle

#@# Prompt
prompt = 'Create a scene with 4 rectangles around a triangle in the center.'
#@#

# Set the background color as a soft blue
soft_blue = '#add8e6'  # Hex code for light blue

# Create a scene with a soft blue background
scene = Scene(size=(1024, 768), bg_color=soft_blue)

# Create a central triangle with a deep blue color
central_triangle = Triangle(80, color='navy')
central_triangle.place_shape_global((512, 384))  # Placing it at the center of the scene
scene.add_shape(central_triangle)

# Create four rectangles with different colors

# Create a red rectangle above the triangle
rectangle_1 = Rectangle(120, 60, color='red')
rectangle_1.place_shape_local(central_triangle, 'above')  # 100 pixels above the triangle
scene.add_shape(rectangle_1)

# Create a green rectangle below the triangle
rectangle_2 = Rectangle(120, 60, color='green')
rectangle_2.place_shape_local(central_triangle, 'below')  # 100 pixels below the triangle
scene.add_shape(rectangle_2)

# Create a yellow rectangle to the left of the triangle
rectangle_3 = Rectangle(60, 120, color='yellow')
rectangle_3.place_shape_local(central_triangle, 'left')  # 100 pixels to the left of the triangle
scene.add_shape(rectangle_3)

# Create a purple rectangle to the right of the triangle
rectangle_4 = Rectangle(60, 120, color='purple')
rectangle_4.place_shape_local(central_triangle, 'right')  # 100 pixels to the right of the triangle
scene.add_shape(rectangle_4)

scene.render("examples/6.png")