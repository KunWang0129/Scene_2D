
# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the body of the bird
body = Circle(radius=100, color='white')
body.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(body)

# Create the head of the bird
head = Circle(radius=50, color='yellow')
head.place_shape_local(body, 'above', offset=(0, 50))
scene.add_shape(head)

# Create the eyes of the bird
eye1 = Circle(radius=10, color='black')
eye1.place_shape_local(head, 'left', offset=(30, 0))
scene.add_shape(eye1)

eye2 = Circle(radius=10, color='black')
eye2.place_shape_local(head, 'right', offset=(-30, 0))
scene.add_shape(eye2)

# Create the beak of the bird
beak = Triangle(size=50, color='orange')
beak.place_shape_local(body, 'below', offset=(0, -50))
scene.add_shape(beak)

# Create the wings of the bird
wing1 = Triangle(size=80, color='brown')
wing1.place_shape_local(body, 'left', offset=(-100, 0))
scene.add_shape(wing1)

wing2 = Triangle(size=80, color='brown')
wing2.place_shape_local(body, 'right', offset=(100, 0))
scene.add_shape(wing2)

# Create the feet of the bird
foot1 = Triangle(size=40, color='gray')
foot1.place_shape_local(body, 'below', offset=(-50, -50))
scene.add_shape(foot1)

foot2 = Triangle(size=40, color='gray')
foot2.place_shape_local(body, 'below', offset=(50, -50))
scene.add_shape(foot2)

# Create the beak outline
beak_outline = Rectangle(width=10, height=60, color='black')
beak_outline.place_shape_local(head, 'above', offset=(0, 30))
scene.add_shape(beak_outline)

# Render the scene to an image file
scene.render(filename='bird_scene.png')
