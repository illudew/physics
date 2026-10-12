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
ch1_sections = [
{"name":"1.1 集合概念、运算与德摩根律","color":"#2563eb","desc":"集合表示、交并补与德摩根律推导",
"items":[
{"id":"e1s1-1","name":"集合的概念与表示","tags":["def","der","exa"],"brief":"集合元素三大特性、列举法与描述法、子集个数推导。",
"body":wrap(
 defn("集合与元素",p("具有某种特定性质的事物的总体称为<strong>集合</strong>，组成集合的事物称为<strong>元素</strong>。若 $a$ 是集合 $A$ 的元素，记 $a\\in A$；否则 $a\\notin A$。"))+
 note(p("集合中元素具有<strong>确定性、互异性、无序性</strong>三大特性。确定性要求能判断任一对象是否属于该集合；互异性要求元素不重复；无序性要求元素排列顺序不影响集合相等。"))+
 der(p("<strong>互异性的推论：</strong>若 $\\{1,2,a\\}=\\{1,2,3\\}$，则 $a$ 只能等于 3。因为集合中已有 1 和 2，由互异性 $a$ 不能取 1 或 2，否则出现重复元素，与互异性矛盾。")+
 p("<strong>子集个数推导：</strong>对 $n$ 元集合 $A$，构造子集时每个元素有「属于」或「不属于」两种选择，由乘法原理子集总数为 $2\\times2\\times\\cdots\\times2=2^n$。其中真子集 $2^n-1$ 个（去掉自身），非空真子集 $2^n-2$ 个（再去掉空集）。"))+
 exa(p("<strong>常见数集：</strong>$\\mathbb{N}$ 自然数集、$\\mathbb{Z}$ 整数集、$\\mathbb{Q}$ 有理数集、$\\mathbb{R}$ 实数集。<br>表示法：① <strong>列举法</strong> $A=\\{1,2,3\\}$；② <strong>描述法</strong> $A=\\{x\\mid x>0, x\\in\\mathbb{R}\\}$；③ <strong>图示法</strong>（韦恩图）。")))
},
{"id":"e1s1-2","name":"集合的交、并、补与德摩根律","tags":["def","thm","der"],"brief":"交集、并集、补集定义与德摩根律双向推导。",
"fig":"set_venn","figCap":"集合 A 与 B 的韦恩图，重叠区为 A∩B",
"body":wrap(
 defn("交集",p("由所有既属于 A 又属于 B 的元素组成的集合：")+
 fml("A\\cap B = \\{x\\mid x\\in A \\text{ 且 } x\\in B\\}"))+
 defn("并集",p("由所有属于 A 或属于 B 的元素组成的集合：")+
 fml("A\\cup B = \\{x\\mid x\\in A \\text{ 或 } x\\in B\\}"))+
 defn("补集",p("设 U 为全集，A 是 U 的子集，则 U 中所有不属于 A 的元素组成 A 相对 U 的补集：")+
 fml("\\complement_U A = \\{x\\mid x\\in U \\text{ 且 } x\\notin A\\}"))+
 thm("德摩根律",p("补集对交并运算满足对偶关系：")+
 fml("\\complement_U(A\\cap B)=\\complement_U A\\cup\\complement_U B,\\quad \\complement_U(A\\cup B)=\\complement_U A\\cap\\complement_U B"))+
 der(p("<strong>第一式推导（双向包含）：</strong>任取 $x\\in\\complement_U(A\\cap B)$，则 $x\\notin A\\cap B$，即 $x\\notin A$ 或 $x\\notin B$，故 $x\\in\\complement_U A$ 或 $x\\in\\complement_U B$，即 $x\\in\\complement_U A\\cup\\complement_U B$，故左 $\\subseteq$ 右。")+
 p("反向：任取 $x\\in\\complement_U A\\cup\\complement_U B$，则 $x\\notin A$ 或 $x\\notin B$，即 $x\\notin A\\cap B$，故 $x\\in\\complement_U(A\\cap B)$，右 $\\subseteq$ 左。两边相等得证。")+
 p("<strong>第二式推导：</strong>在第一式中以 $\\complement_U A$ 代 $A$、$\\complement_U B$ 代 $B$，得 $\\complement_U(\\complement_U A\\cap\\complement_U B)=A\\cup B$，两边再取补集即得 $\\complement_U(A\\cup B)=\\complement_U A\\cap\\complement_U B$。")))
}
]},
{"name":"1.2 子集与容斥原理","color":"#0ea5e9","desc":"子集、真子集、集合相等与容斥原理",
"items":[
{"id":"e1s2-1","name":"子集与容斥原理","tags":["def","thm","der","exa"],"brief":"子集、真子集、集合相等、二元与三元容斥原理。",
"body":wrap(
 defn("子集",p("若集合 A 的每一个元素都属于 B，则称 A 是 B 的<strong>子集</strong>，记 $A\\subseteq B$。若 $A\\subseteq B$ 且 $B\\subseteq A$，则 $A=B$。"))+
 defn("真子集",p("若 $A\\subseteq B$ 且存在 $b\\in B$ 使 $b\\notin A$，则 A 是 B 的<strong>真子集</strong>，记 $A\\subsetneq B$。"))+
 thm("子集个数",p("含 $n$ 个元素的集合共有 $2^n$ 个子集，$2^n-1$ 个真子集，$2^n-2$ 个非空真子集。"))+
 der(p("<strong>推导：</strong>对集合 A 的每个元素，构造子集时都有「选」或「不选」两种可能。$n$ 个元素由乘法原理共 $2^n$ 种组合，故子集总数为 $2^n$。去掉集合本身得真子集 $2^n-1$ 个，再去掉空集得非空真子集 $2^n-2$ 个。"))+
 thm("二元容斥原理",p("")+
 fml("|A\\cup B| = |A|+|B|-|A\\cap B|"))+
 der(p("<strong>二元推导：</strong>$|A|+|B|$ 把 $A\\cap B$ 的元素算了两次（一次在 A 中，一次在 B 中），需减去重复计算的 $|A\\cap B|$，才得 $A\\cup B$ 真实元素个数。")+
 p("<strong>三元推导：</strong>先加 $|A|+|B|+|C|$，其中两两交集被多加一次故减去 $|A\\cap B|+|B\\cap C|+|C\\cap A|$；但 $A\\cap B\\cap C$ 在第一步加了 3 次、第二步减了 3 次共抵消为 0，需再加回 $|A\\cap B\\cap C|$。"))+
 exa(p("<strong>例：</strong>某班 50 人，喜欢数学 30 人，喜欢物理 25 人，两科都喜欢 15 人。至少喜欢一科的人数 $=30+25-15=40$ 人。")))
}
]},
{"name":"1.3 命题、充要条件与量词","color":"#0284c7","desc":"四种命题关系、充要条件、全称存在量词",
"items":[
{"id":"e1s3-1","name":"命题与四种命题","tags":["def","thm","der"],"brief":"原命题、逆命题、否命题、逆否命题及其等价性。",
"body":wrap(
 defn("命题",p("可以判断真假的陈述句称为<strong>命题</strong>。判断为真的叫真命题，判断为假的叫假命题。"))+
 p("设原命题为「若 p，则 q」，则：① <strong>逆命题</strong>：若 q，则 p；② <strong>否命题</strong>：若 $\\neg p$，则 $\\neg q$；③ <strong>逆否命题</strong>：若 $\\neg q$，则 $\\neg p$。")+
 thm("等价性",p("原命题与其逆否命题同真同假（等价）；逆命题与否命题同真同假。但原命题与逆命题、否命题的真假无必然联系。"))+
 der(p("<strong>逆否命题等价性推导：</strong>「若 p 则 q」即 $p\\Rightarrow q$，其逆否为 $\\neg q\\Rightarrow\\neg p$。用真值表验证四种情形：① p 真 q 真：原命题真，$\\neg q$ 假故逆否命题（假推任意）真；② p 真 q 假：原命题假，$\\neg q$ 真 $\\neg p$ 假故逆否假；③ p 假 q 真：原命题（假推任意）真，$\\neg q$ 假故逆否真；④ p 假 q 假：原命题真，$\\neg q$ 真 $\\neg p$ 真故逆否真。两列真值完全相同，故等价。")))
},
{"id":"e1s3-2","name":"充要条件与量词","tags":["def","der","exa"],"brief":"充分必要条件、充要条件、全称存在量词及其否定。",
"body":wrap(
 defn("充分条件与必要条件",p("若 $p\\Rightarrow q$（p 推出 q），则称 p 是 q 的<strong>充分条件</strong>，q 是 p 的<strong>必要条件</strong>。"))+
 defn("充要条件",p("若 $p\\Leftrightarrow q$（p 与 q 可互推），则称 p 是 q 的<strong>充要条件</strong>。"))+
 der(p("<strong>从集合角度看：</strong>设 $P=\\{x\\mid p(x)\\text{ 成立}\\}$，$Q=\\{x\\mid q(x)\\text{ 成立}\\}$。若 $p\\Rightarrow q$，则 $P\\subseteq Q$（满足 p 的必满足 q）。故 p 是 q 的充分条件 $\\Leftrightarrow$ $P\\subseteq Q$；p 是 q 的充要条件 $\\Leftrightarrow$ $P=Q$。")+
 p("<strong>四种条件关系：</strong>若 $P\\subsetneq Q$，p 是 q 的充分不必要条件；若 $Q\\subsetneq P$，p 是 q 的必要不充分条件；$P=Q$ 即充要；$P,Q$ 无包含则既不充分也不必要。"))+
 exa(p("<strong>例：</strong>「$x=1$」是「$x^2=1$」的充分不必要条件（$x=1\\Rightarrow x^2=1$，但 $x^2=1$ 时 $x$ 也可为 $-1$，故 $\\{1\\}\\subsetneq\\{-1,1\\}$。"))+
 defn("全称量词与存在量词",p("<strong>全称量词</strong> $\\forall$ 表示「对任意」，<strong>存在量词</strong> $\\exists$ 表示「存在」。"))+
 der(p("<strong>量词否定推导：</strong>$\\forall x\\in M, p(x)$ 表示「对所有 $x$ 都有 $p(x)$ 成立」，其否定是「并非所有 $x$ 都使 $p(x)$ 成立」，即「存在 $x$ 使 $p(x)$ 不成立」，记作 $\\exists x\\in M, \\neg p(x)$。这正是「$\\forall$ 与 $\\exists$ 互换、并否定后件」的规则。同理 $\\exists x, p(x)$ 的否定为 $\\forall x, \\neg p(x)$。")))
}
]}
]

# ============ 第二章 代数 ============
ch2_sections = [
{"name":"2.1 数系基础","color":"#7c3aed","desc":"实数、有理数、整数与加减乘除运算律、绝对值",
"items":[
{"id":"e2s1-1","name":"实数、有理数与运算律","tags":["def","thm","der"],"brief":"数系分类、加减乘除运算律与有理数稠密性。",
"fig":"number_system","figCap":"数系包含关系 N ⊂ Z ⊂ Q ⊂ R",
"body":wrap(
 defn("数系",p("<strong>自然数集</strong> $\\mathbb{N}$：$\\{0,1,2,\\dots\\}$；<strong>整数集</strong> $\\mathbb{Z}$：含正负整数与零；<strong>有理数集</strong> $\\mathbb{Q}$：可表为 $\\dfrac{p}{q}$（$p\\in\\mathbb{Z},q\\in\\mathbb{N}^*$，互质）的数；<strong>实数集</strong> $\\mathbb{R}$：有理数与无理数（如 $\\sqrt{2},\\pi$）的全体。关系 $\\mathbb{N}\\subset\\mathbb{Z}\\subset\\mathbb{Q}\\subset\\mathbb{R}$。"))+
 thm("运算律",p("对 $a,b,c\\in\\mathbb{R}$：")+
 fml("\\text{交换律：}\\ a+b=b+a,\\ ab=ba")+
 fml("\\text{结合律：}\\ (a+b)+c=a+(b+c),\\ (ab)c=a(bc)")+
 fml("\\text{分配律：}\\ a(b+c)=ab+ac"))+
 der(p("<strong>有理数稠密性推导：</strong>对任意实数 $x$ 和任意 $\\epsilon>0$，取 $n>\\dfrac{1}{\\epsilon}$（由阿基米德性质存在），则 $\\dfrac{1}{n}<\\epsilon$。设 $m=\\lfloor nx\\rfloor$（不超过 $nx$ 的最大整数），则 $m\\le nx<m+1$，即 $\\dfrac{m}{n}\\le x<\\dfrac{m+1}{n}$。取 $r=\\dfrac{m}{n}\\in\\mathbb{Q}$，则 $|x-r|<\\dfrac{1}{n}<\\epsilon$。故任意实数都可用有理数任意逼近，有理数在实数中稠密。")))
},
{"id":"e2s1-2","name":"绝对值定义与性质","tags":["def","thm","der","app"],"brief":"|a| 几何意义、|ab|=|a||b|、三角不等式推导。",
"fig":"abs_value","figCap":"y=|x| 图像，V 形折线，顶点在原点",
"body":wrap(
 defn("绝对值",p("实数 $a$ 的<strong>绝对值</strong>定义为：")+
 fml("|a|=\\begin{cases}a,&a\\ge 0\\\\-a,&a<0\\end{cases}"))+
 p("几何意义：$|a|$ 表示数 $a$ 在数轴上到原点的距离；$|a-b|$ 表示 $a$ 与 $b$ 在数轴上的距离。")+
 thm("绝对值性质",p("")+
 fml("|ab|=|a|\\cdot|b|,\\quad \\left|\\dfrac{a}{b}\\right|=\\dfrac{|a|}{|b|}\\ (b\\neq 0)")+
 fml("|a|^2=a^2,\\quad |a|=\\sqrt{a^2}")+
 fml("|a|-|b|\\le|a+b|\\le|a|+|b|\\ (\\text{三角不等式})"))+
 der(p("<strong>$|ab|=|a||b|$ 推导：</strong>分四种情况讨论。若 $a\\ge 0,b\\ge 0$，则 $ab\\ge 0$，$|ab|=ab=|a||b|$；若 $a\\ge 0,b<0$，则 $ab\\le 0$，$|ab|=-ab=|a|\\cdot(-b)=|a||b|$；其余两种情形类似。综合四种情况恒有 $|ab|=|a||b|$。")+
 p("<strong>三角不等式推导：</strong>由 $-|a|\\le a\\le |a|$ 与 $-|b|\\le b\\le |b|$ 相加得 $-(|a|+|b|)\\le a+b\\le |a|+|b|$，即 $|a+b|\\le |a|+|b|$。等号成立当且仅当 $ab\\ge 0$（同号或之一为零）。将 $b$ 换为 $-b$ 得 $|a-b|\\le |a|+|b|$。又 $|a|=|(a+b)+(-b)|\\le |a+b|+|b|$，故 $|a|-|b|\\le |a+b|$，下界成立。"))+
 app(p("<strong>应用：</strong>解 $|x-a|<b\\ (b>0)$ 型不等式，利用几何意义得 $-b<x-a<b$，即 $a-b<x<a+b$。")))
},
{"id":"e2s1-3","name":"绝对值不等式与方程","tags":["thm","der","exa"],"brief":"|x|<a、|x|>a 的解集与绝对值方程。",
"fig":"number_line","figCap":"数轴上 |x-a|<b 表示以 a 为中心宽度 2b 的区间",
"body":wrap(
 thm("绝对值不等式解集",p("")+
 fml("|x|<a\\ (a>0)\\Leftrightarrow -a<x<a")+
 fml("|x|>a\\ (a>0)\\Leftrightarrow x<-a\\ \\text{或}\\ x>a"))+
 der(p("<strong>推导：</strong>$|x|<a$ 表示数轴上 $x$ 到原点距离小于 $a$，即 $x\\in(-a,a)$；$|x|>a$ 表示距离大于 $a$，即 $x\\in(-\\infty,-a)\\cup(a,+\\infty)$。对 $|x-a|<b\\ (b>0)$，令 $y=x-a$，则 $|y|<b\\Leftrightarrow -b<y<b\\Leftrightarrow a-b<x<a+b$。")+
 p("<strong>推广：</strong>$|f(x)|<g(x)\\Leftrightarrow -g(x)<f(x)<g(x)$（$g(x)>0$）；$|f(x)|>g(x)\\Leftrightarrow f(x)<-g(x)\\text{ 或 }f(x)>g(x)$。"))+
 exa(p("<strong>例：</strong>解 $|2x-1|<3$。由定理得 $-3<2x-1<3$，即 $-1<x<2$，解集 $(-1,2)$。")))
}
]},
{"name":"2.2 整式运算与乘法公式","color":"#8b5cf6","desc":"多项式运算、乘法公式与因式分解",
"items":[
{"id":"e2s2-1","name":"多项式运算与幂的法则","tags":["def","thm","der","exa"],"brief":"幂的运算法则、多项式加减乘。",
"body":wrap(
 defn("多项式",p("几个单项式的代数和称为<strong>多项式</strong>。多项式中每个单项式称为<strong>项</strong>。多项式的加减实质是合并同类项。"))+
 thm("幂的运算法则",p("")+
 fml("a^m\\cdot a^n = a^{m+n},\\quad (a^m)^n = a^{mn},\\quad (ab)^n = a^n b^n")+
 fml("a^m\\div a^n = a^{m-n}\\ (a\\neq 0,\\ m>n)"))+
 der(p("<strong>幂法则推导：</strong>$a^m\\cdot a^n=\\underbrace{a\\cdots a}_{m}\\cdot\\underbrace{a\\cdots a}_{n}=\\underbrace{a\\cdots a}_{m+n}=a^{m+n}$（同底数幂相乘，底数不变指数相加）。$(a^m)^n=\\underbrace{a^m\\cdots a^m}_{n}=a^{mn}$（幂的乘方，底数不变指数相乘）。$(ab)^n=\\underbrace{(ab)\\cdots(ab)}_{n}=a^n b^n$（积的乘方等于各因子乘方之积）。"))+
 exa(p("<strong>多项式乘法：</strong>$(2x^2+3x-1)(x+2)=2x^3+4x^2+3x^2+6x-x-2=2x^3+7x^2+5x-2$。展开时逐项相乘再合并同类项。")))
},
{"id":"e2s2-2","name":"乘法公式（平方差与完全平方）","tags":["thm","der","exa"],"brief":"平方差、完全平方、三数完全平方推导。",
"body":wrap(
 thm("平方差公式",p("")+
 fml("(a+b)(a-b)=a^2-b^2"))+
 der(p("<strong>平方差推导：</strong>$(a+b)(a-b)=a^2-ab+ab-b^2=a^2-b^2$，交叉项 $-ab$ 与 $+ab$ 抵消，剩 $a^2-b^2$。"))+
 thm("完全平方公式",p("")+
 fml("(a\\pm b)^2=a^2 \\pm 2ab + b^2"))+
 der(p("<strong>完全平方推导：</strong>$(a+b)^2=(a+b)(a+b)=a^2+ab+ba+b^2=a^2+2ab+b^2$（$ab=ba$）。差号情形把 $b$ 换为 $-b$：$(a-b)^2=(a+(-b))^2=a^2+2a(-b)+(-b)^2=a^2-2ab+b^2$。"))+
 thm("三数完全平方",p("")+
 fml("(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca"))+
 der(p("<strong>三数完全平方推导：</strong>$(a+b+c)^2=(a+b+c)(a+b+c)$，逐项相乘：$a^2+ab+ac+ab+b^2+bc+ac+bc+c^2$。合并同类项：$a^2+b^2+c^2+2ab+2bc+2ca$。推广：$n$ 个数和的平方等于各数平方和加上两两乘积的二倍。"))+
 exa(p("<strong>例：</strong>化简 $(x+3)(x-3)+(x+3)^2=(x^2-9)+(x^2+6x+9)=2x^2+6x$。")))
},
{"id":"e2s2-3","name":"立方和差公式与因式分解","tags":["thm","der","exa"],"brief":"立方和、立方差公式推导及因式分解方法。",
"body":wrap(
 thm("立方和与立方差公式",p("")+
 fml("a^3+b^3=(a+b)(a^2-ab+b^2),\\quad a^3-b^3=(a-b)(a^2+ab+b^2)"))+
 der(p("<strong>立方和推导：</strong>$(a+b)(a^2-ab+b^2)=a^3-a^2b+ab^2+a^2b-ab^2+b^3=a^3+b^3$，交叉项 $-a^2b$ 与 $+a^2b$、$+ab^2$ 与 $-ab^2$ 全部抵消。")+
 p("<strong>立方差推导：</strong>直接展开 $(a-b)(a^2+ab+b^2)=a^3+a^2b+ab^2-a^2b-ab^2-b^3=a^3-b^3$，交叉项 $+a^2b$ 与 $-a^2b$、$+ab^2$ 与 $-ab^2$ 全部抵消。"))+
 defn("因式分解方法",p("① <strong>提公因式法</strong>：$ma+mb+mc=m(a+b+c)$；② <strong>公式法</strong>：套用乘法公式逆用；③ <strong>十字相乘法</strong>：$x^2+(p+q)x+pq=(x+p)(x+q)$；④ <strong>分组分解法</strong>：适当分组后提取公因式。"))+
 exa(p("<strong>例：</strong>分解 $x^3-3x^2+4$。试根 $x=-1$ 代入得 $-1-3+4=0$，故 $x+1$ 是因式。多项式除法得 $x^3-3x^2+4=(x+1)(x^2-4x+4)=(x+1)(x-2)^2$。")))
}
]},
{"name":"2.3 方程","color":"#6d28d9","desc":"一元一次、二元一次组、一元二次、高次方程",
"items":[
{"id":"e2s3-1","name":"一元一次与二元一次方程组","tags":["def","der","exa"],"brief":"一次方程解法与代入、加减消元。",
"body":wrap(
 defn("一元一次方程",p("形如 $ax+b=0\\ (a\\neq 0)$ 的方程，解为 $x=-\\dfrac{b}{a}$。"))+
 defn("二元一次方程组",p("形如 $\\begin{cases}a_1x+b_1y=c_1\\\\a_2x+b_2y=c_2\\end{cases}$，常用<strong>代入消元</strong>与<strong>加减消元</strong>求解。"))+
 der(p("<strong>代入消元推导：</strong>由第一式解出 $y=\\dfrac{c_1-a_1x}{b_1}$（$b_1\\neq0$），代入第二式得 $a_2x+b_2\\cdot\\dfrac{c_1-a_1x}{b_1}=c_2$，化简为关于 $x$ 的一元一次方程 $(a_2 b_1-a_1 b_2)x=c_2 b_1-c_1 b_2$，解得 $x=\\dfrac{c_2 b_1-c_1 b_2}{a_2 b_1-a_1 b_2}$。")+
 p("<strong>加减消元推导：</strong>用 $b_2$ 乘第一式、$b_1$ 乘第二式，相减消去 $y$ 得 $(a_1 b_2-a_2 b_1)x=c_1 b_2-c_2 b_1$，得 $x=\\dfrac{c_1 b_2-c_2 b_1}{a_1 b_2-a_2 b_1}$。这与代入法结果一致。当 $a_1 b_2-a_2 b_1=0$ 时需讨论：若 $c_1 b_2-c_2 b_1=0$ 则有无穷多解，否则无解。"))+
 exa(p("<strong>例：</strong>解 $\\begin{cases}x+y=5\\\\2x-y=4\\end{cases}$。两式相加得 $3x=9$，$x=3$，代入得 $y=2$。")))
},
{"id":"e2s3-2","name":"一元二次方程","tags":["thm","der","exa"],"brief":"求根公式推导、判别式、韦达定理推导。",
"fig":"quadratic","figCap":"二次函数 y=ax²+bx+c 图像，顶点为判别式决定根的分布",
"body":wrap(
 thm("求根公式",p("方程 $ax^2+bx+c=0\\ (a\\neq0)$ 的根为：")+
 fml("x = \\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}"))+
 der(p("<strong>求根公式推导（配方法）：</strong>$ax^2+bx+c=0$，两边除以 $a$：$x^2+\\dfrac{b}{a}x=-\\dfrac{c}{a}$。配方：$\\left(x+\\dfrac{b}{2a}\\right)^2=\\dfrac{b^2}{4a^2}-\\dfrac{c}{a}=\\dfrac{b^2-4ac}{4a^2}$。开方：$x+\\dfrac{b}{2a}=\\pm\\dfrac{\\sqrt{b^2-4ac}}{2a}$，移项得 $x=\\dfrac{-b\\pm\\sqrt{b^2-4ac}}{2a}$。"))+
 thm("判别式",p("设 $\\Delta=b^2-4ac$。$\\Delta>0$ 有两不等实根；$\\Delta=0$ 有两相等实根；$\\Delta<0$ 无实根。"))+
 thm("韦达定理",p("若 $x_1,x_2$ 为 $ax^2+bx+c=0$ 的两根，则：")+
 fml("x_1+x_2=-\\dfrac{b}{a},\\quad x_1 x_2=\\dfrac{c}{a}"))+
 der(p("<strong>韦达定理推导：</strong>由求根公式 $x_{1,2}=\\dfrac{-b\\pm\\sqrt{\\Delta}}{2a}$。两根之和 $x_1+x_2=\\dfrac{-b+\\sqrt{\\Delta}}{2a}+\\dfrac{-b-\\sqrt{\\Delta}}{2a}=\\dfrac{-2b}{2a}=-\\dfrac{b}{a}$（根号项抵消）。两根之积 $x_1 x_2=\\dfrac{(-b+\\sqrt{\\Delta})(-b-\\sqrt{\\Delta})}{4a^2}=\\dfrac{b^2-\\Delta}{4a^2}=\\dfrac{b^2-(b^2-4ac)}{4a^2}=\\dfrac{4ac}{4a^2}=\\dfrac{c}{a}$（平方差公式）。"))+
 exa(p("<strong>例：</strong>解 $x^2-5x+6=0$。$\\Delta=25-24=1$，$x=\\dfrac{5\\pm1}{2}$，即 $x_1=3,x_2=2$。验算 $x_1+x_2=5=-(-5)/1$，$x_1 x_2=6=6/1$，符合韦达定理。")))
},
{"id":"e2s3-3","name":"高次方程与有理根定理","tags":["thm","der","exa"],"brief":"因式分解降次、有理根定理。",
"body":wrap(
 thm("有理根定理",p("设 $f(x)=a_n x^n+\\cdots+a_1 x+a_0$ 为整系数多项式，若 $\\dfrac{p}{q}$（既约）是有理根，则 $p\\mid a_0$，$q\\mid a_n$。"))+
 der(p("<strong>推导：</strong>将 $x=\\dfrac{p}{q}$ 代入 $f(x)=0$，乘 $q^n$ 得 $a_n p^n+a_{n-1}p^{n-1}q+\\cdots+a_1 p q^{n-1}+a_0 q^n=0$。移项 $a_0 q^n=-p(a_n p^{n-1}+\\cdots+a_1 q^{n-1})$，因 $\\gcd(p,q)=1$，故 $p\\mid a_0 q^n$，从而 $p\\mid a_0$。同理移项 $a_n p^n=-q(\\cdots)$ 可证 $q\\mid a_n p^n$，故 $q\\mid a_n$。"))+
 thm("降次法",p("对 $n$ 次方程 $f(x)=0$，若找到一个根 $r$，则 $f(x)=(x-r)Q(x)$，$Q(x)$ 为 $n-1$ 次多项式，原方程化为 $Q(x)=0$ 实现降次。"))+
 der(p("<strong>降次推导：</strong>由多项式除法（综合除法），$f(x)=(x-r)Q(x)+f(r)$。若 $r$ 是根则 $f(r)=0$，故 $f(x)=(x-r)Q(x)$。对 $Q(x)=0$ 继续求根，逐次降次直至一次或二次方程。"))+
 exa(p("<strong>例：</strong>解 $x^3-6x^2+11x-6=0$。可能的有理根 $p\\mid 6,q\\mid 1$，试根 $x=1$：$1-6+11-6=0$ 是根。综合除法得 $(x-1)(x^2-5x+6)=(x-1)(x-2)(x-3)=0$，根为 $1,2,3$。")))
}
]},
{"name":"2.4 不等式","color":"#5b21b6","desc":"基本性质、一元一次/二次、分式绝对值、均值不等式与放缩",
"items":[
{"id":"e2s4-1","name":"不等式基本性质与一元一次不等式","tags":["def","thm","der","exa"],"brief":"不等式八条性质与一次不等式解法。",
"body":wrap(
 defn("不等式基本性质",p("① $a>b\\Leftrightarrow b<a$（对称性）；② $a>b,b>c\\Rightarrow a>c$（传递性）；③ $a>b\\Rightarrow a+c>b+c$；④ $a>b,c>0\\Rightarrow ac>bc$；$a>b,c<0\\Rightarrow ac<bc$；⑤ $a>b,c>d\\Rightarrow a+c>b+d$；⑥ $a>b>0,c>d>0\\Rightarrow ac>bd$；⑦ $a>b>0\\Rightarrow a^n>b^n\\ (n\\in\\mathbb{N}^*)$；⑧ $a>b>0\\Rightarrow \\sqrt[n]{a}>\\sqrt[n]{b}$。"))+
 der(p("<strong>性质④推导（乘以负数变号）：</strong>设 $a>b$，则 $a-b>0$。乘以 $c<0$：$(a-b)c<0$（正×负=负），即 $ac-bc<0$，故 $ac<bc$。这就是「不等式两边同乘负数，不等号变向」的根源。")+
 p("<strong>性质⑤推导：</strong>由 $a>b$ 加 $c$ 得 $a+c>b+c$；由 $c>d$ 加 $b$ 得 $b+c>b+d$；再由传递性 $a+c>b+d$。"))+
 exa(p("<strong>例：</strong>解 $2x-3<x+2$。移项 $x<5$，解集 $(-\\infty,5)$。")))
},
{"id":"e2s4-2","name":"一元二次不等式与分式不等式","tags":["thm","der","exa"],"brief":"图像法解二次不等式、分式不等式转化。",
"fig":"inequality","figCap":"二次函数图像法：y>0 对应 x 轴上方区间",
"body":wrap(
 thm("一元二次不等式",p("设 $y=ax^2+bx+c\\ (a>0)$，$\\Delta=b^2-4ac$，两根 $x_1\\le x_2$。")+
 fml("ax^2+bx+c>0\\ (a>0)\\Rightarrow x<x_1\\text{ 或 }x>x_2\\ (\\Delta>0)")+
 fml("ax^2+bx+c<0\\ (a>0)\\Rightarrow x_1<x<x_2\\ (\\Delta>0)"))+
 der(p("<strong>图像法推导：</strong>当 $a>0$ 抛物线开口向上。$\\Delta>0$ 时与 $x$ 轴交于 $x_1,x_2$，则在两根之间函数值小于 0（在 $x$ 轴下方），两根之外大于 0。$\\Delta=0$ 顶点在 $x$ 轴上，$ax^2+bx+c\\ge 0$ 恒成立。$\\Delta<0$ 整个图像在 $x$ 轴上方，$ax^2+bx+c>0$ 恒成立。")+
 p("<strong>分式不等式推导：</strong>$\\dfrac{f(x)}{g(x)}>0\\Leftrightarrow f(x)g(x)>0$（同号相乘为正，注意 $g(x)\\neq 0$）；$\\dfrac{f(x)}{g(x)}\\ge 0\\Leftrightarrow f(x)g(x)\\ge 0\\text{ 且 }g(x)\\neq 0$。"))+
 exa(p("<strong>例：</strong>解 $x^2-5x+6>0$。$\\Delta=1>0$，根 $x_1=2,x_2=3$，开口向上，解集 $(-\\infty,2)\\cup(3,+\\infty)$。")))
},
{"id":"e2s4-3","name":"均值不等式链与常见放缩","tags":["thm","der","exa"],"brief":"均值不等式链推导与常见放缩结论。",
"body":wrap(
 thm("均值不等式链",p("对 $a,b>0$：")+
 fml("\\dfrac{2}{\\dfrac{1}{a}+\\dfrac{1}{b}}\\le\\sqrt{ab}\\le\\dfrac{a+b}{2}\\le\\sqrt{\\dfrac{a^2+b^2}{2}}"))+
 der(p("<strong>算术-几何均值推导：</strong>由 $(\\sqrt{a}-\\sqrt{b})^2\\ge 0$ 展开得 $a+b-2\\sqrt{ab}\\ge 0$，即 $\\dfrac{a+b}{2}\\ge\\sqrt{ab}$，等号当 $a=b$。")+
 p("<strong>几何-调和均值推导：</strong>将算术-几何不等式中的 $a,b$ 换为 $\\dfrac{1}{a},\\dfrac{1}{b}$：$\\dfrac{\\dfrac{1}{a}+\\dfrac{1}{b}}{2}\\ge\\sqrt{\\dfrac{1}{ab}}=\\dfrac{1}{\\sqrt{ab}}$，两边取倒数（正数同取倒数不等号反向）：$\\sqrt{ab}\\ge\\dfrac{2}{\\dfrac{1}{a}+\\dfrac{1}{b}}$。")+
 p("<strong>平方-算术均值推导：</strong>由 $(a-b)^2\\ge 0$ 得 $a^2+b^2\\ge 2ab$，两边加 $a^2+b^2$：$2(a^2+b^2)\\ge (a+b)^2$，即 $\\dfrac{a^2+b^2}{2}\\ge\\left(\\dfrac{a+b}{2}\\right)^2$，开方得 $\\sqrt{\\dfrac{a^2+b^2}{2}}\\ge\\dfrac{a+b}{2}$。"))+
 thm("常见放缩",p("")+
 fml("\\dfrac{1}{n^2}<\\dfrac{1}{n(n-1)}=\\dfrac{1}{n-1}-\\dfrac{1}{n}\\ (n\\ge2)")+
 fml("2^n>n^2\\ (n\\ge5),\\quad \\ln(1+x)<x\\ (x>0),\\quad e^x\\ge 1+x")+
 fml("\\sin x<x\\ (x>0),\\quad \\sqrt{n+1}-\\sqrt{n}<\\dfrac{1}{2\\sqrt{n}}"))+
 der(p("<strong>放缩推导：</strong>① $\\dfrac{1}{n^2}<\\dfrac{1}{n(n-1)}$ 因 $n^2>n(n-1)$（即 $n>0$）；② $\\sqrt{n+1}-\\sqrt{n}=\\dfrac{1}{\\sqrt{n+1}+\\sqrt{n}}<\\dfrac{1}{2\\sqrt{n}}$（分子有理化，分母 $\\sqrt{n+1}+\\sqrt{n}>2\\sqrt{n}$）；③ $\\ln(1+x)<x$：令 $f(x)=x-\\ln(1+x)$，$f'(x)=1-\\dfrac{1}{1+x}=\\dfrac{x}{1+x}>0$（$x>0$），$f(0)=0$ 故 $f(x)>0$；④ $e^x\\ge 1+x$：$e^x$ 的泰勒展开 $e^x=1+x+\\dfrac{x^2}{2}+\\cdots\\ge 1+x$。")+
 p("<strong>指数-多项式放缩：</strong>$2^n>n^2\\ (n\\ge5)$：$n=5$ 时 $32>25$ 成立；设 $n=k$ 成立，$n=k+1$ 时 $2^{k+1}=2\\cdot 2^k>2k^2$，需证 $2k^2>(k+1)^2$ 即 $k^2-2k-1>0$，$k\\ge3$ 时成立，故由数学归纳法对 $n\\ge5$ 成立。"))+
 exa(p("<strong>例：</strong>求 $y=x+\\dfrac{4}{x}\\ (x>0)$ 最小值。由均值不等式 $x+\\dfrac{4}{x}\\ge 2\\sqrt{x\\cdot\\dfrac{4}{x}}=4$，等号当 $x=\\dfrac{4}{x}$ 即 $x=2$，最小值 4。")))
}
]}
]

