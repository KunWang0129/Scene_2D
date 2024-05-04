import os
import json
import numpy as np
from tqdm import tqdm
from tools.llm import LLM
from assets.key import api_key
from assets.key_embed import api_key as api_key_embed
from mixedbread_ai.client import MixedbreadAI


class Embedder:
    def __init__(self):
        self.llm = LLM()
        # self.embeddings_model = OpenAIEmbeddings(openai_api_key=api_key)
        self.embeddings_model = MixedbreadAI(api_key=api_key_embed)
        # Subject to change
        self.template = "Describe the layout of the shapes as a paragraph based on the following description. Especially focus on the shape arrangement. Use only circles, triangles, and rectangles "
        self.template += """
Description: 
Create a scene with an orange circle, and arrange four blue rectangles.
Your response:
A circle is placed in the center of the scene. A blue rectangle is placed to the left of the circle. A blue rectangle is placed to the right of the circle. A blue rectangle is placed above the circle. A blue rectangle is placed below the circle.

Description:
Create a scene with a green triangle, a red triangle, and a blue triangle.
Your response:
A green triangle is placed at the center of the scene. A red triangle is placed to the left of the green triangle. A blue triangle is placed to the right of the green triangle.
"""
    def run(self, desc):
        print('desc:', desc)
        query = f"{self.template}\nDescription: \n{desc}\nYour response:\n"
        # query = f"{desc}"
        response = self.llm.run_embed(query)
        response = response.content[0].text
        print('response:', response)
        # vector = self.embeddings_model.embed_query(response)
        
        res = self.embeddings_model.embeddings(
            model='mixedbread-ai/mxbai-embed-large-v1',
            input=desc,
            normalized=False,
            encoding_format='float',
            truncation_strategy='start'
            )
        vector = [entry.embedding for entry in res.data]
        return vector    
    
    def _sanitize_output(self, text: str):
        _, after = text.split("```python")
        return after.split("```")[0]
    
    
class CodeRetriever:
    def __init__(self):
        self.embd = Embedder()
        self.examples = [f'{x}.py' for x in range(1, 11)]
        self.data_path = './examples/'
        self.embd_path = './assets/rag_embeddings.json'
        self.topk = 2
        if os.path.exists(self.embd_path):
            with open(self.embd_path, 'r') as f:
                self.embeddings = json.load(f)
        else:
            self.build()
            
    def build(self):
        print('Building code embeddings')
        self.embeddings = {}
        for ex in tqdm(self.examples):
            with open(self.data_path + ex, 'r') as f:
                lines = f.readlines()
            desc = "".join(lines)
            first = desc.find('##@##')
            second = desc.find('##@##', first+6)
            # description = desc[first+6:second]
            # code = desc[second+5:]
            code = desc
            vector = self.embd.run(code)
            self.embeddings[ex] = vector
            
        with open(self.embd_path, 'w') as f:
            json.dump(self.embeddings, f)
            
    def fetch_example(self, ex):
        with open(self.data_path + ex, 'r') as f:
            lines = f.readlines()
        desc = "".join(lines)
        first = desc.find('##@##')
        add_objs = desc[:first]
        second = desc.find('##@##', first+6)
        user_input = desc[first+6:second]
        code = desc[second+5:]
        return user_input[3:-4], "```"+code+"```"
        # return user_input[3:-4], "```"+add_objs+"```", "```"+code+"```"
    
    def run(self, query):
        print('query:', query)
        query_vector = np.array(self.embd.run(query))
        dataset_vectors = np.array(list(self.embeddings.values()))
        print('query_vector:', query_vector.shape)
        print('dataset_vectors:', dataset_vectors.shape)
        query_vector /= np.linalg.norm(query_vector)
        breakpoint()
        dataset_vectors /= np.linalg.norm(dataset_vectors, axis=1)[:, np.newaxis]
        dataset_vectors = dataset_vectors.squeeze(axis = 1)
        sims = np.dot(dataset_vectors, query_vector.T).squeeze()
        indices = np.argsort(sims)[-self.topk:]
        top_matches = [self.examples[i] for i in indices]
        
        inputs=[]
        # add_objs=[]
        codes=[]
        for ex in top_matches:
            # user_input, add_obj, code = self.fetch_example(ex)
            user_input, code = self.fetch_example(ex)
            inputs.append(user_input)
            # add_objs.append(add_obj)
            codes.append(code)
        return inputs, codes
        # return inputs, add_objs, codes