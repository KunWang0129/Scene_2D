from tools.llm import LLM
class CodeGenerator:
    def __init__(self):
        self.llm = LLM()
        
    def _sanitize_output(self, text: str):
        _, after = text.split("```python")
        return after.split("```")[0]

    def run(self, prompt):
        return self._sanitize_output(self.llm.run(prompt))