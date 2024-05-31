from utils.generator import SceneGenerator
from tools.vlm import VLM
import os
import shutil

DIR = 'threecars'
IMAGE_SUBDIR = 'rendered_scene'
descriptions = dict()
filtered_images = []

print("Coming up with candidate scenes ....")
# SceneGenerator().run('')

# Get the description first
example_files = [f for f in os.listdir(
    DIR) if f.endswith('_0.py') and f != '__init__.py']
print(example_files)
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
    descriptions[file_name[:-5]] = {"description": description,
                                    "path": image_files, "file_name": file_name[:-5]}

vlm = VLM()
for key, value in descriptions.items():
    print(f"Creating scene for {key} ....")
    print(value["path"])
    response = vlm.run(value["path"], value["description"])
    print(response)
    filtered_images.append(response)
    with open(f"selected_images/{value['file_name']}.png", 'wb') as f:
        shutil.copy(response, f"selected_images/{value['file_name']}.png")
    print("\n")

# Copy the filtered images to directory "selected_images"
os.makedirs('selected_images', exist_ok=True)
for i, image_path in enumerate(filtered_images):
    with open(f"selected_images/{i}.png", 'wb') as f:
        shutil.copy(image_path, f"selected_images/{i}.png")
