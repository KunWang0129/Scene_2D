#@# Prompt
prompt = 'Create a scene with red circle surrounded by three light blue triangles.'
#@#

# Initialize the scene with dimensions and background color
scene = Scene(size=(1024, 768))

# Create a large blue rectangle as the main element
main_circle = Circle(75, color='#FF0000')  # Red
main_circle.place_shape_global((512, 384))
scene.add_shape(main_circle)

# Create three smaller triangles around the main circle
small_triangle_1 = Triangle(150, color='#87CEEB')  # Blue
small_triangle_1.place_shape_local(main_circle, 'left')
scene.add_shape(small_triangle_1)

small_triangle_2 = Triangle(150, color='#87CEEB')
small_triangle_2.place_shape_local(main_circle, 'right')
scene.add_shape(small_triangle_2)

small_triangle_3 = Triangle(150, color='#87CEEB')
small_triangle_3.place_shape_local(main_circle, 'above')
scene.add_shape(small_triangle_3)