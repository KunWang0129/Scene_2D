import random

from tools.codegen import CodeGenerator
from tools.llm import LLM
from tools.rag import CodeRetriever


class SceneGenerator:
    def __init__(self):
        self.codegen = CodeGenerator()
        self.retriever = CodeRetriever()
        self.header = """
import math
import numpy as np
from utils.scene import Scene
"""

    def init(self):
        # Reading the Documentation
        self.prompt = """
You are a Large Language Model expert at writing code for creating scene layouts. Write Python code to create a different scene layout based on the shapes defined in the API below.\nTo help you write the code, you should refer to the following APIs:
"""
        with open("assets/api.py", "r") as file:
            self.prompt += file.read()
        
        # Reading the API implementation (Temporary syntax checker)
        self.prompt += """
You are required to write Python code to create a scene layout based on the shapes defined in the API above. The scene should be full and complete, with all the shapes placed in a way that makes the scene look full. Make sure you follow the APIs and structure of the program and add the necessary amount of objects to make it look full."""
        self.prompt += """Here is the full implementation of the API for your reference: \n"""
        with open("utils/Scene.py", "r") as file:
            self.prompt += file.read()
        with open("utils/Shape.py", "r") as file:
            self.prompt += file.read()
        


    def _sanitize_output(self, text: str):
        _, after = text.split("```python")
        return after.split("```")[0]

    def run(self, input, history = None):
        self.init()
        print('input: ', input)
        example_inputs, example_codes = self.retriever.run(input)

        self.prompt += "Following are a few examples of how you should respond: \n"
        for i in range(len(example_inputs)):
            self.prompt += f"""
        User Input:
        {example_inputs[i]}
        Your Response:
        {example_codes[i]}
        """
        # if history != "\n":
        #     self.prompt += "The following is the history of the user inputs and your responses: \n"
        #     self.prompt += history
        #     self.prompt += "Now continue to write code based on further user inputs. \n"

        self.prompt += f"\nUser Input: \n{input} \n"
        self.prompt += "Your Response: \n"
        with open('prompt.txt', 'w') as f:
            f.write(self.prompt)
        print(self.prompt)
        llm = LLM()
        response = llm.run(self.prompt)
        print(response.content[0].text)
        code = self._sanitize_output(response.content[0].text)
        print(code)
        with open("code.py", "w") as file:
            file.write(code)
        # response = self.header + response
        # return response