# ============ 第三章 函数 ============
ch3_sections = [
{"name":"3.1 函数概念与性质","color":"#0d9488","desc":"函数定义、三要素、单调性奇偶性周期性",
"items":[
{"id":"e3s1-1","name":"函数的定义与三要素","tags":["def","der","exa"],"brief":"映射定义函数、定义域值域对应关系三要素。",
"fig":"func_mapping","figCap":"函数 f: A → B 的映射示意，定义域到值域的对应",
"body":wrap(
 defn("函数",p("设 $A,B$ 是两个非空数集，如果存在法则 $f$ 使集合 $A$ 中每个元素按 $f$ 在 $B$ 中都有唯一确定的元素与之对应，则称 $f$ 为从 $A$ 到 $B$ 的<strong>函数</strong>，记 $f:A\\to B$ 或 $y=f(x)$。"))+
 defn("三要素",p("函数由<strong>定义域</strong> $A$、<strong>值域</strong> $\\{f(x)\\mid x\\in A\\}\\subseteq B$、<strong>对应法则</strong> $f$ 三要素确定。两函数相等当且仅当定义域与对应法则都相同。"))+
 der(p("<strong>映射唯一性推导：</strong>设 $A=\\{1,2,3\\}$，$f(1)=2,f(2)=2,f(3)=4$，则值域 $=\\{2,4\\}$（注意 $f(1)=f(2)=2$ 允许「多对一」，但「一对多」不构成函数）。对 $g(x)=x^2$ 与 $h(x)=|x|$，虽 $g(x)=h(x)$ 在 $x\\ge0$ 时相等，但因定义域不同（若取全体实数则相等，若取 $\\mathbb{R}^+$ 则同），需具体判断。")+
 p("<strong>定义域求法推导：</strong>① 分式分母不为 0；② 偶次根号被开方式 $\\ge 0$；③ 对数真数 $>0$、底数 $>0$ 且 $\\neq1$；④ $y=\\tan x$ 要求 $x\\ne\\dfrac{\\pi}{2}+k\\pi$。如 $y=\\dfrac{\\sqrt{x-1}}{\\lg(x+2)}$ 定义域为 $\\{x\\mid x\\ge1, x\\ne-1, x+2>0, x+2\\ne1\\}$，即 $[1,+\\infty)$。"))+
 exa(p("<strong>例：</strong>$f(x)=\\dfrac{1}{\\sqrt{x-1}}+\\lg(3-x)$，定义域：$x-1>0\\Rightarrow x>1$ 且 $3-x>0\\Rightarrow x<3$，故定义域 $(1,3)$。")))
},
{"id":"e3s1-2","name":"单调性、奇偶性与周期性","tags":["def","thm","der"],"brief":"函数单调性、奇偶性、周期性的定义与判定。",
"body":wrap(
 defn("单调性",p("设 $f$ 定义在 $D$ 上，若 $\\forall x_1<x_2\\in D$ 都有 $f(x_1)<f(x_2)$（或 $f(x_1)>f(x_2)$），则称 $f$ 在 $D$ 上<strong>单调递增</strong>（或<strong>递减</strong>）。"))+
 defn("奇偶性",p("若 $f(-x)=-f(x)$，称 $f$ 为<strong>奇函数</strong>，图像关于原点对称；若 $f(-x)=f(x)$，称 $f$ 为<strong>偶函数</strong>，图像关于 $y$ 轴对称。"))+
 defn("周期性",p("若存在非零常数 $T$ 使 $f(x+T)=f(x)$ 恒成立，称 $f$ 为<strong>周期函数</strong>，$T$ 为周期，最小正周期为基本周期。"))+
 thm("复合单调性",p("增函数复合增函数仍为增；减复合减为增（同增异减）；奇复合奇为奇；偶复合偶为偶。"))+
 der(p("<strong>单调性判定推导：</strong>用定义法：任取 $x_1<x_2\\in D$，计算 $f(x_2)-f(x_1)$ 的符号。如证 $f(x)=x+\\dfrac{1}{x}$ 在 $(0,1]$ 递减：$f(x_2)-f(x_1)=(x_2-x_1)+\\left(\\dfrac{1}{x_2}-\\dfrac{1}{x_1}\\right)=(x_2-x_1)-\\dfrac{x_2-x_1}{x_1x_2}=(x_2-x_1)\\left(1-\\dfrac{1}{x_1x_2}\\right)$；当 $0<x_1<x_2\\le1$ 时 $x_1x_2<1$，$1-\\dfrac{1}{x_1x_2}<0$，又 $x_2-x_1>0$，故 $f(x_2)-f(x_1)<0$ 即 $f(x_2)<f(x_1)$，递减。")+
 p("<strong>奇偶性推导：</strong>判定 $f(-x)$ 与 $f(x)$ 关系。如 $f(x)=\\lg\\dfrac{1-x}{1+x}$：$f(-x)=\\lg\\dfrac{1+x}{1-x}=\\lg\\left(\\dfrac{1-x}{1+x}\\right)^{-1}=-\\lg\\dfrac{1-x}{1+x}=-f(x)$，奇函数。")+
 p("<strong>周期推导：</strong>$f(x+2)=-f(x)$ 时，$f(x+4)=-f(x+2)=-(-f(x))=f(x)$，故 $T=4$ 为周期。「自反型」$f(x+a)=-f(x)$ 推出周期 $2a$。")))
},
{"id":"e3s1-3","name":"反函数与复合函数","tags":["def","der","exa"],"brief":"反函数存在条件、复合函数定义域与运算。",
"body":wrap(
 defn("反函数",p("若函数 $y=f(x)$ 在定义域 $D$ 上严格单调，则存在<strong>反函数</strong> $f^{-1}$，其定义域为 $f$ 的值域，对应法则为原法则的逆。"))+
 der(p("<strong>反函数存在性推导：</strong>严格单调函数保证「一对一」映射（不同 $x$ 对应不同 $y$），故映射可逆。若 $f$ 非单调（如 $f(x)=x^2$ 在 $\\mathbb{R}$），则 $y=4$ 对应 $x=\\pm2$，不满足函数唯一性，故需限定区间使 $f$ 单调，如 $f(x)=x^2$ 在 $[0,+\\infty)$ 上反函数为 $f^{-1}(x)=\\sqrt{x}$。")+
 p("<strong>反函数求法：</strong>① 由 $y=f(x)$ 解出 $x=f^{-1}(y)$；② 互换 $x,y$ 得 $y=f^{-1}(x)$；③ 定义域为 $f$ 的值域。如 $y=\\dfrac{2x+1}{x-1}\\ (x>1)$，解 $x=\\dfrac{y+1}{y-2}$，互换得 $f^{-1}(x)=\\dfrac{x+1}{x-2}\\ (x>2)$。"))+
 exa(p("<strong>例：</strong>求 $y=\\lg(x-1)$ 的反函数。由 $10^y=x-1$ 得 $x=10^y+1$，互换 $x,y$：$f^{-1}(x)=10^x+1\\ (x\\in\\mathbb{R})$。")))
}
]},
{"name":"3.2 基本初等函数","color":"#14b8a6","desc":"指数、对数、幂函数与二次函数",
"items":[
{"id":"e3s2-1","name":"指数函数与对数函数","tags":["def","thm","der"],"brief":"指数函数与对数函数定义、图像性质与互为反函数。",
"body":wrap(
 defn("指数函数",p("形如 $y=a^x\\ (a>0,a\\ne1)$ 的函数称为<strong>指数函数</strong>。$a>1$ 时递增，$0<a<1$ 时递减；恒过 $(0,1)$；值域 $(0,+\\infty)$。"))+
 defn("对数函数",p("指数函数的反函数：$y=\\log_a x\\ (a>0,a\\ne1,x>0)$。$a>1$ 时递增，$0<a<1$ 时递减；恒过 $(1,0)$；值域 $\\mathbb{R}$。"))+
 thm("运算法则",p("")+
 fml("a^m\\cdot a^n=a^{m+n},\\quad (a^m)^n=a^{mn},\\quad (ab)^n=a^n b^n")+
 fml("\\log_a(MN)=\\log_a M+\\log_a N,\\quad \\log_a M^n=n\\log_a M,\\quad \\log_a b=\\dfrac{\\log_c b}{\\log_c a}"))+
 der(p("<strong>换底公式推导：</strong>设 $y=\\log_a b$，则 $a^y=b$。两边取以 $c$ 为底的对数：$y\\log_c a=\\log_c b$，故 $y=\\dfrac{\\log_c b}{\\log_c a}$，即 $\\log_a b=\\dfrac{\\log_c b}{\\log_c a}$。")+
 p("<strong>积的对数推导：</strong>设 $M=a^u,N=a^v$（$u=\\log_a M,v=\\log_a N$），则 $MN=a^{u+v}$，故 $\\log_a(MN)=u+v=\\log_a M+\\log_a N$。")+
 p("<strong>单调性推导：</strong>对 $y=a^x$，$a>1$ 时取 $x_1<x_2$，$\\dfrac{a^{x_2}}{a^{x_1}}=a^{x_2-x_1}>1$（因 $a>1,x_2-x_1>0$），故 $a^{x_2}>a^{x_1}$，递增。")))
},
{"id":"e3s2-2","name":"幂函数与二次函数","tags":["def","der","exa"],"brief":"幂函数 $y=x^\\alpha$ 与二次函数图像性质。",
"fig":"quadratic","figCap":"二次函数 $y=ax^2+bx+c$ 的抛物线，顶点为 $(-b/2a, c-b^2/4a)$",
"body":wrap(
 defn("幂函数",p("形如 $y=x^\\alpha$（$\\alpha$ 为常数）的函数称<strong>幂函数</strong>。恒过 $(1,1)$；$\\alpha>0$ 时在 $(0,+\\infty)$ 递增，$\\alpha<0$ 时递减。"))+
 defn("二次函数",p("形如 $y=ax^2+bx+c\\ (a\\ne0)$ 的函数。可化为顶点式 $y=a\\left(x+\\dfrac{b}{2a}\\right)^2+\\dfrac{4ac-b^2}{4a}$，顶点 $\\left(-\\dfrac{b}{2a},\\dfrac{4ac-b^2}{4a}\\right)$，对称轴 $x=-\\dfrac{b}{2a}$。"))+
 der(p("<strong>顶点式推导：</strong>$y=ax^2+bx+c=a\\left(x^2+\\dfrac{b}{a}x\\right)+c=a\\left[\\left(x+\\dfrac{b}{2a}\\right)^2-\\dfrac{b^2}{4a^2}\\right]+c=a\\left(x+\\dfrac{b}{2a}\\right)^2-\\dfrac{b^2}{4a}+c=a\\left(x+\\dfrac{b}{2a}\\right)^2+\\dfrac{4ac-b^2}{4a}$。")+
 p("<strong>判别式与根关系推导：</strong>令 $y=0$ 得 $ax^2+bx+c=0$，配方可写 $a\\left(x+\\dfrac{b}{2a}\\right)^2=\\dfrac{b^2-4ac}{4a}$。当 $\\Delta=b^2-4ac>0$，方程有二不等实根 $x=-\\dfrac{b}{2a}\\pm\\dfrac{\\sqrt{\\Delta}}{2a}$；$\\Delta=0$ 有重根；$\\Delta<0$ 无实根。"))+
 exa(p("<strong>例：</strong>求 $y=x^2-4x+3$ 顶点。$-\\dfrac{b}{2a}=-\\dfrac{-4}{2}=2$，$\\dfrac{4ac-b^2}{4a}=\\dfrac{12-16}{4}=-1$，顶点 $(2,-1)$，对称轴 $x=2$。")))
},
{"id":"e3s2-3","name":"分段函数与绝对值函数","tags":["def","der","exa"],"brief":"分段函数定义、绝对值函数图像与去绝对值法。",
"fig":"abs_value","figCap":"绝对值函数 $y=|x|$ 的 V 形图像",
"body":wrap(
 defn("分段函数",p("在不同区间用不同表达式定义的函数称<strong>分段函数</strong>。如符号函数 $\\operatorname{sgn}(x)=\\begin{cases}1,&x>0\\\\0,&x=0\\\\-1,&x<0\\end{cases}$。"))+
 defn("绝对值函数",p("$y=|x|=\\begin{cases}x,&x\\ge0\\\\-x,&x<0\\end{cases}$，图像为 V 形，顶点在原点。"))+
 der(p("<strong>绝对值去法推导：</strong>① 平方法：$|a|^2=a^2$；② 零点分段法：求各绝对值为 0 的点（零点），划分区间后逐段去绝对值；③ 平方法：$|f(x)|=\\sqrt{f(x)^2}$。")+
 p("<strong>$y=|x-2|+|x+1|$ 化简推导：</strong>零点 $x=2$ 与 $x=-1$ 分三段：① $x<-1$：$y=-(x-2)-(x+1)=-2x+1$；② $-1\\le x<2$：$y=-(x-2)+(x+1)=3$；③ $x\\ge2$：$y=(x-2)+(x+1)=2x-1$。故最小值为 3（在 $[-1,2]$ 上恒为 3）。"))+
 exa(p("<strong>例：</strong>解 $|x-1|<2$。$-2<x-1<2$，即 $-1<x<3$，解集 $(-1,3)$。")))
}
]},
{"name":"3.3 三角函数","color":"#0f766e","desc":"任意角三角函数、同角关系、诱导公式、和差倍半角",
"items":[
{"id":"e3s3-1","name":"六个三角函数的定义","tags":["def","der","exa"],"brief":"弧度制、单位圆定义六个三角函数、符号规律与三角函数线。",
"fig":"trig_circle","figCap":"单位圆上点 $P(\\cos\\theta,\\sin\\theta)$，三角函数线示意",
"body":wrap(
 defn("弧度制",p("弧长等于半径的弧所对圆心角为 1 弧度（rad）。$1^\\circ=\\dfrac{\\pi}{180}\\,\\text{rad}$，$\\pi\\,\\text{rad}=180^\\circ$。"))+
 defn("六个三角函数定义",p("设 $\\alpha$ 为任意角，终边上一点 $P(x,y)$，$r=\\sqrt{x^2+y^2}>0$，则六个三角函数定义为：")+
 fml("\\sin\\alpha=\\dfrac{y}{r},\\quad \\cos\\alpha=\\dfrac{x}{r},\\quad \\tan\\alpha=\\dfrac{y}{x}")+
 fml("\\cot\\alpha=\\dfrac{x}{y},\\quad \\sec\\alpha=\\dfrac{r}{x},\\quad \\csc\\alpha=\\dfrac{r}{y}")+
 p("其中三组互为倒数：$\\tan\\alpha=\\dfrac{1}{\\cot\\alpha}$，$\\cos\\alpha=\\dfrac{1}{\\sec\\alpha}$，$\\sin\\alpha=\\dfrac{1}{\\csc\\alpha}$；$\\cot,\\sec,\\csc$ 常合称<strong>余切、正割、余割</strong>。"))+
 der(p("<strong>单位圆推导：</strong>取 $r=1$（单位圆上），点 $P(\\cos\\alpha,\\sin\\alpha)$，由勾股定理 $x^2+y^2=1$ 即 $\\sin^2\\alpha+\\cos^2\\alpha=1$。")+
 p("<strong>倒数关系推导：</strong>由定义 $\\dfrac{1}{\\cos\\alpha}=\\dfrac{1}{x/r}=\\dfrac{r}{x}=\\sec\\alpha$；$\\dfrac{1}{\\sin\\alpha}=\\dfrac{r}{y}=\\csc\\alpha$；$\\dfrac{1}{\\tan\\alpha}=\\dfrac{x}{y}=\\cot\\alpha$。")+
 p("<strong>符号规律推导：</strong>由定义：第一象限 $x>0,y>0$ 故六个函数均正；第二象限 $x<0,y>0$ 故 $\\sin,\\csc$ 正、其余负；第三象限 $x<0,y<0$ 故 $\\tan,\\cot$ 正（同号相除）、其余负；第四象限 $x>0,y<0$ 故 $\\cos,\\sec$ 正、其余负，即「一全正、二正弦、三正切、四余弦」。")+
 p("<strong>定义域推导：</strong>$\\tan,\\sec$ 的分母为 $x$，故 $x=0$ 即 $\\alpha=\\dfrac{\\pi}{2}+k\\pi$ 处无定义；$\\cot,\\csc$ 的分母为 $y$，故 $y=0$ 即 $\\alpha=k\\pi$ 处无定义。")+
 p("<strong>弧长扇形推导：</strong>弧长 $l=|\\alpha|\\cdot r$（$\\alpha$ 为弧度），扇形面积 $S=\\dfrac{1}{2}lr=\\dfrac{1}{2}|\\alpha|r^2$。"))+
 exa(p("<strong>例：</strong>$\\alpha=\\dfrac{\\pi}{3}$，$\\sin\\dfrac{\\pi}{3}=\\dfrac{\\sqrt3}{2}$，$\\cos\\dfrac{\\pi}{3}=\\dfrac{1}{2}$，$\\tan\\dfrac{\\pi}{3}=\\sqrt3$，$\\cot\\dfrac{\\pi}{3}=\\dfrac{\\sqrt3}{3}$，$\\sec\\dfrac{\\pi}{3}=2$，$\\csc\\dfrac{\\pi}{3}=\\dfrac{2\\sqrt3}{3}$。")))
},
{"id":"e3s3-2","name":"同角关系与诱导公式","tags":["def","thm","der"],"brief":"同角三角函数基本关系、诱导公式推导。",
"body":wrap(
 thm("同角关系",p("")+
 fml("\\sin^2\\alpha+\\cos^2\\alpha=1,\\quad \\tan\\alpha=\\dfrac{\\sin\\alpha}{\\cos\\alpha}")+
 fml("1+\\tan^2\\alpha=\\sec^2\\alpha,\\quad 1+\\cot^2\\alpha=\\csc^2\\alpha"))+
 thm("诱导公式",p("「奇变偶不变，符号看象限」：$\\alpha+\\dfrac{k\\pi}{2}$ 的变换中，$k$ 为奇数函数名变（正余互换），$k$ 为偶数不变，符号由 $\\alpha$ 视作锐角时所在象限确定。"))+
 der(p("<strong>平方和推导：</strong>由单位圆 $x^2+y^2=1$ 代入 $x=\\cos\\alpha,y=\\sin\\alpha$ 即得 $\\sin^2\\alpha+\\cos^2\\alpha=1$。")+
 p("<strong>商关系推导：</strong>$\\dfrac{\\sin\\alpha}{\\cos\\alpha}=\\dfrac{y/r}{x/r}=\\dfrac{y}{x}=\\tan\\alpha$。")+
 p("<strong>$\\sin(\\pi-\\alpha)=\\sin\\alpha$ 推导：</strong>$\\pi-\\alpha$ 与 $\\alpha$ 终边关于 $y$ 轴对称，横坐标取反纵坐标相同，故 $\\cos(\\pi-\\alpha)=-\\cos\\alpha,\\sin(\\pi-\\alpha)=\\sin\\alpha$。")+
 p("<strong>$\\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\cos\\alpha$ 推导：</strong>$\\dfrac{\\pi}{2}-\\alpha$ 与 $\\alpha$ 的终边关于 $y=x$ 对称，横纵坐标互换，故 $\\sin\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\cos\\alpha,\\cos\\left(\\dfrac{\\pi}{2}-\\alpha\\right)=\\sin\\alpha$。")))
},
{"id":"e3s3-3","name":"和差倍半角公式","tags":["def","thm","der"],"brief":"和角公式、倍角半角公式及其推导。",
"body":wrap(
 thm("和角公式",p("")+
 fml("\\sin(\\alpha\\pm\\beta)=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta")+
 fml("\\cos(\\alpha\\pm\\beta)=\\cos\\alpha\\cos\\beta\\mp\\sin\\alpha\\sin\\beta"))+
 thm("倍角公式",p("")+
 fml("\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha,\\quad \\cos 2\\alpha=\\cos^2\\alpha-\\sin^2\\alpha=2\\cos^2\\alpha-1=1-2\\sin^2\\alpha")+
 fml("\\tan 2\\alpha=\\dfrac{2\\tan\\alpha}{1-\\tan^2\\alpha}"))+
 der(p("<strong>$\\cos(\\alpha-\\beta)$ 推导：</strong>设单位圆上 $A(\\cos\\alpha,\\sin\\alpha),B(\\cos\\beta,\\sin\\beta)$，则 $|AB|^2=(\\cos\\alpha-\\cos\\beta)^2+(\\sin\\alpha-\\sin\\beta)^2=2-2(\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta)$。另一方面，$|AB|=2\\sin\\dfrac{\\alpha-\\beta}{2}$，故 $|AB|^2=4\\sin^2\\dfrac{\\alpha-\\beta}{2}=2-2\\cos(\\alpha-\\beta)$。比较得 $\\cos(\\alpha-\\beta)=\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta$。")+
 p("<strong>和角公式推导：</strong>令上式中 $\\beta$ 换成 $-\\beta$ 得 $\\cos(\\alpha+\\beta)=\\cos\\alpha\\cos\\beta-\\sin\\alpha\\sin\\beta$；由 $\\sin\\alpha=\\cos\\left(\\dfrac{\\pi}{2}-\\alpha\\right)$ 化归得 $\\sin(\\alpha+\\beta)=\\sin\\alpha\\cos\\beta+\\cos\\alpha\\sin\\beta$。")+
 p("<strong>倍角推导：</strong>在 $\\sin(\\alpha+\\beta)$ 中令 $\\alpha=\\beta$ 得 $\\sin 2\\alpha=2\\sin\\alpha\\cos\\alpha$；在 $\\cos(\\alpha+\\beta)$ 中令 $\\alpha=\\beta$ 得 $\\cos 2\\alpha=\\cos^2\\alpha-\\sin^2\\alpha$，再由 $\\sin^2\\alpha+\\cos^2\\alpha=1$ 得另两形式 $2\\cos^2\\alpha-1$ 与 $1-2\\sin^2\\alpha$。")+
 p("<strong>半角推导：</strong>由 $\\cos 2\\alpha=2\\cos^2\\alpha-1$，令 $2\\alpha=\\theta$ 得 $\\cos\\theta=2\\cos^2\\dfrac{\\theta}{2}-1$，故 $\\cos\\dfrac{\\theta}{2}=\\pm\\sqrt{\\dfrac{1+\\cos\\theta}{2}}$；同理 $\\sin\\dfrac{\\theta}{2}=\\pm\\sqrt{\\dfrac{1-\\cos\\theta}{2}}$。")))
},
{"id":"e3s3-4","name":"三角恒等变换","tags":["thm","der","exa"],"brief":"和差化积、积化和差与万能公式。",
"body":wrap(
 thm("和差化积",p("")+
 fml("\\sin\\alpha+\\sin\\beta=2\\sin\\dfrac{\\alpha+\\beta}{2}\\cos\\dfrac{\\alpha-\\beta}{2}")+
 fml("\\cos\\alpha+\\cos\\beta=2\\cos\\dfrac{\\alpha+\\beta}{2}\\cos\\dfrac{\\alpha-\\beta}{2}"))+
 thm("积化和差",p("")+
 fml("\\sin\\alpha\\cos\\beta=\\dfrac{1}{2}[\\sin(\\alpha+\\beta)+\\sin(\\alpha-\\beta)]")+
 fml("\\cos\\alpha\\sin\\beta=\\dfrac{1}{2}[\\sin(\\alpha+\\beta)-\\sin(\\alpha-\\beta)]"))+
 der(p("<strong>和差化积推导：</strong>令 $\\alpha+\\beta=2A,\\alpha-\\beta=2B$，由和角公式 $\\sin A\\cos B=\\dfrac{1}{2}[\\sin(A+B)+\\sin(A-B)]$，即 $2\\sin A\\cos B=\\sin(A+B)+\\sin(A-B)$。代回 $A=\\dfrac{\\alpha+\\beta}{2},B=\\dfrac{\\alpha-\\beta}{2}$ 得 $\\sin\\alpha+\\sin\\beta=2\\sin\\dfrac{\\alpha+\\beta}{2}\\cos\\dfrac{\\alpha-\\beta}{2}$。")+
 p("<strong>积化和差推导：</strong>由和角公式 $\\sin(A+B)=\\sin A\\cos B+\\cos A\\sin B$ 与 $\\sin(A-B)=\\sin A\\cos B-\\cos A\\sin B$，相加得 $\\sin A\\cos B=\\dfrac{1}{2}[\\sin(A+B)+\\sin(A-B)]$。")+
 p("<strong>万能公式推导：</strong>令 $t=\\tan\\dfrac{\\alpha}{2}$，由 $\\sin\\alpha=2\\sin\\dfrac{\\alpha}{2}\\cos\\dfrac{\\alpha}{2}=\\dfrac{2\\tan\\dfrac{\\alpha}{2}}{\\sec^2\\dfrac{\\alpha}{2}}=\\dfrac{2t}{1+t^2}$；$\\cos\\alpha=\\cos^2\\dfrac{\\alpha}{2}-\\sin^2\\dfrac{\\alpha}{2}=\\dfrac{1-t^2}{1+t^2}$；$\\tan\\alpha=\\dfrac{2t}{1-t^2}$。"))+
 exa(p("<strong>例：</strong>$\\sin 75^\\circ=\\sin(45^\\circ+30^\\circ)=\\dfrac{\\sqrt2}{2}\\cdot\\dfrac{\\sqrt3}{2}+\\dfrac{\\sqrt2}{2}\\cdot\\dfrac{1}{2}=\\dfrac{\\sqrt6+\\sqrt2}{4}$。")))
}
]},
{"name":"3.4 反三角函数","color":"#15803d","desc":"反三角函数定义与关系",
"items":[
{"id":"e3s4-1","name":"反三角函数定义与关系","tags":["def","thm","der"],"brief":"反正弦、反余弦、反正切定义与互补关系。",
"body":wrap(
 defn("反三角函数",p("在主值区间上的反函数：<strong>反正弦</strong> $y=\\arcsin x$（$x\\in[-1,1],y\\in\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$）；<strong>反余弦</strong> $y=\\arccos x$（$x\\in[-1,1],y\\in[0,\\pi]$）；<strong>反正切</strong> $y=\\arctan x$（$x\\in\\mathbb{R},y\\in\\left(-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right)$）。"))+
 thm("互补关系",p("")+
 fml("\\arcsin x+\\arccos x=\\dfrac{\\pi}{2}\\ (|x|\\le1)")+
 fml("\\arctan x+\\operatorname{arccot} x=\\dfrac{\\pi}{2}"))+
 der(p("<strong>互补关系推导：</strong>设 $\\alpha=\\arcsin x$，则 $\\sin\\alpha=x,\\alpha\\in\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$。由 $\\sin\\alpha=\\cos\\left(\\dfrac{\\pi}{2}-\\alpha\\right)$ 且 $\\dfrac{\\pi}{2}-\\alpha\\in[0,\\pi]$，故 $\\arccos x=\\dfrac{\\pi}{2}-\\alpha=\\dfrac{\\pi}{2}-\\arcsin x$，即 $\\arcsin x+\\arccos x=\\dfrac{\\pi}{2}$。")+
 p("<strong>反三角恒等推导：</strong>$\\sin(\\arcsin x)=x$（定义）；$\\cos(\\arcsin x)=\\sqrt{1-\\sin^2(\\arcsin x)}=\\sqrt{1-x^2}$（由 $\\arcsin x\\in\\left[-\\dfrac{\\pi}{2},\\dfrac{\\pi}{2}\\right]$ 时 $\\cos\\ge0$）；$\\tan(\\arccos x)=\\dfrac{\\sin(\\arccos x)}{\\cos(\\arccos x)}=\\dfrac{\\sqrt{1-x^2}}{x}$。")))
}
]}
]

