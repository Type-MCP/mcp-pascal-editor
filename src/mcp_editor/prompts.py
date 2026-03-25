"""Server-delivered MCP prompts (skills) for editor."""

from mcp.server.fastmcp import FastMCP


def register_prompts(server: FastMCP) -> None:
    """Register prompts with the server."""

    @server.prompt("use_editor")
    async def use_editor_prompt() -> str:
        """Guide for using editor tools effectively"""
        return """You have access to the editor MCP server with these tools:

- interactive.initItem: Init item in the interactive store
- interactive.setControlValue: Set control value in the interactive store
- interactive.removeItem: Remove item in the interactive store
- scene.loadScene: Load scene in the scene store
- scene.clearScene: Clear scene in the scene store
- scene.unloadScene: Unload scene in the scene store
- scene.setScene: Set scene in the scene store
- scene.createNode: Create node in the scene store
- scene.createNodes: Create nodes in the scene store
- scene.updateNode: Update node in the scene store
- scene.updateNodes: Update nodes in the scene store
- scene.deleteNode: Delete node in the scene store
- scene.deleteNodes: Delete nodes in the scene store
- scene.createCollection: Create collection in the scene store
- scene.deleteCollection: Delete collection in the scene store
- scene.updateCollection: Update collection in the scene store
- scene.addToCollection: Add to collection in the scene store
- scene.removeFromCollection: Remove from collection in the scene store
- commandpalette.setOpen: Set open in the commandpalette store
- commandpalette.setMode: Set mode in the commandpalette store

Use the appropriate tool based on the user's request. Always check required parameters before calling a tool."""

    @server.prompt("debug_editor")
    async def debug_editor_prompt(error_message: str) -> str:
        """Diagnose issues with editor operations"""
        return """The user encountered an error while using editor.

Error: {{error_message}}

Available tools: interactive.initItem, interactive.setControlValue, interactive.removeItem, scene.loadScene, scene.clearScene, scene.unloadScene, scene.setScene, scene.createNode, scene.createNodes, scene.updateNode, scene.updateNodes, scene.deleteNode, scene.deleteNodes, scene.createCollection, scene.deleteCollection

Diagnose the issue and suggest which tool to use to resolve it."""

