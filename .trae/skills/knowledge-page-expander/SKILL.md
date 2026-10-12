---
name: "knowledge-page-expander"
description: "Expand or rewrite physics/math knowledge-map pages (gen_*.py -> *.html) with knowledg点扩写、严谨推导、SVG配图、MathJax公式. Invoke when user asks to 扩充/重写/补充 the content of a subject page like 光学/电磁学/力学."
---

# Knowledge Page Expander

批量扩充或重写 `gen_*.py` 生成器中的知识点，产出高质量知识体系页面（`*.html`），并完成验证与推送。

## 适用场景（触发条件）

- 用户说"扩充 X 的知识点"、"把 X 网页做得和 Y 一样多"、"重写 X 的内容"
- 目标学科已有 `gen_<subject>.py` 生成器与 `<subject>.html` 产物
- 仓库为 `/workspace`（静态站点 illudew.github.io）

## 架构总览

每个学科页面由 Python 生成器驱动：

```
gen_<subject>.py
  ├── FIG = { "fig_key": "<svg ...>...</svg>" }     # SVG 配图字典
  ├── TAG_LABEL = {...}                              # 标签中文名
  ├── CORE_FORMULAS = [("名称","LaTeX","说明"), ...] # 核心公式速查
  ├── defn/thm/der/exa/app/note/wrap               # HTML 块辅助函数
  ├── chX_sections = [ {name,color,desc,items:[...]}, ... ]
  ├── CHAPTERS = [ {id,num,title,en,desc,sections:chX_sections}, ... ]
  └── gen_html()  # 拼装完整 HTML（含 MathJax 配置、CSS、JS 渲染逻辑）
```

产物 `<subject>.html` 通过 `python gen_<subject>.py` 生成（非手写 HTML）。

## 执行流程（六步）

### 第 1 步：侦察现状

```bash
cd /workspace && ls gen_*.py                    # 定位生成器
# 统计知识点数量与文件体积（对齐基准）
for f in theoretical-mechanics <subject>; do
  items=$(grep -oE "id:'[a-z]+[0-9]+s[0-9]+-[0-9]+'" "$f.html" | wc -l)
  echo "$f: items=$items, size=$(wc -c < "$f.html")"
done
```

读取生成器，确认：章节列表、现有 section 编号、`wrap()` 调用风格、颜色方案、`CORE_FORMULAS` 结尾位置、`FIG` 字典键名。

### 第 2 步：逐个扩充（并行 Agent 加速）

多学科同时扩充时，用 `Task`(general_purpose_task) 并行派发，每个 Agent 负责一个生成器。派发提示词必须包含：

- 辅助函数签名与语义：`p(text)`、`fml(latex, note="")`、`defn(t,body)`、`thm(t,body)`、`der(body)`、`exa(body)`、`app(body)`、`note(body)`、`wrap(body)`，块间用 `+` 连接
- Item 精确结构：

```python
{"id":"xXsY-Z","name":"名称","tags":["def"],"brief":"一句话简介",
 "fig":"可选FIG键","figCap":"图注",
 "body": wrap(
   defn("标题", p("说明") + fml("LaTeX")) +
   der( p("推导步骤一") + fml("公式一") + p("推导步骤二") + fml("公式二") ) +
   note(p("备注"))
 )},
```

- id 命名规则：`<学科首字母><章号>s<节号>-<序号>`（如 `e1s2-3`）
- Section 结构：`{"name":"1.6 小节名","color":"#2563eb","desc":"...","items":[...]}`
- 每章颜色梯度（如 Ch1 蓝 `#2563eb/#0ea5e9`、Ch2 青绿 `#0d9488/#14b8a6`…）
- 新增 section 必须插入到对应 `chX_sections` 列表的 `]` 之前
- `CORE_FORMULAS` 追加元组 `("名称","LaTeX","说明")`
- **硬性要求**：每个知识点必须含 `der` 推导块；LaTeX 必须准确
- **验证指令**：`python3 -c "import ast; ast.parse(open('gen_X.py').read()); print('PARSE OK')"` 通过后才 `python gen_X.py`