# ============ 第四章 数列 ============
ch4_sections = [
{"name":"4.1 等差数列","color":"#c2410c","desc":"通项公式、前 n 项和、等差中项与性质",
"items":[
{"id":"e4s1-1","name":"等差数列通项与求和","tags":["def","thm","der","exa"],"brief":"等差数列定义、通项公式与前 n 项和公式推导。",
"fig":"sequence","figCap":"等差数列 $a_n=a_1+(n-1)d$ 在数轴上的分布",
"body":wrap(
 defn("等差数列",p("若数列 $\\{a_n\\}$ 满足 $a_{n+1}-a_n=d$（常数），称 $\\{a_n\\}$ 为<strong>等差数列</strong>，$d$ 为公差。"))+
 thm("通项与求和",p("")+
 fml("a_n=a_1+(n-1)d,\\quad S_n=\\dfrac{n(a_1+a_n)}{2}=na_1+\\dfrac{n(n-1)}{2}d"))+
 der(p("<strong>通项推导：</strong>由 $a_2-a_1=d,a_3-a_2=d,\\ldots,a_n-a_{n-1}=d$ 累加：$a_n-a_1=(n-1)d$，故 $a_n=a_1+(n-1)d$。")+
 p("<strong>求和推导（倒序相加）：</strong>设 $S_n=a_1+a_2+\\cdots+a_n$，将各项倒序写：$S_n=a_n+a_{n-1}+\\cdots+a_1$。两式相加：$2S_n=(a_1+a_n)+(a_2+a_{n-1})+\\cdots+(a_n+a_1)$。由等差性质 $a_1+a_n=a_2+a_{n-1}=\\cdots$（首末两项之和等于第二项与倒数第二项之和，因 $a_k+a_{n-k+1}=a_1+(k-1)d+a_1+(n-k)d=2a_1+(n-1)d=a_1+a_n$），共 $n$ 项，故 $2S_n=n(a_1+a_n)$，$S_n=\\dfrac{n(a_1+a_n)}{2}$。"))+
 exa(p("<strong>例：</strong>等差数列 $a_1=2,d=3$，求 $S_{10}$。$a_{10}=2+9\\cdot3=29$，$S_{10}=\\dfrac{10(2+29)}{2}=155$。")))
},
{"id":"e4s1-2","name":"等差数列的性质","tags":["thm","der","exa"],"brief":"等差中项、片段和成等差、下标和性质。",
"body":wrap(
 thm("等差中项",p("若 $a,b,c$ 成等差数列，则 $2b=a+c$，$b=\\dfrac{a+c}{2}$ 称 $a,c$ 的等差中项。"))+
 thm("片段和性质",p("等差数列 $\\{a_n\\}$ 中，$S_n,S_{2n}-S_n,S_{3n}-S_{2n},\\ldots$ 仍成等差数列，公差为 $n^2 d$。"))+
 thm("下标和性质",p("若 $m+n=p+q$（$m,n,p,q$ 为正整数），则 $a_m+a_n=a_p+a_q$。"))+
 der(p("<strong>片段和推导：</strong>设 $A=S_n,B=S_{2n}-S_n,C=S_{3n}-S_{2n}$。$B=A+\\dfrac{n(n-1)}{2}d\\cdot2+nd\\cdot n$（第 $n+1$ 到 $2n$ 项是首项 $a_1+nd$、公差 $d$ 的等差数列，和 $=n(a_1+nd)+\\dfrac{n(n-1)}{2}d$）。简化计算：$A=na_1+\\dfrac{n(n-1)}{2}d$，$B=n(a_1+nd)+\\dfrac{n(n-1)}{2}d=A+n^2 d$，$C=n(a_1+2nd)+\\dfrac{n(n-1)}{2}d=B+n^2 d$。故 $A,B,C$ 成等差，公差 $n^2 d$。")+
 p("<strong>下标和推导：</strong>$a_m+a_n=(a_1+(m-1)d)+(a_1+(n-1)d)=2a_1+(m+n-2)d$，同理 $a_p+a_q=2a_1+(p+q-2)d$。$m+n=p+q$ 时两式相等。"))+
 exa(p("<strong>例：</strong>等差数列 $\\{a_n\\}$ 中 $a_3+a_{11}=20$，求 $S_{13}$。$a_3+a_{11}=a_1+a_{13}=20$（下标 $3+11=1+13$），$S_{13}=\\dfrac{13(a_1+a_{13})}{2}=\\dfrac{13\\cdot20}{2}=130$。")))
}
]},
{"name":"4.2 等比数列","color":"#dc2626","desc":"通项公式、前 n 项和、无穷等比与递推",
"items":[
{"id":"e4s2-1","name":"等比数列通项与求和","tags":["def","thm","der","exa"],"brief":"等比数列定义、通项与前 n 项和错位相减推导。",
"body":wrap(
 defn("等比数列",p("若 $\\dfrac{a_{n+1}}{a_n}=q$（常数，$q\\ne0$），称 $\\{a_n\\}$ 为<strong>等比数列</strong>，$q$ 为公比。"))+
 thm("通项与求和",p("")+
 fml("a_n=a_1 q^{n-1},\\quad S_n=\\dfrac{a_1(1-q^n)}{1-q}\\ (q\\ne1),\\quad S_n=na_1\\ (q=1)"))+
 der(p("<strong>通项推导：</strong>由 $\\dfrac{a_2}{a_1}=q,\\dfrac{a_3}{a_2}=q,\\ldots,\\dfrac{a_n}{a_{n-1}}=q$ 连乘：$\\dfrac{a_n}{a_1}=q^{n-1}$，故 $a_n=a_1 q^{n-1}$。")+
 p("<strong>求和推导（错位相减）：</strong>$S_n=a_1+a_1 q+a_1 q^2+\\cdots+a_1 q^{n-1}$ ①；两边乘 $q$：$qS_n=a_1 q+a_1 q^2+\\cdots+a_1 q^{n}$ ②。①-②：$(1-q)S_n=a_1-a_1 q^n=a_1(1-q^n)$，当 $q\\ne1$ 时 $S_n=\\dfrac{a_1(1-q^n)}{1-q}$。"))+
 exa(p("<strong>例：</strong>等比数列 $a_1=1,q=2$，求 $S_5$。$S_5=\\dfrac{1\\cdot(1-2^5)}{1-2}=\\dfrac{-31}{-1}=31$，即 $1+2+4+8+16=31$。")))
},
{"id":"e4s2-2","name":"无穷等比级数与递推","tags":["def","thm","der"],"brief":"无穷递缩等比数列求和与一阶递推。",
"body":wrap(
 thm("无穷等比求和",p("当 $|q|<1$ 时，无穷等比数列各项和 $S=\\dfrac{a_1}{1-q}$。"))+
 thm("一阶递推",p("$a_{n+1}=p a_n+q\\ (p\\ne1)$ 型递推可通过待定系数化为等比数列。"))+
 der(p("<strong>无穷求和推导：</strong>由 $S_n=\\dfrac{a_1(1-q^n)}{1-q}=\\dfrac{a_1}{1-q}-\\dfrac{a_1 q^n}{1-q}$。当 $|q|<1$ 时，随着项数 $n$ 无限增大，$q^n$ 无限接近于 0，从而 $\\dfrac{a_1 q^n}{1-q}$ 无限接近于 0，故无穷等比数列各项之和 $S=\\dfrac{a_1}{1-q}$。")+
 p("<strong>递推化简推导：</strong>设 $a_{n+1}=p a_n+q$，待定常数 $c$ 使 $a_{n+1}-c=p(a_n-c)$，展开 $a_{n+1}=p a_n+(1-p)c$，比较得 $q=(1-p)c$，$c=\\dfrac{q}{1-p}$。令 $b_n=a_n-c$，则 $b_{n+1}=p b_n$ 为等比，$b_n=(a_1-c)p^{n-1}$，故 $a_n=c+(a_1-c)p^{n-1}$。")+
 p("<strong>循环小数化分数推导：</strong>$0.\\dot{3}=0.333\\ldots=\\dfrac{3}{10}+\\dfrac{3}{100}+\\cdots$，首项 $\\dfrac{3}{10}$，公比 $\\dfrac{1}{10}$，$|q|<1$，和 $=\\dfrac{3/10}{1-1/10}=\\dfrac{1}{3}$。")))
}
]},
{"name":"4.3 数列求和方法","color":"#ea580c","desc":"公式法、倒序相加、错位相减、裂项相消、分组、并项、累加与累乘",
"items":[
{"id":"e4s3-1","name":"裂项相消法","tags":["thm","der","exa"],"brief":"相邻整数乘积裂项与一般裂项方法。",
"body":wrap(
 thm("裂项原理",p("")+
 fml("\\dfrac{1}{n(n+1)}=\\dfrac{1}{n}-\\dfrac{1}{n+1}")+
 fml("\\dfrac{1}{\\sqrt{n}+\\sqrt{n+1}}=\\sqrt{n+1}-\\sqrt{n}"))+
 der(p("<strong>裂项推导：</strong>$\\dfrac{1}{n(n+1)}=\\dfrac{1}{n}-\\dfrac{1}{n+1}$，因 $\\dfrac{1}{n}-\\dfrac{1}{n+1}=\\dfrac{(n+1)-n}{n(n+1)}=\\dfrac{1}{n(n+1)}$。")+
 p("<strong>求和推导：</strong>$S_n=\\sum_{k=1}^n\\dfrac{1}{k(k+1)}=\\sum_{k=1}^n\\left(\\dfrac{1}{k}-\\dfrac{1}{k+1}\\right)=\\left(\\dfrac{1}{1}-\\dfrac{1}{2}\\right)+\\left(\\dfrac{1}{2}-\\dfrac{1}{3}\\right)+\\cdots+\\left(\\dfrac{1}{n}-\\dfrac{1}{n+1}\\right)$。中间项全部抵消，仅剩首末：$S_n=1-\\dfrac{1}{n+1}=\\dfrac{n}{n+1}$。")+
 p("<strong>根式裂项推导：</strong>$\\dfrac{1}{\\sqrt{n}+\\sqrt{n+1}}$ 分子有理化：$=\\dfrac{\\sqrt{n+1}-\\sqrt{n}}{(n+1)-n}=\\sqrt{n+1}-\\sqrt{n}$，求和 $\\sum_{k=1}^n(\\sqrt{k+1}-\\sqrt{k})=\\sqrt{n+1}-1$。"))+
 exa(p("<strong>例：</strong>$\\sum_{k=1}^{99}\\dfrac{1}{k(k+1)}=1-\\dfrac{1}{100}=\\dfrac{99}{100}$。")))
},
{"id":"e4s3-2","name":"错位相减法","tags":["thm","der","exa"],"brief":"等差乘等比型数列求和。",
"body":wrap(
 thm("错位相减",p("形如 $b_n=a_n\\cdot c_n$（$\\{a_n\\}$ 等差、$\\{c_n\\}$ 等比）的数列，可通过乘公比再相减求和。"))+
 der(p("<strong>推导：</strong>设 $S_n=\\sum_{k=1}^n k\\cdot 2^k=1\\cdot2+2\\cdot2^2+\\cdots+n\\cdot2^n$ ①。两边乘 $q=2$：$2S_n=1\\cdot2^2+2\\cdot2^3+\\cdots+(n-1)\\cdot2^n+n\\cdot2^{n+1}$ ②。①-②：$-S_n=(1\\cdot2)+\\sum_{k=2}^n(k-k)\\cdot2^k-n\\cdot2^{n+1}=(2)+(-n\\cdot2^{n+1}+\\text{调整})$。整理：$-S_n=2+0+\\cdots+0-n\\cdot2^{n+1}+(n\\cdot2^n)$，化简 $S_n=(n-1)\\cdot2^{n+1}+2$。")+
 p("<strong>一般推导：</strong>对 $S_n=\\sum_{k=1}^n k q^k$，乘 $q$ 得 $qS_n=\\sum_{k=1}^n k q^{k+1}=\\sum_{k=2}^{n+1}(k-1)q^k$。相减 $(1-q)S_n=\\sum_{k=1}^n q^k-n q^{n+1}=\\dfrac{q(1-q^n)}{1-q}-n q^{n+1}$，故 $S_n=\\dfrac{q-(n+1)q^{n+1}+n q^{n+2}}{(1-q)^2}$。"))+
 exa(p("<strong>例：</strong>$S_n=1\\cdot2+2\\cdot4+3\\cdot8+\\cdots+n\\cdot2^n$，由公式 $S_n=(n-1)2^{n+1}+2$。$n=3$ 时 $S_3=2+8+24=34$，验证 $(3-1)2^4+2=2\\cdot16+2=34$。")))
},
{"id":"e4s3-3","name":"倒序相加与分组求和","tags":["thm","der","exa"],"brief":"对称数列倒序相加、通项分组求和。",
"body":wrap(
 thm("倒序相加",p("首末等距项之和为常数的数列，可倒序相加。"))+
 thm("分组求和",p("若 $a_n=b_n+c_n$，则 $S_n=\\sum b_n+\\sum c_n$，分别求和再合并。"))+
 der(p("<strong>平方和推导（数学归纳法）：</strong>证 $\\sum_{k=1}^n k^2=\\dfrac{n(n+1)(2n+1)}{6}$。$n=1$：$1=\\dfrac{1\\cdot2\\cdot3}{6}=1$ 成立。设 $n=k$ 成立，$n=k+1$ 时：$\\sum_{i=1}^{k+1}i^2=\\dfrac{k(k+1)(2k+1)}{6}+(k+1)^2=\\dfrac{(k+1)[k(2k+1)+6(k+1)]}{6}=\\dfrac{(k+1)(2k^2+7k+6)}{6}=\\dfrac{(k+1)(k+2)(2k+3)}{6}$，即 $n=k+1$ 形式，得证。")+
 p("<strong>立方和推导（倒序思想）：</strong>$\\sum_{k=1}^n k^3=\\left[\\dfrac{n(n+1)}{2}\\right]^2$。利用恒等式 $k^3-(k-1)^3=3k^2-3k+1$ 累加：$n^3=3\\sum k^2-3\\sum k+n$，代入 $\\sum k^2=\\dfrac{n(n+1)(2n+1)}{6}$ 与 $\\sum k=\\dfrac{n(n+1)}{2}$ 解得 $\\sum k^3$。")+
 p("<strong>分组推导：</strong>如 $a_n=2^n+n$，则 $S_n=\\sum 2^k+\\sum k=\\dfrac{2(2^n-1)}{2-1}+\\dfrac{n(n+1)}{2}=2^{n+1}-2+\\dfrac{n(n+1)}{2}$。"))+
 exa(p("<strong>例：</strong>求 $1+2+\\cdots+100$。倒序相加 $2S=(1+100)+(2+99)+\\cdots=101\\times100$，$S=5050$。")))
},
{"id":"e4s3-4","name":"公式法与并项求和法","tags":["thm","der","exa"],"brief":"直接套用已知求和公式、相邻项合并求和。",
"body":wrap(
 thm("常用求和公式",p("")+
 fml("\\sum_{k=1}^n k=\\dfrac{n(n+1)}{2},\\quad \\sum_{k=1}^n k^2=\\dfrac{n(n+1)(2n+1)}{6},\\quad \\sum_{k=1}^n k^3=\\left[\\dfrac{n(n+1)}{2}\\right]^2"))+
 thm("并项求和",p("当数列相邻两项（或若干项）之和为常数或易于计算时，可两两（或若干项）合并后再求和。"))+
 der(p("<strong>公式法推导：</strong>自然数求和 $\\sum k=\\dfrac{n(n+1)}{2}$ 由倒序相加得；平方和 $\\sum k^2=\\dfrac{n(n+1)(2n+1)}{6}$ 由恒等式 $(k+1)^3-k^3=3k^2+3k+1$ 累加（裂项法）整理得；立方和由 $(k+1)^4-k^4=4k^3+6k^2+4k+1$ 累加整理得 $\\sum k^3=\\left[\\dfrac{n(n+1)}{2}\\right]^2$。")+
 p("<strong>并项推导：</strong>典型如 $S_n=1-2+3-4+\\cdots$。当 $n$ 为偶数时两两并项：$(1-2)+(3-4)+\\cdots+((n-1)-n)=-\\dfrac{n}{2}$；当 $n$ 为奇数时 $=-\\dfrac{n-1}{2}+n=\\dfrac{n+1}{2}$。故需按 $n$ 的奇偶分类讨论。"))+
 exa(p("<strong>例：</strong>$S_n=1^2+2^2+\\cdots+n^2$，取 $n=10$：$S_{10}=\\dfrac{10\\cdot11\\cdot21}{6}=385$。")))
},
{"id":"e4s3-5","name":"累加法与累乘法求通项","tags":["thm","der","exa"],"brief":"由相邻差累加、相邻比累乘求数列通项。",
"body":wrap(
 thm("累加法",p("若数列满足 $a_{n+1}-a_n=f(n)$，则 $a_n=a_1+\\sum_{k=1}^{n-1}f(k)$。"))+
 thm("累乘法",p("若数列满足 $\\dfrac{a_{n+1}}{a_n}=g(n)$（$a_n\\ne0$），则 $a_n=a_1\\prod_{k=1}^{n-1}g(k)$。"))+
 der(p("<strong>累加推导：</strong>由 $a_{n+1}-a_n=f(n)$，写出 $n-1$ 个等式：$a_2-a_1=f(1)$，$a_3-a_2=f(2)$，$\\ldots$，$a_n-a_{n-1}=f(n-1)$。左右分别相加，中间项全部抵消：$a_n-a_1=\\sum_{k=1}^{n-1}f(k)$，故 $a_n=a_1+\\sum_{k=1}^{n-1}f(k)$。")+
 p("<strong>累乘推导：</strong>由 $\\dfrac{a_{n+1}}{a_n}=g(n)$，写出 $\\dfrac{a_2}{a_1}=g(1),\\dfrac{a_3}{a_2}=g(2),\\ldots,\\dfrac{a_n}{a_{n-1}}=g(n-1)$。左右相乘，分子分母逐项约去：$\\dfrac{a_n}{a_1}=\\prod_{k=1}^{n-1}g(k)$，故 $a_n=a_1\\prod_{k=1}^{n-1}g(k)$。"))+
 exa(p("<strong>例：</strong>$a_1=1$，$a_{n+1}=a_n+2n$，则 $a_n=1+\\sum_{k=1}^{n-1}2k=1+2\\cdot\\dfrac{(n-1)n}{2}=n^2-n+1$。$n=1$ 时 $a_1=1$ 也满足，故 $a_n=n^2-n+1$。")))
}
]}
]

