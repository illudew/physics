# -*- coding: utf-8 -*-
"""Generate thermal-physics.html: 5 chapters 热力学系统参量与状态方程/气体动理论与统计分布律/输运过程/热力学第一定律/热力学第二定律."""
import json

FIG = {
"thermosystem": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="72" y="28" width="98" height="104" rx="10" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
<text x="100" y="76" font-size="13" fill="#991b1b">系统</text>
<text x="86" y="98" font-size="10" fill="#991b1b">m, T, p, V</text>
<line x1="170" y1="50" x2="222" y2="50" stroke="#0d9488" stroke-width="1.8"/>
<polygon points="222,50 212,46 212,54" fill="#0d9488"/>
<text x="176" y="44" font-size="10" fill="#0d9488">功 W</text>
<line x1="170" y1="80" x2="222" y2="80" stroke="#ea580c" stroke-width="1.8"/>
<polygon points="222,80 212,76 212,84" fill="#ea580c"/>
<text x="176" y="74" font-size="10" fill="#ea580c">热 Q</text>
<line x1="72" y1="112" x2="20" y2="112" stroke="#2563eb" stroke-width="1.8"/>
<polygon points="20,112 30,108 30,116" fill="#2563eb"/>
<text x="22" y="106" font-size="10" fill="#2563eb">物质</text>
<text x="24" y="150" font-size="10" fill="#64748b">系统经边界与外界交换能量与物质</text>
</svg>''',
"pvdiagram": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="132" stroke="#475569" stroke-width="1.2"/>
<polygon points="34,12 30,22 38,22" fill="#475569"/>
<line x1="34" y1="132" x2="226" y2="132" stroke="#475569" stroke-width="1.2"/>
<polygon points="232,132 222,128 222,136" fill="#475569"/>
<text x="16" y="28" font-size="12" fill="#475569">p</text>
<text x="214" y="150" font-size="12" fill="#475569">V</text>
<path d="M 60 40 C 110 92 150 118 216 127" fill="none" stroke="#dc2626" stroke-width="2"/>
<circle cx="60" cy="40" r="3" fill="#dc2626"/>
<circle cx="216" cy="127" r="3" fill="#dc2626"/>
<text x="64" y="36" font-size="10" fill="#dc2626">1</text>
<text x="206" y="120" font-size="10" fill="#dc2626">2</text>
<text x="76" y="112" font-size="10" fill="#64748b">等温线 pV = nRT</text>
</svg>''',
"isotherms": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="18" x2="30" y2="134" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="134" x2="228" y2="134" stroke="#475569" stroke-width="1.2"/>
<text x="14" y="26" font-size="12" fill="#475569">p</text>
<text x="216" y="150" font-size="12" fill="#475569">V</text>
<path d="M 48 34 C 90 84 130 112 218 127" fill="none" stroke="#dc2626" stroke-width="2"/>
<path d="M 48 52 C 90 100 130 122 218 132" fill="none" stroke="#e11d48" stroke-width="2"/>
<path d="M 48 74 C 90 114 130 128 218 133" fill="none" stroke="#ef4444" stroke-width="2"/>
<text x="176" y="32" font-size="10" fill="#dc2626">T₁</text>
<text x="194" y="52" font-size="10" fill="#e11d48">T₂</text>
<text x="208" y="72" font-size="10" fill="#ef4444">T₃</text>
<text x="70" y="150" font-size="10" fill="#64748b">T₁ &lt; T₂ &lt; T₃</text>
</svg>''',
"vanderwaals": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="18" x2="30" y2="136" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="136" x2="228" y2="136" stroke="#475569" stroke-width="1.2"/>
<text x="14" y="26" font-size="12" fill="#475569">p</text>
<text x="216" y="152" font-size="12" fill="#475569">V</text>
<path d="M 40 122 C 60 60 84 42 132 40 C 182 46 212 86 222 130" fill="none" stroke="#dc2626" stroke-width="1.5"/>
<path d="M 46 128 C 70 80 96 62 132 60 C 176 66 208 96 220 132" fill="none" stroke="#e11d48" stroke-width="1.5"/>
<path d="M 58 116 C 66 106 72 96 76 88 C 82 76 90 84 96 98 C 104 116 118 120 140 120 C 176 120 206 130 220 133" fill="none" stroke="#9f1239" stroke-width="2"/>
<line x1="76" y1="98" x2="140" y2="98" stroke="#0d9488" stroke-width="1.2" stroke-dasharray="4 3"/>
<text x="44" y="34" font-size="10" fill="#dc2626">T &gt; T_c</text>
<text x="92" y="70" font-size="10" fill="#9f1239">T = T_c</text>
<text x="150" y="114" font-size="10" fill="#0d9488">等面积法则</text>
</svg>''',
"criticalpoint": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="134" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="134" x2="226" y2="134" stroke="#475569" stroke-width="1.2"/>
<text x="16" y="26" font-size="12" fill="#475569">p</text>
<text x="214" y="150" font-size="12" fill="#475569">V</text>
<path d="M 60 122 C 78 66 96 54 118 54 C 152 56 196 90 220 130" fill="none" stroke="#be123c" stroke-width="2"/>
<circle cx="118" cy="54" r="4" fill="#9f1239"/>
<line x1="118" y1="54" x2="118" y2="134" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="34" y1="54" x2="118" y2="54" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="104" y="46" font-size="10" fill="#9f1239">临界点 C</text>
<text x="118" y="150" font-size="10" fill="#64748b">V_c</text>
<text x="36" y="50" font-size="10" fill="#64748b">p_c</text>
<path d="M 150 120 C 168 112 192 128 214 122" fill="none" stroke="#f43f5e" stroke-width="1.4" stroke-dasharray="4 3"/>
<text x="150" y="142" font-size="10" fill="#f43f5e">气液共存</text>
</svg>''',
"phasediagram": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="40" y1="18" x2="40" y2="136" stroke="#475569" stroke-width="1.2"/>
<line x1="40" y1="136" x2="228" y2="136" stroke="#475569" stroke-width="1.2"/>
<text x="24" y="26" font-size="12" fill="#475569">p</text>
<text x="214" y="152" font-size="12" fill="#475569">T</text>
<line x1="40" y1="136" x2="152" y2="42" stroke="#dc2626" stroke-width="1.8"/>
<line x1="152" y1="42" x2="222" y2="72" stroke="#e11d48" stroke-width="1.8"/>
<line x1="40" y1="136" x2="96" y2="44" stroke="#2563eb" stroke-width="1.8"/>
<line x1="40" y1="136" x2="58" y2="72" stroke="#0d9488" stroke-width="1.8"/>
<circle cx="152" cy="42" r="3.5" fill="#9f1239"/>
<text x="126" y="34" font-size="10" fill="#9f1239">三相点</text>
<text x="158" y="46" font-size="10" fill="#9f1239">临界点</text>
<text x="150" y="62" font-size="10" fill="#dc2626">固</text>
<text x="196" y="100" font-size="10" fill="#e11d48">液</text>
<text x="118" y="114" font-size="10" fill="#0d9488">气</text>
</svg>''',
"idealgasmodel": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="30" width="160" height="100" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
<g fill="#ea580c">
<circle cx="70" cy="55" r="4"/><circle cx="110" cy="45" r="4"/><circle cx="150" cy="60" r="4"/><circle cx="182" cy="48" r="4"/>
<circle cx="66" cy="100" r="4"/><circle cx="100" cy="112" r="4"/><circle cx="140" cy="98" r="4"/><circle cx="176" cy="110" r="4"/>
<circle cx="125" cy="78" r="4"/>
</g>
<line x1="100" y1="112" x2="90" y2="104" stroke="#c2410c" stroke-width="1"/>
<polygon points="90,104 96,107 94,110" fill="#c2410c"/>
<line x1="70" y1="55" x2="84" y2="62" stroke="#c2410c" stroke-width="1"/>
<polygon points="84,62 77,60 79,57" fill="#c2410c"/>
<text x="42" y="150" font-size="10" fill="#9a3412">分子视为弹性小球，除碰撞外无相互作用</text>
</svg>''',
"pressuremicro": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="30" width="160" height="100" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
<line x1="200" y1="30" x2="200" y2="130" stroke="#c2410c" stroke-width="3"/>
<line x1="150" y1="80" x2="192" y2="80" stroke="#dc2626" stroke-width="2"/>
<polygon points="192,80 182,75 182,85" fill="#dc2626"/>
<circle cx="150" cy="80" r="5" fill="#ea580c"/>
<line x1="150" y1="80" x2="126" y2="66" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2"/>
<text x="154" y="64" font-size="10" fill="#c2410c">v_x</text>
<text x="184" y="120" font-size="10" fill="#c2410c">器壁</text>
<text x="50" y="150" font-size="10" fill="#9a3412">Δp = 2mv_x，冲量来自动量变化</text>
</svg>''',
"equipartition": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<text x="18" y="30" font-size="11" fill="#9a3412">平动 3</text>
<line x1="18" y1="42" x2="118" y2="42" stroke="#ea580c" stroke-width="10"/>
<line x1="118" y1="42" x2="204" y2="42" stroke="#e5e7eb" stroke-width="10"/>
<text x="18" y="74" font-size="11" fill="#9a3412">转动 2</text>
<line x1="18" y1="86" x2="88" y2="86" stroke="#f97316" stroke-width="10"/>
<line x1="88" y1="86" x2="204" y2="86" stroke="#e5e7eb" stroke-width="10"/>
<text x="18" y="118" font-size="11" fill="#9a3412">振动 2</text>
<line x1="18" y1="130" x2="58" y2="130" stroke="#c2410c" stroke-width="10"/>
<line x1="58" y1="130" x2="204" y2="130" stroke="#e5e7eb" stroke-width="10"/>
<text x="118" y="152" font-size="10" fill="#64748b">每个自由度平均能量 ½kT</text>
</svg>''',
"maxwelldist": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="130" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="130" x2="226" y2="130" stroke="#475569" stroke-width="1.2"/>
<text x="16" y="26" font-size="12" fill="#475569">f(v)</text>
<text x="212" y="148" font-size="12" fill="#475569">v</text>
<path d="M 34 130 C 60 58 78 32 96 32 C 128 32 160 90 220 128" fill="none" stroke="#ea580c" stroke-width="2"/>
<line x1="96" y1="32" x2="96" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="92" y="150" font-size="10" fill="#64748b">v_p</text>
<text x="136" y="118" font-size="10" fill="#c2410c">最概然速率</text>
</svg>''',
"maxwelltemp": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="130" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="130" x2="226" y2="130" stroke="#475569" stroke-width="1.2"/>
<text x="16" y="26" font-size="12" fill="#475569">f(v)</text>
<text x="212" y="148" font-size="12" fill="#475569">v</text>
<path d="M 34 130 C 54 66 66 44 78 44 C 96 44 120 92 160 126 L 220 130" fill="none" stroke="#c2410c" stroke-width="2"/>
<path d="M 34 130 C 62 92 82 76 100 76 C 124 76 156 106 200 128 L 220 130" fill="none" stroke="#f97316" stroke-width="2"/>
<path d="M 34 130 C 70 108 96 96 118 96 C 146 96 180 116 214 129" fill="none" stroke="#fb923c" stroke-width="2"/>
<text x="62" y="40" font-size="10" fill="#c2410c">低温</text>
<text x="118" y="70" font-size="10" fill="#f97316">中温</text>
<text x="174" y="94" font-size="10" fill="#fb923c">高温</text>
</svg>''',
"boltzmann": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="24" x2="30" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<text x="14" y="32" font-size="11" fill="#475569">n</text>
<text x="214" y="150" font-size="11" fill="#475569">E</text>
<path d="M 30 40 C 100 44 150 92 224 130" fill="none" stroke="#c2410c" stroke-width="2"/>
<line x1="84" y1="26" x2="84" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="40" y="22" font-size="10" fill="#9a3412">n ∝ e^(−E/kT)</text>
<text x="96" y="98" font-size="10" fill="#c2410c">玻尔兹曼分布</text>
</svg>''',
"collisioncylinder": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="90" cy="80" r="12" fill="#fed7aa" stroke="#c2410c" stroke-width="1.6"/>
<line x1="90" y1="80" x2="200" y2="80" stroke="#ea580c" stroke-width="2"/>
<polygon points="200,80 190,75 190,85" fill="#ea580c"/>
<line x1="90" y1="52" x2="200" y2="52" stroke="#0d9488" stroke-width="1.2" stroke-dasharray="5 3"/>
<line x1="90" y1="108" x2="200" y2="108" stroke="#0d9488" stroke-width="1.2" stroke-dasharray="5 3"/>
<line x1="140" y1="52" x2="140" y2="108" stroke="#0d9488" stroke-width="1"/>
<circle cx="140" cy="80" r="9" fill="#f97316" opacity="0.5"/>
<text x="52" y="70" font-size="10" fill="#c2410c">分子</text>
<text x="146" y="44" font-size="10" fill="#0d9488">截面 πd²</text>
<text x="52" y="146" font-size="10" fill="#64748b">碰撞圆柱体积 πd² v̄ Δt</text>
</svg>''',
"meanfreepath": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="20" y="24" width="200" height="112" fill="#fffbeb" stroke="#d97706" stroke-width="1.6"/>
<path d="M 34 100 L 70 50 L 120 120 L 158 44 L 210 96" fill="none" stroke="#b45309" stroke-width="1.6"/>
<g fill="#d97706">
<circle cx="70" cy="50" r="5"/><circle cx="120" cy="120" r="5"/><circle cx="158" cy="44" r="5"/>
</g>
<g fill="#94a3b8">
<circle cx="52" cy="66" r="4"/><circle cx="146" cy="140" r="4"/><circle cx="96" cy="34" r="4"/><circle cx="190" cy="132" r="4"/>
</g>
<text x="76" y="46" font-size="10" fill="#b45309">λ</text>
<text x="30" y="150" font-size="10" fill="#64748b">分子平均自由程 λ</text>
</svg>''',
"viscosity": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="20" y="30" width="200" height="100" fill="#fffbeb" stroke="#d97706" stroke-width="1.4"/>
<line x1="20" y1="52" x2="220" y2="52" stroke="#b45309" stroke-width="1.4"/>
<line x1="20" y1="80" x2="220" y2="80" stroke="#d97706" stroke-width="1.4"/>
<line x1="20" y1="108" x2="220" y2="108" stroke="#ca8a04" stroke-width="1.4"/>
<line x1="60" y1="52" x2="120" y2="52" stroke="#dc2626" stroke-width="2"/>
<polygon points="120,52 110,48 110,56" fill="#dc2626"/>
<line x1="60" y1="108" x2="90" y2="108" stroke="#0d9488" stroke-width="2"/>
<polygon points="90,108 80,104 80,112" fill="#0d9488"/>
<text x="126" y="50" font-size="10" fill="#dc2626">快层</text>
<text x="94" y="122" font-size="10" fill="#0d9488">慢层</text>
<text x="28" y="150" font-size="10" fill="#64748b">速度梯度 du/dz 产生内摩擦力</text>
</svg>''',
"conduction": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="60" width="180" height="40" fill="#fef3c7" stroke="#b45309" stroke-width="1.6"/>
<rect x="30" y="60" width="30" height="40" fill="#dc2626"/>
<rect x="180" y="60" width="30" height="40" fill="#2563eb"/>
<text x="28" y="52" font-size="10" fill="#dc2626">高温 T₁</text>
<text x="172" y="52" font-size="10" fill="#2563eb">低温 T₂</text>
<line x1="76" y1="80" x2="164" y2="80" stroke="#b45309" stroke-width="2"/>
<polygon points="164,80 154,75 154,85" fill="#b45309"/>
<text x="94" y="74" font-size="10" fill="#92400e">dQ/dt</text>
<text x="34" y="126" font-size="10" fill="#64748b">傅里叶定律 dQ/dt = −κA dT/dx</text>
</svg>''',
"diffusion": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="20" y="30" width="200" height="100" fill="#fffbeb" stroke="#d97706" stroke-width="1.4"/>
<line x1="120" y1="30" x2="120" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<g fill="#b45309">
<circle cx="40" cy="50" r="4"/><circle cx="56" cy="70" r="4"/><circle cx="46" cy="94" r="4"/><circle cx="70" cy="112" r="4"/><circle cx="66" cy="46" r="4"/><circle cx="88" cy="88" r="4"/>
</g>
<g fill="#d97706" opacity="0.6">
<circle cx="110" cy="60" r="4"/><circle cx="140" cy="80" r="4"/><circle cx="168" cy="58" r="4"/><circle cx="190" cy="96" r="4"/><circle cx="150" cy="112" r="4"/>
</g>
<text x="30" y="150" font-size="10" fill="#64748b">浓度梯度 dn/dx 引起分子定向迁移</text>
</svg>''',
"transportcoef": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="22" width="180" height="26" rx="6" fill="#fef3c7" stroke="#b45309"/>
<text x="58" y="40" font-size="11" fill="#92400e">黏滞 η ∝ √T</text>
<rect x="30" y="66" width="180" height="26" rx="6" fill="#fef3c7" stroke="#b45309"/>
<text x="58" y="84" font-size="11" fill="#92400e">热导 κ ∝ √T</text>
<rect x="30" y="110" width="180" height="26" rx="6" fill="#fef3c7" stroke="#b45309"/>
<text x="46" y="128" font-size="11" fill="#92400e">扩散 D ∝ T^1.5 / p</text>
<text x="34" y="154" font-size="10" fill="#64748b">三系数之比由分子微观量决定</text>
</svg>''',
"vacuum": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="30" width="150" height="100" fill="#fffbeb" stroke="#ca8a04" stroke-width="1.6"/>
<g fill="#ca8a04">
<circle cx="62" cy="50" r="3"/><circle cx="140" cy="60" r="3"/><circle cx="96" cy="110" r="3"/>
</g>
<line x1="62" y1="50" x2="74" y2="58" stroke="#92400e" stroke-width="0.8"/>
<line x1="140" y1="60" x2="130" y2="82" stroke="#92400e" stroke-width="0.8"/>
<rect x="186" y="60" width="22" height="40" fill="#e5e7eb" stroke="#475569"/>
<text x="184" y="52" font-size="10" fill="#475569">真空泵</text>
<text x="34" y="150" font-size="10" fill="#64748b">平均自由程大于容器尺度即进入稀薄区</text>
</svg>''',
"workpdv": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="132" x2="226" y2="132" stroke="#475569" stroke-width="1.2"/>
<text x="16" y="26" font-size="12" fill="#475569">p</text>
<text x="214" y="150" font-size="12" fill="#475569">V</text>
<path d="M 70 40 C 110 86 150 112 210 126" fill="none" stroke="#0d9488" stroke-width="2"/>
<path d="M 70 40 L 70 118 C 110 118 150 122 198 126 L 198 132 L 70 132 Z" fill="#99f6e4" fill-opacity="0.5" stroke="none"/>
<line x1="70" y1="40" x2="70" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="198" y1="126" x2="198" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="98" y="106" font-size="10" fill="#0f766e">W = ∫p dV</text>
<text x="52" y="146" font-size="10" fill="#64748b">V₁</text>
<text x="192" y="146" font-size="10" fill="#64748b">V₂</text>
</svg>''',
"firstlaw": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="42" fill="#ccfbf1" stroke="#0d9488" stroke-width="2"/>
<text x="98" y="76" font-size="12" fill="#0f766e">内能 U</text>
<text x="98" y="98" font-size="11" fill="#0f766e">ΔU</text>
<line x1="120" y1="38" x2="120" y2="14" stroke="#ea580c" stroke-width="2"/>
<polygon points="120,14 115,24 125,24" fill="#ea580c"/>
<text x="126" y="28" font-size="11" fill="#ea580c">吸热 Q</text>
<line x1="162" y1="80" x2="216" y2="80" stroke="#2563eb" stroke-width="2"/>
<polygon points="216,80 206,75 206,85" fill="#2563eb"/>
<text x="168" y="74" font-size="11" fill="#2563eb">对外做功 W</text>
<text x="54" y="150" font-size="11" fill="#0f766e">Q = ΔU + W</text>
</svg>''',
"isoprocess": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="132" x2="226" y2="132" stroke="#475569" stroke-width="1.2"/>
<text x="16" y="26" font-size="12" fill="#475569">p</text>
<text x="214" y="150" font-size="12" fill="#475569">V</text>
<line x1="70" y1="34" x2="70" y2="120" stroke="#0d9488" stroke-width="2"/>
<text x="50" y="30" font-size="10" fill="#0d9488">等容</text>
<line x1="70" y1="50" x2="200" y2="50" stroke="#2563eb" stroke-width="2"/>
<text x="150" y="44" font-size="10" fill="#2563eb">等压</text>
<path d="M 70 36 C 110 84 150 108 210 124" fill="none" stroke="#ea580c" stroke-width="2"/>
<text x="148" y="98" font-size="10" fill="#ea580c">等温</text>
</svg>''',
"adiabatic": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="132" x2="226" y2="132" stroke="#475569" stroke-width="1.2"/>
<text x="16" y="26" font-size="12" fill="#475569">p</text>
<text x="214" y="150" font-size="12" fill="#475569">V</text>
<path d="M 60 40 C 110 92 160 118 216 128" fill="none" stroke="#ea580c" stroke-width="1.6" stroke-dasharray="5 3"/>
<path d="M 60 40 C 100 110 140 128 200 132" fill="none" stroke="#0d9488" stroke-width="2"/>
<text x="152" y="104" font-size="10" fill="#ea580c">等温</text>
<text x="150" y="130" font-size="10" fill="#0d9488">绝热</text>
<text x="56" y="34" font-size="10" fill="#64748b">同一起点</text>
</svg>''',
"heatengine": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="86" y="60" width="68" height="44" rx="8" fill="#d1fae5" stroke="#059669" stroke-width="2"/>
<text x="100" y="87" font-size="12" fill="#047857">热机</text>
<line x1="120" y1="18" x2="120" y2="58" stroke="#ea580c" stroke-width="2"/>
<polygon points="120,58 115,48 125,48" fill="#ea580c"/>
<text x="126" y="30" font-size="10" fill="#ea580c">Q₁ 高温热源</text>
<line x1="120" y1="106" x2="120" y2="146" stroke="#2563eb" stroke-width="2"/>
<polygon points="120,146 115,136 125,136" fill="#2563eb"/>
<text x="126" y="140" font-size="10" fill="#2563eb">Q₂ 低温热源</text>
<line x1="156" y1="82" x2="206" y2="82" stroke="#dc2626" stroke-width="2"/>
<polygon points="206,82 196,77 196,87" fill="#dc2626"/>
<text x="162" y="76" font-size="11" fill="#dc2626">W</text>
</svg>''',
"secondlaw": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="86" y="58" width="68" height="46" rx="8" fill="#ede9fe" stroke="#7c3aed" stroke-width="2"/>
<text x="96" y="86" font-size="12" fill="#6d28d9">热机</text>
<line x1="120" y1="18" x2="120" y2="56" stroke="#ea580c" stroke-width="2"/>
<polygon points="120,56 115,46 125,46" fill="#ea580c"/>
<text x="126" y="28" font-size="10" fill="#ea580c">Q₁</text>
<line x1="120" y1="104" x2="120" y2="146" stroke="#2563eb" stroke-width="2"/>
<polygon points="120,146 115,136 125,136" fill="#2563eb"/>
<text x="126" y="140" font-size="10" fill="#2563eb">Q₂</text>
<line x1="156" y1="81" x2="204" y2="81" stroke="#dc2626" stroke-width="2"/>
<polygon points="204,81 194,76 194,86" fill="#dc2626"/>
<text x="160" y="74" font-size="10" fill="#dc2626">W</text>
<text x="40" y="52" font-size="10" fill="#7c3aed">η = W/Q₁</text>
<text x="40" y="132" font-size="10" fill="#7c3aed">η &lt; 1</text>
</svg>''',
"carnotcycle": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="132" x2="226" y2="132" stroke="#475569" stroke-width="1.2"/>
<text x="16" y="26" font-size="12" fill="#475569">p</text>
<text x="214" y="150" font-size="12" fill="#475569">V</text>
<path d="M 60 44 C 96 110 130 126 190 128" fill="none" stroke="#dc2626" stroke-width="2"/>
<path d="M 60 44 C 76 60 84 76 86 96" fill="none" stroke="#7c3aed" stroke-width="2"/>
<path d="M 86 96 C 120 118 150 126 190 128" fill="none" stroke="#2563eb" stroke-width="2"/>
<path d="M 190 128 C 176 108 168 88 166 66 L 60 44" fill="none" stroke="#0d9488" stroke-width="2"/>
<circle cx="60" cy="44" r="3" fill="#334155"/><circle cx="86" cy="96" r="3" fill="#334155"/>
<circle cx="190" cy="128" r="3" fill="#334155"/><circle cx="166" cy="66" r="3" fill="#334155"/>
<text x="44" y="40" font-size="10" fill="#334155">1</text>
<text x="72" y="112" font-size="10" fill="#334155">2</text>
<text x="196" y="142" font-size="10" fill="#334155">3</text>
<text x="170" y="60" font-size="10" fill="#334155">4</text>
<text x="104" y="150" font-size="10" fill="#64748b">卡诺循环：两等温 + 两绝热</text>
</svg>''',
"entropy": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="18" x2="34" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="132" x2="226" y2="132" stroke="#475569" stroke-width="1.2"/>
<text x="16" y="26" font-size="12" fill="#475569">T</text>
<text x="214" y="150" font-size="12" fill="#475569">S</text>
<line x1="60" y1="100" x2="200" y2="100" stroke="#dc2626" stroke-width="2"/>
<line x1="200" y1="100" x2="200" y2="40" stroke="#7c3aed" stroke-width="2"/>
<line x1="200" y1="40" x2="60" y2="40" stroke="#2563eb" stroke-width="2"/>
<line x1="60" y1="40" x2="60" y2="100" stroke="#0d9488" stroke-width="2"/>
<circle cx="60" cy="100" r="3" fill="#334155"/><circle cx="200" cy="100" r="3" fill="#334155"/>
<circle cx="200" cy="40" r="3" fill="#334155"/><circle cx="60" cy="40" r="3" fill="#334155"/>
<text x="42" y="106" font-size="10" fill="#334155">A</text>
<text x="204" y="106" font-size="10" fill="#334155">B</text>
<text x="98" y="150" font-size="10" fill="#64748b">T-S 图上面积即交换的热量</text>
</svg>''',
"boltzmannentropy": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="112" cy="80" r="46" fill="#f3e8ff" stroke="#a855f7" stroke-width="1.6"/>
<g fill="#7c3aed">
<circle cx="96" cy="66" r="3"/><circle cx="120" cy="58" r="3"/><circle cx="134" cy="78" r="3"/><circle cx="110" cy="92" r="3"/><circle cx="90" cy="88" r="3"/>
</g>
<text x="164" y="42" font-size="10" fill="#7c3aed">微观态 W</text>
<text x="42" y="150" font-size="11" fill="#6d28d9">S = k ln W</text>
</svg>''',
"thermopotential": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="52" width="78" height="62" rx="10" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.6"/>
<text x="42" y="80" font-size="11" fill="#6d28d9">U (S,V)</text>
<text x="40" y="100" font-size="10" fill="#7c3aed">dU = TdS − pdV</text>
<rect x="132" y="52" width="78" height="62" rx="10" fill="#f3e8ff" stroke="#a855f7" stroke-width="1.6"/>
<text x="142" y="80" font-size="11" fill="#7c3aed">F, H, G</text>
<text x="140" y="100" font-size="10" fill="#a855f7">勒让德变换</text>
<line x1="108" y1="83" x2="132" y2="83" stroke="#334155" stroke-width="1.5"/>
<polygon points="132,83 124,79 124,87" fill="#334155"/>
<text x="36" y="42" font-size="10" fill="#64748b">热力学基本方程与势函数</text>
<text x="56" y="144" font-size="10" fill="#64748b">麦克斯韦关系由此导出</text>
</svg>''',
"clapeyron": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="50" y1="20" x2="50" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="50" y1="132" x2="226" y2="132" stroke="#475569" stroke-width="1.2"/>
<text x="34" y="28" font-size="12" fill="#475569">p</text>
<text x="214" y="150" font-size="12" fill="#475569">T</text>
<path d="M 70 126 C 120 106 170 74 220 40" fill="none" stroke="#7c3aed" stroke-width="2"/>
<text x="140" y="58" font-size="10" fill="#6d28d9">气液平衡线</text>
<line x1="70" y1="126" x2="70" y2="132" stroke="#94a3b8" stroke-width="1"/>
<text x="86" y="122" font-size="10" fill="#64748b">dp/dT = L/(TΔV)</text>
</svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

CORE_FORMULAS = [
    ("理想气体状态方程", "pV = nRT = \\frac{m}{M}RT", "联系压强、体积、温度与物质的量的基本物态方程"),
    ("阿伏伽德罗定律", "N = nN_A,\\quad V_m = \\frac{RT}{p}", "同温同压同体积气体含相同分子数"),
    ("玻意耳定律", "pV = \\text{const}\\quad(T\\ \\text{不变})", "等温过程中压强与体积成反比"),
    ("查理定律", "\\frac{p}{T} = \\text{const}\\quad(V\\ \\text{不变})", "等容过程中压强正比于热力学温度"),
    ("盖-吕萨克定律", "\\frac{V}{T} = \\text{const}\\quad(p\\ \\text{不变})", "等压过程中体积正比于热力学温度"),
    ("道尔顿分压定律", "p = \\sum_i p_i = \\frac{RT}{V}\\sum_i n_i", "混合气体的总压强等于各组分分压之和"),
    ("玻尔兹曼常数", "k = \\frac{R}{N_A} = 1.38\\times10^{-23}\\,\\text{J/K}", "联系宏观气体常数与微观能量尺度"),
    ("范德瓦尔斯方程", "\\left(p+\\frac{an^2}{V^2}\\right)(V-nb) = nRT", "计入分子间引力与分子体积的真实气体方程"),
    ("压缩因子", "Z = \\frac{pV_m}{RT}", "真实气体对理想气体偏离程度的量度"),
    ("对比态方程", "\\left(p_r+\\frac{3}{V_r^2}\\right)(3V_r-1) = 8T_r", "用对比参量表示的普适物态方程"),
    ("临界系数", "\\frac{p_cV_c}{RT_c} = \\frac{3}{8} = 0.375", "范德瓦尔斯气体临界压缩因子为普适常数"),
    ("对比参量定义", "p_r=\\frac{p}{p_c},\\quad V_r=\\frac{V}{V_c},\\quad T_r=\\frac{T}{T_c}", "对应态原理所用的约化状态参量"),
    ("理想气体压强公式", "p = \\frac{1}{3}nm\\overline{v^2} = \\frac{2}{3}n\\bar{\\varepsilon}_k", "气体压强由分子平动动能的统计平均决定"),
    ("平均平动动能", "\\bar{\\varepsilon}_k = \\frac{1}{2}m\\overline{v^2} = \\frac{3}{2}kT", "每个分子平动动能的统计平均值"),
    ("温度微观意义", "T = \\frac{2}{3k}\\bar{\\varepsilon}_k", "热力学温度是分子平均平动动能的量度"),
    ("能量均分定理", "\\bar{\\varepsilon} = \\frac{i}{2}kT", "每个自由度平均分配 ½kT 能量"),
    ("理想气体内能", "U = \\frac{i}{2}nRT = \\frac{m}{M}\\cdot\\frac{i}{2}RT", "理想气体内能只依赖于温度"),
    ("定容摩尔热容", "C_{V,m} = \\frac{i}{2}R", "定容条件下每摩尔气体的热容"),
    ("定压摩尔热容", "C_{p,m} = \\frac{i+2}{2}R", "定压条件下每摩尔气体的热容"),
    ("麦克斯韦速率分布", "f(v) = 4\\pi\\left(\\frac{m}{2\\pi kT}\\right)^{3/2}v^2e^{-\\frac{mv^2}{2kT}}", "平衡态下分子速率分布函数"),
    ("最概然速率", "v_p = \\sqrt{\\frac{2kT}{m}} = \\sqrt{\\frac{2RT}{M}}", "速率分布函数取极大值处的速率"),
    ("平均速率", "\\bar{v} = \\sqrt{\\frac{8kT}{\\pi m}} = \\sqrt{\\frac{8RT}{\\pi M}}", "分子速率的算术平均值"),
    ("方均根速率", "v_{rms} = \\sqrt{\\frac{3kT}{m}} = \\sqrt{\\frac{3RT}{M}}", "与分子平均动能直接相关"),
    ("玻尔兹曼分布", "n = n_0 e^{-\\frac{E_p}{kT}}, \\quad n_i = C g_i e^{-\\frac{\\varepsilon_i}{kT}}", "外场中粒子按势能的分布规律"),
    ("重力场气压公式", "p = p_0 e^{-\\frac{Mgh}{RT}}", "等温大气中压强随高度的指数衰减"),
    ("平均自由程", "\\bar{\\lambda} = \\frac{1}{\\sqrt{2}\\,n\\sigma} = \\frac{kT}{\\sqrt{2}\\,\\pi d^2 p}", "分子两次碰撞间平均走过的距离"),
    ("有效碰撞截面", "\\sigma = \\pi d^2", "把分子视为直径为 d 的刚性球"),
    ("碰撞频率", "\\bar{Z} = \\frac{\\bar{v}}{\\bar{\\lambda}} = \\sqrt{2}\\,\\pi d^2 n\\bar{v}", "单位时间内一个分子的平均碰撞次数"),
    ("总碰撞频率", "Z_{tot} = \\frac{1}{2}n\\bar{Z}V", "单位体积单位时间内分子碰撞总数"),
    ("牛顿黏滞定律", "f = \\eta A\\frac{du}{dz}", "相邻流层间的内摩擦力"),
    ("黏滞系数微观式", "\\eta = \\frac{1}{3}\\rho\\bar{v}\\bar{\\lambda}", "由密度、平均速率与自由程决定"),
    ("傅里叶热传导定律", "\\frac{dQ}{dt} = -\\kappa A\\frac{dT}{dx}", "热量由温度梯度决定地定向输运"),
    ("热导率微观式", "\\kappa = \\frac{1}{3}\\rho c_V\\bar{v}\\bar{\\lambda}", "由密度、比热与分子运动参量决定"),
    ("斐克扩散定律", "J = -D\\frac{d\\rho}{dx}", "分子数通量正比于密度梯度"),
    ("扩散系数微观式", "D = \\frac{1}{3}\\bar{v}\\bar{\\lambda}", "由平均速率与平均自由程决定"),
    ("输运过程一般公式", "\\Delta\\Phi = -\\frac{1}{3}\\bar{v}\\bar{\\lambda}\\left(\\frac{d\\Phi_0}{dz}\\right)A\\Delta t", "统一描述黏滞、热传导与扩散"),
    ("输运系数关系", "\\kappa = \\eta c_V,\\quad D = \\frac{\\eta}{\\rho} = \\frac{\\kappa}{\\rho c_V}", "三个输运系数由同一微观量组合而成"),
    ("热力学第一定律", "Q = \\Delta U + W", "能量守恒在热现象中的表述"),
    ("第一定律微分形式", "\\delta Q = dU + \\delta W = dU + p\\,dV", "无限小过程中的能量守恒"),
    ("准静态功", "W = \\int_{V_1}^{V_2} p\\,dV", "p-V 图曲线下的面积"),
    ("焓的定义", "H = U + pV", "等压过程吸热等于焓的增量"),
    ("迈耶公式", "C_{p,m} - C_{V,m} = R", "理想气体定压与定容摩尔热容之差"),
    ("比热比", "\\gamma = \\frac{C_p}{C_V} = \\frac{i+2}{i}", "绝热指数由自由度决定"),
    ("等温过程", "pV = \\text{const},\\quad W_T = nRT\\ln\\frac{V_2}{V_1}", "温度不变过程的功"),
    ("等压过程", "W_p = p(V_2-V_1),\\quad Q_p = nC_{p,m}\\Delta T", "压强不变过程的功与吸热"),
    ("等容过程", "W_V = 0,\\quad Q_V = nC_{V,m}\\Delta T", "体积不变时气体不做功"),
    ("绝热过程方程", "pV^{\\gamma} = \\text{const},\\quad TV^{\\gamma-1}=\\text{const}", "绝热可逆过程的三个等价形式"),
    ("绝热过程做功", "W_a = \\frac{p_1V_1-p_2V_2}{\\gamma-1}", "绝热膨胀对外所做的功"),
    ("多方过程", "pV^{n} = \\text{const},\\quad C_n = C_V + \\frac{R}{1-n}", "摩尔热容为常数的普遍过程"),
    ("循环过程效率", "\\eta = \\frac{W}{Q_1} = 1 - \\frac{Q_2}{Q_1}", "热机对外做功与吸热之比"),
    ("制冷系数", "\\varepsilon = \\frac{Q_2}{W} = \\frac{Q_2}{Q_1-Q_2}", "制冷机从低温热源吸热与耗功之比"),
    ("奥托循环效率", "\\eta = 1 - \\frac{1}{r^{\\gamma-1}},\\quad r=\\frac{V_1}{V_2}", "定容加热汽油机的理论效率"),
    ("卡诺效率", "\\eta_C = 1 - \\frac{T_2}{T_1}", "只取决于两热源温度的理想效率"),
    ("卡诺定理", "\\eta \\le \\eta_C = 1-\\frac{T_2}{T_1}", "所有工作于两热源间热机的效率上限"),
    ("克劳修斯不等式", "\\oint \\frac{\\delta Q}{T} \\le 0", "可逆循环取等号，不可逆循环取小于号"),
    ("熵的定义", "dS = \\frac{\\delta Q_{rev}}{T},\\quad S_B-S_A=\\int_A^B\\frac{\\delta Q_{rev}}{T}", "态函数熵由可逆过程的热温比定义"),
    ("理想气体熵变", "\\Delta S = nC_{V,m}\\ln\\frac{T_2}{T_1} + nR\\ln\\frac{V_2}{V_1}", "理想气体由状态 1 到状态 2 的熵变"),
    ("熵增原理", "\\Delta S_{iso} \\ge 0", "孤立系统熵永不减少"),
    ("玻尔兹曼熵", "S = k\\ln W", "熵是系统微观状态数的量度"),
    ("亥姆霍兹自由能", "F = U - TS,\\quad dF = -S\\,dT - p\\,dV", "等温等容过程方向的判据"),
    ("吉布斯自由能", "G = H - TS,\\quad dG = -S\\,dT + V\\,dp", "等温等压过程方向的判据"),
    ("热力学基本方程", "dU = T\\,dS - p\\,dV", "内能的全微分形式"),
    ("麦克斯韦关系", "\\left(\\frac{\\partial T}{\\partial V}\\right)_S = -\\left(\\frac{\\partial p}{\\partial S}\\right)_V", "由全微分条件导出的偏导数关系"),
    ("化学势", "\\mu = \\left(\\frac{\\partial G}{\\partial n}\\right)_{T,p}", "等温等压下每摩尔物质的吉布斯自由能"),
    ("克拉珀龙方程", "\\frac{dp}{dT} = \\frac{L}{T\\,(V_2-V_1)}", "相平衡曲线斜率的普遍关系"),
    ("克劳修斯-克拉珀龙方程", "\\ln\\frac{p_2}{p_1} = \\frac{L}{R}\\left(\\frac{1}{T_1}-\\frac{1}{T_2}\\right)", "忽略液相体积时的近似积分形式"),
    ("焦耳-汤姆孙系数", "\\mu_{JT} = \\left(\\frac{\\partial T}{\\partial p}\\right)_H", "节流过程温度随压强的变化率"),
    ("热力学第三定律", "\\lim_{T\\to0}S = 0", "绝对零度时完美晶体的熵趋于零"),
    ("信息熵", "S = -k_B\\sum_i p_i\\ln p_i", "香农熵与热力学熵的统计同构"),
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
"name": "1.1 热力学系统与平衡态",
"color": "#dc2626",
"desc": "系统与外界、平衡态、准静态过程",
"items": [
{"id":"t1s1-1","name":"热力学系统与外界","tags":["def","der"],"brief":"系统、外界与边界及三类系统的划分。",
 "fig":"thermosystem","figCap":"系统通过边界与外界交换能量与物质",
 "body": wrap(
   defn("热力学系统",p("热力学把所要研究的宏观物体（或物体群）称为<strong>热力学系统</strong>，简称系统；系统之外与之发生相互作用的部分称为<strong>外界</strong>（环境）；系统与外界的分界面称为<strong>边界</strong>。"))+
   der(p("<strong>由守恒律看系统分类：</strong>取系统为控制体，单位时间质量守恒写为：")+
   fml("\\frac{dm_{sys}}{dt} = \\dot{m}_{in} - \\dot{m}_{out}")+
   p("对封闭系统进出质量为零，质量恒定；能量守恒则写为：")+
   fml("\\frac{dE_{sys}}{dt} = \\dot{Q} - \\dot{W}")+
   p("对孤立系统 $\\dot{Q}=0$、$\\dot{W}=0$，总能量守恒 $dE_{sys}/dt=0$。据此把系统分为开放、封闭与孤立三类，分类的实质是边界允许通过什么。"))+
   note(p("恰当选择系统可简化问题：研究气缸内气体时取气体为系统，则活塞对气体做功为负值；取气体加活塞为系统则可把外力功化为内部功。"))
 )},
{"id":"t1s1-2","name":"平衡态","tags":["def","der"],"brief":"不受外界影响时宏观性质不随时间变化的状态。",
 "body": wrap(
   defn("平衡态",p("在不受外界影响的条件下，系统各部分宏观性质长时间不发生变化的状态称为<strong>平衡态</strong>。它要求力学平衡、热平衡与相平衡同时满足，是一种<strong>动态平衡</strong>，分子仍在不停运动与碰撞。"))+
   der(p("<strong>由弛豫时间理解平衡态的判据：</strong>设系统偏离平衡的小扰动按指数衰减，弛豫时间 $\\tau$ 决定恢复快慢：")+
   fml("\\Delta X(t) = \\Delta X(0)\\,e^{-t/\\tau}")+
   p("当观测时间 $t\\gg\\tau$ 时系统方可视为处于平衡态。令时间导数为零得平衡条件：")+
   fml("\\frac{dX}{dt} = 0,\\qquad \\frac{\\partial T}{\\partial \\mathbf{r}}=0,\\quad \\frac{\\partial p}{\\partial \\mathbf{r}}=0")+
   p("即温度、压强等强度量处处均匀且不随时间变化，这就是平衡态的判据。"))+
   note(p("平衡态是热力学的基本假设之一，只有平衡态才能用少数几个态参量加以描述；非平衡态需用分布函数或场量描述。"))
 )},
{"id":"t1s1-3","name":"准静态过程与可逆过程","tags":["def","der"],"brief":"无限缓慢、时时处于平衡态的过程。",
 "body": wrap(
   defn("准静态过程",p("若过程进行得足够慢，使系统在每一瞬间都无限接近平衡态，则称该过程为<strong>准静态过程</strong>。只有准静态过程才能在状态图上用一条连续曲线表示。"))+
   der(p("<strong>由功的表达式看准静态条件：</strong>气体膨胀 $dV$ 时对外做功 $\\delta W=p\\,dV$，此式要求压强在气体中处处均匀。设活塞速度为 $u$、气体中声速为 $c_s$，当：")+
   fml("u \\ll c_s")+
   p("时压强波有足够时间传播，$p$ 有确定值。否则压强不再均匀，$\\delta W=p\\,dV$ 失效。对整个体积积分得：")+
   fml("W = \\int_{V_1}^{V_2} p\\,dV")+
   p("可逆过程还要求无耗散，退回原路径时环境恢复原状；此时 $\\oint dU=0$ 而 $\\oint \\delta W\\neq0$，体现态函数与过程量的区别。"))+
   note(p("准静态过程不一定是可逆过程（如存在摩擦时），但可逆过程一定是准静态过程；无摩擦的准静态过程才是可逆过程。"))
 )},
]},
{
"name": "1.2 状态参量与状态函数",
"color": "#e11d48",
"desc": "状态参量、物态方程、态函数与广延强度量",
"items": [
{"id":"t1s2-1","name":"状态参量与物态方程","tags":["def","der"],"brief":"描述平衡态的宏观量及其约束关系。",
 "body": wrap(
   defn("状态参量",p("描述系统平衡态所需要的独立宏观变量称为<strong>状态参量</strong>，如几何参量（体积 $V$）、力学参量（压强 $p$）、热学参量（温度 $T$）与化学参量（物质的量 $n$）。它们之间的函数关系称为<strong>物态方程</strong>：")+
   fml("f(p,V,T)=0"))+
   der(p("<strong>独立参量数目与循环关系：</strong>对单组元均匀系，状态由 $(p,V,T)$ 描述，但物态方程给出一约束，故独立变量只有两个。由隐函数定理，若 $\\partial f/\\partial p\\neq0$，可解出：")+
   fml("p = p(V,T) \\implies dp = \\left(\\frac{\\partial p}{\\partial V}\\right)_T dV + \\left(\\frac{\\partial p}{\\partial T}\\right)_V dT")+
   p("同理可写出 $dV$、$dT$ 的微分，消去 $dp$ 即得三个偏导数之间的循环关系：")+
   fml("\\left(\\frac{\\partial p}{\\partial V}\\right)_T\\left(\\frac{\\partial V}{\\partial T}\\right)_p\\left(\\frac{\\partial T}{\\partial p}\\right)_V = -1")+
   p("说明三个偏导数并非独立，测出其中两个即可推出第三个，这是实验测定物态方程的基础。"))+
   note(p("理想气体的物态方程最简单，真实气体的物态方程往往以维里展开或经验公式表示。"))
 )},
{"id":"t1s2-2","name":"态函数与路径无关性","tags":["def","der"],"brief":"只由状态决定而与路径无关的物理量。",
 "body": wrap(
   defn("态函数",p("只取决于系统当前状态、而与到达该状态所经历的过程无关的物理量称为<strong>态函数</strong>，如内能 $U$、熵 $S$、焓 $H$。其微分是全微分，沿任意闭合路径积分等于零。"))+
   der(p("<strong>全微分判据：</strong>设态函数 $Z=Z(x,y)$，则其微分为：")+
   fml("dZ = M\\,dx + N\\,dy,\\qquad M=\\left(\\frac{\\partial Z}{\\partial x}\\right)_y,\\ N=\\left(\\frac{\\partial Z}{\\partial y}\\right)_x")+
   p("由混合偏导数与求导次序无关，得全微分条件：")+
   fml("\\left(\\frac{\\partial M}{\\partial y}\\right)_x = \\left(\\frac{\\partial N}{\\partial x}\\right)_y \\iff \\oint dZ = 0")+
   p("反之，若某量微分的混合偏导数一般不相等（如功 $\\delta W=p\\,dV$ 中 $p$ 与 $V$ 并不独立），则它是过程量而非态函数。"))+
   note(p("内能、熵、焓是态函数，功与热量是过程量。这正是第一定律 $Q=\\Delta U+W$ 中必须把 $\\Delta U$ 写成差分而把 $Q$、$W$ 视为路径相关量的原因。"))
 )},
{"id":"t1s2-3","name":"广延量与强度量","tags":["def","der"],"brief":"与系统质量成正比或无关的两类物理量。",
 "body": wrap(
   defn("广延量与强度量",p("与系统质量或体积成正比、具有可加性的量称为<strong>广延量</strong>，如质量、体积、内能、熵；与质量无关、不具有可加性的量称为<strong>强度量</strong>，如温度、压强、密度、化学势。"))+
   der(p("<strong>欧拉齐次函数定理：</strong>广延内能 $U$ 是各广延量的一次齐次函数，即 $U(\\lambda S,\\lambda V,\\lambda n)=\\lambda U(S,V,n)$。对 $\\lambda$ 求导并令 $\\lambda=1$：")+
   fml("U = \\left(\\frac{\\partial U}{\\partial S}\\right)_{V,n}S + \\left(\\frac{\\partial U}{\\partial V}\\right)_{S,n}V + \\left(\\frac{\\partial U}{\\partial n}\\right)_{S,V}n")+
   p("由热力学基本方程识别偏导数含义 $\\partial U/\\partial S=T$、$\\partial U/\\partial V=-p$、$\\partial U/\\partial n=\\mu$，得欧拉关系：")+
   fml("U = TS - pV + \\mu n")+
   p("代入焓、自由能定义即得 $H=TS+\\mu n$、$G=\\mu n$，说明化学势就是每摩尔吉布斯自由能。"))+
   note(p("两个广延量之比是强度量（如密度 $\\rho=m/V$）；强度量不能简单相加，广延量可以相加。这一规则是检验热力学关系是否合理的快捷判据。"))
 )},
]},
{
"name": "1.3 温度与温标",
"color": "#ef4444",
"desc": "热平衡与第零定律、经验温标、理想气体温标与热力学温标",
"items": [
{"id":"t1s3-1","name":"热平衡与热力学第零定律","tags":["thm","der"],"brief":"互为热平衡的系统具有相同温度。",
 "body": wrap(
   thm("热力学第零定律",p("若系统 $A$ 与 $B$ 分别与系统 $C$ 处于热平衡，则 $A$ 与 $B$ 也彼此处于热平衡。由此可引入一个态函数——温度，它是一切互为热平衡系统的共同属性。"))+
   der(p("<strong>温度的引入：</strong>设 $A$、$C$ 达到热平衡，其态参量满足关系 $F_{AC}(p_A,V_A;p_C,V_C)=0$；同理 $B$、$C$ 满足 $F_{BC}=0$。")+
   fml("F_{AC}(p_A,V_A;\\,\\theta)=0,\\qquad F_{BC}(p_B,V_B;\\,\\theta)=0")+
   p("由第零定律，$A$ 与 $B$ 也处于热平衡，故两式可各自解出同一个量 $\\theta$：")+
   fml("\\theta = \\theta_A(p_A,V_A) = \\theta_B(p_B,V_B)")+
   p("这个对所有互为热平衡系统都相同的量 $\\theta$ 就定义为<strong>温度</strong>；温度相等正是热平衡的判据。"))+
   note(p("第零定律保证了温度概念的传递性与自洽性，是建立温标、进行温度测量的逻辑前提，故虽发现较晚仍命名为第零定律。"))
 )},
{"id":"t1s3-2","name":"经验温标与理想气体温标","tags":["def","der"],"brief":"以测温属性线性变化定义的温标。",
 "body": wrap(
   defn("经验温标",p("选定测温物质的某一随温度单调变化的属性 $X$（如水银体积、电阻、气体压强），规定温度与 $X$ 成线性关系 $t=aX+b$，并用两个固定点定标，就得到一种<strong>经验温标</strong>。"))+
   der(p("<strong>由理想气体定标：</strong>取定容气体温度计，保持体积不变，压强随温度线性变化。用水冰点 $t_0$ 与汽化点 $t_{100}$ 定标：")+
   fml("t = 100\\,\\frac{p-p_0}{p_{100}-p_0}\\quad(\\text{摄氏温标})")+
   p("逐步减小测温气体量（降低压强）外推，各种气体给出的温标趋于同一极限，定义理想气体温标：")+
   fml("T = 273.16\\,\\lim_{p\\to0}\\frac{p}{p_{tr}}\\ \\text{K}")+
   p("其中 $p_{tr}$ 为水的三相点压强。极限与外推所得温标不依赖具体气体，故可作为标准温标。"))+
   app(p("<strong>应用：</strong>理想气体温标覆盖很宽范围，是国际温标在中低温区复现的基础；高温用黑体辐射、极低温用磁温度计等一级测温手段延伸。"))
 )},
{"id":"t1s3-3","name":"热力学温标与温标换算","tags":["def","der"],"brief":"不依赖测温物质的热力学温标。",
 "body": wrap(
   defn("热力学温标",p("开尔文根据卡诺定理提出：以可逆卡诺热机与热源交换的热量之比定义温度，$T_1/T_2=Q_1/Q_2$。该定义只依赖热量测量，与测温物质无关，称为<strong>热力学温标</strong>。"))+
   der(p("<strong>两种温标的一致性：</strong>对理想气体卡诺循环，两段等温过程吸放热为：")+
   fml("Q_1 = nRT_1\\ln\\frac{V_2}{V_1},\\qquad Q_2 = nRT_2\\ln\\frac{V_3}{V_4}")+
   p("由绝热关系 $T_1V_2^{\\gamma-1}=T_2V_3^{\\gamma-1}$ 与 $T_1V_1^{\\gamma-1}=T_2V_4^{\\gamma-1}$ 相除得 $V_2/V_1=V_3/V_4$，于是：")+
   fml("\\frac{Q_1}{Q_2} = \\frac{T_1}{T_2}")+
   p("这与热力学温标的定义一致，故理想气体温标与热力学温标在适用范围内数值相同，两者关系为 $t=T-273.15$。"))+
   note(p("热力学温标的零点为绝对零度，是理想化的下限；热力学第三定律指出不可能通过有限步骤达到绝对零度。"))
 )},
]},
{
"name": "1.4 理想气体状态方程",
"color": "#b91c1c",
"desc": "三条实验定律、状态方程、混合理气与气体常数",
"items": [
{"id":"t1s4-1","name":"气体的三条实验定律","tags":["thm","der"],"brief":"玻意耳、查理与盖-吕萨克定律。",
 "fig":"isotherms","figCap":"不同温度下理想气体的等温线，温度越高曲线越靠外",
 "body": wrap(
   thm("气体三定律",p("玻意耳定律（等温）$pV=\\text{const}$；查理定律（等容）$p/T=\\text{const}$；盖-吕萨克定律（等压）$V/T=\\text{const}$。它们分别描述单一过程参量关系。"))+
   der(p("<strong>由三定律导出统一方程：</strong>设气体由态 1 $(p_1,V_1,T_1)$ 经等温到中间态 $(p',V_2,T_1)$，再经等容到态 2 $(p_2,V_2,T_2)$：")+
   fml("p_1V_1 = p'V_2,\\qquad \\frac{p'}{T_1} = \\frac{p_2}{T_2}")+
   p("由第一式得 $p'=p_1V_1/V_2$，代入第二式消去 $p'$：")+
   fml("\\frac{p_1V_1}{V_2 T_1} = \\frac{p_2}{T_2} \\implies \\frac{p_1V_1}{T_1} = \\frac{p_2V_2}{T_2} = \\text{const}")+
   p("可见三定律是同一状态方程在不同约束下的特例，$pV/T$ 是与路径无关的常量。"))+
   note(p("真实气体只在压强趋于零的极限下严格满足三定律，故理想气体是低压高温的极限模型。"))
 )},
{"id":"t1s4-2","name":"理想气体状态方程","tags":["thm","der"],"brief":"pV=nRT 的多种等价形式。",
 "fig":"pvdiagram","figCap":"p-V 图上的等温线：理想气体过程曲线",
 "body": wrap(
   thm("理想气体状态方程",p("对 $n$ 摩尔理想气体：")+
   fml("pV = nRT = \\frac{m}{M}RT = NkT")+
   p("其中 $R=8.314\\,\\text{J/(mol·K)}$ 为气体常数，$M$ 为摩尔质量，$N$ 为分子数。"))+
   der(p("<strong>化为分子数密度形式：</strong>把 $n=N/N_A$ 代入状态方程：")+
   fml("pV = \\frac{N}{N_A}RT = N\\frac{R}{N_A}T = NkT")+
   p("其中 $k=R/N_A=1.38\\times10^{-23}\\,\\text{J/K}$ 为玻尔兹曼常数；记分子数密度 $n=N/V$ 得：")+
   fml("p = nkT")+
   p("该式把宏观压强与微观分子数密度、温度直接联系起来；再结合压强微观公式 $p=\\frac{1}{3}nm\\overline{v^2}$ 即可导出温度的微观意义。"))+
   app(p("<strong>应用：</strong>状态方程用于计算气缸内气体做功、气体质量流量、大气密度随高度的变化，也是热机循环计算的出发点。"))
 )},
{"id":"t1s4-3","name":"混合理气体与道尔顿分压定律","tags":["thm","der"],"brief":"混合气体总压等于各组分分压之和。",
 "body": wrap(
   thm("道尔顿分压定律",p("互不反应的几种理想气体混合后，总压强等于各组分单独占据同一体积、处于同一温度时的分压之和：")+
   fml("p = \\sum_i p_i,\\qquad p_i = \\frac{n_i RT}{V}"))+
   der(p("<strong>推导：</strong>理想气体分子间无相互作用，各组分对壁面的碰撞冲量贡献相互独立。设第 $i$ 种气体分子数为 $N_i$，由 $p=nkT$ 得分压：")+
   fml("p_i = \\frac{N_i kT}{V}")+
   p("总压为各组分贡献之和：")+
   fml("p = \\sum_i \\frac{N_i kT}{V} = \\frac{kT}{V}\\sum_i N_i = nkT")+
   p("其中 $n=\\sum_i N_i/V$ 为总分子数密度，故总压等于各分压之和，且分压之比等于摩尔数之比。"))+
   exa(p("<strong>例：</strong>空气中 $\\text{O}_2$ 约占 21%、$\\text{N}_2$ 约占 79%，在 $p=101.3\\,\\text{kPa}$ 下 $p_{\\text{O}_2}=0.21\\times101.3\\approx21.3\\,\\text{kPa}$，$p_{\\text{N}_2}\\approx80.0\\,\\text{kPa}$。"))+
   app(p("<strong>应用：</strong>呼吸生理中氧分压决定血氧饱和度；潜水、高原医学、气体分离与真空系统中均需按分压处理混合气体。"))
 )},
{"id":"t1s4-4","name":"阿伏伽德罗定律与气体常数","tags":["thm","der"],"brief":"同温同压同体积含相同分子数。",
 "body": wrap(
   thm("阿伏伽德罗定律",p("在相同温度与压强下，相同体积的任何理想气体含有相同的分子数。$1\\,\\text{mol}$ 任何气体含 $N_A=6.022\\times10^{23}$ 个分子，标准状况下摩尔体积约 $22.4\\,\\text{L}$。"))+
   der(p("<strong>由状态方程论证：</strong>对两种气体分别写出状态方程并取相同 $p$、$T$、$V$：")+
   fml("pV = N_1 kT = N_2 kT \\implies N_1 = N_2")+
   p("可见分子数与气体种类无关。标准状况（$T=273.15\\,\\text{K}$、$p=101.325\\,\\text{kPa}$）下摩尔体积为：")+
   fml("V_m = \\frac{RT}{p} = \\frac{8.314\\times273.15}{1.013\\times10^{5}}\\approx 2.24\\times10^{-2}\\,\\text{m}^3/\\text{mol}")+
   p("即 $22.4\\,\\text{L/mol}$。这也是连接宏观量 $R$ 与微观量 $k$ 的桥梁：$R=N_A k$。"))+
   note(p("阿伏伽德罗定律为相对分子质量测定提供依据；配合密度测量可反推未知气体摩尔质量 $M=\\rho RT/p$。"))
 )},
]},
{
"name": "1.5 范德瓦尔斯方程与真实气体",
"color": "#f43f5e",
"desc": "分子力与势能、范德瓦尔斯方程、真实气体等温线与临界点",
"items": [
{"id":"t1s5-1","name":"分子力与分子势能","tags":["def","der"],"brief":"分子间引斥力与势能曲线。",
 "body": wrap(
   defn("分子间作用力",p("分子间同时存在斥力与引力：在很短距离（小于 $10^{-10}\\,\\text{m}$）内表现为斥力，稍远处表现为引力，距离再大则迅速趋于零。对应势能 $E_p(r)$ 在平衡距离 $r_0$ 处取极小值。"))+
   der(p("<strong>由势能求力：</strong>分子间作用力是势能的负梯度：")+
   fml("F(r) = -\\frac{dE_p}{dr}")+
   p("取 Lennard-Jones 势作为模型：")+
   fml("E_p(r) = 4\\varepsilon\\left[\\left(\\frac{\\sigma}{r}\\right)^{12} - \\left(\\frac{\\sigma}{r}\\right)^{6}\\right]")+
   p("求导得：")+
   fml("F(r) = 4\\varepsilon\\left[\\frac{12\\sigma^{12}}{r^{13}} - \\frac{6\\sigma^{6}}{r^{7}}\\right]")+
   p("$r$ 很小时第一项占优给出斥力，$r$ 较大时第二项占优给出引力；令 $dE_p/dr=0$ 得平衡距离 $r_0=2^{1/6}\\sigma$，此处势能最小、作用力为零。"))+
   note(p("分子势能的存在正是真实气体内能依赖于体积的原因：$U$ 既含分子动能，又含由分子间距决定的势能。"))
 )},
{"id":"t1s5-2","name":"范德瓦尔斯方程","tags":["thm","der"],"brief":"对理想气体方程的两项修正。",
 "fig":"vanderwaals","figCap":"范德瓦尔斯等温线：临界温度以下出现气液共存段",
 "body": wrap(
   thm("范德瓦尔斯方程",p("计入分子本身体积与分子间引力，$1\\,\\text{mol}$ 气体的物态方程为：")+
   fml("\\left(p+\\frac{a}{V_m^2}\\right)(V_m-b) = RT")+
   p("$b$ 为分子有效体积修正，$a$ 为引力修正系数。"))+
   der(p("<strong>逐项修正：</strong>其一，分子有体积，可活动空间由 $V_m$ 减为 $V_m-b$，故用 $V_m-b$ 代替 $V_m$。")+
   p("其二，分子间引力使靠近器壁的分子受到向内的净拉力，实测压强比无引力时小，需加上内压强项。内压强正比于分子数密度平方：")+
   fml("p_{in} = a\\left(\\frac{n}{V}\\right)^2 = \\frac{a}{V_m^2}")+
   p("于是真实压强 $p = p_{ideal} - a/V_m^2$，即 $p_{ideal}=p+a/V_m^2$。代回理想气体方程得：")+
   fml("\\left(p+\\frac{a}{V_m^2}\\right)(V_m-b)=RT")+
   p("对方程求导可确定临界点条件 $(\\partial p/\\partial V_m)_T=0$ 与 $(\\partial^2 p/\\partial V_m^2)_T=0$。"))+
   app(p("<strong>应用：</strong>范德瓦尔斯方程定性描述了气液相变、临界现象与焦耳-汤姆孙效应，是理解真实气体行为的经典模型；$a$、$b$ 可由临界参量反求。"))
 )},
{"id":"t1s5-3","name":"真实气体的等温线与临界点","tags":["der","exa"],"brief":"临界温度以上气液无法区分。",
 "fig":"criticalpoint","figCap":"临界点 C 处等温线出现拐点，下方为气液共存区",
 "body": wrap(
   der(p("<strong>由范德瓦尔斯方程求临界参量：</strong>把方程写成 $p=\\frac{RT}{V_m-b}-\\frac{a}{V_m^2}$，临界点满足两个条件：")+
   fml("\\left(\\frac{\\partial p}{\\partial V_m}\\right)_T=0,\\qquad \\left(\\frac{\\partial^2 p}{\\partial V_m^2}\\right)_T=0")+
   p("两式分别给出 $\\frac{RT_c}{(V_c-b)^2}=\\frac{2a}{V_c^3}$ 与 $\\frac{2RT_c}{(V_c-b)^3}=\\frac{6a}{V_c^4}$，联立解得：")+
   fml("V_c = 3b,\\qquad T_c=\\frac{8a}{27Rb},\\qquad p_c=\\frac{a}{27b^2}")+
   p("代入可得临界压缩因子 $Z_c=p_cV_c/(RT_c)=3/8$，与具体气体无关。当 $T>T_c$ 时等温线单调下降，气液无法区分；$T<T_c$ 时出现水平的气液共存段。"))+
   exa(p("<strong>例（二氧化碳）：</strong>实验值 $T_c=304.2\\,\\text{K}$、$p_c=7.38\\,\\text{MPa}$，由 $Z_c=3/8$ 估算 $V_c\\approx0.128\\,\\text{L/mol}$，与实测同量级，说明范德瓦尔斯模型抓住了临界现象的主要特征。"))+
   note(p("临界温度以上，无论加多大压强气体都不能液化，这正是液化气体必须先降温的原因。"))
 )},
]},
{
"name": "1.6 物态方程与临界现象",
"color": "#9f1239",
"desc": "压缩因子、维里方程、对应态原理与相图",
"items": [
{"id":"t1s6-1","name":"物态方程与压缩因子","tags":["def","der"],"brief":"真实气体偏离理想程度的量化。",
 "body": wrap(
   defn("压缩因子",p("定义压缩因子 $Z=pV_m/(RT)$ 衡量真实气体对理想气体的偏离：$Z=1$ 为理想气体；$Z<1$ 表明分子间引力占优；$Z>1$ 表明分子体积（斥力）效应占优。"))+
   der(p("<strong>维里展开：</strong>把 $Z$ 按 $1/V_m$ 的幂次展开，得到维里方程：")+
   fml("Z = \\frac{pV_m}{RT} = 1 + \\frac{B(T)}{V_m} + \\frac{C(T)}{V_m^2} + \\cdots")+
   p("由范德瓦尔斯方程展开可识别第二维里系数：")+
   fml("B(T) = b - \\frac{a}{RT}")+
   p("当 $T$ 很低时 $a/RT$ 占优使 $B<0$，$Z<1$（引力主导）；当 $T>T_B=a/(Rb)$（玻意耳温度）时 $B>0$，$Z>1$（体积效应主导）。令 $B(T)=0$ 即得玻意耳温度。"))+
   app(p("<strong>应用：</strong>天然气、制冷剂等工程计算常用维里系数或通用压缩因子图修正状态方程，以获得准确的质量流量与储气量。"))
 )},
{"id":"t1s6-2","name":"对应态原理与对比态方程","tags":["thm","der"],"brief":"以临界量归一化后物态方程普适化。",
 "body": wrap(
   thm("对应态原理",p("不同物质在相同对比温度、对比压强下具有近似相同的压缩因子，即物态方程可写成只含对比参量的普适形式：")+
   fml("Z = f(p_r, T_r),\\qquad p_r=\\frac{p}{p_c},\\ V_r=\\frac{V}{V_c},\\ T_r=\\frac{T}{T_c}"))+
   der(p("<strong>由范德瓦尔斯方程导出：</strong>引入对比参量 $p=p_rp_c$、$V_m=V_rV_c$、$T=T_rT_c$，代入 $V_c=3b$、$T_c=8a/(27Rb)$、$p_c=a/(27b^2)$：")+
   fml("\\left(p_r p_c+\\frac{a}{V_r^2V_c^2}\\right)(V_rV_c-b)=RT_rT_c")+
   p("把三个临界参量代入并约去 $a,b,R$，得不含物质参量的普适方程：")+
   fml("\\left(p_r+\\frac{3}{V_r^2}\\right)(3V_r-1)=8T_r")+
   p("任何服从范德瓦尔斯方程的气体都满足此式，这正是对应态原理的解析体现。"))+
   app(p("<strong>应用：</strong>用通用压缩因子图由 $p_r$、$T_r$ 查得 $Z$，即可估算任意气体的 $p$、$V$、$T$ 关系，避免逐一测定物态方程。"))
 )},
{"id":"t1s6-3","name":"相图与三相点","tags":["der","app"],"brief":"固液气三态随温度压强的分布。",
 "fig":"phasediagram","figCap":"典型相图：三条相平衡曲线交于三相点，气液线终止于临界点",
 "body": wrap(
   der(p("<strong>相平衡曲线斜率——克拉珀龙方程：</strong>两相平衡时化学势相等 $\\mu_1(T,p)=\\mu_2(T,p)$。沿平衡曲线移动 $dT$、$dp$ 仍保持相等：")+
   fml("d\\mu_1 = d\\mu_2 \\implies -S_{m,1}dT+V_{m,1}dp = -S_{m,2}dT+V_{m,2}dp")+
   p("整理得相平衡曲线斜率：")+
   fml("\\frac{dp}{dT} = \\frac{S_{m,2}-S_{m,1}}{V_{m,2}-V_{m,1}} = \\frac{L}{T\\,\\Delta V_m}")+
   p("其中 $L=T\\Delta S_m$ 为相变潜热。多数物质熔化时 $\\Delta V>0$，故熔化曲线斜率为正；水因冰的密度小于水而斜率为负。"))+
   app(p("<strong>应用：</strong>相图是材料、化工与低温工程的基本工具。三条曲线的交点即三相点，水的三相点温度 $273.16\\,\\text{K}$ 是热力学温标的固定点；超临界流体萃取、干冰升华制冷均利用相图特性。"))
 )},
]},
]
ch2_sections = [
{
"name": "2.1 分子动理论与压强的微观解释",
"color": "#ea580c",
"desc": "分子动理论、理想气体微观模型与压强公式",
"items": [
{"id":"t2s1-1","name":"分子动理论的基本观点","tags":["def","der"],"brief":"物质由大量分子组成，分子永不停息地热运动。",
 "body": wrap(
   defn("分子动理论",p("分子动理论有三条基本观点：物质由大量分子组成；分子永不停息地做无规则热运动；分子间存在相互作用力。布朗运动与扩散现象是其直接实验证据。"))+
   der(p("<strong>由阿伏伽德罗常数估计分子尺度：</strong>设液体摩尔质量为 $M$、密度为 $\\rho$，每个分子平均占据体积约 $M/(\\rho N_A)$，分子直径量级为：")+
   fml("d \\approx \\left(\\frac{M}{\\rho N_A}\\right)^{1/3}")+
   p("以水为例 $M=0.018\\,\\text{kg/mol}$、$\\rho=10^3\\,\\text{kg/m}^3$：")+
   fml("d \\approx \\left(\\frac{0.018}{10^3\\times6.02\\times10^{23}}\\right)^{1/3}\\approx 3.1\\times10^{-10}\\,\\text{m}")+
   p("与分子直径的公认量级 $10^{-10}\\,\\text{m}$ 相符，说明分子极小但数目极大。"))+
   note(p("标准状况下 $1\\,\\text{cm}^3$ 气体约含 $2.7\\times10^{19}$ 个分子，分子间距约为自身直径的 10 倍，这正是气体易被压缩的原因。"))
 )},
{"id":"t2s1-2","name":"理想气体的微观模型","tags":["def","der"],"brief":"分子弹性小球、除碰撞外无相互作用。",
 "fig":"idealgasmodel","figCap":"理想气体微观模型：分子视为弹性小球，除碰撞外无相互作用",
 "body": wrap(
   defn("理想气体微观模型",p("理想气体的微观模型含四条假设：分子本身线度远小于分子间距；除碰撞瞬间外分子间无相互作用；分子间及分子与器壁的碰撞是完全弹性碰撞；大量分子运动服从统计规律。"))+
   der(p("<strong>由模型估计分子间距：</strong>设分子数密度为 $n$，每个分子平均占据体积 $1/n$，分子平均间距为：")+
   fml("l \\approx n^{-1/3}")+
   p("由压强公式 $p=nkT$ 导出 $n=p/kT$，代入得：")+
   fml("l \\approx \\left(\\frac{kT}{p}\\right)^{1/3}")+
   p("常温常压下 $T=300\\,\\text{K}$、$p=10^5\\,\\text{Pa}$ 得 $l\\approx3.4\\times10^{-9}\\,\\text{m}$，确为分子直径的十倍以上，模型假设自洽。"))+
   note(p("模型忽略分子间势能，故理想气体内能只含动能、仅是温度的函数；高压低温下假设失效，需引入真实气体模型。"))
 )},
{"id":"t2s1-3","name":"压强的微观本质与推导","tags":["thm","der"],"brief":"压强是大量分子碰撞器壁的统计平均冲量。",
 "fig":"pressuremicro","figCap":"分子与器壁弹性碰撞，动量变化 2mv_x 给出冲量",
 "body": wrap(
   thm("理想气体压强公式",p("气体压强由大量分子对器壁的碰撞产生，其统计表达式为：")+
   fml("p = \\frac{1}{3}nm\\overline{v^2} = \\frac{2}{3}n\\bar{\\varepsilon}_k")+
   p("$n$ 为分子数密度，$m$ 为分子质量，$\\overline{v^2}$ 为速率平方的平均值。"))+
   der(p("<strong>推导：</strong>取边长 $L$ 的立方体，考虑速度分量为 $v_x$ 的分子在垂直于 $x$ 的两壁间往返。每次碰撞动量变化 $2mv_x$，往返一次用时 $2L/v_x$，其施于壁面的平均力为：")+
   fml("f_i = \\frac{2mv_{xi}}{2L/v_{xi}} = \\frac{mv_{xi}^2}{L}")+
   p("对所有 $N$ 个分子求和得壁面所受总力，除以面积 $L^2$ 得压强：")+
   fml("p = \\frac{1}{L^3}\\sum_i m v_{xi}^2 = nm\\overline{v_x^2}")+
   p("由各向同性 $\\overline{v_x^2}=\\overline{v_y^2}=\\overline{v_z^2}=\\frac{1}{3}\\overline{v^2}$，代入得：")+
   fml("p = \\frac{1}{3}nm\\overline{v^2}")+
   p("推导中碰撞视为弹性且用到大量分子的统计平均，故压强是宏观统计量而非单个分子的属性。"))+
   app(p("<strong>应用：</strong>该式揭示压强的微观本质：增大分子数密度或提高平均动能（升温）都会使压强增大；与 $p=nkT$ 结合即得温度的微观意义。"))
 )},
]},
{
"name": "2.2 温度的微观意义与能量均分定理",
"color": "#f97316",
"desc": "温度微观意义、自由度、能量均分与内能",
"items": [
{"id":"t2s2-1","name":"温度的微观意义","tags":["thm","der"],"brief":"温度是分子平均平动动能的量度。",
 "body": wrap(
   thm("温度的微观意义",p("把压强微观公式与理想气体状态方程比较，得分子平均平动动能与温度的关系：")+
   fml("\\bar{\\varepsilon}_k = \\frac{1}{2}m\\overline{v^2} = \\frac{3}{2}kT")+
   p("温度是分子平均平动动能的量度，这是温度的统计意义。"))+
   der(p("<strong>推导：</strong>由压强微观公式与 $p=nkT$：")+
   fml("\\frac{1}{3}nm\\overline{v^2} = nkT")+
   p("两边约去 $n$：")+
   fml("\\frac{1}{3}m\\overline{v^2} = kT \\implies \\frac{1}{2}m\\overline{v^2} = \\frac{3}{2}kT")+
   p("由此得方均根速率 $v_{rms}=\\sqrt{3kT/m}=\\sqrt{3RT/M}$，温度越高分子运动越剧烈。"))+
   note(p("温度是大量分子的统计平均结果，对单个分子谈温度没有意义；绝对零度时经典理论给出分子动能趋于零，实际由量子零点能所限。"))
 )},
{"id":"t2s2-2","name":"自由度与能量均分定理","tags":["thm","der"],"brief":"每个自由度平均能量 ½kT。",
 "fig":"equipartition","figCap":"平动、转动与振动自由度对能量的贡献",
 "body": wrap(
   thm("能量均分定理",p("在温度为 $T$ 的平衡态下，分子每一个平方项自由度的平均动能都等于 $\\frac{1}{2}kT$。若分子有 $i$ 个自由度，则平均总动能为 $\\frac{i}{2}kT$。"))+
   der(p("<strong>由麦克斯韦分布求平均：</strong>以 $x$ 方向平动为例，由玻尔兹曼因子得速度分布，平均动能为：")+
   fml("\\bar{\\varepsilon}_x = \\frac{\\int_{-\\infty}^{\\infty}\\frac{1}{2}mv_x^2\\,e^{-mv_x^2/2kT}\\,dv_x}{\\int_{-\\infty}^{\\infty}e^{-mv_x^2/2kT}\\,dv_x}")+
   p("利用高斯积分 $\\int_{-\\infty}^{\\infty}x^2e^{-ax^2}dx=\\frac{1}{2}\\sqrt{\\frac{\\pi}{a^3}}$、$\\int_{-\\infty}^{\\infty}e^{-ax^2}dx=\\sqrt{\\frac{\\pi}{a}}$，取 $a=m/2kT$ 得：")+
   fml("\\bar{\\varepsilon}_x = \\frac{1}{2}kT")+
   p("三个平动方向及转动、振动自由度同理，每个平方项贡献 $\\frac{1}{2}kT$，故 $i$ 个自由度总能量为 $\\frac{i}{2}kT$。"))+
   note(p("单原子分子 $i=3$（平动），刚性双原子分子 $i=5$（3 平动加 2 转动），刚性多原子分子 $i=6$；振动自由度还含势能，每个振动自由度贡献 $kT$。"))
 )},
{"id":"t2s2-3","name":"理想气体内能与定容热容","tags":["der","app"],"brief":"内能只与温度有关，C_V=iR/2。",
 "body": wrap(
   der(p("<strong>内能推导：</strong>理想气体分子间无相互作用，内能等于所有分子动能之和。$1\\,\\text{mol}$ 气体有 $N_A$ 个分子，每个分子平均能量 $\\frac{i}{2}kT$：")+
   fml("U_m = N_A\\cdot\\frac{i}{2}kT = \\frac{i}{2}RT")+
   p("对 $n$ 摩尔气体 $U=\\frac{i}{2}nRT$，可见内能只依赖于温度。对温度求导得定容摩尔热容：")+
   fml("C_{V,m} = \\left(\\frac{\\partial U_m}{\\partial T}\\right)_V = \\frac{i}{2}R")+
   p("再由迈耶公式 $C_{p,m}=C_{V,m}+R=\\frac{i+2}{2}R$，得比热比 $\\gamma=(i+2)/i$。"))+
   exa(p("<strong>例：</strong>单原子气体 $i=3$，$C_{V,m}=\\frac{3}{2}R\\approx12.5\\,\\text{J/(mol·K)}$，$\\gamma=5/3\\approx1.67$；刚性双原子气体 $i=5$，$C_{V,m}=\\frac{5}{2}R\\approx20.8$，$\\gamma=1.4$，均与常温实验值吻合。"))+
   note(p("低温下双原子气体转动被冻结、$C_V$ 下降，高温下振动被激发、$C_V$ 上升，需用量子理论解释，这是经典能量均分定理的局限。"))
 )},
]},
{
"name": "2.3 麦克斯韦速率分布律",
"color": "#fb923c",
"desc": "速率分布函数、麦克斯韦分布与三种统计速率",
"items": [
{"id":"t2s3-1","name":"速率分布函数","tags":["def","der"],"brief":"描述分子速率分布的概率密度。",
 "body": wrap(
   defn("速率分布函数",p("设总分子数为 $N$，速率在 $v\\sim v+dv$ 区间的分子数为 $dN$，定义<strong>速率分布函数</strong>：")+
   fml("f(v) = \\frac{dN}{N\\,dv}")+
   p("$f(v)$ 是概率密度，$f(v)dv$ 表示分子速率落在该区间的概率，且满足归一化条件。"))+
   der(p("<strong>归一化与统计平均：</strong>所有分子速率必落在 $0\\sim\\infty$ 之间，故：")+
   fml("\\int_0^{\\infty}f(v)\\,dv = 1")+
   p("任意速率函数 $F(v)$ 的统计平均值由分布函数加权平均给出：")+
   fml("\\overline{F(v)} = \\int_0^{\\infty}F(v)f(v)\\,dv")+
   p("取 $F=v$ 得平均速率，取 $F=v^2$ 得方均根速率，取 $F=\\frac{1}{2}mv^2$ 得平均动能。"))+
   note(p("速率分布函数用确定性函数描述大量分子的随机运动规律，体现统计规律性；分布本身随温度改变而改变。"))
 )},
{"id":"t2s3-2","name":"麦克斯韦速率分布律","tags":["thm","der"],"brief":"平衡态下分子速率的分布函数。",
 "fig":"maxwelldist","figCap":"麦克斯韦速率分布曲线，峰值对应最概然速率",
 "body": wrap(
   thm("麦克斯韦速率分布律",p("平衡态下理想气体分子的速率分布函数为：")+
   fml("f(v) = 4\\pi\\left(\\frac{m}{2\\pi kT}\\right)^{3/2}v^2\\,e^{-\\frac{mv^2}{2kT}}")+
   p("曲线从原点上升，在 $v_p$ 处达极大，随后按指数衰减。"))+
   der(p("<strong>由玻尔兹曼因子导出：</strong>分子平动动能 $\\varepsilon=\\frac{1}{2}mv^2$，该能量的相对概率由玻尔兹曼因子 $e^{-\\varepsilon/kT}$ 给出；速度空间中等速率球壳 $4\\pi v^2dv$ 内的状态数正比于 $v^2$，故：")+
   fml("f(v)\\,dv \\propto v^2 e^{-\\frac{mv^2}{2kT}}\\,dv")+
   p("由归一化 $\\int_0^\\infty f(v)dv=1$ 确定系数，利用 $\\int_0^\\infty v^2e^{-av^2}dv=\\frac{\\sqrt{\\pi}}{4a^{3/2}}$（$a=m/2kT$）：")+
   fml("f(v) = 4\\pi\\left(\\frac{m}{2\\pi kT}\\right)^{3/2}v^2\\,e^{-\\frac{mv^2}{2kT}}")+
   p("此即麦克斯韦速率分布律，它只依赖 $m$ 与 $T$，与气体的化学性质无关。"))+
   app(p("<strong>应用：</strong>用于计算分子束强度、化学反应速率与蒸发率；气体扩散法分离铀同位素正是利用不同质量分子速率分布的差异。"))
 )},
{"id":"t2s3-3","name":"三种统计速率","tags":["der","exa"],"brief":"最概然、平均与方均根速率。",
 "fig":"maxwelltemp","figCap":"不同温度下的速率分布：温度升高曲线展宽、峰值右移",
 "body": wrap(
   der(p("<strong>最概然速率：</strong>令 $df/dv=0$，由 $f(v)=Cv^2e^{-mv^2/2kT}$ 得：")+
   fml("\\frac{d}{dv}\\left(v^2e^{-\\frac{mv^2}{2kT}}\\right)=0 \\implies 2v-\\frac{mv^3}{kT}=0 \\implies v_p=\\sqrt{\\frac{2kT}{m}}=\\sqrt{\\frac{2RT}{M}}")+
   p("<strong>平均速率：</strong>代入 $F(v)=v$ 积分，用 $\\int_0^\\infty v^3e^{-av^2}dv=\\frac{1}{2a^2}$：")+
   fml("\\bar{v} = \\int_0^\\infty vf(v)\\,dv = \\sqrt{\\frac{8kT}{\\pi m}} = \\sqrt{\\frac{8RT}{\\pi M}}")+
   p("<strong>方均根速率：</strong>由动能关系 $\\frac{1}{2}m\\overline{v^2}=\\frac{3}{2}kT$ 直接得：")+
   fml("v_{rms} = \\sqrt{\\frac{3kT}{m}} = \\sqrt{\\frac{3RT}{M}}")+
   p("三者之比为 $v_p:\\bar{v}:v_{rms}=1:1.128:1.225$，均与 $\\sqrt{T}$ 成正比、与 $\\sqrt{M}$ 成反比。"))+
   exa(p("<strong>例：</strong>氮气 $M=0.028\\,\\text{kg/mol}$、$T=300\\,\\text{K}$ 时 $v_p=\\sqrt{2\\times8.314\\times300/0.028}\\approx422\\,\\text{m/s}$，$\\bar{v}\\approx476\\,\\text{m/s}$，$v_{rms}\\approx517\\,\\text{m/s}$。"))
 )},
]},
{
"name": "2.4 玻尔兹曼分布律",
"color": "#c2410c",
"desc": "玻尔兹曼分布、重力场气压公式与其应用",
"items": [
{"id":"t2s4-1","name":"玻尔兹曼分布律","tags":["thm","der"],"brief":"外场中粒子按势能的指数分布。",
 "fig":"boltzmann","figCap":"外场中粒子数密度按势能指数衰减的玻尔兹曼分布",
 "body": wrap(
   thm("玻尔兹曼分布律",p("在平衡态下，处于能量为 $\\varepsilon_i$ 状态上的粒子数满足：")+
   fml("n_i = C\\,g_i\\,e^{-\\frac{\\varepsilon_i}{kT}}")+
   p("其中 $g_i$ 为简并度，$C$ 为归一化常数；粒子优先占据低能态，能级越高占据数越少。"))+
   der(p("<strong>由平衡条件导出：</strong>考虑势能 $\\varepsilon_p=mgh$ 的粒子，两高度处粒子数密度之比为：")+
   fml("\\frac{n_2}{n_1} = e^{-\\frac{mgh}{kT}} = e^{-\\frac{\\varepsilon_{p2}-\\varepsilon_{p1}}{kT}}")+
   p("推广到任意能量差 $\\Delta\\varepsilon=\\varepsilon_2-\\varepsilon_1$：")+
   fml("\\frac{n_2}{n_1} = e^{-\\Delta\\varepsilon/kT} \\implies n(\\varepsilon)\\propto e^{-\\varepsilon/kT}")+
   p("这正是玻尔兹曼因子，其物理意义是：能量越高的状态粒子越少，温度越高则高低能态的粒子数比越接近 1。"))+
   app(p("<strong>应用：</strong>玻尔兹曼分布用于解释大气密度随高度衰减、恒星光谱中谱线强度比、半导体载流子分布以及化学平衡常数，是统计物理的基石。"))
 )},
{"id":"t2s4-2","name":"重力场中气压随高度的分布","tags":["der","app"],"brief":"等温大气模型下压强指数衰减。",
 "body": wrap(
   der(p("<strong>推导：</strong>在等温大气模型中，距地面 $h$ 处厚度 $dh$ 的气层所受重力与压强差平衡：")+
   fml("dp = -\\rho g\\,dh")+
   p("由理想气体方程 $\\rho=pM/(RT)$，代入得：")+
   fml("\\frac{dp}{p} = -\\frac{Mg}{RT}dh")+
   p("由 $p(0)=p_0$ 积分：")+
   fml("\\ln\\frac{p}{p_0} = -\\frac{Mgh}{RT} \\implies p = p_0\\,e^{-\\frac{Mgh}{RT}}")+
   p("此即等温气压公式；由于 $\\rho\\propto p$，分子数密度 $n=n_0e^{-mgh/kT}$ 与之等价。"))+
   exa(p("<strong>例：</strong>取 $T=273\\,\\text{K}$、$M=0.029\\,\\text{kg/mol}$，得标高 $H=RT/(Mg)\\approx8.0\\,\\text{km}$，即每升高约 8 km 气压降为原来的 $1/e$；实际大气温度随高度变化，需用标准大气模型修正。"))+
   note(p("气压公式也用于高度计原理：测量压强即可估算海拔，但需按气温与气象条件标定。"))
 )},
{"id":"t2s4-3","name":"玻尔兹曼分布的应用与推广","tags":["der","app"],"brief":"均分、反应速率常数中的玻尔兹曼因子。",
 "body": wrap(
   der(p("<strong>由玻尔兹曼分布求平均能量：</strong>设一维系统粒子势能为 $U(x)$，概率密度正比于 $e^{-U(x)/kT}$，平均势能为：")+
   fml("\\bar{\\varepsilon} = \\frac{\\int U(x)e^{-U(x)/kT}dx}{\\int e^{-U(x)/kT}dx}")+
   p("对简谐势 $U=\\frac{1}{2}\\kappa x^2$，用高斯积分 $\\int x^2e^{-ax^2}dx=\\frac{1}{2}\\sqrt{\\pi/a^3}$ 得：")+
   fml("\\bar{\\varepsilon} = \\frac{1}{2}kT")+
   p("与能量均分定理一致，说明玻尔兹曼分布自动包含了均分结果。"))+
   der(p("<strong>反应速率中的玻尔兹曼因子：</strong>化学反应中能克服活化能 $E_a$ 的分子比例由玻尔兹曼因子给出，故速率常数为：")+
   fml("k_{rate} = A\\,e^{-E_a/(RT)}")+
   p("这正是阿伦尼乌斯公式的来源，温度升高使活化分子数指数增长，反应速率加快。"))+
   app(p("<strong>应用：</strong>玻尔兹曼因子还决定热电子发射电流（理查森公式）、半导体本征载流子浓度以及恒星核聚变反应率，是联系微观能级与宏观速率的普适因子。"))
 )},
]},
{
"name": "2.5 平均自由程与分子碰撞",
"color": "#f59e0b",
"desc": "碰撞截面、平均自由程与碰撞频率",
"items": [
{"id":"t2s5-1","name":"分子碰撞与有效直径","tags":["def","der"],"brief":"刚性球模型与碰撞截面。",
 "fig":"collisioncylinder","figCap":"碰撞圆柱：截面 πd²，长度 v̄Δt",
 "body": wrap(
   defn("有效直径与碰撞截面",p("把分子近似为刚性球，两分子中心间最近距离的统计平均值称为<strong>有效直径</strong> $d$，对应的碰撞截面为 $\\sigma=\\pi d^2$。当两分子中心距离小于 $d$ 时即发生碰撞。"))+
   der(p("<strong>碰撞数的计算：</strong>分子以平均速率 $\\bar{v}$ 运动，在时间 $dt$ 内扫过的碰撞圆柱体积为 $\\pi d^2\\bar{v}\\,dt$，其中与它碰撞的分子数为：")+
   fml("dZ' = n\\,\\pi d^2\\bar{v}\\,dt")+
   p("但全体分子都在运动，需用相对速率代替，由麦克斯韦分布求得相对速率平均 $\\bar{v}_{rel}=\\sqrt{2}\\,\\bar{v}$，故修正为：")+
   fml("\\bar{Z} = \\sqrt{2}\\,\\pi d^2 n\\bar{v}")+
   p("式中因子 $\\sqrt{2}$ 正是考虑相对运动后的结果。"))+
   note(p("<strong>例：</strong>常温常压空气 $d\\approx3.5\\times10^{-10}\\,\\text{m}$、$n\\approx2.7\\times10^{25}\\,\\text{m}^{-3}$，得 $\\bar{Z}\\approx6.5\\times10^{9}\\,\\text{s}^{-1}$，即每秒碰撞约六十五亿次。"))
 )},
{"id":"t2s5-2","name":"平均自由程","tags":["thm","der"],"brief":"两次碰撞间平均走过的距离。",
 "fig":"meanfreepath","figCap":"分子沿折线运动，相邻碰撞间的平均路程为 λ",
 "body": wrap(
   thm("平均自由程",p("分子在连续两次碰撞之间平均走过的路程称为平均自由程：")+
   fml("\\bar{\\lambda} = \\frac{\\bar{v}}{\\bar{Z}} = \\frac{1}{\\sqrt{2}\\,\\pi d^2 n} = \\frac{kT}{\\sqrt{2}\\,\\pi d^2 p}"))+
   der(p("<strong>推导：</strong>由定义 $\\bar{\\lambda}=\\bar{v}/\\bar{Z}$，代入碰撞频率 $\\bar{Z}=\\sqrt{2}\\pi d^2 n\\bar{v}$：")+
   fml("\\bar{\\lambda} = \\frac{\\bar{v}}{\\sqrt{2}\\,\\pi d^2 n\\bar{v}} = \\frac{1}{\\sqrt{2}\\,\\pi d^2 n}")+
   p("再用 $n=p/kT$ 化为压强与温度的形式：")+
   fml("\\bar{\\lambda} = \\frac{kT}{\\sqrt{2}\\,\\pi d^2 p}")+
   p("可见 $\\bar{\\lambda}$ 与分子平均速率无关；压强一定时正比于 $T$，温度一定时反比于 $p$。"))+
   exa(p("<strong>例：</strong>常温常压空气 $\\bar{\\lambda}\\approx6.8\\times10^{-8}\\,\\text{m}$，约为分子直径的 200 倍；当压强降到 $10^{-4}\\,\\text{Pa}$ 时 $\\bar{\\lambda}$ 达米级，进入高真空区。"))+
   app(p("<strong>应用：</strong>平均自由程决定真空度划分、气体输运性质以及电子器件与真空系统的尺寸设计。"))
 )},
{"id":"t2s5-3","name":"碰撞频率与总碰撞数","tags":["der","app"],"brief":"分子碰撞频率及其与输运的联系。",
 "body": wrap(
   der(p("<strong>单位体积的碰撞总数：</strong>每个分子平均每秒碰撞 $\\bar{Z}$ 次，但每次碰撞涉及两个分子，故单位体积单位时间的碰撞次数为：")+
   fml("Z_{tot} = \\frac{1}{2}n\\bar{Z} = \\frac{1}{2}\\sqrt{2}\\,\\pi d^2 n^2\\bar{v}")+
   p("因子 $1/2$ 用于避免每对分子被重复计数。代入 $\\bar{v}=\\sqrt{8kT/\\pi m}$：")+
   fml("Z_{tot} = \\sqrt{2}\\,\\pi d^2 n^2\\sqrt{\\frac{kT}{\\pi m}}")+
   p("可见碰撞总数正比于 $n^2$ 与 $\\sqrt{T}$。"))+
   der(p("<strong>碰撞与输运的联系：</strong>分子在自由程 $\\bar{\\lambda}$ 内携带其出发处的动量、能量与质量，碰撞后被就地平均。设某物理量的梯度为 $d\\Phi/dz$，越过单位面积的净输运量为：")+
   fml("\\Delta\\Phi = -\\frac{1}{3}\\bar{v}\\bar{\\lambda}\\frac{d\\Phi}{dz}")+
   p("这一表达式正是下一章黏滞、热传导与扩散三个输运定律的共同来源。"))+
   note(p("温度升高时碰撞更频繁，但因 $\\bar{\\lambda}$ 也随 $T$ 增大，输运系数对温度的依赖并非简单单调，需具体分析。"))
 )},
]},
{
"name": "2.6 麦克斯韦-玻尔兹曼统计",
"color": "#ea580c",
"desc": "等概率假设、麦克斯韦-玻尔兹曼分布与配分函数",
"items": [
{"id":"t2s6-1","name":"等概率假设与微观状态","tags":["def","der"],"brief":"统计物理的基本假设。",
 "body": wrap(
   defn("等概率假设",p("对于处于平衡态的孤立系统，系统处于各可能微观状态的<strong>概率相等</strong>。这是统计物理的基本假设，其正确性由推论与实验相符来验证。"))+
   der(p("<strong>由等概率假设求平均：</strong>设系统可能微观状态总数为 $W$，则每个微观状态出现的概率为 $p_i=1/W$，任一宏观量 $M$ 的统计平均为：")+
   fml("\\bar{M} = \\sum_{i=1}^{W} p_i M_i = \\frac{1}{W}\\sum_{i=1}^{W}M_i")+
   p("宏观平衡态对应于 $W$ 取极大的状态。对由 $N$ 个分子、体积 $V$ 组成的系统，微观状态数写为：")+
   fml("W = W(E,V,N)")+
   p("它与熵通过玻尔兹曼关系 $S=k\\ln W$ 相联系，这正是统计与热力学的桥梁。"))+
   note(p("等概率假设只适用于孤立系统的平衡态；对与热库接触的系统，需改用正则分布的玻尔兹曼因子。"))
 )},
{"id":"t2s6-2","name":"麦克斯韦-玻尔兹曼分布律","tags":["thm","der"],"brief":"经典粒子的平衡分布律。",
 "body": wrap(
   thm("麦克斯韦-玻尔兹曼分布",p("对于可分辨的经典近独立粒子，处于能量为 $\\varepsilon_i$（简并度 $g_i$）的粒子数为：")+
   fml("n_i = \\frac{N}{Z}g_i\\,e^{-\\frac{\\varepsilon_i}{kT}},\\qquad Z=\\sum_i g_i e^{-\\frac{\\varepsilon_i}{kT}}")+
   p("$Z$ 为单粒子配分函数，该分布是麦克斯韦速度分布与玻尔兹曼能量分布的统称。"))+
   der(p("<strong>由最概然分布导出：</strong>在粒子数守恒 $\\sum n_i=N$ 与能量守恒 $\\sum n_i\\varepsilon_i=E$ 约束下，使微观状态数 $W=\\prod_i g_i^{n_i}/n_i!$ 取极大。用斯特林公式 $\\ln n!\\approx n\\ln n-n$ 并作拉格朗日乘子变分：")+
   fml("\\delta\\left[\\ln W-\\alpha\\sum_i n_i-\\beta\\sum_i n_i\\varepsilon_i\\right]=0")+
   p("得 $\\ln(n_i/g_i)+\\alpha+\\beta\\varepsilon_i=0$，即 $n_i=g_ie^{-\\alpha}e^{-\\beta\\varepsilon_i}$。与热力学比较定出 $\\beta=1/kT$，于是：")+
   fml("n_i=\\frac{N}{Z}g_ie^{-\\varepsilon_i/kT}"))+
   app(p("<strong>应用：</strong>M-B 分布适用于气体、稀薄等离子体等经典体系；对电子等费米子需改用费米-狄拉克分布，光子与玻色子需改用玻色-爱因斯坦分布，二者在高温低密度时都退化为 M-B 分布。"))
 )},
{"id":"t2s6-3","name":"配分函数与热力学量","tags":["der","app"],"brief":"配分函数是统计与热力学的桥梁。",
 "body": wrap(
   der(p("<strong>配分函数与内能：</strong>单粒子配分函数 $Z=\\sum_i g_ie^{-\\varepsilon_i/kT}$，其对数对 $\\beta=1/kT$ 的导数给出平均能量：")+
   fml("\\bar{\\varepsilon} = -\\frac{\\partial\\ln Z}{\\partial\\beta}")+
   p("对 $N$ 个近独立粒子，内能为 $U=-N\\partial\\ln Z/\\partial\\beta$；代入理想气体平动配分函数 $Z_{tr}=V(2\\pi mkT/h^2)^{3/2}$ 得：")+
   fml("U = \\frac{3}{2}NkT")+
   p("与能量均分结果一致，验证了配分函数方法的正确性。"))+
   der(p("<strong>配分函数与熵：</strong>由亥姆霍兹自由能 $F=-kT\\ln Z$ 及 $S=-\\partial F/\\partial T$ 得：")+
   fml("S = k\\ln Z + kT\\frac{\\partial\\ln Z}{\\partial T}")+
   p("对 $N$ 粒子体系（含不可分辨因子 $1/N!$）得萨克-特特罗德方程，可算出理想气体的绝对熵，与热力学熵定义一致。"))+
   app(p("<strong>应用：</strong>配分函数用于计算比热、化学平衡常数、电离平衡（萨哈方程）与热辐射，是连接微观能级结构与宏观热力学量的通用工具。"))
 )},
]},
]
ch3_sections = [
{
"name": "3.1 黏滞现象",
"color": "#d97706",
"desc": "牛顿黏滞定律、黏滞系数的微观表达与实验规律",
"items": [
{"id":"t3s1-1","name":"牛顿黏滞定律","tags":["thm","der"],"brief":"流层间的内摩擦力与速度梯度成正比。",
 "fig":"viscosity","figCap":"速度梯度 du/dz 使相邻流层间产生内摩擦力",
 "body": wrap(
   thm("牛顿黏滞定律",p("当气体各流层速度不同时，相邻流层间存在沿切向的内摩擦力，其大小与速度梯度及接触面积成正比：")+
   fml("f = \\eta A\\frac{du}{dz}")+
   p("$\\eta$ 为黏滞系数（动力黏度），单位为 $\\text{Pa·s}$。"))+
   der(p("<strong>由动量输运理解：</strong>分子在自由程内携带自身动量 $mu$ 穿越流层。沿 $+z$ 与 $-z$ 方向运动的分子各占 $1/6$，跨越单位面积单位时间的净动量输运为：")+
   fml("f = \\frac{1}{6}n\\bar{v}\\,m\\,u(z-\\bar{\\lambda}) - \\frac{1}{6}n\\bar{v}\\,m\\,u(z+\\bar{\\lambda})")+
   p("把 $u(z\\pm\\bar{\\lambda})$ 作泰勒展开：")+
   fml("u(z\\mp\\bar{\\lambda})\\approx u(z)\\mp\\bar{\\lambda}\\frac{du}{dz}")+
   p("代入相减得：")+
   fml("f = -\\frac{1}{3}nm\\bar{v}\\bar{\\lambda}\\frac{du}{dz} = -\\frac{1}{3}\\rho\\bar{v}\\bar{\\lambda}\\frac{du}{dz}")+
   p("取大小即得 $f=\\eta A\\,du/dz$，其中 $\\eta=\\frac{1}{3}\\rho\\bar{v}\\bar{\\lambda}$。"))+
   note(p("黏滞现象输运的是动量：高速层分子把动量带给低速层，低速层分子把动量带给高速层，宏观上表现为内摩擦。"))
 )},
{"id":"t3s1-2","name":"黏滞系数的微观表达","tags":["der","exa"],"brief":"η 与压强无关，正比于 √T。",
 "body": wrap(
   der(p("<strong>推导与化简：</strong>由 $\\eta=\\frac{1}{3}\\rho\\bar{v}\\bar{\\lambda}$，代入 $\\rho=nm$、$\\bar{v}=\\sqrt{8kT/\\pi m}$、$\\bar{\\lambda}=1/(\\sqrt{2}\\pi d^2 n)$：")+
   fml("\\eta = \\frac{1}{3}nm\\sqrt{\\frac{8kT}{\\pi m}}\\cdot\\frac{1}{\\sqrt{2}\\pi d^2 n}")+
   p("分子数密度 $n$ 相消，得：")+
   fml("\\eta = \\frac{2}{3\\pi^{3/2}}\\cdot\\frac{\\sqrt{mkT}}{d^2}")+
   p("可见黏滞系数与分子数密度（即压强）无关，只与温度、分子质量与有效直径有关，且 $\\eta\\propto\\sqrt{T}$。"))+
   exa(p("<strong>例：</strong>麦克斯韦曾由此预言气体黏滞系数与压强无关，这与液体黏度随温度升高而减小的行为相反；实验证实气体 $\\eta$ 在相当宽压强范围内保持不变，仅在极低压时随 $p$ 减小，成为分子动理论的有力证据。"))+
   note(p("由于有效直径 $d$ 随温度微弱变化，实际 $\\eta$ 对温度的依赖略强于 $\\sqrt{T}$，常用萨瑟兰公式修正。"))
 )},
{"id":"t3s1-3","name":"黏滞现象的实验规律","tags":["der","app"],"brief":"旋转黏度计中黏滞力矩的计算。",
 "body": wrap(
   der(p("<strong>圆柱形气体黏滞实验：</strong>两同轴圆筒半径 $R_1<R_2$，长度 $L$，内筒静止、外筒以角速度 $\\omega$ 转动。气体速度沿径向近似线性变化，速度梯度约为：")+
   fml("\\frac{du}{dz}\\approx\\frac{\\omega R_2}{R_2-R_1}")+
   p("作用在内筒上的黏滞力矩为：")+
   fml("M = \\eta\\,(2\\pi R_1 L)\\,\\frac{\\omega R_2}{R_2-R_1}\\cdot R_1")+
   p("测量使内筒保持静止所需的平衡力矩即可求出 $\\eta$，这是旋转黏度计的原理。"))+
   exa(p("<strong>例：</strong>设 $R_1=5.0\\,\\text{cm}$、$R_2=5.2\\,\\text{cm}$、$L=20\\,\\text{cm}$、$\\omega=2\\pi\\,\\text{rad/s}$，取 $\\eta=1.8\\times10^{-5}\\,\\text{Pa·s}$，代入得所需平衡力矩约 $3.4\\times10^{-6}\\,\\text{N·m}$，量级与实验相符。"))+
   app(p("<strong>应用：</strong>黏滞系数测量用于气体纯度分析与温度标定；气体黏滞阻尼影响真空系统中转子与悬臂的运动，也用于气体轴承与黏滞真空计的设计。"))
 )},
]},
{
"name": "3.2 热传导",
"color": "#b45309",
"desc": "傅里叶定律与热导率的微观表达",
"items": [
{"id":"t3s2-1","name":"傅里叶热传导定律","tags":["thm","der"],"brief":"热流密度与温度阶梯成正比。",
 "fig":"conduction","figCap":"温度梯度 dT/dx 引起热量由高温向低温输运",
 "body": wrap(
   thm("傅里叶定律",p("气体中热量由高温区向低温区输运，单位时间通过面积 $A$ 的热量为：")+
   fml("\\frac{dQ}{dt} = -\\kappa A\\frac{dT}{dx}")+
   p("$\\kappa$ 为热导率，单位为 $\\text{W/(m·K)}$，负号表示热流方向与温度梯度方向相反。"))+
   der(p("<strong>由能量输运理解：</strong>分子在自由程内携带平均动能 $\\frac{i}{2}kT$，记单分子热容 $c_V=\\frac{i}{2}k$。沿 $\\pm x$ 方向运动的分子各占 $1/6$，跨越单位面积单位时间输运的净能量（热流密度）为：")+
   fml("q = \\frac{1}{6}n\\bar{v}c_V T(x-\\bar{\\lambda}) - \\frac{1}{6}n\\bar{v}c_V T(x+\\bar{\\lambda})")+
   p("把 $T(x\\mp\\bar{\\lambda})$ 泰勒展开：")+
   fml("T(x\\mp\\bar{\\lambda})\\approx T(x)\\mp\\bar{\\lambda}\\frac{dT}{dx}")+
   p("代入相减得 $q=-\\frac{1}{3}n\\bar{v}\\bar{\\lambda}c_V\\,dT/dx$，乘面积 $A$ 即得 $dQ/dt=-\\kappa A\\,dT/dx$，其中 $\\kappa=\\frac{1}{3}n\\bar{v}\\bar{\\lambda}c_V=\\frac{1}{3}\\rho c_V\\bar{v}\\bar{\\lambda}$。"))+
   app(p("<strong>应用：</strong>热传导系数用于保温材料、真空绝热（杜瓦瓶）与气体导热分析；气体导热率低是双层玻璃与真空夹层保温的原理。"))
 )},
{"id":"t3s2-2","name":"热导率的微观表达","tags":["der","exa"],"brief":"κ 与压强无关，随 √T 缓慢增大。",
 "body": wrap(
   der(p("<strong>化简：</strong>由 $\\kappa=\\frac{1}{3}\\rho c_V\\bar{v}\\bar{\\lambda}$，对理想气体有 $\\rho c_V=\\frac{i}{2}nk$。代入 $\\bar{v}=\\sqrt{8kT/\\pi m}$ 与 $\\bar{\\lambda}=1/(\\sqrt{2}\\pi d^2 n)$：")+
   fml("\\kappa = \\frac{1}{3}\\cdot\\frac{i}{2}nk\\cdot\\sqrt{\\frac{8kT}{\\pi m}}\\cdot\\frac{1}{\\sqrt{2}\\pi d^2 n}")+
   p("$n$ 相消，得：")+
   fml("\\kappa = \\frac{i}{3\\pi^{3/2}}\\cdot\\frac{k}{d^2}\\sqrt{\\frac{kT}{m}}")+
   p("与黏滞系数类似，热导率与压强无关，仅随 $\\sqrt{T}$ 缓慢增大。"))+
   exa(p("<strong>例：</strong>氩气 $i=3$、常温下由上式估得 $\\kappa\\approx1.7\\times10^{-2}\\,\\text{W/(m·K)}$，与实验值约 $1.8\\times10^{-2}$ 同量级；轻气体（氦、氢）$\\kappa$ 较大，因为 $\\sqrt{1/m}$ 因子使轻分子输运能量更有效。"))+
   note(p("气体低压时 $\\bar{\\lambda}$ 增大到与容器尺寸相当时，$\\kappa$ 将随压强下降，这一背离经典结果的现象正是真空绝热保温的基础。"))
 )},
]},
{
"name": "3.3 扩散",
"color": "#f59e0b",
"desc": "斐克定律、扩散系数与自扩散互扩散",
"items": [
{"id":"t3s3-1","name":"斐克扩散定律","tags":["thm","der"],"brief":"扩散流密度与浓度梯度成正比。",
 "fig":"diffusion","figCap":"浓度梯度 dn/dx 引起分子由高浓度向低浓度定向迁移",
 "body": wrap(
   thm("斐克定律",p("当气体密度（浓度）不均匀时，分子由高浓度区向低浓度区净迁移，单位时间通过单位面积的分子数为：")+
   fml("J = -D\\frac{dn}{dx}")+
   p("$D$ 为扩散系数，单位为 $\\text{m}^2/\\text{s}$。"))+
   der(p("<strong>由质量输运理解：</strong>分子跨越分界面时携带出发处的分子数密度 $n(x\\mp\\bar{\\lambda})$。沿 $\\pm x$ 方向运动的分子各占 $1/6$，净分子流密度为：")+
   fml("J = \\frac{1}{6}\\bar{v}\\,n(x-\\bar{\\lambda}) - \\frac{1}{6}\\bar{v}\\,n(x+\\bar{\\lambda})")+
   p("把 $n(x\\mp\\bar{\\lambda})$ 泰勒展开：")+
   fml("n(x\\mp\\bar{\\lambda})\\approx n(x)\\mp\\bar{\\lambda}\\frac{dn}{dx}")+
   p("代入相减得：")+
   fml("J = -\\frac{1}{3}\\bar{v}\\bar{\\lambda}\\frac{dn}{dx}")+
   p("故 $D=\\frac{1}{3}\\bar{v}\\bar{\\lambda}$。"))+
   app(p("<strong>应用：</strong>扩散用于气体混合、表面渗碳与半导体掺杂；同位素分离中的气体扩散法正是利用不同质量分子扩散系数不同。"))
 )},
{"id":"t3s3-2","name":"扩散系数的微观表达","tags":["der","exa"],"brief":"D 正比于 T^(3/2)，反比于 p。",
 "body": wrap(
   der(p("<strong>化简：</strong>由 $D=\\frac{1}{3}\\bar{v}\\bar{\\lambda}$，代入 $\\bar{v}=\\sqrt{8kT/\\pi m}$ 与 $\\bar{\\lambda}=kT/(\\sqrt{2}\\pi d^2 p)$：")+
   fml("D = \\frac{1}{3}\\sqrt{\\frac{8kT}{\\pi m}}\\cdot\\frac{kT}{\\sqrt{2}\\pi d^2 p}")+
   p("整理得：")+
   fml("D = \\frac{2}{3\\pi^{3/2}}\\cdot\\frac{(kT)^{3/2}}{d^2 p\\sqrt{m}} \\propto \\frac{T^{3/2}}{p}")+
   p("与 $\\eta$、$\\kappa$ 不同，扩散系数与压强成反比，因为压强升高使分子数密度增大、自由程减小，分子迁移受阻。"))+
   exa(p("<strong>例：</strong>标准状况下氧氮混合的 $D\\approx2\\times10^{-5}\\,\\text{m}^2/\\text{s}$；压强降为原来的 $1/10$ 时 $D$ 增大 10 倍，扩散显著加快，这正是低压化学气相沉积利用的效应。"))+
   note(p("扩散与随机行走等价：$\\overline{x^2}=2Dt$，说明分子迁移距离正比于 $\\sqrt{t}$ 而非 $t$，体现了扩散的随机本性。"))
 )},
{"id":"t3s3-3","name":"自扩散与互扩散","tags":["def","der"],"brief":"同类与异类分子混合的两种扩散。",
 "body": wrap(
   defn("自扩散与互扩散",p("同种分子用示踪原子标记后观察其混合过程称为<strong>自扩散</strong>；两种不同气体相互渗入称为<strong>互扩散</strong>。两者的输运机理相同，均可用斐克定律描述。"))+
   der(p("<strong>自扩散系数：</strong>对自扩散，标记分子与背景分子相同，$\\bar{v}$ 与 $\\bar{\\lambda}$ 均由同种分子决定，故：")+
   fml("D_{self} = \\frac{1}{3}\\bar{v}\\bar{\\lambda}")+
   p("对互扩散，两种分子质量与直径不同，按下式用混合平均量计算：")+
   fml("D_{12} = \\frac{1}{3}\\frac{n_1\\bar{v}_1\\bar{\\lambda}_1+n_2\\bar{v}_2\\bar{\\lambda}_2}{n_1+n_2}")+
   p("当两种分子性质相近时 $D_{12}\\approx D_{self}$；差别大时互扩散系数由较慢的一方主导。"))+
   app(p("<strong>应用：</strong>自扩散系数可由核磁共振、准弹性中子散射测量；互扩散用于研究气体分离、燃烧与大气污染物扩散，是化工传质过程设计的核心参数。"))
 )},
]},
{
"name": "3.4 输运系数的微观推导",
"color": "#92400e",
"desc": "输运过程一般公式、三系数关系与温度压强依赖",
"items": [
{"id":"t3s4-1","name":"输运过程的一般公式","tags":["der"],"brief":"三类输运现象的统一定量描述。",
 "fig":"transportcoef","figCap":"黏滞、热传导与扩散系数均由 v̄ 与 λ 组合而成",
 "body": wrap(
   der(p("<strong>统一推导：</strong>设某物理量的单位体积值为 $\\Phi_0$，沿 $z$ 方向有梯度 $d\\Phi_0/dz$。分子沿 $\\pm z$ 方向运动各占 $1/6$，跨越面积 $A$、时间 $\\Delta t$ 的净输运量为：")+
   fml("\\Delta\\Phi = \\frac{1}{6}n\\bar{v}A\\Delta t\\,\\Phi_0(z-\\bar{\\lambda}) - \\frac{1}{6}n\\bar{v}A\\Delta t\\,\\Phi_0(z+\\bar{\\lambda})")+
   p("泰勒展开 $\\Phi_0(z\\mp\\bar{\\lambda})\\approx\\Phi_0(z)\\mp\\bar{\\lambda}\\,d\\Phi_0/dz$，代入相减：")+
   fml("\\Delta\\Phi = -\\frac{1}{3}n\\bar{v}\\bar{\\lambda}A\\Delta t\\frac{d\\Phi_0}{dz}")+
   p("对具体物理量取相应的 $\\Phi_0$（动量、能量、质量），即分别得到黏滞、热传导与扩散三个定律。"))+
   note(p("此式成立的量级条件是平均自由程远小于物理量发生显著变化的尺度，即 $\\bar{\\lambda}\\ll L$；否则需改用玻尔兹曼方程求解。"))
 )},
{"id":"t3s4-2","name":"三个输运系数之间的关系","tags":["der","exa"],"brief":"η、κ、D 的相互联系。",
 "body": wrap(
   der(p("<strong>由统一定义比较：</strong>三个系数分别为：")+
   fml("\\eta=\\frac{1}{3}\\rho\\bar{v}\\bar{\\lambda},\\quad \\kappa=\\frac{1}{3}\\rho c_V\\bar{v}\\bar{\\lambda},\\quad D=\\frac{1}{3}\\bar{v}\\bar{\\lambda}")+
   p("两两相除消去公共因子 $\\frac{1}{3}\\bar{v}\\bar{\\lambda}$，得：")+
   fml("\\kappa = \\eta\\,c_V,\\qquad D = \\frac{\\eta}{\\rho},\\qquad \\frac{\\kappa}{D} = \\rho c_V")+
   p("由此可得 $\\kappa = \\rho c_V D$，三系数之比只由气体本身性质决定。"))+
   exa(p("<strong>例：</strong>对单原子气体 $c_V=\\frac{3}{2}\\frac{k}{m}$，由上式预测 $\\kappa/(\\eta c_V)=1$。实测值约为 1.5 至 2.5，偏差源于简化模型未考虑分子速度分布与关联，需用更精确的玻尔兹曼方程与高阶近似修正。"))+
   note(p("这一关系揭示了看似不同的三种现象具有共同的微观起源——分子热运动与自由程，是分子动理论统一性的体现。"))
 )},
{"id":"t3s4-3","name":"输运系数对温度与压强的依赖","tags":["der","exa"],"brief":"η、κ 与 p 无关，D 反比于 p。",
 "body": wrap(
   der(p("<strong>汇总微观表达式：</strong>把三个系数整理为：")+
   fml("\\eta\\propto\\frac{\\sqrt{mT}}{d^2},\\qquad \\kappa\\propto\\frac{1}{d^2}\\sqrt{\\frac{T}{m}},\\qquad D\\propto\\frac{T^{3/2}}{p\\sqrt{m}}")+
   p("可见 $\\eta$ 与 $\\kappa$ 都与压强无关（因分子数密度 $n$ 相消），只随 $\\sqrt{T}$ 变化；而 $D$ 与压强成反比。"))+
   der(p("<strong>物理解释：</strong>压强增大时分子数密度增大，一方面单位时间跨越的分子数增多，另一方面每个分子的自由程减小，两者恰好抵消；对扩散而言，自由程减小的影响超过浓度差增大的影响，故 $D$ 随 $p$ 减小。"))+
   exa(p("<strong>例：</strong>温度由 $300\\,\\text{K}$ 升到 $600\\,\\text{K}$，$\\eta$、$\\kappa$ 约增大到 $\\sqrt{2}\\approx1.41$ 倍；压强由 $10^5$ 降到 $10^3\\,\\text{Pa}$ 时 $D$ 增大约 100 倍，而 $\\eta$ 基本不变。"))+
   app(p("<strong>应用：</strong>这一差异在真空系统、气体传感与气体分离中至关重要：用黏滞型真空计测量低压时需注意压强过低导致读数偏离。"))
 )},
]},
{
"name": "3.5 稀薄气体与真空",
"color": "#ca8a04",
"desc": "稀薄气体输运、克努森数与真空技术",
"items": [
{"id":"t3s5-1","name":"稀薄气体中的输运","tags":["def","der"],"brief":"平均自由程与容器尺度相当时的输运。",
 "fig":"vacuum","figCap":"稀薄气体中分子与器壁碰撞为主，输运性质改变",
 "body": wrap(
   defn("稀薄气体",p("当气体压强很低、分子平均自由程 $\\bar{\\lambda}$ 与容器特征尺度 $L$ 相当时，分子主要与器壁碰撞而非彼此碰撞，这种气体称为<strong>稀薄气体</strong>，也即真空状态。"))+
   der(p("<strong>输运系数的改变：</strong>分子与器壁碰撞后携带壁面处的物理量，有效自由程被限制为 $L$ 而非 $\\bar{\\lambda}$，故输运系数变为：")+
   fml("\\eta_{eff}=\\frac{1}{3}\\rho\\bar{v}L,\\qquad \\kappa_{eff}=\\frac{1}{3}\\rho c_V\\bar{v}L")+
   p("由于 $\\rho\\propto p$，此时 $\\eta_{eff}$、$\\kappa_{eff}$ 改为正比于压强 $p$，与常压下的行为相反：")+
   fml("\\eta_{eff}\\propto p,\\qquad \\kappa_{eff}\\propto p")+
   p("据此可判别气体处于常压输运区还是稀薄分子流区。"))+
   app(p("<strong>应用：</strong>杜瓦瓶、真空保温杯正是利用稀薄气体热导率正比于压强、压强越低导热越差的特性实现高效隔热。"))
 )},
{"id":"t3s5-2","name":"克努森数与真空技术","tags":["der","app"],"brief":"用克努森数划分流动与输运区域。",
 "body": wrap(
   der(p("<strong>克努森数的定义：</strong>定义无量纲的克努森数 $Kn$ 为平均自由程与特征尺度之比：")+
   fml("Kn = \\frac{\\bar{\\lambda}}{L} = \\frac{kT}{\\sqrt{2}\\,\\pi d^2 p\\,L}")+
   p("据此划分区域：$Kn<0.01$ 为连续介质（黏滞流）区，输运系数与压强无关；$0.01<Kn<1$ 为过渡区；$Kn>1$ 为分子流（自由分子）区，输运系数正比于压强。"))+
   der(p("<strong>真空度与平均自由程的对应：</strong>取容器尺度 $L=0.1\\,\\text{m}$、$T=300\\,\\text{K}$、$d=3.5\\times10^{-10}\\,\\text{m}$，令 $Kn=1$ 得临界压强：")+
   fml("p^* = \\frac{kT}{\\sqrt{2}\\,\\pi d^2 L}\\approx 0.067\\,\\text{Pa}")+
   p("低于此压强即进入分子流区，可见真空度与容器尺寸共同决定气体处于哪个输运区域。"))+
   app(p("<strong>应用：</strong>真空泵选型、真空镀膜、电子显微镜与加速器真空系统均按 $Kn$ 数设计；低温杜瓦瓶的隔热设计也必须避免残余气体进入连续介质导热带。"))
 )},
{"id":"t3s5-3","name":"真空的获得与测量","tags":["der","app"],"brief":"真空泵抽速与极限压强、真空计原理。",
 "body": wrap(
   der(p("<strong>真空度由抽速与漏气平衡决定：</strong>设容器体积为 $V$，泵的抽速为 $S$，漏气率为 $Q$，则压强满足：")+
   fml("V\\frac{dp}{dt} = -Sp + Q")+
   p("稳态时 $dp/dt=0$，得极限压强 $p_{\\infty}=Q/S$。从初始压强 $p_0$ 起积分：")+
   fml("p(t) = p_{\\infty}+(p_0-p_{\\infty})e^{-St/V}")+
   p("可见压强按时间常数 $\\tau=V/S$ 指数下降，趋近泵的极限压强；要获得更高真空，须减小漏气率并提高抽速。"))+
   app(p("<strong>应用：</strong>旋片机械泵可达 $10^{-1}\\,\\text{Pa}$，扩散泵可达 $10^{-7}\\,\\text{Pa}$，涡轮分子泵与离子泵可更低。压强测量按量程选用：热偶真空计利用稀薄气体热导率随压强变化，电离真空计利用气体分子被电离产生的离子电流。"))
 )},
]},
]
ch4_sections = [
{
"name": "4.1 功、热量与内能",
"color": "#0d9488",
"desc": "准静态功、热量与内能的实验基础",
"items": [
{"id":"t4s1-1","name":"准静态过程的功","tags":["thm","der"],"brief":"功是过程量，等于 p-V 图上的面积。",
 "fig":"workpdv","figCap":"准静态膨胀的功等于 p-V 图曲线下的面积",
 "body": wrap(
   thm("准静态功",p("系统在准静态过程中体积改变 $dV$ 时对外做功 $\\delta W=p\\,dV$，整个过程做功为：")+
   fml("W = \\int_{V_1}^{V_2} p\\,dV")+
   p("功在 $p$-$V$ 图上等于过程曲线下的面积，与路径有关，是过程量。"))+
   der(p("<strong>由活塞受力导出：</strong>设活塞面积 $A$，气体压强 $p$，活塞移动微小位移 $dx$，则气体对活塞做功：")+
   fml("\\delta W = F\\,dx = (pA)\\,dx = p\\,(A\\,dx) = p\\,dV")+
   p("若气体被压缩 $dV<0$，则 $\\delta W<0$，表示外界对气体做功。对有限过程积分：")+
   fml("W = \\int_{V_1}^{V_2}p\\,dV")+
   p("当过程路径不同时积分值不同，故不能写成简单差分 $\\Delta W$，只能写 $W$。"))+
   note(p("若过程可逆，逆过程做功与正过程大小相等符号相反；若存在摩擦，正逆过程做功不相等，循环后外界净输入能量，表现为耗散。"))
 )},
{"id":"t4s1-2","name":"热量与热容量","tags":["def","der"],"brief":"热量是过程量，热容与过程有关。",
 "body": wrap(
   defn("热量与热容量",p("热量是系统与外界之间因温度差而传递的能量，也是过程量。热容量定义为单位温度变化吸收的热量 $C=\\delta Q/dT$；对 $1\\,\\text{mol}$ 物质称摩尔热容 $C_m$。"))+
   der(p("<strong>由第一定律看热容与过程有关：</strong>对 $1\\,\\text{mol}$ 理想气体，由 $\\delta Q=dU_m+p\\,dV_m$ 与 $dU_m=C_{V,m}dT$：")+
   fml("\\delta Q = C_{V,m}dT + p\\,dV_m")+
   p("若保持体积不变 $dV_m=0$，得定容摩尔热容 $C_{V,m}=(\\delta Q/dT)_V$；若保持压强不变，由状态方程 $p\\,dV_m=R\\,dT$ 代入得：")+
   fml("C_{p,m} = C_{V,m}+R")+
   p("可见同一物质在不同过程中热容不同，热量因此不能用热容乘温差无条件地写成态函数变化。"))+
   exa(p("<strong>例：</strong>单原子理想气体 $C_{V,m}=\\frac{3}{2}R\\approx12.5\\,\\text{J/(mol·K)}$，$C_{p,m}=\\frac{5}{2}R\\approx20.8\\,\\text{J/(mol·K)}$。同一升温过程定压比定容多吸收 $R\\Delta T$ 的热量，用于对外做功。"))+
   note(p("热容量是广延量，比热容（单位质量）与摩尔热容都是强度量。"))
 )},
{"id":"t4s1-3","name":"内能与焦耳实验","tags":["def","der"],"brief":"理想气体内能只与温度有关。",
 "body": wrap(
   defn("内能与焦耳实验",p("内能是系统内所有分子动能与相互作用势能之和，是态函数。焦耳实验让气体向真空自由膨胀，容器绝热且气体不对外做功（$W=0$、$Q=0$），发现水温不变，说明理想气体内能只与温度有关。"))+
   der(p("<strong>推导：</strong>自由膨胀过程 $Q=0$、$W=0$，由第一定律：")+
   fml("\\Delta U = Q - W = 0")+
   p("而气体体积显著增大、温度未变，故 $U$ 与体积无关，只依赖温度：")+
   fml("\\left(\\frac{\\partial U}{\\partial V}\\right)_T = 0 \\implies U = U(T)")+
   p("对 $1\\,\\text{mol}$ 理想气体 $U_m=C_{V,m}T+\\text{const}$，全微分 $dU_m=C_{V,m}dT$，说明内能变化只由温度决定。"))+
   note(p("真实气体自由膨胀后温度略降，说明其内能与体积有关（分子间引力势能随体积增大）。范德瓦尔斯气体的内能可写为 $U_m=C_{V,m}T-a/V_m$。"))
 )},
]},
{
"name": "4.2 热力学第一定律",
"color": "#0f766e",
"desc": "第一定律的表述、微分形式与循环应用",
"items": [
{"id":"t4s2-1","name":"热力学第一定律","tags":["thm","der"],"brief":"能量守恒在热现象中的表述。",
 "fig":"firstlaw","figCap":"系统吸热一部分增加内能，一部分对外做功",
 "body": wrap(
   thm("热力学第一定律",p("系统从外界吸收的热量，一部分用于增加内能，一部分用于对外做功：")+
   fml("Q = \\Delta U + W")+
   p("对无限小过程写为 $\\delta Q=dU+\\delta W$。第一定律是包含热现象的能量守恒定律，也是第一类永动机不可能制成的理论依据。"))+
   der(p("<strong>由能量守恒论证：</strong>把系统与外界看作一个孤立系统，总能量守恒：")+
   fml("\\Delta E_{sys} + \\Delta E_{surr} = 0")+
   p("系统与外界只通过热量 $Q$ 与功 $W$ 交换能量，外界能量变化为 $\\Delta E_{surr}=W-Q$，代入得：")+
   fml("\\Delta U - (Q - W) = 0 \\implies Q = \\Delta U + W")+
   p("其中把系统能量变化记为 $\\Delta U$；若过程涉及宏观动能变化，还需计入机械能项。"))+
   app(p("<strong>应用：</strong>第一定律用于分析热机、制冷机、节流与相变过程的能量平衡，是工程热力学与能源动力装置分析的基础。"))
 )},
{"id":"t4s2-2","name":"第一定律的微分形式与符号约定","tags":["der"],"brief":"统一符号约定下的微分表达。",
 "body": wrap(
   der(p("<strong>符号约定：</strong>规定系统吸热 $Q>0$、系统对外做功 $W>0$、内能增加 $\\Delta U>0$，则第一定律写为：")+
   fml("\\delta Q = dU + \\delta W = dU + p\\,dV")+
   p("若系统吸热同时对外做功，则 $dU=\\delta Q-\\delta W$。对理想气体代入 $dU=nC_{V,m}dT$ 与等压时 $\\delta W=p\\,dV=nR\\,dT$：")+
   fml("\\delta Q = nC_{V,m}dT + nR\\,dT = nC_{p,m}dT\\quad(p\\ \\text{不变})")+
   p("恰给出定压热容关系。"))+
   der(p("<strong>与不同约定的换算：</strong>工程热力学常规定外界对系统做功为正，此时 $\\delta Q=dU+\\delta W'$ 中 $\\delta W'=-p\\,dV$，方程变为 $\\delta Q=dU-\\delta W'$。两套约定数值相反，使用时必须统一，切忌在同一式中混用。"))+
   note(p("第一定律中 $dU$ 是全微分（态函数），而 $\\delta Q$、$\\delta W$ 是过程量，故用 $\\delta$ 而不用 $d$ 加以区分，这是热力学记号的重要约定。"))
 )},
{"id":"t4s2-3","name":"第一定律对循环过程的应用","tags":["der","exa"],"brief":"循环净吸热等于对外净功。",
 "body": wrap(
   der(p("<strong>推导：</strong>循环过程初末状态相同，内能变化为零 $\\Delta U=0$，由第一定律：")+
   fml("\\oint \\delta Q = \\oint \\delta W = W_{net}")+
   p("即循环净热量等于对外净功。设系统在高温处吸热 $Q_1$、低温处放热 $Q_2$，则 $W_{net}=Q_1-Q_2$。在 $p$-$V$ 图上，顺时针循环（正循环）$W_{net}>0$ 为热机，逆时针循环为制冷机，净功大小等于循环曲线所围面积。"))+
   exa(p("<strong>例：</strong>某循环在 $p$-$V$ 图上围成面积 $200\\,\\text{J}$，顺时针进行，全程吸热 $800\\,\\text{J}$，则对外净功 $W_{net}=200\\,\\text{J}$，放热 $Q_2=Q_1-W_{net}=600\\,\\text{J}$，效率 $\\eta=200/800=25\\%$。"))+
   app(p("<strong>应用：</strong>蒸汽动力循环、内燃机循环与制冷循环的分析都以 $\\oint\\delta Q=\\oint\\delta W$ 为出发点，配合各过程的物态方程逐段计算。"))
 )},
]},
{
"name": "4.3 热容与焓",
"color": "#14b8a6",
"desc": "定容定压热容、焓与迈耶公式、比热比",
"items": [
{"id":"t4s3-1","name":"定容热容与定压热容","tags":["def","der"],"brief":"两种过程的热容定义与关系。",
 "body": wrap(
   defn("定容与定压热容",p("定容摩尔热容 $C_{V,m}=(\\delta Q/dT)_V$，定压摩尔热容 $C_{p,m}=(\\delta Q/dT)_p$。理想气体的 $C_{V,m}$、$C_{p,m}$ 在经典范围内与温度无关。"))+
   der(p("<strong>由第一定律分别导出：</strong>等容过程 $dV=0$，故 $\\delta Q=dU$：")+
   fml("C_{V,m} = \\left(\\frac{\\partial U_m}{\\partial T}\\right)_V")+
   p("等压过程 $dp=0$，$\\delta Q=dU_m+p\\,dV_m$，由 $p\\,dV_m=R\\,dT$ 与 $dU_m=C_{V,m}dT$：")+
   fml("C_{p,m} = C_{V,m} + R")+
   p("可见 $C_{p,m}>C_{V,m}$，多出的 $R$ 正是等压膨胀时对外做功所需的热量。"))+
   note(p("对固体与液体，因体积变化极小，$C_p\\approx C_V$；对气体两者差别显著，是热力学计算中必须区分的量。"))
 )},
{"id":"t4s3-2","name":"焓与迈耶公式","tags":["thm","der"],"brief":"等压吸热等于焓增，Cp−CV=R。",
 "body": wrap(
   thm("焓",p("定义态函数焓 $H=U+pV$。对等压过程 $\\Delta H=Q_p$，即等压过程吸收的热量等于焓的增量，故焓在等压过程分析中极为便利。"))+
   der(p("<strong>由定义导出：</strong>对焓取全微分：")+
   fml("dH = dU + p\\,dV + V\\,dp")+
   p("由第一定律 $\\delta Q=dU+p\\,dV$，代入得：")+
   fml("\\delta Q = dH - V\\,dp")+
   p("等压时 $dp=0$，故 $\\delta Q=dH$，于是 $C_{p,m}=(\\partial H_m/\\partial T)_p$。对理想气体 $H_m=U_m+pV_m=U_m+RT$，求导得 $C_{p,m}=C_{V,m}+R$，即迈耶公式。"))+
   note(p("焓是广延量，单位为焦耳。节流过程（等焓过程）与化学反应热效应都直接与焓相联系，是工程热力学的核心状态函数。"))
 )},
{"id":"t4s3-3","name":"比热比与理想气体","tags":["der","exa"],"brief":"γ=(i+2)/i 及由声速测定。",
 "body": wrap(
   der(p("<strong>由自由度导出：</strong>对具有 $i$ 个自由度的理想气体，$C_{V,m}=\\frac{i}{2}R$、$C_{p,m}=\\frac{i+2}{2}R$，故比热比：")+
   fml("\\gamma = \\frac{C_{p,m}}{C_{V,m}} = \\frac{i+2}{i}")+
   p("单原子 $i=3$ 得 $\\gamma=5/3\\approx1.67$；刚性双原子 $i=5$ 得 $\\gamma=1.4$；刚性多原子 $i=6$ 得 $\\gamma\\approx1.33$。"))+
   der(p("<strong>由声速测定 γ：</strong>气体中声速为 $v_s=\\sqrt{\\gamma p/\\rho}=\\sqrt{\\gamma RT/M}$，测得声速与温度即可反求：")+
   fml("\\gamma = \\frac{Mv_s^2}{RT}")+
   p("这是测定比热比的经典方法（声速法）。"))+
   exa(p("<strong>例：</strong>空气在 $T=293\\,\\text{K}$ 时声速 $v_s=343\\,\\text{m/s}$，$M=0.029\\,\\text{kg/mol}$，代入得 $\\gamma\\approx1.40$，与双原子气体理论值一致，说明常温下空气分子的振动自由度未被激发。"))+
   note(p("比热比 $\\gamma$ 也是绝热过程的关键参数，$\\gamma$ 越大绝热曲线越陡，直接影响热机效率与绝热压缩温升。"))
 )},
]},
{
"name": "4.4 理想气体的典型过程",
"color": "#115e59",
"desc": "等值过程、绝热过程、多方过程与比较",
"items": [
{"id":"t4s4-1","name":"等容、等压与等温过程","tags":["der","app"],"brief":"三个基本等值过程的功与热。",
 "fig":"isoprocess","figCap":"等容、等压、等温过程的 p-V 图",
 "body": wrap(
   der(p("<strong>等容过程：</strong>$V$ 不变，$W=0$，吸热全部变为内能增量：")+
   fml("W_V = 0,\\qquad Q_V = nC_{V,m}\\Delta T")+
   p("<strong>等压过程：</strong>$p$ 不变，做功为矩形面积，吸热等于焓增：")+
   fml("W_p = p(V_2-V_1) = nR\\Delta T,\\qquad Q_p = nC_{p,m}\\Delta T")+
   p("<strong>等温过程：</strong>$T$ 不变，内能不变 $\\Delta U=0$，吸热全部对外做功：")+
   fml("W_T = \\int_{V_1}^{V_2}\\frac{nRT}{V}dV = nRT\\ln\\frac{V_2}{V_1},\\qquad Q_T=W_T")+
   p("三个过程对应 $p$-$V$ 图上不同的曲线，功的大小依次由图线下的面积给出。"))+
   app(p("<strong>应用：</strong>等温过程是理想化极限，缓慢导热过程接近等温；等压过程常见于开放容器加热；等容过程见于密闭刚性容器（如定容加热循环）。"))
 )},
{"id":"t4s4-2","name":"绝热过程与绝热方程","tags":["thm","der"],"brief":"绝热可逆过程 pV^γ=const。",
 "fig":"adiabatic","figCap":"同一起点的绝热线比等温线更陡",
 "body": wrap(
   thm("绝热过程方程",p("对理想气体的准静态绝热过程，$\\delta Q=0$，故 $dU=-\\delta W$，由此得泊松方程：")+
   fml("pV^{\\gamma}=\\text{const},\\qquad TV^{\\gamma-1}=\\text{const},\\qquad p^{1-\\gamma}T^{\\gamma}=\\text{const}"))+
   der(p("<strong>推导：</strong>由 $\\delta Q=0$、$dU=nC_{V,m}dT$、$\\delta W=p\\,dV$：")+
   fml("nC_{V,m}dT = -p\\,dV")+
   p("由理想气体方程 $pV=nRT$ 微分得 $p\\,dV+V\\,dp=nR\\,dT$，故 $dT=(p\\,dV+V\\,dp)/(nR)$，代入消去 $dT$：")+
   fml("\\frac{C_{V,m}}{R}(p\\,dV+V\\,dp) = -p\\,dV")+
   p("整理并用 $\\gamma-1=R/C_{V,m}$ 化简：")+
   fml("\\gamma\\frac{dV}{V} = -\\frac{dp}{p} \\implies \\ln p + \\gamma\\ln V=\\text{const} \\implies pV^{\\gamma}=\\text{const}"))+
   app(p("<strong>应用：</strong>绝热压缩使气体升温（柴油机点火、气筒发热），绝热膨胀使气体降温（制冷、云雾形成）；绝热方程是内燃机循环计算的基础。"))
 )},
{"id":"t4s4-3","name":"多方过程","tags":["der","app"],"brief":"pV^n=const 概括多种过程。",
 "body": wrap(
   der(p("<strong>摩尔热容为常数的过程：</strong>设过程满足 $pV^n=\\text{const}$，$n$ 为多方指数。对该式微分得 $dp/p=-n\\,dV/V$，代入 $\\delta Q=nC_{V,m}dT+p\\,dV$ 并用 $p\\,dV=nR\\,dT$ 整理，可得该过程的摩尔热容：")+
   fml("C_n = C_{V,m} + \\frac{R}{1-n}"))+
   der(p("<strong>与典型过程的对应：</strong>取不同 $n$ 值可得各类过程：")+
   fml("n=0:\\ \\text{等压},\\quad n=1:\\ \\text{等温},\\quad n=\\gamma:\\ \\text{绝热},\\quad n\\to\\infty:\\ \\text{等容}")+
   p("由 $C_n=C_{V,m}+R/(1-n)$ 验证：$n=0$ 得 $C_{V,m}+R=C_{p,m}$（等压）；$n=1$ 时 $C_n\\to\\infty$（等温，有限吸热而温度不变）；$n=\\gamma$ 得 $C_n=0$（绝热）；$n\\to\\infty$ 得 $C_n\\to C_{V,m}$（等容）。"))+
   app(p("<strong>应用：</strong>实际热机中压缩与膨胀过程既非完全绝热也非完全等温，常用多方过程近似描述；$1<n<\\gamma$ 的过程伴随向外界散热，见于有冷却的压缩过程。"))
 )},
{"id":"t4s4-4","name":"绝热与等温过程的比较","tags":["der","exa"],"brief":"绝热线比等温线更陡。",
 "body": wrap(
   der(p("<strong>斜率比较：</strong>等温过程 $pV=\\text{const}$，微分得斜率为：")+
   fml("\\left(\\frac{dp}{dV}\\right)_T = -\\frac{p}{V}")+
   p("绝热过程 $pV^\\gamma=\\text{const}$，微分得斜率：")+
   fml("\\left(\\frac{dp}{dV}\\right)_S = -\\gamma\\frac{p}{V}")+
   p("由于 $\\gamma>1$，同一点处绝热线斜率绝对值比等温线大 $\\gamma$ 倍，故绝热线更陡。"))+
   der(p("<strong>物理解释：</strong>绝热膨胀时气体对外做功但无热量补充，温度下降；等温膨胀时外界不断供热维持温度不变。由 $p=nRT/V$，绝热膨胀中 $T$ 同时减小使 $p$ 下降更快，故绝热线更陡。"))+
   exa(p("<strong>例：</strong>空气 $\\gamma=1.4$，从同一点 $(p_0,V_0)$ 膨胀到 $2V_0$，等温过程压强降为 $p_0/2$，绝热过程压强降为 $p_0/2^{1.4}\\approx0.38p_0$，明显更低。"))+
   note(p("这一差异在气体液化与制冷中十分关键：绝热膨胀可产生显著降温，而等温膨胀不会使温度改变。"))
 )},
]},
{
"name": "4.5 循环过程与热机效率",
"color": "#0d9488",
"desc": "循环过程、热机效率与内燃机循环",
"items": [
{"id":"t4s5-1","name":"循环过程与热机","tags":["def","der"],"brief":"循环过程与热机能流分析。",
 "fig":"heatengine","figCap":"热机从高温热源吸热、向低温热源放热并对外做功",
 "body": wrap(
   defn("循环过程与热机",p("系统经一系列过程回到初态称为<strong>循环过程</strong>。正循环（顺时针）对外做净功，可用于热机：从高温热源吸热 $Q_1$，对外做功 $W$，向低温热源放热 $Q_2$。"))+
   der(p("<strong>能量平衡：</strong>循环一周内能变化为零，由第一定律：")+
   fml("W = Q_1 - Q_2")+
   p("由第二定律（下一章）可知 $Q_2>0$ 不可避免，故 $W<Q_1$，热机效率总是小于 1：")+
   fml("\\eta = \\frac{W}{Q_1} = 1-\\frac{Q_2}{Q_1} < 1")+
   p("$p$-$V$ 图上循环曲线所围面积即为净功 $W$。"))+
   note(p("热机必须同时有高温热源与低温热源；不能只靠单一热源把热量全部转为功，这正是第二定律的开尔文表述。"))
 )},
{"id":"t4s5-2","name":"热机效率与制冷系数","tags":["thm","der"],"brief":"正循环效率与逆循环制冷系数。",
 "body": wrap(
   thm("热机效率与制冷系数",p("热机效率 $\\eta=W/Q_1=1-Q_2/Q_1$；逆循环（制冷机）的制冷系数 $\\varepsilon=Q_2/W=Q_2/(Q_1-Q_2)$。注意 $\\varepsilon$ 可以大于 1，而 $\\eta$ 恒小于 1。"))+
   der(p("<strong>效率的进一步展开：</strong>若循环吸放热总量为 $Q_1$、$Q_2$，则由第一定律：")+
   fml("\\eta = \\frac{Q_1-Q_2}{Q_1}")+
   p("对可逆循环 $Q_1/Q_2=T_1/T_2$，代入得卡诺效率 $\\eta_C=1-T_2/T_1$。对逆循环同理可得：")+
   fml("\\varepsilon = \\frac{Q_2}{Q_1-Q_2} = \\frac{T_2}{T_1-T_2}")+
   p("这是可逆制冷机的最大制冷系数，也是热泵效能系数的理论极限。"))+
   exa(p("<strong>例：</strong>室外 $T_2=273\\,\\text{K}$、室内 $T_1=300\\,\\text{K}$ 的热泵，理论上 $\\varepsilon\\approx273/(300-273)\\approx10.1$，即耗 1 J 电最多可向室内输运约 10 J 热量，远优于直接电加热。"))+
   note(p("实际热机因摩擦、有限速率传热等不可逆因素，效率总低于卡诺效率；提升效率的途径是提高高温热源温度或降低低温热源温度。"))
 )},
{"id":"t4s5-3","name":"奥托循环与狄塞尔循环","tags":["der","app"],"brief":"内燃机理想循环的效率。",
 "body": wrap(
   der(p("<strong>奥托循环：</strong>由两绝热（压缩、膨胀）与两等容（吸热、放热）组成，压缩比 $r=V_1/V_2$。两等容过程吸放热 $Q_1=nC_{V,m}(T_3-T_2)$、$Q_2=nC_{V,m}(T_4-T_1)$，故：")+
   fml("\\eta = 1-\\frac{Q_2}{Q_1} = 1-\\frac{T_4-T_1}{T_3-T_2}")+
   p("由绝热关系 $T_2V_1^{\\gamma-1}=T_3V_2^{\\gamma-1}$ 与 $T_1V_1^{\\gamma-1}=T_4V_2^{\\gamma-1}$ 可证 $(T_4-T_1)/(T_3-T_2)=1/r^{\\gamma-1}$，得：")+
   fml("\\eta_{Otto} = 1-\\frac{1}{r^{\\gamma-1}}"))+
   der(p("<strong>狄塞尔循环：</strong>以等压吸热代替等容吸热，压缩比更高，效率为：")+
   fml("\\eta_{Diesel} = 1-\\frac{1}{r^{\\gamma-1}}\\cdot\\frac{\\rho^{\\gamma}-1}{\\gamma(\\rho-1)}")+
   p("其中 $\\rho$ 为定压预胀比。同一压缩比下狄塞尔效率略低，但可实现更高压缩比，故总体效率往往更高。"))+
   app(p("<strong>应用：</strong>奥托循环对应汽油机，狄塞尔循环对应柴油机。柴油机压缩比可达 20 以上，靠绝热压缩使空气温度超过柴油燃点而自燃，无需火花塞。"))
 )},
]},
{
"name": "4.6 第一定律的应用",
"color": "#059669",
"desc": "焦耳-汤姆孙效应、节流制冷与实例分析",
"items": [
{"id":"t4s6-1","name":"焦耳-汤姆孙效应","tags":["der","exa"],"brief":"节流过程中气体温度随压强变化。",
 "body": wrap(
   der(p("<strong>节流过程的等焓性：</strong>气体经多孔塞节流时绝热且不对外做轴功。上游推入体积 $V_1$ 做功 $p_1V_1$，下游推出体积 $V_2$ 对外做功 $p_2V_2$，由能量守恒：")+
   fml("U_1+p_1V_1 = U_2+p_2V_2 \\implies H_1=H_2")+
   p("即节流过程等焓。定义焦耳-汤姆孙系数 $\\mu_{JT}=(\\partial T/\\partial p)_H$，由热力学关系可证：")+
   fml("\\mu_{JT} = \\frac{1}{C_p}\\left[T\\left(\\frac{\\partial V}{\\partial T}\\right)_p-V\\right]")+
   p("对理想气体 $V=RT/p$，代入得 $\\mu_{JT}=0$，故理想气体节流后温度不变；对真实气体一般不为零。"))+
   exa(p("<strong>例：</strong>室温空气的 $\\mu_{JT}\\approx0.25\\,\\text{K/atm}$，节流降压 10 atm 约降温 2.5 K；在转化温度以下 $\\mu_{JT}>0$ 为致冷效应，以上为致热效应。"))+
   note(p("焦耳-汤姆孙效应是林德空气液化循环的基础：先预冷到转化温度以下，再反复节流降温即可液化气体。"))
 )},
{"id":"t4s6-2","name":"节流过程与制冷循环","tags":["der","app"],"brief":"蒸汽压缩制冷与热泵。",
 "body": wrap(
   der(p("<strong>蒸汽压缩制冷循环：</strong>四步组成：绝热压缩（压缩机）、等压冷凝（放热 $Q_1$）、节流降压、等压蒸发（吸热 $Q_2$）。制冷系数为：")+
   fml("\\varepsilon = \\frac{Q_2}{W_{in}} = \\frac{h_1-h_4}{h_2-h_1}")+
   p("其中 $h$ 为各状态点焓值，$W_{in}=h_2-h_1$ 为压缩机耗功；节流前后焓相等 $h_3=h_4$，故只需测定各点焓值即可计算性能系数。"))+
   der(p("<strong>热泵与制冷的统一：</strong>同一循环若以向高温端排热为目的即为热泵，其效能系数为：")+
   fml("COP_{hp} = \\frac{Q_1}{W_{in}} = \\varepsilon+1")+
   p("可见热泵效能系数总比同工况制冷系数大 1，因为高温端排热等于低温端吸热与输入功之和。"))+
   app(p("<strong>应用：</strong>空调、冰箱、热泵热水器均基于此循环；选用低沸点工质以获得合适的蒸发与冷凝温度，还可利用余热驱动吸收式制冷。"))
 )},
{"id":"t4s6-3","name":"第一定律的实例分析","tags":["der","exa"],"brief":"绝热压缩升温与守恒检验。",
 "body": wrap(
   der(p("<strong>绝热压缩升温计算：</strong>气体从 $T_1$ 绝热压缩到 $T_2$，由 $TV^{\\gamma-1}=\\text{const}$：")+
   fml("T_2 = T_1\\left(\\frac{V_1}{V_2}\\right)^{\\gamma-1}")+
   p("外界对气体做功等于内能增量：")+
   fml("W_{on} = \\Delta U = nC_{V,m}(T_2-T_1)"))+
   exa(p("<strong>例（柴油机点火）：</strong>空气 $\\gamma=1.4$，压缩比 $r=20$，初温 $T_1=300\\,\\text{K}$，则 $T_2=300\\times20^{0.4}\\approx993\\,\\text{K}$，约 $720\\,°\\text{C}$，远超柴油燃点（约 $250\\,°\\text{C}$），故喷入柴油即可自燃。"))+
   der(p("<strong>第一定律的普遍检验：</strong>对任意过程，计算 $\\Delta U$、$W$、$Q$ 后必须满足 $Q=\\Delta U+W$；对循环过程应有 $\\oint dU=0$。用这些守恒关系可检查计算是否正确，也可确定未知的过程量。"))+
   app(p("<strong>应用：</strong>第一定律用于分析气动工具、内燃机、热泵与人体能量代谢，是能量分析的基本工具；配合第二定律才能判断过程方向与效率上限。"))
 )},
]},
]
ch5_sections = [
{
"name": "5.1 可逆过程与不可逆过程",
"color": "#7c3aed",
"desc": "可逆过程、不可逆过程与可逆判据",
"items": [
{"id":"t5s1-1","name":"可逆过程","tags":["def","der"],"brief":"系统与外界都能复原的过程。",
 "body": wrap(
   defn("可逆过程",p("若系统经历某过程后，能沿相反方向使系统和外界同时完全恢复原状而不留下任何变化，则称该过程为<strong>可逆过程</strong>。可逆过程是理想化的极限，要求过程准静态且无耗散。"))+
   der(p("<strong>可逆循环中的功与热：</strong>设系统经历可逆循环后复原，循环中 $\\oint dU=0$，故净功等于净热。对可逆过程各步都在平衡态附近进行，$\\delta W=p\\,dV$、$\\delta Q=T\\,dS$ 均成立：")+
   fml("\\oint \\delta Q = \\oint T\\,dS = \\oint \\delta W = \\oint p\\,dV")+
   p("若过程不可逆，则存在耗散，正逆过程不对称，$\\oint\\delta Q$ 不再等于可逆情形，系统或外界必然留下变化。可逆过程因此成为理想效率的基准。"))+
   note(p("实际过程都是不可逆的，但可逆过程是重要的理想模型：卡诺循环、可逆绝热与可逆等温过程构成热力学分析的理论上限。"))
 )},
{"id":"t5s1-2","name":"不可逆过程与自发过程","tags":["def","der"],"brief":"具有方向性的实际过程。",
 "body": wrap(
   defn("不可逆过程",p("一切实际过程都是不可逆过程：它们具有方向性，可自动朝某一方向进行而不可能自动逆向进行，如热量自发由高温传向低温、气体自由膨胀、摩擦生热等。"))+
   der(p("<strong>由能量退降说明不可逆性：</strong>以传热为例，若把高温热源 $T_1$ 的热量 $Q$ 传给低温热源 $T_2$，可做的最大功由卡诺效率决定：")+
   fml("W_{\\max} = Q\\left(1-\\frac{T_2}{T_1}\\right)")+
   p("传热后系统温度趋于均匀，可做功能力下降，散失的可用能（退降）为：")+
   fml("\\Delta W = Q\\frac{T_2}{T_1} = T_2\\Delta S_{irr}")+
   p("可见不可逆性对应着可用能的耗散与熵的产生，这是第二定律方向性的能量学表现。"))+
   note(p("不可逆过程可以自发进行，但要使其逆行必须借助外界做功（如制冷机、压缩机）；这正是热力学过程具有方向性的根本含义。"))
 )},
{"id":"t5s1-3","name":"可逆过程的判据","tags":["der"],"brief":"可逆的宏观与微观条件。",
 "body": wrap(
   der(p("<strong>宏观判据：</strong>可逆过程必须同时满足两点：一是准静态（过程无限缓慢，$u\\ll c_s$），二是无耗散（无摩擦、无电阻、无黏滞等不可逆因素）。对无摩擦准静态过程，压缩与膨胀互为逆过程 $W_{正}=-W_{逆}$；若存在摩擦则：")+
   fml("W_{正}+W_{逆} = -W_d < 0")+
   p("耗散功 $W_d>0$，正逆不对称。"))+
   der(p("<strong>微观判据与熵产生：</strong>可逆过程要求分子能沿原来的微观路径返回；由于热运动的随机性，这一要求实际上无法实现。熵产生可作为不可逆程度的量度：")+
   fml("S_{gen} = \\Delta S_{sys}-\\int\\frac{\\delta Q}{T_{surr}} \\ge 0")+
   p("$S_{gen}=0$ 对应可逆，越大的 $S_{gen}$ 表示不可逆程度越高。"))+
   note(p("工程中常通过减小温差、减小流速与消除摩擦使过程尽量接近可逆以提高效率；但无论怎样优化，$S_{gen}$ 都不可能为零。"))
 )},
]},
{
"name": "5.2 热力学第二定律的表述",
"color": "#6d28d9",
"desc": "开尔文-普朗克表述、克劳修斯表述与等价性",
"items": [
{"id":"t5s2-1","name":"开尔文-普朗克表述","tags":["thm","der"],"brief":"不能从单一热源吸热完全变功。",
 "fig":"secondlaw","figCap":"热机效率 η<1：必须向低温热源放热",
 "body": wrap(
   thm("开尔文-普朗克表述",p("不可能制成一种循环动作的热机，只从单一热源吸收热量，使之完全变为功而不产生其他影响。换言之，第二类永动机不可能制成。"))+
   der(p("<strong>由效率上限论证：</strong>设热机从单一热源 $T_1$ 吸热 $Q_1$，若全部变为功则 $W=Q_1$、$\\eta=1$。由第一定律循环 $W=Q_1-Q_2$，需 $Q_2=0$。但由卡诺定理可逆效率为：")+
   fml("\\eta \\le 1-\\frac{T_2}{T_1} < 1\\quad(T_2>0)")+
   p("只要低温热源温度 $T_2>0$，就必须有一部分热量 $Q_2>0$ 排向低温热源，故 $\\eta<1$，不可能把单一热源的热量全部变成功。"))+
   note(p("开尔文表述并不禁止把热量完全变成功，只要伴有其他变化即可（如等温膨胀）；它禁止的是在循环中无其他影响地把单一热源热量全部变功。"))
 )},
{"id":"t5s2-2","name":"克劳修斯表述","tags":["thm","der"],"brief":"热量不能自发由低温传向高温。",
 "body": wrap(
   thm("克劳修斯表述",p("不可能把热量从低温物体传到高温物体而不引起其他变化。换言之，热量自发传递的方向只能由高温到低温。"))+
   der(p("<strong>由制冷系数说明：</strong>制冷机把热量 $Q_2$ 从低温热源 $T_2$ 抽到高温热源 $T_1$，必须消耗功 $W$。若不需要消耗功（$W=0$），则制冷系数发散：")+
   fml("\\varepsilon = \\frac{Q_2}{W} \\to \\infty")+
   p("这与实验事实矛盾。由卡诺逆循环，可逆制冷系数为 $\\varepsilon_C=T_2/(T_1-T_2)$，只要 $T_1>T_2$ 就是有限值，必须耗功：")+
   fml("W = Q_2\\frac{T_1-T_2}{T_2} > 0")+
   p("故热量不可能自发地由低温传向高温，克劳修斯表述成立。"))+
   note(p("冰箱、空调能实现热量由低温向高温输运，但代价是消耗电能；这与克劳修斯表述不矛盾，因为过程中引起了其他变化（外界耗功）。"))
 )},
{"id":"t5s2-3","name":"两种表述的等价性","tags":["der"],"brief":"开尔文表述与克劳修斯表述等价。",
 "body": wrap(
   der(p("<strong>反证法证明：</strong>先设克劳修斯表述不成立，存在机器可不耗功地把热量 $Q_2$ 从低温 $T_2$ 送到高温 $T_1$。再令一台卡诺热机在 $T_1$、$T_2$ 间工作，从 $T_1$ 吸热 $Q_2$，对外做功 $W$，向 $T_2$ 放热 $Q_2$：")+
   fml("W = Q_2\\left(1-\\frac{T_2}{T_1}\\right)")+
   p("把两机组合，净效果是热机从 $T_1$ 吸热 $Q_2$ 全部变成功 $W$（送热过程恰好把 $Q_2$ 补回 $T_1$，$T_2$ 净变化为零），这正违反开尔文表述。"))+
   der(p("<strong>反向证明：</strong>同理，若开尔文表述不成立（可把单一热源热量全变功），则该功可驱动制冷机把热量从低温送到高温，净效果等价于热量自发由低温到高温，违反克劳修斯表述。故两种表述完全等价。"))+
   note(p("两种表述分别从产功与传热两个角度描述同一热力学方向性；它们等价说明第二定律有多种表述形式，但内核唯一。"))
 )},
]},
{
"name": "5.3 卡诺循环与卡诺定理",
"color": "#8b5cf6",
"desc": "卡诺循环、卡诺效率与卡诺定理",
"items": [
{"id":"t5s3-1","name":"卡诺循环","tags":["def","der"],"brief":"两等温两绝热的理想循环。",
 "fig":"carnotcycle","figCap":"卡诺循环：两段等温与两段绝热组成，围成最大效率",
 "body": wrap(
   defn("卡诺循环",p("卡诺循环由两个可逆等温过程和两个可逆绝热过程组成，工作于温度 $T_1$ 的高温热源与 $T_2$ 的低温热源之间，是效率最高的理想循环。"))+
   der(p("<strong>各过程分析：</strong>记四状态为 1→2 等温膨胀、2→3 绝热膨胀、3→4 等温压缩、4→1 绝热压缩。等温吸热与放热为：")+
   fml("Q_1 = nRT_1\\ln\\frac{V_2}{V_1},\\qquad Q_2 = nRT_2\\ln\\frac{V_3}{V_4}")+
   p("绝热过程满足 $T_1V_2^{\\gamma-1}=T_2V_3^{\\gamma-1}$ 与 $T_1V_1^{\\gamma-1}=T_2V_4^{\\gamma-1}$，两式相除得：")+
   fml("\\frac{V_2}{V_1} = \\frac{V_3}{V_4}")+
   p("故 $Q_1/Q_2=T_1/T_2$，这与热力学温标的定义一致。"))+
   app(p("<strong>应用：</strong>卡诺循环是热机效率的理论上限，也是制冷机与热泵效能系数的基准；实际热机通过逼近卡诺循环来提高效率，如改善回热与减小温差。"))
 )},
{"id":"t5s3-2","name":"卡诺热机效率","tags":["thm","der"],"brief":"η_C=1−T2/T1，只依赖温度。",
 "body": wrap(
   thm("卡诺效率",p("可逆卡诺热机效率只由两热源温度决定：")+
   fml("\\eta_C = 1-\\frac{T_2}{T_1}")+
   p("与工作物质种类、循环大小无关，这就是热力学温标得以建立的基础。"))+
   der(p("<strong>推导：</strong>由 $Q_1=nRT_1\\ln(V_2/V_1)$、$Q_2=nRT_2\\ln(V_3/V_4)$ 及 $V_2/V_1=V_3/V_4$ 得 $Q_2/Q_1=T_2/T_1$，代入效率定义：")+
   fml("\\eta = 1-\\frac{Q_2}{Q_1} = 1-\\frac{T_2}{T_1}"))+
   exa(p("<strong>例：</strong>热源温度 $T_1=500\\,\\text{K}$、$T_2=300\\,\\text{K}$ 时，$\\eta_C=1-300/500=40\\%$；把 $T_1$ 提高到 $600\\,\\text{K}$ 则 $\\eta_C=50\\%$，说明提高高温热源温度对效率提升显著。"))+
   note(p("效率 $\\eta_C<1$ 总是成立（因 $T_2>0$）；只有当 $T_2\\to0\\,\\text{K}$ 时效率才趋于 1，而绝对零度不可达到（第三定律）。"))
 )},
{"id":"t5s3-3","name":"卡诺定理","tags":["thm","der"],"brief":"所有热机效率不超过卡诺效率。",
 "body": wrap(
   thm("卡诺定理",p("工作于两热源间的一切热机，其效率不可能高于可逆卡诺热机的效率；可逆热机效率与工作物质无关，且同温下相等：")+
   fml("\\eta \\le \\eta_C = 1-\\frac{T_2}{T_1}"))+
   der(p("<strong>反证法证明：</strong>设存在效率 $\\eta'>\\eta_C$ 的热机 $M$，令其驱动一台卡诺制冷机 $R$（逆循环）。调节两机使 $M$ 向低温热源放出的热量恰等于 $R$ 从低温热源吸收的热量，则低温热源净热为零。此时高温热源净放热为：")+
   fml("\\Delta Q_1 = Q_1^R-Q_1^M")+
   p("由 $\\eta'>\\eta_C$ 可得净功 $W=W^M-W^R>0$ 而低温热源无变化，等价于把高温热源的热量完全变成功，违反第二定律。故必有 $\\eta'\\le\\eta_C$。"))+
   der(p("<strong>可逆机效率相等：</strong>若两机都可逆，则互相驱动均不能违反第二定律，故 $\\eta_1\\le\\eta_2$ 与 $\\eta_2\\le\\eta_1$ 同时成立，得 $\\eta_1=\\eta_2$，即效率只与温度有关而与工作物质无关。"))+
   note(p("卡诺定理是热力学温标得以建立、并可定义绝对熵的理论基础，也是判断实际热机性能优劣的标准。"))
 )},
]},
{
"name": "5.4 熵与熵增原理",
"color": "#5b21b6",
"desc": "克劳修斯不等式、熵的定义、熵变计算与熵增原理",
"items": [
{"id":"t5s4-1","name":"克劳修斯不等式与熵的定义","tags":["def","der"],"brief":"∮δQ/T≤0 与态函数熵的引入。",
 "body": wrap(
   defn("克劳修斯不等式",p("对任意循环，系统所吸收的热量与热源温度之比沿循环的积分不大于零：")+
   fml("\\oint \\frac{\\delta Q}{T_{surr}} \\le 0")+
   p("可逆循环取等号，不可逆循环取小于号。它是第二定律的数学表述之一。"))+
   der(p("<strong>由不等式引入熵：</strong>取任意可逆过程 $A\\to B$ 与 $B\\to A$ 组成可逆循环，由克劳修斯不等式取等号：")+
   fml("\\oint_{rev}\\frac{\\delta Q}{T} = \\int_A^B\\frac{\\delta Q}{T}+\\int_B^A\\frac{\\delta Q}{T}=0")+
   p("故 $\\int_A^B \\delta Q/T$ 与路径无关，只由初末态决定，据此定义态函数熵：")+
   fml("dS = \\frac{\\delta Q_{rev}}{T},\\qquad S_B-S_A = \\int_A^B\\frac{\\delta Q_{rev}}{T}")+
   p("对不可逆过程，不等式给出 $\\Delta S > \\int\\delta Q/T$，即熵变大于实际热温比积分。"))+
   note(p("熵的定义中必须用可逆路径积分；对不可逆过程，可设计连接同一初末态的可逆路径来计算熵变，这是熵变计算的通用方法。"))
 )},
{"id":"t5s4-2","name":"熵变的计算","tags":["der","exa"],"brief":"理想气体与典型过程的熵变。",
 "fig":"entropy","figCap":"T-S 图上过程曲线下的面积等于交换的热量",
 "body": wrap(
   der(p("<strong>理想气体熵变：</strong>由第一定律 $\\delta Q=dU+\\delta W=nC_{V,m}dT+p\\,dV$，沿可逆路径除以 $T$：")+
   fml("dS = nC_{V,m}\\frac{dT}{T}+nR\\frac{dV}{V}")+
   p("积分得：")+
   fml("\\Delta S = nC_{V,m}\\ln\\frac{T_2}{T_1}+nR\\ln\\frac{V_2}{V_1}")+
   p("利用 $pV=nRT$ 可改写为等价形式 $\\Delta S=nC_{p,m}\\ln(T_2/T_1)-nR\\ln(p_2/p_1)$。对等温过程 $\\Delta S=nR\\ln(V_2/V_1)$，对等容过程 $\\Delta S=nC_{V,m}\\ln(T_2/T_1)$。"))+
   exa(p("<strong>例（自由膨胀）：</strong>理想气体向真空自由膨胀，$T$ 不变而体积由 $V$ 增至 $2V$，为不可逆过程；设计等温可逆路径计算得 $\\Delta S=nR\\ln2>0$。系统熵增大而温度不变，说明熵增与不可逆性直接相关。"))+
   app(p("<strong>应用：</strong>熵变计算用于判断化学反应方向（配合吉布斯自由能）、计算实际过程的最大可用功，以及分析热机与制冷循环的性能。"))
 )},
{"id":"t5s4-3","name":"熵增原理与自由能判据","tags":["der","app"],"brief":"孤立系统熵不减少，过程方向判据。",
 "body": wrap(
   der(p("<strong>熵增原理推导：</strong>设系统经不可逆过程由 $A$ 到 $B$，再沿可逆路径返回 $A$，由克劳修斯不等式 $\\oint\\delta Q/T\\le0$：")+
   fml("\\int_A^B\\frac{\\delta Q}{T_{surr}}+\\int_B^A\\frac{\\delta Q_{rev}}{T}\\le0")+
   p("第二项等于 $S_A-S_B$，故：")+
   fml("S_B-S_A \\ge \\int_A^B\\frac{\\delta Q}{T_{surr}}")+
   p("对孤立系统 $\\delta Q=0$，得 $S_B\\ge S_A$，即孤立系统熵永不减少：可逆时不变、不可逆时增大。这就是熵增原理。"))+
   der(p("<strong>过程方向判据：</strong>把系统与热源作为孤立整体，可得等温等容过程 $\\Delta F\\le0$、等温等压过程 $\\Delta G\\le0$，自发过程总是朝自由能减小的方向进行，平衡时取极小值。"))+
   app(p("<strong>应用：</strong>熵增原理用于判断化学反应与相变的自发方向、计算过程的最大可用功；自由能判据是材料、化工与生物热力学分析的核心工具。"))
 )},
]},
{
"name": "5.5 熵的统计意义与玻尔兹曼关系",
"color": "#a855f7",
"desc": "熵的统计意义、玻尔兹曼关系与热力学几率",
"items": [
{"id":"t5s5-1","name":"熵的统计意义","tags":["der","exa"],"brief":"熵是系统无序度（微观状态数）的量度。",
 "fig":"boltzmannentropy","figCap":"熵与微观状态数 W 通过 S=k ln W 相联系",
 "body": wrap(
   der(p("<strong>由微观状态数理解熵：</strong>系统宏观态对应的微观状态数 $W$ 越大，出现概率越大，宏观上越无序；平衡态是 $W$ 取极大的态。由玻尔兹曼关系 $S=k\\ln W$，当系统由两部分组成、$W=W_1W_2$ 时：")+
   fml("S = k\\ln(W_1W_2)=k\\ln W_1+k\\ln W_2 = S_1+S_2")+
   p("这正好符合熵的广延可加性，说明 $S=k\\ln W$ 的合理性。"))+
   exa(p("<strong>例（气体自由膨胀）：</strong>分子从体积 $V$ 自由膨胀到 $2V$，每个分子可占据的空间加倍，$N$ 个分子的微观状态数增加 $2^N$ 倍：")+
   fml("\\Delta S = k\\ln 2^N = Nk\\ln2 = nR\\ln2")+
   p("与热力学计算 $\\Delta S=nR\\ln(V_2/V_1)=nR\\ln2$ 完全一致，说明统计熵与热力学熵定义自洽。"))+
   note(p("熵是系统无序程度的量度：越无序、越均匀的状态微观状态数越多，熵越大。第二定律因此可表述为孤立系统总是朝更无序的状态演化。"))
 )},
{"id":"t5s5-2","name":"玻尔兹曼关系","tags":["thm","der"],"brief":"S=k ln W 揭示熵的统计本质。",
 "body": wrap(
   thm("玻尔兹曼关系",p("熵与系统微观状态数的关系为：")+
   fml("S = k\\ln W")+
   p("$W$ 为给定宏观态对应的微观状态数，$k$ 为玻尔兹曼常数。该式把宏观不可逆性的熵与微观状态概率联系起来，是统计物理最基本的公式之一。"))+
   der(p("<strong>由理想气体验证：</strong>把体积 $V$ 分成若干等分小格，所有分子都集中在某一半空间的微观状态数与均匀分布状态数之比为 $2^{-N}$，即均匀分布的微观状态数大 $2^N$ 倍，故：")+
   fml("\\Delta S = k\\ln 2^N = Nk\\ln2 = nR\\ln2")+
   p("与热力学熵变 $nR\\ln2$ 一致（因 $Nk=nR$），定量验证了玻尔兹曼关系。"))+
   note(p("玻尔兹曼关系被刻在其墓碑上。它揭示了不可逆性的统计本质：并非绝对不可能反向，而是反向的概率极其微小，随分子数指数衰减。"))
 )},
{"id":"t5s5-3","name":"热力学几率与不可逆性","tags":["der","exa"],"brief":"不可逆性的统计解释与涨落。",
 "body": wrap(
   der(p("<strong>概率估算：</strong>设气体自由膨胀后回到初始半空间的概率为 $P=2^{-N}$。对宏观量 $N\\sim10^{23}$ 个分子：")+
   fml("P = 2^{-N} \\approx 10^{-3\\times10^{22}}")+
   p("这一概率小到实际不可能观测到，故宏观过程表现为不可逆。由涨落引起的相对熵减估算为：")+
   fml("\\frac{\\Delta S}{S}\\sim \\frac{1}{N}")+
   p("相对涨落随 $N$ 增大而趋于零，这就是宏观确定性与不可逆性的统计来源。"))+
   exa(p("<strong>例（涨落）：</strong>对 $N\\sim10^{10}$ 的微小体系，相对涨落约 $10^{-5}$，可通过精密测量观测到；说明第二定律对微小系统只是统计规律，可能出现短暂违反。"))+
   app(p("<strong>应用：</strong>涨落理论用于解释临界乳光、生物分子马达的定向运动与纳米器件的热噪声；麦克斯韦妖佯谬也通过信息与熵的关系得到解决。"))
 )},
]},
{
"name": "5.6 自由能与热力学势",
"color": "#7c3aed",
"desc": "亥姆霍兹自由能、吉布斯自由能、麦克斯韦关系与化学势",
"items": [
{"id":"t5s6-1","name":"亥姆霍兹自由能","tags":["def","der"],"brief":"F=U−TS，等温等容过程判据。",
 "body": wrap(
   defn("亥姆霍兹自由能",p("定义 $F=U-TS$，又称亥姆霍兹函数。它是在等温等容条件下判断过程方向与做功能力的态函数。"))+
   der(p("<strong>由第一、第二定律导出：</strong>对等温过程 $dT=0$，由 $\\delta Q\\le T\\,dS$ 与 $dU=\\delta Q+\\delta W_{on}$，可得对外做功 $\\delta W\\le -dF$，即：")+
   fml("-\\delta W \\le -dF \\implies W_{max} = -\\Delta F")+
   p("等温过程中系统对外做的最大功等于亥姆霍兹自由能的减少。取全微分：")+
   fml("dF = dU - T\\,dS - S\\,dT = -S\\,dT - p\\,dV")+
   p("由全微分条件得 $S=-(\\partial F/\\partial T)_V$、$p=-(\\partial F/\\partial V)_T$，是重要的热力学关系。"))+
   app(p("<strong>应用：</strong>亥姆霍兹自由能用于等温等容体系（如封闭反应器、电池）的平衡与方向判断：自发过程 $\\Delta F\\le0$，平衡时 $F$ 取极小；也用于计算等温过程的最大功输出。"))
 )},
{"id":"t5s6-2","name":"吉布斯自由能","tags":["def","der"],"brief":"G=H−TS，等温等压过程判据。",
 "body": wrap(
   defn("吉布斯自由能",p("定义 $G=H-TS=U+pV-TS$，又称吉布斯函数或自由焓。它是在等温等压条件下判断过程方向与平衡的态函数，化学反应与相变分析中最为常用。"))+
   der(p("<strong>由焓与熵导出：</strong>取全微分 $dG=dH-T\\,dS-S\\,dT$，由可逆关系 $dH=T\\,dS+V\\,dp$ 代入得：")+
   fml("dG = -S\\,dT + V\\,dp")+
   p("等温时 $dG=V\\,dp$，等压时 $dG=-S\\,dT$。对等温等压的自发过程 $\\Delta G\\le0$，平衡时 $G$ 取极小值。"))+
   der(p("<strong>与化学势的关系：</strong>对多组分系统，吉布斯自由能是各组分化学势的加权和：")+
   fml("G = \\sum_i \\mu_i n_i,\\qquad \\mu_i=\\left(\\frac{\\partial G}{\\partial n_i}\\right)_{T,p,n_j}")+
   p("相平衡条件即为各相中同一组分的化学势相等，这为相图与相变的定量分析提供了基础。"))+
   app(p("<strong>应用：</strong>吉布斯自由能用于判断化学反应方向、计算平衡常数（$\\Delta G^\\circ=-RT\\ln K$）以及分析合金、溶液与相变过程。"))
 )},
{"id":"t5s6-3","name":"麦克斯韦关系","tags":["thm","der"],"brief":"由热力学势全微分导出的偏导数关系。",
 "fig":"thermopotential","figCap":"热力学势的勒让德变换与由此导出的麦克斯韦关系",
 "body": wrap(
   thm("麦克斯韦关系",p("由四个热力学势的全微分条件，可得四组偏导数关系，其中两组为：")+
   fml("\\left(\\frac{\\partial T}{\\partial V}\\right)_S=-\\left(\\frac{\\partial p}{\\partial S}\\right)_V,\\qquad \\left(\\frac{\\partial S}{\\partial V}\\right)_T=\\left(\\frac{\\partial p}{\\partial T}\\right)_V"))+
   der(p("<strong>由全微分条件导出：</strong>取内能的全微分 $dU=T\\,dS-p\\,dV$，视 $U=U(S,V)$，则 $T=(\\partial U/\\partial S)_V$、$p=-(\\partial U/\\partial V)_S$。由混合偏导数相等：")+
   fml("\\frac{\\partial^2 U}{\\partial V\\partial S} = \\frac{\\partial^2 U}{\\partial S\\partial V} \\implies \\left(\\frac{\\partial T}{\\partial V}\\right)_S = -\\left(\\frac{\\partial p}{\\partial S}\\right)_V")+
   p("对 $dF=-S\\,dT-p\\,dV$ 作同样处理，得 $(\\partial S/\\partial V)_T=(\\partial p/\\partial T)_V$，这是最常用的一条麦克斯韦关系。"))+
   app(p("<strong>应用：</strong>麦克斯韦关系把难以直接测量的量（如熵随体积的变化）转化为可测量量（如压强随温度的变化），是推导热力学恒等式、内能与熵的物态方程的重要工具。"))
 )},
{"id":"t5s6-4","name":"特性函数与化学势","tags":["der","app"],"brief":"选择合适的势函数与状态变量。",
 "body": wrap(
   der(p("<strong>勒让德变换：</strong>由内能 $U(S,V)$ 出发，通过勒让德变换更换自变量，可得各热力学势：")+
   fml("F=U-TS\\ (T,V),\\quad H=U+pV\\ (S,p),\\quad G=H-TS\\ (T,p)")+
   p("每个势在其自然变量下是特性函数，其偏导数给出共轭变量：")+
   fml("\\left(\\frac{\\partial F}{\\partial T}\\right)_V=-S,\\qquad \\left(\\frac{\\partial G}{\\partial p}\\right)_T=V"))+
   der(p("<strong>化学势的意义：</strong>化学势 $\\mu=(\\partial G/\\partial n)_{T,p}$ 表示等温等压下每增加 $1\\,\\text{mol}$ 物质所需增加的自由能。物质总是由高化学势流向低化学势，相平衡与化学平衡条件均为化学势相等：")+
   fml("\\mu_i^{\\alpha}=\\mu_i^{\\beta}"))+
   app(p("<strong>应用：</strong>化学势用于解释扩散、相变、渗透压与电化学势（含电势项）；在统计物理中，$\\mu$ 是巨正则分布的关键参数，决定了粒子数的统计平衡。"))
 )},
]},
{
"name": "5.7 第二定律的应用",
"color": "#9333ea",
"desc": "克拉珀龙方程、热力学第三定律与信息熵",
"items": [
{"id":"t5s7-1","name":"克拉珀龙方程与相变","tags":["der","exa"],"brief":"相平衡曲线斜率与潜热的关系。",
 "fig":"clapeyron","figCap":"气液平衡曲线斜率由克拉珀龙方程给定",
 "body": wrap(
   der(p("<strong>克拉珀龙方程：</strong>两相平衡时化学势相等。沿平衡曲线变动 $dT$、$dp$，由 $d\\mu=-S_mdT+V_mdp$ 与 $d\\mu_\\alpha=d\\mu_\\beta$：")+
   fml("-S_{m,\\alpha}dT+V_{m,\\alpha}dp = -S_{m,\\beta}dT+V_{m,\\beta}dp")+
   p("整理并用潜热 $L=T(S_{m,\\beta}-S_{m,\\alpha})$：")+
   fml("\\frac{dp}{dT} = \\frac{L}{T(V_{m,\\beta}-V_{m,\\alpha})}"))+
   der(p("<strong>克劳修斯-克拉珀龙近似：</strong>对气液相变，忽略液相体积并取气相为理想气体 $V_m=RT/p$，代入上式分离变量并积分得：")+
   fml("\\ln\\frac{p_2}{p_1} = \\frac{L}{R}\\left(\\frac{1}{T_1}-\\frac{1}{T_2}\\right)")+
   p("此即克劳修斯-克拉珀龙方程，用于由两温度下的饱和蒸气压求汽化热。"))+
   exa(p("<strong>例：</strong>水的汽化热约 $40.7\\,\\text{kJ/mol}$，在 $373\\,\\text{K}$ 时饱和蒸气压为 $101.3\\,\\text{kPa}$，用上式计算约 $363\\,\\text{K}$ 时蒸气压约 $70\\,\\text{kPa}$。"))
 )},
{"id":"t5s7-2","name":"熵的绝对值与热力学第三定律","tags":["der","app"],"brief":"绝对零度时完美晶体熵趋于零。",
 "body": wrap(
   der(p("<strong>由低温热容确定绝对熵：</strong>由 $dS=C_p\\,dT/T$，物质的绝对熵可由低温热容积分得到：")+
   fml("S(T) = \\int_0^T\\frac{C_p(T')}{T'}dT' + \\sum_i\\frac{L_i}{T_i}")+
   p("求和中 $L_i$、$T_i$ 分别为各相变点的潜热与温度。若 $T\\to0$ 时 $C_p\\to0$ 足够快，积分收敛，熵有有限极限。"))+
   der(p("<strong>能斯特定理与第三定律：</strong>能斯特由实验总结出，当 $T\\to0$ 时凝聚系统在等温过程中的熵变趋于零：")+
   fml("\\lim_{T\\to0}\\Delta S = 0")+
   p("由此普朗克提出绝对熵约定：任何完美晶体在绝对零度时熵为零。第三定律指出绝对零度不可通过有限步骤达到。"))+
   app(p("<strong>应用：</strong>第三定律用于计算化学反应的标准熵变与低温热容实验；由它可推出绝对零度附近热容必须趋于零，与实验一致。"))
 )},
{"id":"t5s7-3","name":"信息熵与第二定律","tags":["der","app"],"brief":"信息与熵的联系、麦克斯韦妖。",
 "body": wrap(
   der(p("<strong>信息熵：</strong>香农定义信息熵 $H=-\\sum_i p_i\\ln p_i$，与热力学熵形式相同（差一个 $k$ 因子）。系统可能状态越多、概率分布越均匀，信息熵越大。")+
   fml("S = -k_B\\sum_i p_i\\ln p_i,\\qquad S = k_B\\ln W\\quad(p_i=1/W)")+
   p("当所有 $W$ 个状态等概率时 $p_i=1/W$，代回即得玻尔兹曼熵 $S=k_B\\ln W$。"))+
   der(p("<strong>麦克斯韦妖与信息：</strong>妖若要分辨分子并控制闸门，必须获取并存储信息。兰道尔原理指出擦除一个比特的信息至少耗散：")+
   fml("Q_{min} = k_BT\\ln2")+
   p("把妖的记忆擦除所耗散的熵至少抵消其造成的熵减，故第二定律不被违反；信息与热力学熵通过 $k_BT\\ln2$ 定量联系。"))+
   app(p("<strong>应用：</strong>信息熵用于数据压缩、编码与机器学习；兰道尔极限界定了计算的最小能耗，是量子计算与低功耗芯片设计的基本约束。"))
 )},
]},
]
CHAPTERS = [
    {"id":"t-ch1","num":"第一章","title":"热力学系统参量与状态方程","en":"THERMODYNAMIC SYSTEM & EQUATION OF STATE",
     "desc":"热力学系统与平衡态、状态参量与态函数、温度与温标、理想气体状态方程、范德瓦尔斯方程与真实气体、物态方程与临界现象。",
     "sections": ch1_sections},
    {"id":"t-ch2","num":"第二章","title":"气体动理论与统计分布律","en":"KINETIC THEORY & STATISTICAL DISTRIBUTIONS",
     "desc":"分子动理论与压强的微观解释、温度的微观意义与能量均分定理、麦克斯韦速率分布律、玻尔兹曼分布律、平均自由程与分子碰撞、麦克斯韦-玻尔兹曼统计。",
     "sections": ch2_sections},
    {"id":"t-ch3","num":"第三章","title":"输运过程","en":"TRANSPORT PROCESSES",
     "desc":"黏滞现象、热传导、扩散、输运系数的微观推导、稀薄气体与真空技术。",
     "sections": ch3_sections},
    {"id":"t-ch4","num":"第四章","title":"热力学第一定律","en":"FIRST LAW OF THERMODYNAMICS",
     "desc":"功、热量与内能、热力学第一定律、热容与焓、理想气体的典型过程、循环过程与热机效率、第一定律的应用。",
     "sections": ch4_sections},
    {"id":"t-ch5","num":"第五章","title":"热力学第二定律","en":"SECOND LAW OF THERMODYNAMICS",
     "desc":"可逆过程与不可逆过程、热力学第二定律的表述、卡诺循环与卡诺定理、熵与熵增原理、熵的统计意义与玻尔兹曼关系、自由能与热力学势、第二定律的应用。",
     "sections": ch5_sections},
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
  .la-phase-title.t-ch1::before{background:#dc2626}
  .la-phase-title.t-ch2::before{background:#ea580c}
  .la-phase-title.t-ch3::before{background:#d97706}
  .la-phase-title.t-ch4::before{background:#0d9488}
  .la-phase-title.t-ch5::before{background:#7c3aed}
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
<meta name="description" content="热学知识体系：热力学系统参量与状态方程、气体动理论与统计分布律、输运过程、热力学第一定律、热力学第二定律">
<title>热学 · 知识体系</title>
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
    <div class="la-eyebrow">THERMAL PHYSICS · KNOWLEDGE MAP</div>
    <h1>热学 · 知识体系</h1>
    <p class="la-subtitle">热力学系统参量与状态方程 · 气体动理论与统计分布律 · 输运过程 · 热力学第一定律 · 热力学第二定律</p>
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
    <div>热学 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于热学核心知识体系整理</div>
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
    with open("/workspace/thermal-physics.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated thermal-physics.html ({len(html)} chars)")
