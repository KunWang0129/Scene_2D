# import anthropic
# from meta_ai_api import MetaAI
from assets.key import api_key
from assets.ckpt_dir import ckpt_dir, tokenizer_path
from llama3.llama import Dialog, Llama
import torch.distributed as dist

class LLM:
    def __init__(self, single_use=True, system_desc=None, seed=0, mode='accurate'):
        self.setup_distributed()

        self.client = Llama.build(
            ckpt_dir=ckpt_dir,
            tokenizer_path=tokenizer_path,
            max_seq_len=4092,
            max_batch_size=4,
        )
        # self.client = anthropic.Anthropic(api_key=api_key)
        # self.client =  MetaAI(fb_email="brianwang03@gmail.com", fb_password="Wal@12658")
        # if mode == 'fast':
        #     self.model = "gpt-3.5-turbo-0125"
        # elif mode == 'accurate':
        #     self.model = "gpt-4-0125-preview"
        # else:
        #     raise ValueError("Invalid mode. Use 'fast' or 'accurate'")
        # self.seed=seed
        # self.single_use= single_use
        # if system_desc is None:
        #     self.system_desc = {"role": "user", "content": "You are a large language model based assistant, expert at designing layouts for indoor scenes."}
        # else:
        #     self.system_desc = system_desc
        
        self.reset()
    
    def setup_distributed(self,world_size=1, rank=0):
        dist.init_process_group(
            backend='nccl',       # or 'gloo' depending on your system's capabilities and requirements
            init_method='env://', # typically used in most setups
            world_size=world_size,
            rank=rank
        )

    def reset(self):
        self.history: List[Dialog] = []
        
    def run(self, query, query_sys = None):
        self.reset()
        curr = []
        if query_sys != None:
            curr_sys = {"role": "system", "content": f"{query_sys}"}
            curr.append(curr_sys)
        curr.append({"role": "user", "content": f"{query}"})
        
        self.history.append(curr)

        response = self.client.chat_completion(
            self.history,
            max_gen_len=None,
            temperature=0.6,
            top_p=0.9,
        )


        # response = self.client.chat.completions.create(
        #     model=self.model,
        #     messages=self.history,
        #     seed=self.seed
        # )
        # response = self.client.messages.create(
        #     model="claude-3-haiku-20240307",
        #     max_tokens=4096,
        #     temperature=0.2,
        #     system="You are a large language model based assistant, expert at designing layouts for indoor scenes. Respond only Python code, nothing else",
        #     messages=self.history
        # )
        # response = self.client.prompt(self.history)
        
        # completion_tokens = response.dict()['usage']['completion_tokens']
        # prompt_tokens = response.dict()['usage']['prompt_tokens']
        # total_tokens = response.dict()['usage']['total_tokens']
        # print(f"Total tokens: {total_tokens}, Prompt tokens: {prompt_tokens}, Completion tokens: {completion_tokens}")
        
        # response = response.dict()['choices'][0]['message']['content']
        #
        # curr = {"role": "assistant", "content": f"{response}"}
        # self.history.append(curr)
        # if self.single_use:
        #     self.reset()


        return response
    
    def run_embed(self, query, query_sys = None):
        self.reset()
        curr = []
        if query_sys != None:
            curr_sys = {"role": "system", "content": f"{query_sys}"}
            curr.append(curr_sys)
        curr.append({"role": "user", "content": f"{query}"})

        
        
        self.history.append(curr)

        response = self.client.chat_completion(
            self.history,
            max_gen_len=None,
            temperature=0.6,
            top_p=0.9,
        )

        
        # completion_tokens = response.dict()['usage']['completion_tokens']
        # prompt_tokens = response.dict()['usage']['prompt_tokens']
        # total_tokens = response.dict()['usage']['total_tokens']
        # print(f"Total tokens: {total_tokens}, Prompt tokens: {prompt_tokens}, Completion tokens: {completion_tokens}")
        
        # response = response.dict()['choices'][0]['message']['content']
        #
        # curr = {"role": "assistant", "content": f"{response}"}
        # self.history.append(curr)
        # if self.single_use:
        #     self.reset()
        return response