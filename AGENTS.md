# editor MCP Server

MCP server for editor (with 72 capabilities)

## Available Tools

Status meanings:
- `ready`: direct implementation was generated
- `proxy`: calls a supported upstream backend
- `scaffolded`: generated code needs manual wiring before production use
- `stubbed`: no implementation was generated

### interactive_init_item

Init item in the interactive store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-interactive.ts::initItem`

Parameters:
- `itemId` (string): itemId (AnyNodeId)
- `interactive` (object): interactive (Interactive)
### interactive_set_control_value

Set control value in the interactive store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-interactive.ts::setControlValue`

Parameters:
- `itemId` (string): itemId (AnyNodeId)
- `index` (number): index (number)
- `value` (object): value (ControlValue)
### interactive_remove_item

Remove item in the interactive store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-interactive.ts::removeItem`

Parameters:
- `itemId` (string): itemId (AnyNodeId)
### scene_load_scene

Load scene in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::loadScene`

### scene_clear_scene

Clear scene in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::clearScene`

### scene_unload_scene

Unload scene in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::unloadScene`

### scene_set_scene

Set scene in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::setScene`

Parameters:
- `nodes` (object): nodes (Record<AnyNodeId, AnyNode>)
- `rootNodeIds` (array): rootNodeIds (AnyNodeId[])
### scene_create_node

Create node in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::createNode`

Parameters:
- `node` (object): node (AnyNode)
- `parentId` (string, optional): parentId (AnyNodeId)
### scene_create_nodes

Create nodes in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::createNodes`

Parameters:
- `ops` (array): ops ({ node: AnyNode; parentId?: AnyNodeId }[])
### scene_update_node

Update node in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::updateNode`

Parameters:
- `id` (string): id (AnyNodeId)
- `data` (object): data (Partial<AnyNode>)
### scene_update_nodes

Update nodes in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::updateNodes`

Parameters:
- `updates` (array): updates ({ id: AnyNodeId; data: Partial<AnyNode> }[])
### scene_delete_node

Delete node in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::deleteNode`

Parameters:
- `id` (string): id (AnyNodeId)
### scene_delete_nodes

Delete nodes in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::deleteNodes`

Parameters:
- `ids` (array): ids (AnyNodeId[])
### scene_create_collection

Create collection in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::createCollection`

Parameters:
- `name` (string): name (string)
- `nodeIds` (array, optional): nodeIds (AnyNodeId[])
### scene_delete_collection

Delete collection in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::deleteCollection`

Parameters:
- `id` (string): id (CollectionId)
### scene_update_collection

Update collection in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::updateCollection`

Parameters:
- `id` (string): id (CollectionId)
- `data` (object): data (Partial<Omit<Collection, 'id'>>)
### scene_add_to_collection

Add to collection in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::addToCollection`

Parameters:
- `id` (string): id (CollectionId)
- `nodeId` (string): nodeId (AnyNodeId)
### scene_remove_from_collection

Remove from collection in the scene store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/core/src/store/use-scene.ts::removeFromCollection`

Parameters:
- `id` (string): id (CollectionId)
- `nodeId` (string): nodeId (AnyNodeId)
### commandpalette_set_open

Set open in the commandpalette store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/components/ui/command-palette/index.tsx::setOpen`

Parameters:
- `open` (boolean): open (boolean)
### commandpalette_set_mode

Set mode in the commandpalette store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/components/ui/command-palette/index.tsx::setMode`

Parameters:
- `mode` (string): mode (string)
### commandpalette_set_input_value

Set input value in the commandpalette store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/components/ui/command-palette/index.tsx::setInputValue`

Parameters:
- `value` (string): value (string)
### commandpalette_navigate_to

Navigate to in the commandpalette store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/components/ui/command-palette/index.tsx::navigateTo`

Parameters:
- `page` (string): page (string)
### commandpalette_go_back

Go back in the commandpalette store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/components/ui/command-palette/index.tsx::goBack`

### commandpalette_set_camera_scope

Set camera scope in the commandpalette store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/components/ui/command-palette/index.tsx::setCameraScope`

