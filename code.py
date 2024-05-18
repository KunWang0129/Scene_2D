
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='white')

# Create the building
building = Rectangle(width=400, height=300, color='gray')
building.place_shape_global((400, 300))
scene.add_shape(building)

# Create the roof
roof = Triangle(size=400, color='red')
roof.place_shape_local(building, 'above')
scene.add_shape(roof)

# Create the door
door = Rectangle(width=100, height=150, color='brown')
door.place_shape_local(building, 'below', offset=(0, -50))
scene.add_shape(door)

# Create the windows
window1 = Rectangle(width=50, height=75, color='blue')
window1.place_shape_local(building, 'right', offset=(-100, 50))
scene.add_shape(window1)

window2 = Rectangle(width=50, height=75, color='blue')
window2.place_shape_local(building, 'left', offset=(100, 50))
scene.add_shape(window2)

# Create the door handle
door_handle = Rectangle(width=10, height=50, color='black')
door_handle.place_shape_local(door, 'right', offset=(-20, 0))
scene.add_shape(door_handle)

# Render the scene
scene.render(filename='house_scene.png')
