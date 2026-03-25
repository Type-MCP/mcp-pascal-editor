"""Data models for editor MCP server."""

from dataclasses import dataclass
from typing import Any


@dataclass
class InteractiveInitItemParams:
    """Parameters for interactive_init_item."""
    itemId: str
    interactive: dict

@dataclass
class InteractiveSetControlValueParams:
    """Parameters for interactive_set_control_value."""
    itemId: str
    index: float
    value: dict

@dataclass
class InteractiveRemoveItemParams:
    """Parameters for interactive_remove_item."""
    itemId: str

@dataclass
class SceneSetSceneParams:
    """Parameters for scene_set_scene."""
    nodes: dict
    rootNodeIds: list

@dataclass
class SceneCreateNodeParams:
    """Parameters for scene_create_node."""
    node: dict
    parentId: str | None = None

@dataclass
class SceneCreateNodesParams:
    """Parameters for scene_create_nodes."""
    ops: list

@dataclass
class SceneUpdateNodeParams:
    """Parameters for scene_update_node."""
    id: str
    data: dict

@dataclass
class SceneUpdateNodesParams:
    """Parameters for scene_update_nodes."""
    updates: list

@dataclass
class SceneDeleteNodeParams:
    """Parameters for scene_delete_node."""
    id: str

@dataclass
class SceneDeleteNodesParams:
    """Parameters for scene_delete_nodes."""
    ids: list

@dataclass
class SceneCreateCollectionParams:
    """Parameters for scene_create_collection."""
    name: str
    nodeIds: list | None = None

@dataclass
class SceneDeleteCollectionParams:
    """Parameters for scene_delete_collection."""
    id: str

@dataclass
class SceneUpdateCollectionParams:
    """Parameters for scene_update_collection."""
    id: str
    data: dict

@dataclass
class SceneAddToCollectionParams:
    """Parameters for scene_add_to_collection."""
    id: str
    nodeId: str

@dataclass
class SceneRemoveFromCollectionParams:
    """Parameters for scene_remove_from_collection."""
    id: str
    nodeId: str

@dataclass
class CommandpaletteSetOpenParams:
    """Parameters for commandpalette_set_open."""
    open: bool

@dataclass
class CommandpaletteSetModeParams:
    """Parameters for commandpalette_set_mode."""
    mode: str

@dataclass
class CommandpaletteSetInputValueParams:
    """Parameters for commandpalette_set_input_value."""
    value: str

@dataclass
class CommandpaletteNavigateToParams:
    """Parameters for commandpalette_navigate_to."""
    page: str

@dataclass
class CommandpaletteSetCameraScopeParams:
    """Parameters for commandpalette_set_camera_scope."""
    scope: dict

@dataclass
class SidebarstoreSetWidthParams:
    """Parameters for sidebarstore_set_width."""
    width: float

@dataclass
class SidebarstoreSetIsDraggingParams:
    """Parameters for sidebarstore_set_is_dragging."""
    isDragging: bool

@dataclass
class AudioSetMasterVolumeParams:
    """Parameters for audio_set_master_volume."""
    v: float

@dataclass
class AudioSetSfxVolumeParams:
    """Parameters for audio_set_sfx_volume."""
    v: float

@dataclass
class AudioSetRadioVolumeParams:
    """Parameters for audio_set_radio_volume."""
    v: float

@dataclass
class AudioSetRadioPlayingParams:
    """Parameters for audio_set_radio_playing."""
    v: bool

@dataclass
class AudioSetAutoplayParams:
    """Parameters for audio_set_autoplay."""
    v: bool

@dataclass
class CommandregistryRegisterParams:
    """Parameters for commandregistry_register."""
    actions: list

@dataclass
class EditorSetPhaseParams:
    """Parameters for editor_set_phase."""
    phase: dict

@dataclass
class EditorSetModeParams:
    """Parameters for editor_set_mode."""
    mode: dict

@dataclass
class EditorSetToolParams:
    """Parameters for editor_set_tool."""
    tool: dict

