import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def return_command_response(command):
    response = openai.Completion.create(
        engine="text-ada-001",
        prompt=command,
        max_tokens=25,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text


def return_explaination_response(command):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=command,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text
