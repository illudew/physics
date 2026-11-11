# -*- coding: utf-8 -*-
"""量子计算 / 量子信息 内容构造助手。"""


def _esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def q(name, formula="", explain="", deriv="", app="", note="", hist="", ext=""):
    parts = [f'"{_esc(name)}"']
    for key, val in (("formula", formula), ("explain", explain), ("deriv", deriv),
                     ("app", app), ("note", note), ("hist", hist), ("ext", ext)):
        if val:
            parts.append(f'{key}="{_esc(val)}"')
    return "T(" + ", ".join(parts) + ")"


def S(name, color, topics):
    return {"name": name, "color": color, "topics": topics}


def C(ch, title, en, sub, sections):
    return {"ch": ch, "title": title, "en": en, "sub": sub, "sections": sections}
