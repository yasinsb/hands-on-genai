# Hands-on GenAI

## Project Structure

### genai_clients/
Client modules for OpenAI and Gemini APIs. Organized by output type:
- `text/`: Text generation using both providers
- `structured/`: Structured output with Pydantic models
- `img/`: Image generation (placeholder for future implementation)

### mcp_integration/
MCP server implementation that exposes GenAI tools for use with MCP clients. Includes configuration files and server definitions.

### notebooks/
Jupyter notebooks demonstrating API usage and experimentation with different GenAI capabilities.

## Prepare Environment
To create an isolated python environment run this.
```
python -m venv .venv
```

Activate it.
```
source .venv/bin/activate
```

Install the requirements
```
pip install -r requirements.txt 
```

