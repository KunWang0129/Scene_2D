from tools.llm import LLM
class CodeGenerator:
    def __init__(self, llm, mode='accurate', seed=None):
        sys_desc = """You are a large language model based assistant, expert at writing python programs to solve the user's problem. Given a specific problem or task, respond exclusively with Python code. Ensure the Python code is complete, functional, and ready to execute to solve the provided problem. Avoid any explanations, discussions, or responses that are not directly Python code. Lastly, you don't have to write class definitions for Scene class or Constraints class as they are already imported in the code. You can directly use them."""
        sys_desc += """Return only python code in Markdown format, e.g.:
```python
....
```"""
        self.sys_desc = {"role": "system", "content": sys_desc} 
        # self.llm = LLM(mode=mode, seed=seed, system_desc=sys_desc)
        self.llm = llm


    def _sanitize_output(self, text: str):
        _, code, _ = text.split("```")
        return code

    def run(self, prompt):
        response = self.llm.run(prompt, self.sys_desc)
        return self._sanitize_output(response[0]['generation']['content'])