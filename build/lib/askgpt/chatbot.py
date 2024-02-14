import os
from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')

if not api_key:
    print('No API key provided. Please provide an API key to use the OpenAI API.')
    exit(0)


OpenAI.api_key = api_key

client = OpenAI()


def return_command_response(command):
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful terminal assistant."}, {
            "role": "user", "content": command}],
        stream=True,
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
