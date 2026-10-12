# -*- coding: utf-8 -*-
"""Generate circuits.html with 10 chapters: 电路基础/等效电路/电路分析法/电路定理/储能元件与时域分析/相量法与正弦稳态分析/耦合电感/电路频率响应/非正弦周期电路/二端口网络."""
import json

FIG = {
"circuit_basic": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="70" width="56" height="20" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<text x="34" y="64" font-size="10" fill="#2563eb">电阻 R</text>
<line x1="86" y1="80" x2="196" y2="80" stroke="#475569" stroke-width="1.6"/>
<line x1="196" y1="80" x2="196" y2="126" stroke="#475569" stroke-width="1.6"/>
<line x1="30" y1="80" x2="30" y2="126" stroke="#475569" stroke-width="1.6"/>
<line x1="30" y1="126" x2="196" y2="126" stroke="#475569" stroke-width="1.6"/>
<line x1="106" y1="116" x2="106" y2="136" stroke="#c2410c" stroke-width="2"/>
<line x1="120" y1="110" x2="120" y2="142" stroke="#c2410c" stroke-width="2"/>
<text x="92" y="152" font-size="10" fill="#c2410c">电源 u_S</text>
<line x1="150" y1="80" x2="150" y2="64" stroke="#2563eb" stroke-width="1.5"/><polygon points="150,58 145,68 155,68" fill="#2563eb"/>
<text x="157" y="70" font-size="10" fill="#2563eb">i</text>
<circle cx="30" cy="80" r="2.5" fill="#475569"/><circle cx="196" cy="80" r="2.5" fill="#475569"/>
<text x="18" y="76" font-size="10" fill="#475569">a</text>
<text x="200" y="76" font-size="10" fill="#475569">b</text>
</svg>''',
"kcl": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="5" fill="#2563eb"/>
<text x="126" y="72" font-size="10" fill="#2563eb">节点</text>
<line x1="120" y1="80" x2="40" y2="80" stroke="#0d9488" stroke-width="1.8"/><polygon points="70,80 60,75 60,85" fill="#0d9488"/>
<line x1="120" y1="80" x2="196" y2="36" stroke="#0d9488" stroke-width="1.8"/><polygon points="168,53 158,52 162,61" fill="#0d9488"/>
<line x1="120" y1="80" x2="196" y2="124" stroke="#c2410c" stroke-width="1.8"/><polygon points="176,106 166,104 168,113" fill="#c2410c"/>
<text x="26" y="72" font-size="10" fill="#0d9488">i₁ 流出</text>
<text x="180" y="30" font-size="10" fill="#0d9488">i₂ 流出</text>
<text x="176" y="142" font-size="10" fill="#c2410c">i₃ 流入</text>
<text x="58" y="150" font-size="11" fill="#475569">Σ i = 0</text>
<circle cx="120" cy="80" r="18" fill="none" stroke="#93c5fd" stroke-width="1" stroke-dasharray="3 3"/>
</svg>''',
"kvl": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="40" width="180" height="84" rx="6" fill="none" stroke="#475569" stroke-width="1.6"/>
<rect x="82" y="33" width="46" height="14" fill="#dbeafe" stroke="#2563eb" stroke-width="1.4"/>
<text x="86" y="26" font-size="10" fill="#2563eb">R₁</text>
<line x1="176" y1="60" x2="176" y2="104" stroke="#c2410c" stroke-width="2"/>
<line x1="188" y1="56" x2="188" y2="108" stroke="#c2410c" stroke-width="2"/>
<text x="176" y="124" font-size="10" fill="#c2410c">u_S</text>
<rect x="82" y="117" width="46" height="14" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.4"/>
<text x="86" y="146" font-size="10" fill="#7c3aed">R₂</text>
<line x1="60" y1="40" x2="60" y2="124" stroke="#475569" stroke-width="1.6"/>
<text x="40" y="88" font-size="10" fill="#475569">绕行</text>
<line x1="42" y1="70" x2="42" y2="70" stroke="#0d9488"/>
<path d="M 40 60 A 30 30 0 1 1 40 100" fill="none" stroke="#0d9488" stroke-width="1.4"/>
<polygon points="40,104 34,94 46,94" fill="#0d9488"/>
<text x="96" y="152" font-size="11" fill="#475569">Σ u = 0</text>
</svg>''',
"series_parallel": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<text x="20" y="20" font-size="11" fill="#7c3aed">串联</text>
<line x1="20" y1="44" x2="46" y2="44" stroke="#475569" stroke-width="1.5"/>
<rect x="46" y="36" width="34" height="16" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.4"/>
<rect x="94" y="36" width="34" height="16" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.4"/>
<line x1="80" y1="44" x2="94" y2="44" stroke="#475569" stroke-width="1.5"/>
<line x1="128" y1="44" x2="156" y2="44" stroke="#475569" stroke-width="1.5"/>
<line x1="156" y1="44" x2="156" y2="66" stroke="#475569" stroke-width="1.5"/>
<line x1="20" y1="44" x2="20" y2="66" stroke="#475569" stroke-width="1.5"/>
<line x1="20" y1="66" x2="156" y2="66" stroke="#475569" stroke-width="1.5"/>
<text x="52" y="30" font-size="9" fill="#7c3aed">R₁</text><text x="100" y="30" font-size="9" fill="#7c3aed">R₂</text>
<text x="60" y="82" font-size="10" fill="#475569">R = R₁ + R₂</text>
<text x="20" y="106" font-size="11" fill="#0891b2">并联</text>
<line x1="20" y1="130" x2="46" y2="130" stroke="#475569" stroke-width="1.5"/>
<line x1="46" y1="112" x2="46" y2="148" stroke="#475569" stroke-width="1.5"/>
<rect x="46" y="112" width="12" height="36" fill="#cffafe" stroke="#0891b2" stroke-width="1.4"/>
<line x1="58" y1="130" x2="96" y2="130" stroke="#475569" stroke-width="1.5"/>
<line x1="96" y1="112" x2="96" y2="148" stroke="#475569" stroke-width="1.5"/>
<rect x="96" y="112" width="12" height="36" fill="#cffafe" stroke="#0891b2" stroke-width="1.4"/>
<line x1="108" y1="130" x2="158" y2="130" stroke="#475569" stroke-width="1.5"/>
<text x="130" y="128" font-size="10" fill="#475569">1/R = 1/R₁ + 1/R₂</text>
</svg>''',
"voltage_divider": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="60" y1="30" x2="60" y2="50" stroke="#475569" stroke-width="1.6"/>
<rect x="46" y="50" width="28" height="18" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.4"/>
<line x1="60" y1="68" x2="60" y2="86" stroke="#475569" stroke-width="1.6"/>
<circle cx="60" cy="86" r="3" fill="#7c3aed"/>
<line x1="60" y1="86" x2="130" y2="86" stroke="#7c3aed" stroke-width="1.4"/>
<text x="132" y="88" font-size="10" fill="#7c3aed">u₂</text>
<line x1="60" y1="86" x2="60" y2="104" stroke="#475569" stroke-width="1.6"/>
<rect x="46" y="104" width="28" height="18" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.4"/>
<line x1="60" y1="122" x2="60" y2="138" stroke="#475569" stroke-width="1.6"/>
<line x1="30" y1="30" x2="30" y2="138" stroke="#475569" stroke-width="1.6"/>
<line x1="30" y1="30" x2="60" y2="30" stroke="#475569" stroke-width="1.6"/>
<line x1="30" y1="138" x2="60" y2="138" stroke="#475569" stroke-width="1.6"/>
<text x="76" y="62" font-size="10" fill="#7c3aed">R₁</text>
<text x="76" y="116" font-size="10" fill="#7c3aed">R₂</text>
<text x="14" y="86" font-size="10" fill="#475569">u₁</text>
<text x="86" y="44" font-size="10" fill="#475569">u₂ = R₂/(R₁+R₂)·u₁</text>
</svg>''',
"delta_wye": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<polygon points="40,40 100,40 70,100" fill="none" stroke="#7c3aed" stroke-width="1.6"/>
<circle cx="40" cy="40" r="2.5" fill="#7c3aed"/><circle cx="100" cy="40" r="2.5" fill="#7c3aed"/><circle cx="70" cy="100" r="2.5" fill="#7c3aed"/>
<text x="30" y="34" font-size="9" fill="#7c3aed">a</text><text x="102" y="34" font-size="9" fill="#7c3aed">b</text><text x="72" y="114" font-size="9" fill="#7c3aed">c</text>
<text x="60" y="30" font-size="9" fill="#7c3aed">Δ</text>
<line x1="150" y1="70" x2="190" y2="34" stroke="#0d9488" stroke-width="1.6"/>
<line x1="150" y1="70" x2="190" y2="106" stroke="#0d9488" stroke-width="1.6"/>
<line x1="150" y1="70" x2="150" y2="120" stroke="#0d9488" stroke-width="1.6"/>
<circle cx="150" cy="70" r="3" fill="#0d9488"/>
<circle cx="190" cy="34" r="2.5" fill="#0d9488"/><circle cx="190" cy="106" r="2.5" fill="#0d9488"/><circle cx="150" cy="120" r="2.5" fill="#0d9488"/>
<text x="196" y="34" font-size="9" fill="#0d9488">a</text><text x="196" y="110" font-size="9" fill="#0d9488">b</text><text x="136" y="132" font-size="9" fill="#0d9488">c</text>
<text x="162" y="66" font-size="9" fill="#0d9488">Y</text>
<text x="14" y="146" font-size="10" fill="#475569">Δ ⇄ Y 等效变换</text>
</svg>''',
"source_transform": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="20" cy="50" r="3" fill="#7c3aed"/>
<line x1="20" y1="50" x2="20" y2="30" stroke="#475569" stroke-width="1.5"/>
<line x1="14" y1="30" x2="26" y2="30" stroke="#c2410c" stroke-width="2"/>
<line x1="16" y1="24" x2="24" y2="24" stroke="#c2410c" stroke-width="2"/>
<line x1="20" y1="50" x2="60" y2="50" stroke="#475569" stroke-width="1.5"/>
<rect x="60" y="42" width="30" height="16" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.4"/>
<line x1="90" y1="50" x2="120" y2="50" stroke="#475569" stroke-width="1.5"/>
<text x="14" y="16" font-size="9" fill="#c2410c">u_S</text><text x="66" y="72" font-size="9" fill="#7c3aed">R_S</text>
<line x1="100" y1="100" x2="128" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 3"/>
<polygon points="134,100 124,95 124,105" fill="#94a3b8"/>
<circle cx="140" cy="40" r="3" fill="#0891b2"/>
<line x1="140" y1="40" x2="140" y2="30" stroke="#475569" stroke-width="1.5"/>
<circle cx="140" cy="40" r="8" fill="none" stroke="#0891b2" stroke-width="1.4"/>
<line x1="140" y1="40" x2="180" y2="40" stroke="#475569" stroke-width="1.5"/>
<rect x="180" y="32" width="30" height="16" fill="#cffafe" stroke="#0891b2" stroke-width="1.4"/>
<line x1="210" y1="40" x2="228" y2="40" stroke="#475569" stroke-width="1.5"/>
<line x1="140" y1="72" x2="228" y2="72" stroke="#475569" stroke-width="1.5"/>
<line x1="140" y1="40" x2="140" y2="72" stroke="#475569" stroke-width="1.5"/>
<line x1="228" y1="40" x2="228" y2="72" stroke="#475569" stroke-width="1.5"/>
<text x="130" y="26" font-size="9" fill="#0891b2">i_S</text><text x="186" y="64" font-size="9" fill="#0891b2">R_S</text>
<text x="150" y="92" font-size="10" fill="#475569">u_S = R_S i_S</text>
</svg>''',
"mesh": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="40" width="150" height="80" fill="none" stroke="#475569" stroke-width="1.6"/>
<line x1="115" y1="40" x2="115" y2="120" stroke="#475569" stroke-width="1.6"/>
<rect x="66" y="33" width="34" height="14" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.4"/>
<rect x="130" y="33" width="34" height="14" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.4"/>
<rect x="66" y="113" width="34" height="14" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.4"/>
<rect x="130" y="113" width="34" height="14" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.4"/>
<path d="M 90 66 A 24 24 0 1 1 90 90" fill="none" stroke="#0d9488" stroke-width="1.4"/>
<polygon points="90,94 84,84 96,84" fill="#0d9488"/>
<text x="72" y="84" font-size="10" fill="#0d9488">i_m1</text>
<path d="M 150 66 A 24 24 0 1 1 150 90" fill="none" stroke="#c2410c" stroke-width="1.4"/>
<polygon points="150,94 144,84 156,84" fill="#c2410c"/>
<text x="136" y="84" font-size="10" fill="#c2410c">i_m2</text>
<text x="40" y="150" font-size="10" fill="#475569">网孔电流法：按独立网孔列 KVL</text>
</svg>''',
"nodal": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="120" y1="24" x2="120" y2="128" stroke="#475569" stroke-width="1.8"/>
<line x1="40" y1="90" x2="120" y2="90" stroke="#475569" stroke-width="1.6"/>
<line x1="120" y1="44" x2="200" y2="44" stroke="#475569" stroke-width="1.6"/>
<line x1="120" y1="128" x2="40" y2="128" stroke="#475569" stroke-width="1.6"/>
<circle cx="40" cy="90" r="3" fill="#0d9488"/><text x="20" y="86" font-size="10" fill="#0d9488">节点1</text>
<circle cx="120" cy="90" r="3.5" fill="#c2410c"/><text x="100" y="84" font-size="10" fill="#c2410c">节点 u_n</text>
<line x1="120" y1="128" x2="200" y2="128" stroke="#475569" stroke-width="1.6"/>
<line x1="200" y1="44" x2="200" y2="128" stroke="#475569" stroke-width="1.6"/>
<circle cx="200" cy="128" r="3" fill="#0d9488"/><text x="206" y="132" font-size="10" fill="#0d9488">参考地</text>
<circle cx="40" cy="128" r="3" fill="#0d9488"/>
<text x="46" y="24" font-size="10" fill="#475569">节点电压法：以节点电压为未知量列 KCL</text>
</svg>''',
"superposition": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="70" y="46" width="100" height="20" fill="#ffedd5" stroke="#c2410c" stroke-width="1.4"/>
<text x="96" y="40" font-size="10" fill="#c2410c">线性电路</text>
<line x1="70" y1="56" x2="34" y2="56" stroke="#475569" stroke-width="1.5"/>
<line x1="170" y1="56" x2="206" y2="56" stroke="#475569" stroke-width="1.5"/>
<line x1="34" y1="56" x2="34" y2="128" stroke="#475569" stroke-width="1.5"/>
<line x1="206" y1="56" x2="206" y2="128" stroke="#475569" stroke-width="1.5"/>
<line x1="34" y1="128" x2="206" y2="128" stroke="#475569" stroke-width="1.5"/>
<line x1="80" y1="118" x2="80" y2="138" stroke="#c2410c" stroke-width="2"/>
<line x1="94" y1="114" x2="94" y2="142" stroke="#c2410c" stroke-width="2"/>
<text x="60" y="152" font-size="10" fill="#c2410c">电源1</text>
<line x1="150" y1="118" x2="150" y2="138" stroke="#0891b2" stroke-width="2"/>
<line x1="164" y1="114" x2="164" y2="142" stroke="#0891b2" stroke-width="2"/>
<text x="136" y="152" font-size="10" fill="#0891b2">电源2</text>
<text x="96" y="20" font-size="10" fill="#475569">总响应 = 各电源单独作用响应之和</text>
</svg>''',
"thevenin": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="40" width="90" height="70" fill="#fef3c7" stroke="#c2410c" stroke-width="1.5"/>
<text x="44" y="80" font-size="10" fill="#c2410c">含源线性网络</text>
<line x1="120" y1="44" x2="190" y2="44" stroke="#475569" stroke-width="1.6"/>
<line x1="120" y1="106" x2="190" y2="106" stroke="#475569" stroke-width="1.6"/>
<circle cx="120" cy="44" r="3" fill="#c2410c"/><text x="110" y="38" font-size="9" fill="#c2410c">a</text>
<circle cx="120" cy="106" r="3" fill="#c2410c"/><text x="110" y="120" font-size="9" fill="#c2410c">b</text>
<line x1="156" y1="44" x2="156" y2="68" stroke="#475569" stroke-width="1.6"/>
<line x1="148" y1="68" x2="164" y2="68" stroke="#0891b2" stroke-width="2"/>
<line x1="152" y1="74" x2="160" y2="74" stroke="#0891b2" stroke-width="2"/>
<line x1="156" y1="74" x2="156" y2="106" stroke="#475569" stroke-width="1.6"/>
<text x="162" y="70" font-size="10" fill="#0891b2">u_oc</text>
<text x="150" y="128" font-size="10" fill="#475569">戴维南：u_oc 串 R_eq</text>
</svg>''',
"norton": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="40" width="80" height="70" fill="#fef3c7" stroke="#c2410c" stroke-width="1.5"/>
<text x="40" y="80" font-size="10" fill="#c2410c">含源网络</text>
<line x1="110" y1="44" x2="180" y2="44" stroke="#475569" stroke-width="1.6"/>
<line x1="180" y1="44" x2="180" y2="70" stroke="#475569" stroke-width="1.6"/>
<circle cx="180" cy="78" r="9" fill="none" stroke="#0891b2" stroke-width="1.5"/>
<line x1="180" y1="70" x2="180" y2="62" stroke="#475569" stroke-width="1.5"/>
<line x1="180" y1="87" x2="180" y2="106" stroke="#475569" stroke-width="1.6"/>
<line x1="110" y1="106" x2="180" y2="106" stroke="#475569" stroke-width="1.6"/>
<line x1="196" y1="44" x2="196" y2="106" stroke="#475569" stroke-width="1.6"/>
<line x1="180" y1="44" x2="196" y2="44" stroke="#475569" stroke-width="1.6"/>
<line x1="180" y1="106" x2="196" y2="106" stroke="#475569" stroke-width="1.6"/>
<rect x="190" y="64" width="12" height="30" fill="#cffafe" stroke="#0891b2" stroke-width="1.4"/>
<text x="150" y="36" font-size="10" fill="#0891b2">i_sc</text>
<text x="206" y="84" font-size="10" fill="#0891b2">R_eq</text>
<text x="30" y="128" font-size="10" fill="#475569">诺顿：i_sc 并 R_eq</text>
</svg>''',
"max_power": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="128" stroke="#475569" stroke-width="1.2"/>
<polygon points="34,12 30,22 38,22" fill="#475569"/>
<line x1="34" y1="128" x2="220" y2="128" stroke="#475569" stroke-width="1.2"/>
<polygon points="226,128 216,124 216,132" fill="#475569"/>
<text x="14" y="26" font-size="10" fill="#475569">P</text>
<text x="200" y="144" font-size="10" fill="#475569">R_L</text>
<path d="M 38 126 C 70 60 100 40 122 38 C 144 40 178 60 214 126" fill="none" stroke="#c2410c" stroke-width="2"/>
<line x1="122" y1="38" x2="122" y2="128" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<circle cx="122" cy="38" r="3" fill="#c2410c"/>
<text x="96" y="30" font-size="10" fill="#c2410c">P_max</text>
<text x="112" y="146" font-size="10" fill="#c2410c">R_eq</text>
</svg>''',
"capacitor": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="40" y1="80" x2="106" y2="80" stroke="#475569" stroke-width="1.6"/>
<line x1="106" y1="52" x2="106" y2="108" stroke="#be185d" stroke-width="2.4"/>
<line x1="118" y1="52" x2="118" y2="108" stroke="#be185d" stroke-width="2.4"/>
<line x1="118" y1="80" x2="184" y2="80" stroke="#475569" stroke-width="1.6"/>
<circle cx="40" cy="80" r="3" fill="#be185d"/><circle cx="184" cy="80" r="3" fill="#be185d"/>
<text x="44" y="72" font-size="10" fill="#475569">+q</text><text x="160" y="72" font-size="10" fill="#475569">−q</text>
<line x1="150" y1="80" x2="150" y2="62" stroke="#be185d" stroke-width="1.5"/><polygon points="150,56 145,66 155,66" fill="#be185d"/>
<text x="156" y="66" font-size="10" fill="#be185d">i</text>
<text x="70" y="132" font-size="10" fill="#be185d">i = C du/dt</text>
<text x="70" y="148" font-size="10" fill="#be185d">w = ½Cu²</text>
</svg>''',
"inductor": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="40" y1="80" x2="70" y2="80" stroke="#475569" stroke-width="1.6"/>
<path d="M 70 80 Q 78 62 86 80 Q 94 62 102 80 Q 110 62 118 80 Q 126 62 134 80 Q 142 62 150 80" fill="none" stroke="#be185d" stroke-width="1.8"/>
<line x1="150" y1="80" x2="184" y2="80" stroke="#475569" stroke-width="1.6"/>
<circle cx="40" cy="80" r="3" fill="#be185d"/><circle cx="184" cy="80" r="3" fill="#be185d"/>
<line x1="110" y1="80" x2="110" y2="58" stroke="#be185d" stroke-width="1.5"/><polygon points="110,52 105,62 115,62" fill="#be185d"/>
<text x="116" y="62" font-size="10" fill="#be185d">i</text>
<text x="66" y="132" font-size="10" fill="#be185d">u = L di/dt</text>
<text x="66" y="148" font-size="10" fill="#be185d">w = ½Li²</text>
</svg>''',
"rc_charge": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="128" stroke="#475569" stroke-width="1.2"/>
<polygon points="34,12 30,22 38,22" fill="#475569"/>
<line x1="34" y1="128" x2="222" y2="128" stroke="#475569" stroke-width="1.2"/>
<polygon points="228,128 218,124 218,132" fill="#475569"/>
<text x="14" y="26" font-size="10" fill="#475569">u_C</text>
<text x="196" y="144" font-size="10" fill="#475569">t</text>
<line x1="34" y1="34" x2="218" y2="34" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<text x="12" y="38" font-size="10" fill="#94a3b8">U</text>
<path d="M 34 128 C 80 70 110 46 150 38 C 180 34 200 34 216 34" fill="none" stroke="#be185d" stroke-width="2"/>
<line x1="86" y1="34" x2="86" y2="128" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<circle cx="86" cy="78" r="2.5" fill="#be185d"/>
<text x="90" y="74" font-size="10" fill="#be185d">0.632U</text>
<text x="70" y="146" font-size="10" fill="#be185d">τ</text>
<text x="118" y="60" font-size="10" fill="#be185d">u_C = U(1−e^(−t/τ))</text>
</svg>''',
"rl_decay": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="128" stroke="#475569" stroke-width="1.2"/>
<polygon points="34,12 30,22 38,22" fill="#475569"/>
<line x1="34" y1="128" x2="222" y2="128" stroke="#475569" stroke-width="1.2"/>
<polygon points="228,128 218,124 218,132" fill="#475569"/>
<text x="14" y="26" font-size="10" fill="#475569">i_L</text>
<text x="200" y="144" font-size="10" fill="#475569">t</text>
<line x1="34" y1="34" x2="60" y2="34" stroke="#be185d" stroke-width="2"/>
<path d="M 60 34 C 90 34 96 108 140 122 C 176 130 200 128 216 128" fill="none" stroke="#be185d" stroke-width="2"/>
<line x1="86" y1="34" x2="86" y2="128" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<circle cx="86" cy="70" r="2.5" fill="#be185d"/>
<text x="90" y="66" font-size="10" fill="#be185d">0.368I₀</text>
<text x="70" y="146" font-size="10" fill="#be185d">τ = L/R</text>
<text x="118" y="60" font-size="10" fill="#be185d">i_L = I₀ e^(−t/τ)</text>
</svg>''',
"rlc_series": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="60" y1="40" x2="60" y2="60" stroke="#475569" stroke-width="1.6"/>
<path d="M 60 60 Q 68 46 76 60 Q 84 46 92 60 Q 100 46 108 60" fill="none" stroke="#be185d" stroke-width="1.8"/>
<line x1="108" y1="60" x2="128" y2="60" stroke="#475569" stroke-width="1.6"/>
<rect x="128" y="52" width="30" height="16" fill="#fce7f3" stroke="#be185d" stroke-width="1.4"/>
<line x1="158" y1="60" x2="182" y2="60" stroke="#475569" stroke-width="1.6"/>
<line x1="60" y1="40" x2="182" y2="40" stroke="#475569" stroke-width="1.6"/>
<line x1="182" y1="40" x2="182" y2="60" stroke="#475569" stroke-width="1.6"/>
<line x1="60" y1="60" x2="60" y2="120" stroke="#475569" stroke-width="1.6"/>
<line x1="182" y1="60" x2="182" y2="120" stroke="#475569" stroke-width="1.6"/>
<line x1="60" y1="120" x2="182" y2="120" stroke="#475569" stroke-width="1.6"/>
<line x1="106" y1="112" x2="106" y2="130" stroke="#c2410c" stroke-width="2"/>
<line x1="120" y1="108" x2="120" y2="134" stroke="#c2410c" stroke-width="2"/>
<text x="70" y="52" font-size="9" fill="#be185d">L</text>
<text x="136" y="48" font-size="9" fill="#be185d">R</text>
<text x="86" y="152" font-size="10" fill="#c2410c">u_S 串联 RLC</text>
</svg>''',
"damping": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="18" x2="30" y2="128" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="80" x2="222" y2="80" stroke="#475569" stroke-width="1.2"/>
<text x="12" y="26" font-size="10" fill="#475569">u_C</text>
<text x="200" y="96" font-size="10" fill="#475569">t</text>
<path d="M 30 80 C 70 34 110 32 150 62 C 180 82 200 78 220 80" fill="none" stroke="#c2410c" stroke-width="2"/>
<path d="M 30 80 C 60 40 90 40 120 62 C 150 82 180 80 220 80" fill="none" stroke="#0d9488" stroke-width="1.8"/>
<path d="M 30 80 C 40 24 60 22 70 80 C 78 128 96 130 118 80 C 138 34 158 34 178 80 C 196 122 210 118 220 80" fill="none" stroke="#be185d" stroke-width="1.6"/>
<text x="150" y="58" font-size="9" fill="#c2410c">过阻尼</text>
<text x="150" y="40" font-size="9" fill="#0d9488">临界</text>
<text x="128" y="132" font-size="9" fill="#be185d">欠阻尼振荡</text>
</svg>''',
"phasor": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="118" cy="84" r="52" fill="none" stroke="#cbd5e1" stroke-width="1"/>
<line x1="118" y1="24" x2="118" y2="146" stroke="#cbd5e1" stroke-width="1"/>
<line x1="56" y1="84" x2="180" y2="84" stroke="#cbd5e1" stroke-width="1"/>
<line x1="118" y1="84" x2="164" y2="46" stroke="#0891b2" stroke-width="2.2"/>
<polygon points="164,46 154,48 158,56" fill="#0891b2"/>
<text x="166" y="44" font-size="10" fill="#0891b2">U̇</text>
<path d="M 138 84 A 20 20 0 0 0 132 70" fill="none" stroke="#c2410c" stroke-width="1.4"/>
<text x="140" y="76" font-size="10" fill="#c2410c">φ</text>
<text x="30" y="150" font-size="10" fill="#475569">旋转相量与正弦量一一对应</text>
</svg>''',
"impedance_triangle": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="50" y1="120" x2="180" y2="120" stroke="#475569" stroke-width="1.6"/>
<polygon points="186,120 176,116 176,124" fill="#475569"/>
<line x1="180" y1="120" x2="180" y2="50" stroke="#0891b2" stroke-width="1.6"/>
<polygon points="180,44 176,54 184,54" fill="#0891b2"/>
<line x1="50" y1="120" x2="180" y2="50" stroke="#c2410c" stroke-width="2"/>
<line x1="180" y1="120" x2="164" y2="120" stroke="#94a3b8" stroke-width="1"/>
<line x1="164" y1="120" x2="164" y2="110" stroke="#94a3b8" stroke-width="1"/>
<text x="112" y="138" font-size="10" fill="#475569">R</text>
<text x="186" y="86" font-size="10" fill="#0891b2">X</text>
<text x="96" y="80" font-size="10" fill="#c2410c">|Z|</text>
<path d="M 78 120 A 28 28 0 0 0 72 106" fill="none" stroke="#7e22ce" stroke-width="1.4"/>
<text x="74" y="112" font-size="10" fill="#7e22ce">φ</text>
<text x="30" y="26" font-size="10" fill="#475569">Z = R + jX，|Z| = √(R²+X²)</text>
</svg>''',
"power_triangle": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="40" y1="120" x2="190" y2="120" stroke="#475569" stroke-width="1.6"/>
<line x1="190" y1="120" x2="190" y2="46" stroke="#0891b2" stroke-width="1.6"/>
<line x1="40" y1="120" x2="190" y2="46" stroke="#c2410c" stroke-width="2"/>
<text x="104" y="136" font-size="10" fill="#0d9488">P = UIcosφ</text>
<text x="196" y="86" font-size="10" fill="#0891b2">Q</text>
<text x="96" y="74" font-size="10" fill="#c2410c">S = UI</text>
<text x="46" y="66" font-size="10" fill="#7e22ce">功率因数 cosφ</text>
</svg>''',
"resonance_curve": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="128" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="128" x2="222" y2="128" stroke="#475569" stroke-width="1.2"/>
<text x="14" y="26" font-size="10" fill="#475569">I</text>
<text x="196" y="144" font-size="10" fill="#475569">ω</text>
<path d="M 40 124 C 80 120 100 60 120 40 C 140 60 160 118 214 124" fill="none" stroke="#0891b2" stroke-width="2"/>
<line x1="120" y1="40" x2="120" y2="128" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="110" y="146" font-size="10" fill="#0891b2">ω₀</text>
<text x="64" y="152" font-size="10" fill="#0d9488">ω₀ = 1/√(LC)</text>
<text x="126" y="60" font-size="10" fill="#c2410c">谐振峰</text>
</svg>''',
"mutual_inductance": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 40 60 Q 48 44 56 60 Q 64 44 72 60 Q 80 44 88 60" fill="none" stroke="#4f46e5" stroke-width="1.8"/>
<path d="M 150 60 Q 158 44 166 60 Q 174 44 182 60 Q 190 44 198 60" fill="none" stroke="#4f46e5" stroke-width="1.8"/>
<line x1="20" y1="60" x2="40" y2="60" stroke="#475569" stroke-width="1.5"/>
<line x1="88" y1="60" x2="108" y2="60" stroke="#475569" stroke-width="1.5"/>
<line x1="132" y1="60" x2="150" y2="60" stroke="#475569" stroke-width="1.5"/>
<line x1="198" y1="60" x2="220" y2="60" stroke="#475569" stroke-width="1.5"/>
<circle cx="40" cy="46" r="2.5" fill="#c2410c"/><text x="32" y="40" font-size="10" fill="#c2410c">•</text>
<circle cx="198" cy="46" r="2.5" fill="#c2410c"/><text x="200" y="40" font-size="10" fill="#c2410c">•</text>
<line x1="120" y1="44" x2="120" y2="76" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="86" y="118" font-size="10" fill="#4f46e5">同名端（•）与互感 M</text>
<text x="40" y="140" font-size="10" fill="#475569">u₂ = ±M di₁/dt</text>
</svg>''',
"transformer": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="112" y="40" width="16" height="80" fill="#e0e7ff" stroke="#4f46e5" stroke-width="1.4"/>
<path d="M 60 44 Q 68 30 76 44 Q 84 30 92 44 Q 100 30 108 44" fill="none" stroke="#4f46e5" stroke-width="1.8"/>
<path d="M 132 44 Q 140 30 148 44 Q 156 30 164 44 Q 172 30 180 44" fill="none" stroke="#4f46e5" stroke-width="1.8"/>
<line x1="60" y1="44" x2="60" y2="110" stroke="#475569" stroke-width="1.5"/>
<line x1="180" y1="44" x2="180" y2="110" stroke="#475569" stroke-width="1.5"/>
<line x1="40" y1="60" x2="60" y2="60" stroke="#475569" stroke-width="1.5"/>
<line x1="180" y1="60" x2="200" y2="60" stroke="#475569" stroke-width="1.5"/>
<line x1="40" y1="110" x2="200" y2="110" stroke="#475569" stroke-width="1.5"/>
<text x="26" y="56" font-size="10" fill="#4f46e5">u₁</text>
<text x="202" y="56" font-size="10" fill="#4f46e5">u₂</text>
<text x="118" y="30" font-size="10" fill="#4f46e5">铁芯</text>
<text x="60" y="140" font-size="10" fill="#475569">u₁/u₂ = n（匝数比）</text>
</svg>''',
"bode": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="126" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="126" x2="222" y2="126" stroke="#475569" stroke-width="1.2"/>
<text x="10" y="26" font-size="10" fill="#475569">dB</text>
<text x="192" y="142" font-size="10" fill="#475569">lg ω</text>
<line x1="34" y1="44" x2="108" y2="44" stroke="#059669" stroke-width="2"/>
<line x1="108" y1="44" x2="200" y2="112" stroke="#059669" stroke-width="2"/>
<line x1="108" y1="20" x2="108" y2="126" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<circle cx="108" cy="44" r="2.5" fill="#c2410c"/>
<text x="114" y="40" font-size="10" fill="#c2410c">−3 dB</text>
<text x="112" y="140" font-size="10" fill="#059669">ω_c</text>
<text x="130" y="96" font-size="10" fill="#059669">−20 dB/十倍频</text>
</svg>''',
"filter_lp": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="40" y1="60" x2="70" y2="60" stroke="#475569" stroke-width="1.6"/>
<rect x="70" y="52" width="34" height="16" fill="#d1fae5" stroke="#059669" stroke-width="1.4"/>
<line x1="104" y1="60" x2="140" y2="60" stroke="#475569" stroke-width="1.6"/>
<line x1="140" y1="60" x2="140" y2="84" stroke="#475569" stroke-width="1.6"/>
<line x1="126" y1="84" x2="154" y2="84" stroke="#059669" stroke-width="2.4"/>
<line x1="126" y1="92" x2="154" y2="92" stroke="#059669" stroke-width="2.4"/>
<line x1="140" y1="92" x2="140" y2="116" stroke="#475569" stroke-width="1.6"/>
<line x1="40" y1="60" x2="40" y2="116" stroke="#475569" stroke-width="1.6"/>
<line x1="40" y1="116" x2="140" y2="116" stroke="#475569" stroke-width="1.6"/>
<line x1="104" y1="60" x2="104" y2="46" stroke="#475569" stroke-width="1.6"/>
<circle cx="104" cy="60" r="3" fill="#059669"/>
<line x1="160" y1="40" x2="214" y2="40" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 164 76 L 196 76 Q 214 68 218 42" fill="none" stroke="#059669" stroke-width="2"/>
<text x="46" y="52" font-size="9" fill="#059669">R</text>
<text x="144" y="80" font-size="9" fill="#059669">C</text>
<text x="150" y="30" font-size="10" fill="#475569">低通幅频</text>
</svg>''',
"two_port": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="70" y="44" width="100" height="72" rx="8" fill="#f3e8ff" stroke="#7e22ce" stroke-width="1.6"/>
<text x="92" y="84" font-size="11" fill="#7e22ce">二端口网络</text>
<line x1="30" y1="60" x2="70" y2="60" stroke="#475569" stroke-width="1.6"/>
<line x1="30" y1="100" x2="70" y2="100" stroke="#475569" stroke-width="1.6"/>
<line x1="170" y1="60" x2="210" y2="60" stroke="#475569" stroke-width="1.6"/>
<line x1="170" y1="100" x2="210" y2="100" stroke="#475569" stroke-width="1.6"/>
<line x1="30" y1="60" x2="30" y2="46" stroke="#7e22ce" stroke-width="1.5"/><polygon points="30,40 25,50 35,50" fill="#7e22ce"/>
<text x="34" y="52" font-size="10" fill="#7e22ce">i₁</text>
<text x="14" y="72" font-size="10" fill="#7e22ce">u₁</text>
<line x1="210" y1="60" x2="210" y2="46" stroke="#7e22ce" stroke-width="1.5"/><polygon points="210,40 205,50 215,50" fill="#7e22ce"/>
<text x="214" y="52" font-size="10" fill="#7e22ce">i₂</text>
<text x="192" y="72" font-size="10" fill="#7e22ce">u₂</text>
<line x1="30" y1="100" x2="64" y2="100" stroke="#475569" stroke-width="1.6"/>
<line x1="176" y1="100" x2="210" y2="100" stroke="#475569" stroke-width="1.6"/>
</svg>''',
"fourier_wave": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="14" y1="80" x2="228" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 20 80 L 20 44 L 60 44 L 60 80 L 60 116 L 100 116 L 100 44 L 140 44 L 140 80 L 140 116 L 180 116 L 180 44 L 220 44" fill="none" stroke="#b45309" stroke-width="1.8"/>
<path d="M 20 80 Q 40 52 60 80 T 100 80 Q 120 108 140 80 Q 160 52 180 80 T 220 80" fill="none" stroke="#0d9488" stroke-width="1.4" stroke-dasharray="4 3"/>
<text x="150" y="34" font-size="10" fill="#b45309">方波</text>
<text x="150" y="132" font-size="10" fill="#0d9488">基波 + 奇次谐波</text>
<text x="24" y="150" font-size="10" fill="#475569">傅里叶分解</text>
</svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

CORE_FORMULAS = [
    ("欧姆定律", "u = R\\,i", "线性电阻两端电压与电流成正比"),
    ("电导", "g = \\frac{1}{R}", "电阻的倒数，单位西门子 S"),
    ("瞬时功率", "p = u\\,i", "元件吸收的瞬时功率"),
    ("电阻功率", "p = i^2 R = \\frac{u^2}{R}", "电阻消耗的功率总为正"),
    ("能量", "W = \\int_{t_1}^{t_2} p\\,dt", "功率对时间的积分即能量"),
    ("基尔霍夫电流定律", "\\sum_{k} i_k = 0", "任一节点电流代数和为零"),
    ("基尔霍夫电压定律", "\\sum_{k} u_k = 0", "任一回路电压降代数和为零"),
    ("电阻串联等效", "R_{eq} = \\sum_{k} R_k", "串联电阻之和"),
    ("串联分压", "u_k = \\frac{R_k}{\\sum R} u", "分压正比于自身电阻"),
    ("电阻并联等效", "\\frac{1}{R_{eq}} = \\sum_{k} \\frac{1}{R_k}", "并联电阻倒数之和的倒数"),
    ("并联分流", "i_k = \\frac{G_k}{\\sum G} i", "分流正比于自身电导"),
    ("两电阻并联", "R_{eq} = \\frac{R_1 R_2}{R_1 + R_2}", "两电阻并联的常用简化式"),
    ("Δ→Y 电阻", "R_a = \\frac{R_{ab}R_{ca}}{R_{ab}+R_{bc}+R_{ca}}", "三角形化为星形"),
    ("Y→Δ 电阻", "R_{ab} = \\frac{R_aR_b+R_bR_c+R_cR_a}{R_c}", "星形化为三角形"),
    ("平衡电桥", "R_1 R_4 = R_2 R_3", "电桥平衡时桥臂无电流"),
    ("电压源串联合并", "u_{eq} = \\sum_{k} u_{S_k}", "极性一致时相加"),
    ("电流源并联合并", "i_{eq} = \\sum_{k} i_{S_k}", "方向一致时相加"),
    ("电源等效变换", "u_S = R_S\\,i_S", "有伴电压源与有伴电流源互换"),
    ("受控源关系", "y = \\mu\\,x", "受控源的控制量—被控量关系"),
    ("支路电流法", "\\sum_{k} R_{jk} i_k = \\sum u_{S_j}", "以支路电流为未知量列 KVL"),
    ("网孔电流法", "R_{11}i_{m1}+R_{12}i_{m2} = u_{S1}", "网孔自阻、互阻与网孔电流方程"),
    ("节点电压法", "\\sum_{j} G_{kj} u_{n j} = \\sum i_{Sk}", "节点电导矩阵方程"),
    ("叠加定理", "y = \\sum_{k} y_k", "线性电路响应为各独立源单独作用之和"),
    ("齐性定理", "y\\big|_{kx} = k\\,y\\big|_{x}", "激励放大 k 倍响应亦放大 k 倍"),
    ("替代定理", "u = u_s\\ (\\text{替代后})", "已知支路可用等效独立源替代"),
    ("戴维南等效电压", "u_{oc} = u\\big|_{RL=\\infty}", "端口开路电压"),
    ("戴维南等效电阻", "R_{eq} = \\frac{u_{oc}}{i_{sc}}", "开路电压比短路电流"),
    ("诺顿等效电流", "i_{sc} = \\frac{u_{oc}}{R_{eq}}", "端口短路电流"),
    ("最大功率传输条件", "R_L = R_{eq}", "负载等于电源内阻时获最大功率"),
    ("最大功率", "P_{max} = \\frac{u_{oc}^2}{4R_{eq}}", "匹配时的最大输出功率"),
    ("互易定理", "\\frac{u_2}{i_1} = \\frac{u_1}{i_2}", "线性无源网络的互易关系"),
    ("对偶原理", "R \\leftrightarrow G,\\ u \\leftrightarrow i", "电路元件与变量的对偶替换"),
    ("电容电荷", "q = C\\,u", "电荷与端电压成正比"),
    ("电容伏安关系", "i = C\\frac{du}{dt}", "电容电流正比于电压变化率"),
    ("电容储能", "w_C = \\frac{1}{2}C u^2", "电容储存的电场能量"),
    ("电容串联", "\\frac{1}{C_{eq}} = \\sum \\frac{1}{C_k}", "电容串联等效电容"),
    ("电容并联", "C_{eq} = \\sum C_k", "电容并联等效电容"),
    ("电感磁链", "\\psi = L\\,i", "磁链与电流成正比"),
    ("电感伏安关系", "u = L\\frac{di}{dt}", "电感电压正比于电流变化率"),
    ("电感储能", "w_L = \\frac{1}{2}L i^2", "电感储存的磁场能量"),
    ("电感串联", "L_{eq} = \\sum L_k", "电感串联等效电感"),
    ("电感并联", "\\frac{1}{L_{eq}} = \\sum \\frac{1}{L_k}", "电感并联等效电感"),
    ("换路定则（电容）", "u_C(0_+) = u_C(0_-)", "电容电压不能跃变"),
    ("换路定则（电感）", "i_L(0_+) = i_L(0_-)", "电感电流不能跃变"),
    ("RC 时间常数", "\\tau = R C", "RC 电路的时间常数"),
    ("RL 时间常数", "\\tau = \\frac{L}{R}", "RL 电路的时间常数"),
    ("RC 零输入响应", "u_C = U_0 e^{-t/\\tau}", "电容放电过程"),
    ("RC 零状态响应", "u_C = U\\left(1-e^{-t/\\tau}\\right)", "电容充电过程"),
    ("一阶全响应", "y = y(\\infty) + \\left[y(0_+)-y(\\infty)\\right]e^{-t/\\tau}", "三要素法一般表达式"),
    ("RL 零输入响应", "i_L = I_0 e^{-t/\\tau}", "电感电流衰减过程"),
    ("二阶特征方程", "s^2 + \\frac{R}{L}s + \\frac{1}{LC} = 0", "串联 RLC 的特征方程"),
    ("RLC 特征根", "s_{1,2} = -\\alpha \\pm \\sqrt{\\alpha^2-\\omega_0^2}", "二阶电路特征根"),
    ("衰减系数", "\\alpha = \\frac{R}{2L}", "表征阻尼强弱"),
    ("固有频率", "\\omega_0 = \\frac{1}{\\sqrt{LC}}", "LC 谐振角频率"),
    ("相量形式", "\\dot{U} = U\\angle\\varphi", "正弦量的复数表示"),
    ("相量欧姆定律", "\\dot{U} = Z\\,\\dot{I}", "复数形式的欧姆定律"),
    ("阻抗", "Z = R + jX", "电阻与电抗的复数和"),
    ("感抗", "X_L = \\omega L", "电感阻抗的虚部"),
    ("容抗", "X_C = -\\frac{1}{\\omega C}", "电容阻抗的虚部"),
    ("导纳", "Y = G + jB", "电导与电纳的复数和"),
    ("有功功率", "P = U I \\cos\\varphi", "正弦稳态平均功率"),
    ("无功功率", "Q = U I \\sin\\varphi", "与电源交换的功率"),
    ("视在功率", "S = U I", "电压电流有效值之积"),
    ("复功率", "\\bar{S} = \\dot{U}\\dot{I}^{*} = P + jQ", "复功率等于电压相量乘电流共轭"),
    ("功率因数", "\\cos\\varphi = \\frac{P}{S}", "有功与视在功率之比"),
    ("串联谐振频率", "\\omega_0 = \\frac{1}{\\sqrt{LC}}", "串联 RLC 谐振角频率"),
    ("品质因数", "Q = \\frac{\\omega_0 L}{R} = \\frac{1}{\\omega_0 R C}", "谐振电路的品质因数"),
    ("通频带", "BW = \\frac{\\omega_0}{Q}", "谐振曲线的 3 dB 带宽"),
    ("并联谐振阻抗", "Z_0 = \\frac{L}{RC}", "并联谐振时的等效阻抗"),
    ("互感电压", "u_2 = M\\frac{di_1}{dt}", "互感产生的感应电压"),
    ("耦合系数", "k = \\frac{M}{\\sqrt{L_1 L_2}}", "表征两线圈耦合紧密程度"),
    ("去耦等效", "L_{eq} = L_1 + L_2 \\pm 2M", "串接互感的等效电感"),
    ("理想变压器电压比", "\\frac{u_1}{u_2} = n", "匝数比等于电压比"),
    ("理想变压器电流比", "\\frac{i_1}{i_2} = -\\frac{1}{n}", "电流比等于匝数比倒数"),
    ("阻抗变换", "Z_{in} = n^2 Z_L", "副边阻抗折算到原边"),
    ("网络函数", "H(j\\omega) = \\frac{\\dot{Y}}{\\dot{X}}", "响应相量与激励相量之比"),
    ("一阶截止频率", "\\omega_c = \\frac{1}{RC}", "RC 低通网络的截止角频率"),
    ("波特图斜率", "-20\\ \\text{dB}/\\text{十倍频}", "一阶网络高频段渐近斜率"),
    ("傅里叶级数", "f(t) = a_0 + \\sum_{n=1}^{\\infty} A_n\\cos(n\\omega_1 t+\\varphi_n)", "周期量的三角级数展开"),
    ("方波傅里叶级数", "f(t) = \\frac{4A}{\\pi}\\sum_{k=0}^{\\infty}\\frac{\\sin(2k+1)\\omega_1 t}{2k+1}", "方波只含奇次谐波"),
    ("非正弦有效值", "I = \\sqrt{I_0^2 + \\sum_{n=1}^{\\infty} I_n^2}", "各次谐波有效值平方和开方"),
    ("非正弦平均功率", "P = U_0 I_0 + \\sum_{n=1}^{\\infty} U_n I_n\\cos\\varphi_n", "各次谐波各自贡献功率"),
    ("Y 参数方程", "\\dot{I}_1 = Y_{11}\\dot{U}_1 + Y_{12}\\dot{U}_2", "短路导纳参数定义式"),
    ("Z 参数方程", "\\dot{U}_1 = Z_{11}\\dot{I}_1 + Z_{12}\\dot{I}_2", "开路阻抗参数定义式"),
    ("T 参数方程", "\\dot{U}_1 = A\\dot{U}_2 - B\\dot{I}_2", "传输参数（级联）方程"),
    ("H 参数方程", "\\dot{U}_1 = h_{11}\\dot{I}_1 + h_{12}\\dot{U}_2", "混合参数方程"),
    ("Y↔Z 互换", "[Z] = [Y]^{-1}", "导纳矩阵与阻抗矩阵互为逆"),
    ("二端口级联", "T = T_1 \\cdot T_2", "级联网络传输矩阵相乘"),
    ("二端口并联", "Y = Y_1 + Y_2", "并联网络导纳矩阵相加"),
]

def js_escape(s):
    return s.replace("\\","\\\\").replace("`","\\`").replace("${","\\${")
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

ch1_sections = [
{
"name": "1.1 电路模型与基本变量",
"color": "#2563eb",
"desc": "集中参数假设、电流电压参考方向与功率",
"items": [
{"id":"ci1s1-1","name":"电路模型与集中参数假设","tags":["def","der"],"brief":"用理想元件及其连接模拟实际电路，须满足集中参数条件。",
 "fig":"circuit_basic","figCap":"基本电路模型：电源、电阻与电流参考方向",
 "body": wrap(
   defn("电路模型", p("将实际器件理想化，抽出其主要电磁性质，用<strong>理想电路元件</strong>及其连接模拟实际电路，即得到电路模型。电压、电流、电荷等物理量称为电路变量。"))+
   der(p("集中参数假设要求电路尺寸远小于工作波长。设电路最大尺寸为 $l$，电磁波在电路中传播速度为 $v$，信号周期为 $T$，则传播延迟为：")+
   fml("\\tau = \\frac{l}{v}")+
   p("若延迟远小于一个周期 $T=1/f$，则同一瞬间电路各点电压电流近似同时建立：")+
   fml("\\tau \\ll T \\iff l \\ll vT = \\frac{v}{f} = \\lambda")+
   p("即 $l\\ll\\lambda$ 时可用集中参数电路描述，此时基尔霍夫定律才是严格成立的。"))+
   note(p("当 $l$ 与 $\\lambda$ 可比时（如高频传输线、天线）必须改用分布参数模型。"))
 )},
{"id":"ci1s1-2","name":"电流、电压与参考方向","tags":["def","der"],"brief":"电流与电压须指定参考方向，关联方向下功率为正。",
 "body": wrap(
   defn("电流与电压", p("电流 $i=\\frac{dq}{dt}$ 表示电荷的定向移动速率，单位安培 A；电压 $u=\\frac{dw}{dq}$ 表示单位电荷在两点间移动时所获得或失去的能量，单位伏特 V。"))+
   der(p("为保证方程符号一致，必须先约定<strong>参考方向</strong>。当电流参考方向由高电位端指向低电位端时，称为电压与电流的<strong>关联参考方向</strong>；此时功率为正表示元件吸收功率。")+
   fml("p = u\\,i > 0 \\iff \\text{元件吸收功率}")+
   fml("p = u\\,i < 0 \\iff \\text{元件发出功率}")+
   p("若采用非关联方向，则功率表达式应取负号 $p=-ui$。参考方向是人为约定的，与真实方向无关。"))+
   note(p("计算结果为负只表示真实方向与参考方向相反，并不改变物理意义。"))
 )},
{"id":"ci1s1-3","name":"电功率与能量","tags":["der","exa"],"brief":"功率 p=ui，能量为功率对时间的积分。",
 "body": wrap(
   der(p("<strong>由电压电流定义推导功率：</strong>功率为单位时间内转换的能量，由 $u=dw/dq$、$i=dq/dt$ 得：")+
   fml("p = \\frac{dw}{dt} = \\frac{dw}{dq}\\cdot\\frac{dq}{dt} = u\\,i")+
   p("在时间区间 $[t_1,t_2]$ 内元件吸收的能量为功率的积分：")+
   fml("W = \\int_{t_1}^{t_2} p\\,dt = \\int_{t_1}^{t_2} u\\,i\\,dt")+
   p("对直流稳态，功率不随时间变化，能量简化为 $W=UIt$。"))+
   exa(p("<strong>例：</strong>某元件电压 $u=5\\,\\text{V}$、电流 $i=2\\,\\text{A}$ 且为关联方向，则 $p=10\\,\\text{W}$，$10\\,\\text{s}$ 内吸收能量 $W=100\\,\\text{J}$。"))+
   note(p("国际单位制中功率单位为瓦特 W，$1\\,\\text{W}=1\\,\\text{J/s}$。"))
 )},
]},
{
"name": "1.2 理想电路元件",
"color": "#0ea5e9",
"desc": "电阻、独立电压源与独立电流源的端口特性",
"items": [
{"id":"ci1s2-1","name":"电阻元件与伏安特性","tags":["def","der"],"brief":"线性电阻满足 u=Ri，是耗能元件。",
 "body": wrap(
   defn("电阻元件", p("电阻元件表征把电能不可逆地转换为热能的二端元件。若其 $u$-$i$ 特性为过原点的直线，则称为<strong>线性电阻</strong>，约束关系为欧姆定律：")+
   fml("u = R\\,i,\\qquad g = \\frac{1}{R}")+
   p("其中 $g$ 称为电导，单位西门子 S。"))+
   der(p("由欧姆定律与功率定义推导电阻消耗的功率：")+
   fml("p = u\\,i = (Ri)\\,i = i^2 R = \\frac{u^2}{R}")+
   p("由于 $R>0$，任意非零电压或电流下 $p\\ge 0$，故电阻总是吸收功率，是耗能元件。"))+
   note(p("短路对应 $R=0$（$u=0$），开路对应 $R\\to\\infty$（$i=0$），是两种极限情形。"))
 )},
{"id":"ci1s2-2","name":"理想电压源","tags":["def","der"],"brief":"端电压由自身决定，与电流无关。",
 "body": wrap(
   defn("理想电压源", p("理想电压源的端电压 $u_S(t)$ 是给定的时间函数，与通过它的电流无关；其输出电流则由外电路决定。直流电压源在 $u$-$i$ 平面上是一条平行于 $i$ 轴的直线：")+
   fml("u = u_S = \\text{const}"))+
   der(p("<strong>端口特性推导：</strong>设理想电压源外接任意负载 $R_L$，由 KVL 得端电压恒为 $u_S$，则负载电流为：")+
   fml("i = \\frac{u_S}{R_L}")+
   p("当 $R_L\\to\\infty$（开路）时 $i\\to 0$，端电压仍为 $u_S$；当 $R_L\\to 0$（短路）时 $i\\to\\infty$，输出功率趋于无穷。可见理想电压源不允许短路，其电流完全由外电路约束。"))+
   note(p("实际电压源用理想电压源串联内阻 $R_S$ 来建模，见第二章电源等效变换。"))
 )},
{"id":"ci1s2-3","name":"理想电流源","tags":["def","der"],"brief":"输出电流由自身决定，与端电压无关。",
 "body": wrap(
   defn("理想电流源", p("理想电流源的输出电流 $i_S(t)$ 是给定的时间函数，与端电压无关；其端电压由外电路决定。直流电流源在 $u$-$i$ 平面上是一条平行于 $u$ 轴的直线：")+
   fml("i = i_S = \\text{const}"))+
   der(p("<strong>端口特性推导：</strong>设理想电流源外接负载 $R_L$，由 KCL 知流过负载的电流恒为 $i_S$，则端电压为：")+
   fml("u = i_S R_L")+
   p("当 $R_L\\to\\infty$（开路）时 $u\\to\\infty$，理想电流源不允许开路；当 $R_L\\to 0$（短路）时 $u\\to 0$。其端电压完全由外电路约束。"))+
   note(p("实际电流源用理想电流源并联内阻 $R_S$ 建模，与电压源模型互为等效变换。"))
 )},
]},
{
"name": "1.3 基尔霍夫定律",
"color": "#3b82f6",
"desc": "KCL、KVL 及独立方程数目",
"items": [
{"id":"ci1s3-1","name":"基尔霍夫电流定律（KCL）","tags":["thm","der"],"brief":"任一节点全部支路电流的代数和为零。",
 "fig":"kcl","figCap":"节点电流的代数和为零（流出为正）",
 "body": wrap(
   thm("基尔霍夫电流定律", p("对电路中任一节点，在任一瞬间，流出该节点（或流入）的电流代数和恒为零：")+
   fml("\\sum_{k} i_k = 0")+
   p("流入取负、流出取正，或反之，结果相同。KCL 与元件性质无关，只由电流的连续性决定。"))+
   der(p("<strong>由电荷守恒推导：</strong>节点只是理想导线连接点，不能积累电荷。设节点在 $dt$ 内净流入电荷为 $dq$，则电荷守恒要求：")+
   fml("dq = \\sum_k i_k\\,dt = 0")+
   p("由于 $dt\\neq 0$，故得")+
   fml("\\sum_k i_k = 0")+
   p("一般形式还可写成 $\\oint_S \\mathbf{J}\\cdot d\\mathbf{S}=0$，即电流处处连续。"))+
   app(p("<strong>应用：</strong>KCL 可推广到包围多个节点的<strong>广义节点</strong>（超节点），是节点电压法的理论基础。"))
 )},
{"id":"ci1s3-2","name":"基尔霍夫电压定律（KVL）","tags":["thm","der"],"brief":"任一回路沿绕行方向电压降的代数和为零。",
 "fig":"kvl","figCap":"沿闭合回路绕行一周，电压降的代数和为零",
 "body": wrap(
   thm("基尔霍夫电压定律", p("对电路中任一回路，沿指定绕行方向，各段电压降的代数和恒为零：")+
   fml("\\sum_{k} u_k = 0"))+
   der(p("<strong>由电位的单值性推导：</strong>设回路各节点电位为 $\\varphi_1,\\varphi_2,\\dots,\\varphi_n$，沿闭合路径绕行一周回到起点，电位变化的总和必为零：")+
   fml("(\\varphi_2-\\varphi_1)+(\\varphi_3-\\varphi_2)+\\cdots+(\\varphi_1-\\varphi_n)=0")+
   p("整理即得 $\\sum u_k=0$。这说明 KVL 本质上是静电场的保守性在集中参数电路中的体现。"))+
   note(p("KVL 与支路元件性质无关；对含源支路，电压降应包含电源的 $\\pm u_S$ 项。"))
 )},
{"id":"ci1s3-3","name":"支路、节点、回路与独立方程数","tags":["def","der"],"brief":"b 条支路、n 个节点时独立 KCL 为 n−1 个。",
 "body": wrap(
   defn("电路拓扑术语", p("<strong>支路</strong>：流过同一电流的一段电路；<strong>节点</strong>：三条及以上支路的连接点；<strong>回路</strong>：由支路构成的闭合路径；<strong>网孔</strong>：内部不含支路的平面回路。"))+
   der(p("<strong>独立方程数目：</strong>设电路有 $b$ 条支路、$n$ 个节点。对全部 $n$ 个节点写 KCL 会多出一个线性相关的方程（因为把所有方程相加，每条支路电流出现两次而抵消），故独立 KCL 方程数为：")+
   fml("N_{KCL} = n-1")+
   p("再由 KVL 补充所需方程。平面电路独立回路数等于网孔数：")+
   fml("N_{KVL} = b-(n-1) = b-n+1")+
   p("两者之和恰为 $b$，等于待求支路电流数，方程组可解。"))+
   note(p("对非平面电路，独立回路数仍为 $b-n+1$，但需选取合适的独立回路集合。"))
 )},
]},
{
"name": "1.4 受控源",
"color": "#1d4ed8",
"desc": "四种受控源及其在电路分析中的处理",
"items": [
{"id":"ci1s4-1","name":"受控源的四种类型","tags":["def"],"brief":"电压/电流控制电压/电流，共四种组合。",
 "body": wrap(
   defn("受控源", p("受控源（非独立源）的电压或电流不独立，由电路中另一处的电压或电流（称为<strong>控制量</strong>）决定，体现器件内部某支路对另一支路的耦合作用。"))+
   defn("四种类型", p("按控制量与被控量的组合分为四类：")+
   fml("\\text{VCVS}:\\ u_2=\\mu u_1,\\quad \\text{VCCS}:\\ i_2=g_m u_1")+
   fml("\\text{CCVS}:\\ u_2=r_m i_1,\\quad \\text{CCCS}:\\ i_2=\\beta i_1")+
   p("分别对应电压控制电压源、电压控制电流源、电流控制电压源与电流控制电流源。"))+
   der(p("以 VCCS 为例，其输出电流与端电压无关，只由控制电压 $u_1$ 线性决定：")+
   fml("i_2 = g_m u_1")+
   p("当控制量 $u_1$ 变化时，输出电流成比例变化，等效于一个由别处电压控制的电流源。"))+
   note(p("受控源是有源元件，可以向电路提供能量，其功率符号要具体计算。"))
 )},
{"id":"ci1s4-2","name":"含受控源电路的分析特点","tags":["der","exa"],"brief":"控制量须用电路未知量表示，求解时不能简单置零。",
 "body": wrap(
   der(p("<strong>列方程原则：</strong>受控源在列 KCL/KVL 时先当作独立源写入方程，再把控制量用它所在支路的未知量表示，使方程中只含电路变量。以节点法为例，若某支路电流受 $u_1$ 控制：")+
   fml("i_2 = g_m u_1 = g_m(\\varphi_a-\\varphi_b)")+
   p("将 $i_2$ 代入节点方程后，方程右边的受控项移到左边，得到含受控系数的规范方程。"))+
   der(p("<strong>等效电阻的求法：</strong>求含受控源单口网络的等效电阻时，把<strong>独立源置零</strong>（电压源短路、电流源开路），但<strong>受控源必须保留</strong>，再用外加电源法：")+
   fml("R_{eq} = \\frac{u}{i}\\Big|_{\\text{外加电源}}")+
   p("因为受控源反映的是电路内部的耦合，置零会破坏元件间的依赖关系。"))+
   exa(p("<strong>例：</strong>若外加电压 $u$ 时测得 $i=u/R_0$ 但受控源使 $i$ 减小，则等效电阻可能大于、等于甚至小于 $R_0$，甚至为负（表示可提供功率）。"))+
   note(p("受控源不能单独作为电路激励，其存在依赖于控制支路。"))
 )},
{"id":"ci1s4-3","name":"受控源的功率与电路等效","tags":["der","note"],"brief":"受控源功率可正可负，可对外提供能量。",
 "body": wrap(
   der(p("受控源发出的功率由端电压与电流共同决定。以 VCCS 为例，其吸收功率为：")+
   fml("p = u_2\\,i_2 = u_2\\,(g_m u_1)")+
   p("若 $p<0$ 则受控源实际发出功率，相当于有源器件（如晶体管放大）向电路供能。")+
   fml("p>0:\\ \\text{吸收功率},\\qquad p<0:\\ \\text{发出功率}"))+
   note(p("在受控源与独立源混合的电路中，含受控源的二端网络可用戴维南/诺顿等效（第四章）处理，但求等效电阻时必须保留受控源。"))
 )},
]},
]

ch2_sections = [
{
"name": "2.1 电阻的串联、并联与分压分流",
"color": "#7c3aed",
"desc": "串联分压、并联分流与混联等效",
"items": [
{"id":"ci2s1-1","name":"电阻串联与分压","tags":["der","exa"],"brief":"串联等效电阻为各电阻之和，电压按阻值分配。",
 "fig":"voltage_divider","figCap":"串联电阻的分压关系",
 "body": wrap(
   der(p("<strong>串联等效电阻：</strong>串联时各电阻流过同一电流 $i$，由 KVL 得总电压等于各电阻电压之和：")+
   fml("u = u_1+u_2+\\cdots+u_n = (R_1+R_2+\\cdots+R_n)\\,i")+
   p("故等效电阻为：")+
   fml("R_{eq} = \\frac{u}{i} = \\sum_{k=1}^{n} R_k")+
   p("由于流过同一电流，第 $k$ 个电阻的电压为 $u_k=R_k i$，与总电压之比即<strong>分压公式</strong>：")+
   fml("u_k = \\frac{R_k}{R_{eq}}\\,u = \\frac{R_k}{\\sum_j R_j}\\,u"))+
   exa(p("<strong>例：</strong>$R_1=2\\,\\Omega$、$R_2=4\\,\\Omega$ 串联，总电压 $12\\,\\text{V}$，则 $R_{eq}=6\\,\\Omega$，$u_1=\\frac{2}{6}\\times12=4\\,\\text{V}$，$u_2=8\\,\\text{V}$。"))+
   note(p("串联电路各电阻功率之比等于阻值之比 $P_k\\propto R_k$。"))
 )},
{"id":"ci2s1-2","name":"电阻并联与分流","tags":["der","exa"],"brief":"并联等效电阻倒数等于各电阻倒数之和，电流按电导分配。",
 "body": wrap(
   der(p("<strong>并联等效电阻：</strong>并联时各电阻承受同一电压 $u$，由 KCL 得总电流等于各支路电流之和：")+
   fml("i = i_1+i_2+\\cdots+i_n = \\left(\\frac{1}{R_1}+\\frac{1}{R_2}+\\cdots+\\frac{1}{R_n}\\right)u")+
   p("故用<strong>电导</strong>表示更简洁，等效电导为各电导之和：")+
   fml("G_{eq} = \\frac{1}{R_{eq}} = \\sum_{k=1}^{n} G_k,\\qquad G_k=\\frac{1}{R_k}")+
   p("第 $k$ 支路电流与总电流之比即<strong>分流公式</strong>：")+
   fml("i_k = \\frac{G_k}{G_{eq}}\\,i = \\frac{G_k}{\\sum_j G_j}\\,i"))+
   exa(p("<strong>例（两电阻并联）：</strong>$R_1=6\\,\\Omega$、$R_2=3\\,\\Omega$ 并联，$R_{eq}=\\frac{6\\times3}{6+3}=2\\,\\Omega$。总电流 $3\\,\\text{A}$ 时，$i_1=\\frac{3}{9}\\times3=1\\,\\text{A}$，$i_2=2\\,\\text{A}$，即电阻小的分流大。"))+
   note(p("并联常用来给负载提供相同电压，分流与自身电阻成反比。"))
 )},
{"id":"ci2s1-3","name":"混联等效与平衡电桥","tags":["der","exa"],"brief":"逐步化简混联；电桥平衡时桥臂无电流。",
 "fig":"series_parallel","figCap":"串联与并联的等效化简",
 "body": wrap(
   der(p("<strong>混联化简：</strong>对既有串联又有并联的网络，可从离端口最远处逐步用串并联公式向内合并，直至化为单个等效电阻。")+
   p("以惠斯通电桥为例，若检流计支路（$R_g$）电流为零，则桥上两点等电位，桥臂可拆开分别串联再并联：")+
   fml("u_{cd}=0 \\implies i_g=0"))+
   der(p("<strong>平衡条件的推导：</strong>桥臂无电流意味着上下两分压相等：")+
   fml("\\frac{R_2}{R_1+R_2}u = \\frac{R_4}{R_3+R_4}u")+
   p("整理得电桥平衡条件：")+
   fml("R_1 R_4 = R_2 R_3")+
   p("此时桥臂可移除，等效电阻为 $(R_1+R_2)\\|(R_3+R_4)$。"))+
   exa(p("<strong>例：</strong>$R_1=10$、$R_2=20$、$R_3=30$、$R_4=60\\,\\Omega$，因 $10\\times60=20\\times30$ 平衡，桥臂电流为零。"))+
   note(p("电桥平衡常用于精确测量电阻、电容与电感（交流电桥）。"))
 )},
]},
{
"name": "2.2 电阻的星形与三角形联结",
"color": "#8b5cf6",
"desc": "Δ 与 Y 联结及其等效互换",
"items": [
{"id":"ci2s2-1","name":"Δ 联结与 Y 联结","tags":["def"],"brief":"三端电阻网络的两种基本联结方式。",
 "fig":"delta_wye","figCap":"三角形（Δ）联结与星形（Y）联结的等效互换",
 "body": wrap(
   defn("Δ 联结与 Y 联结", p("三个电阻首尾相接构成闭合三角形，称为<strong>三角形联结（Δ）</strong>；三个电阻一端连于公共节点、另一端分别引出，称为<strong>星形联结（Y）</strong>。两者都是三端网络，在满足端口等效的条件下可以互换。"))+
   der(p("记 Δ 联结三臂为 $R_{AB},R_{BC},R_{CA}$，Y 联结三臂为 $R_A,R_B,R_C$。等效要求任意两端之间的输入电阻相等，例如对 $A$、$B$ 两端：")+
   fml("R_A+R_B = R_{AB}\\parallel(R_{BC}+R_{CA})")+
   p("其余两端同理，由此可解出两套电阻之间的换算关系。"))+
   note(p("Δ–Y 变换是化简非串非并网络（如不平衡电桥）的重要工具。"))
 )},
{"id":"ci2s2-2","name":"Δ–Y 等效变换推导","tags":["der","thm"],"brief":"由端口等电阻条件联立求出 Y 臂表达式。",
 "body": wrap(
   thm("Δ 转 Y 公式", p("已知三角形三臂，则等效星形各臂为：")+
   fml("R_A=\\frac{R_{AB}R_{CA}}{R_{AB}+R_{BC}+R_{CA}},\\quad R_B=\\frac{R_{AB}R_{BC}}{\\sum R},\\quad R_C=\\frac{R_{BC}R_{CA}}{\\sum R}"))+
   der(p("<strong>推导：</strong>令 $S=R_{AB}+R_{BC}+R_{CA}$。端口 $A$、$B$ 之间，Y 接为 $R_A+R_B$，Δ 接为 $R_{AB}$ 与 $(R_{BC}+R_{CA})$ 并联：")+
   fml("R_A+R_B = \\frac{R_{AB}(R_{BC}+R_{CA})}{S}")+
   p("同理由端口 $B$-$C$、$C$-$A$ 得：")+
   fml("R_B+R_C = \\frac{R_{BC}(R_{CA}+R_{AB})}{S},\\quad R_C+R_A = \\frac{R_{CA}(R_{AB}+R_{BC})}{S}")+
   p("把第一式加第三式再减第二式，得 $2R_A$，两边除以 2 即得：")+
   fml("R_A = \\frac{R_{AB}R_{CA}}{S}")+
   p("轮换下标即得 $R_B$、$R_C$ 的表达式。"))+
   note(p("当 Δ 三臂对称均为 $R_\\Delta$ 时，$R_Y=R_\\Delta/3$。"))
 )},
{"id":"ci2s2-3","name":"Y–Δ 变换与桥式电路化简","tags":["der","exa"],"brief":"由 Y 转 Δ 的乘积和公式化简复杂网络。",
 "body": wrap(
   thm("Y 转 Δ 公式", p("已知星形三臂，则等效三角形各臂为：")+
   fml("R_{AB}=\\frac{R_A R_B+R_B R_C+R_C R_A}{R_C}")+
   p("轮换下标即得 $R_{BC}$、$R_{CA}$。"))+
   der(p("<strong>推导：</strong>由 Δ 转 Y 公式可得三个乘积关系：")+
   fml("R_A R_B = \\frac{R_{AB}^2 R_{BC} R_{CA}}{S^2},\\quad R_A R_B+R_B R_C+R_C R_A = \\frac{R_{AB}R_{BC}R_{CA}}{S}")+
   p("用此和式除以 $R_C=\\frac{R_{BC}R_{CA}}{S}$ 即消去公共因子，得：")+
   fml("\\frac{R_A R_B+R_B R_C+R_C R_A}{R_C} = R_{AB}")+
   p("故 Y 转 Δ 的任一臂等于两两乘积之和除以对应对端臂。"))+
   exa(p("<strong>例：</strong>Y 三臂均为 $R_Y$ 时，$R_\\Delta=\\frac{3R_Y^2}{R_Y}=3R_Y$，与 Δ 转 Y 的 $R_Y=R_\\Delta/3$ 一致。"))+
   app(p("<strong>应用：</strong>不平衡电桥可把其中一个 Y（或 Δ）子网络变换后再用串并联公式化简。"))
 )},
]},
{
"name": "2.3 实际电源的等效变换与含源支路",
"color": "#6d28d9",
"desc": "两种电源模型及其等效变换",
"items": [
{"id":"ci2s3-1","name":"实际电源的两种模型","tags":["def","der"],"brief":"实际电源可用电压源串内阻或电流源并内阻建模。",
 "fig":"source_transform","figCap":"有伴电压源与有伴电流源的等效变换",
 "body": wrap(
   defn("实际电压源模型", p("理想电压源 $u_S$ 串联内阻 $R_S$，其端口伏安关系为：")+
   fml("u = u_S - R_S\\,i"))+
   defn("实际电流源模型", p("理想电流源 $i_S$ 并联内阻 $R_S$，其端口伏安关系为：")+
   fml("i = i_S - \\frac{u}{R_S}"))+
   der(p("由电流源模型解出端电压：")+
   fml("u = R_S(i_S - i) = R_S i_S - R_S i")+
   p("与电压源模型的 $u=u_S-R_S i$ 比较可知，只要满足 $u_S=R_S i_S$ 且内阻相同，两模型对外端口完全等效。"))+
   note(p("两种模型的等效只对外电路成立，内部功率并不相同。"))
 )},
{"id":"ci2s3-2","name":"电源等效变换推导","tags":["der","thm"],"brief":"电压源与电流源模型在 u_S=R_S i_S 时对外等效。",
 "body": wrap(
   thm("电源等效变换", p("有伴电压源与有伴电流源可互相转换，参数关系为：")+
   fml("u_S = R_S\\,i_S,\\qquad i_S = \\frac{u_S}{R_S}"))+
   der(p("<strong>推导：</strong>两个单口网络等效的充要条件是端口伏安关系完全相同。电压源模型的 VCR 为 $u=u_S-R_S i$，电流源模型为 $u=R_S i_S-R_S i$。令二者对任意 $i$ 都相等：")+
   fml("u_S - R_S i \\equiv R_S i_S - R_S i")+
   p("比较系数即得 $u_S=R_S i_S$，而内阻 $R_S$ 保持不变。变换后电源的方向应使端口电压极性一致。"))+
   der(p("<strong>推广：</strong>理想电压源（$R_S=0$）与理想电流源（$R_S\\to\\infty$）之间不能直接互换，因为会得到无穷大参数，需保留原模型。"))+
   app(p("<strong>应用：</strong>电源变换常用于把复杂含源支路逐步化简为单一戴维南或诺顿等效（第四章）。"))
 )},
{"id":"ci2s3-3","name":"含源支路的串并联与受控源变换","tags":["der","exa"],"brief":"电压源可串联、电流源可并联，受控源同样可等效变换。",
 "body": wrap(
   der(p("<strong>电压源串联：</strong>多个电压源串联时，等效电压为各源代数和（极性相同取加）：")+
   fml("u_{eq} = \\sum_k u_{S_k}")+
   p("串联支路总电阻为各内阻之和。"))+
   der(p("<strong>电流源并联：</strong>多个电流源并联时，等效电流为各源代数和：")+
   fml("i_{eq} = \\sum_k i_{S_k}")+
   p("并联支路等效电导为各电导之和。对串联的电流源或并联的电压源，只有完全相同才允许，否则不满足 KCL/KVL。"))+
   der(p("<strong>受控源变换：</strong>受控源同样可以按 $u_S=R_S i_S$ 的关系互换，但<strong>控制支路不能被变换消去</strong>。例如把受控电压源 $\\mu u_1$ 串 $R$ 化为受控电流源：")+
   fml("i = \\frac{\\mu u_1}{R}")+
   p("同时须保证控制量 $u_1$ 所在的支路仍然存在，否则变换后无法确定控制关系。"))+
   exa(p("<strong>例：</strong>$12\\,\\text{V}$ 电压源串 $3\\,\\Omega$ 内阻，可化为 $i_S=4\\,\\text{A}$ 电流源并 $3\\,\\Omega$ 内阻。"))+
   note(p("含受控源支路化简时，求等效电阻须保留受控源并使用外加电源法。"))
 )},
]},
]

ch3_sections = [
{
"name": "3.1 支路电流法",
"color": "#0d9488",
"desc": "以支路电流为未知量的直接求解法",
"items": [
{"id":"ci3s1-1","name":"支路电流法","tags":["def","der"],"brief":"以 b 条支路电流为未知量，列 KCL 与 KVL 联立求解。",
 "body": wrap(
   defn("支路电流法", p("以电路中全部支路电流为未知量，对节点列 KCL、对独立回路列 KVL，得到数目等于支路数的方程组，解出各支路电流后再求电压与功率。"))+
   der(p("<strong>方程建立：</strong>设电路有 $b$ 条支路、$n$ 个节点。先对 $n-1$ 个独立节点列 KCL：")+
   fml("\\sum_{k} i_k = 0\\quad (n-1\\ \\text{个})")+
   p("再对 $b-n+1$ 个独立回路列 KVL，每段电压用 $u=R i$ 或已知源表示：")+
   fml("\\sum_{k} R_k i_k = \\sum_{j} u_{S_j}\\quad (b-n+1\\ \\text{个})")+
   p("两组方程共 $b$ 个，恰好等于未知支路电流数，故可唯一求解。"))+
   note(p("支路电流法物理意义直观，但方程数等于支路数，支路较多时计算量大。"))
 )},
{"id":"ci3s1-2","name":"方程的独立性与回路选择","tags":["der"],"brief":"节点方程需去掉一个，回路须彼此独立。",
 "body": wrap(
   der(p("<strong>KCL 独立性：</strong>把全部 $n$ 个节点的 KCL 相加，每条支路电流一进一出恰好抵消：")+
   fml("\\sum_{j=1}^{n}\\left(\\sum_{k\\in j} i_k\\right) \\equiv 0")+
   p("这说明 $n$ 个节点方程线性相关，只有 $n-1$ 个独立，故只需对其中 $n-1$ 个节点列方程。"))+
   der(p("<strong>KVL 独立性：</strong>平面电路的独立回路数等于网孔数 $b-n+1$。若选取的回路中含有一个此前未用过的新支路，则该回路独立；按网孔选取天然满足独立性。")+
   fml("N_{KVL} = b-(n-1)"))+
   note(p("选网孔作为独立回路最简便，非平面电路需选取合适的独立回路集合。"))
 )},
{"id":"ci3s1-3","name":"支路电流法算例","tags":["exa","der"],"brief":"双网孔电路的求解示例。",
 "body": wrap(
   exa(p("<strong>例：</strong>两网孔电路，网孔 1 含电压源 $10\\,\\text{V}$ 与 $R_1=4\\,\\Omega$、公共电阻 $R_2=2\\,\\Omega$；网孔 2 含电压源 $4\\,\\text{V}$ 与 $R_2=2\\,\\Omega$、$R_3=6\\,\\Omega$。求各支路电流。"))+
   der(p("设网孔电流 $i_1$、$i_2$ 均顺时针。对网孔 1 列 KVL：")+
   fml("4i_1 + 2(i_1-i_2) = 10 \\implies 6i_1-2i_2=10")+
   p("对网孔 2 列 KVL（取逆时针绕行以匹配电源极性）：")+
   fml("-2(i_1-i_2)+6i_2 = 4 \\implies -2i_1+8i_2=4")+
   p("联立求解：由第二式得 $i_1=4i_2-2$，代入第一式：")+
   fml("6(4i_2-2)-2i_2=10 \\implies 22i_2=22 \\implies i_2=1\\,\\text{A}")+
   p("代回得 $i_1=2\\,\\text{A}$，故公共支路电流为 $i_1-i_2=1\\,\\text{A}$。"))+
   note(p("三个支路电流分别为 $2\\,\\text{A}$、$1\\,\\text{A}$、$1\\,\\text{A}$，代入 KCL 可验证守恒。"))
 )},
]},
{
"name": "3.2 网孔电流法",
"color": "#0f766e",
"desc": "以网孔电流为未知量的回路分析法",
"items": [
{"id":"ci3s2-1","name":"网孔电流法","tags":["def","der"],"brief":"假想网孔电流沿网孔环流，自动满足 KCL。",
 "fig":"mesh","figCap":"网孔电流沿每个独立网孔环流",
 "body": wrap(
   defn("网孔电流", p("在平面电路的每个网孔中假想一个沿网孔边界环流的电流 $i_{m}$，称为<strong>网孔电流</strong>。各支路真实电流等于经过该支路的网孔电流的代数和。"))+
   der(p("<strong>自动满足 KCL：</strong>因为网孔电流沿闭合路径连续流动，在每个节点都是流入等于流出，故节点 KCL 自动成立。对第 $k$ 个网孔列 KVL：")+
   fml("\\sum_{j} R_{kj} i_{mj} = \\sum u_{Sk}")+
   p("其中 $R_{kk}$ 为网孔 $k$ 的自阻（恒为正），$R_{kj}$ 为网孔 $k$、$j$ 的互阻（公共支路电阻，通常取负）。方程数等于网孔数 $b-n+1$，比支路法少 $n-1$ 个。"))+
   note(p("网孔电流是虚拟量，求出后再由代数和还原各支路真实电流。"))
 )},
{"id":"ci3s2-2","name":"网孔方程的标准形式","tags":["der"],"brief":"自阻乘本网孔电流减互阻乘邻网孔电流等于网孔内电源代数和。",
 "body": wrap(
   thm("网孔方程标准形式", p("对含 $m$ 个网孔的电路，可统一写成：")+
   fml("R_{11}i_{m1}+R_{12}i_{m2}+\\cdots = u_{S1}")+
   fml("R_{21}i_{m1}+R_{22}i_{m2}+\\cdots = u_{S2}"))+
   der(p("<strong>系数规律推导：</strong>考察网孔 1，其自阻 $R_{11}$ 为网孔 1 内全部电阻之和，因为网孔电流 $i_{m1}$ 在自阻上产生的电压降为 $R_{11}i_{m1}$。")+
   fml("R_{11} = \\sum_{R\\in \\text{mesh}1} R")+
   p("邻网孔电流 $i_{m2}$ 在公共支路上与 $i_{m1}$ 方向相反（默认为同向环流），故对网孔 1 的贡献为 $-R_{12}i_{m2}$，其中 $R_{12}$ 为公共电阻：")+
   fml("R_{12}=R_{21}=-\\!\\!\\sum_{R\\in \\text{公共支路}}\\!\\! R")+
   p("方程右端为网孔内全部电压源的代数和，电压升取正、电压降取负：")+
   fml("u_{S1} = \\sum u_{S}\\ (\\text{网孔1内，升为正})")+
   p("这样就得到规则的对称方程组，互阻矩阵满足 $R_{kj}=R_{jk}$。"))+
   note(p("若各网孔电流统一取顺时针方向，则互阻恒取负号，规律十分整齐。"))
 )},
{"id":"ci3s2-3","name":"含电流源与受控源的网孔方程","tags":["der","exa"],"brief":"电流源所在网孔用超网孔，受控源控制量用网孔电流表示。",
 "body": wrap(
   der(p("<strong>含理想电流源：</strong>若电流源位于两网孔的公共支路，则两网孔电流之差等于该电流源电流，方程可少设一个未知量：")+
   fml("i_{m1}-i_{m2} = \\pm i_S")+
   p("若电流源独占一个网孔（只属于该网孔），则该网孔电流直接已知，无需为它列 KVL。当电流源位于大回路公共支路时，可取<strong>超网孔</strong>（闭合成一个大回路）列 KVL，再补充上述电流约束方程。"))+
   der(p("<strong>含受控源：</strong>先把受控源当作独立源写入网孔方程右端，再把控制量用网孔电流表示后移项到左边，得到含受控系数的方程。例如控制量为 $i_x=i_{m1}-i_{m2}$ 时：")+
   fml("u_{S}\\ \\to\\ \\mu(i_{m1}-i_{m2})")+
   p("整理后未知量系数不再对称，但方程仍可解。"))+
   exa(p("<strong>例：</strong>两网孔间有一受控电压源 $2i_x$，$i_x=i_{m1}-i_{m2}$，则网孔 2 方程右端写 $-2(i_{m1}-i_{m2})$，移到左边即增加相应的 $i_{m1}$、$i_{m2}$ 系数。"))+
   note(p("受控源不得当作独立源移到右边而不处理控制量，否则方程不封闭。"))
 )},
]},
{
"name": "3.3 节点电压法",
"color": "#14b8a6",
"desc": "以节点电压为未知量的分析方法",
"items": [
{"id":"ci3s3-1","name":"节点电压与参考节点","tags":["def","der"],"brief":"选一节点为参考，其余节点相对它的电压为未知量。",
 "fig":"nodal","figCap":"节点电压以参考地为零电位",
 "body": wrap(
   defn("节点电压法", p("任选一个节点作为<strong>参考节点</strong>（零电位点），其余每个节点相对参考节点的电压称为<strong>节点电压</strong>。以节点电压为未知量对各独立节点列 KCL。"))+
   der(p("<strong>支路电压用节点电压表示：</strong>设节点 $k$、$j$ 的电压为 $u_{nk}$、$u_{nj}$，则连接两节点的支路电压为：")+
   fml("u_{kj} = u_{nk}-u_{nj}")+
   p("对含电阻的支路，电流为 $i_{kj}=\\frac{u_{nk}-u_{nj}}{R_{kj}}=G_{kj}(u_{nk}-u_{nj})$，代入节点 KCL 后即得节点电压方程。"))+
   note(p("节点电压自动满足 KVL，因为回路电压由节点电压差沿回路求和必为零。"))
 )},
{"id":"ci3s3-2","name":"节点方程的标准形式","tags":["der","thm"],"brief":"自导纳乘本节点电压减互导纳乘邻节点电压等于节点电流源代数和。",
 "body": wrap(
   thm("节点方程标准形式", p("对含 $n-1$ 个独立节点的电路，节点电压方程统一写为：")+
   fml("G_{11}u_{n1}+G_{12}u_{n2}+\\cdots = i_{S1}")+
   fml("G_{21}u_{n1}+G_{22}u_{n2}+\\cdots = i_{S2}"))+
   der(p("<strong>系数规律推导：</strong>对节点 1 列 KCL（流出为正），与节点 1 相连的各支路电流用节点电压表示并求和：")+
   fml("\\sum_{j\\ne1} G_{1j}(u_{n1}-u_{nj}) = \\sum i_{S}")+
   p("把含 $u_{n1}$ 的项合并，得自导纳：")+
   fml("G_{11} = \\sum_{j\\ne1} G_{1j}\\quad(\\text{接于节点1的全部电导之和})")+
   p("邻节点电压项系数为互导纳，取负：")+
   fml("G_{1j} = -\\sum_{\\text{连接1与j}} G\\quad (j\\ne1)")+
   p("方程右端为流入节点 1 的电流源代数和（流入为正）。由此得对称的节点电导矩阵 $G_{kj}=G_{jk}$。"))+
   note(p("节点法特别适合节点少、支路多的电路，与网孔法互为对偶。"))
 )},
{"id":"ci3s3-3","name":"含电压源与受控源的节点方程","tags":["der","exa"],"brief":"电压源接参考节点时直接给定，否则用超节点。",
 "body": wrap(
   der(p("<strong>电压源接参考节点：</strong>若理想电压源一端接参考节点，则另一端节点电压直接等于该源电压，无需列 KCL：")+
   fml("u_{nk} = \\pm u_S")+
   p("若电压源串有电阻，则按电源等效变换化为电流源再列方程。"))+
   der(p("<strong>超节点：</strong>当理想电压源接在两个非参考节点之间时，把这两个节点合并成<strong>超节点</strong>，对超节点整体列 KCL，再补充电压源约束：")+
   fml("u_{na}-u_{nb} = u_S")+
   p("这样既保留了电压源约束，又减少了一个未知量。"))+
   exa(p("<strong>例（含受控源）：</strong>若某支路电流受电压 $u_x$ 控制，$i_x=g_m u_x$，而 $u_x=u_{n2}-u_{n3}$，则把 $g_m(u_{n2}-u_{n3})$ 代入相应节点方程并移项，控制量即可用节点电压表示。"))+
   note(p("处理受控源时，控制量必须最终只用节点电压表示，方程才不会出现额外未知量。"))
 )},
]},
{
"name": "3.4 分析法的比较与算例",
"color": "#115e59",
"desc": "方法选择、矩阵形式与综合算例",
"items": [
{"id":"ci3s4-1","name":"分析方法的选择","tags":["der","note"],"brief":"按方程数目与电路结构选择支路法、网孔法或节点法。",
 "body": wrap(
   der(p("三种方法的方程数目为：")+
   fml("\\text{支路法}:\\ b\\quad\\text{网孔法}:\\ b-n+1\\quad\\text{节点法}:\\ n-1")+
   p("当节点数少（$n-1 < b-n+1$）时优先用节点法；当网孔数少时优先用网孔法；支路极少时可直接用支路法。含较多理想电流源的电路宜用节点法，含较多理想电压源的电路宜用网孔法。"))+
   note(p("选择合适方法可显著减少方程数与计算量，这是电路分析的重要技巧。"))
 )},
{"id":"ci3s4-2","name":"规范方程的矩阵形式","tags":["der"],"brief":"网孔与节点方程均可写成矩阵形式。",
 "body": wrap(
   der(p("网孔方程组写成矩阵形式：")+
   fml("\\mathbf{R}\\,\\mathbf{i}_m = \\mathbf{u}_S")+
   p("节点方程组写成矩阵形式：")+
   fml("\\mathbf{G}\\,\\mathbf{u}_n = \\mathbf{i}_S")+
   p("其中 $\\mathbf{R}$ 为网孔电阻矩阵（对称），$\\mathbf{G}$ 为节点电导矩阵（对称）。对无受控源的线性电路，两矩阵均为对称阵，可用行列式或高斯消元求解：")+
   fml("\\mathbf{i}_m = \\mathbf{R}^{-1}\\mathbf{u}_S,\\qquad \\mathbf{u}_n = \\mathbf{G}^{-1}\\mathbf{i}_S")+
   p("用计算机辅助分析时，只需自动生成矩阵元素即可求解任意大规模电路。"))+
   app(p("<strong>应用：</strong>SPICE 类电路仿真软件的核心正是以节点法（改进节点法）自动建立并求解 $\\mathbf{G}\\mathbf{u}=\\mathbf{i}$。"))
 )},
{"id":"ci3s4-3","name":"综合算例","tags":["exa","der"],"brief":"用节点法求解含两电源的电路。",
 "body": wrap(
   exa(p("<strong>例：</strong>三节点电路，参考节点接地。节点 1 经 $4\\,\\Omega$ 与节点 2 相连，节点 1 另有 $2\\,\\text{A}$ 电流源流入并接 $2\\,\\Omega$ 电阻到地；节点 2 接 $6\\,\\Omega$ 电阻到地并有 $10\\,\\text{V}$ 电压源经 $2\\,\\Omega$ 接至节点 2 与地之间（等效为 $5\\,\\text{A}$ 并 $2\\,\\Omega$）。求节点电压。"))+
   der(p("对节点 1 列 KCL（流出为正）：")+
   fml("\\frac{u_1}{2}+\\frac{u_1-u_2}{4} = 2")+
   p("对节点 2 列 KCL：")+
   fml("\\frac{u_2-u_1}{4}+\\frac{u_2}{2}+\\frac{u_2}{6}=5")+
   p("整理成标准形式：")+
   fml("0.75u_1-0.25u_2=2,\\qquad -0.25u_1+0.917u_2=5")+
   p("解得 $u_1\\approx 4.86\\,\\text{V}$，$u_2\\approx 6.78\\,\\text{V}$。"))+
   note(p("求出节点电压后，各支路电流与功率均可由 $i=G\\Delta u$、$p=ui$ 依次算出。"))
 )},
]},
]

ch4_sections = [
{
"name": "4.1 叠加定理与齐性定理",
"color": "#c2410c",
"desc": "线性电路响应的可叠加性与齐次性",
"items": [
{"id":"ci4s1-1","name":"叠加定理","tags":["thm","der"],"brief":"线性电路中各独立源单独作用响应的代数和等于总响应。",
 "fig":"superposition","figCap":"多个独立源作用的响应等于各源单独作用响应之和",
 "body": wrap(
   thm("叠加定理", p("在任何由线性元件构成的电路中，当多个独立源同时作用时，任一支路的电流（或电压）等于各独立源<strong>单独作用</strong>时在该支路产生的电流（或电压）的代数和。所谓某源单独作用，是指其余独立电压源短路、独立电流源开路，但受控源与全部电阻保持不动。"))+
   der(p("<strong>由线性方程组推导：</strong>以网孔法为例，电路方程为 $\\mathbf{R}\\mathbf{i}_m=\\mathbf{u}_S$。把激励向量分解为各源单独作用之和：")+
   fml("\\mathbf{u}_S = \\mathbf{u}_S^{(1)}+\\mathbf{u}_S^{(2)}+\\cdots+\\mathbf{u}_S^{(k)}")+
   p("由矩阵乘法的线性性：")+
   fml("\\mathbf{i}_m = \\mathbf{R}^{-1}\\sum_k \\mathbf{u}_S^{(k)} = \\sum_k \\mathbf{R}^{-1}\\mathbf{u}_S^{(k)} = \\sum_k \\mathbf{i}_m^{(k)}")+
   p("即总响应等于各源单独作用响应的叠加，节点法方程同理。"))+
   note(p("叠加定理只适用于线性电路，且只能叠加电流与电压，不能叠加功率。"))
 )},
{"id":"ci4s1-2","name":"齐性定理","tags":["thm","der"],"brief":"激励放大 k 倍，线性响应也放大 k 倍。",
 "body": wrap(
   thm("齐性定理", p("在线性电路中，若全部独立激励同时增大 $k$ 倍，则各支路电流、电压也相应增大 $k$ 倍。该性质是叠加定理的直接推论，也称比例性。"))+
   der(p("<strong>推导：</strong>设激励向量 $\\mathbf{u}_S$ 对应响应 $\\mathbf{i}=\\mathbf{R}^{-1}\\mathbf{u}_S$。当激励变为 $k\\mathbf{u}_S$ 时：")+
   fml("\\mathbf{i}' = \\mathbf{R}^{-1}(k\\mathbf{u}_S) = k\\,\\mathbf{R}^{-1}\\mathbf{u}_S = k\\,\\mathbf{i}")+
   p("由于电阻矩阵 $\\mathbf{R}$ 不随激励变化，响应严格按 $k$ 倍变化。"))+
   app(p("<strong>应用：</strong>齐性定理常用于<strong>比例法</strong>求解梯形网络——先假设末端电流为便于计算的数值，逐级反推至电源，再按比例折算回真实值。"))
 )},
{"id":"ci4s1-3","name":"叠加定理的适用范围与功率","tags":["der","note"],"brief":"功率是电压电流的乘积，不能叠加。",
 "body": wrap(
   der(p("<strong>功率不可叠加的推导：</strong>设两电源单独作用时某电阻上的电压、电流分别为 $(u_1,i_1)$ 与 $(u_2,i_2)$。叠加后的功率为：")+
   fml("p = (u_1+u_2)(i_1+i_2) = u_1i_1+u_2i_2+(u_1i_2+u_2i_1)")+
   p("而各自功率之和为 $p_1+p_2=u_1i_1+u_2i_2$，两者相差交叉项：")+
   fml("p - (p_1+p_2) = u_1i_2+u_2i_1 \\ne 0")+
   p("故功率不是线性量，不能用叠加定理计算，必须先叠加电压电流再求功率。"))+
   note(p("叠加定理也不能用于含非线性元件的电路；受控源始终保留，不参与单独作用的置零操作。"))
 )},
]},
{
"name": "4.2 替代定理",
"color": "#ea580c",
"desc": "用等效独立源替代已知支路",
"items": [
{"id":"ci4s2-1","name":"替代定理","tags":["thm","der"],"brief":"已知支路电压或电流可用等值独立源替代。",
 "body": wrap(
   thm("替代定理", p("若电路中某条支路的电压 $u_k$ 或电流 $i_k$ 已知，则可用一个电压为 $u_k$ 的理想电压源（或电流为 $i_k$ 的理想电流源）替代该支路，替代后电路其余各处的电压、电流均不变。"))+
   der(p("<strong>由解的唯一性证明：</strong>设原电路与替代后电路的节点方程分别为：")+
   fml("\\mathbf{G}\\,\\mathbf{u}_n=\\mathbf{i}_S,\\qquad \\mathbf{G}'\\mathbf{u}_n'=\\mathbf{i}_S'")+
   p("替代前后网络结构未变（只改变了该支路的元件类型），且该支路端口电压（或电流）被强制保持为原值，因此两组方程除该支路外完全相同。由线性方程组解的唯一性，其余节点电压与原电路一致，故其余支路电流不变。"))+
   note(p("替代定理对线性和非线性电路都适用，只要该支路的电压或电流已知。"))
 )},
{"id":"ci4s2-2","name":"替代定理与等效变换的区别","tags":["der","note"],"brief":"替代定理是局部替换，等效变换是对外等效。",
 "body": wrap(
   der(p("<strong>概念辨析：</strong>替代定理要求被替代支路的电压或电流等于原值，替代后<strong>仅该支路</strong>的元件被更换，替换元件本身可能吸收/发出不等于原来的功率；而等效变换要求两个单口网络<strong>对外端口</strong>伏安关系完全相同，内部可以完全不同。")+
   fml("\\text{替代}:\\ u_k\\ \\text{或}\\ i_k\\ \\text{保持不变},\\ \\text{内部功率变}")+
   p("等效变换则强调端口之外的一切响应相同。替代定理的适用面更广，但通常只用于化简某一个已知量的支路。"))+
   note(p("替代定理是戴维南定理等许多定理证明的基础。"))
 )},
{"id":"ci4s2-3","name":"替代定理的应用算例","tags":["exa","der"],"brief":"用电流源替代已知支路简化电路。",
 "body": wrap(
   exa(p("<strong>例：</strong>某电路中已知一条支路的电流为 $i_k=2\\,\\text{A}$，流经该支路两个节点 $a$、$b$（由 $a$ 流向 $b$）。为求其余支路电流，可用一个方向由 $a$ 指向 $b$ 的 $2\\,\\text{A}$ 理想电流源替代该支路。"))+
   der(p("替代后对节点 $a$、$b$ 重新列 KCL，由于电流源直接给出该支路电流，原支路中的电阻不再出现在方程中：")+
   fml("\\sum_{j\\ne k} i_j \\pm i_k = 0")+
   p("方程数目减少，求解更简便。例如原支路为 $R_k$ 时，替代后无需再写 $i_k=\\frac{u_a-u_b}{R_k}$ 的元件方程，直接用已知的 $i_k$ 代入即可。"))+
   note(p("若已知的是支路电压，则用理想电压源替代；已知电流则用理想电流源替代，二者不可混用。"))
 )},
]},
{
"name": "4.3 戴维南定理与诺顿定理",
"color": "#d97706",
"desc": "含源单口网络的等效化简",
"items": [
{"id":"ci4s3-1","name":"戴维南定理","tags":["thm","der"],"brief":"含源线性单口网络可等效为电压源串电阻。",
 "fig":"thevenin","figCap":"戴维南等效：开路电压 u_oc 串联等效电阻 R_eq",
 "body": wrap(
   thm("戴维南定理", p("任何含独立源的线性单口网络，对外电路而言，都可以用一个理想电压源 $u_{oc}$ 与一个电阻 $R_{eq}$ 串联来等效，其中 $u_{oc}$ 为该网络端口开路时的电压，$R_{eq}$ 为网络内全部独立源置零后的等效电阻。"))+
   der(p("<strong>用叠加定理推导：</strong>端口电压 $u$ 可看作网络内独立源单独作用与端口外接电流源 $i$ 单独作用两者的叠加。前者使端口开路，贡献开路电压 $u_{oc}$；后者把内部独立源置零，得到无源网络，外接电流 $i$ 在其等效电阻上产生电压降 $-R_{eq}i$（电流流入端口取负）。故：")+
   fml("u = u_{oc} - R_{eq}\\,i")+
   p("这正是理想电压源 $u_{oc}$ 串联电阻 $R_{eq}$ 的伏安关系，定理得证。"))+
   app(p("<strong>应用：</strong>戴维南定理把复杂网络简化为两元件模型，便于分析负载变化时的端口行为。"))
 )},
{"id":"ci4s3-2","name":"等效电阻的求法","tags":["der","exa"],"brief":"开路短路法、外加电源法与无损源法。",
 "body": wrap(
   der(p("<strong>方法一（开路—短路法）：</strong>分别求端口开路电压 $u_{oc}$ 与短路电流 $i_{sc}$，则：")+
   fml("R_{eq} = \\frac{u_{oc}}{i_{sc}}")+
   p("注意只能在端口外部短路，且需保证短路电流有限。"))+
   der(p("<strong>方法二（外加电源法）：</strong>把网络内全部独立源置零，在端口外加电压 $u$ 测电流 $i$（或外加电流测电压）：")+
   fml("R_{eq} = \\frac{u}{i}")+
   p("该方法对含受控源网络同样适用，且受控源必须保留。"))+
   der(p("<strong>方法三（无损源法）：</strong>若网络内部不含受控源，仅由电阻构成（独立源置零后），可直接用串并联或 Δ–Y 化简求得 $R_{eq}$。"))+
   exa(p("<strong>例：</strong>$6\\,\\text{V}$ 电压源串 $3\\,\\Omega$ 再并 $6\\,\\Omega$，开路电压 $u_{oc}=6\\times\\frac{6}{3+6}=4\\,\\text{V}$，无损源后 $R_{eq}=3\\|6=2\\,\\Omega$。"))+
   note(p("含受控源时等效电阻可能为负，表示网络可向外部提供功率。"))
 )},
{"id":"ci4s3-3","name":"诺顿定理与两定理关系","tags":["thm","der"],"brief":"含源网络可等效为电流源并电阻。",
 "fig":"norton","figCap":"诺顿等效：短路电流 i_sc 并联等效电阻 R_eq",
 "body": wrap(
   thm("诺顿定理", p("任何含独立源的线性单口网络，对外都可等效为一个理想电流源 $i_{sc}$ 与一个电阻 $R_{eq}$ 并联，其中 $i_{sc}$ 为端口短路电流，$R_{eq}$ 与戴维南等效电阻相同。"))+
   der(p("<strong>由电源等效变换推导：</strong>戴维南等效为电压源 $u_{oc}$ 串联 $R_{eq}$，应用有伴电压源到有伴电流源的等效变换：")+
   fml("i_{sc} = \\frac{u_{oc}}{R_{eq}}")+
   p("即得诺顿等效为电流源 $i_{sc}$ 并联 $R_{eq}$。两种等效对外电路完全等价：")+
   fml("u = u_{oc} - R_{eq}i \\ \\Longleftrightarrow\\ i = i_{sc} - \\frac{u}{R_{eq}}"))+
   app(p("<strong>应用：</strong>戴维南模型便于分析负载电压，诺顿模型便于分析负载电流；用哪个取决于所需未知量。"))
 )},
]},
{
"name": "4.4 最大功率传输定理",
"color": "#ea580c",
"desc": "负载获得最大功率的条件与效率",
"items": [
{"id":"ci4s4-1","name":"最大功率传输条件","tags":["thm","der"],"brief":"负载电阻等于等效电阻时获得最大功率。",
 "fig":"max_power","figCap":"负载功率随负载电阻变化，在 R_L=R_eq 处取得最大值",
 "body": wrap(
   thm("最大功率传输定理", p("给定的含源线性单口网络向可变负载 $R_L$ 供电时，当负载电阻等于网络等效电阻时，负载获得最大功率：")+
   fml("R_L = R_{eq},\\qquad P_{max}=\\frac{u_{oc}^2}{4R_{eq}}"))+
   der(p("<strong>推导：</strong>把网络化为戴维南等效，则负载电流与功率为：")+
   fml("i = \\frac{u_{oc}}{R_{eq}+R_L},\\qquad P_L = i^2 R_L = \\frac{u_{oc}^2 R_L}{(R_{eq}+R_L)^2}")+
   p("对 $R_L$ 求导并令其为零：")+
   fml("\\frac{dP_L}{dR_L} = u_{oc}^2\\frac{(R_{eq}+R_L)^2-2R_L(R_{eq}+R_L)}{(R_{eq}+R_L)^4}=0")+
   p("化简得 $(R_{eq}+R_L)^2-2R_L(R_{eq}+R_L)=0$，即 $R_{eq}^2-R_L^2=0$，故 $R_L=R_{eq}$。代回功率表达式：")+
   fml("P_{max}=\\frac{u_{oc}^2 R_{eq}}{(2R_{eq})^2}=\\frac{u_{oc}^2}{4R_{eq}}"))+
   note(p("该条件是极大值，功率对 $R_L$ 在匹配点两侧均下降。"))
 )},
{"id":"ci4s4-2","name":"匹配时的效率","tags":["der","note"],"brief":"匹配时传输效率恰为 50%。",
 "body": wrap(
   der(p("在匹配 $R_L=R_{eq}$ 时，负载功率为 $P_L=\\frac{u_{oc}^2}{4R_{eq}}$，电源总输出功率为：")+
   fml("P_{total}=i^2(R_{eq}+R_L)=\\frac{u_{oc}^2}{4R_{eq}}\\cdot 2=\\frac{u_{oc}^2}{2R_{eq}}")+
   p("故传输效率为：")+
   fml("\\eta = \\frac{P_L}{P_{total}} = \\frac{1}{2} = 50\\%")+
   p("即最大功率传输时有一半功率消耗在网络等效内阻上。"))+
   note(p("最大功率传输与最高效率是两种不同的优化目标：电力系统追求高效率（$R_L\\gg R_{eq}$），而通信、电子电路追求最大功率传输。"))
 )},
{"id":"ci4s4-3","name":"最大功率匹配的应用与局限","tags":["der","exa","app"],"brief":"阻抗匹配在电子系统中的应用。",
 "body": wrap(
   exa(p("<strong>例：</strong>某信号源内阻 $R_{eq}=50\\,\\Omega$，开路电压 $10\\,\\text{V}$，接 $50\\,\\Omega$ 负载时获得最大功率：")+
   fml("P_{max}=\\frac{10^2}{4\\times50}=0.5\\,\\text{W}"))+
   der(p("<strong>交流共轭匹配的推导：</strong>设电源内阻抗 $Z_{eq}=R_{eq}+jX_{eq}$、负载 $Z_L=R_L+jX_L$，电源有效值相量 $\\dot{U}_S$，则负载电流与有功功率为：")+
   fml("P_L=I^2R_L=\\frac{U_S^2 R_L}{(R_{eq}+R_L)^2+(X_{eq}+X_L)^2}")+
   p("先对电抗 $X_L$ 优化：当 $X_L=-X_{eq}$ 时分母最小，功率最大。再对 $R_L$ 求导并令其为零，得 $R_L=R_{eq}$。故交流最大功率传输条件为负载阻抗等于电源内阻抗的共轭：")+
   fml("Z_L=Z_{eq}^{*}\\implies P_{max}=\\frac{U_S^2}{4R_{eq}}"))+
   app(p("<strong>应用：</strong>射频传输线、音频功放输出、天线馈电等场合均采用阻抗匹配以最大程度传递功率。"))+
   note(p("对电力系统，匹配意味着总有一半功率损耗在内阻上，效率极低，故必须避免。"))
 )},
]},
{
"name": "4.5 互易定理与对偶原理",
"color": "#c2410c",
"desc": "线性网络的对偶与互易性质",
"items": [
{"id":"ci4s5-1","name":"互易定理","tags":["thm","der"],"brief":"线性无源网络激励与响应可互换位置。",
 "body": wrap(
   thm("互易定理", p("对一个仅含线性电阻（无独立源、无受控源）的二端口网络，若在端口 1 加激励而在端口 2 测量响应，与在端口 2 加同样的激励、在端口 1 测量响应，所得结果相同。例如：")+
   fml("\\frac{u_2}{i_1}\\Big|_{\\text{激励在1}} = \\frac{u_1}{i_2}\\Big|_{\\text{激励在2}}"))+
   der(p("<strong>由网孔方程推导：</strong>无源线性网络的网孔方程为 $\\mathbf{R}\\mathbf{i}=\\mathbf{u}_S$，其中 $\\mathbf{R}$ 为对称矩阵（$R_{kj}=R_{jk}$）。若单独在网孔 1 加激励 $u_{S1}$，则：")+
   fml("i_2 = \\frac{\\det(\\text{替换第2列})}{\\det\\mathbf{R}} = \\frac{-R_{21}}{\\det\\mathbf{R}}u_{S1}")+
   p("若改在网孔 2 加同样的激励，则由 $R_{21}=R_{12}$ 得 $i_1=\\frac{-R_{12}}{\\det\\mathbf{R}}u_{S2}$。因 $R_{12}=R_{21}$，两种情形响应对称相等，互易定理成立。"))+
   note(p("互易定理只对线性且不含受控源的网络成立；含受控源时 $\\mathbf{R}$ 可能不对称，互易性被破坏。"))
 )},
{"id":"ci4s5-2","name":"对偶原理","tags":["def","der"],"brief":"电阻与电导、电压与电流等成对偶，方程结构相同。",
 "body": wrap(
   defn("对偶量", p("电路中成对出现的量称为对偶量，例如：电阻 $R$ 与电导 $G$、电压 $u$ 与电流 $i$、电压源与电流源、串联与并联、网孔与节点、磁链与电荷。把电路中的每个量换成其对偶量，得到对偶电路。"))+
   der(p("<strong>对偶方程结构相同：</strong>欧姆定律与电容、电感的伏安关系在对偶替换下保持形式：")+
   fml("u = Ri\\ \\longleftrightarrow\\ i = Gu")+
   fml("i = C\\frac{du}{dt}\\ \\longleftrightarrow\\ u = L\\frac{di}{dt}")+
   p("网孔方程 $\\sum R i_m = \\sum u_S$ 与节点方程 $\\sum G u_n = \\sum i_S$ 也互为对偶。因此求解一个电路的结论可通过对偶关系直接移植到对偶电路。"))+
   exa(p("<strong>例：</strong>RC 电路的时间常数 $\\tau=RC$ 与 RL 电路的时间常数 $\\tau=L/R$ 互为对偶；串联谐振 $\\omega_0=1/\\sqrt{LC}$ 与并联谐振同式也体现对偶。"))+
   note(p("对偶原理不改变方程的形式结构，是理解与记忆电路规律的有力工具。"))
 )},
]},
]

ch5_sections = [
{
"name": "5.1 电容元件",
"color": "#be185d",
"desc": "电容的伏安关系、储能与连接",
"items": [
{"id":"ci5s1-1","name":"电容元件与伏安关系","tags":["def","der"],"brief":"q=Cu，电流正比于电压变化率。",
 "fig":"capacitor","figCap":"电容元件的电荷、电压与电流关系",
 "body": wrap(
   defn("电容元件", p("电容元件是储存电场能量的二端元件，其电荷与端电压成正比：")+
   fml("q = C\\,u")+
   p("其中 $C$ 为电容，单位法拉 F。线性电容的 $q$-$u$ 特性为过原点的直线。"))+
   der(p("<strong>由电荷关系推出伏安关系：</strong>对 $q=Cu$ 两边求时间导数，并利用 $i=dq/dt$：")+
   fml("i = \\frac{dq}{dt} = \\frac{d(Cu)}{dt} = C\\frac{du}{dt}")+
   p("可见电容电流正比于电压的变化率。反过来积分可得：")+
   fml("u(t) = u(t_0)+\\frac{1}{C}\\int_{t_0}^{t} i\\,d\\xi")+
   p("若电压不变（直流稳态），则 $i=0$，电容相当于开路，故称电容具有<strong>隔直通交</strong>特性。"))+
   note(p("电容电压不能跃变，否则需要无穷大电流，这一记忆特性是换路定则的基础。"))
 )},
{"id":"ci5s1-2","name":"电容的储能","tags":["der"],"brief":"存储能量 w=½Cu²。",
 "body": wrap(
   der(p("<strong>推导储能：</strong>电容从零电压充到 $u$ 所吸收的能量为功率的积分：")+
   fml("w_C = \\int_{0}^{t} u\\,i\\,d\\xi = \\int_{0}^{t} u\\cdot C\\frac{du}{d\\xi}\\,d\\xi")+
   p("整理后对电压积分：")+
   fml("w_C = C\\int_{0}^{u} u\\,du = \\frac{1}{2}C u^2")+
   p("能量全部储存在电容的电场中。当电压回到零时电容可释放全部能量，故电容是<strong>储能元件</strong>而非耗能元件。"))+
   note(p("能量只取决于当前电压值，与充放电历史无关，说明电容为无记忆储能元件。"))
 )},
{"id":"ci5s1-3","name":"电容的串联与并联","tags":["der","exa"],"brief":"串联等效电容倒数相加，并联相加。",
 "body": wrap(
   der(p("<strong>串联：</strong>串联的电容流过同一电流，故各电容电荷相同 $q$。由 KVL：")+
   fml("u = u_1+u_2+\\cdots = q\\left(\\frac{1}{C_1}+\\frac{1}{C_2}+\\cdots\\right)")+
   p("故等效电容为：")+
   fml("\\frac{1}{C_{eq}} = \\sum_k \\frac{1}{C_k}")+
   p("串联总电容小于任一分电容，且各电容分压与电容成反比。"))+
   der(p("<strong>并联：</strong>并联电容承受同一电压，由 KCL 得总电荷等于各电荷之和：")+
   fml("q = \\sum_k q_k = \\left(\\sum_k C_k\\right)u \\implies C_{eq} = \\sum_k C_k"))+
   exa(p("<strong>例：</strong>$C_1=2\\,\\mu\\text{F}$、$C_2=2\\,\\mu\\text{F}$ 串联得 $1\\,\\mu\\text{F}$；并联得 $4\\,\\mu\\text{F}$，恰与电阻规律相反。"))+
   note(p("电容串并联规律与电阻串并联规律互为对偶。"))
 )},
]},
{
"name": "5.2 电感元件",
"color": "#db2777",
"desc": "电感的伏安关系、储能与连接",
"items": [
{"id":"ci5s2-1","name":"电感元件与伏安关系","tags":["def","der"],"brief":"ψ=Li，电压正比于电流变化率。",
 "fig":"inductor","figCap":"电感元件的磁链、电流与电压关系",
 "body": wrap(
   defn("电感元件", p("电感元件是储存磁场能量的二端元件，其磁链与电流成正比：")+
   fml("\\psi = L\\,i")+
   p("其中 $L$ 为电感，单位亨利 H。线性电感的 $\\psi$-$i$ 特性为过原点的直线。"))+
   der(p("<strong>由法拉第电磁感应定律推出伏安关系：</strong>由 $\\psi=Li$ 两边求导，并利用感应电压 $u=d\\psi/dt$：")+
   fml("u = \\frac{d\\psi}{dt} = \\frac{d(Li)}{dt} = L\\frac{di}{dt}")+
   p("可见电感电压正比于电流变化率。积分形式为：")+
   fml("i(t) = i(t_0)+\\frac{1}{L}\\int_{t_0}^{t} u\\,d\\xi")+
   p("若电流不变（直流稳态），则 $u=0$，电感相当于短路，故称电感具有<strong>通直阻交</strong>特性。"))+
   note(p("电感电流不能跃变，否则需要无穷大电压，这也是换路定则的基础。"))
 )},
{"id":"ci5s2-2","name":"电感的储能","tags":["der"],"brief":"存储能量 w=½Li²。",
 "body": wrap(
   der(p("<strong>推导储能：</strong>电感从零电流增到 $i$ 所吸收的能量为：")+
   fml("w_L = \\int_{0}^{t} u\\,i\\,d\\xi = \\int_{0}^{t} i\\cdot L\\frac{di}{d\\xi}\\,d\\xi")+
   p("对电流积分：")+
   fml("w_L = L\\int_{0}^{i} i\\,di = \\frac{1}{2}L i^2")+
   p("能量全部储存在电感周围的磁场中。电流回到零时能量全部释放，电感也是储能元件。"))+
   note(p("电感的伏安关系与储能公式恰好与电容成对偶，对应 $C\\leftrightarrow L$、$u\\leftrightarrow i$。"))
 )},
{"id":"ci5s2-3","name":"电感的串联、并联与对偶","tags":["der","exa"],"brief":"串联相加，并联倒数相加。",
 "body": wrap(
   der(p("<strong>串联：</strong>串联电感流过同一电流，由 KVL 得各电压之和：")+
   fml("u = L_1\\frac{di}{dt}+L_2\\frac{di}{dt}+\\cdots = \\left(\\sum_k L_k\\right)\\frac{di}{dt}")+
   p("故 $L_{eq}=\\sum_k L_k$，串联总电感增大。"))+
   der(p("<strong>并联：</strong>并联电感承受同一电压，由 KCL 得各电流之和：")+
   fml("i = \\sum_k i_k,\\qquad \\frac{u}{L_{eq}}=\\sum_k \\frac{u}{L_k} \\implies \\frac{1}{L_{eq}}=\\sum_k \\frac{1}{L_k}"))+
   exa(p("<strong>例：</strong>$L_1=4\\,\\text{H}$、$L_2=4\\,\\text{H}$ 串联得 $8\\,\\text{H}$；并联得 $2\\,\\text{H}$。"))+
   note(p("电感串并联规律与电阻相同，与电容相反；这正是电容—电感对偶的体现。"))
 )},
]},
{
"name": "5.3 换路定则与初始值",
"color": "#ec4899",
"desc": "动态元件初始状态与 0+ 等效电路",
"items": [
{"id":"ci5s3-1","name":"换路定则","tags":["thm","der"],"brief":"电容电压与电感电流在换路瞬间不能跃变。",
 "body": wrap(
   thm("换路定则", p("设换路发生在 $t=0$ 时刻，则电容电压与电感电流连续：")+
   fml("u_C(0_+)=u_C(0_-),\\qquad i_L(0_+)=i_L(0_-)"))+
   der(p("<strong>推导：</strong>若电容电压在换路瞬间发生跃变 $\\Delta u$，则所需电流为冲激电流：")+
   fml("i = C\\frac{du}{dt} \\to \\infty\\ (\\text{有限功率源无法提供})")+
   p("同理若电感电流跃变，则所需电压为冲激电压：")+
   fml("u = L\\frac{di}{dt} \\to \\infty")+
   p("在有限功率的实际电路中不允许出现无穷大电压电流，故 $u_C$ 与 $i_L$ 必须连续，换路定则成立。"))+
   note(p("换路定则只约束电容电压与电感电流，其余电压电流可以跃变。"))
 )},
{"id":"ci5s3-2","name":"初始值的计算","tags":["der","exa"],"brief":"由 0− 状态求 0+ 各量。",
 "body": wrap(
   der(p("<strong>计算步骤：</strong>第一步，分析 $t=0_-$ 时的稳态（电容开路、电感短路）求出 $u_C(0_-)$ 与 $i_L(0_-)$；第二步，由换路定则得 $u_C(0_+)$、$i_L(0_+)$；第三步，画出 $t=0_+$ 时刻的等效电路，用 KCL、KVL 求其余初始值。"))+
   fml("u_C(0_+) = u_C(0_-),\\quad i_L(0_+)=i_L(0_-),\\quad \\text{其余量由直流电阻电路求}")+
   exa(p("<strong>例：</strong>$t<0$ 时开关断开，电容经 $5\\,\\Omega$ 接 $10\\,\\text{V}$ 电源已达稳态，则 $u_C(0_-)=10\\,\\text{V}$，换路后 $u_C(0_+)=10\\,\\text{V}$，即使此时电源被断开也保持不变。"))+
   note(p("电容电压与电感电流不能突变，但电容电流、电感电压以及电阻上的电压电流可以突变。"))
 )},
{"id":"ci5s3-3","name":"0+ 等效电路","tags":["der","note"],"brief":"电容用电压源、电感用电流源替代。",
 "body": wrap(
   der(p("<strong>建立 0+ 等效电路：</strong>在 $t=0_+$ 瞬间，把电容用一个电压为 $u_C(0_+)$ 的理想电压源替代，把电感用一个电流为 $i_L(0_+)$ 的理想电流源替代，其余电阻与独立源保持不变，即得 $0_+$ 时刻的电阻电路。")+
   fml("C \\to u_C(0_+)\\ \\text{电压源},\\qquad L \\to i_L(0_+)\\ \\text{电流源}")+
   p("对该电阻电路列 KCL、KVL，即可求出 $0_+$ 时刻所有电阻上的电压和电流。"))+
   app(p("<strong>应用：</strong>0+ 等效电路是求一阶、二阶电路全响应三要素中初始值的关键步骤，也为判断电路能否发生振荡提供初始条件。"))
 )},
]},
{
"name": "5.4 一阶电路的响应",
"color": "#9d174d",
"desc": "RC、RL 电路的零输入、零状态与全响应",
"items": [
{"id":"ci5s4-1","name":"RC 电路的零输入响应","tags":["der","thm"],"brief":"已充电电容经电阻放电呈指数衰减。",
 "fig":"rc_charge","figCap":"RC 电路充电过程，时间常数 τ=RC",
 "body": wrap(
   der(p("<strong>建立方程：</strong>已充电到 $U_0$ 的电容 $C$ 经电阻 $R$ 放电，由 KVL 得：")+
   fml("R i + u_C = 0,\\qquad i = C\\frac{du_C}{dt}")+
   p("代入得关于 $u_C$ 的一阶齐次微分方程：")+
   fml("RC\\frac{du_C}{dt}+u_C=0 \\implies \\frac{du_C}{dt}=-\\frac{1}{RC}u_C")+
   p("分离变量并积分，代入初始条件 $u_C(0_+)=U_0$：")+
   fml("u_C(t)=U_0 e^{-t/RC}=U_0 e^{-t/\\tau},\\qquad \\tau=RC")+
   p("电压按时间常数 $\\tau$ 指数衰减，$\\tau$ 越小衰减越快。"))+
   note(p("工程上认为经过 $(3\\sim5)\\tau$ 后暂态过程基本结束，电容电压衰减到初值的 5% 以下。"))
 )},
{"id":"ci5s4-2","name":"RC 零状态响应与三要素法","tags":["der","exa"],"brief":"零状态充电为 u=U(1−e^(−t/τ))，全响应由三要素确定。",
 "body": wrap(
   der(p("<strong>零状态响应：</strong>电容初始电压为零，换路后接直流电压源 $U$，方程与解为：")+
   fml("RC\\frac{du_C}{dt}+u_C=U,\\qquad u_C(0_+)=0")+
   p("其特解（稳态）为 $u_C(\\infty)=U$，通解为齐次解加特解，代入初值得：")+
   fml("u_C(t)=U\\left(1-e^{-t/\\tau}\\right)"))+
   der(p("<strong>三要素法：</strong>一阶电路任意响应均可写成统一形式，只需求三个要素——初始值 $f(0_+)$、稳态值 $f(\\infty)$ 与时间常数 $\\tau$：")+
   fml("f(t)=f(\\infty)+\\left[f(0_+)-f(\\infty)\\right]e^{-t/\\tau}")+
   p("该式对 RC、RL 电路以及任意一阶变量都成立，是求解一阶电路最常用的方法。"))+
   exa(p("<strong>例：</strong>$R=1\\,\\text{k}\\Omega$、$C=1\\,\\mu\\text{F}$，则 $\\tau=1\\,\\text{ms}$，接 $5\\,\\text{V}$ 时 $u_C(t)=5(1-e^{-t/\\text{ms}})\\,\\text{V}$。"))+
   note(p("时间常数 $\\tau=RC$ 只由电路参数决定，与激励无关。"))
 )},
{"id":"ci5s4-3","name":"RL 电路的响应","tags":["der","thm"],"brief":"电感电流呈指数变化，时间常数 τ=L/R。",
 "fig":"rl_decay","figCap":"RL 电路电感电流的指数衰减，时间常数 τ=L/R",
 "body": wrap(
   der(p("<strong>零输入响应：</strong>有初始电流 $I_0$ 的电感经电阻闭合，由 KVL：")+
   fml("L\\frac{di_L}{dt}+R i_L=0 \\implies i_L(t)=I_0 e^{-t/\\tau},\\qquad \\tau=\\frac{L}{R}")+
   p("电感电流按时间常数 $\\tau=L/R$ 指数衰减。"))+
   der(p("<strong>零状态响应：</strong>电感初始电流为零，接电压源 $U$，则：")+
   fml("L\\frac{di_L}{dt}+R i_L=U \\implies i_L(t)=\\frac{U}{R}\\left(1-e^{-t/\\tau}\\right)")+
   p("稳态时 $i_L(\\infty)=U/R$，电感相当于短路。"))+
   exa(p("<strong>例：</strong>$L=1\\,\\text{H}$、$R=10\\,\\Omega$，则 $\\tau=0.1\\,\\text{s}$；接 $20\\,\\text{V}$ 时 $i_L(\\infty)=2\\,\\text{A}$。"))+
   note(p("RL 电路的 $\\tau=L/R$ 与 RC 电路的 $\\tau=RC$ 互为对偶。"))
 )},
]},
{
"name": "5.5 二阶电路的响应",
"color": "#831843",
"desc": "RLC 电路的特征根与三种阻尼",
"items": [
{"id":"ci5s5-1","name":"RLC 串联电路的方程与特征根","tags":["der"],"brief":"建立二阶方程并求特征根。",
 "fig":"rlc_series","figCap":"串联 RLC 电路",
 "body": wrap(
   der(p("<strong>建立方程：</strong>串联 RLC 电路接电压源 $u_S$，由 KVL：")+
   fml("L\\frac{di}{dt}+Ri+u_C=u_S,\\qquad i=C\\frac{du_C}{dt}")+
   p("把 $i$ 用 $u_C$ 表示后代入，得关于 $u_C$ 的二阶微分方程：")+
   fml("LC\\frac{d^2u_C}{dt^2}+RC\\frac{du_C}{dt}+u_C=u_S")+
   p("其齐次方程对应的特征方程为：")+
   fml("LC s^2+RC s+1=0 \\implies s^2+\\frac{R}{L}s+\\frac{1}{LC}=0")+
   p("解得特征根：")+
   fml("s_{1,2}=-\\alpha\\pm\\sqrt{\\alpha^2-\\omega_0^2},\\qquad \\alpha=\\frac{R}{2L},\\ \\omega_0=\\frac{1}{\\sqrt{LC}}"))+
   note(p("$\\alpha$ 为衰减系数，$\\omega_0$ 为固有（谐振）角频率，二者决定响应的性质。"))
 )},
{"id":"ci5s5-2","name":"三种阻尼情形","tags":["der","exa"],"brief":"按 α 与 ω₀ 的大小分过阻尼、临界与欠阻尼。",
 "fig":"damping","figCap":"过阻尼、临界阻尼与欠阻尼三种响应曲线",
 "body": wrap(
   der(p("<strong>判别依据：</strong>由特征根 $s_{1,2}=-\\alpha\\pm\\sqrt{\\alpha^2-\\omega_0^2}$ 的判别式 $\\alpha^2-\\omega_0^2$ 的符号分三种情况：")+
   fml("\\alpha>\\omega_0:\\ s_{1,2}\\ \\text{为两不等负实根（过阻尼）}")+
   fml("\\alpha=\\omega_0:\\ s_{1,2}=-\\alpha\\ \\text{为重根（临界阻尼）}")+
   fml("\\alpha<\\omega_0:\\ s_{1,2}=-\\alpha\\pm j\\omega_d\\ \\text{为共轭复根（欠阻尼）}")+
   p("其中欠阻尼的振荡角频率为 $\\omega_d=\\sqrt{\\omega_0^2-\\alpha^2}$，响应为衰减振荡：")+
   fml("u_C(t)=A e^{-\\alpha t}\\cos(\\omega_d t+\\theta)"))+
   exa(p("<strong>例：</strong>当 $R<2\\sqrt{L/C}$ 时 $\\alpha<\\omega_0$，电路欠阻尼，会出现衰减振荡与超调；增大 $R$ 使其过阻尼，响应单调收敛，无超调。"))+
   note(p("过阻尼与临界阻尼响应不振荡，欠阻尼响应振荡衰减；临界阻尼是振与非振荡的临界状态。"))
 )},
]},
]

ch6_sections = [
{
"name": "6.1 正弦量与相量",
"color": "#0891b2",
"desc": "正弦量三要素、有效值与相量表示",
"items": [
{"id":"ci6s1-1","name":"正弦量的三要素与有效值","tags":["def","der"],"brief":"幅值、角频率、初相决定正弦量，有效值为幅值的 1/√2。",
 "body": wrap(
   defn("正弦量三要素", p("正弦电压可写为 $u(t)=U_m\\sin(\\omega t+\\varphi)$，其中幅值 $U_m$、角频率 $\\omega=2\\pi f$、初相 $\\varphi$ 称为正弦量的三要素。"))+
   der(p("<strong>有效值的定义与推导：</strong>有效值（均方根值）定义为与直流发热等效的数值：")+
   fml("U = \\sqrt{\\frac{1}{T}\\int_{0}^{T} u^2\\,dt}")+
   p("代入正弦量并利用 $\\sin^2\\theta=\\frac{1-\\cos2\\theta}{2}$，一个周期内余弦项积分为零：")+
   fml("\\frac{1}{T}\\int_0^T U_m^2\\sin^2(\\omega t+\\varphi)\\,dt = \\frac{U_m^2}{2}")+
   p("故得正弦量的有效值：")+
   fml("U = \\frac{U_m}{\\sqrt{2}} \\approx 0.707\\,U_m"))+
   note(p("交流设备的额定电压、电流均指有效值，例如市电 220 V 对应幅值约 311 V。"))
 )},
{"id":"ci6s1-2","name":"相位差与相量表示","tags":["def","der"],"brief":"相量用复数表示正弦量，忽略频率因子。",
 "fig":"phasor","figCap":"旋转相量与正弦量一一对应",
 "body": wrap(
   defn("相量", p("在单一频率的正弦稳态电路中，正弦量 $u=U_m\\sin(\\omega t+\\varphi)$ 可对应一个复常数 $\\dot{U}=U\\angle\\varphi$（有效值相量），它包含幅值与初相信息，略去了共同的旋转因子。"))+
   der(p("<strong>由欧拉公式建立对应关系：</strong>")+
   fml("U_m e^{j(\\omega t+\\varphi)} = U_m\\cos(\\omega t+\\varphi)+jU_m\\sin(\\omega t+\\varphi)")+
   p("取虚部即得正弦量。因各量频率相同，公共因子 $e^{j\\omega t}$ 可略去，于是：")+
   fml("u(t)=\\Im\\{\\sqrt{2}\\dot{U}e^{j\\omega t}\\},\\qquad \\dot{U}=U\\angle\\varphi")+
   p("相量的模为有效值，辐角为初相。相位差 $\\varphi=\\varphi_u-\\varphi_i$ 决定电压超前还是滞后电流。"))+
   note(p("相量是复数而非正弦量本身，两者通过乘以 $e^{j\\omega t}$ 并取虚部相联系。"))
 )},
{"id":"ci6s1-3","name":"相量形式的 KCL 与 KVL","tags":["thm","der"],"brief":"正弦稳态中 KCL、KVL 可直接用相量求和。",
 "body": wrap(
   thm("相量形式基尔霍夫定律", p("正弦稳态下，节点电流相量的代数和为零、回路电压相量的代数和为零：")+
   fml("\\sum_k \\dot{I}_k = 0,\\qquad \\sum_k \\dot{U}_k = 0"))+
   der(p("<strong>推导：</strong>时域 KCL 为 $\\sum i_k(t)=0$。设各支路电流为同频率正弦量 $i_k=\\Im\\{\\sqrt2\\dot{I}_k e^{j\\omega t}\\}$，代入得：")+
   fml("\\Im\\left\\{\\sqrt2\\,e^{j\\omega t}\\sum_k \\dot{I}_k\\right\\}=0")+
   p("因该式对任意时刻 $t$ 均成立，且 $e^{j\\omega t}\\ne0$，故：")+
   fml("\\sum_k \\dot{I}_k=0")+
   p("KVL 同理。于是正弦稳态电路的全部分析方法（网孔法、节点法、叠加、戴维南等）都可直接移植到相量域。"))+
   app(p("<strong>应用：</strong>相量法把微分方程化为复数代数方程，是正弦稳态分析的核心工具。"))
 )},
]},
{
"name": "6.2 阻抗与导纳",
"color": "#0e7490",
"desc": "阻抗、导纳及 R、L、C 的相量关系",
"items": [
{"id":"ci6s2-1","name":"阻抗与导纳的定义","tags":["def","der"],"brief":"Z=U̇/İ，包含电阻与电抗。",
 "fig":"impedance_triangle","figCap":"阻抗三角形：R、X 与 |Z| 的几何关系",
 "body": wrap(
   defn("阻抗", p("无源单口网络端电压相量与电流相量之比定义为<strong>复阻抗</strong>：")+
   fml("Z = \\frac{\\dot{U}}{\\dot{I}} = |Z|\\angle\\varphi = R+jX")+
   p("其中 $|Z|$ 为阻抗模，$R$ 为电阻分量，$X$ 为电抗分量；其倒数 $Y=1/Z=G+jB$ 称为<strong>导纳</strong>。"))+
   der(p("<strong>阻抗三角形：</strong>由 $Z=R+jX$ 得：")+
   fml("|Z|=\\sqrt{R^2+X^2},\\qquad \\varphi=\\arctan\\frac{X}{R}")+
   p("当 $X>0$ 时 $\\varphi>0$，电压超前电流，网络呈感性；$X<0$ 时呈容性；$X=0$ 时纯电阻。"))+
   note(p("阻抗不是相量，而是复常数，其辐角即电压与电流的相位差。"))
 )},
{"id":"ci6s2-2","name":"R、L、C 的相量关系","tags":["der"],"brief":"电阻同相，电感电压超前 90°，电容电压滞后 90°。",
 "body": wrap(
   der(p("<strong>电阻：</strong>由 $u=Ri$，相量形式为：")+
   fml("\\dot{U}=R\\dot{I},\\qquad Z_R=R"))+
   der(p("<strong>电感：</strong>由 $u=L\\frac{di}{dt}$，对 $i=\\Im\\{\\sqrt2\\dot{I}e^{j\\omega t}\\}$ 求导得因子 $j\\omega$：")+
   fml("\\dot{U}=j\\omega L\\dot{I},\\qquad Z_L=j\\omega L = jX_L")+
   p("电压超前电流 $90°$，感抗 $X_L=\\omega L$ 随频率增大。"))+
   der(p("<strong>电容：</strong>由 $i=C\\frac{du}{dt}$，相量形式为 $\\dot{I}=j\\omega C\\dot{U}$，故：")+
   fml("\\dot{U}=\\frac{1}{j\\omega C}\\dot{I}=-j\\frac{1}{\\omega C}\\dot{I},\\qquad Z_C=-j\\frac{1}{\\omega C}")+
   p("电压滞后电流 $90°$，容抗随频率增大而减小。"))+
   exa(p("<strong>例：</strong>$\\omega=1000\\,\\text{rad/s}$，$L=0.1\\,\\text{H}$ 时 $X_L=100\\,\\Omega$；$C=10\\,\\mu\\text{F}$ 时 $X_C=100\\,\\Omega$。"))+
   note(p("记忆口诀：电感电流滞后电压、电容电流超前电压，二者相位差均为 90°。"))
 )},
{"id":"ci6s2-3","name":"阻抗的串并联与相量图","tags":["der","exa"],"brief":"阻抗串联相加、并联倒数相加，相量图辅助求解。",
 "body": wrap(
   der(p("<strong>串联：</strong>串联时电流相同，由相量 KVL：")+
   fml("\\dot{U}=\\dot{U}_1+\\dot{U}_2=(Z_1+Z_2)\\dot{I} \\implies Z_{eq}=Z_1+Z_2")+
   p("注意只能按复数相加，不能直接相加模值。"))+
   der(p("<strong>并联：</strong>并联时电压相同，由相量 KCL：")+
   fml("\\dot{I}=\\dot{I}_1+\\dot{I}_2=\\left(\\frac{1}{Z_1}+\\frac{1}{Z_2}\\right)\\dot{U} \\implies \\frac{1}{Z_{eq}}=\\frac{1}{Z_1}+\\frac{1}{Z_2}"))+
   exa(p("<strong>例：</strong>$Z_1=3+j4\\,\\Omega$ 与 $Z_2=3-j4\\,\\Omega$ 串联，$Z_{eq}=6\\,\\Omega$ 纯电阻，端口电压与电流同相。"))+
   app(p("<strong>相量图法：</strong>把各电压电流相量按 KCL/KVL 首尾相接画在复平面上，可由几何关系直接求出未知量，直观且便于校核。"))
 )},
]},
{
"name": "6.3 正弦稳态电路的功率",
"color": "#06b6d4",
"desc": "有功、无功、视在功率与复功率",
"items": [
{"id":"ci6s3-1","name":"瞬时功率与平均功率","tags":["der","thm"],"brief":"平均功率 P=UIcosφ。",
 "body": wrap(
   der(p("<strong>瞬时功率：</strong>设 $u=\\sqrt2 U\\sin(\\omega t)$、$i=\\sqrt2 I\\sin(\\omega t-\\varphi)$，则：")+
   fml("p=ui=2UI\\sin(\\omega t)\\sin(\\omega t-\\varphi)")+
   p("利用积化和差 $2\\sin A\\sin B=\\cos(A-B)-\\cos(A+B)$：")+
   fml("p=UI\\cos\\varphi-UI\\cos(2\\omega t-\\varphi)")+
   p("对一周期取平均，余弦振荡项积分为零，得<strong>有功功率</strong>：")+
   fml("P=\\frac{1}{T}\\int_0^T p\\,dt=UI\\cos\\varphi")+
   p("$\\cos\\varphi$ 称为功率因数，$\\varphi$ 为电压与电流的相位差。"))+
   note(p("纯电阻 $\\varphi=0$，$P=UI$；纯电感或纯电容 $\\varphi=\\pm90°$，平均功率为零，不消耗能量。"))
 )},
{"id":"ci6s3-2","name":"无功功率与视在功率","tags":["der","def"],"brief":"无功功率反映能量交换，视在功率为电压电流有效值之积。",
 "body": wrap(
   defn("无功功率与视在功率", p("瞬时功率中与电源往复交换的振幅定义为<strong>无功功率</strong> $Q=UI\\sin\\varphi$（单位乏 var）；电压与电流有效值之积称为<strong>视在功率</strong> $S=UI$（单位伏安 VA）。"))+
   der(p("<strong>三者关系：</strong>由 $P=UI\\cos\\varphi$、$Q=UI\\sin\\varphi$，利用 $\\cos^2+\\sin^2=1$ 得：")+
   fml("S=\\sqrt{P^2+Q^2}\\implies P=S\\cos\\varphi,\\ Q=S\\sin\\varphi")+
   p("三者构成直角三角形，$S$ 为斜边、$P$ 为邻边、$Q$ 为对边。感性负载 $Q>0$，容性负载 $Q<0$。"))+
   exa(p("<strong>例：</strong>某负载 $U=220\\,\\text{V}$、$I=5\\,\\text{A}$、$\\cos\\varphi=0.8$，则 $S=1100\\,\\text{VA}$，$P=880\\,\\text{W}$，$Q=660\\,\\text{var}$。"))+
   note(p("无功功率并不做功，但它是建立磁场、电场时必须的能量交换，影响设备容量的利用。"))
 )},
{"id":"ci6s3-3","name":"复功率与功率因数","tags":["der","exa"],"brief":"Ṡ=U̇İ* = P+jQ，功率因数为有功与视在之比。",
 "fig":"power_triangle","figCap":"功率三角形：P、Q、S 与功率因数",
 "body": wrap(
   der(p("<strong>复功率定义与展开：</strong>定义复功率为电压相量与电流共轭相量之积：")+
   fml("\\bar{S}=\\dot{U}\\dot{I}^{*}=(U\\angle\\varphi_u)(I\\angle-\\varphi_i)=UI\\angle(\\varphi_u-\\varphi_i)=UI\\angle\\varphi")+
   p("用欧拉公式展开：")+
   fml("\\bar{S}=UI\\cos\\varphi+jUI\\sin\\varphi=P+jQ")+
   p("复功率的实部为有功、虚部为无功，其模为视在功率。")+
   fml("\\cos\\varphi=\\frac{P}{S},\\qquad \\bar{S}=\\dot{U}\\dot{I}^{*}"))+
   exa(p("<strong>例：</strong>为提高功率因数，常在感性负载两端并联电容，用电容的超前无功补偿电感的滞后无功，使 $\\varphi$ 减小、$\\cos\\varphi$ 升高，从而减小线路电流与损耗。"))+
   note(p("复功率守恒：电路中各元件复功率之和为零，但视在功率一般不守恒。"))
 )},
]},
{
"name": "6.4 正弦稳态电路的分析",
"color": "#0891b2",
"desc": "相量法步骤、功率因数校正与相量图",
"items": [
{"id":"ci6s4-1","name":"相量法分析步骤","tags":["der","note"],"brief":"把时域电路化为相量电路，求解后转回时域。",
 "body": wrap(
   der(p("<strong>标准步骤：</strong>第一步，写出已知正弦量的相量；第二步，把 $R$、$L$、$C$ 换成相应的复阻抗 $R$、$j\\omega L$、$\\frac{1}{j\\omega C}$，得到相量模型；第三步，用直流电阻电路的一切方法（网孔、节点、叠加、戴维南等）求未知相量；第四步，把结果相量转回时域正弦量。")+
   fml("u(t)=\\Im\\{\\sqrt2\\dot{U}e^{j\\omega t}\\}")+
   p("整个过程把微分方程求解转化为复数代数方程求解，大大简化计算。"))+
   app(p("<strong>应用：</strong>交流网络分析、滤波器设计、电力系统潮流计算等均以相量法为基础。"))
 )},
{"id":"ci6s4-2","name":"功率因数校正","tags":["der","exa"],"brief":"并联电容提高功率因数。",
 "body": wrap(
   der(p("<strong>补偿电容的推导：</strong>设负载有功 $P$ 不变，要求把功率因数由 $\\cos\\varphi_1$ 提高到 $\\cos\\varphi_2$。补偿前无功为 $Q_1=P\\tan\\varphi_1$，补偿后为 $Q_2=P\\tan\\varphi_2$，需由电容提供的无功为：")+
   fml("Q_C=Q_1-Q_2=P(\\tan\\varphi_1-\\tan\\varphi_2)")+
   p("又 $Q_C=U^2\\omega C$，故所需电容为：")+
   fml("C=\\frac{P(\\tan\\varphi_1-\\tan\\varphi_2)}{\\omega U^2}")+
   p("并联电容不消耗有功，只是就地提供无功，减小电源与线路负担。"))+
   exa(p("<strong>例：</strong>$P=10\\,\\text{kW}$、$U=220\\,\\text{V}$、$f=50\\,\\text{Hz}$，把 $\\cos\\varphi$ 由 0.7 提到 0.95，可算得所需电容约 $\\mu\\text{F}$ 量级。"))+
   note(p("工厂配电中常采用同步补偿机或电容器组进行无功补偿，避免功率因数过低被罚款。"))
 )},
{"id":"ci6s4-3","name":"相量图法求电压电流","tags":["exa","der"],"brief":"用相量图几何关系求解复杂电路。",
 "body": wrap(
   exa(p("<strong>例：</strong>R 与 L 串联接电压 $\\dot{U}$，已知电阻电压 $\\dot{U}_R$ 与电感电压 $\\dot{U}_L$ 相差 $90°$，求总电压。"))+
   der(p("由相量 KVL：")+
   fml("\\dot{U}=\\dot{U}_R+\\dot{U}_L")+
   p("因 $\\dot{U}_R$ 与 $\\dot{U}_L$ 正交，其模满足勾股关系：")+
   fml("U=\\sqrt{U_R^2+U_L^2}")+
   p("相位角为 $\\varphi=\\arctan\\frac{U_L}{U_R}$，即总电压超前电流 $\\varphi$。相量图把代数运算化为几何关系，便于快速估算与校核。"))+
   note(p("多个支路时，先画参考相量（通常取并联支路的电压或串联支路的电流），再依次画出其余相量。"))
 )},
]},
{
"name": "6.5 谐振电路",
"color": "#22d3ee",
"desc": "串联谐振与并联谐振",
"items": [
{"id":"ci6s5-1","name":"串联谐振","tags":["der","thm"],"brief":"ωL=1/(ωC) 时端口呈纯电阻，电流最大。",
 "fig":"resonance_curve","figCap":"谐振曲线：ω=ω₀ 时电流达到最大",
 "body": wrap(
   thm("串联谐振", p("RLC 串联电路的阻抗为 $Z=R+j(\\omega L-\\frac{1}{\\omega C})$。当电抗为零时电路发生<strong>串联谐振</strong>，此时端口电压与电流同相：")+
   fml("\\omega_0 L=\\frac{1}{\\omega_0 C}\\implies \\omega_0=\\frac{1}{\\sqrt{LC}}"))+
   der(p("<strong>谐振特性推导：</strong>谐振时 $|Z|=R$ 最小，电流达到最大 $I_0=U/R$。电感与电容电压大小相等、相位相反：")+
   fml("U_L=U_C=\\omega_0 L\\cdot\\frac{U}{R}=QU")+
   p("定义品质因数：")+
   fml("Q=\\frac{\\omega_0 L}{R}=\\frac{1}{R}\\sqrt{\\frac{L}{C}}")+
   p("$Q$ 越高，谐振峰越尖锐，选频能力越强。"))+
   note(p("串联谐振时电感与电容上的电压可能远高于电源电压（$Q$ 倍），称为过电压现象，需注意绝缘。"))
 )},
{"id":"ci6s5-2","name":"并联谐振与通频带","tags":["der","exa"],"brief":"并联谐振时阻抗最大，通频带 BW=ω₀/Q。",
 "body": wrap(
   der(p("<strong>并联谐振：</strong>RLC 并联电路导纳为：")+
   fml("Y=G+j\\left(\\omega C-\\frac{1}{\\omega L}\\right)")+
   p("谐振条件仍为 $\\omega C=\\frac{1}{\\omega L}$，即：")+
   fml("\\omega_0=\\frac{1}{\\sqrt{LC}}")+
   p("谐振时导纳最小、阻抗最大，对电流源呈现最大电压。理想情况下谐振阻抗为 $Z_0=\\frac{L}{RC}$。"))+
   der(p("<strong>通频带：</strong>以电流或电压下降到峰值的 $1/\\sqrt2$（即 $-3\\,\\text{dB}$）定义上下截止频率 $\\omega_1$、$\\omega_2$，通频带宽度为：")+
   fml("BW=\\omega_2-\\omega_1=\\frac{\\omega_0}{Q}")+
   p("$Q$ 越大带宽越窄、选择性越好，但通带变窄、信号失真风险增大，需折中。"))+
   exa(p("<strong>例：</strong>$\\omega_0=10^6\\,\\text{rad/s}$、$Q=50$，则 $BW=2\\times10^4\\,\\text{rad/s}$。"))+
   note(p("谐振广泛用于选频、滤波与无线电接收机的调谐回路。"))
 )},
]},
]

ch7_sections = [
{
"name": "7.1 互感与耦合系数",
"color": "#4f46e5",
"desc": "互感现象、同名端与耦合系数",
"items": [
{"id":"ci7s1-1","name":"互感现象与互感系数","tags":["def","der"],"brief":"一线圈电流变化在另一线圈产生感应电压。",
 "fig":"mutual_inductance","figCap":"两线圈的互感耦合与同名端标记",
 "body": wrap(
   defn("互感现象", p("两个线圈相邻时，线圈 1 中电流 $i_1$ 产生的磁通部分穿过线圈 2，形成互感磁链 $\\psi_{21}=M i_1$，其中 $M$ 称为<strong>互感系数</strong>，单位亨利。"))+
   der(p("<strong>互感电压：</strong>由法拉第电磁感应定律，互感磁链变化在线圈 2 中感生电压：")+
   fml("u_{21}=\\frac{d\\psi_{21}}{dt}=M\\frac{di_1}{dt}")+
   p("同理线圈 2 的电流 $i_2$ 在线圈 1 中感生电压 $u_{12}=M\\frac{di_2}{dt}$，且互易 $M_{12}=M_{21}=M$。"))+
   note(p("互感电压的极性取决于两线圈的绕向与电流方向，工程上用同名端标记来统一描述。"))
 )},
{"id":"ci7s1-2","name":"同名端与互感电压极性","tags":["der","note"],"brief":"同名端流入电流产生的磁通相互增强。",
 "body": wrap(
   der(p("<strong>同名端定义：</strong>两线圈中电流分别从<strong>同名端</strong>（用圆点 • 标记）流入时，各自产生的磁通相互加强。据此可确定互感电压的符号。")+
   p("设线圈 1 电压参考方向为从同名端指向另一端，线圈 2 也如此取值，则互感电压为：")+
   fml("u_2 = M\\frac{di_1}{dt}\\ (\\text{同名端同向})")+
   fml("u_2 = -M\\frac{di_1}{dt}\\ (\\text{一进一出})")+
   p("在相量形式下互感电压对应 $j\\omega M\\dot{I}$，符号由同名端决定。"))+
   note(p("同名端由线圈实际绕向决定，与电流方向无关；测量时可通过观察感应电压极性判断同名端。"))
 )},
{"id":"ci7s1-3","name":"耦合系数","tags":["def","der"],"brief":"k=M/√(L₁L₂)，介于 0 与 1 之间。",
 "body": wrap(
   defn("耦合系数", p("表征两线圈耦合紧密程度的量定义为：")+
   fml("k=\\frac{M}{\\sqrt{L_1L_2}}"))+
   der(p("<strong>取值范围：</strong>两线圈全部磁通相互交链时 $k=1$，称为全耦合（理想变压器）；无耦合时 $k=0$。可以证明：")+
   fml("\\psi_{21}\\,\\psi_{12}\\le \\psi_{11}\\,\\psi_{22} \\implies M^2\\le L_1L_2 \\implies k\\le 1")+
   p("因为两个线圈间互相交链的磁通之积不会超过各自自感磁通之积。故 $0\\le k\\le 1$。"))+
   exa(p("<strong>例：</strong>空心变压器的耦合系数通常 $k<0.5$，而铁芯变压器的 $k$ 可达 0.99 以上。"))+
   note(p("$k$ 越接近 1，能量传递效率越高，漏感越小。"))
 )},
]},
{
"name": "7.2 含互感电路的分析",
"color": "#6366f1",
"desc": "互感串联、去耦等效与相量法",
"items": [
{"id":"ci7s2-1","name":"互感线圈的串联","tags":["der","exa"],"brief":"顺接 Leq=L₁+L₂+2M，反接为 L₁+L₂−2M。",
 "body": wrap(
   der(p("<strong>顺接（同向串联）：</strong>两线圈电流同向，自感电压与互感电压同号，总电压为：")+
   fml("u=L_1\\frac{di}{dt}+L_2\\frac{di}{dt}+2M\\frac{di}{dt}=(L_1+L_2+2M)\\frac{di}{dt}")+
   p("故等效电感：")+
   fml("L_{eq}=L_1+L_2+2M"))+
   der(p("<strong>反接（反向串联）：</strong>同名端反向串联时互感电压与自感电压反号：")+
   fml("L_{eq}=L_1+L_2-2M")+
   p("由顺接与反接两次测量可得 $M=\\frac{L_{顺}-L_{反}}{4}$，这是测量互感的常用方法。"))+
   exa(p("<strong>例：</strong>$L_1=L_2=4\\,\\text{H}$、$M=2\\,\\text{H}$，顺接 $L_{eq}=12\\,\\text{H}$，反接 $L_{eq}=4\\,\\text{H}$。"))+
   note(p("互感的存在使等效电感可能增大或减小，取决于连接方式。"))
 )},
{"id":"ci7s2-2","name":"去耦等效（T 形等效）","tags":["der"],"brief":"把互感化为无互感的 T 形电感网络。",
 "body": wrap(
   der(p("<strong>去耦原理：</strong>对具有公共端的两互感线圈，可用三个无互感电感（T 形连接）等效，使电路分析不再显含互感项。以同名端同侧连接为例，去耦等效电感为：")+
   fml("L_a=L_1-M,\\quad L_b=L_2-M,\\quad L_c=M")+
   p("其中 $L_a$、$L_b$ 为两外臂，$L_c$ 为公共臂。这样两线圈的互感耦合被转换为 T 形网络，可直接用串并联或节点法求解。"))+
   der(p("<strong>验证思路：</strong>分别写出原互感电路与 T 形网络在公共节点处的电压方程，比较两端口电压表达式：")+
   fml("u_1=j\\omega L_1\\dot{I}_1+j\\omega M\\dot{I}_2,\\quad u_2=j\\omega M\\dot{I}_1+j\\omega L_2\\dot{I}_2")+
   p("令 T 形网络的节点方程与之逐项相等，即可解得上述 $L_a$、$L_b$、$L_c$，说明两者端口特性完全一致。"))+
   note(p("去耦等效只对外部端口等效，内部电压电流不再与原来一一对应。"))
 )},
{"id":"ci7s2-3","name":"含互感电路的相量法","tags":["der","exa"],"brief":"用 jωM 表示互感耦合，列相量方程求解。",
 "body": wrap(
   der(p("<strong>相量模型：</strong>在正弦稳态下，互感电压的相量形式为：")+
   fml("\\dot{U}_2=j\\omega M\\dot{I}_1,\\qquad \\dot{U}_1=j\\omega M\\dot{I}_2")+
   p("把所有自感项写成 $j\\omega L\\dot{I}$、互感项写成 $\\pm j\\omega M\\dot{I}$，即可对含互感电路列网孔或节点方程。"))+
   exa(p("<strong>例：</strong>两网孔耦合电路，网孔 1 含 $L_1$、网孔 2 含 $L_2$，公共支路有互感 $M$。网孔 1 方程中互感项为 $\\mp j\\omega M\\dot{I}_{m2}$，符号由同名端相对电流方向决定。"))+
   app(p("<strong>应用：</strong>空心变压器、耦合谐振回路、无线充电线圈等均需用互感模型分析。求解时也可先做 T 形去耦，再用常规相量法。"))
 )},
]},
{
"name": "7.3 理想变压器与变压器应用",
"color": "#4338ca",
"desc": "理想变压器的变压、变流与阻抗变换",
"items": [
{"id":"ci7s3-1","name":"理想变压器的定义与变压比","tags":["def","der"],"brief":"u₁/u₂=n=N₁/N₂。",
 "fig":"transformer","figCap":"理想变压器的铁芯耦合与匝数比",
 "body": wrap(
   defn("理想变压器", p("理想变压器是满足下列条件的耦合线圈模型：无漏磁（全耦合 $k=1$）、无损耗（线圈电阻为零、铁芯无涡流磁滞损耗）、自感与互感均为无穷大但匝数比有限。其唯一参数为匝数比 $n=N_1/N_2$。"))+
   der(p("<strong>变压比推导：</strong>理想变压器铁芯中磁通 $\\Phi$ 相同，由法拉第定律，两线圈感应电压与匝数成正比：")+
   fml("u_1=N_1\\frac{d\\Phi}{dt},\\qquad u_2=N_2\\frac{d\\Phi}{dt}")+
   p("两式相除即得：")+
   fml("\\frac{u_1}{u_2}=\\frac{N_1}{N_2}=n")+
   p("当 $n>1$ 时升压（副边少匝），$n<1$ 时降压。"))+
   note(p("理想变压器无损耗地传递能量，瞬时功率守恒 $u_1i_1+u_2i_2=0$。"))
 )},
{"id":"ci7s3-2","name":"变流比与阻抗变换","tags":["der","thm"],"brief":"i₁/i₂=−1/n，Z_in=n²Z_L。",
 "body": wrap(
   der(p("<strong>变流比推导：</strong>理想变压器铁芯磁动势平衡（激磁电流为零），两线圈磁动势相互抵消：")+
   fml("N_1 i_1+N_2 i_2=0 \\implies \\frac{i_1}{i_2}=-\\frac{N_2}{N_1}=-\\frac{1}{n}")+
   p("负号表示两电流对同名端的流入流出关系相反。"))+
   der(p("<strong>阻抗变换：</strong>设副边接负载 $Z_L$，由 $\\dot{U}_1=n\\dot{U}_2$、$\\dot{I}_1=-\\dot{I}_2/n$ 得原边输入阻抗：")+
   fml("Z_{in}=\\frac{\\dot{U}_1}{\\dot{I}_1}=\\frac{n\\dot{U}_2}{-\\dot{I}_2/n}=n^2\\frac{\\dot{U}_2}{-\\dot{I}_2}=n^2 Z_L")+
   p("即理想变压器把副边阻抗按 $n^2$ 折算到原边，实现<strong>阻抗变换</strong>。"))+
   exa(p("<strong>例：</strong>$n=10$ 的变压器，副边 $8\\,\\Omega$ 负载折算到原边为 $800\\,\\Omega$，可用于阻抗匹配。"))+
   note(p("变压、变流、变阻抗三者由理想变压器的能量守恒统一起来，是变压器应用的三大功能。"))
 )},
{"id":"ci7s3-3","name":"变压器的实际应用","tags":["der","app","note"],"brief":"电力传输、隔离与阻抗匹配。",
 "body": wrap(
   der(p("<strong>高压输电降低损耗的推导：</strong>设输送功率为 $P$、线路电阻为 $R_{line}$、功率因数为 $\\cos\\varphi$，则线路电流为：")+
   fml("I=\\frac{P}{U\\cos\\varphi}")+
   p("线路损耗为：")+
   fml("P_{loss}=I^2R_{line}=\\frac{P^2 R_{line}}{U^2\\cos^2\\varphi}")+
   p("可见在输送功率与线路电阻不变时，损耗与输电电压的平方成反比，故用升压变压器提高 $U$ 可大幅降低线路损耗。"))+
   app(p("<strong>电力传输：</strong>用升压变压器升高电压以减小线路电流 $I=P/U$，从而降低线路损耗 $I^2R$；到用户端再用降压变压器降到安全电压。这是交流输电优于早期直流方案的关键。"))+
   app(p("<strong>阻抗匹配：</strong>利用 $Z_{in}=n^2Z_L$ 把负载阻抗变换到与信号源匹配的数值，实现最大功率传输，广泛用于音频输出与射频电路。"))+
   note(p("实际变压器存在漏磁、铜损与铁损，耦合系数 $k<1$，需用漏感、激磁电感和等效电阻的电路模型描述，理想变压器只是其极限情形。"))
 )},
]},
]

ch8_sections = [
{
"name": "8.1 网络函数与频率特性",
"color": "#059669",
"desc": "网络函数、幅频相频特性与零极点",
"items": [
{"id":"ci8s1-1","name":"网络函数","tags":["def","der"],"brief":"响应相量与激励相量之比随频率变化。",
 "body": wrap(
   defn("网络函数", p("线性网络在单一正弦激励下，某响应的相量与激励相量之比定义为<strong>网络函数</strong>：")+
   fml("H(j\\omega)=\\frac{\\dot{Y}(j\\omega)}{\\dot{X}(j\\omega)}")+
   p("它只与网络结构与参数有关，与激励大小无关，表征网络的频率选择特性。"))+
   der(p("<strong>由相量模型求网络函数：</strong>把 $R$、$L$、$C$ 换成 $R$、$j\\omega L$、$\\frac{1}{j\\omega C}$ 后，用分压、分流或节点法求响应与激励之比：")+
   fml("H(j\\omega)=\\frac{\\text{响应相量}}{\\text{激励相量}}"))+
   note(p("网络函数是复频率 $s$ 的函数 $H(s)$ 在 $s=j\\omega$ 时的取值，$H(s)$ 的零点极点决定频率特性形状。"))
 )},
{"id":"ci8s1-2","name":"幅频特性与相频特性","tags":["der","note"],"brief":"H 的模为幅频，辐角为相频。",
 "body": wrap(
   der(p("<strong>分解为幅频与相频：</strong>把网络函数写成极坐标形式：")+
   fml("H(j\\omega)=|H(j\\omega)|\\angle\\varphi(\\omega)")+
   p("其中 $|H|$ 为<strong>幅频特性</strong>，表示输出与输入的幅值比；$\\varphi$ 为<strong>相频特性</strong>，表示相位差。二者共同描述网络对不同频率正弦量的响应。")+
   fml("|H|=\\frac{Y_m}{X_m},\\qquad \\varphi=\\varphi_Y-\\varphi_X")+
   p("当输出幅值随频率升高而下降时网络呈低通特性，反之呈高通；幅频在某一频率出现峰值则呈谐振/带通特性。"))+
   app(p("<strong>应用：</strong>幅频相频特性用于滤波器设计、放大器带宽与相位裕度分析。"))
 )},
{"id":"ci8s1-3","name":"零点、极点与稳定性","tags":["der","note"],"brief":"H(s) 的极点位置决定系统稳定性。",
 "body": wrap(
   der(p("<strong>零极点表示：</strong>把网络函数写成复频域有理分式：")+
   fml("H(s)=K\\frac{(s-z_1)(s-z_2)\\cdots}{(s-p_1)(s-p_2)\\cdots}")+
   p("分子根 $z_i$ 为零点，分母根 $p_j$ 为极点。极点对应暂态响应的自然频率，零点影响幅频的谷值位置。"))+
   der(p("<strong>稳定性判据：</strong>对线性时不变网络，若所有极点实部为负，即位于 $s$ 左半平面：")+
   fml("\\Re\\{p_j\\}<0\\quad \\forall j \\iff \\text{稳定}")+
   p("此时暂态响应随时间衰减；若有极点落在右半平面，则响应发散，系统不稳定。"))+
   note(p("含受控源的网络可能出现右半平面极点，从而自激振荡。"))
 )},
]},
{
"name": "8.2 一阶网络与滤波",
"color": "#10b981",
"desc": "一阶 RC 低通与高通滤波",
"items": [
{"id":"ci8s2-1","name":"一阶 RC 低通网络","tags":["der","thm"],"brief":"H=1/(1+jωRC)，截止频率 ωc=1/RC。",
 "fig":"filter_lp","figCap":"一阶 RC 低通滤波电路与幅频特性",
 "body": wrap(
   der(p("<strong>推导网络函数：</strong>RC 低通电路以电压为激励、电容电压为响应，由分压关系：")+
   fml("H(j\\omega)=\\frac{\\dot{U}_C}{\\dot{U}_1}=\\frac{\\frac{1}{j\\omega C}}{R+\\frac{1}{j\\omega C}}=\\frac{1}{1+j\\omega RC}")+
   p("其幅频特性为：")+
   fml("|H|=\\frac{1}{\\sqrt{1+(\\omega RC)^2}},\\qquad \\varphi=-\\arctan(\\omega RC)")+
   p("当 $\\omega\\to 0$ 时 $|H|\\to 1$（通过），$\\omega\\to\\infty$ 时 $|H|\\to 0$（抑制）。令 $|H|=1/\\sqrt2$ 得截止角频率：")+
   fml("\\omega_c=\\frac{1}{RC},\\qquad f_c=\\frac{1}{2\\pi RC}"))+
   note(p("低于 $f_c$ 的信号基本通过，高于 $f_c$ 的信号被衰减，故称低通滤波器。"))
 )},
{"id":"ci8s2-2","name":"一阶 RC 高通网络","tags":["der","exa"],"brief":"H=jωRC/(1+jωRC)，隔直通交。",
 "body": wrap(
   der(p("<strong>推导网络函数：</strong>把响应取自电阻两端，则：")+
   fml("H(j\\omega)=\\frac{\\dot{U}_R}{\\dot{U}_1}=\\frac{R}{R+\\frac{1}{j\\omega C}}=\\frac{j\\omega RC}{1+j\\omega RC}")+
   p("幅频与相频为：")+
   fml("|H|=\\frac{\\omega RC}{\\sqrt{1+(\\omega RC)^2}},\\qquad \\varphi=90°-\\arctan(\\omega RC)")+
   p("低频时 $|H|\\to 0$（阻挡直流），高频时 $|H|\\to 1$（通过），故为高通，同一截止频率 $\\omega_c=1/RC$。"))+
   exa(p("<strong>例：</strong>$R=1\\,\\text{k}\\Omega$、$C=0.1\\,\\mu\\text{F}$，$f_c=\\frac{1}{2\\pi\\times10^{-4}}\\approx1592\\,\\text{Hz}$。"))+
   note(p("高通与低通互为补充，改变 $RC$ 即可调整截止频率；多级级联可获得更陡的过渡带。"))
 )},
]},
{
"name": "8.3 二阶网络与谐振",
"color": "#34d399",
"desc": "二阶 RLC 网络的频率特性与品质因数",
"items": [
{"id":"ci8s3-1","name":"二阶网络的频率特性","tags":["der"],"brief":"RLC 网络的 H 含二次项，可出现谐振峰。",
 "body": wrap(
   der(p("<strong>推导二阶网络函数：</strong>以串联 RLC 电路取电容电压为响应，由分压得：")+
   fml("H(j\\omega)=\\frac{\\frac{1}{j\\omega C}}{R+j\\omega L+\\frac{1}{j\\omega C}}=\\frac{1}{1-\\omega^2 LC+j\\omega RC}")+
   p("利用固有频率 $\\omega_0=1/\\sqrt{LC}$ 与品质因数 $Q=\\frac{\\omega_0 L}{R}=\\frac{1}{\\omega_0 RC}$ 归一化：")+
   fml("H(j\\omega)=\\frac{1}{1-\\left(\\frac{\\omega}{\\omega_0}\\right)^2+j\\frac{\\omega}{Q\\omega_0}}")+
   p("当 $\\omega\\approx\\omega_0$ 时分母虚部与实部配合，$|H|$ 出现峰值，即谐振现象。"))+
   note(p("二阶低通的幅频在 $\\omega_0$ 附近可能超过 1，$Q$ 越大峰值越尖锐。"))
 )},
{"id":"ci8s3-2","name":"品质因数与带宽","tags":["der","exa"],"brief":"Q 决定谐振峰高度与带宽。",
 "body": wrap(
   der(p("<strong>品质因数与带宽：</strong>对二阶带通特性，上下截止频率对应 $|H|$ 下降到峰值 $1/\\sqrt2$（−3 dB）。带宽为：")+
   fml("BW=\\omega_0/Q")+
   p("即 $Q$ 越大带宽越窄、选择性越强。对串联 RLC，品质因数为：")+
   fml("Q=\\frac{\\omega_0 L}{R}=\\frac{1}{R}\\sqrt{\\frac{L}{C}}")+
   p("谐振时电感或电容电压为电源电压的 $Q$ 倍。"))+
   exa(p("<strong>例：</strong>$L=1\\,\\text{mH}$、$C=1\\,\\mu\\text{F}$，则 $\\omega_0=10^6\\,\\text{rad/s}$；若 $R=1\\,\\Omega$，$Q=1000$，$BW=1000\\,\\text{rad/s}$。"))+
   note(p("高 $Q$ 电路用于窄带选频，低 $Q$ 电路用于宽带传输，需按需求折中。"))
 )},
]},
{
"name": "8.4 波特图与滤波器",
"color": "#047857",
"desc": "对数频率特性与滤波器分类",
"items": [
{"id":"ci8s4-1","name":"波特图","tags":["der","thm"],"brief":"用分贝与对数频率绘制幅频相频，渐近线近似。",
 "fig":"bode","figCap":"一阶低通的波特图：转折频率处 −3 dB，高频 −20 dB/十倍频",
 "body": wrap(
   thm("波特图", p("以频率的对数为横轴，以 $20\\lg|H|$（分贝 dB）为纵轴画幅频，以相位为纵轴画相频，即为波特图。对数坐标可把宽阔的频率范围压缩表示，并可用直线渐近线近似。"))+
   der(p("<strong>一阶低通的渐近线推导：</strong>由 $|H|=\\frac{1}{\\sqrt{1+(\\omega/\\omega_c)^2}}$，取分贝：")+
   fml("20\\lg|H|=-10\\lg\\left[1+(\\omega/\\omega_c)^2\\right]")+
   p("低频 $\\omega\\ll\\omega_c$ 时 $20\\lg|H|\\approx0\\,\\text{dB}$；高频 $\\omega\\gg\\omega_c$ 时：")+
   fml("20\\lg|H|\\approx-20\\lg\\frac{\\omega}{\\omega_c}")+
   p("即每十倍频下降 $20\\,\\text{dB}$。在转折频率 $\\omega_c$ 处 $20\\lg|H|=-3\\,\\text{dB}$。"))+
   note(p("波特图是控制系统与滤波器设计中最常用的频率特性表示法。"))
 )},
{"id":"ci8s4-2","name":"滤波器类型与阶数","tags":["def","note"],"brief":"低通、高通、带通、带阻及阶数对陡度的影响。",
 "body": wrap(
   defn("滤波器分类", p("按通带位置分为低通、高通、带通、带阻四类；按实现元件分为无源（RLC、RC）与有源（含运放）滤波器；按逼近函数分为巴特沃斯、切比雪夫、贝塞尔等类型。"))+
   der(p("<strong>阶数与陡度：</strong>$n$ 阶滤波器在过渡带外的渐近斜率为 $\\pm20n\\,\\text{dB}/\\text{十倍频}$：")+
   fml("\\text{斜率}=-20n\\ \\text{dB}/\\text{十倍频}")+
   p("阶数越高过渡带越陡、逼近理想滤波特性越好，但元件数增多、相移与延迟加大，且可能引入更大的通带波动。"))+
   app(p("<strong>应用：</strong>音频分频、抗混叠滤波、电源去耦、通信信道选择等均依赖不同阶数的滤波器实现。"))
 )},
]},
]

ch9_sections = [
{
"name": "9.1 非正弦周期量的傅里叶分解",
"color": "#b45309",
"desc": "周期量的傅里叶级数与频谱",
"items": [
{"id":"ci9s1-1","name":"周期量的傅里叶级数","tags":["thm","der"],"brief":"周期量可分解为直流与各次谐波之和。",
 "fig":"fourier_wave","figCap":"方波的傅里叶分解：直流与各次奇次谐波叠加",
 "body": wrap(
   thm("傅里叶级数", p("满足狄里赫利条件的周期函数 $f(t)$（周期 $T$、基波角频率 $\\omega_1=2\\pi/T$）可展开为三角级数：")+
   fml("f(t)=a_0+\\sum_{n=1}^{\\infty}\\left[a_n\\cos(n\\omega_1 t)+b_n\\sin(n\\omega_1 t)\\right]"))+
   der(p("<strong>系数推导：</strong>利用三角函数在一个周期内的正交性，例如 $\\int_0^T\\cos^2(n\\omega_1 t)dt=T/2$、不同次谐波积分为零，把级数两边同乘 $\\cos(n\\omega_1 t)$ 并逐项积分，只剩下对应项：")+
   fml("a_0=\\frac{1}{T}\\int_0^T f(t)\\,dt")+
   fml("a_n=\\frac{2}{T}\\int_0^T f(t)\\cos(n\\omega_1 t)\\,dt")+
   fml("b_n=\\frac{2}{T}\\int_0^T f(t)\\sin(n\\omega_1 t)\\,dt")+
   p("也可合并为幅相形式 $f(t)=A_0+\\sum A_n\\cos(n\\omega_1 t+\\varphi_n)$，其中 $A_n=\\sqrt{a_n^2+b_n^2}$。"))+
   note(p("$A_0=a_0$ 为直流分量，$n=1$ 为基波，$n\\ge2$ 为高次谐波。"))
 )},
{"id":"ci9s1-2","name":"常见波形的傅里叶级数","tags":["der","exa"],"brief":"方波、三角波、锯齿波的谐波结构。",
 "body": wrap(
   der(p("<strong>方波谐波分析：</strong>幅值为 $A$、周期为 $T$、上下对称的方波为奇函数，只有正弦项，且由于半波对称只含奇次谐波：")+
   fml("f(t)=\\frac{4A}{\\pi}\\sum_{k=0}^{\\infty}\\frac{\\sin(2k+1)\\omega_1 t}{2k+1}")+
   p("即 $\\frac{4A}{\\pi}(\\sin\\omega_1 t+\\frac{1}{3}\\sin3\\omega_1 t+\\frac{1}{5}\\sin5\\omega_1 t+\\cdots)$，谐波幅值按 $1/n$ 衰减。"))+
   der(p("<strong>三角波：</strong>同样只含奇次谐波，但幅值按 $1/n^2$ 迅速衰减，波形更接近正弦：")+
   fml("f(t)=\\frac{8A}{\\pi^2}\\sum_{k=0}^{\\infty}\\frac{(-1)^k}{(2k+1)^2}\\sin(2k+1)\\omega_1 t")+
   p("锯齿波含全部谐波，幅值按 $1/n$ 衰减。谐波衰减越快，波形越平滑。"))+
   note(p("谐波幅值随次数的衰减速率反映了波形的不连续程度：跳变越多，高次谐波越丰富。"))
 )},
{"id":"ci9s1-3","name":"对称性与谐波分析","tags":["der","note"],"brief":"奇偶对称与半波对称决定所含谐波。",
 "body": wrap(
   der(p("<strong>对称性判据：</strong>若 $f(t)$ 为奇函数 $f(-t)=-f(t)$，则只含正弦项 $a_n=0$；若为偶函数，则只含余弦项 $b_n=0$。若满足半波对称 $f(t+T/2)=-f(t)$，则只含奇次谐波，$a_{2k}=b_{2k}=0$。")+
   fml("f(-t)=-f(t)\\Rightarrow a_n=0;\\quad f(t+T/2)=-f(t)\\Rightarrow \\text{仅奇次谐波}"))+
   der(p("<strong>偶函数只含余弦的证明：</strong>由 $a_n$ 与 $b_n$ 的积分定义，$f(t)\\sin(n\\omega_1 t)$ 为奇函数，在一个周期（对称区间）上积分为零，故 $b_n=0$，只剩下余弦项。"))+
   app(p("<strong>应用：</strong>利用对称性可预先判断谐波成分，简化分解计算，也便于分析整流、变频等非线性电路产生的谐波污染。"))
 )},
]},
{
"name": "9.2 有效值与平均功率",
"color": "#d97706",
"desc": "非正弦量的有效值与功率",
"items": [
{"id":"ci9s2-1","name":"非正弦周期量的有效值","tags":["der"],"brief":"I=√(I₀²+ΣIₙ²)，各次谐波平方和。",
 "body": wrap(
   der(p("<strong>由有效值定义推导：</strong>设 $i(t)=I_0+\\sum i_n(t)$，各次谐波正交。有效值为：")+
   fml("I=\\sqrt{\\frac{1}{T}\\int_0^T i^2(t)\\,dt}")+
   p("展开平方后，不同次谐波交叉项在一个周期内的积分为零，只剩直流项与各次谐波平方项的积分：")+
   fml("\\frac{1}{T}\\int_0^T i^2 dt = I_0^2+\\sum_{n=1}^{\\infty} I_n^2")+
   p("故非正弦周期量的有效值为：")+
   fml("I=\\sqrt{I_0^2+\\sum_{n=1}^{\\infty} I_n^2}"))+
   exa(p("<strong>例：</strong>某电流含直流 $2\\,\\text{A}$、基波有效值 $3\\,\\text{A}$、三次谐波 $1\\,\\text{A}$，则 $I=\\sqrt{4+9+1}=\\sqrt{14}\\approx3.74\\,\\text{A}$。"))+
   note(p("有效值不是各次谐波有效值之和，而是其平方和的开方。"))
 )},
{"id":"ci9s2-2","name":"非正弦周期电路的平均功率","tags":["der","thm"],"brief":"P=U₀I₀+ΣUₙIₙcosφₙ。",
 "body": wrap(
   thm("平均功率", p("非正弦周期电路的平均功率等于直流分量功率与各次谐波有功功率之和：")+
   fml("P=U_0 I_0+\\sum_{n=1}^{\\infty} U_n I_n\\cos\\varphi_n"))+
   der(p("<strong>推导：</strong>把电压、电流分解为各次谐波，代入 $P=\\frac{1}{T}\\int_0^T ui\\,dt$。不同频率的电压与电流乘积在一个周期内积分为零（正交性），只有同次谐波的乘积贡献功率：")+
   fml("\\frac{1}{T}\\int_0^T u_n i_m\\,dt=0\\ (n\\ne m)")+
   p("故求和式中只剩同次谐波项，即得平均功率公式。"))+
   note(p("各次谐波各自贡献功率，且与频率无关；同频率的电压电流才产生平均功率。"))
 )},
]},
{
"name": "9.3 非正弦周期电路的稳态分析",
"color": "#92400e",
"desc": "谐波分析法",
"items": [
{"id":"ci9s3-1","name":"谐波分析法","tags":["der","note"],"brief":"对每一谐波用相量法单独求解再叠加。",
 "body": wrap(
   der(p("<strong>分析步骤：</strong>第一步，把非正弦激励分解为傅里叶级数（直流与各次谐波）；第二步，对每个频率分量分别用相量法求解，注意同一次谐波的电抗为 $n\\omega_1 L$ 与 $\\frac{1}{n\\omega_1 C}$；第三步，把各分量在时域叠加得到总响应。")+
   fml("\\text{各次谐波}:\\ \\dot{Y}_n=H(jn\\omega_1)\\dot{X}_n")+
   p("关键是不能把不同频率的相量直接相加，因为它们的旋转因子不同，相量叠加只对同频率有效。"))+
   app(p("<strong>应用：</strong>整流电源滤波、变频器谐波分析、电力系统谐波治理等均采用谐波分析法。"))
 )},
{"id":"ci9s3-2","name":"非正弦电路计算示例","tags":["exa","der"],"brief":"逐次谐波求解再叠加。",
 "body": wrap(
   exa(p("<strong>例：</strong>某 RL 电路激励为 $u(t)=10+20\\sin(\\omega_1 t)\\,\\text{V}$，$R=5\\,\\Omega$，$\\omega_1 L=5\\,\\Omega$，求电流。"))+
   der(p("直流分量作用时电感短路，电流为：")+
   fml("I_0=\\frac{10}{5}=2\\,\\text{A}")+
   p("基波作用时用相量法，阻抗 $Z_1=R+j\\omega_1 L=5+j5\\,\\Omega$，有效值相量：")+
   fml("\\dot{I}_1=\\frac{20/\\sqrt2\\angle0°}{5\\sqrt2\\angle45°}=\\frac{10}{5\\sqrt2}\\angle-45°\\approx1.41\\angle-45°\\,\\text{A}")+
   p("时域叠加得：")+
   fml("i(t)=2+2\\sin(\\omega_1 t-45°)\\,\\text{A}")+
   p("可见直流与交流分量各自独立计算后再叠加。"))+
   note(p("若含多次谐波，则逐次重复上述过程，最后在时域把各次结果相加。"))
 )},
]},
]

ch10_sections = [
{
"name": "10.1 二端口网络与 Y、Z 参数",
"color": "#7e22ce",
"desc": "端口条件与导纳、阻抗参数",
"items": [
{"id":"ci10s1-1","name":"二端口网络与端口条件","tags":["def"],"brief":"四个端钮构成两个端口，满足端口电流一进一出。",
 "fig":"two_port","figCap":"二端口网络的端口电压与电流参考方向",
 "body": wrap(
   defn("二端口网络", p("具有两个端口的网络称为二端口网络（双口网络）。每个端口由一对端钮构成，且满足<strong>端口条件</strong>：从一个端钮流入的电流等于从同一端口另一端的流出电流，即 $i_1'=i_1$、$i_2'=i_2$。"))+
   der(p("在端口条件满足时，二端口只需用两个端口电压 $\\dot{U}_1,\\dot{U}_2$ 与两个端口电流 $\\dot{I}_1,\\dot{I}_2$ 四个变量描述。任意两个变量可用其余两个线性表示，由此定义不同参数体系：")+
   fml("(\\dot{U}_1,\\dot{I}_1,\\dot{U}_2,\\dot{I}_2)\\ \\text{中任取两个为自变量}"))+
   note(p("由线性时不变无源元件构成的二端口满足互易性，参数间存在约束关系。"))
 )},
{"id":"ci10s1-2","name":"Y 参数（短路导纳参数）","tags":["der","thm"],"brief":"以端口电压为自变量，电流为响应的导纳方程组。",
 "body": wrap(
   thm("Y 参数方程", p("以两端口电压为自变量，电流为响应：")+
   fml("\\dot{I}_1=Y_{11}\\dot{U}_1+Y_{12}\\dot{U}_2")+
   fml("\\dot{I}_2=Y_{21}\\dot{U}_1+Y_{22}\\dot{U}_2"))+
   der(p("<strong>参数定义推导：</strong>令端口 2 短路 $\\dot{U}_2=0$，则：")+
   fml("Y_{11}=\\frac{\\dot{I}_1}{\\dot{U}_1}\\Big|_{\\dot{U}_2=0},\\qquad Y_{21}=\\frac{\\dot{I}_2}{\\dot{U}_1}\\Big|_{\\dot{U}_2=0}")+
   p("同理令 $\\dot{U}_1=0$ 可定义 $Y_{12}$、$Y_{22}$。因测量时端口短路，故称短路导纳参数。互易网络满足 $Y_{12}=Y_{21}$。"))+
   note(p("Y 参数矩阵适合描述并联型二端口；对称网络的 $Y_{11}=Y_{22}$。"))
 )},
{"id":"ci10s1-3","name":"Z 参数（开路阻抗参数）","tags":["der","thm"],"brief":"以端口电流为自变量，电压为响应的阻抗方程组。",
 "body": wrap(
   thm("Z 参数方程", p("以两端口电流为自变量，电压为响应：")+
   fml("\\dot{U}_1=Z_{11}\\dot{I}_1+Z_{12}\\dot{I}_2")+
   fml("\\dot{U}_2=Z_{21}\\dot{I}_1+Z_{22}\\dot{I}_2"))+
   der(p("<strong>参数定义推导：</strong>令端口 2 开路 $\\dot{I}_2=0$，则：")+
   fml("Z_{11}=\\frac{\\dot{U}_1}{\\dot{I}_1}\\Big|_{\\dot{I}_2=0},\\qquad Z_{21}=\\frac{\\dot{U}_2}{\\dot{I}_1}\\Big|_{\\dot{I}_2=0}")+
   p("因测量时端口开路，故称开路阻抗参数。Z 参数矩阵与 Y 参数矩阵互为逆矩阵：")+
   fml("[Z]=[Y]^{-1}"))+
   exa(p("<strong>例：</strong>T 形网络的 $Z_{11}=Z_a+Z_c$、$Z_{22}=Z_b+Z_c$、$Z_{12}=Z_{21}=Z_c$。"))+
   note(p("互易网络 $Z_{12}=Z_{21}$；对称网络 $Z_{11}=Z_{22}$。"))
 )},
]},
{
"name": "10.2 T 参数与 H 参数",
"color": "#9333ea",
"desc": "传输参数与混合参数",
"items": [
{"id":"ci10s2-1","name":"T 参数（传输参数）","tags":["der","thm"],"brief":"以端口 2 的电压电流表示端口 1 的电压电流。",
 "body": wrap(
   thm("T 参数方程", p("以端口 2 的电压电流表示端口 1：")+
   fml("\\dot{U}_1=A\\dot{U}_2-B\\dot{I}_2")+
   fml("\\dot{I}_1=C\\dot{U}_2-D\\dot{I}_2")+
   p("其中 $A,B,C,D$ 称为传输参数（也称 A 参数）。"))+
   der(p("<strong>互易性约束：</strong>对互易二端口，四个传输参数满足：")+
   fml("AD-BC=1")+
   p("该式可由 Z 参数与 T 参数的转换关系代入 $Z_{12}=Z_{21}$ 推出：")+
   fml("A=\\frac{Z_{11}}{Z_{21}},\\ B=\\frac{Z_{11}Z_{22}-Z_{12}Z_{21}}{Z_{21}},\\ C=\\frac{1}{Z_{21}},\\ D=\\frac{Z_{22}}{Z_{21}}")+
   p("代入互易条件 $Z_{12}=Z_{21}$ 即得 $AD-BC=1$。"))+
   note(p("T 参数特别适合级联网络，级联时传输矩阵直接相乘。"))
 )},
{"id":"ci10s2-2","name":"H 参数（混合参数）","tags":["der","exa"],"brief":"以输入电流和输出电压为自变量。",
 "body": wrap(
   thm("H 参数方程", p("以输入电流 $\\dot{I}_1$ 与输出电压 $\\dot{U}_2$ 为自变量：")+
   fml("\\dot{U}_1=h_{11}\\dot{I}_1+h_{12}\\dot{U}_2")+
   fml("\\dot{I}_2=h_{21}\\dot{I}_1+h_{22}\\dot{U}_2"))+
   der(p("<strong>参数定义：</strong>分别令输出短路（$\\dot{U}_2=0$）与输入开路（$\\dot{I}_1=0$）可得：")+
   fml("h_{11}=\\frac{\\dot{U}_1}{\\dot{I}_1}\\Big|_{\\dot{U}_2=0},\\ h_{21}=\\frac{\\dot{I}_2}{\\dot{I}_1}\\Big|_{\\dot{U}_2=0},\\ h_{12}=\\frac{\\dot{U}_1}{\\dot{U}_2}\\Big|_{\\dot{I}_1=0},\\ h_{22}=\\frac{\\dot{I}_2}{\\dot{U}_2}\\Big|_{\\dot{I}_1=0}")+
   p("$h_{11}$ 为短路输入阻抗，$h_{21}$ 为电流放大倍数，$h_{12}$ 为反向电压比，$h_{22}$ 为开路输出导纳。"))+
   exa(p("<strong>例：</strong>晶体管的共射极 $h$ 参数（$h_{ie}$、$h_{fe}$、$h_{re}$、$h_{oe}$）正是 H 参数，广泛用于小信号放大器分析。"))+
   note(p("H 参数因混合量纲而得名，在电子器件手册中极为常见。"))
 )},
]},
{
"name": "10.3 二端口的等效电路",
"color": "#a855f7",
"desc": "T 形与 Π 形等效电路",
"items": [
{"id":"ci10s3-1","name":"二端口的 T 形等效电路","tags":["der"],"brief":"互易二端口可用三个阻抗的 T 形网络等效。",
 "body": wrap(
   der(p("<strong>由 Z 参数构造 T 形等效：</strong>设 T 形网络三个臂为 $Z_a$（端口 1 串臂）、$Z_b$（端口 2 串臂）、$Z_c$（公共并臂），则：")+
   fml("Z_{11}=Z_a+Z_c,\\quad Z_{22}=Z_b+Z_c,\\quad Z_{12}=Z_{21}=Z_c")+
   p("反解出各臂：")+
   fml("Z_c=Z_{12},\\quad Z_a=Z_{11}-Z_{12},\\quad Z_b=Z_{22}-Z_{12}")+
   p("因此任意互易二端口都可用 $Z_a$、$Z_b$、$Z_c$ 三个阻抗构成的 T 形网络等效。"))+
   note(p("该等效要求 $Z_{12}=Z_{21}$，即网络互易；非互易网络需含受控源才能等效。"))
 )},
{"id":"ci10s3-2","name":"二端口的 Π 形等效电路","tags":["der"],"brief":"互易二端口可用三个导纳的 Π 形网络等效。",
 "body": wrap(
   der(p("<strong>由 Y 参数构造 Π 形等效：</strong>设 Π 形网络三个臂为 $Y_A$（端口 1 并臂）、$Y_B$（端口 2 并臂）、$Y_C$（串臂），则：")+
   fml("Y_{11}=Y_A+Y_C,\\quad Y_{22}=Y_B+Y_C,\\quad Y_{12}=Y_{21}=-Y_C")+
   p("反解得：")+
   fml("Y_C=-Y_{12},\\quad Y_A=Y_{11}+Y_{12},\\quad Y_B=Y_{22}+Y_{12}")+
   p("即用三个导纳构成的 Π 形网络等效任意互易二端口。T 形与 Π 形互为对偶结构。"))+
   exa(p("<strong>例：</strong>无源对称二端口若 $Z_{11}=Z_{22}$，其 T 形等效也对称，$Z_a=Z_b$，便于工程实现。"))+
   note(p("选择 T 形或 Π 形取决于参数类型（Z 用 T，Y 用 Π）以及物理实现方便程度。"))
 )},
]},
{
"name": "10.4 二端口的连接",
"color": "#7e22ce",
"desc": "级联、串联与并联",
"items": [
{"id":"ci10s4-1","name":"二端口的级联","tags":["der","exa"],"brief":"级联时传输矩阵相乘。",
 "body": wrap(
   der(p("<strong>级联（链联）：</strong>两二端口级联时，前者的输出端口与后者的输入端口相接。用 T 参数表示：")+
   fml("\\begin{pmatrix}\\dot{U}_1\\\\ \\dot{I}_1\\end{pmatrix}=T_1\\begin{pmatrix}\\dot{U}_2\\\\ -\\dot{I}_2\\end{pmatrix},\\qquad \\begin{pmatrix}\\dot{U}_2\\\\ -\\dot{I}_2\\end{pmatrix}=T_2\\begin{pmatrix}\\dot{U}_3\\\\ -\\dot{I}_3\\end{pmatrix}")+
   p("串联两式得总传输矩阵：")+
   fml("T=T_1\\,T_2")+
   p("多个二端口级联时总传输矩阵等于各段传输矩阵按顺序相乘。"))+
   exa(p("<strong>例：</strong>两段相同的传输线级联，总 T 矩阵为单段 T 矩阵的二次方，衰减与相移加倍。"))+
   app(p("<strong>应用：</strong>滤波器、放大链、传输线等均由级联分析计算总体传输特性。"))
 )},
{"id":"ci10s4-2","name":"二端口的串联与并联","tags":["der","note"],"brief":"串联时 Z 相加，并联时 Y 相加。",
 "body": wrap(
   der(p("<strong>串联：</strong>两二端口串联时对应端口电流相同、电压相加。以 Z 参数表示：")+
   fml("\\dot{U}=\\dot{U}^{(1)}+\\dot{U}^{(2)},\\qquad [Z]=[Z_1]+[Z_2]")+
   p("前提是串接后各端口仍满足端口条件（电流一进一出）。"))+
   der(p("<strong>并联：</strong>两二端口并联时对应端口电压相同、电流相加。以 Y 参数表示：")+
   fml("\\dot{I}=\\dot{I}^{(1)}+\\dot{I}^{(2)},\\qquad [Y]=[Y_1]+[Y_2]")+
   p("同样要求并接后端口条件成立。此外还有串并联（输入串联输出并联）与并串联，分别对应 G 或 H 参数相加。"))+
   note(p("连接前后必须检验端口条件是否被破坏，否则不能简单相加。"))
 )},
]},
]

CHAPTERS = [
    {"id":"ci-ch1","num":"第一章","title":"电路基础","en":"CIRCUIT FUNDAMENTALS",
     "desc":"集中参数假设与电路变量、电流电压参考方向、电功率与能量、电阻与独立源、基尔霍夫电流定律与电压定律、支路节点回路与独立方程数、四种受控源及其处理。",
     "sections": ch1_sections},
    {"id":"ci-ch2","num":"第二章","title":"等效电路","en":"EQUIVALENT CIRCUITS",
     "desc":"电阻串联并联与分压分流、混联与平衡电桥、Δ 与 Y 联结及等效变换、实际电源的两种模型、电源等效变换、含源支路串并联与含受控源网络的化简。",
     "sections": ch2_sections},
    {"id":"ci-ch3","num":"第三章","title":"电路分析法","en":"CIRCUIT ANALYSIS METHODS",
     "desc":"支路电流法、网孔电流法与规范方程、节点电压法与超节点、含电流源与受控源的处理、方程独立性、矩阵形式与三种方法的比较和综合算例。",
     "sections": ch3_sections},
    {"id":"ci-ch4","num":"第四章","title":"电路定理","en":"CIRCUIT THEOREMS",
     "desc":"叠加定理与齐性定理、替代定理、戴维南定理与诺顿定理、等效电阻求法、最大功率传输定理与效率、互易定理与对偶原理。",
     "sections": ch4_sections},
    {"id":"ci-ch5","num":"第五章","title":"储能元件与时域分析","en":"ENERGY STORAGE & TIME DOMAIN",
     "desc":"电容与电感的伏安关系、储能与串并联、换路定则与初始值、0+ 等效电路、一阶 RC/RL 电路零输入与零状态响应、三要素法、二阶 RLC 电路特征根与三种阻尼。",
     "sections": ch5_sections},
    {"id":"ci-ch6","num":"第六章","title":"相量法与正弦稳态分析","en":"PHASORS & SINUSOIDAL STEADY STATE",
     "desc":"正弦量三要素与有效值、相位差与相量表示、相量形式的基尔霍夫定律、阻抗与导纳、RLC 相量关系、有功无功视在功率与复功率、功率因数校正、串联与并联谐振。",
     "sections": ch6_sections},
    {"id":"ci-ch7","num":"第七章","title":"耦合电感","en":"MUTUAL INDUCTANCE",
     "desc":"互感现象与互感系数、同名端与互感电压极性、耦合系数、互感线圈串接、去耦 T 形等效、含互感电路的相量分析、理想变压器的变压变流与阻抗变换。",
     "sections": ch7_sections},
    {"id":"ci-ch8","num":"第八章","title":"电路频率响应","en":"FREQUENCY RESPONSE",
     "desc":"网络函数、幅频相频特性、零点极点与稳定性、一阶 RC 低通与高通、二阶网络频率特性、品质因数与带宽、波特图渐近线与滤波器分类。",
     "sections": ch8_sections},
    {"id":"ci-ch9","num":"第九章","title":"非正弦周期电路","en":"NONSINUSOIDAL PERIODIC CIRCUITS",
     "desc":"周期量的傅里叶级数与系数、方波三角波锯齿波的谐波结构、对称性与谐波、非正弦有效值、非正弦平均功率、谐波分析法步骤与算例。",
     "sections": ch9_sections},
    {"id":"ci-ch10","num":"第十章","title":"二端口网络","en":"TWO-PORT NETWORKS",
     "desc":"二端口网络与端口条件、Y 参数与 Z 参数、T 传输参数与 H 混合参数、参数互易约束、T 形与 Π 形等效电路、级联与串并联连接。",
     "sections": ch10_sections},
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
  .la-nav-tab.c6{color:#0891b2;border-color:#a5f3fc}
  .la-nav-tab.c7{color:#4f46e5;border-color:#c7d2fe}
  .la-nav-tab.c8{color:#059669;border-color:#a7f3d0}
  .la-nav-tab.c9{color:#b45309;border-color:#fde68a}
  .la-nav-tab.c10{color:#7e22ce;border-color:#e9d5ff}
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
  .la-phase-title.ci-ch1::before{background:#2563eb}
  .la-phase-title.ci-ch2::before{background:#7c3aed}
  .la-phase-title.ci-ch3::before{background:#0d9488}
  .la-phase-title.ci-ch4::before{background:#c2410c}
  .la-phase-title.ci-ch5::before{background:#be185d}
  .la-phase-title.ci-ch6::before{background:#0891b2}
  .la-phase-title.ci-ch7::before{background:#4f46e5}
  .la-phase-title.ci-ch8::before{background:#059669}
  .la-phase-title.ci-ch9::before{background:#b45309}
  .la-phase-title.ci-ch10::before{background:#7e22ce}
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
<meta name="description" content="电路知识体系：电路基础、等效电路、电路分析法、电路定理、储能元件与时域分析、相量法与正弦稳态分析、耦合电感、电路频率响应、非正弦周期电路、二端口网络">
<title>电路 · 知识体系</title>
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
    <div class="la-eyebrow">CIRCUITS · KNOWLEDGE MAP</div>
    <h1>电路 · 知识体系</h1>
    <p class="la-subtitle">电路基础 · 等效电路 · 电路分析法 · 电路定理 · 时域分析 · 相量法 · 耦合电感 · 频率响应 · 非正弦周期 · 二端口网络</p>
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
    <div>电路 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于电路核心知识体系整理</div>
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
    with open("/workspace/circuits.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated circuits.html ({len(html)} chars)")
