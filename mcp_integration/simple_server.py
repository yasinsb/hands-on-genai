import os
import sys
from pathlib import Path
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field

# Add project root to sys.path to make imports work
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from fastmcp import FastMCP
from genai_clients.structured.gemini import generate_structured as generate_structured_gemini
from genai_clients.structured.gpt import generate_structured as generate_structured_gpt

app = FastMCP(name="Simple Server")

system_prompt = "You are a helpful assistant."

class MyModel(BaseModel):
    capital: str = Field(description="The capital of the given country")

@app.tool(
    name="get_capital",
    description="Get the capital of a country",
)
def get_capital(country: str, provider: str = "gemini") -> str:
    if provider.lower() == "gemini" or provider.lower() == "google":
        return generate_structured_gemini(system_prompt, country, MyModel).capital
    elif provider.lower() == "gpt" or provider.lower() == "openai":
        return generate_structured_gpt(system_prompt, country, MyModel).capital
    else:
        return "Invalid provider. Please use 'gemini' or 'gpt'."