import os
import json
import numpy as np
from openai import OpenAI
from tqdm import tqdm 
from langchain.embeddings import OpenAIEmbeddings
from tools.llm import LLM
from assets.key import api_key
    
class Embedder:
    def __init__(self):
        self.llm = LLM()
        self.embeddings_model = OpenAIEmbeddings(openai_api_key=api_key)
        # Subject to change
        self.template = "Describe the layout of the shapes as a paragraph based on the following description. Especially focus on the shape arrangement. Use only circles, triangles, and rectangles "
        self.template += """
Description: 
A living room arrangement with a sofa, a coffee table, an armchair and two lamps for lighting.
Your response:
A sofa is placed against the back wall. There is a coffee table in front of the sofa with a lamp on it. To the right of the coffee table is a single armchair. While to the left of the sofa there is a lamp on an end table.

Description:
A bedroom scene with a large bed, two bedside tables, two lamps and a dresser.
Your response:
A large bed is placed against the back wall. Two bedside tables are placed on either side of the bed each with a table lamp on it. An armchair is placed left of the bed, facing the front wall. A dresser is placed against the right and back walls. A chandelier is placed in the center of the room.

Description:
A living room with sofas, coffee table, armchairs, ottomans, TV cabinet, TV and a chandelier.
Your response:
A sofa is placed against the back wall with end tables on either side. There is a plant on each end table. A coffee table is placed in front of the sofa. There are armchairs on either side of the coffee table. A pair of ottomans are placed in front of the coffee table. A TV cabinet is placed against the front wall. A TV is placed on the TV cabinet. A chandelier is placed in the center of the room.
"""
    def run(self, desc):
        query = f"{self.template}\nDescription: \n{desc}\nYour response:\n"
        response = self.llm.run(query)
        vector = self.embeddings_model.embed_query(response)  
        return vector    
    
class CodeRetriever:
    def __init__(self):
        self.embd = Embedder()
        self.examples = [f'{x}.py' for x in range(1, 27)]
        self.data_path = './examples/'
        self.embd_path = './assets/rag_embeddings.json'
        self.topk = 5
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
            # first = desc.find('##@##')
            # second = desc.find('##@##', first+6)
            # code = desc[first+6:second]
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
        
        query_vector = np.array(self.embd.run(query))
        dataset_vectors = np.array(list(self.embeddings.values()))
        
        query_vector /= np.linalg.norm(query_vector)
        dataset_vectors /= np.linalg.norm(dataset_vectors, axis=1)[:, np.newaxis]
        sims = np.dot(dataset_vectors, query_vector)
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