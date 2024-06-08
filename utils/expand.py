import random
import subprocess
import os
from PIL import Image
from tools.codegen import CodeGenerator
from tools.llm import LLM
from tools.rag import CodeRetriever
from tools.seed import SeedRetriever
from tools.promptgen import PromptGenerator


class Expand:
    def __init__(self):
        self.seed_retriever = SeedRetriever()
        self.prompt_generator = PromptGenerator()
        self.codegen = CodeGenerator()
        self.retriever = CodeRetriever()
        self.num_tries = 5

    def init(self):
        # Reading the Documentation
        self.prompt = """Write Python code to create a scene layout based on the shapes defined in the API below.
To write the code, you should refer to the following API:
"""
        with open("assets/api.py", "r") as file:
            self.prompt += file.read()
        
        # Reading the API implementation (Temporary syntax checker)
        self.prompt += "\nHere is the full implementation of the API for your reference:\n"
        with open("utils/Scene.py", "r") as file:
            self.prompt += file.read()
        with open("utils/Shape.py", "r") as file:
            self.prompt += file.read()

    def _sanitize_output(self, text: str):
        _, after = text.split("<code>")
        return after.split("</code>")[0]

    def evaluate(self, prompt, code):
        approval = False
        # Write the code to code.py
        with open("code.py", "w") as file:
            file.write(code)

        # Run the generated code.py to produce an image
        subprocess.run(["python", "code.py"])

        # Assuming the image is saved as 'generated_image.png' by code.py
        image_path = "output.png"
        if os.path.exists(image_path):
            # Load and visualize the image
            image = Image.open(image_path)
            image.show()

            # Prompt the user to input "y" or "n"
            print(f"Please evaluate the generated image from the following prompt:\n{prompt}")
            user_input = input("Is the generated image satisfactory? (y/n): ").strip().lower()

            if user_input == "y":
                print("Image approved.")
                approval = True
            else:
                print("Image not approved.")
        else:
            print("Image not found. Please ensure code.py generates 'output.png'.")
        
        return approval

    def run(self):
        self.init()
        seeds = self.seed_retriever.get_seed()
        chosen_seed = seeds
        print(f"Seed word chosen: {chosen_seed}")

        prompt_generate_mode = ['explore', 'diverse']
        prompt_gen_mode = prompt_generate_mode[random.randrange(0, 10)%2]
        print(f"Prompt generation mode: {prompt_gen_mode}")

        input = self.prompt_generator.run(chosen_seed, prompt_gen_mode)
        # new_prompt = self.prompt
        for i in range(self.num_tries):
            new_prompt = self.prompt
            example_codes, description = self.retriever.run(input)

            new_prompt += "\nFollowing are a few simple examples of how to write code in your response:\n"
            for i in range(len(example_codes)):
                new_prompt += f"\n{example_codes[i]}\n"

            new_prompt += f"""
Now write code to {input}.
You should follow these drawing steps:
{description}
Write your code within <code> tags.
"""
            with open('prompt.txt', 'w') as f:
                f.write(new_prompt)
        
            llm = LLM()
            response = llm.run(new_prompt)
            code = self._sanitize_output(response)
            code = "##@##\n" + f"description = '{input}'" + "\n##@##\n" + code
            code += "scene.render(filename='output.png')"
            approval = self.evaluate(input, code)
            if approval:
                break
        if approval:
            self.seed_retriever.add_seed(input)
            self.retriever.add_example(input, description, code)
