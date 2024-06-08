from tools.llm import LLM
import os
import json
from tqdm import tqdm
import random

class PromptGenerator:
    def __init__(self):
        self.llm = LLM()
        self.data_path = './examples/'
        self.use_expanded = True
        if self.use_expanded:
            self.embd_path = './assets/rag_embeddings_expanded.json'
        else:
            self.embd_path = './assets/rag_embeddings.json'

        if os.path.exists(self.embd_path):
            with open(self.embd_path, 'r') as f:
                self.embeddings = json.load(f)
            self.num_examples = len(self.embeddings)
            self.examples = [f'{x}.py' for x in range(1, self.num_examples + 1)]
        else:
            self.num_examples = 5
            self.examples = [f'{x}.py' for x in range(1, self.num_examples + 1)]


        self.prompt = []
        self.read_prompts()

        self.template_start = """We are creating a diversified dataset of 2D scenes or objects to be used in a RAG system.
Currently we have a few descriptions of scenes or objects and we want to expand on these descriptions to make our dataset more diverse.
These descriptions should be simple but differ from existing ones. Keep in mind that the scenes need to be drawn using 2D shapes like rectangles, circles and triangles, so they can't feature complex objects."""

        self.template_explore = """You are provided a list of seed words. You should come up with one new scene description within <description> tags.
Before writing the description, you should first select one object from the seed word list. Then you come up with an object not from the seed word list. Your description should only contain these two objects.
Document your thought process within <thinking> tags.
Here is an example:
<example>
Seed Words:
sky, mountain
Your response:
<thinking>
I will select the object 'sky' from the seed word list and come up with a new object 'bird'.
</thinking>
<description>
Create a scene with two birds flying in the sky.
</description>
</example>
"""
        self.template_diverse = """You are provided a list of seed words. You should come up with one new scene description within <description> tags.
Before writing the description, you should first select two objects from the seed word list. Your description should only contain these two objects. You are encouraged to include multiple instances of the same objects in the description.
Document your thought process within <thinking> tags.
Here is an example:
<example>
Seed Words:
mountain, sun, tree, cloud, house
Your response:
<thinking>
I will select the object 'sun' and 'tree' from the seed word list.
</thinking>
<description>
Create a scene with five trees in a sunny day.
</description>
</example>
"""

    def read_prompts(self):
        print('Reading Previous Prompts')
        for ex in tqdm(self.examples):
            with open(self.data_path + ex, 'r') as f:
                lines = f.readlines()
            desc = "".join(lines)
            first = desc.find('##@##')
            second = desc.find('##@##', first + 6)
            description = desc[first + 6:second]
            description = description.replace("description = ", "").replace("'", "")
            self.prompt.append(description)
    
    def select_prompt(self):
        return random.sample(self.prompt, 10)
        
    def run(self, seeds, mode="diverse"):
        self.template = f"{self.template_start}"

        selected_prompts = self.select_prompt()
        self.template += f"""Here are five selections of existing scene descriptions, make sure the new description is different from these selctions:
<previous>
{selected_prompts}
</previous>"""
        if mode == "explore":
            self.template += f"\n{self.template_explore}"
        elif mode == "diverse":
            self.template += f"\n{self.template_diverse}"
        else:
            raise ValueError("Invalid mode. Choose 'explore' or 'diverse'.")

        query = f"""{self.template}
Seed Words:
{seeds}
Your response:"""
        response = self.llm.run_generate_prompt(query)
        return self.sanitize_output(response)
    
    def sanitize_output(self, text: str):
        _, after = text.split("<description>")
        return after.split("</description>")[0].replace("\n", "")