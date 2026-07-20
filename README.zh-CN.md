<div align="center">

# Awesome Claude UI Armory 🎨

面向 Claude Code & AI agent 的前端/UI skill 精选索引 —— 一座 UI 军火库。

![Made for Claude Code](https://img.shields.io/badge/Made%20for-Claude%20Code-blueviolet)
![Type: Curated Index](https://img.shields.io/badge/Type-Curated%20Index-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

[English](README.md) · 中文

</div>

## 简介

面向 Claude Code 与 AI agent 的前端/UI skill 精选索引 —— 一座"UI 军火库"。每条目仅链接到原始 skill 仓库并附一句话说明。**仅收录链接**，不重发他人 skill 代码，以尊重上游版权。涵盖本地已安装 skill 与 GitHub 上的优质社区 skill。

## 使用方法

- 将原仓库 clone 到 `~/.claude/skills/<name>`，或
- 通过 `/plugin marketplace add <owner>/<repo>` 添加插件市场，再安装对应 skill 插件。

具体安装步骤以各仓库自身 README 为准。

## 分类

每个分类为一个表格，列：Skill | 说明 | 来源 | 星数。
来源：**Official**（Anthropic 官方）、**Mine**（Ezra-Y 自建）、**Community**（社区）。星数为 Community 条目的 GitHub 实际星数；Official 与 Mine 标 `—`。

---

### 1. UI/UX 视觉设计

| Skill | 说明 | 来源 | 星数 |
|---|---|---|---|
| [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | 做新 UI 或重构界面时的视觉设计指导。推动大胆设计决策、避免 AI 套路审美；配合 React + Tailwind 很好。 | Official | — |
| [ui-ux-pro-max](https://github.com/anthropics/skills) | UI/UX 知识库：50+ 风格、161 配色、57 字体配对、99 条 UX 规则，覆盖 10 个技术栈。用于规划/构建/审查/优化 UI/UX 代码。 | Official | — |
| [ui-styling](https://github.com/anthropics/skills) | 用 shadcn/ui + Radix + Tailwind 做漂亮可访问的界面。主题、暗色模式、响应式布局、一致性样式模式。 | Official | — |
| [web-design-guidelines](https://github.com/anthropics/skills) | 按 Web 界面规范审查 UI 代码——可访问性、UX、站点最佳实践。用于审计/打磨已有界面。 | Official | — |
| [impeccable](https://github.com/anthropics/skills) | 设计、重设计、塑形、评审、审计、打磨界面，直到它有意图且精致。端到端的 UI 工艺。 | Official | — |
| [web-design](https://github.com/KAOPU-XiaoPu/web-design) | 设计美观、一致的网页。专注页面整体设计、有主见的美学。 | Community | ⭐592 |
| [ai-friendly-web-design-skill](https://github.com/ianho7/ai-friendly-web-design-skill) | 构建对 AI 助手和用户都友好的 web 界面——结构、语义、可访问性为 AI 消费调优。 | Community | ⭐70 |
| [web-designer-plugin](https://github.com/MickeyAlton33/web-designer-plugin) | 48 个获奖的 web 设计模式（plugin）。开箱即用的 hero/导航/卡片/表单等模式。 | Community | ⭐76 |
| [tasteful-ui-skill](https://github.com/DonkeyKing01/tasteful-ui-skill) | 品味优先的 UI 设计 skill——先探索视觉方向再下手，避免套路化产出。 | Community | ⭐6 |
| [UIUX-high-taste-skill](https://github.com/Payoss/UIUX-high-taste-skill) | 精选的高品质 UI/UX 设计 skill 合集。高品味、精致产出，适合高标准项目。 | Community | ⭐10 |
| [elite-web-design](https://github.com/RSHVR/elite-web-design) | 高端前端设计 skill 合集——大胆、有辨识度的 web 美学，面向生产应用。 | Community | ⭐1 |
| [frontend-design-engineer-skill](https://github.com/angelapaia/frontend-design-engineer-skill) | 一个 skill 集成艺术总监 + 高级前端工程师。衔接设计愿景与前端实现。 | Community | ⭐4 |

### 2. 设计系统 / 主题 / Token

| Skill | 说明 | 来源 | 星数 |
|---|---|---|---|
| [design-system](https://github.com/anthropics/skills) | 三层 token 架构（原始→语义→组件）、组件规范、CSS 变量、间距/字体尺度、Tailwind 集成。 | Official | — |
| [theme-factory](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | 套用预设主题（10 个内置，如 arctic-frost、midnight-galaxy）或即时生成自定义主题——配色+字体——给 slides/docs/landing page。 | Official | — |
| [material-3-skill](https://github.com/hamen/material-3-skill) | 实现 Google Material Design 3（Material You）。主攻 Jetpack Compose + Flutter，web 有限。30+ 组件、主题、动态配色。 | Community | ⭐1154 |
| [design-systems-index](https://github.com/Ezra-Y/design-systems-index) | 各公司设计系统索引（Material/Fluent/Carbon/Polaris/Atlassian）+ tokens + pattern library + React/RN DS 库。 | Mine | — |
| [design-system-stack](https://github.com/pato-gonzalez/design-system-stack) | 4-skill 包：为 AI agent 端到端提取、构建、维护、文档化设计系统。 | Community | ⭐4 |
| [getdesign](https://github.com/MohtashamMurshid/getdesign) | 从任意 URL 即时提取设计系统。五个面、一个 agent——把线上站点变可复用 DS。 | Community | ⭐44 |

### 3. 静态视觉 / 资源 / 资源索引

| Skill | 说明 | 来源 | 星数 |
|---|---|---|---|
| [canvas-design](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | 用设计哲学生成 .png/.pdf 视觉艺术，内置 30+ 字体。用于海报、艺术、静态作品。 | Official | — |
| [banner-design](https://github.com/anthropics/skills) | 社媒/广告/网站 hero/印刷 banner。多种艺术方向 + AI 生成视觉；按平台尺寸。 | Official | — |
| [slides](https://github.com/anthropics/skills) | 策略型 HTML 演示文稿，含 Chart.js、设计 token、响应式布局、文案公式、幻灯策略。 | Official | — |
| [frontend-slides](https://github.com/zarazhangrui/frontend-slides) | 从零或转换 PowerPoint 创建动画丰富的 HTML 演示。含 bold 模板包。 | Community | ⭐25960 |
| [design](https://github.com/anthropics/skills) | 内置设计生产：logo（55 风格）、CIP 样机、SVG 图标（15 风格）、社媒照片。多平台产出。 | Official | — |
| [design-assets-index](https://github.com/Ezra-Y/design-assets-index) | 现成设计素材索引——图库、图标、字体、配色、Mockup、UI Kit、模板。找素材去哪。 | Mine | — |
| [design-tools-index](https://github.com/Ezra-Y/design-tools-index) | 按用途分类的设计工具索引（动画/配色/原型/handoff/design-to-code…）——30+ 类。 | Mine | — |
| [awesome-design-html](https://github.com/yzfly/awesome-design-html) | 115 品牌主题 HTML 设计（作 Claude skill）——93 web + 22 模板，用于灵感/起步。 | Community | ⭐125 |

### 4. React / 前端工程

| Skill | 说明 | 来源 | 星数 |
|---|---|---|---|
| [react-best-practices](https://github.com/anthropics/skills) | React 和 Next.js 性能优化指南（来自 Vercel 工程）。提速与可维护的模式。 | Official | — |
| [react-view-transitions](https://github.com/anthropics/skills) | 用 React View Transitions API 做顺滑、原生感的动画。共享元素与页面转场。 | Official | — |
| [composition-patterns](https://github.com/anthropics/skills) | 可扩展的 React 组合模式——复合组件、render props、context，避免布尔 prop 泛滥。 | Official | — |
| [react-native-skills](https://github.com/anthropics/skills) | React Native + Expo 最佳实践，做高性能移动应用。构建、优化、发布跨平台。 | Official | — |
| [claude-webdev](https://github.com/alpham8/claude-webdev) | 面向 web 开发的 Claude Code 精选配置——内置 40+ skill（Shopware/React 等）。有主见的起步套件。 | Community | ⭐4 |

### 5. 设计分析 / 集成

| Skill | 说明 | 来源 | 星数 |
|---|---|---|---|
| [taste-skill](https://github.com/senlindesign/taste-skill) | 从 URL 逆向任意网站的设计品味。抓取 DOM+截图，产出 token 和品味 DNA（决策背后的 why）。 | Community | ⭐240 |
| [claude2figma](https://github.com/senlindesign/claude2figma) | Claude + Figma 强制层——组件规则、预检、样式绑定、参考解读。保持 Figma 产出一致。 | Community | ⭐178 |
| [brand](https://github.com/anthropics/skills) | 品牌声音、视觉识别、信息框架、资产管理、品牌一致性。构建/维护品牌体系。 | Official | — |
| [webdesign-agency-skills](https://github.com/peterhadorn/webdesign-agency-skills) | 审计任意网站产出客户级销售简报，或做定向设计评审。代理机构级工作流。 | Community | ⭐30 |

### 6. 移动端 UI（iOS / SwiftUI）

| Skill | 说明 | 来源 | 星数 |
|---|---|---|---|
| [swiftui-design-skill](https://github.com/Wholiver/swiftui-design-skill) | SwiftUI 前端视觉设计——6 条抗 AI-slop 规则、Apple 原生字体、5 维设计审查。有辨识度的 iOS/macOS 界面。 | Community | ⭐146 |
| [SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill) | Paul Hudson 的 SwiftUI agent skill。帮 AI 写更聪明的现代 SwiftUI——API、设计、性能、可访问性、导航。 | Community | ⭐4333 |
| [apple-skills](https://github.com/vabole/apple-skills) | Apple 开发 skill 合集——HIG、ios-design-consultant、ui-craft、swiftui/动画，加框架（StoreKit/HealthKit 等）。 | Community | ⭐285 |
| [ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill) | iOS 模拟器自动化——构建/测试脚本、可访问性导航、屏幕映射、手势、视觉 diff、app 生命周期。 | Community | ⭐1160 |
| [ios-motion-patterns-index](https://github.com/Ezra-Y/ios-motion-patterns-index) | 按分类的 iOS 动画可跑代码索引（菜单/转场/指示器/弹窗/动画/UI），来自 MotionBook。 | Mine | — |

---

## 来源 / 致谢

条目来自本地已安装 skill 与经 GitHub 搜索发现的社区 skill。更多 awesome 列表见 [sindresorhus/awesome](https://github.com/sindresorhus/awesome) 与 [helloianneo/awesome-claude-code-skills](https://github.com/helloianneo/awesome-claude-code-skills)。如果某个 skill 对你有用，请给原仓库点 star。

## 许可证

[MIT](LICENSE) © 2026 Ezra-Y
