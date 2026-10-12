# Code Wiki · 物理学知识体系（illudew.github.io）

> 本项目是一套**纯前端静态网站**，用于可视化展示物理学知识学习路线图与专题知识体系。
> 无构建工具、无框架、无后端依赖，所有页面为单文件 HTML，可直接托管于 GitHub Pages。

---

## 目录

1. [项目概览](#1-项目概览)
2. [文件结构与模块职责](#2-文件结构与模块职责)
3. [整体架构](#3-整体架构)
4. [核心数据结构](#4-核心数据结构)
5. [关键函数说明](#5-关键函数说明)
6. [依赖关系](#6-依赖关系)
7. [项目运行方式](#7-项目运行方式)
8. [扩展指南](#8-扩展指南)

---

## 1. 项目概览

| 项目属性 | 说明 |
| --- | --- |
| 仓库名 | `illudew.github.io` |
| 站点类型 | 单文件静态 HTML 网站（GitHub Pages） |
| 技术栈 | 原生 HTML5 + CSS3 + 原生 JavaScript（ES2015+） |
| 核心依赖 | [MathJax 3](https://www.mathjax.org/)（CDN 加载，用于 LaTeX 公式渲染） |
| 构建工具 | 无 |
| 后端 | 无 |
| 数据持久化 | 浏览器 `localStorage` / `sessionStorage`（浏览量、点赞） |
| 语言 | 中文（zh-CN） |

项目分为两个层级：

- **总览层**（[index.html](file:///workspace/index.html)）：物理学全学科路线图，包含 64 门课程、Arcaea 风格难度评级、前置/后续学科依赖图、推荐教材与 B 站网课链接。
- **专题层**（4 个独立 HTML 页面）：针对某一门课程展开详细的知识点体系，包含定义、定理、推导、公式、SVG 示意图。

---

## 2. 文件结构与模块职责

```
/workspace
├── README.md                     # 仓库说明（仅含仓库名）
├── index.html                    # 主路线图（总览层，658 行）
├── linear-algebra.html           # 线性代数 · 知识体系（1102 行）
├── newtonian-mechanics.html      # 牛顿力学 · 知识体系（1459 行）
├── engineering-optics.html       # 工程光学 · 知识体系（1922 行）
└── quantum-information.html      # 量子信息 · 知识体系（1698 行）
```

### 各文件职责

| 文件 | 职责 | 知识点数 | 章节数 | 命名前缀 |
| --- | --- | --- | --- | --- |
| [index.html](file:///workspace/index.html) | 物理学全学科路线图总览，课程卡片与详情弹窗 | 64 门课程 | 6 大阶段 | 无前缀 / `phys_` |
| [linear-algebra.html](file:///workspace/linear-algebra.html) | 线性代数专题知识体系 | 58 | 5 | `la-` |
| [newtonian-mechanics.html](file:///workspace/newtonian-mechanics.html) | 牛顿力学专题知识体系 | 86 | 6 | `nm-` |
| [engineering-optics.html](file:///workspace/engineering-optics.html) | 工程光学（映像光学）专题知识体系 | 113 | 6 | `la-` |
| [quantum-information.html](file:///workspace/quantum-information.html) | 量子信息专题知识体系 | 92 | 6 | `la-` |

> **命名约定**：`linear-algebra`、`engineering-optics`、`quantum-information` 三个专题页面复用同一套 `la-` 前缀（CSS 类名、JS 变量名 `LA_*`、函数名 `la*`）；`newtonian-mechanics` 页面使用独立的 `nm-` 前缀和 `NM_*` 变量。所有专题页面的结构和逻辑高度一致。

### index.html 引用的专题页

`COURSES` 数据中共引用了 64 个 `knowledgeLink` 目标页，其中**当前仓库已实现**的有 4 个（上表中除 index 外的四个文件），其余 60 个为预留链接（点击会 404），属于待扩展内容。

---

## 3. 整体架构

### 3.1 页面分层架构

```
┌─────────────────────────────────────────────────────────┐
│                    index.html（总览层）                    │
│  6 大学习阶段 → 学科领域 → 课程卡片 → 详情弹窗             │
│  课程数据：COURSES（64 门）                                │
│  交互：浏览量 / 点赞 / 前置后续依赖 / 教材 / 网课            │
└──────────────┬──────────────────┬───────────────────────┘
               │ knowledgeLink    │
               ▼                  ▼
┌──────────────────────┐  ┌──────────────────────────┐
│  专题知识层（4 页）    │  │  外部资源                 │
│  章节 → 节 → 知识点    │  │  Z-Library（教材搜索）     │
│  详情弹窗：公式+SVG    │  │  Bilibili（网课搜索）      │
│  MathJax 公式渲染      │  │  jsDelivr CDN（MathJax）  │
└──────────────────────┘  └──────────────────────────┘
```

### 3.2 单文件页面内部结构

每个专题页面（及 index）均为**单文件 HTML**，内部结构统一：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta .../>
  <title>...</title>
  <script>window.MathJax = {...}</script>          <!-- MathJax 配置 -->
  <script src="...mathjax..."></script>             <!-- MathJax CDN -->
  <style>...</style>                                <!-- 全部内联 CSS -->
</head>
<body>
  <div class="wrap">                                <!-- 页面骨架 -->
    <header>...</header>
    <main class="roadmap" id="roadmap"></main>      <!-- JS 动态渲染 -->
    <footer>...</footer>
  </div>
  <div class="overlay" id="overlay">                <!-- 详情弹窗 -->
    <div class="modal">...</div>
  </div>
  <script>
    const FIG = {...};                              // SVG 图库
    const TAG_LABEL = {...};                        // 标签映射
    const DATA = [...];                             // 核心数据
    const KP = {};                                  // 知识点索引
    function buildCard(){...}                       // 卡片构建
    function render(){...}                          // 主渲染
    function showItem(){...}                        // 弹窗详情
    ...
  </script>
</body>
</html>
```

### 3.3 数据驱动渲染模式

所有页面采用**数据驱动**（Data-Driven）渲染：

1. 静态 HTML 仅提供空容器（`<main id="roadmap">`）和弹窗骨架。
2. JavaScript 在 `DOMContentLoaded` 时遍历数据数组，拼接 HTML 字符串注入容器。
3. 卡片点击事件通过内联 `onclick="showItem(id)"` 绑定，弹窗通过 `id` 查找对应知识点数据。

这种模式的优点是**页面内容与结构完全由数据控制**，新增知识点只需往 `DATA` 数组追加对象，无需改动 HTML 骨架。

---

## 4. 核心数据结构

### 4.1 index.html — `COURSES` 对象

`COURSES` 是一个以课程名（中文）为键的字典，共 **64 门课程**。每个课程值对象包含以下字段：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `desc` | `string` | 课程详细描述（支持 `\n` 换行） |
| `arc` | `string[]` | Arcaea 风格难度数组，元素如 `'PST 1'`、`'FTR 9+'`、`'INS 12'` |
| `quote` | `string` | 一句话金句/吐槽，弹窗中高亮展示 |
| `prereq` | `string[]` | 前置学科名称数组（用于依赖图） |
| `next` | `string[]` | 后续学科名称数组 |
| `books` | `string[]` | 推荐教材列表（生成 Z-Library 搜索链接） |
| `videos` | `{name, keyword}[]` | B 站网课推荐（生成搜索链接） |
| `knowledgeLink` | `string` | 专题知识页面的相对 URL |

**难度等级（arc）体系**（仿音乐游戏 Arcaea）：

| 缩写 | 全称 | 含义 | 数值范围 |
| --- | --- | --- | --- |
| `PST` | Past | 过去 / 入门 | 1–7 |
| `PRS` | Present | 现在 / 进阶 | 2–9+ |
| `FTR` | Future | 未来 / 高阶 | 3–11+ |
| `ETR` | Eternal | 永恒 / 专家 | 9–11 |
| `BYD` | Beyond | 超越 / 极难 | 10–11+ |
| `INS` | Insane | 疯狂 / 终极 | 12–12+ |

**示例**：

```js
'量子力学':{
  desc:'物理学的尽头，或许不是？\n\n这是微观世界的全新理论体系……',
  arc:['PST 6','PRS 8','FTR 10','BYD 11'],
  quote:'遇事不决，量子力学。',
  prereq:['理论力学','数学物理方法','原子物理学','线性代数','群论'],
  next:['固体物理','量子信息','量子计算','原子核物理','粒子物理','规范场论'],
  books:['周世勋《量子力学教程》','曾谨言《量子力学》','Griffiths《量子力学概论》'],
  videos:[{name:'北京大学《量子力学》田光善',keyword:'田光善量子力学'}],
  knowledgeLink:'quantum-mechanics.html'
}
```

### 4.2 专题页 — `LA_DATA` / `NM_DATA` 数组

专题页面的核心数据是一个**三级嵌套数组**：`章节 → 节 → 知识点`。

```
DATA = [ Chapter, Chapter, ... ]
         │
         ├── id, num, title, en, sub, desc
         └── sections: [ Section, Section, ... ]
                          │
                          ├── name, color, desc
                          └── items: [ Item, Item, ... ]
```

#### Chapter（章节）对象

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | `string` | 章节唯一 ID，如 `'la-ch1'`、`'nm-ch2'` |
| `num` | `string` | 章节序号，如 `'第一章'` |
| `title` | `string` | 章节标题 |
| `en` | `string` | 英文标题（大写） |
| `sub` | `string` | 章节副标题 |
| `desc` | `string` | 章节描述 |
| `sections` | `Section[]` | 该章节下的所有节 |

#### Section（节）对象

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `name` | `string` | 节名，如 `'1.1 线性空间与子空间'` |
| `color` | `string` | 该节左侧色条颜色（十六进制） |
| `desc` | `string` | 节描述 |
| `items` | `Item[]` | 该节下的知识点 |

#### Item（知识点）对象

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `id` | `string` | 知识点唯一 ID，如 `'la-k1-1'` |
| `name` | `string` | 知识点名称 |
| `tags` | `string[]` | 知识类型标签，从 `TAG_LABEL` 键中选取 |
| `brief` | `string` | 一句话简介（卡片上展示） |
| `fig` | `string`（可选） | 对应 `LA_FIG`/`FIG` 中的 SVG 图键名 |
| `figCap` | `string`（可选） | 图注（支持 LaTeX） |
| `body` | `string` | 知识点详细正文（HTML 字符串，含 LaTeX） |

### 4.3 `LA_TAG_LABEL` / `NM_TAG_LABEL` 标签映射

知识点类型标签，用于在卡片和弹窗上显示彩色徽章。

**通用型**（`linear-algebra` / `engineering-optics` / `quantum-information`）：

```js
const LA_TAG_LABEL = {
  def:'定 义',   // definition
  thm:'定 理',   // theorem
  der:'推 导',   // derivation
  exa:'例 子',   // example
  app:'应 用',   // application
  his:'注 记'    // historical note
};
```

**力学型**（`newtonian-mechanics`）：

```js
const NM_TAG_LABEL = {
  def:'定 义',   // definition
  law:'定 律',   // physical law
  der:'推 导',   // derivation
  mod:'模 型',   // model
  exp:'实 验',   // experiment
  his:'历 史'    // history
};
```

### 4.4 `LA_FIG` / `FIG` SVG 图库

一个以键名索引的 SVG 字符串字典，值为完整的 `<svg>...</svg>` 字符串。知识点通过 `fig` 字段引用对应键名，渲染时插入弹窗正文顶部。

- 图库集中定义，可被多个知识点复用。
- SVG 内部使用自包含的 `<defs>`、`<marker>` 等，不依赖外部资源。
- 图注 `figCap` 支持 LaTeX，由 MathJax 渲染。

### 4.5 `LA_KP` / `NM_KP` 知识点索引

渲染时动态生成的扁平字典，以知识点 `id` 为键：

```js
LA_KP[item.id] = {
  item: item,              // 原始知识点对象
  section: sec.name,       // 所属节名
  chapter: `${ch.num} · ${ch.title}`  // 所属章节
};
```

该索引用于弹窗中显示面包屑（章节 ／ 节），避免点击时重新遍历整个数据树。

---

## 5. 关键函数说明

### 5.1 index.html 函数

| 函数 | 位置 | 说明 |
| --- | --- | --- |
| `zlibBookUrl(n)` | [index.html:571](file:///workspace/index.html#L571) | 将教材名转为 Z-Library 搜索 URL：`https://z-library.biz/s/<encodeURIComponent(name)>` |
| `biliSearchUrl(k)` | [index.html:572](file:///workspace/index.html#L572) | 将关键词转为 B 站搜索 URL：`https://search.bilibili.com/all?keyword=<keyword>` |
| `showCourse(name)` | [index.html:574-636](file:///workspace/index.html#L574-L636) | 核心交互函数：根据课程名查 `COURSES`，填充弹窗（标题、描述、金句、难度徽章、专题页链接、前置/后续学科、教材列表、网课列表）并显示 |
| `hideInfo()` | [index.html:637](file:///workspace/index.html#L637) | 移除弹窗 `show` 类，关闭弹窗 |
| `closeInfo(e)` | [index.html:638](file:///workspace/index.html#L638) | 点击遮罩层时关闭弹窗（仅当点击目标为 `overlay` 本身） |
| `initViewCount()` | [index.html:641-643](file:///workspace/index.html#L641-L643) | 初始化浏览量：每会话 +1，存 `localStorage('phys_views')`，会话标记存 `sessionStorage` |
| `initLikes()` | [index.html:644-647](file:///workspace/index.html#L644-L647) | 初始化点赞数与点赞状态（`localStorage('phys_likes')` / `'phys_liked'`） |
| `toggleLike()` | [index.html:648-653](file:///workspace/index.html#L648-L653) | 点赞/取消点赞切换，更新计数与按钮样式 |

**`showCourse` 流程**：

```
COURSES[name]
  ├─ 填充 modalTitle / modalText
  ├─ 显示/隐藏 quote
  ├─ 渲染 arc 难度徽章（arcDiffRow）
  ├─ 渲染 knowledgeLink 专题页按钮（knowledgeLinkBox）
  ├─ 渲染 prereq 前置学科 chips（可点击跳转 showCourse）
  ├─ 渲染 next 后续学科 chips（可点击跳转 showCourse）
  ├─ 渲染 books 教材链接 → zlibBookUrl
  ├─ 渲染 videos 网课链接 → biliSearchUrl
  └─ overlay.classList.add('show')
```

### 5.2 专题页函数（以 `la-` 前缀为例）

| 函数 | 说明 |
| --- | --- |
| `laBuildCard(item)` | 构建单个知识点卡片 HTML：标签徽章 + 名称 + 简介，绑定 `onclick="showLaItem(id)"` |
| `renderLa()` | 主渲染函数：遍历 `LA_DATA` 生成章节标题、节、卡片网格，填充 `#laRoadmap`；同时构建 `LA_KP` 索引；统计知识点数与公式块数（`$$` 出现次数 / 2） |
| `showLaItem(id)` | 弹窗详情：查 `LA_KP`，填充面包屑、标题、标签、正文（前置 SVG 图 + body HTML），调用 MathJax 重新排版 |
| `hideLaInfo()` | 关闭弹窗 |
| `closeLaInfo(e)` | 点击遮罩关闭 |
| `expandAllLa()` | 占位函数，提示用户点击卡片查看 |

**`renderLa` 统计逻辑**：

```js
const kCount = Object.keys(LA_KP).length;              // 知识点总数
const fCount = (root.innerHTML.match(/\$\$/g) || []).length;
document.getElementById('laKCount').textContent = kCount;
document.getElementById('laFCount').textContent = Math.round(fCount / 2);  // $$ 成对出现
```

**`showLaItem` MathJax 重排版**：

```js
if (window.MathJax && window.MathJax.typesetPromise) {
  window.MathJax.typesetPromise([document.getElementById('laBody')]).catch(()=>{});
}
```

> `newtonian-mechanics.html` 对应函数为 `nmBuildCard` / `renderNewton` / `showNmItem` / `hideNmInfo` / `closeNmInfo`，逻辑完全一致，仅前缀与变量名不同（`NM_KP`、`FIG`、`NM_TAG_LABEL`、`NM_DATA`）。

### 5.3 键盘与初始化事件

所有页面统一绑定：

```js
document.addEventListener('keydown', e => {
  if(e.key === 'Escape') hideInfo();   // 或 hideLaInfo / hideNmInfo
});

document.addEventListener('DOMContentLoaded', () => {
  renderLa();                          // 或 renderNewton
  MathJax.typesetPromise([document.getElementById('laRoadmap')]).catch(()=>{});
});
```

---

## 6. 依赖关系

### 6.1 外部依赖

| 依赖 | 来源 | 用途 | 加载方式 |
| --- | --- | --- | --- |
| **MathJax 3** | `https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js` | LaTeX 数学公式渲染（行内 `$...$`、块级 `$$...$$`） | CDN `<script>` 异步加载 |
| **Z-Library** | `https://z-library.biz/s/` | 教材搜索外链 | 运行时拼接 URL |
| **Bilibili 搜索** | `https://search.bilibili.com/all?keyword=` | 网课搜索外链 | 运行时拼接 URL |

> MathJax 配置通过 `window.MathJax` 全局对象在加载脚本前定义，启用 `ams`、`boldsymbol` 扩展包（`quantum-information` 额外启用 `physics` 包）。

### 6.2 内部页面跳转关系

```
index.html
  ├── (课程卡片) → knowledgeLink → 专题页面
  │     ├── linear-algebra.html
  │     ├── newtonian-mechanics.html
  │     ├── engineering-optics.html
  │     └── quantum-information.html
  └── 前置/后续学科 chips → showCourse(name)（同页弹窗跳转）

专题页面 → 返回总览按钮 → index.html
```

### 6.3 课程依赖关系（节选）

`COURSES.prereq` 与 `next` 字段构成学科依赖图。以下为核心链路：

```
初等数学 → 微积分 → 数学物理方法 → 电动力学
         → 线性代数 → 群论 → 量子力学 → 固体物理 → 半导体物理
                                   ↘ 量子信息 / 量子计算
微积分 → 力学 → 理论力学 → 量子力学 / 相对论
电磁学 → 电动力学 → 相对论 / 粒子物理 → 规范场论 → 量子场论 → 弦理论 / 量子引力
固体物理 → 超导物理 / 拓扑物态 → 拓扑量子场论
```

---

## 7. 项目运行方式

### 7.1 本地预览

由于项目为纯静态 HTML，无需安装任何依赖。任意方式打开 `index.html` 即可：

**方式一：直接双击打开**

```
在文件管理器中双击 index.html
```

> 注意：直接 `file://` 打开时，MathJax CDN 仍可正常加载，但某些浏览器可能对 `localStorage` 有安全限制。

**方式二：本地静态服务器（推荐）**

```bash
# Python 3
cd /workspace && python3 -m http.server 8000

# Node.js
npx serve /workspace

# PHP
php -S localhost:8000
```

然后浏览器访问 `http://localhost:8000/index.html`。

### 7.2 部署到 GitHub Pages

1. 将仓库推送到 GitHub，仓库名需为 `<username>.github.io` 或开启仓库的 Pages 功能。
2. Pages 源选择 `main` 分支根目录。
3. 访问 `https://<username>.github.io/` 即可看到 `index.html`。

> 本仓库 `index.html` 的 `<footer>` 已注明"适用于 GitHub Pages"。

### 7.3 浏览器兼容性

- 使用 CSS 变量（`--bg`、`--card` 等），需现代浏览器（Chrome 49+、Firefox 31+、Safari 9.1+）。
- `backdrop-filter` 仅在部分页面使用，不支持时自动降级。
- MathJax 3 支持所有现代浏览器。
- 响应式断点：`@media(max-width:900px)`。

---

## 8. 扩展指南

### 8.1 在 index.html 中新增课程

在 `COURSES` 对象中追加一个键值对：

```js
'新课程名':{
  desc:'课程描述……',
  arc:['PST 3','PRS 5','FTR 7'],
  quote:'一句话金句。',
  prereq:['前置课程1'],
  next:['后续课程1'],
  books:['教材名《书名》'],
  videos:[{name:'网课名',keyword:'搜索关键词'}],
  knowledgeLink:'new-topic.html'   // 若无专题页可省略该字段
}
```

### 8.2 新增专题知识页面

1. 复制 `linear-algebra.html` 或 `newtonian-mechanics.html` 作为模板。
2. 修改 `<title>`、页面 `<h1>`、`footer` 文案。
3. 替换 `LA_DATA`（或 `NM_DATA`）数组内容为新学科的章节/节/知识点。
4. 按需在 `LA_FIG`（或 `FIG`）中添加 SVG 图。
5. 在 `index.html` 的对应课程 `knowledgeLink` 中填入新文件名。
6. 若使用 `nm-` 前缀，注意所有类名与变量名需保持一致（`nm-`、`NM_`、`nm*`）。

### 8.3 新增知识点（在专题页内）

在目标章节的 `sections[i].items` 数组中追加：

```js
{
  id:'la-kX-N',
  name:'知识点名称',
  tags:['def','thm'],
  brief:'一句话简介（卡片显示）',
  fig:'figKeyName',          // 可选，需在 LA_FIG 中定义
  figCap:'图注（支持 $LaTeX$）',
  body:`<p>详细正文，支持 <strong>HTML</strong> 与 $LaTeX$ 公式。</p>
<div class="la-fml">$$ E = mc^2 $$</div>`
}
```

### 8.4 自定义标签类型

修改 `LA_TAG_LABEL`（或 `NM_TAG_LABEL`）添加新类型，并在 CSS 中添加对应颜色类：

```js
const LA_TAG_LABEL = {..., newtype:'新标签'};
```

```css
.la-arc-newtype{ background:#颜色; color:#文字色; }
```

### 8.5 注意事项

- **MathJax 转义**：JS 字符串中的 LaTeX 反斜杠需双写，如 `\\frac`、`\\boldsymbol`。
- **公式计数**：渲染函数通过统计 `$$` 出现次数除以 2 估算公式块数，新增公式会自动更新页头统计。
- **SVG 复用**：`LA_FIG` 中的 SVG 应自包含（`<defs>` 内的 `id` 需在图内唯一），避免跨图 ID 冲突。
- **单文件约束**：所有 CSS、JS、数据均内联于单个 HTML，无外部本地资源依赖，便于直接部署。
