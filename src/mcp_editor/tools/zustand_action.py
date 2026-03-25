"""zustand_action tools for editor."""

import inspect
import json
import sys
import importlib
import importlib.util
from pathlib import Path

from mcp.server.fastmcp import FastMCP

from mcp_editor.backend import BackendError

# Instance cache for reusing class instances across tool calls
_instance_cache: dict[str, object] = {}


def _get_or_create_instance(mod, class_name: str, **init_kwargs):
    """Get a cached class instance or create a new one."""
    cache_key = f"{mod.__name__}.{class_name}"
    if init_kwargs:
        # When explicit init args are provided, always create fresh
        cls = getattr(mod, class_name)
        return cls(**init_kwargs)
    if cache_key not in _instance_cache:
        cls = getattr(mod, class_name)
        try:
            _instance_cache[cache_key] = cls()
        except TypeError:
            # __init__ requires arguments we don't have — try with empty defaults
            import inspect as _ins
            sig = _ins.signature(cls.__init__)
            kwargs = {}
            for name, param in sig.parameters.items():
                if name == "self":
                    continue
                if param.default is not _ins.Parameter.empty:
                    kwargs[name] = param.default
                elif param.annotation is str or param.annotation == "str":
                    kwargs[name] = ""
                elif param.annotation is int or param.annotation == "int":
                    kwargs[name] = 0
                elif param.annotation is bool or param.annotation == "bool":
                    kwargs[name] = False
                elif param.annotation is list or param.annotation == "list":
                    kwargs[name] = []
                elif param.annotation is dict or param.annotation == "dict":
                    kwargs[name] = {}
                else:
                    kwargs[name] = None
            _instance_cache[cache_key] = cls(**kwargs)
    return _instance_cache[cache_key]


def _setup_import_path(codebase_path: str):
    """Add codebase to sys.path for imports."""
    codebase = Path(codebase_path)
    for path in [str(codebase), str(codebase.parent)]:
        if path not in sys.path:
            sys.path.insert(0, path)


