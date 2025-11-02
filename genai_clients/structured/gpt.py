import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


def generate_structured(
    system_prompt: str,
    user_prompt: str,
    response_model: type[BaseModel],
    model: str = "gpt-4o-mini",
):
    """
    Generate structured output using OpenAI's API with Pydantic models.
    
    Args:
        system_prompt: System instructions for the model
        user_prompt: User message/query
        response_model: Pydantic BaseModel class defining the expected output structure
        model: OpenAI model to use
        
    Returns:
        Parsed Pydantic model instance
    """
    input = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    response = client.responses.parse(
        model=model,
        input=input,
        text_format=response_model,
    )
    
    return response.output_parsed
