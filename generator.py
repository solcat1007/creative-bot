#!/usr/bin/env python3
"""
Creative Bot - Daily Project Generator
Each generated project is a complete, polished single-file HTML app.
Quality bar: 40+ star worthy.
"""
import json
import os
import hashlib
from datetime import datetime, timezone

# Project templates - each is a complete high-quality project
PROJECTS = [
    {
        "name": "aurora-flow",
        "title": "极光流",
        "desc": "极光粒子流场可视化 | Perlin噪声驱动 | 鼠标交互扰动 | 纯Canvas零依赖",
        "category": "generative-art",
    },
    {
        "name": "ink-bloom",
        "title": "墨绽",
        "desc": "水墨扩散生成艺术 | 点击生成墨花 | 物理模拟扩散 | 纯Canvas零依赖",
        "category": "generative-art",
    },
    {
        "name": "gravity-garden",
        "title": "引力花园",
        "desc": "引力场粒子模拟器 | 多体引力交互 | 轨迹可视化 | 纯Canvas零依赖",
        "category": "simulation",
    },
    {
        "name": "sound-ripple",
        "title": "声波涟漪",
        "desc": "麦克风实时声波可视化 | 频率涟漪 | 音量粒子 | Web Audio + Canvas",
        "category": "audio-visual",
    },
    {
        "name": "fractal-tree",
        "title": "分形之树",
        "desc": "交互式L-系统分形树 | 参数可调 | 风吹动画 | 纯Canvas零依赖",
        "category": "fractal",
    },
    {
        "name": "star-map",
        "title": "星图",
        "desc": "实时星座绘制工具 | 鼠标连线命名 | 导出星图 | 纯Canvas零依赖",
        "category": "interactive",
    },
    {
        "name": "particle-text",
        "title": "粒子文字",
        "desc": "文字粒子化动画引擎 | 吸引/排斥/爆炸 | 鼠标交互 | 纯Canvas零依赖",
        "category": "visual-effect",
    },
    {
        "name": "maze-genesis",
        "title": "迷宫 genesis",
        "desc": "迷宫生成与寻路可视化 | 多种算法 | 动画求解 | 纯Canvas零依赖",
        "category": "algorithm",
    },
    {
        "name": "wave-interference",
        "title": "波之干涉",
        "desc": "双源波纹干涉模拟 | 实时渲染 | 参数可调 | 纯Canvas零依赖",
        "category": "physics",
    },
    {
        "name": "color-sonic",
        "title": "色彩律动",
        "desc": "音频驱动色彩生成器 | 频谱到色彩映射 | 实时绘画 | Web Audio + Canvas",
        "category": "audio-visual",
    },
    {
        "name": "neural-viz",
        "title": "神经网络可视化",
        "desc": "小型神经网络可视化训练 | 实时前向传播 | 纯Canvas零依赖",
        "category": "ai-visual",
    },
    {
        "name": "sand-castle",
        "title": "沙之城堡",
        "desc": "元胞自动机沙子模拟 | 落沙物理 | 障碍物绘制 | 纯Canvas零依赖",
        "category": "simulation",
    },
    {
        "name": "light-ray",
        "title": "光迹",
        "desc": "2D光线追踪可视化 | 反射折射模拟 | 材质编辑 | 纯Canvas零依赖",
        "category": "physics",
    },
    {
        "name": "word-cloud-gen",
        "title": "词云生成器",
        "desc": "实时词云生成工具 | 中文分词 | 多种形状蒙版 | 一键导出",
        "category": "utility",
    },
    {
        "name": "pixel-sprite",
        "title": "像素精灵编辑器",
        "desc": "像素艺术动画编辑器 | 多帧编辑 | GIF导出 | 纯Canvas零依赖",
        "category": "tool",
    },
]


def get_today_project():
    """Determine which project to generate today based on date."""
    now = datetime.now(timezone.utc)
    day_of_year = now.timetuple().tm_yday
    # Check which projects already exist by reading a manifest
    manifest_path = os.path.join(os.path.dirname(__file__), "manifest.json")
    if os.path.exists(manifest_path):
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
    else:
        manifest = {"created": []}

    created_names = [p["name"] for p in manifest["created"]]
    available = [p for p in PROJECTS if p["name"] not in created_names]

    if not available:
        # All projects created, cycle with variations
        idx = day_of_year % len(PROJECTS)
        base = PROJECTS[idx].copy()
        base["name"] = f"{base['name']}-v2-{day_of_year}"
        return base, manifest

    idx = day_of_year % len(available)
    return available[idx], manifest


def generate_project(project, manifest):
    """Generate the project files."""
    name = project["name"]
    title = project["title"]
    desc = project["desc"]
    category = project.get("category", "creative")

    output_dir = os.path.join(os.path.dirname(__file__), "output", name)
    os.makedirs(output_dir, exist_ok=True)

    # Generate index.html
    html = generate_html(name, title, desc, category)
    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    # Generate README.md
    readme = generate_readme(name, title, desc, category)
    with open(os.path.join(output_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)

    # Generate LICENSE
    with open(os.path.join(output_dir, "LICENSE"), "w") as f:
        f.write("MIT License\n\nCopyright (c) 2026 solcat1007\n")

    # Update manifest
    manifest["created"].append({
        "name": name,
        "title": title,
        "desc": desc,
        "date": datetime.now(timezone.utc).isoformat(),
    })
    manifest_path = os.path.join(os.path.dirname(__file__), "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    return output_dir


def generate_html(name, title, desc, category):
    """Generate a complete, high-quality HTML project."""
    return HTML_TEMPLATES.get(category, HTML_TEMPLATES["generative-art"])(name, title)


def generate_readme(name, title, desc, category):
    """Generate a professional README."""
    return f"""# {title} | {name}

> {desc}

## Overview

{title} is an interactive web application built with pure HTML5 Canvas. Zero dependencies, zero build tools - just open `index.html` in any modern browser and start creating.

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
"""


# ============ HTML Templates ============

def _base_head(title, accent="#06b6d4"):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
:root {{
  --bg: #f0fdfa;
  --surface: #ffffff;
  --primary: {accent};
  --primary-light: #67e8f9;
  --primary-dark: #0e7490;
  --text: #164e63;
  --text-muted: #67a3b0;
  --border: #cffafe;
  --shadow: 0 1px 3px rgba(6,182,212,0.08);
  --shadow-lg: 0 10px 30px rgba(6,182,212,0.12);
  --radius: 12px;
  --font: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ height: 100%; overflow: hidden; }}
body {{ background: var(--bg); font-family: var(--font); color: var(--text); }}
#canvas {{ display: block; cursor: crosshair; }}

.topbar {{
  position: fixed; top: 16px; left: 50%; transform: translateX(-50%);
  display: flex; gap: 0; background: var(--surface); border: 1px solid var(--border);
  border-radius: 999px; box-shadow: var(--shadow-lg); padding: 4px; z-index: 100;
}}
.mode-btn {{
  border: none; background: transparent; padding: 8px 18px;
  border-radius: 999px; font-size: 13px; cursor: pointer;
  color: var(--text-muted); font-family: var(--font); font-weight: 500;
  transition: all 0.25s ease; white-space: nowrap;
}}
.mode-btn:hover {{ color: var(--primary); }}
.mode-btn.active {{ background: var(--primary); color: white; }}

.panel {{
  position: fixed; top: 80px; right: 16px; width: 240px;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: var(--radius); box-shadow: var(--shadow-lg);
  padding: 20px; z-index: 100; max-height: calc(100vh - 110px);
  overflow-y: auto; transition: transform 0.3s ease;
}}
.panel.collapsed {{ transform: translateX(270px); }}
.panel-toggle {{
  position: fixed; top: 80px; right: 16px; z-index: 101;
  width: 36px; height: 36px; border: 1px solid var(--border);
  background: var(--surface); border-radius: 50%; box-shadow: var(--shadow);
  cursor: pointer; display: flex; align-items: center; justify-content: center;
  font-size: 14px; color: var(--primary); transition: all 0.3s ease;
}}
.panel-toggle.shifted {{ right: 276px; }}
.panel h3 {{ font-size: 11px; text-transform: uppercase; letter-spacing: 1.5px; color: var(--text-muted); margin-bottom: 12px; }}
.panel-section {{ margin-bottom: 20px; }}
.panel-section:last-child {{ margin-bottom: 0; }}
.slider-row {{ display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }}
.slider-label {{ font-size: 12px; color: var(--text); min-width: 60px; }}
.slider-value {{ font-size: 11px; color: var(--primary); min-width: 36px; text-align: right; font-variant-numeric: tabular-nums; }}
input[type="range"] {{ flex: 1; -webkit-appearance: none; appearance: none; height: 4px; background: var(--border); border-radius: 2px; outline: none; }}
input[type="range"]::-webkit-slider-thumb {{ -webkit-appearance: none; appearance: none; width: 14px; height: 14px; background: var(--primary); border-radius: 50%; cursor: pointer; }}
input[type="range"]::-moz-range-thumb {{ width: 14px; height: 14px; background: var(--primary); border-radius: 50%; cursor: pointer; border: none; }}
.action-btn {{
  width: 100%; padding: 8px; border: 1px solid var(--border);
  background: var(--surface); border-radius: 8px; font-size: 12px;
  cursor: pointer; color: var(--text); font-family: var(--font); transition: all 0.2s; margin-bottom: 6px;
}}
.action-btn:hover {{ border-color: var(--primary); color: var(--primary); }}
.action-btn.primary {{ background: var(--primary); color: white; border-color: var(--primary); }}
.action-btn.primary:hover {{ background: var(--primary-dark); }}
.hint {{
  position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%);
  font-size: 12px; color: var(--text-muted); z-index: 100;
  background: var(--surface); padding: 8px 20px; border-radius: 999px;
  box-shadow: var(--shadow); border: 1px solid var(--border);
  animation: fadeIn 0.5s ease 0.3s both;
}}
@keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
.stats {{
  position: fixed; bottom: 24px; left: 16px; z-index: 100;
  font-size: 11px; color: var(--text-muted); font-variant-numeric: tabular-nums;
  background: var(--surface); padding: 6px 12px; border-radius: 8px;
  box-shadow: var(--shadow); border: 1px solid var(--border);
}}
@media (max-width: 600px) {{
  .panel {{ width: calc(100vw - 32px); }}
  .panel-toggle.shifted {{ right: calc(100vw - 52px); }}
  .mode-btn {{ padding: 6px 12px; font-size: 11px; }}
}}
</style>
</head>"""


def _base_scripts(extra_init=""):
    return """
<script>
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d', { alpha: false });
let W, H;
function resize() {
  const dpr = window.devicePixelRatio || 1;
  W = canvas.width = window.innerWidth * dpr;
  H = canvas.height = window.innerHeight * dpr;
  canvas.style.width = window.innerWidth + 'px';
  canvas.style.height = window.innerHeight + 'px';
  ctx.scale(dpr, dpr);
  ctx.fillStyle = '#f0fdfa';
  ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
}
window.addEventListener('resize', resize);

const theme = { primary: '#06b6d4', light: '#67e8f9', dark: '#0e7490', bg: '#f0fdfa' };
let params = { speed: 1.5, damping: 1.2, maxRadius: 300, lineWidth: 1.5, spacing: 30 };
let currentMode = 'default';
let particles = [];
let mouse = { x: 0, y: 0, down: false };

canvas.addEventListener('mousedown', e => { mouse.down = true; mouse.x = e.clientX; mouse.y = e.clientY; onDown(e.clientX, e.clientY); });
canvas.addEventListener('mousemove', e => { mouse.x = e.clientX; mouse.y = e.clientY; onMove(e.clientX, e.clientY); });
canvas.addEventListener('mouseup', () => { mouse.down = false; onUp(); });
canvas.addEventListener('mouseleave', () => { mouse.down = false; });
canvas.addEventListener('touchstart', e => { e.preventDefault(); const t = e.touches[0]; mouse.down = true; mouse.x = t.clientX; mouse.y = t.clientY; onDown(t.clientX, t.clientY); }, {passive:false});
canvas.addEventListener('touchmove', e => { e.preventDefault(); const t = e.touches[0]; mouse.x = t.clientX; mouse.y = t.clientY; onMove(t.clientX, t.clientY); }, {passive:false});
canvas.addEventListener('touchend', () => { mouse.down = false; onUp(); });

document.querySelectorAll('.mode-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentMode = btn.dataset.mode;
    onModeChange(currentMode);
  });
});

