# -*- coding: utf-8 -*-
"""Generate engineering-optics.html with 6 chapters:
几何光学基础 / 理想光学系统 / 平面镜棱镜系统 / 光束限制与光阑 / 像差理论 / 典型光学系统."""
import json

FIG = {
"fermat": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="120" x2="220" y2="120" stroke="#475569" stroke-width="2"/>
<text x="186" y="140" font-size="11" fill="#475569">界面</text>
<circle cx="45" cy="40" r="4" fill="#2563eb"/><text x="34" y="34" font-size="11" fill="#2563eb">A</text>
<circle cx="195" cy="40" r="4" fill="#2563eb"/><text x="200" y="34" font-size="11" fill="#2563eb">B</text>
<circle cx="120" cy="120" r="4" fill="#ef4444"/><text x="126" y="114" font-size="11" fill="#ef4444">P</text>
<line x1="45" y1="40" x2="120" y2="120" stroke="#2563eb" stroke-width="1.6"/>
<line x1="120" y1="120" x2="195" y2="40" stroke="#2563eb" stroke-width="1.6"/>
<line x1="45" y1="40" x2="195" y2="40" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="4 3"/>
<text x="70" y="84" font-size="10" fill="#2563eb">n1</text>
<text x="152" y="84" font-size="10" fill="#2563eb">n2</text>
<text x="86" y="26" font-size="10" fill="#94a3b8">光程取极值</text></svg>''',
"sphere_mirror": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 150 20 A 80 80 0 0 0 150 140" fill="none" stroke="#2563eb" stroke-width="2.5"/>
<line x1="20" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="4 3"/>
<circle cx="150" cy="80" r="3" fill="#0f172a"/><text x="144" y="72" font-size="10" fill="#0f172a">C</text>
<circle cx="110" cy="80" r="3" fill="#ef4444"/><text x="102" y="72" font-size="10" fill="#ef4444">F</text>
<line x1="40" y1="42" x2="40" y2="80" stroke="#64748b" stroke-width="1.5"/>
<text x="24" y="38" font-size="10" fill="#64748b">物</text>
<line x1="40" y1="42" x2="148" y2="118" stroke="#10b981" stroke-width="1.6"/>
<text x="60" y="152" font-size="10" fill="#94a3b8">球面镜（r=2f）</text></svg>''',
"spherical_refract": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="4 3"/>
<path d="M 130 20 A 70 70 0 0 0 130 140" fill="none" stroke="#2563eb" stroke-width="2.5"/>
<circle cx="130" cy="80" r="3" fill="#0f172a"/><text x="134" y="72" font-size="10" fill="#0f172a">C</text>
<text x="34" y="52" font-size="11" fill="#2563eb">n</text>
<text x="176" y="52" font-size="11" fill="#7c3aed">n'</text>
<line x1="50" y1="80" x2="150" y2="80" stroke="#10b981" stroke-width="1.6"/>
<polygon points="150,80 141,75 141,85" fill="#10b981"/>
<line x1="50" y1="28" x2="50" y2="80" stroke="#64748b" stroke-width="1.5"/>
<text x="20" y="26" font-size="10" fill="#64748b">物</text>
<text x="118" y="152" font-size="10" fill="#94a3b8">单球面折射</text></svg>''',
"principal": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<line x1="100" y1="16" x2="100" y2="144" stroke="#2563eb" stroke-width="1.6"/>
<line x1="140" y1="16" x2="140" y2="144" stroke="#7c3aed" stroke-width="1.6"/>
<text x="62" y="14" font-size="10" fill="#2563eb">H 物方主面</text>
<text x="146" y="14" font-size="10" fill="#7c3aed">H' 像方主面</text>
<line x1="30" y1="50" x2="100" y2="50" stroke="#f59e0b" stroke-width="1.8"/>
<line x1="100" y1="50" x2="140" y2="50" stroke="#f59e0b" stroke-width="1.2" stroke-dasharray="3 3"/>
<line x1="140" y1="50" x2="212" y2="112" stroke="#10b981" stroke-width="1.6"/>
<polygon points="212,112 201,107 205,97" fill="#10b981"/>
<text x="56" y="150" font-size="10" fill="#94a3b8">主平面：β=+1 的共轭面</text></svg>''',
"focal": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<ellipse cx="120" cy="80" rx="12" ry="44" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<circle cx="58" cy="80" r="3" fill="#ef4444"/><text x="50" y="72" font-size="10" fill="#ef4444">F</text>
<circle cx="182" cy="80" r="3" fill="#ef4444"/><text x="186" y="72" font-size="10" fill="#ef4444">F'</text>
<line x1="58" y1="80" x2="120" y2="80" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<line x1="120" y1="80" x2="182" y2="80" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<text x="80" y="98" font-size="10" fill="#94a3b8">f</text>
<text x="146" y="98" font-size="10" fill="#94a3b8">f'</text>
<line x1="18" y1="44" x2="112" y2="44" stroke="#f59e0b" stroke-width="1.5"/>
<line x1="112" y1="44" x2="200" y2="112" stroke="#10b981" stroke-width="1.5"/>
<text x="40" y="36" font-size="10" fill="#f59e0b">平行光</text></svg>''',
"comb_lens": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<ellipse cx="90" cy="80" rx="10" ry="40" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<ellipse cx="150" cy="80" rx="10" ry="40" fill="#fae8ff" stroke="#7c3aed" stroke-width="1.5"/>
<line x1="30" y1="50" x2="90" y2="50" stroke="#f59e0b" stroke-width="1.6"/>
<line x1="90" y1="50" x2="150" y2="96" stroke="#10b981" stroke-width="1.4"/>
<line x1="150" y1="96" x2="208" y2="60" stroke="#10b981" stroke-width="1.4"/>
<line x1="90" y1="126" x2="150" y2="126" stroke="#94a3b8" stroke-width="1"/>
<line x1="90" y1="122" x2="90" y2="130" stroke="#94a3b8" stroke-width="1"/>
<line x1="150" y1="122" x2="150" y2="130" stroke="#94a3b8" stroke-width="1"/>
<text x="104" y="150" font-size="10" fill="#94a3b8">光学间隔 d</text></svg>''',
"mirror_rotate": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="70" y1="132" x2="110" y2="28" stroke="#2563eb" stroke-width="2.5"/>
<line x1="100" y1="132" x2="140" y2="28" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>
<line x1="26" y1="80" x2="100" y2="80" stroke="#ef4444" stroke-width="1.6"/>
<line x1="100" y1="80" x2="204" y2="50" stroke="#10b981" stroke-width="1.6"/>
<line x1="100" y1="80" x2="204" y2="110" stroke="#f59e0b" stroke-width="1.6"/>
<text x="172" y="44" font-size="10" fill="#10b981">原反射</text>
<text x="172" y="122" font-size="10" fill="#f59e0b">转 2θ</text>
<text x="34" y="150" font-size="10" fill="#94a3b8">平面镜转角 θ</text></svg>''',
"right_prism": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<polygon points="70,30 70,130 170,130" fill="#e0f2fe" stroke="#2563eb" stroke-width="2"/>
<line x1="20" y1="80" x2="70" y2="80" stroke="#ef4444" stroke-width="1.6"/>
<line x1="70" y1="80" x2="120" y2="130" stroke="#ef4444" stroke-width="1.6"/>
<line x1="120" y1="130" x2="120" y2="60" stroke="#ef4444" stroke-width="1.6"/>
<line x1="120" y1="60" x2="202" y2="60" stroke="#ef4444" stroke-width="1.6"/>
<polygon points="202,60 193,55 193,65" fill="#ef4444"/>
<text x="52" y="150" font-size="10" fill="#94a3b8">直角棱镜：光线转 90°</text></svg>''',
"dove_prism": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<polygon points="60,38 170,38 150,122 40,122" fill="#fae8ff" stroke="#7c3aed" stroke-width="2"/>
<line x1="18" y1="80" x2="60" y2="80" stroke="#ef4444" stroke-width="1.6"/>
<line x1="60" y1="80" x2="150" y2="80" stroke="#ef4444" stroke-width="1.4" stroke-dasharray="3 3"/>
<line x1="150" y1="80" x2="204" y2="80" stroke="#ef4444" stroke-width="1.6"/>
<polygon points="204,80 195,75 195,85" fill="#ef4444"/>
<text x="42" y="146" font-size="10" fill="#94a3b8">道威棱镜（像倒转）</text></svg>''',
"aperture": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="80" x2="220" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<ellipse cx="90" cy="80" rx="10" ry="42" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<line x1="120" y1="28" x2="120" y2="70" stroke="#0f172a" stroke-width="3"/>
<line x1="120" y1="90" x2="120" y2="132" stroke="#0f172a" stroke-width="3"/>
<text x="96" y="22" font-size="10" fill="#0f172a">孔径光阑</text>
<line x1="40" y1="44" x2="172" y2="30" stroke="#10b981" stroke-width="1.3"/>
<line x1="40" y1="116" x2="172" y2="130" stroke="#10b981" stroke-width="1.3"/>
<text x="46" y="152" font-size="10" fill="#94a3b8">边缘光线限定光束</text></svg>''',
"field_stop": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="80" x2="220" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<rect x="105" y="28" width="6" height="42" fill="#0d9488"/>
<rect x="105" y="90" width="6" height="42" fill="#0d9488"/>
<text x="94" y="22" font-size="10" fill="#0d9488">视场光阑</text>
<line x1="28" y1="80" x2="105" y2="58" stroke="#ef4444" stroke-width="1.3"/>
<line x1="28" y1="80" x2="105" y2="102" stroke="#ef4444" stroke-width="1.3"/>
<line x1="111" y1="58" x2="208" y2="42" stroke="#ef4444" stroke-width="1.2"/>
<line x1="111" y1="102" x2="208" y2="118" stroke="#ef4444" stroke-width="1.2"/>
<text x="34" y="146" font-size="10" fill="#94a3b8">限制物方视场角</text></svg>''',
"dof": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<ellipse cx="120" cy="80" rx="9" ry="40" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<circle cx="206" cy="80" r="3" fill="#0f172a"/><text x="192" y="100" font-size="10" fill="#0f172a">像面</text>
<line x1="120" y1="40" x2="152" y2="80" stroke="#10b981" stroke-width="1.3"/>
<line x1="120" y1="120" x2="152" y2="80" stroke="#10b981" stroke-width="1.3"/>
<line x1="52" y1="28" x2="52" y2="132" stroke="#f59e0b" stroke-width="1.4" stroke-dasharray="4 3"/>
<line x1="186" y1="28" x2="186" y2="132" stroke="#f59e0b" stroke-width="1.4" stroke-dasharray="4 3"/>
<text x="36" y="152" font-size="10" fill="#f59e0b">近景</text>
<text x="170" y="152" font-size="10" fill="#f59e0b">远景</text>
<text x="90" y="152" font-size="10" fill="#94a3b8">景深</text></svg>''',
"spherical_aber": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<ellipse cx="70" cy="80" rx="10" ry="46" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<line x1="18" y1="40" x2="70" y2="40" stroke="#ef4444" stroke-width="1.3"/><line x1="70" y1="40" x2="176" y2="80" stroke="#ef4444" stroke-width="1.3"/>
<line x1="18" y1="120" x2="70" y2="120" stroke="#ef4444" stroke-width="1.3"/><line x1="70" y1="120" x2="176" y2="80" stroke="#ef4444" stroke-width="1.3"/>
<line x1="18" y1="80" x2="70" y2="80" stroke="#10b981" stroke-width="1.3"/><line x1="70" y1="80" x2="206" y2="80" stroke="#10b981" stroke-width="1.3"/>
<line x1="176" y1="70" x2="176" y2="90" stroke="#0f172a" stroke-width="1"/>
<line x1="206" y1="70" x2="206" y2="90" stroke="#0f172a" stroke-width="1"/>
<text x="172" y="106" font-size="10" fill="#0f172a">δL'</text>
<text x="34" y="152" font-size="10" fill="#94a3b8">边缘光焦点更近</text></svg>''',
"coma": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<ellipse cx="70" cy="80" rx="10" ry="44" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<line x1="18" y1="38" x2="70" y2="44" stroke="#ef4444" stroke-width="1.2"/><line x1="70" y1="44" x2="168" y2="56" stroke="#ef4444" stroke-width="1.2"/>
<line x1="18" y1="80" x2="70" y2="80" stroke="#10b981" stroke-width="1.2"/><line x1="70" y1="80" x2="168" y2="80" stroke="#10b981" stroke-width="1.2"/>
<line x1="18" y1="122" x2="70" y2="116" stroke="#7c3aed" stroke-width="1.2"/><line x1="70" y1="116" x2="168" y2="104" stroke="#7c3aed" stroke-width="1.2"/>
<ellipse cx="182" cy="72" rx="7" ry="15" fill="#f59e0b" opacity="0.75"/>
<text x="152" y="126" font-size="10" fill="#94a3b8">彗星状弥散</text></svg>''',
"astig_curv": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="90" x2="230" y2="90" stroke="#cbd5e1" stroke-width="1"/>
<ellipse cx="60" cy="90" rx="9" ry="44" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<path d="M 60 90 Q 140 38 220 90" fill="none" stroke="#ef4444" stroke-width="1.6"/>
<path d="M 60 90 Q 140 60 220 90" fill="none" stroke="#10b981" stroke-width="1.6"/>
<text x="150" y="40" font-size="10" fill="#ef4444">子午场曲</text>
<text x="150" y="60" font-size="10" fill="#10b981">弧矢场曲</text>
<line x1="150" y1="46" x2="150" y2="58" stroke="#0f172a" stroke-width="1"/>
<text x="154" y="56" font-size="9" fill="#0f172a">像散差</text></svg>''',
"distortion": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="28" y="40" width="60" height="80" fill="none" stroke="#94a3b8" stroke-width="1.2"/>
<path d="M150 40 Q180 32 210 40" fill="none" stroke="#2563eb" stroke-width="1.6"/>
<path d="M150 120 Q180 128 210 120" fill="none" stroke="#2563eb" stroke-width="1.6"/>
<line x1="150" y1="40" x2="150" y2="120" stroke="#2563eb" stroke-width="1.6"/>
<line x1="210" y1="40" x2="210" y2="120" stroke="#2563eb" stroke-width="1.6"/>
<text x="32" y="140" font-size="10" fill="#94a3b8">理想方物</text>
<text x="152" y="140" font-size="10" fill="#2563eb">枕形畸变</text></svg>''',
"microscope": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<ellipse cx="70" cy="80" rx="8" ry="26" fill="#dbeafe" stroke="#2563eb" stroke-width="1.4"/>
<ellipse cx="150" cy="80" rx="10" ry="36" fill="#fae8ff" stroke="#7c3aed" stroke-width="1.4"/>
<line x1="20" y1="80" x2="70" y2="60" stroke="#ef4444" stroke-width="1.1"/><line x1="70" y1="60" x2="150" y2="112" stroke="#ef4444" stroke-width="1.1"/>
<line x1="150" y1="112" x2="222" y2="60" stroke="#10b981" stroke-width="1.1"/>
<circle cx="30" cy="80" r="2.5" fill="#0f172a"/><text x="12" y="98" font-size="9" fill="#0f172a">物</text>
<text x="58" y="144" font-size="10" fill="#94a3b8">物镜</text><text x="140" y="144" font-size="10" fill="#94a3b8">目镜</text></svg>''',
"telescope": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<ellipse cx="70" cy="80" rx="9" ry="40" fill="#dbeafe" stroke="#2563eb" stroke-width="1.4"/>
<ellipse cx="160" cy="80" rx="9" ry="30" fill="#fae8ff" stroke="#7c3aed" stroke-width="1.4"/>
<line x1="20" y1="60" x2="70" y2="60" stroke="#ef4444" stroke-width="1.1"/><line x1="70" y1="60" x2="160" y2="92" stroke="#ef4444" stroke-width="1.1"/>
<line x1="20" y1="100" x2="70" y2="100" stroke="#ef4444" stroke-width="1.1"/><line x1="70" y1="100" x2="160" y2="68" stroke="#ef4444" stroke-width="1.1"/>
<line x1="160" y1="80" x2="224" y2="80" stroke="#10b981" stroke-width="1.2"/>
<text x="58" y="148" font-size="10" fill="#94a3b8">物镜 f₁'</text><text x="148" y="148" font-size="10" fill="#94a3b8">目镜 f₂'</text></svg>''',
"mtf": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="130" x2="222" y2="130" stroke="#cbd5e1" stroke-width="1"/>
<line x1="30" y1="18" x2="30" y2="130" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 30 30 Q 90 30 140 70 Q 180 104 222 128" fill="none" stroke="#2563eb" stroke-width="2"/>
<path d="M 30 46 Q 80 56 120 90 Q 162 118 212 128" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="5 3"/>
<text x="190" y="148" font-size="10" fill="#94a3b8">空间频率</text>
<text x="4" y="24" font-size="10" fill="#94a3b8">MTF</text>
<text x="148" y="54" font-size="10" fill="#2563eb">衍射极限</text>
<text x="96" y="118" font-size="10" fill="#10b981">实际系统</text></svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

CORE_FORMULAS = [
    ("费马原理", "\\delta \\int_A^B n\\,ds = 0", "光沿光程取极值（极小、极大或稳定值）的路径传播"),
    ("反射定律", "\\theta_i = \\theta_r", "入射角等于反射角，反射光线与入射光线分居法线两侧"),
    ("折射定律（斯涅尔定律）", "n_1\\sin\\theta_1 = n_2\\sin\\theta_2", "折射角与入射角的正弦之比由两介质折射率决定"),
    ("全反射临界角", "\\sin\\theta_c = \\frac{n_2}{n_1}\\quad(n_1>n_2)", "光由光密介质射向光疏介质时的临界入射角"),
    ("光程", "L = \\int_A^B n\\,ds", "几何路程与折射率之积，反映光的相位累积"),
    ("折射率与光速", "n = \\frac{c}{v}", "介质折射率等于真空中光速与介质中光速之比"),
    ("拉格朗日不变量", "J = n y u = n' y' u'", "近轴光学中成像前后保持不变的量"),
    ("球面反射成像公式", "\\frac{1}{l'} + \\frac{1}{l} = \\frac{2}{r}", "球面镜的物距、像距与曲率半径关系"),
    ("球面折射成像公式", "\\frac{n'}{l'} - \\frac{n}{l} = \\frac{n'-n}{r}", "单球面折射的物像共轭关系"),
    ("垂轴放大率", "\\beta = \\frac{y'}{y} = \\frac{n\\,l'}{n'\\,l}", "像高与物高之比"),
    ("轴向放大率", "\\alpha = \\frac{dl'}{dl} = \\frac{n\\,l'^{2}}{n'\\,l^{2}} = \\beta^{2}\\frac{n'}{n}", "沿轴方向微小位移的放大率"),
    ("角放大率", "\\gamma = \\frac{u'}{u} = \\frac{n}{n'\\beta}", "共轭光线的孔径角之比"),
    ("放大率关系", "\\alpha\\,\\gamma = \\beta", "三种放大率之间的普遍关系"),
    ("棱镜最小偏向角", "n = \\frac{\\sin\\frac{A+\\delta_m}{2}}{\\sin\\frac{A}{2}}", "光路对称时偏向角最小，用于测折射率"),
    ("光楔偏向角", "\\delta = (n-1)A", "小顶角棱镜（光楔）的近似偏向角"),
    ("牛顿公式", "x\\,x' = f\\,f'", "以焦点为原点的物像关系"),
    ("高斯公式", "\\frac{f'}{l'} + \\frac{f}{l} = 1", "以主点为原点的物像关系"),
    ("光焦度", "\\Phi = \\frac{n'}{f'} = -\\frac{n}{f}", "系统的聚光本领，单位屈光度 (m⁻¹)"),
    ("两光组组合焦距", "f' = -\\frac{f_1' f_2'}{\\Delta}", "两光组光学间隔为 Δ 时的组合像方焦距"),
    ("两光组组合光焦度", "\\Phi = \\Phi_1 + \\Phi_2 - d\\,\\Phi_1\\Phi_2", "间距为 d 的两薄透镜组合光焦度"),
    ("薄透镜焦距", "\\frac{1}{f'} = (n-1)\\left(\\frac{1}{r_1}-\\frac{1}{r_2}\\right)", "透镜制造者公式（薄透镜）"),
    ("节点位置", "x_J = f',\\qquad x_J' = f", "节点相对焦点的位置，γ=+1"),
    ("平面镜旋转", "\\Delta\\varphi = 2\\theta", "平面镜转 θ 时反射光线转 2θ"),
    ("平行平板侧移", "\\Delta = \\frac{d\\,\\sin(i-i')}{\\cos i'}", "光线通过平行平板的横向位移"),
    ("平行平板轴向位移", "\\Delta l' = d\\left(1-\\frac{1}{n}\\right)", "平行平板引起的像面轴向位移"),
    ("数值孔径", "\\mathrm{NA} = n\\sin u", "物方孔径角的正弦与折射率之积"),
    ("相对孔径与 F 数", "F = \\frac{f'}{D} = \\frac{1}{2\\mathrm{NA}}", "焦距与入瞳直径之比，表征集光能力"),
    ("渐晕系数", "K = \\frac{D_k}{D}", "轴外点光束被拦去后的孔径比"),
    ("景深公式", "\\Delta_1 = \\frac{\\delta\\,p\\,D}{D+\\delta},\\quad \\Delta_2 = \\frac{\\delta\\,p\\,D}{D-\\delta}", "近景与远景深度，δ 为容许弥散圆"),
    ("焦深", "\\Delta' = 2\\delta' F", "允许像面轴向离焦的范围"),
    ("显微镜放大率", "\\Gamma = \\beta_{\\text{物}}\\cdot\\Gamma_{\\text{目}} = -\\frac{\\Delta\\cdot 250}{f_1' f_2'}", "物镜垂轴放大率与目镜视角放大率之积"),
    ("放大镜视角放大率", "\\Gamma = \\frac{250}{f'}", "明视距离 250 mm 处的视角放大率"),
    ("望远镜视角放大率", "\\Gamma = -\\frac{f_1'}{f_2'}", "物镜焦距与目镜焦距之比"),
    ("显微镜分辨率", "\\delta = \\frac{0.61\\lambda}{\\mathrm{NA}}", "由数值孔径决定的极限分辨距离"),
    ("望远镜分辨率", "\\delta\\theta = \\frac{1.22\\lambda}{D}", "由入瞳直径决定的极限分辨角"),
    ("fθ 物镜扫描", "y' = f'\\theta", "激光扫描中像高与扫描角成正比"),
    ("轴向球差", "\\delta L' = L' - l'", "边缘光线与近轴光线焦点之差"),
    ("波像差", "W = \\int \\Delta n\\,ds", "实际波面与理想球面波的光程差"),
    ("彗差", "K_s = \\frac{\\eta'}{h}", "轴外点弥散斑的不对称度量"),
    ("像散", "x_t' - x_s' = \\Delta x'", "子午与弧矢焦线的轴向间距"),
    ("Petzval 场曲", "\\frac{1}{r_p} = -\\sum_i \\frac{\\Phi_i}{n_i}", "各光组贡献的匹兹伐场曲之和"),
    ("畸变", "\\delta y' = y' - y_0'", "实际像高与理想像高之差"),
    ("位置色差", "\\Delta l'_{FC} = l'_F - l'_C", "F 光与 C 光的轴向焦点之差"),
    ("倍率色差", "\\Delta y'_{FC} = y'_F - y'_C", "F 光与 C 光的像高之差"),
    ("瑞利判据", "W \\le \\frac{\\lambda}{4}", "波像差小于四分之一波长时系统视为完善"),
    ("赛德尔像差多项式", "W = A\\rho^4 + B\\rho^3\\cos\\theta + C\\rho^2\\cos^2\\theta + D\\rho^2 + E\\rho\\cos\\theta", "初级（赛德尔）像差的波像差展开"),
    ("点扩散函数", "\\mathrm{PSF}(x,y) = |\\mathcal{F}\\{P\\}|^2", "光瞳函数的傅里叶变换模平方"),
    ("调制传递函数", "\\mathrm{MTF}(f) = \\frac{M'(f)}{M(f)}", "像与物的对比度之比随空间频率的变化"),
    ("摄影曝光量", "H = E\\,t", "感光面上的照度与曝光时间之积"),
    ("像面照度", "E' = \\pi L\\tau \\sin^{2}u'", "轴上像点照度与孔径角、透过率的关系"),
    ("柯勒照明", "\\text{光源成像于入瞳}", "使光源不均匀性不反映到物面照度上"),
    ("阿贝数", "V_d = \\frac{n_d-1}{n_F-n_C}", "表征光学材料色散，用于消色差选材"),
    ("消色差条件", "\\frac{\\Phi_1}{V_1} + \\frac{\\Phi_2}{V_2} = 0", "双胶合消色差透镜的光焦度条件"),
    ("平移矩阵", "T = \\begin{pmatrix} 1 & d/n \\\\ 0 & 1 \\end{pmatrix}", "近轴光线沿轴平移 d 的传递矩阵"),
    ("折射矩阵", "R = \\begin{pmatrix} 1 & 0 \\\\ -\\Phi & 1 \\end{pmatrix}", "近轴光线在球面上的折射矩阵"),
    ("系统矩阵", "M = R_m T_m \\cdots R_1 T_1,\\ \\det M = 1", "近轴光线的系统矩阵与行列式守恒"),
    ("等效空气层", "d_{\\text{等效}} = \\frac{d}{n}", "平行平板等效的减薄空气层厚度"),
    ("回射器条件", "\\mathbf{s}' = -\\mathbf{s}", "角锥棱镜使光线沿原方向返回"),
    ("变倍比", "\\Gamma_{\\text{变}} = \\frac{\\beta_{\\max}}{\\beta_{\\min}}", "变焦距系统的变倍能力"),
    ("超焦距", "H = \\frac{f'^{2}}{F\\,\\delta}", "对焦于此时景深从 H/2 延伸到无穷远"),
    ("相对照度", "E'(\\omega) = E'_0\\cos^{4}\\omega", "轴外照度按视场角的余弦四次方衰减"),
    ("二级光谱", "\\Delta l'_{\\text{二级}} \\propto f'\\,\\frac{P_1-P_2}{V_1-V_2}", "消色差后的残余色差，与部分色散有关"),
    ("显微镜线视场", "y = \\frac{\\phi}{2\\beta}", "目镜视场数与物方线视场的关系"),
    ("光学扩展量", "U = \\iint n^{2}\\,\\mathrm{d}A\\,\\cos\\theta\\,\\mathrm{d}\\Omega", "守恒量，决定系统的光能传递与信息量"),
    ("目视系统出瞳", "D_{\\text{出瞳}} = \\frac{D_{\\text{入瞳}}}{|\\Gamma|}", "出瞳直径等于入瞳直径除以视角放大率"),
    ("双平面镜偏转", "\\delta = 2\\alpha", "两镜夹角为 α 时出射光相对入射光的偏转"),
    ("校正镜组", "\\Phi = \\Phi_1 + \\Phi_2 - d\\,\\Phi_1\\Phi_2", "分离薄透镜组的组合光焦度"),
]

def js_escape(s):
    return s.replace("\\","\\\\").replace("`","\\`").replace("${","\\${")
def defn(t, body): return f'<section class="la-kp-sec la-kp-def"><h5>定 义</h5><p><strong>{t}</strong></p>{body}</section>'
def thm(t, body): return f'<section class="la-kp-sec la-kp-thm"><h5>定 理 · {t}</h5>{body}</section>'
def der(body): return f'<section class="la-kp-sec la-kp-der"><h5>推 导</h5>{body}</section>'
def exa(body): return f'<section class="la-kp-sec la-kp-exa"><h5>例 子</h5>{body}</section>'
def app(body): return f'<section class="la-kp-sec la-kp-app"><h5>应 用</h5>{body}</section>'
def note(body): return f'<section class="la-kp-sec la-kp-note"><h5>备 注</h5>{body}</section>'
def fml(latex, caption=""):
    cap = f'<span class="note">{caption}</span>' if caption else ""
    return f'<div class="la-fml">$${latex}$$ {cap}</div>'
def p(txt): return f'<p>{txt}</p>'
def wrap(body): return f'<div class="la-kp">{body}</div>'

# =====================================================
#  CHAPTER 1: 几何光学基础
# =====================================================
ch1_sections = [
{
"name": "1.1 光线、波面与基本定律",
"color": "#2563eb",
"desc": "光线与波面、光路可逆、费马原理、反射与折射定律",
"items": [
{"id":"eo1s1-1","name":"光线与波面","tags":["def","der"],"brief":"用光线描述传播方向，用波面描述等相位面。",
 "body": wrap(
   defn("光线",p("光线是垂直于波面、指示光传播方向的几何线，是几何光学的基本模型。它忽略光的波动性，把光能视为沿一定路径传播的射线。"))+
   defn("波面（波前）",p("波面是光波场中相位相同的点所构成的面。平面波的波面为平面，点光源发出的球面波的波面为同心球面；波面的法线方向即光线的传播方向。"))+
   der(p("<strong>光线方向与波面的关系：</strong>设波的相位为 $\\phi(\\mathbf{r},t)$，等相位面满足 $\\phi=\\text{const}$。光沿相位梯度方向传播，光线方向单位矢为：")+
   fml("\\mathbf{s} = \\frac{\\nabla \\phi}{|\\nabla \\phi|}","光线方向即波面法线方向")+
   p("对平面单色波 $\\phi=\\mathbf{k}\\cdot\\mathbf{r}-\\omega t$，等相位面 $\\mathbf{k}\\cdot\\mathbf{r}=\\text{const}$ 为平面，其法线与 $\\mathbf{k}$ 一致，故光线垂直于波面。"))+
   note(p("当元件尺寸与波长可比拟时，光线模型失效，须用波动光学（衍射）处理；几何光学是 $\\lambda\\to0$ 的极限。"))+
   note(p("<strong>光线模型的价值：</strong>它把复杂的衍射问题简化为几何追迹，使透镜、棱镜、光阑等元件的成像关系可用代数与几何方法求解；工程光学的绝大多数计算（成像位置、放大率、像差、光束限制）都建立在光线模型之上，只有在极限分辨或微小尺度问题中才需要回到波动光学。"))
 )},
{"id":"eo1s1-2","name":"光路可逆性","tags":["thm","der"],"brief":"光沿反方向传播时路径不变。",
 "body": wrap(
   thm("光路可逆性",p("在无吸收、无外场的介质中，若光线沿某一路径由 $A$ 传到 $B$，则将光反向，它必沿同一路径由 $B$ 传回 $A$。"))+
   der(p("<strong>由费马原理证明：</strong>光程 $L_{AB}=\\int_A^B n\\,\\mathrm{d}s$ 与传播方向无关（弧长元 $\\mathrm{d}s$ 恒为正），因此 $L_{AB}=L_{BA}$。若正向路径使 $\\delta L_{AB}=0$，则反向路径同样使 $\\delta L_{BA}=0$，故反向路径仍是实际光路：")+
   fml("L_{AB} = \\int_A^B n\\,\\mathrm{d}s = \\int_B^A n\\,\\mathrm{d}s = L_{BA}")+
   p("反射定律与折射定律在交换入射、出射方向后形式不变，也印证了可逆性。"))+
   app(p("<strong>应用：</strong>光路可逆是光学系统设计的重要依据——正向设计的成像关系可直接用于逆向光路追迹；激光谐振腔、干涉仪的光路分析均依赖该性质。"))
 )},
{"id":"eo1s1-3","name":"费马原理","tags":["def","thm","der"],"brief":"光沿光程取极值的路径传播。",
 "fig":"fermat","figCap":"光在界面上的实际光路使总光程取极值",
 "body": wrap(
   defn("光程",p("折射率为 $n$ 的介质中，光在几何路程 $\\mathrm{d}s$ 上对应的光程为 $n\\,\\mathrm{d}s$。光程表示与真空中等相位相对应的几何长度，即 $\\mathrm{d}L=n\\,\\mathrm{d}s$。"))+
   thm("费马原理",p("光从一点传到另一点，所走的实际路径使光程取极值（极小、极大或稳定值）：")+
   fml("\\delta L = \\delta \\int_A^B n\\,\\mathrm{d}s = 0"))+
   der(p("<strong>推导（导出折射定律）：</strong>设界面为 $x$ 轴，光由介质 $n_1$ 中 $A(0,h_1)$ 经界面点 $P(x,0)$ 射向介质 $n_2$ 中 $B(d,-h_2)$，总光程为：")+
   fml("L(x) = n_1\\sqrt{x^2+h_1^2} + n_2\\sqrt{(d-x)^2+h_2^2}")+
   p("令 $\\dfrac{\\mathrm{d}L}{\\mathrm{d}x}=0$，注意 $\\dfrac{x}{\\sqrt{x^2+h_1^2}}=\\sin\\theta_1$、$\\dfrac{d-x}{\\sqrt{(d-x)^2+h_2^2}}=\\sin\\theta_2$，得：")+
   fml("n_1\\sin\\theta_1 = n_2\\sin\\theta_2")+
   p("即折射定律。可见反射定律与折射定律都是费马原理的直接推论。"))+
   note(p("费马原理是几何光学的最高原理，反射定律、折射定律与各类成像公式均可由它导出；它同时揭示了几何光学与波动光学（稳相条件）的内在联系。"))
 )},
{"id":"eo1s1-4","name":"反射定律与折射定律","tags":["thm","der"],"brief":"入射、反射、折射光线共面且满足角度关系。",
 "body": wrap(
   thm("反射定律",p("入射光线、反射光线与法线共面，反射光线与入射光线分居法线两侧，入射角等于反射角：")+
   fml("\\theta_i = \\theta_r"))+
   thm("折射定律",p("入射光线、折射光线与法线共面，入射角正弦与折射角正弦之比等于两介质折射率之反比：")+
   fml("n_1\\sin\\theta_1 = n_2\\sin\\theta_2"))+
   der(p("<strong>反射定律证明：</strong>作 $B$ 关于界面的对称点 $B'$，则 $PB=PB'$，光程 $AP+PB=AP+PB'$。使 $AP+PB'$ 最小须 $A,P,B'$ 三点共线，由此可得反射光线与入射光线共面且 $\\theta_i=\\theta_r$：")+
   fml("AP + PB' \\ \\text{最小} \\iff A,\\,P,\\,B'\\ \\text{共线} \\implies \\theta_i=\\theta_r"))+
   note(p("两定律中的角均自法线量起；$n_1\\sin\\theta_1=n_2\\sin\\theta_2$ 对任意入射角成立，是研究一切光学系统的基本关系。"))
 )},
]},
{
"name": "1.2 全反射与光程不变量",
"color": "#3b82f6",
"desc": "全反射与临界角、等光程条件、拉格朗日不变量",
"items": [
{"id":"eo1s2-1","name":"全反射与临界角","tags":["def","der","app"],"brief":"光密到光疏介质界面上的全反射现象。",
 "body": wrap(
   defn("全反射",p("光由光密介质（$n_1$）射向光疏介质（$n_2<n_1$）时，当入射角超过一定值，折射光消失，入射光全部返回原介质，这一现象称为全反射。"))+
   der(p("<strong>临界角推导：</strong>由折射定律 $n_1\\sin\\theta_1=n_2\\sin\\theta_2$，因 $n_1>n_2$ 故 $\\theta_2>\\theta_1$。当 $\\theta_2=90°$ 时对应的入射角即为临界角 $\\theta_c$：")+
   fml("n_1\\sin\\theta_c = n_2\\sin 90° = n_2 \\implies \\sin\\theta_c = \\frac{n_2}{n_1}")+
   p("当 $\\theta_1>\\theta_c$ 时方程无实数解，界面处出现沿界面迅速衰减的隐失波，能量被全部反射。"))+
   app(p("<strong>应用：</strong>光纤利用纤芯与包层界面的全反射导光；全反射棱镜用于转折光路；此外还有内窥镜、液面传感器与激光准直等。"))
 )},
{"id":"eo1s2-2","name":"光程与等光程条件","tags":["def","der"],"brief":"理想成像要求各条光路的光程相等。",
 "body": wrap(
   defn("等光程",p("若发自物点 $A$ 的任意多条光线经光学系统后都到达像点 $A'$，且各条路径的光程彼此相等，则称满足等光程条件。"))+
   der(p("<strong>等光程与理想成像：</strong>由物点发出的光波经系统后应变为以 $A'$ 为球心的球面波，即出射波面为球面：")+
   fml("\\int_A^{A'} n\\,\\mathrm{d}s = \\text{const}\\quad(\\text{对全部实际光路})")+
   p("对反射情形，等光程条件体现为二次曲面镜的无像差性质：抛物面镜把轴上平行光无像差地会聚于焦点，正是由于各路径光程相等；椭球面镜把一焦点发出的光会聚于另一焦点。"))+
   note(p("实际光学系统只能对有限孔径与视场近似满足等光程，偏离等光程的部分即表现为波像差，是像差理论的基础。"))
 )},
{"id":"eo1s2-3","name":"拉格朗日不变量","tags":["thm","der"],"brief":"近轴光学中物像共轭前保持不变的量。",
 "body": wrap(
   thm("拉格朗日不变量",p("在近轴区，光线与光轴夹角为 $u$、光线在共轭面上的高度为 $y$，则沿光路传播时 $n\\,y\\,u$ 保持不变：")+
   fml("J = n\\,y\\,u = n'\\,y'\\,u'"))+
   der(p("<strong>推导：</strong>以单球面折射为例，近轴折射关系为 $n\\,u=n'\\,u'$，物像高度改变满足 $y'=y+u' d$（$d$ 为沿轴微小间隔）。对球面成像公式两侧作微小变化并整理，可证：")+
   fml("n\\,y\\,\\tan u = n'\\,y'\\,\\tan u' \\ \\xrightarrow{\\ \\text{近轴}\\ }\\ n\\,y\\,u = n'\\,y'\\,u'")+
   p("该量 $J$ 称为拉格朗日不变量，它把垂轴放大率 $\\beta=y'/y$ 与角放大率 $\\gamma=u'/u$ 联系起来，即 $\\beta\\gamma=n/n'$。"))+
   note(p("拉格朗日不变量反映了光学系统的信息传递能力（光学扩展量 étendue）守恒，是说明亮度不能通过无源光学系统提高的理论依据。"))+
   app(p("<strong>应用（光学扩展量守恒）：</strong>聚光照明中，收集角 $u$ 与像面受照立体角（由面积与孔径角构成的量 $\\iint n^{2}\\,\\mathrm{d}A\\cos\\theta\\,\\mathrm{d}\\Omega$）之积守恒，因此增大收集角必然要求增大照明面积或出射立体角；这一规律决定了投影、照明与聚光系统的能量利用上限。"))
 )},
]},
{
"name": "1.3 球面反射与球面折射成像",
"color": "#1d4ed8",
"desc": "球面反射成像、单球面折射、近轴近似",
"items": [
{"id":"eo1s3-1","name":"球面反射成像公式","tags":["thm","der"],"brief":"球面镜的物像关系与焦距。",
 "fig":"sphere_mirror","figCap":"球面镜的近轴成像",
 "body": wrap(
   thm("球面镜成像公式",p("近轴条件下球面镜的物距 $l$ 与像距 $l'$ 满足共轭关系：")+
   fml("\\frac{1}{l'} + \\frac{1}{l} = \\frac{1}{f},\\qquad f = \\frac{r}{2}")+
   p("其中 $r$ 为球面镜曲率半径。习惯上取凹面镜焦距为正（会聚光），凸面镜焦距为负（发散光）。"))+
   der(p("<strong>推导：</strong>顶点取为原点，物在镜前、物距为 $l$，像距为 $l'$。取一条近轴光线，由几何关系与反射定律可得 $\\dfrac{h}{l}+\\dfrac{h}{l'}=\\dfrac{2h}{r}$（角关系 $u+u'=2\\varphi$ 且 $u\\approx h/l$、$u'\\approx h/l'$、$\\varphi\\approx h/r$），消去高度 $h$：")+
   fml("\\frac{1}{l'} + \\frac{1}{l} = \\frac{2}{r}"))+
   note(p("垂轴放大率 $\\beta=-l'/l$：实物经凹面镜成实像时倒立；当物位于焦点以内时 $l'$ 反号，成放大正立虚像，这正是凹面镜用作反射式望远镜与化妆镜的原因。"))
 )},
{"id":"eo1s3-2","name":"单球面折射成像公式","tags":["thm","der"],"brief":"两种介质分界球面的物像共轭关系。",
 "fig":"spherical_refract","figCap":"单球面折射成像",
 "body": wrap(
   thm("单球面折射公式",p("折射球面曲率半径为 $r$，物方介质折射率 $n$、像方 $n'$，近轴成像满足：")+
   fml("\\frac{n'}{l'} - \\frac{n}{l} = \\frac{n'-n}{r}"))+
   der(p("<strong>推导：</strong>由折射定律的近轴形式 $n\\,u=n'\\,u'$，并利用几何关系 $u=\\varphi-\\theta$、$u'=\\varphi-\\theta'$，其中 $\\varphi\\approx h/r$、$\\theta\\approx h/l$、$\\theta'\\approx h/l'$。代入得：")+
   fml("n\\left(\\frac{h}{r}-\\frac{h}{l}\\right) = n'\\left(\\frac{h}{r}-\\frac{h}{l'}\\right)")+
   p("两边除以 $h$ 并整理，即得 $\\dfrac{n'}{l'}-\\dfrac{n}{l}=\\dfrac{n'-n}{r}$。"))+
   note(p("令 $l\\to-\\infty$ 得像方焦距 $f'=\\dfrac{n' r}{n'-n}$，令 $l'\\to\\infty$ 得物方焦距 $f=-\\dfrac{n r}{n'-n}$，二者满足 $\\dfrac{f'}{f}=-\\dfrac{n'}{n}$。"))
 )},
{"id":"eo1s3-3","name":"近轴近似与光线追迹","tags":["def","der"],"brief":"小角度近似是近轴光学的基础。",
 "body": wrap(
   defn("近轴区",p("限制在光轴附近、且与光轴夹角很小的区域称为近轴区。近轴光线满足 $u\\ll1$，可用 $\\sin u\\approx u$、$\\cos u\\approx1$、$\\tan u\\approx u$ 的近似。"))+
   der(p("<strong>由折射定律作近轴展开：</strong>斯涅尔定律 $n\\sin u=n'\\sin u'$，把正弦展开到一阶：")+
   fml("n\\left(u-\\frac{u^3}{6}+\\cdots\\right) = n'\\left(u'-\\frac{u'^3}{6}+\\cdots\\right) \\ \\xrightarrow{\\ \\text{近轴}\\ }\\ n\\,u = n'\\,u'")+
   p("舍弃高阶项后折射关系线性化，系统近似为线性系统，从而得到共轭点、放大率等理想成像性质；而被舍去的高阶项正是球差等单色像差的来源。"))+
   note(p("近轴光学给出理想像的位置与大小，是评价实际系统（实际光线追迹）的基准，故也称高斯光学。"))
 )},
]},
{
"name": "1.4 共轭关系与放大率",
"color": "#0284c7",
"desc": "物像共轭、垂轴放大率与轴向放大率",
"items": [
{"id":"eo1s4-1","name":"物像共轭关系","tags":["def","der"],"brief":"近轴区内物点与像点一一对应。",
 "body": wrap(
   defn("共轭关系",p("在近轴区内，物空间的每一点都对应像空间的一点，这两点称为共轭点；对应的面称为共轭面。共轭是物像关系的核心。"))+
   der(p("<strong>由成像公式验证：</strong>对单球面折射 $\\dfrac{n'}{l'}-\\dfrac{n}{l}=\\dfrac{n'-n}{r}$，给定物距 $l$，像距 $l'$ 唯一确定：")+
   fml("l' = \\frac{n' r\\,l}{n\\,r+(n'-n)\\,l}")+
   p("因此物点唯一对应像点，物面上各点的共轭像点构成像面，物面与像面互为共轭面。"))+
   note(p("共轭关系配合光路可逆具有对称性：把物点移到原像点，新像点必落在原物点位置。这为系统的正、反向使用提供了依据。"))
 )},
{"id":"eo1s4-2","name":"垂轴放大率与轴向放大率","tags":["def","der"],"brief":"像与物在线度上的放大关系。",
 "body": wrap(
   defn("垂轴放大率",p("像高与物高之比称为垂轴（横向）放大率：$\\beta=y'/y$。"))+
   der(p("<strong>垂轴放大率：</strong>由单球面折射的近轴几何关系（相似三角形）可得：")+
   fml("\\beta = \\frac{y'}{y} = \\frac{n\\,l'}{n'\\,l}")+
   p("$\\beta>0$ 成正立像，$\\beta<0$ 成倒立像；$|\\beta|>1$ 放大，$|\\beta|<1$ 缩小。")+
   p("<strong>轴向放大率：</strong>物沿轴移动 $\\mathrm{d}l$ 时像移动 $\\mathrm{d}l'$，定义 $\\alpha=\\mathrm{d}l'/\\mathrm{d}l$。对成像公式微分 $\\dfrac{n'}{l'^{2}}\\mathrm{d}l'=\\dfrac{n}{l^{2}}\\mathrm{d}l$：")+
   fml("\\alpha = \\frac{\\mathrm{d}l'}{\\mathrm{d}l} = \\frac{n\\,l'^{2}}{n'\\,l^{2}} = \\beta^{2}\\frac{n'}{n}")+
   p("结合角放大率 $\\gamma=u'/u=\\dfrac{n}{n'\\beta}$，可得三角放大率关系 $\\alpha\\,\\gamma=\\beta$，$\\beta\\,\\gamma=n/n'$。"))+
   note(p("由于 $\\alpha=\\beta^{2}(n'/n)$，当 $\\beta\\neq1$ 时立体像在轴向被拉伸，造成空间失真；这也是焦深、景深与立体摄影讨论的基础。"))
 )},
]},
{
"name": "1.5 折射棱镜与色散",
"color": "#6366f1",
"desc": "折射棱镜的偏向角与最小偏向角、色散",
"items": [
{"id":"eo1s5-1","name":"折射棱镜与色散","tags":["def","der"],"brief":"棱镜使不同波长光偏折不同形成色散。",
 "body": wrap(
   defn("折射棱镜",p("折射棱镜由两个相交的折射平面（折射面）构成，两面夹角 $A$ 称为折射棱角（顶角）。单色光经棱镜两次折射后出射方向相对入射方向偏转，偏转角 $\\delta$ 称为偏向角。"))+
   der(p("<strong>偏向角与几何关系：</strong>设第一面入射角 $\\theta_1$、折射角 $\\theta_1'$，第二面入射角 $\\theta_2'=\\theta_1'-A$、出射角 $\\theta_2$，则：")+
   fml("\\delta = \\theta_1 + \\theta_2 - A")+
   p("由于材料折射率随波长变化 $n=n(\\lambda)$，不同波长光偏向角不同，白光出射后展开成光谱，即色散：")+
   fml("\\frac{\\mathrm{d}\\delta}{\\mathrm{d}\\lambda} = \\frac{\\mathrm{d}\\delta}{\\mathrm{d}n}\\cdot\\frac{\\mathrm{d}n}{\\mathrm{d}\\lambda}"))+
   note(p("一般光学材料 $\\dfrac{\\mathrm{d}n}{\\mathrm{d}\\lambda}<0$，波长越短折射率越大，紫光偏折最多，故棱镜光谱中紫端偏向角最大。"))
 )},
{"id":"eo1s5-2","name":"棱镜最小偏向角","tags":["thm","der","exa"],"brief":"光路对称时偏向角最小，可用于测折射率。",
 "body": wrap(
   thm("最小偏向角",p("当光线在棱镜内对称传播（$\\theta_1=\\theta_2$、$\\theta_1'=\\theta_2'$）时，偏向角取最小值 $\\delta_m$，此时折射率为：")+
   fml("n = \\frac{\\sin\\frac{A+\\delta_m}{2}}{\\sin\\frac{A}{2}}"))+
   der(p("<strong>推导：</strong>由 $\\delta=\\theta_1+\\theta_2-A$ 及折射定律，把 $\\delta$ 表示为 $\\theta_1$ 的函数并取极值 $\\dfrac{\\mathrm{d}\\delta}{\\mathrm{d}\\theta_1}=0$。由对称性得 $\\theta_1=\\theta_2$，即光路对称，此时 $\\theta_1'=\\theta_2'=A/2$：")+
   fml("\\theta_1 = \\frac{A+\\delta_m}{2},\\qquad \\theta_1'=\\frac{A}{2}")+
   p("代入 $n=\\dfrac{\\sin\\theta_1}{\\sin\\theta_1'}$ 即得最小偏向角公式。"))+
   exa(p("<strong>例：</strong>等边棱镜 $A=60°$，测得 $\\delta_m=51.0°$，则 $n=\\dfrac{\\sin 55.5°}{\\sin 30°}\\approx1.65$。最小偏向角法是测量固体、液体折射率的一种经典方法。"))+
   note(p("最小偏向角法要求棱镜材料均匀、棱角精确；高精度测量还需严格控制温度与光谱线纯度。"))
 )},
]},
]

# =====================================================
#  CHAPTER 2: 理想光学系统
# =====================================================
ch2_sections = [
{
"name": "2.1 理想光学系统与基点基面",
"color": "#7c3aed",
"desc": "理想光学系统的定义、性质，焦点焦距与主点主平面",
"items": [
{"id":"eo2s1-1","name":"理想光学系统与共线成像","tags":["def","thm","der"],"brief":"点成点、直线成直线、平面成平面的无像差系统。",
 "body": wrap(
   defn("理想光学系统",p("能够对任意大的空间范围内、以任意宽的光束成完善像的光学系统称为理想光学系统。其成像遵循点对点、直线对直线、平面对平面的一一对应关系，故又称共线成像。"))+
   thm("理想光学系统的成像性质",p("理想光学系统满足：(1) 物空间的每一点、线、面分别对应像空间的共轭点、线、面；(2) 物方平行于光轴的光线经系统后必通过像方焦点 $F'$；(3) 过物方焦点 $F$ 的光线经系统后平行于光轴出射。"))+
   der(p("<strong>共线成像的推论：</strong>由共线对应，物面上一条直线在像面上仍是一条直线，且物、像空间坐标间为线性变换。设物方坐标 $(x,y,z)$、像方 $(x',y',z')$，共线条件可写为：")+
   fml("\\frac{x'}{y'} = \\frac{a_1 x + a_2 y + a_3}{\\cdots}\\ \\Rightarrow\\ \\text{像方坐标为物方坐标的分式线性函数}")+
   p("由此可推出：同一共轭面上的放大率只与该面位置有关；两对共轭面（或焦点、主点）即可完全确定系统的成像性质。"))+
   note(p("实际系统只能在近轴区、有限孔径与视场下近似理想；理想系统为实际系统提供了理想的比较基准，是像质评价的出发点。"))+
   note(p("<strong>与高斯光学的关系：</strong>理想光学系统只要求共线成像，是更一般的公理化描述；高斯光学则是它在近轴条件下的一阶实现。实际系统的像差就是实际波面相对理想球面波的偏离，因此理想系统的基点、放大率与物像公式构成像差计算的基准。"))
 )},
{"id":"eo2s1-2","name":"焦点、焦距与主点主平面","tags":["def","der"],"brief":"描述理想光学系统的基点与基面。",
 "fig":"principal","figCap":"物方主平面 H 与像方主平面 H'",
 "body": wrap(
   defn("焦点与焦平面",p("平行于光轴的物方光线经系统后交于光轴上一点 $F'$，称为像方焦点；过 $F'$ 的垂轴平面为像方焦平面。同理，由像方平行光反向对应的物方会聚点为物方焦点 $F$，其垂轴平面为物方焦平面。"))+
   der(p("<strong>主平面（β=+1 的共轭面）推导：</strong>对给定系统，垂轴放大率 $\\beta$ 随共轭面位置连续变化，必存在使 $\\beta=+1$ 的一对共轭面，称为物方主平面 $H$ 与像方主平面 $H'$。它们与光轴的交点 $H$、$H'$ 即主点。物方焦距 $f$ 与像方焦距 $f'$ 定义为：")+
   fml("f = HF,\\qquad f' = H'F'")+
   p("主平面的物理意义：入射到 $H$ 面上的光线高度与出射到 $H'$ 面上的光线高度相等（$\\beta=+1$），光在两者之间的传播可视为平行的直线平移。"))+
   note(p("物方焦距与像方焦距满足 $f'/f=-n'/n$，当物像空间均为空气时 $f'=-f$。基点（$F,F',H,H',J,J'$）与基面完全决定了理想系统的成像。"))
 )},
]},
{
"name": "2.2 物像关系公式",
"color": "#8b5cf6",
"desc": "牛顿公式、高斯公式与物像位置解析关系",
"items": [
{"id":"eo2s2-1","name":"牛顿公式与高斯公式","tags":["thm","der"],"brief":"以焦点或主点为原点的物像关系。",
 "fig":"focal","figCap":"平行光经系统后过像方焦点 F'，焦距 f'=H'F'",
 "body": wrap(
   thm("牛顿公式",p("以物方焦点 $F$、像方焦点 $F'$ 为原点，物距 $x$、像距 $x'$（顺光线方向为正），则物像关系为：")+
   fml("x\\,x' = f\\,f'"))+
   der(p("<strong>推导：</strong>物高 $y$，像高 $y'$。作两条特征光线：由物点发出的平行于光轴的光线过 $F'$ 出射。由相似三角形 $\\triangle$（物点、$F$、主点）与 $\\triangle$（像点、$F'$、主点）可得：")+
   fml("\\frac{y'}{y} = -\\frac{f}{x} = -\\frac{x'}{f'} \\ \\Longrightarrow\\ x\\,x' = f\\,f'")+
   p("<strong>高斯公式：</strong>令 $x=l-f$、$x'=l'-f'$ 代入牛顿公式，整理得：")+
   fml("\\frac{f'}{l'} + \\frac{f}{l} = 1")+
   p("当物像空间介质相同时 $f'=-f$，高斯公式化为 $\\dfrac{1}{l'}-\\dfrac{1}{l}=\\dfrac{1}{f'}$，即常见的薄透镜成像公式。"))+
   note(p("牛顿公式以焦点为原点，形式简洁；高斯公式以主点为原点，便于与系统的实际结构尺寸联系。二者等价，可按需选用。"))
 )},
{"id":"eo2s2-2","name":"由基点求物像位置","tags":["der","exa"],"brief":"利用基点基面解析求解任一物的像。",
 "body": wrap(
   der(p("<strong>解析求解步骤：</strong>已知系统的 $f$、$f'$ 及主点 $H$、$H'$，对给定物距 $l$（相对 $H$）：先由高斯公式求 $l'$：")+
   fml("l' = \\frac{f' l}{l - f}")+
   p("再由垂轴放大率求像高 $y'=\\beta y$；像的虚实由 $l'$ 的符号判定，像的正倒由 $\\beta$ 的符号判定。")+
   p("<strong>物像位置的一般关系：</strong>综合牛顿公式与放大率公式，可得系统的物像传递关系：")+
   fml("\\beta = -\\frac{f}{x} = -\\frac{x'}{f'} = \\frac{f\\,l'}{f'\\,l}\\cdot\\frac{n'}{n}"))+
   exa(p("<strong>例：</strong>某系统 $f'=100\\,\\text{mm}$、$f=-100\\,\\text{mm}$，物在 $H$ 前 $150\\,\\text{mm}$（$l=-150\\,\\text{mm}$），则 $l'=\\dfrac{100\\times(-150)}{-150-100}=60\\,\\text{mm}$，像方为实像；$\\beta=\\dfrac{f\\,l'}{f'\\,l}=\\dfrac{-100\\times60}{100\\times(-150)}=0.4$，成正立缩小实像。"))+
   note(p("物在无穷远时 $l'=f'$，像位于像方焦平面；物在物方焦平面时 $l'\\to\\infty$，出射为平行光。这两种特殊情况在望远镜、准直系统中反复用到。"))
 )},
]},
{
"name": "2.3 放大率",
"color": "#6d28d9",
"desc": "垂轴放大率、轴向放大率与角放大率",
"items": [
{"id":"eo2s3-1","name":"垂轴放大率","tags":["def","der"],"brief":"像高与物高之比及其位置表达式。",
 "body": wrap(
   defn("垂轴放大率",p("理想光学系统中，垂轴放大率定义为像高与物高之比 $\\beta=y'/y$，它是共轭面位置的函数。"))+
   der(p("<strong>三种等价形式：</strong>由牛顿公式的相似三角形关系与拉格朗日不变量 $n y u=n' y' u'$：")+
   fml("\\beta = \\frac{y'}{y} = -\\frac{f}{x} = -\\frac{x'}{f'} = \\frac{n\\,l'}{n'\\,l}")+
   p("其中 $x=l-f$、$x'=l'-f'$。$\\beta$ 只与共轭面位置有关，与孔径无关——这正是理想光学系统无像差的体现。"))+
   note(p("$\\beta>0$ 正立像，$\\beta<0$ 倒立像；$|\\beta|>1$ 放大，$|\\beta|<1$ 缩小。对同一系统，物像位置与放大率一一对应。"))
 )},
{"id":"eo2s3-2","name":"轴向放大率","tags":["der"],"brief":"物沿轴微小位移与像位移之比。",
 "body": wrap(
   der(p("<strong>推导：</strong>设物沿光轴移动 $\\mathrm{d}x$ 时像移动 $\\mathrm{d}x'$，定义轴向放大率 $\\alpha=\\mathrm{d}x'/\\mathrm{d}x$。对牛顿公式 $xx'=ff'$ 微分得 $x'\\mathrm{d}x + x\\,\\mathrm{d}x'=0$：")+
   fml("\\alpha = \\frac{\\mathrm{d}x'}{\\mathrm{d}x} = -\\frac{x'}{x}")+
   p("代入 $\\beta=-f/x=-x'/f'$，并注意 $f'/f=-n'/n$，可得：")+
   fml("\\alpha = \\beta^{2}\\frac{n'}{n} = \\beta^{2}\\frac{f'}{f}"))+
   note(p("由于 $\\alpha\\propto\\beta^{2}$，垂轴放大率为 $\\beta$ 的像在轴向被拉伸 $\\beta^{2}$ 倍，导致空间物体成像产生纵向失真，这是显微镜等系统需要三维校正的原因。"))
 )},
{"id":"eo2s3-3","name":"角放大率","tags":["def","der"],"brief":"共轭光线与轴夹角之比。",
 "body": wrap(
   defn("角放大率",p("轴上物点发出的一对共轭光线与光轴的夹角分别为 $u$、$u'$，定义角放大率 $\\gamma=u'/u$。"))+
   der(p("<strong>推导：</strong>由拉格朗日不变量 $n\\,y\\,u=n'\\,y'\\,u'$，两边除以 $y\\,y'$ 得：")+
   fml("\\gamma = \\frac{u'}{u} = \\frac{n\\,y}{n'\\,y'} = \\frac{n}{n'\\beta} = \\frac{n\\,f}{n'\\,f'}\\cdot\\frac{1}{\\beta}")+
   p("在物像空间介质相同时 $\\gamma=1/\\beta$。三种放大率满足关系 $\\alpha\\,\\gamma=\\beta$ 与 $\\beta\\,\\gamma=n/n'$。"))+
   note(p("角放大率表征系统对光束发散（会聚）程度的改变。当 $\\gamma=+1$ 时物、像方共轭光线平行，对应的共轭点即为节点。"))
 )},
]},
{
"name": "2.4 节点与系统组合",
"color": "#a855f7",
"desc": "节点节平面、两光组组合的焦距与光焦度",
"items": [
{"id":"eo2s4-1","name":"节点与节平面","tags":["def","der"],"brief":"角放大率为 +1 的共轭点。",
 "body": wrap(
   defn("节点",p("角放大率 $\\gamma=+1$ 的一对共轭点称为物方节点 $J$ 与像方节点 $J'$，过节点且垂直于光轴的平面为节平面。"))+
   der(p("<strong>节点位置推导：</strong>由 $\\gamma=\\dfrac{n}{n'\\beta}=1$，得 $\\beta=\\dfrac{n}{n'}$。代入 $\\beta=-f/x$ 及 $f'/f=-n'/n$：")+
   fml("x_J = -\\frac{f}{\\beta} = -\\frac{n' f}{n} = f',\\qquad x_J' = -f'\\beta = f")+
   p("即物方节点在像方焦点 $F'$ 前 $f'$ 处（相对 $H$ 的量），像方节点在物方焦点附近，二者相对主点的位置为 $HJ=H'J'=f'-f$。"))+
   note(p("当物像空间介质相同时（$n=n'$）有 $f'=-f$，此时 $x_J=-f$、$x_J'=f$，节点与主点重合。因此空气中系统的节点即主点。节点的实用意义：过节点的共轭光线方向不变，用于测量焦距与系统装调。"))
 )},
{"id":"eo2s4-2","name":"光学系统的组合","tags":["thm","der"],"brief":"两个光组组合后的焦距与主点。",
 "fig":"comb_lens","figCap":"两光组的组合",
 "body": wrap(
   thm("两光组组合公式",p("两光组的像方焦距分别为 $f_1'$、$f_2'$，二者之间的光学间隔 $\\Delta=F_1'F_2$，则组合系统像方焦距为：")+
   fml("f' = -\\frac{f_1' f_2'}{\\Delta},\\qquad \\Delta = d - f_1' + f_2"))+
   der(p("<strong>推导：</strong>先由第一光组求中间像，再由第二光组求最终像。对物在无穷远的情形，第一光组的像在其像方焦面；该中间像对第二光组为物，最终像位置由两光组的传递矩阵（或逐次高斯公式）给出。整理后得组合焦距公式；组合系统的像方主点 $H'$ 相对第二光组主点 $H_2'$ 的距离为：")+
   fml("H_2'H' = \\frac{f_2'\\,d}{\\Delta}"))+
   note(p("当两系统紧贴（$d\\to0$）时 $\\Delta=-f_1'+f_2$，组合光焦度简化为 $\\Phi=\\Phi_1+\\Phi_2$。组合系统的基点基面由两光组各自基点及间隔完全决定，这是复杂光学系统设计的基本工具。"))
 )},
]},
{
"name": "2.5 典型构件与作图",
"color": "#9333ea",
"desc": "厚薄透镜、光焦度、远心光路与作图法",
"items": [
{"id":"eo2s5-1","name":"厚透镜与薄透镜","tags":["def","der"],"brief":"透镜的基点与透镜制造者公式。",
 "body": wrap(
   defn("厚透镜与薄透镜",p("两折射面间距与焦距相比不可忽略的透镜为厚透镜；间距趋于零的为薄透镜。厚透镜需用两主平面描述，薄透镜的两主平面近似重合于透镜中心。"))+
   der(p("<strong>薄透镜焦距（透镜制造者公式）：</strong>把透镜视为两个折射球面的组合。第一面 $r_1$ 的像方焦距 $f_1'=\\dfrac{n}{n-1}r_1$（空气中的玻璃 $n$），第二面 $r_2$ 的物方焦距 $f_2=-\\dfrac{n}{n-1}r_2$，厚度取零时组合光焦度：")+
   fml("\\frac{1}{f'} = (n-1)\\left(\\frac{1}{r_1}-\\frac{1}{r_2}\\right)")+
   p("对双凸、平凸等正透镜 $f'>0$（会聚）；双凹、平凹等负透镜 $f'<0$（发散）。"))+
   note(p("厚透镜的 $f'=\\dfrac{n r_1 r_2}{(n-1)[n(r_2-r_1)+(n-1)d]}$，其主平面一般位于透镜内部，需按基点定义确定。镜头设计中常把厚透镜等效为薄透镜加间隔处理。"))
 )},
{"id":"eo2s5-2","name":"光焦度与屈光度","tags":["def","der"],"brief":"表征系统聚光能力的量。",
 "body": wrap(
   defn("光焦度",p("像方折射率 $n'$ 与像方焦距 $f'$ 之比称为光焦度：$\\Phi=n'/f'$。光焦度表征系统的会聚（或发散）本领，正值会聚、负值发散。"))+
   der(p("<strong>单位与组合：</strong>当焦距以米为单位时，光焦度的单位为屈光度（D，$\\text{m}^{-1}$）。由组合焦距公式可得两光组组合的光焦度：")+
   fml("\\Phi = \\Phi_1 + \\Phi_2 - d\\,\\Phi_1\\Phi_2")+
   p("其中 $d$ 为两主面间的距离。两薄透镜紧贴时 $d=0$，$\\Phi=\\Phi_1+\\Phi_2$，光焦度可直接相加。"))+
   note(p("眼镜度数即光焦度的 $100$ 倍，如 $-200$ 度对应 $\\Phi=-2\\,\\text{D}$，$f'=-0.5\\,\\text{m}$。光焦度是镜头设计与光度学的基本参数。"))
 )},
{"id":"eo2s5-3","name":"远心光路","tags":["def","der","app"],"brief":"物方远心与像方远心光路的构成与作用。",
 "body": wrap(
   defn("远心光路",p("把孔径光阑置于焦平面上，使主光线（过入瞳或出瞳中心的光线）在物方或像方平行于光轴的光路称为远心光路；分为物方远心与像方远心。"))+
   der(p("<strong>物方远心（孔径光阑置于像方焦平面）：</strong>此时入瞳位于物方无限远，主光线在物方平行于光轴。当物面沿轴离焦 $\\mathrm{d}l$ 时，物高虽变但仍以相同角度成像：")+
   fml("y' = \\beta\\,y = \\frac{f'}{x}\\,y\\ \\text{中 } x \\text{ 随离焦改变，但主光线方向不变}")+
   p("物方远心使离焦不引起放大率误差，故用于精密测量（如工具显微镜）；像方远心（光阑置于物方焦平面，出射主光线平行于光轴）使像面照度均匀，用于遥感与照度均匀的投影系统。"))+
   note(p("远心系统的特点是主光线平行于光轴的一侧，因而该侧照明或探测的孔径角受限于远心度；设计时须统筹光阑位置与分辨率。"))
 )},
{"id":"eo2s5-4","name":"理想光学系统的作图法","tags":["der","app"],"brief":"用特征光线作图求像。",
 "body": wrap(
   der(p("<strong>三条特征光线：</strong>已知基点 $F,F',H,H'$，可用三条特征光线中的任意两条确定像点：(1) 平行于光轴的入射光线，出射后过 $F'$；(2) 过 $F$ 的入射光线，出射后平行于光轴；(3) 过物方节点 $J$ 的入射光线，出射后仍过像方节点 $J'$ 且方向不变。")+
   fml("\\text{平行入射} \\to \\text{过 } F'\\ ;\\qquad \\text{过 } F\\ \\text{入射} \\to \\text{平行出射}")+
   p("以正透镜为例：物在焦点外，两条特征光线交于像方成实像（倒立）；物在焦点内，两条光线反向延长交于像方成虚像（正立放大）。"))+
   note(p("作图法直观、快速，是理解成像规律与判断像的正倒、虚实、放缩的有力手段；当物在无穷远时，用一条平行光线与一条过 $F'$ 的光线确定焦面上的像点。"))
 )},
]},
{
"name": "2.6 矩阵光学与变焦系统",
"color": "#8b5cf6",
"desc": "近轴光线传递矩阵、变焦距系统的变倍与补偿",
"items": [
{"id":"eo2s6-1","name":"近轴光线传递矩阵","tags":["def","der"],"brief":"用 2×2 矩阵描述近轴光线的传输。",
 "body": wrap(
   defn("光线向量与系统矩阵",p("把近轴光线的状态用二维向量 $(y,\\,n\\,u)$ 表示（$y$ 为光线在参考面上的高度，$u$ 为与光轴夹角，$n$ 为当地折射率）。系统对光线的变换是线性的，可用 $2\\times2$ 矩阵描述：")+
   fml("\\begin{pmatrix} y' \\\\ n'u' \\end{pmatrix} = M \\begin{pmatrix} y \\\\ n\\,u \\end{pmatrix},\\qquad M = \\begin{pmatrix} M_{11} & M_{12} \\\\ M_{21} & M_{22} \\end{pmatrix}"))+
   der(p("<strong>基本矩阵：</strong>沿轴平移距离 $d$（介质折射率 $n$）的平移矩阵为：")+
   fml("T = \\begin{pmatrix} 1 & d/n \\\\ 0 & 1 \\end{pmatrix}")+
   p("折射球面（曲率半径 $r$，光焦度 $\\Phi=(n'-n)/r$）的折射矩阵为：")+
   fml("R = \\begin{pmatrix} 1 & 0 \\\\ -\\Phi & 1 \\end{pmatrix}")+
   p("由 $\\det T=\\det R=1$，整个系统的 $\\det M=M_{11}M_{22}-M_{12}M_{21}=1$。当两参考面互为共轭（成像条件 $M_{12}=0$）时，$M_{11}$ 即垂轴放大率 $\\beta$，$M_{22}$ 即角放大率 $\\gamma$，此时 $\\beta\\gamma=1$（同介质情形），与拉格朗日不变量一致。"))+
   note(p("矩阵法便于借助计算机进行系统的一阶（近轴）分析，是光学设计软件求解初始结构与一阶量（焦点、主点、放大率）的基础。"))
 )},
{"id":"eo2s6-2","name":"变焦距系统","tags":["def","der","app"],"brief":"通过移动光组实现焦距连续变化并保持像面。",
 "body": wrap(
   defn("变焦距系统",p("通过沿轴移动一个或多个光组，使系统焦距（放大率）连续改变，同时保持像面位置稳定，这样的系统称为变焦距（变倍）系统。改变焦距的组称变倍组，补偿像面位移的组称补偿组。"))+
   der(p("<strong>变倍原理：</strong>由组合公式，两光组的组合焦距随间隔 $d$ 变化。当变倍组移动使系统倍率由 $\\beta_{\\min}$ 变到 $\\beta_{\\max}$ 时，补偿组按特定轨迹移动以保持最终像面固定。变倍比定义为：")+
   fml("\\Gamma_{\\text{变}} = \\frac{\\beta_{\\max}}{\\beta_{\\min}}")+
   p("补偿方式有机械补偿（变倍组与补偿组按凸轮曲线运动）与光学补偿（多组同向运动）两种。"))+
   app(p("<strong>应用：</strong>变焦镜头、变倍望远镜与机器视觉变焦系统均基于此原理；设计难点在于各焦距位置均须校正像差，且补偿曲线须保证像面稳定。"))
 )},
]},
]

# =====================================================
#  CHAPTER 3: 平面镜棱镜系统
# =====================================================
ch3_sections = [
{
"name": "3.1 平面镜与双平面镜",
"color": "#0d9488",
"desc": "平面镜成像、平面镜旋转特性与双平面镜（角镜）",
"items": [
{"id":"eo3s1-1","name":"平面镜成像性质","tags":["def","der"],"brief":"平面镜成等大正立的虚像，像物对称。",
 "body": wrap(
   defn("平面镜成像",p("平面镜对光的反射使物点发出的光束经反射后成为发散的同心光束，其反向延长线交于镜后一点，成虚像。像与物关于镜面对称，大小相等、正立、左右互换（镜像）。"))+
   der(p("<strong>推导（像距等于物距）：</strong>物点 $S$ 位于镜前距离 $u$。取两条入射光线，入射角均为 $\\theta$，由反射定律反射角也为 $\\theta$。设反射光线反向延长线交光轴于 $S'$，由相似三角形：")+
   fml("\\frac{h}{u} = \\tan\\theta,\\qquad \\frac{h}{v} = \\tan\\theta \\ \\Longrightarrow\\ v = u")+
   p("任意两条反射光线反向延长后都交于镜后与物等距的一点，故成等距虚像；因光线并未实际会聚，像为虚像。"))+
   note(p("平面镜的垂轴放大率 $\\beta=+1$，不改变像的大小与正倒，只改变光线方向；它是多数棱镜系统的等效元件。"))
 )},
{"id":"eo3s1-2","name":"平面镜旋转特性","tags":["thm","der","app"],"brief":"平面镜转 θ，反射光线转 2θ。",
 "fig":"mirror_rotate","figCap":"平面镜旋转 θ，反射光线偏转 2θ",
 "body": wrap(
   thm("平面镜旋转特性",p("入射光线方向不变，当平面镜绕垂直于入射面的轴旋转角度 $\\theta$ 时，反射光线同向旋转 $2\\theta$：")+
   fml("\\Delta\\varphi = 2\\theta"))+
   der(p("<strong>推导：</strong>设初始入射角为 $i$，反射角为 $i$。镜面转 $\\theta$ 后，法线转过 $\\theta$，新的入射角为 $i+\\theta$，新反射角也为 $i+\\theta$（相对新法线）。反射光线相对原反射光线的偏转角为入射光线方向改变量（0）与反射方向改变量之和：")+
   fml("\\Delta\\varphi = 2(i+\\theta) - 2i = 2\\theta")+
   p("结果与入射角无关，因此可用于把微小角位移放大为可观测的线位移：$\\Delta y = 2\\theta L$（$L$ 为镜到屏距离）。"))+
   app(p("<strong>应用：</strong>光学杠杆（灵敏电流计、原子力显微镜悬臂偏转检测）、激光扫描与准直中的角度放大测量均基于此特性。"))
 )},
{"id":"eo3s1-3","name":"双平面镜（角镜）","tags":["der","app"],"brief":"两镜夹角决定出射光偏转，与入射角无关。",
 "body": wrap(
   defn("双平面镜",p("由两个相交的平面反射镜组成的系统称为双平面镜（角镜）。两镜夹角为 $\\alpha$，光线依次在两镜上各反射一次后出射。"))+
   der(p("<strong>推导：</strong>设光线在两镜上的入射角分别为 $i_1,i_2$。经第一次反射光线偏转 $2i_1$，经第二次反射再偏转 $2i_2$（同一转向）。由两镜夹角与法线夹角的关系 $i_1+i_2=\\alpha$，出射光线相对入射光线的总偏转角为：")+
   fml("\\delta = 2i_1 + 2i_2 = 2\\alpha")+
   p("即出射光方向相对入射光的偏转恒为 $2\\alpha$，与入射角无关。当 $\\alpha=90°$ 时为 $180°$ 反向器；$\\alpha=45°$ 时为 $90°$ 转折器。"))+
   app(p("<strong>应用：</strong>直角屋脊反射器（$\\alpha=90°$）把光线反向折回，用于激光测距、自行车尾灯与光学陀螺；双平面镜还用于光路转折与合束。"))
 )},
]},
{
"name": "3.2 平行平板",
"color": "#14b8a6",
"desc": "平行平板的侧向位移、轴向位移与色散",
"items": [
{"id":"eo3s2-1","name":"平行平板的位移与色散","tags":["der","note"],"brief":"平行平板不改变方向，只产生位移与色差。",
 "body": wrap(
   defn("平行平板",p("两个相互平行的折射平面构成的玻璃板。光线两次折射后出射方向与入射方向平行，仅产生侧向位移。"))+
   der(p("<strong>侧向位移推导：</strong>板厚 $d$、折射率 $n$，入射角 $i$、折射角 $i'$（$\\sin i=n\\sin i'$）。光线在板内走的斜距为 $d/\\cos i'$，出射光相对入射光的侧移为：")+
   fml("\\Delta = \\frac{d\\,\\sin(i-i')}{\\cos i'} = d\\,\\sin i\\left(1-\\frac{\\cos i}{\\sqrt{n^2-\\sin^2 i}}\\right)")+
   p("<strong>轴向位移：</strong>近轴时平板使像面沿轴后移（等效厚度减小）：")+
   fml("\\Delta l' = d\\left(1-\\frac{1}{n}\\right)"))+
   note(p("<strong>色散：</strong>因 $n=n(\\lambda)$，不同波长的侧移 $\\Delta$ 不同，产生倍率色差；平行平板是插入光路（如分划板、滤光片）时引入色差的根源，设计时需加以补偿。"))
 )},
]},
{
"name": "3.3 反射棱镜",
"color": "#0f766e",
"desc": "直角棱镜、屋脊棱镜、道威棱镜与棱镜展开",
"items": [
{"id":"eo3s3-1","name":"直角棱镜","tags":["def","der"],"brief":"利用全反射转折光路的棱镜。",
 "fig":"right_prism","figCap":"直角棱镜使光路转折 90°",
 "body": wrap(
   defn("直角棱镜",p("截面为等腰直角三角形的棱镜，具有一个直角面和两个直角边面。利用直角面上的全反射实现光线转折，常用于 90° 或 180° 转折。"))+
   der(p("<strong>转折原理：</strong>光线垂直入射一直角边面（无偏折），在斜面上入射角 $45°$。若玻璃折射率满足 $\\sin45°\\ge1/n$（即 $n\\ge\\sqrt2\\approx1.414$），则发生全反射，反射光线垂直另一面出射，光路转折 $90°$：")+
   fml("\\theta_i = 45° \\ge \\theta_c = \\arcsin\\frac{1}{n} \\ \\Longrightarrow\\ n\\ge\\sqrt2")+
   p("若光线从斜面入射并在两个直角面上各全反射一次，则光路转折 $180°$。"))+
   note(p("与镀银反射镜相比，全反射棱镜无色差、反射率高、装调稳定，是望远镜转像、潜望镜与光学系统折转光路的核心元件。"))
 )},
{"id":"eo3s3-2","name":"屋脊棱镜","tags":["def","der"],"brief":"用屋脊面取代反射面以改变像的倒转。",
 "body": wrap(
   defn("屋脊棱镜",p("把一个反射面用两个互相垂直的反射面（屋脊面）代替，使该处由一次反射变为两次反射，从而改变像的倒正方向。屋脊面与棱镜光轴的交线称为屋脊棱。"))+
   der(p("<strong>屋脊两面反射的等效：</strong>屋脊面的两个反射面互为垂直，光线在其上依次反射两次，相当于绕屋脊棱方向旋转 $180°$ 的镜像变换。两次反射的合成相当于一次反射再翻转，使像在垂直于屋脊棱的方向倒转。"))+
   fml("\\text{屋脊面} = \\text{两次反射} \\ \\Longrightarrow\\ \\text{像的倒转次数增加一次}")+
   note(p("屋脊棱镜用于需要倒转像且要求系统结构紧凑的场合（如屋脊棱镜转像的望远镜、单反相机取景器）。屋脊面的垂直度误差会引起双像与像倾斜，加工要求高。"))
 )},
{"id":"eo3s3-3","name":"道威棱镜","tags":["def","der","app"],"brief":"可绕光轴旋转以倒转或旋转像。",
 "fig":"dove_prism","figCap":"道威棱镜及其像倒转特性",
 "body": wrap(
   defn("道威棱镜",p("一种截面为等腰梯形的反射棱镜，光线沿平行于棱镜长边的方向进入，在斜面上发生一次全反射后出射。其特点是棱镜绕光轴旋转时像随之旋转。"))+
   der(p("<strong>像旋转特性：</strong>光线在道威棱镜中经一次反射，像被倒转。当棱镜绕光轴旋转 $\\theta$ 时，由于其反射面的法线也随之转动，出射像的旋转角为棱镜转角的两倍：")+
   fml("\\varphi_{\\text{像}} = 2\\theta_{\\text{棱镜}}")+
   p("该关系与平面镜旋转特性（反射光转 2θ）同源，只是作用在像的方位上。"))+
   app(p("<strong>应用：</strong>道威棱镜用于需要调整像方位的系统（如周视望远镜、潜望镜），也常与旋转道威棱镜配合实现像旋转扫描；缺点是对光轴准直敏感。"))+
   note(p("<strong>与其他转像棱镜的比较：</strong>道威棱镜沿光轴放置，不改变光轴方向，但绕光轴旋转时使像以两倍角旋转；别汉棱镜与屋脊棱镜在折转光路的同时完成倒像转正。选用时须兼顾镜筒长度、光轴方向与装调精度。"))
 )},
{"id":"eo3s3-4","name":"棱镜展开与成像方向判断","tags":["def","der"],"brief":"把棱镜展开为玻璃平板以分析光路。",
 "body": wrap(
   defn("棱镜展开",p("把反射棱镜沿其反射面依次展开（镜像翻折），使反射光路变为直线传播，展开后的等效元件是一块玻璃平板，其厚度称为展开厚度。"))+
   der(p("<strong>展开法要点：</strong>光线在展开后的平板中沿直线传播，平板厚度 $L$ 等于光线在棱镜中各反射面间实际路径之和。对直角棱镜（腿长 $D$，光路在棱内转折 $90°$），展开后平板厚度为：")+
   fml("L = \\text{各段光路长度之和} = \\text{常数} \\times D")+
   p("展开法把棱镜对光束的限制、口径与像面位置转化为等效平板的计算，便于判断通光孔径与成像方向。"))+
   note(p("用展开法可确定棱镜的出射面口径、入射面位置及是否发生光束切割；结合三次反射方向规则可完整判定棱镜系统的成像方向。"))
 )},
]},
{
"name": "3.4 棱镜应用与判定",
"color": "#0891b2",
"desc": "成像方向判定、光楔、偏振分束与制造误差",
"items": [
{"id":"eo3s4-1","name":"棱镜系统成像方向判定","tags":["thm","der"],"brief":"三条规则判断反射棱镜系统的像方方向。",
 "body": wrap(
   thm("成像方向判定规则",p("设物方坐标系 $(x,y,z)$，$z$ 沿光轴。对反射棱镜系统：(1) 光轴方向 $z$ 经棱镜后方向不变（仍沿新光轴）；(2) 每经过一次反射，像的侧向（垂直于反射面与光轴）方向倒转一次；(3) 屋脊面相当于两次反射。合起来：奇数次反射使像的某一个方向倒转，偶数次反射使像的方位完全不变。"))+
   der(p("<strong>用反射矩阵推导：</strong>一次平面反射对光线方向的变换可用 Householder 型矩阵 $R=\\mathbf{I}-2\\mathbf{n}\\mathbf{n}^T$ 表示（$\\mathbf{n}$ 为反射面法线）。对右手坐标系，镜像反射使行列式为 $-1$，即一个方向倒转。两次反射的合成矩阵行列式为 $+1$，对应纯旋转。"))+
   fml("\\det(R) = -1\\ (\\text{一次反射，镜像})\\ ;\\qquad \\det(R_2 R_1) = +1\\ (\\text{两次反射，旋转})")+
   note(p("该规则用于判断棱镜转像系统是否给出与物一致的像方向。实际装调中还须考虑棱线方向与像倾斜，工程上常用棱镜转向符号法（如 $z$ 方向不变、$y$ 方向倒转）快速判定。"))
 )},
{"id":"eo3s4-2","name":"光楔及其应用","tags":["def","der","app"],"brief":"小顶角棱镜的偏向与光楔对。",
 "body": wrap(
   defn("光楔",p("顶角 $A$ 很小的折射棱镜称为光楔。光线近于垂直入射，偏向角很小，主要用于产生微小偏折或校正。"))+
   der(p("<strong>偏向角推导：</strong>对光楔，$A\\to0$，由最小偏向角公式或直接近轴展开 $\\delta\\approx(n-1)A$：")+
   fml("\\delta = (n-1)A")+
   p("两个光楔可反向组合：同向转动时光楔角相减、偏向角连续可调，用于精密的角度微调与光束平移；反向组合可构成消色差光楔（两个材料色散相抵）。"))+
   app(p("<strong>应用：</strong>光楔用于激光准直、光束偏转器、自准直前后的角度补偿；在天文与光谱仪器中用作色散补偿元件。"))
 )},
{"id":"eo3s4-3","name":"偏振分束棱镜（PBS）","tags":["def","der","app"],"brief":"把不同偏振态的光分离的棱镜。",
 "body": wrap(
   defn("偏振分束棱镜",p("偏振分束棱镜（PBS）由两块直角棱镜胶合而成，其胶合面镀有偏振分光膜。它把一束光分解为振动方向互相垂直的两束偏振光：p 光透射、s 光反射。"))+
   der(p("<strong>分光原理：</strong>在胶合界面处，p 偏振（电矢量平行于入射面）的等效折射率使其满足透射条件，而 s 偏振（电矢量垂直于入射面）在膜系中满足反射条件。以布儒斯特角工作的界面对 p 光几乎全透：")+
   fml("\\tan\\theta_B = \\frac{n_2}{n_1},\\qquad R_p\\approx0,\\quad R_s\\ \\text{较大}")+
   p("多层介质膜可把 s 光反射率提高到接近 $100\\%$，同时保持 p 光高透，从而实现高消光比的偏振分束。"))+
   app(p("<strong>应用：</strong>PBS 广泛用于偏振投影显示（LCD/LCoS）、光隔离器、激光加工、光通信与干涉测量中，是操控偏振态的关键元件。"))
 )},
{"id":"eo3s4-4","name":"反射棱镜制造误差的影响","tags":["def","der","note"],"brief":"角度与面形误差引起像倾斜、双像与光轴偏折。",
 "body": wrap(
   defn("棱镜误差",p("反射棱镜在加工与装调中会产生角度误差（棱镜角偏差、屋脊面垂直度）、面形误差与材料不均匀等，直接影响成像质量与光轴方向。"))+
   der(p("<strong>角度误差对光轴的影响：</strong>对单次反射的光路折转棱镜，反射面转角误差 $\\varepsilon$ 使反射光线偏转 $2\\varepsilon$；对屋脊棱镜，屋脊面垂直度误差 $\\delta$ 使两半光束分别偏转，形成双像，其角分离量约为：")+
   fml("\\Delta\\varphi \\approx 2n\\,\\delta")+
   p("对 $90°$ 直角棱镜，直角误差使光轴偏折约 $2n\\varepsilon$；对转像棱镜系统，多个面的角度误差会累积成像倾斜与光轴偏移。"))+
   note(p("减小误差的措施：提高棱镜角精度与屋脊面垂直度、采用胶合或光胶替代空气间隙、在装调中用自准直仪逐面校正；对成像系统还需把棱镜误差纳入总体公差分配。"))
 )},
]},
{
"name": "3.5 平板、别汉棱镜与回射器",
"color": "#14b8a6",
"desc": "平行平板等效空气层、别汉棱镜与角锥棱镜",
"items": [
{"id":"eo3s5-1","name":"平行平板的等效空气层","tags":["der","app"],"brief":"平板等效为减薄的空气层。",
 "body": wrap(
   der(p("<strong>等效空气层推导：</strong>由平行平板轴向位移 $\\Delta l'=d(1-1/n)$，即插入平板后像面沿轴后移 $\\Delta l'$。若把玻璃平板换成空气，为保持像面位置不变，空气层厚度应等于平板的等效光学长度：")+
   fml("d_{\\text{等效}} = d - \\Delta l' = \\frac{d}{n}")+
   p("因此插入厚度 $d$、折射率 $n$ 的平行平板，等效于一个厚度 $d/n$ 的空气层加上一段 $d(1-1/n)$ 的轴向位移。"))+
   app(p("<strong>应用：</strong>在光路中插入分划板、滤光片、棱镜或探测器窗口后，须用等效空气层重新计算像面位置并进行调焦补偿；这也是棱镜展开法进行光路计算的依据。"))
 )},
{"id":"eo3s5-2","name":"别汉棱镜（转像系统）","tags":["def","der"],"brief":"用于望远镜转像的棱镜组。",
 "body": wrap(
   defn("别汉棱镜",p("别汉棱镜由半五角棱镜与屋脊棱镜组合而成，光线在其中经过多次反射与一次屋脊面反射，可实现倒像转正，同时把光路折叠以缩短镜筒长度。"))+
   der(p("<strong>成像方向分析：</strong>别汉棱镜含一次屋脊面（等效两次反射）与若干次普通反射，总反射次数的奇偶性决定了像的倒正。按棱镜转向规则，光轴方向不变，屋脊面使垂直于屋脊棱的方向倒转，综合后把物镜所成的倒像转为正像：")+
   fml("\\text{总反射次数（屋脊面计两次）为偶数} \\ \\Longrightarrow\\ \\text{像方位与物一致（正像）}"))+
   note(p("别汉棱镜广泛用于双筒望远镜、枪瞄与观靶镜的转像系统，具有结构紧凑、光轴稳定的优点；屋脊面垂直度误差会引起双像与像倾斜，加工精度要求高。"))
 )},
{"id":"eo3s5-3","name":"角锥棱镜（回射器）","tags":["def","der","app"],"brief":"三面互相垂直，光线原方向返回。",
 "body": wrap(
   defn("角锥棱镜",p("角锥棱镜（回射器）由三个互相垂直的反射面（相当于一个立方体的一个角）构成，光线从底面入射，经三个面各反射一次后从底面出射。"))+
   der(p("<strong>回射原理：</strong>三个互相垂直的反射面对光线方向的作用相当于把入射方向矢量的三个分量同时反号，故出射光线方向与入射光线方向严格相反（沿原方向返回），与入射角无关：")+
   fml("\\mathbf{s}' = -\\mathbf{s}")+
   p("出射光平行于入射光且方向相反（偏离角恒为 $180°$），对棱镜的倾斜与光轴晃动不敏感。"))+
   app(p("<strong>应用：</strong>角锥棱镜用于激光测距、激光跟踪、干涉仪反射器与光学准直；三面直角棱镜（角反射器）在交通反光标识与月球激光反射器上也有广泛应用。"))
 )},
]},
]

# =====================================================
#  CHAPTER 4: 光束限制与光阑
# =====================================================
ch4_sections = [
{
"name": "4.1 孔径光阑与光瞳",
"color": "#c2410c",
"desc": "孔径光阑的确定、入瞳与出瞳",
"items": [
{"id":"eo4s1-1","name":"孔径光阑","tags":["def","der"],"brief":"限制轴上物点光束孔径的光阑。",
 "body": wrap(
   defn("光阑",p("光学系统中设置的对光束起限制作用的带孔金属片（或元件的边框、接收器边框）称为光阑。按作用不同分为孔径光阑、视场光阑、渐晕光阑与消杂光光阑。"))+
   defn("孔径光阑",p("限制轴上物点成像光束孔径（即决定进入系统的最大光束锥角）的光阑称为孔径光阑，它决定系统的通光能力与像面照度。"))+
   der(p("<strong>确定方法：</strong>把系统中每个光阑经其前面的光学系统成像到物方空间，得到各像（或光阑本身）。对轴上物点中心发出的光线，比较各个像对物点所张的孔径角 $u$，其中张角最小者对应的光阑即为孔径光阑：")+
   fml("u_{\\text{最小}} \\ \\Longrightarrow\\ \\text{该光阑为孔径光阑}")+
   p("因为张角最小的光阑最先切割轴上光束，它决定了进入系统的光束锥角，故为孔径光阑。"))+
   note(p("孔径光阑与物方、像方孔径角 $u$、$u'$ 直接相关；它与视场光阑分工不同：孔径光阑限制轴上点的光束粗细，视场光阑限制轴外点的成像范围。"))
 )},
{"id":"eo4s1-2","name":"入瞳与出瞳","tags":["def","der","thm"],"brief":"孔径光阑在物方、像方的共轭像。",
 "fig":"aperture","figCap":"孔径光阑与限制光束的边缘光线",
 "body": wrap(
   defn("入瞳与出瞳",p("孔径光阑经其前面光学系统所成的像称为入射光瞳（入瞳）；经其后面光学系统所成的像称为出射光瞳（出瞳）。入瞳限定了物方进入系统的光束，出瞳限定了像方的出射光束。"))+
   der(p("<strong>位置与大小的求法：</strong>设孔径光阑位于某面，其前面系统的物像关系已知。用理想系统公式求孔径光阑的像位置：")+
   fml("\\frac{1}{l_p'} - \\frac{1}{l_p} = \\frac{1}{f_{\\text{前}}'}")+
   p("像的直径即入瞳或出瞳的直径。入瞳与出瞳对系统而言互为共轭，二者满足物像关系，其放大率满足 $\\beta_p=D'/D$。"))+
   thm("光瞳的作用",p("入瞳是物方孔径角 $u$ 的起算点（入射光束的腰），出瞳是像方孔径角 $u'$ 的起算点；入瞳大小决定进入系统的光能量，出瞳与像面距离决定像面照度分布。"))+
   note(p("常见的入瞳、出瞳：单反相机镜头的光圈即孔径光阑，其入瞳为光圈经前组所成像，出瞳为经后组所成像；人眼瞳孔即入瞳与出瞳近似重合的孔径光阑。"))
 )},
]},
{
"name": "4.2 视场光阑与光窗",
"color": "#ea580c",
"desc": "视场光阑、入窗与出窗",
"items": [
{"id":"eo4s2-1","name":"视场光阑","tags":["def","der"],"brief":"限制物方成像范围的光阑。",
 "fig":"field_stop","figCap":"视场光阑限制物方视场角",
 "body": wrap(
   defn("视场光阑",p("限制物平面上能被系统成像的范围（即限制物方视场角）的光阑称为视场光阑。它通常是安置在中间像面或像面处的边框、分划板或探测器靶面。"))+
   der(p("<strong>视场角的确定：</strong>把各光阑（含孔径光阑的入瞳）经其前面系统成像到物方，比较它们对入瞳中心所张的角，其中最限制物方视场的光阑即为视场光阑。轴上点只受孔径光阑限制，轴外点将先被视场光阑遮拦。")+
   fml("2\\omega = 2\\arctan\\frac{y_{\\text{max}}}{l}")+
   p("其中 $2\\omega$ 为物方线视场对应的角视场，$y_{\\max}$ 为视场光阑半口径在物方的共轭高度。"))+
   note(p("视场光阑决定系统的成像范围：照相机的画幅框、显微镜目镜视场光阑、望远镜的视场光阑都决定了可观测的物方范围。"))
 )},
{"id":"eo4s2-2","name":"入窗与出窗","tags":["def","der"],"brief":"视场光阑在物方、像方的共轭像。",
 "body": wrap(
   defn("入窗与出窗",p("视场光阑经其前面光学系统所成的像称为入射窗（入窗）；经其后面光学系统所成的像称为出射窗（出窗）。入窗限制物方视场，出窗限制像方视场。"))+
   der(p("<strong>共轭关系：</strong>入窗、视场光阑与出窗三者依次共轭，其位置与大小由系统的物像关系确定：")+
   fml("\\beta_{\\text{窗}} = \\frac{D_{\\text{视场光阑}}}{D_{\\text{入窗}}},\\qquad \\text{视场光阑与入窗、出窗互为共轭}")+
   p("当视场光阑与入窗重合（视场光阑位于物方或前焦面）时，入窗与视场光阑重合；实际系统中视场光阑常位于中间像面，入窗是其经前组所成的像。"))+
   note(p("入窗、出窗与入瞳、出瞳共同限定了系统的成像范围与光束形状，是光束限制分析（渐晕、照度）的基础。"))
 )},
]},
{
"name": "4.3 渐晕",
"color": "#f97316",
"desc": "轴外点光束的渐晕与渐晕系数",
"items": [
{"id":"eo4s3-1","name":"渐晕与渐晕系数","tags":["def","der"],"brief":"轴外点光束被部分遮拦的现象。",
 "body": wrap(
   defn("渐晕",p("轴外点发出的、充满入瞳的光束，在通过系统时被除孔径光阑、视场光阑以外的其他光阑（渐晕光阑）部分遮拦，使实际通过的光束截面小于入瞳截面，这种现象称为渐晕。"))+
   der(p("<strong>渐晕系数：</strong>设轴上点光束的孔径为 $D$（入瞳直径），轴外点实际通过光束的孔径为 $D_k$，定义线渐晕系数：")+
   fml("K = \\frac{D_k}{D}")+
   p("用角量表示时定义几何渐晕系数 $K=\\tan u_k/\\tan u$（$u_k$ 为轴外点实际光束的孔径角）。当 $K=1$ 无渐晕，$K=0$ 时该点光束被完全遮拦。"))+
   note(p("工程上允许适当的渐晕（如 $K\\ge0.5$）以减小前组口径、降低成本，但会使像面照度由中心向边缘逐渐下降，需与照度要求折中。"))
 )},
]},
{
"name": "4.4 景深与焦深",
"color": "#d97706",
"desc": "景深公式推导与焦深",
"items": [
{"id":"eo4s4-1","name":"景深","tags":["def","der","app"],"brief":"物方能清晰成像的深度范围。",
 "fig":"dof","figCap":"景深：近景与远景之间的清晰成像范围",
 "body": wrap(
   defn("景深",p("在保持像面清晰的前提下，物平面可以沿轴前后移动的范围称为景深，分为近景深度 $\\Delta_1$ 与远景深度 $\\Delta_2$。其大小由容许弥散圆直径 $\\delta$、入瞳直径 $D$、对准距离 $p$ 决定。"))+
   der(p("<strong>景深公式推导：</strong>设物距为 $p$、入瞳直径 $D$、容许弥散圆直径 $\\delta$。物点沿轴移动到 $p+\\Delta_1$（靠近）时，成像弥散圆恰好等于 $\\delta$，由相似三角形：")+
   fml("\\frac{\\Delta_1}{D}=\\frac{\\delta}{D-\\delta}\\cdot\\frac{p+\\Delta_1}{p}\\ \\Longrightarrow\\ \\Delta_1 = \\frac{p\\,\\delta\\,D}{D+\\delta}")+
   p("同理物点远移 $\\Delta_2$ 时：$\\Delta_2=\\dfrac{p\\,\\delta\\,D}{D-\\delta}$（近似取 $p\\gg\\Delta$）。总景深 $\\Delta=\\Delta_1+\\Delta_2\\approx\\dfrac{2p\\,\\delta\\,D}{D^2-\\delta^2}$。"))+
   app(p("<strong>结论：</strong>光圈越小（$D$ 越小、F 数越大）、对准距离越远、容许弥散圆越大，景深越大。远景深度大于近景深度（$\\Delta_2>\\Delta_1$）；当 $D=\\delta$ 时远景深度趋于无穷，对应超焦距。"))+
   note(p("<strong>容许弥散圆的确定：</strong>$\\delta$ 通常取探测器像元尺寸或按其允许的模糊量确定，数字相机常取 $\\delta$ 等于 $1\\sim2$ 倍像元间距。当弥散圆接近衍射斑（$1.22\\lambda F$）时，实际清晰度还受衍射限制，须把景深与衍射极限一并考虑。"))
 )},
{"id":"eo4s4-2","name":"焦深","tags":["def","der"],"brief":"像方允许的离焦范围。",
 "body": wrap(
   defn("焦深",p("在物面固定的情况下，像平面沿轴前后移动而仍能保持像清晰的允许范围称为焦深，它是景深在像方的共轭量。"))+
   der(p("<strong>焦深推导：</strong>令像方容许弥散圆为 $\\delta'$，像方孔径角为 $u'$。像面离焦 $\\Delta'$ 时弥散圆直径不超过 $\\delta'$，由几何关系 $\\delta'=2\\Delta'\\tan u'$，故：")+
   fml("\\Delta' = \\frac{\\delta'}{2\\tan u'} \\approx \\frac{\\delta'}{2\\,u'} = \\delta'\\,F")+
   p("定义焦深为对称的允许范围 $\\Delta'_{\\text{总}}=2\\delta' F$（$F=f'/D$ 为 F 数）。F 数越大，焦深越大。"))+
   note(p("焦深与景深互为共轭：焦深越大对应的景深也越大。探测器（CCD/CMOS）的焦深关系到装配公差与调焦精度，是光学系统机械设计的重要依据。"))
 )},
]},
{
"name": "4.5 数值孔径与照明系统",
"color": "#b45309",
"desc": "数值孔径、光阑位置、场镜与照明、光能传递",
"items": [
{"id":"eo4s5-1","name":"数值孔径与相对孔径","tags":["def","der"],"brief":"表征系统集光与分辨能力的参数。",
 "body": wrap(
   defn("数值孔径",p("物方数值孔径定义为物方孔径角正弦与物方折射率之积：$\\mathrm{NA}=n\\sin u$。它表征系统收集光能与分辨细节的能力，对显微镜尤为重要。"))+
   defn("相对孔径与 F 数",p("入瞳直径 $D$ 与焦距 $f'$ 之比 $D/f'$ 称为相对孔径，其倒数 $F=f'/D$ 称为 F 数（光圈数）。"))+
   der(p("<strong>F 数与 NA 的关系：</strong>在物像空间均为空气、且物在有限远时，像方孔径角 $u'$ 满足 $\\tan u'=D/(2f')$（近似），故：")+
   fml("F = \\frac{f'}{D} = \\frac{1}{2\\tan u'} \\approx \\frac{1}{2\\mathrm{NA}'}")+
   p("相对孔径越大（F 数越小），进入系统的光能越多、分辨本领越高，但像差校正越困难。"))+
   note(p("照相物镜习惯用 F 数（如 F/2.8），显微物镜习惯用 NA（如 NA=0.9），二者本质相同，都是孔径的量度。"))
 )},
{"id":"eo4s5-2","name":"远心系统的光阑配置","tags":["der","app"],"brief":"光阑置于焦面构成远心光路。",
 "body": wrap(
   defn("远心光路",p("把孔径光阑安置在系统的像方焦平面或物方焦平面上，使主光线在物方或像方平行于光轴的光路。"))+
   der(p("<strong>从光阑角度分析：</strong>孔径光阑位于像方焦平面时，入瞳为其经前组所成像，位于物方无穷远，故主光线（过入瞳中心的光线）在物方平行于光轴——构成物方远心光路。此时物面沿轴离焦不改变像高，测量误差消除：")+
   fml("y' = \\beta\\,y\\ \\xrightarrow{\\ \\text{物方远心}\\ }\\ \\text{离焦时 } \\beta \\text{ 不变}")+
   p("反之，把光阑置于物方焦平面，则出瞳位于像方无穷远，出射主光线平行于光轴，构成像方远心光路，使像面照度均匀。"))+
   app(p("<strong>应用：</strong>工具显微镜、影像测量仪采用物方远心以消除调焦误差；遥感相机、均匀投影与照明系统采用像方远心以改善照度均匀性。"))
 )},
{"id":"eo4s5-3","name":"光阑位置对成像的影响","tags":["der","note"],"brief":"光阑位置改变影响孔径、渐晕与像差。",
 "body": wrap(
   der(p("<strong>光阑移动的影响：</strong>孔径光阑（或其入瞳、出瞳）沿轴移动时：(1) 物方孔径角 $u$ 与像方孔径角 $u'$ 改变，直接影响分辨率与照度；(2) 轴外光束的拦光量改变，从而改变渐晕与视场边缘照度；(3) 主光线在系统各面上的高度与入射角改变，影响像差（尤其轴外像差如彗差、像散、畸变）的校正。")+
   fml("u' \\uparrow \\Rightarrow \\mathrm{NA}\\uparrow,\\ \\text{分辨本领}\\uparrow,\\ \\text{但像差校正难度}\\uparrow")+
   p("把光阑（入瞳）前置或后置还会改变主光线走向：入瞳远离系统时主光线趋于平行，有利于轴外像差的平衡。"))+
   note(p("实际设计中常通过光阑（光阑面）位置与形状的优化来平衡像差、控制渐晕与照度；对称型物镜即利用光阑位置使前后组像差相互抵消。"))
 )},
{"id":"eo4s5-4","name":"场镜与照明系统","tags":["def","der","app"],"brief":"场镜与柯勒/临界照明。",
 "body": wrap(
   defn("场镜",p("安置在物面或中间像面附近、与像面重合的透镜（或透镜组）称为场镜。它不改变成像放大率，但可把主光线折向光轴，从而缩小其后光学元件的口径、降低渐晕与像差负担。"))+
   der(p("<strong>柯勒照明原理：</strong>柯勒照明中，光源经集光镜后成像于系统的入瞳（孔径光阑）处，而物面由另一组透镜均匀照明。设入瞳位置为光源像的位置，则物面上每一点的照明由光源整体提供：")+
   fml("\\text{光源} \\to \\text{成像于入瞳}\\ ;\\qquad \\text{入瞳} \\to \\text{成像于物面照明的均匀化}")+
   p("临界照明则把光源直接成像于物面，结构简单但光源不均匀性会反映到物面；柯勒照明用两组成像关系把光源不均匀性均匀化，照明更均匀。"))+
   app(p("<strong>应用：</strong>显微照明、投影照明、机器视觉光源普遍采用柯勒照明；场镜用于大视场系统（如目镜、中继系统）以压缩主光线高度。"))
 )},
{"id":"eo4s5-5","name":"光能传递与像面照度","tags":["der","note"],"brief":"像面照度与孔径角、透过率的关系。",
 "body": wrap(
   der(p("<strong>轴上像点照度：</strong>设物面亮度为 $L$、系统透过率为 $\\tau$、像方孔径角为 $u'$，则轴上像点的照度为：")+
   fml("E' = \\pi L\\tau\\sin^{2}u'")+
   p("可见照度与像方孔径角的正弦平方成正比，即与 $\\mathrm{NA}'^{2}$ 成正比，因此增大孔径是提高像面照度的主要途径。")+
   p("<strong>轴外照度（余弦四次方定律）：</strong>轴外视场角为 $\\omega$ 处，考虑口径投影、距离与出射角变化，照度按 $\\cos^4\\omega$ 衰减：")+
   fml("E'(\\omega) = E'_0\\cos^{4}\\omega"))+
   note(p("渐晕会进一步加剧边缘照度下降；工程上用渐晕、像差平衡与探测器灵敏度补偿来控制全视场照度均匀性。"))
 )},
]},
{
"name": "4.6 视场、超焦距与照度均匀化",
"color": "#ea580c",
"desc": "线视场与角视场、超焦距、像面照度均匀化",
"items": [
{"id":"eo4s6-1","name":"线视场与角视场","tags":["def","der"],"brief":"物方线视场与角视场的换算。",
 "body": wrap(
   defn("视场的两种表示",p("系统的成像范围可用物方线视场（物平面上可成像区域的直径 $2y$）或用角视场（对应的张角 $2\\omega$）表示，二者由物距 $l$ 联系。"))+
   der(p("<strong>换算关系：</strong>当物位于有限距离 $l$ 处时，物方线视场半高与角视场的关系为：")+
   fml("y = l\\tan\\omega,\\qquad 2y = 2l\\tan\\omega")+
   p("对物在无穷远的望远系统，只能用角视场 $2\\omega$ 描述；对投影与显微系统，常用物方线视场。物方线视场与像方线视场之比等于垂轴放大率，即 $2y'=2y\\cdot\\beta$。"))+
   note(p("视场与孔径共同决定系统的信息量，也是光学扩展量（étendue）的组成部分；增大视场往往使轴外像差（像散、场曲、畸变）与渐晕加大。"))
 )},
{"id":"eo4s6-2","name":"超焦距","tags":["der","app"],"brief":"使远景深度趋于无穷的对焦距离。",
 "body": wrap(
   der(p("<strong>超焦距推导：</strong>由景深公式 $\\Delta_2=\\dfrac{p\\,\\delta\\,D}{D-\\delta}$，当分母中的 $D\\to\\delta$（入瞳直径等于容许弥散圆直径）时远景深度趋于无穷。对应的物距定义为超焦距 $H$：")+
   fml("H = \\frac{f'^{2}}{F\\,\\delta}")+
   p("当物镜对焦于超焦距 $H$ 时，从 $H/2$ 到无穷远的景物都落在景深范围内，这是大景深（泛焦）拍摄的常用策略。"))+
   app(p("<strong>应用：</strong>风景摄影、监控相机常把对焦设在超焦距以获得最大清晰范围；F 数越大、容许弥散圆越大，超焦距越小、景深越大。"))
 )},
{"id":"eo4s6-3","name":"像面照度均匀化","tags":["der","app"],"brief":"控制轴外照度下降的措施。",
 "body": wrap(
   der(p("<strong>措施与原理：</strong>轴外照度按 $\\cos^4\\omega$ 下降，可用多种方法改善：(1) 采用像方远心光路减小口径投影损失；(2) 适当引入渐晕以平衡照度与口径成本；(3) 加入场镜压缩主光线高度；(4) 用探测器增益或图像处理补偿。综合后的相对照度可写为：")+
   fml("E'(\\omega) = E'_0\\cos^{4}\\omega\\cdot K_{\\text{渐晕}}\\cdot K_{\\text{补偿}}")+
   p("其中 $K_{\\text{渐晕}}$ 为渐晕引起的衰减，$K_{\\text{补偿}}$ 为探测器或后处理的补偿因子。"))+
   app(p("<strong>应用：</strong>相机、手机镜头、遥感相机与投影系统都要给出相对照度曲线（相对照度图）作为验收指标，并通过上述措施把边缘照度保持在中心的一定比例以上。"))
 )},
]},
]

# =====================================================
#  CHAPTER 5: 像差理论
# =====================================================
ch5_sections = [
{
"name": "5.1 像差概述",
"color": "#be185d",
"desc": "实际光学系统偏离理想成像的原因与像差分类",
"items": [
{"id":"eo5s1-1","name":"像差概述","tags":["def","der"],"brief":"实际系统偏离理想成像的偏差及其分类。",
 "body": wrap(
   defn("像差",p("实际光学系统在非近轴、有限孔径与有限视场条件下所成的像，与理想像之间存在偏差，这种偏差称为像差。像差使像点扩散成弥散斑，降低清晰度与位置精度。"))+
   defn("像差分类",p("单色光成像的像差称为单色像差，包括球差、彗差、像散、场曲与畸变；复色光成像还产生色差，分为位置色差与倍率色差。前五种中，球差与彗差为轴上或近轴像差，像散、场曲与畸变为轴外像差。"))+
   der(p("<strong>由泰勒展开看像差来源：</strong>折射定律 $n\\sin\\theta=n'\\sin\\theta'$，把正弦展开：")+
   fml("\\sin\\theta = \\theta - \\frac{\\theta^3}{6} + \\frac{\\theta^5}{120} - \\cdots")+
   p("近轴近似仅保留一阶项 $n\\theta=n'\\theta'$，得到理想成像。保留高阶项后，实际光线与理想光线的偏离正比于孔径与视场的高次幂，即形成各阶像差。以波像差表示，展开为孔径坐标 $\\rho$ 与视场坐标的幂级数：")+
   fml("W(\\rho,\\theta) = W_{040}\\rho^4 + W_{131}\\rho^3\\cos\\theta + W_{222}\\rho^2\\cos^2\\theta + W_{220}\\rho^2 + W_{311}\\rho\\cos\\theta"))+
   note(p("上式中各项依次对应球差、彗差、像散、场曲、畸变，均为初级（赛德尔）像差。实际系统需在各种像差之间权衡，使综合像质达到要求。"))
 )},
]},
{
"name": "5.2 单色像差",
"color": "#db2777",
"desc": "球差、彗差、像散、场曲与畸变",
"items": [
{"id":"eo5s2-1","name":"球差","tags":["def","der","app"],"brief":"轴上点不同孔径光线焦点不同。",
 "fig":"spherical_aber","figCap":"球差：边缘光线焦点较近轴焦点更近",
 "body": wrap(
   defn("球差",p("轴上物点发出的、不同孔径（不同 $u$）的光线经系统后交于光轴不同位置，边缘光线与近轴光线焦点不重合，这种轴向差异称为轴向球差；同一像面上的弥散构成垂轴球差。"))+
   der(p("<strong>轴向球差与波像差：</strong>边缘光线交点 $L'$ 与近轴焦点 $l'$ 之差定义为轴向球差：")+
   fml("\\delta L' = L' - l'")+
   p("其波像差为孔径的四次项 $W_{040}\\rho^4$，故球差是孔径的偶函数，对孔径正方对称。初级球差与孔径的平方相关：")+
   fml("\\delta L' = a\\,u^2")+
   p("球差使轴上点弥散成圆斑，降低分辨率与对比度。"))+
   app(p("<strong>校正：</strong>正透镜的球差与负透镜相反，用正、负透镜组合可校正球差；单透镜可用配曲（改变两面的曲率分配）使球差最小；非球面可直接消除球差。"))+
   note(p("<strong>球差的表征：</strong>工程上用轴向球差曲线 $\\delta L'(u)$、垂轴球差曲线与光线扇形图（ray fan）表示；当球差随孔径出现正负交替的极值时对应最佳校正状态。球差过大会使弥散斑明显增大，从而降低调制传递函数。"))
 )},
{"id":"eo5s2-2","name":"彗差","tags":["def","der"],"brief":"轴外点光束的不对称弥散。",
 "fig":"coma","figCap":"彗差：轴外点弥散成彗星状",
 "body": wrap(
   defn("彗差",p("轴外点发出的、充满入瞳的宽光束经系统后，在像面上形成一端明亮、一端弥散的彗星状光斑，这种不对称像差称为彗差。它反映光束对主光线的不对称性，与孔径和视场均有关。"))+
   der(p("<strong>彗差与孔径、视场的关系：</strong>彗差的波像差含 $\\rho^3\\cos\\theta$ 项，即孔径坐标的三次项且对主光线不对称：")+
   fml("W_{131} = B\\,\\rho^{3}\\cos\\theta")+
   p("弥散斑的垂轴尺寸正比于视场 $y$ 与孔径平方 $u^2$，故彗差随视场线性增大、随孔径平方增大；它与球差同为宽光束像差，缩小孔径可显著减小彗差。"))+
   note(p("彗差在宽光束轴上或近轴成像中最为显著（如抛物面镜在离轴时的彗差）。校正方法是使系统满足正弦条件 $n\\,y\\,\\sin u = n'\\,y'\\,\\sin u'$（等晕条件），或用对称结构自动消除彗差。"))
 )},
{"id":"eo5s2-3","name":"像散","tags":["def","der"],"brief":"子午与弧矢光束焦点分离。",
 "fig":"astig_curv","figCap":"像散与场曲：子午、弧矢焦线分离",
 "body": wrap(
   defn("像散",p("轴外点发出的光束，其子午面（含主光线的平面）内光线与弧矢面（垂直于子午面的平面）内光线聚焦于不同位置，形成两条互相垂直的焦线，这种像差称为像散。两焦线之间的最小弥散圆处成像最清晰。"))+
   der(p("<strong>像散差的量度：</strong>子午焦点位置 $x_t'$ 与弧矢焦点位置 $x_s'$ 之差定义为像散差：")+
   fml("\\Delta x' = x_t' - x_s'")+
   p("像散的波像差含 $\\rho^2\\cos^2\\theta$ 项，其大小与视场平方 $y^2$ 成正比、与孔径平方 $u^2$ 成正比：")+
   fml("W_{222} = C\\,\\rho^{2}\\cos^{2}\\theta")+
   p("像散使轴外点沿不同方向有不同清晰度（一个方向清晰、另一方向模糊）。"))+
   note(p("校正像散需要在系统中引入与像散相反的贡献（如厚透镜、分离透镜组）；人眼的像散是角膜两方向曲率不同所致，用柱面镜（散光镜）校正。"))
 )},
{"id":"eo5s2-4","name":"场曲","tags":["def","der"],"brief":"清晰像面为弯曲曲面。",
 "body": wrap(
   defn("场曲",p("实际光学系统中，能清晰成像的点所构成的像面不是一个平面，而是一个弯曲的曲面，称为场曲（像面弯曲）。即使校正了像散，子午、弧矢焦面仍可能弯曲。"))+
   der(p("<strong>匹兹伐场曲：</strong>对薄透镜系统，场曲由各光组的焦距与折射率决定。匹兹伐和给出场曲曲率：")+
   fml("\\frac{1}{r_p} = -\\sum_i \\frac{\\Phi_i}{n_i}")+
   p("匹兹伐场曲仅与各光组的光焦度和折射率有关，与光阑位置无关；而像散场曲还受光阑位置影响。二者之和构成实际场曲。"))+
   note(p("校正场曲的方法：采用高折射率、低光焦度的正透镜与负透镜组合使匹兹伐和减小；或使用厚弯月透镜、场镜把像面压平。平场物镜（平场消色差、平场复消色差）即为此设计。"))
 )},
{"id":"eo5s2-5","name":"畸变","tags":["def","der","app"],"brief":"放大率随视场变化导致像变形。",
 "fig":"distortion","figCap":"畸变：方物成像为枕形或桶形",
 "body": wrap(
   defn("畸变",p("由于垂轴放大率随视场变化，轴外点的实际像高与理想像高不等，使像产生几何变形，这种像差称为畸变。畸变不改变像的清晰度，只改变像的形状。"))+
   der(p("<strong>畸变与视场的关系：</strong>设理想像高为 $y_0'$、实际像高为 $y'$，定义畸变：")+
   fml("\\delta y' = y' - y_0',\\qquad \\text{相对畸变} = \\frac{y' - y_0'}{y_0'}\\times100\\%")+
   p("畸变的波像差含 $\\rho\\cos\\theta$ 项，且与视场三次方 $y^3$ 成正比：$W_{311}=E\\,\\rho^{3}\\cos\\theta\\cdot y^{3}$。$\\delta y'>0$（放大率随视场增大）为枕形畸变，$\\delta y'<0$ 为桶形畸变。"))+
   app(p("<strong>校正：</strong>畸变与光阑位置密切相关，把光阑置于系统中心（对称结构光阑居中）可自动消畸变；全对称型光路（如双高斯物镜）对畸变、倍率色差有很好的校正。测量与测绘镜头对畸变要求严格。"))
 )},
]},
{
"name": "5.3 色差",
"color": "#e11d48",
"desc": "位置色差与倍率色差",
"items": [
{"id":"eo5s3-1","name":"位置色差","tags":["def","der","app"],"brief":"不同波长光轴向焦点不同。",
 "body": wrap(
   defn("位置色差",p("由于光学材料的折射率随波长变化（色散），同一物点发出的不同波长光经系统后交点沿轴不同，形成轴向（位置）色差，使轴上点呈现彩色弥散。"))+
   der(p("<strong>色差的量度：</strong>以 F 光（486.1 nm）与 C 光（656.3 nm）的焦点之差表示位置色差：")+
   fml("\\Delta l'_{FC} = l'_F - l'_C")+
   p("对单透镜，$f'$ 随 $n$ 变化 $\\dfrac{\\mathrm{d}f'}{f'} = -\\dfrac{\\mathrm{d}n}{n-1}$，故色差正比于焦距与材料色散 $\\Delta n$。正透镜 $\\Delta l'_{FC}<0$，负透镜相反。"))+
   app(p("<strong>消色差：</strong>用不同色散的材料（如冕玻璃正透镜 + 火石玻璃负透镜）胶合成双胶合消色差透镜，使两种波长焦点重合（消色差）；进一步使三色光焦点重合为复消色差（apochromatic）。"))
 )},
{"id":"eo5s3-2","name":"倍率色差","tags":["def","der"],"brief":"不同波长光的像高不同。",
 "body": wrap(
   defn("倍率色差",p("由于系统的垂轴放大率随波长变化，不同波长的光所成的像高不同，使轴外点成像出现彩色边缘，这种色差称为倍率色差（垂轴色差）。"))+
   der(p("<strong>量度与校正：</strong>以 F 光与 C 光的像高之差表示倍率色差：")+
   fml("\\Delta y'_{FC} = y'_F - y'_C")+
   p("倍率色差与视场成正比，只影响轴外像点；它使像的边缘出现彩边。校正的方法是用对称型结构（光阑居中），使前后组产生符号相反的倍率色差而相互抵消。"))+
   note(p("位置色差与倍率色差往往同时存在。消色差物镜对位置色差进行校正，而全消色差、复消色差物镜则同时控制两种色差，用于高倍显微与精密测量。"))
 )},
]},
{
"name": "5.4 波像差与赛德尔像差",
"color": "#ec4899",
"desc": "波像差、瑞利判据与初级像差多项式",
"items": [
{"id":"eo5s4-1","name":"波像差与瑞利判据","tags":["def","thm","der"],"brief":"波面偏差及其容许标准。",
 "body": wrap(
   defn("波像差",p("实际出射波面与理想球面波之间的光程差称为波像差，记为 $W$。它从波面角度统一描述各种几何像差，是评价光学系统质量的重要指标。"))+
   der(p("<strong>波像差与几何像差的关系：</strong>波像差是折射率沿光路变化的积累：")+
   fml("W = \\int \\Delta n\\,\\mathrm{d}s")+
   p("几何像差与波像差满足梯度关系（横向像差正比于波像差对孔径坐标的偏导数）：$\\Delta y' = -\\dfrac{R}{n'}\\dfrac{\\partial W}{\\partial \\rho}$。"))+
   thm("瑞利判据",p("当光学系统的最大波像差小于四分之一波长时，系统的成像质量与理想系统相比没有显著差别：")+
   fml("W_{\\max} \\le \\frac{\\lambda}{4}")+
   p("该判据是光学设计中最常用的像质公差准则，对应斯特列尔比 $\\ge0.8$。"))+
   note(p("瑞利判据给出了“完善成像”的定量标准；实际系统中常以其为界限分配各像差与制造公差。"))
 )},
{"id":"eo5s4-2","name":"赛德尔像差多项式","tags":["thm","der"],"brief":"初级像差的统一波像差展开。",
 "body": wrap(
   thm("赛德尔像差多项式",p("在初级（三阶）近似下，波像差可按孔径坐标 $\\rho$ 与视场坐标表示为：")+
   fml("W = W_{040}\\rho^4 + W_{131}\\rho^3\\cos\\theta + W_{222}\\rho^2\\cos^2\\theta + W_{220}\\rho^2 + W_{311}\\rho\\cos\\theta"))+
   der(p("<strong>各项含义：</strong>逐项对应五种初级单色像差：$W_{040}$ 球差（与孔径四次方成正比，与视场无关）；$W_{131}$ 彗差（孔径三次方、视场一次）；$W_{222}$ 像散（孔径二次方、视场二次）；$W_{220}$ 场曲（孔径二次方，属匹兹伐与像散场曲）；$W_{311}$ 畸变（孔径一次、视场三次）。")+
   fml("\\text{球差}:\\rho^4\\ ;\\ \\text{彗差}:\\rho^3\\cos\\theta\\ ;\\ \\text{像散}:\\rho^2\\cos^2\\theta\\ ;\\ \\text{场曲}:\\rho^2\\ ;\\ \\text{畸变}:\\rho\\cos\\theta"))+
   note(p("赛德尔多项式是光学设计的理论基础，各系数由系统的结构参数（曲率、厚度、折射率、光阑位置）决定。高阶像差可用更高阶的幂级数补充。"))
 )},
]},
{
"name": "5.5 像质评价",
"color": "#9d174d",
"desc": "像差校正与平衡、点列图与传递函数",
"items": [
{"id":"eo5s5-1","name":"像差的校正与平衡","tags":["der","app"],"brief":"通过互相平衡获得最佳综合像质。",
 "body": wrap(
   der(p("<strong>像差平衡原理：</strong>实际系统往往不能把每种像差单独校正到零，而利用各像差之间的相互补偿使综合弥散最小。例如：球差可通过对透镜配曲或正负透镜组合校正；彗差、畸变、倍率色差可用对称型结构自动消除；色差用双胶合消色差透镜校正。")+
   fml("\\text{综合取舍：} \\sqrt{\\sum_i \\text{像差}_i^2}\\ \\text{最小}")+
   p("校正顺序一般为：先校正位置色差、球差、彗差等轴上与近轴像差，再平衡像散、场曲、畸变等轴外像差；同时兼顾孔径、视场与结构紧凑性。"))+
   app(p("<strong>方法：</strong>经典设计依靠像差理论计算与人工平衡，现代设计借助光学设计软件（Zemax、Code V）自动优化，用评价函数（含波像差、点列图、MTF 等）驱动参数迭代。"))
 )},
{"id":"eo5s5-2","name":"点列图","tags":["def","der"],"brief":"弥散斑的几何分布评价。",
 "body": wrap(
   defn("点列图",p("点列图（spot diagram）是把物点发出的多条实际光线追迹到像面上，标出各光线与像面交点的几何分布图。它直观反映弥散斑的大小与形状。"))+
   der(p("<strong>定量指标：</strong>常用均方根（RMS）半径与几何半径描述弥散斑大小：")+
   fml("\\text{RMS} = \\sqrt{\\frac{1}{N}\\sum_{i=1}^{N}\\left[(x_i-\\bar{x})^2+(y_i-\\bar{y})^2\\right]}")+
   p("弥散斑大小与衍射极限（艾里斑半径 $1.22\\lambda\\,F$）比较，可判断系统是几何像差受限还是衍射受限。"))+
   note(p("点列图计算简便、直观，但只反映几何光线分布，未计入衍射；当弥散斑接近艾里斑时须改用波像差或 MTF 评价。"))
 )},
{"id":"eo5s5-3","name":"光学传递函数（MTF）","tags":["def","der","app"],"brief":"以空间频率描述系统传递能力。",
 "fig":"mtf","figCap":"调制传递函数曲线（MTF）",
 "body": wrap(
   defn("光学传递函数",p("把系统视为线性空间不变系统，用正弦光栅作为输入，像的对比度与相位随空间频率的变化关系。其模称为调制传递函数（MTF），辐角称为相位传递函数（PTF）。"))+
   der(p("<strong>从点扩散函数推导：</strong>系统对点物的响应为点扩散函数 $\\mathrm{PSF}(x,y)$，其傅里叶变换为光瞳函数 $P$ 的自相关（光学传递函数）：")+
   fml("\\mathrm{OTF}(f_x,f_y) = \\mathcal{F}\\{\\mathrm{PSF}\\} = \\frac{P\\star P}{\\iint|P|^2}")+
   p("其模即 MTF：$\\mathrm{MTF}(f)=M'(f)/M(f)$，表示该空间频率处对比度的传递比率。衍射受限系统 MTF 有理论上限，实际系统因像差而低于上限。"))+
   app(p("<strong>应用：</strong>MTF 是镜头、望远系统与成像链条最综合的像质评价指标，把衍射、像差、装配误差统一到空间频率响应中；工程上常给出指定空间频率（如 50 lp/mm）的 MTF 值作为验收标准。"))
 )},
]},
{
"name": "5.6 高级像差与波前检验",
"color": "#db2777",
"desc": "二级光谱、复消色差与波前测量",
"items": [
{"id":"eo5s6-1","name":"二级光谱与复消色差","tags":["def","der"],"brief":"消色差后残余的色差与复消色差。",
 "body": wrap(
   defn("二级光谱",p("普通消色差透镜使 F 光与 C 光焦点重合后，其他波长（如 d 光或 g 光）的焦点仍与之不同，这种残余色差称为二级光谱（残余色差）。"))+
   der(p("<strong>成因与校正：</strong>消色差只校正了两个波长，色差曲线仍然弯曲。二级光谱的大小与玻璃的相对部分色散 $P$ 有关，可表示为：")+
   fml("\\Delta l'_{\\text{二级}} \\propto f'\\,\\frac{P_1-P_2}{V_1-V_2}")+
   p("要减小二级光谱须选用部分色散差很小的特种玻璃（如萤石、ED 玻璃）或晶体，使三个乃至更多波长焦点重合，即实现复消色差。"))+
   note(p("复消色差（apochromatic）物镜用于高倍显微、天文与精密测量；二级光谱是限制宽波段（可见到近红外）成像质量的重要因素。"))
 )},
{"id":"eo5s6-2","name":"波前测量与干涉检验","tags":["der","app"],"brief":"用干涉法测量波像差以检验系统。",
 "body": wrap(
   der(p("<strong>干涉测量原理：</strong>把被测系统的出射波面与参考波面叠加，产生干涉条纹。条纹形状反映两波面的光程差，即波像差 $W$：")+
   fml("\\Delta W = \\frac{\\lambda}{2}\\,\\Delta N")+
   p("其中 $\\Delta N$ 为条纹移动数。用干涉仪（如泰曼-格林、斐索干涉仪）测出波面后，可按 Zernike 多项式展开，得到离焦、像散、彗差、球差等各阶像差系数。"))+
   app(p("<strong>应用：</strong>波前干涉检验用于光学元件面形检测（球面、非球面）、系统像质检验与自适应光学波前传感；Zernike 系数是评价波前质量的标准化描述。"))
 )},
]},
]

# =====================================================
#  CHAPTER 6: 典型光学系统
# =====================================================
ch6_sections = [
{
"name": "6.1 放大镜",
"color": "#0891b2",
"desc": "视角放大率及其推导",
"items": [
{"id":"eo6s1-1","name":"放大镜的视角放大率","tags":["def","der","app"],"brief":"放大镜把近物视角放大的能力。",
 "body": wrap(
   defn("放大镜",p("放大镜是短焦距的正透镜，把物体置于其物方焦点内侧（或焦点处），使物在明视距离处或无穷远处成放大的虚像，便于眼睛观察细节。"))+
   der(p("<strong>视角放大率推导：</strong>视角放大率定义为像对眼睛张角的正切与物在明视距离（$D=250\\,\\text{mm}$）处直接观察时张角的正切之比。当像成在无穷远（物位于物方焦平面）时，物高 $y$ 的视角 $\\tan\\omega'=y/f'$；不用放大镜时物置于明视距离，$\\tan\\omega=y/250$：")+
   fml("\\Gamma = \\frac{\\tan\\omega'}{\\tan\\omega} = \\frac{250}{f'}")+
   p("若像成在明视距离处（物略置于焦点内侧），放大率可略大于 $250/f'$（约 $250/f'+1$）。"))+
   app(p("<strong>结论：</strong>放大镜的放大率与焦距成反比，焦距越短放大率越高；但受像差、工作距离与人眼调节能力限制，单透镜放大镜通常不超过 $20\\times$。放大镜常用于读数、检验与低倍观察。"))
 )},
]},
{
"name": "6.2 显微镜",
"color": "#06b6d4",
"desc": "显微镜放大率、数值孔径与分辨率",
"items": [
{"id":"eo6s2-1","name":"显微镜的放大率与数值孔径","tags":["def","der"],"brief":"物镜与目镜组合的放大能力。",
 "fig":"microscope","figCap":"显微镜光路：物镜与目镜两次放大",
 "body": wrap(
   defn("显微镜",p("显微镜由物镜与目镜组成：物镜把近物成一放大的实像于目镜的物方焦平面附近，目镜再把这实像放大成虚像供眼睛观察，实现两次放大。"))+
   der(p("<strong>放大率推导：</strong>设物镜垂轴放大率为 $\\beta$，目镜视角放大率为 $\\Gamma_{\\text{目}}$，显微镜总视角放大率为二者之积。物镜的光学筒长（物镜像方焦点到目镜物方焦点距离）为 $\\Delta$，物方焦距 $f_1'$、目镜焦距 $f_2'$：")+
   fml("\\Gamma = \\beta\\cdot\\Gamma_{\\text{目}} = -\\frac{\\Delta\\cdot 250}{f_1' f_2'}")+
   p("显微镜的物方数值孔径 $\\mathrm{NA}=n\\sin u$ 决定其分辨能力与集光能力，是显微物镜的首要参数。"))+
   note(p("常用物镜标注如 $40\\times/0.65$ 表示放大率 $40\\times$、数值孔径 $0.65$；高倍物镜采用浸液（油浸）以提高 $n$ 与 NA。"))+
   app(p("<strong>照明与场镜：</strong>显微系统在物镜与目镜之间常设场镜以压缩主光线高度、减小目镜口径，照明采用柯勒照明保证物面照度均匀。物镜按用途分为消色差、平场消色差与复消色差，分别对应不同的色差与场曲校正水平。"))
 )},
{"id":"eo6s2-2","name":"显微镜的分辨率","tags":["def","der","note"],"brief":"由数值孔径与波长决定的极限分辨距离。",
 "body": wrap(
   defn("显微镜分辨率",p("显微镜能分辨的两物点间的最小距离称为极限分辨距离。由于衍射，物点成像为艾里斑，两斑过近则无法区分。"))+
   der(p("<strong>分辨率公式：</strong>由瑞利判据，圆孔衍射极限分辨距离为：")+
   fml("\\delta = \\frac{0.61\\lambda}{\\mathrm{NA}}")+
   p("可见提高分辨率有两个途径：增大数值孔径（增大孔径角或浸液提高 $n$）与减小波长（紫外显微）。当物被斜照明时，分辨率可提高至 $\\delta=\\lambda/(2\\mathrm{NA})$。"))+
   note(p("受衍射限制，光学显微镜的极限分辨距离约 $200\\,\\text{nm}$（NA=1.4、$\\lambda=550\\,\\text{nm}$），这一衍射极限催生了电子显微镜与近场光学显微镜等超分辨技术。"))
 )},
]},
{
"name": "6.3 望远镜",
"color": "#0e7490",
"desc": "开普勒与伽利略望远镜、放大率与分辨率",
"items": [
{"id":"eo6s3-1","name":"开普勒与伽利略望远镜","tags":["def","der"],"brief":"两种目视望远系统的结构与特点。",
 "fig":"telescope","figCap":"开普勒望远镜：物镜与目镜共焦",
 "body": wrap(
   defn("开普勒望远镜",p("由长焦距正物镜与短焦距正目镜组成，二者像方焦点与物方焦点重合。物镜把无穷远物成一倒立实像于焦平面，目镜再放大为虚像，故观察到的是倒立像；加转像棱镜（如别汉棱镜、屋脊棱镜）后成正立像。"))+
   defn("伽利略望远镜",p("由正物镜与负目镜组成，物镜的像方焦点与目镜的物方焦点重合，物镜所成的发散光束直接由负目镜变为平行光射出，中间无实像，故看到的是正立像。"))+
   der(p("<strong>共焦条件：</strong>两系统均要求物镜像方焦面与目镜物方焦面重合，即镜筒长度分别为 $L=f_1'+f_2'$（开普勒）与 $L=f_1'-|f_2'|$（伽利略）：")+
   fml("L_{\\text{开普勒}} = f_1' + f_2',\\qquad L_{\\text{伽利略}} = f_1' - |f_2'|"))+
   note(p("开普勒望远镜有中间实像，可安装分划板与转像棱镜，视场大，是军用与天文望远镜的主流；伽利略望远镜结构短、成正立像，但视场小、无实像位置，多用于观剧镜与低倍望远镜。"))
 )},
{"id":"eo6s3-2","name":"望远镜的放大率与分辨率","tags":["der","app"],"brief":"视角放大率与衍射极限分辨率。",
 "body": wrap(
   der(p("<strong>视角放大率：</strong>物在无穷远，物镜焦距 $f_1'$、目镜焦距 $f_2'$，望远镜视角放大率为两焦距之比：")+
   fml("\\Gamma = -\\frac{f_1'}{f_2'} = \\frac{D}{D'}")+
   p("其中 $D$ 为物镜（入瞳）直径、$D'$ 为出瞳直径；负号表示开普勒望远镜成倒立像。出瞳是目镜对物镜所成的像，观察时眼睛应位于出瞳处（镜目距）。")+
   p("<strong>分辨率：</strong>受物镜口径的衍射限制，最小分辨角为：")+
   fml("\\delta\\theta = \\frac{1.22\\lambda}{D}"))+
   app(p("<strong>关系与选配：</strong>放大率并非越大越好：当 $\\Gamma D'$ 超过人眼分辨能力（现象放大率）时进一步增大放大率并不能提高细节分辨，只使像变暗。天文望远镜通常取有效放大率 $\\Gamma\\approx D/\\text{mm}$（出瞳约 $1\\,\\text{mm}$）。"))+
   note(p("<strong>视场与出瞳距离：</strong>望远系统的视场受目镜视场光阑限制，出瞳距离（镜目距）一般不小于约 $10\\,\\text{mm}$；军用望远镜还要求较长出瞳距离以适配护目镜。转像棱镜把倒像转为正像，但会增加筒长与光能损失。"))
 )},
]},
{
"name": "6.4 摄影、投影与照明系统",
"color": "#0284c7",
"desc": "摄影系统、投影系统与照明系统设计",
"items": [
{"id":"eo6s4-1","name":"摄影系统","tags":["def","der"],"brief":"物镜相对孔径、曝光与景深。",
 "body": wrap(
   defn("摄影系统",p("摄影系统由摄影物镜与探测器（胶片或图像传感器）组成，把远处或近处物体成像于感光面上。其核心指标是焦距、相对孔径（F 数）、视场与分辨率。"))+
   der(p("<strong>曝光与照度：</strong>像面照度 $E'=\\pi L\\tau\\sin^{2}u'$，与 F 数的平方成反比；曝光量为照度与时间之积：")+
   fml("H = E'\\,t = \\frac{\\pi L\\tau t}{4F^{2}}")+
   p("故光圈每减小一级（F 数乘以 $\\sqrt2$），曝光量减半，需相应延长曝光时间。景深与 F 数、对焦距离的关系见第四章景深公式。"))+
   note(p("摄影物镜需综合校正球差、彗差、像散、场曲、畸变与色差；大孔径、大视场与高分辨率往往相互制约，需按用途（人像、风景、微距、航拍）取舍。"))
 )},
{"id":"eo6s4-2","name":"投影系统","tags":["def","der"],"brief":"把物放大投影到屏幕上的系统。",
 "body": wrap(
   defn("投影系统",p("投影系统把较小的物（如幻灯片、LCD/DMD 光阀）放大并成像于远处屏幕上，通常由照明系统与投影物镜组成，要求放大率大、像面照度均匀、畸变小。"))+
   der(p("<strong>放大率与工作距离：</strong>设物距（光阀到物镜）为 $l$、投影像距为 $l'$，投影物镜放大率为：")+
   fml("\\beta = -\\frac{l'}{l}")+
   p("为使屏幕照度均匀并避免光阀发热，照明常用柯勒照明（光源成像于入瞳）；高端投影采用远心投影物镜以抑制彩色偏移与梯形畸变。"))+
   note(p("投影物镜常采用反远距结构（后工作距大于焦距）以容纳分色棱镜与照明组件；对色彩还原要求高时须校正倍率色差与场曲。"))
 )},
{"id":"eo6s4-3","name":"照明系统设计","tags":["der","app"],"brief":"柯勒照明与临界照明的实现与选择。",
 "body": wrap(
   der(p("<strong>柯勒照明的成像关系：</strong>光源经集光镜成像于物镜的入瞳（孔径光阑）处，同时集光镜把孔径光阑成像于物面。于是物面上任一点的照明都来自整个光源，克服了光源不均匀性：")+
   fml("\\text{光源}\\xrightarrow{\\text{集光镜}}\\text{入瞳},\\qquad \\text{入瞳}\\xrightarrow{\\text{物镜}}\\text{物面}")+
   p("临界照明则把光源直接成像于物面，光能利用率高但照度均匀性差（光源像叠加在物上）。"))+
   app(p("<strong>选择：</strong>显微与机器视觉要求照度均匀，选柯勒照明；投影与聚光要求高光能利用率且物面较小，可选临界照明。照明设计还需考虑孔径角与物镜 NA 匹配，以提高分辨率与对比度。"))
 )},
]},
{
"name": "6.5 特种系统与总体设计",
"color": "#0891b2",
"desc": "目视系统光束限制、激光扫描、光纤耦合、红外紫外与总体设计",
"items": [
{"id":"eo6s5-1","name":"目视光学系统的光束限制","tags":["der","note"],"brief":"出瞳、镜目距与眼睛瞳孔的匹配。",
 "body": wrap(
   der(p("<strong>光束限制分析：</strong>目视系统（显微镜、望远镜、放大镜）的孔径光阑常为物镜框或其后方光阑，出瞳即其像。为保证全部光束进入眼睛，要求出瞳直径不大于人眼瞳孔直径（约 $2\\sim3\\,\\text{mm}$ 明亮环境），且眼睛位于出瞳处：")+
   fml("D_{\\text{出瞳}} = \\frac{D_{\\text{入瞳}}}{|\\Gamma|} \\le D_{\\text{眼瞳}}")+
   p("出瞳到目镜最后一面（或眼睛）的距离称为镜目距，一般要求 $\\ge10\\,\\text{mm}$ 以便戴眼镜或眼罩观察；出瞳太小会因衍射与眼睛定位误差影响观察。"))+
   note(p("目视系统的视场还受目镜通光口径与视场光阑限制；对显微镜，物方线视场 $y$ 与目镜视场数 $\\phi$ 的关系为 $y=\\phi/(2\\beta)$。"))
 )},
{"id":"eo6s5-2","name":"激光扫描系统（fθ 物镜）","tags":["def","der","app"],"brief":"等速扫描需像高与扫描角成正比。",
 "body": wrap(
   defn("fθ 物镜",p("fθ 物镜是激光扫描（打标、打印、扫描成像）中使用的物镜，其成像满足像高与扫描角成正比的关系，使匀速转动的振镜或转镜对应扫描面上匀速移动的光点。"))+
   der(p("<strong>原理：</strong>普通物镜（如照相物镜）满足 $y'=f'\\tan\\theta$，扫描角线性变化时像点位置非线性变化，导致扫描速度不均匀。fθ 物镜通过引入桶形畸变，使像高与扫描角成正比：")+
   fml("y' = f'\\theta")+
   p("这样当扫描角以恒定角速度变化时，像面上的扫描速度恒定、扫描线段等间距。"))+
   app(p("<strong>应用：</strong>激光打标、激光打印、共焦显微扫描、激光雷达（LiDAR）与激光显示广泛使用 fθ 物镜；系统还需与扫描振镜、准直扩束镜配合，并校正平场与像散。"))
 )},
{"id":"eo6s5-3","name":"光纤耦合系统","tags":["der","app"],"brief":"激光到光纤的高效耦合条件。",
 "body": wrap(
   der(p("<strong>耦合条件：</strong>把激光耦合进光纤，需同时满足数值孔径匹配与模式匹配。设光纤数值孔径 $\\mathrm{NA}_f$ 与芯径 $d_f$，聚焦光束的会聚角与光斑半径应与之匹配：")+
   fml("u' \\le \\arcsin\\frac{\\mathrm{NA}_f}{n},\\qquad w_{\\text{焦点}} \\le \\frac{d_f}{2}")+
   p("光斑尺寸由聚焦透镜焦距与入射光束直径决定 $w\\approx\\dfrac{\\lambda f}{\\pi w_0}$；单模光纤还要求模场直径匹配以减小模式失配损耗。"))+
   app(p("<strong>优化：</strong>为提高耦合效率，常先用准直器把激光变为平行光，再用聚焦镜匹配光纤 NA 与芯径；还须控制光纤端面质量、轴向与横向对准误差（亚微米级）以及反射回光，必要时加隔离器。"))
 )},
{"id":"eo6s5-4","name":"红外与紫外光学系统的特点","tags":["def","der","note"],"brief":"波段决定材料、探测器与设计要点。",
 "body": wrap(
   defn("红外与紫外系统",p("红外系统工作在 $0.75\\sim1000\\,\\mu\\text{m}$，紫外系统工作在 $10\\sim400\\,\\text{nm}$。二者与可见光系统在设计上有显著差异，主要取决于材料透过率、探测器与衍射效应。"))+
   der(p("<strong>衍射与分辨率：</strong>由衍射极限 $\\delta\\theta=1.22\\lambda/D$，波长越长分辨角越大。红外波长比可见光长约一个量级，相同口径下分辨率显著降低，且系统往往接近衍射极限（像差易校正好）：")+
   fml("\\delta\\theta \\propto \\lambda \\ \\Longrightarrow\\ \\text{红外分辨能力低于可见光，紫外高于可见光}")+
   p("红外材料（Ge、Si、ZnSe、硫系玻璃）吸收与色散特性不同，且随温度变化大，常为无热化设计；红外探测器多为制冷型，需在 $100\\,\\text{K}$ 左右工作，故要设置冷光阑（冷屏）以抑制背景辐射。"+
   "紫外系统需用熔石英、CaF$_2$、MgF$_2$ 等透过材料，并注意材料在紫外波段的吸收与色散剧增、胶合层老化等问题。"))+
   note(p("红外系统的冷光阑应与入瞳匹配以抑制杂散辐射，提高信噪比；紫外系统常采用反射式或全石英结构以避免胶合与吸收。"))
 )},
{"id":"eo6s5-5","name":"光学材料选择与总体设计","tags":["def","der","note"],"brief":"材料参数与光学系统总体设计流程。",
 "body": wrap(
   defn("光学材料参数",p("常用光学玻璃的关键参数包括折射率 $n_d$、阿贝数 $V_d=(n_d-1)/(n_F-n_C)$（表征色散）、透过率、均匀性与热膨胀系数。阿贝数越小色散越大。"))+
   der(p("<strong>消色差选材：</strong>双胶合消色差透镜要求正、负透镜的光焦度满足消色差条件：")+
   fml("\\frac{\\Phi_1}{V_1} + \\frac{\\Phi_2}{V_2} = 0")+
   p("故须选阿贝数差别大的两种材料（如低色散冕玻璃 + 高色散火石玻璃），在保证总光焦度的同时使 F、C 光焦点重合。复消色差则须选用特殊色散（部分色散）玻璃或晶体。"))+
   defn("总体设计流程",p("光学系统总体设计一般包括：明确使用要求（孔径、视场、波段、分辨率、外形尺寸）；选型与初始结构；像差校正与平衡（近轴计算 + 实际光线追迹 + 优化）；公差分析与工艺性校核；与机械、电子、探测器接口的综合。"))+
   note(p("设计是性能、成本与工艺的折中：镜片数量越多像质越好但成本与体积上升；须统筹材料可获得性、加工与装调公差，并使系统在温度、振动等环境下稳定工作。"))
 )},
]},
{
"name": "6.6 系统集成与工程实例",
"color": "#0e7490",
"desc": "光学系统的公差与装调、成像链条的分辨率匹配",
"items": [
{"id":"eo6s6-1","name":"光学系统的公差与装调","tags":["def","der"],"brief":"公差分配、加工与装调对像质的影响。",
 "body": wrap(
   defn("公差",p("光学系统公差是指各结构参数（曲率半径、厚度、面形、材料折射率与均匀性）以及装调量（元件偏心、倾斜、间隔）允许的偏差范围。公差分配直接决定加工难度与成本。"))+
   der(p("<strong>公差合成：</strong>把各项误差折算为波像差或弥散斑，按统计规律（均方根）合成，使其总和不超出瑞利判据或设计要求：")+
   fml("W_{\\text{总}} = \\sqrt{\\sum_i W_i^{2}} \\le \\frac{\\lambda}{4}")+
   p("元件偏心与倾斜主要引入彗差、像散与光轴偏移；面形误差引入与空间频率相关的散射与波像差；间隔误差主要引起离焦。"))+
   app(p("<strong>装调与检验：</strong>采用自准直、干涉检验、星点检验与传函测量逐项校准；精密系统还须考虑温度、振动与重力的影响，进行无热化与刚度设计。"))
 )},
{"id":"eo6s6-2","name":"成像链条的分辨率匹配","tags":["der","app"],"brief":"光学极限与探测器像元的匹配。",
 "body": wrap(
   der(p("<strong>Nyquist 匹配：</strong>数字成像系统的分辨率由光学系统的衍射极限与探测器像元尺寸共同决定。为避免欠采样，像面上的采样间隔应不大于光学极限的一半（Nyquist 条件）：")+
   fml("2\\,\\text{像元尺寸} \\le \\frac{\\lambda F}{\\text{放大率}} \\ \\Longleftrightarrow\\ \\text{采样频率} \\ge 2\\,f_{\\text{截止}}")+
   p("其中 $f_{\\text{截止}}\\approx D/(1.22\\lambda f')$ 为光学截止频率。像元过大则欠采样（出现摩尔纹、分辨不足），像元过小则信噪比下降。"))+
   app(p("<strong>应用：</strong>相机、遥感载荷与显微成像系统须在光学分辨率、探测器像元、视场与信噪比之间取得平衡；工程上用光学 MTF 与探测器 MTF 的乘积作为系统级分辨率指标。"))
 )},
]},
]

CHAPTERS = [
    {"id":"eo-ch1","num":"第一章","title":"几何光学基础","en":"GEOMETRICAL OPTICS",
     "desc":"光线与波面、费马原理、反射与折射定律、全反射与临界角、光程与拉格朗日不变量、球面反射与球面折射成像、垂轴与轴向放大率、折射棱镜与最小偏向角。",
     "sections": ch1_sections},
    {"id":"eo-ch2","num":"第二章","title":"理想光学系统","en":"IDEAL OPTICAL SYSTEMS",
     "desc":"理想光学系统与共线成像、焦点焦距与主点主平面、牛顿公式与高斯公式、垂轴/轴向/角放大率、节点与节平面、两光组组合、厚薄透镜与光焦度、远心光路与作图法。",
     "sections": ch2_sections},
    {"id":"eo-ch3","num":"第三章","title":"平面镜棱镜系统","en":"MIRRORS & PRISMS",
     "desc":"平面镜成像与旋转特性、双平面镜、平行平板位移与色散、直角棱镜与屋脊棱镜、道威棱镜、棱镜展开与成像方向判定、光楔、偏振分束棱镜与制造误差。",
     "sections": ch3_sections},
    {"id":"eo-ch4","num":"第四章","title":"光束限制与光阑","en":"BEAM LIMITING",
     "desc":"孔径光阑与入瞳出瞳、视场光阑与入窗出窗、渐晕与渐晕系数、景深与焦深、数值孔径与相对孔径、远心系统光阑、场镜与柯勒照明、光能传递与像面照度。",
     "sections": ch4_sections},
    {"id":"eo-ch5","num":"第五章","title":"像差理论","en":"ABERRATION THEORY",
     "desc":"像差概述、球差、彗差、像散、场曲与畸变、位置色差与倍率色差、波像差与瑞利判据、赛德尔像差多项式、像差校正与平衡、点列图与光学传递函数 MTF。",
     "sections": ch5_sections},
    {"id":"eo-ch6","num":"第六章","title":"典型光学系统","en":"TYPICAL SYSTEMS",
     "desc":"放大镜视角放大率、显微镜放大率与分辨率、开普勒与伽利略望远镜、摄影与投影系统、照明系统、目视系统光束限制、激光扫描 fθ 物镜、光纤耦合、红外紫外系统与总体设计。",
     "sections": ch6_sections},
]

total_items = sum(sum(len(s["items"]) for s in ch["sections"]) for ch in CHAPTERS)
print(f"Total items: {total_items}")


def fix_lt_math(s):
    import re
    return re.sub(r"\$\$[\s\S]*?\$\$|\$[^$\n]*?\$", lambda m: m.group(0).replace("<", "&lt;"), s)
def fix_lt_text(s):
    return s.replace("<", "&lt;")
def fix_svg_lt(s):
    import re
    return re.sub(r"<(?!/?(?:svg|g|defs|line|rect|circle|ellipse|path|polygon|polyline|text|tspan|use|marker|linearGradient|radialGradient|stop|clipPath|symbol|pattern|mask|filter|title|desc|animate|animateTransform|image|style)\b)([A-Za-z])", r"&lt;\1", s)

def gen_html():
    data_lines = []
    for ch in CHAPTERS:
        sec_strs = []
        for sec in ch["sections"]:
            item_strs = []
            for it in sec["items"]:
                tags_js = json.dumps(it["tags"], ensure_ascii=False)
                body_esc = js_escape(fix_lt_math(it["body"]))
                fig_field = f",fig:{json.dumps(it.get('fig',''),ensure_ascii=False)}" if it.get("fig") else ""
                figcap_field = f",figCap:{json.dumps(fix_lt_text(it.get('figCap','')),ensure_ascii=False)}" if it.get("figCap") else ""
                item_strs.append(
                    f"{{id:'{it['id']}',name:{json.dumps(it['name'],ensure_ascii=False)},"
                    f"tags:{tags_js},brief:{json.dumps(fix_lt_text(it['brief']),ensure_ascii=False)},"
                    f"body:`{body_esc}`{fig_field}{figcap_field}}}"
                )
            sec_strs.append(
                f"{{name:{json.dumps(sec['name'],ensure_ascii=False)},"
                f"color:'{sec['color']}',desc:{json.dumps(sec['desc'],ensure_ascii=False)},"
                f"items:[{','.join(item_strs)}]}}"
            )
        data_lines.append(
            f"{{id:'{ch['id']}',num:{json.dumps(ch['num'],ensure_ascii=False)},"
            f"title:{json.dumps(ch['title'],ensure_ascii=False)},en:'{ch['en']}',"
            f"desc:{json.dumps(ch['desc'],ensure_ascii=False)},"
            f"sections:[{','.join(sec_strs)}]}}"
        )
    la_data = "[" + ",".join(data_lines) + "]"

    fig_entries = []
    for k, v in FIG.items():
        fig_entries.append(f"{json.dumps(k)}:`{js_escape(fix_svg_lt(v))}`")
    fig_js = "{" + ",".join(fig_entries) + "}"
    tag_label_js = json.dumps(TAG_LABEL, ensure_ascii=False)

    nav_tabs = "".join(
        f'<a class="la-nav-tab c{i+1}" href="#{ch["id"]}">{ch["num"]} · {ch["title"]}</a>'
        for i, ch in enumerate(CHAPTERS)
    )

    css = '''  :root{--la-bg:#f4f7fb;--la-card:#ffffff;--la-ink:#152033;--la-muted:#607089;--la-shadow:0 12px 32px rgba(20,36,60,.09);}
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;color:var(--la-ink);background:radial-gradient(circle at 10% 10%,rgba(37,99,235,.08),transparent 28%),radial-gradient(circle at 90% 10%,rgba(124,58,237,.08),transparent 28%),var(--la-bg);line-height:1.7}
  a{color:inherit}
  .la-wrap{width:min(1400px,94vw);margin:auto}
  .la-header{padding:52px 0 20px;text-align:center}
  .la-eyebrow{font-size:13px;letter-spacing:.22em;color:var(--la-muted);font-weight:700;text-transform:uppercase}
  h1{margin:10px 0 8px;font-size:clamp(30px,5vw,54px);line-height:1.08;letter-spacing:-.03em}
  .la-subtitle{margin:0 auto;color:var(--la-muted);font-size:16px;max-width:820px;line-height:1.8}
  .back-bar{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:22px 0 6px}
  .back-btn{display:inline-flex;align-items:center;gap:8px;padding:10px 22px;border-radius:999px;text-decoration:none;font-size:14px;font-weight:800;background:#fff;color:#1e3a8a;border:1px solid #c7d7ee;box-shadow:0 8px 20px rgba(20,36,60,.08);transition:.25s;cursor:pointer}
  .back-btn:hover{transform:translateY(-2px);box-shadow:0 14px 30px rgba(20,36,60,.14);color:#4c1d95;border-color:#ddd6fe}
  .la-nav-tabs{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:22px 0 8px}
  .la-nav-tab{padding:8px 16px;border-radius:999px;text-decoration:none;font-weight:700;font-size:13px;border:1px solid #d5deea;background:#fff;transition:.25s;color:#334155}
  .la-nav-tab:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(20,36,60,.1)}
  .la-nav-tab.c1{color:#2563eb;border-color:#bfdbfe}
  .la-nav-tab.c2{color:#7c3aed;border-color:#ddd6fe}
  .la-nav-tab.c3{color:#0d9488;border-color:#99f6e4}
  .la-nav-tab.c4{color:#c2410c;border-color:#fed7aa}
  .la-nav-tab.c5{color:#be185d;border-color:#fbcfe8}
  .la-nav-tab.c6{color:#0891b2;border-color:#a5f3fc}
  .la-engagement-bar{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:26px 0 10px}
  .la-stat-item{display:inline-flex;align-items:center;gap:8px;padding:8px 16px;border-radius:999px;background:#fff;border:1px solid #e2e8f0;font-size:13px;color:#334155;font-weight:600}
  .la-stat-value{color:#6366f1;font-weight:800;font-size:15px}
  .la-stat-link{cursor:pointer;text-decoration:none;transition:.2s}
  .la-stat-link:hover{background:#eef2ff;border-color:#c7d2fe}
  .la-legend{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin:0 0 24px;font-size:12px;color:#64748b}
  .la-legend-title{font-weight:700;margin-right:4px}
  .la-arc-badge{font-size:11px;padding:3px 10px;border-radius:999px;font-weight:700;letter-spacing:.04em}
  .la-arc-def{background:#dbeafe;color:#1e40af}
  .la-arc-thm{background:#ede9fe;color:#6d28d9}
  .la-arc-der{background:#e0f2fe;color:#0369a1}
  .la-arc-exa{background:#dcfce7;color:#15803d}
  .la-arc-app{background:#fef3c7;color:#b45309}
  .la-arc-note{background:#fee2e2;color:#b91c1c}
  .la-roadmap{padding:30px 0}
  .la-phase-title{font-size:24px;color:#1e293b;margin:40px 0 6px 18px;display:flex;align-items:center;gap:12px}
  .la-phase-title::before{content:"";width:6px;height:26px;border-radius:4px}
  .la-phase-title.eo-ch1::before{background:#2563eb}
  .la-phase-title.eo-ch2::before{background:#7c3aed}
  .la-phase-title.eo-ch3::before{background:#0d9488}
  .la-phase-title.eo-ch4::before{background:#c2410c}
  .la-phase-title.eo-ch5::before{background:#be185d}
  .la-phase-title.eo-ch6::before{background:#0891b2}
  .la-phase-en{font-size:11px;letter-spacing:.36em;color:#94a3b8;font-weight:700;text-transform:uppercase;margin:0 0 12px 18px;font-style:italic}
  .la-phase-desc{color:var(--la-muted);font-size:14px;margin:0 0 24px 18px;line-height:1.8;max-width:960px}
  .la-domain{margin-bottom:26px;padding:16px 18px 18px 22px;position:relative;background:rgba(255,255,255,.6);border-radius:18px;border:1px solid #e5ebf2}
  .la-domain::before{content:"";position:absolute;left:6px;top:16px;bottom:16px;width:5px;border-radius:5px;background:var(--domain-color,#2563eb);box-shadow:0 0 12px rgba(37,99,235,.25)}
  .la-domain-header{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:12px}
  .la-domain-header h3{margin:0;font-size:17px;color:#1e293b}
  .la-domain-count{font-size:11px;padding:2px 10px;border-radius:999px;background:#eef2ff;color:#4f46e5;font-weight:700}
  .la-domain-desc{font-size:12px;color:#94a3b8}
  .la-domain-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}
  .la-course-card{background:#fff;border:1px solid #e5ebf2;border-radius:14px;padding:14px 16px;cursor:pointer;transition:.22s;box-shadow:var(--la-shadow)}
  .la-course-card:hover{transform:translateY(-3px);border-color:#c7d2fe;box-shadow:0 16px 40px rgba(37,99,235,.12)}
  .la-course-card h4{margin:6px 0;font-size:15px;color:#1e293b}
  .la-course-card p{margin:4px 0 0;font-size:12.5px;color:#64748b;line-height:1.6}
  .la-arc-badges{display:flex;gap:5px;flex-wrap:wrap;margin-bottom:2px}
  .la-overlay{position:fixed;inset:0;background:rgba(15,23,42,.5);display:none;align-items:center;justify-content:center;padding:18px;z-index:60;backdrop-filter:blur(2px)}
  .la-overlay.show{display:flex}
  .la-modal{width:min(820px,96vw);background:white;border-radius:24px;padding:30px;box-shadow:0 24px 80px rgba(0,0,0,.28);animation:laPopIn .3s;max-height:90vh;overflow-y:auto}
  @keyframes laPopIn{from{transform:scale(.94);opacity:0}to{transform:scale(1);opacity:1}}
  .la-modal h2{margin:0 0 10px;font-size:23px;color:#1e293b;line-height:1.35}
  .la-modal .la-crumbs{font-size:12px;color:#94a3b8;margin:0 0 14px;font-weight:600;letter-spacing:.02em}
  .la-modal .la-arc-badges{margin:0 0 16px}
  .la-modal-body{color:#334155;font-size:15px;line-height:1.9}
  .la-modal-body p{margin:0 0 12px}
  .la-modal-body strong{color:#0f172a}
  .la-modal-body ul{margin:0 0 12px;padding-left:22px}
  .la-modal-body li{margin-bottom:6px}
  .la-fml{margin:16px 0;padding:14px 18px;background:linear-gradient(135deg,#f8fafc,#eef4fb);border-left:4px solid #93b4e8;border-radius:10px;overflow-x:auto;font-size:16px;color:#0f172a}
  .la-fml .note{display:block;font-size:12.5px;color:#8496ad;margin-top:8px;line-height:1.6;font-family:system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
  .la-fml mjx-container[display="true"]{margin:0 !important}
  mjx-container, mjx-container *{color:#0f172a !important;opacity:1 !important}
  mjx-mi{font-style:italic !important}
  mjx-mo{color:#0f172a !important}
  .la-modal-body mjx-container, .la-modal-body mjx-container *{color:#0f172a !important;opacity:1 !important}
  .la-fig{margin:18px auto;padding:14px 16px 10px;background:#fafcff;border:1px solid #e2ebf7;border-radius:14px;display:flex;flex-direction:column;align-items:center;max-width:600px}
  .la-fig svg{display:block;width:100%;height:auto;max-width:560px}
  .la-fig .la-fig-cap{font-size:12px;color:#8496ad;margin-top:8px;text-align:center;letter-spacing:.02em}
  .la-callout{margin:14px 0;padding:12px 16px;background:#fffbeb;border-left:3px solid #fbbf24;border-radius:8px;font-size:13.5px;color:#78350f;line-height:1.8}
  .la-kp-sec{margin:0 0 18px;padding:14px 16px;border-radius:12px;background:#f8fafc;border:1px solid #eef2f7}
  .la-kp-sec h5{margin:0 0 10px;font-size:14px;color:#1e293b;letter-spacing:.04em;display:flex;align-items:center;gap:8px}
  .la-kp-sec h5::before{content:"";width:4px;height:14px;border-radius:2px;background:var(--la-accent,#3b82f6)}
  .la-kp-def{border-left:3px solid #3b82f6}
  .la-kp-thm{border-left:3px solid #8b5cf6;background:#faf7ff}
  .la-kp-der{border-left:3px solid #0ea5e9;background:#f0f9ff}
  .la-kp-exa{border-left:3px solid #10b981;background:#f0fdf4}
  .la-kp-app{border-left:3px solid #f59e0b;background:#fffbeb}
  .la-kp-note{border-left:3px solid #ef4444;background:#fef2f2}
  .la-kp-his{border-left:3px solid #64748b;background:#f8fafc}
  .la-kp-sec p:last-child{margin-bottom:0}
  .la-modal-close{margin-top:22px;background:#0f172a;color:white;border-color:#0f172a;padding:10px 20px;font-weight:bold}
  .la-footer{padding:34px 0 50px;color:var(--la-muted);text-align:center;font-size:13px;line-height:1.9}
  .la-core-fmls{margin:40px 0 20px;padding:28px 24px;background:linear-gradient(135deg,#f0f4ff,#faf7ff);border:1px solid #e0e7ff;border-radius:18px}
  .la-core-fmls h3{font-size:18px;color:#1e293b;margin:0 0 20px;text-align:center;letter-spacing:.04em}
  .la-core-fmls h3 .la-core-count{display:inline-block;background:#6366f1;color:#fff;font-size:13px;padding:2px 10px;border-radius:20px;margin-left:8px;vertical-align:middle}
  .la-core-item{display:flex;gap:12px;margin:0 0 14px;padding:12px 16px;background:#fff;border-radius:12px;border-left:3px solid #6366f1;align-items:flex-start}
  .la-core-num{flex-shrink:0;width:26px;height:26px;border-radius:50%;background:#6366f1;color:#fff;font-size:13px;display:flex;align-items:center;justify-content:center;font-weight:bold}
  .la-core-body{flex:1;min-width:0}
  .la-core-body .la-core-name{font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px}
  .la-core-body .la-fml{margin:6px 0 0;padding:8px 14px;font-size:15px}
  .la-back-top{display:inline-block;margin-top:20px;padding:10px 28px;background:#1e293b;color:#fff;border:none;border-radius:25px;font-size:14px;cursor:pointer;letter-spacing:.04em;transition:background .2s}
  .la-back-top:hover{background:#334155}
  @media(max-width:900px){.la-wrap{width:min(94vw,720px)}.la-roadmap{padding:20px}.la-phase-title{font-size:19px}.la-phase-en{font-size:10px;letter-spacing:.26em}.la-domain-desc{display:none}.la-domain-grid{grid-template-columns:repeat(auto-fill,minmax(160px,1fr))}.la-modal{padding:22px}}'''

    js = f'''const LA_DATA = {la_data};
const LA_TAG_LABEL = {tag_label_js};
const LA_FIG = {fig_js};
const LA_KP = {{}};
function laBuildCard(item){{
  const tags = item.tags.map(t => `<span class="la-arc-badge la-arc-${{t}}">${{LA_TAG_LABEL[t]}}</span>`).join('');
  return `<div class="la-course-card" onclick="showLaItem('${{item.id}}')"><div class="la-arc-badges">${{tags}}</div><h4>${{item.name}}</h4><p>${{item.brief}}</p></div>`;
}}
function renderLa(){{
  const root = document.getElementById('laRoadmap');
  let html = '';
  LA_DATA.forEach(ch => {{
    html += `<h2 class="la-phase-title ${{ch.id}}" id="${{ch.id}}">${{ch.num}} · ${{ch.title}}</h2>`;
    html += `<div class="la-phase-en">${{ch.en}}</div>`;
    html += `<p class="la-phase-desc">${{ch.desc}}</p>`;
    ch.sections.forEach(sec => {{
      html += `<div class="la-domain" style="--domain-color:${{sec.color}};"><div class="la-domain-header"><h3>${{sec.name}}</h3><span class="la-domain-count">${{sec.items.length}} 个知识点</span><span class="la-domain-desc">${{sec.desc}}</span></div><div class="la-domain-grid">`;
      sec.items.forEach(it => {{ html += laBuildCard(it); LA_KP[it.id] = {{item: it, section: sec.name, chapter: `${{ch.num}} · ${{ch.title}}`}}; }});
      html += `</div></div>`;
    }});
  }});
  root.innerHTML = html;
  const kCount = Object.keys(LA_KP).length;
  document.getElementById('laKCount').textContent = kCount;
}}
function showLaItem(id){{
  const rec = LA_KP[id];
  if(!rec) return;
  const it = rec.item;
  document.getElementById('laCrumbs').textContent = rec.chapter + ' ／ ' + rec.section;
  document.getElementById('laTitle').textContent = it.name;
  document.getElementById('laTags').innerHTML = it.tags.map(t => `<span class="la-arc-badge la-arc-${{t}}">${{LA_TAG_LABEL[t]}}</span>`).join('');
  let bodyHtml = it.body;
  if (it.fig && LA_FIG[it.fig]) {{
    const figHtml = `<div class="la-fig">${{LA_FIG[it.fig]}}<div class="la-fig-cap">${{it.figCap || ''}}</div></div>`;
    bodyHtml = figHtml + bodyHtml;
  }}
  document.getElementById('laBody').innerHTML = bodyHtml;
  document.getElementById('laOverlay').classList.add('show');
  document.querySelector('.la-modal').scrollTop = 0;
  if (window.MathJax && window.MathJax.typesetPromise) {{ window.MathJax.typesetPromise([document.getElementById('laBody')]).catch(()=>{{}}); }}
}}
function hideLaInfo(){{ document.getElementById('laOverlay').classList.remove('show'); }}
function closeLaInfo(e){{ if(e.target.id === 'laOverlay') hideLaInfo(); }}
document.addEventListener('keydown', e => {{ if(e.key === 'Escape') hideLaInfo(); }});
document.addEventListener('DOMContentLoaded', () => {{
  renderLa();
  if (window.MathJax && window.MathJax.typesetPromise) {{ window.MathJax.typesetPromise([document.getElementById('laRoadmap')]).catch(()=>{{}}); }}
}});'''

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="工程光学知识体系：几何光学基础、理想光学系统、棱镜系统、光束限制、像差理论、典型光学系统">
<title>工程光学 · 知识体系</title>
<script>
window.MathJax = {{
  tex: {{
    inlineMath: [['$','$'], ['\\\\(','\\\\)']],
    displayMath: [['$$','$$'], ['\\\\[','\\\\]']],
    processEscapes: true,
    packages: {{'[+]': ['ams','boldsymbol']}}
  }},
  options: {{
    skipHtmlTags: ['script','noscript','style','textarea','pre','code'],
    ignoreHtmlClass: 'tex2jax_ignore'
  }},
  svg: {{ fontCache: 'global' }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" id="MathJax-script" async></script>
<style>
{css}
</style>
</head>
<body>
<div class="la-wrap">
  <header class="la-header">
    <div class="la-eyebrow">ENGINEERING OPTICS · KNOWLEDGE MAP</div>
    <h1>工程光学 · 知识体系</h1>
    <p class="la-subtitle">几何光学基础 · 理想光学系统 · 平面镜棱镜系统 · 光束限制与光阑 · 像差理论 · 典型光学系统</p>
    <div class="back-bar"><a class="back-btn" href="index.html">← 返回总览</a></div>
    <div class="la-nav-tabs">{nav_tabs}</div>
    <div class="la-engagement-bar">
      <div class="la-stat-item"><span>📘</span><span class="la-stat-value" id="laKCount">--</span><span>个知识点</span></div>
      <a class="la-stat-item la-stat-link" href="#laCoreFmls" onclick="event.preventDefault();document.getElementById('laCoreFmls').scrollIntoView({{behavior:'smooth',block:'start'}})"><span>🧮</span><span class="la-stat-value">{len(CORE_FORMULAS)}</span><span>条核心公式 · 点击速查</span></a>
    </div>
  </header>
  <div class="la-legend">
    <span class="la-legend-title">知识记号</span>
    <span class="la-arc-badge la-arc-def">定 义</span>
    <span class="la-arc-badge la-arc-thm">定 理</span>
    <span class="la-arc-badge la-arc-der">推 导</span>
    <span class="la-arc-badge la-arc-exa">例 子</span>
    <span class="la-arc-badge la-arc-app">应 用</span>
    <span class="la-arc-badge la-arc-note">备 注</span>
  </div>
  <main class="la-roadmap" id="laRoadmap"></main>
  <section class="la-core-fmls" id="laCoreFmls">
    <h3>核心公式速查 <span class="la-core-count">{len(CORE_FORMULAS)} 条</span></h3>
{chr(10).join(f'    <div class="la-core-item"><div class="la-core-num">{i+1}</div><div class="la-core-body"><div class="la-core-name">{name.replace("<","&lt;")}</div><div class="la-fml">$${latex.replace("<","&lt;")}$$</div><div class="note" style="font-size:12px;color:#8496ad;margin-top:4px">{desc.replace("<","&lt;")}</div></div></div>' for i,(name,latex,desc) in enumerate(CORE_FORMULAS))}
  </section>
  <footer class="la-footer">
    <div>工程光学 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于工程光学核心知识体系整理</div>
    <button class="la-back-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">↑ 回到顶部</button>
  </footer>
</div>
<div class="la-overlay" id="laOverlay" onclick="closeLaInfo(event)">
  <div class="la-modal" onclick="event.stopPropagation()">
    <p class="la-crumbs" id="laCrumbs"></p>
    <h2 id="laTitle">知识点</h2>
    <div class="la-arc-badges" id="laTags"></div>
    <div class="la-modal-body" id="laBody"></div>
    <button class="la-modal-close" onclick="hideLaInfo()">关 闭</button>
  </div>
</div>
<script>
{js}
</script>
</body>
</html>'''
    return html

if __name__ == "__main__":
    html = gen_html()
    with open("/workspace/engineering-optics.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated engineering-optics.html ({len(html)} chars)")