### 第 3 步：语法与产物校验

```bash
cd /workspace
for gen in gen_calc gen_linalg gen_mechanics gen_electromagnetism gen_electrodynamics; do
  echo -n "$gen: "; python3 -c "import ast; ast.parse(open('$gen.py').read()); print('PARSE OK')"
done
python gen_<subject>.py     # 确认 "Total items: N" 与生成字符数
```

### 第 4 步：浏览器验证（必须）

```bash
python3 -m http.server 8767   # non-blocking, web_server 类型
```

用 `browser_use` agent 打开 `http://localhost:8767/<subject>.html`，验证：
1. 页面正常加载、标题正确
2. 章节导航标签齐全
3. 随机点击 2-3 个知识点卡片 → 模态框弹出、LaTeX 无乱码、SVG 图显示
4. 底部「核心公式速查」区域完整

> 每轮 browser_use 最多验证 2-3 个 URL，超出需拆分调用。

### 第 5 步：提交推送

```bash
cd /workspace
git add gen_<subject>.py <subject>.html
git commit -m "feat: expand <subject> knowledge points with derivations and figures"
git push origin main
```

> 若推送要求认证：`git config credential.helper 'store --file=/run/shared/git/credentials'` 后 `git push origin main`。

## 内容质量红线

| 项 | 要求 |
|----|------|
| 推导 | 每个知识点至少一个 `der` 块，且分步（多段 `p()` + `fml()` 交替） |
| 公式 | LaTeX 语法正确，反斜杠在 Python 字符串中写 `\\`（如 `\\frac`、`\\nabla`） |
| 配图 | SVG 用 `viewBox="0 0 240 160"`，配色与所属章节一致，含关键标注文字 |
| 体积 | 目标与基准页持平（理论力学 ≈175KB / 74 项） |
| 章节 | "节"编号连续（1.5、1.6…），不得跳号或重复 |

## 常见坑（必须规避）

1. **括号不匹配**：`wrap(defn("a",p("b")+fml("c"))+thm(...))` 每个 `(` 都要有 `)`。写一小段就 `ast.parse` 校验一次，出错立即定位修复，不要攒到最后。
2. **中文字符串里的 ASCII 双引号**：会截断 Python 字符串导致语法错误，改用中文直角引号「」或 `\\text{...}`。
3. **`js_escape` 转义**：body 中的反斜杠经 `js_escape` 处理，Python 源码里写 `\\`，生成 JS 里是 `\\\\`，渲染后 MathJax 收到 `\`，属正常链路，不要手动"修正"。
4. **Edit 的 old_string 唯一性**：HTML/Python 中追加块时，锚点要带上层容器或唯一内容；纯 `</div>`、`]` 这类片段会命中多处以致失败。
5. **不要手改产物 HTML**：一切改生成器再重跑，避免下次生成被覆盖。
6. **验证口径**：浏览器 agent 报告 BLOCKED/截断时，不得宣称"已验证"。补一轮验证或如实说明未覆盖项。
7. **LaTeX 里的 `<` 会被当作 HTML 标签**：`$a<b$` 中的 `<b` 会被 `innerHTML` 解析为标签起始，吞掉后续整段内容（卡片打开后文字缺失）。生成器已在 `gen_html()` 中对每个知识点 body 调用 `fix_lt_math()` 把数学区间的 `<` 转义为 `&lt;`；新增或改写内容时保留该调用即可，勿在 `<` 后直接跟字母。
8. **浏览器验证需绕过缓存**：重新生成 HTML 后用 `?nocache=1` 之类的查询串导航，否则 browser_use 可能命中缓存而给出旧结果。

## 基准参照

`theoretical-mechanics.html`（175KB，3 章 74 项）为内容量基准；重写新学科时章节数按知识体系自然划分，不必强凑。