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
        self.template = """Describe the 2D layout of the shapes as a paragraph based on the following description.
Especially focus on the shape arrangement and describe the drawing steps using only circles, triangles, and rectangles.
You should first draw the background objects and then the more detailed objects.
If you are asked to describe a complex object, drawing steps should start go the more general outer shape to the more inner details.
Your answer should have only a numbered list of steps and each line ends with what the shapes represent enclosed in parentheses.
Here is an example:
<example>
Description:
Create a scene with a car in a field.
Your expected response:
1. A large grey rectangle is placed in the bottom of the scene (field).
2. A brown rectangle is placed in the center of the scene (car body).
3. Two black circles are placed at the bottom of the car body, one on each side (wheels).
4. A smaller black rectangle is placed at the front of the car body (front bumper).
5. A smaller black rectangle is placed at the rear of the car body (rear bumper).
6. A lightblue rectangle is placed at the top front of the car body (windshield).
7. A lightblue rectangle is placed at the top rear of the car body (rear window).
8. A small brown rectangle is placed at the center top of the car body (roof).
9. A small yellow circle is placed on the front of the car body (headlight).
10. A small red circle is placed on the rear of the car body (taillight).
</example>
"""

    def run(self, desc, write_file=None, generate=True):
        
        if write_file is not None and os.path.exists(write_file):
            with open(write_file, 'r') as file:
                response = file.read()
                print(response)
        elif generate:
            query = f"{self.template}\nCan you write the drawing steps for the following description:\n{desc}\n"
            response = self.llm.run_embed(query)
            if write_file is not None:
                with open(write_file, 'w') as file:
                    file.write(response)
        else:
            response = desc
            if write_file is not None:
                with open(write_file, 'w') as file:
                    file.write(response)

        res = self.embeddings_model.embeddings(
            model='mixedbread-ai/mxbai-embed-large-v1',
            input=response,
            normalized=False,
            encoding_format='float',
            truncation_strategy='start'
        )
        vector = [entry.embedding for entry in res.data]
        return vector, response


class CodeRetriever:
    def __init__(self):
        self.embd = Embedder()
        self.use_expanded = True
        self.data_path = './examples/'
        self.topk = 2

        if self.use_expanded:
            self.embd_path = './assets/rag_embeddings_expanded.json'
        else:
            self.embd_path = './assets/rag_embeddings.json'

        if os.path.exists(self.embd_path):
            with open(self.embd_path, 'r') as f:
                self.embeddings = json.load(f)
            self.num_examples = len(self.embeddings)
            self.examples = [f'{x}.py' for x in range(1, self.num_examples + 1)]
        else:
            self.num_examples = 25
            self.examples = [f'{x}.py' for x in range(1, self.num_examples + 1)]
            self.build()

    def build(self, num=None):
        print('Building code embeddings')
        self.embeddings = {}
        for ex in tqdm(self.examples):
            with open(self.data_path + ex, 'r') as f:
                lines = f.readlines()
            desc = "".join(lines)
            first = desc.find('##@##')
            second = desc.find('##@##', first + 6)
            description = desc[first + 6:second]
            description = description.replace("description = ", "").replace("'", "")
            # code = desc[second+5:]
            # code = desc
            outfile = f'{self.data_path}{ex.replace(".", "_")}description.txt'
            vector, _ = self.embd.run(description, outfile)
            self.embeddings[ex] = vector

        with open(self.embd_path, 'w') as f:
            json.dump(self.embeddings, f)

    def fetch_example(self, ex):
        with open(self.data_path + ex, 'r') as f:
            lines = f.readlines()
        desc = "".join(lines)
        first = desc.find('##@##')
        add_objs = desc[:first]
        second = desc.find('##@##', first + 6)
        user_input = desc[first + 6:second]
        code = desc[second + 5:]
        return code
        # return user_input[3:-4], "```"+add_objs+"```", "```"+code+"```"

    def add_example(self, input, desc, code):
        self.num_examples += 1
        ex = f'{self.num_examples}.py'
        # if os.path.exists(self.data_path + ex) == False:
        with open(self.data_path + ex, "w") as file:
            file.write(code)
        description = desc

        outfile = f'{self.data_path}{ex.replace(".", "_")}description.txt'
        vector, _ = self.embd.run(description, outfile, generate=False)
        self.embeddings[ex] = vector
        with open(self.embd_path, 'w') as f:
            json.dump(self.embeddings, f)
        

    def run(self, query):
        print('query:', query)
        vector, description = self.embd.run(query)
        query_vector = np.array(vector)
        dataset_vectors = np.array(list(self.embeddings.values()))
        print('query_vector:', query_vector.shape)
        print('dataset_vectors:', dataset_vectors.shape)
        query_vector /= np.linalg.norm(query_vector)
        dataset_vectors /= np.linalg.norm(dataset_vectors, axis=1)[:, np.newaxis]
        dataset_vectors = dataset_vectors.squeeze(axis=1)
        sims = np.dot(dataset_vectors, query_vector.T).squeeze()
        indices = np.argsort(sims)[-self.topk:]
        top_matches = [self.examples[i] for i in indices]
        # inputs = []
        # add_objs=[]
        codes = []
        
        for ex in top_matches:
            # user_input, add_obj, code = self.fetch_example(ex)
            code = self.fetch_example(ex)
            # add_objs.append(add_obj)
            codes.append(code)
        return codes, description
        # return inputs, add_objs, codes