import random

from tools.codegen import CodeGenerator
from tools.llm import LLM
from tools.rag import CodeRetriever

class SceneGenerator:
    def __init__(self):
        self.codegen = CodeGenerator()
        # self.retriever = CodeRetriever()
        self.header = """
import math
import numpy as np
from utils.scene import Scene
# from utils.constraints import Constraints
"""
    def init(self):
        self.prompt = """
You are a Large Language Model expert at writing code for creating scene layouts. Write Python code to create a different scene layout based on the shapes defined in the API below.
To help you write the code, you should refer to the following APIs:
"""
        with open('../assets/api.py', 'r') as file:
            self.prompt += file.read()


    def _sanitize_output(self, text: str):
        _, after = text.split("```python")
        return after.split("```")[0]
        

    def run(self):
        self.init()

        self.prompt += "Following is an example that creates a scene with a square with four circles around: \n"
        
        #example_inputs, example_codes = self.retriever.run(input)
        with open('../examples/1.5.py', 'r') as file:
            self.prompt += file.read()
        
        # self.prompt += "Following are a few examples of how you should respond: \n"
#         for i in range(len(example_inputs)):
#             self.prompt += f"""
# User Input:
# {example_inputs[i]}
# Your Response:
# {example_codes[i]}
# """
        # if history != "\n":
        #     self.prompt += "The following is the history of the user inputs and your responses: \n"
        #     self.prompt += history
        #     self.prompt += "Now continue to write code based on further user inputs. \n"
            
        # self.prompt += f"\nUser Input: \n{input} \n"
        # self.prompt += "Your Response: \n"
        # with open('prompt.txt', 'w') as f:
        #     f.write(self.prompt)
        #print(self.prompt)
        llm = LLM()
        response = llm.run(self.prompt)
        print(response.content[0].text)
        code = self._sanitize_output(response.content[0].text)
        print(code)
        with open('../code.py', 'w') as file:
            file.write(code)
        #response = self.header + response
        #return response