Parameters:
- `scope` (object): scope ({ nodeId: string; label: string } | null)
### sidebarstore_set_width

Set width in the sidebarstore store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/components/ui/primitives/sidebar.tsx::setWidth`

Parameters:
- `width` (number): width (number)
### sidebarstore_set_is_dragging

Set is dragging in the sidebarstore store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/components/ui/primitives/sidebar.tsx::setIsDragging`

Parameters:
- `isDragging` (boolean): isDragging (boolean)
### audio_set_master_volume

Set master volume in the audio store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-audio.tsx::setMasterVolume`

Parameters:
- `v` (number): v (number)
### audio_set_sfx_volume

Set sfx volume in the audio store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-audio.tsx::setSfxVolume`

Parameters:
- `v` (number): v (number)
### audio_set_radio_volume

Set radio volume in the audio store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-audio.tsx::setRadioVolume`

Parameters:
- `v` (number): v (number)
### audio_set_radio_playing

Set radio playing in the audio store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-audio.tsx::setRadioPlaying`

Parameters:
- `v` (boolean): v (boolean)
### audio_toggle_radio_playing

Toggle radio playing in the audio store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-audio.tsx::toggleRadioPlaying`

### audio_toggle_mute

Toggle mute in the audio store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-audio.tsx::toggleMute`

### audio_set_autoplay

Set autoplay in the audio store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-audio.tsx::setAutoplay`

Parameters:
- `v` (boolean): v (boolean)
### commandregistry_register

Register in the commandregistry store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-command-registry.ts::register`

Parameters:
- `actions` (array): actions (CommandAction[])
### editor_set_phase

Set phase in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setPhase`

Parameters:
- `phase` (object): phase (Phase)
### editor_set_mode

Set mode in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setMode`

Parameters:
- `mode` (object): mode (Mode)
### editor_set_tool

Set tool in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setTool`

Parameters:
- `tool` (object): tool (Tool | null)
### editor_set_structure_layer

Set structure layer in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setStructureLayer`

Parameters:
- `layer` (object): layer (StructureLayer)
### editor_set_catalog_category

Set catalog category in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setCatalogCategory`

Parameters:
- `category` (object): category (CatalogCategory | null)
### editor_set_selected_item

Set selected item in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setSelectedItem`

Parameters:
- `item` (object): item (AssetInput)
### editor_set_selected_reference_id

Set selected reference id in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setSelectedReferenceId`

Parameters:
- `id` (string): id (string | null)
### editor_set_spaces

Set spaces in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setSpaces`

Parameters:
- `spaces` (object): spaces (Record<string, Space>)
### editor_set_editing_hole

Set editing hole in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setEditingHole`

Parameters:
- `hole` (object): hole ({ nodeId: string; holeIndex: number } | null)
### editor_set_preview_mode

Set preview mode in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setPreviewMode`

Parameters:
- `preview` (boolean): preview (boolean)
### editor_set_floorplan_open

Set floorplan open in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setFloorplanOpen`

Parameters:
- `open` (boolean): open (boolean)
### editor_toggle_floorplan_open

Toggle floorplan open in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::toggleFloorplanOpen`

### editor_set_floorplan_hovered

Set floorplan hovered in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setFloorplanHovered`

Parameters:
- `hovered` (boolean): hovered (boolean)
### editor_set_allow_underground_camera

Set allow underground camera in the editor store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-editor.tsx::setAllowUndergroundCamera`

Parameters:
- `enabled` (boolean): enabled (boolean)
### paletteviewregistry_register

Register in the paletteviewregistry store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-palette-view-registry.ts::register`

Parameters:
- `view` (object): view (PaletteView)
### uploadstore_start_upload

Start upload in the uploadstore store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-upload.ts::startUpload`

Parameters:
- `levelId` (string): levelId (string)
- `assetType` (string): assetType ('scan' | 'guide')
- `fileName` (string): fileName (string)
### uploadstore_set_progress

