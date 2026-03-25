# mcp-pascal-editor

MCP server for [Pascal Editor](https://github.com/pascalorg/editor?tab=readme-ov-file) — lets Claude Code control the editor's Zustand stores directly via a WebSocket bridge.

72 tools covering the full store surface: scene, viewer, editor, command palette, audio, uploads, and more.

> Generated with [mcp-anything](https://github.com/Type-MCP/mcp-anything) — a tool that auto-generates MCP servers from any application's source code.

---

## How it works

```
Claude Code  →  mcp-pascal-editor (Python, stdio)  →  WebSocket  →  McpBridge (React)  →  Zustand stores
```

The Python MCP server starts a local WebSocket server on port `9001`. A thin React component (`McpBridge`) mounted in your app connects to it and relays store actions in real time.

---

## Setup

### 1. Install the MCP server

```bash
pip install mcp-pascal-editor
```

Or from source:

```bash
git clone https://github.com/Type-MCP/mcp-pascal-editor.git
cd mcp-pascal-editor
pip install -e .
```

### 2. Add the bridge component to your app

Copy `bridge/McpBridge.tsx` into your Pascal Editor app (e.g. `app/McpBridge.tsx`), then mount it in your **root layout** — `app/layout.tsx`:

```tsx
// app/layout.tsx
import { McpBridge } from './McpBridge'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body>
        {children}
        <McpBridge />   {/* renders nothing, connects to ws://localhost:9001 */}
      </body>
    </html>
  )
}
```

The component renders nothing visible. It opens a WebSocket connection to `ws://localhost:9001` and auto-reconnects every 3 seconds if the connection drops.

> **Note:** `McpBridge` imports store hooks from `@pascal-app/core`, `@pascal-app/editor`, and `@pascal-app/viewer`. These packages are already available in a Pascal Editor workspace — no extra installation needed.

### 3. Register the server with Claude Code

Add to your project's `.mcp.json` (or `~/.claude/claude_desktop_config.json` for global use):

```json
{
  "mcpServers": {
    "pascal-editor": {
      "command": "mcp-editor",
      "args": []
    }
  }
}
```

Or use the Claude Code CLI:

```bash
claude mcp add pascal-editor mcp-editor
```

### 4. Open your app and start using it

1. Start your Pascal Editor dev server (e.g. `pnpm dev` on port `3002`)
2. Open the app in the browser — McpBridge will connect automatically
3. Open Claude Code — the `pascal-editor` MCP server is now live

You should see `[McpBridge] Connected to MCP server at ws://localhost:9001` in the browser console.

---

## Usage example

Once connected, Claude can directly manipulate the scene:

```
Create a small apartment with a pool next to it
```

Claude will call tools like `scene_set_scene`, `scene_create_node`, `viewer_set_camera_mode`, etc. to build and navigate the scene without any manual interaction.

---

## Troubleshooting

**"No browser client connected"**

The Python server started but the browser hasn't connected yet (or a stale process is holding port 9001).

1. Check the browser console for `[McpBridge] Connected` — if it's missing, the WebSocket handshake failed
2. Run `lsof -i :9001` to check for stale Python processes and `kill <PID>` if needed
3. Run `/mcp` in Claude Code to reconnect the MCP server
4. Reload the browser tab — McpBridge will reconnect within 3 seconds

**Port conflict on startup**

If two `mcp-editor` processes run simultaneously (e.g. from a previous Claude Code session), the second one can't bind port 9001. Kill the old process and reconnect.

Set a custom port to avoid conflicts:

```json
{
  "mcpServers": {
    "pascal-editor": {
      "command": "mcp-editor",
      "args": [],
      "env": { "EDITOR_BRIDGE_PORT": "9002" }
    }
  }
}
```

Then set `NEXT_PUBLIC_MCP_BRIDGE_PORT=9002` in your app's `.env.local`.

---

## License

Apache 2.0
