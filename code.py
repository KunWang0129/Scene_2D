
from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

# Create a scene with a light blue background
scene = Scene(size=(1200, 800), bg_color='#ADD8E6')

# Create a large blue rectangle as the main element
blue_rect = Rectangle(width=600, height=400, color='#1E90FF')
blue_rect.place_shape_global((400, 300))
scene.add_shape(blue_rect)

# Create four smaller yellow rectangles around the blue rectangle
yellow_rect1 = Rectangle(width=200, height=150, color='#FFFF00')
yellow_rect1.place_shape_local(blue_rect, 'left')
scene.add_shape(yellow_rect1)

yellow_rect2 = Rectangle(width=200, height=150, color='#FFFF00')
yellow_rect2.place_shape_local(blue_rect, 'right')
scene.add_shape(yellow_rect2)

yellow_rect3 = Rectangle(width=200, height=150, color='#FFFF00')
yellow_rect3.place_shape_local(blue_rect, 'above')
scene.add_shape(yellow_rect3)

yellow_rect4 = Rectangle(width=200, height=150, color='#FFFF00')
yellow_rect4.place_shape_local(blue_rect, 'below')
scene.add_shape(yellow_rect4)

# Create a green triangle in the center of the scene
green_triangle = Triangle(size=200, color='#008000')
green_triangle.place_shape_global((600, 400))
scene.add_shape(green_triangle)

# Create four red circles around the green triangle
red_circle1 = Circle(radius=50, color='#FF0000')
red_circle1.place_shape_local(green_triangle, 'left')
scene.add_shape(red_circle1)

red_circle2 = Circle(radius=50, color='#FF0000')
red_circle2.place_shape_local(green_triangle, 'right')
scene.add_shape(red_circle2)

red_circle3 = Circle(radius=50, color='#FF0000')
red_circle3.place_shape_local(green_triangle, 'above')
scene.add_shape(red_circle3)

red_circle4 = Circle(radius=50, color='#FF0000')
red_circle4.place_shape_local(green_triangle, 'below')
scene.add_shape(red_circle4)

# Render the scene and save it to an image file
scene.render("scene.png")
