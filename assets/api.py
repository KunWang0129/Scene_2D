"""
Scene Setup:
- Axes: x (left to right), y (top to bottom).
- Dimensions: Configured upon scene initialization with width and height.
- Colors: Background color is set during scene initialization.
Create scene with scene = Scene(size=(WIDTH, HEIGHT), bg_color='COLOR'). Manage objects by their shape types such as 'circle1', 'rectangle2', etc.

API for Adding Shapes:
- scene.add_shape(shape): Add shapes to the scene. Supported shapes include Circle, Rectangle, Triangle.
- scene.remove_shape(shape): Remove a shape from the scene.

Shape Classes and Initialization:
- Circle(radius, color='black', rotation=0): Initialize a circle with radius, color, and rotation.
- Rectangle(width, height, color='black', rotation=0): Initialize a rectangle with width, height, color, and rotation.
- Triangle(size, color='black', rotation=0): Initialize a triangle with side size, color, and rotation.

Shape Positioning:
- shape.place_shape_global(position): Set global position of the shape.
- shape.place_shape_local(reference_shape, position): Position the shape relative to another shape (positions include 'left', 'right', 'above', 'below').

Rendering and Visual Setup:
- scene.create_background(): Creates a background image for the scene.
- scene.render(filename='scene.png'): Renders the entire scene to an image file with specified filename.
- Draw functions for each shape are internal methods used during the rendering process to depict shapes on the canvas.

Object Access and Manipulation:
- Direct scene.shapes for accessing list of shapes.
- Properties for shapes include color, position, and rotation.
- Methods for moving and rotating shapes are provided to adjust their positions and orientations within the scene.

Constraints:
- Only basic constraints are shown through shape placement methods. No overlaps or out of bounds constraints are handled explicitly in the API.

The general structure of the program is as follows:
1. Initialize scene with dimensions.
2. Add shapes (circles, rectangles, triangles)
3. Place objects in the scene.

Note: Make sure you follow the above APIs, and structure of the program and add necessary amount of objects to make it look full. 
"""