# ============ 第五章 平面几何 ============
ch5_sections = [
{"name":"5.1 平行线","color":"#be185d","desc":"平行公理、平行线的判定与性质、平行线间距离",
"items":[
{"id":"e5l-1","name":"平行线的判定与性质","tags":["def","thm","der","exa"],"brief":"平行公理、三线八角的判定与性质定理、平行线间距离。",
"body":wrap(
 defn("平行线",p("在同一平面内不相交的两条直线称<strong>平行线</strong>，记 $a\\parallel b$。两条直线被第三条直线所截，形成同位角、内错角、同旁内角。"))+
 thm("平行公理",p("过直线外一点，有且只有一条直线与已知直线平行。"))+
 thm("判定定理",p("两条直线被第三条直线所截：① 同位角相等；② 内错角相等；③ 同旁内角互补——满足其一，则两直线平行。"))+
 thm("性质定理",p("若两直线平行，则同位角相等、内错角相等、同旁内角互补。"))+
 der(p("<strong>判定推导（同位角）：</strong>设 $a,b$ 被 $c$ 所截，同位角 $\\angle1=\\angle2$。反设 $a,b$ 相交于 $P$，则 $\\angle1,\\angle2$ 与三角形外角关系矛盾（三角形外角等于不相邻两内角之和，必大于任一不相邻内角），故 $a\\parallel b$。")+
 p("<strong>性质推导（内错角）：</strong>设 $a\\parallel b$，内错角 $\\angle1$ 与 $\\angle2$。由平行线同位角相等，$\\angle1$ 等于其同位角 $\\angle3$；而 $\\angle3$ 与 $\\angle2$ 是对顶角相等，故 $\\angle1=\\angle2$。")+
 p("<strong>平行线间距离推导：</strong>两平行线间距离定义为一条直线上任一点到另一条直线的距离。取 $a$ 上两点 $A,B$ 向 $b$ 作垂线，垂足 $A',B'$，四边形 $AA'B'B$ 为矩形（$AA'\\parallel BB'$、$AB\\parallel A'B'$、$\\angle A'=90^\\circ$），故 $AA'=BB'$，即距离与取点无关，为定值。"))+
 exa(p("<strong>例：</strong>若内错角 $\\angle1=\\angle2=60^\\circ$，则两被截直线平行；反之两直线平行时同旁内角之和为 $180^\\circ$。")))
}
]},
{"name":"5.2 三角形","color":"#be185d","desc":"三角形内角和、正余弦定理、面积公式与四心",
"items":[
{"id":"e5s1-1","name":"三角形内角和与面积","tags":["def","thm","der"],"brief":"三角形内角和定理、面积公式的多种形式。",
"fig":"triangle","figCap":"三角形 ABC，底边 a 与高 h",
"body":wrap(
 defn("三角形",p("由三条线段首尾顺次连接组成的封闭图形称<strong>三角形</strong>。按角分锐角、直角、钝角三角形；按边分不等边、等腰、等边三角形。"))+
 thm("内角和定理",p("三角形三内角之和等于 $\\pi$（$180^\\circ$）。")+
 fml("A+B+C=\\pi"))+
 thm("面积公式",p("")+
 fml("S=\\dfrac{1}{2}ah=\\dfrac{1}{2}ab\\sin C=\\sqrt{p(p-a)(p-b)(p-c)}")+
 fml("p=\\dfrac{a+b+c}{2}\\text{（半周长）}"))+
 der(p("<strong>内角和推导：</strong>过顶点 $A$ 作 $BC$ 的平行线 $l$。由平行线内错角相等，$\\angle B=\\angle$（$B$ 侧内错角），$\\angle C=\\angle$（$C$ 侧内错角）。这三个角在 $A$ 处拼成平角 $\\pi$，故 $A+B+C=\\pi$。")+
 p("<strong>面积推导：</strong>① 底高法：以 $a$ 为底、$h$ 为高，三角形面积等于底乘高除以二 $S=\\dfrac{1}{2}ah$（由矩形面积一半，沿对角线分割）。② 夹角法：$h=b\\sin C$（$b$ 边作斜边、$C$ 为邻角），代入 $S=\\dfrac{1}{2}a\\cdot b\\sin C$。")))
},
{"id":"e5s1-2","name":"正弦定理与余弦定理","tags":["def","thm","der","exa"],"brief":"正弦定理、余弦定理及推导，解三角形应用。",
"body":wrap(
 thm("正弦定理",p("")+
 fml("\\dfrac{a}{\\sin A}=\\dfrac{b}{\\sin B}=\\dfrac{c}{\\sin C}=2R"))+
 thm("余弦定理",p("")+
 fml("c^2=a^2+b^2-2ab\\cos C,\\quad a^2=b^2+c^2-2bc\\cos A"))+
 der(p("<strong>正弦定理推导：</strong>设 $\\triangle ABC$ 外接圆半径 $R$，圆心 $O$。由圆周角定理，$\\angle ACB$ 所对弦 $AB=c$，$c=2R\\sin\\angle ACB$（直径所对圆周角的推论：直径 $2R$ 对应的圆周角为直角，一般情形由直径构造直角三角形得 $c=2R\\sin C$）。故 $\\dfrac{c}{\\sin C}=2R$，同理 $\\dfrac{a}{\\sin A}=\\dfrac{b}{\\sin B}=2R$。")+
 p("<strong>余弦定理推导：</strong>以 $A$ 为原点，$AB$ 方向为 $x$ 轴正向建立直角坐标系。$B(c,0)$，$C(b\\cos A,b\\sin A)$。则 $|BC|^2=(b\\cos A-c)^2+(b\\sin A)^2=b^2\\cos^2 A-2bc\\cos A+c^2+b^2\\sin^2 A=b^2+c^2-2bc\\cos A$，即 $a^2=b^2+c^2-2bc\\cos A$。")+
 p("<strong>勾股定理推论：</strong>当 $C=\\dfrac{\\pi}{2}$ 时 $\\cos C=0$，余弦定理退化为 $c^2=a^2+b^2$ 即勾股定理。"))+
 exa(p("<strong>例：</strong>$\\triangle ABC$ 中 $a=3,b=4,C=60^\\circ$，求 $c$。$c^2=9+16-2\\cdot3\\cdot4\\cdot\\dfrac{1}{2}=25-12=13$，$c=\\sqrt{13}$。")))
},
{"id":"e5s1-3","name":"海伦公式与中位线定理","tags":["thm","der","exa"],"brief":"海伦公式推导与三角形中位线性质。",
"body":wrap(
 thm("海伦公式",p("")+
 fml("S=\\sqrt{p(p-a)(p-b)(p-c)},\\quad p=\\dfrac{a+b+c}{2}"))+
 thm("中位线定理",p("三角形两边中点连线平行于第三边且等于第三边一半。"))+
 der(p("<strong>海伦公式推导：</strong>由 $S=\\dfrac{1}{2}ab\\sin C$ 与余弦定理 $\\cos C=\\dfrac{a^2+b^2-c^2}{2ab}$，则 $\\sin^2 C=1-\\cos^2 C=1-\\dfrac{(a^2+b^2-c^2)^2}{4a^2b^2}=\\dfrac{4a^2b^2-(a^2+b^2-c^2)^2}{4a^2b^2}$。分子用平方差分解：$4a^2b^2-(a^2+b^2-c^2)^2=[2ab+(a^2+b^2-c^2)][2ab-(a^2+b^2-c^2)]=[(a+b)^2-c^2][c^2-(a-b)^2]=(a+b+c)(a+b-c)(c+a-b)(c-a+b)$。代入 $p$：$=2p\\cdot 2(p-c)\\cdot 2(p-b)\\cdot 2(p-a)=16p(p-a)(p-b)(p-c)$。故 $S=\\dfrac{1}{2}ab\\cdot\\dfrac{4\\sqrt{p(p-a)(p-b)(p-c)}}{2ab}=\\sqrt{p(p-a)(p-b)(p-c)}$。")+
 p("<strong>中位线推导：</strong>设 $D,E$ 分别为 $AB,AC$ 中点。由相似三角形，$\\triangle ADE\\sim\\triangle ABC$，相似比 $\\dfrac{AD}{AB}=\\dfrac{1}{2}$，故 $DE=\\dfrac{1}{2}BC$ 且 $DE\\parallel BC$。"))+
 exa(p("<strong>例：</strong>三边 $a=3,b=4,c=5$，$p=6$，$S=\\sqrt{6\\cdot3\\cdot2\\cdot1}=\\sqrt{36}=6$。")))
},
{"id":"e5s1-4","name":"三角形的四心","tags":["def","thm","der","exa"],"brief":"内心、外心、重心、垂心的定义、性质与推导。",
"body":wrap(
 defn("重心",p("三条中线的交点称<strong>重心</strong> $G$，重心到顶点的距离是到对边中点距离的 2 倍。"))+
 defn("内心",p("三条角平分线的交点称<strong>内心</strong> $I$，是内切圆圆心，到三边距离相等（等于内切圆半径 $r$）。"))+
 defn("外心",p("三边中垂线的交点称<strong>外心</strong> $O$，是外接圆圆心，到三顶点距离相等（等于外接圆半径 $R$）。"))+
 defn("垂心",p("三条高所在直线的交点称<strong>垂心</strong> $H$。"))+
 der(p("<strong>内心推导（角平分线共点）：</strong>设 $\\angle B,\\angle C$ 的平分线交于 $I$。因 $I$ 在 $\\angle B$ 平分线上，到 $BA,BC$ 距离相等；又在 $\\angle C$ 平分线上，到 $CB,CA$ 距离相等。于是 $I$ 到三边距离全相等，特别地到 $AB,AC$ 距离也相等，故 $I$ 也在 $\\angle A$ 平分线上——三平分线共点，且 $I$ 到三边等距，为内切圆圆心。")+
 p("<strong>外心推导（中垂线共点）：</strong>$AB,BC$ 的中垂线交于 $O$。由中垂线性质 $OA=OB$（$O$ 在 $AB$ 中垂线上）、$OB=OC$，故 $OA=OC$，即 $O$ 也在 $AC$ 中垂线上——三中垂线共点，且到三顶点等距，为外接圆圆心。")+
 p("<strong>重心推导（分中线为 2:1）：</strong>设中线 $AD$ 与 $BE$ 交于 $G$（$D,E$ 为边中点）。取 $AG$ 中点 $M$、$BG$ 中点 $N$。在 $\\triangle ABG$ 中 $MN\\parallel AB$ 且 $MN=\\dfrac12 AB$（中位线）；又在 $\\triangle ABC$ 中 $DE\\parallel AB$ 且 $DE=\\dfrac12 AB$。故 $DE\\parallel MN$ 且 $DE=MN$，四边形 $DGMN$ 为平行四边形，得 $DG=GM=MA$，即 $AG=2GD$，重心分中线为 $2:1$。"))+
 exa(p("<strong>例：</strong>直角三角形的外心在斜边中点；等边三角形四心重合。内切圆半径 $r=\\dfrac{S}{p}$（$p$ 为半周长），外接圆半径 $R=\\dfrac{abc}{4S}$。")))
}
]},
{"name":"5.3 平行四边形","color":"#db2777","desc":"平行四边形的性质、判定与面积",
"items":[
{"id":"e5s2-1","name":"平行四边形","tags":["def","thm","der","exa"],"brief":"平行四边形性质、判定定理与面积公式。",
"body":wrap(
 defn("平行四边形",p("两组对边分别平行的四边形称为<strong>平行四边形</strong>。"))+
 thm("性质",p("①对边平行且相等；②对角相等；③邻角互补；④对角线互相平分；⑤是中心对称图形。"))+
 thm("判定",p("①两组对边分别平行；②两组对边分别相等；③一组对边平行且相等；④对角线互相平分。"))+
 der(p("<strong>面积推导：</strong>以 $a$ 为底、$h$ 为高，将平行四边形沿高切割补成矩形，面积 $S=ah$。也可用邻边 $a,b$ 和夹角 $\\theta$：$h=b\\sin\\theta$，故 $S=ab\\sin\\theta$。")+
 fml("S=ah=ab\\sin\\theta"))+
 exa(p("例如菱形和矩形都是特殊的平行四边形，继承平行四边形的所有性质。")))
}]},
{"name":"5.4 矩形","color":"#be185d","desc":"矩形的性质、判定与面积",
"items":[
{"id":"e5s3-1","name":"矩形","tags":["def","thm","der","exa"],"brief":"矩形性质、判定定理与面积公式。",
"body":wrap(
 defn("矩形",p("有一个角是直角的平行四边形称为<strong>矩形</strong>。"))+
 thm("性质",p("①具有平行四边形的一切性质；②四个角都是直角；③对角线相等；④既是中心对称又是轴对称图形。"))+
 thm("判定",p("①有一个角是直角的平行四边形；②对角线相等的平行四边形；③有三个角是直角的四边形。"))+
 der(p("<strong>对角线相等推导：</strong>设矩形 $ABCD$，$\\angle B=90^\\circ$。在 $\\triangle ABC$ 和 $\\triangle DCB$ 中，$AB=DC$（对边），$BC$ 公共，$\\angle ABC=\\angle DCB=90^\\circ$，由 SAS 得 $\\triangle ABC\\cong\\triangle DCB$，故 $AC=DB$。")+
 fml("S=ab","长乘宽")))
}]},
{"name":"5.5 菱形","color":"#be185d","desc":"菱形的性质、判定与面积",
"items":[
{"id":"e5s4-1","name":"菱形","tags":["def","thm","der","exa"],"brief":"菱形性质、判定定理与面积公式。",
"body":wrap(
 defn("菱形",p("一组邻边相等的平行四边形称为<strong>菱形</strong>。"))+
 thm("性质",p("①具有平行四边形的一切性质；②四条边都相等；③对角线互相垂直平分；④每条对角线平分一组对角；⑤既是中心对称又是轴对称图形。"))+
 thm("判定",p("①一组邻边相等的平行四边形；②对角线互相垂直的平行四边形；③四边相等的四边形。"))+
 der(p("<strong>面积推导：</strong>菱形对角线 $d_1,d_2$ 互相垂直，将菱形分为四个全等的直角三角形，每个三角形面积为 $\\frac{1}{2}\\cdot\\frac{d_1}{2}\\cdot\\frac{d_2}{2}=\\frac{d_1 d_2}{8}$，四个共 $\\frac{d_1 d_2}{2}$。")+
 fml("S=\\dfrac{1}{2}d_1 d_2","对角线乘积一半")))
}]},
{"name":"5.6 正方形","color":"#be185d","desc":"正方形的性质、判定与面积",
"items":[
{"id":"e5s5-1","name":"正方形","tags":["def","thm","der","exa"],"brief":"正方形性质、判定定理与面积公式。",
"body":wrap(
 defn("正方形",p("既是矩形又是菱形的平行四边形称为<strong>正方形</strong>，即有一组邻边相等且有一个直角的平行四边形。"))+
 thm("性质",p("①具有矩形和菱形的一切性质；②四边相等、四角都是直角；③对角线相等且互相垂直平分。"))+
 thm("判定",p("①一组邻边相等的矩形；②有一个直角的菱形；③对角线相等且互相垂直平分的四边形。"))+
 der(p("<strong>面积推导：</strong>正方形边长 $a$，面积 $S=a^2$。也可用对角线 $d$：由勾股定理 $d=a\\sqrt{2}$，故 $a=\\frac{d}{\\sqrt{2}}$，$S=a^2=\\frac{d^2}{2}$。")+
 fml("S=a^2=\\dfrac{d^2}{2}")))
}]},
{"name":"5.7 梯形","color":"#be185d","desc":"梯形的性质、等腰梯形与面积",
"items":[
{"id":"e5s6-1","name":"梯形与中位线定理","tags":["def","thm","der","exa"],"brief":"梯形定义、等腰梯形性质、中位线定理与面积公式。",
"body":wrap(
 defn("梯形",p("一组对边平行而另一组对边不平行的四边形称为<strong>梯形</strong>。平行的两边称为底（上底 $a$、下底 $b$），不平行的两边称为腰，两底距离为高 $h$。"))+
 defn("等腰梯形",p("两腰相等的梯形称为<strong>等腰梯形</strong>。性质：两腰相等、同一底上的两角相等、对角线相等、轴对称图形。"))+
 thm("中位线定理",p("梯形的中位线（两腰中点连线）平行于两底且等于两底之和的一半。"))+
 der(p("<strong>中位线推导：</strong>设梯形 $ABCD$，$AD\\parallel BC$，$M,N$ 分别为 $AB,CD$ 中点。连接 $MN$ 并延长至 $P$ 使 $NP=MN$，可证 $\\triangle MNC\\cong\\triangle PND$（SAS），故 $MC=PD$，$\\angle MCN=\\angle PDN$，得 $MC\\parallel PD$。由于 $A,M,B$ 共线且 $MC\\parallel PD\\parallel AD$，故 $MN\\parallel AD\\parallel BC$。再由 $MN=\\frac{1}{2}(AD+BC)$ 即证。")+
 fml("m=\\dfrac{a+b}{2}","中位线"))+
 fml("S=\\dfrac{(a+b)h}{2}","梯形面积"))
}]},
{"name":"5.8 圆","color":"#9d174d","desc":"圆的定义、垂径定理、圆心角与圆周角、切线",
"items":[
{"id":"e5s7-1","name":"圆的定义与垂径定理","tags":["def","thm","der","exa"],"brief":"圆的定义、弧弦圆心概念、垂径定理及推论。",
"body":wrap(
 defn("圆",p("平面上到定点（圆心）距离等于定长（半径）的所有点组成的集合。记 $\\odot O$，半径 $r$。"))+
 defn("弧、弦、圆心角",p("<strong>弧</strong>：圆上两点间的部分；<strong>弦</strong>：连接圆上两点的线段；<strong>直径</strong>是最长的弦；<strong>圆心角</strong>：顶点在圆心的角。"))+
 thm("垂径定理",p("垂直于弦的直径平分这条弦，并且平分弦所对的两条弧。"))+
 der(p("<strong>垂径定理推导：</strong>设圆 $O$ 半径 $r$，弦 $AB$，直径 $CD\\perp AB$ 于 $E$。连接 $OA,OB$，则 $OA=OB=r$（半径相等）。在 $\\triangle OAB$ 中 $OE\\perp AB$，即 $OE$ 是等腰三角形的高，也是中线和中线。故 $AE=EB$（平分弦），且 $\\angle AOC=\\angle BOC$（平分弧），同理平分劣弧。"))+
 note(p("推论：平分弦（非直径）的直径垂直于弦且平分弦所对弧；平分弧的直径垂直平分弦。")))
},
{"id":"e5s8-1","name":"圆心角定理与圆周角定理","tags":["def","thm","der","exa"],"brief":"圆心角等于同弧所对圆周角的两倍。",
"body":wrap(
 defn("圆周角",p("顶点在圆上，两边都是圆的弦的角称为<strong>圆周角</strong>。"))+
 thm("圆心角定理",p("圆心角的度数等于它所对弧的度数。"))+
 thm("圆周角定理",p("圆周角的度数等于它所对弧的度数的一半，即同弧所对的圆周角等于圆心角的一半。"))+
 der(p("<strong>圆周角定理推导：</strong>设圆 $O$，弧 $AB$ 所对圆心角 $\\angle AOB=\\alpha$，圆周角 $\\angle ACB$。分三种情况：①圆心 $O$ 在 $\\angle ACB$ 内部：连接 $CO$ 延长交圆于 $D$，则 $\\angle ACD=\\angle AOD/2$（等腰 $\\triangle AOD$），$\\angle BCD=\\angle BOD/2$，相加 $\\angle ACB=\\angle AOB/2$。②圆心在角边上：$\\angle ACB=\\angle AOB/2$（外角定理）。③圆心在角外：类似用差证明。三种情况均得 $\\angle ACB=\\frac{1}{2}\\angle AOB$。")+
 fml("\\angle ACB=\\dfrac{1}{2}\\angle AOB"))+
 note(p("推论：①同弧或等弧所对圆周角相等；②直径所对圆周角为直角；③圆内接四边形对角互补。")))
},
{"id":"e5s9-1","name":"切线性质与圆幂定理","tags":["def","thm","der","exa"],"brief":"切线判定与性质、切线长定理、相交弦与切割线定理。",
"body":wrap(
 defn("切线",p("与圆只有一个公共点的直线称为圆的<strong>切线</strong>，公共点称为切点。"))+
 thm("切线判定定理",p("经过半径的外端且垂直于这条半径的直线是圆的切线。"))+
 thm("切线性质定理",p("圆的切线垂直于过切点的半径。"))+
 thm("切线长定理",p("从圆外一点引圆的两条切线，它们的切线长相等，且这点与圆心的连线平分两切线所夹角。"))+
 thm("相交弦定理",p("圆内两弦 $AB,CD$ 交于 $P$，则 $PA\\cdot PB=PC\\cdot PD$。"))+
 thm("切割线定理",p("从圆外一点 $P$ 引切线 $PT$（$T$ 为切点）和割线 $PAB$，则 $PT^2=PA\\cdot PB$。"))+
 der(p("<strong>切割线定理推导：</strong>连接 $TA,TB$。因 $\\angle PTA$ 为弦切角，由弦切角定理 $\\angle PTA=\\angle TBA$（所对弧 $TA$ 的圆周角）。又 $\\angle P$ 公共，故 $\\triangle PTA\\sim\\triangle PBT$（AA），得 $\\frac{PT}{PB}=\\frac{PA}{PT}$，即 $PT^2=PA\\cdot PB$。")+
 fml("PT^2=PA\\cdot PB","切割线定理"))+
 der(p("<strong>切线性质推导：</strong>设切线 $l$ 切圆 $O$ 于 $T$。若 $l$ 不垂直于 $OT$，则 $l$ 上存在点使到 $O$ 距离小于 $r$（垂线段最短），即 $l$ 与圆有两个交点，与切线定义矛盾。故 $l\\perp OT$。")))
}
]},
{"name":"5.9 对称、旋转与平移","color":"#9d174d","desc":"轴对称、中心对称、旋转与平移",
"items":[
{"id":"e5sym-1","name":"图形的对称、旋转与平移","tags":["def","thm","der","exa"],"brief":"轴对称、中心对称、平移与旋转的定义与性质。",
"body":wrap(
 defn("轴对称",p("把一个图形沿一条直线折叠，若它能与另一个图形重合，则两图形关于这条直线<strong>轴对称</strong>，这条直线称对称轴。"))+
 defn("中心对称",p("把一个图形绕某一点旋转 $180^\\circ$，若能与另一个图形重合，则两图形关于该点<strong>中心对称</strong>，该点称对称中心。"))+
 defn("平移",p("把图形上所有点沿同一方向移动相同距离，称<strong>平移</strong>。平移不改变图形的形状和大小。"))+
 defn("旋转",p("把图形绕一个定点按一定方向转动一个角度，称<strong>旋转</strong>，定点称旋转中心，转动的角称旋转角。"))+
 thm("性质",p("① 平移：对应线段平行且相等、对应角相等；② 旋转：对应点到旋转中心距离相等、对应点与中心连线夹角等于旋转角；③ 轴对称：对应点连线被对称轴垂直平分；④ 中心对称：对应点连线被对称中心平分。"))+
 der(p("<strong>轴对称性质推导：</strong>设点 $A$ 与 $A'$ 关于直线 $l$ 对称，$AA'$ 交 $l$ 于 $O$。折叠后两点重合，$l$ 上任一点到 $A,A'$ 距离相等，特别地 $OA=OA'$；又 $AA'\\perp l$（否则折叠后 $A$ 落到 $A'$ 以外的点），故 $l$ 垂直平分 $AA'$。")+
 p("<strong>旋转性质推导：</strong>点 $P$ 绕中心 $O$ 旋转角 $\\theta$ 到 $P'$。由定义 $OP=OP'$（到中心距离不变）、$\\angle POP'=\\theta$，故 $\\triangle OPP'$ 是以 $O$ 为顶点的等腰三角形，旋转保持图形形状与大小不变。"))+
 exa(p("<strong>例：</strong>正方形既是轴对称图形（4 条对称轴）又是中心对称图形（对称中心为对角线交点）；正三角形是轴对称图形但不是中心对称图形。")))
}
]},
{"name":"5.10 平面图形面积与周长","color":"#9d174d","desc":"常见平面图形面积周长公式汇总",
"items":[
{"id":"e5s10-1","name":"常见平面图形面积周长公式表","tags":["def","der","app","note"],"brief":"三角形、四边形、圆、扇形、弓形面积周长公式汇总。",
"body":wrap(
 defn("公式汇总",p("以下为常见平面图形的面积与周长公式汇总表："))+
 p("<strong>三角形：</strong>$S=\\frac{1}{2}ah=\\frac{1}{2}ab\\sin C=\\sqrt{s(s-a)(s-b)(s-c)}=rs$（$s$ 为半周长，$r$ 为内切圆半径），$C=a+b+c$。")+
 p("<strong>平行四边形：</strong>$S=ah=ab\\sin\\theta$，$C=2(a+b)$。")+
 p("<strong>矩形：</strong>$S=ab$，$C=2(a+b)$。")+
 p("<strong>菱形：</strong>$S=\\frac{1}{2}d_1 d_2=a^2\\sin\\theta$，$C=4a$。")+
 p("<strong>正方形：</strong>$S=a^2$，$C=4a$。")+
 p("<strong>梯形：</strong>$S=\\frac{(a+b)h}{2}=mh$（$m$ 为中位线），$C=a+b+c+d$。")+
 p("<strong>圆：</strong>$S=\\pi r^2$，$C=2\\pi r$。")+
 p("<strong>扇形：</strong>$S=\\frac{1}{2}lr=\\frac{1}{2}r^2\\alpha$（$l$ 为弧长，$\\alpha$ 为圆心角弧度），$l=r\\alpha=\\frac{n\\pi r}{180}$。")+
 p("<strong>弓形：</strong>$S=\\frac{1}{2}r^2(\\alpha-\\sin\\alpha)$（$\\alpha$ 为圆心角弧度）。")+
 der(p("<strong>扇形与弓形面积推导：</strong>整圆面积 $\\pi r^2$ 对应圆心角 $2\\pi$（弧度）。圆心角 $\\alpha$ 的扇形按比例占 $\\frac{\\alpha}{2\\pi}$，故 $S_{\\text{扇}}=\\frac{\\alpha}{2\\pi}\\cdot\\pi r^2=\\frac{1}{2}r^2\\alpha$。弧长 $l=r\\alpha$，代入得 $S=\\frac{1}{2}lr$。弓形等于扇形减去圆心与弦端点连线构成的三角形，三角形面积 $\\frac{1}{2}r^2\\sin\\alpha$，故 $S_{\\text{弓}}=\\frac{1}{2}r^2(\\alpha-\\sin\\alpha)$。")))
}]}
]