@dataclass
class EditorSetStructureLayerParams:
    """Parameters for editor_set_structure_layer."""
    layer: dict

@dataclass
class EditorSetCatalogCategoryParams:
    """Parameters for editor_set_catalog_category."""
    category: dict

@dataclass
class EditorSetSelectedItemParams:
    """Parameters for editor_set_selected_item."""
    item: dict

@dataclass
class EditorSetSelectedReferenceIdParams:
    """Parameters for editor_set_selected_reference_id."""
    id: str

@dataclass
class EditorSetSpacesParams:
    """Parameters for editor_set_spaces."""
    spaces: dict

@dataclass
class EditorSetEditingHoleParams:
    """Parameters for editor_set_editing_hole."""
    hole: dict

@dataclass
class EditorSetPreviewModeParams:
    """Parameters for editor_set_preview_mode."""
    preview: bool

@dataclass
class EditorSetFloorplanOpenParams:
    """Parameters for editor_set_floorplan_open."""
    open: bool

@dataclass
class EditorSetFloorplanHoveredParams:
    """Parameters for editor_set_floorplan_hovered."""
    hovered: bool

@dataclass
class EditorSetAllowUndergroundCameraParams:
    """Parameters for editor_set_allow_underground_camera."""
    enabled: bool

@dataclass
class PaletteviewregistryRegisterParams:
    """Parameters for paletteviewregistry_register."""
    view: dict

@dataclass
class UploadstoreStartUploadParams:
    """Parameters for uploadstore_start_upload."""
    levelId: str
    assetType: str
    fileName: str

@dataclass
class UploadstoreSetProgressParams:
    """Parameters for uploadstore_set_progress."""
    levelId: str
    progress: float

@dataclass
class UploadstoreSetStatusParams:
    """Parameters for uploadstore_set_status."""
    levelId: str
    status: dict

@dataclass
class UploadstoreSetErrorParams:
    """Parameters for uploadstore_set_error."""
    levelId: str
    error: str

@dataclass
class UploadstoreSetResultParams:
    """Parameters for uploadstore_set_result."""
    levelId: str
    url: str

@dataclass
class UploadstoreClearUploadParams:
    """Parameters for uploadstore_clear_upload."""
    levelId: str

@dataclass
class ItemlightpoolRegisterParams:
    """Parameters for itemlightpool_register."""
    key: str
    nodeId: str
    effect: dict
    interactive: dict

@dataclass
class ItemlightpoolUnregisterParams:
    """Parameters for itemlightpool_unregister."""
    key: str

@dataclass
class ViewerSetHoveredIdParams:
    """Parameters for viewer_set_hovered_id."""
    id: str

@dataclass
class ViewerSetCameraModeParams:
    """Parameters for viewer_set_camera_mode."""
    mode: str

@dataclass
class ViewerSetThemeParams:
    """Parameters for viewer_set_theme."""
    theme: str

@dataclass
class ViewerSetUnitParams:
    """Parameters for viewer_set_unit."""
    unit: str

@dataclass
class ViewerSetLevelModeParams:
    """Parameters for viewer_set_level_mode."""
    mode: str

@dataclass
class ViewerSetWallModeParams:
    """Parameters for viewer_set_wall_mode."""
    mode: str

@dataclass
class ViewerSetShowScansParams:
    """Parameters for viewer_set_show_scans."""
    show: bool

@dataclass
class ViewerSetShowGuidesParams:
    """Parameters for viewer_set_show_guides."""
    show: bool

@dataclass
class ViewerSetShowGridParams:
    """Parameters for viewer_set_show_grid."""
    show: bool

@dataclass
class ViewerSetProjectIdParams:
    """Parameters for viewer_set_project_id."""
    id: str

@dataclass
class ViewerSetSelectionParams:
    """Parameters for viewer_set_selection."""
    updates: dict

@dataclass
class ViewerSetDebugColorsParams:
    """Parameters for viewer_set_debug_colors."""
    enabled: bool

@dataclass
class ViewerSetCameraDraggingParams:
    """Parameters for viewer_set_camera_dragging."""
    dragging: bool

