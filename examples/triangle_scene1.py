from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

#@# Prompt
prompt = 'Create a scene with eight triangles, each with a different color.'
#@#

# Light gray background color can be represented as a hex color code
light_gray = '#d3d3d3'  # This is a common representation for light gray

# Create a scene with a light gray background
scene = Scene(size=(1024, 768), bg_color=light_gray)

# Create triangles with different colors and placements

# Create a red triangle, place it and add it to the scene
triangle_1 = Triangle(50, color='red')
triangle_1.place_shape_global((250, 400))
scene.add_shape(triangle_1)

# Create a blue triangle, place it and add it to the scene
triangle_2 = Triangle(50, color='blue')
triangle_2.place_shape_global((350, 400))
scene.add_shape(triangle_2)

# Create a green triangle, place it and add it to the scene
triangle_3 = Triangle(50, color='green')
triangle_3.place_shape_local(triangle_1, 'left')
scene.add_shape(triangle_3)

# Create a yellow triangle, place it and add it to the scene
triangle_4 = Triangle(50, color='yellow')
triangle_4.place_shape_local(triangle_2, 'right')
scene.add_shape(triangle_4)

# Create a purple triangle, place it and add it to the scene
triangle_5 = Triangle(50, color='purple')
triangle_5.place_shape_local(triangle_3, 'above')
scene.add_shape(triangle_5)

# Create an orange triangle, place it and add it to the scene
triangle_6 = Triangle(50, color='orange')
triangle_6.place_shape_local(triangle_4, 'below')
scene.add_shape(triangle_6)

# Create a pink triangle, place it and add it to the scene
triangle_7 = Triangle(50, color='pink')
triangle_7.place_shape_local(triangle_5, 'left')
scene.add_shape(triangle_7)

# Create a cyan triangle, place it and add it to the scene
triangle_8 = Triangle(50, color='cyan')
triangle_8.place_shape_local(triangle_6, 'right')
scene.add_shape(triangle_8)

# Render the scene and save it to an image file
scene.render("examples/triangles_scene1.png")