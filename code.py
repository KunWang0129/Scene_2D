
from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

# Initialize the scene with dimensions and background color
scene = Scene(size=(1024, 768), bg_color='#f0f8ff')  # Light blue background color

# Create and place the shapes
# 1. A large blue rectangle in the center
rect_1 = Rectangle(400, 300, color='#add8e6')  # Light blue color
rect_1.place_shape_global((512, 384))
scene.add_shape(rect_1)

# 2. Four smaller yellow rectangles around the large rectangle
rect_2 = Rectangle(150, 100, color='#ffff00')  # Yellow color
rect_2.place_shape_local(rect_1, 'left')
scene.add_shape(rect_2)

rect_3 = Rectangle(150, 100, color='#ffff00')
rect_3.place_shape_local(rect_1, 'right')
scene.add_shape(rect_3)

rect_4 = Rectangle(100, 150, color='#ffff00')
rect_4.place_shape_local(rect_1, 'above')
scene.add_shape(rect_4)

rect_5 = Rectangle(100, 150, color='#ffff00')
rect_5.place_shape_local(rect_1, 'below')
scene.add_shape(rect_5)

# 3. A green triangle in the top-right corner
tri_1 = Triangle(200, color='#008000')  # Green color
tri_1.place_shape_global((900, 100))
scene.add_shape(tri_1)

# 4. Three red circles in the bottom-left corner
circle_1 = Circle(50, color='#ff0000')  # Red color
circle_1.place_shape_global((200, 600))
scene.add_shape(circle_1)

circle_2 = Circle(50, color='#ff0000')
circle_2.place_shape_local(circle_1, 'right')
scene.add_shape(circle_2)

circle_3 = Circle(50, color='#ff0000')
circle_3.place_shape_local(circle_2, 'right')
scene.add_shape(circle_3)

# Render the scene and save it to an image file
scene.render("scene.png")
