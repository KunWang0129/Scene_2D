from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

# Cream white background color can be represented as a hex color code
cream_white = '#f5f5dc'  # This is a common representation for cream white

# Create a scene with a cream white background
scene = Scene(size=(1024, 768), bg_color=cream_white)

# Create orange circles and place them in the scene
for i in range(10):
    circle = Circle(50, color='orange')
    circle.place_shape_global((100 + i * 80, 100 + i * 60))
    scene.add_shape(circle)

# Create blue rectangles and place them around the circles
rectangle_1 = Rectangle(400, 100, color='blue', rotation=90)
rectangle_1.place_shape_global((100, 400))
scene.add_shape(rectangle_1)

rectangle_2 = Rectangle(400, 100, color='blue', rotation=90)
rectangle_2.place_shape_global((900, 400))
scene.add_shape(rectangle_2)

rectangle_3 = Rectangle(800, 100, color='blue', rotation=0)
rectangle_3.place_shape_global((300, 100))
scene.add_shape(rectangle_3)

rectangle_4 = Rectangle(800, 100, color='blue', rotation=0)
rectangle_4.place_shape_global((300, 600))
scene.add_shape(rectangle_4)

# Render the scene to an image file
scene.render('scene.png')
