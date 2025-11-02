import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def generate_json(system_prompt: str, user_prompt: str, response_schema: dict, model: str = "gemini-2.5-flash-lite"):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_prompt),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=0,
        ),
        response_mime_type="application/json",
        response_schema=response_schema,
        system_instruction=system_prompt,
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )
     
    return response.parsed