import os
from utils.Scene import Scene
from utils.Shape import Circle, Rectangle, Triangle

# Get a list of all files in the 'examples' directory
# example_files = [f for f in os.listdir('examples') if f.endswith('.py') and f != '__init__.py']
example_files = [f for f in os.listdir('test_examples') if f.endswith('.py') and f != '__init__.py']
# example_files = ['code8_0.py']

# Loop through each file
for file_name in example_files:
    # Construct the full file path
    file_path = os.path.join('test_examples', file_name)

    # Open the file and execute the code
    with open(file_path, 'r') as file:
        exec(file.read())

    # Assuming that the 'scene' variable is defined in each file,
    # render the scene and save it as an image
    print(file_name[:-3])
    image = scene.render(f'test_examples/rendered_scene/{file_name[:-3]}.png')