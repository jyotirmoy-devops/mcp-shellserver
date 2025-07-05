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


@mcp.tool(description="Run kubectl commands")
def run_kubectl_command(command: str) -> str:
    """
     Use this tool to access Kubernetes cluster information via kubectl commands. It supports commands like 'kubectl get pods', 'kubectl get nodes', 'kubectl describe svc', and other read-only Kubernetes queries. Use this tool when the user asks about Kubernetes clusters, nodes, pods, deployments, services, namespaces, or logs. This is the primary interface for querying Kubernetes cluster status and resource information.
     param command: The kubectl command to run (e.g., 'get pods -n default').
    return: The output or error from the kubectl command.
    """
    try:
        # Split the command string into a list for subprocess
        cmd_list = ["kubectl"] + command.split()
        result = run(cmd_list, capture_output=True, text=True, check=True)
        return result.stdout
    except CalledProcessError as e:
        return f"Error: {e.stderr}"
    
@mcp.tool(description="Run helm commands")
def run_helm_command(command: str) -> str:
    """
    Run a helm command on the local system.
    param command: The kubehelmctl command to run (e.g., 'list -n namespace, upgrade').
    return: The output or error from the helm command.
    """
    try:
        # Split the command string into a list for subprocess
        cmd_list = ["helm"] + command.split()
        result = run(cmd_list, capture_output=True, text=True, check=True)
        return result.stdout
    except CalledProcessError as e:
        return f"Error: {e.stderr}"

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
