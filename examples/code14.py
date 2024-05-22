
# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the building
building = Rectangle(width=400, height=300, color='gray')
building.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(building)

# Create the roof
roof = Triangle(size=400, color='red')
roof.place_shape_local(building, 'above')
scene.add_shape(roof)

# Create the door
door = Rectangle(width=80, height=120, color='brown')
door.place_shape_local(building, 'below', offset=(0, -50))
scene.add_shape(door)

# Create the windows
window1 = Rectangle(width=60, height=80, color='blue')
window1.place_shape_local(building, 'left', offset=(50, 50))
scene.add_shape(window1)

window2 = Rectangle(width=60, height=80, color='blue')
window2.place_shape_local(building, 'right', offset=(-50, 50))
scene.add_shape(window2)

# Create the door handle
door_handle = Rectangle(width=10, height=30, color='black')
door_handle.place_shape_local(door, 'center')
scene.add_shape(door_handle)

# Create the chimneys
chimney1 = Rectangle(width=30, height=60, color='gray')
chimney1.place_shape_local(building, 'left', offset=(100, -100))
scene.add_shape(chimney1)

chimney2 = Rectangle(width=30, height=60, color='gray')
chimney2.place_shape_local(building, 'right', offset=(-100, -100))
scene.add_shape(chimney2)

# Create the grass
grass = Rectangle(width=800, height=200, color='green')
grass.place_shape_global((400, 500))
scene.add_shape(grass)

# Create the flowers
flower1 = Circle(radius=10, color='yellow')
flower1.place_shape_local(grass, 'above', offset=(100, -50))
scene.add_shape(flower1)

flower2 = Circle(radius=10, color='yellow')
flower2.place_shape_local(grass, 'above', offset=(300, -70))
scene.add_shape(flower2)

flower3 = Circle(radius=10, color='yellow')
flower3.place_shape_local(grass, 'above', offset=(500, -60))
scene.add_shape(flower3)

# Render the scene to an image file
scene.render(filename='house_scene.png')
