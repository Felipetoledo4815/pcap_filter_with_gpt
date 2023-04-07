import os
import openai

CONTEXT = """"
    TODO
"""


def query1(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="ada", prompt="Say this is a test", temperature=0, max_tokens=7)
    print(response['choices'][0]['text'])
    return response['choices'][0]['text']
