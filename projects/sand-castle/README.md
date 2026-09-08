# 沙之城堡 | sand-castle

> 元胞自动机沙子模拟 | 落沙物理 | 障碍物绘制 | 纯Canvas零依赖

## Overview

沙之城堡 is an interactive web application built with pure HTML5 Canvas. Zero dependencies, zero build tools - just open `index.html` in any modern browser and start creating.

## Features

- Pure HTML5 Canvas rendering, zero external dependencies
- Smooth 60fps animation with requestAnimationFrame
- Full mouse and keyboard interaction
- Real-time parameter control panel
- Responsive design, works on desktop and mobile
- High DPI / Retina display support
- One-click PNG export

## Usage

```bash
# Just open in browser
open index.html
# Or serve locally
python3 -m http.server 8000
# Visit http://localhost:8000
```

## Controls

| Input | Action |
|-------|--------|
| Mouse Click | Create / Interact |
| Mouse Drag | Continuous effect |
| Mouse Move | Influence field |
| `Space` | Clear canvas |
| `S` | Save as PNG |
| `H` | Toggle control panel |
| `1-5` | Switch modes |

## Technical Details

- **Rendering**: HTML5 Canvas 2D API
- **Animation**: requestAnimationFrame loop with delta-time
- **Physics**: Custom particle system with velocity Verlet integration
- **Audio**: Web Audio API (OscillatorNode + BiquadFilter)
- **Input**: Mouse, touch, keyboard event handling
- **Export**: Canvas toDataURL for PNG download

## Design Philosophy

Every pixel is computed in real-time. No images, no external assets, no frameworks. The entire experience is self-contained in a single HTML file under 50KB.

## License

MIT
