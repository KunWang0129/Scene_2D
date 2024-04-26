from openai import OpenAI
from assets.key import api_key
class LLM:
    def __init__(self, single_use=True, system_desc=None, seed=0, mode='accurate'):
        self.client = OpenAI(api_key = api_key)
        if mode == 'fast':
            self.model = "gpt-3.5-turbo-0125"
        elif mode == 'accurate':
            self.model = "gpt-4-0125-preview"
        else:
            raise ValueError("Invalid mode. Use 'fast' or 'accurate'")
        self.seed=seed
        self.single_use= single_use
        if system_desc is None:
            self.system_desc = {"role": "system", "content": "You are a large language model based assistant, expert at designing layouts for indoor scenes."}
        else:
            self.system_desc = system_desc
        
        self.reset()
        
    def reset(self):
        self.history = [self.system_desc]
        
    def run(self, query):
        curr = {"role": "user", "content": f"{query}"}
        self.history.append(curr)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history, 
            seed=self.seed
        )
        
        # completion_tokens = response.dict()['usage']['completion_tokens']
        # prompt_tokens = response.dict()['usage']['prompt_tokens']
        # total_tokens = response.dict()['usage']['total_tokens']
        # print(f"Total tokens: {total_tokens}, Prompt tokens: {prompt_tokens}, Completion tokens: {completion_tokens}")
        
        response = response.dict()['choices'][0]['message']['content']
        
        curr = {"role": "assistant", "content": f"{response}"}
        self.history.append(curr)
        if self.single_use:
            self.reset()
        return response 