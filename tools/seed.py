import os
import json
import numpy as np
from tqdm import tqdm
from tools.llm import LLM
from assets.key import api_key

class SeedCollector:
    def __init__(self):
        self.llm = LLM()
        # Subject to change
        self.template = """Extract seed words from the descriptions of scene. You should focus on the objects within the scene and extract the most relevant words that describe the scene.
Your answer should have only a list of words. Do not include any other information.
Here is an example:
<example>
Description:
Create a scene with a mountain with some trees, and a bird flying.
Your response:
mountain,trees,bird
</example>
"""

    def run(self, desc, write_file=None):
        if write_file is not None and os.path.exists(write_file):
            with open(write_file, 'r') as file:
                response = file.read()
                print(response)
        else:
            query = f"{self.template}\nCan you write the drawing steps for the following description:\n{desc}\n"
            response = self.llm.run_collect_seed(query)
            if write_file is not None:
                with open(write_file, 'w') as file:
                    file.write(response)

        return response

class SeedRetriever:
    def __init__(self):
        self.examples = [f'{x}.py' for x in range(1, 6)]
        self.collector = SeedCollector()
        self.data_path = './examples/'
        self.seed_path = './assets/seed_words.json'
        if os.path.exists(self.seed_path):
            with open(self.seed_path, 'r') as f:
                self.seeds = json.load(f)
        else:
            self.build()

    def build(self):
        print('Building seed word list')
        self.seeds = []
        for ex in tqdm(self.examples):
            with open(self.data_path + ex, 'r') as f:
                lines = f.readlines()
            desc = "".join(lines)
            first = desc.find('##@##')
            second = desc.find('##@##', first + 6)
            description = desc[first + 6:second]
            description = description.replace("description = ", "").replace("'", "")
            # code = desc[second+5:]
            # code = desc
            # outfile = f'{self.data_path}{ex.replace(".", "_")}description.txt'
            seeds = self.collector.run(description)
            seed_list = seeds.split(',')
            for seed in seed_list:
                if seed not in self.seeds:
                    self.seeds.append(seed)
        with open(self.seed_path, 'w') as f:
            json.dump(self.seeds, f)
    
    def get_seed(self):
        return self.seeds
    
    def add_seed(self, description):
        seeds = self.collector.run(description)
        seed_list = seeds.split(',')
        for seed in seed_list:
            if seed not in self.seeds:
                self.seeds.append(seed)
                with open(self.seed_path, 'w') as f:
                    json.dump(self.seeds, f)
    
