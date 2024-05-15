##@##
description = 'Create a scene with a car.'
##@##

# Create a scene with a cream white background
scene = Scene(size=(1024, 768))

wheel_back = Circle(50, color='black')
wheel_back.place_shape_global((370, 475))
scene.add_shape(wheel_back)

wheel_front = Circle(50, color='black')
wheel_front.place_shape_global((650, 475))
scene.add_shape(wheel_front)

body = Rectangle(500, 180, color='red')
body.place_shape_global((512, 384))
scene.add_shape(body)

window = Rectangle(100, 60, color='cyan')
window.place_shape_global((650, 384))
scene.add_shape(window)
