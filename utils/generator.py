import random

from tools.codegen import CodeGenerator
from tools.llm import LLM
from tools.rag import CodeRetriever
import tqdm


class SceneGenerator:
    def __init__(self):
        self.codegen = CodeGenerator()
        self.retriever = CodeRetriever()

    def init(self):
        # Reading the Documentation
        self.prompt = """Write Python code to create a scene layout based on the shapes defined in the API below.
To write the code, you should refer to the following API:
"""
        with open("assets/api.py", "r") as file:
            self.prompt += file.read()

        # Reading the API implementation (Temporary syntax checker)
        self.prompt += (
            "\nHere is the full implementation of the API for your reference:\n"
        )
        with open("utils/Scene.py", "r") as file:
            self.prompt += file.read()
        with open("utils/Shape.py", "r") as file:
            self.prompt += file.read()

    def _sanitize_output( self, text: str):
        _, after = text.split("```python")
        return after.split("```")[0]

    def generate_descriptions(self):
        descriptions = []  # List of descriptions
        for ex in tqdm.tqdm(self.retriever.examples):
            with open(self.retriever.data_path + ex, "r") as f:
                lines = f.readlines()
            desc = "".join(lines)
            first = desc.find("##@##")
            second = desc.find("##@##", first + 6)
            description = desc[first + 6 : second]
            description = description.replace("description = ", "").replace("'", "")
            descriptions.append(description)

        self.input_prompt = """We are creating a diversified dataset of 2D scenes or objects to be used in a RAG system.
Currently we have a few descriptions of scenes or objects and we want to expand on these descriptions to make our dataset more diverse.
These descriptions should be simple but differ from existing ones. Keep in mind that the scenes need to be drawn using 2D shapes like rectangles, circles and triangles, so they can't feature complex objects.
Respond with 10 new descriptions, all consecutive using $$ as separator.
Your response should have only the new descriptions, nothing else. When reading your output I will be doing split on the $$ separtor.
Here are the descriptions that we have so far:
"""

        # MJ
        # self.input_prompt = """We are creating a diverse dataset of 2D scenes and objects
        # and need to generate descriptions of scenes and objects. You are provided
        # with a few example descriptions and are expected to respond with 20 new descriptions.
        # You should separate out the descriptions using '$$'. Your response should have only the new descriptions, nothing else.
        # Here are the example descrptions:"""

        # Rebecca
        # self.input_prompt = """You are a helpful assistant and an excellent thinker.
        # You expand upon the descriptions we will give you next to create new description that considers different scenarios and contexts.
        # You will be given a few example descriptions and you will need to generate 10 new descriptions.
        # You should separate out the descriptions using '$$'.
        # Here are the example descriptions:"""

        for i in range(len(descriptions) - 1):
            self.input_prompt += f"{descriptions[i]}$$"
        self.input_prompt += f"{descriptions[-1]}"
        llm = LLM()
        input = llm.run(self.input_prompt)
        print(f"New LLM generated candidate descriptions:{input}")
        input = input.replace("\n", "").split("$$")
        input = [i for i in input if i != ""]
        print(f"After split: {input}")
        return input

    def generate_code(self, input: str, index="", j=""):
        example_codes, description = self.retriever.run(input)

        self.prompt += (
            "\nFollowing is a simple example of how to write code in your response:\n"
        )
        for i in range(len(example_codes)):
            self.prompt += f"\n{example_codes[i]}\n"

        self.prompt += f"""
Now write code to {input}.
You should follow these drawing steps:
{description}"""

        with open("prompt.txt", "w") as f:
            f.write(self.prompt)
        llm = LLM()
        response = llm.run(self.prompt)
        code = f"""##@##\ndescription = '{input}'\n##@##\n"""
        code += self._sanitize_output(response)
        
        with open(f"../examples/code{index}_{j}.py", "w") as file:
            file.write(code)

    def run(self, input: str = ""):
        self.init()

        if input == "":
            descriptions = self.generate_descriptions()
            for j in range(1):
                for i in range(len(descriptions)):
                    self.generate_code(
                        descriptions[i], len(self.retriever.examples) + i + 1, j
                    )
        else:
            self.generate_code(input)
