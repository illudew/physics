# -*- coding: utf-8 -*-
"""Generate optics.html with 6 chapters: 几何光学/波动光学基础/干涉/衍射/偏振/散射吸收色散."""
import json

FIG = {
"refraction": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="80" width="220" height="70" fill="#eef4fb"/>
<line x1="10" y1="80" x2="230" y2="80" stroke="#475569" stroke-width="1.5"/>
<line x1="120" y1="10" x2="120" y2="150" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="4 3"/>
<line x1="120" y1="80" x2="70" y2="30" stroke="#2563eb" stroke-width="2"/>
<polygon points="70,30 80,37 73,44" fill="#2563eb"/>
<line x1="120" y1="80" x2="176" y2="124" stroke="#2563eb" stroke-width="2"/>
<polygon points="176,124 166,118 172,110" fill="#2563eb"/>
<line x1="120" y1="80" x2="176" y2="36" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="5 3"/>
<polygon points="176,36 166,42 172,50" fill="#ef4444"/>
<text x="86" y="62" font-size="11" fill="#64748b">θ1</text>
<text x="136" y="60" font-size="11" fill="#64748b">θ1'</text>
<text x="130" y="104" font-size="11" fill="#64748b">θ2</text>
<text x="16" y="26" font-size="11" fill="#2563eb">n1</text>
<text x="16" y="146" font-size="11" fill="#2563eb">n2</text>
<text x="188" y="32" font-size="10" fill="#ef4444">反射</text>
<text x="130" y="146" font-size="10" fill="#2563eb">折射</text>
</svg>''',
"lens": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 120 28 Q 106 80 120 132 Q 134 80 120 28 Z" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<line x1="120" y1="18" x2="120" y2="142" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<circle cx="40" cy="80" r="2.5" fill="#0f172a"/><text x="34" y="95" font-size="10" fill="#0f172a">F</text>
<circle cx="200" cy="80" r="2.5" fill="#0f172a"/><text x="194" y="95" font-size="10" fill="#0f172a">F'</text>
<line x1="40" y1="50" x2="40" y2="80" stroke="#64748b" stroke-width="1.5"/>
<text x="20" y="46" font-size="10" fill="#64748b">物 h</text>
<line x1="40" y1="50" x2="120" y2="50" stroke="#ef4444" stroke-width="1.8"/>
<line x1="120" y1="50" x2="180" y2="110" stroke="#2563eb" stroke-width="1.6"/>
<line x1="40" y1="50" x2="180" y2="110" stroke="#ef4444" stroke-width="1.4" stroke-dasharray="4 3"/>
<line x1="180" y1="80" x2="180" y2="110" stroke="#10b981" stroke-width="1.5"/>
<polygon points="180,110 177,101 183,101" fill="#10b981"/>
<text x="184" y="122" font-size="10" fill="#10b981">像 h'</text>
</svg>''',
"doubleslit": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="78" y="20" width="4" height="35" fill="#475569"/>
<rect x="78" y="65" width="4" height="28" fill="#475569"/>
<rect x="78" y="103" width="4" height="37" fill="#475569"/>
<circle cx="30" cy="80" r="6" fill="#f59e0b"/>
<text x="14" y="70" font-size="10" fill="#f59e0b">S</text>
<line x1="36" y1="80" x2="78" y2="62" stroke="#f59e0b" stroke-width="1"/>
<line x1="36" y1="80" x2="78" y2="98" stroke="#f59e0b" stroke-width="1"/>
<text x="82" y="150" font-size="10" fill="#475569">双缝</text>
<line x1="82" y1="62" x2="208" y2="72" stroke="#2563eb" stroke-width="1"/>
<line x1="82" y1="98" x2="208" y2="88" stroke="#2563eb" stroke-width="1"/>
<line x1="208" y1="20" x2="208" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<text x="190" y="152" font-size="10" fill="#94a3b8">屏</text>
<line x1="204" y1="52" x2="214" y2="52" stroke="#2563eb" stroke-width="1"/>
<line x1="204" y1="108" x2="214" y2="108" stroke="#2563eb" stroke-width="1"/>
<text x="186" y="36" font-size="10" fill="#2563eb">Δy</text>
</svg>''',
"newtonring": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 60 88 A 60 42 0 0 1 180 88" fill="none" stroke="#2563eb" stroke-width="2"/>
<path d="M 60 88 A 45 30 0 0 1 180 88" fill="none" stroke="#7c3aed" stroke-width="2"/>
<path d="M 60 88 A 30 19 0 0 1 180 88" fill="none" stroke="#0ea5e9" stroke-width="2"/>
<line x1="30" y1="88" x2="210" y2="88" stroke="#475569" stroke-width="1.5" stroke-dasharray="4 3"/>
<rect x="30" y="92" width="180" height="10" fill="#e2e8f0" stroke="#94a3b8"/>
<text x="96" y="116" font-size="10" fill="#475569">平板玻璃</text>
<text x="70" y="140" font-size="10" fill="#7c3aed">明暗相间同心圆环</text>
</svg>''',
"singleslit": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 20 80 Q 60 80 80 80 Q 92 80 97 56 Q 102 80 108 80 Q 114 80 120 22 Q 126 80 132 80 Q 138 80 143 56 Q 148 80 160 80 Q 180 80 220 80" fill="none" stroke="#0d9488" stroke-width="2"/>
<line x1="80" y1="30" x2="80" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<line x1="160" y1="30" x2="160" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<text x="104" y="18" font-size="10" fill="#0d9488">主极大</text>
<text x="60" y="24" font-size="10" fill="#94a3b8">次极大</text>
<text x="30" y="150" font-size="10" fill="#64748b">sinc² 光强分布</text>
<text x="74" y="98" font-size="10" fill="#64748b">−λ/a</text>
<text x="156" y="98" font-size="10" fill="#64748b">λ/a</text>
</svg>''',
"grating": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<g stroke="#475569" stroke-width="4">
<line x1="70" y1="36" x2="70" y2="124"/>
<line x1="82" y1="36" x2="82" y2="124"/>
<line x1="94" y1="36" x2="94" y2="124"/>
<line x1="106" y1="36" x2="106" y2="124"/>
<line x1="118" y1="36" x2="118" y2="124"/>
</g>
<line x1="26" y1="80" x2="64" y2="80" stroke="#f59e0b" stroke-width="1.5"/>
<polygon points="64,80 55,75 55,85" fill="#f59e0b"/>
<text x="14" y="74" font-size="10" fill="#f59e0b">入射</text>
<line x1="124" y1="80" x2="212" y2="80" stroke="#0d9488" stroke-width="1.5"/>
<polygon points="212,80 203,75 203,85" fill="#0d9488"/>
<line x1="124" y1="80" x2="204" y2="34" stroke="#0d9488" stroke-width="1"/>
<line x1="124" y1="80" x2="204" y2="126" stroke="#0d9488" stroke-width="1"/>
<line x1="210" y1="16" x2="210" y2="144" stroke="#94a3b8" stroke-width="1.5"/>
<text x="190" y="28" font-size="10" fill="#0d9488">0级</text>
<text x="172" y="50" font-size="10" fill="#0d9488">+1</text>
<text x="172" y="140" font-size="10" fill="#0d9488">−1</text>
<text x="26" y="150" font-size="10" fill="#475569">d sinθ = kλ</text>
</svg>''',
"airy": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="78" cy="80" r="46" fill="none" stroke="#94a3b8" stroke-width="1"/>
<circle cx="78" cy="80" r="30" fill="none" stroke="#94a3b8" stroke-width="1"/>
<circle cx="78" cy="80" r="12" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5"/>
<text x="60" y="26" font-size="10" fill="#64748b">圆孔</text>
<line x1="132" y1="80" x2="178" y2="80" stroke="#94a3b8" stroke-width="1"/>
<polygon points="178,80 169,76 169,84" fill="#94a3b8"/>
<circle cx="200" cy="80" r="14" fill="#f0fdfa" stroke="#0d9488" stroke-width="1.5"/>
<circle cx="200" cy="80" r="28" fill="none" stroke="#14b8a6" stroke-width="1"/>
<circle cx="200" cy="80" r="40" fill="none" stroke="#5eead4" stroke-width="1"/>
<line x1="186" y1="80" x2="214" y2="80" stroke="#0d9488" stroke-width="1" stroke-dasharray="2 2"/>
<text x="174" y="128" font-size="10" fill="#0d9488">艾里斑</text>
<text x="180" y="40" font-size="10" fill="#64748b">D</text>
</svg>''',
"brewster": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="88" width="160" height="52" fill="#fff7ed" stroke="#c2410c" stroke-width="1.5"/>
<line x1="10" y1="88" x2="230" y2="88" stroke="#cbd5e1" stroke-width="1"/>
<line x1="30" y1="38" x2="110" y2="88" stroke="#c2410c" stroke-width="2"/>
<polygon points="110,88 99,80 104,76" fill="#c2410c"/>
<line x1="110" y1="88" x2="190" y2="138" stroke="#c2410c" stroke-width="2"/>
<polygon points="190,138 180,133 187,127" fill="#c2410c"/>
<line x1="110" y1="88" x2="182" y2="38" stroke="#2563eb" stroke-width="2"/>
<polygon points="182,38 174,48 180,52" fill="#2563eb"/>
<text x="118" y="80" font-size="10" fill="#64748b">iB</text>
<text x="140" y="48" font-size="10" fill="#2563eb">反射光全偏振</text>
<text x="150" y="120" font-size="10" fill="#c2410c">折射光部分偏振</text>
<text x="26" y="28" font-size="10" fill="#c2410c">自然光</text>
</svg>''',
"birefringence": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="4 3"/>
<rect x="70" y="38" width="100" height="84" fill="#fff7ed" stroke="#c2410c" stroke-width="1.5"/>
<line x1="14" y1="80" x2="70" y2="80" stroke="#ea580c" stroke-width="2"/>
<polygon points="70,80 61,75 61,85" fill="#ea580c"/>
<line x1="170" y1="80" x2="222" y2="58" stroke="#ef4444" stroke-width="2"/>
<polygon points="222,58 211,61 215,68" fill="#ef4444"/>
<line x1="170" y1="80" x2="222" y2="102" stroke="#3b82f6" stroke-width="2"/>
<polygon points="222,102 211,99 215,92" fill="#3b82f6"/>
<text x="78" y="30" font-size="10" fill="#c2410c">各向异性晶体</text>
<text x="182" y="54" font-size="10" fill="#ef4444">o光</text>
<text x="182" y="118" font-size="10" fill="#3b82f6">e光</text>
</svg>''',
"waveplate": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="14" y1="80" x2="226" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 30 80 Q 45 40 60 80 T 90 80" fill="none" stroke="#ef4444" stroke-width="2"/>
<path d="M 30 80 Q 45 120 60 80 T 90 80" fill="none" stroke="#2563eb" stroke-width="2"/>
<rect x="112" y="34" width="26" height="92" fill="#fff1f2" stroke="#be185d" stroke-width="1.5"/>
<text x="98" y="28" font-size="10" fill="#be185d">波片</text>
<path d="M 140 80 Q 160 50 180 80 T 210 80" fill="none" stroke="#db2777" stroke-width="2"/>
<path d="M 140 80 Q 160 110 180 80 T 210 80" fill="none" stroke="#db2777" stroke-width="1.2" stroke-dasharray="3 3"/>
<text x="20" y="72" font-size="10" fill="#ef4444">o</text>
<text x="20" y="120" font-size="10" fill="#2563eb">e</text>
<text x="160" y="140" font-size="10" fill="#be185d">δ = 2πΔn·d/λ</text>
</svg>''',
"fourier4f": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<rect x="30" y="50" width="6" height="60" fill="#dbeafe" stroke="#be185d"/>
<text x="20" y="44" font-size="10" fill="#be185d">物</text>
<path d="M 88 45 Q 78 80 88 115 Q 98 80 88 45 Z" fill="#dbeafe" stroke="#be185d" stroke-width="1.2"/>
<path d="M 152 45 Q 142 80 152 115 Q 162 80 152 45 Z" fill="#dbeafe" stroke="#be185d" stroke-width="1.2"/>
<rect x="116" y="60" width="10" height="40" fill="#fce7f3" stroke="#db2777" stroke-width="1.2"/>
<circle cx="121" cy="80" r="2.5" fill="#db2777"/>
<rect x="204" y="50" width="6" height="60" fill="#dbeafe" stroke="#be185d"/>
<text x="196" y="44" font-size="10" fill="#be185d">像</text>
<line x1="36" y1="66" x2="88" y2="73" stroke="#94a3b8" stroke-width="1"/>
<line x1="88" y1="73" x2="116" y2="80" stroke="#94a3b8" stroke-width="1"/>
<line x1="126" y1="80" x2="152" y2="73" stroke="#94a3b8" stroke-width="1"/>
<line x1="152" y1="73" x2="204" y2="66" stroke="#94a3b8" stroke-width="1"/>
<text x="100" y="52" font-size="10" fill="#db2777">频谱面</text>
<text x="100" y="102" font-size="10" fill="#db2777">空间滤波</text>
</svg>''',
"gaussianbeam": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="5 4"/>
<path d="M 30 80 Q 120 18 210 80" fill="none" stroke="#ec4899" stroke-width="1.6"/>
<path d="M 30 80 Q 120 142 210 80" fill="none" stroke="#ec4899" stroke-width="1.6"/>
<line x1="120" y1="30" x2="120" y2="130" stroke="#be185d" stroke-width="1"/>
<polygon points="120,30 116,40 124,40" fill="#be185d"/>
<polygon points="120,130 116,120 124,120" fill="#be185d"/>
<text x="124" y="46" font-size="10" fill="#be185d">2w0</text>
<text x="34" y="76" font-size="10" fill="#94a3b8">z</text>
<circle cx="120" cy="80" r="2.5" fill="#be185d"/>
<text x="60" y="150" font-size="10" fill="#64748b">高斯光束：束腰 w0 与双曲线包络</text>
</svg>''',
"lasercavity": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="40" y="40" width="8" height="80" fill="#a7f3d0" stroke="#059669" stroke-width="1.5"/>
<rect x="192" y="50" width="8" height="60" fill="#bfdbfe" stroke="#2563eb" stroke-width="1.5"/>
<text x="18" y="34" font-size="10" fill="#059669">全反镜</text>
<text x="180" y="34" font-size="10" fill="#2563eb">输出镜</text>
<rect x="80" y="55" width="70" height="50" fill="#fce7f3" stroke="#be185d" stroke-width="1.2"/>
<text x="90" y="84" font-size="10" fill="#be185d">增益介质</text>
<line x1="48" y1="70" x2="192" y2="70" stroke="#ef4444" stroke-width="1.5"/>
<polygon points="150,70 140,66 140,74" fill="#ef4444"/>
<line x1="192" y1="92" x2="48" y2="92" stroke="#ef4444" stroke-width="1.5"/>
<polygon points="90,92 100,88 100,96" fill="#ef4444"/>
<line x1="200" y1="80" x2="228" y2="80" stroke="#be185d" stroke-width="2"/>
<polygon points="228,80 218,75 218,85" fill="#be185d"/>
<text x="196" y="104" font-size="10" fill="#be185d">激光</text>
</svg>''',
"emwave": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="16" y1="80" x2="228" y2="80" stroke="#94a3b8" stroke-width="1"/>
<polygon points="228,80 218,76 218,84" fill="#94a3b8"/>
<text x="200" y="96" font-size="10" fill="#94a3b8">k</text>
<path d="M 30 80 Q 50 34 70 80 T 110 80 T 150 80 T 190 80" fill="none" stroke="#2563eb" stroke-width="1.8"/>
<path d="M 30 80 Q 50 126 70 80 T 110 80 T 150 80 T 190 80" fill="none" stroke="#7c3aed" stroke-width="1.4"/>
<g stroke="#2563eb" stroke-width="0.8">
<line x1="50" y1="80" x2="50" y2="46"/>
<line x1="90" y1="80" x2="90" y2="36"/>
<line x1="130" y1="80" x2="130" y2="46"/>
</g>
<g stroke="#7c3aed" stroke-width="0.8">
<line x1="50" y1="80" x2="50" y2="112"/>
<line x1="90" y1="80" x2="90" y2="124"/>
<line x1="130" y1="80" x2="130" y2="112"/>
</g>
<text x="24" y="34" font-size="10" fill="#2563eb">E</text>
<text x="24" y="128" font-size="10" fill="#7c3aed">B</text>
<text x="58" y="150" font-size="10" fill="#64748b">横波：E ⊥ B ⊥ k</text>
</svg>''',
"waveadd": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 20 34 Q 45 12 70 34 T 120 34 T 170 34 T 220 34" fill="none" stroke="#7c3aed" stroke-width="1.6"/>
<path d="M 20 76 Q 45 54 70 76 T 120 76 T 170 76 T 220 76" fill="none" stroke="#2563eb" stroke-width="1.6"/>
<path d="M 20 122 Q 45 96 70 122 T 120 122 T 170 122 T 220 122" fill="none" stroke="#0d9488" stroke-width="2"/>
<text x="186" y="26" font-size="10" fill="#7c3aed">E₁</text>
<text x="186" y="68" font-size="10" fill="#2563eb">E₂</text>
<text x="176" y="114" font-size="10" fill="#0d9488">E₁+E₂</text>
<text x="22" y="30" font-size="10" fill="#94a3b8">+</text>
<text x="40" y="150" font-size="10" fill="#64748b">线性叠加与波的独立传播</text>
</svg>''',
"coherence": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="14" y1="60" x2="226" y2="60" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 20 60 Q 30 36 40 60 T 60 60 T 80 60 T 100 60 T 120 60 T 140 60" fill="none" stroke="#7c3aed" stroke-width="1.6"/>
<path d="M 150 60 Q 158 44 166 60 T 182 60 T 198 60 T 214 60" fill="none" stroke="#a855f7" stroke-width="1.6"/>
<line x1="146" y1="30" x2="146" y2="84" stroke="#ef4444" stroke-width="1" stroke-dasharray="3 3"/>
<text x="52" y="24" font-size="10" fill="#7c3aed">一个波列</text>
<line x1="20" y1="94" x2="140" y2="94" stroke="#0891b2" stroke-width="1.4"/>
<polygon points="20,94 30,90 30,98" fill="#0891b2"/>
<polygon points="140,94 130,90 130,98" fill="#0891b2"/>
<text x="56" y="110" font-size="10" fill="#0891b2">相干长度 L_c</text>
<text x="34" y="134" font-size="10" fill="#64748b">L_c = λ²/Δλ</text>
</svg>''',
"rayleigh": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="28" cy="80" r="12" fill="#fbbf24"/>
<text x="14" y="112" font-size="10" fill="#b45309">阳光</text>
<line x1="40" y1="80" x2="120" y2="80" stroke="#f59e0b" stroke-width="2"/>
<g fill="#0e7490">
<circle cx="80" cy="80" r="3"/><circle cx="132" cy="58" r="3"/><circle cx="132" cy="104" r="3"/><circle cx="186" cy="80" r="3"/>
</g>
<line x1="80" y1="80" x2="106" y2="50" stroke="#3b82f6" stroke-width="1.4"/>
<polygon points="106,50 96,54 101,60" fill="#3b82f6"/>
<line x1="80" y1="80" x2="106" y2="110" stroke="#3b82f6" stroke-width="1.4"/>
<polygon points="106,110 96,106 101,100" fill="#3b82f6"/>
<text x="86" y="40" font-size="10" fill="#2563eb">蓝光散射</text>
<line x1="120" y1="80" x2="226" y2="80" stroke="#ef4444" stroke-width="2"/>
<polygon points="226,80 216,75 216,85" fill="#ef4444"/>
<text x="180" y="98" font-size="10" fill="#ef4444">红光透射</text>
<text x="82" y="140" font-size="10" fill="#64748b">分子尺度远小于波长</text>
<text x="24" y="150" font-size="10" fill="#64748b">⟹ 瑞利散射 I ∝ λ⁻⁴</text>
</svg>''',
"absorption": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="20" x2="34" y2="130" stroke="#475569" stroke-width="1.2"/>
<polygon points="34,14 30,24 38,24" fill="#475569"/>
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.2"/>
<polygon points="228,130 218,126 218,134" fill="#475569"/>
<text x="16" y="26" font-size="10" fill="#475569">I</text>
<text x="214" y="146" font-size="10" fill="#475569">l</text>
<path d="M 34 26 C 70 70 110 108 210 126" fill="none" stroke="#0891b2" stroke-width="2"/>
<line x1="34" y1="26" x2="72" y2="26" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="34" y1="90" x2="58" y2="90" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<circle cx="58" cy="90" r="2.5" fill="#0891b2"/>
<text x="62" y="86" font-size="10" fill="#0891b2">I₀/e</text>
<text x="104" y="56" font-size="10" fill="#0891b2">I = I₀ e⁻ᵅˡ</text>
<text x="86" y="150" font-size="10" fill="#64748b">朗伯-比尔定律</text>
</svg>''',
"dispersion": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="20" x2="34" y2="130" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.2"/>
<text x="14" y="26" font-size="10" fill="#475569">n</text>
<text x="206" y="146" font-size="10" fill="#475569">λ</text>
<path d="M 44 40 C 80 70 110 96 140 100" fill="none" stroke="#0891b2" stroke-width="2"/>
<path d="M 140 100 C 152 102 156 60 168 46" fill="none" stroke="#ef4444" stroke-width="2"/>
<path d="M 168 46 C 180 36 196 40 214 52" fill="none" stroke="#0891b2" stroke-width="2"/>
<line x1="150" y1="20" x2="150" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="52" y="120" font-size="10" fill="#0891b2">正常色散</text>
<text x="152" y="30" font-size="10" fill="#ef4444">反常色散</text>
<text x="174" y="120" font-size="10" fill="#0891b2">正常色散</text>
<text x="122" y="150" font-size="10" fill="#64748b">吸收带</text>
</svg>''',
"groupspeed": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 20 80 Q 60 26 100 80 Q 140 134 180 80 Q 200 54 224 80" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<path d="M 20 80 Q 30 60 40 80 T 60 80 T 80 80 T 100 80 T 120 80 T 140 80 T 160 80 T 180 80 T 200 80 T 220 80" fill="none" stroke="#0891b2" stroke-width="1.6"/>
<circle cx="100" cy="80" r="3" fill="#ef4444"/>
<polygon points="114,80 104,75 104,85" fill="#ef4444"/>
<text x="74" y="106" font-size="10" fill="#ef4444">v_g 波包</text>
<text x="146" y="62" font-size="10" fill="#0891b2">v_p 相位</text>
<text x="42" y="148" font-size="10" fill="#64748b">群速度与相速度色散</text>
</svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

CORE_FORMULAS = [
    ("反射定律", "\\theta_i = \\theta_r", "入射角等于反射角，入射线、反射线与法线共面"),
    ("折射定律", "n_1\\sin\\theta_1 = n_2\\sin\\theta_2", "斯涅尔定律，界面两侧折射角与折射率的关系"),
    ("费马原理", "\\delta\\int_A^B n\\,ds = 0", "光沿光程取极值的路径传播"),
    ("折射率", "n = \\frac{c}{v}", "介质折射率等于真空中光速与介质中光速之比"),
    ("全反射临界角", "\\sin\\theta_c = \\frac{n_2}{n_1}\\ (n_1>n_2)", "由光密介质射向光疏介质时的临界入射角"),
    ("棱镜最小偏向角", "n = \\frac{\\sin[(A+\\delta_m)/2]}{\\sin(A/2)}", "由最小偏向角与顶角测折射率"),
    ("球面镜成像公式", "\\frac{1}{u} + \\frac{1}{v} = \\frac{1}{f},\\quad f=\\frac{R}{2}", "凹/凸球面镜的物像关系"),
    ("球面折射成像", "\\frac{n_2}{v} - \\frac{n_1}{u} = \\frac{n_2-n_1}{R}", "近轴条件下单球面折射成像公式"),
    ("薄透镜公式", "\\frac{1}{u} + \\frac{1}{v} = \\frac{1}{f}", "薄透镜的物距、像距与焦距关系"),
    ("透镜制造者公式", "\\frac{1}{f} = (n-1)\\left(\\frac{1}{R_1}-\\frac{1}{R_2}\\right)", "由材料折射率与两曲面半径求焦距"),
    ("横向放大率", "M = \\frac{h'}{h} = \\frac{v}{u}", "像高与物高之比"),
    ("组合透镜焦距", "\\frac{1}{f} = \\frac{1}{f_1}+\\frac{1}{f_2}-\\frac{d}{f_1 f_2}", "相距 d 的两薄透镜组合的等效焦距"),
    ("放大镜角放大率", "\\Gamma = \\frac{25\\,\\text{cm}}{f}", "明视距离为 25 cm 时的角放大率"),
    ("显微镜放大率", "M = \\frac{L}{f_o}\\cdot\\frac{25\\,\\text{cm}}{f_e}", "物镜线放大率与目镜角放大率之积"),
    ("望远镜放大率", "\\Gamma = \\frac{f_o}{f_e}", "物镜焦距与目镜焦距之比"),
    ("照度", "E = \\frac{I\\cos\\theta}{r^2}", "点光源在受照面产生的照度"),
    ("光程", "\\Delta = \\sum_i n_i r_i", "几何路程与折射率乘积之和"),
    ("相干加强条件", "\\delta = k\\lambda\\ (k=0,\\pm1,\\dots)", "两相干光光程差为波长整数倍时加强"),
    ("双缝条纹间距", "\\Delta y = \\frac{\\lambda D}{d}", "杨氏双缝干涉相邻明纹间距"),
    ("双缝光强分布", "I = 4I_0\\cos^2\\frac{\\delta}{2}", "两等强度相干光叠加的光强"),
    ("等倾干涉光程差", "\\delta = 2nd\\cos\\theta + \\frac{\\lambda}{2}", "薄膜上下表面反射光的附加半波损失"),
    ("增透膜条件", "nd = \\frac{\\lambda}{4}", "单层减反射膜的厚度条件"),
    ("牛顿环暗环半径", "r_k = \\sqrt{kR\\lambda}", "第 k 级暗环半径与曲率半径关系"),
    ("劈尖条纹间距", "\\Delta x = \\frac{\\lambda}{2n\\theta}", "等厚干涉相邻条纹间距"),
    ("迈克尔逊干涉仪", "\\Delta d = N\\frac{\\lambda}{2}", "移动距离与条纹移动数的关系"),
    ("多光束干涉透射强度", "I_t = \\frac{I_0}{1+F\\sin^2(\\delta/2)}", "法布里-珀罗干涉仪透射光强"),
    ("精细度", "F = \\frac{4R}{(1-R)^2}", "由反射率 R 决定的干涉峰锐度参数"),
    ("相干长度", "L_c = \\frac{\\lambda^2}{\\Delta\\lambda}", "光谱宽度决定的最大可干涉光程差"),
    ("相干时间", "\\tau_c = \\frac{L_c}{c}", "相干长度对应的时间"),
    ("惠更斯-菲涅耳原理", "\\tilde{E}(P) = C\\int_\\Sigma \\frac{A(Q)}{r}e^{i(kr-\\omega t)}\\,dS", "波前上各次波源相干叠加求衍射场"),
    ("菲涅耳半波带半径", "r_k = \\sqrt{k\\lambda R}", "第 k 个半波带的半径"),
    ("单缝衍射光强", "I = I_0\\frac{\\sin^2\\alpha}{\\alpha^2},\\quad \\alpha=\\frac{\\pi a\\sin\\theta}{\\lambda}", "单缝夫琅禾费衍射的 sinc² 光强分布"),
    ("单缝暗纹条件", "a\\sin\\theta = k\\lambda\\ (k=\\pm1,\\pm2,\\dots)", "单缝衍射极小值位置"),
    ("艾里斑半角宽", "\\theta = 1.22\\frac{\\lambda}{D}", "圆孔衍射中央亮斑的角半径"),
    ("瑞利判据", "\\theta_R = 1.22\\frac{\\lambda}{D}", "两像点恰能分辨的最小角距离"),
    ("光栅方程", "d\\sin\\theta = k\\lambda\\ (k=0,\\pm1,\\dots)", "光栅主极大位置与波长关系"),
    ("光栅角色散", "\\frac{d\\theta}{d\\lambda} = \\frac{k}{d\\cos\\theta}", "光栅将波长分开的能力"),
    ("光栅分辨本领", "R = \\frac{\\lambda}{\\Delta\\lambda} = kN", "由级次 k 与刻线总数 N 决定"),
    ("布拉格公式", "2d\\sin\\theta = k\\lambda", "X 射线在晶面上的相干衍射条件"),
    ("波带片焦距", "f = \\frac{r_1^2}{\\lambda}", "菲涅耳波带片的焦点距离"),
    ("马吕斯定律", "I = I_0\\cos^2\\theta", "线偏振光通过检偏器的强度变化"),
    ("布儒斯特角", "\\tan\\theta_B = \\frac{n_2}{n_1}", "反射光成为完全偏振光时的入射角"),
    ("双折射相位差", "\\delta = \\frac{2\\pi}{\\lambda}(n_o-n_e)d", "o 光与 e 光通过晶体后的相位差"),
    ("四分之一波片厚度", "d = \\frac{\\lambda}{4|n_o-n_e|}", "将线偏振光变为圆偏振光的晶体厚度"),
    ("偏振度", "P = \\frac{I_p}{I_p+I_u}", "部分偏振光中偏振成分所占比例"),
    ("旋光角", "\\alpha = [\\alpha]_t\\,l\\,c", "溶液旋光角与浓度、光程的关系"),
    ("琼斯矢量", "\\mathbf{J} = \\begin{pmatrix} E_x \\\\ E_y \\end{pmatrix}", "用复数分量描述偏振态"),
    ("傅里叶变换", "F(u) = \\int_{-\\infty}^{\\infty} f(x)e^{-i2\\pi ux}\\,dx", "空间域到空间频域的变换"),
    ("夫琅禾费衍射场", "\\tilde{E}(u) = C\\,\\mathcal{F}\\{t(x)\\} \\Big|_{u=\\sin\\theta/\\lambda}", "衍射场为孔径函数的傅里叶变换"),
    ("阿贝成像公式", "I(x) = |\\mathcal{F}^{-1}\\{\\mathcal{F}\\{O\\}\\cdot H\\}|^2", "成像为频谱经滤波后的逆变换"),
    ("电磁波动方程", "\\nabla^2\\mathbf{E} = \\mu\\varepsilon\\frac{\\partial^2\\mathbf{E}}{\\partial t^2}", "无源介质中电场满足的波动方程"),
    ("单色平面波", "\\tilde{E} = E_0 e^{i(\\mathbf{k}\\cdot\\mathbf{r}-\\omega t+\\varphi_0)}", "单色平面波的复指数表示"),
    ("介质中光速", "v = \\frac{1}{\\sqrt{\\mu\\varepsilon}} = \\frac{c}{n}", "介质中光速由介电常数与磁导率决定"),
    ("光强与振幅", "I = \\frac{1}{2}c\\varepsilon_0 E_0^2 \\propto E_0^2", "光强正比于振幅平方"),
    ("相位差与光程差", "\\delta = \\frac{2\\pi}{\\lambda}\\Delta", "相位差与光程差的换算关系"),
    ("坡印廷矢量", "\\mathbf{S} = \\frac{1}{\\mu_0}\\mathbf{E}\\times\\mathbf{B}", "电磁场能流密度矢量"),
    ("辐射压力", "p_{rad} = \\frac{I}{c}\\ (\\text{吸收}),\\ \\frac{2I}{c}\\ (\\text{反射})", "光对物体表面施加的辐射压力"),
    ("空间相干宽度", "d_c \\approx \\frac{\\lambda z}{b}", "扩展光源在距离 z 处的横向相干宽度"),
    ("瑞利散射截面", "\\sigma_{sca} = \\frac{128\\pi^5 a^6}{3\\lambda^4}\\left|\\frac{m^2-1}{m^2+2}\\right|^2", "小颗粒瑞利散射截面与 λ⁻⁴ 定律"),
    ("拉曼频移", "\\nu_s = \\nu_0 \\pm \\Delta\\nu_{vib}", "分子振动引起的散射光频移"),
    ("布里渊频移", "\\Delta\\nu_B = \\pm\\frac{2nv_a}{\\lambda_0}\\sin\\frac{\\theta}{2}", "声波散射引起的多普勒频移"),
    ("朗伯-比尔定律", "I = I_0 e^{-\\alpha l} = I_0 10^{-\\varepsilon c l}", "吸收介质中光强的指数衰减"),
    ("复折射率", "\\tilde{n} = n + i\\kappa", "统一描述折射与吸收的复折射率"),
    ("吸收系数与消光系数", "\\alpha = \\frac{4\\pi\\kappa}{\\lambda_0}", "吸收系数由消光系数决定"),
    ("洛伦兹色散公式", "\\tilde{n}^2 = 1 + \\frac{Ne^2}{m\\varepsilon_0}\\cdot\\frac{1}{\\omega_0^2-\\omega^2-i\\gamma\\omega}", "经典振子模型的色散与吸收"),
    ("柯西公式", "n(\\lambda) = A + \\frac{B}{\\lambda^2} + \\frac{C}{\\lambda^4}", "透明区折射率的经验色散公式"),
    ("塞耳迈耶尔方程", "n^2(\\lambda) = 1 + \\sum_i \\frac{B_i\\lambda^2}{\\lambda^2-C_i}", "多共振叠加的精确色散公式"),
    ("群速度", "v_g = \\frac{d\\omega}{dk} = v_p - \\lambda\\frac{dv_p}{d\\lambda}", "波包传播速度与相速度的关系"),
    ("法拉第旋转角", "\\alpha = V B l", "磁场引起的偏振面旋转（法拉第效应）"),
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
"name": "1.1 光的直线传播与反射",
"color": "#2563eb",
"desc": "光线模型、反射定律与平面镜成像",
"items": [
{"id":"o1s1-1","name":"光的直线传播与光束","tags":["def","der"],"brief":"均匀介质中光沿直线传播，用光线描述。",
 "body": wrap(
   exa(p("<strong>例（小孔成像）：</strong>小孔成像中像高与物高之比由孔到屏与物到孔的距离之比决定：")+
   fml("\\frac{h'}{h}=\\frac{b}{a}")+
   p("该关系源于光的直线传播，是几何光学最朴素的验证。")+
   note(p("孔过大会因重叠而像模糊，孔过小则会因衍射而变模糊，存在最佳孔径。")))+
   defn("光线与光束",p("忽略光的波动性、用带箭头的直线表示光传播方向时称为<strong>光线</strong>。由一系列光线组成的集合称为光束，分为平行光束、发散光束与会聚光束。"))+
   der(p("<strong>由费马原理导出：</strong>光沿光程 $\\int n\\,ds$ 取极值的路径传播。在均匀介质中 $n$ 为常数，两点间最短路径为直线，其光程取极小值：")+
   fml("\\delta\\int_A^B n\\,ds = n\\,\\delta\\int_A^B ds = 0 \\implies \\int_A^B ds \\ \\text{取极值}","均匀介质中的光程极值")+
   p("故光在均匀各向同性介质中沿直线传播，这是几何光学的基础。"))+
   note(p("介质不均匀（如大气折射率随高度变化）时光线弯曲，形成海市蜃楼等现象。"))
 )},
{"id":"o1s1-2","name":"反射定律","tags":["thm","der"],"brief":"入射角等于反射角，三线共面。",
 "body": wrap(
   exa(p("<strong>例：</strong>入射角 $\\theta_i$ 由 $0°$ 增大时，反射率随角度变化，垂直入射时玻璃-空气界面反射率约 4%。")+
   fml("R_\\perp=\\left|\\frac{n_1\\cos\\theta_i-n_2\\cos\\theta_t}{n_1\\cos\\theta_i+n_2\\cos\\theta_t}\\right|^2")+
   note(p("反射定律是角反射器与潜望镜的基础：三面直角棱镜可把光线反向折回，广泛用于激光测距与自行车尾灯。")))+
   exa(p("<strong>例：</strong>入射角 $\\theta_i$ 由 $0°$ 增大时，反射率随角度变化，垂直入射时玻璃-空气界面反射率约 4%。")+
   fml("R_\\perp=\\left|\\frac{n_1\\cos\\theta_i-n_2\\cos\\theta_t}{n_1\\cos\\theta_i+n_2\\cos\\theta_t}\\right|^2")+
   note(p("反射定律是角反射器与潜望镜的基础：三面直角棱镜可把光线反向折回，广泛用于激光测距与自行车尾灯。")))+
   thm("光的反射定律",p("反射光线、入射光线与法线在同一平面内；反射光线与入射光线分居法线两侧；入射角等于反射角：")+
   fml("\\theta_i = \\theta_r")+
   p("反射光与入射光的频率相同，反射光强度由菲涅耳公式决定。"))+
   der(p("<strong>用费马原理证明：</strong>设光从 $A$ 点经镜面上 $P$ 点到达 $B$ 点。作 $B$ 关于镜面的对称点 $B'$，则 $PB=PB'$，光程 $AP+PB=AP+PB'$。")+
   fml("AP + PB' \\ \\text{最小} \\iff A,P,B'\\ \\text{共线}")+
   p("当 $A,P,B'$ 共线时，由几何关系可得入射角等于反射角，即 $\\theta_i=\\theta_r$；同时三线共面，反射定律得证。"))
 )},
{"id":"o1s1-3","name":"平面镜成像","tags":["der","exa"],"brief":"平面镜成等大正立的虚像。",
 "body": wrap(
   exa(p("<strong>例：</strong>平面镜绕垂直轴转过小角 $\\theta$ 时，反射光线转过 $2\\theta$：")+
   fml("\\Delta\\varphi = 2\\theta,\\qquad \\Delta y = 2\\theta L")+
   p("$L$ 为屏到镜的距离。微小角位移被放大为可观测的线位移，构成光学杠杆。")+
   note(p("该放大关系用于灵敏电流计、原子力显微镜的悬臂偏转检测与激光准直中的角度测量。")))+
   exa(p("<strong>例：</strong>平面镜绕垂直轴转过小角 $\\theta$ 时，反射光线转过 $2\\theta$：")+
   fml("\\Delta\\varphi = 2\\theta,\\qquad \\Delta y = 2\\theta L")+
   p("$L$ 为屏到镜的距离。微小角位移被放大为可观测的线位移，构成光学杠杆。")+
   note(p("该放大关系用于灵敏电流计、原子力显微镜的悬臂偏转检测与激光准直中的角度测量。")))+
   exa(p("<strong>问题：</strong>点光源 $S$ 位于平面镜前距离 $u$ 处，求其成像位置。"))+
   der(p("<strong>推导：</strong>取由 $S$ 发出的两条反射光线，反向延长交于 $S'$。设入射角为 $\\theta$，由反射定律反射角也为 $\\theta$。")+
   fml("\\frac{h}{u} = \\tan\\theta,\\quad \\frac{h}{v}=\\tan\\theta \\implies u = v")+
   p("任意两条反射光线的反向延长线都交于镜后与物等距的一点 $S'$。由于该点并非光线实际会聚，故为<strong>虚像</strong>。"))+
   note(p("平面镜成像特点：像与物关于镜面对称，大小相等、正立、左右互换，像距等于物距 $v=u$。"))
 )},
]},
{
"name": "1.2 折射与全反射",
"color": "#0ea5e9",
"desc": "折射定律、费马原理、全反射与棱镜色散",
"items": [
{"id":"o1s2-1","name":"折射定律与费马原理","tags":["thm","der"],"brief":"入射角正弦与折射角正弦之比为常数。",
 "fig":"refraction","figCap":"光在介质分界面上的反射与折射",
 "body": wrap(
   thm("折射定律（斯涅尔定律）",p("入射光线、折射光线与法线共面；入射角与折射角的正弦之比由两介质折射率决定：")+
   fml("n_1\\sin\\theta_1 = n_2\\sin\\theta_2")+
   p("其中 $n=c/v$ 为折射率，反射光与折射光能量分配由菲涅耳公式给出。"))+
   der(p("<strong>由费马原理推导：</strong>设界面为 $x$ 轴，光从介质 1 中 $A(0,h_1)$ 经界面上 $P(x,0)$ 到介质 2 中 $B(d,-h_2)$。总光程为：")+
   fml("L(x) = n_1\\sqrt{x^2+h_1^2} + n_2\\sqrt{(d-x)^2+h_2^2}")+
   p("令 $dL/dx=0$：")+
   fml("n_1\\frac{x}{\\sqrt{x^2+h_1^2}} = n_2\\frac{d-x}{\\sqrt{(d-x)^2+h_2^2}} \\implies n_1\\sin\\theta_1 = n_2\\sin\\theta_2")+
   p("这正是折射定律，说明光程取极值的路径即为实际光路。"))
 )},
{"id":"o1s2-2","name":"全反射与光纤","tags":["der","app"],"brief":"光从光密介质射向光疏介质时的全反射现象。",
 "body": wrap(
   exa(p("<strong>例（光纤数值孔径）：</strong>光在纤芯-包层界面全反射，能在光纤内传输的最大入射半角由数值孔径决定：")+
   fml("\\text{NA}=n_0\\sin\\theta_{\\max}=\\sqrt{n_1^2-n_2^2}")+
   p("取 $n_1=1.48$、$n_2=1.46$ 得 NA$\\approx0.24$，对应接收角约 $14°$。")+
   note(p("数值孔径越大越易耦合入光，但也增加模式色散；单模光纤需很小的芯径以只支持一个模式。")))+
   exa(p("<strong>例（光纤数值孔径）：</strong>光在纤芯-包层界面全反射，能在光纤内传输的最大入射半角由数值孔径决定：")+
   fml("\\text{NA}=n_0\\sin\\theta_{\\max}=\\sqrt{n_1^2-n_2^2}")+
   p("取 $n_1=1.48$、$n_2=1.46$ 得 NA$\\approx0.24$，对应接收角约 $14°$。")+
   note(p("数值孔径越大越易耦合入光，但也增加模式色散；单模光纤需很小的芯径以只支持一个模式。")))+
   defn("全反射",p("光从光密介质（$n_1$）射向光疏介质（$n_2<n_1$）时，若入射角大于某一临界角，折射光消失，光全部返回第一种介质。临界角满足：")+
   fml("\\sin\\theta_c = \\frac{n_2}{n_1}"))+
   der(p("<strong>推导：</strong>由折射定律 $n_1\\sin\\theta_1=n_2\\sin\\theta_2$，因 $n_2<n_1$，当 $\\theta_1$ 增大到使 $\\theta_2=90°$ 时：")+
   fml("n_1\\sin\\theta_c = n_2\\sin 90° = n_2 \\implies \\theta_c=\\arcsin\\frac{n_2}{n_1}")+
   p("当 $\\theta_1>\\theta_c$ 时方程无实数解，折射波成为沿界面衰减的隐失波，能量完全反射。"))+
   app(p("<strong>应用：</strong>光纤利用纤芯（高折射率）与包层（低折射率）界面的全反射导引光信号，实现低损耗长距离通信；此外还有全反射棱镜、内窥镜、激光准直等应用。"))
 )},
{"id":"o1s2-3","name":"棱镜与色散","tags":["der","app"],"brief":"棱镜使不同波长光偏折不同形成色散。",
 "body": wrap(
   exa(p("<strong>例：</strong>等边棱镜 $A=60°$，测得某波长最小偏向角 $\\delta_m=51.0°$，求折射率：")+
   fml("n=\\frac{\\sin[(60°+51.0°)/2]}{\\sin(30°)}=\\frac{\\sin 55.5°}{0.5}\\approx 1.65")+
   p("色散本领由角色散 $\\frac{d\\delta}{d\\lambda}$ 描述，波长越短偏向角越大，故紫光偏折最多。")+
   note(p("棱镜色散随波长非线性变化，红外与紫外波段常改用光栅；棱镜也在激光腔内作色散与调谐元件。")))+
   exa(p("<strong>例：</strong>等边棱镜 $A=60°$，测得某波长最小偏向角 $\\delta_m=51.0°$，求折射率：")+
   fml("n=\\frac{\\sin[(60°+51.0°)/2]}{\\sin(30°)}=\\frac{\\sin 55.5°}{0.5}\\approx 1.65")+
   p("色散本领由角色散 $\\frac{d\\delta}{d\\lambda}$ 描述，波长越短偏向角越大，故紫光偏折最多。")+
   note(p("棱镜色散随波长非线性变化，红外与紫外波段常改用光栅；棱镜也在激光腔内作色散与调谐元件。")))+
   defn("棱镜与偏向角",p("棱镜由两个折射面组成，顶角为 $A$。单色光通过棱镜后出射方向相对入射方向偏折，偏向角记为 $\\delta$。"))+
   der(p("<strong>最小偏向角与折射率：</strong>由几何关系 $\\delta=(\\theta_1-\\theta_1')+(\\theta_2-\\theta_2')$ 及 $\\theta_1'+\\theta_2'=A$ 得 $\\delta=\\theta_1+\\theta_2-A$。当光路对称（$\\theta_1=\\theta_2$）时偏向角最小 $\\delta_m$，此时：")+
   fml("\\theta_1=\\frac{A+\\delta_m}{2},\\quad \\theta_1'=\\frac{A}{2}")+
   p("代入折射定律得：")+
   fml("n = \\frac{\\sin[(A+\\delta_m)/2]}{\\sin(A/2)}")+
   p("由于材料折射率随波长变化 $n=n(\\lambda)$（色散），不同颜色的光偏向角不同，白光通过棱镜后展开成光谱。"))+
   app(p("<strong>应用：</strong>棱镜光谱仪、棱镜摄谱仪用于分光；棱镜亦可作为反射镜实现 90°、180° 光路转折。"))
 )},
]},
{
"name": "1.3 球面镜与球面折射",
"color": "#3b82f6",
"desc": "球面镜成像公式与单球面折射成像",
"items": [
{"id":"o1s3-1","name":"球面镜成像公式","tags":["der","thm"],"brief":"凹面镜与凸面镜的物像关系。",
 "body": wrap(
   exa(p("<strong>例：</strong>凹面镜半径 $R=40\\,\\text{cm}$，物在镜前 $60\\,\\text{cm}$ 处，求像距与放大率：")+
   fml("f=\\frac{R}{2}=20\\,\\text{cm},\\quad \\frac{1}{60}+\\frac{1}{v}=\\frac{1}{20}\\Rightarrow v=30\\,\\text{cm}")+
   fml("M=-\\frac{v}{u}=-0.5","倒立缩小实像")+
   note(p("当物移到焦点以内（$u<f$）时 $v<0$，成放大正立虚像，这正是凹面镜作化妆镜与反射式望远镜的原因。")))+
   exa(p("<strong>例：</strong>凹面镜半径 $R=40\\,\\text{cm}$，物在镜前 $60\\,\\text{cm}$ 处，求像距与放大率：")+
   fml("f=\\frac{R}{2}=20\\,\\text{cm},\\quad \\frac{1}{60}+\\frac{1}{v}=\\frac{1}{20}\\Rightarrow v=30\\,\\text{cm}")+
   fml("M=-\\frac{v}{u}=-0.5","倒立缩小实像")+
   note(p("当物移到焦点以内（$u<f$）时 $v<0$，成放大正立虚像，这正是凹面镜作化妆镜与反射式望远镜的原因。")))+
   thm("球面镜成像公式",p("近轴条件下，球面镜的物距 $u$、像距 $v$ 与焦距 $f$ 满足：")+
   fml("\\frac{1}{u} + \\frac{1}{v} = \\frac{1}{f},\\quad f=\\frac{R}{2}")+
   p("凹面镜 $f>0$，凸面镜 $f<0$。"))+
   der(p("<strong>推导：</strong>设物高 $h$ 位于主轴上 $u$ 处，经顶点 $O$ 附近近轴光线成像于 $v$ 处，像高 $h'$。利用近轴近似 $\\sin\\theta\\approx\\tan\\theta\\approx\\theta$，由两个三角形相似关系：")+
   fml("\\frac{h}{u-O} \\approx \\frac{h'}{O-v}")+
   p("又由曲率中心处的相似关系 $\\frac{h}{R}=-\\frac{h'}{R-2f}$，联立消去 $h,h'$ 并整理得：")+
   fml("\\frac{1}{u}+\\frac{1}{v}=\\frac{2}{R}=\\frac{1}{f}")+
   p("符号规则：凹面镜曲率中心在镜前，$R>0$。"))+
   note(p("放大率 $M=-v/u$，负号表示倒立实像或正立虚像的区别。"))
 )},
{"id":"o1s3-2","name":"球面折射成像","tags":["der","thm"],"brief":"单球面折射的近轴成像公式。",
 "body": wrap(
   thm("单球面折射公式",p("近轴光线下，两种介质折射率分别为 $n_1,n_2$，界面曲率半径为 $R$，则：")+
   fml("\\frac{n_2}{v} - \\frac{n_1}{u} = \\frac{n_2-n_1}{R}"))+
   der(p("<strong>推导：</strong>利用近轴光线的光程相等原理。物点 $O$ 发出光线经球面 $P$ 点折射到像点 $I$，两条近轴路径光程相等。设物距 $u$、像距 $v$：")+
   fml("n_1\\sqrt{u^2+y^2} + n_2\\sqrt{v^2+y^2} \\approx n_1 u + n_2 v + \\frac{y^2}{2}\\left(\\frac{n_1}{u}+\\frac{n_2}{v}\\right)")+
   p("考虑球面弯曲带来的附加光程，令不同 $y$ 的光程相等（消去 $y^2$ 项）得：")+
   fml("\\frac{n_1}{u} + \\frac{n_2}{v} = \\frac{n_2-n_1}{R}")+
   p("采用物距 $u<0$ 的符号约定即得标准形式 $\\frac{n_2}{v}-\\frac{n_1}{u}=\\frac{n_2-n_1}{R}$。"))+
   note(p("两次应用球面折射公式即可得到厚透镜乃至整个共轴球面系统的成像公式。"))
 )},
]},
{
"name": "1.4 薄透镜与成像",
"color": "#2563eb",
"desc": "薄透镜公式、透镜制造者公式与组合透镜",
"items": [
{"id":"o1s4-1","name":"薄透镜公式","tags":["thm","der"],"brief":"薄透镜的物像关系与放大率。",
 "fig":"lens","figCap":"凸透镜成像光路",
 "body": wrap(
   exa(p("<strong>例：</strong>凸透镜 $f=10\\,\\text{cm}$，物在 $15\\,\\text{cm}$ 处：")+
   fml("\\frac{1}{15}+\\frac{1}{v}=\\frac{1}{10}\\Rightarrow v=30\\,\\text{cm},\\quad M=\\frac{v}{u}=2")+
   p("成倒立放大实像，可用屏接收。光焦度 $\\Phi=1/f=10\\,\\text{D}$（屈光度）。")+
   note(p("物在焦点以内时 $v<0$，成放大正立虚像，这就是放大镜的成像方式。")))+
   exa(p("<strong>例：</strong>凸透镜 $f=10\\,\\text{cm}$，物在 $15\\,\\text{cm}$ 处：")+
   fml("\\frac{1}{15}+\\frac{1}{v}=\\frac{1}{10}\\Rightarrow v=30\\,\\text{cm},\\quad M=\\frac{v}{u}=2")+
   p("成倒立放大实像，可用屏接收。光焦度 $\\Phi=1/f=10\\,\\text{D}$（屈光度）。")+
   note(p("物在焦点以内时 $v<0$，成放大正立虚像，这就是放大镜的成像方式。")))+
   thm("薄透镜公式",p("对于厚度可忽略的薄透镜，物距 $u$、像距 $v$ 与焦距 $f$ 满足：")+
   fml("\\frac{1}{u} + \\frac{1}{v} = \\frac{1}{f}")+
   p("横向放大率 $M=v/u$。凸透镜 $f>0$（会聚），凹透镜 $f<0$（发散）。"))+
   der(p("<strong>推导：</strong>把薄透镜视为两个紧靠的单球面折射面（半径 $R_1,R_2$，介质折射率 $n$，两侧为空气）。对第一面：")+
   fml("\\frac{n}{v_1} - \\frac{1}{u} = \\frac{n-1}{R_1}")+
   p("对第二面，物距为 $-v_1$：")+
   fml("\\frac{1}{v} - \\frac{n}{v_1} = \\frac{1-n}{R_2}")+
   p("两式相加消去中间量 $v_1$：")+
   fml("\\frac{1}{v}-\\frac{1}{u} = (n-1)\\left(\\frac{1}{R_1}-\\frac{1}{R_2}\\right)=\\frac{1}{f}")+
   p("换成物距正号约定即为薄透镜公式。"))
 )},
{"id":"o1s4-2","name":"透镜制造者公式","tags":["der","app"],"brief":"由几何与材料参数确定透镜焦距。",
 "body": wrap(
   exa(p("<strong>例：</strong>双凸透镜 $n=1.52$、$R_1=20\\,\\text{cm}$、$R_2=-30\\,\\text{cm}$：")+
   fml("\\frac{1}{f}=(1.52-1)\\left(\\frac{1}{0.20}-\\frac{1}{-0.30}\\right)=0.52\\times8.33\\approx4.33\\,\\text{m}^{-1}")+
   p("故 $f\\approx23\\,\\text{cm}$，即约 $+4.3\\,\\text{D}$。")+
   note(p("同种玻璃，凸面越弯（半径越小）光焦度越大；把透镜浸入折射率相近的液体中会显著削弱会聚。")))+
   defn("焦距的构成",p("透镜焦距由材料折射率 $n$ 与两表面曲率半径 $R_1,R_2$ 共同决定。"))+
   der(p("<strong>推导：</strong>在薄透镜公式推导中，令 $u\\to\\infty$（平行光入射）则 $v\\to f$，于是：")+
   fml("\\frac{1}{f} = (n-1)\\left(\\frac{1}{R_1}-\\frac{1}{R_2}\\right)")+
   p("凸透镜（双凸）$R_1>0,R_2<0$，$f>0$；凹透镜则 $f<0$。因 $n=n(\\lambda)$，同一透镜对不同波长焦距不同，即<strong>色差</strong>。"))+
   app(p("<strong>应用：</strong>设计消色差透镜组（正负透镜组合），使两个波长的焦点重合；眼镜片度数 $\\Phi=1/f$（屈光度 D，$f$ 以米计）。"))+
   note(p("当 $n$ 与周围介质折射率接近时透镜失去会聚能力，故透镜在液体中焦距会显著改变。"))
 )},
{"id":"o1s4-3","name":"组合透镜","tags":["der"],"brief":"多个薄透镜组合的等效焦距与成像。",
 "body": wrap(
   exa(p("<strong>例：</strong>两透镜 $f_1=10\\,\\text{cm}$、$f_2=20\\,\\text{cm}$，相距 $d=5\\,\\text{cm}$：")+
   fml("\\frac{1}{f}=\\frac{1}{10}+\\frac{1}{20}-\\frac{5}{10\\times20}=0.1+0.05-0.025=0.125\\,\\text{cm}^{-1}")+
   p("故组合焦距 $f=8\\,\\text{cm}$，比任一单透镜都短。")+
   note(p("当 $d=f_1+f_2$ 时两透镜构成无焦系统，用于望远镜与扩束镜；$d=0$ 时光焦度相加。")))+
   defn("组合系统",p("两个焦距为 $f_1,f_2$ 的薄透镜相距 $d$ 放置，构成共轴组合系统。"))+
   der(p("<strong>推导：</strong>第一透镜使物 $u$ 成像于 $v_1$（$\\frac{1}{v_1}=\\frac{1}{f_1}-\\frac{1}{u}$）。该像作为第二透镜的物，物距为 $u_2=d-v_1$（透过后位置为负）：")+
   fml("\\frac{1}{u_2}+\\frac{1}{v}=\\frac{1}{f_2}")+
   p("消去 $v_1$ 并令总光焦度 $\\Phi=1/f$、$\\Phi_i=1/f_i$，得到等效焦距：")+
   fml("\\frac{1}{f} = \\frac{1}{f_1}+\\frac{1}{f_2}-\\frac{d}{f_1 f_2}")+
   p("当 $d=0$（紧贴）时简化为 $1/f=1/f_1+1/f_2$，光焦度可加。"))+
   note(p("用光焦度表示更方便：$\\Phi=\\Phi_1+\\Phi_2-d\\,\\Phi_1\\Phi_2$。"))
 )},
]},
{
"name": "1.5 光学仪器",
"color": "#0ea5e9",
"desc": "放大镜、显微镜与望远镜的放大原理",
"items": [
{"id":"o1s5-1","name":"放大镜","tags":["der","app"],"brief":"凸透镜作为放大镜的角放大率。",
 "body": wrap(
   defn("角放大率",p("仪器角放大率定义为像对人眼的张角 $\\omega'$ 与物在明视距离处直接观察时张角 $\\omega$ 之比：$\\Gamma=\\omega'/\\omega$。明视距离 $D=25\\,\\text{cm}$。"))+
   der(p("<strong>推导：</strong>物置于透镜焦平面附近。像成在明视距离 $D$ 处时，物距 $u$ 满足 $\\frac{1}{u}-\\frac{1}{D}=\\frac{1}{f}$，解得 $u=\\frac{Df}{D+f}$，像张角 $\\omega'\\approx\\frac{h}{u}$，而 $\\omega\\approx h/D$，故：")+
   fml("\\Gamma = \\frac{\\omega'}{\\omega}=\\frac{D}{u}=\\frac{D+f}{f}=1+\\frac{D}{f}")+
   p("若物恰在焦点上（像在无穷远），则 $\\Gamma=D/f=25/f$。"))+
   app(p("<strong>应用：</strong>放大镜焦距越短放大率越高，但短焦透镜像差大、工作距离小，通常 $\\Gamma<10$。"))
 )},
{"id":"o1s5-2","name":"显微镜","tags":["der","app"],"brief":"物镜与目镜两次放大。",
 "body": wrap(
   exa(p("<strong>例：</strong>物镜 $f_o=4\\,\\text{mm}$、数值孔径 NA$=0.65$，目镜 $f_e=25\\,\\text{mm}$，光学筒长 $160\\,\\text{mm}$：")+
   fml("M_o=\\frac{160}{4}=40,\\quad \\Gamma_e=\\frac{250}{25}=10,\\quad M=400")+
   p("分辨极限 $\\delta=0.61\\lambda/\\text{NA}$。")+
   note(p("油浸物镜以 $n\\approx1.5$ 的介质填充物镜与标本间隙，把 NA 提高到 1.3 以上，显著提升分辨本领。")))+
   exa(p("<strong>例：</strong>物镜 $f_o=4\\,\\text{mm}$、数值孔径 NA$=0.65$，目镜 $f_e=25\\,\\text{mm}$，光学筒长 $160\\,\\text{mm}$：")+
   fml("M_o=\\frac{160}{4}=40,\\quad \\Gamma_e=\\frac{250}{25}=10,\\quad M=400")+
   p("分辨极限 $\\delta=0.61\\lambda/\\text{NA}$。")+
   note(p("油浸物镜以 $n\\approx1.5$ 的介质填充物镜与标本间隙，把 NA 提高到 1.3 以上，显著提升分辨本领。")))+
   defn("显微镜结构",p("显微镜由短焦物镜与目镜组成，物镜成放大实像，再由目镜放大为虚像供眼睛观察。"))+
   der(p("<strong>推导：</strong>物镜将物放在略超焦距处，成放大倒立实像，放大率 $M_o=L/f_o$（$L$ 为光学筒长）。目镜作放大镜使用，角放大率 $\\Gamma_e=D/f_e$。总放大率为两者之积：")+
   fml("M = M_o\\cdot\\Gamma_e = \\frac{L}{f_o}\\cdot\\frac{D}{f_e}")+
   p("取 $D=25\\,\\text{cm}$，$L\\approx16\\,\\text{cm}$。"))+
   app(p("<strong>应用：</strong>显微镜分辨率受限于物镜数值孔径 $\\text{NA}=n\\sin U$，$\\delta=0.61\\lambda/\\text{NA}$；油浸物镜可提高 NA 从而提升分辨本领。"))
 )},
{"id":"o1s5-3","name":"望远镜","tags":["der","app"],"brief":"物镜与目镜组成无焦系统。",
 "body": wrap(
   exa(p("<strong>例：</strong>物镜 $f_o=1200\\,\\text{mm}$、目镜 $f_e=25\\,\\text{mm}$：")+
   fml("\\Gamma=\\frac{f_o}{f_e}=\\frac{1200}{25}=48")+
   p("角放大率约 48 倍；物镜口径 $D=100\\,\\text{mm}$ 时分辨角 $\\theta_R=1.22\\lambda/D\\approx1.3''$。")+
   note(p("有效放大率上限约为物镜口径（以毫米计）的 2 倍，超过则不增加信息量，只放大模糊。")))+
   defn("开普勒望远镜",p("物镜焦距长、目镜焦距短，两者焦点重合使系统无焦，平行光入射平行光出射。"))+
   der(p("<strong>推导：</strong>远处物体对物镜张角 $\\omega\\approx h/f_o'$（$h$ 为物镜焦面上像高）。该像经目镜后对人眼张角 $\\omega'\\approx h/f_e$。故角放大率：")+
   fml("\\Gamma = \\frac{\\omega'}{\\omega} = \\frac{f_o}{f_e}")+
   p("物镜口径 $D$ 决定分辨角 $\\theta_R=1.22\\lambda/D$ 与集光能力，与放大率无关。"))+
   app(p("<strong>应用：</strong>天文望远镜追求大口径；伽利略望远镜以凹透镜作目镜成正立虚像；望远镜倍率过高会使像变暗、视场变小。"))
 )},
]},
{
"name": "1.6 光阑与光度学",
"color": "#3b82f6",
"desc": "光阑与孔径的作用、光度学基本量",
"items": [
{"id":"o1s6-1","name":"光阑与孔径","tags":["def","der"],"brief":"限制光束与视场的元件。",
 "body": wrap(
   defn("光阑与孔径",p("<strong>孔径光阑</strong>限制进入系统的光束口径，决定像的亮度与分辨率；<strong>视场光阑</strong>限制成像范围。孔径光阑在物方的像称为入射光瞳，在像方的像称为出射光瞳。"))+
   der(p("<strong>相对孔径与 f 数：</strong>物镜口径 $D$ 与焦距 $f$ 之比 $D/f$ 称为相对孔径。像面照度与相对孔径平方成正比：")+
   fml("E \\propto \\left(\\frac{D}{f}\\right)^2 = \\frac{1}{F^2}","f 数 $F=f/D$")+
   p("f 数（光圈数）$F=f/D$ 越小，进光量越大，像越亮。"))+
   note(p("孔径光阑还决定景深与衍射极限：衍射斑角半径 $\\theta=1.22\\lambda/D$，口径越大分辨越高。"))
 )},
{"id":"o1s6-2","name":"光度学基础","tags":["def","der"],"brief":"光通量、发光强度、亮度与照度。",
 "body": wrap(
   exa(p("<strong>例：</strong>发光强度 $I=100\\,\\text{cd}$ 的点光源，求距其 $2\\,\\text{m}$ 处正对表面的照度：")+
   fml("E=\\frac{I\\cos\\theta}{r^2}=\\frac{100\\times1}{2^2}=25\\,\\text{lx}")+
   p("若入射角变为 $60°$，则 $E\\approx12.5\\,\\text{lx}$，减少一半。")+
   note(p("照明设计中需综合考虑光源强度、距离与入射方向，并避免眩光与照度不均。")))+
   exa(p("<strong>例：</strong>发光强度 $I=100\\,\\text{cd}$ 的点光源，求距其 $2\\,\\text{m}$ 处正对表面的照度：")+
   fml("E=\\frac{I\\cos\\theta}{r^2}=\\frac{100\\times1}{2^2}=25\\,\\text{lx}")+
   p("若入射角变为 $60°$，则 $E\\approx12.5\\,\\text{lx}$，减少一半。")+
   note(p("照明设计中需综合考虑光源强度、距离与入射方向，并避免眩光与照度不均。")))+
   defn("四个基本量",p("<strong>光通量</strong> $\\Phi$（流明 lm）表示辐射功率按人眼视见函数加权后的量；<strong>发光强度</strong> $I=\\Phi/\\Omega$（坎德拉 cd）；<strong>亮度</strong> $L=I/(dS\\cos\\theta)$；<strong>照度</strong> $E=\\Phi/S$（勒克斯 lx）。"))+
   der(p("<strong>照度与距离的关系：</strong>点光源发光强度 $I$，在距其 $r$、法线与光线成 $\\theta$ 的面上，立体角 $d\\Omega=dS\\cos\\theta/r^2$：")+
   fml("E = \\frac{d\\Phi}{dS} = \\frac{I\\,d\\Omega}{dS} = \\frac{I\\cos\\theta}{r^2}")+
   p("即照度遵循平方反比定律，并随入射角余弦衰减。"))+
   note(p("亮度守恒：理想光学系统像的亮度不超过物的亮度，故放大像必然变暗。"))
 )},
]},
]

ch2_sections = [
{
"name": "2.1 光的电磁本性",
"color": "#7c3aed",
"desc": "电磁波性质、麦克斯韦波动方程、平面波解与光速",
"items": [
{"id":"o2s1-1","name":"光的电磁波性质","tags":["def","der"],"brief":"光是横波，由交变的电场与磁场构成。",
 "fig":"emwave","figCap":"单色平面电磁波：E ⊥ B ⊥ k，电场与磁场同相位",
 "body": wrap(
   defn("光波",p("光是一种电磁波：相互垂直的电场 $\\mathbf{E}$ 与磁场 $\\mathbf{B}$ 随时间与空间周期变化，在真空中以 $c$ 传播。可见光波长约 $380\\sim760\\,\\text{nm}$，频率约 $4\\times10^{14}\\sim8\\times10^{14}\\,\\text{Hz}$，只占电磁波谱的极窄一段。"))+
   der(p("<strong>横波性的导出：</strong>在无源区 $\\rho=0$、$\\mathbf{J}=0$，取平面单色波 $\\mathbf{E}=\\mathbf{E}_0e^{i(\\mathbf{k}\\cdot\\mathbf{r}-\\omega t)}$，由 $\\nabla\\cdot\\mathbf{E}=0$ 得：")+
   fml("i\\mathbf{k}\\cdot\\mathbf{E}_0=0\\ \\Rightarrow\\ \\mathbf{k}\\perp\\mathbf{E},\\qquad \\mathbf{k}\\perp\\mathbf{B}")+
   p("电场与磁场均垂直于传播方向，故光波为横波；再由 $\\nabla\\times\\mathbf{E}=-\\partial\\mathbf{B}/\\partial t$ 得 $\\mathbf{B}$ 与 $\\mathbf{E}$ 同相位并互相垂直，且 $E=cB$。"))+
   note(p("横波性正是偏振现象存在的根本前提；纵波（如声波）不存在偏振态。"))
 )},
{"id":"o2s1-2","name":"麦克斯韦方程组与波动方程","tags":["thm","der"],"brief":"由麦克斯韦方程组导出电磁波动方程。",
 "body": wrap(
   thm("电磁波动方程",p("在无源均匀介质中，电场与磁场分别满足齐次波动方程：")+
   fml("\\nabla^2\\mathbf{E}=\\mu\\varepsilon\\frac{\\partial^2\\mathbf{E}}{\\partial t^2},\\qquad \\nabla^2\\mathbf{B}=\\mu\\varepsilon\\frac{\\partial^2\\mathbf{B}}{\\partial t^2}")+
   p("方程预言了以速度 $v=1/\\sqrt{\\mu\\varepsilon}$ 传播的电磁波。"))+
   der(p("<strong>推导：</strong>对法拉第定律 $\\nabla\\times\\mathbf{E}=-\\partial\\mathbf{B}/\\partial t$ 取旋度，并利用 $\\nabla\\times(\\nabla\\times\\mathbf{E})=\\nabla(\\nabla\\cdot\\mathbf{E})-\\nabla^2\\mathbf{E}$，在无源区 $\\nabla\\cdot\\mathbf{E}=0$：")+
   fml("\\nabla\\times(\\nabla\\times\\mathbf{E})=-\\frac{\\partial}{\\partial t}(\\nabla\\times\\mathbf{B})=-\\mu\\varepsilon\\frac{\\partial^2\\mathbf{E}}{\\partial t^2}")+
   p("与恒等式联立即得电场波动方程；对 $\\nabla\\times\\mathbf{B}$ 重复同样步骤可得磁场方程，二者结构完全一致，说明 $\\mathbf{E}$、$\\mathbf{B}$ 以同一速度传播。"))+
   note(p("麦克斯韦由此算得 $c=1/\\sqrt{\\mu_0\\varepsilon_0}\\approx3\\times10^8\\,\\text{m/s}$，与实测光速吻合，从而确认光就是电磁波。"))
 )},
{"id":"o2s1-3","name":"平面波解与单色波","tags":["der","exa"],"brief":"单色平面波的复数表示与实部意义。",
 "body": wrap(
   der(p("<strong>平面波解：</strong>波动方程最简单的解为单色平面波，复数形式为：")+
   fml("\\tilde{E}(\\mathbf{r},t)=E_0e^{i(\\mathbf{k}\\cdot\\mathbf{r}-\\omega t+\\varphi_0)}")+
   p("其中 $k=2\\pi/\\lambda$ 为波数，$\\omega=2\\pi\\nu$ 为角频率，等相位面 $\\mathbf{k}\\cdot\\mathbf{r}=\\text{const}$ 为平面。真实场取其实部：")+
   fml("E(\\mathbf{r},t)=E_0\\cos(\\mathbf{k}\\cdot\\mathbf{r}-\\omega t+\\varphi_0)")+
   p("复指数表示使相位运算化为乘法，便于处理叠加、干涉与衍射问题。"))+
   exa(p("<strong>例：</strong>He-Ne 激光 $\\lambda=632.8\\,\\text{nm}$，则 $k=2\\pi/\\lambda\\approx9.93\\times10^6\\,\\text{m}^{-1}$，$\\omega=2\\pi c/\\lambda\\approx2.98\\times10^{15}\\,\\text{s}^{-1}$。")+
   note(p("球面波解为 $\\tilde{E}=\\frac{A}{r}e^{i(kr-\\omega t)}$，振幅随 $1/r$ 衰减以保持能流守恒。")))
 )},
{"id":"o2s1-4","name":"光速与折射率","tags":["der","def"],"brief":"介质中光速与折射率的关系。",
 "body": wrap(
   der(p("<strong>推导：</strong>介质中电磁波速度由介电常数与磁导率决定：")+
   fml("v=\\frac{1}{\\sqrt{\\mu\\varepsilon}}=\\frac{c}{n},\\qquad n=\\sqrt{\\mu_r\\varepsilon_r}\\approx\\sqrt{\\varepsilon_r}")+
   p("对非磁性介质 $\\mu_r\\approx1$，折射率主要由相对介电常数决定。频率 $\\nu$ 在界面两侧不变，故介质中波长变短：")+
   fml("\\lambda_n=\\frac{v}{\\nu}=\\frac{\\lambda_0}{n}"))+
   defn("折射率",p("$n=c/v$ 描述介质对光的减速程度，是真空中光速与介质中相速之比，也是表征介质光学性质的基本参数。"))+
   note(p("色散使 $n=n(\\lambda)$；在吸收带附近折射率出现反常变化，须用复折射率 $\\tilde{n}=n+i\\kappa$ 描述。"))
 )},
]},
{
"name": "2.2 光强与光程",
"color": "#8b5cf6",
"desc": "光强与振幅、单色波与波列、相位与光程、光程差",
"items": [
{"id":"o2s2-1","name":"光强与振幅","tags":["der"],"brief":"光强正比于振幅平方。",
 "body": wrap(
   der(p("<strong>推导：</strong>光频极高（约 $10^{14}\\,\\text{Hz}$），探测器只能响应时间平均值。能流密度大小为 $S=c\\varepsilon_0E^2$，取时间平均：")+
   fml("I=\\langle S\\rangle=c\\varepsilon_0\\langle E^2\\rangle=\\frac{1}{2}c\\varepsilon_0E_0^2\\propto E_0^2")+
   p("故<strong>光强正比于振幅平方</strong>。两波叠加时须先叠加振幅再求平方，交叉项即干涉项。"))+
   exa(p("<strong>例：</strong>强度分别为 $I_1$、$I_2$ 的两相干光叠加，$I=I_1+I_2+2\\sqrt{I_1I_2}\\cos\\delta$；不相干时交叉项时间平均为零，$I=I_1+I_2$。"))+
   note(p("计算中常省略常数，直接写 $I=A^2$，此时振幅以相对单位计。"))
 )},
{"id":"o2s2-2","name":"单色波与波列","tags":["def","der"],"brief":"实际光波由有限长波列组成。",
 "body": wrap(
   defn("波列",p("原子发光持续时间约 $10^{-8}\\,\\text{s}$，发射的是有限长正弦片段，称为<strong>波列</strong>。普通光源是大量随机波列的叠加，相位不恒定；激光波列很长，单色性好。"))+
   der(p("<strong>波列长度与谱宽：</strong>设波列时长 $\\tau_0$，由傅里叶分析其频谱宽度满足：")+
   fml("\\Delta\\nu\\,\\tau_0\\sim1\\ \\Rightarrow\\ \\Delta\\lambda=\\frac{\\lambda^2}{c}\\Delta\\nu\\sim\\frac{\\lambda^2}{c\\tau_0}")+
   p("波列越长，谱线越窄、单色性越好，可干涉的最大光程差也越大，由此给出相干长度的估计。"))+
   note(p("谱线加宽机制包括自然加宽（有限寿命）、多普勒加宽（热运动）与碰撞加宽（压强），它们共同决定实际谱宽。"))
 )},
{"id":"o2s2-3","name":"相位与光程","tags":["der","def"],"brief":"光程等于折射率与几何路程之积。",
 "body": wrap(
   defn("光程",p("光在折射率为 $n$ 的介质中走过几何路程 $r$，其光程定义为 $\\Delta=nr$；它等于相同时向内光在真空中走过的距离，是描述相位积累的等效路程。"))+
   der(p("<strong>推导：</strong>介质中波长为 $\\lambda/n$，走过路程 $r$ 引起的相位变化为：")+
   fml("\\varphi=\\frac{2\\pi}{\\lambda/n}\\,r=\\frac{2\\pi}{\\lambda}\\,nr=\\frac{2\\pi}{\\lambda}\\Delta")+
   p("故相位变化只由光程 $\\Delta=nr$ 决定。对分段介质 $\\Delta=\\sum_i n_ir_i$；对连续变化介质 $\\Delta=\\int n\\,ds$。"))+
   note(p("费马原理 $\\delta\\int n\\,ds=0$ 的物理含义即实际光路的相位取极值（稳定值）。"))
 )},
{"id":"o2s2-4","name":"光程差与相位差","tags":["der","thm"],"brief":"相位差等于光程差乘以波数。",
 "body": wrap(
   der(p("<strong>推导：</strong>两相干光的光程分别为 $\\Delta_1$、$\\Delta_2$，其相位差为：")+
   fml("\\delta=\\frac{2\\pi}{\\lambda}(\\Delta_2-\\Delta_1)=\\frac{2\\pi}{\\lambda}\\Delta")+
   p("由此得到干涉判据：")+
   fml("\\Delta=k\\lambda\\ (\\text{加强}),\\qquad \\Delta=\\left(k+\\tfrac12\\right)\\lambda\\ (\\text{减弱})"))+
   exa(p("<strong>例：</strong>$\\Delta=1.5\\lambda$ 时 $\\delta=3\\pi$，$\\cos\\delta=-1$，两波相消，光强取极小。"))+
   note(p("相位差与光程差的换算是全部干涉问题的核心工具：先算光程差，再换算相位差，最后代入光强公式。"))
 )},
]},
{
"name": "2.3 波的传播与叠加",
"color": "#a855f7",
"desc": "波前与波面、惠更斯原理、叠加原理、能流与坡印廷矢量",
"items": [
{"id":"o2s3-1","name":"波前与波面","tags":["def","der"],"brief":"等相位面与波前的几何描述。",
 "body": wrap(
   defn("波面与波前",p("相位相同的点构成<strong>波面</strong>（等相位面）；最前面的那个波面称为<strong>波前</strong>。波面可以是平面（平面波）、球面（球面波）或复杂曲面。"))+
   der(p("<strong>波面与光线的关系：</strong>由相位 $\\varphi=\\mathbf{k}\\cdot\\mathbf{r}-\\omega t$ 为常数得波面方程 $\\mathbf{k}\\cdot\\mathbf{r}=\\text{const}$，其法线方向即 $\\mathbf{k}$。在各向同性介质中：")+
   fml("\\mathbf{k}\\parallel\\nabla\\varphi\\ \\Rightarrow\\ \\text{光线}\\perp\\text{波面}")+
   p("因此几何光学中的光线就是波面的法线，几何光学可视为波长趋于零时波动光学的极限。"))+
   note(p("在各向异性晶体（如方解石）中光线与波面法线不再一致，出现双折射，此时须区分光线方向与波面法线方向。"))
 )},
{"id":"o2s3-2","name":"惠更斯原理","tags":["thm","der"],"brief":"波前上每点都是新的次波源。",
 "body": wrap(
   thm("惠更斯原理",p("波前上每一点都可看作发射球面次波的新波源，这些次波的包络面构成下一时刻的新波前。"))+
   der(p("<strong>用于推导反射与折射定律：</strong>设平面波以角 $\\theta_1$ 入射到界面，波前先后到达 $A$、$B$ 两点，同一时间间隔内次波在两侧传播距离为：")+
   fml("AA'=v_1\\Delta t,\\qquad BB'=v_2\\Delta t")+
   p("由包络面的几何关系 $AA'=\\overline{AB}\\sin\\theta_1$、$BB'=\\overline{AB}\\sin\\theta_2$，消去 $\\overline{AB}$ 并以 $v=c/n$ 代入得：")+
   fml("\\frac{\\sin\\theta_1}{v_1}=\\frac{\\sin\\theta_2}{v_2}\\ \\Rightarrow\\ n_1\\sin\\theta_1=n_2\\sin\\theta_2")+
   p("即折射定律；同法令两侧速度相同可得 $\\theta_i=\\theta_r$，即反射定律。"))+
   note(p("菲涅耳进一步假设次波相干叠加并引入倾斜因子，得到惠更斯-菲涅耳原理，成为衍射理论的基础。"))
 )},
{"id":"o2s3-3","name":"叠加原理与波的独立传播","tags":["thm","der"],"brief":"线性介质中光波线性叠加、互不干扰。",
 "fig":"waveadd","figCap":"两列波在线性介质中独立传播并叠加为合振动",
 "body": wrap(
   thm("叠加原理",p("在线性介质中，多个光波同时存在时的总场强为各波单独存在时的矢量之和：")+
   fml("\\mathbf{E}=\\mathbf{E}_1+\\mathbf{E}_2+\\cdots")+
   p("各波相遇后仍保持原有的频率、振幅与传播方向，互不干扰，称为波的独立传播。"))+
   der(p("<strong>线性依据：</strong>波动方程对场量是线性的，若 $\\mathbf{E}_1$、$\\mathbf{E}_2$ 均为解，则任意线性组合亦为解：")+
   fml("\\nabla^2(\\mathbf{E}_1+\\mathbf{E}_2)=\\mu\\varepsilon\\frac{\\partial^2(\\mathbf{E}_1+\\mathbf{E}_2)}{\\partial t^2}")+
   p("但光强与振幅为平方关系，叠加后出现交叉项，故光强并不简单相加：")+
   fml("I=\\langle|\\mathbf{E}_1+\\mathbf{E}_2|^2\\rangle=I_1+I_2+2\\sqrt{I_1I_2}\\,\\langle\\cos\\delta\\rangle")+
   p("仅当交叉项的时间平均值不为零时才出现干涉。"))+
   note(p("强光（如聚焦激光）下介质响应呈非线性，叠加原理失效，产生倍频、自聚焦等非线性光学效应。"))
 )},
{"id":"o2s3-4","name":"波的能流与坡印廷矢量","tags":["der","app"],"brief":"用坡印廷矢量描述光能量输运。",
 "body": wrap(
   der(p("<strong>坡印廷矢量：</strong>电磁场能流密度定义为：")+
   fml("\\mathbf{S}=\\frac{1}{\\mu_0}\\mathbf{E}\\times\\mathbf{B}")+
   p("其方向为能量传播方向，大小为单位时间通过单位面积的能量。对平面波 $B=E/c$：")+
   fml("S=\\frac{E^2}{\\mu_0c}=c\\varepsilon_0E^2\\ \\Rightarrow\\ I=\\langle S\\rangle=\\frac12c\\varepsilon_0E_0^2")+
   p("由能流还可得到光对物体的辐射压力：")+
   fml("p_{rad}=\\frac{I}{c}\\ (\\text{吸收}),\\qquad p_{rad}=\\frac{2I}{c}\\ (\\text{反射})"))+
   app(p("<strong>应用：</strong>光镊与激光冷却利用辐射压力操控原子与微粒；太阳帆、激光推进器则利用光压获得推力。"))
 )},
]},
{
"name": "2.4 相干性 偏振态与光谱",
"color": "#9333ea",
"desc": "偏振态基础、时间与空间相干性、相干长度、光谱与色散",
"items": [
{"id":"o2s4-1","name":"偏振态基础","tags":["def","der"],"brief":"光波横振动方向构成偏振态。",
 "body": wrap(
   defn("偏振态",p("光波电矢量 $\\mathbf{E}$ 在垂直于传播方向的平面内的振动方式称为偏振态，基本形式有线偏振、圆偏振与椭圆偏振，此外还有完全无规则的自然光。"))+
   der(p("<strong>偏振态的参数描述：</strong>把 $\\mathbf{E}$ 分解为两个正交分量：")+
   fml("E_x=a_1\\cos(\\omega t+\\varphi_1),\\qquad E_y=a_2\\cos(\\omega t+\\varphi_2)")+
   p("消去时间 $t$ 得轨迹方程：")+
   fml("\\frac{E_x^2}{a_1^2}+\\frac{E_y^2}{a_2^2}-\\frac{2E_xE_y}{a_1a_2}\\cos\\delta=\\sin^2\\delta,\\quad \\delta=\\varphi_2-\\varphi_1")+
   p("$\\delta=0,\\pi$ 时退化为直线（线偏振）；$\\delta=\\pm\\pi/2$ 且 $a_1=a_2$ 时为圆偏振；其余情形为椭圆偏振，旋转方向由 $\\delta$ 的符号决定。"))+
   note(p("偏振态也可用斯托克斯参量或琼斯矢量表示，后者在偏振器件的矩阵计算中最方便。"))
 )},
{"id":"o2s4-2","name":"时间相干性与空间相干性","tags":["der"],"brief":"相干性在时间与空间两个维度的体现。",
 "body": wrap(
   der(p("<strong>时间相干性：</strong>源于光源谱宽有限，同一波列在不同时刻的相位相关程度随延迟 $\\tau$ 下降，相干时间 $\\tau_c\\sim1/\\Delta\\nu$ 决定最大可干涉光程差。"))+
   der(p("<strong>空间相干性：</strong>源于光源尺寸有限，横向相距 $d$ 的两点相位相关程度随 $d$ 增大而下降。对尺寸为 $b$ 的非相干扩展光源，距离 $z$ 处相干宽度为：")+
   fml("d_c\\approx\\frac{\\lambda z}{b}")+
   p("杨氏双缝实验中若缝距超过 $d_c$，条纹对比度将显著下降。"))+
   exa(p("<strong>例：</strong>太阳角直径约 $0.009\\,\\text{rad}$，$\\lambda=550\\,\\text{nm}$ 时地面相干宽度仅约 $0.06\\,\\text{mm}$，故用太阳光做双缝实验必须用极窄的缝。"))+
   note(p("相干性可用复空间-时间相干度统一描述，干涉条纹对比度等于相干度的模。"))
 )},
{"id":"o2s4-3","name":"相干长度与相干时间","tags":["der","thm"],"brief":"谱宽决定可干涉的最大光程差。",
 "fig":"coherence","figCap":"有限长波列与相干长度：光程差超过 L_c 后条纹消失",
 "body": wrap(
   der(p("<strong>推导：</strong>谱宽为 $\\Delta\\lambda$ 的光，只有当光程差不超过一个波列长度时才能观察到干涉，该长度称为相干长度：")+
   fml("L_c=\\frac{\\lambda^2}{\\Delta\\lambda},\\qquad \\tau_c=\\frac{L_c}{c}=\\frac{\\lambda^2}{c\\,\\Delta\\lambda}")+
   p("由 $\\Delta\\nu=\\frac{c}{\\lambda^2}\\Delta\\lambda$ 可见 $\\tau_c\\,\\Delta\\nu\\approx1$，即相干时间与谱宽成反比。"))+
   exa(p("<strong>例：</strong>白光 $\\Delta\\lambda\\approx300\\,\\text{nm}$ 时 $L_c\\approx1\\,\\mu\\text{m}$，只能看到几条彩色条纹；稳频激光 $\\Delta\\lambda\\sim10^{-6}\\,\\text{nm}$ 时 $L_c$ 可达数百米。")+
   note(p("相干长度给出干涉仪的最大可测光程差，是选择光源与设计干涉系统的关键指标。")))
 )},
{"id":"o2s4-4","name":"光谱与色散基础","tags":["der","app"],"brief":"光谱的波长分布与介质色散。",
 "body": wrap(
   der(p("<strong>色散的物理来源：</strong>介质折射率随波长变化 $n=n(\\lambda)$。远离吸收带时可用柯西公式近似：")+
   fml("n(\\lambda)=A+\\frac{B}{\\lambda^2}+\\frac{C}{\\lambda^4}")+
   p("由此得色散率 $\\frac{dn}{d\\lambda}<0$（正常色散），即短波（紫光）折射率大、偏折强，棱镜分光正基于此。"))+
   defn("光谱",p("把复色光按波长（或频率）展开后得到的强度分布称为光谱，分为线状谱（原子）、带状谱（分子）与连续谱（热辐射）。"))+
   app(p("<strong>应用：</strong>光谱分析用于鉴别物质成分与测定天体运动（多普勒频移），棱镜与光栅是常用的分光元件。"))+
   note(p("在吸收带附近 $\\frac{dn}{d\\lambda}>0$，称为反常色散，须用完整的振子模型（塞耳迈耶尔方程）描述，详见第六章。"))
 )},
]},
]

ch3_sections = [
{
"name": "3.1 相干性与光程差",
"color": "#7c3aed",
"desc": "相干条件、光程差与杨氏双缝干涉",
"items": [
{"id":"o3s1-1","name":"相干条件与相干叠加","tags":["def","der"],"brief":"频率相同、振动方向相同、相位差恒定。",
 "body": wrap(
   exa(p("<strong>例：</strong>两相干光强度相等 $I_1=I_2=I_0$，相位差 $\\delta=\\pi/3$：")+
   fml("I=2I_0(1+\\cos\\delta)=2I_0(1+0.5)=3I_0")+
   p("当 $\\delta=0$ 时为 $4I_0$，$\\delta=\\pi$ 时为 0，出现完全的明暗对比。")+
   note(p("条纹对比度 $V=\\frac{I_{\\max}-I_{\\min}}{I_{\\max}+I_{\\min}}$，等强度相干时 $V=1$。")))+
   defn("相干条件",p("两束光发生稳定干涉的必要条件：<strong>频率相同</strong>、<strong>振动方向相同（或有平行分量）</strong>、<strong>相位差恒定</strong>。满足条件的波源称为相干光源。"))+
   der(p("<strong>光强的相干叠加：</strong>两相干光 $E_1=E_{10}\\cos(\\omega t+\\varphi_1)$、$E_2=E_{20}\\cos(\\omega t+\\varphi_2)$，合振幅平方：")+
   fml("I = I_1+I_2+2\\sqrt{I_1 I_2}\\cos\\delta,\\quad \\delta=\\varphi_2-\\varphi_1","$\\delta$ 为相位差")+
   p("当 $\\delta=2k\\pi$ 时 $I$ 最大，$\\delta=(2k+1)\\pi$ 时 $I$ 最小；非相干光第三项平均为零，$I=I_1+I_2$。"))+
   note(p("普通光源各原子独立发光，只有把同一束光分为两束再叠加才能获得恒定的相位差。"))
 )},
{"id":"o3s1-2","name":"光程与光程差","tags":["der"],"brief":"相位差与光程差的换算关系。",
 "body": wrap(
   exa(p("<strong>例：</strong>一束光在折射率 $n=1.5$ 的玻璃中走过 $r=2\\,\\text{mm}$，与另一束在真空中走过相同几何距离：")+
   fml("\\Delta=nr-r=0.5\\times2\\,\\text{mm}=1.0\\,\\text{mm}")+
   p("对应相位差 $\\delta=2\\pi\\Delta/\\lambda$，$\\lambda=500\\,\\text{nm}$ 时约 $4000\\pi$。")+
   note(p("光程概念把不同介质中的几何路径统一折合为真空尺度，是处理干涉的核心工具。")))+
   defn("光程",p("光在折射率 $n$ 的介质中传播几何路程 $r$ 时，光程为 $\\Delta=nr$，其物理意义为折合到真空中的等效路程。"))+
   der(p("<strong>相位差与光程差：</strong>介质中波长为 $\\lambda_n=\\lambda/n$，光走过 $r$ 引起的相位变化 $\\varphi=\\frac{2\\pi}{\\lambda_n}r=\\frac{2\\pi}{\\lambda}nr$。故两束光相位差：")+
   fml("\\delta = \\frac{2\\pi}{\\lambda}\\Delta,\\quad \\Delta=\\sum_i n_i r_i")+
   p("干涉加强条件 $\\delta=2k\\pi$ 等价于光程差 $\\Delta=k\\lambda$。"))+
   note(p("引入光程后，不同介质中光路可在统一尺度上比较，是把几何路径换算成相位的关键。"))
 )},
{"id":"o3s1-3","name":"杨氏双缝干涉","tags":["thm","der"],"brief":"双缝干涉条纹间距公式。",
 "fig":"doubleslit","figCap":"杨氏双缝干涉装置与条纹",
 "body": wrap(
   exa(p("<strong>例：</strong>$\\lambda=600\\,\\text{nm}$，双缝间距 $d=0.20\\,\\text{mm}$，屏距 $D=1.0\\,\\text{m}$：")+
   fml("\\Delta y=\\frac{\\lambda D}{d}=\\frac{600\\times10^{-9}\\times1.0}{0.20\\times10^{-3}}=3.0\\,\\text{mm}")+
   p("第 5 级明纹距中央 $y_5=15\\,\\text{mm}$。")+
   note(p("由条纹间距可反求波长：$\\lambda=\\frac{d\\Delta y}{D}$，这正是杨氏实验测量光波长的原理。")))+
   exa(p("<strong>例：</strong>$\\lambda=600\\,\\text{nm}$，双缝间距 $d=0.20\\,\\text{mm}$，屏距 $D=1.0\\,\\text{m}$：")+
   fml("\\Delta y=\\frac{\\lambda D}{d}=\\frac{600\\times10^{-9}\\times1.0}{0.20\\times10^{-3}}=3.0\\,\\text{mm}")+
   p("第 5 级明纹距中央 $y_5=15\\,\\text{mm}$。")+
   note(p("由条纹间距可反求波长：$\\lambda=\\frac{d\\Delta y}{D}$，这正是杨氏实验测量光波长的原理。")))+
   thm("杨氏双缝干涉",p("单色光经双缝 $S_1,S_2$（间距 $d$）后在距离 $D$ 的屏上形成等间距明暗条纹，光程差 $\\Delta\\approx d\\sin\\theta\\approx d\\,y/D$。"))+
   der(p("<strong>推导：</strong>屏上距轴线 $y$ 处到两缝的距离差约为 $\\Delta=r_2-r_1\\approx d\\sin\\theta$。近轴时 $\\sin\\theta\\approx\\tan\\theta=y/D$，故 $\\Delta\\approx dy/D$。明纹条件 $\\Delta=k\\lambda$：")+
   fml("y_k = k\\frac{\\lambda D}{d}","明纹位置")+
   p("相邻明纹间距：")+
   fml("\\Delta y = y_{k+1}-y_k = \\frac{\\lambda D}{d}")+
   fml("I = 4I_0\\cos^2\\frac{\\pi d y}{\\lambda D}","双缝光强分布"))+
   note(p("条纹间距与 $\\lambda,D$ 成正比、与 $d$ 成反比，可用于测量波长或缝间距。"))
 )},
]},
{
"name": "3.2 分波前干涉",
"color": "#8b5cf6",
"desc": "菲涅耳双镜、劳埃德镜与半波损失",
"items": [
{"id":"o3s2-1","name":"菲涅耳双镜","tags":["der"],"brief":"用双平面镜获得相干光。",
 "body": wrap(
   exa(p("<strong>例：</strong>双镜夹角偏离 $180°$ 的角为 $\\alpha=10'$，光源到交线距离 $r=20\\,\\text{cm}$：")+
   fml("d=2r\\alpha=2\\times0.20\\times\\frac{10}{60}\\times\\frac{\\pi}{180}\\approx1.16\\times10^{-3}\\,\\text{m}")+
   p("屏距 $D=1.5\\,\\text{m}$ 时条纹间距 $\\Delta y=\\lambda D/d\\approx0.8\\,\\text{mm}$。")+
   note(p("菲涅耳双镜干涉无需狭缝分光，是早期验证光的波动性的重要实验。")))+
   exa(p("<strong>例：</strong>双镜夹角偏离 $180°$ 的角为 $\\alpha=10'$，光源到交线距离 $r=20\\,\\text{cm}$：")+
   fml("d=2r\\alpha=2\\times0.20\\times\\frac{10}{60}\\times\\frac{\\pi}{180}\\approx1.16\\times10^{-3}\\,\\text{m}")+
   p("屏距 $D=1.5\\,\\text{m}$ 时条纹间距 $\\Delta y=\\lambda D/d\\approx0.8\\,\\text{mm}$。")+
   note(p("菲涅耳双镜干涉无需狭缝分光，是早期验证光的波动性的重要实验。")))+
   defn("菲涅耳双镜",p("两块夹角略小于 180° 的平面镜构成双镜，点光源 $S$ 经两镜反射形成两个虚像 $S_1,S_2$，它们是相干光源，在重叠区产生干涉。"))+
   der(p("<strong>推导：</strong>设镜面夹角为 $\\alpha$（偏离 180° 的小角），光源到交线距离为 $r$。两虚像对交线张角约为 $2\\alpha$，两相干光源间距：")+
   fml("d \\approx 2r\\alpha")+
   p("用杨氏双缝干涉的条纹间距公式，屏距 $D$ 时：")+
   fml("\\Delta y = \\frac{\\lambda D}{d} = \\frac{\\lambda D}{2r\\alpha}")+
   p("调节夹角 $\\alpha$ 即可改变条纹间距，常用于演示与测量。"))+
   note(p("分波前干涉的共同特点：把同一波前的不同部分分割后叠加，故要求光源足够小以保证空间相干性。"))
 )},
{"id":"o3s2-2","name":"劳埃德镜与半波损失","tags":["der"],"brief":"掠入射反射引入附加半波损失。",
 "body": wrap(
   exa(p("<strong>例（半波损失的相位）：</strong>反射光在光疏-光密界面反射时相位突变 $\\pi$：")+
   fml("\\Delta\\varphi=\\pi \\Longleftrightarrow \\Delta_{\\text{附加}}=\\frac{\\lambda}{2}")+
   p("劳埃德镜实验中镜面接触点两光几何路程相等却为暗纹，正是该附加光程差的直接证据。")+
   note(p("增透膜的两个界面反射条件不同，正是利用这一附加相位差实现相消。")))+
   exa(p("<strong>例（半波损失的相位）：</strong>反射光在光疏-光密界面反射时相位突变 $\\pi$：")+
   fml("\\Delta\\varphi=\\pi \\Longleftrightarrow \\Delta_{\\text{附加}}=\\frac{\\lambda}{2}")+
   p("劳埃德镜实验中镜面接触点两光几何路程相等却为暗纹，正是该附加光程差的直接证据。")+
   note(p("增透膜的两个界面反射条件不同，正是利用这一附加相位差实现相消。")))+
   defn("劳埃德镜",p("点光源直接发出的光与经平面镜掠入射反射的光叠加发生干涉，是典型的反射光干涉装置。"))+
   der(p("<strong>半波损失：</strong>光由光疏介质射向光密介质（$n_1<n_2$）并在界面反射时，反射光相位突变为 $\\pi$，等效附加光程 $\\lambda/2$，称为半波损失。故两光路的光程差为：")+
   fml("\\Delta = r_2 - r_1 + \\frac{\\lambda}{2}")+
   p("劳埃德镜实验中，镜面接触点处两光几何路程相等却出现暗纹，正是半波损失的实验证据。"))+
   note(p("反射光发生半波损失的条件是 $n_1<n_2$；若 $n_1>n_2$ 则无附加相位突变。"))
 )},
]},
{
"name": "3.3 薄膜干涉",
"color": "#a855f7",
"desc": "等倾干涉、等厚干涉与牛顿环",
"items": [
{"id":"o3s3-1","name":"等倾干涉","tags":["der"],"brief":"薄膜厚度均匀、倾角相同的条纹。",
 "body": wrap(
   defn("等倾干涉",p("厚度均匀的薄膜，入射角相同的光对应同一条干涉条纹，条纹呈同心圆环，故称等倾干涉。"))+
   der(p("<strong>光程差推导：</strong>光在厚度 $d$、折射率 $n$ 的膜内以折射角 $\\theta$ 传播，往返路程 $2d/\\cos\\theta$，其中一段在空气中，等效光程差：")+
   fml("\\Delta = 2nd\\cos\\theta")+
   p("若考虑上下表面反射条件不同（上表面有半波损失），需附加 $\\lambda/2$：")+
   fml("\\Delta = 2nd\\cos\\theta + \\frac{\\lambda}{2}")+
   p("明纹条件 $\\Delta=k\\lambda$。因 $\\cos\\theta$ 随入射角变化，同一倾角对应同一级次，形成同心环。"))+
   app(p("<strong>应用：</strong>用来检验光学表面平行度、测量薄膜厚度；观察方式有反射光与透射光两种，条纹互补。"))
 )},
{"id":"o3s3-2","name":"等厚干涉与劈尖","tags":["der"],"brief":"厚度线性变化的楔形膜条纹。",
 "body": wrap(
   exa(p("<strong>例（测细丝直径）：</strong>两玻璃片夹入直径 $D$ 的细丝形成长 $L$ 的劈尖，条纹总数 $N$：")+
   fml("D=\\frac{N\\lambda}{2},\\qquad \\theta=\\frac{D}{L}")+
   p("由条纹间距 $\\Delta x=\\lambda/(2\\theta)$ 可同时求得楔角。")+
   note(p("劈尖干涉对微小厚度变化极敏感，可分辨纳米级的高度差，用于检验平面度与膜层均匀性。")))+
   exa(p("<strong>例（测细丝直径）：</strong>两玻璃片夹入直径 $D$ 的细丝形成长 $L$ 的劈尖，条纹总数 $N$：")+
   fml("D=\\frac{N\\lambda}{2},\\qquad \\theta=\\frac{D}{L}")+
   p("由条纹间距 $\\Delta x=\\lambda/(2\\theta)$ 可同时求得楔角。")+
   note(p("劈尖干涉对微小厚度变化极敏感，可分辨纳米级的高度差，用于检验平面度与膜层均匀性。")))+
   defn("等厚干涉",p("当光近似垂直入射时，光程差主要由膜厚 $d$ 决定，厚度相同的点连成同一干涉条纹，称等厚干涉。"))+
   der(p("<strong>劈尖条纹推导：</strong>两玻璃片一端接触形成楔角 $\\theta$ 的空气劈尖，距棱边 $x$ 处空气层厚 $d=x\\theta$。垂直入射光程差 $\\Delta=2d+\\lambda/2$。明纹 $\\Delta=k\\lambda$：")+
   fml("x_k = \\frac{(2k-1)\\lambda}{4\\theta}","空气劈尖明纹位置")+
   p("相邻条纹间距：")+
   fml("\\Delta x = \\frac{\\lambda}{2\\theta}")+
   p("若中间充以折射率 $n$ 的液体则 $\\Delta x=\\lambda/(2n\\theta)$。"))+
   app(p("<strong>应用：</strong>劈尖干涉可测量微小角度、薄膜厚度、细丝直径，检验平面度。"))
 )},
{"id":"o3s3-3","name":"牛顿环","tags":["der","app"],"brief":"平凸透镜与平板间空气层形成的圆环条纹。",
 "fig":"newtonring","figCap":"牛顿环干涉圆环",
 "body": wrap(
   exa(p("<strong>例：</strong>测得第 10 与第 20 暗环直径 $D_{10}=6.0\\,\\text{mm}$、$D_{20}=8.6\\,\\text{mm}$，$\\lambda=589\\,\\text{nm}$：")+
   fml("R=\\frac{D_{20}^2-D_{10}^2}{4\\times(20-10)\\lambda}\\approx\\frac{73.96-36.0}{4\\times10\\times589\\times10^{-6}}\\approx1.6\\,\\text{m}")+
   p("用两环直径之差可消除接触形变带来的系统误差。")+
   note(p("牛顿环还用于测量微小位移：中心每移动一个条纹对应空气层厚度变化 $\\lambda/2$。")))+
   exa(p("<strong>例：</strong>测得第 10 与第 20 暗环直径 $D_{10}=6.0\\,\\text{mm}$、$D_{20}=8.6\\,\\text{mm}$，$\\lambda=589\\,\\text{nm}$：")+
   fml("R=\\frac{D_{20}^2-D_{10}^2}{4\\times(20-10)\\lambda}\\approx\\frac{73.96-36.0}{4\\times10\\times589\\times10^{-6}}\\approx1.6\\,\\text{m}")+
   p("用两环直径之差可消除接触形变带来的系统误差。")+
   note(p("牛顿环还用于测量微小位移：中心每移动一个条纹对应空气层厚度变化 $\\lambda/2$。")))+
   defn("牛顿环",p("平凸透镜（曲率半径 $R$）凸面与平板玻璃接触，其间空气层厚度随半径变化，形成等厚干涉的同心圆环。"))+
   der(p("<strong>测量曲率半径：</strong>距接触点 $r$ 处空气层厚 $d$，由几何关系 $d\\approx\\frac{r^2}{2R}$。垂直入射光程差 $\\Delta=2d+\\lambda/2$。暗环条件 $\\Delta=(2k+1)\\lambda/2$：")+
   fml("2\\cdot\\frac{r_k^2}{2R}+\\frac{\\lambda}{2}=(2k+1)\\frac{\\lambda}{2} \\implies r_k^2=kR\\lambda")+
   fml("r_k = \\sqrt{kR\\lambda}","第 k 级暗环半径")+
   p("测出两暗环直径 $D_m,D_n$ 可消去接触形变误差：")+
   fml("R = \\frac{D_m^2-D_n^2}{4(m-n)\\lambda}"))+
   app(p("<strong>应用：</strong>测量透镜曲率半径、检验透镜表面质量，中心应为暗斑（半波损失）。"))
 )},
]},
{
"name": "3.4 多光束干涉与干涉仪",
"color": "#7c3aed",
"desc": "迈克尔逊干涉仪、法布里-珀罗干涉仪与干涉滤光片",
"items": [
{"id":"o3s4-1","name":"迈克尔逊干涉仪","tags":["der","app"],"brief":"分振幅双光束干涉仪。",
 "body": wrap(
   exa(p("<strong>例：</strong>移动动镜 $\\Delta d=0.10\\,\\text{mm}$ 时数得 $N=316$ 条条纹移过，求波长：")+
   fml("\\lambda=\\frac{2\\Delta d}{N}=\\frac{2\\times0.10\\times10^{-3}}{316}\\approx633\\,\\text{nm}")+
   p("该结果对应氦氖激光波长，说明干涉仪可用于极精密的长度与波长测量。")+
   note(p("用白光照明时仅在等光程位置出现彩色条纹，据此可确定零光程差。")))+
   exa(p("<strong>例：</strong>移动动镜 $\\Delta d=0.10\\,\\text{mm}$ 时数得 $N=316$ 条条纹移过，求波长：")+
   fml("\\lambda=\\frac{2\\Delta d}{N}=\\frac{2\\times0.10\\times10^{-3}}{316}\\approx633\\,\\text{nm}")+
   p("该结果对应氦氖激光波长，说明干涉仪可用于极精密的长度与波长测量。")+
   note(p("用白光照明时仅在等光程位置出现彩色条纹，据此可确定零光程差。")))+
   defn("迈克尔逊干涉仪",p("由分束镜 $G_1$、补偿板 $G_2$、动镜 $M_1$ 与定镜 $M_2$ 组成。光被分为两束分别经两臂反射后叠加，等效于厚度可调的空气薄膜。"))+
   der(p("<strong>条纹移动与位移：</strong>移动动镜 $M_1$ 使一臂光程改变 $2\\Delta d$，条纹每移动一条光程差变化一个 $\\lambda$：")+
   fml("\\Delta d = N\\frac{\\lambda}{2}","N 为移过的条纹数")+
   p("据此可精确测定长度或由已知位移测波长。等倾干涉时呈现同心圆环，等厚干涉时呈现直条纹。"))+
   app(p("<strong>应用：</strong>精密测长、测折射率、傅里叶变换光谱仪（FTIR）的基础，也是迈克尔逊-莫雷实验的核心装置。"))
 )},
{"id":"o3s4-2","name":"多光束干涉与法布里-珀罗","tags":["der"],"brief":"高反射率平行板的多光束干涉。",
 "body": wrap(
   exa(p("<strong>例：</strong>反射率 $R=0.90$，求精细度参数与条纹锐度：")+
   fml("F=\\frac{4R}{(1-R)^2}=\\frac{4\\times0.90}{0.01}=360")+
   p("精细度 $\\mathcal F=\\frac{\\pi\\sqrt F}{2}\\approx30$，即相邻透射峰之间可容纳约 30 个半宽。")+
   note(p("$R\\to1$ 时透射峰极锐，法布里-珀罗干涉仪因此具有超高光谱分辨率。")))+
   exa(p("<strong>例：</strong>反射率 $R=0.90$，求精细度参数与条纹锐度：")+
   fml("F=\\frac{4R}{(1-R)^2}=\\frac{4\\times0.90}{0.01}=360")+
   p("精细度 $\\mathcal F=\\frac{\\pi\\sqrt F}{2}\\approx30$，即相邻透射峰之间可容纳约 30 个半宽。")+
   note(p("$R\\to1$ 时透射峰极锐，法布里-珀罗干涉仪因此具有超高光谱分辨率。")))+
   defn("法布里-珀罗干涉仪",p("两块高反射率平行平板间形成多次反射，多束透射光叠加，得到极锐细的干涉亮纹。"))+
   der(p("<strong>透射光强：</strong>设振幅反射率 $r$、透射率 $t$，相邻透射光相位差 $\\delta$。多光束叠加得：")+
   fml("I_t = \\frac{I_0}{1+F\\sin^2(\\delta/2)},\\quad F=\\frac{4R}{(1-R)^2}","精细度参数 $F$")+
   p("其中 $R=r^2$ 为反射率。$R$ 越大 $F$ 越大，透射峰越锐。峰的半高全宽 $\\Delta\\delta\\approx\\frac{4}{\\sqrt F}$，精细度 $\\mathcal F=\\frac{2\\pi}{\\Delta\\delta}$。"))+
   app(p("<strong>应用：</strong>高分辨光谱、激光谐振腔（纵模选择）、窄带滤光片与光学频率梳。"))
 )},
{"id":"o3s4-3","name":"干涉滤光片","tags":["der","app"],"brief":"利用多光束干涉选择特定波长。",
 "body": wrap(
   defn("干涉滤光片",p("在两层高反射膜之间夹一层介质间隔层（厚度 $d$、折射率 $n$），构成法布里-珀罗型滤光片。"))+
   der(p("<strong>中心波长：</strong>透射极大由间隔层光程差决定 $2nd=k\\lambda$：")+
   fml("\\lambda = \\frac{2nd}{k}")+
   p("半宽度 $\\Delta\\lambda$ 与反射率有关，可通过增加反射层数变窄：")+
   fml("\\frac{\\Delta\\lambda}{\\lambda} \\approx \\frac{1-R}{\\pi\\sqrt{R}}\\frac{\\lambda}{2nd}")+
   p("多层介质膜滤光片可做到带宽 1 nm 以下。"))+
   app(p("<strong>应用：</strong>荧光显微、天文观测、光通信中的窄带滤波；多个间隔层构成多腔滤光片可获得矩形透过带。"))
 )},
]},
{
"name": "3.5 相干性与薄膜应用",
"color": "#8b5cf6",
"desc": "相干长度、时间空间相干性与增透增反膜",
"items": [
{"id":"o3s5-1","name":"相干长度与相干时间","tags":["der"],"brief":"光谱宽度决定可干涉的最大光程差。",
 "body": wrap(
   exa(p("<strong>例：</strong>氦氖激光 $\\lambda=632.8\\,\\text{nm}$，谱线宽度 $\\Delta\\lambda=10^{-3}\\,\\text{nm}$：")+
   fml("L_c=\\frac{\\lambda^2}{\\Delta\\lambda}=\\frac{(632.8\\times10^{-9})^2}{10^{-12}}\\approx4.0\\times10^5\\,\\text{m}")+
   p("相干长度达数百公里；而白光 $\\Delta\\lambda\\approx300\\,\\text{nm}$ 时 $L_c$ 仅约 1 微米。")+
   note(p("激光的长时间相干性是全息、干涉测长与激光雷达得以实现的基础。")))+
   exa(p("<strong>例：</strong>氦氖激光 $\\lambda=632.8\\,\\text{nm}$，谱线宽度 $\\Delta\\lambda=10^{-3}\\,\\text{nm}$：")+
   fml("L_c=\\frac{\\lambda^2}{\\Delta\\lambda}=\\frac{(632.8\\times10^{-9})^2}{10^{-12}}\\approx4.0\\times10^5\\,\\text{m}")+
   p("相干长度达数百公里；而白光 $\\Delta\\lambda\\approx300\\,\\text{nm}$ 时 $L_c$ 仅约 1 微米。")+
   note(p("激光的长时间相干性是全息、干涉测长与激光雷达得以实现的基础。")))+
   defn("相干长度",p("能观察到干涉现象的最大光程差称为相干长度 $L_c$，对应的时间 $\\tau_c=L_c/c$ 称为相干时间。"))+
   der(p("<strong>由光谱宽度导出：</strong>准单色光光谱宽度为 $\\Delta\\lambda$（对应频率宽度 $\\Delta\\nu$）。当光程差超过几个波长时相位关系失去相关。由 $\\nu=c/\\lambda$ 取微分：")+
   fml("\\Delta\\nu = \\frac{c}{\\lambda^2}\\Delta\\lambda")+
   p("时域与频域不确定关系 $\\tau_c\\Delta\\nu\\approx 1$，故：")+
   fml("L_c = c\\tau_c \\approx \\frac{c}{\\Delta\\nu} = \\frac{\\lambda^2}{\\Delta\\lambda}")+
   p("单色性越好（$\\Delta\\lambda$ 越小），相干长度越长；白光相干长度仅数微米，激光可达公里量级。"))+
   note(p("迈克尔逊干涉仪中白光只在零光程差附近出现彩色条纹，可用于精确确定等光程位置。"))
 )},
{"id":"o3s5-2","name":"时间相干性与空间相干性","tags":["der"],"brief":"相干性在时间与空间两个维度的体现。",
 "body": wrap(
   exa(p("<strong>例：</strong>扩展光源宽 $b=1\\,\\text{mm}$、距双缝 $R=1\\,\\text{m}$、$\\lambda=550\\,\\text{nm}$：")+
   fml("d_c=\\frac{\\lambda R}{b}=\\frac{550\\times10^{-9}\\times1}{10^{-3}}=0.55\\,\\text{mm}")+
   p("故双缝间距须小于约 $0.55\\,\\text{mm}$ 才能观察到稳定条纹，这与双缝实验中用狭缝限制光源一致。")+
   note(p("空间相干性决定了干涉仪对光源尺寸的要求，恒星干涉仪正是利用它测量恒星角直径。")))+
   defn("两种相干性",p("<strong>时间相干性</strong>描述同一空间点不同时刻光场的相关性，由光谱宽度决定；<strong>空间相干性</strong>描述同一时刻不同空间点光场的相关性，由光源的有限尺寸决定。"))+
   der(p("<strong>横向相干宽度：</strong>设光源为宽度 $b$ 的扩展光源，距双缝 $R$，波长 $\\lambda$。当光源宽度使两侧条纹互相错开一个条纹时条纹消失，得横向相干宽度：")+
   fml("d_c = \\frac{\\lambda R}{b}")+
   p("故双缝间距 $d<d_c$ 才能观察到干涉；这也是为什么需要狭缝限制光源尺寸。"))+
   note(p("复空间相干度 $\\mu=\\frac{\\langle E_1 E_2^*\\rangle}{\\sqrt{I_1 I_2}}$，$|\\mu|=1$ 完全相干，$|\\mu|=0$ 完全不相干，$0<|\\mu|<1$ 部分相干。"))
 )},
{"id":"o3s5-3","name":"增透膜与增反膜","tags":["der","app"],"brief":"利用薄膜干涉控制反射率。",
 "body": wrap(
   defn("增透膜",p("在光学元件表面镀一层折射率介于空气与玻璃之间、厚度为四分之一波长的薄膜，使反射光相干相消，增强透射。"))+
   der(p("<strong>条件推导：</strong>垂直入射时两反射光光程差 $2nd$，两界面均存在半波损失（或均无）时相互抵消。相消条件：")+
   fml("2nd = \\left(k+\\frac{1}{2}\\right)\\lambda","增透条件")+
   p("取 $k=0$ 得最小厚度 $d=\\lambda/(4n)$，同时要求 $n=\\sqrt{n_{\\text{air}}n_{\\text{glass}}}$ 以达到零反射。"))+
   der(p("<strong>增反膜：</strong>多层高低折射率交替膜，使各界面反射光相干增强，可实现接近 100% 的反射率，如介质高反镜。"))+
   app(p("<strong>应用：</strong>镜头、眼镜、太阳能电池的减反射镀膜；介质膜高反镜、分束镜与激光腔镜。"))
 )},
]},
{
"name": "3.6 干涉应用",
"color": "#a855f7",
"desc": "干涉测量、条纹计数与白光干涉",
"items": [
{"id":"o3s6-1","name":"干涉测量与条纹移动","tags":["der","app"],"brief":"以条纹移动量作精密长度计量。",
 "body": wrap(
   defn("干涉计量",p("利用干涉条纹的移动数 $N$ 与光程变化的关系实现亚微米乃至纳米级长度测量。"))+
   der(p("<strong>灵敏度：</strong>光程每变化 $\\lambda/2$，条纹移动一条。故测长分辨率约半个波长，采用条纹细分或相位检测可达 $\\lambda/100$：")+
   fml("\\delta L = \\lambda/2 \\ \\text{(单条纹)} \\to \\lambda/100 \\ \\text{(细分)}")+
   p("干涉测长还广泛用于测微小位移、振动、形变与折射率变化。"))+
   app(p("<strong>应用：</strong>激光干涉仪（如用于光刻机工作台）、原子力显微镜的探测、引力波探测（LIGO）等。"))
 )},
{"id":"o3s6-2","name":"白光干涉与彩色条纹","tags":["der"],"brief":"白光下零级条纹呈白色，其余呈彩色。",
 "body": wrap(
   exa(p("<strong>例：</strong>白光干涉仪中连续移动动镜，只在零光程差附近出现少数几条清晰的彩色条纹：")+
   fml("L_c^{\\text{白}}\\approx\\frac{\\lambda^2}{\\Delta\\lambda}\\sim1\\,\\mu\\text{m}")+
   p("中央为白色亮纹，两侧呈对称彩色，随级次增大迅速模糊。")+
   note(p("白光干涉常用于色散与相位测量：零级条纹的白色位置可精确定位等光程点。")))+
   defn("白光干涉",p("白光包含各种波长，各波长干涉条纹间距不同，只在零光程差处各色条纹重合为白色亮纹。"))+
   der(p("<strong>条纹叠加：</strong>第 $k$ 级条纹位置 $y_k=k\\lambda D/d$ 与 $\\lambda$ 有关，不同颜色同级条纹错开。合成光强：")+
   fml("I(y) = \\sum_\\lambda I_\\lambda(y)")+
   p("零级（$k=0$，$\\Delta=0$）对所有波长都加强，故呈白色；高级次条纹因不同波长错开而呈现彩虹色并随级次变模糊。"))+
   app(p("<strong>应用：</strong>白光干涉用于确定零光程差位置、测量薄膜厚度与表面形貌（白光干涉轮廓仪），也解释了肥皂泡与油膜的彩色。"))
 )},
]},
]

ch4_sections = [
{
"name": "4.1 惠更斯-菲涅耳原理",
"color": "#0d9488",
"desc": "子波相干叠加的衍射理论基础",
"items": [
{"id":"o4s1-1","name":"惠更斯-菲涅耳原理","tags":["def","der"],"brief":"波前上各点作为子波源相干叠加。",
 "body": wrap(
   exa(p("<strong>例（泊松亮斑）：</strong>按惠更斯-菲涅耳原理，圆盘阴影中心并非全黑，而应出现亮点。")+
   fml("I_{\\text{中心}}\\approx I_0","圆盘完全遮挡几何阴影中心仍亮")+
   p("菲涅耳计算预言并很快被实验证实，成为波动说的有力证据。")+
   note(p("泊松亮斑表明衍射并非边缘的微小修正，而是波动传播的必然结果。")))+
   exa(p("<strong>例（泊松亮斑）：</strong>按惠更斯-菲涅耳原理，圆盘阴影中心并非全黑，而应出现亮点。")+
   fml("I_{\\text{中心}}\\approx I_0","圆盘完全遮挡几何阴影中心仍亮")+
   p("菲涅耳计算预言并很快被实验证实，成为波动说的有力证据。")+
   note(p("泊松亮斑表明衍射并非边缘的微小修正，而是波动传播的必然结果。")))+
   defn("惠更斯-菲涅耳原理",p("波前 $\\Sigma$ 上每一点都可视为发射子波的次波源，各子波在空间某点的相干叠加决定该点的光场。因此衍射本质上是子波的相干叠加。"))+
   der(p("<strong>衍射积分公式：</strong>设波前上 $Q$ 点处面元 $dS$ 的复振幅为 $A(Q)$，到观察点 $P$ 的距离为 $r$，则 $P$ 点合复振幅：")+
   fml("\\tilde{E}(P) = C\\int_\\Sigma \\frac{A(Q)}{r}e^{i(kr-\\omega t)}\\,dS")+
   p("其中 $C$ 为比例常数，倾斜因子已并入。该式称为菲涅耳-基尔霍夫衍射积分，是一切衍射计算的基础。"))+
   note(p("当障碍物尺寸远大于波长时，子波除几何阴影边界附近外相互抵消，回到几何光学直线传播的结果。"))
 )},
]},
{
"name": "4.2 菲涅耳衍射",
"color": "#14b8a6",
"desc": "半波带法、菲涅耳积分与波带片",
"items": [
{"id":"o4s2-1","name":"菲涅耳衍射与半波带法","tags":["der"],"brief":"用半波带定量分析近场衍射。",
 "body": wrap(
   exa(p("<strong>例：</strong>圆孔恰好露出第 1 个半波带时，中心光强最大；露出 2 个半波带时几乎全暗：")+
   fml("A_1=a_1\\ (\\text{最亮}),\\qquad A_2=a_1-a_2\\approx0\\ (\\text{最暗})")+
   p("故随孔径增大，中心光强呈不规则振荡。")+
   note(p("半波带法把复杂的衍射积分化为一维级数求和，是分析近场衍射的简洁工具。")))+
   exa(p("<strong>例：</strong>圆孔恰好露出第 1 个半波带时，中心光强最大；露出 2 个半波带时几乎全暗：")+
   fml("A_1=a_1\\ (\\text{最亮}),\\qquad A_2=a_1-a_2\\approx0\\ (\\text{最暗})")+
   p("故随孔径增大，中心光强呈不规则振荡。")+
   note(p("半波带法把复杂的衍射积分化为一维级数求和，是分析近场衍射的简洁工具。")))+
   defn("半波带",p("以观察点 $P$ 为中心，将球面波前分成一系列环带，使相邻环带到 $P$ 的光程差恰为 $\\lambda/2$，这样的环带称为菲涅耳半波带。"))+
   der(p("<strong>半波带半径与振幅：</strong>设波前到 $P$ 的距离为 $R$，第 $k$ 个半波带半径满足：")+
   fml("r_k = \\sqrt{k\\lambda R}")+
   p("相邻半波带到 $P$ 的相位差为 $\\pi$，故各带在 $P$ 点贡献的振幅符号相反。设第 $k$ 带振幅为 $a_k$，合振幅：")+
   fml("A = a_1 - a_2 + a_3 - a_4 + \\cdots \\approx \\frac{a_1}{2}")+
   p("因 $a_k$ 随 $k$ 缓慢单调减小，故合振幅约等于第一半波带贡献的一半。"))+
   note(p("圆孔衍射中，随孔的大小露出不同数量的半波带，中心可交替出现明暗，这是菲涅耳衍射与夫琅禾费衍射的重要区别。"))
 )},
{"id":"o4s2-2","name":"菲涅耳积分与螺旋","tags":["der"],"brief":"用积分描述近场衍射光强分布。",
 "body": wrap(
   exa(p("<strong>例（科纽螺线）：</strong>自由空间（无遮挡）时衍射积分为螺线两端连线，其长度对应振幅：")+
   fml("|A|=\\frac{1}{\\sqrt2}a_1")+
   p("与半波带法所得 $a_1/2$ 一致（相差常数）。直边衍射时，几何边界处落在螺线中点，光强为 $I_0/4$。")+
   note(p("螺线的卷曲结构决定了直边、狭缝与圆孔衍射光强的振荡规律。")))+
   defn("菲涅耳积分",p("将衍射积分沿波前展开，用菲涅耳积分的组合表达观察点复振幅。"))+
   der(p("<strong>科纽螺线：</strong>定义菲涅耳积分：")+
   fml("C(v)=\\int_0^v \\cos\\frac{\\pi t^2}{2}\\,dt,\\quad S(v)=\\int_0^v \\sin\\frac{\\pi t^2}{2}\\,dt")+
   p("观察点复振幅正比于 $\\{C(v)+iS(v)\\}$，在复平面上描出<strong>科纽螺线</strong>。自由空间（无遮挡）时积分趋于螺线两端的连线，其长度为 $1/\\sqrt2$，对应半波带法的 $a_1/2$ 结果。"))+
   note(p("科纽螺线是分析直边、狭缝、圆孔等菲涅耳衍射的直观工具，曲线绕卷曲点的位置决定光强的振荡。"))
 )},
{"id":"o4s2-3","name":"菲涅耳波带片","tags":["der","app"],"brief":"只让奇数或偶数半波带透光的衍射透镜。",
 "body": wrap(
   exa(p("<strong>例：</strong>波带片第一带半径 $r_1=1.0\\,\\text{mm}$，用于 $\\lambda=633\\,\\text{nm}$：")+
   fml("f=\\frac{r_1^2}{\\lambda}=\\frac{(10^{-3})^2}{633\\times10^{-9}}\\approx1.58\\,\\text{m}")+
   p("该波带片对 633 nm 光在约 1.6 m 处形成强焦点。")+
   note(p("波带片存在多个次焦点 $f/3,f/5,\\cdots$，故单色性差的入射光成像对比度下降。")))+
   exa(p("<strong>例：</strong>波带片第一带半径 $r_1=1.0\\,\\text{mm}$，用于 $\\lambda=633\\,\\text{nm}$：")+
   fml("f=\\frac{r_1^2}{\\lambda}=\\frac{(10^{-3})^2}{633\\times10^{-9}}\\approx1.58\\,\\text{m}")+
   p("该波带片对 633 nm 光在约 1.6 m 处形成强焦点。")+
   note(p("波带片存在多个次焦点 $f/3,f/5,\\cdots$，故单色性差的入射光成像对比度下降。")))+
   defn("波带片",p("遮挡偶数（或奇数）半波带、只让其余半波带透光的屏称为菲涅耳波带片。"))+
   der(p("<strong>焦距：</strong>由半波带半径 $r_k=\\sqrt{k\\lambda R}$，当 $R\\to\\infty$（平行光入射）时第 $k$ 带半径 $r_k\\approx\\sqrt{k\\lambda f}$，故：")+
   fml("f = \\frac{r_1^2}{\\lambda}")+
   p("仅保留奇数带时各带贡献同相叠加，振幅 $A=a_1+a_3+a_5+\\cdots$ 远大于自由传播时的 $a_1/2$，故波带片具有很强的会聚能力。"))+
   app(p("<strong>应用：</strong>波带片可作透镜使用，且能在紫外、X 射线等无法用普通玻璃透镜的波段聚焦；也用于微波准直与成像。"))
 )},
]},
{
"name": "4.3 夫琅禾费衍射",
"color": "#059669",
"desc": "单缝、圆孔衍射与光学仪器分辨率",
"items": [
{"id":"o4s3-1","name":"单缝夫琅禾费衍射","tags":["der","thm"],"brief":"单缝衍射的 sinc² 光强分布。",
 "fig":"singleslit","figCap":"单缝夫琅禾费衍射光强分布",
 "body": wrap(
   exa(p("<strong>例：</strong>缝宽 $a=0.10\\,\\text{mm}$，$\\lambda=500\\,\\text{nm}$，求中央亮纹的角宽度：")+
   fml("\\sin\\theta_1=\\frac{\\lambda}{a}=5\\times10^{-3},\\quad \\Delta\\theta\\approx2\\theta_1\\approx0.57°")+
   p("屏距 $D=1\\,\\text{m}$ 时中央亮纹宽度约 $2\\lambda D/a=10\\,\\text{mm}$。")+
   note(p("缝越窄中央亮纹越宽，衍射现象越明显；缝远大于波长时衍射可忽略，回到几何阴影。")))+
   exa(p("<strong>例：</strong>缝宽 $a=0.10\\,\\text{mm}$，$\\lambda=500\\,\\text{nm}$，求中央亮纹的角宽度：")+
   fml("\\sin\\theta_1=\\frac{\\lambda}{a}=5\\times10^{-3},\\quad \\Delta\\theta\\approx2\\theta_1\\approx0.57°")+
   p("屏距 $D=1\\,\\text{m}$ 时中央亮纹宽度约 $2\\lambda D/a=10\\,\\text{mm}$。")+
   note(p("缝越窄中央亮纹越宽，衍射现象越明显；缝远大于波长时衍射可忽略，回到几何阴影。")))+
   thm("单缝衍射光强分布",p("宽为 $a$ 的单缝，平行光垂直入射，衍射角 $\\theta$ 处光强：")+
   fml("I = I_0\\frac{\\sin^2\\alpha}{\\alpha^2},\\quad \\alpha=\\frac{\\pi a\\sin\\theta}{\\lambda}"))+
   der(p("<strong>推导：</strong>把缝分成无数宽度 $dx$ 的细条，各细条发出子波在 $\\theta$ 方向的相位为 $\\frac{2\\pi}{\\lambda}x\\sin\\theta$。合振幅为积分：")+
   fml("\\tilde{E}(\\theta)=\\int_0^a e^{i\\frac{2\\pi}{\\lambda}x\\sin\\theta}dx = a\\,\\frac{\\sin\\alpha}{\\alpha}e^{i\\alpha}")+
   p("取模平方得光强 $I=I_0\\sin^2\\alpha/\\alpha^2$。极小值出现在 $\\alpha=k\\pi$，即：")+
   fml("a\\sin\\theta = k\\lambda\\ (k=\\pm1,\\pm2,\\dots)","暗纹条件")+
   p("中央主极大宽度为 $2\\lambda/a$，缝越窄衍射越显著。"))+
   note(p("次极大强度迅速衰减，约为中央极大的 4.7%、1.7%、0.8%……"))
 )},
{"id":"o4s3-2","name":"圆孔衍射与艾里斑","tags":["der"],"brief":"圆孔衍射形成中央亮斑（艾里斑）。",
 "fig":"airy","figCap":"圆孔衍射与艾里斑",
 "body": wrap(
   exa(p("<strong>例：</strong>圆孔直径 $D=2\\,\\text{mm}$、$\\lambda=500\\,\\text{nm}$、焦距 $f=1\\,\\text{m}$：")+
   fml("r=1.22\\frac{\\lambda f}{D}=1.22\\times\\frac{500\\times10^{-9}\\times1}{2\\times10^{-3}}\\approx0.31\\,\\text{mm}")+
   p("艾里斑半径约 $0.31\\,\\text{mm}$，约 84% 能量集中其中，外围为迅速衰减的亮环。")+
   note(p("若两点相距小于艾里斑半径即无法分辨，这直接联系到瑞利判据与光学仪器分辨率。")))+
   defn("艾里斑",p("平行光经圆孔衍射，在焦面上形成中央明亮圆斑（艾里斑）与外围同心暗环。"))+
   der(p("<strong>角半径：</strong>圆孔的衍射由含贝塞尔函数的积分描述，第一暗环对应的角半径：")+
   fml("\\theta_1 = 1.22\\frac{\\lambda}{D}")+
   p("其中 $D$ 为圆孔直径。焦面上艾里斑半径 $r=1.22\\lambda f/D$，约 84% 的光能量集中在艾里斑内。"))+
   app(p("<strong>应用：</strong>艾里斑决定成像系统的分辨极限；大口径望远镜与显微镜可获得更小的衍射斑。"))
 )},
{"id":"o4s3-3","name":"光学仪器分辨率","tags":["der","app"],"brief":"瑞利判据决定的极限分辨角。",
 "body": wrap(
   exa(p("<strong>例：</strong>人眼瞳孔 $D=3\\,\\text{mm}$、$\\lambda=550\\,\\text{nm}$：")+
   fml("\\theta_R=1.22\\frac{\\lambda}{D}\\approx2.2\\times10^{-4}\\,\\text{rad}\\approx45''")+
   p("即人眼理论分辨角约 $1'$，与视网膜感光细胞间距相当的观测相符。")+
   note(p("望远镜口径 $D$ 越大 $\\theta_R$ 越小；要看到月面 1 米细节需巨大口径或干涉阵列。")))+
   exa(p("<strong>例：</strong>人眼瞳孔 $D=3\\,\\text{mm}$、$\\lambda=550\\,\\text{nm}$：")+
   fml("\\theta_R=1.22\\frac{\\lambda}{D}\\approx2.2\\times10^{-4}\\,\\text{rad}\\approx45''")+
   p("即人眼理论分辨角约 $1'$，与视网膜感光细胞间距相当的观测相符。")+
   note(p("望远镜口径 $D$ 越大 $\\theta_R$ 越小；要看到月面 1 米细节需巨大口径或干涉阵列。")))+
   defn("瑞利判据",p("当一个点的艾里斑中心恰好落在另一个点艾里斑的第一暗环上时，两像恰能被分辨。"))+
   der(p("<strong>分辨角：</strong>由瑞利判据与艾里斑角半径得最小分辨角：")+
   fml("\\theta_R = 1.22\\frac{\\lambda}{D}")+
   p("望远镜分辨本领 $1/\\theta_R$，显微镜的分辨极限（阿贝极限）为：")+
   fml("\\delta = \\frac{0.61\\lambda}{n\\sin U} = \\frac{0.61\\lambda}{\\text{NA}}")+
   p("提高分辨率需增大口径或数值孔径 NA，或减小波长。"))+
   app(p("<strong>应用：</strong>电子显微镜、紫外光刻、浸没式光刻与超分辨荧光显微技术正是据此突破衍射极限。"))
 )},
]},
{
"name": "4.4 光栅衍射",
"color": "#0d9488",
"desc": "光栅方程、角色散与分辨本领",
"items": [
{"id":"o4s4-1","name":"光栅方程与角色散","tags":["der","thm"],"brief":"多缝干涉与单缝衍射的综合。",
 "fig":"grating","figCap":"光栅衍射主极大方向",
 "body": wrap(
   exa(p("<strong>例：</strong>光栅每毫米 500 条（$d=2\\,\\mu\\text{m}$），$\\lambda=600\\,\\text{nm}$，求第二级衍射角：")+
   fml("\\sin\\theta_2=\\frac{2\\lambda}{d}=\\frac{2\\times600}{2000}=0.60\\Rightarrow\\theta_2\\approx37°")+
   p("该级角色散 $\\frac{d\\theta}{d\\lambda}=\\frac{k}{d\\cos\\theta}\\approx9.4\\times10^5\\,\\text{rad/m}$。")+
   note(p("受 $|\\sin\\theta|\\le1$ 限制，可见光的最高级次约为 $d/\\lambda$。")))+
   exa(p("<strong>例：</strong>光栅每毫米 500 条（$d=2\\,\\mu\\text{m}$），$\\lambda=600\\,\\text{nm}$，求第二级衍射角：")+
   fml("\\sin\\theta_2=\\frac{2\\lambda}{d}=\\frac{2\\times600}{2000}=0.60\\Rightarrow\\theta_2\\approx37°")+
   p("该级角色散 $\\frac{d\\theta}{d\\lambda}=\\frac{k}{d\\cos\\theta}\\approx9.4\\times10^5\\,\\text{rad/m}$。")+
   note(p("受 $|\\sin\\theta|\\le1$ 限制，可见光的最高级次约为 $d/\\lambda$。")))+
   defn("衍射光栅",p("由大量等宽等间距的平行狭缝（缝距 $d$，刻线总数 $N$）构成，是精密分光元件。"))+
   der(p("<strong>光栅方程：</strong>相邻缝在 $\\theta$ 方向的光程差为 $d\\sin\\theta$，多缝干涉主极大条件：")+
   fml("d\\sin\\theta = k\\lambda\\ (k=0,\\pm1,\\pm2,\\dots)","光栅方程")+
   p("实际光强为单缝衍射因子与多缝干涉因子之积，缺级由两者共同决定。角色散表征分光能力：")+
   fml("\\frac{d\\theta}{d\\lambda}=\\frac{k}{d\\cos\\theta}")+
   p("级次越高、缝距越小，色散越大。"))+
   note(p("光栅刻痕（不透光部分）产生的单缝衍射起调制作用，若 $d/a$ 为整数则某些级次缺级。"))
 )},
{"id":"o4s4-2","name":"光栅分辨本领","tags":["der"],"brief":"由刻线总数与级次决定分辨能力。",
 "body": wrap(
   exa(p("<strong>例：</strong>光栅宽 $5\\,\\text{cm}$、每毫米 600 条，在第二级工作：")+
   fml("N=600\\times50=3.0\\times10^4,\\quad R=kN=6.0\\times10^4")+
   p("在 $\\lambda=600\\,\\text{nm}$ 处分辨极限 $\\Delta\\lambda=\\lambda/R=0.010\\,\\text{nm}$。")+
   note(p("光栅分辨本领随级次与刻线数提高，是光谱分析中分辨精细结构的关键指标。")))+
   exa(p("<strong>例：</strong>光栅宽 $5\\,\\text{cm}$、每毫米 600 条，在第二级工作：")+
   fml("N=600\\times50=3.0\\times10^4,\\quad R=kN=6.0\\times10^4")+
   p("在 $\\lambda=600\\,\\text{nm}$ 处分辨极限 $\\Delta\\lambda=\\lambda/R=0.010\\,\\text{nm}$。")+
   note(p("光栅分辨本领随级次与刻线数提高，是光谱分析中分辨精细结构的关键指标。")))+
   defn("分辨本领",p("光栅恰能分开波长差为 $\\Delta\\lambda$ 的两条谱线的能力，定义为 $R=\\lambda/\\Delta\\lambda$。"))+
   der(p("<strong>推导：</strong>第 $k$ 级主极大半角宽为 $\\Delta\\theta=\\frac{\\lambda}{Nd\\cos\\theta}$。两波长在同一级的主极大角间距为 $\\frac{k\\Delta\\lambda}{d\\cos\\theta}$。由瑞利判据令两者相等：")+
   fml("\\frac{k\\Delta\\lambda}{d\\cos\\theta} = \\frac{\\lambda}{Nd\\cos\\theta} \\implies R=\\frac{\\lambda}{\\Delta\\lambda}=kN")+
   p("分辨本领正比于级次 $k$ 与刻线总数 $N$，与缝距无关。"))+
   app(p("<strong>应用：</strong>天文光谱仪、拉曼光谱仪依靠高刻线数光栅分辨精细光谱结构；$N$ 越大光谱越纯。"))
 )},
{"id":"o4s4-3","name":"光栅衍射光强分布","tags":["der"],"brief":"干涉因子与衍射因子的乘积。",
 "body": wrap(
   defn("强度分布",p("光栅的衍射场由单缝衍射与多缝干涉共同决定。"))+
   der(p("<strong>推导：</strong>设缝宽 $a$、缝距 $d$，单缝衍射因子 $\\frac{\\sin\\alpha}{\\alpha}$（$\\alpha=\\pi a\\sin\\theta/\\lambda$），$N$ 缝干涉因子 $\\frac{\\sin N\\beta}{\\sin\\beta}$（$\\beta=\\pi d\\sin\\theta/\\lambda$）。总光强：")+
   fml("I = I_0\\left(\\frac{\\sin\\alpha}{\\alpha}\\right)^2\\left(\\frac{\\sin N\\beta}{\\sin\\beta}\\right)^2")+
   p("当 $\\beta=k\\pi$ 时干涉因子取主极大 $N^2$；主极大之间有 $N-1$ 个次极大与 $N-2$ 个极小，故条纹极细锐。"))+
   note(p("$N$ 越大主极大越亮越窄，正是光栅比双缝更适合精密分光的原因。"))
 )},
]},
{
"name": "4.5 晶体衍射与全息",
"color": "#14b8a6",
"desc": "X 射线布拉格衍射与全息术",
"items": [
{"id":"o4s5-1","name":"X射线衍射与布拉格公式","tags":["der","app"],"brief":"晶体点阵对 X 射线的相干衍射。",
 "body": wrap(
   exa(p("<strong>例：</strong>用 $\\lambda=0.154\\,\\text{nm}$ 的 X 射线，测得一级衍射掠射角 $\\theta=21.7°$：")+
   fml("d=\\frac{\\lambda}{2\\sin\\theta}=\\frac{0.154}{2\\sin21.7°}\\approx0.209\\,\\text{nm}")+
   p("该值正对应 NaCl 晶体的晶面间距。")+
   note(p("不同晶面产生不同衍射角，据此可反推晶体结构与原子排列，是 X 射线晶体学的核心方法。")))+
   exa(p("<strong>例：</strong>用 $\\lambda=0.154\\,\\text{nm}$ 的 X 射线，测得一级衍射掠射角 $\\theta=21.7°$：")+
   fml("d=\\frac{\\lambda}{2\\sin\\theta}=\\frac{0.154}{2\\sin21.7°}\\approx0.209\\,\\text{nm}")+
   p("该值正对应 NaCl 晶体的晶面间距。")+
   note(p("不同晶面产生不同衍射角，据此可反推晶体结构与原子排列，是 X 射线晶体学的核心方法。")))+
   defn("布拉格衍射",p("X 射线波长与晶面间距同量级，晶体规则排列的原子层作为三维光栅对 X 射线产生衍射。"))+
   der(p("<strong>布拉格公式：</strong>相邻晶面间距为 $d$，掠射角为 $\\theta$，两相邻晶面反射线的光程差为 $2d\\sin\\theta$。相干加强条件：")+
   fml("2d\\sin\\theta = k\\lambda")+
   p("该式表明只有特定角度才出现衍射极大，据此可测定晶面间距与晶体结构。"))+
   app(p("<strong>应用：</strong>X 射线晶体学、DNA 双螺旋结构的发现、粉末衍射物相分析、布拉格反射镜。"))
 )},
{"id":"o4s5-2","name":"全息术原理","tags":["der","app"],"brief":"记录并再现光波振幅与相位。",
 "body": wrap(
   exa(p("<strong>例：</strong>以物光 $O$ 与参考光 $R$ 记录，再现时用 $R$ 照明，透射场第三项给出原始物光：")+
   fml("U_3=O|R|^2\\propto O")+
   p("该分量正比于物光波前，包含振幅与相位，故能重建三维立体像。")+
   note(p("再现像的共轭项 $O^*R^2$ 会形成孪生像，需通过离轴参考光或相位恢复技术加以分离。")))+
   defn("全息术",p("利用参考光与物光的干涉，把物体的振幅与相位信息同时记录在全息底片上；再现时用参考光照射即可重建物光波前。"))+
   der(p("<strong>记录与再现：</strong>设物光 $O$、参考光 $R$，底片记录的光强：")+
   fml("I = |O+R|^2 = |O|^2+|R|^2+O^*R+OR^*")+
   p("再现时用参考光 $R$ 照射，透射光含 $R|O|^2$、$OR^*R$ 等项，其中 $O|R|^2$ 项正比于原始物光波前，重建出三维像：")+
   fml("U \\propto (|O|^2+|R|^2)R + O^*R^2 + O|R|^2")+
   p("第三项即再现的物光，包含完整的振幅与相位信息，故能呈现立体感。"))+
   app(p("<strong>应用：</strong>三维显示、全息存储、全息显微、防伪标签与光学测量（全息干涉计量）。"))
 )},
]},
{
"name": "4.6 衍射应用",
"color": "#059669",
"desc": "衍射的工程与现代应用",
"items": [
{"id":"o4s6-1","name":"衍射在分光与测量中的应用","tags":["app","der"],"brief":"光栅光谱仪与衍射计量。",
 "body": wrap(
   exa(p("<strong>例：</strong>用 $\\lambda=632.8\\,\\text{nm}$ 激光，测得单缝第 1 级暗纹与中央的角距离为 $0.63°$：")+
   fml("a=\\frac{\\lambda}{\\sin\\theta_1}=\\frac{632.8\\times10^{-9}}{\\sin0.63°}\\approx5.8\\times10^{-5}\\,\\text{m}")+
   p("即缝宽约 $58\\,\\mu\\text{m}$，说明衍射法可测亚毫米级尺寸。")+
   note(p("利用光栅方程 $d\\sin\\theta=k\\lambda$ 亦可测定光栅常数，精度可达纳米级。")))+
   app(p("衍射是精密分光与测量的基础：光栅光谱仪、单色仪利用光栅衍射分离波长；衍射法可测量微小位移、狭缝宽度与细丝直径。"))+
   der(p("<strong>测量原理：</strong>由单缝衍射暗纹 $a\\sin\\theta=k\\lambda$，测得第 $k$ 级暗纹角位置即可求缝宽：")+
   fml("a = \\frac{k\\lambda}{\\sin\\theta}")+
   p("由光栅方程 $d\\sin\\theta=k\\lambda$ 可测光栅常数；利用衍射条纹的移动可探测角位移与形变。"))+
   note(p("光栅刻划与全息光栅制作本身也依赖衍射和干涉技术。"))
 )},
{"id":"o4s6-2","name":"圆孔与直边的菲涅耳衍射","tags":["der"],"brief":"近场衍射的光强振荡与边缘效应。",
 "body": wrap(
   defn("菲涅耳衍射现象",p("圆孔衍射时，随孔径增大中心光强周期性明暗变化；直边衍射时几何阴影边界外侧出现明暗条纹，内侧光强单调下降。"))+
   der(p("<strong>直边衍射：</strong>用科纽螺线分析，直边外侧光强在几何边界处为自由光强的 $1/4$，随后振荡趋近 $I_0$：")+
   fml("I_{\\text{边}} = \\frac{I_0}{4}\\ \\text{(边界处)}")+
   p("这些近场效应表明几何光学的明暗边界并不锐利，是衍射的普遍表现。"))+
   note(p("菲涅耳衍射与夫琅禾费衍射的区分在于光源与观察面到衍射屏的距离是否有限。"))
 )},
{"id":"o4s6-3","name":"衍射极限与现代应用","tags":["app","der"],"brief":"突破衍射极限的现代光学技术。",
 "body": wrap(
   app(p("衍射极限限制了传统成像与光刻的精度，现代技术通过缩短波长、增大数值孔径或非线性效应突破该极限。"))+
   der(p("<strong>决定因素：</strong>成像分辨极限与光刻线宽均正比于 $\\lambda/\\text{NA}$：")+
   fml("\\delta \\propto \\frac{\\lambda}{\\text{NA}}")+
   p("采用深紫外/极紫外光源、浸没式镜头与相移掩模可显著减小线宽；超分辨显微（STED、PALM/STORM）则利用荧光分子的非线性与单分子定位实现纳米分辨。"))+
   app(p("<strong>应用：</strong>半导体光刻、超分辨荧光显微、光镊与光学操控、衍射光学元件（DOE）与结构光。"))
 )},
]},
]

ch5_sections = [
{
"name": "5.1 偏振光基础",
"color": "#c2410c",
"desc": "自然光、线偏振光与马吕斯、布儒斯特定律",
"items": [
{"id":"o5s1-1","name":"自然光与偏振光","tags":["def","der"],"brief":"光波横振动与偏振态的描述。",
 "body": wrap(
   exa(p("<strong>例：</strong>部分偏振光极大光强 $I_{\\max}=8$、极小 $I_{\\min}=2$：")+
   fml("P=\\frac{I_{\\max}-I_{\\min}}{I_{\\max}+I_{\\min}}=\\frac{8-2}{8+2}=0.6")+
   p("即该光为偏振度 0.6 的部分偏振光，自然光 $P=0$，线偏振光 $P=1$。")+
   note(p("部分偏振光可分解为自然光与线偏振光的叠加，其偏振度随观察方向改变，如天空散射光。")))+
   defn("自然光与偏振光",p("光是横波，电场矢量 $\\mathbf{E}$ 垂直于传播方向。若 $\\mathbf{E}$ 的振动方向恒定，则为<strong>线偏振光</strong>；若各方向振动均匀且无固定相位关系，则为<strong>自然光</strong>；介于两者之间为<strong>部分偏振光</strong>。"))+
   der(p("<strong>自然光的分解：</strong>自然光可等效为两个振幅相等、无固定相位差的垂直偏振分量：")+
   fml("I_x = I_y = \\frac{I_0}{2}")+
   p("自然光通过理想偏振片后光强减半：")+
   fml("I = \\frac{I_0}{2}")+
   p("这正是检验自然光的常用判据。"))+
   note(p("偏振度 $P=(I_{\\max}-I_{\\min})/(I_{\\max}+I_{\\min})$，自然光 $P=0$，线偏振光 $P=1$。"))
 )},
{"id":"o5s1-2","name":"马吕斯定律","tags":["der","thm"],"brief":"线偏振光经检偏器后的强度变化。",
 "body": wrap(
   exa(p("<strong>例：</strong>自然光先通过起偏器，再通过与其透振方向成 $30°$ 的检偏器：")+
   fml("I=\\frac{I_0}{2}\\cos^2 30°=\\frac{I_0}{2}\\times\\frac{3}{4}=\\frac{3}{8}I_0")+
   p("旋转检偏器时透射光强按 $\\cos^2\\theta$ 周期变化，每 $180°$ 出现一次消光。")+
   note(p("两片偏振片正交时完全消光，是检验偏振片性能与制作液晶器件的基本方法。")))+
   exa(p("<strong>例：</strong>自然光先通过起偏器，再通过与其透振方向成 $30°$ 的检偏器：")+
   fml("I=\\frac{I_0}{2}\\cos^2 30°=\\frac{I_0}{2}\\times\\frac{3}{4}=\\frac{3}{8}I_0")+
   p("旋转检偏器时透射光强按 $\\cos^2\\theta$ 周期变化，每 $180°$ 出现一次消光。")+
   note(p("两片偏振片正交时完全消光，是检验偏振片性能与制作液晶器件的基本方法。")))+
   thm("马吕斯定律",p("强度为 $I_0$ 的线偏振光通过偏振化方向与振动方向成 $\\theta$ 角的检偏器后，透射强度：")+
   fml("I = I_0\\cos^2\\theta"))+
   der(p("<strong>推导：</strong>线偏振光振动方向与检偏器透振方向的夹角为 $\\theta$，只有沿透振方向的分量能通过：")+
   fml("E_\\parallel = E_0\\cos\\theta")+
   p("光强正比于振幅平方，故：")+
   fml("I = |E_\\parallel|^2 = I_0\\cos^2\\theta")+
   p("当 $\\theta=0$ 全透，$\\theta=90°$ 全消光。"))+
   app(p("<strong>应用：</strong>两片偏振片即可实现光强调节；结合旋转检偏器可判断偏振态与测量偏振度。"))
 )},
{"id":"o5s1-3","name":"布儒斯特定律","tags":["der","thm"],"brief":"反射光成为完全偏振光的入射角。",
 "fig":"brewster","figCap":"布儒斯特角下的反射与折射",
 "body": wrap(
   exa(p("<strong>例：</strong>玻璃 $n_2=1.50$、空气 $n_1=1.00$，布儒斯特角：")+
   fml("\\theta_B=\\arctan\\frac{1.50}{1.00}\\approx56.3°")+
   p("此时折射角 $\\theta_2=90°-\\theta_B\\approx33.7°$，反射光为完全线偏振光。")+
   note(p("照相机偏振镜正是利用该角度附近的反射光偏振特性，转动滤光片即可削弱水面与玻璃反光。")))+
   exa(p("<strong>例：</strong>玻璃 $n_2=1.50$、空气 $n_1=1.00$，布儒斯特角：")+
   fml("\\theta_B=\\arctan\\frac{1.50}{1.00}\\approx56.3°")+
   p("此时折射角 $\\theta_2=90°-\\theta_B\\approx33.7°$，反射光为完全线偏振光。")+
   note(p("照相机偏振镜正是利用该角度附近的反射光偏振特性，转动滤光片即可削弱水面与玻璃反光。")))+
   thm("布儒斯特定律",p("当入射角 $\\theta_B$ 满足 $\\tan\\theta_B=n_2/n_1$ 时，反射光成为振动方向垂直于入射面的完全偏振光，且反射光与折射光互相垂直。"))+
   der(p("<strong>推导：</strong>反射光的 $p$ 分量（平行于入射面）由菲涅耳公式给出。当反射光与折射光垂直时，$\\theta_B+\\theta_2=90°$，此时 $p$ 分量反射率为零。由折射定律：")+
   fml("n_1\\sin\\theta_B = n_2\\sin(90°-\\theta_B)=n_2\\cos\\theta_B")+
   p("整理得：")+
   fml("\\tan\\theta_B = \\frac{n_2}{n_1}")+
   p("此即布儒斯特角（偏振角）。"))+
   app(p("<strong>应用：</strong>偏振片、激光器布儒斯特窗、摄影中偏振镜消除玻璃与水面反光。"))
 )},
]},
{
"name": "5.2 双折射与晶体光学",
"color": "#ea580c",
"desc": "双折射、o 光与 e 光、偏振器件",
"items": [
{"id":"o5s2-1","name":"双折射现象","tags":["def","der"],"brief":"各向异性晶体中一束光分为两束。",
 "fig":"birefringence","figCap":"双折射产生 o 光与 e 光",
 "body": wrap(
   exa(p("<strong>例：</strong>方解石 $|n_o-n_e|=0.172$，厚度 $d=0.10\\,\\text{mm}$，$\\lambda=589\\,\\text{nm}$：")+
   fml("\\delta=\\frac{2\\pi}{\\lambda}|n_o-n_e|d=\\frac{2\\pi}{589\\times10^{-9}}\\times0.172\\times10^{-4}\\approx183\\pi")+
   p("即两光通过后相位差约 183$\\pi$，等效附加 $\\pi$ 相位。")+
   note(p("双折射使 o 光与 e 光产生可调相位差，是制作波片与偏振干涉器件的基础。")))+
   exa(p("<strong>例：</strong>方解石 $|n_o-n_e|=0.172$，厚度 $d=0.10\\,\\text{mm}$，$\\lambda=589\\,\\text{nm}$：")+
   fml("\\delta=\\frac{2\\pi}{\\lambda}|n_o-n_e|d=\\frac{2\\pi}{589\\times10^{-9}}\\times0.172\\times10^{-4}\\approx183\\pi")+
   p("即两光通过后相位差约 183$\\pi$，等效附加 $\\pi$ 相位。")+
   note(p("双折射使 o 光与 e 光产生可调相位差，是制作波片与偏振干涉器件的基础。")))+
   defn("双折射",p("光进入各向异性晶体（如方解石）后分为两束：一束遵守折射定律的<strong>寻常光（o 光）</strong>，一束不遵守折射定律的<strong>非常光（e 光）</strong>，两者均为线偏振光且振动方向互相垂直。"))+
   der(p("<strong>折射率与相位差：</strong>o 光各方向折射率均为 $n_o$（球面波面），e 光折射率随方向变化（椭球波面），主折射率 $n_e$。通过厚度 $d$ 的晶体后两光相位差：")+
   fml("\\delta = \\frac{2\\pi}{\\lambda}(n_o-n_e)d")+
   p("方解石 $n_o>n_e$ 为负晶体，石英 $n_o<n_e$ 为正晶体。"))+
   note(p("沿光轴方向传播时无双折射，o 光与 e 光速度相同。"))
 )},
{"id":"o5s2-2","name":"o光与e光及晶体光学","tags":["der"],"brief":"波面、光轴与主平面。",
 "body": wrap(
   exa(p("<strong>例：</strong>石英为正晶体（$n_e>n_o$），光轴方向无双折射；垂直光轴方向 e 光折射率取主值 $n_e$。")+
   fml("n(\\theta):\\ \\frac{1}{n_e(\\theta)^2}=\\frac{\\cos^2\\theta}{n_o^2}+\\frac{\\sin^2\\theta}{n_e^2}")+
   p("由惠更斯作图，o 光波面为球面，e 光波面为旋转椭球面，两者仅在光轴处相切。")+
   note(p("正是这一波面差异导致 e 光不遵守普通折射定律，其传播方向与波法线方向一般不同。")))+
   exa(p("<strong>例：</strong>石英为正晶体（$n_e>n_o$），光轴方向无双折射；垂直光轴方向 e 光折射率取主值 $n_e$。")+
   fml("n(\\theta):\\ \\frac{1}{n_e(\\theta)^2}=\\frac{\\cos^2\\theta}{n_o^2}+\\frac{\\sin^2\\theta}{n_e^2}")+
   p("由惠更斯作图，o 光波面为球面，e 光波面为旋转椭球面，两者仅在光轴处相切。")+
   note(p("正是这一波面差异导致 e 光不遵守普通折射定律，其传播方向与波法线方向一般不同。")))+
   defn("晶体光学基本概念",p("<strong>光轴</strong>是晶体中不产生双折射的方向；<strong>主平面</strong>为光线与光轴所决定的平面。o 光振动垂直于主平面，e 光振动在主平面内。"))+
   der(p("<strong>惠更斯作图与波面：</strong>o 光波面为球面（半径 $v_o t$），e 光波面为旋转椭球面。单轴晶体按 $n_e>n_o$（正晶体）或 $n_e<n_o$（负晶体）分类。由惠更斯作图可确定两折射光的方向：")+
   fml("v_o = \\frac{c}{n_o},\\quad v_e(\\theta)=\\frac{c}{n_e(\\theta)}")+
   p("e 光在一般方向的折射率 $\\frac{1}{n_e(\\theta)^2}=\\frac{\\cos^2\\theta}{n_o^2}+\\frac{\\sin^2\\theta}{n_e^2}$。"))+
   note(p("双折射的物理根源是晶体中原子排列的各向异性导致介电常数张量的各向异性。"))
 )},
{"id":"o5s2-3","name":"偏振器件与尼科尔棱镜","tags":["der","app"],"brief":"利用双折射产生纯净线偏振光。",
 "body": wrap(
   defn("偏振分光器件",p("利用双折射晶体的全反射或镀膜分光，把自然光分离为分开的 o 光与 e 光，从而获得线偏振光。"))+
   der(p("<strong>尼科尔棱镜：</strong>将方解石按特定角度剖开并用加拿大树胶粘合，胶的折射率介于 $n_o$ 与 $n_e$ 之间。o 光在胶层发生全反射，e 光透过，故出射为纯净线偏振光。全反射条件：")+
   fml("n_{\\text{胶}} < n_o \\Rightarrow \\sin\\theta_c=\\frac{n_{\\text{胶}}}{n_o}")+
   p("另类的格兰-汤姆逊、格兰-泰勒棱镜则用空气隙实现分光，可承受更高功率。"))+
   app(p("<strong>应用：</strong>激光器起偏、偏振分束器（PBS）、光隔离器与光学实验中的偏振分析。"))
 )},
]},
{
"name": "5.3 相位延迟器件",
"color": "#f97316",
"desc": "波片、椭圆偏振与色偏振",
"items": [
{"id":"o5s3-1","name":"波片与相位延迟","tags":["der","thm"],"brief":"四分之一波片与二分之一波片。",
 "fig":"waveplate","figCap":"波片引入 o、e 光相位差",
 "body": wrap(
   exa(p("<strong>例：</strong>石英 $|n_o-n_e|=0.0091$，$\\lambda=589\\,\\text{nm}$，求 $\\lambda/4$ 波片厚度：")+
   fml("d=\\frac{\\lambda}{4|n_o-n_e|}=\\frac{589\\times10^{-9}}{4\\times0.0091}\\approx1.6\\times10^{-5}\\,\\text{m}")+
   p("即约 16 微米，故实用中常用云母或聚合物薄膜制造波片。")+
   note(p("波片对波长敏感，窄带应用需定标波长；宽带应用可用多个波片组合消色差。")))+
   exa(p("<strong>例：</strong>石英 $|n_o-n_e|=0.0091$，$\\lambda=589\\,\\text{nm}$，求 $\\lambda/4$ 波片厚度：")+
   fml("d=\\frac{\\lambda}{4|n_o-n_e|}=\\frac{589\\times10^{-9}}{4\\times0.0091}\\approx1.6\\times10^{-5}\\,\\text{m}")+
   p("即约 16 微米，故实用中常用云母或聚合物薄膜制造波片。")+
   note(p("波片对波长敏感，窄带应用需定标波长；宽带应用可用多个波片组合消色差。")))+
   defn("波片",p("由单轴晶体制成的平行薄片，光轴平行于表面。o 光与 e 光通过后产生相位差 $\\delta=\\frac{2\\pi}{\\lambda}|n_o-n_e|d$，是相位延迟器件。"))+
   der(p("<strong>常用波片：</strong>令相位差取特定值确定厚度：")+
   fml("\\delta=\\frac{2\\pi}{\\lambda}|n_o-n_e|d=\\begin{cases} \\pi/2, & \\lambda/4\\ \\text{波片}\\\\ \\pi, & \\lambda/2\\ \\text{波片}\\end{cases}")+
   p("即 $d_{\\lambda/4}=\\frac{\\lambda}{4|n_o-n_e|}$，$d_{\\lambda/2}=\\frac{\\lambda}{2|n_o-n_e|}$。"))+
   app(p("<strong>作用：</strong>$\\lambda/4$ 波片把线偏振光变为椭圆/圆偏振光，或反之；$\\lambda/2$ 波片把线偏振方向转过 $2\\alpha$（$\\alpha$ 为入射方向与光轴夹角）。"))
 )},
{"id":"o5s3-2","name":"椭圆与圆偏振光的产生","tags":["der"],"brief":"两垂直分量的合成。",
 "body": wrap(
   exa(p("<strong>例：</strong>$45°$ 线偏振光通过 $\\lambda/4$ 波片（$\\delta=\\pi/2$，$a_1=a_2$）：")+
   fml("E_x=a\\cos\\omega t,\\quad E_y=a\\cos(\\omega t\\pm\\pi/2)=\\mp a\\sin\\omega t")+
   p("合成得 $E_x^2+E_y^2=a^2$，即圆偏振光；符号对应左旋或右旋。")+
   note(p("若夹角不是 $45°$ 或相位差不是 $\\pi/2$，则得椭圆偏振光，其长短轴方向随相位差旋转。")))+
   exa(p("<strong>例：</strong>$45°$ 线偏振光通过 $\\lambda/4$ 波片（$\\delta=\\pi/2$，$a_1=a_2$）：")+
   fml("E_x=a\\cos\\omega t,\\quad E_y=a\\cos(\\omega t\\pm\\pi/2)=\\mp a\\sin\\omega t")+
   p("合成得 $E_x^2+E_y^2=a^2$，即圆偏振光；符号对应左旋或右旋。")+
   note(p("若夹角不是 $45°$ 或相位差不是 $\\pi/2$，则得椭圆偏振光，其长短轴方向随相位差旋转。")))+
   defn("椭圆偏振光",p("两束振动方向垂直、有固定相位差的线偏振光叠加，端点轨迹一般为椭圆，称为椭圆偏振光。"))+
   der(p("<strong>轨迹方程：</strong>设 $E_x=a_1\\cos\\omega t$，$E_y=a_2\\cos(\\omega t+\\delta)$，消去 $t$：")+
   fml("\\frac{E_x^2}{a_1^2}+\\frac{E_y^2}{a_2^2}-\\frac{2E_xE_y}{a_1a_2}\\cos\\delta=\\sin^2\\delta")+
   p("当 $\\delta=\\pm\\pi/2$ 且 $a_1=a_2$ 时退化为圆偏振光：$E_x^2+E_y^2=a^2$；当 $\\delta=0,\\pi$ 时为线偏振光。"))+
   app(p("<strong>产生方法：</strong>线偏振光垂直通过 $\\lambda/4$ 波片且与光轴成 $45°$ 即得圆偏振光；调整夹角可得任意椭圆偏振光。"))
 )},
{"id":"o5s3-3","name":"偏振光的干涉与色偏振","tags":["der"],"brief":"偏振光干涉产生色彩。",
 "body": wrap(
   exa(p("<strong>例：</strong>正交偏振片间放双折射晶片，$\\alpha=45°$ 时透射光强：")+
   fml("I=I_0\\sin^2 2\\alpha\\,\\sin^2\\frac{\\delta}{2}=I_0\\sin^2\\frac{\\delta}{2},\\quad \\delta=\\frac{2\\pi}{\\lambda}(n_o-n_e)d")+
   p("白光下不同波长 $\\delta$ 不同，某些波长被相消、某些被加强，合成即为彩色条纹。")+
   note(p("旋转晶片或改变厚度时颜色随之变化，这为偏光显微镜与应力检测提供了偏振显色手段。")))+
   defn("色偏振",p("两偏振片之间放入双折射晶片，白光的各波长干涉条件不同，透射光呈现彩色，称为色偏振（偏振光干涉）。"))+
   der(p("<strong>干涉条件：</strong>起偏器与检偏器正交时，透射光强：")+
   fml("I = I_0\\sin^2 2\\alpha\\,\\sin^2\\frac{\\delta}{2},\\quad \\delta=\\frac{2\\pi}{\\lambda}(n_o-n_e)d")+
   p("$\\alpha$ 为晶片光轴与起偏方向的夹角。不同波长 $\\lambda$ 对应不同 $\\delta$，故白光入射时某些波长被相消、某些被加强，形成彩色图样。"))+
   app(p("<strong>应用：</strong>偏光显微镜观察矿物与生物晶体、应力分析（光弹）、液晶显示中的色彩控制。"))
 )},
]},
{
"name": "5.4 旋光与琼斯矩阵",
"color": "#c2410c",
"desc": "旋光现象与偏振态的矩阵描述",
"items": [
{"id":"o5s4-1","name":"旋光现象","tags":["der"],"brief":"偏振面在介质中发生旋转。",
 "body": wrap(
   exa(p("<strong>例：</strong>某糖溶液比旋光率 $[\\alpha]=66.5°\\,\\text{mL}/(\\text{dm}\\cdot\\text{g})$，管长 $l=2\\,\\text{dm}$，测得旋光角 $\\alpha=13.3°$：")+
   fml("c=\\frac{\\alpha}{[\\alpha]l}=\\frac{13.3}{66.5\\times2}\\approx0.10\\,\\text{g/mL}")+
   p("由此可快速测定溶液浓度，即旋光法测糖。")+
   note(p("旋光方向与分子手性有关，旋光仪因此成为制药与食品工业的重要分析工具。")))+
   exa(p("<strong>例：</strong>某糖溶液比旋光率 $[\\alpha]=66.5°\\,\\text{mL}/(\\text{dm}\\cdot\\text{g})$，管长 $l=2\\,\\text{dm}$，测得旋光角 $\\alpha=13.3°$：")+
   fml("c=\\frac{\\alpha}{[\\alpha]l}=\\frac{13.3}{66.5\\times2}\\approx0.10\\,\\text{g/mL}")+
   p("由此可快速测定溶液浓度，即旋光法测糖。")+
   note(p("旋光方向与分子手性有关，旋光仪因此成为制药与食品工业的重要分析工具。")))+
   defn("旋光",p("线偏振光通过某些物质（如石英、糖溶液）后，振动面发生旋转，称为旋光。顺时针旋转称右旋，逆时针称左旋。"))+
   der(p("<strong>旋光角公式：</strong>旋转角与光程及浓度成正比：")+
   fml("\\alpha = [\\alpha]_t\\,l\\,c")+
   p("其中 $[\\alpha]_t$ 为比旋光率，$l$ 为光程，$c$ 为溶液浓度。旋光率随波长变化（旋光色散）。"))+
   app(p("<strong>应用：</strong>旋光仪测糖溶液浓度、鉴别手性分子、药物纯度检测；法拉第效应中磁场可使介质产生旋光，用于光隔离器。"))
 )},
{"id":"o5s4-2","name":"琼斯矩阵","tags":["der"],"brief":"用矩阵运算描述偏振态与器件。",
 "body": wrap(
   exa(p("<strong>例：</strong>$\\lambda/4$ 波片（快轴竖直）作用于 $45°$ 线偏振光：")+
   fml("W=\\begin{pmatrix}1&0\\\\0&-i\\end{pmatrix},\\quad \\mathbf{J}_{45}=\\frac{1}{\\sqrt2}\\begin{pmatrix}1\\\\1\\end{pmatrix}")+
   fml("\\mathbf{J}_{\\text{out}}=W\\mathbf{J}_{45}=\\frac{1}{\\sqrt2}\\begin{pmatrix}1\\\\-i\\end{pmatrix}=\\mathbf{J}_R")+
   p("输出为右旋圆偏振光，与几何分析一致。"))+
   note(p("琼斯矩阵使多器件偏振光路的计算化为矩阵连乘，便于系统设计与仿真。"))+
   defn("琼斯矢量与矩阵",p("用二维复矢量 $\\mathbf{J}=\\begin{pmatrix}E_x\\\\E_y\\end{pmatrix}$ 表示偏振态，用 $2\\times2$ 琼斯矩阵表示偏振器件。"))+
   der(p("<strong>典型琼斯矢量：</strong>线偏振（水平/45°）与圆偏振：")+
   fml("\\mathbf{J}_x=\\begin{pmatrix}1\\\\0\\end{pmatrix},\\quad \\mathbf{J}_{45}=\\frac{1}{\\sqrt2}\\begin{pmatrix}1\\\\1\\end{pmatrix},\\quad \\mathbf{J}_R=\\frac{1}{\\sqrt2}\\begin{pmatrix}1\\\\-i\\end{pmatrix}")+
   p("偏振片与波片的琼斯矩阵：")+
   fml("P_\\theta=\\begin{pmatrix}\\cos^2\\theta & \\sin\\theta\\cos\\theta\\\\ \\sin\\theta\\cos\\theta & \\sin^2\\theta\\end{pmatrix},\\quad W_{\\lambda/4}=\\begin{pmatrix}1 & 0\\\\ 0 & -i\\end{pmatrix}")+
   p("多器件串联时总矩阵为各器件矩阵之积 $\\mathbf{J}_{\\text{out}}=M_n\\cdots M_2 M_1\\mathbf{J}_{\\text{in}}$。"))+
   note(p("琼斯矩阵只适用于完全偏振光；部分偏振光需用相干矩阵或斯托克斯参数描述。"))
 )},
]},
{
"name": "5.5 电光与光弹效应",
"color": "#ea580c",
"desc": "应力双折射与电场致双折射",
"items": [
{"id":"o5s5-1","name":"光弹效应","tags":["der","app"],"brief":"应力使各向同性材料产生双折射。",
 "body": wrap(
   defn("光弹效应",p("各向同性透明材料（如玻璃、塑料）受力时变为光学各向异性，产生与应力成正比的双折射，称为光弹效应或应力双折射。"))+
   der(p("<strong>相位差与主应力差：</strong>设主应力差为 $\\sigma_1-\\sigma_2$，材料应力光学系数为 $C$，光程 $d$：")+
   fml("\\delta = 2\\pi C(\\sigma_1-\\sigma_2)\\frac{d}{\\lambda}")+
   p("把模型置于正交偏振片之间，白光下应力集中处呈现彩色条纹，据此读出应力分布。"))+
   app(p("<strong>应用：</strong>光弹应力分析、透明塑料制品内应力检验、光弹调制器与应力传感器。"))
 )},
{"id":"o5s5-2","name":"电光效应","tags":["der","app"],"brief":"电场引起折射率变化（克尔与泡克尔斯）。",
 "body": wrap(
   exa(p("<strong>例：</strong>泡克尔斯晶体电光系数 $r$、长度 $d$，半波电压 $V_\\pi$ 对应相位延迟 $\\pi$：")+
   fml("V_\\pi=\\frac{\\lambda}{2n^3 r}")+
   p("当外加电压为 $V_\\pi/2$ 时相位延迟为 $\\pi/2$，可把线偏振光变为圆偏振光。")+
   note(p("电光调制器以电压高速控制光相位与偏振，是光通信与激光调 Q 的核心器件。")))+
   exa(p("<strong>例：</strong>泡克尔斯晶体电光系数 $r$、长度 $d$，半波电压 $V_\\pi$ 对应相位延迟 $\\pi$：")+
   fml("V_\\pi=\\frac{\\lambda}{2n^3 r}")+
   p("当外加电压为 $V_\\pi/2$ 时相位延迟为 $\\pi/2$，可把线偏振光变为圆偏振光。")+
   note(p("电光调制器以电压高速控制光相位与偏振，是光通信与激光调 Q 的核心器件。")))+
   defn("电光效应",p("外加电场使介质折射率改变，从而改变偏振光的相位，分为与电场平方成正比的克尔效应和有线性关系的泡克尔斯效应。"))+
   der(p("<strong>相位差：</strong>泡克尔斯效应中折射率变化 $\\Delta n\\propto E$，通过电光晶体后相位延迟随电压线性变化：")+
   fml("\\delta = \\frac{2\\pi}{\\lambda}n^3 r E\\,d = \\pi\\frac{V}{V_\\pi}")+
   p("其中 $r$ 为电光系数，$V_\\pi$ 为半波电压。克尔效应则有 $\\Delta n=K E^2$。"))+
   app(p("<strong>应用：</strong>电光调制器、Q 开关、偏振控制器与高速光通信；液晶显示利用电场改变液晶分子取向实现偏振调控。"))
 )},
]},
{
"name": "5.6 偏振应用",
"color": "#f97316",
"desc": "偏振检测、液晶显示与工程应用",
"items": [
{"id":"o5s6-1","name":"偏振光的检测与应用","tags":["app","der"],"brief":"偏振态的鉴别与工程应用。",
 "body": wrap(
   exa(p("<strong>例：</strong>旋转检偏器，光强有两处消光则为线偏振光；强度不变则可能是自然光或圆偏振光。在检偏器前加 $\\lambda/4$ 波片再判别：")+
   fml("\\text{出现消光}\\Rightarrow\\text{圆偏振},\\quad \\text{不消光}\\Rightarrow\\text{自然光}")+
   p("同时用极大极小光强按偏振度公式定量描述部分偏振光。")+
   note(p("偏振检测在偏光显微镜、应力分析与光通信偏振控制中广泛使用。")))+
   app(p("偏振光检测：旋转检偏器观察光强变化即可判别偏振态——自然光强度不变，线偏振光有两消光位置，部分偏振光有极大极小但无消光，圆偏振光强度不变但经 $\\lambda/4$ 波片后变为线偏振。"))+
   der(p("<strong>判别流程：</strong>先用检偏器测极大极小光强得偏振度：")+
   fml("P=\\frac{I_{\\max}-I_{\\min}}{I_{\\max}+I_{\\min}}")+
   p("再在检偏器前加 $\\lambda/4$ 波片，若出现消光则为圆偏振光，否则为部分偏振或椭圆偏振光。"))+
   app(p("<strong>应用：</strong>偏光太阳镜消除反光、摄影偏振镜、应力检测、3D 电影的偏振分像、光通信中的偏振复用。"))
 )},
{"id":"o5s6-2","name":"液晶显示与偏振","tags":["app","der"],"brief":"液晶扭曲调控偏振实现显示。",
 "body": wrap(
   defn("液晶显示原理",p("液晶分子在电场中取向改变，使通过它的偏振光偏振面发生旋转（扭曲向列 TN 模式），配合两片正交偏振片实现明暗控制。"))+
   der(p("<strong>透过率：</strong>无电场时液晶将偏振面旋转 90°，光可通过正交检偏器（亮）；加电场后旋转消失，光被阻挡（暗）。透过率为：")+
   fml("I = I_0\\sin^2 2\\phi\\,\\sin^2\\frac{\\pi\\Delta n\\,d}{\\lambda}")+
   p("通过像素电极独立控制各处电场即可显示图像，彩色则借助滤色片。"))+
   app(p("<strong>应用：</strong>液晶显示器、电子纸、智能窗户与空间光调制器（SLM）——后者正是傅里叶光学中的可编程滤波器。"))
 )},
]},
]

ch6_sections = [
{
"name": "6.1 光的散射",
"color": "#0891b2",
"desc": "瑞利散射、米氏散射、无选择性散射、天空颜色与丁达尔效应",
"items": [
{"id":"o6s1-1","name":"瑞利散射与 λ⁻⁴ 定律","tags":["thm","der"],"brief":"微小颗粒的散射强度与波长四次方成反比。",
 "fig":"rayleigh","figCap":"大气分子对阳光的瑞利散射：蓝光被散射，红光透射",
 "body": wrap(
   thm("瑞利散射定律",p("当散射颗粒尺寸远小于波长（$a\\ll\\lambda$）时，散射光强与波长的四次方成反比：")+
   fml("I_{sca}\\propto\\frac{1}{\\lambda^4}")+
   p("散射强度还正比于颗粒体积平方，并具有 $1+\\cos^2\\theta$ 的方向分布。"))+
   der(p("<strong>推导：</strong>入射光场使颗粒内电子做受迫振动，形成振荡电偶极子 $p=p_0e^{-i\\omega t}$。电偶极辐射功率为：")+
   fml("P=\\frac{\\omega^4|p_0|^2}{12\\pi\\varepsilon_0c^3}\\propto\\omega^4\\propto\\frac{1}{\\lambda^4}")+
   p("因颗粒远小于波长，感生偶极矩 $p_0=\\alpha\\varepsilon_0E_0$ 与频率近似无关，故散射截面：")+
   fml("\\sigma_{sca}=\\frac{8\\pi}{3}k^4|\\alpha|^2=\\frac{128\\pi^5a^6}{3\\lambda^4}\\left|\\frac{m^2-1}{m^2+2}\\right|^2,\\quad m=\\frac{n_{part}}{n_{med}}")+
   p("可见 $\\sigma\\propto\\lambda^{-4}$，蓝光（$450\\,\\text{nm}$）的散射比红光（$650\\,\\text{nm}$）强约 $(650/450)^4\\approx4.4$ 倍。"))+
   app(p("<strong>应用：</strong>解释天空呈蓝色、朝霞晚霞呈红色；浊度计与激光粒度仪利用散射强度反演颗粒尺寸与浓度。"))
 )},
{"id":"o6s1-2","name":"米氏散射","tags":["der","app"],"brief":"颗粒尺寸与波长相当时的散射规律。",
 "body": wrap(
   der(p("<strong>米氏理论：</strong>当 $a\\sim\\lambda$ 时瑞利近似失效，须用米氏理论求解球形颗粒对平面波的严格麦克斯韦方程解，散射截面为：")+
   fml("\\sigma_{Mie}=\\frac{2\\pi}{k^2}\\sum_{l=1}^{\\infty}(2l+1)\\left(|a_l|^2+|b_l|^2\\right)")+
   p("其中 $a_l$、$b_l$ 为米氏系数，由球贝塞尔函数与尺寸参量 $x=2\\pi a/\\lambda$ 决定。"))+
   p("<strong>主要特征：</strong>散射强度对波长的依赖显著减弱（近似 $\\lambda^{-1}$ 甚至更弱），前向散射明显增强，散射光的方向分布出现复杂的花瓣状结构。")+
   app(p("<strong>应用：</strong>云、雾、牛奶与气溶胶对光的散射都属于米氏散射，故云呈白色；激光雷达与大气颗粒物监测依赖米氏散射回波反演。"))
 )},
{"id":"o6s1-3","name":"无选择性散射","tags":["def","der"],"brief":"颗粒远大于波长时各色光被同等散射。",
 "body": wrap(
   defn("无选择性散射",p("当颗粒尺寸 $a\\gg\\lambda$ 时，散射不再依赖于波长，各种颜色的光被同等散射，散射光呈现入射光的颜色（白光入射则散射白光）。"))+
   der(p("<strong>判断依据：</strong>由几何光学极限，大颗粒的散射截面趋于几何截面：")+
   fml("\\sigma\\to2\\pi a^2\\quad(a\\gg\\lambda)")+
   p("式中因子 2 表示几何遮挡与衍射的共同贡献，与 $\\lambda$ 无关，故散射没有颜色选择性。"))+
   exa(p("<strong>例：</strong>云滴半径约 $5\\sim20\\,\\mu\\text{m}$，远大于可见光波长，故乌云、白云均呈灰白色；雾天使能见度下降但景物颜色基本不失真。")+
   note(p("雾灯用黄光并非因黄光散射最弱（长波红光散射更弱），而是黄光在人眼灵敏度、穿透力与警示色之间取得平衡。")))
 )},
{"id":"o6s1-4","name":"大气散射与天空颜色","tags":["der","app"],"brief":"瑞利散射解释天空蓝与朝霞晚霞红。",
 "body": wrap(
   der(p("<strong>天空为何是蓝色：</strong>大气分子（$\\text{N}_2$、$\\text{O}_2$）尺寸约 $0.3\\,\\text{nm}$，远小于可见光波长，满足瑞利散射条件，散射光强与 $\\lambda^{-4}$ 成正比：")+
   fml("\\frac{I_{450}}{I_{650}}=\\left(\\frac{650}{450}\\right)^4\\approx4.4")+
   p("蓝光被散射得更多，来自各方向的散射光进入人眼，故天空呈蓝色。"))+
   der(p("<strong>朝霞晚霞为何是红色：</strong>日出日落时光线斜穿大气，路径长约增加 $1/\\sin\\theta$ 倍，蓝光被大量散射掉，透射光中长波红光占优：")+
   fml("I_{trans}=I_0e^{-\\tau},\\qquad \\tau\\propto\\lambda^{-4}")+
   p("散射损耗的波长选择性使透过光偏红，形成朝霞与晚霞；沙尘、污染（大颗粒）会削弱该效应使天色发白。"))+
   app(p("<strong>应用：</strong>大气散射模型是大气光学与遥感反演的基础；天文观测中的大气消光（瑞利散射加臭氧吸收）需按波长修正。"))
 )},
{"id":"o6s1-5","name":"丁达尔效应","tags":["der","app"],"brief":"含悬浮微粒介质中出现可见光柱。",
 "body": wrap(
   defn("丁达尔效应",p("当一束光通过含悬浮微粒的胶体或浑浊介质时，从侧面可以观察到一条明亮的散射光柱，这一现象称为丁达尔效应，是区分胶体与真溶液的重要判据。"))+
   der(p("<strong>机理与判据：</strong>胶体粒子半径约 $1\\sim100\\,\\text{nm}$，满足 $a\\ll\\lambda$，发生瑞利散射：")+
   fml("I_{sca}\\propto N\\,V^2\\,\\lambda^{-4}")+
   p("散射光强正比于粒子数密度 $N$ 与粒子体积平方 $V^2$，且对短波更敏感，故侧向观察到蓝白色光柱；溶液中的分子太小，散射微弱而无可见光柱。"))+
   app(p("<strong>应用：</strong>丁达尔效应用于鉴别胶体与溶液、演示激光光路；大气中的丁达尔现象形成云隙光（耶稣光）。"))
 )},
]},
{
"name": "6.2 拉曼散射与散射应用",
"color": "#0891b2",
"desc": "拉曼散射、布里渊散射与散射的工程应用",
"items": [
{"id":"o6s2-1","name":"拉曼散射","tags":["der","app"],"brief":"分子振动使散射光发生频移。",
 "body": wrap(
   der(p("<strong>现象与规律：</strong>单色光被分子散射时，除与入射频率相同的瑞利线 $\\nu_0$ 外，还出现对称分布的伴线：")+
   fml("\\nu_s=\\nu_0\\pm\\Delta\\nu_{vib}")+
   p("频移量 $\\Delta\\nu$ 由分子振动（或转动）能级差决定 $h\\Delta\\nu=\\Delta E$，与入射波长无关，故拉曼谱可作为分子指纹。"))+
   der(p("<strong>量子解释：</strong>光子与分子发生非弹性碰撞。光子损失能量交给分子（斯托克斯线，$\\nu_0-\\Delta\\nu$）或从振动激发态分子获得能量（反斯托克斯线，$\\nu_0+\\Delta\\nu$），两者强度比为：")+
   fml("\\frac{I_{as}}{I_{s}}=\\exp\\left(-\\frac{h\\Delta\\nu}{k_BT}\\right)")+
   p("室温下 $h\\Delta\\nu\\gg k_BT$，故斯托克斯线远强于反斯托克斯线。"))+
   app(p("<strong>应用：</strong>拉曼光谱用于化学分析与材料表征；光纤中的自发与受激拉曼散射既是损耗机制，也可用于拉曼光纤放大器与拉曼激光器。"))
 )},
{"id":"o6s2-2","name":"布里渊散射","tags":["der","app"],"brief":"声波引起的光频移散射。",
 "body": wrap(
   der(p("<strong>机理：</strong>光被介质中的声波（声子）散射，由于声速远小于光速，多普勒频移很小，频移量由声速 $v_a$ 与散射角 $\\theta$ 决定：")+
   fml("\\Delta\\nu_B=\\pm\\frac{2nv_a}{\\lambda_0}\\sin\\frac{\\theta}{2}")+
   p("对石英光纤典型值为约 $11\\,\\text{GHz}$（$\\lambda=1550\\,\\text{nm}$、背向散射），比拉曼频移（约 $13\\,\\text{THz}$）小几个量级。"))+
   exa(p("<strong>例：</strong>布里渊光时域反射利用布里渊频移随应变与温度的线性变化，实现分布式应变与温度传感，空间分辨率可达米级。")+
   note(p("受激布里渊散射会限制光纤中可传输的最大光功率，是光纤通信与高功率光纤激光器的重要限制因素。")))
 )},
{"id":"o6s2-3","name":"散射的应用与光纤损耗","tags":["app","der"],"brief":"散射在测量与光纤损耗中的作用。",
 "body": wrap(
   der(p("<strong>散射损耗：</strong>光纤中本征瑞利散射引起的衰减系数近似为：")+
   fml("\\alpha_R=\\frac{A}{\\lambda^4}\\approx0.85\\ \\text{dB/km}\\quad(\\lambda=1550\\,\\text{nm})")+
   p("叠加吸收损耗后，石英光纤总损耗在 $1550\\,\\text{nm}$ 附近最低（约 $0.2\\,\\text{dB/km}$），这正是光通信窗口选择该波长的原因。"))+
   app(p("<strong>测量应用：</strong>浊度计以 $90°$ 散射光强标定浊度（NTU）；激光粒度仪用散射角分布反演粒径；光时域反射计利用后向散射定位光纤断点。"))+
   app(p("<strong>医学与日用品：</strong>光学相干层析利用生物组织散射成像；防晒霜中的 $\\text{TiO}_2$、$\\text{ZnO}$ 颗粒通过散射与吸收屏蔽紫外；牛奶因酪蛋白微粒散射呈白色。"))
 )},
]},
{
"name": "6.3 光的吸收",
"color": "#0891b2",
"desc": "朗伯-比尔定律、复折射率、洛伦兹振子模型",
"items": [
{"id":"o6s3-1","name":"光的吸收与朗伯-比尔定律","tags":["thm","der"],"brief":"吸收使光强随厚度指数衰减。",
 "fig":"absorption","figCap":"朗伯-比尔定律：光强随介质厚度指数衰减",
 "body": wrap(
   thm("朗伯-比尔定律",p("光通过吸收介质时，光强随传播距离按指数规律衰减：")+
   fml("I=I_0e^{-\\alpha l}=I_0\\,10^{-\\varepsilon c l}")+
   p("$\\alpha$ 为线性吸收系数，$\\varepsilon$ 为摩尔吸光系数，$c$ 为吸收物质浓度，$l$ 为光程。"))+
   der(p("<strong>推导：</strong>在厚度 $dx$ 的薄层内，光强的减少量正比于入射光强与该层内吸收粒子数：")+
   fml("-dI=\\alpha I\\,dx\\ \\Rightarrow\\ \\frac{dI}{I}=-\\alpha\\,dx")+
   p("由 $I(0)=I_0$ 积分：")+
   fml("\\int_{I_0}^{I}\\frac{dI'}{I'}=-\\alpha\\int_0^l dx'\\ \\Rightarrow\\ I=I_0e^{-\\alpha l}")+
   p("以粒子数密度 $N$ 与吸收截面 $\\sigma_a$ 表示有 $\\alpha=N\\sigma_a$，与浓度成正比，故可写为 $I=I_010^{-\\varepsilon cl}$，即比尔定律。"))+
   app(p("<strong>应用：</strong>分光光度计据此测定溶液浓度；大气痕量气体（$\\text{NO}_2$、$\\text{SO}_2$）用差分吸收光谱监测。"))
 )},
{"id":"o6s3-2","name":"复折射率与吸收系数","tags":["der"],"brief":"用复折射率统一描述折射与吸收。",
 "body": wrap(
   der(p("<strong>推导：</strong>把折射率推广为复数 $\\tilde{n}=n+i\\kappa$，平面波传播因子变为：")+
   fml("e^{i\\frac{\\omega}{c}(\\tilde{n}z-ct)}=e^{-\\frac{\\omega\\kappa}{c}z}\\,e^{i\\frac{\\omega}{c}(nz-ct)}")+
   p("实部 $n$ 决定相位速度，虚部 $\\kappa$（消光系数）决定振幅的指数衰减。与朗伯定律比较得：")+
   fml("\\alpha=\\frac{2\\omega\\kappa}{c}=\\frac{4\\pi\\kappa}{\\lambda_0}")+
   p("吸收与色散并非独立：$n$ 与 $\\kappa$ 通过克拉默斯-克勒尼希关系相互联系：")+
   fml("n(\\omega)=1+\\frac{2}{\\pi}\\,\\mathcal{P}\\!\\int_0^{\\infty}\\frac{\\omega'\\kappa(\\omega')}{\\omega'^2-\\omega^2}\\,d\\omega'"))+
   note(p("金属的高反射源于其很大的 $\\kappa$；半导体在带边附近的强吸收由 $\\kappa$ 的变化体现，是光电探测器的工作基础。"))
 )},
{"id":"o6s3-3","name":"洛伦兹振子模型","tags":["der","thm"],"brief":"经典电子振子模型统一解释吸收与色散。",
 "body": wrap(
   der(p("<strong>运动方程：</strong>把介质中的束缚电子视为受驱阻尼振子（质量 $m$、本征频率 $\\omega_0$、阻尼 $\\gamma$），在光场 $E=E_0e^{-i\\omega t}$ 驱动下：")+
   fml("m\\ddot{x}+m\\gamma\\dot{x}+m\\omega_0^2x=-eE_0e^{-i\\omega t}")+
   p("稳态解 $x=\\dfrac{-eE_0/m}{\\omega_0^2-\\omega^2-i\\gamma\\omega}e^{-i\\omega t}$。由极化强度 $P=-Nex$ 与 $\\varepsilon_r=1+P/\\varepsilon_0E$ 得：")+
   fml("\\tilde{n}^2=\\tilde{\\varepsilon}_r=1+\\frac{Ne^2}{m\\varepsilon_0}\\cdot\\frac{1}{\\omega_0^2-\\omega^2-i\\gamma\\omega}")+
   p("令 $\\tilde{n}=n+i\\kappa$ 并分离实虚部，即得洛伦兹吸收线型与色散曲线：")+
   fml("\\kappa(\\omega)\\approx\\frac{Ne^2}{2m\\varepsilon_0n}\\cdot\\frac{\\gamma\\omega}{(\\omega_0^2-\\omega^2)^2+\\gamma^2\\omega^2}")+
   p("远离共振时 $n$ 随频率单调增大（正常色散）；共振点附近 $dn/d\\omega$ 反号出现反常色散，同时 $\\kappa$ 达到峰值产生强吸收。"))+
   note(p("洛伦兹模型的量子对应是电偶极跃迁；多共振叠加即塞耳迈耶尔方程，用于描述透明区的折射率。"))
 )},
]},
{
"name": "6.4 色散 群速度与磁光效应",
"color": "#0891b2",
"desc": "正常与反常色散、柯西与塞耳迈耶尔公式、群速度、旋光色散与法拉第效应",
"items": [
{"id":"o6s4-1","name":"正常色散与反常色散","tags":["der","thm"],"brief":"折射率随波长变化的两种规律。",
 "fig":"dispersion","figCap":"色散曲线：正常色散区折射率随波长减小，吸收带附近出现反常色散",
 "body": wrap(
   thm("正常色散与反常色散",p("正常色散：折射率随波长增大而减小，$\\dfrac{dn}{d\\lambda}<0$。反常色散：在吸收带附近 $\\dfrac{dn}{d\\lambda}>0$。"))+
   der(p("<strong>判据：</strong>由洛伦兹模型，远离共振时 $\\tilde{n}\\approx1+\\dfrac{A}{\\omega_0^2-\\omega^2}$，对波长求导：")+
   fml("\\frac{dn}{d\\lambda}=\\frac{dn}{d\\omega}\\cdot\\frac{d\\omega}{d\\lambda}\\approx-\\frac{2\\pi c}{\\lambda^2}\\cdot\\frac{2A\\omega}{(\\omega_0^2-\\omega^2)^2}<0")+
   p("在 $\\omega\\to\\omega_0$ 的共振区，$\\omega_0^2-\\omega^2$ 变号使导数反号，$\\dfrac{dn}{d\\lambda}>0$，即反常色散，同时伴随强吸收。"))+
   exa(p("<strong>例：</strong>普通玻璃在可见光区为正常色散，紫光折射率大于红光；钠蒸气在 D 线附近出现反常色散，可用交叉棱镜法观测。")+
   note(p("反常色散不违反因果律：它只出现在吸收带内，该波段光被强烈吸收，信号传播速度仍由群速度保证不超过 $c$。")))
 )},
{"id":"o6s4-2","name":"柯西公式与塞耳迈耶尔方程","tags":["der","app"],"brief":"描述透明波段色散的经验公式。",
 "body": wrap(
   der(p("<strong>柯西公式：</strong>在远离吸收带的透明区，把洛伦兹模型作长波展开得：")+
   fml("n(\\lambda)=A+\\frac{B}{\\lambda^2}+\\frac{C}{\\lambda^4}")+
   p("$A$、$B$、$C$ 为材料常数，由若干波长的测量值拟合。求导得色散率：")+
   fml("\\frac{dn}{d\\lambda}=-\\frac{2B}{\\lambda^3}-\\frac{4C}{\\lambda^5}<0")+
   p("与正常色散一致。"))+
   der(p("<strong>塞耳迈耶尔方程：</strong>考虑多个吸收共振后更为精确：")+
   fml("n^2(\\lambda)=1+\\sum_i\\frac{B_i\\lambda^2}{\\lambda^2-C_i}")+
   p("它由洛伦兹振子模型对多个共振频率求和得到，能同时覆盖可见与红外波段，是玻璃库标定色散的标准形式。"))+
   app(p("<strong>应用：</strong>光学设计软件用塞耳迈耶尔系数计算色差与设计消色差透镜；光纤中材料色散与波导色散之和决定零色散波长。"))
 )},
{"id":"o6s4-3","name":"群速度与相速度色散","tags":["der","thm"],"brief":"波包传播速度与相速度的区别。",
 "fig":"groupspeed","figCap":"波包由群速度传播，而等相位面以相速度移动",
 "body": wrap(
   der(p("<strong>推导：</strong>两频率相近的单色波叠加形成波包，振幅峰以群速度传播：")+
   fml("v_g=\\frac{d\\omega}{dk}=v_p+k\\frac{dv_p}{dk}=v_p-\\lambda\\frac{dv_p}{d\\lambda}")+
   p("其中 $v_p=\\omega/k=c/n$ 为相速度。代入 $v_p=c/n$ 得：")+
   fml("v_g=\\frac{c}{n}+\\frac{c\\omega}{n^2}\\frac{dn}{d\\omega}=\\frac{c}{n}\\left(1+\\frac{\\lambda}{n}\\frac{dn}{d\\lambda}\\right)^{-1}")+
   p("正常色散时 $\\dfrac{dn}{d\\lambda}<0$，$v_g<v_p$；反常色散时 $v_g>v_p$，但此时波形严重畸变，信息速度仍不超过 $c$。"))+
   app(p("<strong>应用：</strong>光纤中不同波长的群速度不同造成脉冲展宽，限制传输带宽；色散补偿光纤与啁啾光栅用于抵消累积色散。"))
 )},
{"id":"o6s4-4","name":"旋光色散与法拉第效应","tags":["der","app"],"brief":"偏振面旋转随波长与磁场变化。",
 "body": wrap(
   der(p("<strong>旋光色散：</strong>旋光介质的偏振面旋转角随波长变化，由毕奥定律：")+
   fml("\\alpha=[\\alpha]_\\lambda\\,l\\,c,\\qquad [\\alpha]_\\lambda\\propto\\frac{1}{\\lambda^2}")+
   p("短波旋转更强，故白光通过旋光介质后各色偏振面转角不同，形成旋光色散。其微观来源是左右旋圆偏振光折射率不同：")+
   fml("\\alpha=\\frac{\\pi l}{\\lambda}(n_L-n_R)"))+
   der(p("<strong>法拉第效应：</strong>外加磁场使介质产生圆双折射，偏振面旋转角正比于磁场与光程：")+
   fml("\\alpha=V\\,B\\,l")+
   p("$V$ 为费尔德常数。与天然旋光不同，法拉第旋转的方向由磁场方向决定而与光的传播方向无关，故光往返一次旋转角加倍，可制成光隔离器。"))+
   app(p("<strong>应用：</strong>光隔离器、磁光调制器、磁场与电流传感（法拉第传感器）、磁光存储；旋光色散亦用于研究材料中的载流子浓度。"))
 )},
]},
]

CHAPTERS = [
    {"id":"o-ch1","num":"第一章","title":"几何光学","en":"GEOMETRICAL OPTICS",
     "desc":"光的直线传播、反射与折射定律、费马原理、全反射与光纤、棱镜色散、球面镜与球面折射成像、薄透镜与透镜制造者公式、组合透镜、光学仪器、光阑与光度学。",
     "sections": ch1_sections},
    {"id":"o-ch2","num":"第二章","title":"波动光学基础","en":"WAVE OPTICS",
     "desc":"光的电磁本性、麦克斯韦波动方程、平面波解、光速与折射率、光强与振幅、单色波与波列、相位与光程、光程差、波前与波面、惠更斯原理、叠加原理、坡印廷矢量、偏振态基础、空间与时间相干性、相干长度、光谱与色散基础。",
     "sections": ch2_sections},
    {"id":"o-ch3","num":"第三章","title":"干涉","en":"INTERFERENCE",
     "desc":"相干条件与光程差、杨氏双缝干涉、分波前干涉、薄膜等倾与等厚干涉、牛顿环、迈克尔逊与法布里-珀罗干涉仪、相干性与干涉应用。",
     "sections": ch3_sections},
    {"id":"o-ch4","num":"第四章","title":"衍射","en":"DIFFRACTION",
     "desc":"惠更斯-菲涅耳原理、菲涅耳衍射与波带片、单缝与圆孔夫琅禾费衍射、光学仪器分辨率、光栅衍射、布拉格衍射与全息。",
     "sections": ch4_sections},
    {"id":"o-ch5","num":"第五章","title":"偏振","en":"POLARIZATION",
     "desc":"自然光与偏振光、马吕斯定律、布儒斯特定律、双折射与晶体光学、波片与椭圆偏振、偏振光干涉与色偏振、旋光与琼斯矩阵、电光效应与偏振应用。",
     "sections": ch5_sections},
    {"id":"o-ch6","num":"第六章","title":"散射 吸收 色散","en":"SCATTERING · ABSORPTION · DISPERSION",
     "desc":"瑞利散射与 λ⁻⁴ 定律、米氏散射、无选择性散射、大气散射与天空颜色、丁达尔效应、拉曼与布里渊散射、朗伯-比尔定律、复折射率、洛伦兹振子模型、正常与反常色散、柯西与塞耳迈耶尔公式、群速度色散、旋光色散与法拉第效应。",
     "sections": ch6_sections},
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
  .la-phase-title.o-ch1::before{background:#2563eb}
  .la-phase-title.o-ch2::before{background:#7c3aed}
  .la-phase-title.o-ch3::before{background:#0d9488}
  .la-phase-title.o-ch4::before{background:#c2410c}
  .la-phase-title.o-ch5::before{background:#be185d}
  .la-phase-title.o-ch6::before{background:#0891b2}
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
<meta name="description" content="光学知识体系：几何光学、波动光学基础、干涉、衍射、偏振、散射吸收色散">
<title>光学 · 知识体系</title>
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
    <div class="la-eyebrow">OPTICS · KNOWLEDGE MAP</div>
    <h1>光学 · 知识体系</h1>
    <p class="la-subtitle">几何光学 · 波动光学基础 · 干涉 · 衍射 · 偏振 · 散射吸收色散</p>
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
    <div>光学 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于光学核心知识体系整理</div>
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
    with open("/workspace/optics.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated optics.html ({len(html)} chars)")
