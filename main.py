from utils.generator import SceneGenerator
from tools.vlm import VLM, BLIP
import os
import shutil

DIR = 'threecars'
IMAGE_SUBDIR = 'rendered_scene'
descriptions = dict()

print("Coming up with candidate scenes ....")
# SceneGenerator().run('')

# Get the description first
example_files = [f for f in os.listdir(
    DIR) if f.endswith('_0.py') and f != '__init__.py']

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
    description = desc[first + 6: second]
    description = description.replace("description = ", "").replace("'", "")
    image_files = [f"{DIR}/{IMAGE_SUBDIR}/{f}" for f in os.listdir(f"{DIR}/{IMAGE_SUBDIR}") if f.startswith(
        f"{f.split('_')[0]}") and f.endswith("png") and f != file_name]
    image_files = sorted(image_files, key=lambda x: int(x.split('_')[-1].split('.')[0]))
    descriptions[file_name[:-5]] = {"description": description,
                                    "path": image_files, "file_name": file_name[:-5]}

vlm = VLM()

for key, value in descriptions.items():
    file = vlm.run(value['path'], value['description'], value['file_name'])
    with open(f"selected_images/{value['file_name']}.png", 'wb') as f:
        shutil.copy(file, f"selected_images/{value['file_name']}.png") 