# ============ 第六章 立体几何 ============
ch6_sections = [
{"name":"6.1 多面体","color":"#7c3aed","desc":"棱柱、棱锥、棱台与欧拉公式",
"items":[
{"id":"e6s1-1","name":"棱柱与棱锥","tags":["def","thm","der","exa"],"brief":"棱柱棱锥定义、侧面积与体积公式。",
"fig":"cube","figCap":"正方体是特殊的棱柱，体积 $V=a^3$",
"body":wrap(
 defn("棱柱",p("两底面是全等多边形且对应边平行的多面体称<strong>棱柱</strong>。侧棱平行的称平行六面体；底面为正多边形、侧棱垂直底面的称正棱柱。"))+
 defn("棱锥",p("一个面是多边形、其余各面是有公共顶点的三角形的多面体称<strong>棱锥</strong>。底面为正多边形、顶点在底面射影为底面中心的称正棱锥。"))+
 thm("体积与侧面积",p("")+
 fml("V_{\\text{柱}}=Sh,\\quad V_{\\text{锥}}=\\dfrac{1}{3}Sh")+
 fml("S_{\\text{正棱柱侧}}=n a h,\\quad S_{\\text{正棱锥侧}}=\\dfrac{1}{2}n a l"))+
 der(p("<strong>棱柱体积推导：</strong>棱柱可由平移底面扫过形成，体积 = 底面积 $\\times$ 高 $=Sh$。")+
 p("<strong>棱锥体积推导（祖暅原理）：</strong>同底等高的棱锥与圆锥体积相等。取三棱锥，可用「三个三棱锥拼成一个三棱柱」（沿面对角线分割），故 $V_{\\text{锥}}=\\dfrac{1}{3}V_{\\text{柱}}=\\dfrac{1}{3}Sh$。")+
 p("<strong>侧面积推导：</strong>正棱柱侧面展开为矩形，长 $na$（$n$ 边形周长）、宽 $h$（侧棱长），故 $S_{侧}=nah$。正棱锥侧面展开为扇形，由 $n$ 个全等三角形组成，每个面积 $\\dfrac{1}{2}al$（$a$ 底边、$l$ 斜高），故 $S_{侧}=\\dfrac{1}{2}nal$。"))+
 exa(p("<strong>例：</strong>正方体棱长 $a$，$V=a^3$，$S_{全}=6a^2$。")))
},
{"id":"e6s1-2","name":"棱台与体积比","tags":["def","thm","der"],"brief":"棱台定义、体积公式与截面积比。",
"fig":"pyramid","figCap":"棱台由棱锥截去顶部得到，体积 $V=\\dfrac{h}{3}(S_上+\\sqrt{S_上 S_下}+S_下)$",
"body":wrap(
 defn("棱台",p("棱锥被平行于底面的平面截去顶部后剩余部分称<strong>棱台</strong>。两底面是相似多边形。"))+
 thm("棱台体积",p("")+
 fml("V_{\\text{台}}=\\dfrac{1}{3}h(S_{上}+\\sqrt{S_{上}S_{下}}+S_{下})"))+
 der(p("<strong>棱台体积推导：</strong>棱台可视为大棱锥减去小棱锥。设大棱锥高 $H$、底面积 $S_{下}$，小棱锥高 $h'$、底面积 $S_{上}$，棱台高 $h=H-h'$。由相似，$\\dfrac{S_{上}}{S_{下}}=\\left(\\dfrac{h'}{H}\\right)^2$，故 $h'=H\\sqrt{\\dfrac{S_{上}}{S_{下}}}$。$V_{台}=\\dfrac{1}{3}S_{下}H-\\dfrac{1}{3}S_{上}h'=\\dfrac{1}{3}\\left[S_{下}H-S_{上}H\\sqrt{\\dfrac{S_{上}}{S_{下}}}\\right]=\\dfrac{H}{3}\\left[S_{下}-\\dfrac{S_{上}^{3/2}}{S_{下}^{1/2}}\\right]$。代入 $H=h+h'=h+H\\sqrt{S_{上}/S_{下}}$，解 $H=\\dfrac{h}{1-\\sqrt{S_{上}/S_{下}}}$，整理得 $V=\\dfrac{h}{3}(S_{上}+\\sqrt{S_{上}S_{下}}+S_{下})$。")+
 p("<strong>截面积比推导：</strong>平行底面的截面面积与到顶点距离平方成正比。设截面到顶点距离 $x$，底面到顶点距离 $H$，则 $\\dfrac{S_{截}}{S_{底}}=\\left(\\dfrac{x}{H}\\right)^2$。")))
},
{"id":"e6s1-3","name":"欧拉公式与多面体","tags":["thm","der","exa"],"brief":"简单多面体顶点数-棱数-面数关系。",
"body":wrap(
 thm("欧拉公式",p("简单多面体顶点数 $V$、面数 $F$、棱数 $E$ 满足：")+
 fml("V-E+F=2"))+
 der(p("<strong>欧拉公式推导（去面法）：</strong>对简单多面体，逐步去掉一面并展开为平面图。每去掉一面，$F$ 减 1；展开后保持顶点棱数。对平面图作三角剖分：每加一条对角线，$E$ 与 $F$ 同增 1，$V-E+F$ 不变。化简为全部三角形后，逐步去掉边界三角形：去掉一个三角形若去掉一边则 $E,F$ 各减 1；若去掉两边则 $E$ 减 2、$F$ 减 1、$V$ 减 1；若去掉三边则三角缩小为一点，$V,E,F$ 各减适当值。每步 $V-E+F$ 不变。最终剩一个三角形：$V=3,E=3,F=1$（含外），$V-E+F=3-3+1=1$，但开始去掉一面已使 $F$ 含外，故原多面体 $V-E+F=1+1=2$。")+
 p("<strong>正多面体推导：</strong>由欧拉公式与每面 $n$ 边、每顶点 $m$ 棱，$nF=2E$、$mV=2E$。代入 $V-E+F=2$ 得 $\\dfrac{2E}{m}-E+\\dfrac{2E}{n}=2$，即 $\\dfrac{1}{m}+\\dfrac{1}{n}=\\dfrac{1}{2}+\\dfrac{1}{E}>\\dfrac{1}{2}$。枚举正整数解得 $(m,n)=(3,3),(3,4),(4,3),(3,5),(5,3)$ 共五种正多面体。"))+
 exa(p("<strong>例：</strong>正方体 $V=8,E=12,F=6$，$8-12+6=2$。")))
}
]},
{"name":"6.2 旋转体","color":"#6d28d9","desc":"圆柱、圆锥、圆台、球",
"items":[
{"id":"e6s2-1","name":"圆柱、圆锥与圆台","tags":["def","thm","der","exa"],"brief":"旋转体定义、体积与侧面积公式。",
"fig":"cone","figCap":"圆锥 $V=\\dfrac{1}{3}\\pi r^2 h$，由直角三角形旋转得到",
"body":wrap(
 defn("圆柱圆锥",p("矩形绕一边旋转得<strong>圆柱</strong>；直角三角形绕一直角边旋转得<strong>圆锥</strong>；圆锥被平行底面截去顶部得<strong>圆台</strong>。"))+
 thm("体积与侧面积",p("")+
 fml("V_{\\text{圆柱}}=\\pi r^2 h,\\quad S_{\\text{侧}}=2\\pi r h")+
 fml("V_{\\text{圆锥}}=\\dfrac{1}{3}\\pi r^2 h,\\quad S_{\\text{侧}}=\\pi r l\\ (l=\\sqrt{r^2+h^2})"))+
 der(p("<strong>圆柱体积推导：</strong>圆柱由圆盘沿高堆叠，体积 = 底面积 $\\pi r^2\\times$ 高 $h$。侧面积：展开为矩形，长 $2\\pi r$（底周长）、宽 $h$，故 $S_{侧}=2\\pi r h$。")+
 p("<strong>圆锥体积推导（祖暅原理）：</strong>同底等高的圆锥与三棱锥体积相等（用祖暅原理，二者在每一等高处截面积按同一比例对应），而棱锥体积为 $\\dfrac{1}{3}Sh$，故 $V_{\\text{圆锥}}=\\dfrac{1}{3}\\pi r^2 h$。")+
 p("<strong>圆锥侧面积推导：</strong>展开为扇形，半径 $l$（母线），弧长 $2\\pi r$（底周长）。扇形面积 $=\\dfrac{1}{2}\\cdot l\\cdot 2\\pi r=\\pi r l$。"))+
 exa(p("<strong>例：</strong>圆锥 $r=3,h=4$，$l=5$，$V=\\dfrac{1}{3}\\pi\\cdot9\\cdot4=12\\pi$，$S_{侧}=\\pi\\cdot3\\cdot5=15\\pi$。")))
},
{"id":"e6s2-2","name":"球与球面","tags":["def","thm","der"],"brief":"球的表面积、体积公式推导。",
"fig":"sphere","figCap":"球 $S=4\\pi R^2, V=\\dfrac{4}{3}\\pi R^3$",
"body":wrap(
 defn("球",p("半圆绕其直径旋转一周形成的旋转面称球面，球面所围立体称<strong>球</strong>。球心到球面任一点距离为半径 $R$。"))+
 thm("球的公式",p("")+
 fml("S_{\\text{球}}=4\\pi R^2,\\quad V_{\\text{球}}=\\dfrac{4}{3}\\pi R^3"))+
 der(p("<strong>表面积推导（祖暅原理）：</strong>将半径 $R$ 的球置于底面半径 $R$、高 $2R$ 的圆柱内。任取水平截面：球截面为小圆，半径 $\\sqrt{R^2-x^2}$（$x$ 为到球心距离），面积 $\\pi(R^2-x^2)$；圆柱去圆锥（同底等高）截面为环形，面积 $\\pi R^2-\\pi x^2=\\pi(R^2-x^2)$。两者截面面积相等，由祖暅原理体积相等。圆柱体积 $\\pi R^2\\cdot 2R=2\\pi R^3$，圆锥体积 $\\dfrac{1}{3}\\pi R^2\\cdot 2R=\\dfrac{2}{3}\\pi R^3$，球体积 $=2\\pi R^3-\\dfrac{2}{3}\\pi R^3=\\dfrac{4}{3}\\pi R^3$。")+
 p("<strong>表面积结论（阿基米德）：</strong>阿基米德证明：球面面积等于其<strong>大圆面积的 4 倍</strong>，即 $S_{\\text{球}}=4\\pi R^2$。直观上，球面可视为外切圆柱侧面（面积 $2\\pi R\\cdot 2R=4\\pi R^2$）的「投影」，两者面积相等。")))
}
]},
{"name":"6.3 空间位置关系","color":"#5b21b6","desc":"线面平行垂直、二面角与空间距离",
"items":[
{"id":"e6s3-1","name":"线面平行与垂直","tags":["def","thm","der"],"brief":"线面平行垂直的判定与性质定理。",
"body":wrap(
 defn("线面位置关系",p("直线与平面位置关系：在面内、相交、平行。两平面：平行、相交。"))+
 thm("线面平行判定",p("若平面外一条直线与平面内一条直线平行，则该直线与平面平行。"))+
 thm("线面垂直判定",p("若一条直线与平面内两条相交直线都垂直，则该直线与平面垂直。"))+
 der(p("<strong>线面平行推导：</strong>设 $l$ 在 $\\alpha$ 外，$m\\subset\\alpha$ 且 $l\\parallel m$。反证若 $l$ 与 $\\alpha$ 相交于 $P$，则 $l,m$ 确定平面 $\\beta$，$\\alpha\\cap\\beta=m$，$P\\in\\beta\\cap\\alpha$，故 $P\\in m$。但 $l\\parallel m$ 无公共点，矛盾。故 $l\\parallel\\alpha$。")+
 p("<strong>线面垂直推导：</strong>设 $l\\perp a, l\\perp b$（$a,b\\subset\\alpha$ 相交于 $O$）。证 $l\\perp\\alpha$ 即证 $l$ 垂直 $\\alpha$ 内任一直线 $c$。在 $l$ 上取 $P,Q$ 关于 $O$ 对称（$OP=OQ$），$a,b$ 上取 $A,B$ 使 $OA=OB$，则 $PA=PB,QA=QB$（线段垂直平分线性质）。由对称性 $\\triangle PAB$ 与 $\\triangle QAB$ 关于 $l$ 对称，可证 $l\\perp c$。")))
},
{"id":"e6s3-2","name":"二面角与距离","tags":["def","thm","der","exa"],"brief":"二面角定义、平面角求法与点到面距离。",
"body":wrap(
 defn("二面角",p("两平面相交形成四个二面角。二面角的平面角：在棱上取点，两平面内作棱的垂线，两垂线夹角即平面角。"))+
 thm("二面角余弦",p("")+
 fml("\\cos\\varphi=\\pm\\dfrac{\\vec{n_1}\\cdot\\vec{n_2}}{|\\vec{n_1}||\\vec{n_2}|}"))+
 thm("点面距离",p("")+
 fml("d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}"))+
 der(p("<strong>二面角推导：</strong>两平面 $\\alpha_1,\\alpha_2$ 法向量 $\\vec{n_1},\\vec{n_2}$，二面角的平面角与法向量夹角相等或互补。由 $\\vec{n_1}\\cdot\\vec{n_2}=|\\vec{n_1}||\\vec{n_2}|\\cos\\theta$，得 $\\cos\\varphi=\\pm\\dfrac{\\vec{n_1}\\cdot\\vec{n_2}}{|\\vec{n_1}||\\vec{n_2}|}$（符号由二面角为锐角或钝角确定）。")+
 p("<strong>点面距离推导：</strong>平面 $Ax+By+Cz+D=0$ 法向量 $\\vec{n}=(A,B,C)$。点 $P_0(x_0,y_0,z_0)$ 到平面距离 = $P_0$ 沿法向量方向到平面的有向距离绝对值。设 $P$ 为垂足，$\\vec{P_0P}=t\\vec{n}/|\\vec{n}|$ 代入平面方程 $A(x_0+tA/|n|)+\\cdots+D=0$ 解 $t$，得 $d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}$。"))+
 exa(p("<strong>例：</strong>原点到平面 $2x+3y+6z-21=0$ 距离 $d=\\dfrac{21}{\\sqrt{4+9+36}}=\\dfrac{21}{7}=3$。")))
}
]},
{"name":"6.4 立体几何公式汇总","color":"#4c1d95","desc":"柱、锥、台、球体积与表面积汇总表",
"items":[
{"id":"e6s4-1","name":"常见立体图形体积与表面积汇总表","tags":["def","der","app","note"],"brief":"柱、锥、台、球及正多面体的侧面积、表面积与体积公式汇总。",
"body":wrap(
 defn("公式汇总",p("以下为常见立体图形的侧面积、表面积与体积公式汇总（$S$ 为底面积、$h$ 为高、$r,R$ 为半径、$l$ 为母线/斜高、$C$ 为底面周长）："))+
 p("<strong>棱柱：</strong>$V=Sh$，$S_{侧}=Ch$，$S_{全}=2S+Ch$。")+
 p("<strong>圆柱：</strong>$V=\\pi r^2 h$，$S_{侧}=2\\pi rh$，$S_{全}=2\\pi r^2+2\\pi rh$。")+
 p("<strong>棱锥：</strong>$V=\\dfrac{1}{3}Sh$，$S_{侧}=\\dfrac{1}{2}Cl$（正棱锥），$S_{全}=S+\\dfrac{1}{2}Cl$。")+
 p("<strong>圆锥：</strong>$V=\\dfrac{1}{3}\\pi r^2 h$，$S_{侧}=\\pi rl$，$S_{全}=\\pi r^2+\\pi rl$（母线 $l=\\sqrt{r^2+h^2}$）。")+
 p("<strong>棱台：</strong>$V=\\dfrac{h}{3}\\left(S_{上}+\\sqrt{S_{上}S_{下}}+S_{下}\\right)$。")+
 p("<strong>圆台：</strong>$V=\\dfrac{\\pi h}{3}(r^2+rR+R^2)$，$S_{侧}=\\pi(r+R)l$。")+
 p("<strong>球：</strong>$V=\\dfrac{4}{3}\\pi R^3$，$S_{球}=4\\pi R^2$。")+
 p("<strong>正方体：</strong>$V=a^3$，$S_{全}=6a^2$，体对角线 $\\sqrt3 a$。")+
 p("<strong>正四面体：</strong>$V=\\dfrac{\\sqrt2}{12}a^3$，$S_{全}=\\sqrt3 a^2$（棱长 $a$）。")+
 der(p("<strong>台的统一性推导：</strong>棱台（圆台）体积 $V=\\dfrac{h}{3}(S_{上}+\\sqrt{S_{上}S_{下}}+S_{下})$。当 $S_{上}=S_{下}=S$ 时 $V=\\dfrac{h}{3}(S+S+S)=Sh$，退化为<strong>柱</strong>体积；当 $S_{上}=0$ 时 $V=\\dfrac{h}{3}S_{下}$，退化为<strong>锥</strong>体积。故柱、锥皆为台的特例。")+
 p("<strong>球体积推导（祖暅原理）：</strong>半径 $R$ 的球与「底面半径 $R$、高 $2R$ 的圆柱挖去同底等高圆锥」等积。水平截面处球截面 $\\pi(R^2-x^2)$ 与挖空后环形截面 $\\pi R^2-\\pi x^2$ 面积相等，由祖暅原理体积相等，得 $V_{球}=2\\pi R^3-\\dfrac{2}{3}\\pi R^3=\\dfrac{4}{3}\\pi R^3$。")+
 p("<strong>圆台侧面积推导：</strong>圆台由圆锥截得，母线 $l$，侧面积等于两圆锥侧面积之差 $=\\pi R l_1-\\pi r l_2$，由相似 $\\dfrac{l_2}{l_1}=\\dfrac{r}{R}$、$l_1-l_2=l$ 解得 $=\\pi(r+R)l$。")+
 note(p("记忆要点：柱 $V=Sh$、锥 $V=\\dfrac{1}{3}Sh$、台取「上下底面积几何平均」形式，球为特殊旋转体；侧面积只算侧面，全面积需加上下底。"))))
}
]}
]

