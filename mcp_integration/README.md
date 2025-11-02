# Simple MCP Server

A basic MCP server that exposes a `get_capital` tool using OpenAI or Gemini to return country capitals.

## Run Server

```bash
fastmcp run simple_server.py --transport http --port 8008
```

- `--transport http`: Serves over HTTP instead of stdio (allows remote connections)
- `--port 8008`: Listens on port 8008
- `mcp.json`: Configuration file that tells MCP clients (like Claude Desktop) where to find this server
