
# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='lightgreen')

# Create the ball
ball = Circle(radius=100, color='white')
ball.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(ball)

# Create the ball's outline
ball_outline = Circle(radius=95, color='black')
ball_outline.place_shape_local(ball, 'global')
scene.add_shape(ball_outline)

# Create the ball's highlights
highlight1 = Circle(radius=20, color='white')
highlight1.place_shape_local(ball, 'right', offset=(-40, 0))
scene.add_shape(highlight1)

highlight2 = Circle(radius=20, color='white')
highlight2.place_shape_local(ball, 'left', offset=(40, 0))
scene.add_shape(highlight2)

# Create the ball's shadow
ball_shadow = Triangle(size=150, color='gray', rotation=45)
ball_shadow.place_shape_local(ball, 'above', offset=(0, -50))
scene.add_shape(ball_shadow)

# Render the scene to an image file
scene.render(filename='ball_scene.png')