# ============ 第七章 解析几何 ============
ch7_sections = [
{"name":"7.1 坐标系与参数方程","color":"#0891b2","desc":"极坐标、柱坐标、球坐标、参数方程",
"items":[
{"id":"e7s1-1","name":"极坐标与直角坐标","tags":["def","thm","der","exa"],"brief":"极坐标定义、与直角坐标互化、常见极坐标方程。",
"fig":"polar_coord","figCap":"极坐标 $P(\\rho,\\theta)$，极径与极角",
"body":wrap(
 defn("极坐标",p("平面上取定点 $O$ 为极点、射线 $Ox$ 为极轴。点 $P$ 的极坐标 $(\\rho,\\theta)$，$\\rho$ 为极径（$|OP|$）、$\\theta$ 为极角（$Ox$ 到 $OP$ 的角）。"))+
 thm("坐标互化",p("")+
 fml("x=\\rho\\cos\\theta,\\ y=\\rho\\sin\\theta,\\ \\rho^2=x^2+y^2,\\ \\tan\\theta=\\dfrac{y}{x}"))+
 der(p("<strong>互化推导：</strong>以极点为原点、极轴为 $x$ 轴正向建立直角坐标系。设 $P$ 直角坐标 $(x,y)$、极坐标 $(\\rho,\\theta)$。由直角三角形 $OP$ 在 $x$ 轴投影 $x=\\rho\\cos\\theta$，$y$ 轴投影 $y=\\rho\\sin\\theta$（三角函数定义）。反过来 $\\rho=\\sqrt{x^2+y^2}$（距离公式），$\\tan\\theta=\\dfrac{y}{x}$（正切定义），$\\theta$ 由象限确定。")+
 p("<strong>极坐标方程推导：</strong>圆 $x^2+y^2=r^2$ 化为 $\\rho=r$；直线 $x=a$ 化为 $\\rho\\cos\\theta=a$；心形线 $\\rho=a(1+\\cos\\theta)$（由动点与圆上点距离关系构造）；玫瑰线 $\\rho=a\\cos(n\\theta)$。"))+
 exa(p("<strong>例：</strong>$\\rho=2\\cos\\theta$ 化直角坐标。$\\rho=2\\dfrac{x}{\\rho}$，$\\rho^2=2x$，$x^2+y^2=2x$，即 $(x-1)^2+y^2=1$，圆心 $(1,0)$ 半径 1。")))
},
{"id":"e7s1-2","name":"参数方程与坐标变换","tags":["def","thm","der"],"brief":"参数方程概念、直线圆的参数方程、坐标变换。",
"body":wrap(
 defn("参数方程",p("曲线上点的坐标 $(x,y)$ 用第三变量 $t$（参数）表示：$\\begin{cases}x=f(t)\\\\y=g(t)\\end{cases}$，称曲线的参数方程。"))+
 thm("常见参数方程",p("")+
 fml("\\text{直线过}(x_0,y_0)\\text{方向}(a,b):\\ \\begin{cases}x=x_0+a t\\\\y=y_0+b t\\end{cases}")+
 fml("\\text{圆}(x_0,y_0)\\text{半径}r:\\ \\begin{cases}x=x_0+r\\cos t\\\\y=y_0+r\\sin t\\end{cases}")+
 fml("\\text{椭圆}:\\ \\begin{cases}x=a\\cos t\\\\y=b\\sin t\\end{cases}"))+
 der(p("<strong>圆参数方程推导：</strong>圆 $(x-x_0)^2+(y-y_0)^2=r^2$，设圆心 $(x_0,y_0)$、半径 $r$。圆上点 $P$ 与圆心连线和 $x$ 轴正向夹角 $t$，由三角函数 $P$ 相对圆心位移 $(r\\cos t,r\\sin t)$，故 $x=x_0+r\\cos t$，$y=y_0+r\\sin t$。")+
 p("<strong>椭圆参数推导：</strong>椭圆 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1$。设 $x=a\\cos t$，代入方程 $\\dfrac{a^2\\cos^2 t}{a^2}+\\dfrac{y^2}{b^2}=1$，得 $y^2=b^2\\sin^2 t$，$y=\\pm b\\sin t$，取 $y=b\\sin t$ 得参数方程。参数 $t$ 是辅助圆上对应圆心角，不是椭圆上点与原点连线和 $x$ 轴的夹角。")+
 p("<strong>化参数为普通方程：</strong>消去参数 $t$。如 $\\begin{cases}x=2t\\\\y=t^2\\end{cases}$，由 $t=\\dfrac{x}{2}$ 代入 $y=\\left(\\dfrac{x}{2}\\right)^2=\\dfrac{x^2}{4}$，即抛物线 $x^2=4y$。")))
},
{"id":"e7s1-3","name":"柱坐标与球坐标","tags":["def","thm","der","exa"],"brief":"柱坐标、球坐标定义及与直角坐标互化。",
"body":wrap(
 defn("柱坐标",p("空间点 $P$ 的柱坐标 $(\\rho,\\theta,z)$，其中 $(\\rho,\\theta)$ 为 $P$ 在 $xy$ 平面投影的极坐标，$z$ 为 $P$ 的高度。"))+
 defn("球坐标",p("空间点 $P$ 的球坐标 $(r,\\theta,\\varphi)$，$r$ 为到原点距离，$\\theta$ 为方位角（$x$ 轴正向与投影夹角），$\\varphi$ 为俯仰角（$z$ 轴正向与 $OP$ 夹角）。"))+
 thm("坐标互化",p("")+
 fml("\\text{柱: }x=\\rho\\cos\\theta,\\ y=\\rho\\sin\\theta,\\ z=z")+
 fml("\\text{球: }x=r\\sin\\varphi\\cos\\theta,\\ y=r\\sin\\varphi\\sin\\theta,\\ z=r\\cos\\varphi"))+
 der(p("<strong>柱坐标推导：</strong>柱坐标是极坐标在 $z$ 方向的推广。$P$ 在 $xy$ 平面投影 $P'$ 的极坐标为 $(\\rho,\\theta)$，$P$ 的 $z$ 坐标即 $P'$ 加上 $z$ 方向位移，故 $x=\\rho\\cos\\theta$，$y=\\rho\\sin\\theta$，$z=z$。")+
 p("<strong>球坐标推导：</strong>$P$ 到原点距离 $r$。$OP$ 与 $z$ 轴正向夹角 $\\varphi$，则 $P$ 在 $z$ 轴投影 $z=r\\cos\\varphi$。$P$ 在 $xy$ 平面投影长度 $\\rho'=r\\sin\\varphi$（由直角三角形 $OP'P$）。该投影的极角为 $\\theta$，故 $x=\\rho'\\cos\\theta=r\\sin\\varphi\\cos\\theta$，$y=\\rho'\\sin\\theta=r\\sin\\varphi\\sin\\theta$。"))+
 exa(p("<strong>例：</strong>直角坐标 $(0,0,1)$ 的球坐标为 $(1,0,0)$（$r=1,\\varphi=0$）。")))
}
]},
{"name":"7.2 向量","color":"#0e7490","desc":"平面向量与空间向量的运算、数量积与坐标表示",
"items":[
{"id":"e7v-1","name":"平面向量及其运算","tags":["def","thm","der","exa"],"brief":"向量概念、加减数乘、坐标运算、数量积与共线垂直判定。",
"body":wrap(
 defn("向量",p("既有大小又有方向的量称<strong>向量</strong>，记 $\\vec{a}$。大小称模 $|\\vec{a}|$；模为 1 的称单位向量，模为 0 的称零向量。坐标表示 $\\vec{a}=(x,y)$。"))+
 thm("线性运算",p("")+
 fml("\\vec{a}\\pm\\vec{b}=(x_1\\pm x_2,\\ y_1\\pm y_2),\\quad \\lambda\\vec{a}=(\\lambda x_1,\\lambda y_1)"))+
 thm("数量积",p("")+
 fml("\\vec{a}\\cdot\\vec{b}=x_1x_2+y_1y_2=|\\vec{a}||\\vec{b}|\\cos\\theta"))+
 thm("共线与垂直",p("共线（平行）$\\vec{a}\\parallel\\vec{b}\\Leftrightarrow x_1y_2-x_2y_1=0$（即 $\\vec{a}=\\lambda\\vec{b}$）；垂直 $\\vec{a}\\perp\\vec{b}\\Leftrightarrow \\vec{a}\\cdot\\vec{b}=0$。"))+
 der(p("<strong>坐标运算推导（加法）：</strong>按单位基底分解 $\\vec{a}=x_1\\vec{i}+y_1\\vec{j},\\ \\vec{b}=x_2\\vec{i}+y_2\\vec{j}$，相加合并同类项得 $\\vec{a}+\\vec{b}=(x_1+x_2)\\vec{i}+(y_1+y_2)\\vec{j}=(x_1+x_2,\\ y_1+y_2)$。")+
 p("<strong>数量积坐标推导：</strong>由 $\\vec{i}\\cdot\\vec{i}=\\vec{j}\\cdot\\vec{j}=1$、$\\vec{i}\\cdot\\vec{j}=0$，展开 $(x_1\\vec{i}+y_1\\vec{j})\\cdot(x_2\\vec{i}+y_2\\vec{j})=x_1x_2+y_1y_2$，即坐标对应相乘再相加。")+
 p("<strong>模与夹角：</strong>$|\\vec{a}|=\\sqrt{x_1^2+y_1^2}$，$\\cos\\theta=\\dfrac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}||\\vec{b}|}=\\dfrac{x_1x_2+y_1y_2}{\\sqrt{x_1^2+y_1^2}\\sqrt{x_2^2+y_2^2}}$。"))+
 exa(p("<strong>例：</strong>$\\vec{a}=(1,2),\\vec{b}=(3,-1)$，$\\vec{a}\\cdot\\vec{b}=3-2=1$，$\\vec{a}+\\vec{b}=(4,1)$，$|\\vec{a}|=\\sqrt5$。")))
},
{"id":"e7v-2","name":"空间向量","tags":["def","thm","der","exa"],"brief":"空间向量坐标运算、数量积、夹角与空间距离。",
"body":wrap(
 defn("空间向量",p("空间向量坐标表示 $\\vec{a}=(x,y,z)$，模 $|\\vec{a}|=\\sqrt{x^2+y^2+z^2}$。空间任意向量可由三个不共面向量线性表示。"))+
 thm("数量积",p("")+
 fml("\\vec{a}\\cdot\\vec{b}=x_1x_2+y_1y_2+z_1z_2=|\\vec{a}||\\vec{b}|\\cos\\langle\\vec{a},\\vec{b}\\rangle"))+
 thm("距离与夹角",p("")+
 fml("|P_1P_2|=\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}"))+
 der(p("<strong>数量积推导：</strong>由 $\\vec{a}\\cdot\\vec{b}=|\\vec{a}||\\vec{b}|\\cos\\theta$ 及余弦定理 $|\\vec{a}-\\vec{b}|^2=|\\vec{a}|^2+|\\vec{b}|^2-2\\vec{a}\\cdot\\vec{b}$，得 $\\vec{a}\\cdot\\vec{b}=\\dfrac{|\\vec{a}|^2+|\\vec{b}|^2-|\\vec{a}-\\vec{b}|^2}{2}$。代入坐标 $|\\vec{a}-\\vec{b}|^2=(x_1-x_2)^2+(y_1-y_2)^2+(z_1-z_2)^2$ 展开化简得 $\\vec{a}\\cdot\\vec{b}=x_1x_2+y_1y_2+z_1z_2$。")+
 p("<strong>夹角推导：</strong>$\\cos\\theta=\\dfrac{x_1x_2+y_1y_2+z_1z_2}{\\sqrt{x_1^2+y_1^2+z_1^2}\\sqrt{x_2^2+y_2^2+z_2^2}}$；$\\vec{a}\\perp\\vec{b}\\Leftrightarrow\\vec{a}\\cdot\\vec{b}=0$，$\\vec{a}\\parallel\\vec{b}\\Leftrightarrow\\vec{a}=\\lambda\\vec{b}$。"))+
 exa(p("<strong>例：</strong>$\\vec{a}=(1,0,1),\\vec{b}=(0,1,1)$，$\\vec{a}\\cdot\\vec{b}=1$，$|\\vec{a}|=|\\vec{b}|=\\sqrt2$，$\\cos\\theta=\\dfrac12$，$\\theta=60^\\circ$。")))
}
]},
{"name":"7.3 直线与圆","color":"#0e7490","desc":"直线方程、圆的方程、距离公式",
"items":[
{"id":"e7s2-1","name":"直线方程与位置关系","tags":["def","thm","der","exa"],"brief":"点斜式、斜截式、一般式及两直线位置关系。",
"body":wrap(
 defn("直线方程",p("① <strong>点斜式</strong> $y-y_0=k(x-x_0)$（过 $(x_0,y_0)$ 斜率 $k$）；② <strong>斜截式</strong> $y=kx+b$；③ <strong>两点式</strong> $\\dfrac{y-y_1}{y_2-y_1}=\\dfrac{x-x_1}{x_2-x_1}$；④ <strong>一般式</strong> $Ax+By+C=0$。"))+
 thm("位置关系",p("")+
 fml("l_1: A_1 x+B_1 y+C_1=0,\\ l_2: A_2 x+B_2 y+C_2=0")+
 fml("\\dfrac{A_1}{A_2}=\\dfrac{B_1}{B_2}\\ne\\dfrac{C_1}{C_2}\\Rightarrow\\text{平行}"))+
 der(p("<strong>夹角推导：</strong>两直线斜率 $k_1,k_2$，方向向量 $(1,k_1),(1,k_2)$，夹角 $\\varphi$ 满足 $\\tan\\varphi=\\left|\\dfrac{k_2-k_1}{1+k_1 k_2}\\right|$（$k_1 k_2\\ne-1$）。由两方向向量夹角公式 $\\cos\\varphi=\\dfrac{1+k_1 k_2}{\\sqrt{1+k_1^2}\\sqrt{1+k_2^2}}$ 取正切整理得。")+
 p("<strong>平行重合推导：</strong>两直线 $A_1 x+B_1 y+C_1=0$ 与 $A_2 x+B_2 y+C_2=0$ 法向量 $(A_1,B_1),(A_2,B_2)$。平行 $\\Leftrightarrow$ 法向量平行 $\\Leftrightarrow\\dfrac{A_1}{A_2}=\\dfrac{B_1}{B_2}$；重合 $\\Leftrightarrow$ 比值相等且 $\\dfrac{C_1}{C_2}$ 同比值；相交 $\\Leftrightarrow$ 法向量不平行。")+
 p("<strong>垂直推导：</strong>斜率存在时 $k_1 k_2=-1$；一般式 $A_1 A_2+B_1 B_2=0$（法向量数量积为零）。"))+
 exa(p("<strong>例：</strong>过 $(1,2)$ 斜率 $-1$ 的直线：$y-2=-(x-1)$ 即 $x+y-3=0$。")))
},
{"id":"e7s2-2","name":"圆的方程与切线","tags":["def","thm","der","exa"],"brief":"圆的标准方程、一般方程与切线方程。",
"fig":"circle","figCap":"圆 $(x-a)^2+(y-b)^2=r^2$，圆心 $(a,b)$ 半径 $r$",
"body":wrap(
 defn("圆的方程",p("① <strong>标准方程</strong> $(x-a)^2+(y-b)^2=r^2$，圆心 $(a,b)$、半径 $r$；② <strong>一般方程</strong> $x^2+y^2+Dx+Ey+F=0$（$D^2+E^2-4F>0$），圆心 $\\left(-\\dfrac{D}{2},-\\dfrac{E}{2}\\right)$、半径 $\\dfrac{1}{2}\\sqrt{D^2+E^2-4F}$。"))+
 thm("切线方程",p("过圆 $(x-a)^2+(y-b)^2=r^2$ 上一点 $(x_0,y_0)$ 的切线：")+
 fml("(x_0-a)(x-a)+(y_0-b)(y-b)=r^2"))+
 der(p("<strong>标准方程推导：</strong>圆是到定点 $(a,b)$ 距离等于 $r$ 的点集，由距离公式 $\\sqrt{(x-a)^2+(y-b)^2}=r$，平方得 $(x-a)^2+(y-b)^2=r^2$。")+
 p("<strong>一般方程推导：</strong>展开标准方程 $x^2+y^2-2ax-2by+(a^2+b^2-r^2)=0$，令 $D=-2a,E=-2b,F=a^2+b^2-r^2$ 得 $x^2+y^2+Dx+Ey+F=0$。圆心 $(-D/2,-E/2)$，半径平方 $=a^2+b^2-F=\\dfrac{D^2+E^2}{4}-F=\\dfrac{D^2+E^2-4F}{4}$，需 $D^2+E^2-4F>0$。")+
 p("<strong>切线推导：</strong>切线过 $(x_0,y_0)$ 且与半径垂直。圆心到切点向量 $(x_0-a,y_0-b)$，切线方向与此向量垂直，故切线方程 $(x_0-a)(x-x_0)+(y_0-b)(y-y_0)=0$，化简用 $(x_0-a)^2+(y_0-b)^2=r^2$ 得 $(x_0-a)(x-a)+(y_0-b)(y-b)=r^2$。"))+
 exa(p("<strong>例：</strong>圆 $x^2+y^2=4$ 上 $(1,\\sqrt3)$ 处切线：$1\\cdot x+\\sqrt3\\cdot y=4$，即 $x+\\sqrt3 y=4$。")))
},
{"id":"e7s2-3","name":"距离公式","tags":["def","thm","der"],"brief":"两点距离、点到直线距离、平行线距离。",
"fig":"number_line","figCap":"数轴上两点距离 $|a-b|$，平面距离公式推广",
"body":wrap(
 thm("距离公式",p("")+
 fml("d_{\\text{两点}}=\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}")+
 fml("d_{\\text{点线}}=\\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}")+
 fml("d_{\\text{平行线}}=\\dfrac{|C_1-C_2|}{\\sqrt{A^2+B^2}}\\ (A_1=A_2,B_1=B_2)"))+
 der(p("<strong>两点距离推导：</strong>设 $P_1(x_1,y_1),P_2(x_2,y_2)$，构造直角三角形，两直角边 $|x_2-x_1|$ 与 $|y_2-y_1|$，由勾股定理 $|P_1P_2|=\\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$。")+
 p("<strong>点线距离推导：</strong>点 $P_0(x_0,y_0)$ 到直线 $Ax+By+C=0$。直线法向量 $\\vec{n}=(A,B)$，单位法向量 $\\dfrac{\\vec{n}}{|\\vec{n}|}$。设 $P$ 为 $P_0$ 到直线的垂足，$\\vec{P_0P}=t\\dfrac{\\vec{n}}{|\\vec{n}|}$。$P$ 在直线上：$A(x_0+tA/|n|)+B(y_0+tB/|n|)+C=0$，解 $t=-\\dfrac{Ax_0+By_0+C}{|n|}\\cdot|n|=-(Ax_0+By_0+C)/|n|\\cdot...$，距离 $d=|t|=\\dfrac{|Ax_0+By_0+C|}{\\sqrt{A^2+B^2}}$。")+
 p("<strong>平行线距离推导：</strong>两平行线 $Ax+By+C_1=0$ 与 $Ax+By+C_2=0$（法向量相同故平行）。在第一条上任取一点 $P_0$（满足 $Ax_0+By_0+C_1=0$），到第二条距离 $=\\dfrac{|Ax_0+By_0+C_2|}{\\sqrt{A^2+B^2}}=\\dfrac{|C_2-C_1|}{\\sqrt{A^2+B^2}}$。")))
}
]},
{"name":"7.4 圆锥曲线","color":"#0e7490","desc":"椭圆、双曲线、抛物线的定义与标准方程",
"items":[
{"id":"e7c-1","name":"椭圆","tags":["def","thm","der","exa"],"brief":"椭圆定义、标准方程推导、离心率与几何性质。",
"fig":"ellipse","figCap":"椭圆 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1$，两焦点 $F_1,F_2$",
"body":wrap(
 defn("椭圆",p("平面内到两定点 $F_1,F_2$ 距离之和等于常数 $2a$（$2a>|F_1F_2|=2c$）的点的轨迹称<strong>椭圆</strong>。$F_1,F_2$ 为焦点，$a$ 为长半轴，$b=\\sqrt{a^2-c^2}$ 为短半轴。"))+
 thm("标准方程",p("焦点在 $x$ 轴、中心在原点：")+
 fml("\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1\\quad(a>b>0)"))+
 thm("几何性质",p("范围 $|x|\\le a,|y|\\le b$；顶点 $(\\pm a,0),(0,\\pm b)$；离心率 $e=\\dfrac{c}{a}\\in(0,1)$；长轴 $2a$、短轴 $2b$、焦距 $2c$，满足 $a^2=b^2+c^2$。"))+
 der(p("<strong>标准方程推导：</strong>设焦点 $F_1(-c,0),F_2(c,0)$。由定义 $\\sqrt{(x+c)^2+y^2}+\\sqrt{(x-c)^2+y^2}=2a$。移项平方化简得 $a^2-cx=a\\sqrt{(x-c)^2+y^2}$，再平方整理得 $(a^2-c^2)x^2+a^2y^2=a^2(a^2-c^2)$。令 $b^2=a^2-c^2$，两边除以 $a^2b^2$ 即得 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1$。")+
 p("<strong>离心率意义：</strong>$e=\\dfrac{c}{a}=\\sqrt{1-\\dfrac{b^2}{a^2}}$。离心率越小，$b$ 越接近 $a$，椭圆越接近圆；离心率越大，椭圆越扁平。"))+
 exa(p("<strong>例：</strong>椭圆 $\\dfrac{x^2}{25}+\\dfrac{y^2}{9}=1$，$a=5,b=3,c=\\sqrt{25-9}=4$，$e=\\dfrac{4}{5}$，焦点 $(\\pm4,0)$。")))
},
{"id":"e7c-2","name":"双曲线","tags":["def","thm","der","exa"],"brief":"双曲线定义、标准方程、渐近线与离心率。",
"body":wrap(
 defn("双曲线",p("平面内到两定点 $F_1,F_2$ 距离之差的绝对值等于常数 $2a$（$0<2a<|F_1F_2|=2c$）的点的轨迹称<strong>双曲线</strong>。"))+
 thm("标准方程",p("焦点在 $x$ 轴、中心在原点：")+
 fml("\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=1\\quad(a,b>0)"))+
 thm("几何性质",p("渐近线 $y=\\pm\\dfrac{b}{a}x$；离心率 $e=\\dfrac{c}{a}\\in(1,+\\infty)$；$c^2=a^2+b^2$；实轴 $2a$、虚轴 $2b$。"))+
 der(p("<strong>标准方程推导：</strong>设焦点 $F_1(-c,0),F_2(c,0)$。由定义 $\\left|\\sqrt{(x+c)^2+y^2}-\\sqrt{(x-c)^2+y^2}\\right|=2a$。平方整理（同椭圆）得 $(c^2-a^2)x^2-a^2y^2=a^2(c^2-a^2)$。令 $b^2=c^2-a^2$，除以 $a^2b^2$ 得 $\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=1$。")+
 p("<strong>渐近线推导：</strong>当 $|x|$ 很大时，$\\dfrac{y^2}{b^2}=\\dfrac{x^2}{a^2}-1\\approx\\dfrac{x^2}{a^2}$，故 $y\\approx\\pm\\dfrac{b}{a}x$，即双曲线向两直线 $y=\\pm\\dfrac{b}{a}x$（渐近线）无限靠拢。"))+
 exa(p("<strong>例：</strong>双曲线 $\\dfrac{x^2}{9}-\\dfrac{y^2}{16}=1$，$a=3,b=4,c=5$，渐近线 $y=\\pm\\dfrac{4}{3}x$，$e=\\dfrac{5}{3}$。")))
},
{"id":"e7c-3","name":"抛物线","tags":["def","thm","der","exa"],"brief":"抛物线定义、标准方程、焦点与准线。",
"body":wrap(
 defn("抛物线",p("平面内到定点 $F$（焦点）与定直线 $l$（准线）距离相等的点的轨迹称<strong>抛物线</strong>。"))+
 thm("标准方程",p("开口向右、顶点在原点：")+
 fml("y^2=2px\\quad(p>0)"))+
 thm("几何性质",p("焦点 $F\\left(\\dfrac{p}{2},0\\right)$，准线 $x=-\\dfrac{p}{2}$，离心率 $e=1$。$p$ 为焦点到准线的距离；开口方向由一次项决定（$y^2=2px$ 向右，$y^2=-2px$ 向左，$x^2=2py$ 向上，$x^2=-2py$ 向下）。"))+
 der(p("<strong>标准方程推导：</strong>设焦点 $F\\left(\\dfrac{p}{2},0\\right)$、准线 $x=-\\dfrac{p}{2}$。由定义 $\\sqrt{\\left(x-\\dfrac{p}{2}\\right)^2+y^2}=\\left|x+\\dfrac{p}{2}\\right|$，两边平方：$x^2-px+\\dfrac{p^2}{4}+y^2=x^2+px+\\dfrac{p^2}{4}$，整理得 $y^2=2px$。")+
 p("<strong>通径：</strong>过焦点垂直于对称轴的弦称通径，长为 $2p$，是过焦点的最短弦。"))+
 exa(p("<strong>例：</strong>抛物线 $y^2=8x$，$2p=8$，$p=4$，焦点 $(2,0)$，准线 $x=-2$。")))
}
]},
{"name":"7.5 空间解析几何","color":"#155e75","desc":"空间直线方程、平面方程、线面关系",
"items":[
{"id":"e7s3-1","name":"空间直线方程","tags":["def","thm","der","exa"],"brief":"空间直线参数方程、对称式方程与一般式方程。",
"body":wrap(
 defn("空间直线方程",p("空间直线由一点 $P_0(x_0,y_0,z_0)$ 和方向向量 $\\vec{v}=(m,n,p)$ 确定。三种形式：① <strong>参数方程</strong> $\\vec{r}=\\vec{r_0}+t\\vec{v}$，即 $\\begin{cases}x=x_0+mt\\\\y=y_0+nt\\\\z=z_0+pt\\end{cases}$；② <strong>对称式</strong> $\\dfrac{x-x_0}{m}=\\dfrac{y-y_0}{n}=\\dfrac{z-z_0}{p}$；③ <strong>一般式</strong>（两平面交线）$\\begin{cases}A_1 x+B_1 y+C_1 z+D_1=0\\\\A_2 x+B_2 y+C_2 z+D_2=0\\end{cases}$。"))+
 thm("方向向量与夹角",p("")+
 fml("\\cos\\varphi=\\dfrac{|m_1 m_2+n_1 n_2+p_1 p_2|}{\\sqrt{m_1^2+n_1^2+p_1^2}\\sqrt{m_2^2+n_2^2+p_2^2}}"))+
 der(p("<strong>参数方程推导：</strong>直线上一点 $P_0$，方向向量 $\\vec{v}$。直线上任一点 $P$ 满足 $\\vec{P_0P}=t\\vec{v}$（$t$ 为参数），即 $(x-x_0,y-y_0,z-z_0)=t(m,n,p)$，分量形式即参数方程。")+
 p("<strong>对称式推导：</strong>由参数方程 $x=x_0+mt$ 解出 $t=\\dfrac{x-x_0}{m}$，同理 $t=\\dfrac{y-y_0}{n}=\\dfrac{z-z_0}{p}$，消去 $t$ 得对称式。当 $m,n,p$ 中有零时相应分子也为零。")+
 p("<strong>一般式推导：</strong>两平面 $\\Pi_1,\\Pi_2$ 的法向量 $\\vec{n_1},\\vec{n_2}$ 不平行时交线为直线，方向向量 $\\vec{v}=\\vec{n_1}\\times\\vec{n_2}$（叉积）。"))+
 exa(p("<strong>例：</strong>过 $(1,2,3)$ 方向向量 $(1,0,1)$ 的直线参数方程 $\\begin{cases}x=1+t\\\\y=2\\\\z=3+t\\end{cases}$。")))
},
{"id":"e7s3-2","name":"平面方程","tags":["def","thm","der","exa"],"brief":"平面点法式、一般式与截距式方程。",
"body":wrap(
 defn("平面方程",p("过点 $P_0(x_0,y_0,z_0)$、法向量 $\\vec{n}=(A,B,C)$ 的平面方程：① <strong>点法式</strong> $A(x-x_0)+B(y-y_0)+C(z-z_0)=0$；② <strong>一般式</strong> $Ax+By+Cz+D=0$；③ <strong>截距式</strong> $\\dfrac{x}{a}+\\dfrac{y}{b}+\\dfrac{z}{c}=1$（$a,b,c$ 为三轴截距）。"))+
 thm("两平面夹角",p("")+
 fml("\\cos\\varphi=\\dfrac{|A_1 A_2+B_1 B_2+C_1 C_2|}{\\sqrt{A_1^2+B_1^2+C_1^2}\\sqrt{A_2^2+B_2^2+C_2^2}}"))+
 der(p("<strong>点法式推导：</strong>平面上任一点 $P(x,y,z)$，向量 $\\vec{P_0P}=(x-x_0,y-y_0,z-z_0)$ 与法向量 $\\vec{n}$ 垂直，故 $\\vec{n}\\cdot\\vec{P_0P}=0$，即 $A(x-x_0)+B(y-y_0)+C(z-z_0)=0$。")+
 p("<strong>一般式推导：</strong>展开点法式 $Ax+By+Cz+(-Ax_0-By_0-Cz_0)=0$，令 $D=-Ax_0-By_0-Cz_0$ 得一般式 $Ax+By+Cz+D=0$。")+
 p("<strong>截距式推导：</strong>平面与三坐标轴交于 $(a,0,0),(0,b,0),(0,0,c)$，代入一般式得 $Aa+D=0$ 故 $A=-D/a$，同理 $B=-D/b,C=-D/c$。代入一般式除以 $-D$ 得 $\\dfrac{x}{a}+\\dfrac{y}{b}+\\dfrac{z}{c}=1$。"))+
 exa(p("<strong>例：</strong>过 $(1,2,3)$ 法向量 $(1,1,1)$ 的平面：$1(x-1)+1(y-2)+1(z-3)=0$，即 $x+y+z-6=0$。")))
},
{"id":"e7s3-3","name":"线面关系与距离","tags":["def","thm","der","exa"],"brief":"线面平行垂直判定、面面夹角、点到面距离公式。",
"body":wrap(
 defn("线面关系",p("直线方向向量 $\\vec{v}$，平面法向量 $\\vec{n}$。线面平行 $\\Leftrightarrow\\vec{v}\\perp\\vec{n}$（$\\vec{v}\\cdot\\vec{n}=0$）；线面垂直 $\\Leftrightarrow\\vec{v}\\parallel\\vec{n}$（$\\vec{v}=\\lambda\\vec{n}$）。"))+
 thm("点到面距离",p("")+
 fml("d=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}"))+
 der(p("<strong>点面距离推导：</strong>平面 $Ax+By+Cz+D=0$ 法向量 $\\vec{n}=(A,B,C)$。点 $P_0(x_0,y_0,z_0)$ 到平面距离 = $P_0$ 沿法向量方向到平面的有向距离。设 $P$ 为垂足，$\\vec{P_0P}=t\\dfrac{\\vec{n}}{|\\vec{n}|}$。$P$ 在平面上：$A(x_0+tA/|n|)+B(y_0+tB/|n|)+C(z_0+tC/|n|)+D=0$，解 $t=-\\dfrac{Ax_0+By_0+Cz_0+D}{|\\vec{n}|}$，距离 $d=|t|=\\dfrac{|Ax_0+By_0+Cz_0+D|}{\\sqrt{A^2+B^2+C^2}}$。")+
 p("<strong>线面平行推导：</strong>直线 $l$ 方向向量 $\\vec{v}$，平面 $\\Pi$ 法向量 $\\vec{n}$。$l\\parallel\\Pi$ $\\Leftrightarrow$ $\\vec{v}\\perp\\vec{n}$ $\\Leftrightarrow$ $\\vec{v}\\cdot\\vec{n}=0$（方向向量与法向量垂直，则直线与法向量垂直的平面平行）。")+
 p("<strong>面面夹角推导：</strong>两平面法向量 $\\vec{n_1},\\vec{n_2}$，二面角的平面角与法向量夹角相等或互补，$\\cos\\varphi=\\dfrac{|\\vec{n_1}\\cdot\\vec{n_2}|}{|\\vec{n_1}||\\vec{n_2}|}$。"))+
 exa(p("<strong>例：</strong>原点到平面 $2x+3y+6z-21=0$ 距离 $d=\\dfrac{|-21|}{\\sqrt{4+9+36}}=\\dfrac{21}{7}=3$。")))
}
]},
{"name":"7.6 二次曲面","color":"#0f766e","desc":"椭球面、双曲面、抛物面、锥面",
"items":[
{"id":"e7s4-1","name":"椭球面与单叶双曲面","tags":["def","thm","der","exa"],"brief":"椭球面与单叶双曲面的标准方程与截痕法。",
"body":wrap(
 defn("椭球面",p("标准方程 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}+\\dfrac{z^2}{c^2}=1$。三个半轴长 $a,b,c$，若 $a=b=c$ 退化为球面。"))+
 defn("单叶双曲面",p("标准方程 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=1$。形如腰鼓，单叶（连通）且为直纹面。"))+
 thm("截痕法",p("用坐标面 $z=h$ 截曲面，分析截口曲线形状，从而推断曲面整体形状。"))+
 der(p("<strong>椭球面截痕推导：</strong>用 $z=h$（$|h|\\le c$）截 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1-\\dfrac{h^2}{c^2}$，即椭圆 $\\dfrac{x^2}{a'^2}+\\dfrac{y^2}{b'^2}=1$，其中 $a'=a\\sqrt{1-h^2/c^2}$，$b'=b\\sqrt{1-h^2/c^2}$。$h=0$ 时截口最大，$h=\\pm c$ 时退化为点。同理 $x=h,y=h$ 截口均为椭圆。")+
 p("<strong>单叶双曲面截痕推导：</strong>用 $z=h$ 截 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=1+\\dfrac{h^2}{c^2}$，恒为椭圆（对任意 $h$ 都存在），$|h|$ 越大椭圆越大。用 $y=h$ 截 $\\dfrac{x^2}{a^2}-\\dfrac{z^2}{c^2}=1-\\dfrac{h^2}{b^2}$，$|h|<b$ 时为双曲线，$|h|=b$ 时为两相交直线。"))+
 exa(p("<strong>例：</strong>地球近似为椭球面 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}+\\dfrac{z^2}{c^2}=1$（$a=b>c$，扁率反映地球自转）。")))
},
{"id":"e7s4-2","name":"双叶双曲面与椭圆抛物面","tags":["def","thm","der","exa"],"brief":"双叶双曲面与椭圆抛物面的标准方程与性质。",
"body":wrap(
 defn("双叶双曲面",p("标准方程 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=-1$。分上下两叶，$z$ 轴为对称轴。"))+
 defn("椭圆抛物面",p("标准方程 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=z$。顶点在原点，开口朝 $z$ 轴正向。$a=b$ 时为旋转抛物面。"))+
 thm("截痕特征",p("")+
 fml("\\text{双叶: }\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=\\dfrac{z^2}{c^2}-1\\ (|z|\\ge c)"))+
 der(p("<strong>双叶双曲面截痕推导：</strong>用 $z=h$ 截 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=\\dfrac{h^2}{c^2}-1$。$|h|>c$ 时为椭圆，$|h|=c$ 时退化为点，$|h|<c$ 时无实截口（故分两叶，$z\\ge c$ 与 $z\\le-c$）。用 $y=h$ 截得 $\\dfrac{x^2}{a^2}-\\dfrac{z^2}{c^2}=-1-\\dfrac{h^2}{b^2}$，恒为双曲线。")+
 p("<strong>椭圆抛物面截痕推导：</strong>用 $z=h$（$h\\ge0$）截 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=h$，为椭圆（$h>0$）或点（$h=0$）。用 $y=h$ 截 $\\dfrac{x^2}{a^2}=z-\\dfrac{h^2}{b^2}$，为抛物线（$z\\ge h^2/b^2$）。"))+
 exa(p("<strong>例：</strong>旋转抛物面 $x^2+y^2=z$ 由抛物线 $x^2=z$ 绕 $z$ 轴旋转得到，用于反射望远镜面。")))
},
{"id":"e7s4-3","name":"双曲抛物面与二次锥面","tags":["def","thm","der","exa"],"brief":"双曲抛物面（马鞍面）与二次锥面的标准方程。",
"body":wrap(
 defn("双曲抛物面",p("标准方程 $\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=z$。形似马鞍，又称<strong>马鞍面</strong>。是直纹面。"))+
 defn("二次锥面",p("标准方程 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}-\\dfrac{z^2}{c^2}=0$。顶点在原点，关于 $z$ 轴对称。"))+
 thm("截痕特征",p("")+
 fml("\\text{锥面: }\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=\\dfrac{z^2}{c^2}"))+
 der(p("<strong>马鞍面截痕推导：</strong>用 $z=h$ 截 $\\dfrac{x^2}{a^2}-\\dfrac{y^2}{b^2}=h$。$h>0$ 时为横轴在 $x$ 方向的双曲线；$h<0$ 时为横轴在 $y$ 方向的双曲线；$h=0$ 时为两相交直线 $\\dfrac{x}{a}=\\pm\\dfrac{y}{b}$。用 $y=h$ 截 $\\dfrac{x^2}{a^2}-z=\\dfrac{h^2}{b^2}$ 即 $z=\\dfrac{x^2}{a^2}-\\dfrac{h^2}{b^2}$，为开口朝上的抛物线。用 $x=h$ 截为开口朝下的抛物线，故呈马鞍形。")+
 p("<strong>二次锥面截痕推导：</strong>用 $z=h$（$h\\ne0$）截 $\\dfrac{x^2}{a^2}+\\dfrac{y^2}{b^2}=\\dfrac{h^2}{c^2}$，为椭圆（$a=b$ 时为圆）。$h=0$ 时退化为顶点（原点）。二次锥面是单叶双曲面与双叶双曲面之间的过渡曲面。"))+
 exa(p("<strong>例：</strong>马鞍面 $z=x^2-y^2$ 在原点附近形似马鞍：沿 $x$ 方向向上弯、沿 $y$ 方向向下弯，故又称双曲抛物面。")))
}
]},
{"name":"7.7 空间曲线","color":"#115e59","desc":"空间曲线参数方程、螺旋线与投影",
"items":[
{"id":"e7s5-1","name":"空间曲线参数方程与圆柱螺旋线","tags":["def","thm","der","exa"],"brief":"空间曲线参数方程、圆柱螺旋线及其弧长（展开法）。",
"body":wrap(
 defn("空间曲线",p("空间曲线用参数方程 $\\vec{r}(t)=(x(t),y(t),z(t))$ 表示，$t$ 为参数。"))+
 defn("圆柱螺旋线",p("参数方程 $\\begin{cases}x=a\\cos t\\\\y=a\\sin t\\\\z=bt\\end{cases}$（$a>0$）。点在半径 $a$ 的圆柱面上，每转一整圈上升 $2\\pi b$（螺距）。"))+
 thm("螺旋线弧长（展开法）",p("把圆柱侧面沿母线剪开铺平，圆柱面展成一个矩形，螺旋线展开后恰是一条<strong>直线段</strong>，故可用勾股定理求其长。"))+
 der(p("<strong>展开法推导：</strong>螺旋线转一整圈，沿高度方向上升 $2\\pi b$，沿圆周方向走过一周周长 $2\\pi a$。将圆柱面展开为平面矩形，这段曲线展开后是两直角边分别为 $2\\pi a$ 与 $2\\pi b$ 的直角三角形斜边，由勾股定理，一圈弧长 $s=\\sqrt{(2\\pi a)^2+(2\\pi b)^2}=2\\pi\\sqrt{a^2+b^2}$。")+
 p("<strong>一般弧长：</strong>转过 $t$ 弧度（即 $\\dfrac{t}{2\\pi}$ 圈）时，弧长 $s=\\sqrt{a^2+b^2}\\,t$，与参数成正比。"))+
 exa(p("<strong>例：</strong>螺旋线 $a=1,b=1$，一圈弧长 $s=2\\pi\\sqrt{1+1}=2\\sqrt2\\pi$。")))
},
{"id":"e7s5-2","name":"空间曲线在坐标面上的投影","tags":["def","thm","der","exa"],"brief":"空间曲线投影到坐标面的方法与消元法。",
"body":wrap(
 defn("投影曲线",p("空间曲线 $\\Gamma$ 在 $xOy$ 面上的<strong>投影</strong>，是把 $\\Gamma$ 上每一点 $P(x,y,z)$ 沿 $z$ 方向作垂线所得垂足 $P'(x,y,0)$ 的集合。"))+
 thm("投影求法（消元法）",p("由两曲面 $F_1(x,y,z)=0$ 与 $F_2(x,y,z)=0$ 的交线，消去 $z$ 得投影柱面方程 $H(x,y)=0$，再与 $z=0$ 联立即得 $xOy$ 面上的投影曲线 $\\begin{cases}H(x,y)=0\\\\z=0\\end{cases}$。"))+
 der(p("<strong>消元法推导：</strong>投影过程丢掉了 $z$ 坐标，要刻画投影就要建立只含 $x,y$ 的关系。把两曲面方程看作关于 $z$ 的方程组，消去 $z$ 得 $H(x,y)=0$，它恰是过 $\\Gamma$ 且平行于 $z$ 轴的投影柱面；该柱面与 $xOy$ 面的交线即投影曲线。")+
 p("<strong>直观类比：</strong>投影如同阳光垂直照射下物体在地面的影子，$z$ 方向的光线把曲线压到 $xOy$ 面上。"))+
 exa(p("<strong>例：</strong>圆柱 $x^2+y^2=1$ 与平面 $z=y$ 的交线，把 $z=y$ 视为消去 $z$ 的结果，得投影柱面 $x^2+y^2=1$，故在 $xOy$ 面上的投影为圆 $x^2+y^2=1$。")))
}
]}
]

