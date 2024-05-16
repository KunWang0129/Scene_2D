
from utils.Shape import Circle, Rectangle, Triangle
from utils.Scene import Scene

# Initialize the scene
scene = Scene(size=(800, 600), bg_color='skyblue')

# Create the sea
sea = Rectangle(width=800, height=400, color='blue')
sea.place_shape_global((400, 300))
scene.add_shape(sea)

# Create the sky
sky = Rectangle(width=800, height=200, color='lightblue')
sky.place_shape_global((400, 100))
scene.add_shape(sky)

# Create the sail
sail = Triangle(size=200, color='white')
sail.place_shape_global((400, 500))
scene.add_shape(sail)

# Create the hull
hull = Rectangle(width=150, height=80, color='brown')
hull.place_shape_local(sail, 'below', offset=(0, 20))
scene.add_shape(hull)

# Create the oars
oar1 = Rectangle(width=50, height=20, color='brown')
oar1.place_shape_local(hull, 'left', offset=(40, 0))
scene.add_shape(oar1)

oar2 = Rectangle(width=50, height=20, color='brown')
oar2.place_shape_local(hull, 'right', offset=(-40, 0))
scene.add_shape(oar2)

# Create the sun
sun = Circle(radius=30, color='yellow')
sun.place_shape_global((700, 100))
scene.add_shape(sun)

# Create the clouds
cloud1 = Circle(radius=40, color='white')
cloud1.place_shape_global((100, 150))
scene.add_shape(cloud1)

cloud2 = Circle(radius=50, color='white')
cloud2.place_shape_global((300, 120))
scene.add_shape(cloud2)

cloud3 = Circle(radius=30, color='white')
cloud3.place_shape_global((550, 180))
scene.add_shape(cloud3)

# Create the waves
wave1 = Triangle(size=80, color='white')
wave1.place_shape_global((200, 550))
scene.add_shape(wave1)

wave2 = Triangle(size=60, color='white')
wave2.place_shape_global((500, 580))
scene.add_shape(wave2)

wave3 = Triangle(size=70, color='white')
wave3.place_shape_global((650, 560))
scene.add_shape(wave3)

# Render the scene
scene.render(filename='sailing_boat_scene.png')
