#@# Prompt
# prompt = 'Create a scnene with mountains and meadows.'
#@#

# Create the Scene object with desired dimensions and background color
scene = Scene(size=(800, 600), bg_color="skyblue")

# Create multiple mountains using Triangle objects
mountain1 = Triangle(size=300, color="darkgray")
mountain1.place_shape_global((300, 400))  # Larger mountain to the left

mountain2 = Triangle(size=200, color="gray")
mountain2.place_shape_global((500, 450))  # Medium-sized mountain in the middle

mountain3 = Triangle(size=250, color="lightgray")
mountain3.place_shape_global((200, 450))  # Smaller mountain on the left side

# Create the ground using a Rectangle object
ground = Rectangle(width=800, height=100, color="green")
ground.place_shape_global((400, 550))  # Position ground at the bottom of the scene

# Add all shapes to the scene
scene.add_shape(mountain1)
scene.add_shape(mountain2)
scene.add_shape(mountain3)
scene.add_shape(ground)
