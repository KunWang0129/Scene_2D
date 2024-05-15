
from PIL import Image, ImageDraw

from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='lightblue')

# 1. Add a rectangle in the center of the scene (car body)
car_body = Rectangle(width=300, height=150, color='gray')
car_body.place_shape_global((400, 300))
scene.add_shape(car_body)

# 2. Add two smaller rectangles on top of the car body (windows)
window1 = Rectangle(width=100, height=50, color='white')
window1.place_shape_local(car_body, 'above', offset=(0, 20))
scene.add_shape(window1)

window2 = Rectangle(width=100, height=50, color='white')
window2.place_shape_local(car_body, 'above', offset=(0, -20))
scene.add_shape(window2)

# 3. Add two circles at the bottom of the car body (wheels)
wheel1 = Circle(radius=30, color='black')
wheel1.place_shape_local(car_body, 'below', offset=(-80, 0))
scene.add_shape(wheel1)

wheel2 = Circle(radius=30, color='black')
wheel2.place_shape_local(car_body, 'below', offset=(80, 0))
scene.add_shape(wheel2)

# 4. Add a smaller rectangle at the front of the car body (front bumper)
front_bumper = Rectangle(width=50, height=30, color='gray')
front_bumper.place_shape_local(car_body, 'left', offset=(0, 0))
scene.add_shape(front_bumper)

# 5. Add another smaller rectangle at the back of the car body (rear bumper)
rear_bumper = Rectangle(width=50, height=30, color='gray')
rear_bumper.place_shape_local(car_body, 'right', offset=(0, 0))
scene.add_shape(rear_bumper)

# Render the scene
scene.render('car_scene.png')
