import time
import anthropic
# from meta_ai_api import MetaAI
from assets.key import api_key


class LLM:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.reset()

    def reset(self):
        self.history = []

    def run(self, query):
        curr = {"role": "user", "content": f"{query}"}

        self.history.append(curr)

        while True:
            try:
                response = self.client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=4096,
                    temperature=0.2,
                    system="You are a large language model based assistant, expert at writing code for drawing 2D scene layouts. Respond only Python code, nothing else",
                    messages=self.history
                )
                response = response.content[0].text
                print(response)
            except Exception as e:
                print(e)
                time.sleep(10)
                response = ""
            if response != "":
                break

        return response

    def run_embed(self, query):
        self.reset()
        curr = {"role": "user", "content": f"{query}"}

        self.history.append(curr)

        while True:
            try:
                response = self.client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=4096,
                    temperature=0.3,
                    system="You are a large language model based assistant, expert at designing 2D layouts scenes.",
                    messages=self.history
                )
                response = response.content[0].text
                print(response)
            except Exception as e:
                print(e)
                time.sleep(10)
                response = ""
            if response != "":
                break

        return response
    
    def run_collect_seed(self, query):
        self.reset()
        curr = {"role": "user", "content": f"{query}"}

        self.history.append(curr)

        while True:
            try:
                response = self.client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=4096,
                    temperature=0.1,
                    system="You are a large language model based assistant, expert at extracting seed words from a given scene description.",
                    messages=self.history
                )
                response = response.content[0].text
                print(response)
            except Exception as e:
                print(e)
                time.sleep(10)
                response = ""
            if response != "":
                break

        return response
    
    def run_generate_prompt(self, query):
        self.reset()
        curr = {"role": "user", "content": f"{query}"}

        self.history.append(curr)

        while True:
            try:
                response = self.client.messages.create(
                    model="claude-3-haiku-20240307",
                    max_tokens=4096,
                    temperature=0.3,
                    system="You are a large language model based assistant, expert at generating simple prompts for scene generation.",
                    messages=self.history
                )
                response = response.content[0].text
                print(response)
            except Exception as e:
                print(e)
                time.sleep(10)
                response = ""
            if response != "":
                break

        return response
