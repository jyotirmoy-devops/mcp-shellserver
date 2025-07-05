"""
A simple MCP server exposing a 'call_terminal' tool to run terminal commands.

This server uses the MCP Python SDK and demonstrates how to expose a tool
that executes shell commands and returns their output.
"""
from mcp.server.fastmcp import FastMCP
import subprocess
import asyncio
from mcp.server.fastmcp import FastMCP
from kubernetes import config
from subprocess import run, PIPE, CalledProcessError
import requests

# Load your kubeconfig (used by kubectl) to connect to the cluster
config.load_kube_config()
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


    




@mcp.tool(description="Fetch products from a local API endpoint.")
def fetch_products() -> dict:
    """
     Use this tool to fetch a list of products from the product catalog API. It returns detailed product information including product name, product ID, quantity, price, and category. Use this tool whenever the user asks to view available products, search for items by category, list all items in the catalog, or explore products.
    Returns:
        dict: The JSON response containing products, or an error message.
    """
    try:
        response = requests.get("http://localhost:5000/getproducts", timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}



if __name__ == "__main__":
    mcp.run()
