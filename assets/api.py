"""
Scene Setup:
- Axes: x (left to right), y (top to bottom).
- Dimensions: Configured upon scene initialization with width and height.
- Colors: Background color is set during scene initialization.
Create scene with scene = Scene(size=(WIDTH, HEIGHT), bg_color='COLOR'). Manage objects by their shape types such as 'circle1', 'rectangle2', etc.
 
API for Adding Shapes:
- scene.add_shape(shape): Add shapes to the scene. Supported shapes include Circle, Rectangle, Triangle.
 
Shape Classes and Initialization:
- Circle(radius, color='black'): Initialize a circle with radius, color.
- Rectangle(width, height, color='black'): Initialize a rectangle with width, height, color.
- Triangle(size, color='black'): Initialize a triangle with side size, color.
 
Shape Positioning:
- shape.place_shape_global(position): Set global position of the shape.
- shape.place_shape_local(reference_shape, position, offset): Position the shape relative to another shape (position can be 'left', 'right', 'above', 'below', 'center').
 
Rendering and Visual Setup:
- scene.render(filename='scene.png'): Renders the entire scene to an image file with specified filename.
- Draw functions for each shape are internal methods used during the rendering process to depict shapes on the canvas.
 
Object Access and Manipulation:
- Direct scene.shapes for accessing list of shapes.
- Properties for shapes include color, position.
- Methods for moving is provided to adjust their positions and orientations within the scene.
 
The general structure of the program is as follows:
1. Initialize scene with dimensions.
2. Add shapes (circles, rectangles, triangles)
3. Place objects in the scene.
 
Note: Make sure you follow the above APIs, and structure of the program and add necessary amount of objects to make it look full. 
"""