Set progress in the uploadstore store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-upload.ts::setProgress`

Parameters:
- `levelId` (string): levelId (string)
- `progress` (number): progress (number)
### uploadstore_set_status

Set status in the uploadstore store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-upload.ts::setStatus`

Parameters:
- `levelId` (string): levelId (string)
- `status` (object): status (UploadStatus)
### uploadstore_set_error

Set error in the uploadstore store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-upload.ts::setError`

Parameters:
- `levelId` (string): levelId (string)
- `error` (string): error (string)
### uploadstore_set_result

Set result in the uploadstore store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-upload.ts::setResult`

Parameters:
- `levelId` (string): levelId (string)
- `url` (string): url (string)
### uploadstore_clear_upload

Clear upload in the uploadstore store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/editor/src/store/use-upload.ts::clearUpload`

Parameters:
- `levelId` (string): levelId (string)
### itemlightpool_register

Register in the itemlightpool store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-item-light-pool.ts::register`

Parameters:
- `key` (string): key (string)
- `nodeId` (string): nodeId (AnyNodeId)
- `effect` (object): effect (LightEffect)
- `interactive` (object): interactive (Interactive)
### itemlightpool_unregister

Unregister in the itemlightpool store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-item-light-pool.ts::unregister`

Parameters:
- `key` (string): key (string)
### viewer_set_hovered_id

Set hovered id in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setHoveredId`

Parameters:
- `id` (string): id (AnyNode['id'] | ZoneNode['id'] | null)
### viewer_set_camera_mode

Set camera mode in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setCameraMode`

Parameters:
- `mode` (string): mode ('perspective' | 'orthographic')
### viewer_set_theme

Set theme in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setTheme`

Parameters:
- `theme` (string): theme ('light' | 'dark')
### viewer_set_unit

Set unit in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setUnit`

Parameters:
- `unit` (string): unit ('metric' | 'imperial')
### viewer_set_level_mode

Set level mode in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setLevelMode`

Parameters:
- `mode` (string): mode ('stacked' | 'exploded' | 'solo' | 'manual')
### viewer_set_wall_mode

Set wall mode in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setWallMode`

Parameters:
- `mode` (string): mode ('up' | 'cutaway' | 'down')
### viewer_set_show_scans

Set show scans in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setShowScans`

Parameters:
- `show` (boolean): show (boolean)
### viewer_set_show_guides

Set show guides in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setShowGuides`

Parameters:
- `show` (boolean): show (boolean)
### viewer_set_show_grid

Set show grid in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setShowGrid`

Parameters:
- `show` (boolean): show (boolean)
### viewer_set_project_id

Set project id in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setProjectId`

Parameters:
- `id` (string): id (string | null)
### viewer_set_selection

Set selection in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setSelection`

Parameters:
- `updates` (object): updates (Partial<SelectionPath>)
### viewer_reset_selection

Reset selection in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::resetSelection`

### viewer_export_scene

Export scene in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::exportScene`

### viewer_set_debug_colors

Set debug colors in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setDebugColors`

Parameters:
- `enabled` (boolean): enabled (boolean)
### viewer_set_camera_dragging

Set camera dragging in the viewer store

Implementation status: `proxy`
Notes: Forwards action to the browser's Zustand store via the generated WebSocket bridge.
Source hint: `Source: packages/viewer/src/store/use-viewer.ts::setCameraDragging`

Parameters:
- `dragging` (boolean): dragging (boolean)

## Available Resources

- `app://editor/status` — Current status and version of editor
- `app://editor/commands` — Available commands and tools in editor
- `docs://editor/tool-index` — Complete index of all editor tools with parameters and usage
- `docs://editor/zustand_action` — Documentation for editor zustand_action capabilities

## Available Prompts

- `use_editor` — Guide for using editor tools effectively
- `debug_editor` — Diagnose issues with editor operations

## Usage

This server runs over stdio. Add it to your MCP client config:

```json
{
  "mcpServers": {
    "editor": {
      "command": "mcp-editor"
    }
  }
}
```