# ============ 第八章 概率统计 ============
ch8_sections = [
{"name":"8.1 计数原理","color":"#16a34a","desc":"排列、组合、二项式定理",
"items":[
{"id":"e8s1-1","name":"排列与组合","tags":["def","thm","der","exa"],"brief":"排列数组合数定义、性质与计算。",
"fig":"bayes_tree","figCap":"分类计数与分步计数的树状图",
"body":wrap(
 thm("加法原理与乘法原理",p("加法原理：完成一件事有 $n$ 类办法，各类分别 $m_i$ 种，共 $\\sum m_i$ 种。乘法原理：分 $n$ 步，各步 $m_i$ 种，共 $\\prod m_i$ 种。"))+
 thm("排列与组合",p("")+
 fml("A_n^m=\\dfrac{n!}{(n-m)!},\\quad C_n^m=\\dfrac{n!}{m!(n-m)!}"))+
 der(p("<strong>排列数推导：</strong>从 $n$ 个不同元素取 $m$ 个排成一列。第一位 $n$ 种选法，第二位 $(n-1)$ 种（已用去一个），...，第 $m$ 位 $(n-m+1)$ 种。由乘法原理 $A_n^m=n(n-1)\\cdots(n-m+1)=\\dfrac{n!}{(n-m)!}$。")+
 p("<strong>组合数推导：</strong>组合是不考虑顺序的选取。先选 $m$ 个排列 $A_n^m$ 种，每种组合对应 $m!$ 种排列，故组合数 $C_n^m=\\dfrac{A_n^m}{m!}=\\dfrac{n!}{m!(n-m)!}$。")+
 p("<strong>组合性质推导：</strong>① 对称性 $C_n^m=C_n^{n-m}$：$C_n^{n-m}=\\dfrac{n!}{(n-m)!(n-(n-m))!}=\\dfrac{n!}{(n-m)!m!}=C_n^m$；② 帕斯卡 $C_n^m=C_{n-1}^m+C_{n-1}^{m-1}$：从 $n$ 个中选 $m$ 个，按某元素是否入选分类，不选该元素 $C_{n-1}^m$，选该元素 $C_{n-1}^{m-1}$，相加。"))+
 exa(p("<strong>例：</strong>5 人中选 3 人拍照排列 $A_5^3=60$ 种，选 3 人组队 $C_5^3=10$ 种。")))
},
{"id":"e8s1-2","name":"二项式定理","tags":["def","thm","der","exa"],"brief":"二项式展开、通项公式与性质。",
"body":wrap(
 thm("二项式定理",p("")+
 fml("(a+b)^n=\\sum_{k=0}^n \\binom{n}{k}a^{n-k}b^k,\\quad T_{k+1}=\\binom{n}{k}a^{n-k}b^k"))+
 thm("二项式系数性质",p("")+
 fml("\\sum_{k=0}^n \\binom{n}{k}=2^n,\\quad \\binom{n}{k}=\\binom{n}{n-k}")+
 fml("\\binom{n}{k}=\\binom{n-1}{k}+\\binom{n-1}{k-1}\\text{（递推）}"))+
 der(p("<strong>二项式定理推导：</strong>$(a+b)^n$ 展开式中任一项形如 $a^{n-k}b^k$，需在 $n$ 个因子 $(a+b)$ 中选 $k$ 个取 $b$、其余取 $a$。选 $k$ 个因子的方法数 $C_n^k=\\binom{n}{k}$，故 $a^{n-k}b^k$ 的系数 $\\binom{n}{k}$，求和得 $(a+b)^n=\\sum\\binom{n}{k}a^{n-k}b^k$。")+
 p("<strong>求和推导：</strong>令 $a=b=1$，$(1+1)^n=\\sum\\binom{n}{k}=2^n$。")+
 p("<strong>对称性推导：</strong>展开式中 $a^{n-k}b^k$ 与 $a^k b^{n-k}$ 系数分别为 $\\binom{n}{k}$ 与 $\\binom{n}{n-k}$，二者在 $(a+b)^n$ 与 $(b+a)^n$ 中地位对称（$a,b$ 互换），故 $\\binom{n}{k}=\\binom{n}{n-k}$。"))+
 exa(p("<strong>例：</strong>$(x+1)^5$ 中 $x^3$ 系数 $\\binom{5}{2}=10$，常数项 $\\binom{5}{0}=1$。")))
}
]},
{"name":"8.2 概率","color":"#15803d","desc":"古典概型、条件概率、全概率与贝叶斯",
"items":[
{"id":"e8s2-1","name":"古典概型与几何概型","tags":["def","thm","der","exa"],"brief":"古典概型定义、概率计算与几何概型。",
"fig":"probability","figCap":"古典概型 P(A)=m/n，4 个等可能事件",
"body":wrap(
 defn("古典概型",p("若试验满足：① 有限性（基本事件数有限）；② 等可能性（每基本事件概率相等），称<strong>古典概型</strong>。"))+
 thm("概率公式",p("")+
 fml("P(A)=\\dfrac{\\text{A 含基本事件数}}{\\text{基本事件总数}}=\\dfrac{m}{n}")+
 fml("P(A)=\\dfrac{\\mu(A)}{\\mu(\\Omega)}\\text{（几何概型）}"))+
 der(p("<strong>古典概型推导：</strong>由等可能性，$n$ 个基本事件每个概率 $\\dfrac{1}{n}$。事件 $A$ 含 $m$ 个互斥基本事件，由有限可加性 $P(A)=\\sum_{i=1}^m\\dfrac{1}{n}=\\dfrac{m}{n}$。")+
 p("<strong>几何概型推导：</strong>当基本事件无限（线段、平面区域、立体），用测度（长度、面积、体积）比代替个数比。事件 $A$ 在区域 $\\Omega$ 中，$P(A)=\\dfrac{\\mu(A)}{\\mu(\\Omega)}$（均匀分布意义下）。")+
 p("<strong>加法公式推导：</strong>对任意两事件 $P(A\\cup B)=P(A)+P(B)-P(A\\cap B)$。$A\\cup B$ 中 $A$ 与 $B$ 部分重叠时重复计算了 $A\\cap B$，需减去。互斥时 $A\\cap B=\\emptyset$，$P(A\\cup B)=P(A)+P(B)$。"))+
 exa(p("<strong>例：</strong>掷一枚骰子，$P(\\text{偶数})=\\dfrac{3}{6}=\\dfrac{1}{2}$。")))
},
{"id":"e8s2-2","name":"条件概率与全概率公式","tags":["def","thm","der","exa"],"brief":"条件概率、乘法公式、全概率公式推导。",
"body":wrap(
 defn("条件概率",p("事件 $B$ 发生条件下 $A$ 发生的概率：$P(A|B)=\\dfrac{P(AB)}{P(B)}$（$P(B)>0$）。"))+
 thm("乘法公式与全概率",p("")+
 fml("P(AB)=P(B)P(A|B)=P(A)P(B|A)")+
 fml("P(A)=\\sum_i P(B_i)P(A|B_i)\\text{（全概率，$B_i$ 为分割）}"))+
 der(p("<strong>条件概率推导：</strong>$B$ 发生后样本空间缩小为 $B$，$A$ 在 $B$ 内的部分为 $AB$。$A$ 在新样本空间 $B$ 中所占比例 $=\\dfrac{P(AB)}{P(B)}$（用古典概型：$B$ 含 $n_B$ 个基本事件，$AB$ 含 $n_{AB}$ 个，比例 $\\dfrac{n_{AB}}{n_B}=\\dfrac{n_{AB}/n}{n_B/n}=\\dfrac{P(AB)}{P(B)}$）。")+
 p("<strong>乘法公式推导：</strong>由条件概率 $P(A|B)=\\dfrac{P(AB)}{P(B)}$，两边乘 $P(B)$ 得 $P(AB)=P(B)P(A|B)$。对称地 $P(AB)=P(A)P(B|A)$。")+
 p("<strong>全概率推导：</strong>设 $B_1,\\ldots,B_n$ 互斥且 $\\bigcup B_i=\\Omega$（$B_i$ 是样本空间分割）。$A=A\\cap\\Omega=A\\cap\\bigcup B_i=\\bigcup(A\\cap B_i)$（分配律），各 $A\\cap B_i$ 互斥（因 $B_i$ 互斥）。由有限可加性 $P(A)=\\sum P(A\\cap B_i)=\\sum P(B_i)P(A|B_i)$（后者用乘法公式）。"))+
 exa(p("<strong>例：</strong>两厂生产同零件，甲占 60%、合格 95%；乙占 40%、合格 90%。任取一件合格概率 $=0.6\\times0.95+0.4\\times0.9=0.57+0.36=0.93$。")))
},
{"id":"e8s2-3","name":"贝叶斯公式","tags":["def","thm","der","exa"],"brief":"贝叶斯公式推导与后验概率应用。",
"body":wrap(
 thm("贝叶斯公式",p("")+
 fml("P(B_i|A)=\\dfrac{P(B_i)P(A|B_i)}{\\sum_j P(B_j)P(A|B_j)}"))+
 der(p("<strong>贝叶斯推导：</strong>由条件概率定义 $P(B_i|A)=\\dfrac{P(A\\cap B_i)}{P(A)}$。分子用乘法公式 $P(A\\cap B_i)=P(B_i)P(A|B_i)$；分母用全概率公式 $P(A)=\\sum_j P(B_j)P(A|B_j)$。代入得贝叶斯公式。")+
 p("<strong>意义：</strong>$P(B_i)$ 是先验概率（试验前各原因可能性），$P(B_i|A)$ 是后验概率（试验后由结果 $A$ 反推各原因可能性）。贝叶斯公式实现「由果溯因」。")+
 p("<strong>独立事件推导：</strong>若 $P(A|B)=P(A)$（$B$ 发生不影响 $A$ 概率），称 $A,B$ 独立。此时 $P(AB)=P(A)P(B)$（乘法公式结合条件概率等于原概率）。"))+
 exa(p("<strong>例：</strong>接上例，已知取出的是合格品，求来自甲厂概率。$P(B_甲|A)=\\dfrac{0.6\\times0.95}{0.93}=\\dfrac{0.57}{0.93}\\approx0.613$。")))
}
]},
{"name":"8.3 随机变量与统计","color":"#166534","desc":"分布、期望方差、正态分布、回归",
"items":[
{"id":"e8s3-1","name":"离散型随机变量与数字特征","tags":["def","thm","der","exa"],"brief":"分布列、期望与方差的定义及性质。",
"fig":"normal_dist","figCap":"正态分布 $N(\\mu,\\sigma^2)$ 的钟形曲线",
"body":wrap(
 defn("随机变量",p("取值随试验结果而变的变量 $X$ 称<strong>随机变量</strong>。取有限或可列个值的称离散型，取连续区间的称连续型。"))+
 thm("期望与方差",p("")+
 fml("E(X)=\\sum_i x_i p_i,\\quad D(X)=E[(X-E(X))^2]=E(X^2)-[E(X)]^2")+
 fml("E(aX+b)=aE(X)+b,\\quad D(aX+b)=a^2 D(X)"))+
 der(p("<strong>期望推导：</strong>期望是随机变量取值的「加权平均」，权重为概率。$E(X)=\\sum x_i p_i$。由概率归一性 $\\sum p_i=1$，期望是 $x_i$ 的概率加权平均。")+
 p("<strong>方差推导：</strong>方差度量 $X$ 偏离期望的程度。$D(X)=E[(X-E(X))^2]$（偏差平方的期望）。化简：$D(X)=E[X^2-2XE(X)+(E(X))^2]=E(X^2)-2E(X)E(X)+(E(X))^2=E(X^2)-[E(X)]^2$（用 $E$ 线性性及 $E(E(X))=E(X)$）。")+
 p("<strong>线性性质推导：</strong>$E(aX+b)=\\sum(ax_i+b)p_i=a\\sum x_i p_i+b\\sum p_i=aE(X)+b$。$D(aX+b)=E[(aX+b-E(aX+b))^2]=E[(aX-aE(X))^2]=a^2 E[(X-E(X))^2]=a^2 D(X)$。"))+
 exa(p("<strong>例：</strong>掷骰子 $X$ 为点数，$E(X)=\\dfrac{1+2+\\cdots+6}{6}=3.5$，$D(X)=E(X^2)-3.5^2=\\dfrac{91}{6}-12.25\\approx2.92$。")))
},
{"id":"e8s3-2","name":"二项分布与正态分布","tags":["def","thm","der","exa"],"brief":"二项分布、正态分布密度与 3σ 原则。",
"body":wrap(
 defn("二项分布",p("$n$ 次独立重复试验，每次成功概率 $p$，成功次数 $X\\sim B(n,p)$。分布列 $P(X=k)=\\binom{n}{k}p^k(1-p)^{n-k}$。"))+
 thm("二项分布特征",p("")+
 fml("E(X)=np,\\quad D(X)=np(1-p)"))+
 defn("正态分布",p("概率密度 $f(x)=\\dfrac{1}{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$，记 $X\\sim N(\\mu,\\sigma^2)$。$\\mu$ 为均值、$\\sigma^2$ 为方差。"))+
 der(p("<strong>二项分布期望推导：</strong>设 $X_i$ 为第 $i$ 次试验成功次数（0/1），$X_i$ 期望 $p$（伯努利分布）。$X=\\sum X_i$，由期望线性性 $E(X)=\\sum E(X_i)=np$。")+
 p("<strong>二项分布方差推导：</strong>各 $X_i$ 独立，$D(X)=\\sum D(X_i)$。$D(X_i)=E(X_i^2)-[E(X_i)]^2=p-p^2=p(1-p)$（$X_i^2=X_i$ 因 0/1）。故 $D(X)=np(1-p)$。")+
 p("<strong>正态 3σ 推导：</strong>标准正态 $Z=\\dfrac{X-\\mu}{\\sigma}\\sim N(0,1)$。查表：$P(|Z|<1)\\approx0.683$，$P(|Z|<2)\\approx0.954$，$P(|Z|<3)\\approx0.997$。即数据约 68% 在 $\\mu\\pm\\sigma$、95% 在 $\\mu\\pm2\\sigma$、99.7% 在 $\\mu\\pm3\\sigma$ 内。"))+
 exa(p("<strong>例：</strong>抛 10 次硬币，正面次数 $X\\sim B(10,0.5)$，$E(X)=5$，$D(X)=2.5$。")))
},
{"id":"e8s3-3","name":"样本均值与线性回归","tags":["def","thm","der","exa"],"brief":"样本均值方差、回归直线斜率与最小二乘。",
"body":wrap(
 defn("样本统计量",p("样本 $x_1,\\ldots,x_n$：<strong>均值</strong> $\\bar{x}=\\dfrac{1}{n}\\sum x_i$；<strong>方差</strong> $s^2=\\dfrac{1}{n}\\sum(x_i-\\bar{x})^2$（或 $\\dfrac{1}{n-1}$ 无偏估计）。"))+
 thm("回归方程",p("最小二乘法回归直线 $\\hat y=a+bx$，斜率与截距：")+
 fml("b=\\dfrac{\\sum(x_i-\\bar{x})(y_i-\\bar{y})}{\\sum(x_i-\\bar{x})^2},\\quad a=\\bar{y}-b\\bar{x}"))+
 der(p("<strong>最小二乘推导（代数法）：</strong>离差平方和 $Q=\\sum(y_i-a-bx_i)^2$ 是 $a$ 的开口向上二次函数，在对称轴处取最小值。把它按 $a$ 整理：$Q=na^2-2a\\sum(y_i-bx_i)+\\text{常数}$，对称轴 $a=\\dfrac{\\sum(y_i-bx_i)}{n}=\\bar y-b\\bar x$，故回归直线必过样本中心 $(\\bar x,\\bar y)$，得 $a=\\bar y-b\\bar x$。")+
 p("<strong>斜率推导：</strong>将 $a=\\bar y-b\\bar x$ 代回，$Q=\\sum[(y_i-\\bar y)-b(x_i-\\bar x)]^2$ 也是 $b$ 的开口向上二次函数，由对称轴位置解得 $b=\\dfrac{\\sum(x_i-\\bar x)(y_i-\\bar y)}{\\sum(x_i-\\bar x)^2}$。")+
 p("<strong>样本方差推导：</strong>$\\sum(x_i-\\bar x)^2=\\sum x_i^2-2\\bar x\\sum x_i+n\\bar x^2=\\sum x_i^2-n\\bar x^2$，故 $s^2=\\dfrac{1}{n}\\left(\\sum x_i^2-n\\bar x^2\\right)=\\dfrac{\\sum x_i^2}{n}-\\bar x^2$（简化计算公式）。")+
 p("<strong>相关系数推导：</strong>$r=\\dfrac{\\sum(x_i-\\bar x)(y_i-\\bar y)}{\\sqrt{\\sum(x_i-\\bar x)^2}\\sqrt{\\sum(y_i-\\bar y)^2}}\\in[-1,1]$，衡量线性相关程度。$|r|$ 越接近 $1$ 线性相关性越强，$r=0$ 表示无线性关系。"))+
 exa(p("<strong>例：</strong>三点 $(1,2),(2,4),(3,5)$，$\\bar x=2,\\bar y=\\dfrac{11}{3}$，$\\sum(x_i-\\bar x)(y_i-\\bar y)=(-1)(-\\dfrac{5}{3})+0+1\\cdot\\dfrac{4}{3}=3$，$\\sum(x_i-\\bar x)^2=2$，$b=1.5$，$a=\\dfrac{11}{3}-3=\\dfrac{2}{3}$，回归方程 $\\hat y=\\dfrac{2}{3}+1.5x$。")))
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
