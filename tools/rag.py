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
If you are asked to describe a complex object, drawing steps should start go the more general outer shape to the more inner details.
Feel free to add as many steps as necessary to make the final drawing look realistic.
Your answer should have only a numbered list of steps and each line ends with what the shapes represent enclosed in parentheses.
Here is an example:
<example>
Description:
Create a scene with a house.
Your expected response:
1. A large gray rectangle is placed in the center of the scene (building).
2. A red triangle is placed above the building, with its base aligned to the top edge of the building (roof).
3. A smaller dark brown rectangle is placed at the bottom center of the building (door).
4. Two small blue rectangles are placed symmetrically on either side of the door, near the middle of the building (windows).
5. A thin, elongated black rectangle is placed vertically in the center of the door (door handle).
</example>
"""

    def run(self, desc, write_file=None):
        if write_file is not None and os.path.exists(write_file):
            with open(write_file, "r") as file:
                response = file.read()
                print(response)
        else:
            query = f"{self.template}\nCan you write the drawing steps for the following description:\n{desc}\n"
            response = self.llm.run_embed(query)
            if write_file is not None:
                with open(write_file, "w") as file:
                    file.write(response)

        res = self.embeddings_model.embeddings(
            model="mixedbread-ai/mxbai-embed-large-v1",
            input=response,
            normalized=False,
            encoding_format="float",
            truncation_strategy="start",
        )
        vector = [entry.embedding for entry in res.data]
        return vector, response


class CodeRetriever:
    def __init__(self):
        self.embd = Embedder()
        self.examples = [f"{x}.py" for x in range(1, 6)]
        self.data_path = "./examples/"
        self.embd_path = "./assets/rag_embeddings.json"
        self.topk = 1
        if os.path.exists(self.embd_path):
            with open(self.embd_path, "r") as f:
                self.embeddings = json.load(f)
        else:
            self.build()
    def get_examples(self):
        return self.examples
    
    def build(self):
        print("Building code embeddings")
        self.embeddings = {}
        for ex in tqdm(self.examples):
            with open(self.data_path + ex, "r") as f:
                lines = f.readlines()
            desc = "".join(lines)
            first = desc.find("##@##")
            second = desc.find("##@##", first + 6)
            description = desc[first + 6 : second]
            description = description.replace("description = ", "").replace("'", "")
            # code = desc[second+5:]
            # code = desc
            outfile = f'{self.data_path}{ex.replace(".", "_")}description.txt'
            vector, _ = self.embd.run(description, outfile)
            self.embeddings[ex] = vector

        with open(self.embd_path, "w") as f:
            json.dump(self.embeddings, f)

    def fetch_example(self, ex):
        with open(self.data_path + ex, "r") as f:
            lines = f.readlines()
        desc = "".join(lines)
        first = desc.find("##@##")
        add_objs = desc[:first]
        second = desc.find("##@##", first + 6)
        user_input = desc[first + 6 : second]
        code = desc[second + 5 :]
        return code
        # return user_input[3:-4], "```"+add_objs+"```", "```"+code+"```"

    def run(self, query):
        print("query:", query)
        vector, description = self.embd.run(query)
        query_vector = np.array(vector)
        dataset_vectors = np.array(list(self.embeddings.values()))
        print("query_vector:", query_vector.shape)
        print("dataset_vectors:", dataset_vectors.shape)
        query_vector /= np.linalg.norm(query_vector)
        dataset_vectors /= np.linalg.norm(dataset_vectors, axis=1)[:, np.newaxis]
        dataset_vectors = dataset_vectors.squeeze(axis=1)
        sims = np.dot(dataset_vectors, query_vector.T).squeeze()
        indices = np.argsort(sims)[-self.topk :]
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