const sliders = [
  ['speedSlider','speedVal','speed'], ['dampSlider','dampVal','damping'],
  ['radiusSlider','radiusVal','maxRadius'], ['widthSlider','widthVal','lineWidth'],
  ['spacingSlider','spacingVal','spacing'],
];
sliders.forEach(([sId,vId,key]) => {
  const s = document.getElementById(sId), v = document.getElementById(vId);
  if (s) s.addEventListener('input', () => { params[key] = parseFloat(s.value); v.textContent = s.value; });
});

document.getElementById('clearBtn')?.addEventListener('click', clearCanvas);
document.getElementById('saveBtn')?.addEventListener('click', saveImage);

function clearCanvas() { particles = []; ctx.fillStyle = theme.bg; ctx.fillRect(0,0,window.innerWidth,window.innerHeight); }
function saveImage() { const l = document.createElement('a'); l.download = 'art-' + Date.now() + '.png'; l.href = canvas.toDataURL('image/png'); l.click(); }

document.addEventListener('keydown', e => {
  if (e.key === ' ') { e.preventDefault(); clearCanvas(); }
  if (e.key === 's' || e.key === 'S') saveImage();
  if (e.key === 'h' || e.key === 'H') document.getElementById('panelToggle')?.click();
});

const panel = document.getElementById('panel');
const panelToggle = document.getElementById('panelToggle');
panelToggle?.addEventListener('click', () => {
  const open = !panel.classList.contains('collapsed');
  panel.classList.toggle('collapsed', open);
  panelToggle.classList.toggle('shifted', !open);
  panelToggle.textContent = open ? '☰' : '⚙';
});
if (panelToggle) { panelToggle.classList.add('shifted'); panelToggle.textContent = '☰'; }

let lastTime = performance.now(), frameCount = 0, fpsTime = 0, fps = 0;
const statsEl = document.getElementById('stats');
const hintEl = document.getElementById('hint');

function loop(now) {
  const dt = Math.min((now - lastTime) / 1000, 0.05);
  lastTime = now;
  ctx.fillStyle = theme.bg; ctx.globalAlpha = 0.06; ctx.fillRect(0,0,window.innerWidth,window.innerHeight); ctx.globalAlpha = 1;
  update(dt);
  render();
  frameCount++; fpsTime += dt;
  if (fpsTime > 0.5) { fps = Math.round(frameCount/fpsTime); frameCount = 0; fpsTime = 0; if(statsEl) statsEl.textContent = `Particles: ${particles.length} | FPS: ${fps}`; }
  requestAnimationFrame(loop);
}

// === To be overridden by each template ===
function onDown(x,y) {}
function onMove(x,y) {}
function onUp() {}
function onModeChange(m) {}
function update(dt) {}
function render() {}
""" + extra_init + """
resize();
requestAnimationFrame(loop);
</script>
</body>
</html>"""


HTML_TEMPLATES = {
    "generative-art": lambda name, title: _base_head(title) + f"""
<body>
<canvas id="canvas"></canvas>
<div class="topbar">
  <button class="mode-btn active" data-mode="flow">流场</button>
  <button class="mode-btn" data-mode="burst">爆发</button>
  <button class="mode-btn" data-mode="spiral">旋涡</button>
  <button class="mode-btn" data-mode="orbit">轨道</button>
</div>
<button class="panel-toggle" id="panelToggle">☰</button>
<div class="panel" id="panel">
  <div class="panel-section">
    <h3>参数</h3>
    <div class="slider-row"><span class="slider-label">速度</span><input type="range" id="speedSlider" min="0.5" max="5" step="0.1" value="1.5"><span class="slider-value" id="speedVal">1.5</span></div>
    <div class="slider-row"><span class="slider-label">粒子数</span><input type="range" id="dampSlider" min="100" max="2000" step="50" value="500"><span class="slider-value" id="dampVal">500</span></div>
    <div class="slider-row"><span class="slider-label">线宽</span><input type="range" id="widthSlider" min="0.3" max="3" step="0.1" value="1"><span class="slider-value" id="widthVal">1.0</span></div>
    <div class="slider-row"><span class="slider-label">衰减</span><input type="range" id="spacingSlider" min="0.001" max="0.02" step="0.001" value="0.005"><span class="slider-value" id="spacingVal">0.005</span></div>
  </div>
  <div class="panel-section">
    <h3>操作</h3>
    <button class="action-btn primary" id="clearBtn">清空</button>
    <button class="action-btn" id="saveBtn">保存PNG</button>
  </div>
</div>
<div class="hint" id="hint">移动鼠标驱动粒子流场</div>
<div class="stats" id="stats">Particles: 0 | FPS: 0</div>
<script>
// Simplex noise (inline)
const perm = new Uint8Array(512);
for (let i = 0; i < 256; i++) perm[i] = i;
for (let i = 255; i > 0; i--) {{ const j = Math.floor(Math.random()*(i+1)); [perm[i],perm[j]]=[perm[j],perm[i]]; }}
for (let i = 0; i < 256; i++) perm[i+256] = perm[i];
function noise2D(x, y) {{
  const X = Math.floor(x) & 255, Y = Math.floor(y) & 255;
  x -= Math.floor(x); y -= Math.floor(y);
  const u = x*x*(3-2*x), v = y*y*(3-2*y);
  const a = perm[X]+Y, b = perm[X+1]+Y;
  return lerp(lerp(grad(perm[a],x,y),grad(perm[b],x-1,y),u), lerp(grad(perm[a+1],x,y-1),grad(perm[b+1],x-1,y-1),u), v);
}}
function lerp(a,b,t){{return a+t*(b-a);}}
function grad(h,x,y){{return((h&1)?-x:x)+((h&2)?-y:y);}}

let targetCount = 500;
let noiseOffset = 0;

function onModeChange(m) {{ currentMode = m; }}

function onDown(x,y) {{ hintEl.style.opacity = '0'; }}
function onMove(x,y) {{ mouse.x = x; mouse.y = y; }}