def _load_source_module(codebase_path: str, module_path: str):
    """Load a module from the source codebase, avoiding package name collisions.

    Strategy:
    1. If codebase is inside a proper Python package (has __init__.py in parent),
       use the package's canonical import path.
    2. Otherwise, use importlib.util.spec_from_file_location to load directly
       from the source file, bypassing sys.modules name conflicts.
    """
    codebase = Path(codebase_path)

    # Check if codebase is itself a Python package (e.g., /path/to/wand/)
    if (codebase / "__init__.py").exists():
        # This is a package — import using package.module path
        package_name = codebase.name
        parent_dir = str(codebase.parent)
        if parent_dir not in sys.path:
            sys.path.insert(0, parent_dir)
        full_module = f"{package_name}.{module_path}" if module_path != package_name else package_name
        try:
            return importlib.import_module(full_module)
        except ImportError:
            pass

    # For standalone files, load directly by file path to avoid name collisions
    parts = module_path.split(".")
    file_path = codebase / (parts[-1] + ".py") if len(parts) == 1 else codebase / "/".join(parts[:-1]) / (parts[-1] + ".py")
    if not file_path.exists():
        file_path = codebase / (module_path.replace(".", "/") + ".py")
    if not file_path.exists():
        # Final fallback: regular import
        return importlib.import_module(module_path)

    # Use a collision-safe name in sys.modules
    safe_name = f"_mcp_src_{codebase.name}_.{module_path}"
    if safe_name in sys.modules:
        return sys.modules[safe_name]

    spec = importlib.util.spec_from_file_location(safe_name, file_path,
        submodule_search_locations=[str(codebase)])
    if spec is None or spec.loader is None:
        return importlib.import_module(module_path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[safe_name] = mod
    spec.loader.exec_module(mod)
    return mod


def register_tools(server: FastMCP, _get_backend) -> None:
    """Register zustand_action tools with the server."""

    @server.tool()
    async def interactive_init_item(
        itemId: str,
        interactive: dict,
    ) -> str:
        """Init item in the interactive store"""
        # Protocol call: interactive_init_item
        kwargs: dict[str, object] = {}
        if itemId is not None:
            kwargs["itemId"] = itemId
        if interactive is not None:
            kwargs["interactive"] = interactive
        try:
            return await _get_backend().execute("interactive_init_item", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def interactive_set_control_value(
        itemId: str,
        index: float,
        value: dict,
    ) -> str:
        """Set control value in the interactive store"""
        # Protocol call: interactive_set_control_value
        kwargs: dict[str, object] = {}
        if itemId is not None:
            kwargs["itemId"] = itemId
        if index is not None:
            kwargs["index"] = index
        if value is not None:
            kwargs["value"] = value
        try:
            return await _get_backend().execute("interactive_set_control_value", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def interactive_remove_item(
        itemId: str,
    ) -> str:
        """Remove item in the interactive store"""
        # Protocol call: interactive_remove_item
        kwargs: dict[str, object] = {}
        if itemId is not None:
            kwargs["itemId"] = itemId
        try:
            return await _get_backend().execute("interactive_remove_item", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_load_scene(
    ) -> str:
        """Load scene in the scene store"""
        # Protocol call: scene_load_scene
        kwargs: dict[str, object] = {}
        try:
            return await _get_backend().execute("scene_load_scene", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_clear_scene(
    ) -> str:
        """Clear scene in the scene store"""
        # Protocol call: scene_clear_scene
        kwargs: dict[str, object] = {}
        try:
            return await _get_backend().execute("scene_clear_scene", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_unload_scene(
    ) -> str:
        """Unload scene in the scene store"""
        # Protocol call: scene_unload_scene
        kwargs: dict[str, object] = {}
        try:
            return await _get_backend().execute("scene_unload_scene", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_set_scene(
        nodes: dict,
        rootNodeIds: list,
    ) -> str:
        """Set scene in the scene store"""
        # Protocol call: scene_set_scene
        kwargs: dict[str, object] = {}
        if nodes is not None:
            kwargs["nodes"] = nodes
        if rootNodeIds is not None:
            kwargs["rootNodeIds"] = rootNodeIds
        try:
            return await _get_backend().execute("scene_set_scene", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_create_node(
        node: dict,
        parentId: str | None = None,
    ) -> str:
        """Create node in the scene store"""
        # Protocol call: scene_create_node
        kwargs: dict[str, object] = {}
        if node is not None:
            kwargs["node"] = node
        if parentId is not None:
            kwargs["parentId"] = parentId
        try:
            return await _get_backend().execute("scene_create_node", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_create_nodes(
        ops: list,
    ) -> str:
        """Create nodes in the scene store"""
        # Protocol call: scene_create_nodes
        kwargs: dict[str, object] = {}
        if ops is not None:
            kwargs["ops"] = ops
        try:
            return await _get_backend().execute("scene_create_nodes", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_update_node(
        id: str,
        data: dict,
    ) -> str:
        """Update node in the scene store"""
        # Protocol call: scene_update_node
        kwargs: dict[str, object] = {}
        if id is not None:
            kwargs["id"] = id
        if data is not None:
            kwargs["data"] = data
        try:
            return await _get_backend().execute("scene_update_node", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_update_nodes(
        updates: list,
    ) -> str:
        """Update nodes in the scene store"""
        # Protocol call: scene_update_nodes
        kwargs: dict[str, object] = {}
        if updates is not None:
            kwargs["updates"] = updates
        try:
            return await _get_backend().execute("scene_update_nodes", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_delete_node(
        id: str,
    ) -> str:
        """Delete node in the scene store"""
        # Protocol call: scene_delete_node
        kwargs: dict[str, object] = {}
        if id is not None:
            kwargs["id"] = id
        try:
            return await _get_backend().execute("scene_delete_node", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_delete_nodes(
        ids: list,
    ) -> str:
        """Delete nodes in the scene store"""
        # Protocol call: scene_delete_nodes
        kwargs: dict[str, object] = {}
        if ids is not None:
            kwargs["ids"] = ids
        try:
            return await _get_backend().execute("scene_delete_nodes", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_create_collection(
        name: str,
        nodeIds: list | None = None,
    ) -> str:
        """Create collection in the scene store"""
        # Protocol call: scene_create_collection
        kwargs: dict[str, object] = {}
        if name is not None:
            kwargs["name"] = name
        if nodeIds is not None:
            kwargs["nodeIds"] = nodeIds
        try:
            return await _get_backend().execute("scene_create_collection", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_delete_collection(
        id: str,
    ) -> str:
        """Delete collection in the scene store"""
        # Protocol call: scene_delete_collection
        kwargs: dict[str, object] = {}
        if id is not None:
            kwargs["id"] = id
        try:
            return await _get_backend().execute("scene_delete_collection", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_update_collection(
        id: str,
        data: dict,
    ) -> str:
        """Update collection in the scene store"""
        # Protocol call: scene_update_collection
        kwargs: dict[str, object] = {}
        if id is not None:
            kwargs["id"] = id
        if data is not None:
            kwargs["data"] = data
        try:
            return await _get_backend().execute("scene_update_collection", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_add_to_collection(
        id: str,
        nodeId: str,
    ) -> str:
        """Add to collection in the scene store"""
        # Protocol call: scene_add_to_collection
        kwargs: dict[str, object] = {}
        if id is not None:
            kwargs["id"] = id
        if nodeId is not None:
            kwargs["nodeId"] = nodeId
        try:
            return await _get_backend().execute("scene_add_to_collection", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def scene_remove_from_collection(
        id: str,
        nodeId: str,
    ) -> str:
        """Remove from collection in the scene store"""
        # Protocol call: scene_remove_from_collection
        kwargs: dict[str, object] = {}
        if id is not None:
            kwargs["id"] = id
        if nodeId is not None:
            kwargs["nodeId"] = nodeId
        try:
            return await _get_backend().execute("scene_remove_from_collection", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def commandpalette_set_open(
        open: bool,
    ) -> str:
        """Set open in the commandpalette store"""
        # Protocol call: commandpalette_set_open
        kwargs: dict[str, object] = {}
        if open is not None:
            kwargs["open"] = open
        try:
            return await _get_backend().execute("commandpalette_set_open", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def commandpalette_set_mode(
        mode: str,
    ) -> str:
        """Set mode in the commandpalette store"""
        # Protocol call: commandpalette_set_mode
        kwargs: dict[str, object] = {}
        if mode is not None:
            kwargs["mode"] = mode
        try:
            return await _get_backend().execute("commandpalette_set_mode", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def commandpalette_set_input_value(
        value: str,
    ) -> str:
        """Set input value in the commandpalette store"""
        # Protocol call: commandpalette_set_input_value
        kwargs: dict[str, object] = {}
        if value is not None:
            kwargs["value"] = value
        try:
            return await _get_backend().execute("commandpalette_set_input_value", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def commandpalette_navigate_to(
        page: str,
    ) -> str:
        """Navigate to in the commandpalette store"""
        # Protocol call: commandpalette_navigate_to
        kwargs: dict[str, object] = {}
        if page is not None:
            kwargs["page"] = page
        try:
            return await _get_backend().execute("commandpalette_navigate_to", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def commandpalette_go_back(
    ) -> str:
        """Go back in the commandpalette store"""
        # Protocol call: commandpalette_go_back
        kwargs: dict[str, object] = {}
        try:
            return await _get_backend().execute("commandpalette_go_back", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def commandpalette_set_camera_scope(
        scope: dict,
    ) -> str:
        """Set camera scope in the commandpalette store"""
        # Protocol call: commandpalette_set_camera_scope
        kwargs: dict[str, object] = {}
        if scope is not None:
            kwargs["scope"] = scope
        try:
            return await _get_backend().execute("commandpalette_set_camera_scope", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def sidebarstore_set_width(
        width: float,
    ) -> str:
        """Set width in the sidebarstore store"""
        # Protocol call: sidebarstore_set_width
        kwargs: dict[str, object] = {}
        if width is not None:
            kwargs["width"] = width
        try:
            return await _get_backend().execute("sidebarstore_set_width", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def sidebarstore_set_is_dragging(
        isDragging: bool,
    ) -> str:
        """Set is dragging in the sidebarstore store"""
        # Protocol call: sidebarstore_set_is_dragging
        kwargs: dict[str, object] = {}
        if isDragging is not None:
            kwargs["isDragging"] = isDragging
        try:
            return await _get_backend().execute("sidebarstore_set_is_dragging", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def audio_set_master_volume(
        v: float,
    ) -> str:
        """Set master volume in the audio store"""
        # Protocol call: audio_set_master_volume
        kwargs: dict[str, object] = {}
        if v is not None:
            kwargs["v"] = v
        try:
            return await _get_backend().execute("audio_set_master_volume", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def audio_set_sfx_volume(
        v: float,
    ) -> str:
        """Set sfx volume in the audio store"""
        # Protocol call: audio_set_sfx_volume
        kwargs: dict[str, object] = {}
        if v is not None:
            kwargs["v"] = v
        try:
            return await _get_backend().execute("audio_set_sfx_volume", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def audio_set_radio_volume(
        v: float,
    ) -> str:
        """Set radio volume in the audio store"""
        # Protocol call: audio_set_radio_volume
        kwargs: dict[str, object] = {}
        if v is not None:
            kwargs["v"] = v
        try:
            return await _get_backend().execute("audio_set_radio_volume", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def audio_set_radio_playing(
        v: bool,
    ) -> str:
        """Set radio playing in the audio store"""
        # Protocol call: audio_set_radio_playing
        kwargs: dict[str, object] = {}
        if v is not None:
            kwargs["v"] = v
        try:
            return await _get_backend().execute("audio_set_radio_playing", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def audio_toggle_radio_playing(
    ) -> str:
        """Toggle radio playing in the audio store"""
        # Protocol call: audio_toggle_radio_playing
        kwargs: dict[str, object] = {}
        try:
            return await _get_backend().execute("audio_toggle_radio_playing", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def audio_toggle_mute(
    ) -> str:
        """Toggle mute in the audio store"""
        # Protocol call: audio_toggle_mute
        kwargs: dict[str, object] = {}
        try:
            return await _get_backend().execute("audio_toggle_mute", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def audio_set_autoplay(
        v: bool,
    ) -> str:
        """Set autoplay in the audio store"""
        # Protocol call: audio_set_autoplay
        kwargs: dict[str, object] = {}
        if v is not None:
            kwargs["v"] = v
        try:
            return await _get_backend().execute("audio_set_autoplay", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def commandregistry_register(
        actions: list,
    ) -> str:
        """Register in the commandregistry store"""
        # Protocol call: commandregistry_register
        kwargs: dict[str, object] = {}
        if actions is not None:
            kwargs["actions"] = actions
        try:
            return await _get_backend().execute("commandregistry_register", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_phase(
        phase: dict,
    ) -> str:
        """Set phase in the editor store"""
        # Protocol call: editor_set_phase
        kwargs: dict[str, object] = {}
        if phase is not None:
            kwargs["phase"] = phase
        try:
            return await _get_backend().execute("editor_set_phase", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_mode(
        mode: dict,
    ) -> str:
        """Set mode in the editor store"""
        # Protocol call: editor_set_mode
        kwargs: dict[str, object] = {}
        if mode is not None:
            kwargs["mode"] = mode
        try:
            return await _get_backend().execute("editor_set_mode", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_tool(
        tool: dict,
    ) -> str:
        """Set tool in the editor store"""
        # Protocol call: editor_set_tool
        kwargs: dict[str, object] = {}
        if tool is not None:
            kwargs["tool"] = tool
        try:
            return await _get_backend().execute("editor_set_tool", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_structure_layer(
        layer: dict,
    ) -> str:
        """Set structure layer in the editor store"""
        # Protocol call: editor_set_structure_layer
        kwargs: dict[str, object] = {}
        if layer is not None:
            kwargs["layer"] = layer
        try:
            return await _get_backend().execute("editor_set_structure_layer", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_catalog_category(
        category: dict,
    ) -> str:
        """Set catalog category in the editor store"""
        # Protocol call: editor_set_catalog_category
        kwargs: dict[str, object] = {}
        if category is not None:
            kwargs["category"] = category
        try:
            return await _get_backend().execute("editor_set_catalog_category", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_selected_item(
        item: dict,
    ) -> str:
        """Set selected item in the editor store"""
        # Protocol call: editor_set_selected_item
        kwargs: dict[str, object] = {}
        if item is not None:
            kwargs["item"] = item
        try:
            return await _get_backend().execute("editor_set_selected_item", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_selected_reference_id(
        id: str,
    ) -> str:
        """Set selected reference id in the editor store"""
        # Protocol call: editor_set_selected_reference_id
        kwargs: dict[str, object] = {}
        if id is not None:
            kwargs["id"] = id
        try:
            return await _get_backend().execute("editor_set_selected_reference_id", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_spaces(
        spaces: dict,
    ) -> str:
        """Set spaces in the editor store"""
        # Protocol call: editor_set_spaces
        kwargs: dict[str, object] = {}
        if spaces is not None:
            kwargs["spaces"] = spaces
        try:
            return await _get_backend().execute("editor_set_spaces", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_editing_hole(
        hole: dict,
    ) -> str:
        """Set editing hole in the editor store"""
        # Protocol call: editor_set_editing_hole
        kwargs: dict[str, object] = {}
        if hole is not None:
            kwargs["hole"] = hole
        try:
            return await _get_backend().execute("editor_set_editing_hole", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_preview_mode(
        preview: bool,
    ) -> str:
        """Set preview mode in the editor store"""
        # Protocol call: editor_set_preview_mode
        kwargs: dict[str, object] = {}
        if preview is not None:
            kwargs["preview"] = preview
        try:
            return await _get_backend().execute("editor_set_preview_mode", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_floorplan_open(
        open: bool,
    ) -> str:
        """Set floorplan open in the editor store"""
        # Protocol call: editor_set_floorplan_open
        kwargs: dict[str, object] = {}
        if open is not None:
            kwargs["open"] = open
        try:
            return await _get_backend().execute("editor_set_floorplan_open", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_toggle_floorplan_open(
    ) -> str:
        """Toggle floorplan open in the editor store"""
        # Protocol call: editor_toggle_floorplan_open
        kwargs: dict[str, object] = {}
        try:
            return await _get_backend().execute("editor_toggle_floorplan_open", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_floorplan_hovered(
        hovered: bool,
    ) -> str:
        """Set floorplan hovered in the editor store"""
        # Protocol call: editor_set_floorplan_hovered
        kwargs: dict[str, object] = {}
        if hovered is not None:
            kwargs["hovered"] = hovered
        try:
            return await _get_backend().execute("editor_set_floorplan_hovered", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def editor_set_allow_underground_camera(
        enabled: bool,
    ) -> str:
        """Set allow underground camera in the editor store"""
        # Protocol call: editor_set_allow_underground_camera
        kwargs: dict[str, object] = {}
        if enabled is not None:
            kwargs["enabled"] = enabled
        try:
            return await _get_backend().execute("editor_set_allow_underground_camera", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def paletteviewregistry_register(
        view: dict,
    ) -> str:
        """Register in the paletteviewregistry store"""
        # Protocol call: paletteviewregistry_register
        kwargs: dict[str, object] = {}
        if view is not None:
            kwargs["view"] = view
        try:
            return await _get_backend().execute("paletteviewregistry_register", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def uploadstore_start_upload(
        levelId: str,
        assetType: str,
        fileName: str,
    ) -> str:
        """Start upload in the uploadstore store"""
        # Protocol call: uploadstore_start_upload
        kwargs: dict[str, object] = {}
        if levelId is not None:
            kwargs["levelId"] = levelId
        if assetType is not None:
            kwargs["assetType"] = assetType
        if fileName is not None:
            kwargs["fileName"] = fileName
        try:
            return await _get_backend().execute("uploadstore_start_upload", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def uploadstore_set_progress(
        levelId: str,
        progress: float,
    ) -> str:
        """Set progress in the uploadstore store"""
        # Protocol call: uploadstore_set_progress
        kwargs: dict[str, object] = {}
        if levelId is not None:
            kwargs["levelId"] = levelId
        if progress is not None:
            kwargs["progress"] = progress
        try:
            return await _get_backend().execute("uploadstore_set_progress", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def uploadstore_set_status(
        levelId: str,
        status: dict,
    ) -> str:
        """Set status in the uploadstore store"""
        # Protocol call: uploadstore_set_status
        kwargs: dict[str, object] = {}
        if levelId is not None:
            kwargs["levelId"] = levelId
        if status is not None:
            kwargs["status"] = status
        try:
            return await _get_backend().execute("uploadstore_set_status", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def uploadstore_set_error(
        levelId: str,
        error: str,
    ) -> str:
        """Set error in the uploadstore store"""
        # Protocol call: uploadstore_set_error
        kwargs: dict[str, object] = {}
        if levelId is not None:
            kwargs["levelId"] = levelId
        if error is not None:
            kwargs["error"] = error
        try:
            return await _get_backend().execute("uploadstore_set_error", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def uploadstore_set_result(
        levelId: str,
        url: str,
    ) -> str:
        """Set result in the uploadstore store"""
        # Protocol call: uploadstore_set_result
        kwargs: dict[str, object] = {}
        if levelId is not None:
            kwargs["levelId"] = levelId
        if url is not None:
            kwargs["url"] = url
        try:
            return await _get_backend().execute("uploadstore_set_result", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def uploadstore_clear_upload(
        levelId: str,
    ) -> str:
        """Clear upload in the uploadstore store"""
        # Protocol call: uploadstore_clear_upload
        kwargs: dict[str, object] = {}
        if levelId is not None:
            kwargs["levelId"] = levelId
        try:
            return await _get_backend().execute("uploadstore_clear_upload", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def itemlightpool_register(
        key: str,
        nodeId: str,
        effect: dict,
        interactive: dict,
    ) -> str:
        """Register in the itemlightpool store"""
        # Protocol call: itemlightpool_register
        kwargs: dict[str, object] = {}
        if key is not None:
            kwargs["key"] = key
        if nodeId is not None:
            kwargs["nodeId"] = nodeId
        if effect is not None:
            kwargs["effect"] = effect
        if interactive is not None:
            kwargs["interactive"] = interactive
        try:
            return await _get_backend().execute("itemlightpool_register", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def itemlightpool_unregister(
        key: str,
    ) -> str:
        """Unregister in the itemlightpool store"""
        # Protocol call: itemlightpool_unregister
        kwargs: dict[str, object] = {}
        if key is not None:
            kwargs["key"] = key
        try:
            return await _get_backend().execute("itemlightpool_unregister", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_hovered_id(
        id: str,
    ) -> str:
        """Set hovered id in the viewer store"""
        # Protocol call: viewer_set_hovered_id
        kwargs: dict[str, object] = {}
        if id is not None:
            kwargs["id"] = id
        try:
            return await _get_backend().execute("viewer_set_hovered_id", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_camera_mode(
        mode: str,
    ) -> str:
        """Set camera mode in the viewer store"""
        # Protocol call: viewer_set_camera_mode
        kwargs: dict[str, object] = {}
        if mode is not None:
            kwargs["mode"] = mode
        try:
            return await _get_backend().execute("viewer_set_camera_mode", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_theme(
        theme: str,
    ) -> str:
        """Set theme in the viewer store"""
        # Protocol call: viewer_set_theme
        kwargs: dict[str, object] = {}
        if theme is not None:
            kwargs["theme"] = theme
        try:
            return await _get_backend().execute("viewer_set_theme", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_unit(
        unit: str,
    ) -> str:
        """Set unit in the viewer store"""
        # Protocol call: viewer_set_unit
        kwargs: dict[str, object] = {}
        if unit is not None:
            kwargs["unit"] = unit
        try:
            return await _get_backend().execute("viewer_set_unit", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_level_mode(
        mode: str,
    ) -> str:
        """Set level mode in the viewer store"""
        # Protocol call: viewer_set_level_mode
        kwargs: dict[str, object] = {}
        if mode is not None:
            kwargs["mode"] = mode
        try:
            return await _get_backend().execute("viewer_set_level_mode", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_wall_mode(
        mode: str,
    ) -> str:
        """Set wall mode in the viewer store"""
        # Protocol call: viewer_set_wall_mode
        kwargs: dict[str, object] = {}
        if mode is not None:
            kwargs["mode"] = mode
        try:
            return await _get_backend().execute("viewer_set_wall_mode", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_show_scans(
        show: bool,
    ) -> str:
        """Set show scans in the viewer store"""
        # Protocol call: viewer_set_show_scans
        kwargs: dict[str, object] = {}
        if show is not None:
            kwargs["show"] = show
        try:
            return await _get_backend().execute("viewer_set_show_scans", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_show_guides(
        show: bool,
    ) -> str:
        """Set show guides in the viewer store"""
        # Protocol call: viewer_set_show_guides
        kwargs: dict[str, object] = {}
        if show is not None:
            kwargs["show"] = show
        try:
            return await _get_backend().execute("viewer_set_show_guides", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_show_grid(
        show: bool,
    ) -> str:
        """Set show grid in the viewer store"""
        # Protocol call: viewer_set_show_grid
        kwargs: dict[str, object] = {}
        if show is not None:
            kwargs["show"] = show
        try:
            return await _get_backend().execute("viewer_set_show_grid", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_project_id(
        id: str,
    ) -> str:
        """Set project id in the viewer store"""
        # Protocol call: viewer_set_project_id
        kwargs: dict[str, object] = {}
        if id is not None:
            kwargs["id"] = id
        try:
            return await _get_backend().execute("viewer_set_project_id", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_selection(
        updates: dict,
    ) -> str:
        """Set selection in the viewer store"""
        # Protocol call: viewer_set_selection
        kwargs: dict[str, object] = {}
        if updates is not None:
            kwargs["updates"] = updates
        try:
            return await _get_backend().execute("viewer_set_selection", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_reset_selection(
    ) -> str:
        """Reset selection in the viewer store"""
        # Protocol call: viewer_reset_selection
        kwargs: dict[str, object] = {}
        try:
            return await _get_backend().execute("viewer_reset_selection", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_export_scene(
    ) -> str:
        """Export scene in the viewer store"""
        # Protocol call: viewer_export_scene
        kwargs: dict[str, object] = {}
        try:
            return await _get_backend().execute("viewer_export_scene", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_debug_colors(
        enabled: bool,
    ) -> str:
        """Set debug colors in the viewer store"""
        # Protocol call: viewer_set_debug_colors
        kwargs: dict[str, object] = {}
        if enabled is not None:
            kwargs["enabled"] = enabled
        try:
            return await _get_backend().execute("viewer_set_debug_colors", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

    @server.tool()
    async def viewer_set_camera_dragging(
        dragging: bool,
    ) -> str:
        """Set camera dragging in the viewer store"""
        # Protocol call: viewer_set_camera_dragging
        kwargs: dict[str, object] = {}
        if dragging is not None:
            kwargs["dragging"] = dragging
        try:
            return await _get_backend().execute("viewer_set_camera_dragging", **kwargs)
        except BackendError as exc:
            return json.dumps(exc.to_dict(), indent=2)

