# Creative Bot

> GitHub Actions 驱动的自动化创意项目生成器 | 每日自动生成高质量交互式 Web 项目

## 工作原理

1. GitHub Actions 每天北京时间 09:00 自动触发
2. Python 生成器从模板库中选取一个项目类型
3. 生成完整的单文件 HTML 项目（含 Canvas 交互、控制面板、参数调节）
4. 自动推送到本仓库的 `projects/` 目录下
5. 更新首页 `index.html` 自动索引所有项目

## 项目模板

| 模板 | 类别 | 说明 |
|------|------|------|
| aurora-flow | 生成式艺术 | Perlin 噪声粒子流场，鼠标交互扰动 |
| ink-bloom | 生成式艺术 | 水墨扩散效果，点击生成墨花 |
| gravity-garden | 物理模拟 | 多体引力场粒子模拟，轨道可视化 |
| sound-ripple | 音频可视化 | 麦克风实时声波涟漪，频谱可视化 |
| fractal-tree | 分形 | L-系统分形树，风吹动画，多种分形模式 |
| star-map | 交互工具 | 实时星座绘制，鼠标连线命名 |
| particle-text | 视觉效果 | 粒子系统，吸引/排斥/爆炸/漩涡模式 |
| maze-genesis | 算法可视化 | 迷宫生成与寻路，DFS/BFS/A* |
| wave-interference | 物理模拟 | 双源波纹干涉，实时像素级渲染 |
| color-sonic | 音频可视化 | 音频驱动色彩生成器 |
| neural-viz | AI可视化 | 小型神经网络可视化训练过程 |
| sand-castle | 物理模拟 | 元胞自动机沙子模拟 |
| light-ray | 物理模拟 | 2D 光线追踪反射折射 |
| word-cloud-gen | 实用工具 | 实时词云生成器 |
| pixel-sprite | 创作工具 | 像素艺术动画编辑器 |

## 技术特点

- 所有生成项目均为纯 HTML5 + Canvas，零外部依赖
- 青白配色，简洁干净的 UI 风格
- 支持鼠标/触摸/键盘交互
- 响应式设计，高 DPI 支持
- 参数控制面板，实时调节
- 一键 PNG 导出

## 手动触发

在 GitHub 仓库页面 → Actions → Daily Creative Project → Run workflow 即可手动触发。

## 添加新模板

编辑 `generator.py` 中的 `PROJECTS` 列表和 `HTML_TEMPLATES` 字典即可。

## License

MIT