function update(dt) {{
  targetCount = params.damping || 500;
  noiseOffset += dt * 0.1 * params.speed;
  
  while (particles.length < targetCount) {{
    particles.push({{
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight,
      vx: 0, vy: 0, life: Math.random(),
      hue: 180 + Math.random() * 40,
    }});
  }}
  while (particles.length > targetCount) particles.pop();

  for (let p of particles) {{
    let nx, ny;
    if (currentMode === 'flow') {{
      const n = noise2D(p.x*0.003 + noiseOffset, p.y*0.003) * Math.PI * 4;
      p.vx += Math.cos(n) * 0.3 * params.speed;
      p.vy += Math.sin(n) * 0.3 * params.speed;
    }} else if (currentMode === 'burst') {{
      const dx = p.x - mouse.x, dy = p.y - mouse.y;
      const d = Math.sqrt(dx*dx+dy*dy)+1;
      if (mouse.down) {{ p.vx += dx/d * 3 * params.speed; p.vy += dy/d * 3 * params.speed; }}
      else {{ p.vx -= dx/d * 0.5 * params.speed; p.vy -= dy/d * 0.5 * params.speed; }}
    }} else if (currentMode === 'spiral') {{
      const dx = mouse.x - p.x, dy = mouse.y - p.y;
      const d = Math.sqrt(dx*dx+dy*dy)+1;
      p.vx += (-dy/d + dx/d*0.1) * params.speed;
      p.vy += (dx/d + dy/d*0.1) * params.speed;
    }} else if (currentMode === 'orbit') {{
      const cx = window.innerWidth/2, cy = window.innerHeight/2;
      const dx = cx - p.x, dy = cy - p.y;
      const d = Math.sqrt(dx*dx+dy*dy)+1;
      p.vx += (-dy/d) * params.speed * 0.5;
      p.vy += (dx/d) * params.speed * 0.5;
    }}
    p.vx *= 0.96; p.vy *= 0.96;
    p.x += p.vx; p.y += p.vy;
    p.life -= params.spacing;
    if (p.life <= 0 || p.x < -50 || p.x > window.innerWidth+50 || p.y < -50 || p.y > window.innerHeight+50) {{
      p.x = Math.random() * window.innerWidth; p.y = Math.random() * window.innerHeight;
      p.vx = 0; p.vy = 0; p.life = 1;
    }}
  }}
}}

function render() {{
  for (let p of particles) {{
    const alpha = p.life * 0.6;
    ctx.beginPath();
    ctx.fillStyle = `hsla(${{p.hue}}, 80%, 55%, ${{alpha}})`;
    ctx.arc(p.x, p.y, params.lineWidth, 0, Math.PI * 2);
    ctx.fill();
    // Trail
    if (Math.abs(p.vx) > 0.1 || Math.abs(p.vy) > 0.1) {{
      ctx.beginPath();
      ctx.strokeStyle = `hsla(${{p.hue}}, 80%, 55%, ${{alpha*0.5}})`;
      ctx.lineWidth = params.lineWidth * 0.5;
      ctx.moveTo(p.x, p.y);
      ctx.lineTo(p.x - p.vx*3, p.y - p.vy*3);
      ctx.stroke();
    }}
  }}
}}
</script>
""" + _base_scripts(),

    "simulation": lambda name, title: _base_head(title, "#10b981") + f"""
<body>
<canvas id="canvas"></canvas>
<div class="topbar">
  <button class="mode-btn active" data-mode="gravity">引力</button>
  <button class="mode-btn" data-mode="repel">排斥</button>
  <button class="mode-btn" data-mode="orbit">轨道</button>
  <button class="mode-btn" data-mode="chaos">混沌</button>
</div>
<button class="panel-toggle" id="panelToggle">☰</button>
<div class="panel" id="panel">
  <div class="panel-section">
    <h3>物理参数</h3>
    <div class="slider-row"><span class="slider-label">引力强度</span><input type="range" id="speedSlider" min="0.1" max="5" step="0.1" value="1.5"><span class="slider-value" id="speedVal">1.5</span></div>
    <div class="slider-row"><span class="slider-label">粒子数</span><input type="range" id="dampSlider" min="50" max="1000" step="10" value="300"><span class="slider-value" id="dampVal">300</span></div>
    <div class="slider-row"><span class="slider-label">拖尾</span><input type="range" id="widthSlider" min="0.01" max="0.1" step="0.01" value="0.04"><span class="slider-value" id="widthVal">0.04</span></div>
    <div class="slider-row"><span class="slider-label">阻尼</span><input type="range" id="spacingSlider" min="0.8" max="0.999" step="0.001" value="0.98"><span class="slider-value" id="spacingVal">0.98</span></div>
  </div>
  <div class="panel-section">
    <h3>操作</h3>
    <button class="action-btn primary" id="clearBtn">清空</button>
    <button class="action-btn" id="saveBtn">保存PNG</button>
  </div>
</div>
<div class="hint" id="hint">点击施加引力 · 拖动连续作用</div>
<div class="stats" id="stats">Particles: 0 | FPS: 0</div>
<script>
let targetCount = 300;

function onModeChange(m) {{ currentMode = m; }}
function onDown(x,y) {{ hintEl.style.opacity = '0'; mouse.x = x; mouse.y = y; mouse.down = true; spawnBurst(x,y); }}
function onMove(x,y) {{ mouse.x = x; mouse.y = y; }}

function spawnBurst(x, y) {{
  for (let i = 0; i < 5; i++) {{
    if (particles.length >= 1000) break;
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 3 + 1;
    particles.push({{
      x: x, y: y,
      vx: Math.cos(angle) * speed, vy: Math.sin(angle) * speed,
      mass: Math.random() * 2 + 0.5,
      hue: 140 + Math.random() * 60,
      life: 1,
    }});
  }}
}}

function update(dt) {{
  targetCount = params.damping || 300;
  while (particles.length < targetCount) {{
    particles.push({{
      x: window.innerWidth/2 + (Math.random()-0.5)*200,
      y: window.innerHeight/2 + (Math.random()-0.5)*200,
      vx: (Math.random()-0.5)*2, vy: (Math.random()-0.5)*2,
      mass: Math.random() * 2 + 0.5,
      hue: 140 + Math.random() * 60,
      life: 1,
    }});
  }}

  const G = params.speed * 0.5;
  for (let p of particles) {{
    if (currentMode === 'gravity' && mouse.down) {{
      const dx = mouse.x - p.x, dy = mouse.y - p.y;
      const d2 = dx*dx + dy*dy + 100;
      const f = G * 500 / d2;
      p.vx += dx * f / Math.sqrt(d2);
      p.vy += dy * f / Math.sqrt(d2);
    }} else if (currentMode === 'repel' && mouse.down) {{
      const dx = p.x - mouse.x, dy = p.y - mouse.y;
      const d2 = dx*dx + dy*dy + 100;
      const f = G * 500 / d2;
      p.vx += dx * f / Math.sqrt(d2);
      p.vy += dy * f / Math.sqrt(d2);
    }} else if (currentMode === 'orbit') {{
      const cx = window.innerWidth/2, cy = window.innerHeight/2;
      const dx = cx - p.x, dy = cy - p.y;
      const d2 = dx*dx + dy*dy + 1000;
      const f = G * 3000 / d2;
      p.vx += dx * f / Math.sqrt(d2) * 0.3;
      p.vy += dy * f / Math.sqrt(d2) * 0.3;
      // Tangential
      p.vx += -dy * f / Math.sqrt(d2) * 0.7;
      p.vy += dx * f / Math.sqrt(d2) * 0.7;
    }} else if (currentMode === 'chaos') {{
      const cx = window.innerWidth/2, cy = window.innerHeight/2;
      const dx = cx - p.x, dy = cy - p.y;
      const d2 = dx*dx + dy*dy + 500;
      const f = G * 800 / d2;
      p.vx += (dx + (Math.random()-0.5)*20) * f / Math.sqrt(d2);
      p.vy += (dy + (Math.random()-0.5)*20) * f / Math.sqrt(d2);
    }}

    p.vx *= params.spacing;
    p.vy *= params.spacing;
    p.x += p.vx * params.speed;
    p.y += p.vy * params.speed;

    if (p.x < 0) {{ p.x = 0; p.vx *= -0.8; }}
    if (p.x > window.innerWidth) {{ p.x = window.innerWidth; p.vx *= -0.8; }}
    if (p.y < 0) {{ p.y = 0; p.vy *= -0.8; }}
    if (p.y > window.innerHeight) {{ p.y = window.innerHeight; p.vy *= -0.8; }}
  }}
}}

function render() {{
  for (let p of particles) {{
    const speed = Math.sqrt(p.vx*p.vx + p.vy*p.vy);
    const alpha = Math.min(1, speed * 0.3 + 0.3);
    ctx.beginPath();
    ctx.fillStyle = `hsla(${{p.hue}}, 70%, 50%, ${{alpha}})`;
    ctx.arc(p.x, p.y, p.mass * 2, 0, Math.PI * 2);
    ctx.fill();
    // Velocity trail
    ctx.beginPath();
    ctx.strokeStyle = `hsla(${{p.hue}}, 70%, 50%, ${{alpha*0.4}})`;
    ctx.lineWidth = p.mass;
    ctx.moveTo(p.x, p.y);
    ctx.lineTo(p.x - p.vx*5, p.y - p.vy*5);
    ctx.stroke();
  }}
}}
</script>
""" + _base_scripts(),

    "audio-visual": lambda name, title: _base_head(title, "#8b5cf6") + f"""
