import os
import json
from openai import OpenAI
from openai.types.responses.response_text_config_param import ResponseTextConfigParam
from dotenv import load_dotenv
from pydantic import json_schema

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def get_text_format(response_schema: dict):
    response_schema["additionalProperties"] = False
    text_format = {
        "format": {
            "type": "json_schema",
            "name": "structured_output",
            "strict": True,
            "schema": response_schema,
        }
    }
    return text_format


def generate_json(
    system_prompt: str,
    user_prompt: str,
    response_schema: dict,
    model: str = "gpt-4o-mini",
):

    input = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    response = client.responses.create(
        model=model,
        instructions=system_prompt,
        input=input,
        text=get_text_format(response_schema),
    )
    return json.loads(response.output[0].content[0].text)
