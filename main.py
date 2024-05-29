from utils.generator import SceneGenerator
from tools.vlm import VLM
import os

DIR = 'threecars'
# IMAGE_SUBDIR = 'rendered_scene'
IMAGE_SUBDIR = 'rendered_scene'
descriptions = dict()
filtered_images = []

print("Coming up with candidate scenes ....")
# SceneGenerator().run('')

# Get the description first
example_files = [f for f in os.listdir(DIR) if f.endswith('_0.py') and f != '__init__.py']
# example_files = [f for f in os.listdir(DIR) if f.endswith('.py') and f != '__init__.py']
for file_name in example_files:
    # Construct the full file path
    file_path = os.path.join(DIR, file_name)

    # Open the file and execute the code
    with open(file_path, 'r') as file:
        lines = file.readlines()
    desc = "".join(lines)
    first = desc.find("##@##")
    second = desc.find("##@##", first + 6)
    description = desc[first + 6 : second]
    description = description.replace("description = ", "").replace("'", "")
    image_files = [f"{DIR}/{IMAGE_SUBDIR}/{f}" for f in os.listdir(f"{DIR}") if f.startswith(f"{f.split('_')[0]}_") and f != file_name]
    descriptions[file_name[:-5]] = {"description": description, "path": image_files}

vlm = VLM()
for key, value in descriptions.items():
    print(f"Creating scene for {key} ....")
    print(value["path"])
    response = vlm.run(value["path"], value["description"])
    print(response)
    filtered_images.append(response)
    print("\n")

# TODO: store the filtered images in a directory

# Create a scene with five trees on top of a grass floor
# Create a scene with a sailing boat on the sea in a sunny day

# vlm = VLM()
# desc = "Create a scene with three cars parked on the street"
# image_paths = ["threecars/threecars1.png", "threecars/threecars2.png", "threecars/threecars3.png", "threecars/threecars4.png", "threecars/threecars5.png"]
# response = vlm.run(image_paths, desc)
# print(response.content[0].text)