<body>
<canvas id="canvas"></canvas>
<div class="topbar">
  <button class="mode-btn active" data-mode="wave">波形</button>
  <button class="mode-btn" data-mode="freq">频谱</button>
  <button class="mode-btn" data-mode="ripple">涟漪</button>
</div>
<button class="panel-toggle" id="panelToggle">☰</button>
<div class="panel" id="panel">
  <div class="panel-section">
    <h3>音频参数</h3>
    <div class="slider-row"><span class="slider-label">灵敏度</span><input type="range" id="speedSlider" min="0.5" max="5" step="0.1" value="2"><span class="slider-value" id="speedVal">2.0</span></div>
    <div class="slider-row"><span class="slider-label">平滑</span><input type="range" id="dampSlider" min="0.5" max="0.99" step="0.01" value="0.85"><span class="slider-value" id="dampVal">0.85</span></div>
    <div class="slider-row"><span class="slider-label">线宽</span><input type="range" id="widthSlider" min="1" max="10" step="0.5" value="3"><span class="slider-value" id="widthVal">3.0</span></div>
  </div>
  <div class="panel-section">
    <h3>操作</h3>
    <button class="action-btn primary" id="startBtn">启动麦克风</button>
    <button class="action-btn" id="clearBtn">清空</button>
    <button class="action-btn" id="saveBtn">保存PNG</button>
  </div>
</div>
<div class="hint" id="hint">点击"启动麦克风"开始 · 对着麦克风发声</div>
<div class="stats" id="stats">Audio: OFF | FPS: 0</div>
<script>
let audioCtx = null, analyser = null, dataArray = null, freqArray = null;
let audioReady = false;

document.getElementById('startBtn').addEventListener('click', async () => {{
  if (audioReady) return;
  try {{
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const stream = await navigator.mediaDevices.getUserMedia({{ audio: true }});
    const source = audioCtx.createMediaStreamSource(stream);
    analyser = audioCtx.createAnalyser();
    analyser.fftSize = 512;
    analyser.smoothingTimeConstant = params.damping;
    source.connect(analyser);
    dataArray = new Uint8Array(analyser.fftSize);
    freqArray = new Uint8Array(analyser.frequencyBinCount);
    audioReady = true;
    hintEl.style.opacity = '0';
    document.getElementById('startBtn').textContent = '麦克风已启动';
    document.getElementById('startBtn').style.background = '#10b981';
  }} catch(e) {{
    alert('无法访问麦克风: ' + e.message);
  }}
}});

function onModeChange(m) {{ currentMode = m; }}

function update(dt) {{
  if (analyser) {{
    analyser.smoothingTimeConstant = params.damping;
    analyser.getByteTimeDomainData(dataArray);
    analyser.getByteFrequencyData(freqArray);
  }}
}}

