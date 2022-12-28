from promptify.models.nlp.models import GPT3
from promptify.models.nlp.model_list import top_model_list
import random

api_key = "<api-key>"
gpt3_model = GPT3(api_key)

model_name = random.choice(top_model_list)
prompt1 = """
The following is a list of companies and the categories they fall into:

Apple, Facebook, Fedex

Apple
Category:
"""

results = gpt3_model.prompt_model_generation(model_name=model_name, prompts=prompt1, multiple=False, stop=["\n"])

print(results)