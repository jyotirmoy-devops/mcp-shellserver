"""
A simple MCP server exposing a 'call_terminal' tool to run terminal commands.

This server uses the MCP Python SDK and demonstrates how to expose a tool
that executes shell commands and returns their output.
"""
from mcp.server.fastmcp import FastMCP
import subprocess
import asyncio

# Create an MCP server instance
mcp = FastMCP("TerminalServer")

@mcp.tool()
async def call_terminal(command: str) -> dict:
    """
    Run a terminal command asynchronously and return its output as a dictionary.

    Args:
        command (str): The shell command to execute.
    Returns:
        dict: {
            'success': bool,         # True if command succeeded, False otherwise
            'output': str,           # Standard output from the command
            'error': str | None      # Error message or None
        }
    """
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()
        success = process.returncode == 0
        return {
            'success': success,
            'output': stdout.decode().strip(),
            'error': None if success else stderr.decode().strip()
        }
    except Exception as e:
        return {
            'success': False,
            'output': '',
            'error': str(e)
        }

@mcp.resource("file:///mcpreadme")
def get_mcp_readme() -> str:
    """
    Return the contents of the 'mcpreadme.md' file in the current directory.
    Returns:
        str: The contents of the file, or an error message if not found.
    """
    try:
        with open("C:\\Users\\jnath\\Documents\\Projects\\mcp-project\\shellserver\\mcpreadme.md", "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error reading mcpreadme.md: {str(e)}"

if __name__ == "__main__":
    mcp.run()
