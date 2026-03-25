"""Resources for editor."""

import json

from mcp.server.fastmcp import FastMCP

_TOOL_METADATA = {
    "interactive_init_item": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-interactive.ts::initItem",
        "manual_steps": [],
    },
    "interactive_set_control_value": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-interactive.ts::setControlValue",
        "manual_steps": [],
    },
    "interactive_remove_item": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-interactive.ts::removeItem",
        "manual_steps": [],
    },
    "scene_load_scene": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::loadScene",
        "manual_steps": [],
    },
    "scene_clear_scene": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::clearScene",
        "manual_steps": [],
    },
    "scene_unload_scene": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::unloadScene",
        "manual_steps": [],
    },
    "scene_set_scene": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::setScene",
        "manual_steps": [],
    },
    "scene_create_node": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::createNode",
        "manual_steps": [],
    },
    "scene_create_nodes": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::createNodes",
        "manual_steps": [],
    },
    "scene_update_node": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::updateNode",
        "manual_steps": [],
    },
    "scene_update_nodes": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::updateNodes",
        "manual_steps": [],
    },
    "scene_delete_node": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::deleteNode",
        "manual_steps": [],
    },
    "scene_delete_nodes": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::deleteNodes",
        "manual_steps": [],
    },
    "scene_create_collection": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::createCollection",
        "manual_steps": [],
    },
    "scene_delete_collection": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::deleteCollection",
        "manual_steps": [],
    },
    "scene_update_collection": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::updateCollection",
        "manual_steps": [],
    },
    "scene_add_to_collection": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::addToCollection",
        "manual_steps": [],
    },
    "scene_remove_from_collection": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/core/src/store/use-scene.ts::removeFromCollection",
        "manual_steps": [],
    },
    "commandpalette_set_open": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/components/ui/command-palette/index.tsx::setOpen",
        "manual_steps": [],
    },
    "commandpalette_set_mode": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/components/ui/command-palette/index.tsx::setMode",
        "manual_steps": [],
    },
    "commandpalette_set_input_value": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/components/ui/command-palette/index.tsx::setInputValue",
        "manual_steps": [],
    },
    "commandpalette_navigate_to": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/components/ui/command-palette/index.tsx::navigateTo",
        "manual_steps": [],
    },
    "commandpalette_go_back": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/components/ui/command-palette/index.tsx::goBack",
        "manual_steps": [],
    },
    "commandpalette_set_camera_scope": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/components/ui/command-palette/index.tsx::setCameraScope",
        "manual_steps": [],
    },
    "sidebarstore_set_width": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/components/ui/primitives/sidebar.tsx::setWidth",
        "manual_steps": [],
    },
    "sidebarstore_set_is_dragging": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/components/ui/primitives/sidebar.tsx::setIsDragging",
        "manual_steps": [],
    },
    "audio_set_master_volume": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-audio.tsx::setMasterVolume",
        "manual_steps": [],
    },
    "audio_set_sfx_volume": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-audio.tsx::setSfxVolume",
        "manual_steps": [],
    },
    "audio_set_radio_volume": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-audio.tsx::setRadioVolume",
        "manual_steps": [],
    },
    "audio_set_radio_playing": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-audio.tsx::setRadioPlaying",
        "manual_steps": [],
    },
    "audio_toggle_radio_playing": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-audio.tsx::toggleRadioPlaying",
        "manual_steps": [],
    },
    "audio_toggle_mute": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-audio.tsx::toggleMute",
        "manual_steps": [],
    },
    "audio_set_autoplay": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-audio.tsx::setAutoplay",
        "manual_steps": [],
    },
    "commandregistry_register": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-command-registry.ts::register",
        "manual_steps": [],
    },
    "editor_set_phase": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setPhase",
        "manual_steps": [],
    },
    "editor_set_mode": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setMode",
        "manual_steps": [],
    },
    "editor_set_tool": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setTool",
        "manual_steps": [],
    },
    "editor_set_structure_layer": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setStructureLayer",
        "manual_steps": [],
    },
    "editor_set_catalog_category": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setCatalogCategory",
        "manual_steps": [],
    },
    "editor_set_selected_item": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setSelectedItem",
        "manual_steps": [],
    },
    "editor_set_selected_reference_id": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setSelectedReferenceId",
        "manual_steps": [],
    },
    "editor_set_spaces": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setSpaces",
        "manual_steps": [],
    },
    "editor_set_editing_hole": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setEditingHole",
        "manual_steps": [],
    },
    "editor_set_preview_mode": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setPreviewMode",
        "manual_steps": [],
    },
    "editor_set_floorplan_open": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setFloorplanOpen",
        "manual_steps": [],
    },
    "editor_toggle_floorplan_open": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::toggleFloorplanOpen",
        "manual_steps": [],
    },
    "editor_set_floorplan_hovered": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setFloorplanHovered",
        "manual_steps": [],
    },
    "editor_set_allow_underground_camera": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-editor.tsx::setAllowUndergroundCamera",
        "manual_steps": [],
    },
    "paletteviewregistry_register": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-palette-view-registry.ts::register",
        "manual_steps": [],
    },
    "uploadstore_start_upload": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-upload.ts::startUpload",
        "manual_steps": [],
    },
    "uploadstore_set_progress": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-upload.ts::setProgress",
        "manual_steps": [],
    },
    "uploadstore_set_status": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-upload.ts::setStatus",
        "manual_steps": [],
    },
    "uploadstore_set_error": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-upload.ts::setError",
        "manual_steps": [],
    },
    "uploadstore_set_result": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-upload.ts::setResult",
        "manual_steps": [],
    },
    "uploadstore_clear_upload": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/editor/src/store/use-upload.ts::clearUpload",
        "manual_steps": [],
    },
    "itemlightpool_register": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-item-light-pool.ts::register",
        "manual_steps": [],
    },
    "itemlightpool_unregister": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-item-light-pool.ts::unregister",
        "manual_steps": [],
    },
    "viewer_set_hovered_id": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setHoveredId",
        "manual_steps": [],
    },
    "viewer_set_camera_mode": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setCameraMode",
        "manual_steps": [],
    },
    "viewer_set_theme": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setTheme",
        "manual_steps": [],
    },
    "viewer_set_unit": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setUnit",
        "manual_steps": [],
    },
    "viewer_set_level_mode": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setLevelMode",
        "manual_steps": [],
    },
    "viewer_set_wall_mode": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setWallMode",
        "manual_steps": [],
    },
    "viewer_set_show_scans": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setShowScans",
        "manual_steps": [],
    },
    "viewer_set_show_guides": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setShowGuides",
        "manual_steps": [],
    },
    "viewer_set_show_grid": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setShowGrid",
        "manual_steps": [],
    },
    "viewer_set_project_id": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setProjectId",
        "manual_steps": [],
    },
    "viewer_set_selection": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setSelection",
        "manual_steps": [],
    },
    "viewer_reset_selection": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::resetSelection",
        "manual_steps": [],
    },
    "viewer_export_scene": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::exportScene",
        "manual_steps": [],
    },
    "viewer_set_debug_colors": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setDebugColors",
        "manual_steps": [],
    },
    "viewer_set_camera_dragging": {
        "generation_status": "proxy",
        "generation_notes": "Forwards action to the browser\u0027s Zustand store via the generated WebSocket bridge.",
        "implementation_hint": "Source: packages/viewer/src/store/use-viewer.ts::setCameraDragging",
        "manual_steps": [],
    },
}


