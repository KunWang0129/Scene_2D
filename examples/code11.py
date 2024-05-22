
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the rainbow
rainbow_radius = 300
rainbow = Circle(radius=rainbow_radius, color='transparent')
rainbow.place_shape_global((400, 300))
scene.add_shape(rainbow)

# Draw the rainbow colors
rainbow_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
for i in range(7):
    start_angle = i * 90 / 7
    end_angle = (i + 1) * 90 / 7
    rainbow_slice = Circle(radius=rainbow_radius, color=rainbow_colors[i], rotation=start_angle)
    rainbow_slice.place_shape_global((400, 300))
    scene.add_shape(rainbow_slice)

# Create the sun
sun = Circle(radius=50, color='yellow')
sun.place_shape_global((400, 300))
scene.add_shape(sun)

# Create the clouds
cloud1 = Triangle(size=100, color='gray')
cloud1.place_shape_global((100, 550))
scene.add_shape(cloud1)

cloud2 = Triangle(size=100, color='gray')
cloud2.place_shape_global((700, 550))
scene.add_shape(cloud2)

# Create the grass
grass = Rectangle(width=800, height=100, color='green')
grass.place_shape_global((400, 550))
scene.add_shape(grass)

# Render the scene to an image file
scene.render(filename='rainbow_scene.png')
