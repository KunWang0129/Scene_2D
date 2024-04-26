import random
from tools.llm import LLM
from tools.rag import CodeRetriever

class SceneGenerator:
    def __init__(self):
        # self.codegen = CodeGenerator(mode='accurate')
        # self.retriever = CodeRetriever()
        self.header = """
import math
import numpy as np
from utils.scene import Scene
# from utils.constraints import Constraints
"""
    def init(self):
        self.prompt = """
You are a Large Language Model expert at writing code for creating scene layouts. Given the user query, you are supposed to respond by writing Python code to create a scene layout.
To help you write the code, you should refer to the following APIs:
"""
        with open('assets/api.py', 'r') as file:
            self.prompt += file.read()
        

    def run(self, input, history=None):
        self.init()
        
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
        response = self.codegen.run(self.prompt)
        response = self.header + response
        return response
    
class Scene2D:
    def __init__(self):
        self.MAX_TRIALS=5

    def run(self, user_input, history=None):
        from tqdm import tqdm
        print("Coming up with candidate scenes ....")
        codes = SceneGenerator().run(user_input, history=history)
        # codes, feedbacks, scene_graphs = SceneGeneratorWithAutoCorrection().run(user_input, history=history)

        # print("Resolving constraints....")
        # for i in tqdm(range(self.MAX_TRIALS)):
        #     codes, feedbacks, scene_graphs = ConstraintResolver(codes, feedbacks, scene_graphs).run()
        #     if feedbacks == 0:
        #         break
        
        # if i == self.MAX_TRIALS-1:
        #     print("Failed to generate scene! Please try changing the hyperparamers or the user input.")
        #     return None
        
        print("Generating final scene....")
        code = exec(codes, export=True)
        print(code)
        print("Scene Successfully Generated! for user input: ", user_input)
        return codes