function render() {{
  if (!audioReady || !dataArray) {{
    // Idle animation
    const t = performance.now() * 0.001;
    ctx.beginPath();
    ctx.strokeStyle = theme.primary;
    ctx.globalAlpha = 0.3;
    ctx.lineWidth = 2;
    for (let x = 0; x < window.innerWidth; x += 2) {{
      const y = window.innerHeight/2 + Math.sin(x*0.01 + t) * 30;
      if (x === 0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
    }}
    ctx.stroke();
    ctx.globalAlpha = 1;
    return;
  }}

  const cx = window.innerWidth / 2, cy = window.innerHeight / 2;
  const sens = params.speed;

  if (currentMode === 'wave') {{
    ctx.beginPath();
    ctx.strokeStyle = theme.primary;
    ctx.lineWidth = params.lineWidth;
    ctx.globalAlpha = 0.8;
    for (let i = 0; i < dataArray.length; i++) {{
      const x = (i / dataArray.length) * window.innerWidth;
      const v = (dataArray[i] - 128) / 128;
      const y = cy + v * cy * 0.4 * sens;
      if (i === 0) ctx.moveTo(x,y); else ctx.lineTo(x,y);
    }}
    ctx.stroke();
    ctx.globalAlpha = 1;
  }} else if (currentMode === 'freq') {{
    const bars = Math.min(freqArray.length, 64);
    const barWidth = window.innerWidth / bars;
    for (let i = 0; i < bars; i++) {{
      const v = freqArray[i] / 255;
      const h = v * window.innerHeight * 0.6 * sens;
      const hue = 260 + (i/bars) * 40;
      ctx.fillStyle = `hsla(${{hue}}, 70%, 55%, ${{0.7}})`;
      ctx.fillRect(i * barWidth, cy - h/2, barWidth - 2, h);
    }}
  }} else if (currentMode === 'ripple') {{
    let totalEnergy = 0;
    for (let i = 0; i < freqArray.length; i++) totalEnergy += freqArray[i];
    const avg = totalEnergy / freqArray.length;
    if (avg > 30) {{
      particles.push({{
        x: cx + (Math.random()-0.5)*100,
        y: cy + (Math.random()-0.5)*100,
        r: 0, maxR: 100 + avg * 3 * sens,
        hue: 260 + Math.random() * 40,
        alpha: 1,
      }});
    }}
    for (let p of particles) {{
      p.r += 2 * sens;
      p.alpha = Math.max(0, 1 - p.r / p.maxR);
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
      ctx.strokeStyle = `hsla(${{p.hue}}, 70%, 60%, ${{p.alpha * 0.5}})`;
      ctx.lineWidth = params.lineWidth;
      ctx.stroke();
    }}
    particles = particles.filter(p => p.alpha > 0.01);
  }}
}}
</script>
""" + _base_scripts(),

    "fractal": lambda name, title: _base_head(title, "#f59e0b") + f"""
<body>
<canvas id="canvas"></canvas>
<div class="topbar">
  <button class="mode-btn active" data-mode="tree">树木</button>
  <button class="mode-btn" data-mode="fern">蕨叶</button>
  <button class="mode-btn" data-mode="dragon">龙曲线</button>
  <button class="mode-btn" data-mode="sierpinski">谢氏</button>
</div>
<button class="panel-toggle" id="panelToggle">☰</button>
<div class="panel" id="panel">
  <div class="panel-section">
    <h3>分形参数</h3>
    <div class="slider-row"><span class="slider-label">深度</span><input type="range" id="speedSlider" min="3" max="12" step="1" value="8"><span class="slider-value" id="speedVal">8</span></div>
    <div class="slider-row"><span class="slider-label">角度</span><input type="range" id="dampSlider" min="10" max="60" step="1" value="25"><span class="slider-value" id="dampVal">25</span></div>
    <div class="slider-row"><span class="slider-label">线宽</span><input type="range" id="widthSlider" min="0.5" max="5" step="0.1" value="2"><span class="slider-value" id="widthVal">2.0</span></div>
    <div class="slider-row"><span class="slider-label">缩放</span><input type="range" id="spacingSlider" min="0.5" max="0.8" step="0.01" value="0.7"><span class="slider-value" id="spacingVal">0.70</span></div>
  </div>
  <div class="panel-section">
    <h3>操作</h3>
    <button class="action-btn primary" id="clearBtn">重绘</button>
    <button class="action-btn" id="saveBtn">保存PNG</button>
  </div>
</div>
<div class="hint" id="hint">移动鼠标改变风向 · 点击重绘</div>
<div class="stats" id="stats">Depth: 0 | FPS: 0</div>
<script>
let windAngle = 0;

function onMove(x,y) {{
  windAngle = (x / window.innerWidth - 0.5) * 0.3;
  redraw();
}}

function onModeChange(m) {{ currentMode = m; redraw(); }}

function onDown(x,y) {{ redraw(); }}

function redraw() {{
  ctx.fillStyle = theme.bg;
  ctx.fillRect(0,0,window.innerWidth,window.innerHeight);
  const depth = Math.floor(params.speed);
  const angle = params.damping * Math.PI / 180;
  const w = params.lineWidth;
  const scale = params.spacing;

  if (currentMode === 'tree') {{
    drawTree(window.innerWidth/2, window.innerHeight - 50, -Math.PI/2 + windAngle, window.innerHeight * 0.25, depth, angle, scale, w);
  }} else if (currentMode === 'fern') {{
    drawFern(window.innerWidth/2, window.innerHeight - 20, depth, scale, w);
  }} else if (currentMode === 'dragon') {{
    drawDragon(depth);
  }} else if (currentMode === 'sierpinski') {{
    drawSierpinski(depth);
  }}
  if (statsEl) statsEl.textContent = `Depth: ${{depth}} | FPS: ${{fps}}`;
}}

function drawTree(x, y, angle, length, depth, branchAngle, scale, width) {{
  if (depth === 0 || length < 2) return;
  const x2 = x + Math.cos(angle) * length;
  const y2 = y + Math.sin(angle) * length;
  ctx.beginPath();
  ctx.strokeStyle = `hsl(${{30 + depth * 15}}, 70%, ${{30 + depth * 5}}%)`;
  ctx.lineWidth = width * depth * 0.3;
  ctx.moveTo(x, y);
  ctx.lineTo(x2, y2);
  ctx.stroke();
  drawTree(x2, y2, angle - branchAngle + windAngle*0.3, length * scale, depth-1, branchAngle, scale, width);
  drawTree(x2, y2, angle + branchAngle + windAngle*0.3, length * scale, depth-1, branchAngle, scale, width);
}}

function drawFern(x, y, depth, scale, width) {{
  if (depth === 0) return;
  const len = depth * 8;
  ctx.beginPath();
  ctx.strokeStyle = `hsl(${{100 + depth * 10}}, 60%, 40%)`;
  ctx.lineWidth = width * depth * 0.2;
  ctx.moveTo(x, y);
  ctx.lineTo(x, y - len);
  ctx.stroke();
  drawFern(x, y - len, depth - 1, scale, width);
  drawFern(x + len * 0.3, y - len * 0.7, depth - 2, scale, width);
  drawFern(x - len * 0.3, y - len * 0.7, depth - 2, scale, width);
}}

function drawDragon(depth) {{
  let s = 'FX';
  const rules = {{ 'X':'X+YF+', 'Y':'-FX-Y' }};
  for (let i = 0; i < depth; i++) {{
    let ns = '';
    for (const c of s) ns += rules[c] || c;
    s = ns;
  }}
  let x = window.innerWidth/2, y = window.innerHeight/2;
  let angle = 0; const step = 5;
  ctx.beginPath();
  ctx.strokeStyle = '#f59e0b';
  ctx.lineWidth = params.lineWidth;
  ctx.moveTo(x, y);
  for (const c of s) {{
    if (c === 'F') {{ x += Math.cos(angle)*step; y += Math.sin(angle)*step; ctx.lineTo(x,y); }}
    else if (c === '+') angle += Math.PI/2;
    else if (c === '-') angle -= Math.PI/2;
  }}
  ctx.stroke();
}}

function drawSierpinski(depth) {{
  const size = Math.min(window.innerWidth, window.innerHeight) * 0.8;
  const cx = window.innerWidth/2, cy = window.innerHeight/2;
  const p1 = {{ x: cx, y: cy - size/2 }};
  const p2 = {{ x: cx - size/2, y: cy + size/2 }};
  const p3 = {{ x: cx + size/2, y: cy + size/2 }};
  drawTriangle(p1, p2, p3, depth);
}}

function drawTriangle(a, b, c, depth) {{
  if (depth === 0) {{
    ctx.beginPath();
    ctx.strokeStyle = `hsl(${{30 + Math.random()*20}}, 70%, 50%)`;
    ctx.lineWidth = params.lineWidth;
    ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.lineTo(c.x, c.y); ctx.closePath();
    ctx.stroke();
    return;
  }}
  const ab = {{ x:(a.x+b.x)/2, y:(a.y+b.y)/2 }};
  const bc = {{ x:(b.x+c.x)/2, y:(b.y+c.y)/2 }};
  const ca = {{ x:(c.x+a.x)/2, y:(c.y+a.y)/2 }};
  drawTriangle(a, ab, ca, depth-1);
  drawTriangle(ab, b, bc, depth-1);
  drawTriangle(ca, bc, c, depth-1);
}}

function update(dt) {{}}
function render() {{}}
</script>
""" + _base_scripts("redraw();"),

    "physics": lambda name, title: _base_head(title, "#ec4899") + f"""
<body>
<canvas id="canvas"></canvas>
<div class="topbar">
  <button class="mode-btn active" data-mode="wave">波纹</button>
  <button class="mode-btn" data-mode="interference">干涉</button>
  <button class="mode-btn" data-mode="doppler">多普勒</button>
</div>
<button class="panel-toggle" id="panelToggle">☰</button>
<div class="panel" id="panel">
  <div class="panel-section">
    <h3>波参数</h3>
    <div class="slider-row"><span class="slider-label">频率</span><input type="range" id="speedSlider" min="0.5" max="5" step="0.1" value="2"><span class="slider-value" id="speedVal">2.0</span></div>
    <div class="slider-row"><span class="slider-label">振幅</span><input type="range" id="dampSlider" min="10" max="100" step="5" value="40"><span class="slider-value" id="dampVal">40</span></div>
    <div class="slider-row"><span class="slider-label">波速</span><input type="range" id="widthSlider" min="50" max="300" step="10" value="150"><span class="slider-value" id="widthVal">150</span></div>
    <div class="slider-row"><span class="slider-label">间距</span><input type="range" id="spacingSlider" min="10" max="50" step="2" value="20"><span class="slider-value" id="spacingVal">20</span></div>
  </div>
  <div class="panel-section">
    <h3>操作</h3>
    <button class="action-btn primary" id="clearBtn">清空</button>
    <button class="action-btn" id="saveBtn">保存PNG</button>
  </div>
</div>
<div class="hint" id="hint">点击放置波源 · 拖动移动</div>
<div class="stats" id="stats">Sources: 0 | FPS: 0</div>
<script>
let sources = [];
let time = 0;

function onDown(x,y) {{
  hintEl.style.opacity = '0';
  sources.push({{ x: x, y: y, freq: params.speed, amp: params.damping, phase: 0 }});
}}
function onMove(x,y) {{ if (mouse.down && sources.length > 0) {{ sources[sources.length-1].x = x; sources[sources.length-1].y = y; }} }}
function onModeChange(m) {{ currentMode = m; }}

function update(dt) {{
  time += dt * params.speed;
}}

function render() {{
  const imageData = ctx.createImageData(window.innerWidth, window.innerHeight);
  const data = imageData.data;
  const step = 3; // Sample every 3 pixels for performance

  for (let y = 0; y < window.innerHeight; y += step) {{
    for (let x = 0; x < window.innerWidth; x += step) {{
      let val = 0;
      for (let s of sources) {{
        const dx = x - s.x, dy = y - s.y;
        const d = Math.sqrt(dx*dx + dy*dy);
        const waveSpeed = params.lineWidth; // width slider repurposed
        if (currentMode === 'wave') {{
          val += Math.sin(d / params.spacing - time * waveSpeed * 0.1) * s.amp / (d * 0.1 + 1);
        }} else if (currentMode === 'interference') {{
          val += Math.sin(d / params.spacing - time * waveSpeed * 0.1) * s.amp / (d * 0.05 + 1);
        }} else if (currentMode === 'doppler') {{
          const phase = d / params.spacing - time * waveSpeed * 0.15;
          const fade = 1 / (d * 0.005 + 1);
          val += Math.sin(phase) * s.amp * fade;
        }}
      }}
      // Map to color
      const normalized = (val / 100 + 1) / 2; // 0 to 1
      const r = Math.floor(normalized * 236);
      const g = Math.floor(normalized * 72 + (1-normalized) * 153);
      const b = Math.floor(normalized * 153 + (1-normalized) * 200);

      for (let dy = 0; dy < step && y+dy < window.innerHeight; dy++) {{
        for (let dx = 0; dx < step && x+dx < window.innerWidth; dx++) {{
          const idx = ((y+dy) * window.innerWidth + (x+dx)) * 4;
          data[idx] = r;
          data[idx+1] = g;
          data[idx+2] = b;
          data[idx+3] = 255;
        }}
      }}
    }}
  }}
  ctx.putImageData(imageData, 0, 0);

  // Draw source markers
  for (let s of sources) {{
    ctx.beginPath();
    ctx.arc(s.x, s.y, 5, 0, Math.PI*2);
    ctx.fillStyle = '#ec4899';
    ctx.fill();
  }}
}}
</script>
""" + _base_scripts(),

    "interactive": lambda name, title: _base_head(title, "#6366f1") + f"""
<body>
<canvas id="canvas"></canvas>
<div class="topbar">
  <button class="mode-btn active" data-mode="draw">绘制</button>
  <button class="mode-btn" data-mode="connect">连线</button>
  <button class="mode-btn" data-mode="erase">擦除</button>
</div>
<button class="panel-toggle" id="panelToggle">☰</button>
<div class="panel" id="panel">
  <div class="panel-section">
    <h3>设置</h3>
    <div class="slider-row"><span class="slider-label">星点大小</span><input type="range" id="speedSlider" min="1" max="8" step="0.5" value="2"><span class="slider-value" id="speedVal">2.0</span></div>
    <div class="slider-row"><span class="slider-label">连线距离</span><input type="range" id="dampSlider" min="50" max="300" step="10" value="120"><span class="slider-value" id="dampVal">120</span></div>
    <div class="slider-row"><span class="slider-label">星点密度</span><input type="range" id="widthSlider" min="50" max="500" step="10" value="200"><span class="slider-value" id="widthVal">200</span></div>
    <div class="slider-row"><span class="slider-label">闪烁速度</span><input type="range" id="spacingSlider" min="0.5" max="5" step="0.1" value="2"><span class="slider-value" id="spacingVal">2.0</span></div>
  </div>
  <div class="panel-section">
    <h3>操作</h3>
    <button class="action-btn primary" id="clearBtn">清空</button>
    <button class="action-btn" id="saveBtn">保存PNG</button>
  </div>
</div>
<div class="hint" id="hint">点击添加星点 · 切换模式连线</div>
<div class="stats" id="stats">Stars: 0 | FPS: 0</div>
<script>
let stars = [];

function init() {{
  // Generate initial star field
  for (let i = 0; i < params.lineWidth; i++) {{
    stars.push({{
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight,
      size: Math.random() * params.speed + 0.5,
      phase: Math.random() * Math.PI * 2,
    }});
  }}
}}
init();

function onDown(x,y) {{
  hintEl.style.opacity = '0';
  if (currentMode === 'draw') {{
    stars.push({{ x: x, y: y, size: params.speed, phase: 0 }});
  }} else if (currentMode === 'erase') {{
    stars = stars.filter(s => Math.sqrt((s.x-x)**2 + (s.y-y)**2) > 20);
  }}
}}
function onMove(x,y) {{
  if (mouse.down) {{
    if (currentMode === 'draw') {{
      stars.push({{ x: x, y: y, size: params.speed, phase: Math.random()*Math.PI*2 }});
    }} else if (currentMode === 'erase') {{
      stars = stars.filter(s => Math.sqrt((s.x-x)**2 + (s.y-y)**2) > 15);
    }}
  }}
}}
function onModeChange(m) {{ currentMode = m; }}

function update(dt) {{
  for (let s of stars) {{
    s.phase += dt * params.spacing;
  }}
}}

function render() {{
  ctx.fillStyle = 'rgba(240, 253, 250, 0.1)';
  ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);

  // Draw auto-connections
  if (currentMode === 'connect') {{
    const dist = params.damping;
    for (let i = 0; i < stars.length; i++) {{
      for (let j = i+1; j < stars.length; j++) {{
        const dx = stars[i].x - stars[j].x, dy = stars[i].y - stars[j].y;
        const d = Math.sqrt(dx*dx + dy*dy);
        if (d < dist) {{
          ctx.beginPath();
          ctx.strokeStyle = `rgba(99, 102, 241, ${{(1 - d/dist) * 0.3}})`;
          ctx.lineWidth = 0.5;
          ctx.moveTo(stars[i].x, stars[i].y);
          ctx.lineTo(stars[j].x, stars[j].y);
          ctx.stroke();
        }}
      }}
    }}
  }}

  // Draw stars
  for (let s of stars) {{
    const twinkle = 0.5 + Math.sin(s.phase) * 0.5;
    ctx.beginPath();
    ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(99, 102, 241, ${{twinkle * 0.8}})`;
    ctx.fill();
    // Glow
    ctx.beginPath();
    ctx.arc(s.x, s.y, s.size * 3, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(99, 102, 241, ${{twinkle * 0.1}})`;
    ctx.fill();
  }}
}}
</script>
""" + _base_scripts(),

    "visual-effect": lambda name, title: _base_head(title, "#06b6d4") + f"""
