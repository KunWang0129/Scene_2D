from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

#@# Prompt
prompt = 'Create a scene with a sky blue background, a blue rectangle in the middle surrounded by four yellow smaller rectangles square, a green triangle on the top left with some rotation and a red circle bottom right.'
#@#

# Initialize the scene with dimensions and background color
scene = Scene(size=(1024, 768), bg_color='#87CEEB')  # Sky blue background

# Create a large blue rectangle as the main element
main_rect = Rectangle(400, 300, color='#1E90FF')  # Dodger blue
main_rect.place_shape_global((512, 384))
scene.add_shape(main_rect)

# Create four smaller yellow rectangles around the main rectangle
small_rect_1 = Rectangle(150, 100, color='#FFFF00')  # Yellow
small_rect_1.place_shape_local(main_rect, 'left')
scene.add_shape(small_rect_1)

small_rect_2 = Rectangle(150, 100, color='#FFFF00')
small_rect_2.place_shape_local(main_rect, 'right')
scene.add_shape(small_rect_2)

small_rect_3 = Rectangle(100, 150, color='#FFFF00')
small_rect_3.place_shape_local(main_rect, 'above')
scene.add_shape(small_rect_3)

small_rect_4 = Rectangle(100, 150, color='#FFFF00')
small_rect_4.place_shape_local(main_rect, 'below')
scene.add_shape(small_rect_4)

# Create a green triangle in the top-left corner
triangle_1 = Triangle(150, color='#008000', rotation=25)  # Green
triangle_1.place_shape_global((150, 150))
scene.add_shape(triangle_1)

# Create a red circle in the bottom-right corner
circle_1 = Circle(75, color='#FF0000')  # Red
circle_1.place_shape_global((900, 600))
scene.add_shape(circle_1)

# Render the scene and save it to an image file
scene.render("examples/5.png")