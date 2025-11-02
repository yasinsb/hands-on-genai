import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_text(system_prompt: str, user_prompt: str, model: str = "gpt-4o-mini", temperature: float = 0):
    input=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    response = client.responses.create(
        model=model,
        instructions=system_prompt,
        input=input,
        temperature=temperature,
    )

    return response.output_text