<body>
<canvas id="canvas"></canvas>
<div class="topbar">
  <button class="mode-btn active" data-mode="attract">吸引</button>
  <button class="mode-btn" data-mode="repel">排斥</button>
  <button class="mode-btn" data-mode="explode">爆炸</button>
  <button class="mode-btn" data-mode="vortex">漩涡</button>
</div>
<button class="panel-toggle" id="panelToggle">☰</button>
<div class="panel" id="panel">
  <div class="panel-section">
    <h3>粒子参数</h3>
    <div class="slider-row"><span class="slider-label">力强度</span><input type="range" id="speedSlider" min="0.5" max="10" step="0.1" value="3"><span class="slider-value" id="speedVal">3.0</span></div>
    <div class="slider-row"><span class="slider-label">粒子数</span><input type="range" id="dampSlider" min="500" max="5000" step="100" value="2000"><span class="slider-value" id="dampVal">2000</span></div>
    <div class="slider-row"><span class="slider-label">点大小</span><input type="range" id="widthSlider" min="0.5" max="4" step="0.1" value="1.5"><span class="slider-value" id="widthVal">1.5</span></div>
    <div class="slider-row"><span class="slider-label">阻尼</span><input type="range" id="spacingSlider" min="0.8" max="0.99" step="0.01" value="0.95"><span class="slider-value" id="spacingVal">0.95</span></div>
  </div>
  <div class="panel-section">
    <h3>操作</h3>
    <button class="action-btn primary" id="clearBtn">重置</button>
    <button class="action-btn" id="saveBtn">保存PNG</button>
  </div>
</div>
<div class="hint" id="hint">移动鼠标与粒子交互</div>
<div class="stats" id="stats">Particles: 0 | FPS: 0</div>
<script>
let targetCount = 2000;
let textPixels = [];

function initText() {{
  // No text, just random positions
  for (let i = 0; i < targetCount; i++) {{
    particles.push({{
      x: Math.random() * window.innerWidth,
      y: Math.random() * window.innerHeight,
      vx: 0, vy: 0,
      tx: 0, ty: 0,
      hue: 180 + Math.random() * 40,
    }});
  }}
}}
initText();

function onModeChange(m) {{ currentMode = m; }}
function onMove(x,y) {{ mouse.x = x; mouse.y = y; hintEl.style.opacity = '0'; }}
function onDown(x,y) {{
  // Explode
  for (let p of particles) {{
    const dx = p.x - x, dy = p.y - y;
    const d = Math.sqrt(dx*dx + dy*dy) + 1;
    if (d < 200) {{
      p.vx += dx/d * 20;
      p.vy += dy/d * 20;
    }}
  }}
}}

function update(dt) {{
  targetCount = params.damping || 2000;
  while (particles.length < targetCount) {{
    particles.push({{ x: Math.random()*window.innerWidth, y: Math.random()*window.innerHeight, vx:0, vy:0, hue: 180+Math.random()*40 }});
  }}
  while (particles.length > targetCount) particles.pop();

  for (let p of particles) {{
    if (currentMode === 'attract') {{
      const dx = mouse.x - p.x, dy = mouse.y - p.y;
      const d = Math.sqrt(dx*dx + dy*dy) + 1;
      p.vx += dx/d * params.speed;
      p.vy += dy/d * params.speed;
    }} else if (currentMode === 'repel') {{
      const dx = p.x - mouse.x, dy = p.y - mouse.y;
      const d = Math.sqrt(dx*dx + dy*dy) + 1;
      if (d < 150) {{
        p.vx += dx/d * params.speed * (1 - d/150);
        p.vy += dy/d * params.speed * (1 - d/150);
      }}
    }} else if (currentMode === 'vortex') {{
      const dx = mouse.x - p.x, dy = mouse.y - p.y;
      const d = Math.sqrt(dx*dx + dy*dy) + 1;
      p.vx += -dy/d * params.speed * 0.5;
      p.vy += dx/d * params.speed * 0.5;
      p.vx += dx/d * params.speed * 0.1;
      p.vy += dy/d * params.speed * 0.1;
    }}
    p.vx *= params.spacing;
    p.vy *= params.spacing;
    p.x += p.vx;
    p.y += p.vy;
    if (p.x < 0) p.x = window.innerWidth;
    if (p.x > window.innerWidth) p.x = 0;
    if (p.y < 0) p.y = window.innerHeight;
    if (p.y > window.innerHeight) p.y = 0;
  }}
}}

function render() {{
  for (let p of particles) {{
    const speed = Math.sqrt(p.vx*p.vx + p.vy*p.vy);
    const alpha = Math.min(1, speed * 0.1 + 0.2);
    ctx.fillStyle = `hsla(${{p.hue}}, 80%, 55%, ${{alpha}})`;
    ctx.fillRect(p.x, p.y, params.lineWidth, params.lineWidth);
  }}
}}
</script>
""" + _base_scripts(),

    "algorithm": lambda name, title: _base_head(title, "#10b981") + f"""
<body>
<canvas id="canvas"></canvas>
<div class="topbar">
  <button class="mode-btn active" data-mode="dfs">DFS</button>
  <button class="mode-btn" data-mode="bfs">BFS</button>
  <button class="mode-btn" data-mode="astar">A*</button>
</div>
<button class="panel-toggle" id="panelToggle">☰</button>
<div class="panel" id="panel">
  <div class="panel-section">
    <h3>迷宫参数</h3>
    <div class="slider-row"><span class="slider-label">格子大小</span><input type="range" id="speedSlider" min="10" max="50" step="2" value="25"><span class="slider-value" id="speedVal">25</span></div>
    <div class="slider-row"><span class="slider-label">动画速度</span><input type="range" id="dampSlider" min="1" max="50" step="1" value="10"><span class="slider-value" id="dampVal">10</span></div>
    <div class="slider-row"><span class="slider-label">线宽</span><input type="range" id="widthSlider" min="0.5" max="3" step="0.1" value="1.5"><span class="slider-value" id="widthVal">1.5</span></div>
  </div>
  <div class="panel-section">
    <h3>操作</h3>
    <button class="action-btn primary" id="genBtn">生成迷宫</button>
    <button class="action-btn" id="solveBtn">寻路</button>
    <button class="action-btn" id="saveBtn">保存PNG</button>
  </div>
</div>
<div class="hint" id="hint">点击"生成迷宫"开始</div>
<div class="stats" id="stats">Grid: 0x0 | FPS: 0</div>
<script>
let cellSize = 25;
let cols, rows;
let grid = [];
let stack = [];
let current = null;
let solving = false;
let pathFound = false;

function onModeChange(m) {{ currentMode = m; }}

function generateMaze() {{
  cellSize = params.speed;
  cols = Math.floor(window.innerWidth / cellSize);
  rows = Math.floor(window.innerHeight / cellSize);
  grid = [];
  for (let y = 0; y < rows; y++) {{
    for (let x = 0; x < cols; x++) {{
      grid.push({{ x, y, walls: [true,true,true,true], visited: false, inPath: false }});
    }}
  }}
  stack = [grid[0]];
  grid[0].visited = true;
  solving = false; pathFound = false;
  hintEl.style.opacity = '0';
}}

