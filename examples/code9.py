
# Import necessary classes from the provided API
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene with dimensions and background color
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the boat body
boat_body = Rectangle(width=400, height=150, color='blue')
boat_body.place_shape_global((400, 300))  # Center of the scene
scene.add_shape(boat_body)

# Create the boat deck
boat_deck = Rectangle(width=350, height=100, color='white')
boat_deck.place_shape_local(boat_body, 'above', offset=(0, 20))
scene.add_shape(boat_deck)

# Create the boat bow
boat_bow = Triangle(size=100, color='gray')
boat_bow.place_shape_local(boat_body, 'left')
scene.add_shape(boat_bow)

# Create the boat stern
boat_stern = Triangle(size=80, color='gray')
boat_stern.place_shape_local(boat_body, 'right')
scene.add_shape(boat_stern)

# Create the boat windows
boat_window1 = Circle(radius=15, color='white')
boat_window1.place_shape_local(boat_body, 'right', offset=(-100, 0))
scene.add_shape(boat_window1)

boat_window2 = Circle(radius=15, color='white')
boat_window2.place_shape_local(boat_body, 'left', offset=(100, 0))
scene.add_shape(boat_window2)

# Create the boat mast
boat_mast = Rectangle(width=10, height=150, color='black')
boat_mast.place_shape_local(boat_deck, 'above')
scene.add_shape(boat_mast)

# Create the boat sail
boat_sail = Triangle(size=150, color='white')
boat_sail.place_shape_local(boat_mast, 'above')
scene.add_shape(boat_sail)

# Render the scene to an image file
scene.render(filename='boat_scene.png')
