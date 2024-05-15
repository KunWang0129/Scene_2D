#@# Prompt
# prompt = 'Create a scene with a table.'
#@#

# Create the Scene object with desired dimensions and background color
scene = Scene(size=(800, 600), bg_color="lightgray")

# Create the table using a Rectangle object
table_top = Rectangle(width=300, height=30, color="brown")
table_top.place_shape_global((400, 300))  # Center the table's top

# Position the legs directly under the table top
table_leg1 = Rectangle(width=20, height=100, color="brown")
table_leg1.place_shape_global((275, 365))  # Left leg directly beneath the left side of the table top

table_leg2 = Rectangle(width=20, height=100, color="brown")
table_leg2.place_shape_global((525, 365))  # Right leg directly beneath the right side of the table top

# Add all shapes to the scene
scene.add_shape(table_top)
scene.add_shape(table_leg1)
scene.add_shape(table_leg2)