def register_resources(server: FastMCP, _get_backend) -> None:
    """Register resources with the server."""

    @server.resource("app://editor/status")
    async def editor_status() -> str:
        """Current status and version of editor"""
        return json.dumps({
            "name": "editor",
            "status": "running",
            "tool_generation": {
                "ready": 0,
                "proxy": 72,
                "scaffolded": 0,
                "stubbed": 0,
            },
        }, indent=2)

    @server.resource("app://editor/commands")
    async def editor_commands() -> str:
        """Available commands and tools in editor"""
        tools = await server.list_tools()
        commands = []
        for tool in tools:
            metadata = _TOOL_METADATA.get(tool.name, {})
            commands.append({
                "name": tool.name,
                "description": tool.description or "",
                "generation_status": metadata.get("generation_status", "ready"),
                "generation_notes": metadata.get("generation_notes", ""),
                "manual_steps": metadata.get("manual_steps", []),
            })
        return json.dumps({"commands": commands}, indent=2)

    @server.resource("docs://editor/tool-index")
    async def editor_tool_index() -> str:
        """Complete index of all editor tools with parameters and usage"""
        # Dynamic documentation resource
        tools = await server.list_tools()
        doc_entries = []
        for tool in tools:
            metadata = _TOOL_METADATA.get(tool.name, {})
            entry = {"name": tool.name, "description": tool.description or ""}
            if hasattr(tool, "inputSchema") and tool.inputSchema:
                entry["parameters"] = tool.inputSchema.get("properties", {})
                entry["required"] = tool.inputSchema.get("required", [])
            entry["generation_status"] = metadata.get("generation_status", "ready")
            entry["generation_notes"] = metadata.get("generation_notes", "")
            entry["implementation_hint"] = metadata.get("implementation_hint", "")
            entry["manual_steps"] = metadata.get("manual_steps", [])
            doc_entries.append(entry)
        return json.dumps({
            "server": "editor",
            "resource": "docs://editor/tool-index",
            "tools": doc_entries,
        }, indent=2)

    @server.resource("docs://editor/zustand_action")
    async def editor_zustand_action_docs() -> str:
        """Documentation for editor zustand_action capabilities"""
        # Dynamic documentation resource
        tools = await server.list_tools()
        doc_entries = []
        for tool in tools:
            metadata = _TOOL_METADATA.get(tool.name, {})
            entry = {"name": tool.name, "description": tool.description or ""}
            if hasattr(tool, "inputSchema") and tool.inputSchema:
                entry["parameters"] = tool.inputSchema.get("properties", {})
                entry["required"] = tool.inputSchema.get("required", [])
            entry["generation_status"] = metadata.get("generation_status", "ready")
            entry["generation_notes"] = metadata.get("generation_notes", "")
            entry["implementation_hint"] = metadata.get("implementation_hint", "")
            entry["manual_steps"] = metadata.get("manual_steps", [])
            doc_entries.append(entry)
        return json.dumps({
            "server": "editor",
            "resource": "docs://editor/zustand_action",
            "tools": doc_entries,
        }, indent=2)