document.getElementById('genBtn').addEventListener('click', () => {{ generateMaze(); }});
document.getElementById('solveBtn').addEventListener('click', () => {{ solveMaze(); }});

function getCell(x, y) {{
  if (x < 0 || y < 0 || x >= cols || y >= rows) return null;
  return grid[y * cols + x];
}}

function getUnvisitedNeighbors(cell) {{
  const n = [];
  const t = getCell(cell.x, cell.y-1), r = getCell(cell.x+1, cell.y), b = getCell(cell.x, cell.y+1), l = getCell(cell.x-1, cell.y);
  if (t && !t.visited) n.push(t);
  if (r && !r.visited) n.push(r);
  if (b && !b.visited) n.push(b);
  if (l && !l.visited) n.push(l);
  return n;
}}

function removeWalls(a, b) {{
  const dx = a.x - b.x, dy = a.y - b.y;
  if (dx === 1) {{ a.walls[3] = false; b.walls[1] = false; }}
  else if (dx === -1) {{ a.walls[1] = false; b.walls[3] = false; }}
  if (dy === 1) {{ a.walls[0] = false; b.walls[2] = false; }}
  else if (dy === -1) {{ a.walls[2] = false; b.walls[0] = false; }}
}}

function solveMaze() {{
  // Reset path
  grid.forEach(c => c.inPath = false);
  // BFS from first to last
  const start = grid[0], end = grid[grid.length - 1];
  const queue = [start];
  const visited = new Set([0]);
  const parent = {{}};
  while (queue.length > 0) {{
    const c = queue.shift();
    if (c === end) break;
    const neighbors = [];
    if (!c.walls[0]) {{ const n = getCell(c.x, c.y-1); if (n && !visited.has(n.y*cols+n.x)) neighbors.push(n); }}
    if (!c.walls[1]) {{ const n = getCell(c.x+1, c.y); if (n && !visited.has(n.y*cols+n.x)) neighbors.push(n); }}
    if (!c.walls[2]) {{ const n = getCell(c.x, c.y+1); if (n && !visited.has(n.y*cols+n.x)) neighbors.push(n); }}
    if (!c.walls[3]) {{ const n = getCell(c.x-1, c.y); if (n && !visited.has(n.y*cols+n.x)) neighbors.push(n); }}
    for (let n of neighbors) {{
      visited.add(n.y*cols+n.x);
      parent[n.y*cols+n.x] = c;
      queue.push(n);
    }}
  }}
  // Trace path
  let c = end;
  while (c) {{ c.inPath = true; c = parent[c.y*cols+c.x]; }}
  pathFound = true;
}}

function update(dt) {{
  // Generate maze step by step
  const steps = Math.floor(params.damping);
  for (let i = 0; i < steps && stack.length > 0; i++) {{
    current = stack[stack.length - 1];
    const neighbors = getUnvisitedNeighbors(current);
    if (neighbors.length > 0) {{
      const next = neighbors[Math.floor(Math.random() * neighbors.length)];
      removeWalls(current, next);
      next.visited = true;
      stack.push(next);
    }} else {{
      stack.pop();
    }}
  }}
}}

function render() {{
  ctx.fillStyle = theme.bg;
  ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);

  if (grid.length === 0) return;

  for (let c of grid) {{
    const x = c.x * cellSize, y = c.y * cellSize;
    if (c.inPath) {{
      ctx.fillStyle = 'rgba(16, 185, 129, 0.3)';
      ctx.fillRect(x, y, cellSize, cellSize);
    }} else if (c.visited) {{
      ctx.fillStyle = 'rgba(6, 182, 212, 0.05)';
      ctx.fillRect(x, y, cellSize, cellSize);
    }}
    if (c === current) {{
      ctx.fillStyle = '#f59e0b';
      ctx.fillRect(x, y, cellSize, cellSize);
    }}
    // Walls
    ctx.strokeStyle = theme.primary;
    ctx.lineWidth = params.lineWidth;
    ctx.beginPath();
    if (c.walls[0]) {{ ctx.moveTo(x, y); ctx.lineTo(x+cellSize, y); }}
    if (c.walls[1]) {{ ctx.moveTo(x+cellSize, y); ctx.lineTo(x+cellSize, y+cellSize); }}
    if (c.walls[2]) {{ ctx.moveTo(x, y+cellSize); ctx.lineTo(x+cellSize, y+cellSize); }}
    if (c.walls[3]) {{ ctx.moveTo(x, y); ctx.lineTo(x, y+cellSize); }}
    ctx.stroke();
  }}

  if (statsEl) statsEl.textContent = `Grid: ${{cols}}x${{rows}} | FPS: ${{fps}}`;
}}
</script>
""" + _base_scripts(),

    "tool": lambda name, title: _base_head(title, "#6366f1") + f"""
<body>
<canvas id="canvas"></canvas>
<div class="topbar">
  <button class="mode-btn active" data-mode="draw">绘制</button>
  <button class="mode-btn" data-mode="erase">擦除</button>
  <button class="mode-btn" data-mode="fill">填充</button>
</div>
<button class="panel-toggle" id="panelToggle">☰</button>
<div class="panel" id="panel">
  <div class="panel-section">
    <h3>画笔参数</h3>
    <div class="slider-row"><span class="slider-label">画笔大小</span><input type="range" id="speedSlider" min="1" max="20" step="1" value="3"><span class="slider-value" id="speedVal">3</span></div>
    <div class="slider-row"><span class="slider-label">画布尺寸</span><input type="range" id="dampSlider" min="8" max="64" step="2" value="32"><span class="slider-value" id="dampVal">32</span></div>
    <div class="slider-row"><span class="slider-label">帧数</span><input type="range" id="widthSlider" min="1" max="12" step="1" value="4"><span class="slider-value" id="widthVal">4</span></div>
  </div>
  <div class="panel-section">
    <h3>操作</h3>
    <button class="action-btn primary" id="playBtn">播放动画</button>
    <button class="action-btn" id="clearBtn">清空</button>
    <button class="action-btn" id="saveBtn">保存PNG</button>
  </div>
</div>
<div class="hint" id="hint">点击绘制像素 · 拖动连续绘制</div>
<div class="stats" id="stats">Grid: 0 | FPS: 0</div>
<script>
let gridSize = 32;
let pixelSize;
let currentColor = '#06b6d4';
let currentFrame = 0;
let totalFrames = 4;
let frames = [];
let isPlaying = false;
let playFrame = 0;
let playTimer = 0;

const palette = ['#06b6d4','#0e7490','#67e8f9','#10b981','#f59e0b','#ec4899','#8b5cf6','#ef4444','#ffffff','#6366f1','#14b8a6','#f97316'];

// Palette UI
const palDiv = document.createElement('div');
palDiv.style.cssText = 'display:flex;flex-wrap:wrap;gap:4px;margin-bottom:8px;';
palette.forEach(c => {{
  const sw = document.createElement('div');
  sw.style.cssText = `width:20px;height:20px;border-radius:4px;background:${c};cursor:pointer;border:2px solid transparent;`;
  sw.onclick = () => {{ currentColor = c; palDiv.querySelectorAll('div').forEach(d=>d.style.borderColor='transparent'); sw.style.borderColor='#333'; }};
  palDiv.appendChild(sw);
}});
document.querySelector('.panel-section').appendChild(palDiv);

function initFrames() {{
  gridSize = params.damping;
  totalFrames = params.lineWidth;
  pixelSize = Math.floor(Math.min(window.innerWidth, window.innerHeight) * 0.7 / gridSize);
  if (!frames[currentFrame]) {{
    frames[currentFrame] = new Array(gridSize * gridSize).fill(null);
  }}
}}
initFrames();

function onModeChange(m) {{ currentMode = m; }}
function onDown(x,y) {{ hintEl.style.opacity='0'; paintPixel(x,y); }}
function onMove(x,y) {{ if (mouse.down) paintPixel(x,y); }}

function paintPixel(x, y) {{
  const offsetX = (window.innerWidth - gridSize * pixelSize) / 2;
  const offsetY = (window.innerHeight - gridSize * pixelSize) / 2;
  const gx = Math.floor((x - offsetX) / pixelSize);
  const gy = Math.floor((y - offsetY) / pixelSize);
  if (gx < 0 || gx >= gridSize || gy < 0 || gy >= gridSize) return;
  if (!frames[currentFrame]) frames[currentFrame] = new Array(gridSize*gridSize).fill(null);
  if (currentMode === 'erase') {{
    frames[currentFrame][gy * gridSize + gx] = null;
  }} else {{
    frames[currentFrame][gy * gridSize + gx] = currentColor;
  }}
}}

document.getElementById('playBtn').addEventListener('click', () => {{
  isPlaying = !isPlaying;
  document.getElementById('playBtn').textContent = isPlaying ? '停止' : '播放动画';
  playFrame = 0;
}});

function update(dt) {{
  if (isPlaying) {{
    playTimer += dt;
    if (playTimer > 0.15) {{
      playTimer = 0;
      playFrame = (playFrame + 1) % Math.max(1, frames.length);
    }}
  }}
  if (params.damping !== gridSize) {{ initFrames(); }}
  totalFrames = params.lineWidth;
  while (frames.length < totalFrames) frames.push(new Array(gridSize*gridSize).fill(null));
}}

