import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)


def return_command_response(command):
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a helpful terminal assistant."}, {
            "role": "user", "content": command}],
        stream=True,
    )
    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")