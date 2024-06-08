
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='lightblue')

# Create the sea
sea = Rectangle(width=800, height=400, color='blue')
sea.place_shape_global((400, 500))
scene.add_shape(sea)

# Create the sky
sky = Rectangle(width=800, height=300, color='lightblue')
sky.place_shape_global((400, 150))
scene.add_shape(sky)

# Create the sun
sun = Circle(radius=50, color='yellow')
sun.place_shape_global((700, 100))
scene.add_shape(sun)

# Create the sailing boat
# Boat body
boat_body = Rectangle(width=200, height=100, color='white')
boat_body.place_shape_global((400, 450))
scene.add_shape(boat_body)

# Sail
sail = Triangle(size=150, color='white')
sail.place_shape_local(boat_body, 'above', offset=(0, -50))
scene.add_shape(sail)

# Boat keel
keel_1 = Rectangle(width=20, height=50, color='black')
keel_1.place_shape_local(boat_body, 'below', offset=(-40, 0))
scene.add_shape(keel_1)

keel_2 = Rectangle(width=20, height=50, color='black')
keel_2.place_shape_local(boat_body, 'below', offset=(40, 0))
scene.add_shape(keel_2)

# Mast
mast = Rectangle(width=20, height=100, color='brown')
mast.place_shape_local(boat_body, 'above', offset=(0, -50))
scene.add_shape(mast)

# Sails
sail_1 = Triangle(size=50, color='white')
sail_1.place_shape_local(mast, 'left', offset=(-10, 0))
scene.add_shape(sail_1)

sail_2 = Triangle(size=50, color='white')
sail_2.place_shape_local(mast, 'right', offset=(10, 0))
scene.add_shape(sail_2)

# Bow
bow = Rectangle(width=20, height=50, color='white')
bow.place_shape_local(boat_body, 'left', offset=(-100, 0))
scene.add_shape(bow)

# Stern
stern = Rectangle(width=20, height=50, color='white')
stern.place_shape_local(boat_body, 'right', offset=(100, 0))
scene.add_shape(stern)

# Render the scene
scene.render('sailing_boat_scene.png')
scene.render(filename='output.png')
