# -*- coding: utf-8 -*-
"""内容库：主题驱动的知识点生成。
每个主题生成一个知识点（一张卡片），定义/定理/推导/例题/应用/注记/背景/拓展
作为模态框内的分区集中展示。只有真实内容的分区才会出现，不生成填充文本。
"""

def make_item(id, name, tags, brief, body, fig="", figCap=""):
    return {"id": id, "name": name, "tags": tags, "brief": brief, "body": body,
            "fig": fig, "figCap": figCap}

# ---------- 小型 HTML 构造助手 ----------
def p(t): return f"<p>{t}</p>"
def h5(t): return f"<h5>{t}</h5>"
def fml(eq): return f'<div class="la-fml">$${eq}$$</div>'
def fml_inline(eq): return f"\\({eq}\\)"
def bold(t): return f"<strong>{t}</strong>"
def ul(items): return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
def sec(cls, title, content):
    """生成一个分区，仅当 content 非空时"""
    if not content: return ""
    return f'<section class="la-kp-sec la-kp-{cls}"><h5>{title}</h5>{content}</section>'

# ---------- 主题 -> 单一知识点 ----------
def build_kp(prefix, idx, name, formula="", explain="", deriv="",
             ex="", app="", note="", hist="", ext="", fig="", figCap=""):
    """将一个主题构建为一个知识点 item。
    只有提供了真实内容的分区才会出现在 body 中。
    """
    parts = []

    # 定义 —— 只放文字说明，避免与公式重复
    parts.append(sec("def", "定 义", p(explain) if explain else ""))

    # 定理 / 公式（独立分区，突出公式本身）
    if formula:
        parts.append(sec("thm", "定理 · 公式", fml(formula)))

    # 推导
    parts.append(sec("der", "推 导", p(deriv) if deriv else ""))

    # 例题
    parts.append(sec("ex", "例 题", p(ex) if ex else ""))

    # 应用
    parts.append(sec("app", "应 用", p(app) if app else ""))

    # 注记
    parts.append(sec("note", "注 记", p(note) if note else ""))

    # 背景
    parts.append(sec("his", "背 景", p(hist) if hist else ""))

    # 拓展
    parts.append(sec("ext", "拓 展", p(ext) if ext else ""))

    body = f'<div class="la-kp">{"".join(parts)}</div>'

    # brief：取 explain 的前若干字作为卡片简介
    brief = explain[:60] + ("…" if len(explain) > 60 else "") if explain else (formula or name)

    tags = []
    if explain: tags.append("def")
    if formula: tags.append("thm")
    if deriv: tags.append("der")
    if app: tags.append("app")
    if note: tags.append("note")

    return make_item(f"{prefix}-{idx}", name, tags, brief, body, fig=fig, figCap=figCap)


def build_section(prefix, sname, color, desc, topics):
    """topics: list of dicts with keys name, formula, explain, deriv, ex, app, note, hist, ext, fig, figCap"""
    items = []
    for i, t in enumerate(topics, 1):
        items.append(build_kp(prefix, i, t["name"],
            formula=t.get("formula",""), explain=t.get("explain",""),
            deriv=t.get("deriv",""), ex=t.get("ex",""), app=t.get("app",""),
            note=t.get("note",""), hist=t.get("hist",""), ext=t.get("ext",""),
            fig=t.get("fig",""), figCap=t.get("figCap","")))
    return {"name": sname, "color": color, "desc": desc, "items": items}

def build_chapter(cid, num, title, en, sub, desc, sections):
    return {"id": cid, "num": num, "title": title, "en": en, "sub": sub, "desc": desc, "sections": sections}

# 紧凑主题构造
def T(name, formula="", explain="", deriv="", ex="", app="", note="", hist="", ext="", fig="", figCap=""):
    return {"name": name, "formula": formula, "explain": explain,
            "deriv": deriv, "ex": ex, "app": app, "note": note,
            "hist": hist, "ext": ext, "fig": fig, "figCap": figCap}

print("content_bank v3 loaded (grouped, quality-only)")