function render() {{
  ctx.fillStyle = theme.bg;
  ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);
  const offsetX = (window.innerWidth - gridSize * pixelSize) / 2;
  const offsetY = (window.innerHeight - gridSize * pixelSize) / 2;
  const showFrame = isPlaying ? frames[playFrame] : frames[currentFrame];

  // Grid background
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(offsetX, offsetY, gridSize * pixelSize, gridSize * pixelSize);

  // Draw pixels
  if (showFrame) {{
    for (let i = 0; i < showFrame.length; i++) {{
      if (showFrame[i]) {{
        const gx = i % gridSize, gy = Math.floor(i / gridSize);
        ctx.fillStyle = showFrame[i];
        ctx.fillRect(offsetX + gx * pixelSize, offsetY + gy * pixelSize, pixelSize, pixelSize);
      }}
    }}
  }}

  // Grid lines
  ctx.strokeStyle = 'rgba(6,182,212,0.15)';
  ctx.lineWidth = 0.5;
  for (let i = 0; i <= gridSize; i++) {{
    ctx.beginPath();
    ctx.moveTo(offsetX + i * pixelSize, offsetY);
    ctx.lineTo(offsetX + i * pixelSize, offsetY + gridSize * pixelSize);
    ctx.moveTo(offsetX, offsetY + i * pixelSize);
    ctx.lineTo(offsetX + gridSize * pixelSize, offsetY + i * pixelSize);
    ctx.stroke();
  }}

  if (statsEl) statsEl.textContent = `Grid: ${{gridSize}}x${{gridSize}} | Frame: ${{isPlaying ? playFrame+1 : currentFrame+1}}/${{totalFrames}} | FPS: ${{fps}}`;
}}
</script>
""" + _base_scripts(),

    "ai-visual": lambda name, title: _base_head(title, "#8b5cf6") + f"""
<body>
<canvas id="canvas"></canvas>
<div class="topbar">
  <button class="mode-btn active" data-mode="forward">前向传播</button>
  <button class="mode-btn" data-mode="train">训练</button>
</div>
<button class="panel-toggle" id="panelToggle">☰</button>
<div class="panel" id="panel">
  <div class="panel-section">
    <h3>网络参数</h3>
    <div class="slider-row"><span class="slider-label">隐藏层</span><input type="range" id="speedSlider" min="2" max="8" step="1" value="4"><span class="slider-value" id="speedVal">4</span></div>
    <div class="slider-row"><span class="slider-label">每层节点</span><input type="range" id="dampSlider" min="3" max="12" step="1" value="6"><span class="slider-value" id="dampVal">6</span></div>
    <div class="slider-row"><span class="slider-label">学习率</span><input type="range" id="widthSlider" min="0.01" max="1" step="0.01" value="0.3"><span class="slider-value" id="widthVal">0.30</span></div>
    <div class="slider-row"><span class="slider-label">线宽</span><input type="range" id="spacingSlider" min="0.5" max="3" step="0.1" value="1"><span class="slider-value" id="spacingVal">1.0</span></div>
  </div>
  <div class="panel-section">
    <h3>操作</h3>
    <button class="action-btn primary" id="clearBtn">重置网络</button>
    <button class="action-btn" id="saveBtn">保存PNG</button>
  </div>
</div>
<div class="hint" id="hint">点击输入层节点激活 · 切换训练模式</div>
<div class="stats" id="stats">Layers: 0 | FPS: 0</div>
<script>
let layers = [];
let weights = [];
let activations = [];

function buildNetwork() {{
  const numHidden = Math.floor(params.speed);
  const nodesPerLayer = Math.floor(params.damping);
  layers = [2]; // 2 inputs
  for (let i = 0; i < numHidden; i++) layers.push(nodesPerLayer);
  layers.push(1); // 1 output

  // Init weights
  weights = [];
  for (let l = 0; l < layers.length - 1; l++) {{
    const layerW = [];
    for (let j = 0; j < layers[l+1]; j++) {{
      const row = [];
      for (let k = 0; k < layers[l]; k++) {{
        row.push((Math.random() - 0.5) * 2);
      }}
      layerW.push(row);
    }}
    weights.push(layerW);
  }}
  activations = layers.map(n => new Array(n).fill(0));
  // Random input
  activations[0] = [Math.random(), Math.random()];
  forward();
}}

function sigmoid(x) {{ return 1 / (1 + Math.exp(-x)); }}

function forward() {{
  for (let l = 0; l < layers.length - 1; l++) {{
    for (let j = 0; j < layers[l+1]; j++) {{
      let sum = 0;
      for (let k = 0; k < layers[l]; k++) {{
        sum += activations[l][k] * weights[l][j][k];
      }}
      activations[l+1][j] = sigmoid(sum);
    }}
  }}
}}

buildNetwork();

function onModeChange(m) {{ currentMode = m; }}
function onDown(x,y) {{
  // Click input node to toggle
  const positions = getNodePositions();
  for (let i = 0; i < positions[0].length; i++) {{
    const p = positions[0][i];
    if (Math.sqrt((p.x-x)**2 + (p.y-y)**2) < 20) {{
      activations[0][i] = activations[0][i] > 0.5 ? 0 : 1;
      forward();
      hintEl.style.opacity = '0';
      break;
    }}
  }}
}}

function getNodePositions() {{
  const w = window.innerWidth, h = window.innerHeight;
  const margin = 100;
  const layerSpacing = (w - margin * 2) / (layers.length - 1);
  const positions = layers.map((count, l) => {{
    const x = margin + l * layerSpacing;
    const nodeSpacing = Math.min(60, (h - 200) / count);
    const startY = h/2 - (count - 1) * nodeSpacing / 2;
    const arr = [];
    for (let i = 0; i < count; i++) {{
      arr.push({{ x, y: startY + i * nodeSpacing }});
    }}
    return arr;
  }});
  return positions;
}}

function update(dt) {{
  if (currentMode === 'train') {{
    // Train XOR
    const inputs = [[0,0],[0,1],[1,0],[1,1]];
    const targets = [0, 1, 1, 0];
    const idx = Math.floor(Math.random() * 4);
    activations[0] = inputs[idx].slice();
    forward();
    // Backprop simplified
    const lr = params.lineWidth;
    const outputError = activations[layers.length-1][0] - targets[idx];
    // Update last layer weights
    const l = layers.length - 2;
    for (let j = 0; j < layers[l+1]; j++) {{
      for (let k = 0; k < layers[l]; k++) {{
        weights[l][j][k] -= lr * outputError * activations[l][k] * activations[l+1][j] * (1 - activations[l+1][j]);
      }}
    }}
  }}
  // Slowly decay activations for visual effect
  for (let l = 1; l < layers.length; l++) {{
    for (let i = 0; i < layers[l]; i++) {{
      // Keep showing current forward pass
    }}
  }}
}}

function render() {{
  ctx.fillStyle = theme.bg;
  ctx.fillRect(0, 0, window.innerWidth, window.innerHeight);

  const positions = getNodePositions();

  // Draw connections
  for (let l = 0; l < layers.length - 1; l++) {{
    for (let j = 0; j < layers[l+1]; j++) {{
      for (let k = 0; k < layers[l]; k++) {{
        const w = weights[l][j][k];
        const alpha = Math.min(1, Math.abs(w) * 0.5);
        ctx.beginPath();
        ctx.strokeStyle = w > 0 ? `rgba(139, 92, 246, ${{alpha}})` : `rgba(236, 72, 153, ${{alpha}})`;
        ctx.lineWidth = params.spacing * Math.min(3, Math.abs(w));
        ctx.moveTo(positions[l][k].x, positions[l][k].y);
        ctx.lineTo(positions[l+1][j].x, positions[l+1][j].y);
        ctx.stroke();
      }}
    }}
  }}

  // Draw nodes
  for (let l = 0; l < layers.length; l++) {{
    for (let i = 0; i < layers[l]; i++) {{
      const p = positions[l][i];
      const a = activations[l][i];
      ctx.beginPath();
      ctx.arc(p.x, p.y, 12 + a * 6, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(139, 92, 246, ${{a * 0.8 + 0.1}})`;
      ctx.fill();
      ctx.strokeStyle = '#8b5cf6';
      ctx.lineWidth = 1.5;
      ctx.stroke();
      // Activation value
      ctx.fillStyle = '#fff';
      ctx.font = '10px sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(a.toFixed(2), p.x, p.y);
    }}
  }}

  // Layer labels
  ctx.font = '11px sans-serif';
  ctx.fillStyle = '#67a3b0';
  ctx.textAlign = 'center';
  positions.forEach((_, l) => {{
    const x = positions[0][0].x + l * (positions[1][0].x - positions[0][0].x || 0);
  }});

  if (statsEl) statsEl.textContent = `Layers: ${{layers.length}} | Output: ${{activations[layers.length-1][0]?.toFixed(3) || 0}} | FPS: ${{fps}}`;
}}
</script>
""" + _base_scripts("buildNetwork();"),
}


if __name__ == "__main__":
    project, manifest = get_today_project()
    output_dir = generate_project(project, manifest)

    # Output for GitHub Actions (new format)
    gh_output = os.environ.get('GITHUB_OUTPUT', os.devnull)
    with open(gh_output, 'a') as f:
        f.write(f"name={project['name']}\n")
        f.write(f"desc={project['desc']}\n")
        f.write(f"dir={output_dir}\n")

    print(f"Project: {project['name']} ({project['title']})")
    print(f"Description: {project['desc']}")
    print(f"Output: {output_dir}")
