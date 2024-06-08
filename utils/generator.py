import random

from tools.codegen import CodeGenerator
from tools.llm import LLM
from tools.rag import CodeRetriever


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
        self.prompt += "\nHere is the full implementation of the API for your reference:\n"
        with open("utils/Scene.py", "r") as file:
            self.prompt += file.read()
        with open("utils/Shape.py", "r") as file:
            self.prompt += file.read()

    def _sanitize_output(self, text: str):
        _, after = text.split("<code>")
        return after.split("</code>")[0]

    def run(self, input):
        self.init()
        example_codes, description = self.retriever.run(input)

        self.prompt += "\nFollowing are a few simple examples of how to write code in your response:\n"
        for i in range(len(example_codes)):
            self.prompt += f"\n{example_codes[i]}\n"

        self.prompt += f"""
Now write code to {input}.
You should follow these drawing steps:
{description}
Write your code within <code> tags.
"""
        with open('prompt.txt', 'w') as f:
            f.write(self.prompt)
        llm = LLM()
        response = llm.run(self.prompt)
        code = self._sanitize_output(response)
        with open("code.py", "w") as file:
            file.write(code)
