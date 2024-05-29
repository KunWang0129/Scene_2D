import anthropic
from assets.key import api_key
import base64

class VLM:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=api_key)        
        self.reset()

    def reset(self):
        self.history = []
        
    def run(self, images, description):
        
        content = []

        for i, image_path in enumerate(images):
            image = open(image_path, 'rb').read()
            image_data = base64.b64encode(image).decode("utf-8")
            
            image_ref = {
                "type": "text",
                "text": f"Image Reference Number {i+1}:"
            }
            image_query = {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": "image/png",
                    "data": image_data,
                }
            }
            
            content.append(image_ref)
            content.append(image_query)

        
        prompt = f"""You have exceptional vision and a keen eye for detail, making 
you an expert at evaluating and ranking images based on how well they match a given description.
The images you'll be evaluating are 2D drawings composed of simple shapes.
Given a description of a scene and will need to establish criteria for assessing the visual features in each image.
Here is the description: {description}
Please rank the provided images according to how closely they align with the description. 
Provide your ranking in a comma-separated list of image reference numbers, with the image that best matches the description listed first.
The response format for ranking five images is: <answer>1,3,2,5,4</answer>
Before providing the ranking, analyze each image in detail according to the 
defined criteria, and document your thought process within <thinking> tags."""


        task_description = {
                "type": "text",
                "text": prompt
        }
        
        content.append(task_description)
        
        curr = {"role": "user", "content": content}

        self.history.append(curr)

        response = self.client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=2048,
            temperature=0.0,
            # system="Follow the instructions closely.",
            messages=self.history
        )
        response = response.content[0].text

        print(response)

        _, after = response.split("<answer>")
        best_rank = int(after.split(",")[0])

        return images[best_rank - 1]

        # return response


# # Load image file 
# image = open('examples/rendered_scene/car.png', 'rb').read()
# image_media_type = "image/png"

# # Run the VLM
# vlm = VLM()
# response = vlm.run(query=image)
# print(response)