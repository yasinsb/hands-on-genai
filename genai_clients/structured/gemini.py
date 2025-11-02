import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


def generate_structured(
    system_prompt: str,
    user_prompt: str,
    response_model: type[BaseModel],
    model: str = "gemini-2.5-flash-lite",
):
    """
    Generate structured output using Google's Gemini API with Pydantic models.
    
    Args:
        system_prompt: System instructions for the model
        user_prompt: User message/query
        response_model: Pydantic BaseModel class defining the expected output structure
        model: Gemini model to use
        
    Returns:
        Parsed Pydantic model instance
    """
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_prompt),
            ],
        ),
    ]
    
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_budget=0,
        ),
        response_mime_type="application/json",
        response_schema=response_model,
        system_instruction=system_prompt,
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )
     
    return response.parsed