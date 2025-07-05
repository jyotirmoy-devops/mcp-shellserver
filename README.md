# ShellServer MCP Example

This project demonstrates a simple MCP server using the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk). The server exposes a single tool, `call_terminal`, which allows users to run terminal commands asynchronously and receive their output.

## Features
- Exposes a single tool: `call_terminal`
- Allows running terminal commands from MCP-compatible clients
- Asynchronous implementation for non-blocking command execution

## Prerequisites
- Python 3.8+
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

## Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <your-repo-url>
   cd shellserver
   ```

2. **Install dependencies** (using pip):
   ```bash
   pip install "mcp[cli]"
   ```
   Or with [uv](https://github.com/astral-sh/uv):
   ```bash
   uv pip install "mcp[cli]"
   ```

## Usage

### Start the MCP Server

Run the server script:

```bash
python server.py
```

Or, for development/testing with the MCP CLI:

```bash
mcp dev server.py
```

### How the Tool Works

The server exposes a tool called `call_terminal` that takes a single argument:
- `command` (str): The shell command to execute.

It returns the standard output or error from the command.

#### Example Usage

If you connect to this server using an MCP-compatible client, you can call the tool like this:

- **Tool name:** `call_terminal`
- **Arguments:**
  - `command`: `echo Hello, MCP!`

**Response:**
```
Hello, MCP!
```

### Security Note
This tool executes arbitrary shell commands. For demonstration and local use only. **Do not expose this server to untrusted users or production environments.**

## References
- [MCP Python SDK Documentation](https://github.com/modelcontextprotocol/python-sdk)
- [Model Context Protocol (MCP) Website](https://modelcontextprotocol.io/)
