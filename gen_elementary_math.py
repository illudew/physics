# -*- coding: utf-8 -*-
"""Generate elementary-math.html with 8 chapters: 集合与逻辑/代数/函数/数列/平面几何/立体几何/解析几何/概率统计."""
import json

FIG = {
"set_venn": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="10" width="220" height="140" fill="#f8fafc" stroke="#cbd5e1" rx="10"/>
<text x="18" y="28" font-size="11" fill="#64748b">U（全集）</text>
<circle cx="92" cy="86" r="48" fill="#dbeafe" fill-opacity="0.6" stroke="#2563eb" stroke-width="1.5"/>
<circle cx="148" cy="86" r="48" fill="#ede9fe" fill-opacity="0.6" stroke="#7c3aed" stroke-width="1.5"/>
<text x="62" y="86" font-size="12" fill="#1e40af" font-weight="bold">A</text>
<text x="168" y="86" font-size="12" fill="#6d28d9" font-weight="bold">B</text>
<text x="108" y="90" font-size="10" fill="#475569">A∩B</text>
</svg>''',
"quadratic": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="220" y2="130" stroke="#475569" stroke-width="1.2"/>
<line x1="120" y1="20" x2="120" y2="140" stroke="#475569" stroke-width="1.2"/>
<path d="M 40 110 Q 120 20 200 110" fill="none" stroke="#2563eb" stroke-width="2"/>
<circle cx="120" cy="50" r="3" fill="#ef4444"/>
<line x1="120" y1="50" x2="120" y2="130" stroke="#ef4444" stroke-width="1" stroke-dasharray="3 3"/>
<text x="124" y="48" font-size="10" fill="#ef4444">顶点</text>
<text x="208" y="124" font-size="10" fill="#475569">x</text>
<text x="110" y="18" font-size="10" fill="#475569">y</text>
</svg>''',
"func_mapping": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="55" cy="80" rx="38" ry="50" fill="#dbeafe" fill-opacity="0.5" stroke="#2563eb"/>
<ellipse cx="185" cy="80" rx="38" ry="50" fill="#dcfce7" fill-opacity="0.5" stroke="#16a34a"/>
<text x="40" y="18" font-size="11" fill="#1e40af" font-weight="bold">定义域 A</text>
<text x="168" y="18" font-size="11" fill="#15803d" font-weight="bold">值域 B</text>
<circle cx="55" cy="50" r="3" fill="#2563eb"/><text x="62" y="54" font-size="10" fill="#2563eb">x1</text>
<circle cx="55" cy="80" r="3" fill="#2563eb"/><text x="62" y="84" font-size="10" fill="#2563eb">x2</text>
<circle cx="55" cy="110" r="3" fill="#2563eb"/><text x="62" y="114" font-size="10" fill="#2563eb">x3</text>
<circle cx="185" cy="60" r="3" fill="#16a34a"/><text x="194" y="64" font-size="10" fill="#16a34a">y1</text>
<circle cx="185" cy="100" r="3" fill="#16a34a"/><text x="194" y="104" font-size="10" fill="#16a34a">y2</text>
<line x1="58" y1="50" x2="182" y2="60" stroke="#f59e0b" stroke-width="1.3" marker-end="url(#arr2)"/>
<line x1="58" y1="80" x2="182" y2="60" stroke="#f59e0b" stroke-width="1.3"/>
<line x1="58" y1="110" x2="182" y2="100" stroke="#f59e0b" stroke-width="1.3"/>
<defs><marker id="arr2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#f59e0b"/></marker></defs>
<text x="100" y="148" font-size="10" fill="#475569">f: A → B</text>
</svg>''',
"triangle": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<polygon points="40,130 200,130 120,40" fill="#eef4fb" stroke="#2563eb" stroke-width="1.8"/>
<line x1="120" y1="40" x2="120" y2="130" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="4 3"/>
<text x="110" y="148" font-size="10" fill="#475569">a（底边）</text>
<text x="124" y="88" font-size="10" fill="#ef4444">h（高）</text>
<text x="70" y="96" font-size="10" fill="#2563eb">b</text>
<text x="158" y="96" font-size="10" fill="#2563eb">c</text>
<text x="108" y="34" font-size="10" fill="#475569">A</text>
<text x="34" y="126" font-size="10" fill="#475569">B</text>
<text x="202" y="126" font-size="10" fill="#475569">C</text>
</svg>''',
"circle": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="56" fill="none" stroke="#2563eb" stroke-width="2"/>
<line x1="120" y1="80" x2="176" y2="80" stroke="#ef4444" stroke-width="1.8"/>
<circle cx="120" cy="80" r="2.5" fill="#475569"/>
<line x1="64" y1="80" x2="176" y2="80" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="140" y="76" font-size="10" fill="#ef4444">r</text>
<text x="110" y="76" font-size="10" fill="#475569">O</text>
<text x="100" y="150" font-size="10" fill="#475569">C = 2πr,  S = πr²</text>
</svg>''',
"cone": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 120 28 L 60 132 L 180 132 Z" fill="#eef4fb" stroke="#2563eb" stroke-width="1.8"/>
<ellipse cx="120" cy="132" rx="60" ry="12" fill="none" stroke="#2563eb" stroke-width="1.5"/>
<line x1="120" y1="28" x2="120" y2="132" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="4 3"/>
<text x="124" y="82" font-size="10" fill="#ef4444">h</text>
<text x="80" y="148" font-size="10" fill="#475569">r</text>
<text x="78" y="14" font-size="10" fill="#2563eb">V = (1/3)πr²h</text>
</svg>''',
"conic": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="220" y2="130" stroke="#475569" stroke-width="1"/>
<line x1="120" y1="16" x2="120" y2="148" stroke="#475569" stroke-width="1"/>
<ellipse cx="120" cy="74" rx="70" ry="40" fill="none" stroke="#2563eb" stroke-width="2"/>
<circle cx="96" cy="74" r="2.5" fill="#ef4444"/><text x="84" y="70" font-size="9" fill="#ef4444">F1</text>
<circle cx="144" cy="74" r="2.5" fill="#ef4444"/><text x="148" y="70" font-size="9" fill="#ef4444">F2</text>
<text x="40" y="146" font-size="10" fill="#2563eb">椭圆 x²/a²+y²/b²=1</text>
</svg>''',
"probability": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="40" width="160" height="80" fill="#f8fafc" stroke="#cbd5e1" rx="8"/>
<circle cx="72" cy="70" r="12" fill="#2563eb"/>
<circle cx="110" cy="70" r="12" fill="#f59e0b"/>
<circle cx="148" cy="70" r="12" fill="#16a34a"/>
<circle cx="186" cy="70" r="12" fill="#ef4444"/>
<text x="66" y="74" font-size="10" fill="white" font-weight="bold">1</text>
<text x="104" y="74" font-size="10" fill="white" font-weight="bold">2</text>
<text x="142" y="74" font-size="10" fill="white" font-weight="bold">3</text>
<text x="180" y="74" font-size="10" fill="white" font-weight="bold">4</text>
<text x="70" y="110" font-size="11" fill="#475569">P(事件A) = m/n</text>
</svg>''',
"trig_circle": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="56" fill="none" stroke="#2563eb" stroke-width="1.6"/>
<line x1="40" y1="80" x2="200" y2="80" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="16" x2="120" y2="144" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="80" x2="160" y2="40" stroke="#ef4444" stroke-width="1.8"/>
<circle cx="160" cy="40" r="2.5" fill="#ef4444"/>
<line x1="160" y1="40" x2="160" y2="80" stroke="#10b981" stroke-width="1.3" stroke-dasharray="3 2"/>
<line x1="120" y1="80" x2="160" y2="80" stroke="#0ea5e9" stroke-width="1.3"/>
<text x="164" y="38" font-size="10" fill="#ef4444">P(cosθ,sinθ)</text>
<text x="132" y="76" font-size="9" fill="#0ea5e9">cosθ</text>
<text x="164" y="62" font-size="9" fill="#10b981">sinθ</text>
<text x="122" y="22" font-size="10" fill="#2563eb">单位圆</text>
</svg>''',
"sequence": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="130" x2="210" y2="130" stroke="#94a3b8" stroke-width="1"/>
<circle cx="50" cy="110" r="4" fill="#c2410c"/><circle cx="80" cy="90" r="4" fill="#c2410c"/>
<circle cx="110" cy="70" r="4" fill="#c2410c"/><circle cx="140" cy="50" r="4" fill="#c2410c"/>
<circle cx="170" cy="30" r="4" fill="#c2410c"/>
<line x1="50" y1="110" x2="170" y2="30" stroke="#c2410c" stroke-width="1.4" stroke-dasharray="3 3"/>
<text x="42" y="140" font-size="9" fill="#475569">a₁</text><text x="72" y="140" font-size="9" fill="#475569">a₂</text>
<text x="102" y="140" font-size="9" fill="#475569">a₃</text><text x="132" y="140" font-size="9" fill="#475569">a₄</text>
<text x="162" y="140" font-size="9" fill="#475569">a₅</text>
<text x="70" y="36" font-size="11" fill="#c2410c" font-weight="bold">公差 d</text>
</svg>''',
"polar_coord": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="130" x2="210" y2="130" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="140" x2="120" y2="10" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="130" x2="180" y2="70" stroke="#0891b2" stroke-width="1.8"/>
<circle cx="180" cy="70" r="3" fill="#ef4444"/>
<path d="M 150 130 A 30 30 0 0 0 138 112" fill="none" stroke="#f59e0b" stroke-width="1.4"/>
<text x="144" y="118" font-size="10" fill="#f59e0b">θ</text>
<text x="148" y="106" font-size="10" fill="#0891b2">ρ</text>
<text x="184" y="66" font-size="10" fill="#ef4444">P(ρ,θ)</text>
<text x="122" y="126" font-size="10" fill="#475569">O</text>
<text x="206" y="126" font-size="10" fill="#475569">极轴</text>
</svg>''',
"cube": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<polygon points="70,40 170,40 200,70 100,70" fill="#eef4fb" stroke="#2563eb" stroke-width="1.6"/>
<polygon points="70,40 100,70 100,140 70,110" fill="#dbeafe" stroke="#2563eb" stroke-width="1.6"/>
<polygon points="100,70 200,70 200,140 100,140" fill="#bfdbfe" stroke="#2563eb" stroke-width="1.6"/>
<line x1="170" y1="40" x2="200" y2="70" stroke="#2563eb" stroke-width="1.6"/>
<text x="130" y="110" font-size="11" fill="#1e40af" font-weight="bold">a</text>
<text x="150" y="66" font-size="10" fill="#475569">正方体</text>
</svg>''',
"parabola": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="80" x2="220" y2="80" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="16" x2="120" y2="144" stroke="#94a3b8" stroke-width="1"/>
<path d="M 120 20 Q 200 80 120 140" fill="none" stroke="#0891b2" stroke-width="2"/>
<line x1="60" y1="16" x2="60" y2="144" stroke="#ef4444" stroke-width="1" stroke-dasharray="4 3"/>
<circle cx="150" cy="80" r="2.5" fill="#ef4444"/>
<text x="154" y="76" font-size="10" fill="#ef4444">F(p/2,0)</text>
<text x="40" y="20" font-size="9" fill="#ef4444">x=-p/2</text>
<text x="170" y="146" font-size="10" fill="#0891b2">y²=2px</text>
</svg>''',
"parallelogram": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<polygon points="40,120 100,60 200,60 140,120" fill="#fde7f3" stroke="#be185d" stroke-width="1.8"/>
<line x1="40" y1="120" x2="40" y2="60" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="4 3"/>
<text x="22" y="92" font-size="10" fill="#ef4444">h</text>
<text x="62" y="124" font-size="10" fill="#be185d">a</text>
<text x="160" y="58" font-size="10" fill="#be185d">b</text>
<text x="80" y="146" font-size="10" fill="#475569">S = a·h = b·a·sinθ</text>
</svg>''',
"sphere": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="56" fill="#ede9fe" fill-opacity="0.45" stroke="#7c3aed" stroke-width="1.8"/>
<ellipse cx="120" cy="80" rx="56" ry="14" fill="none" stroke="#7c3aed" stroke-width="1" stroke-dasharray="3 3"/>
<ellipse cx="120" cy="80" rx="14" ry="56" fill="none" stroke="#7c3aed" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="120" y1="80" x2="176" y2="80" stroke="#ef4444" stroke-width="1.8"/>
<text x="140" y="76" font-size="10" fill="#ef4444">R</text>
<text x="80" y="148" font-size="10" fill="#7c3aed">S=4πR², V=(4/3)πR³</text>
</svg>''',
"helix": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="60" y1="20" x2="60" y2="150" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="180" y1="20" x2="180" y2="150" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<path d="M 60 30 Q 90 40 120 50 Q 150 60 180 50 Q 150 70 120 80 Q 90 90 60 80 Q 90 100 120 110 Q 150 120 180 110 Q 150 130 120 140" fill="none" stroke="#0891b2" stroke-width="2"/>
<text x="120" y="18" font-size="10" fill="#0891b2" font-weight="bold">圆柱螺旋线</text>
<text x="70" y="36" font-size="9" fill="#475569">x=a cos t</text>
<text x="70" y="48" font-size="9" fill="#475569">y=a sin t</text>
<text x="70" y="60" font-size="9" fill="#475569">z=bt</text>
</svg>''',
"quadric": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="220" y2="130" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="20" x2="120" y2="148" stroke="#94a3b8" stroke-width="1"/>
<line x1="40" y1="80" x2="200" y2="80" stroke="#94a3b8" stroke-width="1"/>
<ellipse cx="120" cy="80" rx="75" ry="32" fill="#e0f2fe" fill-opacity="0.5" stroke="#0891b2" stroke-width="1.6"/>
<ellipse cx="120" cy="58" rx="32" ry="10" fill="none" stroke="#0891b2" stroke-width="1.2"/>
<ellipse cx="120" cy="102" rx="50" ry="16" fill="none" stroke="#0891b2" stroke-width="1.2"/>
<text x="80" y="18" font-size="10" fill="#0891b2" font-weight="bold">单叶双曲面</text>
</svg>''',
"normal_dist": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="220" y2="130" stroke="#475569" stroke-width="1.2"/>
<line x1="120" y1="20" x2="120" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<path d="M 40 128 Q 80 128 120 40 Q 160 128 200 128" fill="none" stroke="#10b981" stroke-width="2"/>
<text x="124" y="36" font-size="10" fill="#10b981" font-weight="bold">μ</text>
<text x="60" y="146" font-size="9" fill="#475569">μ-σ</text>
<text x="100" y="146" font-size="9" fill="#475569">μ</text>
<text x="140" y="146" font-size="9" fill="#475569">μ+σ</text>
<text x="180" y="146" font-size="9" fill="#475569">μ+2σ</text>
<text x="40" y="20" font-size="10" fill="#10b981">N(μ,σ²) 钟形曲线</text>
</svg>''',
"number_line": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="80" x2="220" y2="80" stroke="#475569" stroke-width="1.5"/>
<polygon points="220,80 212,76 212,84" fill="#475569"/>
<circle cx="80" cy="80" r="3" fill="#ef4444"/>
<circle cx="120" cy="80" r="3" fill="#ef4444"/>
<line x1="80" y1="60" x2="120" y2="60" stroke="#2563eb" stroke-width="2"/>
<text x="74" y="100" font-size="10" fill="#475569">a</text>
<text x="114" y="100" font-size="10" fill="#475569">b</text>
<text x="92" y="54" font-size="10" fill="#2563eb">|a-b|</text>
<text x="20" y="40" font-size="10" fill="#475569">|x-a| &lt; b</text>
</svg>''',
"abs_value": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="220" y2="130" stroke="#94a3b8" stroke-width="1"/>
<line x1="120" y1="20" x2="120" y2="140" stroke="#94a3b8" stroke-width="1"/>
<path d="M 40 40 L 120 130 L 200 40" fill="none" stroke="#7c3aed" stroke-width="2"/>
<text x="40" y="34" font-size="10" fill="#7c3aed" font-weight="bold">y=|x|</text>
<text x="208" y="124" font-size="10" fill="#475569">x</text>
<text x="124" y="22" font-size="10" fill="#475569">y</text>
<text x="80" y="148" font-size="9" fill="#475569">|ab|=|a||b|</text>
</svg>''',
"number_system": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="20" y="20" width="200" height="120" fill="#ede9fe" fill-opacity="0.5" stroke="#7c3aed" stroke-width="1.5" rx="8"/>
<rect x="30" y="30" width="180" height="100" fill="#dbeafe" fill-opacity="0.6" stroke="#2563eb" stroke-width="1.2" rx="6"/>
<rect x="40" y="40" width="160" height="80" fill="#dcfce7" fill-opacity="0.6" stroke="#16a34a" stroke-width="1.2" rx="6"/>
<rect x="50" y="50" width="140" height="60" fill="#fef3c7" fill-opacity="0.7" stroke="#f59e0b" stroke-width="1.2" rx="6"/>
<text x="30" y="18" font-size="10" fill="#7c3aed" font-weight="bold">实数 R</text>
<text x="40" y="28" font-size="9" fill="#2563eb">有理数 Q</text>
<text x="50" y="38" font-size="9" fill="#16a34a">整数 Z</text>
<text x="60" y="48" font-size="9" fill="#b45309">自然数 N</text>
<text x="110" y="135" font-size="9" fill="#475569">N ⊂ Z ⊂ Q ⊂ R</text>
</svg>''',
"inequality": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="220" y2="130" stroke="#475569" stroke-width="1.2"/>
<line x1="120" y1="16" x2="120" y2="140" stroke="#94a3b8" stroke-width="1"/>
<path d="M 40 110 Q 120 20 200 110" fill="none" stroke="#7c3aed" stroke-width="2"/>
<line x1="60" y1="130" x2="60" y2="85" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="3 2"/>
<line x1="180" y1="130" x2="180" y2="85" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="3 2"/>
<line x1="60" y1="85" x2="180" y2="85" stroke="#10b981" stroke-width="2"/>
<text x="40" y="146" font-size="9" fill="#ef4444">x1</text>
<text x="170" y="146" font-size="9" fill="#ef4444">x2</text>
<text x="100" y="80" font-size="10" fill="#10b981">y&gt;0</text>
<text x="20" y="20" font-size="10" fill="#7c3aed">不等式图像法</text>
</svg>''',
"pyramid": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<polygon points="120,30 60,130 180,130" fill="#eef4fb" stroke="#8b5cf6" stroke-width="1.8"/>
<polygon points="120,30 180,130 200,110 140,30" fill="#ddd6fe" fill-opacity="0.5" stroke="#8b5cf6" stroke-width="1.2"/>
<line x1="120" y1="30" x2="120" y2="130" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="4 3"/>
<text x="124" y="82" font-size="10" fill="#ef4444">h</text>
<text x="78" y="148" font-size="10" fill="#8b5cf6">棱锥 V=1/3·S·h</text>
</svg>''',
"bayes_tree": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="40" cy="80" r="6" fill="#10b981"/>
<circle cx="140" cy="40" r="5" fill="#0891b2"/>
<circle cx="140" cy="120" r="5" fill="#0891b2"/>
<circle cx="210" cy="25" r="4" fill="#ef4444"/>
<circle cx="210" cy="55" r="4" fill="#94a3b8"/>
<circle cx="210" cy="105" r="4" fill="#ef4444"/>
<circle cx="210" cy="135" r="4" fill="#94a3b8"/>
<line x1="46" y1="78" x2="135" y2="42" stroke="#94a3b8" stroke-width="1.2"/>
<line x1="46" y1="82" x2="135" y2="118" stroke="#94a3b8" stroke-width="1.2"/>
<line x1="145" y1="40" x2="206" y2="27" stroke="#94a3b8" stroke-width="1"/>
<line x1="145" y1="40" x2="206" y2="53" stroke="#94a3b8" stroke-width="1"/>
<line x1="145" y1="120" x2="206" y2="107" stroke="#94a3b8" stroke-width="1"/>
<line x1="145" y1="120" x2="206" y2="133" stroke="#94a3b8" stroke-width="1"/>
<text x="30" y="100" font-size="9" fill="#10b981">A</text>
<text x="120" y="36" font-size="9" fill="#0891b2">B₁</text>
<text x="120" y="116" font-size="9" fill="#0891b2">B₂</text>
<text x="200" y="22" font-size="8" fill="#ef4444">A|B₁</text>
<text x="200" y="148" font-size="8" fill="#475569">A|B₂</text>
</svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","note":"备 注"}

CORE_FORMULAS = [
    ("集合交换律", "A\\cap B = B\\cap A,\\quad A\\cup B = B\\cup A", "交集与并集满足交换律"),
    ("集合结合律", "(A\\cap B)\\cap C = A\\cap(B\\cap C)", "交集与并集满足结合律"),
    ("德摩根律·交", "\\complement_U(A\\cap B) = \\complement_U A \\cup \\complement_U B", "补集对交集的对偶"),
    ("德摩根律·并", "\\complement_U(A\\cup B) = \\complement_U A \\cap \\complement_U B", "补集对并集的对偶"),
    ("容斥原理·二元", "|A\\cup B| = |A|+|B|-|A\\cap B|", "两集合并集的元素个数"),
    ("容斥原理·三元", "|A\\cup B\\cup C| = |A|+|B|+|C|-|A\\cap B|-|B\\cap C|-|C\\cap A|+|A\\cap B\\cap C|", "三集合并集的元素个数"),
    ("子集个数", "|\\mathcal{P}(A)|=2^{|A|}", "n 元集合的子集总数"),
    ("绝对值定义", "|a|=\\begin{cases}a,&a\\ge0\\\\-a,&a<0\\end{cases}", "绝对值的分段定义"),
    ("绝对值乘性", "|ab|=|a|\\cdot|b|", "乘积的绝对值等于绝对值之积"),
    ("三角不等式", "|a|-|b|\\le|a\\pm b|\\le|a|+|b|", "绝对值三角不等式"),
    ("完全平方公式", "(a\\pm b)^2 = a^2 \\pm 2ab + b^2", "二项式平方展开"),
    ("平方差公式", "a^2 - b^2 = (a+b)(a-b)", "因式分解基本公式"),
    ("立方和公式", "a^3+b^3 = (a+b)(a^2-ab+b^2)", "立方和分解"),
    ("立方差公式", "a^3-b^3 = (a-b)(a^2+ab+b^2)", "立方差分解"),
    ("三数完全平方", "(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca", "三数和的平方展开"),
    ("二项式定理", "(a+b)^n = \\sum_{k=0}^n \\binom{n}{k} a^{n-k}b^k", "二项式展开"),
    ("一元二次求根", "x = \\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}", "ax²+bx+c=0 的求根公式"),
    ("判别式", "\\Delta = b^2-4ac", "判别二次方程实根个数"),
    ("韦达定理·和", "x_1+x_2=-\\dfrac{b}{a}", "两根之和"),
    ("韦达定理·积", "x_1x_2=\\dfrac{c}{a}", "两根之积"),
    ("有理根定理", "x=\\dfrac{p}{q}\\ (p|a_0,\\ q|a_n)", "整系数多项式有理根的可能值"),
    ("基本不等式", "a^2+b^2\\ge 2ab", "平方和非负的推论"),
    ("均值不等式·二元", "\\dfrac{a+b}{2}\\ge\\sqrt{ab}\\ (a,b>0)", "算术平均不小于几何平均"),
    ("均值不等式链", "\\dfrac{2}{\\frac{1}{a}+\\frac{1}{b}}\\le\\sqrt{ab}\\le\\dfrac{a+b}{2}\\le\\sqrt{\\dfrac{a^2+b^2}{2}}", "调和≤几何≤算术≤平方平均"),
    ("常见放缩·平方", "\\dfrac{1}{n^2}<\\dfrac{1}{n(n-1)}\\ (n\\ge2)", "平方裂项放缩"),
    ("常见放缩·阶乘", "n!<n^n\\ (n\\ge2)", "阶乘不超过 n 的 n 次幂"),
    ("常见放缩·指数", "2^n>n^2\\ (n\\ge5)", "指数增长快于多项式"),
    ("常见放缩·对数", "\\ln(1+x)<x\\ (x>0)", "对数上界"),
    ("常见放缩·指数函数", "e^x\\ge 1+x", "指数函数下界"),
    ("常见放缩·正弦", "\\sin x<x\\ (x>0)", "正弦不超过自变量"),
    ("常见放缩·根差", "\\sqrt{n+1}-\\sqrt{n}<\\dfrac{1}{2\\sqrt{n}}", "根式差的有理化放缩"),
    ("同角关系·平方", "\\sin^2\\alpha+\\cos^2\\alpha=1", "正弦余弦平方和为 1"),
    ("同角关系·商", "\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}", "正切等于正弦比余弦"),
    ("同角关系·倒数", "\\cot\\alpha=\\dfrac{1}{\\tan\\alpha},\\ \\sec\\alpha=\\dfrac{1}{\\cos\\alpha},\\ \\csc\\alpha=\\dfrac{1}{\\sin\\alpha}", "余切正割余割定义"),
    ("同角关系·切平方", "1+\\tan^2\\alpha=\\sec^2\\alpha", "正切正割平方关系"),
    ("同角关系·余切平方", "1+\\cot^2\\alpha=\\csc^2\\alpha", "余切余割平方关系"),
    ("诱导公式·π-α", "\\sin(\\pi-\\alpha)=\\sin\\alpha,\\ \\cos(\\pi-\\alpha)=-\\cos\\alpha", "奇变偶不变符号看象限"),
    ("诱导公式·π/2-α", "\\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\cos\\alpha,\\ \\cos\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\sin\\alpha", "互余关系"),
    ("和角正弦", "\\sin(\\alpha+\\beta)=\\sin\\alpha\\cos\\beta+\\cos\\alpha\\sin\\beta", "正弦和角公式"),
    ("和角余弦", "\\cos(\\alpha+\\beta)=\\cos\\alpha\\cos\\beta-\\sin\\alpha\\sin\\beta", "余弦和角公式"),
    ("倍角正弦", "\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha", "二倍角正弦"),
    ("倍角余弦", "\\cos 2\\alpha=\\cos^2\\alpha-\\sin^2\\alpha=2\\cos^2\\alpha-1=1-2\\sin^2\\alpha", "二倍角余弦三种形式"),
    ("倍角正切", "\\tan 2\\alpha=\\dfrac{2\\tan\\alpha}{1-\\tan^2\\alpha}", "二倍角正切"),
    ("半角正弦", "\\sin\\dfrac{\\alpha}{2}=\\pm\\sqrt{\\dfrac{1-\\cos\\alpha}{2}}", "半角正弦"),
    ("半角余弦", "\\cos\\dfrac{\\alpha}{2}=\\pm\\sqrt{\\dfrac{1+\\cos\\alpha}{2}}", "半角余弦"),
    ("半角正切", "\\tan\\dfrac{\\alpha}{2}=\\dfrac{1-\\cos\\alpha}{\\sin\\alpha}=\\dfrac{\\sin\\alpha}{1+\\cos\\alpha}", "半角正切有理式"),
    ("对数换底", "\\log_a b = \\dfrac{\\log_c b}{\\log_c a}", "对数换底公式"),
    ("对数运算·积", "\\log_a(MN)=\\log_aM+\\log_aN", "积的对数等于对数之和"),
    ("对数运算·商", "\\log_a\\dfrac{M}{N}=\\log_aM-\\log_aN", "商的对数等于对数之差"),
    ("对数运算·幂", "\\log_a M^n = n\\log_a M", "幂的对数"),
    ("指数运算", "a^m\\cdot a^n=a^{m+n},\\ (a^m)^n=a^{mn}", "指数运算法则"),
    ("等差数列通项", "a_n = a_1 + (n-1)d", "公差为 d 的等差数列第 n 项"),
    ("等差数列求和", "S_n = \\dfrac{n(a_1+a_n)}{2} = na_1+\\dfrac{n(n-1)}{2}d", "前 n 项和"),
    ("等差中项", "2A=a+b \\Rightarrow A=\\dfrac{a+b}{2}", "a,b 的等差中项"),
    ("等差片段和", "S_n,\\ S_{2n}-S_n,\\ S_{3n}-S_{2n}\\text{ 成等差}", "片段和的等差性质"),
    ("等差求和二次型", "S_n=An^2+Bn\\ (A=\\dfrac{d}{2},B=a_1-\\dfrac{d}{2})", "前 n 项和是 n 的二次函数"),
    ("等比数列通项", "a_n = a_1 q^{n-1}", "公比为 q 的等比数列第 n 项"),
    ("等比数列求和", "S_n = \\dfrac{a_1(1-q^n)}{1-q}\\ (q\\neq 1)", "前 n 项和"),
    ("无穷等比级数", "S = \\dfrac{a_1}{1-q}\\ (|q|<1)", "公比绝对值小于 1 时的和"),
    ("等比中项", "G^2=ab \\Rightarrow G=\\pm\\sqrt{ab}", "a,b 的等比中项"),
    ("裂项·相邻", "\\dfrac{1}{n(n+1)}=\\dfrac{1}{n}-\\dfrac{1}{n+1}", "相邻整数乘积的裂项"),
    ("平方和公式", "\\sum_{k=1}^n k^2=\\dfrac{n(n+1)(2n+1)}{6}", "前 n 个自然数平方和"),
    ("立方和公式", "\\sum_{k=1}^n k^3=\\left[\\dfrac{n(n+1)}{2}\\right]^2", "前 n 个自然数立方和"),
    ("勾股定理", "a^2+b^2 = c^2", "直角三角形两直角边平方和等于斜边平方"),
    ("正弦定理", "\\dfrac{a}{\\sin A} = \\dfrac{b}{\\sin B} = \\dfrac{c}{\\sin C} = 2R", "三角形边与对角正弦之比"),
    ("余弦定理", "c^2 = a^2+b^2-2ab\\cos C", "已知两边夹角求第三边"),
    ("三角形面积·底高", "S = \\dfrac{1}{2}ah", "底乘高除以二"),
    ("三角形面积·夹角", "S = \\dfrac{1}{2}ab\\sin C", "两边及其夹角求面积"),
    ("海伦公式", "S = \\sqrt{p(p-a)(p-b)(p-c)},\\ p=\\dfrac{a+b+c}{2}", "已知三边求面积"),
    ("平行四边形面积", "S = ah = ab\\sin\\theta", "底乘高或两边夹角"),
    ("矩形面积", "S = ab", "长乘宽"),
    ("菱形面积", "S = \\dfrac{1}{2}d_1d_2", "对角线乘积一半"),
    ("正方形面积", "S = a^2", "边长平方"),
    ("梯形面积", "S = \\dfrac{(a+b)h}{2}", "上底加下底乘高除以二"),
    ("梯形中位线", "m=\\dfrac{a+b}{2}", "梯形中位线长"),
    ("圆周长", "C = 2\\pi r", "圆的周长公式"),
    ("圆面积", "S = \\pi r^2", "圆的面积公式"),
    ("垂径定理", "CD\\perp AB \\Rightarrow AE=EB", "垂直于弦的直径平分弦"),
    ("圆心角定理", "\\angle AOB = 2\\angle ACB", "圆心角等于两倍圆周角"),
    ("切线性质", "PT\\perp OT", "切线垂直于过切点的半径"),
    ("切割线定理", "PT^2 = PA\\cdot PB", "切线长是割线两段的比例中项"),
    ("扇形弧长", "l = \\alpha r = \\dfrac{n\\pi r}{180}", "弧长与圆心角关系"),
    ("扇形面积", "S = \\dfrac{1}{2}lr = \\dfrac{1}{2}\\alpha r^2", "扇形面积公式"),
    ("球表面积", "S = 4\\pi R^2", "球面面积"),
    ("球体积", "V = \\dfrac{4}{3}\\pi R^3", "球的体积"),
    ("圆柱体积", "V = \\pi r^2 h", "底面积乘高"),
    ("圆锥体积", "V = \\dfrac{1}{3}\\pi r^2 h", "同底等高圆柱体积的 1/3"),
    ("棱柱体积", "V_{\\text{柱}} = Sh", "底面积乘高"),
    ("棱锥体积", "V_{\\text{锥}} = \\dfrac{1}{3}Sh", "锥体积是同底等高柱的 1/3"),
    ("台体体积", "V_{\\text{台}} = \\dfrac{1}{3}h(S_{上}+\\sqrt{S_{上}S_{下}}+S_{下})", "台体体积一般公式"),
    ("点面距离", "d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}", "点到平面距离"),
    ("两点距离", "d = \\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}", "平面内两点间距离"),
    ("点到直线距离", "d = \\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}", "点到直线的距离"),
    ("圆方程", "(x-a)^2+(y-b)^2 = r^2", "圆心 (a,b) 半径 r 的圆"),
    ("椭圆标准方程", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2} = 1\\ (a>b>0)", "焦点在 x 轴的椭圆"),
    ("双曲线标准方程", "\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2} = 1", "焦点在 x 轴的双曲线"),
    ("双曲线渐近线", "y=\\pm\\dfrac{b}{a}x", "双曲线渐近线方程"),
    ("抛物线标准方程", "y^2 = 2px\\ (p>0)", "开口向右的抛物线"),
    ("抛物线焦点准线", "F\\left(\\dfrac{p}{2},0\\right),\\ x=-\\dfrac{p}{2}", "y^2=2px 的焦点与准线"),
    ("平面向量数量积", "\\vec{a}\\cdot\\vec{b}=x_1x_2+y_1y_2", "平面向量数量积坐标式"),
    ("空间向量数量积", "\\vec{a}\\cdot\\vec{b}=x_1x_2+y_1y_2+z_1z_2", "空间向量数量积坐标式"),
    ("向量夹角", "\\cos\\theta=\\dfrac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}||\\vec{b}|}", "两向量夹角余弦"),
    ("三角形重心性质", "AG:GD=2:1", "重心分中线为 2:1"),
    ("三角形内切圆半径", "r=\\dfrac{S}{p}", "p 为半周长"),
    ("三角形外接圆半径", "R=\\dfrac{abc}{4S}", "外接圆半径"),
    ("平行线判定", "\\text{内错角相等}\\Rightarrow a\\parallel b", "平行线判定（内错角）"),
    ("空间曲线投影柱面", "\\text{消去 }z:\\ H(x,y)=0", "投影到 xOy 面的柱面方程"),
    ("极坐标互化", "x=\\rho\\cos\\theta,\\ y=\\rho\\sin\\theta,\\ \\rho^2=x^2+y^2", "极坐标与直角坐标互化"),
    ("柱坐标关系", "x=\\rho\\cos\\theta,\\ y=\\rho\\sin\\theta,\\ z=z", "柱坐标与直角坐标关系"),
    ("球坐标关系", "x=r\\sin\\varphi\\cos\\theta,\\ y=r\\sin\\varphi\\sin\\theta,\\ z=r\\cos\\varphi", "球坐标与直角坐标关系"),
    ("空间直线对称式", "\\dfrac{x-x_0}{m}=\\dfrac{y-y_0}{n}=\\dfrac{z-z_0}{p}", "过点方向向量的直线"),
    ("平面点法式", "A(x-x_0)+B(y-y_0)+C(z-z_0)=0", "过点法向量的平面"),
    ("椭球面", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}+\\dfrac{z^2}{c^2}=1", "椭球面标准方程"),
    ("单叶双曲面", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=1", "单叶双曲面"),
    ("双叶双曲面", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=-1", "双叶双曲面"),
    ("椭圆抛物面", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=z", "椭圆抛物面"),
    ("双曲抛物面", "\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=z", "马鞍面"),
    ("二次锥面", "\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=0", "二次锥面"),
    ("圆柱螺旋线", "x=a\\cos t,\\ y=a\\sin t,\\ z=bt", "圆柱螺旋线参数方程"),
    ("螺旋线弧长", "s=\\sqrt{a^2+b^2}\\cdot t", "螺旋线一段弧长"),
    ("排列数", "A_n^m = \\dfrac{n!}{(n-m)!}", "从 n 个中取 m 个的排列数"),
    ("组合数", "C_n^m = \\dfrac{n!}{m!(n-m)!}", "从 n 个中取 m 个的组合数"),
    ("组合恒等式·对称", "C_n^m = C_n^{n-m}", "组合数对称性"),
    ("组合恒等式·帕斯卡", "C_n^m = C_{n-1}^m+C_{n-1}^{m-1}", "帕斯卡恒等式"),
    ("二项式通项", "T_{k+1}=\\binom{n}{k}a^{n-k}b^k", "二项展开第 k+1 项"),
    ("古典概型", "P(A) = \\dfrac{m}{n}", "事件 A 含 m 个基本事件共 n 个等可能"),
    ("互斥事件加法", "P(A\\cup B) = P(A)+P(B)", "A、B 互斥时的概率加法"),
    ("独立事件乘法", "P(A\\cap B) = P(A)\\cdot P(B)", "A、B 独立时的概率乘法"),
    ("条件概率", "P(A|B) = \\dfrac{P(A\\cap B)}{P(B)}", "B 发生条件下 A 发生的概率"),
    ("全概率公式", "P(A) = \\sum_i P(B_i)P(A|B_i)", "由分割 B_i 求 A 的概率"),
    ("贝叶斯公式", "P(B_i|A) = \\dfrac{P(B_i)P(A|B_i)}{\\sum_j P(B_j)P(A|B_j)}", "后验概率公式"),
    ("期望", "E(X) = \\sum_i x_i p_i", "离散型随机变量的数学期望"),
    ("方差", "D(X) = E[(X-E(X))^2] = E(X^2)-[E(X)]^2", "随机变量的方差"),
    ("二项分布概率", "P(X=k)=\\binom{n}{k}p^k(1-p)^{n-k}", "X~B(n,p) 的分布列"),
    ("二项分布期望方差", "E(X)=np,\\ D(X)=np(1-p)", "二项分布的期望与方差"),
    ("正态分布密度", "f(x) = \\dfrac{1}{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}", "N(μ,σ²) 的概率密度"),
    ("3σ 原则", "P(\\mu-3\\sigma<X<\\mu+3\\sigma)\\approx 99.7\\%", "正态分布的 3σ 范围"),
    ("样本均值", "\\bar{x} = \\dfrac{1}{n}\\sum_{i=1}^n x_i", "样本算术平均值"),
    ("样本方差", "s^2 = \\dfrac{1}{n}\\sum_{i=1}^n (x_i-\\bar{x})^2", "样本方差"),
    ("线性回归斜率", "b = \\dfrac{\\sum(x_i-\\bar{x})(y_i-\\bar{y})}{\\sum(x_i-\\bar{x})^2}", "回归直线斜率"),
    ("反三角关系", "\\arcsin x+\\arccos x=\\dfrac{\\pi}{2}", "反正弦与反余弦互补"),
    ("函数单调性定义", "\\forall x_1<x_2:\\ f(x_1)<f(x_2)\\ (\\text{增})", "严格单调递增的定义"),
    ("奇函数定义", "f(-x)=-f(x)", "奇函数关于原点对称"),
    ("偶函数定义", "f(-x)=f(x)", "偶函数关于 y 轴对称"),
    ("周期函数", "f(x+T)=f(x)", "T 为函数的周期"),
    ("指数函数", "y=a^x\\ (a>0,a\\neq1)", "指数函数定义"),
    ("对数函数", "y=\\log_a x\\ (a>0,a\\neq1,x>0)", "对数函数定义"),
    ("幂函数", "y=x^\\alpha", "幂函数定义"),
    ("几何概型", "P(A)=\\dfrac{\\mu(A)}{\\mu(\\Omega)}", "几何概型概率公式"),
    ("组合恒等式·求和", "\\sum_{k=0}^n C_n^k=2^n", "组合数求和"),
    ("三角形内角和", "A+B+C=\\pi", "三角形三内角之和"),
    ("圆周角定理", "\\angle ACB = \\dfrac{1}{2}\\angle AOB", "同弧所对圆周角是圆心角之半"),
    ("二面角", "\\cos\\varphi=\\pm\\dfrac{\\vec{n_1}\\cdot\\vec{n_2}}{|\\vec{n_1}||\\vec{n_2}|}", "二面角的余弦"),
    ("空间两点距离", "|P_1P_2| = \\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}", "空间两点距离"),
    ("平面一般式", "Ax+By+Cz+D=0", "平面的一般方程"),
    ("相交弦定理", "PA\\cdot PB = PC\\cdot PD", "圆内两弦交点分四段比例"),
    ("切线长定理", "PA=PB", "从圆外一点引两切线长相等"),
    ("双曲线离心率", "e=\\dfrac{c}{a}>1,\\ c^2=a^2+b^2", "双曲线离心率大于 1"),
    ("椭圆离心率", "e=\\dfrac{c}{a}\\in(0,1),\\ c^2=a^2-b^2", "椭圆扁平程度"),
]

def js_escape(s): return s.replace("\\","\\\\").replace("`","\\`").replace("${","\\${")
def fix_lt_math(s):
    import re
    return re.sub(r"\$\$[\s\S]*?\$\$|\$[^$\n]*?\$", lambda m: m.group(0).replace("<", "&lt;"), s)
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

# ============ 第一章 集合与逻辑 ============
# ============ 第一章 集合与逻辑 ============
ch1_sections = [
{"name":"1.1 集合概念、运算与德摩根律","color":"#2563eb","desc":"集合表示、交并补与德摩根律推导",
"items":[
{"id":"e1s1-1","name":"集合的概念与表示","tags":["def","der","exa"],"brief":"集合元素三大特性、列举法与描述法、子集个数推导。",
"body":wrap(
 defn("集合与元素",p("具有某种特定性质的事物的总体称为<strong>集合</strong>，组成集合的事物称为<strong>元素</strong>。若 $a$ 是集合 $A$ 的元素，记作 $a\\in A$；否则记作 $a\\notin A$。"))+
 note(p("集合中的元素具有<strong>确定性、互异性、无序性</strong>三大特性：确定性要求任一对象是否属于该集合都能明确判断；互异性要求同一集合内不出现重复元素；无序性要求元素排列顺序不影响集合本身。"))+
 der(p("<strong>第一步（互异性的应用）：</strong>已知 $\\{1,2,a\\}=\\{1,2,3\\}$。由两集合相等，元素必须完全一致。假设 $a\\ne 3$，则 $a\\in\\{1,2,3\\}$ 只能是 $a=1$ 或 $a=2$。")+
 p("<strong>第二步（反证排除）：</strong>若 $a=1$，则 $\\{1,2,a\\}=\\{1,2\\}$，缺少元素 $3$，与两集合相等矛盾；若 $a=2$，同理 $\\{1,2,a\\}=\\{1,2\\}$，仍然矛盾。故假设不成立。")+
 p("<strong>第三步（得出结论）：</strong>由前两步排除，唯一可能是 $a=3$；代回验证 $\\{1,2,3\\}=\\{1,2,3\\}$ 成立。这里正是「互异性」在起作用——元素不能因取值而重复。")+
 p("<strong>第四步（子集个数的分类）：</strong>对 $n$ 元集合 $A$，按其子集所含元素的个数 $k$ 分类计数，$k$ 可取 $0,1,2,\\dots,n$，而 $k$ 元子集的个数恰为组合数 $C_n^k$。")+
 fml("\\text{子集总数}=C_n^0+C_n^1+C_n^2+\\cdots+C_n^n")+
 p("<strong>第五步（二项式定理求和）：</strong>在二项式定理中令 $x=1$，即可把上式的组合数和化为一个幂。")+
 fml("(1+x)^n=\\sum_{k=0}^{n}C_n^k x^k,\\quad \\text{取 }x=1\\text{ 得 }\\sum_{k=0}^{n}C_n^k=(1+1)^n=2^n")+
 p("<strong>第六步（三种数目的关系）：</strong>故子集共 $2^n$ 个；去掉集合自身得真子集 $2^n-1$ 个；再去掉空集 $\\varnothing$ 得非空真子集 $2^n-2$ 个。"))+
 exa(p("<strong>常见数集：</strong>$\\mathbb{N}$ 自然数集、$\\mathbb{Z}$ 整数集、$\\mathbb{Q}$ 有理数集、$\\mathbb{R}$ 实数集。<br>三种表示法：① <strong>列举法</strong>（把元素一一列出）$A=\\{1,2,3\\}$；② <strong>描述法</strong>（刻画元素共性）$A=\\{x\\mid x>0,\\,x\\in\\mathbb{R}\\}$；③ <strong>图示法</strong>（用韦恩图画圈表示）。")+
 p("<strong>例：</strong>集合 $B=\\{x\\mid x^2-3x+2=0\\}$，解方程得 $x=1$ 或 $x=2$，故 $B=\\{1,2\\}$。其全部子集为 $\\varnothing,\\{1\\},\\{2\\},\\{1,2\\}$，个数恰为 $2^2=4$，与公式一致。")))
},
{"id":"e1s1-2","name":"集合的交、并、补与德摩根律","tags":["def","thm","der"],"brief":"交集、并集、补集定义与德摩根律双向推导。",
"fig":"set_venn","figCap":"集合 A 与 B 的韦恩图，重叠区为 A∩B",
"body":wrap(
 defn("交集",p("由所有既属于 $A$ 又属于 $B$ 的元素组成的集合称为 $A$ 与 $B$ 的<strong>交集</strong>：")+
 fml("A\\cap B=\\{x\\mid x\\in A\\text{ 且 }x\\in B\\}"))+
 defn("并集",p("由所有属于 $A$ 或属于 $B$ 的元素组成的集合称为 $A$ 与 $B$ 的<strong>并集</strong>：")+
 fml("A\\cup B=\\{x\\mid x\\in A\\text{ 或 }x\\in B\\}"))+
 defn("补集",p("设 $U$ 为全集，$A\\subseteq U$，则 $U$ 中所有不属于 $A$ 的元素组成的集合称为 $A$ 在 $U$ 中的<strong>补集</strong>：")+
 fml("\\complement_U A=\\{x\\mid x\\in U\\text{ 且 }x\\notin A\\}"))+
 thm("德摩根律",p("补集对交、并运算满足如下对偶关系：")+
 fml("\\complement_U(A\\cap B)=\\complement_U A\\cup\\complement_U B,\\qquad \\complement_U(A\\cup B)=\\complement_U A\\cap\\complement_U B"))+
 der(p("<strong>第一式 · 证明左包含右：</strong>任取 $x\\in\\complement_U(A\\cap B)$，由补集定义得 $x\\in U$ 且 $x\\notin A\\cap B$。")+
 p("<strong>第一步（否定交集）：</strong>$x\\notin A\\cap B$ 意味着命题「$x\\in A$ 且 $x\\in B$」不成立，由逻辑否定律得 $x\\notin A$ 或 $x\\notin B$。")+
 p("<strong>第二步（并入补集）：</strong>结合 $x\\in U$：由 $x\\notin A$ 得 $x\\in\\complement_U A$；由 $x\\notin B$ 得 $x\\in\\complement_U B$。二者至少有一个成立，故 $x\\in\\complement_U A\\cup\\complement_U B$，于是 $\\complement_U(A\\cap B)\\subseteq\\complement_U A\\cup\\complement_U B$。")+
 p("<strong>第三步（证明右包含左）：</strong>反向任取 $x\\in\\complement_U A\\cup\\complement_U B$，则 $x\\in\\complement_U A$ 或 $x\\in\\complement_U B$，即 $x\\notin A$ 或 $x\\notin B$。于是「$x\\in A$ 且 $x\\in B$」不成立，即 $x\\notin A\\cap B$；又 $x\\in U$，故 $x\\in\\complement_U(A\\cap B)$，得 $\\complement_U A\\cup\\complement_U B\\subseteq\\complement_U(A\\cap B)$。")+
 p("<strong>第四步（双向包含得相等）：</strong>两个方向的包含均成立，故 $\\complement_U(A\\cap B)=\\complement_U A\\cup\\complement_U B$，第一式得证。")+
 p("<strong>第五步（由第一式推第二式）：</strong>在第一式中用 $\\complement_U A$ 代 $A$、$\\complement_U B$ 代 $B$，并注意补集的补集 $\\complement_U(\\complement_U A)=A$。")+
 fml("\\complement_U(\\complement_U A\\cap\\complement_U B)=A\\cup B\\quad\\Longrightarrow\\quad \\complement_U(A\\cup B)=\\complement_U A\\cap\\complement_U B")+
 p("对最后一式两边同时取补集即得第二式，德摩根律两式全部得证。一般地，该对偶关系可推广到任意有限多个集合。"))+
 exa(p("<strong>例：</strong>设 $U=\\{1,2,3,4,5\\}$，$A=\\{1,2\\}$，$B=\\{2,3\\}$。则 $A\\cap B=\\{2\\}$，$A\\cup B=\\{1,2,3\\}$，$\\complement_U A=\\{3,4,5\\}$，$\\complement_U B=\\{1,4,5\\}$。验证第一式：$\\complement_U(A\\cap B)=\\{1,3,4,5\\}$，而 $\\complement_U A\\cup\\complement_U B=\\{3,4,5\\}\\cup\\{1,4,5\\}=\\{1,3,4,5\\}$，两者相等。")))
}
]},
{"name":"1.2 子集与容斥原理","color":"#0ea5e9","desc":"子集、真子集、集合相等与容斥原理",
"items":[
{"id":"e1s2-1","name":"子集与容斥原理","tags":["def","thm","der","exa"],"brief":"子集、真子集、集合相等、二元与三元容斥原理。",
"body":wrap(
 defn("子集",p("若集合 $A$ 的每一个元素都属于 $B$，则称 $A$ 是 $B$ 的<strong>子集</strong>，记作 $A\\subseteq B$。特别地，空集 $\\varnothing$ 是任何集合的子集，任何集合都是它自身的子集。"))+
 defn("集合相等",p("若 $A\\subseteq B$ 且 $B\\subseteq A$，则 $A=B$；反之，若 $A=B$ 则两方向包含同时成立。即两集合相等 $\\Leftrightarrow$ 二者互为子集。"))+
 defn("真子集",p("若 $A\\subseteq B$ 且存在 $b\\in B$ 使 $b\\notin A$（即 $B$ 中至少有一个元素不属于 $A$），则称 $A$ 是 $B$ 的<strong>真子集</strong>，记作 $A\\subsetneq B$。"))+
 thm("子集个数",p("含 $n$ 个元素的集合共有 $2^n$ 个子集，$2^n-1$ 个真子集，$2^n-2$ 个非空真子集。"))+
 der(p("<strong>推导（乘法原理）：</strong>构造 $A$ 的任一子集时，对 $A$ 的每个元素都只需决定「选入子集」或「不选入子集」两种处理方式。$n$ 个元素各自独立地二选一，由乘法原理共有 $2^n$ 种取法，故子集总数为 $2^n$。去掉 $A$ 自身得真子集 $2^n-1$ 个，再去掉空集得非空真子集 $2^n-2$ 个。"))+
 thm("二元容斥原理",p("设 $A,B$ 为有限集，则")+
 fml("|A\\cup B|=|A|+|B|-|A\\cap B|"))+
 der(p("<strong>二元容斥 · 推导：</strong>把 $A\\cup B$ 的元素按来源分为三类——只属于 $A$、只属于 $B$、同时属于两者。")+
 p("<strong>第一步（重复计数）：</strong>直接相加 $|A|+|B|$ 时，既属于 $A$ 又属于 $B$ 的元素（即 $A\\cap B$ 中每个元素）被计算了两次，一次在 $|A|$ 中、一次在 $|B|$ 中。")+
 p("<strong>第二步（减法修正）：</strong>要得到并集的真实元素个数，须减去多算一次的部分，即 $|A\\cup B|=|A|+|B|-|A\\cap B|$。"))+
 thm("三元容斥原理",p("设 $A,B,C$ 为有限集，则")+
 fml("|A\\cup B\\cup C|=|A|+|B|+|C|-|A\\cap B|-|B\\cap C|-|C\\cap A|+|A\\cap B\\cap C|"))+
 der(p("<strong>三元容斥 · 推导（逐步补偿）：</strong>")+
 p("<strong>第一步（求和）：</strong>先求 $|A|+|B|+|C|$，此时两两交集 $A\\cap B$、$B\\cap C$、$C\\cap A$ 中的元素各被多算了一次。")+
 p("<strong>第二步（减去两两交）：</strong>减去 $|A\\cap B|+|B\\cap C|+|C\\cap A|$，于是两两交集中「只属于两个集合」的元素被恰好纠正。")+
 p("<strong>第三步（考察三交）：</strong>三重交 $A\\cap B\\cap C$ 的元素同时属于三个集合：它在第一步被算了 $3$ 次，在第二步又被减去 $3$ 次，净计数为 $3-3=0$。")+
 p("<strong>第四步（补回一次）：</strong>为使三交元素计数恢复为 $1$，需再加回 $|A\\cap B\\cap C|$，即得三元容斥公式。"))+
 exa(p("<strong>例（二元）：</strong>某班 $50$ 人，喜欢数学 $30$ 人，喜欢物理 $25$ 人，两科都喜欢 $15$ 人。至少喜欢一科的人数为 $|A\\cup B|=30+25-15=40$ 人，故两科都不喜欢的有 $50-40=10$ 人。")+
 p("<strong>例（三元）：</strong>某班 $40$ 人中，参加数学竞赛 $20$ 人、物理 $15$ 人、化学 $10$ 人；数理双报 $8$ 人、理化双报 $5$ 人、数化双报 $6$ 人，三科都报 $2$ 人。至少参加一科的人数为 $20+15+10-8-5-6+2=28$ 人。")))
}
]},
{"name":"1.3 命题、充要条件与量词","color":"#0284c7","desc":"四种命题关系、充要条件、全称存在量词",
"items":[
{"id":"e1s3-1","name":"命题与四种命题","tags":["def","thm","der"],"brief":"原命题、逆命题、否命题、逆否命题及其等价性。",
"body":wrap(
 defn("命题",p("可以判断真假的陈述句称为<strong>命题</strong>。判断为真的叫真命题，判断为假的叫假命题。不能判断真假的语句（如疑问句、祈使句）不是命题。"))+
 defn("四种命题",p("设原命题为「若 $p$，则 $q$」，记作 $p\\Rightarrow q$，其中 $p$ 是条件、$q$ 是结论。则：① <strong>逆命题</strong>：若 $q$ 则 $p$；② <strong>否命题</strong>：若 $\\neg p$ 则 $\\neg q$；③ <strong>逆否命题</strong>：若 $\\neg q$ 则 $\\neg p$。"))+
 note(p("注意区分「否命题」与「命题的否定」：否命题是同时否定条件与结论（$\\neg p\\Rightarrow\\neg q$），而命题的否定只否定整个命题，其形式为「$p$ 且 $\\neg q$」，二者含义不同。"))+
 thm("等价性",p("原命题与其逆否命题同真同假（互为等价）；逆命题与否命题同真同假；而原命题与逆命题、否命题之间的真假没有必然联系。"))+
 der(p("<strong>逆否命题等价性 · 推导（真值表法）：</strong>逐一举出 $p,q$ 的四种取值组合，比较「原命题 $p\\Rightarrow q$」与「逆否命题 $\\neg q\\Rightarrow\\neg p$」的真假。")+
 p("<strong>情形①：</strong>$p$ 真、$q$ 真。此时 $p\\Rightarrow q$ 为真；同时 $\\neg q$ 为假，以假为前提的蕴含式恒为真，故 $\\neg q\\Rightarrow\\neg p$ 也为真。两者同真。")+
 p("<strong>情形②：</strong>$p$ 真、$q$ 假。此时 $p\\Rightarrow q$ 为假（真推假）；又 $\\neg q$ 真而 $\\neg p$ 假，故 $\\neg q\\Rightarrow\\neg p$ 为假。两者同假。")+
 p("<strong>情形③：</strong>$p$ 假、$q$ 真。$p\\Rightarrow q$ 前提为假故为真；$\\neg q$ 为假，故 $\\neg q\\Rightarrow\\neg p$ 也为真。两者同真。")+
 p("<strong>情形④：</strong>$p$ 假、$q$ 假。$p\\Rightarrow q$ 前提为假故为真；$\\neg q$ 真、$\\neg p$ 真，故 $\\neg q\\Rightarrow\\neg p$ 为真。两者同真。")+
 p("<strong>结论：</strong>四种情形下两命题的真值逐一对应、完全相同，故原命题与逆否命题等价。又因为逆命题与否命题互为逆否命题，由同一结论可知逆命题与否命题也等价。"))+
 exa(p("<strong>例：</strong>原命题「若 $x=1$，则 $x^2=1$」为真；其逆否命题「若 $x^2\\ne 1$，则 $x\\ne 1$」由等价性也必为真。而其逆命题「若 $x^2=1$，则 $x=1$」为假（$x=-1$ 时结论不成立），可见原命题真并不能保证逆命题真。")))
},
{"id":"e1s3-2","name":"充要条件与量词","tags":["def","der","exa"],"brief":"充分必要条件、充要条件、全称存在量词及其否定。",
"body":wrap(
 defn("充分条件与必要条件",p("若 $p\\Rightarrow q$（由 $p$ 能推出 $q$），则称 $p$ 是 $q$ 的<strong>充分条件</strong>，同时称 $q$ 是 $p$ 的<strong>必要条件</strong>。"))+
 defn("充要条件",p("若 $p\\Rightarrow q$ 且 $q\\Rightarrow p$，即 $p\\Leftrightarrow q$，则称 $p$ 是 $q$ 的<strong>充分必要条件</strong>（简称<strong>充要条件</strong>），此时 $p$ 与 $q$ 互为充要条件。"))+
 der(p("<strong>从集合角度看条件（推导）：</strong>设 $P=\\{x\\mid p(x)\\text{ 成立}\\}$，$Q=\\{x\\mid q(x)\\text{ 成立}\\}$。")+
 p("<strong>第一步（充分性对应包含）：</strong>若 $p\\Rightarrow q$ 对一切 $x$ 成立，则凡满足 $p$ 的 $x$ 必满足 $q$，即 $x\\in P\\Rightarrow x\\in Q$，故 $P\\subseteq Q$。反之若 $P\\subseteq Q$，则 $p$ 的成立范围被 $q$ 的成立范围包含，即 $p\\Rightarrow q$。")+
 p("<strong>第二步（必要性同理）：</strong>上式中 $Q\\supseteq P$，即 $q$ 的成立是 $p$ 成立所必不可少的前提，故 $p$ 是 $q$ 的充分条件等价于 $P\\subseteq Q$，$q$ 是 $p$ 的必要条件。")+
 p("<strong>第三步（充要条件）：</strong>若同时 $P\\subseteq Q$ 与 $Q\\subseteq P$，则 $P=Q$，即 $p\\Leftrightarrow q$，此时 $p$ 是 $q$ 的充要条件。于是条件的判断完全化归为集合的包含判断。")+
 p("<strong>第四步（四种关系细分）：</strong>若 $P\\subsetneq Q$，则 $p$ 是 $q$ 的充分不必要条件；若 $Q\\subsetneq P$，则 $p$ 是 $q$ 的必要不充分条件；若 $P=Q$，则 $p$ 是 $q$ 的充要条件；若 $P,Q$ 互不包含，则 $p$ 是 $q$ 的既不充分也不必要条件。"))+
 exa(p("<strong>例：</strong>判断「$x=1$」是「$x^2=1$」的什么条件。设 $P=\\{1\\}$，$Q=\\{-1,1\\}$。由 $x=1\\Rightarrow x^2=1$ 得 $P\\subseteq Q$，故充分；但 $x^2=1$ 时 $x$ 还可为 $-1$，即存在 $x\\in Q$ 而 $x\\notin P$，故 $P\\subsetneq Q$，不必要。综上为充分不必要条件。")+
 p("<strong>例：</strong>「$ab=0$」与「$a=0$ 或 $b=0$」（$a,b\\in\\mathbb{R}$）互为充要条件，因为二者所对应的数对集合完全相同。"))+
 defn("全称量词与存在量词",p("<strong>全称量词</strong> $\\forall$ 表示「对任意」；<strong>存在量词</strong> $\\exists$ 表示「存在」。含全称量词的命题称为全称命题，含存在量词的命题称为特称（存在）命题。"))+
 der(p("<strong>量词否定 · 推导：</strong>")+
 p("<strong>第一步（全称命题的含义）：</strong>$\\forall x\\in M,\\,p(x)$ 表示「对 $M$ 中的每一个 $x$，都使 $p(x)$ 成立」。它的否定就是「并非每一个 $x$ 都使 $p(x)$ 成立」。")+
 p("<strong>第二步（转化为存在）：</strong>「并非每一个都成立」等价于「至少存在一个 $x$ 使 $p(x)$ 不成立」，即 $\\exists x\\in M,\\,\\neg p(x)$。")+
 fml("\\neg\\big(\\forall x\\in M,\\,p(x)\\big)=\\exists x\\in M,\\,\\neg p(x)")+
 p("<strong>第三步（存在命题的否定）：</strong>同理，$\\exists x\\in M,\\,p(x)$ 表示「存在使 $p(x)$ 成立的 $x$」，其否定是「不存在这样的 $x$」，即对所有 $x$ 都有 $p(x)$ 不成立。")+
 fml("\\neg\\big(\\exists x\\in M,\\,p(x)\\big)=\\forall x\\in M,\\,\\neg p(x)")+
 p("两式合起来即量词否定法则：全称量词与存在量词互换，同时否定其后的命题。"))+
 exa(p("<strong>例：</strong>命题「$\\forall x\\in\\mathbb{R},\\,x^2\\ge 0$」为真命题，其否定为「$\\exists x\\in\\mathbb{R},\\,x^2<0$」，为假命题。又如「$\\exists x\\in\\mathbb{R},\\,x^2=2$」为真，其否定「$\\forall x\\in\\mathbb{R},\\,x^2\\ne 2$」为假。")))
}
]}
]
# ============ 第二章 代数 ============
# ============ 第二章 代数 ============
ch2_sections = [
{"name":"2.1 数系基础","color":"#7c3aed","desc":"实数、有理数、整数与加减乘除运算律、绝对值",
"items":[
{"id":"e2s1-1","name":"实数、有理数与运算律","tags":["def","thm","der","app"],"brief":"数系包含关系、实数域运算律与由运算律导出的符号法则。",
"fig":"number_system","figCap":"数系包含关系 N ⊂ Z ⊂ Q ⊂ R",
"body":wrap(
 defn("数系",p("<strong>自然数集</strong> $\\mathbb{N}=\\{0,1,2,\\dots\\}$；<strong>整数集</strong> $\\mathbb{Z}=\\{\\dots,-2,-1,0,1,2,\\dots\\}$；<strong>有理数集</strong> $\\mathbb{Q}=\\left\\{\\dfrac{p}{q}:p\\in\\mathbb{Z},\\,q\\in\\mathbb{N}^*,\\ \\gcd(p,q)=1\\right\\}$；<strong>无理数</strong>是不能表示为两整数之比的实数，如 $\\sqrt{2},\\ \\pi,\\ e$。<strong>实数集</strong> $\\mathbb{R}$ 为有理数与无理数的全体，且 $\\mathbb{N}\\subset\\mathbb{Z}\\subset\\mathbb{Q}\\subset\\mathbb{R}$。")+
  p("数集按包含关系逐层扩张，每层都是为填补上一层的运算缺口：整数补齐减法，有理数补齐除法，实数补齐开方与取极限。"))+
 thm("实数域的运算律",p("对任意 $a,b,c\\in\\mathbb{R}$：")+
  fml("\\text{加法交换律}\\ a+b=b+a,\\qquad \\text{加法结合律}\\ (a+b)+c=a+(b+c)")+
  fml("\\text{乘法交换律}\\ ab=ba,\\qquad \\text{乘法结合律}\\ (ab)c=a(bc)")+
  fml("\\text{分配律}\\ a(b+c)=ab+ac")+
  fml("\\text{零元}\\ a+0=a,\\quad \\text{加法逆元}\\ a+(-a)=0,\\quad \\text{乘法单位元}\\ a\\cdot1=a"))+
 der(p("<strong>推导一（零乘任意数为零）：</strong>先证 $0\\cdot b=0$。由零元与分配律：")+
  fml("0\\cdot b=(0+0)\\cdot b=0\\cdot b+0\\cdot b")+
  p("两边同加 $-(0\\cdot b)$，由加法逆元得 $0=0\\cdot b$。")+
  p("<strong>推导二（相反数的乘法）：</strong>证 $(-a)b=-(ab)$。利用分配律与已证的零乘：")+
  fml("(-a)b+ab=(-a+a)b=0\\cdot b=0")+
  p("故 $(-a)b$ 与 $ab$ 之和为零，即 $(-a)b$ 是 $ab$ 的加法逆元，$(-a)b=-(ab)$。")+
  p("<strong>推导三（负负得正）：</strong>证 $(-a)(-b)=ab$。由推导二与分配律：")+
  fml("(-a)(-b)+a(-b)=(-a+a)(-b)=0\\cdot(-b)=0")+
  p("又 $a(-b)=-(ab)$，代入得 $(-a)(-b)-ab=0$，两边加 $ab$ 即 $(-a)(-b)=ab$。可见「负负得正」是运算律的必然推论，而非人为规定。"))+
 der(p("<strong>有理数的稠密性：</strong>对任意实数 $x$ 与任意 $\\epsilon>0$，总存在有理数 $r$ 使 $|x-r|<\\epsilon$，即有理数在实数中处处稠密。证明分三步。")+
  p("<strong>第一步（阿基米德性质）：</strong>取正整数 $n$ 使 $n>\\dfrac{1}{\\epsilon}$，则 $\\dfrac{1}{n}<\\epsilon$：")+
  fml("n>\\dfrac{1}{\\epsilon}\\ \\Longrightarrow\\ \\dfrac{1}{n}<\\epsilon")+
  p("<strong>第二步（取整夹逼）：</strong>令 $m=\\lfloor nx\\rfloor$ 为不超过 $nx$ 的最大整数，则 $m\\le nx<m+1$，两边除以 $n$：")+
  fml("\\dfrac{m}{n}\\le x<\\dfrac{m+1}{n}")+
  p("<strong>第三步（逼近）：</strong>取 $r=\\dfrac{m}{n}\\in\\mathbb{Q}$，则 $0\\le x-r<\\dfrac{1}{n}<\\epsilon$，故 $|x-r|<\\epsilon$。由于 $\\epsilon$ 任意小，有理数可无限逼近 $x$。"))+
 exa(p("<strong>例：</strong>用分配律简算 $25\\times99=25\\times(100-1)=25\\times100-25\\times1=2500-25=2475$；而 $(-3)\\times(-4)=12$ 正是推导三的直接应用。"))+
 app(p("<strong>应用：</strong>稠密性是极限与逼近的基础——计算 $\\sqrt{2}$ 时用一串有理数 $1.4,\\ 1.41,\\ 1.414,\\dots$ 逐步逼近，其误差可任意小，这正是一切实数计算与数值方法的理论依据。"))
)},
{"id":"e2s1-2","name":"绝对值定义与性质","tags":["def","thm","der","app"],"brief":"|a| 的代数定义与几何意义、乘积绝对值与三角不等式推导。",
"fig":"abs_value","figCap":"y=|x| 图像，V 形折线，顶点在原点",
"body":wrap(
 defn("绝对值",p("实数 $a$ 的<strong>绝对值</strong>定义为")+
  fml("|a|=\\begin{cases}\\ a,&a\\ge0\\\\ -a,&a<0\\end{cases}"))+
  p("几何意义：$|a|$ 表示数轴上点 $a$ 到原点的距离，$|a-b|$ 表示点 $a$ 与点 $b$ 之间的距离。由此 $|a|\\ge0$ 恒成立，且 $|a|=0\\Leftrightarrow a=0$。")+
 thm("绝对值的基本性质",p("对任意 $a,b\\in\\mathbb{R}$：")+
  fml("|ab|=|a|\\cdot|b|,\\qquad \\left|\\dfrac{a}{b}\\right|=\\dfrac{|a|}{|b|}\\ (b\\neq0)")+
  fml("|a|^2=a^2,\\qquad |a|=\\sqrt{a^2},\\qquad -|a|\\le a\\le|a|")+
  fml("\\big||a|-|b|\\big|\\le|a+b|\\le|a|+|b|\\qquad(\\text{三角不等式})"))+
 der(p("<strong>推导一（乘积的绝对值）：</strong>按符号分四种情况讨论。")+
  p("若 $a\\ge0,b\\ge0$，则 $ab\\ge0$，$|ab|=ab=|a||b|$；若 $a\\ge0,b<0$，则 $ab\\le0$，$|ab|=-ab=a\\cdot(-b)=|a||b|$；若 $a<0,b\\ge0$，同理 $|ab|=(-a)b=|a||b|$；若 $a<0,b<0$，则 $ab>0$，$|ab|=ab=(-a)(-b)=|a||b|$。四种情况合计得 $|ab|=|a||b|$。")+
  fml("|ab|=|a|\\,|b|\\quad\\text{（分四种符号情形逐一验证）}")+
  p("<strong>推导二（三角不等式右半）：</strong>由 $-|a|\\le a\\le|a|$ 与 $-|b|\\le b\\le|b|$，两式相加：")+
  fml("-\\big(|a|+|b|\\big)\\le a+b\\le|a|+|b|")+
  p("这正是 $|a+b|\\le|a|+|b|$。等号成立当且仅当 $ab\\ge0$（$a,b$ 同号或至少一个为零）。")+
  p("<strong>推导三（三角不等式左半）：</strong>把 $b$ 换成 $-b$ 得 $|a-b|\\le|a|+|b|$。又")+
  fml("|a|=\\big|(a+b)+(-b)\\big|\\le|a+b|+|-b|=|a+b|+|b|")+
  p("移项得 $|a|-|b|\\le|a+b|$；交换 $a,b$ 又得 $|b|-|a|\\le|a+b|$。合并即 $\\big||a|-|b|\\big|\\le|a+b|$。"))+
 app(p("<strong>应用：</strong>解 $|x-a|<b\\ (b>0)$ 时，用几何意义（到点 $a$ 的距离小于 $b$）直接得 $-b<x-a<b$，即 $a-b<x<a+b$；反之 $|x-a|>b$ 得 $x<a-b$ 或 $x>a+b$。"))
)},
{"id":"e2s1-3","name":"绝对值不等式与方程","tags":["thm","der","exa","note"],"brief":"|x|<a、|x|>a 型解集、平移推广、绝对值方程与含参讨论。",
"fig":"number_line","figCap":"数轴上 |x-a|<b 表示以 a 为中心、半宽为 b 的开区间",
"body":wrap(
 thm("绝对值不等式解集",p("设 $a>0$，则")+
  fml("|x|<a\\ \\Leftrightarrow\\ -a<x<a,\\qquad |x|\\le a\\ \\Leftrightarrow\\ -a\\le x\\le a")+
  fml("|x|>a\\ \\Leftrightarrow\\ x<-a\\ \\text{或}\\ x>a,\\qquad |x|\\ge a\\ \\Leftrightarrow\\ x\\le-a\\ \\text{或}\\ x\\ge a"))+
 der(p("<strong>推导一（几何法）：</strong>$|x|<a$ 表示数轴上点 $x$ 到原点的距离小于 $a$，故 $x$ 落在以原点为中心、半径 $a$ 的开区间内：")+
  fml("|x|<a\\ \\Leftrightarrow\\ x\\in(-a,a),\\qquad |x|>a\\ \\Leftrightarrow\\ x\\in(-\\infty,-a)\\cup(a,+\\infty)")+
  p("<strong>推导二（代数法）：</strong>分 $x\\ge0$ 与 $x<0$ 讨论。$x\\ge0$ 时 $|x|=x<a$；$x<0$ 时 $|x|=-x<a$ 即 $x>-a$。合并得 $-a<x<a$。同理 $|x|>a$ 时 $x\\ge0$ 给 $x>a$，$x<0$ 给 $-x>a$ 即 $x<-a$。")+
  p("<strong>推导三（平移推广）：</strong>对 $|x-a|<b\\ (b>0)$，令 $y=x-a$，则 $|y|<b\\Leftrightarrow-b<y<b$，代回得")+
  fml("|x-a|<b\\ \\Leftrightarrow\\ a-b<x<a+b")+
  p("即数轴上以 $a$ 为中心、半径 $b$ 的开区间。"))+
 exa(p("<strong>例 1：</strong>解 $|2x-1|<3$。由定理 $-3<2x-1<3$，各边加 $1$ 得 $-2<2x<4$，除以 $2$ 得 $-1<x<2$，解集 $(-1,2)$。")+
  p("<strong>例 2：</strong>解 $|x-2|\\ge3$。得 $x-2\\le-3$ 或 $x-2\\ge3$，即 $x\\le-1$ 或 $x\\ge5$，解集 $(-\\infty,-1]\\cup[5,+\\infty)$。")+
  p("<strong>例 3：</strong>解绝对值方程 $|3x+1|=5$，则 $3x+1=5$ 或 $3x+1=-5$，得 $x=\\dfrac{4}{3}$ 或 $x=-2$。"))+
 note(p("右侧为参数 $a$ 时须分类：$a>0$ 按上述公式；$a=0$ 时 $|x|<0$ 无解而 $|x|>0$ 化为 $x\\neq0$；$a<0$ 时 $|x|<a$ 无解而 $|x|>a$ 恒成立（解集为 $\\mathbb{R}$）。"))
)}
]},
{"name":"2.2 整式运算与乘法公式","color":"#8b5cf6","desc":"多项式运算、乘法公式与因式分解",
"items":[
{"id":"e2s2-1","name":"多项式运算与幂的法则","tags":["def","thm","der","exa"],"brief":"单项式与多项式的概念、幂的四条运算法则及其推导。",
"body":wrap(
 defn("多项式",p("<strong>单项式</strong>是数与字母的积（如 $3x^2y$），其中数字因数称为<strong>系数</strong>，所有字母指数之和称为<strong>次数</strong>。<strong>多项式</strong>是有限个单项式的代数和，每个单项式称为<strong>项</strong>，次数最高项的次数称为多项式的次数。多项式相加减就是合并同类项。"))+
 thm("幂的运算法则",p("设 $m,n$ 为正整数，$a\\neq0$：")+
  fml("a^m\\cdot a^n=a^{m+n},\\qquad (a^m)^n=a^{mn},\\qquad (ab)^n=a^n b^n")+
  fml("a^m\\div a^n=a^{m-n}\\ (m>n),\\qquad a^0=1\\ (a\\neq0),\\qquad a^{-n}=\\dfrac{1}{a^n}"))+
 der(p("<strong>推导一（同底数幂相乘）：</strong>把幂写成连乘，$a^m$ 有 $m$ 个因子 $a$，$a^n$ 有 $n$ 个因子 $a$，相乘共 $m+n$ 个因子：")+
  fml("a^m\\cdot a^n=\\underbrace{a\\cdots a}_{m}\\cdot\\underbrace{a\\cdots a}_{n}=\\underbrace{a\\cdots a}_{m+n}=a^{m+n}")+
  p("<strong>推导二（幂的乘方）：</strong>$(a^m)^n$ 表示 $n$ 个 $a^m$ 相乘，每个 $a^m$ 含 $m$ 个因子 $a$，共 $mn$ 个：")+
  fml("(a^m)^n=\\underbrace{a^m\\cdots a^m}_{n}=a^{mn}")+
  p("<strong>推导三（积的乘方）：</strong>由乘法交换律与结合律，把各因子重新配对：")+
  fml("(ab)^n=\\underbrace{(ab)\\cdots(ab)}_{n}=\\underbrace{(a\\cdots a)}_{n}\\underbrace{(b\\cdots b)}_{n}=a^n b^n")+
  p("<strong>推导四（同底数幂相除）：</strong>由除法的意义，$a^m\\div a^n$ 是把分子中 $n$ 个 $a$ 与分母约去：")+
  fml("a^m\\div a^n=\\dfrac{a\\cdots a\\ (m\\text{ 个})}{a\\cdots a\\ (n\\text{ 个})}=a^{m-n}\\ (m>n)"))+
 exa(p("<strong>例（多项式乘法）：</strong>$(2x^2+3x-1)(x+2)$ 逐项相乘后合并同类项：")+
  fml("(2x^2+3x-1)(x+2)=2x^3+4x^2+3x^2+6x-x-2=2x^3+7x^2+5x-2"))
)},
{"id":"e2s2-2","name":"乘法公式（平方差与完全平方）","tags":["thm","der","exa","note"],"brief":"平方差、完全平方、三数完全平方公式的多步展开推导。",
"body":wrap(
 thm("平方差公式",p("")+fml("(a+b)(a-b)=a^2-b^2"))+
 der(p("<strong>推导（逐项展开）：</strong>由分配律把第一个括号逐项乘入第二个括号：")+
  fml("(a+b)(a-b)=a\\cdot a-a\\cdot b+b\\cdot a-b\\cdot b")+
  p("由乘法交换律 $b\\cdot a=ab$，交叉项 $-ab+ab=0$ 抵消，仅剩平方项：")+
  fml("(a+b)(a-b)=a^2-ab+ab-b^2=a^2-b^2"))+
 thm("完全平方公式",p("")+fml("(a+b)^2=a^2+2ab+b^2,\\qquad (a-b)^2=a^2-2ab+b^2"))+
 der(p("<strong>推导一（和的平方）：</strong>把 $(a+b)^2$ 写成 $(a+b)(a+b)$ 再逐项展开：")+
  fml("(a+b)^2=(a+b)(a+b)=a^2+ab+ba+b^2=a^2+2ab+b^2")+
  p("由乘法交换律 $ab=ba$，两个交叉项相同，故为 $2ab$。")+
  p("<strong>推导二（差的平方）：</strong>把 $b$ 换成 $-b$ 代入上式：")+
  fml("(a-b)^2=\\big(a+(-b)\\big)^2=a^2+2a(-b)+(-b)^2=a^2-2ab+b^2")+
  p("这里用到负负得正 $(-b)^2=b^2$。几何理解：边长为 $a+b$ 的正方形由面积 $a^2,b^2$ 的两个正方形与两个面积 $ab$ 的矩形拼成。"))+
 thm("三数完全平方",p("")+fml("(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca"))+
 der(p("<strong>推导（逐项相乘）：</strong>把 $(a+b+c)^2$ 写成两个括号相乘，按第一个括号的每一项分配：")+
  fml("(a+b+c)^2=(a+b+c)(a+b+c)")+
  p("展开共 $3\\times3=9$ 项，按第一个括号的项分组写成：")+
  fml("a^2+ab+ac+ba+b^2+bc+ca+cb+c^2")+
  p("由交换律 $ab=ba,\\ ac=ca,\\ bc=cb$，合并同类项得：")+
  fml("(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca")+
  p("推广：$n$ 个数之和的平方等于各数平方之和加上所有两两乘积的二倍。"))+
 exa(p("<strong>例：</strong>化简 $(x+3)(x-3)+(x+3)^2$。分别用平方差与完全平方：")+
  fml("(x^2-9)+(x^2+6x+9)=2x^2+6x"))+
 note(p("公式逆用即为因式分解：$a^2-b^2=(a+b)(a-b)$，$a^2\\pm2ab+b^2=(a\\pm b)^2$，这是因式分解「公式法」的依据。"))
)},
{"id":"e2s2-3","name":"立方和差公式与因式分解","tags":["thm","der","exa"],"brief":"立方和差公式的展开推导、一般幂差分解与因式分解方法体系。",
"body":wrap(
 thm("立方和与立方差公式",p("")+
  fml("a^3+b^3=(a+b)(a^2-ab+b^2),\\qquad a^3-b^3=(a-b)(a^2+ab+b^2)"))+
 der(p("<strong>推导一（立方和）：</strong>用分配律展开右端：")+
  fml("(a+b)(a^2-ab+b^2)=a^3-a^2b+ab^2+a^2b-ab^2+b^3")+
  p("交叉项 $-a^2b$ 与 $+a^2b$ 抵消、$+ab^2$ 与 $-ab^2$ 抵消，故：")+
  fml("(a+b)(a^2-ab+b^2)=a^3+b^3")+
  p("<strong>推导二（立方差）：</strong>直接展开或把 $b$ 换成 $-b$：")+
  fml("(a-b)(a^2+ab+b^2)=a^3+a^2b+ab^2-a^2b-ab^2-b^3=a^3-b^3")+
  p("<strong>推导三（一般幂差）：</strong>对任意正整数 $n$，用等比求和的配凑可证：")+
  fml("a^n-b^n=(a-b)(a^{n-1}+a^{n-2}b+\\cdots+ab^{n-2}+b^{n-1})")+
  p("验证方式是把右端展开，中间各项逐对抵消，只剩 $a^n-b^n$。当 $n$ 为奇数时把 $b$ 换成 $-b$，得 $a^n+b^n=(a+b)(a^{n-1}-a^{n-2}b+\\cdots+b^{n-1})$。立方和差公式即 $n=3$ 的特例。"))+
 defn("因式分解方法",p("把多项式写成几个整式乘积的形式叫<strong>因式分解</strong>。常用方法：① <strong>提公因式法</strong> $ma+mb+mc=m(a+b+c)$；② <strong>公式法</strong> 逆用乘法公式；③ <strong>十字相乘法</strong> $x^2+(p+q)x+pq=(x+p)(x+q)$；④ <strong>分组分解法</strong> 适当分组后各组提取公因式再整体提取。分解须进行到每个因式在指定数域内都不能再分为止。"))+
 exa(p("<strong>例：</strong>分解 $x^3-3x^2+4$。用试根法找有理根：代入 $x=-1$ 得 $-1-3+4=0$，故含因式 $x+1$。作多项式除法：")+
  fml("x^3-3x^2+4=(x+1)(x^2-4x+4)=(x+1)(x-2)^2")+
  p("其中 $x^2-4x+4$ 恰为完全平方 $(x-2)^2$，故分解完成。"))
)},
{"id":"e2s2-4","name":"十字相乘法与分组分解","tags":["def","thm","der","exa"],"brief":"二次三项式十字相乘的原理与分组分解的配凑技巧。",
"body":wrap(
 defn("十字相乘法",p("对首项系数为 $1$ 的二次三项式 $x^2+px+q$，若能找到两数 $m,n$ 使 $m+n=p$ 且 $mn=q$，则 $x^2+px+q=(x+m)(x+n)$。对一般二次三项式 $ax^2+bx+c\\ (a\\neq0)$，把二次项系数拆为 $a_1a_2$、常数项拆为 $c_1c_2$，使交叉相乘之和满足 $a_1c_2+a_2c_1=b$，则 $ax^2+bx+c=(a_1x+c_1)(a_2x+c_2)$。"))+
 thm("十字相乘原理",p("")+
  fml("(a_1x+c_1)(a_2x+c_2)=a_1a_2x^2+(a_1c_2+a_2c_1)x+c_1c_2"))+
 der(p("<strong>推导一（首一情形）：</strong>直接展开验证：")+
  fml("(x+m)(x+n)=x^2+(m+n)x+mn")+
  p("故只要 $m+n=p$ 且 $mn=q$，就有 $x^2+px+q=(x+m)(x+n)$——即把一次项系数拆成两数之和、常数项拆成同一对数的积。")+
  p("<strong>推导二（一般情形）：</strong>把一次项拆成两项，再用分组分解验证：")+
  fml("a_1a_2x^2+a_1c_2x+a_2c_1x+c_1c_2=a_1x(a_2x+c_2)+c_1(a_2x+c_2)=(a_1x+c_1)(a_2x+c_2)")+
  p("这正是「十字相乘」中交叉相乘之和等于一次项系数 $b$ 的来历。")+
  p("<strong>推导三（分组分解）：</strong>四项式 $ax+ay+bx+by$ 前两项一组、后两项一组，各自提取公因式后再整体提取：")+
  fml("ax+ay+bx+by=a(x+y)+b(x+y)=(a+b)(x+y)"))+
 exa(p("<strong>例 1：</strong>分解 $x^2-5x+6$。找两数之和为 $-5$、之积为 $6$，取 $-2,-3$，故 $x^2-5x+6=(x-2)(x-3)$。")+
  p("<strong>例 2：</strong>分解 $6x^2+11x+4$。把 $6$ 拆为 $2\\times3$、$4$ 拆为 $1\\times4$，交叉和 $2\\times4+3\\times1=11$，故 $6x^2+11x+4=(2x+1)(3x+4)$。")+
  p("<strong>例 3：</strong>分解 $x^3+x^2-4x-4$。分组为 $(x^3+x^2)-(4x+4)=x^2(x+1)-4(x+1)=(x+1)(x^2-4)=(x+1)(x-2)(x+2)$。"))
)}
]},
{"name":"2.3 方程","color":"#6d28d9","desc":"一元一次、二元一次组、一元二次、高次方程",
"items":[
{"id":"e2s3-1","name":"一元一次与二元一次方程组","tags":["def","der","exa"],"brief":"一元一次方程的解法、代入消元与加减消元推导及解的判定。",
"body":wrap(
 defn("一元一次方程",p("形如 $ax+b=0\\ (a\\neq0)$ 的方程叫<strong>一元一次方程</strong>，去分母、去括号、移项、合并同类项后系数化为 $1$ 即得解：")+
  fml("ax+b=0\\ (a\\neq0)\\ \\Longrightarrow\\ x=-\\dfrac{b}{a}"))+
 defn("二元一次方程组",p("形如 $\\begin{cases}a_1x+b_1y=c_1\\\\ a_2x+b_2y=c_2\\end{cases}$ 的方程组称为二元一次方程组，核心思想是<strong>消元</strong>——减少未知数个数，化为已会解的一元一次方程，常用代入消元与加减消元。"))+
 der(p("<strong>推导一（代入消元）：</strong>当 $b_1\\neq0$ 时，由第一式解出 $y$：")+
  fml("y=\\dfrac{c_1-a_1x}{b_1}")+
  p("代入第二式消去 $y$，得仅含 $x$ 的一元一次方程：")+
  fml("a_2x+b_2\\cdot\\dfrac{c_1-a_1x}{b_1}=c_2")+
  p("两边乘 $b_1$ 整理得 $(a_2b_1-a_1b_2)x=c_2b_1-c_1b_2$，于是")+
  fml("x=\\dfrac{c_2b_1-c_1b_2}{a_2b_1-a_1b_2}=\\dfrac{b_1c_2-b_2c_1}{a_1b_2-a_2b_1}")+
  p("再回代第一式即得 $y$。")+
  p("<strong>推导二（加减消元）：</strong>用 $b_2$ 乘第一式、$b_1$ 乘第二式：")+
  fml("\\begin{cases}a_1b_2x+b_1b_2y=c_1b_2\\\\ a_2b_1x+b_1b_2y=c_2b_1\\end{cases}")+
  p("两式相减消去 $y$：")+
  fml("(a_1b_2-a_2b_1)x=c_1b_2-c_2b_1")+
  p("其结果与代入法完全一致。记系数行列式 $D=a_1b_2-a_2b_1$。")+
  p("<strong>推导三（解的判定）：</strong>当 $D\\neq0$ 时 $x=\\dfrac{c_1b_2-c_2b_1}{D}$ 唯一确定，方程组有唯一解；当 $D=0$ 时两直线平行或重合——若 $c_1b_2-c_2b_1=0$ 则重合，有无穷多组解，否则平行无解。"))+
 exa(p("<strong>例：</strong>解 $\\begin{cases}x+y=5\\\\ 2x-y=4\\end{cases}$。两式相加消去 $y$ 得 $3x=9$，$x=3$；代入第一式得 $y=2$。故解为 $\\begin{cases}x=3\\\\ y=2\\end{cases}$。"))
)},
{"id":"e2s3-2","name":"一元二次方程","tags":["thm","der","exa","app"],"brief":"配方法推导求根公式、判别式与韦达定理的两种证明。",
"fig":"quadratic","figCap":"二次函数 y=ax²+bx+c 的抛物线，顶点与 x 轴交点决定根的分布",
"body":wrap(
 thm("求根公式",p("一元二次方程 $ax^2+bx+c=0\\ (a\\neq0)$ 的根为")+
  fml("x=\\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}"))+
 der(p("<strong>配方法推导（共四步）：</strong>")+
  p("<strong>第一步（化二次项系数为 $1$）：</strong>两边同除以 $a\\neq0$：")+
  fml("x^2+\\dfrac{b}{a}x+\\dfrac{c}{a}=0\\ \\Longrightarrow\\ x^2+\\dfrac{b}{a}x=-\\dfrac{c}{a}")+
  p("<strong>第二步（配方）：</strong>两边加上一次项系数一半的平方 $\\left(\\dfrac{b}{2a}\\right)^2$，左端凑成完全平方：")+
  fml("x^2+\\dfrac{b}{a}x+\\left(\\dfrac{b}{2a}\\right)^2=\\left(\\dfrac{b}{2a}\\right)^2-\\dfrac{c}{a}")+
  p("即")+
  fml("\\left(x+\\dfrac{b}{2a}\\right)^2=\\dfrac{b^2-4ac}{4a^2}")+
  p("<strong>第三步（开方）：</strong>右端分母 $4a^2>0$，当 $b^2-4ac\\ge0$ 时两边开方：")+
  fml("x+\\dfrac{b}{2a}=\\pm\\dfrac{\\sqrt{b^2-4ac}}{2a}")+
  p("<strong>第四步（移项）：</strong>")+
  fml("x=\\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}"))+
 thm("判别式",p("记 $\\Delta=b^2-4ac$，它由配方第二步右端的符号决定根的情况：")+
  fml("\\Delta>0\\ \\text{两不等实根};\\quad \\Delta=0\\ \\text{两相等实根};\\quad \\Delta<0\\ \\text{无实根}"))+
 thm("韦达定理",p("设 $x_1,x_2$ 是 $ax^2+bx+c=0\\ (a\\neq0)$ 的两根，则")+
  fml("x_1+x_2=-\\dfrac{b}{a},\\qquad x_1x_2=\\dfrac{c}{a}"))+
 der(p("<strong>推导一（由求根公式）：</strong>记 $\\Delta=b^2-4ac$，$x_{1,2}=\\dfrac{-b\\pm\\sqrt{\\Delta}}{2a}$。两根之和：")+
  fml("x_1+x_2=\\dfrac{-b+\\sqrt{\\Delta}}{2a}+\\dfrac{-b-\\sqrt{\\Delta}}{2a}=\\dfrac{-2b}{2a}=-\\dfrac{b}{a}")+
  p("根号项 $+\\sqrt{\\Delta}$ 与 $-\\sqrt{\\Delta}$ 相消。两根之积用平方差公式：")+
  fml("x_1x_2=\\dfrac{(-b+\\sqrt{\\Delta})(-b-\\sqrt{\\Delta})}{4a^2}=\\dfrac{b^2-\\Delta}{4a^2}=\\dfrac{b^2-(b^2-4ac)}{4a^2}=\\dfrac{c}{a}")+
  p("<strong>推导二（由因式分解）：</strong>因 $x_1,x_2$ 为根，方程可写成 $a(x-x_1)(x-x_2)=0$，展开并比较系数：")+
  fml("a(x-x_1)(x-x_2)=ax^2-a(x_1+x_2)x+ax_1x_2=ax^2+bx+c")+
  p("对应得 $-a(x_1+x_2)=b$、$ax_1x_2=c$，即 $x_1+x_2=-\\dfrac{b}{a}$、$x_1x_2=\\dfrac{c}{a}$。两法结论一致。"))+
 exa(p("<strong>例：</strong>解 $x^2-5x+6=0$。$\\Delta=25-24=1>0$，$x=\\dfrac{5\\pm1}{2}$，即 $x_1=3,\\ x_2=2$。验算：$x_1+x_2=5=-\\dfrac{-5}{1}$，$x_1x_2=6=\\dfrac{6}{1}$，符合韦达定理。"))+
 app(p("<strong>应用：</strong>已知一根求另一根；不解方程求对称式 $x_1^2+x_2^2=(x_1+x_2)^2-2x_1x_2$；构造以给定两数为根的方程 $x^2-(x_1+x_2)x+x_1x_2=0$，均以韦达定理为工具。"))
)},
{"id":"e2s3-3","name":"高次方程与有理根定理","tags":["thm","der","exa","note"],"brief":"有理根定理的整除证明、因式定理与综合除法降次。",
"body":wrap(
 thm("有理根定理",p("设整系数多项式 $f(x)=a_nx^n+a_{n-1}x^{n-1}+\\cdots+a_1x+a_0\\ (a_0\\neq0,\\ a_n\\neq0)$。若既约分数 $\\dfrac{p}{q}$（$\\gcd(p,q)=1$）是 $f(x)=0$ 的根，则分子整除常数项、分母整除首项系数：")+
  fml("p\\mid a_0,\\qquad q\\mid a_n"))+
 der(p("<strong>推导（逐步整除）：</strong>把 $x=\\dfrac{p}{q}$ 代入 $f(x)=0$，两边同乘 $q^n$ 消去分母：")+
  fml("a_np^n+a_{n-1}p^{n-1}q+\\cdots+a_1pq^{n-1}+a_0q^n=0")+
  p("<strong>第一步（证 $p\\mid a_0$）：</strong>把含因子 $p$ 的项移到一边：")+
  fml("a_0q^n=-p\\big(a_np^{n-1}+a_{n-1}p^{n-2}q+\\cdots+a_1q^{n-1}\\big)")+
  p("故 $p\\mid a_0q^n$。又因 $\\gcd(p,q)=1$，$p$ 与 $q^n$ 互质，故必有 $p\\mid a_0$。")+
  p("<strong>第二步（证 $q\\mid a_n$）：</strong>把含因子 $q$ 的项移到另一边：")+
  fml("a_np^n=-q\\big(a_{n-1}p^{n-1}+\\cdots+a_1pq^{n-2}+a_0q^{n-1}\\big)")+
  p("故 $q\\mid a_np^n$，再由 $\\gcd(p,q)=1$ 得 $q\\mid a_n$。证明完成。"))+
 thm("因式定理与综合除法",p("$x=r$ 是 $f(x)=0$ 的根当且仅当 $(x-r)$ 是 $f(x)$ 的因式，即 $f(x)=(x-r)Q(x)$，其中 $\\deg Q=\\deg f-1$，从而把方程<strong>降次</strong>。"))+
 der(p("<strong>推导（带余除法）：</strong>用 $(x-r)$ 作带余除法，商为 $Q(x)$、余式为常数 $R$：")+
  fml("f(x)=(x-r)Q(x)+R")+
  p("把 $x=r$ 代入，第一项为零：")+
  fml("f(r)=(r-r)Q(r)+R=R")+
  p("即余数恰等于 $f(r)$（余数定理）。当且仅当 $f(r)=0$ 时 $R=0$，此时 $f(x)=(x-r)Q(x)$，原方程化为 $Q(x)=0$。如此逐次降次，直到化为一元一次或二次方程求解。"))+
 exa(p("<strong>例：</strong>解 $x^3-6x^2+11x-6=0$。可能的有理根由 $p\\mid6,\\ q\\mid1$ 得 $\\pm1,\\pm2,\\pm3,\\pm6$。试 $x=1$：$1-6+11-6=0$，故 $x=1$ 是根。综合除法得：")+
  fml("x^3-6x^2+11x-6=(x-1)(x^2-5x+6)=(x-1)(x-2)(x-3)")+
  p("故方程的根为 $x=1,2,3$。"))+
 note(p("有理根定理只给出<strong>可能存在</strong>的候选根，须逐一验证。对没有有理根的高次方程（如 $x^3-2=0$，候选根 $\\pm1,\\pm2$ 均不满足），须借助数值方法或三次求根公式。"))
)}
]},
{"name":"2.4 不等式","color":"#5b21b6","desc":"基本性质、一元一次/二次、分式绝对值、均值不等式与放缩",
"items":[
{"id":"e2s4-1","name":"不等式基本性质与一元一次不等式","tags":["def","thm","der","exa"],"brief":"不等式八条性质及乘负数变号、同向相加、正数相乘的推导。",
"body":wrap(
 defn("不等式基本性质",p("对实数 $a,b,c,d$：")+
  p("① 对称性：$a>b\\Leftrightarrow b<a$；")+
  p("② 传递性：$a>b,\\ b>c\\Rightarrow a>c$；")+
  p("③ 可加性：$a>b\\Rightarrow a+c>b+c$；")+
  p("④ 可乘正数：$a>b,\\ c>0\\Rightarrow ac>bc$；可乘负数：$a>b,\\ c<0\\Rightarrow ac<bc$（<strong>不等号变向</strong>）；")+
  p("⑤ 同向相加：$a>b,\\ c>d\\Rightarrow a+c>b+d$；")+
  p("⑥ 正数同向相乘：$a>b>0,\\ c>d>0\\Rightarrow ac>bd$；")+
  p("⑦ 正数乘方：$a>b>0\\Rightarrow a^n>b^n\\ (n\\in\\mathbb{N}^*)$；")+
  p("⑧ 正数开方：$a>b>0\\Rightarrow \\sqrt[n]{a}>\\sqrt[n]{b}$。"))+
 der(p("<strong>推导一（可加性）：</strong>不等式 $a>b$ 等价于 $a-b>0$。于是")+
  fml("(a+c)-(b+c)=a-b>0")+
  p("即 $a+c>b+c$——加同一个数不改变两者之差。")+
  p("<strong>推导二（乘负数变号）：</strong>设 $a>b$，则 $a-b>0$。两边同乘 $c$：")+
  fml("(a-b)c\\ \\begin{cases}>0,&c>0\\\\ =0,&c=0\\\\ <0,&c<0\\end{cases}")+
  p("当 $c<0$ 时 $ac-bc<0$，即 $ac<bc$，不等号方向反转。这就是「同乘负数，不等号变向」的根源。")+
  p("<strong>推导三（同向相加）：</strong>由 $a>b$ 与 $c>d$ 得 $a-b>0$、$c-d>0$，两者相加：")+
  fml("(a+c)-(b+d)=(a-b)+(c-d)>0\\ \\Longrightarrow\\ a+c>b+d")+
  p("<strong>推导四（正数同向相乘）：</strong>因 $a>b$ 且 $c>0$，由性质④得 $ac>bc$；又因 $c>d$ 且 $b>0$，得 $bc>bd$。再由传递性得 $ac>bd$。"))+
 exa(p("<strong>例：</strong>解 $2x-3<x+2$。移项得 $x<5$，解集 $(-\\infty,5)$。若不等式为 $-2x<6$，则两边除以 $-2$ 时须变号，得 $x>-3$，解集 $(-3,+\\infty)$。"))+
 app(p("<strong>应用：</strong>利用不等式性质可给代数式定界（如已知 $1<x<3$ 与 $2<y<5$，则 $3<x+y<8$、$2<xy<15$），这是估计与放缩的第一步。"))
)},
{"id":"e2s4-2","name":"一元二次不等式与分式不等式","tags":["thm","der","exa","note"],"brief":"图像法与因式分解法解二次不等式、分式不等式的等价转化。",
"fig":"inequality","figCap":"二次函数图像法：y>0 对应 x 轴上方区间，y<0 对应下方区间",
"body":wrap(
 thm("一元二次不等式",p("设 $y=ax^2+bx+c\\ (a>0)$，$\\Delta=b^2-4ac$。当 $\\Delta>0$ 时有两根 $x_1<x_2$：")+
  fml("ax^2+bx+c>0\\ \\Leftrightarrow\\ x<x_1\\ \\text{或}\\ x>x_2")+
  fml("ax^2+bx+c<0\\ \\Leftrightarrow\\ x_1<x<x_2")+
  p("当 $\\Delta=0$ 时 $ax^2+bx+c\\ge0$ 恒成立（仅 $x=-\\frac{b}{2a}$ 处取等）；当 $\\Delta<0$ 时 $ax^2+bx+c>0$ 恒成立。"))+
 der(p("<strong>推导一（图像法）：</strong>$a>0$ 时抛物线开口向上。$\\Delta>0$ 时图像与 $x$ 轴交于 $x_1,x_2$，两根之间图像在 $x$ 轴下方（$y<0$），两根之外在 $x$ 轴上方（$y>0$），故得上述解集。")+
  p("<strong>推导二（因式分解法）：</strong>$\\Delta>0$ 时 $ax^2+bx+c=a(x-x_1)(x-x_2)$。由于 $a>0$，符号只由 $(x-x_1)(x-x_2)$ 决定：两因式同号（$x<x_1$ 或 $x>x_2$）积为正，异号（$x_1<x<x_2$）积为负。这与图像法一致，且不依赖画图。")+
  p("<strong>推导三（分式不等式）：</strong>关键是「同号相乘为正」。由 $\\dfrac{f}{g}=g^{-2}\\cdot fg$ 且 $g^{-2}>0$，$\\dfrac{f}{g}$ 与 $fg$ 同号，故")+
  fml("\\dfrac{f(x)}{g(x)}>0\\ \\Leftrightarrow\\ f(x)g(x)>0\\quad(g(x)\\neq0)")+
  p("含等号时须剔除分母零点：")+
  fml("\\dfrac{f(x)}{g(x)}\\ge0\\ \\Leftrightarrow\\ f(x)g(x)\\ge0\\ \\text{且}\\ g(x)\\neq0"))+
 exa(p("<strong>例 1：</strong>解 $x^2-5x+6>0$。$\\Delta=1>0$，根 $x_1=2,x_2=3$，开口向上，解集 $(-\\infty,2)\\cup(3,+\\infty)$。")+
  p("<strong>例 2：</strong>解 $\\dfrac{x-1}{x+2}\\le0$。等价于 $(x-1)(x+2)\\le0$ 且 $x\\neq-2$，得 $-2<x\\le1$，解集 $(-2,1]$。"))+
 note(p("恒成立问题：$ax^2+bx+c>0$ 对一切 $x$ 成立 $\\Leftrightarrow a>0$ 且 $\\Delta<0$；$ax^2+bx+c<0$ 对一切 $x$ 成立 $\\Leftrightarrow a<0$ 且 $\\Delta<0$。这是「分离参数求最值」的重要依据。"))
)},
{"id":"e2s4-3","name":"均值不等式链与常见放缩","tags":["thm","der","exa","app"],"brief":"调和≤几何≤算术≤平方均值链的逐步证明与常用放缩。",
"body":wrap(
 thm("均值不等式链",p("对 $a,b>0$，四种平均数满足")+
  fml("\\dfrac{2}{\\dfrac{1}{a}+\\dfrac{1}{b}}\\ \\le\\ \\sqrt{ab}\\ \\le\\ \\dfrac{a+b}{2}\\ \\le\\ \\sqrt{\\dfrac{a^2+b^2}{2}}")+
  p("依次称为调和平均 $H$、几何平均 $G$、算术平均 $A$、平方平均 $Q$。"))+
 der(p("<strong>推导一（算术 ≥ 几何）：</strong>由完全平方非负：")+
  fml("(\\sqrt{a}-\\sqrt{b})^2\\ge0\\ \\Longrightarrow\\ a+b-2\\sqrt{ab}\\ge0\\ \\Longrightarrow\\ \\dfrac{a+b}{2}\\ge\\sqrt{ab}")+
  p("等号当且仅当 $\\sqrt{a}=\\sqrt{b}$，即 $a=b$。")+
  p("<strong>推导二（几何 ≥ 调和）：</strong>把上式中的 $a,b$ 换成 $\\dfrac{1}{a},\\dfrac{1}{b}$：")+
  fml("\\dfrac{\\dfrac{1}{a}+\\dfrac{1}{b}}{2}\\ge\\sqrt{\\dfrac{1}{ab}}=\\dfrac{1}{\\sqrt{ab}}")+
  p("两边取倒数（正数同取倒数，不等号反向）：")+
  fml("\\sqrt{ab}\\ \\ge\\ \\dfrac{2}{\\dfrac{1}{a}+\\dfrac{1}{b}}")+
  p("<strong>推导三（平方 ≥ 算术）：</strong>由 $a^2+b^2\\ge2ab$，两边同加 $a^2+b^2$：")+
  fml("2(a^2+b^2)\\ge(a+b)^2\\ \\Longrightarrow\\ \\dfrac{a^2+b^2}{2}\\ge\\left(\\dfrac{a+b}{2}\\right)^2")+
  p("两边开方（均非负）得 $\\sqrt{\\dfrac{a^2+b^2}{2}}\\ge\\dfrac{a+b}{2}$，等号同样当 $a=b$。三式合并即得均值不等式链。"))+
 thm("常见放缩公式",p("")+
  fml("\\dfrac{1}{n^2}<\\dfrac{1}{n(n-1)}=\\dfrac{1}{n-1}-\\dfrac{1}{n}\\quad(n\\ge2)")+
  fml("\\sqrt{n+1}-\\sqrt{n}=\\dfrac{1}{\\sqrt{n+1}+\\sqrt{n}}<\\dfrac{1}{2\\sqrt{n}}")+
  fml("\\ln(1+x)<x\\ (x>0),\\qquad e^x\\ge1+x\\ (x\\in\\mathbb{R}),\\qquad \\sin x<x\\ (x>0)"))+
 der(p("<strong>放缩推导一（裂项）：</strong>因 $n>0$ 时 $n^2>n(n-1)$，故 $\\dfrac{1}{n^2}<\\dfrac{1}{n(n-1)}$；又")+
  fml("\\dfrac{1}{n(n-1)}=\\dfrac{n-(n-1)}{n(n-1)}=\\dfrac{1}{n-1}-\\dfrac{1}{n}")+
  p("于是 $\\sum_{n=2}^{N}\\dfrac{1}{n^2}<\\sum_{n=2}^{N}\\left(\\dfrac{1}{n-1}-\\dfrac{1}{n}\\right)=1-\\dfrac{1}{N}<1$，可证 $\\sum\\dfrac{1}{n^2}$ 有界。")+
  p("<strong>放缩推导二（分子有理化）：</strong>")+
  fml("\\sqrt{n+1}-\\sqrt{n}=\\dfrac{(n+1)-n}{\\sqrt{n+1}+\\sqrt{n}}=\\dfrac{1}{\\sqrt{n+1}+\\sqrt{n}}")+
  p("由 $\\sqrt{n+1}>\\sqrt{n}$ 得分母大于 $2\\sqrt{n}$，故原式小于 $\\dfrac{1}{2\\sqrt{n}}$。")+
  p("<strong>放缩推导三（对数与指数）：</strong>令 $f(x)=x-\\ln(1+x)\\ (x\\ge0)$，则 $f(0)=0$ 且")+
  fml("f'(x)=1-\\dfrac{1}{1+x}=\\dfrac{x}{1+x}>0\\quad(x>0)")+
  p("故 $f$ 在 $[0,+\\infty)$ 单调递增，$f(x)>0$，即 $\\ln(1+x)<x$。对 $e^x\\ge1+x$，令 $g(x)=e^x-1-x$，由 $g'(x)=e^x-1$ 知 $g$ 在 $x=0$ 处取最小值 $g(0)=0$，故 $g(x)\\ge0$；也可由展开式 $e^x=1+x+\\dfrac{x^2}{2}+\\cdots\\ge1+x$ 看出。"))+
 exa(p("<strong>例：</strong>求 $y=x+\\dfrac{4}{x}\\ (x>0)$ 的最小值。由算术 ≥ 几何：")+
  fml("x+\\dfrac{4}{x}\\ \\ge\\ 2\\sqrt{x\\cdot\\dfrac{4}{x}}=2\\sqrt{4}=4")+
  p("等号当 $x=\\dfrac{4}{x}$ 即 $x=2$ 时取到，故最小值为 $4$。"))+
 app(p("<strong>应用与技巧：</strong>使用均值不等式须满足「一正、二定、三相等」；当和或积不是定值时，常用拆项配凑（如 $x+\\dfrac{1}{x-2}=(x-2)+\\dfrac{1}{x-2}+2$）把它化为定值，再用等号条件检验取等点。"))
)},
{"id":"e2s4-4","name":"含绝对值的不等式与恒成立","tags":["thm","der","exa","note"],"brief":"单绝对值与多绝对值不等式、三角不等式定界及恒成立问题。",
"body":wrap(
 thm("含绝对值不等式的等价转化",p("当 $g(x)>0$ 时")+
  fml("|f(x)|<g(x)\\ \\Leftrightarrow\\ -g(x)<f(x)<g(x)")+
  fml("|f(x)|>g(x)\\ \\Leftrightarrow\\ f(x)<-g(x)\\ \\text{或}\\ f(x)>g(x)"))+
 der(p("<strong>推导一（直接转化）：</strong>由 $|t|<g\\Leftrightarrow-g<t<g$（$g>0$）取 $t=f(x)$ 即得第一式；由 $|t|>g\\Leftrightarrow t<-g$ 或 $t>g$ 即得第二式。若 $g(x)\\le0$，则 $|f|<g$ 无解、$|f|>g$ 恒成立。")+
  p("<strong>推导二（多绝对值定界）：</strong>由三角不等式 $|u|+|v|\\ge|u+v|$ 与 $|u+v|\\ge\\big||u|-|v|\\big|$，可得")+
  fml("|x-a|+|x-b|\\ \\ge\\ \\big|(x-a)-(x-b)\\big|=|a-b|")+
  p("故 $|x-a|+|x-b|$ 的最小值为 $|a-b|$，当 $x$ 位于 $a,b$ 之间时取到。据此可用「零点分段法」把含多个绝对值的不等式拆成若干区间分别求解。"))+
 exa(p("<strong>例：</strong>解 $|x-1|+|x-3|\\le4$。以 $1,3$ 为分点讨论。")+
  p("当 $x<1$：$1-x+3-x=4-2x\\le4\\Rightarrow x\\ge0$，得 $0\\le x<1$；当 $1\\le x\\le3$：$x-1+3-x=2\\le4$ 恒成立；当 $x>3$：$x-1+x-3=2x-4\\le4\\Rightarrow x\\le4$，得 $3<x\\le4$。合并三区间得解集 $[0,4]$。"))+
 note(p("恒成立问题常用分离参数法：$m\\ge f(x)$ 恒成立 $\\Leftrightarrow m\\ge f(x)_{\\max}$；$m\\le f(x)$ 恒成立 $\\Leftrightarrow m\\le f(x)_{\\min}$，再借助均值不等式或二次函数求最值。"))
)}
]}
]
# ============ 第三章 函数 ============
# ============ 第三章 函数 ============
ch3_sections = [
{"name":"3.1 函数概念与性质","color":"#0d9488","desc":"函数定义、三要素、单调性奇偶性周期性",
"items":[
{"id":"e3s1-1","name":"函数的定义与三要素","tags":["def","der","exa"],"brief":"映射定义的函数、定义域值域对应关系三要素及其判定。",
"fig":"func_mapping","figCap":"函数 $f:A\\to B$ 的映射示意，定义域到值域的对应",
"body":wrap(
 defn("函数",p("设 $A,B$ 是非空数集，若对 $A$ 中<strong>任意</strong>一个 $x$，按对应法则 $f$，在 $B$ 中都有<strong>唯一确定</strong>的 $y$ 与之对应，则称 $f$ 为从 $A$ 到 $B$ 的<strong>函数</strong>，记作 $y=f(x),\\ x\\in A$。其中 $x$ 为自变量，$A$ 为定义域，集合 $\\{f(x)\\mid x\\in A\\}\\subseteq B$ 为值域。定义的关键在于「任意」与「唯一」：允许「多对一」，不允许「一对多」。"))+
 defn("三要素",p("函数由<strong>定义域</strong> $A$、<strong>值域</strong> $\\{f(x)\\mid x\\in A\\}$ 与<strong>对应法则</strong> $f$ 三要素确定。两函数相等当且仅当<strong>定义域相同</strong>且<strong>对应法则相同</strong>，值域随之确定。"))+
 der(p("<strong>同一函数的判定：</strong>只需比较定义域与对应法则。例如 $f(x)=x$ 与 $g(x)=\\dfrac{x^2}{x}$，虽然化简后都写成 $x$，但 $f$ 的定义域为 $\\mathbb{R}$，而 $g$ 的定义域为 $\\{x\\mid x\\ne0\\}$，二者<strong>不是</strong>同一函数。")+
 p("<strong>定义域求法的逐条来源：</strong>分母不为零、偶次根号下非负、对数真数为正且底数合法、正切终边不与 $y$ 轴重合，可归纳为")+
 fml("\\dfrac{u}{v}\\Rightarrow v\\ne0;\\qquad \\sqrt[2n]{u}\\Rightarrow u\\ge0;\\qquad \\log_a u\\Rightarrow u>0,\\ a>0,\\ a\\ne1")+
 fml("y=\\tan x\\Rightarrow x\\ne\\dfrac{\\pi}{2}+k\\pi;\\qquad y=\\cot x\\Rightarrow x\\ne k\\pi\\quad(k\\in\\mathbb{Z})")+
 p("<strong>综合示例推导：</strong>求 $y=\\dfrac{\\sqrt{x-1}}{\\lg(x+2)}$ 的定义域，需使三个限制同时成立：")+
 fml("x-1\\ge0\\Rightarrow x\\ge1;\\quad x+2>0\\Rightarrow x>-2;\\quad \\lg(x+2)\\ne0\\Rightarrow x+2\\ne1\\Rightarrow x\\ne-1")+
 p("三者取交集，注意 $x\\ge1$ 已自动满足 $x>-2$，且 $x\\ne-1$ 不影响，故定义域为 $[1,+\\infty)$。"))+
 exa(p("<strong>例：</strong>求 $y=\\dfrac{1}{\\sqrt{x-1}}+\\lg(3-x)$ 的定义域。由 $x-1>0$ 得 $x>1$；由 $3-x>0$ 得 $x<3$；取交集得定义域 $(1,3)$。"))+
 note(p("对应法则不因自变量字母而改变，$y=f(x)$ 与 $y=f(t)$ 是同一法则。分段函数是用不同表达式在各自区间上定义的一个函数，仍满足「任意一个 $x$ 对应唯一一个 $y$」。"))
)
},
{"id":"e3s1-2","name":"单调性、奇偶性与周期性","tags":["def","thm","der","exa"],"brief":"单调性、奇偶性、周期性的定义、判定与证明。",
"body":wrap(
 defn("单调性",p("设 $f$ 的定义域为 $D$。若 $\\forall x_1<x_2\\in D$ 都有 $f(x_1)<f(x_2)$，则称 $f$ 在 $D$ 上<strong>严格递增</strong>；若有 $f(x_1)>f(x_2)$，则称<strong>严格递减</strong>。区间 $D$ 称为单调区间。"))+
 defn("奇偶性",p("设定义域 $D$ 关于原点对称。若 $\\forall x\\in D$ 有 $f(-x)=-f(x)$，则 $f$ 为<strong>奇函数</strong>，图像关于原点对称；若 $f(-x)=f(x)$，则 $f$ 为<strong>偶函数</strong>，图像关于 $y$ 轴对称。定义域不对称的函数既非奇也非偶。"))+
 defn("周期性",p("若存在非零常数 $T$，使 $\\forall x\\in D$ 都有 $f(x+T)=f(x)$，则称 $f$ 为<strong>周期函数</strong>，$T$ 为其周期；最小的正周期称为<strong>最小正周期</strong>。"))+
 thm("复合与运算性质",p("单调性遵循「同增异减」：增复合增为增，减复合减为增，增减复合为减。奇偶性：奇$\\pm$奇为奇，偶$\\pm$偶为偶，奇$\\times$奇为偶，偶$\\times$偶为偶，奇$\\times$偶为奇。"))+
 der(p("<strong>定义法证单调性（作差）：</strong>证明 $f(x)=x+\\dfrac{1}{x}$ 在 $(0,1]$ 上递减。任取 $0<x_1<x_2\\le1$，作差并通分：")+
 fml("f(x_2)-f(x_1)=(x_2-x_1)+\\left(\\dfrac{1}{x_2}-\\dfrac{1}{x_1}\\right)=(x_2-x_1)-\\dfrac{x_2-x_1}{x_1x_2}=(x_2-x_1)\\left(1-\\dfrac{1}{x_1x_2}\\right)")+
 p("因 $0<x_1<x_2\\le1$，故 $x_1x_2<1$，从而 $1-\\dfrac{1}{x_1x_2}<0$；又 $x_2-x_1>0$，故乘积为负，即 $f(x_2)-f(x_1)<0$，$f(x_2)<f(x_1)$，所以 $f$ 在 $(0,1]$ 上递减。")+
 p("<strong>奇偶性判定：</strong>先验证定义域是否关于原点对称，再计算 $f(-x)$ 并与 $f(x)$ 比较。取 $f(x)=\\lg\\dfrac{1-x}{1+x}$，其定义域由 $\\dfrac{1-x}{1+x}>0$ 解得 $-1<x<1$，关于原点对称；且")+
 fml("f(-x)=\\lg\\dfrac{1+x}{1-x}=\\lg\\left(\\dfrac{1-x}{1+x}\\right)^{-1}=-\\lg\\dfrac{1-x}{1+x}=-f(x)")+
 p("故 $f$ 为奇函数。")+
 p("<strong>周期推导：</strong>若已知 $f(x+a)=-f(x)\\ (a\\ne0)$，把自变量换成 $x+a$ 得 $f(x+2a)=-f(x+a)$；代入前式得 $f(x+2a)=-\\big(-f(x)\\big)=f(x)$，故 $2a$ 为周期。同理若 $f(x+a)=\\dfrac{1}{f(x)}$，则 $f(x+2a)=\\dfrac{1}{f(x+a)}=f(x)$，周期也是 $2a$。"))+
 exa(p("<strong>例：</strong>判断 $f(x)=x^3+x$ 的奇偶性与单调性。定义域 $\\mathbb{R}$ 关于原点对称，$f(-x)=(-x)^3+(-x)=-(x^3+x)=-f(x)$，为奇函数；又对任意 $x_1<x_2$ 有 $f(x_2)-f(x_1)=(x_2^3-x_1^3)+(x_2-x_1)>0$，故在 $\\mathbb{R}$ 上递增。"))+
 note(p("奇函数若在 $x=0$ 处有定义，必有 $f(0)=0$。偶函数在关于原点对称的两个区间上单调性相反，奇函数则相同。"))
)
},
{"id":"e3s1-3","name":"反函数与复合函数","tags":["def","der","exa"],"brief":"反函数存在条件与求法、复合函数定义与定义域。",
"body":wrap(
 defn("反函数",p("若函数 $y=f(x)$ 在定义域 $D$ 上严格单调，则存在<strong>反函数</strong> $y=f^{-1}(x)$：其定义域为 $f$ 的值域，值域为 $D$，且满足 $f^{-1}(f(x))=x,\\ f(f^{-1}(x))=x$。$y=f(x)$ 与 $y=f^{-1}(x)$ 的图像关于直线 $y=x$ 对称。"))+
 defn("复合函数",p("若 $y=f(u)$ 的定义域为 $D_f$，$u=g(x)$ 的值域是 $D_f$ 的子集，则 $y=f\\big(g(x)\\big)$ 称为 $f$ 与 $g$ 的<strong>复合函数</strong>，$u$ 为中间变量，其定义域是使 $g(x)\\in D_f$ 的 $x$ 的全体。"))+
 der(p("<strong>存在性推导：</strong>严格单调保证「一对一」映射，不同自变量对应不同函数值，故映射可逆。反之若 $f$ 不单调，如 $f(x)=x^2$ 在 $\\mathbb{R}$ 上，$y=4$ 对应两解 $x=\\pm2$，不满足函数唯一性；但限制在 $[0,+\\infty)$ 上严格递增，反函数为 $f^{-1}(x)=\\sqrt{x}$。")+
 p("<strong>求反函数的一般步骤：</strong>① 由 $y=f(x)$ 解出 $x$；② 交换字母 $x,y$；③ 由 $f$ 的值域写出反函数定义域。以 $y=\\dfrac{2x+1}{x-1}\\ (x>1)$ 为例：")+
 fml("y(x-1)=2x+1\\Rightarrow yx-2x=y+1\\Rightarrow x(y-2)=y+1\\Rightarrow x=\\dfrac{y+1}{y-2}")+
 p("交换 $x,y$ 得 $f^{-1}(x)=\\dfrac{x+1}{x-2}$。又 $y=\\dfrac{2x+1}{x-1}=2+\\dfrac{3}{x-1}$，当 $x>1$ 时 $y>2$，故反函数定义域为 $(2,+\\infty)$。")+
 p("<strong>图像对称性推导：</strong>设点 $(a,b)$ 在 $y=f(x)$ 上，即 $b=f(a)$，则 $a=f^{-1}(b)$，即点 $(b,a)$ 在 $y=f^{-1}(x)$ 上。而 $(a,b)$ 与 $(b,a)$ 关于直线 $y=x$ 对称，故两图像关于 $y=x$ 对称。"))+
 exa(p("<strong>例：</strong>求 $y=\\lg(x-1)$ 的反函数。由 $10^y=x-1$ 得 $x=10^y+1$，交换字母得 $f^{-1}(x)=10^x+1\\ (x\\in\\mathbb{R})$。"))+
 note(p("原函数与反函数的定义域、值域互换，单调性一致。求复合函数定义域时不可直接把内层定义域当整体，必须先求使内层值域落入外层定义域的 $x$ 范围。"))
)
},
]},
{"name":"3.2 基本初等函数","color":"#14b8a6","desc":"指数、对数、幂函数与二次函数",
"items":[
{"id":"e3s2-1","name":"指数函数与对数函数","tags":["def","thm","der","exa"],"brief":"指数函数、对数函数定义、图像性质、互为反函数与运算法则推导。",
"body":wrap(
 defn("指数函数",p("形如 $y=a^x\\ (a>0,\\ a\\ne1)$ 的函数称<strong>指数函数</strong>，定义域为 $\\mathbb{R}$，值域为 $(0,+\\infty)$，图像恒过定点 $(0,1)$。当 $a>1$ 时递增，当 $0<a<1$ 时递减。"))+
 defn("对数函数",p("指数函数 $y=a^x$ 的反函数为 $y=\\log_a x\\ (a>0,\\ a\\ne1,\\ x>0)$，称<strong>对数函数</strong>，定义域 $(0,+\\infty)$，值域 $\\mathbb{R}$，恒过 $(1,0)$。$a>1$ 时递增，$0<a<1$ 时递减。"))+
 thm("运算法则",p("设 $a>0,\\ a\\ne1$，$M>0,\\ N>0$，则")+
 fml("a^m\\cdot a^n=a^{m+n},\\quad \\dfrac{a^m}{a^n}=a^{m-n},\\quad (a^m)^n=a^{mn}")+
 fml("\\log_a(MN)=\\log_a M+\\log_a N,\\quad \\log_a\\dfrac{M}{N}=\\log_a M-\\log_a N")+
 fml("\\log_a M^n=n\\log_a M,\\quad \\log_a b=\\dfrac{\\log_c b}{\\log_c a},\\quad a^{\\log_a N}=N"))+
 der(p("<strong>积的对数推导：</strong>设 $M=a^u,\\ N=a^v$，则 $u=\\log_a M,\\ v=\\log_a N$。由指数律 $MN=a^u\\cdot a^v=a^{u+v}$，两边取以 $a$ 为底的对数得")+
 fml("\\log_a(MN)=u+v=\\log_a M+\\log_a N")+
 p("<strong>商的对数推导：</strong>在上式中把 $N$ 换成 $N^{-1}$，利用 $\\log_a N^{-1}=-\\log_a N$ 即得 $\\log_a\\dfrac{M}{N}=\\log_a M-\\log_a N$。")+
 p("<strong>幂的对数推导：</strong>设 $M=a^u$，则 $M^n=(a^u)^n=a^{nu}$，两边取对数得 $\\log_a M^n=nu=n\\log_a M$。")+
 p("<strong>换底公式推导：</strong>设 $y=\\log_a b$，则 $a^y=b$。两边取以 $c$ 为底的对数：$\\log_c a^y=\\log_c b$，即 $y\\log_c a=\\log_c b$，故")+
 fml("y=\\log_a b=\\dfrac{\\log_c b}{\\log_c a}")+
 p("<strong>单调性推导：</strong>对 $y=a^x\\ (a>1)$，取 $x_1<x_2$，则 $\\dfrac{a^{x_2}}{a^{x_1}}=a^{x_2-x_1}>1$（因 $a>1$ 且指数 $x_2-x_1>0$），故 $a^{x_2}>a^{x_1}$，函数递增；$0<a<1$ 时同理得 $a^{x_2}<a^{x_1}$，递减。")+
 p("<strong>互为反函数推导：</strong>由 $y=a^x$ 解出 $x=\\log_a y$，交换字母得 $y=\\log_a x$，即对数函数是指数函数的反函数，两图像关于 $y=x$ 对称。"))+
 exa(p("<strong>例：</strong>计算 $\\log_2 8+\\log_2\\dfrac{1}{4}-\\log_2 16$。因 $\\log_2 8=3$，$\\log_2\\dfrac{1}{4}=\\log_2 2^{-2}=-2$，$\\log_2 16=4$，故原式 $=3-2-4=-3$。"))+
 note(p("比较对数值大小先化为同底，再利用单调性判断。恒等式 $a^{\\log_a N}=N$ 体现了指数与对数运算的互逆。"))
)
},
{"id":"e3s2-2","name":"幂函数与二次函数","tags":["def","der","exa"],"brief":"幂函数性质与二次函数配方法、顶点、对称轴、根的分布。",
"fig":"quadratic","figCap":"二次函数 $y=ax^2+bx+c$ 的抛物线，顶点为 $\\left(-\\dfrac{b}{2a},\\dfrac{4ac-b^2}{4a}\\right)$",
"body":wrap(
 defn("幂函数",p("形如 $y=x^\\alpha$（$\\alpha$ 为常数）的函数称<strong>幂函数</strong>，图像恒过点 $(1,1)$。当 $\\alpha>0$ 时在 $(0,+\\infty)$ 上递增，当 $\\alpha<0$ 时在 $(0,+\\infty)$ 上递减；奇偶性由 $\\alpha$ 的具体取值决定。"))+
 defn("二次函数",p("形如 $y=ax^2+bx+c\\ (a\\ne0)$ 的函数。其图像为抛物线，对称轴为 $x=-\\dfrac{b}{2a}$，顶点为 $\\left(-\\dfrac{b}{2a},\\dfrac{4ac-b^2}{4a}\\right)$；$a>0$ 时开口向上，$a<0$ 时开口向下。"))+
 der(p("<strong>配方法推导顶点式：</strong>对一般式提取首项系数并配方：")+
 fml("y=ax^2+bx+c=a\\left(x^2+\\dfrac{b}{a}x\\right)+c=a\\left[\\left(x+\\dfrac{b}{2a}\\right)^2-\\dfrac{b^2}{4a^2}\\right]+c")+
 fml("=a\\left(x+\\dfrac{b}{2a}\\right)^2-\\dfrac{b^2}{4a}+c=a\\left(x+\\dfrac{b}{2a}\\right)^2+\\dfrac{4ac-b^2}{4a}")+
 p("由 $\\left(x+\\dfrac{b}{2a}\\right)^2\\ge0$ 知，对称轴为 $x=-\\dfrac{b}{2a}$，函数最值为 $\\dfrac{4ac-b^2}{4a}$（$a>0$ 取最小值，$a<0$ 取最大值）。")+
 p("<strong>求根公式推导：</strong>令 $ax^2+bx+c=0$，配方得 $a\\left(x+\\dfrac{b}{2a}\\right)^2=\\dfrac{b^2-4ac}{4a}$，即 $\\left(x+\\dfrac{b}{2a}\\right)^2=\\dfrac{\\Delta}{4a^2}$（其中 $\\Delta=b^2-4ac$）。当 $\\Delta\\ge0$ 时开方得")+
 fml("x=-\\dfrac{b}{2a}\\pm\\dfrac{\\sqrt{\\Delta}}{2a}=\\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}")+
 p("<strong>韦达定理推导：</strong>设两根为 $x_1,x_2$，则 $ax^2+bx+c=a(x-x_1)(x-x_2)=a\\left[x^2-(x_1+x_2)x+x_1x_2\\right]$，比较各项系数得")+
 fml("x_1+x_2=-\\dfrac{b}{a},\\qquad x_1x_2=\\dfrac{c}{a}")+
 p("<strong>判别式与根的关系：</strong>$\\Delta>0$ 时有两个不相等实根；$\\Delta=0$ 时有两个相等实根；$\\Delta<0$ 时无实根。"))+
 exa(p("<strong>例：</strong>求 $y=x^2-4x+3$ 的顶点、对称轴与最值。由 $-\\dfrac{b}{2a}=\\dfrac{4}{2}=2$，$\\dfrac{4ac-b^2}{4a}=\\dfrac{12-16}{4}=-1$，得顶点 $(2,-1)$，对称轴 $x=2$；开口向上，故最小值为 $-1$。"))+
 note(p("在闭区间 $[m,n]$ 上求二次函数最值，需判断顶点横坐标 $-\\dfrac{b}{2a}$ 是否落在区间内：在区间内取顶点值，否则最值在端点处取得。"))
)
},
{"id":"e3s2-3","name":"分段函数与绝对值函数","tags":["def","der","exa"],"brief":"分段函数定义、绝对值函数图像与去绝对值方法。",
"fig":"abs_value","figCap":"绝对值函数 $y=|x|$ 的 V 形图像",
"body":wrap(
 defn("分段函数",p("在定义域的不同子区间上用不同解析式表示的函数称<strong>分段函数</strong>。如符号函数 $\\operatorname{sgn}(x)=\\begin{cases}1,&x>0\\\\0,&x=0\\\\-1,&x<0\\end{cases}$。它是<strong>一个</strong>函数，只是表达式分段而已。"))+
 defn("绝对值函数",p("$y=|x|=\\begin{cases}x,&x\\ge0\\\\-x,&x<0\\end{cases}$，图像为 V 形折线，顶点在原点，值域 $[0,+\\infty)$，是偶函数。几何意义：$|x|$ 表示数轴上点 $x$ 到原点的距离，$|x-a|$ 表示 $x$ 到点 $a$ 的距离。"))+
 der(p("<strong>去绝对值的三种方法：</strong>① 定义法，直接按被绝对值的正负分段；② 零点分段法，令各绝对值为零求出零点，用零点划分区间后逐段讨论；③ 平方法，利用 $|u|^2=u^2$ 与 $|u|=\\sqrt{u^2}$。")+
 p("<strong>三角不等式推导：</strong>由 $-|a|\\le a\\le|a|$ 与 $-|b|\\le b\\le|b|$ 相加得 $-(|a|+|b|)\\le a+b\\le|a|+|b|$，即 $|a+b|\\le|a|+|b|$；又 $|a|=|(a+b)-b|\\le|a+b|+|b|$，得 $|a|-|b|\\le|a+b|$。综合得")+
 fml("\\big||a|-|b|\\big|\\le|a+b|\\le|a|+|b|")+
 p("<strong>分段化简推导：</strong>化简 $y=|x-2|+|x+1|$。零点为 $x=2$ 与 $x=-1$，据此分三段讨论：")+
 fml("y=\\begin{cases}-2x+1,&x<-1\\\\3,&-1\\le x<2\\\\2x-1,&x\\ge2\\end{cases}")+
 p("当 $x\\in[-1,2]$ 时 $y\\equiv3$，为该函数的最小值，说明 $y\\ge3$。这正是三角不等式的体现：$|x-2|+|x+1|\\ge|(x-2)-(x+1)|=3$。")+
 p("<strong>不等式的等价转化：</strong>对 $b>0$，$|u|\\le b\\Leftrightarrow-b\\le u\\le b$；$|u|\\ge b\\Leftrightarrow u\\le-b$ 或 $u\\ge b$。"))+
 exa(p("<strong>例：</strong>解不等式 $|x-1|<2$。由等价转化得 $-2<x-1<2$，各边加 1 得 $-1<x<3$，故解集为 $(-1,3)$。"))+
 note(p("含多个绝对值的函数一般用零点分段法化为分段函数。注意 $\\sqrt{x^2}=|x|$ 而非 $x$，这是二次根式化简中最易出错之处。"))
)
},
]},
{"name":"3.3 三角函数","color":"#0f766e","desc":"任意角三角函数、同角关系、诱导公式、和差倍半角",
"items":[
{"id":"e3s3-1","name":"六个三角函数的定义","tags":["def","der","exa"],"brief":"弧度制、单位圆定义六个三角函数、符号规律与三角函数线。",
"fig":"trig_circle","figCap":"单位圆上点 $P(\\cos\\theta,\\sin\\theta)$ 及正弦线、余弦线、正切线",
"body":wrap(
 defn("弧度制",p("弧长等于半径的弧所对的圆心角为 1 弧度（rad）。$\\pi\\ \\text{rad}=180^\\circ$，故 $1^\\circ=\\dfrac{\\pi}{180}\\ \\text{rad}\\approx0.01745\\ \\text{rad}$。角的概念推广到任意角后，逆时针为正角、顺时针为负角、不旋转为零角。"))+
 defn("六个三角函数",p("设 $\\alpha$ 为任意角，在其终边上任取一点 $P(x,y)$（$P\\ne O$），记 $r=\\sqrt{x^2+y^2}>0$，则定义")+
 fml("\\sin\\alpha=\\dfrac{y}{r},\\quad \\cos\\alpha=\\dfrac{x}{r},\\quad \\tan\\alpha=\\dfrac{y}{x}")+
 fml("\\cot\\alpha=\\dfrac{x}{y},\\quad \\sec\\alpha=\\dfrac{r}{x},\\quad \\csc\\alpha=\\dfrac{r}{y}")+
 p("六者两两成对互为倒数：$\\tan\\alpha=\\dfrac{1}{\\cot\\alpha}$，$\\cos\\alpha=\\dfrac{1}{\\sec\\alpha}$，$\\sin\\alpha=\\dfrac{1}{\\csc\\alpha}$。定义与所取点的位置无关，只取决于终边。"))+
 der(p("<strong>单位圆推导：</strong>取 $r=1$，终边与单位圆交于 $P(\\cos\\alpha,\\sin\\alpha)$，由圆的方程 $x^2+y^2=1$ 立即得到")+
 fml("\\sin^2\\alpha+\\cos^2\\alpha=1")+
 p("<strong>倒数关系推导：</strong>由定义 $\\dfrac{1}{\\cos\\alpha}=\\dfrac{1}{x/r}=\\dfrac{r}{x}=\\sec\\alpha$，同理 $\\dfrac{1}{\\sin\\alpha}=\\csc\\alpha$，$\\dfrac{1}{\\tan\\alpha}=\\cot\\alpha$。")+
 p("<strong>符号规律推导：</strong>由定义，符号取决于 $x,y$ 的正负。第一象限 $x>0,y>0$，六函数全正；第二象限 $x<0,y>0$，故 $\\sin,\\csc$ 为正、其余负；第三象限 $x<0,y<0$，故 $\\tan,\\cot$ 为正（负负相除）其余负；第四象限 $x>0,y<0$，故 $\\cos,\\sec$ 为正、其余负。即「一全正、二正弦、三正切、四余弦」。")+
 p("<strong>定义域推导：</strong>$\\tan,\\sec$ 含分母 $x$，故 $x=0$ 即 $\\alpha=\\dfrac{\\pi}{2}+k\\pi$ 处无定义；$\\cot,\\csc$ 含分母 $y$，故 $y=0$ 即 $\\alpha=k\\pi$ 处无定义。")+
 p("<strong>三角函数线推导：</strong>在单位圆中，设角 $\\alpha$ 终边与单位圆交于 $P$，作 $PM\\perp x$ 轴于 $M$，过 $A(1,0)$ 作圆切线与终边所在直线交于 $T$，则有向线段 $MP=\\sin\\alpha$（正弦线），$OM=\\cos\\alpha$（余弦线），$AT=\\tan\\alpha$（正切线）。当 $0<\\alpha<\\dfrac{\\pi}{2}$ 时，比较 $\\triangle OAP$、扇形 $OAP$、$\\triangle OAT$ 的面积：")+
 fml("\\dfrac{1}{2}\\sin\\alpha<\\dfrac{1}{2}\\alpha<\\dfrac{1}{2}\\tan\\alpha\\ \\Rightarrow\\ \\sin\\alpha<\\alpha<\\tan\\alpha")+
 p("<strong>弧长与扇形面积：</strong>由弧度定义，弧长 $l=|\\alpha|r$，扇形面积 $S=\\dfrac{1}{2}lr=\\dfrac{1}{2}|\\alpha|r^2$。"))+
 exa(p("<strong>例：</strong>取 $\\alpha=\\dfrac{\\pi}{3}$，终边过 $P(1,\\sqrt3)$，$r=2$，故 $\\sin\\dfrac{\\pi}{3}=\\dfrac{\\sqrt3}{2}$，$\\cos\\dfrac{\\pi}{3}=\\dfrac{1}{2}$，$\\tan\\dfrac{\\pi}{3}=\\sqrt3$，$\\cot\\dfrac{\\pi}{3}=\\dfrac{\\sqrt3}{3}$，$\\sec\\dfrac{\\pi}{3}=2$，$\\csc\\dfrac{\\pi}{3}=\\dfrac{2\\sqrt3}{3}$。"))+
 note(p("三角函数线把三角函数值转化为有向线段的数量，是理解符号、单调性与不等式的重要几何工具；$\\sin\\alpha<\\alpha<\\tan\\alpha$ 常用于比较大小与证明不等式。"))
)
},
{"id":"e3s3-2","name":"同角关系与诱导公式","tags":["def","thm","der","exa"],"brief":"同角三角函数基本关系与诱导公式的推导。",
"body":wrap(
 defn("同角三角函数基本关系",p("对同一个角 $\\alpha$，六个三角函数之间存在相互制约的基本恒等式，统称<strong>同角基本关系</strong>，含平方关系与商数关系：")+
 fml("\\sin^2\\alpha+\\cos^2\\alpha=1,\\qquad \\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}")+
 fml("1+\\tan^2\\alpha=\\sec^2\\alpha,\\qquad 1+\\cot^2\\alpha=\\csc^2\\alpha"))+
 thm("诱导公式",p("规律为「奇变偶不变，符号看象限」：$\\dfrac{k\\pi}{2}\\pm\\alpha$ 的三角函数，$k$ 为奇数时函数名互换（正余互换），$k$ 为偶数时函数名不变，符号由把 $\\alpha$ 视作锐角时原角所在象限确定。"))+
 der(p("<strong>平方关系推导：</strong>由单位圆 $x^2+y^2=1$，代入 $x=\\cos\\alpha,\\ y=\\sin\\alpha$ 即得 $\\sin^2\\alpha+\\cos^2\\alpha=1$。")+
 p("<strong>商数关系推导：</strong>$\\dfrac{\\sin\\alpha}{\\cos\\alpha}=\\dfrac{y/r}{x/r}=\\dfrac{y}{x}=\\tan\\alpha$（要求 $\\cos\\alpha\\ne0$）。")+
 p("<strong>平方关系的变形推导：</strong>将 $\\sin^2\\alpha+\\cos^2\\alpha=1$ 两边同除 $\\cos^2\\alpha$ 得 $\\tan^2\\alpha+1=\\sec^2\\alpha$；两边同除 $\\sin^2\\alpha$ 得 $1+\\cot^2\\alpha=\\csc^2\\alpha$。")+
 p("<strong>$\\sin(\\pi-\\alpha)$ 推导：</strong>$\\pi-\\alpha$ 的终边与 $\\alpha$ 的终边关于 $y$ 轴对称，对应点横坐标互为相反数、纵坐标相同，故")+
 fml("\\sin(\\pi-\\alpha)=\\sin\\alpha,\\qquad \\cos(\\pi-\\alpha)=-\\cos\\alpha")+
 p("<strong>$\\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)$ 推导：</strong>$\\dfrac{\\pi}{2}-\\alpha$ 的终边与 $\\alpha$ 的终边关于直线 $y=x$ 对称，横纵坐标互换，故")+
 fml("\\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\cos\\alpha,\\qquad \\cos\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\sin\\alpha")+
 p("<strong>负角与 $\\pi+\\alpha$ 推导：</strong>$-\\alpha$ 与 $\\alpha$ 终边关于 $x$ 轴对称，故 $\\sin(-\\alpha)=-\\sin\\alpha,\\ \\cos(-\\alpha)=\\cos\\alpha$；$\\pi+\\alpha$ 与 $\\alpha$ 终边关于原点对称，故 $\\sin(\\pi+\\alpha)=-\\sin\\alpha,\\ \\cos(\\pi+\\alpha)=-\\cos\\alpha$。")+
 p("<strong>「知一求二」推导：</strong>已知 $\\sin\\alpha=m$，由平方关系 $\\cos\\alpha=\\pm\\sqrt{1-m^2}$，符号由 $\\alpha$ 所在象限决定；再由商数关系 $\\tan\\alpha=\\dfrac{m}{\\pm\\sqrt{1-m^2}}$。"))+
 exa(p("<strong>例：</strong>已知 $\\sin\\alpha=\\dfrac{3}{5}$ 且 $\\alpha$ 为第二象限角，求 $\\cos\\alpha,\\tan\\alpha$。第二象限余弦为负，故 $\\cos\\alpha=-\\sqrt{1-\\sin^2\\alpha}=-\\sqrt{1-\\dfrac{9}{25}}=-\\dfrac{4}{5}$，从而 $\\tan\\alpha=\\dfrac{3/5}{-4/5}=-\\dfrac{3}{4}$。"))+
 note(p("使用平方关系开方时务必依据象限确定符号。诱导公式可统一为「把任意角化到 $0^\\circ\\sim90^\\circ$ 再求值」，是化简与求值的基础。"))
)
},
{"id":"e3s3-3","name":"和差倍半角公式","tags":["def","thm","der","exa"],"brief":"两角和差、二倍角、半角公式的推导。",
"body":wrap(
 defn("两角和与差的三角函数公式",p("把 $\\sin(\\alpha\\pm\\beta)$、$\\cos(\\alpha\\pm\\beta)$、$\\tan(\\alpha\\pm\\beta)$ 用 $\\alpha,\\beta$ 的三角函数表示的公式统称<strong>和差角公式</strong>，它是全部三角恒等变换的出发点：")+
 fml("\\sin(\\alpha\\pm\\beta)=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta")+
 fml("\\cos(\\alpha\\pm\\beta)=\\cos\\alpha\\cos\\beta\\mp\\sin\\alpha\\sin\\beta")+
 fml("\\tan(\\alpha\\pm\\beta)=\\dfrac{\\tan\\alpha\\pm\\tan\\beta}{1\\mp\\tan\\alpha\\tan\\beta}"))+
 thm("倍角公式",p("在和角公式中令 $\\beta=\\alpha$ 即得")+
 fml("\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha")+
 fml("\\cos 2\\alpha=\\cos^2\\alpha-\\sin^2\\alpha=2\\cos^2\\alpha-1=1-2\\sin^2\\alpha")+
 fml("\\tan 2\\alpha=\\dfrac{2\\tan\\alpha}{1-\\tan^2\\alpha}"))+
 der(p("<strong>$\\cos(\\alpha-\\beta)$ 的单位圆推导：</strong>在单位圆上取 $A(\\cos\\alpha,\\sin\\alpha)$、$B(\\cos\\beta,\\sin\\beta)$，由两点间距离公式：")+
 fml("|AB|^2=(\\cos\\alpha-\\cos\\beta)^2+(\\sin\\alpha-\\sin\\beta)^2=2-2(\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta)")+
 p("另一方面，半径 $OA,OB$ 的夹角为 $\\alpha-\\beta$，由余弦定理 $|AB|^2=1^2+1^2-2\\cos(\\alpha-\\beta)=2-2\\cos(\\alpha-\\beta)$。两式比较即得")+
 fml("\\cos(\\alpha-\\beta)=\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta")+
 p("<strong>和角公式推导：</strong>把上式中 $\\beta$ 换成 $-\\beta$，利用 $\\cos(-\\beta)=\\cos\\beta$、$\\sin(-\\beta)=-\\sin\\beta$ 得 $\\cos(\\alpha+\\beta)=\\cos\\alpha\\cos\\beta-\\sin\\alpha\\sin\\beta$；再由 $\\sin\\theta=\\cos\\left(\\dfrac{\\pi}{2}-\\theta\\right)$ 化归：")+
 fml("\\sin(\\alpha+\\beta)=\\cos\\left[\\left(\\dfrac{\\pi}{2}-\\alpha\\right)-\\beta\\right]=\\sin\\alpha\\cos\\beta+\\cos\\alpha\\sin\\beta")+
 p("<strong>正切和角推导：</strong>$\\tan(\\alpha+\\beta)=\\dfrac{\\sin(\\alpha+\\beta)}{\\cos(\\alpha+\\beta)}=\\dfrac{\\sin\\alpha\\cos\\beta+\\cos\\alpha\\sin\\beta}{\\cos\\alpha\\cos\\beta-\\sin\\alpha\\sin\\beta}$，分子分母同除 $\\cos\\alpha\\cos\\beta$ 得 $\\dfrac{\\tan\\alpha+\\tan\\beta}{1-\\tan\\alpha\\tan\\beta}$。")+
 p("<strong>倍角推导：</strong>在 $\\sin(\\alpha+\\beta)$ 中令 $\\beta=\\alpha$ 得 $\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha$；在 $\\cos(\\alpha+\\beta)$ 中令 $\\beta=\\alpha$ 得 $\\cos 2\\alpha=\\cos^2\\alpha-\\sin^2\\alpha$，再由 $\\sin^2\\alpha+\\cos^2\\alpha=1$ 化为 $2\\cos^2\\alpha-1$ 与 $1-2\\sin^2\\alpha$。")+
 p("<strong>半角推导：</strong>由 $\\cos 2\\theta=1-2\\sin^2\\theta$ 与 $\\cos 2\\theta=2\\cos^2\\theta-1$，令 $2\\theta=\\alpha$ 得")+
 fml("\\sin\\dfrac{\\alpha}{2}=\\pm\\sqrt{\\dfrac{1-\\cos\\alpha}{2}},\\qquad \\cos\\dfrac{\\alpha}{2}=\\pm\\sqrt{\\dfrac{1+\\cos\\alpha}{2}}")+
 p("符号由 $\\dfrac{\\alpha}{2}$ 所在象限决定。"))+
 exa(p("<strong>例：</strong>求 $\\sin 75^\\circ$。$\\sin 75^\\circ=\\sin(45^\\circ+30^\\circ)=\\dfrac{\\sqrt2}{2}\\cdot\\dfrac{\\sqrt3}{2}+\\dfrac{\\sqrt2}{2}\\cdot\\dfrac{1}{2}=\\dfrac{\\sqrt6+\\sqrt2}{4}$。"))+
 note(p("辅助角公式：$a\\sin x+b\\cos x=\\sqrt{a^2+b^2}\\,\\sin(x+\\varphi)$，其中 $\\tan\\varphi=\\dfrac{b}{a}$，常用于求三角式的最值与周期。"))
)
},
{"id":"e3s3-4","name":"三角恒等变换","tags":["thm","der","exa"],"brief":"和差化积、积化和差与万能公式的推导。",
"body":wrap(
 defn("三角恒等变换",p("综合运用和差角、倍角、半角等公式，对三角式进行化简、求值与证明，这类变形统称<strong>三角恒等变换</strong>。常用工具为和差化积、积化和差、万能公式与降幂公式。"))+
 thm("和差化积",p("")+
 fml("\\sin\\alpha+\\sin\\beta=2\\sin\\dfrac{\\alpha+\\beta}{2}\\cos\\dfrac{\\alpha-\\beta}{2}")+
 fml("\\cos\\alpha+\\cos\\beta=2\\cos\\dfrac{\\alpha+\\beta}{2}\\cos\\dfrac{\\alpha-\\beta}{2}")+
 fml("\\cos\\alpha-\\cos\\beta=-2\\sin\\dfrac{\\alpha+\\beta}{2}\\sin\\dfrac{\\alpha-\\beta}{2}"))+
 thm("积化和差",p("")+
 fml("\\sin\\alpha\\cos\\beta=\\dfrac{1}{2}\\big[\\sin(\\alpha+\\beta)+\\sin(\\alpha-\\beta)\\big]")+
 fml("\\cos\\alpha\\sin\\beta=\\dfrac{1}{2}\\big[\\sin(\\alpha+\\beta)-\\sin(\\alpha-\\beta)\\big]")+
 fml("\\cos\\alpha\\cos\\beta=\\dfrac{1}{2}\\big[\\cos(\\alpha+\\beta)+\\cos(\\alpha-\\beta)\\big]"))+
 thm("万能公式",p("设 $t=\\tan\\dfrac{\\alpha}{2}$，则")+
 fml("\\sin\\alpha=\\dfrac{2t}{1+t^2},\\qquad \\cos\\alpha=\\dfrac{1-t^2}{1+t^2},\\qquad \\tan\\alpha=\\dfrac{2t}{1-t^2}"))+
 der(p("<strong>积化和差推导：</strong>由和角公式")+
 fml("\\sin(A+B)=\\sin A\\cos B+\\cos A\\sin B,\\qquad \\sin(A-B)=\\sin A\\cos B-\\cos A\\sin B")+
 p("两式相加得 $2\\sin A\\cos B=\\sin(A+B)+\\sin(A-B)$，即 $\\sin A\\cos B=\\dfrac{1}{2}[\\sin(A+B)+\\sin(A-B)]$；两式相减得 $\\cos A\\sin B=\\dfrac{1}{2}[\\sin(A+B)-\\sin(A-B)]$。")+
 p("<strong>和差化积推导：</strong>令 $\\alpha=A+B,\\ \\beta=A-B$，则 $A=\\dfrac{\\alpha+\\beta}{2},\\ B=\\dfrac{\\alpha-\\beta}{2}$。把 $\\sin\\alpha+\\sin\\beta=\\sin(A+B)+\\sin(A-B)=2\\sin A\\cos B$ 代回即得")+
 fml("\\sin\\alpha+\\sin\\beta=2\\sin\\dfrac{\\alpha+\\beta}{2}\\cos\\dfrac{\\alpha-\\beta}{2}")+
 p("<strong>万能公式推导：</strong>令 $t=\\tan\\dfrac{\\alpha}{2}$，由 $\\sin\\alpha=2\\sin\\dfrac{\\alpha}{2}\\cos\\dfrac{\\alpha}{2}$，分子分母同除 $\\cos^2\\dfrac{\\alpha}{2}$：")+
 fml("\\sin\\alpha=\\dfrac{2\\tan\\dfrac{\\alpha}{2}}{1+\\tan^2\\dfrac{\\alpha}{2}}=\\dfrac{2t}{1+t^2}")+
 p("又 $\\cos\\alpha=\\cos^2\\dfrac{\\alpha}{2}-\\sin^2\\dfrac{\\alpha}{2}=\\dfrac{1-\\tan^2\\dfrac{\\alpha}{2}}{1+\\tan^2\\dfrac{\\alpha}{2}}=\\dfrac{1-t^2}{1+t^2}$，从而 $\\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}=\\dfrac{2t}{1-t^2}$。")+
 p("<strong>降幂公式推导：</strong>由 $\\cos 2\\alpha=2\\cos^2\\alpha-1=1-2\\sin^2\\alpha$ 反解得 $\\sin^2\\alpha=\\dfrac{1-\\cos 2\\alpha}{2}$，$\\cos^2\\alpha=\\dfrac{1+\\cos 2\\alpha}{2}$。"))+
 exa(p("<strong>例：</strong>化简 $\\sin 40^\\circ+\\sin 20^\\circ$。由和差化积得 $2\\sin 30^\\circ\\cos 10^\\circ=2\\cdot\\dfrac{1}{2}\\cos 10^\\circ=\\cos 10^\\circ$。"))+
 note(p("万能公式把三角函数有理式统一化为关于 $t=\\tan\\dfrac{\\alpha}{2}$ 的有理式，是解三角方程与积分的重要工具，但需注意 $\\alpha\\ne(2k+1)\\pi$。"))
)
},
]},
{"name":"3.4 反三角函数","color":"#15803d","desc":"反三角函数定义与关系",
"items":[
{"id":"e3s4-1","name":"反三角函数定义与关系","tags":["def","thm","der","exa"],"brief":"反正弦、反余弦、反正切定义、主值区间与互补关系推导。",
"body":wrap(
 defn("反三角函数",p("在三角函数各自的单调区间上定义其反函数：<strong>反正弦</strong> $y=\\arcsin x$，$x\\in[-1,1]$，$y\\in\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$；<strong>反余弦</strong> $y=\\arccos x$，$x\\in[-1,1]$，$y\\in[0,\\pi]$；<strong>反正切</strong> $y=\\arctan x$，$x\\in\\mathbb{R}$，$y\\in\\left(-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right)$。所选定的区间称<strong>主值区间</strong>。"))+
 thm("互补关系与恒等式",p("")+
 fml("\\arcsin x+\\arccos x=\\dfrac{\\pi}{2}\\quad(|x|\\le1)")+
 fml("\\arctan x+\\operatorname{arccot}x=\\dfrac{\\pi}{2}")+
 fml("\\sin(\\arcsin x)=x,\\quad \\cos(\\arcsin x)=\\sqrt{1-x^2},\\quad \\tan(\\arccos x)=\\dfrac{\\sqrt{1-x^2}}{x}"))+
 der(p("<strong>主值区间的必要性：</strong>以 $y=\\sin x$ 为例，它在一个周期内不单调，整体不可逆；但限制在 $\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$ 上严格递增且值域恰为 $[-1,1]$，故可定义反函数 $y=\\arcsin x$。同理 $y=\\cos x$ 限制在 $[0,\\pi]$、$y=\\tan x$ 限制在 $\\left(-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right)$ 上单调可逆。")+
 p("<strong>互补关系推导：</strong>设 $\\alpha=\\arcsin x$，则 $\\sin\\alpha=x$ 且 $\\alpha\\in\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$。由 $\\sin\\alpha=\\cos\\left(\\dfrac{\\pi}{2}-\\alpha\\right)$，且 $\\dfrac{\\pi}{2}-\\alpha\\in[0,\\pi]$ 恰落在 $y=\\arccos x$ 的主值区间内，故")+
 fml("\\arccos x=\\dfrac{\\pi}{2}-\\alpha=\\dfrac{\\pi}{2}-\\arcsin x\\ \\Rightarrow\\ \\arcsin x+\\arccos x=\\dfrac{\\pi}{2}")+
 p("<strong>反三角恒等式推导：</strong>$\\sin(\\arcsin x)=x$ 由定义直接得到。对 $\\cos(\\arcsin x)$，因 $\\arcsin x\\in\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$ 时 $\\cos\\ge0$，故")+
 fml("\\cos(\\arcsin x)=\\sqrt{1-\\sin^2(\\arcsin x)}=\\sqrt{1-x^2}")+
 p("从而 $\\tan(\\arccos x)=\\dfrac{\\sin(\\arccos x)}{\\cos(\\arccos x)}=\\dfrac{\\sqrt{1-x^2}}{x}\\ (x\\ne0)$。"))+
 exa(p("<strong>例：</strong>求 $\\arcsin\\dfrac{\\sqrt3}{2}+\\arccos\\dfrac{1}{2}$。由 $\\arcsin\\dfrac{\\sqrt3}{2}=\\dfrac{\\pi}{3}$，$\\arccos\\dfrac{1}{2}=\\dfrac{\\pi}{3}$，故原式 $=\\dfrac{2\\pi}{3}$；亦可由互补关系验证 $\\arccos\\dfrac{1}{2}=\\dfrac{\\pi}{2}-\\arcsin\\dfrac{1}{2}=\\dfrac{\\pi}{2}-\\dfrac{\\pi}{6}=\\dfrac{\\pi}{3}$。"))+
 note(p("反三角函数的结果必须落在主值区间内，如 $\\arcsin\\left(\\sin\\dfrac{5\\pi}{6}\\right)=\\arcsin\\dfrac{1}{2}=\\dfrac{\\pi}{6}\\ne\\dfrac{5\\pi}{6}$，切勿误认为「反函数与原函数复合等于自变量本身」。"))
)
},
]}
]
# ============ 第四章 数列 ============
# ============ 第四章 数列 ============
ch4_sections = [
{"name":"4.1 等差数列","color":"#c2410c","desc":"通项公式、前 n 项和、等差中项与性质",
"items":[
{"id":"e4s1-1","name":"等差数列通项与求和","tags":["def","thm","der","exa"],"brief":"等差数列定义、通项公式与前 n 项和公式（倒序相加）的严格推导。",
"fig":"sequence","figCap":"等差数列 $a_n=a_1+(n-1)d$ 在数轴上的等距分布",
"body":wrap(
 defn("等差数列",p("若数列 $\\{a_n\\}$ 满足 $a_{n+1}-a_n=d$（$d$ 为与 $n$ 无关的常数），则称 $\\{a_n\\}$ 为<strong>等差数列</strong>，$d$ 称为<strong>公差</strong>；即从第 2 项起，每一项与前一项的差都等于同一个常数。当 $d>0$ 时数列递增，$d<0$ 时递减，$d=0$ 时为常数列。"))+
 thm("通项公式与前 n 项和",p("设等差数列 $\\{a_n\\}$ 的首项为 $a_1$、公差为 $d$，则")+
 fml("a_n=a_1+(n-1)d")+
 fml("S_n=\\dfrac{n(a_1+a_n)}{2}=na_1+\\dfrac{n(n-1)}{2}\\,d")+
 p("其中 $S_n=a_1+a_2+\\cdots+a_n$ 为前 $n$ 项和。"))+
 der(p("<strong>第一步：由定义写出 $n-1$ 个等式。</strong>由 $a_{k+1}-a_k=d$ 依次取 $k=1,2,\\ldots,n-1$：")+
 fml("a_2-a_1=d,\\quad a_3-a_2=d,\\quad \\ldots,\\quad a_n-a_{n-1}=d")+
 p("<strong>第二步：将 $n-1$ 个等式左右分别相加。</strong>左端中间项两两抵消（裂项相消），只剩首末两项 $a_n-a_1$：")+
 fml("(a_2-a_1)+(a_3-a_2)+\\cdots+(a_n-a_{n-1})=a_n-a_1=(n-1)d")+
 p("<strong>第三步：解出通项。</strong>移项即得 $a_n=a_1+(n-1)d$；当 $n=1$ 时右端为 $a_1$，等式也成立，故通项公式对一切正整数 $n$ 成立。")+
 p("<strong>第四步：前 $n$ 项和（倒序相加）。</strong>设")+
 fml("S_n=a_1+a_2+\\cdots+a_{n-1}+a_n\\quad\\text{①}")+
 p("将其各项<strong>倒序</strong>重写：")+
 fml("S_n=a_n+a_{n-1}+\\cdots+a_2+a_1\\quad\\text{②}")+
 p("<strong>第五步：①、② 两式相加。</strong>左端为 $2S_n$，右端按位置配对，每一对都是 $a_1+a_n$：")+
 fml("2S_n=(a_1+a_n)+(a_2+a_{n-1})+\\cdots+(a_n+a_1)")+
 p("<strong>第六步：证明每对之和都等于 $a_1+a_n$。</strong>对任意 $k$（$1\\le k\\le n$）有")+
 fml("a_k+a_{n-k+1}=\\big[a_1+(k-1)d\\big]+\\big[a_1+(n-k)d\\big]=2a_1+(n-1)d=a_1+a_n")+
 p("故右端共有 $n$ 对、每对都等于 $a_1+a_n$，即 $2S_n=n(a_1+a_n)$，从而")+
 fml("S_n=\\dfrac{n(a_1+a_n)}{2}")+
 p("<strong>第七步：化为只含 $a_1,d$ 的形式。</strong>把 $a_n=a_1+(n-1)d$ 代入上式：")+
 fml("S_n=\\dfrac{n\\big[2a_1+(n-1)d\\big]}{2}=na_1+\\dfrac{n(n-1)}{2}\\,d"))+
 exa(p("<strong>例：</strong>等差数列中 $a_1=2$，$d=3$，求 $a_{10}$ 与 $S_{10}$。")+
 fml("a_{10}=2+9\\times3=29,\\qquad S_{10}=\\dfrac{10\\times(2+29)}{2}=155")+
 p("用第二个求和公式验证：$S_{10}=10\\times2+\\dfrac{10\\times9}{2}\\times3=20+135=155$，两种算法一致。"))+
 note(p("通项公式说明：$d\\ne0$ 时 $a_n$ 是 $n$ 的一次函数，其图象是直线 $y=dx+(a_1-d)$ 上横坐标为正整数的一串孤立点，故可用「$a_n$ 关于 $n$ 线性」来判断等差数列。"))
)
},
{"id":"e4s1-2","name":"等差数列的性质","tags":["def","thm","der","exa"],"brief":"等差中项、下标和性质与片段和成等差数列的严格证明。",
"body":wrap(
 defn("等差中项",p("若 $a,A,b$ 三数成等差数列，则称 $A$ 为 $a$ 与 $b$ 的<strong>等差中项</strong>，且满足 $2A=a+b$，即 $A=\\dfrac{a+b}{2}$。三数成等差 $\\iff$ 中间数等于另外两数的算术平均。"))+
 thm("下标和性质",p("在等差数列 $\\{a_n\\}$ 中，若 $m+n=p+q$（$m,n,p,q$ 为正整数），则")+
 fml("a_m+a_n=a_p+a_q")+
 p("特别地 $a_1+a_n=a_2+a_{n-1}=\\cdots$，这正是倒序相加能成立的根本原因。"))+
 thm("片段和性质",p("设 $S_n$ 为等差数列前 $n$ 项和，则")+
 fml("S_n,\\ \\ S_{2n}-S_n,\\ \\ S_{3n}-S_{2n},\\ \\ldots")+
 p("仍成等差数列，其公差为 $n^2 d$。"))+
 der(p("<strong>（一）等差中项的推导。</strong>设 $a,A,b$ 成等差，则公差相等 $A-a=b-A$，两边加 $A+a$ 得 $2A=a+b$，故 $A=\\dfrac{a+b}{2}$；反之若 $2A=a+b$，则 $A-a=b-A$，三数成等差。")+
 p("<strong>（二）下标和性质的推导。</strong>由通项公式 $a_k=a_1+(k-1)d$ 分别展开两端：")+
 fml("a_m+a_n=\\big[a_1+(m-1)d\\big]+\\big[a_1+(n-1)d\\big]=2a_1+(m+n-2)d")+
 fml("a_p+a_q=2a_1+(p+q-2)d")+
 p("当 $m+n=p+q$ 时两式右端完全相等，故 $a_m+a_n=a_p+a_q$。")+
 p("<strong>（三）片段和性质——第一段。</strong>记 $A=S_n$，由求和公式")+
 fml("A=na_1+\\dfrac{n(n-1)}{2}d")+
 p("<strong>（四）第二段。</strong>$B=S_{2n}-S_n=a_{n+1}+a_{n+2}+\\cdots+a_{2n}$，这是首项 $a_{n+1}=a_1+nd$、项数 $n$、公差仍为 $d$ 的等差数列之和：")+
 fml("B=n(a_1+nd)+\\dfrac{n(n-1)}{2}d=A+n^2 d")+
 p("<strong>（五）第三段。</strong>$C=S_{3n}-S_{2n}$ 是首项 $a_{2n+1}=a_1+2nd$、项数 $n$ 的等差数列之和：")+
 fml("C=n(a_1+2nd)+\\dfrac{n(n-1)}{2}d=A+2n^2 d")+
 p("<strong>（六）检验等差。</strong>由 $B-A=n^2 d$ 与 $C-B=n^2 d$ 相等（与 $n$ 无关），故 $A,B,C$ 成等差数列，公差为 $n^2 d$；对更多片段同理递推成立。"))+
 exa(p("<strong>例：</strong>等差数列中 $a_3+a_{11}=20$，求 $S_{13}$。由下标和 $3+11=1+13$ 得 $a_1+a_{13}=a_3+a_{11}=20$，于是")+
 fml("S_{13}=\\dfrac{13(a_1+a_{13})}{2}=\\dfrac{13\\times20}{2}=130"))+
 app(p("<strong>应用（前 $n$ 项和的最值）：</strong>由 $S_n=\\dfrac{d}{2}n^2+\\Big(a_1-\\dfrac{d}{2}\\Big)n$ 知 $S_n$ 是 $n$ 的二次函数。$d>0$ 时 $S_n$ 先减后增、有最小值；$d<0$ 时先增后减、有最大值。$d<0$ 时 $S_n$ 取最大值的 $n$ 满足 $a_n\\ge0$ 且 $a_{n+1}\\le0$，即在数列由正转负的临界项处取到。"))+
 note(p("凡涉及「两项之和」的已知条件，优先配成首末项之和；凡涉及 $S_n,\\ S_{2n}-S_n,\\ \\ldots$，直接套用公差 $n^2 d$ 的片段和结论。"))
)
}
]},
{"name":"4.2 等比数列","color":"#dc2626","desc":"通项公式、前 n 项和、无穷等比与递推",
"items":[
{"id":"e4s2-1","name":"等比数列通项与求和","tags":["def","thm","der","exa"],"brief":"等比数列定义、通项公式与前 n 项和公式（错位相减）的严格推导。",
"body":wrap(
 defn("等比数列",p("若数列 $\\{a_n\\}$ 满足 $\\dfrac{a_{n+1}}{a_n}=q$（常数，$q\\ne0$，且 $a_n\\ne0$），则称 $\\{a_n\\}$ 为<strong>等比数列</strong>，$q$ 称为<strong>公比</strong>。由 $a_1\\ne0$、$q\\ne0$ 知各项均不为零。"))+
 thm("通项公式与前 n 项和",p("设等比数列首项为 $a_1$、公比为 $q$，则")+
 fml("a_n=a_1 q^{n-1}")+
 fml("S_n=\\dfrac{a_1(1-q^n)}{1-q}\\ (q\\ne1),\\qquad S_n=na_1\\ (q=1)"))+
 der(p("<strong>第一步：累乘求通项。</strong>由定义 $\\dfrac{a_{k+1}}{a_k}=q$ 依次取 $k=1,2,\\ldots,n-1$：")+
 fml("\\dfrac{a_2}{a_1}=q,\\quad \\dfrac{a_3}{a_2}=q,\\quad \\ldots,\\quad \\dfrac{a_n}{a_{n-1}}=q")+
 p("<strong>第二步：将 $n-1$ 个等式左右相乘。</strong>左端分子分母逐项约去，只剩 $\\dfrac{a_n}{a_1}$：")+
 fml("\\dfrac{a_2}{a_1}\\cdot\\dfrac{a_3}{a_2}\\cdots\\dfrac{a_n}{a_{n-1}}=\\dfrac{a_n}{a_1}=q^{\\,n-1}")+
 p("故 $a_n=a_1 q^{n-1}$，通项公式得证。")+
 p("<strong>第三步：$q=1$ 时求和。</strong>此时各项都等于 $a_1$，故 $S_n=na_1$。")+
 p("<strong>第四步：$q\\ne1$ 时求和（错位相减）。</strong>设")+
 fml("S_n=a_1+a_1 q+a_1 q^2+\\cdots+a_1 q^{n-1}\\quad\\text{①}")+
 p("两边同乘 $q$，右端各项指数整体升高一次（即「向左错一位」）：")+
 fml("qS_n=a_1 q+a_1 q^2+\\cdots+a_1 q^{n-1}+a_1 q^{n}\\quad\\text{②}")+
 p("<strong>第五步：①$-$②。</strong>相同的中间项 $a_1q,a_1q^2,\\ldots,a_1q^{n-1}$ 全部相消，只剩①的首项 $a_1$ 与②的末项 $a_1q^n$：")+
 fml("(1-q)S_n=a_1-a_1 q^{n}=a_1(1-q^n)")+
 p("<strong>第六步：解出和。</strong>当 $q\\ne1$ 时 $1-q\\ne0$，两边除以 $1-q$：")+
 fml("S_n=\\dfrac{a_1(1-q^n)}{1-q}")+
 p("分子分母同乘 $-1$ 得等价形式 $S_n=\\dfrac{a_1(q^n-1)}{q-1}$；与 $a_n=a_1q^{n-1}$ 联立还可写成 $S_n=\\dfrac{a_1-a_n q}{1-q}$。"))+
 exa(p("<strong>例：</strong>等比数列 $a_1=1$，$q=2$，求 $S_5$。由公式")+
 fml("S_5=\\dfrac{1\\times(1-2^5)}{1-2}=\\dfrac{1-32}{-1}=31")+
 p("直接相加验证：$1+2+4+8+16=31$，一致。"))+
 note(p("使用求和公式时<strong>必须先判断 $q$ 是否为 1</strong>：$q=1$ 时 $\\dfrac{a_1(1-q^n)}{1-q}$ 的分母为零、无意义，需单独按 $S_n=na_1$ 计算。这是等比求和最常见的失分点。"))
)
},
{"id":"e4s2-2","name":"无穷等比级数与递推","tags":["def","thm","der","app"],"brief":"无穷递缩等比数列求和、一阶线性递推化归与循环小数化分数。",
"body":wrap(
 defn("无穷等比级数",p("当等比数列的公比满足 $|q|<1$ 时，称它为<strong>无穷递缩等比数列</strong>；其前 $n$ 项和 $S_n$ 当 $n\\to\\infty$ 时的极限，称为该<strong>无穷等比数列各项之和</strong>，记作 $S=a_1+a_2+a_3+\\cdots$。"))+
 thm("无穷等比求和",p("当 $|q|<1$ 时")+
 fml("S=\\dfrac{a_1}{1-q}"))+
 thm("一阶线性递推化归",p("形如 $a_{n+1}=p\\,a_n+q\\ (p\\ne1)$ 的递推关系，可通过待定常数化为等比数列求解。"))+
 der(p("<strong>（一）无穷求和推导。</strong>由等比前 $n$ 项和拆项：")+
 fml("S_n=\\dfrac{a_1(1-q^n)}{1-q}=\\dfrac{a_1}{1-q}-\\dfrac{a_1}{1-q}\\,q^{n}")+
 p("当 $|q|<1$ 时，随着 $n$ 无限增大，$q^n$ 无限趋于 $0$：")+
 fml("\\lim_{n\\to\\infty} q^{n}=0\\quad(|q|<1)")+
 p("于是 $\\dfrac{a_1}{1-q}q^{n}\\to0$，$S_n\\to\\dfrac{a_1}{1-q}$，故无穷等比数列各项之和 $S=\\dfrac{a_1}{1-q}$。当 $|q|\\ge1$ 时 $q^n$ 不趋于 $0$，级数发散、无有限和。")+
 p("<strong>（二）递推化归推导（待定系数法）。</strong>对 $a_{n+1}=p\\,a_n+q$，设想存在常数 $c$ 使递推写成等比形式")+
 fml("a_{n+1}-c=p\\,(a_n-c)")+
 p("展开右端并与原式比较：$a_{n+1}=p\\,a_n+(1-p)c$，与 $a_{n+1}=p\\,a_n+q$ 逐项比较得 $(1-p)c=q$。因 $p\\ne1$，解得")+
 fml("c=\\dfrac{q}{1-p}")+
 p("令 $b_n=a_n-c$，则 $b_{n+1}=p\\,b_n$，$\\{b_n\\}$ 是公比为 $p$ 的等比数列，故")+
 fml("b_n=(a_1-c)\\,p^{\\,n-1}\\ \\Longrightarrow\\ a_n=c+(a_1-c)\\,p^{\\,n-1}")+
 p("<strong>（三）循环小数化分数。</strong>把 $0.\\dot{3}=0.333\\ldots$ 看作无穷等比数列之和，首项 $a_1=\\dfrac{3}{10}$，公比 $q=\\dfrac{1}{10}$，$|q|<1$，故")+
 fml("0.\\dot{3}=\\dfrac{3/10}{1-1/10}=\\dfrac{3}{10}\\times\\dfrac{10}{9}=\\dfrac{1}{3}"))+
 app(p("<strong>应用：</strong>几何概型中的无限分形（如科赫雪花、反复取半的线段）的面积或长度，均可用无穷递缩等比数列求和公式计算，体现「无限次的有限操作之和却是有限值」的思想。"))+
 exa(p("<strong>例：</strong>数列满足 $a_1=1$，$a_{n+1}=2a_n+3$，求通项。此处 $p=2,q=3$，$c=\\dfrac{3}{1-2}=-3$，故 $b_n=a_n+3$ 是公比 $2$ 的等比数列，$b_1=4$，得 $b_n=4\\cdot2^{\\,n-1}=2^{\\,n+1}$，进而 $a_n=2^{\\,n+1}-3$。验证：$a_2=2\\times1+3=5=2^{3}-3$，正确。"))
)
}
]},
{"name":"4.3 数列求和方法","color":"#ea580c","desc":"公式法、倒序相加、错位相减、裂项相消、分组、并项、累加与累乘",
"items":[
{"id":"e4s3-1","name":"裂项相消法","tags":["def","thm","der","exa"],"brief":"裂项恒等式的推导与裂项相消求和的一般方法。",
"body":wrap(
 defn("裂项相消法",p("把数列的每一项拆成两项（或多个部分）之差，使求和时前一项的后部与后一项的前部成对抵消，只剩首末有限几项，从而求得 $S_n$ 的方法，称为<strong>裂项相消法</strong>。"))+
 thm("基本裂项恒等式",p("")+
 fml("\\dfrac{1}{n(n+1)}=\\dfrac{1}{n}-\\dfrac{1}{n+1}")+
 fml("\\dfrac{1}{n(n+k)}=\\dfrac{1}{k}\\left(\\dfrac{1}{n}-\\dfrac{1}{n+k}\\right)\\ (k\\ne0)")+
 fml("\\dfrac{1}{\\sqrt{n}+\\sqrt{n+1}}=\\sqrt{n+1}-\\sqrt{n}"))+
 der(p("<strong>（一）推导第一式。</strong>右端通分：")+
 fml("\\dfrac{1}{n}-\\dfrac{1}{n+1}=\\dfrac{(n+1)-n}{n(n+1)}=\\dfrac{1}{n(n+1)}")+
 p("故恒等式成立（$n\\ne0,-1$）。")+
 p("<strong>（二）推导一般式。</strong>对 $k\\ne0$，")+
 fml("\\dfrac{1}{k}\\left(\\dfrac{1}{n}-\\dfrac{1}{n+k}\\right)=\\dfrac{1}{k}\\cdot\\dfrac{(n+k)-n}{n(n+k)}=\\dfrac{1}{k}\\cdot\\dfrac{k}{n(n+k)}=\\dfrac{1}{n(n+k)}")+
 p("它把分母为「两项之差恰为 $k$」的分式拆成便于相消的两项。")+
 p("<strong>（三）由裂项恒等式求和。</strong>取 $k=1$：")+
 fml("S_n=\\sum_{k=1}^{n}\\dfrac{1}{k(k+1)}=\\sum_{k=1}^{n}\\left(\\dfrac{1}{k}-\\dfrac{1}{k+1}\\right)")+
 p("把和式逐项写出，可见每个 $-\\dfrac{1}{k+1}$ 与下一项 $+\\dfrac{1}{k+1}$ 相消：")+
 fml("S_n=\\left(\\dfrac11-\\dfrac12\\right)+\\left(\\dfrac12-\\dfrac13\\right)+\\cdots+\\left(\\dfrac1n-\\dfrac1{n+1}\\right)")+
 p("中间全部抵消，仅剩首项 $1$ 与末项 $-\\dfrac{1}{n+1}$：")+
 fml("S_n=1-\\dfrac{1}{n+1}=\\dfrac{n}{n+1}")+
 p("<strong>（四）根式裂项。</strong>分子有理化：")+
 fml("\\dfrac{1}{\\sqrt{n}+\\sqrt{n+1}}=\\dfrac{\\sqrt{n+1}-\\sqrt{n}}{(n+1)-n}=\\sqrt{n+1}-\\sqrt{n}")+
 p("求和得 $\\sum_{k=1}^{n}(\\sqrt{k+1}-\\sqrt{k})=\\sqrt{n+1}-\\sqrt{1}=\\sqrt{n+1}-1$。"))+
 exa(p("<strong>例：</strong>求 $\\sum_{k=1}^{99}\\dfrac{1}{k(k+1)}$。由公式")+
 fml("\\sum_{k=1}^{99}\\dfrac{1}{k(k+1)}=1-\\dfrac{1}{100}=\\dfrac{99}{100}"))+
 note(p("裂项相消的关键是「配成差值」：若分母两因子之差为 $k\\ne1$，须在整体前乘系数 $\\dfrac{1}{k}$ 才配平；若分子恰为分母两因子之差，则可直接裂项。求后应核对首尾各剩下哪些项——通常不是首尾各一项，须仔细数清。"))
)
},
{"id":"e4s3-2","name":"错位相减法","tags":["def","thm","der","exa"],"brief":"等差乘等比型数列求和的错位相减推导与一般公式。",
"body":wrap(
 defn("错位相减法",p("当通项形如 $b_n=a_n\\,c_n$，其中 $\\{a_n\\}$ 为等差数列、$\\{c_n\\}$ 为等比数列时，将和式 $S_n$ 乘以该等比数列的公比 $q$，再把两式错位相减，消去中间同底数的幂项，这种方法称为<strong>错位相减法</strong>。"))+
 thm("等差 $\\times$ 等比型求和",p("设 $S_n=\\sum_{k=1}^{n}k\\,q^{k}\\ (q\\ne1)$，则")+
 fml("S_n=\\dfrac{q-(n+1)q^{n+1}+n q^{n+2}}{(1-q)^2}")+
 p("一般地，若 $a_n=a_1+(n-1)d$，则 $S_n=\\sum_{k=1}^{n}a_k q^{k-1}$ 亦可用同样的错位相减逐项消去求得。"))+
 der(p("<strong>第一步：写出和式并乘公比。</strong>")+
 fml("S_n=1\\cdot q+2\\cdot q^2+3\\cdot q^3+\\cdots+n\\,q^{n}\\quad\\text{①}")+
 fml("qS_n=1\\cdot q^2+2\\cdot q^3+\\cdots+(n-1)q^{n}+n\\,q^{n+1}\\quad\\text{②}")+
 p("② 就是把①整体「向左错一位」（各项指数 $+1$），末项多出 $n q^{n+1}$。")+
 p("<strong>第二步：①$-$②，逐项相消。</strong>注意 $q^k$ 的系数在①中是 $k$、在②中是 $k-1$，相减后系数为 $1$：")+
 fml("(1-q)S_n=1\\cdot q+(2-1)q^2+(3-2)q^3+\\cdots+\\big(n-(n-1)\\big)q^{n}-n q^{n+1}")+
 p("即中间各项系数全变成 $1$，剩下一个等比片段：")+
 fml("(1-q)S_n=q+q^2+q^3+\\cdots+q^{n}-n q^{n+1}")+
 p("<strong>第三步：对剩下的等比部分求和。</strong>前面是首项 $q$、公比 $q$、共 $n$ 项的等比数列：")+
 fml("q+q^2+\\cdots+q^{n}=\\dfrac{q(1-q^{n})}{1-q}")+
 p("代入即得")+
 fml("(1-q)S_n=\\dfrac{q(1-q^{n})}{1-q}-n q^{n+1}")+
 p("<strong>第四步：解出 $S_n$。</strong>两边除以 $1-q$（$q\\ne1$）并通分：")+
 fml("S_n=\\dfrac{q(1-q^{n})}{(1-q)^2}-\\dfrac{n q^{n+1}}{1-q}=\\dfrac{q-(n+1)q^{n+1}+n q^{n+2}}{(1-q)^2}"))+
 exa(p("<strong>例：</strong>求 $S_n=1\\cdot2+2\\cdot2^2+3\\cdot2^3+\\cdots+n\\cdot2^n$（$q=2$）。代入公式（因 $(1-2)^2=1$）：")+
 fml("S_n=2-(n+1)2^{n+1}+n\\,2^{n+2}=(n-1)2^{n+1}+2")+
 p("验证 $n=3$：直接相加 $2+8+24=34$；公式给出 $(3-1)2^{4}+2=32+2=34$，一致。"))+
 note(p("错位相减务必注意三点：①乘公比后各项指数整体平移，末项指数最高；②相减后中间系数应都化为相同值（等差型为公差 $d$，本例 $d=1$）；③最后按 $q=1$ 与 $q\\ne1$ 分类，$q=1$ 时回退为等差求和 $S_n=na_1$。"))
)
},
{"id":"e4s3-3","name":"倒序相加与分组求和","tags":["def","thm","der","exa"],"brief":"对称型数列倒序相加与通项分组求和的推导。",
"body":wrap(
 defn("倒序相加法",p("若数列与首末等距的两项之和为常数（即 $a_k+a_{n+1-k}=$ 常数），则可把 $S_n$ 正写、倒写两式相加，一次配成若干对常数之和，这种方法称为<strong>倒序相加法</strong>。"))+
 defn("分组求和法",p("若通项可分解为若干个易求和数列之和（差），即 $a_n=b_n\\pm c_n\\pm\\cdots$，则 $S_n=\\sum b_n\\pm\\sum c_n\\pm\\cdots$，分别套用已知公式再合并，这种方法称为<strong>分组求和法</strong>。"))+
 thm("倒序相加",p("首末等距项之和恒为常数的数列，其前 $n$ 项和为 $S_n=\\dfrac{n\\times(\\text{每对之和})}{2}$。"))+
 der(p("<strong>（一）倒序相加推导 $\\sum_{k=1}^{n}k$。</strong>设 $S=1+2+\\cdots+n$ ①，倒序写 $S=n+(n-1)+\\cdots+1$ ②。①$+$② 按位置配对：")+
 fml("2S=(1+n)+(2+n-1)+\\cdots+(n+1)=\\underbrace{(n+1)+\\cdots+(n+1)}_{n\\ \\text{个}}")+
 p("故 $2S=n(n+1)$，即")+
 fml("\\sum_{k=1}^{n}k=\\dfrac{n(n+1)}{2}")+
 p("<strong>（二）更一般的对称配对。</strong>对满足 $a_k+a_{n+1-k}=c$（常数）的数列，正倒两式相加得 $2S_n=nc$，故 $S_n=\\dfrac{nc}{2}$。这正是等差数列求和公式的来源。")+
 p("<strong>（三）分组求和的推导。</strong>设 $a_n=b_n+c_n$，由加法结合律与交换律：")+
 fml("S_n=\\sum_{k=1}^{n}(b_k+c_k)=\\sum_{k=1}^{n}b_k+\\sum_{k=1}^{n}c_k")+
 p("以 $a_n=2^{n}+n$ 为例，分别求两部分：")+
 fml("\\sum_{k=1}^{n}2^{k}=\\dfrac{2(2^{n}-1)}{2-1}=2^{n+1}-2,\\qquad \\sum_{k=1}^{n}k=\\dfrac{n(n+1)}{2}")+
 p("合并得")+
 fml("S_n=2^{n+1}-2+\\dfrac{n(n+1)}{2}"))+
 exa(p("<strong>例：</strong>求 $1+2+\\cdots+100$。倒序相加：$2S=(1+100)+(2+99)+\\cdots+(100+1)=101\\times100$，故 $S=5050$。"))+
 note(p("分组求和适用于通项是「多段拼接」的情形，如 $a_n=2^n+3n-1$ 型；其可行前提是每一子数列都能用已有公式（等差、等比或本章其他方法）求和。"))
)
},
{"id":"e4s3-4","name":"公式法与并项求和法","tags":["def","thm","der","exa"],"brief":"幂和公式的裂项法推导与并项（含奇偶分类）求和。",
"body":wrap(
 defn("公式法",p("直接套用已知的求和公式计算 $S_n$ 的方法，称为<strong>公式法</strong>。常用幂和公式见下，其中 $\\sum_{k=1}^{n}$ 简记为 $\\sum$。"))+
 thm("常用幂和公式",p("")+
 fml("\\sum_{k=1}^{n}k=\\dfrac{n(n+1)}{2},\\quad \\sum_{k=1}^{n}k^{2}=\\dfrac{n(n+1)(2n+1)}{6},\\quad \\sum_{k=1}^{n}k^{3}=\\left[\\dfrac{n(n+1)}{2}\\right]^{2}"))+
 defn("并项求和法",p("当数列相邻若干项之和为常数或易于计算时，把相邻项两两（或若干项一组）合并后再求和，这种方法称为<strong>并项求和法</strong>。"))+
 der(p("<strong>（一）平方和公式的推导（裂项累加）。</strong>取恒等式")+
 fml("(k+1)^3-k^3=3k^2+3k+1")+
 p("对 $k=1,2,\\ldots,n$ 累加，左端裂项相消仅剩 $(n+1)^3-1$：")+
 fml("(n+1)^3-1=3\\sum k^2+3\\sum k+n")+
 p("代入 $\\sum k=\\dfrac{n(n+1)}{2}$，解出 $\\sum k^2$：")+
 fml("\\sum k^2=\\dfrac{1}{3}\\left[(n+1)^3-1-\\dfrac{3n(n+1)}{2}-n\\right]=\\dfrac{n(n+1)(2n+1)}{6}")+
 p("<strong>（二）立方和公式的推导。</strong>取恒等式")+
 fml("(k+1)^4-k^4=4k^3+6k^2+4k+1")+
 p("对 $k=1,\\ldots,n$ 累加，左端仅剩 $(n+1)^4-1$：")+
 fml("(n+1)^4-1=4\\sum k^3+6\\sum k^2+4\\sum k+n")+
 p("把已知的 $\\sum k$、$\\sum k^2$ 代入即可解得 $\\sum k^3=\\dfrac{n^2(n+1)^2}{4}=\\left[\\dfrac{n(n+1)}{2}\\right]^2$。")+
 p("<strong>（三）并项求和推导（含奇偶分类）。</strong>求和 $S_n=1-2+3-4+\\cdots+(-1)^{n+1}n$。当 $n$ 为偶数时两两并项：")+
 fml("S_n=(1-2)+(3-4)+\\cdots+\\big((n-1)-n\\big)=\\underbrace{(-1)+\\cdots+(-1)}_{n/2\\ \\text{个}}=-\\dfrac{n}{2}")+
 p("当 $n$ 为奇数时，先并前 $n-1$ 项（偶数项），再加末项：")+
 fml("S_n=-\\dfrac{n-1}{2}+n=\\dfrac{n+1}{2}")+
 p("综上 $S_n=-\\dfrac{n}{2}$（$n$ 为偶数），$S_n=\\dfrac{n+1}{2}$（$n$ 为奇数）。并项法必须按 $n$ 的奇偶分类讨论。"))+
 exa(p("<strong>例 1：</strong>求 $S_{10}=1^2+2^2+\\cdots+10^2$，由平方和公式 $S_{10}=\\dfrac{10\\times11\\times21}{6}=385$。")+
 p("<strong>例 2：</strong>求 $S=1-2+3-4+\\cdots-2020+2021$。$n=2021$ 为奇数，$S=\\dfrac{2021+1}{2}=1011$。"))+
 note(p("幂和公式的推导本质都是「找一个相邻差能裂项的恒等式」再累加，这是求和公式的通用生成方式；并项法的核心是「先并项、再按奇偶分类」，切勿在 $n$ 的奇偶未定时就武断合并。"))
)
},
{"id":"e4s3-5","name":"累加法与累乘法求通项","tags":["def","thm","der","exa"],"brief":"由相邻差累加、相邻比累乘求通项公式的严格推导。",
"body":wrap(
 defn("累加法",p("若数列满足 $a_{n+1}-a_n=f(n)$（相邻差可求和），则把 $n-1$ 个相邻差等式相加，中间的 $a_2,\\ldots,a_{n-1}$ 两两抵消，从而得到通项，这种方法称为<strong>累加法</strong>。"))+
 defn("累乘法",p("若数列满足 $\\dfrac{a_{n+1}}{a_n}=g(n)$ 且 $a_n\\ne0$（相邻比可求积），则把 $n-1$ 个相邻比等式相乘，中间因子逐项约去，从而得到通项，这种方法称为<strong>累乘法</strong>。"))+
 thm("累加法公式",p("若 $a_{n+1}-a_n=f(n)$，则")+
 fml("a_n=a_1+\\sum_{k=1}^{\\,n-1}f(k)\\quad(n\\ge2)"))+
 thm("累乘法公式",p("若 $\\dfrac{a_{n+1}}{a_n}=g(n)$ 且 $a_n\\ne0$，则")+
 fml("a_n=a_1\\prod_{k=1}^{\\,n-1}g(k)\\quad(n\\ge2)"))+
 der(p("<strong>（一）累加法推导。</strong>由 $a_{k+1}-a_k=f(k)$ 依次取 $k=1,2,\\ldots,n-1$，写出 $n-1$ 个等式：")+
 fml("a_2-a_1=f(1),\\ \\ a_3-a_2=f(2),\\ \\ \\ldots,\\ \\ a_n-a_{n-1}=f(n-1)")+
 p("左右分别相加，左端中间项两两抵消仅剩 $a_n-a_1$：")+
 fml("a_n-a_1=\\sum_{k=1}^{\\,n-1}f(k)")+
 p("故 $a_n=a_1+\\sum_{k=1}^{\\,n-1}f(k)$；若 $f(k)$ 为等差或等比数列，即可用本章求和法算出右端的和。")+
 p("<strong>（二）累乘法推导。</strong>由 $\\dfrac{a_{k+1}}{a_k}=g(k)$ 依次取 $k=1,\\ldots,n-1$：")+
 fml("\\dfrac{a_2}{a_1}=g(1),\\ \\ \\dfrac{a_3}{a_2}=g(2),\\ \\ \\ldots,\\ \\ \\dfrac{a_n}{a_{n-1}}=g(n-1)")+
 p("左右分别相乘，左端分子分母逐项约去（$a_2,\\ldots,a_{n-1}$ 全部消去），仅剩 $\\dfrac{a_n}{a_1}$：")+
 fml("\\dfrac{a_n}{a_1}=\\prod_{k=1}^{\\,n-1}g(k)")+
 p("故 $a_n=a_1\\prod_{k=1}^{\\,n-1}g(k)$，其中每个 $g(k)$ 非零保证乘积有意义。"))+
 exa(p("<strong>例 1（累加）：</strong>$a_1=1$，$a_{n+1}=a_n+2n$，求 $a_n$。由累加公式")+
 fml("a_n=1+\\sum_{k=1}^{\\,n-1}2k=1+2\\cdot\\dfrac{(n-1)n}{2}=n^2-n+1")+
 p("$n=1$ 时 $a_1=1$ 也满足该式，故通项对一切 $n\\ge1$ 成立。")+
 p("<strong>例 2（累乘）：</strong>$a_1=1$，$\\dfrac{a_{n+1}}{a_n}=\\dfrac{n+1}{n}$，求 $a_n$。由累乘公式")+
 fml("a_n=1\\cdot\\prod_{k=1}^{\\,n-1}\\dfrac{k+1}{k}=\\dfrac{2}{1}\\cdot\\dfrac{3}{2}\\cdots\\dfrac{n}{n-1}=n")+
 p("验证：$a_1=1$，$a_2=a_1\\cdot\\dfrac{2}{1}=2$，与 $a_n=n$ 一致。"))+
 note(p("累加法的关键是右端 $\\sum f(k)$ 必须可算；累乘法只适用于相邻<strong>比</strong>已知且规律的情形。当递推为 $a_{n+1}=p a_n+q$ 这类时，应优先用待定系数法化为等比（见 4.2 节）。"))
)
}
]}
]
# ============ 第五章 平面几何 ============
# ============ 第五章 平面几何 ============
ch5_sections = [
{"name":"5.1 平行线","color":"#be185d","desc":"平行公理、平行线的判定与性质、平行线间距离",
"items":[
{"id":"e5s1-1","name":"平行线的判定与性质","tags":["def","thm","der","exa"],"brief":"平行公理、三线八角的判定与性质定理、平行线间距离。",
"body":wrap(
 defn("平行线",p("在同一平面内不相交的两条直线称为<strong>平行线</strong>，记作 $a\\parallel b$。两条直线被第三条直线所截，在截线同旁、被截线同侧的角称<strong>同位角</strong>，在截线两侧、两被截线之间的角称<strong>内错角</strong>，在截线同旁、两被截线之间的角称<strong>同旁内角</strong>，它们合称三线八角。"))+
 thm("平行公理",p("过直线外一点，有且只有一条直线与这条直线平行。由此可得<strong>平行公理的推论</strong>：平行于同一条直线的两条直线互相平行（平行的传递性）。"))+
 thm("平行线的判定定理",p("两条直线被第三条直线所截，若满足下列条件之一：①同位角相等；②内错角相等；③同旁内角互补——则这两条直线平行。"))+
 thm("平行线的性质定理",p("若两条平行直线被第三条直线所截，则同位角相等、内错角相等、同旁内角互补。"))+
 der(p("<strong>第一步，先证性质（内错角相等）。</strong>设 $a\\parallel b$，$c$ 为截线，内错角 $\\angle1$ 与 $\\angle2$。取 $\\angle1$ 的同位角 $\\angle3$。由「两直线平行，同位角相等」得：")+
 fml("\\angle1=\\angle3")+
 p("又 $\\angle2$ 与 $\\angle3$ 是对顶角，对顶角相等，故 $\\angle3=\\angle2$。由等量代换得 $\\angle1=\\angle2$。同旁内角互补亦同理：内错角之和与其邻补角之和为平角 $\\pi$。")+
 fml("\\angle1=\\angle2,\\qquad \\angle1+\\angle4=\\pi")+
 p("<strong>第二步，再证判定（同位角相等则平行）。</strong>用反证法。设 $a,b$ 被 $c$ 所截，同位角 $\\angle1=\\angle2$。若 $a$ 与 $b$ 不平行，则它们相交于一点 $P$，与截线 $c$ 围成一个三角形。此时 $\\angle2$ 是该三角形的一个外角，$\\angle1$ 是与它不相邻的内角。由三角形外角定理（外角大于任一不相邻的内角）必成立 $\\angle2>\\angle1$，与 $\\angle1=\\angle2$ 矛盾。故反设不成立，$a\\parallel b$。")+
 p("<strong>第三步，证平行线间距离为定值。</strong>两平行线间距离定义为一条直线上任一点到另一条直线的垂线段长。在 $a$ 上取两点 $A,B$，过 $A,B$ 分别向 $b$ 作垂线，垂足为 $A',B'$。由 $AA'\\perp b$、$BB'\\perp b$ 得 $AA'\\parallel BB'$，又 $AB\\parallel A'B'$，故四边形 $AA'B'B$ 是平行四边形；再由 $\\angle AA'B'=\\dfrac{\\pi}{2}$ 知它是矩形，于是 $AA'=BB'$。这说明距离与取点无关，是定值。")+
 fml("d(A,b)=d(B,b)=|AA'|=|BB'|"))+
 exa(p("<strong>例：</strong>若一对内错角 $\\angle1=\\angle2=60^\\circ$，则两被截直线平行；反之若两直线平行，同旁内角 $\\angle1,\\angle4$ 满足 $\\angle1+\\angle4=180^\\circ$，当 $\\angle1=60^\\circ$ 时得 $\\angle4=120^\\circ$。")))
}
]},
{"name":"5.2 三角形","color":"#be185d","desc":"三角形内角和、正余弦定理、面积公式与四心",
"items":[
{"id":"e5s2-1","name":"三角形内角和与面积","tags":["def","thm","der","exa"],"brief":"三角形内角和定理、面积公式的多种形式。",
"fig":"triangle","figCap":"三角形 ABC，底边 a 与高 h",
"body":wrap(
 defn("三角形",p("由三条线段首尾顺次相接所组成的封闭图形称为<strong>三角形</strong>。按角可分为锐角、直角、钝角三角形；按边可分为不等边、等腰、等边三角形。三边 $a,b,c$ 所对的角分别记为 $A,B,C$。"))+
 thm("内角和定理",p("三角形三个内角的和等于 $\\pi$（即 $180^\\circ$）。")+
 fml("A+B+C=\\pi"))+
 der(p("<strong>第一步，作辅助线。</strong>过顶点 $A$ 作直线 $l\\parallel BC$。由平行线内错角相等，$l$ 在 $AB$ 一侧与 $AB$ 所成的角等于 $\\angle B$，在 $AC$ 一侧与 $AC$ 所成的角等于 $\\angle C$。")+
 fml("\\angle(l,AB)=\\angle B,\\qquad \\angle(AC,l)=\\angle C")+
 p("<strong>第二步，拼成平角。</strong>因 $A$ 在直线 $l$ 上，在顶点 $A$ 处，$\\angle B$、$\\angle A$、$\\angle C$ 恰好依次拼合，占据 $l$ 上方的一个平角：")+
 fml("\\angle B+\\angle A+\\angle C=\\pi")+
 p("<strong>第三步，得出底高面积公式。</strong>以 $a$ 为底、$h$ 为高，三角形面积等于同底等高的矩形面积之半，得 $S=\\dfrac12 ah$。再把 $b$ 视为斜边、$b$ 与 $a$ 的夹角为 $C$，则高 $h=b\\sin C$，代入得夹角公式。")+
 fml("S=\\dfrac12 ah=\\dfrac12 ab\\sin C")+
 p("<strong>第四步，导出内切圆半径公式。</strong>设内切圆半径为 $r$，圆心 $I$ 到三边距离均为 $r$，把 $\\triangle ABC$ 分成三个高均为 $r$ 的小三角形：")+
 fml("S=\\dfrac12 ar+\\dfrac12 br+\\dfrac12 cr=\\dfrac12(a+b+c)r=pr"))+
 thm("面积公式汇总",p("")+
 fml("S=\\dfrac12 ah=\\dfrac12 ab\\sin C=pr=\\sqrt{p(p-a)(p-b)(p-c)}")+
 fml("p=\\dfrac{a+b+c}{2}\\text{（半周长）}"))+
 exa(p("<strong>例：</strong>$a=3,b=4,C=60^\\circ$，则 $S=\\dfrac12\\cdot3\\cdot4\\cdot\\dfrac{\\sqrt3}{2}=3\\sqrt3$。若内切圆半径 $r=1$，由 $S=pr$ 得半周长 $p=3\\sqrt3$，故周长 $a+b+c=2p=6\\sqrt3$。")))
},
{"id":"e5s2-2","name":"正弦定理与余弦定理","tags":["def","thm","der","exa"],"brief":"正弦定理、余弦定理及其严格证明，解三角形应用。",
"body":wrap(
 thm("正弦定理",p("在 $\\triangle ABC$ 中，各边与它所对角的正弦之比都相等，且等于外接圆的直径 $2R$：")+
 fml("\\dfrac{a}{\\sin A}=\\dfrac{b}{\\sin B}=\\dfrac{c}{\\sin C}=2R"))+
 thm("余弦定理",p("三角形任一边的平方，等于另两边的平方和减去这两边与其夹角余弦之积的两倍：")+
 fml("a^2=b^2+c^2-2bc\\cos A"))+
 der(p("<strong>正弦定理的严格证明（外接圆法）：</strong>设 $\\triangle ABC$ 的外接圆半径为 $R$，圆心为 $O$，先证边 $c=AB$ 与其对角 $C$ 的关系。")+
 p("<strong>情形一：</strong>$C$ 为锐角。连接 $AO$ 并延长交外接圆于点 $D$，则 $AD=2R$ 为直径。由「直径所对的圆周角是直角」得 $\\angle ABD=90^\\circ$；又圆周角 $\\angle ADB$ 与 $\\angle ACB$ 同对弧 $AB$，故 $\\angle ADB=\\angle C$。于是在直角三角形中：")+
 fml("c=AB=AD\\sin\\angle ADB=2R\\sin C")+
 p("<strong>情形二：</strong>$C$ 为直角。此时 $AB$ 为直径，$c=2R=2R\\sin90^\\circ=2R\\sin C$，式子仍成立。")+
 p("<strong>情形三：</strong>$C$ 为钝角。圆内接四边形对角互补，故 $\\angle ADB=\\pi-C$，于是 $\\sin\\angle ADB=\\sin(\\pi-C)=\\sin C$，同样得 $c=2R\\sin C$。")+
 p("三种情形统一为 $c=2R\\sin C$。对边 $a,b$ 重复同样的论证，即得正弦定理。")+
 fml("\\dfrac{a}{\\sin A}=\\dfrac{b}{\\sin B}=\\dfrac{c}{\\sin C}=2R")+
 p("<strong>余弦定理的严格证明（坐标法）：</strong>以 $A$ 为原点，射线 $AB$ 为 $x$ 轴正方向建立平面直角坐标系，则 $B(c,0)$。因 $AC=b$ 且 $AC$ 与 $x$ 轴正方向的夹角为 $A$，故 $C(b\\cos A,\\ b\\sin A)$。边 $a=BC$ 的平方等于两点间距离的平方：")+
 fml("a^2=(b\\cos A-c)^2+(b\\sin A-0)^2")+
 p("展开并利用 $\\sin^2A+\\cos^2A=1$：")+
 fml("a^2=b^2\\cos^2A-2bc\\cos A+c^2+b^2\\sin^2A=b^2+c^2-2bc\\cos A")+
 p("证毕。另两边同理可得 $b^2=c^2+a^2-2ca\\cos B$、$c^2=a^2+b^2-2ab\\cos C$。"))+
 app(p("<strong>推论（勾股定理及其逆定理）：</strong>当 $A=\\dfrac{\\pi}{2}$ 时 $\\cos A=0$，余弦定理退化为 $a^2=b^2+c^2$，即勾股定理。反之，若 $a^2=b^2+c^2$，由余弦定理得 $\\cos A=0$，故 $A=\\dfrac{\\pi}{2}$——这正是勾股定理的逆定理。"))+
 exa(p("<strong>例：</strong>已知 $a=3,b=4,C=60^\\circ$，由余弦定理 $c^2=3^2+4^2-2\\cdot3\\cdot4\\cdot\\cos60^\\circ=9+16-12=13$，故 $c=\\sqrt{13}$。")))
},
{"id":"e5s2-3","name":"海伦公式与中位线定理","tags":["def","thm","der","exa"],"brief":"海伦公式的完整推导与三角形中位线性质。",
"body":wrap(
 thm("海伦公式",p("设 $\\triangle ABC$ 的三边为 $a,b,c$，半周长 $p=\\dfrac{a+b+c}{2}$，则其面积")+
 fml("S=\\sqrt{p(p-a)(p-b)(p-c)}"))+
 thm("三角形中位线定理",p("连接三角形两边中点的线段（中位线）平行于第三边，且等于第三边的一半。"))+
 der(p("<strong>海伦公式的完整推导：</strong>出发点是两边夹角的面积公式与余弦定理。")+
 fml("S=\\dfrac12 ab\\sin C,\\qquad \\cos C=\\dfrac{a^2+b^2-c^2}{2ab}")+
 p("<strong>第一步，把 $\\sin C$ 化为边的表达式。</strong>由 $\\sin^2C=1-\\cos^2C$：")+
 fml("\\sin^2C=1-\\dfrac{(a^2+b^2-c^2)^2}{4a^2b^2}=\\dfrac{4a^2b^2-(a^2+b^2-c^2)^2}{4a^2b^2}")+
 p("<strong>第二步，对分子作平方差分解。</strong>记 $X=a^2+b^2$，则分子 $=(2ab)^2-(X-c^2)^2=(2ab-X+c^2)(2ab+X-c^2)$。分别整理两个因式：")+
 fml("2ab-(a^2+b^2)+c^2=c^2-(a-b)^2=(c+a-b)(c-a+b)")+
 fml("2ab+(a^2+b^2)-c^2=(a+b)^2-c^2=(a+b+c)(a+b-c)")+
 p("<strong>第三步，用半周长改写。</strong>注意 $a+b+c=2p$、$a+b-c=2(p-c)$、$c+a-b=2(p-b)$、$c-a+b=2(p-a)$，故分子为：")+
 fml("4a^2b^2-(a^2+b^2-c^2)^2=16\\,p(p-a)(p-b)(p-c)")+
 p("<strong>第四步，开方得面积。</strong>代入 $\\sin C=\\dfrac{4\\sqrt{p(p-a)(p-b)(p-c)}}{2ab}$，再乘 $\\dfrac12 ab$：")+
 fml("S=\\dfrac12 ab\\cdot\\dfrac{4\\sqrt{p(p-a)(p-b)(p-c)}}{2ab}=\\sqrt{p(p-a)(p-b)(p-c)}")+
 p("<strong>中位线定理的证明：</strong>设 $D,E$ 分别为 $AB,AC$ 的中点，则 $\\dfrac{AD}{AB}=\\dfrac{AE}{AC}=\\dfrac12$，且 $\\angle A$ 为公共角，由 SAS 相似判定：")+
 fml("\\triangle ADE\\sim\\triangle ABC,\\qquad \\text{相似比}=\\dfrac12")+
 p("于是 $\\angle ADE=\\angle ABC$，得 $DE\\parallel BC$；且 $\\dfrac{DE}{BC}=\\dfrac12$，即 $DE=\\dfrac12 BC$。证毕。"))+
 exa(p("<strong>例：</strong>$a=3,b=4,c=5$，$p=6$，则 $S=\\sqrt{6\\cdot3\\cdot2\\cdot1}=\\sqrt{36}=6$。若 $D,E$ 为 $AB,AC$ 中点且 $BC=5$，则 $DE=2.5$ 且 $DE\\parallel BC$。")))
},
{"id":"e5s2-4","name":"三角形的四心","tags":["def","thm","der","exa"],"brief":"重心、内心、外心、垂心的定义、性质与共点性证明。",
"body":wrap(
 defn("重心",p("三角形三条中线的交点称为<strong>重心</strong> $G$。重心将每条中线分成 $2:1$ 两段，即重心到顶点的距离是它到对边中点距离的 $2$ 倍。"))+
 defn("内心",p("三角形三条角平分线的交点称为<strong>内心</strong> $I$。它是内切圆的圆心，到三边距离相等，等于内切圆半径 $r$。"))+
 defn("外心",p("三角形三边垂直平分线的交点称为<strong>外心</strong> $O$。它是外接圆的圆心，到三顶点距离相等，等于外接圆半径 $R$。"))+
 defn("垂心",p("三角形三条高所在直线的交点称为<strong>垂心</strong> $H$。"))+
 der(p("<strong>内心共点性证明：</strong>设 $\\angle B$ 与 $\\angle C$ 的平分线交于点 $I$。由角平分线的性质（角平分线上的点到角两边距离相等），$I$ 到 $BA$、$BC$ 的距离相等；又 $I$ 在 $\\angle C$ 的平分线上，到 $CB$、$CA$ 的距离相等。")+
 fml("d(I,BA)=d(I,BC)=d(I,CA)")+
 p("故 $I$ 到 $AB$、$AC$ 的距离也相等，说明 $I$ 落在 $\\angle A$ 的平分线上。于是三条角平分线共点，且该点到三边等距，是内切圆的圆心。")+
 p("<strong>外心共点性证明：</strong>设 $AB$、$BC$ 的垂直平分线交于点 $O$。由线段垂直平分线的性质（到线段两端距离相等）：")+
 fml("OA=OB,\\qquad OB=OC\\;\\Rightarrow\\;OA=OC")+
 p("故 $O$ 到 $A,C$ 等距，落在 $AC$ 的垂直平分线上，三条垂直平分线共点。又 $OA=OB=OC$，故 $O$ 为外接圆的圆心。")+
 p("<strong>重心分中线为 $2:1$ 的证明：</strong>设中线 $AD$ 与 $BE$ 交于 $G$（$D,E$ 为边中点）。取 $AG$ 的中点 $M$、$BG$ 的中点 $N$。在 $\\triangle ABG$ 中 $MN$ 是中位线，在 $\\triangle ABC$ 中 $DE$ 是中位线，故")+
 fml("MN\\parallel AB,\\;MN=\\dfrac12 AB;\\qquad DE\\parallel AB,\\;DE=\\dfrac12 AB")+
 p("于是 $DE\\parallel MN$ 且 $DE=MN$，四边形 $DGMN$ 是平行四边形，从而 $DG=GM$；又 $GM=MA$，得")+
 fml("AG=2\\,GD")+
 p("即重心分中线为 $2:1$。同理第三条中线也过 $G$，三条中线共点。")+
 p("<strong>垂心共点性证明（外心向量法）：</strong>设 $O$ 为外心，取点 $H$ 使 $\\overrightarrow{OH}=\\overrightarrow{OA}+\\overrightarrow{OB}+\\overrightarrow{OC}$。则由 $R=OA$ 得")+
 fml("\\overrightarrow{AH}\\cdot\\overrightarrow{BC}=(\\overrightarrow{OB}+\\overrightarrow{OC})\\cdot(\\overrightarrow{OC}-\\overrightarrow{OB})=|\\overrightarrow{OC}|^2-|\\overrightarrow{OB}|^2=R^2-R^2=0")+
 p("故 $AH\\perp BC$，即 $AH$ 是 $BC$ 边上的高；同理 $BH\\perp CA$、$CH\\perp AB$。三条高共点于 $H$，即垂心。"))+
 note(p("四心的常用关系：内切圆半径 $r=\\dfrac{S}{p}$，外接圆半径 $R=\\dfrac{abc}{4S}=\\dfrac{a}{2\\sin A}$；直角三角形的外心在斜边中点、垂心为直角顶点；等边三角形四心重合。外心 $O$、重心 $G$、垂心 $H$ 三点共线（欧拉线），且 $OG:GH=1:2$。"))+
 exa(p("<strong>例：</strong>若 $\\triangle ABC$ 的 $S=6$、$p=6$，则 $r=\\dfrac{S}{p}=1$；若 $abc=60$，则 $R=\\dfrac{60}{4\\cdot6}=2.5$。")))
}
]},
{"name":"5.3 平行四边形","color":"#db2777","desc":"平行四边形的性质、判定与面积",
"items":[
{"id":"e5s3-1","name":"平行四边形","tags":["def","thm","der","exa"],"brief":"平行四边形的性质、判定定理与面积公式。",
"fig":"parallelogram","figCap":"平行四边形 ABCD，底 a 与高 h",
"body":wrap(
 defn("平行四边形",p("两组对边分别平行的四边形称为<strong>平行四边形</strong>。"))+
 thm("性质定理",p("在平行四边形 $ABCD$ 中：①两组对边分别平行且相等；②对角相等、邻角互补；③两条对角线互相平分；④是中心对称图形，对称中心为对角线交点。"))+
 thm("判定定理",p("满足下列任一条件的四边形是平行四边形：①两组对边分别平行；②两组对边分别相等；③一组对边平行且相等；④两条对角线互相平分。"))+
 der(p("<strong>对边相等与对角相等的证明：</strong>连接对角线 $AC$。由 $AB\\parallel CD$、$AD\\parallel BC$ 得内错角 $\\angle BAC=\\angle DCA$、$\\angle BCA=\\angle DAC$，又 $AC$ 公共，由 ASA 得：")+
 fml("\\triangle ABC\\cong\\triangle CDA\\;\\Rightarrow\\;AB=CD,\\;BC=AD,\\;\\angle B=\\angle D")+
 p("<strong>对角线互相平分的证明：</strong>设对角线 $AC,BD$ 交于 $O$。由 $AD\\parallel BC$ 得 $\\angle ADO=\\angle CBO$、$\\angle DAO=\\angle BCO$，又对边 $AD=BC$，由 ASA：")+
 fml("\\triangle AOD\\cong\\triangle COB\\;\\Rightarrow\\;AO=CO,\\;DO=BO")+
 p("即对角线互相平分。反之，若已知 $AO=CO,DO=BO$，且 $\\angle AOD=\\angle COB$ 为对顶角，由 SAS 得 $\\triangle AOD\\cong\\triangle COB$，从而 $AD=BC$ 且 $\\angle ADO=\\angle CBO$，故 $AD\\parallel BC$，四边形是平行四边形——这正是判定④的证明。")+
 p("<strong>面积公式推导：</strong>以 $a$ 为底、$h$ 为高，沿高剪下三角形平移拼接，可把平行四边形补成同底等高的矩形，故面积 $S=ah$。若用邻边 $a,b$ 及其夹角 $\\theta$，则高 $h=b\\sin\\theta$，于是")+
 fml("S=ah=ab\\sin\\theta"))+
 exa(p("<strong>例：</strong>平行四边形两边为 $3,5$，夹角 $30^\\circ$，则 $S=3\\cdot5\\cdot\\sin30^\\circ=7.5$。矩形与菱形都是特殊的平行四边形，自然继承上述一切性质。")))
}]},
{"name":"5.4 矩形","color":"#be185d","desc":"矩形的性质、判定与面积",
"items":[
{"id":"e5s4-1","name":"矩形","tags":["def","thm","der","exa"],"brief":"矩形的性质、判定定理与面积公式。",
"body":wrap(
 defn("矩形",p("有一个角是直角的平行四边形称为<strong>矩形</strong>（长方形）。"))+
 thm("性质定理",p("矩形具有：①平行四边形的一切性质；②四个角都是直角；③两条对角线相等；④既是中心对称图形，又是轴对称图形（两条对称轴为两组对边中点的连线）。"))+
 thm("判定定理",p("①有一个角是直角的平行四边形是矩形；②对角线相等的平行四边形是矩形；③有三个角是直角的四边形是矩形。"))+
 der(p("<strong>对角线相等（性质）的证明：</strong>设矩形 $ABCD$ 中 $\\angle B=90^\\circ$。比较 $\\triangle ABC$ 与 $\\triangle DCB$：$AB=DC$（对边相等），$BC$ 公共，$\\angle ABC=\\angle DCB=90^\\circ$，由 SAS 得：")+
 fml("\\triangle ABC\\cong\\triangle DCB\\;\\Rightarrow\\;AC=DB")+
 p("即矩形的两条对角线相等。")+
 p("<strong>判定②（对角线相等的平行四边形是矩形）的证明：</strong>设平行四边形 $ABCD$ 中 $AC=BD$。由对边相等 $AB=DC$，又 $BC$ 公共，三边对应相等：")+
 fml("AB=DC,\\quad BC=CB,\\quad AC=DB\\;\\Rightarrow\\;\\triangle ABC\\cong\\triangle DCB\\;(\\text{SSS})")+
 p("故 $\\angle ABC=\\angle DCB$。又 $AB\\parallel DC$，同旁内角互补 $\\angle ABC+\\angle DCB=\\pi$，于是")+
 fml("\\angle ABC=\\angle DCB=\\dfrac{\\pi}{2}")+
 p("即有一个角为直角，故为矩形。")+
 fml("S=ab","长乘宽"))+
 exa(p("<strong>例：</strong>矩形长 $4$、宽 $3$，则面积 $S=4\\times3=12$，对角线 $AC=\\sqrt{3^2+4^2}=5$。")))
}]},
{"name":"5.5 菱形","color":"#be185d","desc":"菱形的性质、判定与面积",
"items":[
{"id":"e5s5-1","name":"菱形","tags":["def","thm","der","exa"],"brief":"菱形的性质、判定定理与面积公式。",
"body":wrap(
 defn("菱形",p("有一组邻边相等的平行四边形称为<strong>菱形</strong>。"))+
 thm("性质定理",p("菱形具有：①平行四边形的一切性质；②四条边都相等；③两条对角线互相垂直平分；④每条对角线平分一组对角；⑤既是中心对称图形，又是轴对称图形（两条对称轴为对角线所在直线）。"))+
 thm("判定定理",p("①有一组邻边相等的平行四边形是菱形；②对角线互相垂直的平行四边形是菱形；③四条边都相等的四边形是菱形。"))+
 der(p("<strong>对角线互相垂直的证明：</strong>设菱形 $ABCD$ 中 $AB=AD$。由平行四边形性质，对角线互相平分，设 $AC$ 与 $BD$ 交于 $O$，则 $BO=DO$，即 $O$ 是 $BD$ 的中点。在 $\\triangle ABD$ 中，$AB=AD$，由等腰三角形三线合一定理：")+
 fml("AO\\perp BD,\\qquad AO \\text{ 平分 } \\angle BAD")+
 p("故对角线 $AC\\perp BD$，且 $AC$ 平分对角 $\\angle A$、$\\angle C$；同理 $BD$ 平分 $\\angle B$、$\\angle D$。")+
 p("<strong>面积公式推导：</strong>设两条对角线 $AC=d_1,BD=d_2$，它们互相垂直平分，交点为 $O$，把菱形分成四个全等的直角三角形，每个三角形的两条直角边分别为 $\\dfrac{d_1}{2},\\dfrac{d_2}{2}$：")+
 fml("S=4\\cdot\\dfrac12\\cdot\\dfrac{d_1}{2}\\cdot\\dfrac{d_2}{2}=\\dfrac12 d_1 d_2")+
 p("若用边长 $a$ 与顶角 $\\theta$，也可写成 $S=a^2\\sin\\theta$。"))+
 exa(p("<strong>例：</strong>菱形对角线为 $6,8$，则 $S=\\dfrac12\\times6\\times8=24$；边长 $a=\\sqrt{3^2+4^2}=5$，周长 $=20$。")))
}]},
{"name":"5.6 正方形","color":"#be185d","desc":"正方形的性质、判定与面积",
"items":[
{"id":"e5s6-1","name":"正方形","tags":["def","thm","der","exa"],"brief":"正方形的性质、判定定理与面积公式。",
"body":wrap(
 defn("正方形",p("既是矩形又是菱形的平行四边形称为<strong>正方形</strong>，即有一组邻边相等且有一个角是直角的平行四边形。"))+
 thm("性质定理",p("正方形具有：①矩形和菱形的一切性质；②四条边相等、四个角都是直角；③两条对角线相等、互相垂直平分，且每条对角线平分一组对角（与边成 $45^\\circ$）。"))+
 thm("判定定理",p("①有一组邻边相等的矩形是正方形；②有一个角是直角的菱形是正方形；③对角线互相垂直且相等的平行四边形是正方形。"))+
 der(p("<strong>面积与对角线关系推导：</strong>设正方形边长为 $a$，由矩形面积公式直接得 $S=a^2$。其对角线 $d$ 由勾股定理：")+
 fml("d=\\sqrt{a^2+a^2}=a\\sqrt2")+
 p("反解得 $a=\\dfrac{d}{\\sqrt2}$，代入面积公式：")+
 fml("S=a^2=\\left(\\dfrac{d}{\\sqrt2}\\right)^2=\\dfrac{d^2}{2}")+
 p("这与菱形面积公式 $S=\\dfrac12 d_1d_2$ 一致（此时 $d_1=d_2=d$）。"))+
 exa(p("<strong>例：</strong>正方形边长 $5$，则 $S=25$、对角线 $d=5\\sqrt2$；反之若对角线为 $10$，则 $S=\\dfrac{10^2}{2}=50$。")))
}]},
{"name":"5.7 梯形","color":"#be185d","desc":"梯形的性质、等腰梯形与面积",
"items":[
{"id":"e5s7-1","name":"梯形与中位线定理","tags":["def","thm","der","exa"],"brief":"梯形定义、等腰梯形性质、中位线定理与面积公式。",
"body":wrap(
 defn("梯形",p("一组对边平行、另一组对边不平行的四边形称为<strong>梯形</strong>。平行的两边叫底（上底 $a$、下底 $b$），不平行的两边叫腰，两底之间的距离叫高 $h$。"))+
 defn("等腰梯形",p("两腰相等的梯形称为<strong>等腰梯形</strong>。其性质：两腰相等、同一底上的两个角相等、两条对角线相等、是轴对称图形（对称轴为两底中点的连线）。"))+
 thm("梯形中位线定理",p("连接梯形两腰中点的线段（中位线）平行于两底，且等于两底和的一半。")+
 fml("m=\\dfrac{a+b}{2}"))+
 der(p("<strong>中位线定理的证明（旋转法）：</strong>设梯形 $ABCD$ 中 $AD\\parallel BC$，$M,N$ 分别为腰 $AB,CD$ 的中点。连接 $MN$ 并延长，交 $CB$ 的延长线于 $P$。")+
 p("<strong>第一步，证全等。</strong>由 $AD\\parallel BC$ 得内错角 $\\angle MDN=\\angle MPN$；又 $DN=CN$、$\\angle MND=\\angle PNC$（对顶角），由 ASA：")+
 fml("\\triangle MND\\cong\\triangle PNC\\;\\Rightarrow\\;MN=PN,\\;AD=CP")+
 p("<strong>第二步，证平行且等于两底半和。</strong>此时 $M$ 为 $AP$ 中点、$N$ 为 $MP$ 中点，故 $MN$ 是 $\\triangle ABP$ 的中位线：")+
 fml("MN\\parallel BP\\parallel AD\\parallel BC,\\qquad MN=\\dfrac12 BP")+
 p("而 $BP=BC+CP=BC+AD=a+b$，于是")+
 fml("m=MN=\\dfrac{a+b}{2}")+
 p("<strong>面积公式推导：</strong>用两个全等梯形拼成一个底为 $a+b$、高为 $h$ 的平行四边形，其面积为 $(a+b)h$，故单个梯形面积：")+
 fml("S=\\dfrac{(a+b)h}{2}=mh"))+
 exa(p("<strong>例：</strong>上底 $3$、下底 $7$、高 $4$，则 $S=\\dfrac{(3+7)\\times4}{2}=20$，中位线 $m=\\dfrac{3+7}{2}=5$，且 $S=mh=5\\times4=20$。")))
}]},
{"name":"5.8 圆","color":"#9d174d","desc":"圆的定义、垂径定理、圆心角与圆周角、切线",
"items":[
{"id":"e5s8-1","name":"圆的定义与垂径定理","tags":["def","thm","der","exa"],"brief":"圆的定义、弧弦圆心概念、垂径定理及其逆定理。",
"fig":"circle","figCap":"圆 O 与弦 AB、垂直于弦的直径 CD",
"body":wrap(
 defn("圆",p("平面上到定点（圆心）的距离等于定长（半径）的所有点组成的集合称为<strong>圆</strong>，记作 $\\odot O$，半径记为 $r$。"))+
 defn("弧、弦、圆心角",p("<strong>弧</strong>是圆上两点之间的部分；<strong>弦</strong>是连接圆上两点的线段，经过圆心的弦叫<strong>直径</strong>，是最长的弦；顶点在圆心的角叫<strong>圆心角</strong>。"))+
 thm("垂径定理",p("垂直于弦的直径平分这条弦，并且平分弦所对的两条弧。"))+
 der(p("<strong>垂径定理的证明：</strong>设 $\\odot O$ 半径为 $r$，弦 $AB$，直径 $CD\\perp AB$，垂足为 $E$。连接 $OA,OB$。")+
 p("<strong>第一步，说明等腰。</strong>因 $OA=OB=r$，故 $\\triangle OAB$ 是等腰三角形：")+
 fml("OA=OB=r")+
 p("<strong>第二步，用三线合一。</strong>因 $OE\\perp AB$，即 $OE$ 是等腰 $\\triangle OAB$ 底边上的高，由等腰三角形三线合一定理，它同时是底边上的中线与顶角的平分线：")+
 fml("AE=EB,\\qquad \\angle AOC=\\angle BOC")+
 p("<strong>第三步，得出弧相等。</strong>相等的圆心角所对的弧相等，故直径 $CD$ 同时平分弦 $AB$ 所对的劣弧与优弧。")+
 p("<strong>逆定理（平分弦的直径垂直于弦）：</strong>设直径 $CD$ 交非直径弦 $AB$ 于 $E$ 且 $AE=EB$。由 $OA=OB$ 及 $AE=EB$，知 $OE$ 是等腰 $\\triangle OAB$ 底边上的中线，由三线合一得 $OE\\perp AB$，即 $CD\\perp AB$，同时平分弦 $AB$ 所对的弧。"))+
 note(p("推论：圆的两条平行弦所夹的弧相等；弦的垂直平分线必过圆心；过圆心且平分弦（非直径）的直线垂直于弦。这些可由垂径定理与逆定理直接得到，常用于求弦长与弦心距。"))+
 exa(p("<strong>例：</strong>$\\odot O$ 半径 $5$，弦心距 $OE=3$，则 $AE=\\sqrt{OA^2-OE^2}=\\sqrt{25-9}=4$，弦长 $AB=2\\times4=8$。")))
},
{"id":"e5s8-2","name":"圆心角定理与圆周角定理","tags":["def","thm","der","exa"],"brief":"同弧所对的圆周角等于圆心角的一半及推论。",
"body":wrap(
 defn("圆周角",p("顶点在圆上、并且两边都与圆相交（即两边都是圆的弦）的角称为<strong>圆周角</strong>。"))+
 thm("圆心角定理",p("在同圆或等圆中，圆心角的度数等于它所对弧的度数；相等的圆心角所对的弧相等、所对的弦相等。"))+
 thm("圆周角定理",p("一条弧所对的圆周角等于它所对的圆心角的一半，即等于该弧的度数的一半。")+
 fml("\\angle ACB=\\dfrac12\\angle AOB"))+
 der(p("<strong>圆周角定理的证明（分三种情形）：</strong>设 $\\odot O$ 中弧 $AB$ 所对的圆心角为 $\\angle AOB$，圆周角为 $\\angle ACB$。")+
 p("<strong>情形一：圆心 $O$ 在圆周角的一条边上。</strong>此时 $CA$ 过圆心，$OC=OB=r$，$\\triangle OBC$ 是等腰三角形。由三角形外角定理，外角 $\\angle AOB$ 等于两个不相邻内角之和：")+
 fml("\\angle AOB=\\angle OCB+\\angle OBC=2\\angle OCB")+
 fml("\\Rightarrow\\;\\angle ACB=\\angle OCB=\\dfrac12\\angle AOB")+
 p("<strong>情形二：圆心 $O$ 在圆周角内部。</strong>作直径 $CD$，把圆周角分成两角之和 $\\angle ACB=\\angle ACD+\\angle DCB$。对 $\\angle ACD$ 与 $\\angle DCB$ 分别应用情形一的结论：")+
 fml("\\angle ACD=\\dfrac12\\angle AOD,\\qquad \\angle DCB=\\dfrac12\\angle DOB")+
 p("两式相加：")+
 fml("\\angle ACB=\\dfrac12(\\angle AOD+\\angle DOB)=\\dfrac12\\angle AOB")+
 p("<strong>情形三：圆心 $O$ 在圆周角外部。</strong>仍作直径 $CD$，此时圆周角为两角之差 $\\angle ACB=\\angle DCB-\\angle DCA$，同样分别用情形一：")+
 fml("\\angle ACB=\\dfrac12(\\angle DOB-\\angle DOA)=\\dfrac12\\angle AOB")+
 p("三种情形结论一致，定理得证。"))+
 note(p("推论：①同弧或等弧所对的圆周角相等，相等的圆周角所对的弧相等；②直径所对的圆周角是直角；$90^\\circ$ 的圆周角所对的弦是直径；③圆内接四边形对角互补，且任一外角等于它的内对角。"))+
 exa(p("<strong>例：</strong>若 $\\angle AOB=80^\\circ$，则同弧所对的圆周角 $\\angle ACB=40^\\circ$；若 $AB$ 为直径，则 $\\angle ACB=90^\\circ$。")))
},
{"id":"e5s8-3","name":"切线性质与圆幂定理","tags":["def","thm","der","exa"],"brief":"切线判定与性质、切线长定理、相交弦与切割线定理（圆幂定理）。",
"body":wrap(
 defn("切线",p("与圆只有一个公共点的直线称为圆的<strong>切线</strong>，这个公共点称为<strong>切点</strong>。"))+
 thm("切线判定定理",p("经过半径的外端并且垂直于这条半径的直线是圆的切线。"))+
 thm("切线性质定理",p("圆的切线垂直于经过切点的半径。"))+
 thm("切线长定理",p("从圆外一点引圆的两条切线，它们的切线长相等，且该点与圆心的连线平分两条切线所夹的角。"))+
 thm("弦切角定理",p("弦切角（顶点在圆上，一边为切线、一边为弦）等于它所夹的弧所对的圆周角。"))+
 thm("圆幂定理",p("记点 $P$ 对圆的幂为 $\\big||OP|^2-r^2\\big|$：<strong>相交弦定理</strong>——圆内两弦 $AB,CD$ 交于 $P$，则 $PA\\cdot PB=PC\\cdot PD$；<strong>切割线定理</strong>——圆外点 $P$ 引切线 $PT$（$T$ 为切点）与割线 $PAB$，则 $PT^2=PA\\cdot PB$。"))+
 der(p("<strong>切线性质的证明（反证法）：</strong>设直线 $l$ 切 $\\odot O$ 于 $T$。若 $l$ 不垂直于 $OT$，则过 $O$ 向 $l$ 作垂线，垂足为 $H\\neq T$，此时 $H$ 到 $O$ 的距离小于 $OT=r$。于是以 $O$ 为圆心、$r$ 为半径的圆与直线 $l$ 有两个交点（在 $H$ 的两侧），这与「切线与圆只有一个公共点」矛盾。故必有")+
 fml("l\\perp OT")+
 p("<strong>切线长定理的证明：</strong>从点 $P$ 引两条切线 $PA,PB$，切点为 $A,B$。连接 $OA,OB,OP$。由切线性质 $OA\\perp PA$、$OB\\perp PB$，故 $\\angle OAP=\\angle OBP=90^\\circ$；又 $OA=OB=r$，$OP$ 公共，由 HL 得两个直角三角形全等：")+
 fml("\\mathrm{Rt}\\triangle OAP\\cong\\mathrm{Rt}\\triangle OBP\\;\\Rightarrow\\;PA=PB")+
 p("且对应角相等 $\\angle APO=\\angle BPO$，即 $OP$ 平分 $\\angle APB$。")+
 p("<strong>相交弦定理的证明：</strong>圆内两弦 $AB,CD$ 交于 $P$。连接 $AC,BD$。由同弧 $AD$ 所对圆周角相等得 $\\angle A=\\angle D$；由同弧 $BC$ 得 $\\angle C=\\angle B$；又 $\\angle APC=\\angle DPB$（对顶角），故")+
 fml("\\triangle APC\\sim\\triangle DPB\\;\\Rightarrow\\;\\dfrac{PA}{PD}=\\dfrac{PC}{PB}\\;\\Rightarrow\\;PA\\cdot PB=PC\\cdot PD")+
 p("<strong>切割线定理的证明：</strong>从圆外点 $P$ 引切线 $PT$ 与割线 $PAB$（$A$ 在 $P,B$ 之间）。连接 $TA,TB$。由弦切角定理，弦切角 $\\angle PTA$ 等于它所夹弧 $TA$ 所对的圆周角 $\\angle TBA$；又 $\\angle P$ 为公共角，故")+
 fml("\\triangle PTA\\sim\\triangle PBT\\;\\Rightarrow\\;\\dfrac{PT}{PB}=\\dfrac{PA}{PT}\\;\\Rightarrow\\;PT^2=PA\\cdot PB"))+
 note(p("以上三定理统一为<strong>圆幂定理</strong>：过点 $P$ 任作一条直线交圆于 $X,Y$，则 $PX\\cdot PY$ 恒为定值，等于点 $P$ 对圆的幂——$P$ 在圆内时为 $r^2-|OP|^2$（相交弦），$P$ 在圆外时为 $|OP|^2-r^2$（切割线或割线）。"))+
 exa(p("<strong>例：</strong>圆外点 $P$ 到圆心距离为 $5$、半径为 $3$，则圆幂 $=|OP|^2-r^2=25-9=16$。故过 $P$ 任作割线交圆于 $A,B$ 时 $PA\\cdot PB=16$，切线长 $PT=\\sqrt{16}=4$。")))
}
]},
{"name":"5.9 对称、旋转与平移","color":"#9d174d","desc":"轴对称、中心对称、旋转与平移",
"items":[
{"id":"e5s9-1","name":"图形的对称、旋转与平移","tags":["def","thm","der","exa"],"brief":"轴对称、中心对称、平移与旋转的定义与性质。",
"body":wrap(
 defn("轴对称",p("把一个图形沿一条直线折叠，若它能与另一个图形完全重合，则这两个图形关于这条直线<strong>轴对称</strong>，这条直线称为<strong>对称轴</strong>。"))+
 defn("中心对称",p("把一个图形绕某一点旋转 $180^\\circ$，若它能与另一个图形完全重合，则这两个图形关于该点<strong>中心对称</strong>，该点称为<strong>对称中心</strong>。"))+
 defn("平移",p("把图形上所有点都沿同一方向移动相同的距离，这样的图形变换称为<strong>平移</strong>。平移不改变图形的形状和大小。"))+
 defn("旋转",p("把图形绕一个定点按一定方向转动一个角度，这样的变换称为<strong>旋转</strong>；定点称为<strong>旋转中心</strong>，转动的角称为<strong>旋转角</strong>。"))+
 thm("三种变换的性质",p("①平移：对应线段平行（或共线）且相等，对应角相等；②旋转：对应点到旋转中心的距离相等，每一对对应点与旋转中心连线的夹角都等于旋转角；③轴对称：对应点的连线被对称轴垂直平分；④中心对称：对应点的连线被对称中心平分。"))+
 der(p("<strong>轴对称性质的证明：</strong>设点 $A$ 与 $A'$ 关于直线 $l$ 对称，线段 $AA'$ 交 $l$ 于 $O$。沿 $l$ 折叠后 $A$ 与 $A'$ 重合，故 $l$ 上每一点到 $A,A'$ 的距离相等，特别地")+
 fml("OA=OA'")+
 p("又若 $AA'$ 不垂直于 $l$，则折叠后 $A$ 的像会落在 $A'$ 以外的点（垂线方向是使两点沿 $l$ 重合的唯一方向），与 $A'$ 是 $A$ 的像矛盾。故 $AA'\\perp l$。两者合起来说明 $l$ 垂直平分 $AA'$：")+
 fml("l\\perp AA',\\qquad OA=OA'")+
 p("<strong>旋转性质的证明：</strong>设点 $P$ 绕旋转中心 $O$ 旋转角 $\\theta$ 后到达 $P'$。由旋转定义，转动的半径长不变，故")+
 fml("OP=OP'")+
 p("并且从 $OP$ 转到 $OP'$ 所经过的角恰为旋转角：$\\angle POP'=\\theta$。于是 $\\triangle OPP'$ 是以 $O$ 为顶点、腰长为 $OP$ 的等腰三角形。由于圆上每一点绕 $O$ 旋转 $\\theta$ 后到 $O$ 的距离仍为 $OP$、夹角仍为 $\\theta$，整个图形旋转后与原图形全等，形状与大小不变。")+
 p("<strong>平移性质的证明：</strong>设平移把点 $A,B$ 分别映到 $A',B'$，平移向量为 $\\vec{v}$，则 $\\overrightarrow{AA'}=\\overrightarrow{BB'}=\\vec{v}$。于是 $AA'\\parallel BB'$ 且 $AA'=BB'$，四边形 $ABB'A'$ 是平行四边形，从而 $AB\\parallel A'B'$ 且 $AB=A'B'$，即对应线段平行且相等、对应角相等。"))+
 exa(p("<strong>例：</strong>正方形有 $4$ 条对称轴，又是中心对称图形（对称中心为对角线交点）；正三角形有 $3$ 条对称轴，是轴对称图形但不是中心对称图形；线段是中心对称图形（对称中心为中点）。")))
}
]},
{"name":"5.10 平面图形面积与周长","color":"#9d174d","desc":"常见平面图形面积周长公式汇总",
"items":[
{"id":"e5s10-1","name":"常见平面图形面积周长公式表","tags":["def","der","app","note"],"brief":"三角形、四边形、圆、扇形、弓形面积周长公式汇总与推导。",
"body":wrap(
 defn("公式汇总",p("记半周长 $s$、内切圆半径 $r$、外接圆半径 $R$。以下为常见平面图形的面积 $S$ 与周长 $C$："))+
 p("<strong>三角形：</strong>$S=\\dfrac12 ah=\\dfrac12 ab\\sin C=rs=\\sqrt{s(s-a)(s-b)(s-c)}=\\dfrac{abc}{4R}$，$C=a+b+c$。")+
 p("<strong>平行四边形：</strong>$S=ah=ab\\sin\\theta$（$\\theta$ 为邻边夹角），$C=2(a+b)$。")+
 p("<strong>矩形：</strong>$S=ab$，$C=2(a+b)$。")+
 p("<strong>菱形：</strong>$S=\\dfrac12 d_1d_2=a^2\\sin\\theta$，$C=4a$。")+
 p("<strong>正方形：</strong>$S=a^2=\\dfrac12 d^2$，$C=4a$。")+
 p("<strong>梯形：</strong>$S=\\dfrac{(a+b)h}{2}=mh$（$m$ 为中位线），$C=a+b+c+d$。")+
 p("<strong>圆：</strong>$S=\\pi r^2$，$C=2\\pi r=\\pi d$。")+
 p("<strong>扇形：</strong>$S=\\dfrac12 lr=\\dfrac12 r^2\\alpha=\\dfrac{n\\pi r^2}{360}$，弧长 $l=r\\alpha=\\dfrac{n\\pi r}{180}$（$\\alpha$ 为圆心角弧度，$n$ 为圆心角度数）。")+
 p("<strong>弓形：</strong>$S=\\dfrac12 r^2(\\alpha-\\sin\\alpha)$（对应劣弧弓形，$\\alpha$ 为圆心角弧度）。")+
 der(p("<strong>扇形与弓形面积公式推导：</strong>整个圆的面积为 $\\pi r^2$，对应圆心角 $2\\pi$（弧度）。圆心角为 $\\alpha$ 的扇形按比例占整个圆的 $\\dfrac{\\alpha}{2\\pi}$，因此")+
 fml("S_{\\text{扇}}=\\dfrac{\\alpha}{2\\pi}\\cdot\\pi r^2=\\dfrac12 r^2\\alpha")+
 p("又弧长 $l=r\\alpha$，代入得用弧长表示的扇形面积公式：")+
 fml("S_{\\text{扇}}=\\dfrac12 lr")+
 p("弓形是由弦 $AB$ 与弧 $\\overset{\\frown}{AB}$ 围成的图形，它等于扇形 $OAB$ 减去由两条半径与弦组成的等腰三角形 $OAB$。该等腰三角形面积为")+
 fml("S_{\\triangle OAB}=\\dfrac12 r^2\\sin\\alpha")+
 p("两式相减即得弓形面积公式：")+
 fml("S_{\\text{弓}}=S_{\\text{扇}}-S_{\\triangle OAB}=\\dfrac12 r^2(\\alpha-\\sin\\alpha)"))+
 app(p("<strong>应用：</strong>扇形面积与弧长公式广泛用于求花坛、扇面、弯道等实际图形的用料；已知弓形的弦长 $a$ 与弓高 $h$ 时，可先由 $r=\\dfrac{a^2+4h^2}{8h}$ 求半径，再用弓形公式求出面积。"))+
 note(p("记忆要点：各类「底乘高」型公式（三角形、平行四边形、梯形）本质上都是矩形面积的分割与拼接结果；圆、扇形、弓形三者按同一比例关系 $S_{\\text{扇}}=\\dfrac12 lr$ 相互联系，而弓形只是扇形减去一个三角形。")))
}]}
]
# ============ 第六章 立体几何 ============
# ============ 第六章 立体几何 ============
ch6_sections = [
{"name":"6.1 多面体","color":"#7c3aed","desc":"棱柱、棱锥、棱台与欧拉公式",
"items":[
{"id":"e6s1-1","name":"棱柱与棱锥","tags":["def","thm","der","exa"],"brief":"棱柱、棱锥的定义，体积与侧面积公式的严格推导。",
"fig":"cube","figCap":"正方体是特殊的棱柱，体积 $V=a^3$",
"body":wrap(
 defn("棱柱",p("两个面互相平行、其余各面都是四边形、并且每相邻两个四边形的公共边都互相平行的多面体称为<strong>棱柱</strong>。两个互相平行的面叫底面，其余各面叫侧面，相邻侧面的公共边叫侧棱。侧棱垂直于底面的棱柱叫<strong>直棱柱</strong>；底面是正多边形的直棱柱叫<strong>正棱柱</strong>；底面为平行四边形的棱柱叫平行六面体。"))+
 defn("棱锥",p("有一个面是多边形、其余各面都是有一个公共顶点的三角形的多面体称为<strong>棱锥</strong>。多边形面叫底面，公共顶点叫顶点，各侧面都是三角形。底面是正多边形、且顶点在底面的射影是底面中心的棱锥叫<strong>正棱锥</strong>，其侧面三角形底边上的高叫斜高，记为 $l$。"))+
 thm("体积与侧面积公式",p("设底面积为 $S$、高为 $h$、底面周长为 $C$、斜高为 $l$，则")+
 fml("V_{\\text{柱}}=S h,\\qquad V_{\\text{锥}}=\\dfrac{1}{3}S h")+
 fml("S_{\\text{正棱柱侧}}=C h,\\qquad S_{\\text{正棱锥侧}}=\\dfrac{1}{2}C l"))+
 der(
  p("<strong>第一步，棱柱的体积。</strong>棱柱的每一个平行于底面的截面都与底面全等，面积恒为 $S$。由祖暅原理（等高处截面积相等则体积相等），棱柱与一个底面积为 $S$、高为 $h$ 的长方体体积相等，故")+
  fml("V_{\\text{柱}}=S h")+
  p("<strong>第二步，把任意棱锥化归为三棱锥。</strong>取一个棱锥，从顶点出发用若干个对角面把底面多边形分割成若干三角形，棱锥随之被分成若干个以顶点为公共顶点、高均为 $h$ 的三棱锥。若各三角形面积为 $S_1,S_2,\\dots,S_n$，则")+
  fml("V_{\\text{锥}}=\\sum_{i=1}^{n}\\dfrac{1}{3}S_i h=\\dfrac{1}{3}\\Big(\\sum_{i=1}^{n}S_i\\Big)h=\\dfrac{1}{3}S h")+
  p("因此只须证明三棱锥体积公式 $V=\\dfrac{1}{3}Sh$。")+
  p("<strong>第三步，三棱柱剖分为三个等体积三棱锥。</strong>取三棱柱 $ABC\\text{-}A'B'C'$，用平面 $A'BC$ 与平面 $A'B'C$ 把它剖分成三个三棱锥：$A'ABC$、$A'BB'C$、$A'B'C'C$。")+
  p("先比较三棱锥 $A'ABC$ 与 $A'BB'C$：它们可以分别以 $\\triangle A'AB$ 与 $\\triangle A'BB'$ 为底、以 $C$ 为公共顶点。四边形 $ABB'A'$ 是平行四边形，其对角线 $A'B$ 把它分成两个全等的三角形 $\\triangle A'AB$ 与 $\\triangle A'BB'$，面积相等；又二者在同一平面内、顶点同为 $C$，故高相等，于是")+
  fml("V_{A'ABC}=V_{A'BB'C}")+
  p("再比较三棱锥 $A'BB'C$ 与 $A'B'C'C$：它们可以分别以 $\\triangle BB'C$ 与 $\\triangle B'C'C$ 为底、以 $A'$ 为公共顶点。平行四边形 $BCC'B'$ 被对角线 $B'C$ 分成两个全等三角形，同理得")+
  fml("V_{A'BB'C}=V_{A'B'C'C}")+
  p("故三个三棱锥体积相等，各为三棱柱体积的三分之一。而三棱柱体积为 $Sh$，所以三棱锥体积为 $\\dfrac{1}{3}Sh$。")+
  p("<strong>第四步，正棱柱的侧面积。</strong>沿一条侧棱把侧面剪开展平，正棱柱的侧面展开图是矩形：一边为底面周长 $C=na$（$n$ 为底面边数、$a$ 为底边），另一边为侧棱长 $h$，故")+
  fml("S_{\\text{正棱柱侧}}=C h=n a h")+
  p("<strong>第五步，正棱锥的侧面积。</strong>正棱锥的 $n$ 个侧面是全等的等腰三角形，每个三角形的底为 $a$、高为斜高 $l$，面积为 $\\dfrac{1}{2}al$，故")+
  fml("S_{\\text{正棱锥侧}}=n\\cdot\\dfrac{1}{2}al=\\dfrac{1}{2}(na)l=\\dfrac{1}{2}C l"))+
 exa(p("<strong>例：</strong>正三棱柱底面边长为 $2$、高为 $3$：底面积 $S=\\dfrac{\\sqrt3}{4}\\cdot2^2=\\sqrt3$，$V=Sh=3\\sqrt3$，侧面积 $S_{侧}=Ch=6\\times3=18$。正四棱锥底面边长 $2$、斜高 $\\sqrt5$，则 $S=4$，$S_{侧}=\\dfrac{1}{2}\\times8\\times\\sqrt5=4\\sqrt5$。棱长 $a$ 的正四面体各面均为正三角形，其体积为 $V=\\dfrac{\\sqrt2}{12}a^3$。")))
},
{"id":"e6s1-2","name":"棱台与体积比","tags":["def","thm","der","exa"],"brief":"棱台定义、体积公式与平行截面积比的严格推导。",
"fig":"pyramid","figCap":"棱台由棱锥截去顶部得到，体积 $V=\\dfrac{h}{3}(S_{上}+\\sqrt{S_{上}S_{下}}+S_{下})$",
"body":wrap(
 defn("棱台",p("用平行于棱锥底面的平面去截棱锥，底面与截面之间的部分称为<strong>棱台</strong>。截去的部分是小棱锥；剩下的两个平行面分别叫上底面与下底面，它们是对应边平行的相似多边形，侧面都是梯形，各侧棱延长后交于一点。"))+
 thm("棱台体积公式",p("设上、下底面积分别为 $S_{上},S_{下}$，高为 $h$，则")+
 fml("V_{\\text{台}}=\\dfrac{1}{3}h\\big(S_{上}+\\sqrt{S_{上}S_{下}}+S_{下}\\big)"))+
 der(
  p("<strong>第一步，还原为两个棱锥之差。</strong>把棱台补成完整的棱锥：设补上的小棱锥高为 $h_1$、整个大棱锥高为 $H$，则棱台高 $h=H-h_1$，棱台体积等于大棱锥减去小棱锥：")+
  fml("V_{\\text{台}}=\\dfrac{1}{3}S_{下}H-\\dfrac{1}{3}S_{上}h_1")+
  p("<strong>第二步，由相似求两个高的关系。</strong>截面平行于底面，故小棱锥与大棱锥相似，相似比为 $\\dfrac{h_1}{H}$。相似图形的面积比等于相似比的平方，于是")+
  fml("\\dfrac{S_{上}}{S_{下}}=\\Big(\\dfrac{h_1}{H}\\Big)^2\\;\\Rightarrow\\;h_1=H\\sqrt{\\dfrac{S_{上}}{S_{下}}}=Hk,\\quad k=\\sqrt{\\dfrac{S_{上}}{S_{下}}}")+
  p("其中 $S_{上}=k^2S_{下}$。")+
  p("<strong>第三步，用 $h$ 表示 $H$。</strong>由 $h=H-h_1=H(1-k)$ 解得")+
  fml("H=\\dfrac{h}{1-k}")+
  p("<strong>第四步，代入并化简。</strong>将 $h_1=Hk$、$S_{上}=k^2S_{下}$ 代入第一步的式子：")+
  fml("V_{\\text{台}}=\\dfrac{1}{3}\\big(S_{下}H-S_{上}Hk\\big)=\\dfrac{H S_{下}}{3}\\big(1-k^3\\big)")+
  p("利用立方差公式 $1-k^3=(1-k)(1+k+k^2)$，并代入 $H(1-k)=h$：")+
  fml("V_{\\text{台}}=\\dfrac{H S_{下}(1-k)(1+k+k^2)}{3}=\\dfrac{h S_{下}}{3}\\big(1+k+k^2\\big)")+
  p("再把 $k=\\sqrt{S_{上}/S_{下}}$ 代回，注意 $k S_{下}=\\sqrt{S_{上}S_{下}}$、$k^2 S_{下}=S_{上}$，即得棱台体积公式：")+
  fml("V_{\\text{台}}=\\dfrac{h}{3}\\big(S_{上}+\\sqrt{S_{上}S_{下}}+S_{下}\\big)")+
  p("<strong>第五步，平行截面的面积比。</strong>设棱锥顶点到某个平行截面的距离为 $x$、到底面的距离为 $H$，则该截面与底面相似，相似比为 $\\dfrac{x}{H}$，由面积比等于相似比的平方得")+
  fml("\\dfrac{S_{\\text{截}}}{S_{\\text{底}}}=\\Big(\\dfrac{x}{H}\\Big)^2")+
  p("这说明截面面积与它到顶点距离的平方成正比；反之若两个截面的面积之比为 $m:n$，则它们到顶点的距离之比为 $\\sqrt m:\\sqrt n$。"))+
 exa(p("<strong>例：</strong>棱台上底面积 $S_{上}=4$、下底面积 $S_{下}=9$、高 $h=6$，则 $\\sqrt{S_{上}S_{下}}=\\sqrt{4\\times9}=6$，故 $V=\\dfrac{6}{3}(4+6+9)=2\\times19=38$。特别地，当 $S_{上}=S_{下}=S$ 时公式退化为 $V=Sh$（柱），当 $S_{上}=0$ 时退化为 $V=\\dfrac{1}{3}Sh$（锥）。")))
},
{"id":"e6s1-3","name":"欧拉公式与多面体","tags":["def","thm","der","exa"],"brief":"简单多面体的顶点-棱-面关系与五种正多面体的完整推导。",
"body":wrap(
 defn("简单多面体与正多面体",p("表面可以连续地变形为一个球面（表面没有孔洞）的多面体称为<strong>简单多面体</strong>，凸多面体都是简单多面体。<strong>正多面体</strong>是指各个面都是全等的正多边形、并且每个顶点处聚集的棱数都相同的多面体。"))+
 thm("欧拉公式",p("对任意简单多面体，设顶点数为 $V$、棱数为 $E$、面数为 $F$，则恒有")+
 fml("V-E+F=2"))+
 der(
  p("<strong>第一步，去掉一面并展平。</strong>把简单多面体的一个面剪去，把剩下的表面沿棱拉伸、压平成一个平面连通图：顶点数 $V$ 与棱数 $E$ 不变，原来的 $F$ 个面中剪掉的那一个变成图的外部无界区域，故平面图共含 $F$ 个区域（含外部）。于是证明 $V-E+F=2$ 就化为研究这个平面连通图。")+
  p("<strong>第二步，三角剖分保持不变量。</strong>对每一个非三角形的面，连接它的一对不相邻顶点作对角线。每添一条对角线，棱数 $E$ 增加 $1$，同时该面被一分为二使面数 $F$ 也增加 $1$，两者抵消，故 $V-E+F$ 的值不变。反复操作可把平面图全部化为三角形。")+
  p("<strong>第三步，逐次去掉耳朵保持不变量。</strong>三角剖分后的图总有若干<strong>耳朵</strong>——只有两条边落在最外边界上的三角形，对应一个度为 $2$ 的边界顶点 $P$（其两条边为 $PQ,PR$）。去掉这个耳朵：删去顶点 $P$ 及边 $PQ,PR$，同时该三角形所在的面消失，于是")+
  fml("V\\to V-1,\\qquad E\\to E-2,\\qquad F\\to F-1")+
  p("代入得 $V-E+F\\to(V-1)-(E-2)+(F-1)=V-E+F$，不变量保持不变。反复去掉耳朵，直到只剩下一个三角形。")+
  p("<strong>第四步，算出不变量。</strong>最后剩下的三角形满足 $V=3$、$E=3$，而平面图含内部与外部共 $F=2$ 个区域，故")+
  fml("V-E+F=3-3+2=2")+
  p("因每一步都不改变 $V-E+F$，故原多面体满足 $V-E+F=2$，欧拉公式得证。")+
  p("<strong>第五步，推导正多面体只有五种。</strong>设正多面体每个面是正 $n$ 边形、每个顶点处聚集 $m$ 条棱。各面的边数之和为 $nF$，而每条棱恰属于两个面，故 $nF=2E$；各顶点的棱数之和为 $mV$，而每条棱恰有两个端点，故 $mV=2E$。代入欧拉公式 $V-E+F=2$：")+
  fml("\\dfrac{2E}{m}-E+\\dfrac{2E}{n}=2")+
  p("两端同除以 $2E$（$E>0$）：")+
  fml("\\dfrac{1}{m}+\\dfrac{1}{n}=\\dfrac{1}{2}+\\dfrac{1}{E}>\\dfrac{1}{2}")+
  p("又每个面至少是三角形、每个顶点处至少聚集 $3$ 条棱，故 $n\\ge3$、$m\\ge3$。对正整数 $(m,n)$ 逐一讨论 $\\dfrac{1}{m}+\\dfrac{1}{n}>\\dfrac{1}{2}$：")+
  fml("m=3:\\ \\dfrac{1}{n}>\\dfrac{1}{6}\\Rightarrow n=3,4,5")+
  fml("m=4:\\ \\dfrac{1}{n}>\\dfrac{1}{4}\\Rightarrow n=3")+
  fml("m=5:\\ \\dfrac{1}{n}>\\dfrac{3}{10}\\Rightarrow n=3")+
  fml("m\\ge6:\\ \\dfrac{1}{m}+\\dfrac{1}{n}\\le\\dfrac{1}{6}+\\dfrac{1}{3}=\\dfrac{1}{2}\\text{，不可能}")+
  p("故只有 $(m,n)=(3,3),(4,3),(5,3),(3,4),(3,5)$ 五种组合，分别对应正四面体、正六面体、正十二面体、正八面体、正二十面体。所以正多面体只有五种。"))+
 exa(p("<strong>例：</strong>正方体 $V=8$、$E=12$、$F=6$，验证 $8-12+6=2$。正八面体 $(m,n)=(4,3)$：由 $3F=2E$、$4V=2E$ 与 $V-E+F=2$ 解得 $V=6,E=12,F=8$，验证 $6-12+8=2$。正十二面体（每面正五边形、每顶点 $3$ 棱）为 $V=20,E=30,F=12$，验证 $20-30+12=2$；正二十面体为 $V=12,E=30,F=20$。")))
}
]},
{"name":"6.2 旋转体","color":"#6d28d9","desc":"圆柱、圆锥、圆台、球",
"items":[
{"id":"e6s2-1","name":"圆柱、圆锥与圆台","tags":["def","thm","der","exa"],"brief":"旋转体的定义，圆柱、圆锥、圆台的表面积与体积推导。",
"fig":"cone","figCap":"圆锥 $V=\\dfrac{1}{3}\\pi r^2 h$，由直角三角形绕一直角边旋转得到",
"body":wrap(
 defn("旋转体",p("平面图形绕它所在平面内的一条定直线（轴）旋转一周所形成的几何体称为<strong>旋转体</strong>。矩形绕一边旋转得<strong>圆柱</strong>，直角三角形绕一条直角边旋转得<strong>圆锥</strong>，直角梯形绕垂直于底边的腰旋转得<strong>圆台</strong>；圆锥被平行于底面的平面截去顶部也得到圆台。"))+
 thm("圆柱、圆锥、圆台的表面积与体积",p("设底面半径为 $r$（圆台为下底 $R$、上底 $r$）、高为 $h$、母线为 $l$，则")+
 fml("V_{\\text{圆柱}}=\\pi r^2 h,\\qquad S_{\\text{圆柱侧}}=2\\pi r h,\\qquad S_{\\text{圆柱全}}=2\\pi r^2+2\\pi r h")+
 fml("V_{\\text{圆锥}}=\\dfrac{1}{3}\\pi r^2 h,\\qquad S_{\\text{圆锥侧}}=\\pi r l,\\qquad S_{\\text{圆锥全}}=\\pi r^2+\\pi r l")+
 fml("V_{\\text{圆台}}=\\dfrac{\\pi h}{3}\\big(r^2+rR+R^2\\big),\\qquad S_{\\text{圆台侧}}=\\pi(r+R)l"))+
 der(
  p("<strong>第一步，圆柱的体积与侧面积。</strong>圆柱可看作一个半径为 $r$ 的圆盘沿轴方向平移 $h$ 扫出的立体，每个平行于底面的截面都是半径为 $r$ 的圆，面积恒为 $\\pi r^2$，由祖暅原理体积等于底面积乘高：")+
  fml("V_{\\text{圆柱}}=\\pi r^2\\cdot h=\\pi r^2 h")+
  p("沿一条母线把侧面剪开展平，得到一个矩形：长为底面圆周长 $2\\pi r$，宽为高 $h$，故")+
  fml("S_{\\text{圆柱侧}}=2\\pi r\\cdot h=2\\pi r h,\\qquad S_{\\text{圆柱全}}=2\\pi r^2+2\\pi r h")+
  p("<strong>第二步，圆锥的体积（极限思想）。</strong>圆锥可看作底面正 $n$ 边形内接棱锥当 $n\\to\\infty$ 时的极限。正 $n$ 边形棱锥体积为 $\\dfrac{1}{3}S_n h$（$S_n$ 为内接正 $n$ 边形面积），当 $n\\to\\infty$ 时 $S_n\\to\\pi r^2$，故")+
  fml("V_{\\text{圆锥}}=\\lim_{n\\to\\infty}\\dfrac{1}{3}S_n h=\\dfrac{1}{3}\\pi r^2 h")+
  p("<strong>第三步，圆锥的侧面积（展开图）。</strong>沿一条母线把圆锥侧面剪开展平，得到一个扇形：扇形半径等于母线 $l$，弧长等于底面圆周长 $2\\pi r$。由扇形面积公式（面积等于半径与弧长乘积之半）：")+
  fml("S_{\\text{圆锥侧}}=\\dfrac{1}{2}\\cdot l\\cdot 2\\pi r=\\pi r l")+
  p("其中母线由勾股定理给出 $l=\\sqrt{r^2+h^2}$，加上底面圆得 $S_{\\text{圆锥全}}=\\pi r^2+\\pi r l$。")+
  p("<strong>第四步，圆台的体积。</strong>圆台是圆锥截去顶部所得。设截去的小圆锥底面半径为 $r$、高为 $h_1$，完整圆锥底面半径为 $R$、高为 $H$，则台高 $h=H-h_1$，且由相似 $\\dfrac{r}{R}=\\dfrac{h_1}{H}$。把棱台体积公式中的面积换成圆面积 $S_{上}=\\pi r^2,\\ S_{下}=\\pi R^2$ 即得")+
  fml("V_{\\text{圆台}}=\\dfrac{h}{3}\\big(\\pi r^2+\\sqrt{\\pi r^2\\cdot\\pi R^2}+\\pi R^2\\big)=\\dfrac{\\pi h}{3}\\big(r^2+rR+R^2\\big)")+
  p("<strong>第五步，圆台的侧面积。</strong>圆台侧面展开是一个扇环（大扇形挖去小扇形）。由相似得两个扇形母线之比 $\\dfrac{l_1}{l_2}=\\dfrac{R}{r}$，且 $l_1-l_2=l$，侧面积等于两个扇形面积之差：")+
  fml("S_{\\text{圆台侧}}=\\pi R l_1-\\pi r l_2=\\pi(R l_1-r l_2)")+
  p("由 $l_1=\\dfrac{R}{r}l_2$ 与 $l_1-l_2=l$ 解得 $l_2=\\dfrac{r l}{R-r}$，代入化简得")+
  fml("S_{\\text{圆台侧}}=\\pi(r+R)l"))+
 exa(p("<strong>例：</strong>圆锥底面半径 $r=3$、高 $h=4$，则母线 $l=\\sqrt{3^2+4^2}=5$，$V=\\dfrac{1}{3}\\pi\\cdot9\\cdot4=12\\pi$，$S_{侧}=\\pi\\cdot3\\cdot5=15\\pi$，$S_{全}=9\\pi+15\\pi=24\\pi$。圆柱若 $r=2,h=3$，则 $V=4\\pi\\times3=12\\pi$，$S_{侧}=2\\pi\\times2\\times3=12\\pi$。")))
},
{"id":"e6s2-2","name":"球与球面","tags":["def","thm","der","exa"],"brief":"球的表面积与体积公式的严格推导（祖暅原理与无限分割）。",
"fig":"sphere","figCap":"球 $S=4\\pi R^2,\\ V=\\dfrac{4}{3}\\pi R^3$",
"body":wrap(
 defn("球与球面",p("半圆绕它的直径所在的直线旋转一周所成的曲面称为<strong>球面</strong>，球面所围成的几何体称为<strong>球</strong>。球心到球面上任意一点的距离都等于半径 $R$；用经过球心的平面去截球，所得的圆叫大圆。"))+
 thm("球的表面积与体积",p("半径为 $R$ 的球，其表面积与体积分别为")+
 fml("S_{\\text{球}}=4\\pi R^2,\\qquad V_{\\text{球}}=\\dfrac{4}{3}\\pi R^3"))+
 der(
  p("<strong>第一步，用祖暅原理求球的体积。</strong>取一个半径为 $R$ 的半球，与一个底面半径为 $R$、高为 $R$ 的圆柱（再挖去一个以圆柱下底面为底、下底面圆心为顶点、高为 $R$ 的倒圆锥）放在同一水平面上，使二者的下底面共面、轴重合。")+
  p("<strong>第二步，比较同一高度处的截面面积。</strong>设到球心（即半球底面圆心所在水平面）的距离为 $x$。半球在该高度处的截面是半径为 $\\sqrt{R^2-x^2}$ 的圆，面积")+
  fml("S_{\\text{半球截面}}=\\pi\\big(R^2-x^2\\big)")+
  p("而挖空后的圆柱在同一高度处的截面是外半径为 $R$、内半径为 $x$（倒圆锥在此处的半径）的圆环，面积为 $\\pi R^2-\\pi x^2$，即")+
  fml("S_{\\text{圆环}}=\\pi R^2-\\pi x^2=\\pi\\big(R^2-x^2\\big)=S_{\\text{半球截面}}")+
  p("两者在任意高度处截面面积都相等，由祖暅原理体积相等：")+
  fml("V_{\\text{半球}}=\\pi R^2\\cdot R-\\dfrac{1}{3}\\pi R^2\\cdot R=\\dfrac{2}{3}\\pi R^3")+
  p("故整个球的体积为")+
  fml("V_{\\text{球}}=2V_{\\text{半球}}=\\dfrac{4}{3}\\pi R^3")+
  p("<strong>第三步，用无限分割求球的表面积。</strong>把球面分割成 $n$ 个小曲面片，面积记为 $\\Delta S_1,\\Delta S_2,\\dots,\\Delta S_n$。把每一小片与球心 $O$ 连成一个以 $O$ 为顶点、以该小片为底的小锥体，其高近似等于半径 $R$。球的体积即这些小锥体体积之和：")+
  fml("V_{\\text{球}}\\approx\\sum_{i=1}^{n}\\dfrac{1}{3}\\Delta S_i\\cdot R=\\dfrac{R}{3}\\sum_{i=1}^{n}\\Delta S_i=\\dfrac{R}{3}S_{\\text{球}}")+
  p("当分割无限加密（$n\\to\\infty$，每片直径趋于 $0$）时近似变为等式，即 $V_{\\text{球}}=\\dfrac{1}{3}R S_{\\text{球}}$，于是")+
  fml("S_{\\text{球}}=\\dfrac{3V_{\\text{球}}}{R}=\\dfrac{3}{R}\\cdot\\dfrac{4}{3}\\pi R^3=4\\pi R^2")+
  p("这正是阿基米德的著名结论：球的表面积等于它的大圆面积的 $4$ 倍；球的体积等于其外切圆柱（底面半径 $R$、高 $2R$，体积 $2\\pi R^3$）体积的 $\\dfrac{2}{3}$。"))+
 exa(p("<strong>例：</strong>半径 $R=3$ 的球，$S=4\\pi\\cdot3^2=36\\pi$，$V=\\dfrac{4}{3}\\pi\\cdot3^3=36\\pi$（此例中二者数值恰好相等）。若球的体积为 $\\dfrac{32}{3}\\pi$，由 $\\dfrac{4}{3}\\pi R^3=\\dfrac{32}{3}\\pi$ 得 $R^3=8$，故 $R=2$，表面积 $S=4\\pi\\cdot2^2=16\\pi$。")))
}
]},
{"name":"6.3 空间位置关系","color":"#5b21b6","desc":"线面平行垂直、二面角与空间距离",
"items":[
{"id":"e6s3-1","name":"线面平行与垂直","tags":["def","thm","der","exa"],"brief":"直线与平面平行、垂直的判定定理与性质定理及其严格证明。",
"body":wrap(
 defn("直线与平面的位置关系",p("直线与平面的位置关系有三种：直线在平面内（无数个公共点）、直线与平面相交（有且只有一个公共点）、直线与平面平行（没有公共点）。两个平面的位置关系有两种：平行与相交。"))+
 thm("线面平行的判定定理",p("平面外的一条直线与此平面内的一条直线平行，则该直线与此平面平行。"))+
 thm("线面平行的性质定理",p("一条直线与一个平面平行，如果过这条直线的平面与此平面相交，那么这条直线与交线平行。"))+
 thm("线面垂直的判定定理",p("一条直线与一个平面内的两条相交直线都垂直，则该直线与此平面垂直。"))+
 thm("线面垂直的性质定理",p("垂直于同一平面的两条直线互相平行；反过来，若两条平行直线中的一条垂直于一个平面，则另一条也垂直于这个平面。"))+
 der(
  p("<strong>一、判定定理（平行）的证明（反证法）。</strong>设直线 $l$ 在平面 $\\alpha$ 外，$m\\subset\\alpha$ 且 $l\\parallel m$。若 $l$ 与 $\\alpha$ 有公共点，则由 $l\\parallel m$ 知 $l$ 与 $m$ 确定唯一平面 $\\beta$，而 $\\alpha$ 与 $\\beta$ 都经过直线 $m$，故其交线就是 $m$。于是 $l$ 与 $\\alpha$ 的公共点必落在 $\\alpha\\cap\\beta=m$ 上，即 $l$ 与 $m$ 有公共点，这与 $l\\parallel m$ 矛盾。所以 $l$ 与 $\\alpha$ 无公共点，即 $l\\parallel\\alpha$。")+
  p("<strong>二、性质定理（平行）的证明。</strong>设 $l\\parallel\\alpha$，$l\\subset\\beta$，$\\alpha\\cap\\beta=b$。由 $l\\parallel\\alpha$ 知 $l$ 与 $\\alpha$ 无公共点；又 $b\\subset\\alpha$，故 $l$ 与 $b$ 也无公共点。而 $l$ 与 $b$ 都在平面 $\\beta$ 内，同一平面内不相交的两条直线平行，故 $l\\parallel b$。")+
  p("<strong>三、判定定理（垂直）的证明。</strong>设平面 $\\alpha$ 内两条相交直线 $a,b$ 交于点 $O$，且 $l\\perp a$、$l\\perp b$。要证 $l\\perp\\alpha$，只须证 $l$ 垂直于 $\\alpha$ 内任意一条直线 $c$。")+
  p("把 $l$ 平移到经过点 $O$（垂直关系在平移下不变）。记直线 $l$ 的方向向量为 $\\vec u$，$a,b,c$ 的方向向量分别为 $\\vec a,\\vec b,\\vec c$。由 $l\\perp a$、$l\\perp b$ 得")+
  fml("\\vec u\\cdot\\vec a=0,\\qquad \\vec u\\cdot\\vec b=0")+
  p("因 $a,b$ 是平面 $\\alpha$ 内两条相交直线，$\\vec a,\\vec b$ 不共线，它们可线性表示 $\\alpha$ 内任意直线的方向向量 $\\vec c$：")+
  fml("\\vec c=\\lambda\\vec a+\\mu\\vec b")+
  p("对上式两端与 $\\vec u$ 作内积，利用内积的双线性：")+
  fml("\\vec u\\cdot\\vec c=\\lambda(\\vec u\\cdot\\vec a)+\\mu(\\vec u\\cdot\\vec b)=0")+
  p("故 $\\vec u\\perp\\vec c$，即 $l\\perp c$。由 $c$ 在 $\\alpha$ 内的任意性，$l$ 垂直于 $\\alpha$ 内所有直线，即 $l\\perp\\alpha$。")+
  p("<strong>四、性质定理（垂直）的证明。</strong>设 $l\\perp\\alpha$，取 $\\alpha$ 内两条相交直线 $a,b$，由 $l\\perp\\alpha$ 得 $l\\perp a$、$l\\perp b$。若 $l'\\parallel l$，则 $l'$ 的方向向量与 $l$ 相同，仍垂直于 $\\vec a,\\vec b$，由判定定理得 $l'\\perp\\alpha$。")+
  p("若另有直线 $l''\\perp\\alpha$，则 $l''$ 的方向向量也同时垂直于不共线的 $\\vec a,\\vec b$。在空间中同时垂直于两条不共线向量的方向至多相差一个标量因子，故 $l''\\parallel l$——这正是「垂直于同一平面的两条直线平行」。"))+
 exa(p("<strong>例：</strong>在正方体 $ABCD\\text{-}A'B'C'D'$ 中，$AB\\parallel A'B'$，而 $AB$ 在底面 $ABCD$ 内、$A'B'$ 在底面外，故由判定定理得 $A'B'\\parallel$ 平面 $ABCD$。又 $AA'\\perp AB$、$AA'\\perp AD$，而 $AB$ 与 $AD$ 是底面内的相交直线，故 $AA'\\perp$ 平面 $ABCD$。")))
},
{"id":"e6s3-2","name":"二面角与距离","tags":["def","thm","der","exa"],"brief":"二面角与平面角的定义、平面角的唯一性证明与点面距离公式推导。",
"body":wrap(
 defn("二面角",p("从一条直线出发的两个半平面所组成的图形称为<strong>二面角</strong>，这条直线叫二面角的棱，两个半平面叫二面角的面。在棱上任取一点 $O$，分别在两个半平面内作垂直于棱的射线 $OA,OB$，则 $\\angle AOB$ 称为二面角的<strong>平面角</strong>。平面角的度数就是二面角的度数，取值范围是 $[0^\\circ,180^\\circ]$。"))+
 thm("平面角与点的选取无关",p("二面角的平面角的大小不依赖于棱上点的选取，因而定义是相容的。"))+
 thm("用向量求二面角",p("设两个半平面所在平面的法向量为 $\\vec{n_1},\\vec{n_2}$，则二面角 $\\varphi$ 满足")+
 fml("|\\cos\\varphi|=\\dfrac{|\\vec{n_1}\\cdot\\vec{n_2}|}{|\\vec{n_1}|\\,|\\vec{n_2}|"))+
 thm("点到平面的距离",p("点 $P_0(x_0,y_0,z_0)$ 到平面 $Ax+By+Cz+D=0$ 的距离为")+
 fml("d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}"))+
 der(
  p("<strong>一、平面角定义相容性的证明。</strong>设二面角的棱为 $l$，在 $l$ 上取两点 $O$ 与 $O'$，分别在两个半平面内作 $l$ 的垂线 $OA,OB$ 与 $O'A',O'B'$。因 $OA,O'A'$ 都垂直于 $l$ 且位于同一半平面内，故 $OA\\parallel O'A'$；同理 $OB\\parallel O'B'$。于是 $\\angle AOB$ 与 $\\angle A'O'B'$ 的两组对应边分别平行且开口方向相同，由「两组对应边分别平行的两个角相等」得")+
  fml("\\angle AOB=\\angle A'O'B'")+
  p("故平面角的大小与点 $O$ 的选取无关，二面角的定义是相容的。")+
  p("<strong>二、用向量求二面角。</strong>设两个半平面所在的平面为 $\\alpha_1,\\alpha_2$，其法向量为 $\\vec{n_1},\\vec{n_2}$。二面角的平面角与这两个法向量的夹角相等或互补（取决于法向量的指向）。由内积公式 $\\vec{n_1}\\cdot\\vec{n_2}=|\\vec{n_1}||\\vec{n_2}|\\cos\\theta$，取绝对值即得")+
  fml("|\\cos\\varphi|=\\dfrac{|\\vec{n_1}\\cdot\\vec{n_2}|}{|\\vec{n_1}|\\,|\\vec{n_2}|}")+
  p("再根据二面角是锐角还是钝角确定其符号，即可得二面角的度数。")+
  p("<strong>三、点到平面距离公式的推导。</strong>设平面 $\\alpha:Ax+By+Cz+D=0$，其法向量为 $\\vec n=(A,B,C)$。点 $P_0(x_0,y_0,z_0)$ 到 $\\alpha$ 的距离，就是 $\\overrightarrow{P_0P}$ 沿法向方向到平面的有向距离的绝对值。取平面内任一点 $P(x,y,z)$，则")+
  fml("d=\\dfrac{|\\overrightarrow{P_0P}\\cdot\\vec n|}{|\\vec n|}=\\dfrac{\\big|A(x-x_0)+B(y-y_0)+C(z-z_0)\\big|}{\\sqrt{A^2+B^2+C^2}}")+
  p("因 $P$ 在平面内，有 $Ax+By+Cz=-D$，故分子可整理为")+
  fml("\\big|(Ax+By+Cz)-(Ax_0+By_0+Cz_0)\\big|=\\big|-D-(Ax_0+By_0+Cz_0)\\big|")+
  fml("=\\big|Ax_0+By_0+Cz_0+D\\big|")+
  p("代回即得点到平面的距离公式：")+
  fml("d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}")+
  p("<strong>四、体积法求距离（几何途径）。</strong>若不便建立坐标系，可用等体积法：把所求的点面距离看作某个三棱锥的高，用两组不同的底与对应高计算同一个三棱锥的体积，由 $V=\\dfrac{1}{3}Sh$ 反解该高，即得所求距离。"))+
 exa(p("<strong>例：</strong>原点到平面 $2x+3y+6z-21=0$ 的距离为 $d=\\dfrac{|0+0+0-21|}{\\sqrt{2^2+3^2+6^2}}=\\dfrac{21}{7}=3$。又设平面 $\\alpha$ 的法向量 $\\vec n=(0,1,0)$、平面 $\\beta$ 的法向量 $\\vec n'=(1,1,0)$，则 $|\\cos\\varphi|=\\dfrac{|1|}{1\\cdot\\sqrt2}=\\dfrac{\\sqrt2}{2}$，故二面角为 $45^\\circ$ 或 $135^\\circ$。")))
}
]},
{"name":"6.4 立体几何公式汇总","color":"#4c1d95","desc":"柱、锥、台、球体积与表面积汇总表",
"items":[
{"id":"e6s4-1","name":"常见立体图形体积与表面积汇总表","tags":["def","der","app","note"],"brief":"柱、锥、台、球及正多面体的侧面积、表面积与体积公式汇总与内在联系。",
"body":wrap(
 defn("公式汇总",p("记底面积为 $S$、底面周长为 $C$、高为 $h$、母线（或斜高）为 $l$、半径为 $r,R$。以下为常见立体图形的侧面积、全面积与体积公式："))+
 p("<strong>棱柱：</strong>$V=Sh$，$S_{侧}=Ch$，$S_{全}=2S+Ch$。")+
 p("<strong>圆柱：</strong>$V=\\pi r^2 h$，$S_{侧}=2\\pi r h$，$S_{全}=2\\pi r^2+2\\pi r h$。")+
 p("<strong>棱锥：</strong>$V=\\dfrac{1}{3}Sh$，正棱锥 $S_{侧}=\\dfrac{1}{2}Cl$，$S_{全}=S+\\dfrac{1}{2}Cl$。")+
 p("<strong>圆锥：</strong>$V=\\dfrac{1}{3}\\pi r^2 h$，$S_{侧}=\\pi r l$，$S_{全}=\\pi r^2+\\pi r l$（母线 $l=\\sqrt{r^2+h^2}$）。")+
 p("<strong>棱台：</strong>$V=\\dfrac{h}{3}\\big(S_{上}+\\sqrt{S_{上}S_{下}}+S_{下}\\big)$，$S_{侧}=\\dfrac{1}{2}(C_{上}+C_{下})l$。")+
 p("<strong>圆台：</strong>$V=\\dfrac{\\pi h}{3}\\big(r^2+rR+R^2\\big)$，$S_{侧}=\\pi(r+R)l$。")+
 p("<strong>球：</strong>$V=\\dfrac{4}{3}\\pi R^3$，$S_{球}=4\\pi R^2$。")+
 p("<strong>正方体与正四面体：</strong>正方体（棱长 $a$）：$V=a^3$、$S_{全}=6a^2$、体对角线 $\\sqrt3a$；正四面体（棱长 $a$）：$V=\\dfrac{\\sqrt2}{12}a^3$、$S_{全}=\\sqrt3 a^2$。")+
 der(
  p("<strong>一、台体公式统一了柱与锥。</strong>棱台（圆台）的体积公式 $V=\\dfrac{h}{3}\\big(S_{上}+\\sqrt{S_{上}S_{下}}+S_{下}\\big)$ 中，当上底面<strong>缩</strong>到与下底面相等，即 $S_{上}=S_{下}=S$ 时：")+
  fml("V=\\dfrac{h}{3}(S+S+S)=Sh")+
  p("退化为柱体体积；当上底面缩为一点，即 $S_{上}=0$ 时：")+
  fml("V=\\dfrac{h}{3}S_{下}=\\dfrac{1}{3}Sh")+
  p("退化为锥体体积。可见柱、锥都是台的特例，台体公式是三者统一的桥梁。")+
  p("<strong>二、圆台侧面积公式的推导。</strong>圆台侧面展开为扇环，设大、小扇形母线为 $l_1,l_2$，由相似 $\\dfrac{l_1}{l_2}=\\dfrac{R}{r}$ 与 $l_1-l_2=l$ 解得 $l_2=\\dfrac{r l}{R-r}$、$l_1=\\dfrac{R l}{R-r}$，故侧面积等于两扇形面积之差：")+
  fml("S_{侧}=\\pi R l_1-\\pi r l_2=\\dfrac{\\pi l}{R-r}\\big(R^2-r^2\\big)=\\pi(R+r)l")+
  p("<strong>三、球体积公式的推导。</strong>取半径 $R$ 的半球与「底面半径 $R$、高 $R$ 的圆柱挖去同底等高的倒圆锥」作对比。距底面（球心所在水平面）为 $x$ 处，半球的截面半径为 $\\sqrt{R^2-x^2}$、面积 $\\pi(R^2-x^2)$；挖空圆柱的截面为外径 $R$、内径 $x$ 的圆环，面积 $\\pi R^2-\\pi x^2$。两者处处相等，由祖暅原理体积相等：")+
  fml("V_{\\text{半球}}=\\pi R^2\\cdot R-\\dfrac{1}{3}\\pi R^2\\cdot R=\\dfrac{2}{3}\\pi R^3,\\qquad V_{\\text{球}}=\\dfrac{4}{3}\\pi R^3")+
  p("<strong>四、球表面积公式的推导。</strong>把球面分割成许多小球面片，各片与球心连成小锥体，其体积之和等于球体积：")+
  fml("V_{\\text{球}}=\\dfrac{1}{3}RS_{\\text{球}}\\;\\Rightarrow\\;S_{\\text{球}}=\\dfrac{3V_{\\text{球}}}{R}=4\\pi R^2"))+
 app(p("<strong>应用：</strong>求容器容积、材料用量、堆积体体积等问题都要用到上表。例如已知球的体积可反求半径 $R=\\sqrt[3]{\\dfrac{3V}{4\\pi}}$，已知圆柱容积 $V$ 与高 $h$ 可求底面半径 $r=\\sqrt{\\dfrac{V}{\\pi h}}$；正多面体的顶点数、棱数、面数之间由欧拉公式 $V-E+F=2$ 相联系，可互相推算。"))+
 note(p("记忆要点：柱体 $V=Sh$，锥体 $V=\\dfrac{1}{3}Sh$，台体取「上、下底面积的平方根型平均」形式 $V=\\dfrac{h}{3}(S_{上}+\\sqrt{S_{上}S_{下}}+S_{下})$——当 $S_{上}=S_{下}$ 得柱、$S_{上}=0$ 得锥；侧面积只算侧面，全面积须再加上、下底；旋转体的侧面积多用展开图求得，而球的表面积由「无限分割」得到 $S=4\\pi R^2$。")))
}
]}
]
# ============ 第七章 解析几何 ============
# ============ 第七章 解析几何 ============
ch7_sections = [
{"name":"7.1 坐标系与参数方程","color":"#0891b2","desc":"极坐标、柱坐标、球坐标、参数方程",
"items":[
{"id":"e7s1-1","name":"极坐标与直角坐标","tags":["def","thm","der","exa"],"brief":"极坐标定义、与直角坐标互化、常见极坐标方程。",
"fig":"polar_coord","figCap":"极坐标 $P(\\rho,\\theta)$，极径与极角",
"body":wrap(
 defn("极坐标",p("平面上取定点 $O$ 为<strong>极点</strong>，以 $O$ 出发的射线 $Ox$ 为<strong>极轴</strong>，并规定逆时针为正方向。点 $P$ 的位置由它到极点的距离 $\\rho=|OP|$ 与射线 $Ox$ 到 $OP$ 的角 $\\theta$ 确定，有序数对 $(\\rho,\\theta)$ 称点 $P$ 的<strong>极坐标</strong>；$\\rho$ 称极径（$\\rho\\ge0$），$\\theta$ 称极角。"))+
 thm("直角坐标与极坐标互化",p("以极点为原点、极轴为 $x$ 轴正方向建立直角坐标系，则")+
 fml("x=\\rho\\cos\\theta,\\qquad y=\\rho\\sin\\theta")+
 p("反之")+
 fml("\\rho^2=x^2+y^2,\\qquad \\tan\\theta=\\dfrac{y}{x}\\ (x\\neq0)"))+
 der(p("<strong>第一步 · 正变换：</strong>设点 $P$ 的直角坐标为 $(x,y)$、极坐标为 $(\\rho,\\theta)$。过 $P$ 作 $x$ 轴的垂线，垂足为 $M$，则 $|OM|=x$、$|MP|=y$，在直角三角形 $OMP$ 中斜边 $|OP|=\\rho$，由锐角三角函数定义")+
 fml("\\cos\\theta=\\dfrac{|OM|}{|OP|}=\\dfrac{x}{\\rho},\\qquad \\sin\\theta=\\dfrac{|MP|}{|OP|}=\\dfrac{y}{\\rho}")+
 p("<strong>第二步 · 反变换：</strong>把上式两边分别乘 $\\rho$，即得 $x=\\rho\\cos\\theta$、$y=\\rho\\sin\\theta$。将两式平方相加消去 $\\theta$：")+
 fml("x^2+y^2=\\rho^2(\\cos^2\\theta+\\sin^2\\theta)=\\rho^2")+
 p("<strong>第三步 · 求极角：</strong>由 $\\rho^2=x^2+y^2$ 得 $\\rho=\\sqrt{x^2+y^2}$；两式相除消去 $\\rho$ 得 $\\tan\\theta=\\dfrac{y}{x}$。由于 $\\tan\\theta$ 以 $\\pi$ 为周期，须结合 $x,y$ 的符号（所在象限）确定 $\\theta$ 的具体值。")+
 p("<strong>第四步 · 化极坐标方程为直角坐标方程：</strong>常利用 $\\rho\\cos\\theta=x$、$\\rho\\sin\\theta=y$、$\\rho^2=x^2+y^2$ 三个代换。例如圆 $x^2+y^2=r^2$ 化为 $\\rho=r$；直线 $x=a$ 化为 $\\rho\\cos\\theta=a$；直线 $\\rho\\cos(\\theta-\\theta_0)=d$ 表示到极点距离为 $d$、法向角为 $\\theta_0$ 的直线。"))+
 exa(p("<strong>例 1：</strong>将 $\\rho=2\\cos\\theta$ 化为直角坐标方程。两边同乘 $\\rho$ 得 $\\rho^2=2\\rho\\cos\\theta$，代换 $\\rho^2=x^2+y^2$、$\\rho\\cos\\theta=x$ 得 $x^2+y^2=2x$，配方得")+
 fml("(x-1)^2+y^2=1")+
 p("即圆心 $(1,0)$、半径 $1$ 的圆，且过极点。")+
 p("<strong>例 2：</strong>以焦点为极点的圆锥曲线统一极坐标方程为 $\\rho=\\dfrac{p}{1-e\\cos\\theta}$（$e$ 为离心率）：$e<1$ 为椭圆，$e=1$ 为抛物线，$e>1$ 为双曲线。"))+
 note(p("极坐标不唯一：$(\\rho,\\theta)$ 与 $(\\rho,\\theta+2k\\pi)$（$k\\in\\mathbb{Z}$）表示同一点；若允许 $\\rho<0$，则 $(-\\rho,\\theta+\\pi)$ 也与之重合。通常限定 $\\rho\\ge0,\\ 0\\le\\theta<2\\pi$ 使表示基本唯一。")))
},
{"id":"e7s1-2","name":"参数方程与坐标变换","tags":["def","thm","der","exa"],"brief":"参数方程概念、直线圆的参数方程、平移与旋转变换。",
"body":wrap(
 defn("参数方程",p("若当参数 $t$ 在某区间内变动时，曲线上点的坐标 $(x,y)$ 满足联立方程")+
 fml("\\begin{cases}x=f(t)\\\\ y=g(t)\\end{cases}")+
 p("且反过来曲线上每一点都对应某个 $t$，则称此为曲线的<strong>参数方程</strong>，$t$ 称<strong>参数</strong>。"))+
 thm("常见曲线的参数方程",p("")+
 fml("\\text{过}(x_0,y_0)\\text{方向向量}(a,b)\\text{的直线}:\\ \\begin{cases}x=x_0+at\\\\ y=y_0+bt\\end{cases}")+
 fml("\\text{圆心}(x_0,y_0)\\text{半径}r\\text{的圆}:\\ \\begin{cases}x=x_0+r\\cos t\\\\ y=y_0+r\\sin t\\end{cases}")+
 fml("\\text{椭圆}\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1:\\ \\begin{cases}x=a\\cos t\\\\ y=b\\sin t\\end{cases}"))+
 der(p("<strong>第一步 · 圆参数方程推导：</strong>圆上动点 $P(x,y)$ 与圆心 $C(x_0,y_0)$ 的连线 $CP$ 与 $x$ 轴正向成角 $t$，则位移向量 $\\overrightarrow{CP}=(x-x_0,\\ y-y_0)$ 的方向由 $t$ 确定，长度为 $r$，故 $\\overrightarrow{CP}=(r\\cos t,\\ r\\sin t)$，即")+
 fml("x=x_0+r\\cos t,\\qquad y=y_0+r\\sin t")+
 p("<strong>第二步 · 椭圆参数方程推导：</strong>把 $x=a\\cos t$ 代入椭圆方程，得 $\\dfrac{a^2\\cos^2t}{a^2}+\\dfrac{y^2}{b^2}=1$，即 $\\dfrac{y^2}{b^2}=1-\\cos^2t=\\sin^2t$，故 $y=\\pm b\\sin t$，取正号得")+
 fml("y=b\\sin t\\quad\\Longrightarrow\\quad \\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=\\cos^2t+\\sin^2t=1")+
 p("<strong>第三步 · 消参化普通方程：</strong>由参数方程解出 $t$ 再代入（或用三角恒等式 $\\cos^2t+\\sin^2t=1$）消去 $t$。例如 $\\begin{cases}x=2t\\\\ y=t^2\\end{cases}$，由 $t=\\dfrac{x}{2}$ 得 $y=\\left(\\dfrac{x}{2}\\right)^2=\\dfrac{x^2}{4}$，即抛物线 $x^2=4y$。")+
 p("<strong>第四步 · 平移变换：</strong>把原点移到 $O'(h,k)$、坐标轴方向不变，新坐标 $(x',y')$ 与旧坐标关系为")+
 fml("\\begin{cases}x=x'+h\\\\ y=y'+k\\end{cases}\\quad\\Longleftrightarrow\\quad \\begin{cases}x'=x-h\\\\ y'=y-k\\end{cases}")+
 p("<strong>第五步 · 旋转变换：</strong>坐标轴绕原点逆时针旋转角 $\\alpha$，新 $x'$ 轴正方向在旧系中为 $\\vec{e_1}=(\\cos\\alpha,\\sin\\alpha)$，新 $y'$ 轴正方向为 $\\vec{e_2}=(-\\sin\\alpha,\\cos\\alpha)$。点 $P=x'\\vec{e_1}+y'\\vec{e_2}$，展开分量得")+
 fml("\\begin{cases}x=x'\\cos\\alpha-y'\\sin\\alpha\\\\ y=x'\\sin\\alpha+y'\\cos\\alpha\\end{cases}"))+
 exa(p("<strong>例：</strong>曲线 $\\begin{cases}x=\\cos t\\\\ y=1+\\sin t\\end{cases}$（$t\\in[0,2\\pi]$）中，由 $x^2+(y-1)^2=\\cos^2t+\\sin^2t=1$ 知它是圆心 $(0,1)$、半径 $1$ 的圆。")))
},
{"id":"e7s1-3","name":"柱坐标与球坐标","tags":["def","thm","der","exa"],"brief":"柱坐标、球坐标定义及与直角坐标互化。",
"body":wrap(
 defn("柱坐标",p("空间中取与极坐标相同的极点与极轴，点 $P$ 的<strong>柱坐标</strong>为 $(\\rho,\\theta,z)$：$(\\rho,\\theta)$ 是 $P$ 在 $xy$ 平面上投影 $P'$ 的极坐标，$z$ 是 $P$ 到该平面的有向高度。"))+
 defn("球坐标",p("以原点 $O$ 为顶点，点 $P$ 的<strong>球坐标</strong>为 $(r,\\theta,\\varphi)$：$r=|OP|$ 为到原点的距离（$r\\ge0$），$\\theta$ 为<strong>方位角</strong>（投影 $OP'$ 与 $x$ 轴正向的角），$\\varphi$ 为<strong>天顶角</strong>（$z$ 轴正向与 $OP$ 的角，$0\\le\\varphi\\le\\pi$）。"))+
 thm("柱、球坐标与直角坐标互化",p("")+
 fml("\\text{柱坐标}:\\ x=\\rho\\cos\\theta,\\quad y=\\rho\\sin\\theta,\\quad z=z")+
 fml("\\text{球坐标}:\\ x=r\\sin\\varphi\\cos\\theta,\\quad y=r\\sin\\varphi\\sin\\theta,\\quad z=r\\cos\\varphi"))+
 der(p("<strong>第一步 · 柱坐标推导：</strong>柱坐标是极坐标沿 $z$ 方向的直接推广。$P(x,y,z)$ 与其投影 $P'(x,y,0)$ 有相同的 $x,y$ 坐标，而 $P'$ 的极坐标为 $(\\rho,\\theta)$，由极坐标正变换即得 $x=\\rho\\cos\\theta$、$y=\\rho\\sin\\theta$，且 $z=z$。")+
 p("<strong>第二步 · 球坐标求高度：</strong>过 $P$ 作 $z$ 轴的垂线，垂足为 $M$。在直角三角形 $OMP$ 中 $|OP|=r$、$\\angle POM=\\varphi$，故由三角定义")+
 fml("z=r\\cos\\varphi")+
 p("<strong>第三步 · 球坐标求投影半径：</strong>同一三角形中 $P$ 到 $z$ 轴的垂距即投影 $OP'$ 的长度")+
 fml("\\rho'=|OP|\\sin\\varphi=r\\sin\\varphi")+
 p("<strong>第四步 · 合成水平坐标：</strong>投影 $OP'$ 与 $x$ 轴正向夹角为方位角 $\\theta$，由极坐标正变换得")+
 fml("x=\\rho'\\cos\\theta=r\\sin\\varphi\\cos\\theta,\\qquad y=\\rho'\\sin\\theta=r\\sin\\varphi\\sin\\theta")+
 p("<strong>第五步 · 反解与体积元：</strong>由前三式平方相加得 $r^2=x^2+y^2+z^2$；在球坐标下体积元为 $dV=r^2\\sin\\varphi\\,dr\\,d\\varphi\\,d\\theta$，这是三重积分换元的基础。"))+
 exa(p("<strong>例：</strong>直角坐标 $(0,0,1)$ 的球坐标：$r=\\sqrt{0^2+0^2+1^2}=1$，由 $z=r\\cos\\varphi$ 得 $\\cos\\varphi=1$，即 $\\varphi=0$，方位角可取 $\\theta=0$，故为 $(1,0,0)$；球面 $x^2+y^2+z^2=R^2$ 的球坐标方程为 $r=R$。")))
}
]},
{"name":"7.2 向量","color":"#0e7490","desc":"平面向量与空间向量的运算、数量积与坐标表示",
"items":[
{"id":"e7s2-1","name":"平面向量及其运算","tags":["def","thm","der","exa"],"brief":"向量概念、加减数乘、坐标运算、数量积、夹角与投影推导。",
"body":wrap(
 defn("向量",p("既有大小又有方向的量称<strong>向量</strong>，记 $\\vec{a}$；其大小称<strong>模</strong> $|\\vec{a}|$。在平面直角坐标系中，以 $\\vec{i},\\vec{j}$ 为两坐标轴正方向的单位向量，则 $\\vec{a}=x\\vec{i}+y\\vec{j}$，简记 $\\vec{a}=(x,y)$。模为 $1$ 的向量称单位向量，模为 $0$ 的称零向量。"))+
 thm("线性运算（坐标）",p("")+
 fml("\\vec{a}\\pm\\vec{b}=(x_1\\pm x_2,\\ y_1\\pm y_2),\\qquad \\lambda\\vec{a}=(\\lambda x_1,\\ \\lambda y_1)"))+
 thm("数量积",p("")+
 fml("\\vec{a}\\cdot\\vec{b}=|\\vec{a}||\\vec{b}|\\cos\\theta=x_1x_2+y_1y_2"))+
 thm("共线、垂直与投影",p("$\\vec{a}\\parallel\\vec{b}\\Leftrightarrow x_1y_2-x_2y_1=0$（即存在 $\\lambda$ 使 $\\vec{a}=\\lambda\\vec{b}$）；$\\vec{a}\\perp\\vec{b}\\Leftrightarrow x_1x_2+y_1y_2=0$；$\\vec{b}$ 在 $\\vec{a}$ 上的投影为 $\\dfrac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}|}$。"))+
 der(p("<strong>第一步 · 加法坐标推导：</strong>按单位基底分解 $\\vec{a}=x_1\\vec{i}+y_1\\vec{j}$、$\\vec{b}=x_2\\vec{i}+y_2\\vec{j}$，利用 $\\vec{i},\\vec{j}$ 的分配律合并同类项：")+
 fml("\\vec{a}+\\vec{b}=(x_1+x_2)\\vec{i}+(y_1+y_2)\\vec{j}=(x_1+x_2,\\ y_1+y_2)")+
 p("<strong>第二步 · 数量积坐标推导：</strong>由 $\\vec{i}\\cdot\\vec{i}=\\vec{j}\\cdot\\vec{j}=1$、$\\vec{i}\\cdot\\vec{j}=0$ 及数量积的双线性展开：")+
 fml("\\vec{a}\\cdot\\vec{b}=(x_1\\vec{i}+y_1\\vec{j})\\cdot(x_2\\vec{i}+y_2\\vec{j})=x_1x_2+y_1y_2")+
 p("<strong>第三步 · 模与夹角推导：</strong>取 $\\vec{b}=\\vec{a}$ 得 $|\\vec{a}|^2=\\vec{a}\\cdot\\vec{a}=x_1^2+y_1^2$，故 $|\\vec{a}|=\\sqrt{x_1^2+y_1^2}$；再由数量积的几何定义反解")+
 fml("\\cos\\theta=\\dfrac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}||\\vec{b}|}=\\dfrac{x_1x_2+y_1y_2}{\\sqrt{x_1^2+y_1^2}\\,\\sqrt{x_2^2+y_2^2}}")+
 p("<strong>第四步 · 投影公式推导：</strong>$\\vec{b}$ 在 $\\vec{a}$ 方向上的投影定义为 $|\\vec{b}|\\cos\\theta$，而 $\\vec{a}\\cdot\\vec{b}=|\\vec{a}||\\vec{b}|\\cos\\theta$，两边除以 $|\\vec{a}|$ 得投影 $=\\dfrac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}|}$；其正负表示投影与 $\\vec{a}$ 同向或反向。"))+
 exa(p("<strong>例：</strong>$\\vec{a}=(1,2),\\vec{b}=(3,-1)$：$\\vec{a}+\\vec{b}=(4,1)$，$\\vec{a}\\cdot\\vec{b}=3-2=1$，$|\\vec{a}|=\\sqrt5$，$\\cos\\theta=\\dfrac{1}{\\sqrt5\\cdot\\sqrt{10}}$，$\\vec{b}$ 在 $\\vec{a}$ 上的投影为 $\\dfrac{1}{\\sqrt5}$。"))+
 note(p("三角不等式 $|\\vec{a}+\\vec{b}|\\le|\\vec{a}|+|\\vec{b}|$ 由 $|\\vec{a}+\\vec{b}|^2=|\\vec{a}|^2+2\\vec{a}\\cdot\\vec{b}+|\\vec{b}|^2\\le(|\\vec{a}|+|\\vec{b}|)^2$ 开方即得，等号当且仅当 $\\vec{a},\\vec{b}$ 同向时成立。")))
},
{"id":"e7s2-2","name":"空间向量","tags":["def","thm","der","exa"],"brief":"空间向量坐标运算、数量积、向量积（叉积）、夹角与空间距离。",
"body":wrap(
 defn("空间向量",p("空间向量 $\\vec{a}=(x,y,z)$，以 $\\vec{i},\\vec{j},\\vec{k}$ 为三坐标轴正方向的单位向量。模 $|\\vec{a}|=\\sqrt{x^2+y^2+z^2}$；空间中任意向量可由三个不共面的向量唯一线性表示。"))+
 thm("数量积与距离",p("")+
 fml("\\vec{a}\\cdot\\vec{b}=x_1x_2+y_1y_2+z_1z_2=|\\vec{a}||\\vec{b}|\\cos\\langle\\vec{a},\\vec{b}\\rangle")+
 fml("|P_1P_2|=\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}"))+
 thm("向量积（叉积）",p("$\\vec{a}\\times\\vec{b}$ 是一个向量，模 $|\\vec{a}\\times\\vec{b}|=|\\vec{a}||\\vec{b}|\\sin\\theta$（等于以 $\\vec{a},\\vec{b}$ 为邻边的平行四边形面积），方向同时垂直于 $\\vec{a},\\vec{b}$，且 $(\\vec{a},\\vec{b},\\vec{a}\\times\\vec{b})$ 构成右手系。坐标式为三阶行列式")+
 fml("\\vec{a}\\times\\vec{b}=\\begin{vmatrix}\\vec{i}&\\vec{j}&\\vec{k}\\\\ x_1&y_1&z_1\\\\ x_2&y_2&z_2\\end{vmatrix}=(y_1z_2-z_1y_2,\\ z_1x_2-x_1z_2,\\ x_1y_2-y_1x_2)"))+
 der(p("<strong>第一步 · 数量积坐标推导：</strong>由 $\\vec{a}\\cdot\\vec{b}=|\\vec{a}||\\vec{b}|\\cos\\theta$ 与余弦定理 $|\\vec{a}-\\vec{b}|^2=|\\vec{a}|^2+|\\vec{b}|^2-2\\vec{a}\\cdot\\vec{b}$，解出")+
 fml("\\vec{a}\\cdot\\vec{b}=\\dfrac{|\\vec{a}|^2+|\\vec{b}|^2-|\\vec{a}-\\vec{b}|^2}{2}")+
 p("<strong>第二步：</strong>代入 $|\\vec{a}|^2=x_1^2+y_1^2+z_1^2$、$|\\vec{b}|^2=x_2^2+y_2^2+z_2^2$、$|\\vec{a}-\\vec{b}|^2=(x_1-x_2)^2+(y_1-y_2)^2+(z_1-z_2)^2$，展开后前后项相消得")+
 fml("\\vec{a}\\cdot\\vec{b}=x_1x_2+y_1y_2+z_1z_2")+
 p("<strong>第三步 · 夹角与垂直：</strong>由数量积几何定义反解 $\\cos\\theta=\\dfrac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}||\\vec{b}|}$，分子分母用坐标代入即得夹角余弦公式；$\\vec{a}\\perp\\vec{b}\\Leftrightarrow\\vec{a}\\cdot\\vec{b}=0$，$\\vec{a}\\parallel\\vec{b}\\Leftrightarrow\\vec{a}=\\lambda\\vec{b}$。")+
 p("<strong>第四步 · 向量积坐标推导：</strong>由循环关系 $\\vec{i}\\times\\vec{j}=\\vec{k}$、$\\vec{j}\\times\\vec{k}=\\vec{i}$、$\\vec{k}\\times\\vec{i}=\\vec{j}$ 与 $\\vec{i}\\times\\vec{i}=\\vec{j}\\times\\vec{j}=\\vec{k}\\times\\vec{k}=0$，把 $(x_1\\vec{i}+y_1\\vec{j}+z_1\\vec{k})\\times(x_2\\vec{i}+y_2\\vec{j}+z_2\\vec{k})$ 按分配律展开，再用反对称性 $\\vec{j}\\times\\vec{i}=-\\vec{k}$ 等合并同类项：")+
 fml("\\vec{a}\\times\\vec{b}=(y_1z_2-z_1y_2)\\vec{i}+(z_1x_2-x_1z_2)\\vec{j}+(x_1y_2-y_1x_2)\\vec{k}")+
 p("<strong>第五步 · 模的恒等式：</strong>由上式可得拉格朗日恒等式 $|\\vec{a}\\times\\vec{b}|^2=|\\vec{a}|^2|\\vec{b}|^2-(\\vec{a}\\cdot\\vec{b})^2=|\\vec{a}|^2|\\vec{b}|^2\\sin^2\\theta$，说明叉积模等于平行四边形面积。"))+
 exa(p("<strong>例：</strong>$\\vec{a}=(1,0,1),\\vec{b}=(0,1,1)$：$\\vec{a}\\cdot\\vec{b}=1$，$|\\vec{a}|=|\\vec{b}|=\\sqrt2$，$\\cos\\theta=\\dfrac{1}{2}$，$\\theta=60^\\circ$；$\\vec{a}\\times\\vec{b}=(-1,-1,1)$，模为 $\\sqrt3$，等于以两者为邻边的平行四边形面积。"))+
 note(p("混合积 $(\\vec{a}\\times\\vec{b})\\cdot\\vec{c}$ 的绝对值等于以 $\\vec{a},\\vec{b},\\vec{c}$ 为棱的平行六面体体积；三向量共面 $\\Leftrightarrow$ 混合积为零，空间四点共面亦可用此判定。")))
}
]},
{"name":"7.3 直线与圆","color":"#0e7490","desc":"直线方程、圆的方程、距离公式",
"items":[
{"id":"e7s3-1","name":"直线方程与位置关系","tags":["def","thm","der","exa"],"brief":"点斜式、斜截式、一般式及两直线位置关系。",
"body":wrap(
 defn("直线方程的形式",p("① <strong>点斜式</strong> $y-y_0=k(x-x_0)$（过 $(x_0,y_0)$、斜率 $k$）；② <strong>斜截式</strong> $y=kx+b$（$b$ 为 $y$ 轴截距）；③ <strong>两点式</strong> $\\dfrac{y-y_1}{y_2-y_1}=\\dfrac{x-x_1}{x_2-x_1}$；④ <strong>一般式</strong> $Ax+By+C=0$（$A,B$ 不同时为 $0$）。"))+
 thm("两直线的位置关系",p("设 $l_1:A_1x+B_1y+C_1=0$、$l_2:A_2x+B_2y+C_2=0$，法向量 $\\vec{n_1}=(A_1,B_1)$、$\\vec{n_2}=(A_2,B_2)$：")+
 fml("l_1\\parallel l_2\\ \\Leftrightarrow\\ A_1B_2-A_2B_1=0\\ (\\text{且非重合})")+
 fml("l_1\\perp l_2\\ \\Leftrightarrow\\ A_1A_2+B_1B_2=0"))+
 thm("夹角公式",p("")+
 fml("\\tan\\varphi=\\left|\\dfrac{k_2-k_1}{1+k_1k_2}\\right|\\quad(k_1k_2\\neq-1)"))+
 der(p("<strong>第一步 · 斜率的几何来源：</strong>直线的倾角 $\\alpha\\in[0,\\pi)$ 定义为直线向上的方向与 $x$ 轴正向的夹角，斜率 $k=\\tan\\alpha$。取直线上两点 $(x_1,y_1),(x_2,y_2)$，由 $\\tan\\alpha=\\dfrac{y_2-y_1}{x_2-x_1}$ 得斜率公式，点斜式即由 $k=\\dfrac{y-y_0}{x-x_0}$ 变形而来。")+
 p("<strong>第二步 · 平行与垂直的向量解释：</strong>直线 $Ax+By+C=0$ 的一个法向量为 $\\vec{n}=(A,B)$：因可取方向向量 $(B,-A)$，而 $(B,-A)\\cdot(A,B)=AB-BA=0$。两直线平行即法向量平行，垂直即法向量垂直，于是")+
 fml("\\parallel:\\ A_1B_2-A_2B_1=0,\\qquad \\perp:\\ A_1A_2+B_1B_2=0")+
 p("<strong>第三步 · 夹角公式推导：</strong>两直线方向向量可取 $\\vec{v_1}=(1,k_1),\\vec{v_2}=(1,k_2)$，由向量夹角余弦公式")+
 fml("\\cos\\varphi=\\dfrac{\\vec{v_1}\\cdot\\vec{v_2}}{|\\vec{v_1}||\\vec{v_2}|}=\\dfrac{1+k_1k_2}{\\sqrt{1+k_1^2}\\,\\sqrt{1+k_2^2}}")+
 p("<strong>第四步 · 化为正切形式：</strong>取 $\\varphi$ 为锐角并利用 $\\tan^2\\varphi=\\dfrac{1}{\\cos^2\\varphi}-1$，代入上式整理，得 $\\tan\\varphi=\\left|\\dfrac{k_2-k_1}{1+k_1k_2}\\right|$；当 $k_1k_2=-1$ 时分母为零，两直线垂直。"))+
 exa(p("<strong>例：</strong>过点 $(1,2)$、斜率 $-1$ 的直线为 $y-2=-(x-1)$，即 $x+y-3=0$；判断 $l_1:x+2y-1=0$ 与 $l_2:2x+4y+3=0$，因 $1\\cdot4-2\\cdot2=0$ 且常数项不同，故两直线平行。"))+
 note(p("当直线斜率不存在（垂直于 $x$ 轴）时，应单独写成 $x=x_0$，夹角与平行垂直判定改用一般式的法向量形式，以避免除零。")))
},
{"id":"e7s3-2","name":"圆的方程与切线","tags":["def","thm","der","exa"],"brief":"圆的标准方程、一般方程、切线方程与弦长。",
"fig":"circle","figCap":"圆 $(x-a)^2+(y-b)^2=r^2$，圆心 $(a,b)$ 半径 $r$",
"body":wrap(
 defn("圆的方程",p("① <strong>标准方程</strong> $(x-a)^2+(y-b)^2=r^2$，圆心 $(a,b)$、半径 $r$；② <strong>一般方程</strong> $x^2+y^2+Dx+Ey+F=0$，当 $D^2+E^2-4F>0$ 时表示圆，圆心 $\\left(-\\dfrac{D}{2},-\\dfrac{E}{2}\\right)$、半径 $\\dfrac{1}{2}\\sqrt{D^2+E^2-4F}$。"))+
 thm("切线方程",p("过圆 $(x-a)^2+(y-b)^2=r^2$ 上一点 $(x_0,y_0)$ 的切线为")+
 fml("(x_0-a)(x-a)+(y_0-b)(y-b)=r^2"))+
 der(p("<strong>第一步 · 标准方程推导：</strong>圆是到定点 $C(a,b)$ 距离恒等于 $r$ 的点的集合，由两点距离公式 $\\sqrt{(x-a)^2+(y-b)^2}=r$，两边平方即得 $(x-a)^2+(y-b)^2=r^2$。")+
 p("<strong>第二步 · 一般方程推导：</strong>把标准方程展开")+
 fml("x^2+y^2-2ax-2by+(a^2+b^2-r^2)=0")+
 p("令 $D=-2a,\\ E=-2b,\\ F=a^2+b^2-r^2$ 即得一般式；反解 $a=-\\dfrac{D}{2},\\ b=-\\dfrac{E}{2}$，且 $r^2=\\dfrac{D^2+E^2}{4}-F=\\dfrac{D^2+E^2-4F}{4}>0$ 时才表示实圆。")+
 p("<strong>第三步 · 切线推导：</strong>切线过点 $(x_0,y_0)$ 且与过该点的半径垂直。切点处半径向量 $\\overrightarrow{CP}=(x_0-a,\\ y_0-b)$，切线上任一点 $(x,y)$ 满足 $(x-x_0,\\ y-y_0)\\perp\\overrightarrow{CP}$，故")+
 fml("(x_0-a)(x-x_0)+(y_0-b)(y-y_0)=0")+
 p("<strong>第四步 · 化简：</strong>把上式改写为 $(x_0-a)(x-a+a-x_0)+(y_0-b)(y-b+b-y_0)=0$，注意 $(x_0-a)^2+(y_0-b)^2=r^2$，整理即得 $(x_0-a)(x-a)+(y_0-b)(y-b)=r^2$。")+
 p("<strong>第五步 · 弦长公式：</strong>圆心到直线 $Ax+By+C=0$ 的距离 $d=\\dfrac{|Aa+Bb+C|}{\\sqrt{A^2+B^2}}$，被圆截得的弦长为 $2\\sqrt{r^2-d^2}$（由半径、弦心距、半弦长构成的直角三角形）。"))+
 exa(p("<strong>例：</strong>圆 $x^2+y^2=4$ 上点 $(1,\\sqrt3)$ 处的切线为 $1\\cdot x+\\sqrt3\\cdot y=4$，即 $x+\\sqrt3y=4$；圆心到该切线的距离 $\\dfrac{|-4|}{\\sqrt{1+3}}=2=r$，验证相切。")))
},
{"id":"e7s3-3","name":"距离公式","tags":["thm","der","exa"],"brief":"两点距离、点到直线距离、平行线距离的推导。",
"body":wrap(
 thm("三种距离公式",p("")+
 fml("d_{\\text{两点}}=\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}")+
 fml("d_{\\text{点线}}=\\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}")+
 fml("d_{\\text{平行线}}=\\dfrac{|C_1-C_2|}{\\sqrt{A^2+B^2}}\\quad(A_1=A_2,\\ B_1=B_2)"))+
 der(p("<strong>第一步 · 两点距离推导：</strong>设 $P_1(x_1,y_1),P_2(x_2,y_2)$，以 $P_1P_2$ 为斜边作直角三角形，两直角边长分别为 $|x_2-x_1|$ 与 $|y_2-y_1|$，由勾股定理 $|P_1P_2|^2=(x_2-x_1)^2+(y_2-y_1)^2$，开方即得。")+
 p("<strong>第二步 · 点线距离（向量法）：</strong>直线 $l:Ax+By+C=0$ 的法向量 $\\vec{n}=(A,B)$，单位法向量 $\\vec{n_0}=\\dfrac{\\vec{n}}{\\sqrt{A^2+B^2}}$。设 $Q$ 为点 $P_0(x_0,y_0)$ 在 $l$ 上的垂足，则 $\\overrightarrow{P_0Q}\\parallel\\vec{n}$，可设 $\\overrightarrow{P_0Q}=t\\,\\vec{n_0}$，所求距离 $d=|t|$。")+
 p("<strong>第三步 · 由垂足在直线上求 $t$：</strong>把垂足坐标 $\\left(x_0+\\dfrac{tA}{\\sqrt{A^2+B^2}},\\ y_0+\\dfrac{tB}{\\sqrt{A^2+B^2}}\\right)$ 代入直线方程：")+
 fml("A\\left(x_0+\\dfrac{tA}{\\sqrt{A^2+B^2}}\\right)+B\\left(y_0+\\dfrac{tB}{\\sqrt{A^2+B^2}}\\right)+C=0")+
 p("即 $Ax_0+By_0+C+\\dfrac{t(A^2+B^2)}{\\sqrt{A^2+B^2}}=0$，解得 $t=-\\dfrac{Ax_0+By_0+C}{\\sqrt{A^2+B^2}}$，于是")+
 fml("d=|t|=\\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}")+
 p("<strong>第四步 · 平行线距离推导：</strong>两平行线 $Ax+By+C_1=0$ 与 $Ax+By+C_2=0$ 有相同法向量。在第一条上任取点 $P_0$（满足 $Ax_0+By_0=-C_1$），它到第二条的距离为")+
 fml("d=\\dfrac{|Ax_0+By_0+C_2|}{\\sqrt{A^2+B^2}}=\\dfrac{|C_2-C_1|}{\\sqrt{A^2+B^2}}")+
 p("与 $P_0$ 的选取无关，故为两平行线间的定距离。"))+
 exa(p("<strong>例：</strong>点 $(3,-2)$ 到直线 $4x-3y+1=0$ 的距离 $d=\\dfrac{|12+6+1|}{\\sqrt{16+9}}=\\dfrac{19}{5}$；把 $6x+3y-4=0$ 化为 $2x+y-\\dfrac43=0$，则它与 $2x+y-1=0$ 的距离为 $\\dfrac{\\left|\\dfrac43-1\\right|}{\\sqrt5}=\\dfrac{\\sqrt5}{15}$。")))
}
]},
{"name":"7.4 圆锥曲线","color":"#0e7490","desc":"椭圆、双曲线、抛物线的定义与标准方程",
"items":[
{"id":"e7s4-1","name":"椭圆","tags":["def","thm","der","exa"],"brief":"椭圆定义、标准方程推导、离心率与几何性质。",
"fig":"conic","figCap":"圆锥曲线：用平面截圆锥面得到椭圆、抛物线、双曲线",
"body":wrap(
 defn("椭圆",p("平面内到两个定点 $F_1,F_2$ 的距离之和等于常数 $2a$（且 $2a>|F_1F_2|=2c>0$）的点的轨迹称<strong>椭圆</strong>。$F_1,F_2$ 为焦点，$|F_1F_2|=2c$ 为焦距，$a$ 为长半轴，$b=\\sqrt{a^2-c^2}$ 为短半轴。"))+
 thm("标准方程",p("以 $F_1F_2$ 所在直线为 $x$ 轴、线段中点为原点：")+
 fml("\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1\\quad(a>b>0)")+
 p("焦点为 $(\\pm c,0)$，$c^2=a^2-b^2$；若焦点在 $y$ 轴，则方程为 $\\dfrac{y^2}{a^2}+\\dfrac{x^2}{b^2}=1$，焦点 $(0,\\pm c)$。"))+
 thm("几何性质与离心率",p("范围 $|x|\\le a,\\ |y|\\le b$；顶点 $(\\pm a,0),(0,\\pm b)$；对称轴为两坐标轴、对称中心为原点；长轴长 $2a$、短轴长 $2b$、焦距 $2c$，满足 $a^2=b^2+c^2$；离心率 $e=\\dfrac{c}{a}\\in(0,1)$。"))+
 der(p("<strong>第一步 · 由定义列方程：</strong>以 $F_1F_2$ 为 $x$ 轴、中点为原点，则 $F_1(-c,0),\\ F_2(c,0)$。设动点 $P(x,y)$，由 $|PF_1|+|PF_2|=2a$ 得")+
 fml("\\sqrt{(x+c)^2+y^2}+\\sqrt{(x-c)^2+y^2}=2a")+
 p("<strong>第二步 · 移项平方：</strong>移项得 $\\sqrt{(x+c)^2+y^2}=2a-\\sqrt{(x-c)^2+y^2}$，两边平方：")+
 fml("(x+c)^2+y^2=4a^2-4a\\sqrt{(x-c)^2+y^2}+(x-c)^2+y^2")+
 p("展开消去 $x^2+y^2$ 后得 $4cx=4a^2-4a\\sqrt{(x-c)^2+y^2}$，即 $a\\sqrt{(x-c)^2+y^2}=a^2-cx$。")+
 p("<strong>第三步 · 再平方整式化：</strong>两边再平方")+
 fml("a^2\\left[(x-c)^2+y^2\\right]=(a^2-cx)^2")+
 p("展开整理：$a^2x^2-2a^2cx+a^2c^2+a^2y^2=a^4-2a^2cx+c^2x^2$，消去 $-2a^2cx$ 得 $(a^2-c^2)x^2+a^2y^2=a^2(a^2-c^2)$。")+
 p("<strong>第四步 · 引入 $b$：</strong>因 $a>c$，令 $b^2=a^2-c^2>0$，则上式即 $b^2x^2+a^2y^2=a^2b^2$，两边同除 $a^2b^2$ 得标准方程 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1$。")+
 p("<strong>第五步 · 离心率的意义：</strong>由 $c^2=a^2-b^2$ 得 $e=\\dfrac{c}{a}=\\sqrt{1-\\dfrac{b^2}{a^2}}$。$e\\to0$ 时 $b\\to a$，椭圆趋于圆；$e\\to1$ 时 $b\\to0$，椭圆越扁平。"))+
 exa(p("<strong>例：</strong>椭圆 $\\dfrac{x^2}{25}+\\dfrac{y^2}{9}=1$：$a=5,\\ b=3,\\ c=\\sqrt{25-9}=4$，焦点 $(\\pm4,0)$，$e=\\dfrac45$，长轴长 $10$、短轴长 $6$。"))+
 note(p("推导中出现两次平方，故须验证所得方程上的点都满足原定义（无增根）；由 $a>c$ 保证 $b^2>0$，曲线为实椭圆。")))
},
{"id":"e7s4-2","name":"双曲线","tags":["def","thm","der","exa"],"brief":"双曲线定义、标准方程、渐近线与离心率。",
"body":wrap(
 defn("双曲线",p("平面内到两个定点 $F_1,F_2$ 的距离之差的绝对值等于常数 $2a$（且 $0<2a<|F_1F_2|=2c$）的点的轨迹称<strong>双曲线</strong>。"))+
 thm("标准方程与几何性质",p("焦点在 $x$ 轴：")+
 fml("\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=1\\quad(a,b>0),\\qquad c^2=a^2+b^2")+
 p("焦点 $(\\pm c,0)$；顶点 $(\\pm a,0)$；实轴长 $2a$、虚轴长 $2b$；渐近线 $y=\\pm\\dfrac{b}{a}x$；离心率 $e=\\dfrac{c}{a}\\in(1,+\\infty)$。"))+
 der(p("<strong>第一步 · 由定义列方程：</strong>取 $F_1(-c,0),F_2(c,0)$，动点 $P(x,y)$，由 $\\bigl||PF_1|-|PF_2|\\bigr|=2a$ 得")+
 fml("\\left|\\sqrt{(x+c)^2+y^2}-\\sqrt{(x-c)^2+y^2}\\right|=2a")+
 p("<strong>第二步 · 去绝对值并平方：</strong>去掉绝对值并移项平方，化简过程与椭圆完全类似，得 $cx-a^2=a\\sqrt{(x-c)^2+y^2}$。")+
 p("<strong>第三步 · 再平方整式化：</strong>两边再平方并整理得")+
 fml("(c^2-a^2)x^2-a^2y^2=a^2(c^2-a^2)")+
 p("<strong>第四步 · 引入 $b$：</strong>因 $c>a$，令 $b^2=c^2-a^2>0$，得 $b^2x^2-a^2y^2=a^2b^2$，两边同除 $a^2b^2$ 得 $\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=1$。")+
 p("<strong>第五步 · 渐近线推导：</strong>把方程改写为 $\\dfrac{y^2}{b^2}=\\dfrac{x^2}{a^2}-1$。当 $|x|$ 充分大时 $\\dfrac{x^2}{a^2}-1\\to\\dfrac{x^2}{a^2}$，故 $y\\approx\\pm\\dfrac{b}{a}x$，即双曲线随 $|x|\\to\\infty$ 无限靠近两直线 $y=\\pm\\dfrac{b}{a}x$。")+
 p("<strong>第六步 · 离心率：</strong>$e=\\dfrac{c}{a}=\\sqrt{1+\\dfrac{b^2}{a^2}}$，$e$ 越大开口越开阔，且恒有 $e>1$。"))+
 exa(p("<strong>例：</strong>双曲线 $\\dfrac{x^2}{9}-\\dfrac{y^2}{16}=1$：$a=3,\\ b=4,\\ c=5$，焦点 $(\\pm5,0)$，渐近线 $y=\\pm\\dfrac43x$，$e=\\dfrac53$。"))+
 note(p("若 $a=b$ 称<strong>等轴双曲线</strong>，渐近线 $y=\\pm x$ 互相垂直，离心率 $e=\\sqrt2$；焦点在 $y$ 轴的双曲线方程为 $\\dfrac{y^2}{a^2}-\\dfrac{x^2}{b^2}=1$。")))
},
{"id":"e7s4-3","name":"抛物线","tags":["def","thm","der","exa"],"brief":"抛物线定义、标准方程、焦点准线与离心率。",
"fig":"parabola","figCap":"抛物线 $y^2=2px$，焦点 $F$ 与准线 $l$",
"body":wrap(
 defn("抛物线",p("平面内到定点 $F$（焦点）与到定直线 $l$（准线，$F\\notin l$）的距离相等的点的轨迹称<strong>抛物线</strong>。"))+
 thm("标准方程与几何性质",p("顶点在原点、开口向右：")+
 fml("y^2=2px\\quad(p>0)")+
 p("焦点 $F\\left(\\dfrac{p}{2},0\\right)$，准线 $x=-\\dfrac{p}{2}$，离心率 $e=1$，$p$ 为焦点到准线的距离，对称轴为 $x$ 轴。"))+
 der(p("<strong>第一步 · 建系设点：</strong>取焦点 $F\\left(\\dfrac{p}{2},0\\right)$、准线 $x=-\\dfrac{p}{2}$，则焦点到准线的距离为 $p$。设动点 $P(x,y)$。")+
 p("<strong>第二步 · 由定义列方程：</strong>由 $|PF|=d(P,l)$ 得")+
 fml("\\sqrt{\\left(x-\\dfrac{p}{2}\\right)^2+y^2}=\\left|x+\\dfrac{p}{2}\\right|")+
 p("<strong>第三步 · 平方化简：</strong>两边平方 $x^2-px+\\dfrac{p^2}{4}+y^2=x^2+px+\\dfrac{p^2}{4}$，消去相同项得 $-px+y^2=px$，即")+
 fml("y^2=2px")+
 p("<strong>第四步 · 开口方向的四种标准形式：</strong>由一次项所在轴及符号决定开口方向：")+
 fml("y^2=2px\\ (\\text{右}),\\quad y^2=-2px\\ (\\text{左}),\\quad x^2=2py\\ (\\text{上}),\\quad x^2=-2py\\ (\\text{下})")+
 p("<strong>第五步 · 通径与焦半径：</strong>过焦点且垂直于对称轴的弦称<strong>通径</strong>。把 $x=\\dfrac{p}{2}$ 代入 $y^2=2px$ 得 $y=\\pm p$，故通径长为 $2p$；由定义得焦半径 $|PF|=x+\\dfrac{p}{2}$。"))+
 exa(p("<strong>例：</strong>抛物线 $y^2=8x$：$2p=8$，$p=4$，焦点 $(2,0)$，准线 $x=-2$，通径长 $8$；点 $(2,4)$ 在其上，焦半径 $=2+2=4$。")))
}
]},
{"name":"7.5 空间解析几何","color":"#155e75","desc":"空间直线方程、平面方程、线面关系",
"items":[
{"id":"e7s5-1","name":"空间直线方程","tags":["def","thm","der","exa"],"brief":"空间直线参数方程、对称式方程与一般式方程。",
"body":wrap(
 defn("空间直线的方程",p("空间直线由其上一点 $P_0(x_0,y_0,z_0)$ 与方向向量 $\\vec{v}=(m,n,p)$ 唯一确定，有三种常用形式。① <strong>参数方程</strong>：")+
 fml("\\begin{cases}x=x_0+mt\\\\ y=y_0+nt\\\\ z=z_0+pt\\end{cases}")+
 p("② <strong>对称式（点向式）</strong> $\\dfrac{x-x_0}{m}=\\dfrac{y-y_0}{n}=\\dfrac{z-z_0}{p}$；③ <strong>一般式</strong>（两平面交线）$\\begin{cases}A_1x+B_1y+C_1z+D_1=0\\\\ A_2x+B_2y+C_2z+D_2=0\\end{cases}$。"))+
 thm("两直线夹角",p("方向向量 $\\vec{v_1}=(m_1,n_1,p_1)$、$\\vec{v_2}=(m_2,n_2,p_2)$，夹角 $\\varphi$ 满足")+
 fml("\\cos\\varphi=\\dfrac{|m_1m_2+n_1n_2+p_1p_2|}{\\sqrt{m_1^2+n_1^2+p_1^2}\\,\\sqrt{m_2^2+n_2^2+p_2^2}}"))+
 der(p("<strong>第一步 · 参数方程推导：</strong>设 $P(x,y,z)$ 为直线上任一点，则 $\\overrightarrow{P_0P}=(x-x_0,y-y_0,z-z_0)$ 与方向向量 $\\vec{v}$ 共线，即存在实数 $t$ 使 $\\overrightarrow{P_0P}=t\\vec{v}$，分量形式即参数方程。")+
 p("<strong>第二步 · 对称式推导：</strong>由 $x=x_0+mt$ 解出 $t=\\dfrac{x-x_0}{m}$，同理 $t=\\dfrac{y-y_0}{n}=\\dfrac{z-z_0}{p}$，消去 $t$ 得对称式")+
 fml("\\dfrac{x-x_0}{m}=\\dfrac{y-y_0}{n}=\\dfrac{z-z_0}{p}")+
 p("当 $m,n,p$ 中有零时，对应分子也须为零（如 $m=0$ 时表示 $x=x_0$）。")+
 p("<strong>第三步 · 一般式与方向向量：</strong>两平面 $\\Pi_1,\\Pi_2$ 的法向量为 $\\vec{n_1}=(A_1,B_1,C_1)$、$\\vec{n_2}=(A_2,B_2,C_2)$。当两平面不平行（$\\vec{n_1}\\times\\vec{n_2}\\neq\\vec{0}$）时交线为直线，其方向向量同时垂直于两法向量，故取")+
 fml("\\vec{v}=\\vec{n_1}\\times\\vec{n_2}")+
 p("<strong>第四步 · 夹角公式：</strong>两直线夹角等于其方向向量所成的锐角，故由空间向量夹角公式取绝对值即得上面的 $\\cos\\varphi$ 表达式。"))+
 exa(p("<strong>例：</strong>过点 $(1,2,3)$、方向向量 $(1,0,1)$ 的直线：参数方程 $\\begin{cases}x=1+t\\\\ y=2\\\\ z=3+t\\end{cases}$，对称式 $\\dfrac{x-1}{1}=\\dfrac{z-3}{1},\\ y=2$。")))
},
{"id":"e7s5-2","name":"平面方程","tags":["def","thm","der","exa"],"brief":"平面点法式、一般式与截距式方程。",
"body":wrap(
 defn("平面的方程",p("过点 $P_0(x_0,y_0,z_0)$、法向量 $\\vec{n}=(A,B,C)$ 的平面：① <strong>点法式</strong> $A(x-x_0)+B(y-y_0)+C(z-z_0)=0$；② <strong>一般式</strong> $Ax+By+Cz+D=0$；③ <strong>截距式</strong> $\\dfrac{x}{a}+\\dfrac{y}{b}+\\dfrac{z}{c}=1$（$a,b,c$ 为三个坐标轴上的截距，均非零）。"))+
 thm("两平面夹角",p("法向量 $\\vec{n_1},\\vec{n_2}$，夹角 $\\varphi$ 满足")+
 fml("\\cos\\varphi=\\dfrac{|A_1A_2+B_1B_2+C_1C_2|}{\\sqrt{A_1^2+B_1^2+C_1^2}\\,\\sqrt{A_2^2+B_2^2+C_2^2}}"))+
 der(p("<strong>第一步 · 点法式推导：</strong>平面过 $P_0$、法向量为 $\\vec{n}$，则平面上任一点 $P(x,y,z)$ 满足 $\\overrightarrow{P_0P}\\cdot\\vec{n}=0$，即")+
 fml("A(x-x_0)+B(y-y_0)+C(z-z_0)=0")+
 p("<strong>第二步 · 一般式推导：</strong>展开点法式并令常数项 $D=-Ax_0-By_0-Cz_0$，得 $Ax+By+Cz+D=0$；反之任一形如 $Ax+By+Cz+D=0$（$A,B,C$ 不全为零）的方程都表示一个以 $(A,B,C)$ 为法向量的平面。")+
 p("<strong>第三步 · 截距式推导：</strong>设平面与三坐标轴分别交于 $(a,0,0),(0,b,0),(0,0,c)$，代入一般式得 $Aa+D=0$、$Bb+D=0$、$Cc+D=0$，故 $A=-\\dfrac{D}{a},\\ B=-\\dfrac{D}{b},\\ C=-\\dfrac{D}{c}$。代回并两边除以 $-D$，得")+
 fml("\\dfrac{x}{a}+\\dfrac{y}{b}+\\dfrac{z}{c}=1")+
 p("<strong>第四步 · 夹角公式：</strong>两平面的夹角等于其法向量的夹角（取锐角），由空间向量夹角公式取绝对值即得；两平面垂直 $\\Leftrightarrow A_1A_2+B_1B_2+C_1C_2=0$，平行 $\\Leftrightarrow \\vec{n_1}\\parallel\\vec{n_2}$。"))+
 exa(p("<strong>例：</strong>过点 $(1,2,3)$、法向量 $(1,1,1)$ 的平面：$1(x-1)+1(y-2)+1(z-3)=0$，即 $x+y+z-6=0$；其截距式为 $\\dfrac{x}{6}+\\dfrac{y}{6}+\\dfrac{z}{6}=1$。")))
},
{"id":"e7s5-3","name":"线面关系与距离","tags":["def","thm","der","exa"],"brief":"线面平行垂直判定、面面夹角、点到面距离公式。",
"body":wrap(
 defn("线面位置关系",p("设直线方向向量 $\\vec{v}$、平面法向量 $\\vec{n}$：线面平行或直线落在平面内 $\\Leftrightarrow \\vec{v}\\perp\\vec{n}$，即 $\\vec{v}\\cdot\\vec{n}=0$；线面垂直 $\\Leftrightarrow \\vec{v}\\parallel\\vec{n}$，即 $\\vec{v}=\\lambda\\vec{n}$。"))+
 thm("点到平面距离",p("点 $P_0(x_0,y_0,z_0)$ 到平面 $Ax+By+Cz+D=0$ 的距离：")+
 fml("d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}"))+
 der(p("<strong>第一步 · 向量设定：</strong>平面法向量 $\\vec{n}=(A,B,C)$，点 $P_0$ 到平面的距离即 $\\overrightarrow{P_0Q}$ 在 $\\vec{n}$ 方向上投影的绝对值，其中 $Q$ 为垂足，$\\overrightarrow{P_0Q}\\parallel\\vec{n}$，设 $\\overrightarrow{P_0Q}=t\\vec{n}$。")+
 p("<strong>第二步 · 由垂足求 $t$：</strong>垂足 $Q(x_0+tA,\\ y_0+tB,\\ z_0+tC)$ 在平面上，代入得 $A(x_0+tA)+B(y_0+tB)+C(z_0+tC)+D=0$，即 $Ax_0+By_0+Cz_0+D+t(A^2+B^2+C^2)=0$，解得")+
 fml("t=-\\dfrac{Ax_0+By_0+Cz_0+D}{A^2+B^2+C^2}")+
 p("<strong>第三步 · 求距离：</strong>距离 $d=|\\overrightarrow{P_0Q}|=|t|\\,|\\vec{n}|=|t|\\sqrt{A^2+B^2+C^2}$，代入 $t$ 得")+
 fml("d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}")+
 p("<strong>第四步 · 线面平行判定：</strong>直线与平面平行时方向向量与法向量垂直，$\\vec{v}\\cdot\\vec{n}=0$，此时直线上任一点到平面的距离处处相等。")+
 p("<strong>第五步 · 面面夹角：</strong>两平面法向量 $\\vec{n_1},\\vec{n_2}$，二面角与其法向量所成角相等或互补，故")+
 fml("\\cos\\varphi=\\dfrac{|\\vec{n_1}\\cdot\\vec{n_2}|}{|\\vec{n_1}||\\vec{n_2}|}"))+
 exa(p("<strong>例：</strong>原点到平面 $2x+3y+6z-21=0$ 的距离 $d=\\dfrac{|-21|}{\\sqrt{4+9+36}}=\\dfrac{21}{7}=3$。"))+
 note(p("直线与平面的夹角 $\\theta$ 用方向向量与法向量夹角 $\\varphi$ 表示，$\\sin\\theta=|\\cos\\varphi|$；各夹角公式取绝对值以保证得到不超过 $90^\\circ$ 的角。")))
}
]},
{"name":"7.6 二次曲面","color":"#0f766e","desc":"椭球面、双曲面、抛物面、锥面",
"items":[
{"id":"e7s6-1","name":"椭球面与单叶双曲面","tags":["def","thm","der","exa"],"brief":"椭球面与单叶双曲面的标准方程与截痕法。",
"fig":"quadric","figCap":"二次曲面（椭球面、双曲面、抛物面）的截痕示意",
"body":wrap(
 defn("椭球面",p("方程 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}+\\dfrac{z^2}{c^2}=1$（$a,b,c>0$）所表示的曲面称<strong>椭球面</strong>，三个半轴长为 $a,b,c$；当 $a=b=c$ 时退化为球面。"))+
 defn("单叶双曲面",p("方程 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=1$ 所表示的曲面称<strong>单叶双曲面</strong>，形状如腰鼓，整体连通（单叶），且是<strong>直纹面</strong>（可由直线族生成）。"))+
 thm("截痕法",p("用一族平行平面 $z=h$ 去截曲面，分析所得截口曲线的类型与变化规律，从而推断曲面整体形状，这种方法称<strong>截痕法</strong>。"))+
 der(p("<strong>第一步 · 椭球面用 $z=h$ 截：</strong>把 $z=h$（$|h|\\le c$）代入椭球面方程得")+
 fml("\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1-\\dfrac{h^2}{c^2}")+
 p("<strong>第二步 · 判断截口：</strong>因 $|h|\\le c$，右端非负，故截口为椭圆，半轴分别为 $a'=a\\sqrt{1-\\dfrac{h^2}{c^2}}$、$b'=b\\sqrt{1-\\dfrac{h^2}{c^2}}$。$h=0$ 时截口最大，$|h|=c$ 时退化为两个点 $(0,0,\\pm c)$。同理用 $x=h$、$y=h$ 截得的也都是椭圆。")+
 p("<strong>第三步 · 单叶双曲面用 $z=h$ 截：</strong>代入得")+
 fml("\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1+\\dfrac{h^2}{c^2}")+
 p("<strong>第四步：</strong>右端恒大于 $0$，故对任意 $h$ 截口都是椭圆，且 $|h|$ 越大椭圆越大，这正是单叶连通的表现。")+
 p("<strong>第五步 · 用 $y=h$ 截：</strong>得 $\\dfrac{x^2}{a^2}-\\dfrac{z^2}{c^2}=1-\\dfrac{h^2}{b^2}$。当 $|h|<b$ 时为双曲线，$|h|=b$ 时退化为两条相交直线，$|h|>b$ 时横轴转向 $z$ 方向的双曲线。"))+
 exa(p("<strong>例：</strong>地球近似为扁椭球面 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}+\\dfrac{z^2}{c^2}=1$（取 $a=b>c$），其自转导致的扁率由长短半轴之比刻画；单叶双曲面是工程中常见的冷却塔外形。")))
},
{"id":"e7s6-2","name":"双叶双曲面与椭圆抛物面","tags":["def","thm","der","exa"],"brief":"双叶双曲面与椭圆抛物面的标准方程与性质。",
"body":wrap(
 defn("双叶双曲面",p("方程 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=-1$ 所表示的曲面称<strong>双叶双曲面</strong>，它分成 $z\\ge c$ 与 $z\\le-c$ 上下不相连的两叶，$z$ 轴为对称轴。"))+
 defn("椭圆抛物面",p("方程 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=z$ 所表示的曲面称<strong>椭圆抛物面</strong>，顶点在原点，开口朝 $z$ 轴正向；当 $a=b$ 时为<strong>旋转抛物面</strong>。"))+
 thm("截痕特征",p("")+
 fml("\\text{双叶双曲面}:\\ \\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=\\dfrac{z^2}{c^2}-1\\quad(|z|\\ge c)"))+
 der(p("<strong>第一步 · 双叶双曲面用 $z=h$ 截：</strong>代得 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=\\dfrac{h^2}{c^2}-1$，右端符号随 $h$ 变化：")+
 fml("\\dfrac{h^2}{c^2}-1>0\\ (|h|>c)\\ \\text{为椭圆},\\qquad =0\\ (|h|=c)\\ \\text{退化为点},\\qquad <0\\ (|h|<c)\\ \\text{无实截口}")+
 p("<strong>第二步 · 分叶结论：</strong>因 $|h|<c$ 处无实点，曲面被分成 $z\\ge c$ 与 $z\\le-c$ 两叶；用 $y=h$ 截得 $\\dfrac{x^2}{a^2}-\\dfrac{z^2}{c^2}=-1-\\dfrac{h^2}{b^2}$，恒为双曲线。")+
 p("<strong>第三步 · 椭圆抛物面用 $z=h$ 截：</strong>代得 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=h$：")+
 fml("h>0:\\ \\text{椭圆},\\qquad h=0:\\ \\text{原点（顶点）},\\qquad h<0:\\ \\text{无实截口}")+
 p("<strong>第四步 · 用 $y=h$ 截椭圆抛物面：</strong>得 $\\dfrac{x^2}{a^2}=z-\\dfrac{h^2}{b^2}$，即 $x^2=a^2\\left(z-\\dfrac{h^2}{b^2}\\right)$，为开口朝上的抛物线（$z\\ge\\dfrac{h^2}{b^2}$），故曲面整体向上无限张开。"))+
 exa(p("<strong>例：</strong>旋转抛物面 $x^2+y^2=z$（即 $a=b=1$）由抛物线 $x^2=z$ 绕 $z$ 轴旋转一周得到，其聚焦性质被用于反射望远镜与卫星天线。")))
},
{"id":"e7s6-3","name":"双曲抛物面与二次锥面","tags":["def","thm","der","exa"],"brief":"双曲抛物面（马鞍面）与二次锥面的标准方程。",
"fig":"quadric","figCap":"马鞍面与二次锥面的截痕示意",
"body":wrap(
 defn("双曲抛物面",p("方程 $\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=z$ 所表示的曲面称<strong>双曲抛物面</strong>，因形似马鞍又称<strong>马鞍面</strong>，它同样是直纹面。"))+
 defn("二次锥面",p("方程 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=0$ 所表示的曲面称<strong>二次锥面</strong>，顶点在原点，关于 $z$ 轴对称；它是单叶双曲面与双叶双曲面之间的过渡曲面。"))+
 thm("截痕特征",p("")+
 fml("\\text{二次锥面}:\\ \\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=\\dfrac{z^2}{c^2}"))+
 der(p("<strong>第一步 · 马鞍面用 $z=h$ 截：</strong>代得 $\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=h$：")+
 fml("h>0:\\ \\text{横轴沿}x\\text{方向的双曲线},\\quad h<0:\\ \\text{横轴沿}y\\text{方向的双曲线},\\quad h=0:\\ \\text{两相交直线}\\ \\dfrac{x}{a}=\\pm\\dfrac{y}{b}")+
 p("<strong>第二步 · 用 $y=h$ 截马鞍面：</strong>得 $\\dfrac{x^2}{a^2}-z=\\dfrac{h^2}{b^2}$，即")+
 fml("z=\\dfrac{x^2}{a^2}-\\dfrac{h^2}{b^2}\\quad(\\text{开口朝上的抛物线})")+
 p("<strong>第三步 · 用 $x=h$ 截马鞍面：</strong>得 $z=\\dfrac{h^2}{a^2}-\\dfrac{y^2}{b^2}$，为开口朝下的抛物线。两个方向一上一下，故曲面呈马鞍形。")+
 p("<strong>第四步 · 二次锥面用 $z=h$ 截：</strong>当 $h\\neq0$ 时")+
 fml("\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=\\dfrac{h^2}{c^2}\\quad(h\\neq0)\\ \\Longrightarrow\\ \\text{椭圆}")+
 p("（$a=b$ 时为圆），$h=0$ 时退化为原点这一顶点。"))+
 exa(p("<strong>例：</strong>马鞍面 $z=x^2-y^2$（$a=b=1$）在原点附近沿 $x$ 方向上翘、沿 $y$ 方向下垂，过原点沿不同方向的截口一上一下，是典型的负曲率曲面。")))
}
]},
{"name":"7.7 空间曲线","color":"#115e59","desc":"空间曲线参数方程、螺旋线与投影",
"items":[
{"id":"e7s7-1","name":"空间曲线参数方程与圆柱螺旋线","tags":["def","thm","der","exa"],"brief":"空间曲线参数方程、圆柱螺旋线及其弧长（展开法）。",
"fig":"helix","figCap":"圆柱螺旋线：点在圆柱面上匀速旋转并匀速上升",
"body":wrap(
 defn("空间曲线的参数方程",p("若动点坐标都是参数 $t$ 的函数 $x=x(t),\\ y=y(t),\\ z=z(t)$，则 $\\vec{r}(t)=(x(t),y(t),z(t))$ 表示一条<strong>空间曲线</strong>。"))+
 defn("圆柱螺旋线",p("参数方程")+
 fml("\\begin{cases}x=a\\cos t\\\\ y=a\\sin t\\\\ z=bt\\end{cases}\\quad(a>0)")+
 p("所表示的曲线称<strong>圆柱螺旋线</strong>：点在半径 $a$ 的圆柱面 $x^2+y^2=a^2$ 上，每转一整圈（$t$ 增加 $2\\pi$）沿轴向上升 $2\\pi b$，该值称<strong>螺距</strong>。"))+
 thm("螺旋线弧长（展开法）",p("把圆柱侧面沿一条母线剪开铺平成平面矩形，螺旋线展开后恰好是一条<strong>直线段</strong>，故其长可由勾股定理求得。"))+
 der(p("<strong>第一步 · 分解运动：</strong>螺旋线运动可分解为 $xy$ 平面内半径 $a$ 的匀速圆周运动与 $z$ 方向速度 $b$ 的匀速直线运动，两者同时进行且相互独立。")+
 p("<strong>第二步 · 展开圆柱面：</strong>取转一整圈（$t:0\\to2\\pi$），圆周方向走过的弧长为圆周长，轴向上升高度为")+
 fml("s_{\\text{周}}=2\\pi a,\\qquad s_{\\text{轴}}=2\\pi b")+
 p("<strong>第三步 · 化为直角三角形斜边：</strong>把圆柱面剪开展平后，圆周方向成为水平边、轴向成为竖直边，螺旋线的一段展开成连接两端的斜线段，由勾股定理，一整圈弧长")+
 fml("s=\\sqrt{(2\\pi a)^2+(2\\pi b)^2}=2\\pi\\sqrt{a^2+b^2}")+
 p("<strong>第四步 · 一般弧长：</strong>转过 $t$ 弧度（即 $\\dfrac{t}{2\\pi}$ 圈）时，弧长与参数成正比")+
 fml("s(t)=\\dfrac{t}{2\\pi}\\cdot2\\pi\\sqrt{a^2+b^2}=\\sqrt{a^2+b^2}\\,t"))+
 exa(p("<strong>例：</strong>取 $a=1,\\ b=1$，一整圈弧长 $s=2\\pi\\sqrt{1+1}=2\\sqrt2\\pi$；若 $t=4\\pi$（转两圈），则 $s=\\sqrt2\\cdot4\\pi=4\\sqrt2\\pi$。")))
},
{"id":"e7s7-2","name":"空间曲线在坐标面上的投影","tags":["def","thm","der","exa"],"brief":"空间曲线投影到坐标面的方法与消元法。",
"fig":"sphere","figCap":"曲面与坐标面：把曲线沿坐标轴方向投影到坐标面",
"body":wrap(
 defn("投影曲线",p("空间曲线 $\\Gamma$ 上每一点 $P(x,y,z)$ 沿 $z$ 轴方向作垂线，垂足 $P'(x,y,0)$ 的全体构成的平面曲线，称 $\\Gamma$ 在 $xOy$ 面上的<strong>投影曲线</strong>。"))+
 thm("消元求投影",p("若 $\\Gamma$ 由两曲面 $F_1(x,y,z)=0$ 与 $F_2(x,y,z)=0$ 的交线给出，则从两式中消去 $z$ 得投影柱面 $H(x,y)=0$，再与 $z=0$ 联立即得 $xOy$ 面上的投影曲线")+
 fml("\\begin{cases}H(x,y)=0\\\\ z=0\\end{cases}"))+
 der(p("<strong>第一步 · 投影的代数含义：</strong>投影过程丢掉了 $z$ 坐标，只保留 $x,y$，因此刻画投影就要建立只含 $x,y$ 的关系式。")+
 p("<strong>第二步 · 消元构造投影柱面：</strong>把 $F_1=0$ 与 $F_2=0$ 看成关于 $z$ 的方程组，消去 $z$ 得 $H(x,y)=0$。该方程与 $z$ 无关，几何上是过 $\\Gamma$ 且母线平行于 $z$ 轴的<strong>投影柱面</strong>：")+
 fml("H(x,y)=0\\quad(\\text{投影柱面，母线}\\parallel z\\text{轴})")+
 p("<strong>第三步 · 与坐标面相交得投影：</strong>投影柱面与 $xOy$ 面（$z=0$）的交线即投影曲线；若由 $H(x,y)=0$ 还能解出 $y=g(x)$，代回原方程组即可得投影曲线的显式表示。")+
 p("<strong>第四步 · 直观类比：</strong>投影如同平行光沿 $z$ 轴方向照射，曲线在 $xOy$ 面上投下的影子；同理，消去 $y$ 得 $xOz$ 面投影，消去 $x$ 得 $yOz$ 面投影。"))+
 exa(p("<strong>例：</strong>求圆柱面 $x^2+y^2=1$ 与平面 $z=y$ 的交线在 $xOy$ 面上的投影。两方程中 $x^2+y^2=1$ 已不含 $z$，可直接作为投影柱面，故投影曲线为 $\\begin{cases}x^2+y^2=1\\\\ z=0\\end{cases}$，即 $xOy$ 面上的单位圆。")))
}
]}
]
# ============ 第八章 概率统计 ============
# ============ 第八章 概率统计（重写：内容充足、推导严谨，结构不变） ============
ch8_sections = [
{"name":"8.1 计数原理","color":"#16a34a","desc":"排列、组合、二项式定理",
"items":[
{"id":"e8s1-1","name":"排列与组合","tags":["def","thm","der","exa","note"],"brief":"两个基本计数原理、排列数与组合数的定义、性质与计算。",
"fig":"bayes_tree","figCap":"分类计数与分步计数的树状图",
"body":wrap(
 defn("两个基本计数原理",
  p("① <strong>分类加法计数原理：</strong>完成一件事有 $n$ 类互不重叠的办法，第 $i$ 类含 $m_i$ 种，则总办法数为 $\\sum_{i=1}^{n}m_i$。② <strong>分步乘法计数原理：</strong>完成一件事需依次经过 $n$ 个步骤，第 $i$ 步含 $m_i$ 种，则总办法数为 $\\prod_{i=1}^{n}m_i$。"))+
 thm("排列数与组合数",
  p("从 $n$ 个不同元素中取出 $m$（$0\\le m\\le n$）个，按一定顺序排成一列的排法数称<strong>排列数</strong> $A_n^m$；只取不排（不计顺序）的取法数称<strong>组合数</strong> $C_n^m$：")+
  fml("A_n^m=n(n-1)\\cdots(n-m+1)=\\dfrac{n!}{(n-m)!},\\qquad C_n^m=\\dfrac{A_n^m}{m!}=\\dfrac{n!}{m!\\,(n-m)!}"))+
 der(
  p("<strong>第一步 · 排列数公式的推导：</strong>从 $n$ 个不同元素中依次取出 $m$ 个排成一列，可看成依次填 $m$ 个位置：第 1 位有 $n$ 种选法；取出一个后，第 2 位剩 $n-1$ 种；依此类推，第 $m$ 位剩下 $n-(m-1)=n-m+1$ 种。由分步乘法计数原理，把各步相乘：")+
  fml("A_n^m=n(n-1)(n-2)\\cdots(n-m+1)")+
  p("<strong>第二步 · 引入阶乘化简：</strong>上式共有 $m$ 个连续递减的因子。若在末尾再乘上从 $(n-m)$ 到 $1$ 的连乘，恰好凑成 $n!$；为保持等式不变，再除以 $(n-m)!$ 即可：")+
  fml("A_n^m=\\dfrac{n(n-1)\\cdots(n-m+1)\\cdot(n-m)!}{(n-m)!}=\\dfrac{n!}{(n-m)!}")+
  p("<strong>第三步 · 组合数公式的推导：</strong>组合只关心「取了哪 $m$ 个」，不关心它们的先后次序。对任意取出的一组 $m$ 个元素，其内部排列数为 $m!$，故每一种组合恰好对应 $m!$ 种排列，于是 $C_n^m\\cdot m!=A_n^m$，得")+
  fml("C_n^m=\\dfrac{A_n^m}{m!}=\\dfrac{n!}{m!\\,(n-m)!}")+
  p("<strong>第四步 · 组合数的对称性：</strong>在上式中把 $m$ 换成 $n-m$，直接计算：$C_n^{n-m}=\\dfrac{n!}{(n-m)!\\,(n-(n-m))!}=\\dfrac{n!}{(n-m)!\\,m!}=C_n^m$。其组合意义是「选出 $m$ 个」与「留下 $n-m$ 个」一一对应。")+
  p("<strong>第五步 · 帕斯卡递推公式：</strong>从 $n$ 个元素中选 $m$ 个，按某个指定元素 $a$ 是否被选中，分成互斥的两类：不选 $a$，则从其余 $n-1$ 个中选 $m$ 个，有 $C_{n-1}^{m}$ 种；选 $a$，则从其余 $n-1$ 个中再选 $m-1$ 个，有 $C_{n-1}^{m-1}$ 种。由分类加法计数原理：")+
  fml("C_n^m=C_{n-1}^{m}+C_{n-1}^{m-1}"))+
 exa(
  p("<strong>例：</strong>从 5 名同学中选 3 人排成一排照相，因讲顺序，排法数为 $A_5^3=5\\times4\\times3=60$；若仅选 3 人组成小组，因不讲顺序，选法数为 $C_5^3=\\dfrac{5!}{3!\\,2!}=10$。可见 $60=C_5^3\\times3!=10\\times6$，正印证了「组合数 $\\times$ 内部排列数 $=$ 排列数」这一关系。"))+
 note(
  p("规定 $0!=1$，于是 $C_n^0=C_n^n=1$。全排列数为 $A_n^n=n!$。当 $m=n$ 时 $A_n^n=n!$，$C_n^n=1$。"))+
 p(""))
},
{"id":"e8s1-2","name":"二项式定理","tags":["def","thm","der","exa","note"],"brief":"二项式展开、通项公式与二项式系数性质。",
"body":wrap(
 thm("二项式定理",
  p("对任意正整数 $n$：")+
  fml("(a+b)^n=\\sum_{k=0}^{n}\\binom{n}{k}a^{n-k}b^{k}")+
  p("其中 $\\binom{n}{k}=C_n^k$ 称<strong>二项式系数</strong>，展开式中的第 $k+1$ 项（<strong>通项</strong>）为")+
  fml("T_{k+1}=\\binom{n}{k}a^{n-k}b^{k}\\quad(k=0,1,\\dots,n)"))+
 thm("二项式系数的性质",
  p("")+
  fml("\\sum_{k=0}^{n}\\binom{n}{k}=2^n,\\qquad \\binom{n}{k}=\\binom{n}{n-k}")+
  fml("\\sum_{k=0}^{n}(-1)^{k}\\binom{n}{k}=0,\\qquad \\binom{n}{k}=\\binom{n-1}{k}+\\binom{n-1}{k-1}"))+
 der(
  p("<strong>第一步 · 通项公式的推导：</strong>把 $(a+b)^n$ 看成 $n$ 个因子 $(a+b)$ 相乘，即 $(a+b)^n=\\underbrace{(a+b)(a+b)\\cdots(a+b)}_{n\\text{ 个因子}}$。展开时每个因子都贡献一个字母（$a$ 或 $b$），故每一项都形如 $a^{n-k}b^{k}$：它表示恰有 $k$ 个因子取 $b$、其余 $n-k$ 个因子取 $a$。")+
  fml("(a+b)^n=\\underbrace{(a+b)(a+b)\\cdots(a+b)}_{n\\text{ 个因子}}")+
  p("<strong>第二步 · 系数来源：</strong>要得到 $a^{n-k}b^{k}$，只需从 $n$ 个因子中任选 $k$ 个让它们出 $b$（其余自然出 $a$）。这样的选法数正是组合数 $\\binom{n}{k}$，故该项的系数为 $\\binom{n}{k}$。让 $k$ 取遍 $0,1,\\dots,n$ 并求和，即得二项式定理。")+
  fml("(a+b)^n=\\sum_{k=0}^{n}\\binom{n}{k}a^{n-k}b^{k}")+
  p("<strong>第三步 · 求和性质（赋值法）：</strong>在定理中令 $a=b=1$，左边为 $2^n$，右边每一项的 $a^{n-k}b^{k}=1$，于是")+
  fml("\\sum_{k=0}^{n}\\binom{n}{k}=(1+1)^n=2^n")+
  p("<strong>第四步 · 交错和（再赋值）：</strong>令 $a=1,\\,b=-1$，左边为 $(1-1)^n=0$，右边为 $\\sum_{k=0}^{n}(-1)^k\\binom{n}{k}$，故偶数项的系数和等于奇数项的系数和，均等于 $2^{n-1}$。")+
  fml("\\sum_{k=0}^{n}(-1)^{k}\\binom{n}{k}=0\\ \\Rightarrow\\ \\sum_{k\\text{ 偶}}\\binom{n}{k}=\\sum_{k\\text{ 奇}}\\binom{n}{k}=2^{n-1}")+
  p("<strong>第五步 · 对称性与递推：</strong>把 $(a+b)^n$ 中 $a,b$ 互换即 $(b+a)^n$，展开式不变，比较 $a^{n-k}b^{k}$ 与 $a^{k}b^{n-k}$ 的系数得 $\\binom{n}{k}=\\binom{n}{n-k}$。又因为首因子取 $a$ 或取 $b$ 两类互斥，由计数原理得递推 $\\binom{n}{k}=\\binom{n-1}{k}+\\binom{n-1}{k-1}$（即杨辉三角的构造规律）。"))+
 exa(
  p("<strong>例：</strong>求 $(x+1)^5$ 的展开式中 $x^3$ 的系数。由通项 $T_{k+1}=\\binom{5}{k}x^{5-k}$，令 $5-k=3$ 得 $k=2$，系数为 $\\binom{5}{2}=10$。又常数项需 $5-k=0$，即 $k=5$，系数为 $\\binom{5}{5}=1$；各二项式系数之和验证为 $\\binom{5}{0}+\\cdots+\\binom{5}{5}=2^5=32$。"))+
 note(
  p("展开式共 $n+1$ 项；二项式系数先增后减，$n$ 为偶数时中间一项 $\\binom{n}{n/2}$ 最大，$n$ 为奇数时中间两项相等且最大。注意「二项式系数」$\\binom{n}{k}$ 与「项的系数」（含数字因式）不是一回事。"))+
 p(""))
}
]},
{"name":"8.2 概率","color":"#15803d","desc":"古典概型、条件概率、全概率与贝叶斯",
"items":[
{"id":"e8s2-1","name":"古典概型与几何概型","tags":["def","thm","der","exa","note"],"brief":"古典概型定义、概率计算、几何概型与加法公式。",
"fig":"probability","figCap":"古典概型 P(A)=m/n，4 个等可能事件",
"body":wrap(
 defn("随机试验与古典概型",
  p("对随机现象加以观察或试验称<strong>随机试验</strong>，其每一种可能结果称<strong>基本事件</strong>，全体基本事件构成<strong>样本空间</strong> $\\Omega$。若试验满足：① <strong>有限性</strong>（基本事件总数有限）；② <strong>等可能性</strong>（每个基本事件发生的概率相等），则称<strong>古典概型</strong>。"))+
 thm("概率计算公式",
  p("古典概型中，事件 $A$ 所包含的基本事件数记 $m$，基本事件总数记 $n$，则")+
  fml("P(A)=\\dfrac{m}{n}=\\dfrac{A\\text{ 所含基本事件数}}{\\text{基本事件总数}}")+
  p("当基本事件无限时，用几何测度（长度、面积、体积）之比代替个数之比，得<strong>几何概型</strong>：")+
  fml("P(A)=\\dfrac{\\mu(A)}{\\mu(\\Omega)}"))+
 der(
  p("<strong>第一步 · 古典概型公式的推导：</strong>设样本空间含 $n$ 个基本事件 $\\omega_1,\\dots,\\omega_n$。由等可能性，每个基本事件的概率都相等，设为 $q$；又由概率的归一性（必然事件概率为 $1$）有 $\\sum_{i=1}^{n}q=1$，即 $nq=1$，解得 $q=\\dfrac{1}{n}$。")+
  fml("P(\\omega_1)=P(\\omega_2)=\\cdots=P(\\omega_n)=\\dfrac{1}{n}")+
  p("<strong>第二步 · 有限可加性求和：</strong>若事件 $A$ 恰含 $m$ 个基本事件，则 $A=\\omega_{i_1}\\cup\\cdots\\cup\\omega_{i_m}$，这些基本事件两两互斥，由概率的有限可加性得")+
  fml("P(A)=\\sum_{j=1}^{m}P(\\omega_{i_j})=\\sum_{j=1}^{m}\\dfrac{1}{n}=\\dfrac{m}{n}")+
  p("<strong>第三步 · 几何概型的推导：</strong>当基本事件是某个区域 $\\Omega$ 内的点、且点落入任意子区域的概率与该区域测度成正比、与位置形状无关（均匀分布）时，事件 $A$ 对应测度为 $\\mu(A)$ 的子区域。个数之比 $m/n$ 便自然地推广为测度之比 $\\mu(A)/\\mu(\\Omega)$，测度取长度、面积或体积。")+
  fml("P(A)=\\dfrac{\\mu(A)}{\\mu(\\Omega)}\\quad(\\mu\\text{ 为长度/面积/体积})")+
  p("<strong>第四步 · 对立事件公式：</strong>因为 $A\\cup\\bar A=\\Omega$ 且 $A\\bar A=\\emptyset$，由可加性 $P(A)+P(\\bar A)=P(\\Omega)=1$，故 $P(\\bar A)=1-P(A)$。当直接求 $P(A)$ 困难而 $P(\\bar A)$ 易求时，此式尤为有用。")+
  fml("P(\\bar A)=1-P(A)")+
  p("<strong>第五步 · 加法公式（容斥）：</strong>对任意两事件，把 $A\\cup B$ 分解为互斥的 $A$ 与 $B\\bar A$：$P(A\\cup B)=P(A)+P(B\\bar A)$；又 $B=B A\\cup B\\bar A$ 且二者互斥，故 $P(B\\bar A)=P(B)-P(AB)$。代入即得 $P(A\\cup B)=P(A)+P(B)-P(AB)$，其中 $A\\cap B$ 被重复计入一次故须减去；当 $A,B$ 互斥时 $A\\cap B=\\emptyset$，得 $P(A\\cup B)=P(A)+P(B)$。")+
  fml("P(A\\cup B)=P(A)+P(B)-P(A\\cap B)"))+
 exa(
  p("<strong>例：</strong>掷一枚均匀骰子，样本空间 $\\Omega=\\{1,2,3,4,5,6\\}$，$n=6$。事件「出现偶数」$A=\\{2,4,6\\}$，$m=3$，故 $P(A)=\\dfrac{3}{6}=\\dfrac{1}{2}$。「点数大于 $4$」有 $\\{5,6\\}$，概率为 $\\dfrac{2}{6}=\\dfrac{1}{3}$。"))+
 note(
  p("互斥（不同时发生，$A\\cap B=\\emptyset$）与对立（$A\\cap B=\\emptyset$ 且 $A\\cup B=\\Omega$）不同：对立必互斥，互斥未必对立。古典概型中求 $m,n$ 常借助排列组合，务必先判定「讲不讲顺序」再计数。"))+
 p(""))
},
{"id":"e8s2-2","name":"条件概率与全概率公式","tags":["def","thm","der","exa","note"],"brief":"条件概率、乘法公式、全概率公式的推导。",
"body":wrap(
 defn("条件概率",
  p("设 $P(B)>0$，在「事件 $B$ 已发生」的条件下，事件 $A$ 发生的<strong>条件概率</strong>定义为")+
  fml("P(A\\mid B)=\\dfrac{P(AB)}{P(B)}"))+
 thm("乘法公式与全概率公式",
  p("由条件概率定义可直接变形得<strong>乘法公式</strong>：")+
  fml("P(AB)=P(B)\\,P(A\\mid B)=P(A)\\,P(B\\mid A)")+
  p("若 $B_1,B_2,\\dots,B_n$ 两两互斥且 $B_1\\cup\\cdots\\cup B_n=\\Omega$（称样本空间的一个<strong>分割</strong>），则")+
  fml("P(A)=\\sum_{i=1}^{n}P(B_i)\\,P(A\\mid B_i)\\quad(\\text{全概率公式})"))+
 der(
  p("<strong>第一步 · 条件概率定义的合理性：</strong>已知 $B$ 已发生，说明试验结果落在了 $B$ 内，样本空间由 $\\Omega$ 缩小为 $B$。此时 $A$ 发生当且仅当结果落在 $A\\cap B$ 内。用古典概型说明：设 $B$ 含 $n_B$ 个基本事件、$AB$ 含 $n_{AB}$ 个，则在「缩小后的样本空间 $B$」中 $A$ 所占比例为")+
  fml("\\dfrac{n_{AB}}{n_B}=\\dfrac{n_{AB}/n}{n_B/n}=\\dfrac{P(AB)}{P(B)}")+
  p("<strong>第二步 · 乘法公式的推导：</strong>由定义 $P(A\\mid B)=\\dfrac{P(AB)}{P(B)}$，两边同乘 $P(B)>0$，即得 $P(AB)=P(B)\\,P(A\\mid B)$。对称地把 $A,B$ 交换，又可写 $P(AB)=P(A)\\,P(B\\mid A)$，两式即乘法公式。")+
  fml("P(AB)=P(B)\\,P(A\\mid B)=P(A)\\,P(B\\mid A)")+
  p("<strong>第三步 · 全概率公式的推导（分配律）：</strong>因为 $B_i$ 构成分割，$\\bigcup_{i}B_i=\\Omega$，故")+
  fml("A=A\\cap\\Omega=A\\cap\\Big(\\bigcup_{i=1}^{n}B_i\\Big)=\\bigcup_{i=1}^{n}(A\\cap B_i)")+
  p("<strong>第四步 · 互斥性与有限可加性：</strong>由于 $B_i$ 两两互斥，故 $A\\cap B_i$ 也两两互斥。对上述互斥并集用概率的有限可加性，再用乘法公式 $P(A\\cap B_i)=P(B_i)\\,P(A\\mid B_i)$ 代入：")+
  fml("P(A)=\\sum_{i=1}^{n}P(A\\cap B_i)=\\sum_{i=1}^{n}P(B_i)\\,P(A\\mid B_i)")+
  p("<strong>第五步 · 两点说明：</strong>① 全概率公式把「复杂事件 $A$ 的概率」分解为「按原因 $B_i$ 分类后各自贡献之和」，体现了「化整为零」；② 使用前必须确认 $B_i$ 是样本空间的分割（互斥且穷尽），且每个 $P(B_i)>0$。"))+
 exa(
  p("<strong>例：</strong>甲、乙两厂生产同种零件，甲厂产量占 $60\\%$、次品率 $5\\%$（合格率 $95\\%$）；乙厂占 $40\\%$、合格率 $90\\%$。设取到甲厂产品为 $B_1$、乙厂为 $B_2$，取到合格品为 $A$。由全概率公式，任取一件为合格品的概率")+
  fml("P(A)=P(B_1)P(A\\mid B_1)+P(B_2)P(A\\mid B_2)=0.6\\times0.95+0.4\\times0.90=0.93"))+
 note(
  p("条件概率满足概率的一切性质：$P(\\Omega\\mid B)=1$，$0\\le P(A\\mid B)\\le 1$，且 $P(\\bar A\\mid B)=1-P(A\\mid B)$。这些都可从定义直接验证。"))+
 p(""))
},
{"id":"e8s2-3","name":"贝叶斯公式","tags":["def","thm","der","exa","note"],"brief":"贝叶斯公式的推导与先验、后验概率的应用。",
"body":wrap(
 defn("先验概率与后验概率",
  p("设 $B_1,\\dots,B_n$ 为样本空间的一个分割（各 $B_i$ 是可能的原因）。试验前对诸原因的判断 $P(B_i)$ 称<strong>先验概率</strong>；在观察到结果 $A$ 之后，重新评估各原因的可能性 $P(B_i\\mid A)$ 称<strong>后验概率</strong>。"))+
 thm("贝叶斯公式",
  p("在 $P(A)>0$ 时：")+
  fml("P(B_i\\mid A)=\\dfrac{P(B_i)\\,P(A\\mid B_i)}{\\sum_{j=1}^{n}P(B_j)\\,P(A\\mid B_j)}\\quad(i=1,\\dots,n)"))+
 der(
  p("<strong>第一步 · 后验概率的定义式：</strong>由条件概率的定义（交换 $A,B_i$ 的位置）")+
  fml("P(B_i\\mid A)=\\dfrac{P(B_i\\cap A)}{P(A)}")+
  p("<strong>第二步 · 分子用乘法公式：</strong>把分子展开成一个「原因在先、结果在后」的乘积，它正是「原因 $B_i$ 发生」与「在 $B_i$ 下结果 $A$ 发生」的联合概率：")+
  fml("P(B_i\\cap A)=P(B_i)\\,P(A\\mid B_i)")+
  p("<strong>第三步 · 分母用全概率公式：</strong>结果 $A$ 可由任一原因 $B_j$ 引起，各途径互斥，故")+
  fml("P(A)=\\sum_{j=1}^{n}P(B_j)\\,P(A\\mid B_j)")+
  p("<strong>第四步 · 合成公式：</strong>把第二步的分子与第三步的分母同时代入第一步，即得贝叶斯公式，它实现了「由结果 $A$ 反推原因 $B_i$」：")+
  fml("P(B_i\\mid A)=\\dfrac{P(B_i)\\,P(A\\mid B_i)}{\\sum_{j=1}^{n}P(B_j)\\,P(A\\mid B_j)}")+
  p("<strong>第五步 · 两个事件的独立：</strong>若 $P(A\\mid B)=P(A)$（$B$ 的发生不改变 $A$ 的概率），则称 $A$ 与 $B$ <strong>相互独立</strong>。代入乘法公式得 $P(AB)=P(B)P(A\\mid B)=P(A)P(B)$，即独立等价于 $P(AB)=P(A)P(B)$；进一步可得 $P(A\\mid B)=P(A\\mid\\bar B)$。"))+
 exa(
  p("<strong>例：</strong>承上例，已知取出的零件是合格品 $A$，问它来自甲厂的概率。由贝叶斯公式")+
  fml("P(B_1\\mid A)=\\dfrac{P(B_1)P(A\\mid B_1)}{P(A)}=\\dfrac{0.6\\times0.95}{0.93}=\\dfrac{0.57}{0.93}\\approx0.613")+
  p("即合格品中约 $61.3\\%$ 来自甲厂，其余 $38.7\\%$ 来自乙厂。可见乙厂产品虽只占 $40\\%$，但因合格率较低，其合格品在总体中的占比被进一步压低。"))+
 note(
  p("先验 $\\to$ 后验的过程就是「用证据修正信念」。贝叶斯公式中 $P(A\\mid B_i)$ 称<strong>似然</strong>，它刻画原因 $B_i$ 产生结果 $A$ 的能力；后验概率正比于「先验 $\\times$ 似然」。"))+
 p(""))
}
]},
{"name":"8.3 随机变量与统计","color":"#166534","desc":"分布、期望方差、正态分布、回归",
"items":[
{"id":"e8s3-1","name":"离散型随机变量与数字特征","tags":["def","thm","der","exa","note"],"brief":"分布列、数学期望与方差的定义、性质及证明。",
"fig":"normal_dist","figCap":"正态分布 $N(\\mu,\\sigma^2)$ 的钟形曲线",
"body":wrap(
 defn("离散型随机变量与分布列",
  p("取值随随机试验结果而变的变量 $X$ 称<strong>随机变量</strong>；只取有限或可列个值的称<strong>离散型随机变量</strong>。设 $X$ 的取值为 $x_1,x_2,\\dots$，对应概率 $P(X=x_i)=p_i$，则 $\\{p_i\\}$ 称 $X$ 的<strong>分布列</strong>，它满足非负性与归一性：")+
  fml("p_i\\ge0,\\qquad \\sum_{i}p_i=1"))+
 thm("数学期望与方差",
  p("")+
  fml("E(X)=\\sum_{i}x_i p_i,\\qquad D(X)=E\\big[(X-E(X))^2\\big]=E(X^2)-[E(X)]^2")+
  fml("E(aX+b)=aE(X)+b,\\qquad D(aX+b)=a^2 D(X)"))+
 der(
  p("<strong>第一步 · 期望的意义：</strong>期望 $E(X)=\\sum_i x_i p_i$ 是取值 $x_i$ 以概率 $p_i$ 为权的<strong>加权平均</strong>。由归一性 $\\sum_i p_i=1$，若所有取值均为同一常数 $c$，则 $E(c)=c\\cdot\\sum_i p_i=c$，即常数的期望等于它本身。")+
  fml("E(X)=\\sum_{i}x_i p_i")+
  p("<strong>第二步 · 期望线性性质的证明：</strong>设 $X,Y$ 的联合分布为 $p_{ij}=P(X=x_i,\\,Y=y_j)$，则 $X$ 的边缘分布为 $\\sum_j p_{ij}$。由定义")+
  fml("E(X+Y)=\\sum_{i}\\sum_{j}(x_i+y_j)p_{ij}=\\sum_{i}x_i\\Big(\\sum_{j}p_{ij}\\Big)+\\sum_{j}y_j\\Big(\\sum_{i}p_{ij}\\Big)=E(X)+E(Y)")+
  p("进一步对任意常数 $a,b$，把 $aX+b$ 的每个取值代入定义：$E(aX+b)=\\sum_i(ax_i+b)p_i=a\\sum_i x_ip_i+b\\sum_i p_i=aE(X)+b$。期望的线性性对任意随机变量都成立，无需独立。")+
  fml("E(aX+bY)=aE(X)+bE(Y)")+
  p("<strong>第三步 · 方差定义的化简：</strong>方差度量 $X$ 偏离期望的程度。把平方展开并利用期望线性性与 $E\\big(E(X)\\big)=E(X)$：")+
  fml("D(X)=E\\big[(X-E(X))^2\\big]=E\\big[X^2-2X\\,E(X)+[E(X)]^2\\big]=E(X^2)-2[E(X)]^2+[E(X)]^2")+
  p("即得常用计算公式 $D(X)=E(X^2)-[E(X)]^2$。此式表明：方差等于「平方的期望」减去「期望的平方」。")+
  fml("D(X)=E(X^2)-[E(X)]^2")+
  p("<strong>第四步 · 线性变换下方差的变化：</strong>先算 $E(aX+b)=aE(X)+b$，故偏差 $aX+b-E(aX+b)=a\\big(X-E(X)\\big)$，两端平方取期望：$D(aX+b)=a^2 E\\big[(X-E(X))^2\\big]=a^2D(X)$。由此可见平移不改变波动，伸缩 $a$ 使方差放大 $a^2$ 倍。")+
  fml("D(aX+b)=E\\big[a^2(X-E(X))^2\\big]=a^2D(X)"))+
 exa(
  p("<strong>例：</strong>掷一枚均匀骰子，$X$ 为出现的点数，$E(X)=\\dfrac{1+2+\\cdots+6}{6}=\\dfrac{21}{6}=3.5$。又 $E(X^2)=\\dfrac{1^2+2^2+\\cdots+6^2}{6}=\\dfrac{91}{6}$，故 $D(X)=E(X^2)-[E(X)]^2=\\dfrac{91}{6}-\\dfrac{49}{4}\\approx2.92$。"))+
 note(
  p("期望反映取值的「集中位置」，方差（及其算术平方根——标准差 $\\sigma=\\sqrt{D(X)}$）反映取值的「离散程度」。方差取非负值，仅当 $X$ 恒为常数时 $D(X)=0$。"))+
 p(""))
},
{"id":"e8s3-2","name":"二项分布与正态分布","tags":["def","thm","der","exa","note"],"brief":"二项分布及其期望方差、正态分布密度与 3σ 原则。",
"body":wrap(
 defn("二项分布",
  p("在 $n$ 次<strong>独立重复</strong>试验中，每次试验只有「成功」与「失败」两种结果，成功概率恒为 $p$。以 $X$ 表示 $n$ 次试验中成功的次数，则 $X$ 服从<strong>二项分布</strong>，记 $X\\sim B(n,p)$，其分布列为")+
  fml("P(X=k)=\\binom{n}{k}p^{k}(1-p)^{n-k},\\qquad k=0,1,\\dots,n"))+
 thm("二项分布的数字特征",
  p("")+
  fml("E(X)=np,\\qquad D(X)=np(1-p)"))+
 defn("正态分布",
  p("若连续型随机变量 $X$ 的概率密度为 $f(x)=\\dfrac{1}{\\sqrt{2\\pi}\\,\\sigma}e^{-\\dfrac{(x-\\mu)^2}{2\\sigma^2}}$，则称 $X$ 服从<strong>正态分布</strong>，记 $X\\sim N(\\mu,\\sigma^2)$。其中 $\\mu$ 为均值，$\\sigma^2$ 为方差，曲线关于 $x=\\mu$ 对称、呈钟形。"))+
 der(
  p("<strong>第一步 · 用 0-1 变量分解（引入伯努利变量）：</strong>把第 $i$ 次试验的成功数记为 $X_i$，则 $X_i$ 只取 $0$ 或 $1$，且 $P(X_i=1)=p,\\ P(X_i=0)=1-p$（称伯努利变量），并且总成功次数是各次之和")+
  fml("X=X_1+X_2+\\cdots+X_n,\\qquad E(X_i)=1\\cdot p+0\\cdot(1-p)=p")+
  p("<strong>第二步 · 二项分布期望的推导：</strong>对 $X=\\sum_i X_i$ 用期望的线性性（不必独立）")+
  fml("E(X)=E\\Big(\\sum_{i=1}^{n}X_i\\Big)=\\sum_{i=1}^{n}E(X_i)=np")+
  p("<strong>第三步 · 单个伯努利变量方差的推导：</strong>因 $X_i$ 只取 $0,1$，故 $X_i^2=X_i$，于是 $E(X_i^2)=E(X_i)=p$，从而")+
  fml("D(X_i)=E(X_i^2)-[E(X_i)]^2=p-p^2=p(1-p)")+
  p("<strong>第四步 · 二项分布方差的推导：</strong>各次试验相互独立，故 $X_1,\\dots,X_n$ 相互独立，独立变量之和的方差等于方差之和：")+
  fml("D(X)=D\\Big(\\sum_{i=1}^{n}X_i\\Big)=\\sum_{i=1}^{n}D(X_i)=n\\,p(1-p)")+
  p("<strong>第五步 · 正态分布的标准化：</strong>作线性变换 $Z=\\dfrac{X-\\mu}{\\sigma}$，则 $E(Z)=\\dfrac{E(X)-\\mu}{\\sigma}=0$，$D(Z)=\\dfrac{D(X)}{\\sigma^2}=1$，即 $Z\\sim N(0,1)$ 称标准正态分布。这一步把一般正态化为可查表的标准正态。")+
  fml("Z=\\dfrac{X-\\mu}{\\sigma}\\sim N(0,1)")+
  p("<strong>第六步 · 3σ 原则：</strong>由标准正态分布表可得：$P(|Z|<1)\\approx0.683$，$P(|Z|<2)\\approx0.954$，$P(|Z|<3)\\approx0.997$。把 $|Z|<k$ 还原为 $|X-\\mu|<k\\sigma$，即知数据约有 $68.3\\%$ 落在 $\\mu\\pm\\sigma$、$95.4\\%$ 落在 $\\mu\\pm2\\sigma$、$99.7\\%$ 落在 $\\mu\\pm3\\sigma$ 内，这就是<strong>3σ 原则</strong>。")+
  fml("P(|X-\\mu|<k\\sigma)=P(|Z|<k)"))+
 exa(
  p("<strong>例：</strong>抛一枚均匀硬币 10 次，记正面出现次数为 $X$，则 $X\\sim B(10,0.5)$，故 $E(X)=np=10\\times0.5=5$，$D(X)=np(1-p)=10\\times0.5\\times0.5=2.5$。若某次考试成绩 $X\\sim N(70,10^2)$，则约 $95\\%$ 的学生成绩落在 $70\\pm20$，即 $50\\sim90$ 之间。"))+
 note(
  p("二项分布的期望 $np$ 符合直觉：$n$ 次试验平均成功 $np$ 次。当 $n$ 很大时，二项分布近似于正态分布 $N\\big(np,\\,np(1-p)\\big)$（中心极限思想的体现），这是正态分布在统计中广泛应用的根源。"))+
 p(""))
},
{"id":"e8s3-3","name":"样本均值与线性回归","tags":["def","thm","der","exa","note"],"brief":"样本均值方差、最小二乘回归系数与相关系数的推导。",
"body":wrap(
 defn("样本均值、样本方差与相关系数",
  p("设样本数据为 $x_1,x_2,\\dots,x_n$，则<strong>样本均值</strong>与<strong>样本方差</strong>为")+
  fml("\\bar x=\\dfrac{1}{n}\\sum_{i=1}^{n}x_i,\\qquad s^2=\\dfrac{1}{n}\\sum_{i=1}^{n}(x_i-\\bar x)^2")+
  p("<strong>相关系数</strong> $r=\\dfrac{\\sum(x_i-\\bar x)(y_i-\\bar y)}{\\sqrt{\\sum(x_i-\\bar x)^2}\\,\\sqrt{\\sum(y_i-\\bar y)^2}}\\in[-1,1]$ 刻画两组数据的线性相关程度。"))+
 thm("最小二乘回归直线",
  p("对成对数据 $(x_i,y_i)$，使离差平方和最小的回归直线 $\\hat y=a+bx$ 的斜率与截距为")+
  fml("b=\\dfrac{\\sum_{i=1}^{n}(x_i-\\bar x)(y_i-\\bar y)}{\\sum_{i=1}^{n}(x_i-\\bar x)^2},\\qquad a=\\bar y-b\\bar x"))+
 der(
  p("<strong>第一步 · 最小二乘的目标：</strong>希望用直线 $\\hat y_i=a+bx_i$ 逼近观测值 $y_i$。残差 $y_i-\\hat y_i=y_i-a-bx_i$ 可正可负，直接相加会抵消，故取其平方和作为总误差（离差平方和），最小化")+
  fml("Q(a,b)=\\sum_{i=1}^{n}(y_i-a-bx_i)^2")+
  p("<strong>第二步 · 先对截距 $a$ 优化：</strong>固定 $b$，把 $Q$ 看成 $a$ 的二次函数。展开 $a$ 的项得 $Q=na^2-2a\\sum_i(y_i-bx_i)+\\text{（与 }a\\text{ 无关的项）}$。这是开口向上的抛物线，其对称轴（最小值点）为")+
  fml("a=\\dfrac{1}{n}\\sum_{i=1}^{n}(y_i-bx_i)=\\bar y-b\\bar x")+
  p("<strong>第三步 · 回归直线过样本中心：</strong>上式表明无论 $b$ 取何值，最优直线的截距恒满足 $a=\\bar y-b\\bar x$。把它写成 $\\bar y=a+b\\bar x$，说明回归直线必经过样本中心点 $(\\bar x,\\bar y)$。")+
  fml("\\bar y=a+b\\bar x")+
  p("<strong>第四步 · 再对斜率 $b$ 优化：</strong>把 $a=\\bar y-b\\bar x$ 代回 $Q$，并记中心化数据 $u_i=x_i-\\bar x,\\ v_i=y_i-\\bar y$，则 $y_i-a-bx_i=v_i-bu_i$，于是")+
  fml("Q(b)=\\sum_{i=1}^{n}(v_i-bu_i)^2=b^2\\sum_i u_i^2-2b\\sum_i u_iv_i+\\sum_i v_i^2")+
  p("这仍是关于 $b$ 的开口向上二次函数，对称轴（最小值点）为")+
  fml("b=\\dfrac{\\sum_i u_iv_i}{\\sum_i u_i^2}=\\dfrac{\\sum_{i=1}^{n}(x_i-\\bar x)(y_i-\\bar y)}{\\sum_{i=1}^{n}(x_i-\\bar x)^2}")+
  p("至此斜率 $b$ 与截距 $a=\\bar y-b\\bar x$ 全部确定，回归方程唯一。")+
  p("<strong>第五步 · 样本方差的变形公式：</strong>展开平方并注意 $\\sum_i(x_i-\\bar x)=0$：")+
  fml("\\sum_i(x_i-\\bar x)^2=\\sum_i x_i^2-2\\bar x\\sum_i x_i+n\\bar x^2=\\sum_i x_i^2-n\\bar x^2")+
  p("两边除以 $n$，即得便于手算的形式 $s^2=\\dfrac{1}{n}\\sum_i x_i^2-\\bar x^2$（「平方的平均」减「平均的平方」）。")+
  p("<strong>第六步 · 相关系数的意义：</strong>把 $b$ 的分母乘到左边并做归一化，可得 $r=\\dfrac{\\sum(x_i-\\bar x)(y_i-\\bar y)}{\\sqrt{\\sum(x_i-\\bar x)^2}\\sqrt{\\sum(y_i-\\bar y)^2}}$。由柯西不等式 $|r|\\le1$：$|r|$ 越接近 $1$，点越贴近直线，线性相关越强；$r>0$ 为正相关（$y$ 随 $x$ 增大），$r<0$ 为负相关，$r\\approx0$ 表示无线性关系。"))+
 exa(
  p("<strong>例：</strong>三点 $(1,2),(2,4),(3,5)$。$\\bar x=2$，$\\bar y=\\dfrac{11}{3}$。中心化后 $u=(-1,0,1)$，$v=\\big(-\\tfrac53,\\tfrac13,\\tfrac43\\big)$，$\\sum u_iv_i=(-1)\\big(-\\tfrac53\\big)+0+1\\cdot\\tfrac43=\\tfrac{10}{6}+0+\\tfrac{8}{6}=3$，$\\sum u_i^2=2$，故 $b=\\dfrac{3}{2}=1.5$，$a=\\bar y-b\\bar x=\\dfrac{11}{3}-3=\\dfrac{2}{3}$，回归方程为 $\\hat y=\\dfrac{2}{3}+1.5x$。"))+
 note(
  p("用 $\\dfrac{1}{n}\\sum(x_i-\\bar x)^2$ 估计总体方差是有偏的，实际统计中常用无偏估计 $s^2=\\dfrac{1}{n-1}\\sum(x_i-\\bar x)^2$（$n-1$ 为自由度）。回归中只有相关显著时预测才有意义，切忌外推到样本范围之外。"))+
 p(""))
}
]}
]
CHAPTERS = [
    {"id":"e-ch1","num":"第一章","title":"集合与逻辑","en":"SETS & LOGIC",
     "desc":"集合概念与表示、交并补运算与德摩根律、子集与容斥原理、命题与四种命题关系、充要条件与全称存在量词。",
     "sections": ch1_sections},
    {"id":"e-ch2","num":"第二章","title":"代数","en":"ALGEBRA",
     "desc":"实数有理数整数与加减乘除运算律、绝对值与三角不等式、整式运算与平方差/完全平方/立方和差公式、因式分解、一元一次与二元一次方程组、一元二次方程与韦达定理、高次方程、一元二次与分式绝对值不等式、均值不等式链与常见放缩。",
     "sections": ch2_sections},
    {"id":"e-ch3","num":"第三章","title":"函数","en":"FUNCTIONS",
     "desc":"函数定义与三要素、单调性奇偶性周期性、反函数与复合函数、指数对数幂函数、二次函数、分段与绝对值函数、六个三角函数定义、同角关系与诱导公式、和差倍半角、三角恒等变换（和差化积与万能公式）、反三角函数。",
     "sections": ch3_sections},
    {"id":"e-ch4","num":"第四章","title":"数列","en":"SEQUENCES",
     "desc":"等差数列通项求和与性质（等差中项、片段和）、等比数列通项求和与无穷递缩、裂项相消、错位相减、倒序相加、分组、并项、公式法、累加法与累乘法求通项。",
     "sections": ch4_sections},
    {"id":"e-ch5","num":"第五章","title":"平面几何","en":"PLANE GEOMETRY",
     "desc":"平行线的判定与性质、三角形内角和与面积公式、正弦定理与余弦定理、海伦公式与中位线、三角形的四心、平行四边形、矩形、菱形、正方形、梯形、圆（垂径定理、圆心角与圆周角、切线与圆幂定理）、对称旋转与平移、平面图形面积周长汇总。",
     "sections": ch5_sections},
    {"id":"e-ch6","num":"第六章","title":"立体几何","en":"SOLID GEOMETRY",
     "desc":"棱柱棱锥与体积、棱台与截面积比、欧拉公式与正多面体、圆柱圆锥圆台、球与球面、线面平行与垂直、二面角与点面距离、体积与表面积汇总表。",
     "sections": ch6_sections},
    {"id":"e-ch7","num":"第七章","title":"解析几何","en":"ANALYTIC GEOMETRY",
     "desc":"极坐标柱坐标球坐标与参数方程、平面向量与空间向量、直线与圆的方程、距离公式、椭圆双曲线抛物线、空间直线与平面方程、椭球面与双曲面、抛物面与锥面、空间曲线与螺旋线、投影。",
     "sections": ch7_sections},
    {"id":"e-ch8","num":"第八章","title":"概率统计","en":"PROBABILITY & STATISTICS",
     "desc":"排列与组合、二项式定理、古典概型与几何概型、条件概率与全概率公式、贝叶斯公式、离散型随机变量与期望方差、二项分布与正态分布、样本均值与线性回归。",
     "sections": ch8_sections},
]

total_items = sum(sum(len(s["items"]) for s in ch["sections"]) for ch in CHAPTERS)
print(f"Total items: {total_items}")


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
  .la-nav-tab.c6{color:#6d28d9;border-color:#ddd6fe}
  .la-nav-tab.c7{color:#0891b2;border-color:#a5f3fc}
  .la-nav-tab.c8{color:#16a34a;border-color:#bbf7d0}
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
  .la-phase-title.e-ch1::before{background:#2563eb}
  .la-phase-title.e-ch2::before{background:#7c3aed}
  .la-phase-title.e-ch3::before{background:#0d9488}
  .la-phase-title.e-ch4::before{background:#c2410c}
  .la-phase-title.e-ch5::before{background:#be185d}
  .la-phase-title.e-ch6::before{background:#6d28d9}
  .la-phase-title.e-ch7::before{background:#0891b2}
  .la-phase-title.e-ch8::before{background:#16a34a}
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
  .la-course-card:hover{transform:translateY(-3px);border-color:#c7d7fe;box-shadow:0 16px 40px rgba(37,99,235,.12)}
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
<meta name="description" content="初等数学知识体系：集合与逻辑、代数、函数、数列、平面几何、立体几何、解析几何、概率统计">
<title>初等数学 · 知识体系</title>
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
    <div class="la-eyebrow">ELEMENTARY MATH · KNOWLEDGE MAP</div>
    <h1>初等数学 · 知识体系</h1>
    <p class="la-subtitle">集合与逻辑 · 代数 · 函数 · 数列 · 平面几何 · 立体几何 · 解析几何 · 概率统计</p>
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
    <div>初等数学 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于初等数学核心知识体系整理</div>
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
    with open("/workspace/elementary-math.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated elementary-math.html ({len(html)} chars)")
