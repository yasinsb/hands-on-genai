import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

def generate_text(system_prompt: str, user_prompt: str, model: str = "gemini-2.5-flash-lite", temperature: float = 0):
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
        temperature=temperature,
        system_instruction=system_prompt,
        thinking_config = types.ThinkingConfig(
            thinking_budget=0,
        )
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config
    )

    return response.text