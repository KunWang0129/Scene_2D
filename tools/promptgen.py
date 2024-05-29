from tools.llm import LLM
class PromptGenerator:
    def __init__(self):
        self.llm = LLM()
        self.template = """We are creating a diversified dataset of 2D scenes or objects to be used in a RAG system.
Currently we have a few descriptions of scenes or objects and we want to expand on these descriptions to make our dataset more diverse.
These descriptions should be simple but differ from existing ones. Keep in mind that the scenes need to be drawn using 2D shapes like rectangles, circles and triangles, so they can't feature complex objects.
You are provided a series of seed words that you can include in your prompt. Optionally, you can also include new seed words in your prompt. You are encouraged to include multiple instances of the same object.
Your answer should be a single sentence, do not include descriptions of the scene.
Here is an example:
<example>
Seed Words:
Trees, Mountain
Your response:
Create a scene with two trees next to a mountain.
</example>
"""
        

    def run(self, seeds):
        query = f"{self.template}\nCan you generate a prompt with the following seed:\n{seeds}\nYour response:"
        response = self.llm.run_generate_prompt(query)

        return response