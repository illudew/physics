# -*- coding: utf-8 -*-
"""Generate statistical-mechanics.html with 7 chapters: 热力学与统计物理."""
import json

FIG = {
"system": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="20" y="20" width="140" height="120" fill="#fee2e2" stroke="#dc2626" stroke-width="1.8" rx="6"/>
<text x="62" y="84" font-size="14" fill="#7f1d1d" font-weight="bold">系统</text>
<text x="52" y="104" font-size="11" fill="#991b1b">P,V,T,U,S</text>
<rect x="170" y="10" width="60" height="140" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 4" rx="6"/>
<text x="180" y="80" font-size="11" fill="#475569">外界</text>
<text x="176" y="96" font-size="9" fill="#64748b">热源</text>
<line x1="160" y1="60" x2="172" y2="60" stroke="#dc2626" stroke-width="1.5" marker-end="url(#ar)"/>
<text x="140" y="54" font-size="10" fill="#dc2626">Q</text>
<line x1="160" y1="100" x2="172" y2="100" stroke="#0891b2" stroke-width="1.5" marker-end="url(#ar2)"/>
<text x="140" y="96" font-size="10" fill="#0891b2">W</text>
<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#dc2626"/></marker>
<marker id="ar2" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#0891b2"/></marker></defs>
</svg>''',
"pvdiagram": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<polygon points="224,130 216,126 216,134" fill="#475569"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<polygon points="34,20 30,28 38,28" fill="#475569"/>
<text x="210" y="148" font-size="11" fill="#475569">V</text>
<text x="14" y="26" font-size="11" fill="#475569">P</text>
<path d="M 60 100 C 100 70 150 50 200 42" fill="none" stroke="#dc2626" stroke-width="2"/>
<text x="168" y="38" font-size="10" fill="#dc2626">T₁ 等温</text>
<path d="M 60 118 C 110 100 160 92 200 88" fill="none" stroke="#0891b2" stroke-width="2" stroke-dasharray="5 3"/>
<text x="172" y="84" font-size="10" fill="#0891b2">T₂<T₁</text>
<circle cx="120" cy="60" r="3" fill="#dc2626"/>
<text x="126" y="56" font-size="10" fill="#1e293b">A</text>
<circle cx="180" cy="100" r="3" fill="#0891b2"/>
<text x="186" y="100" font-size="10" fill="#1e293b">B</text>
</svg>''',
"carnot": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<polygon points="224,130 216,126 216,134" fill="#475569"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<text x="210" y="148" font-size="11" fill="#475569">V</text>
<text x="14" y="26" font-size="11" fill="#475569">P</text>
<path d="M 60 110 C 110 70 160 56 200 50" fill="none" stroke="#dc2626" stroke-width="2"/>
<path d="M 60 110 C 70 96 80 84 90 78" fill="none" stroke="#0d9488" stroke-width="2"/>
<path d="M 90 78 C 140 50 180 44 210 42" fill="none" stroke="#dc2626" stroke-width="2"/>
<path d="M 210 42 C 180 60 150 90 130 116" fill="none" stroke="#0d9488" stroke-width="2"/>
<text x="40" y="124" font-size="9" fill="#dc2626">1(T₁)</text>
<text x="84" y="70" font-size="9" fill="#0d9488">2绝</text>
<text x="196" y="54" font-size="9" fill="#dc2626">3(T₂)</text>
<text x="118" y="124" font-size="9" fill="#0d9488">4绝</text>
</svg>''',
"entropy": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="60" cy="80" r="34" fill="#fef2f2" stroke="#dc2626" stroke-width="1.6"/>
<text x="38" y="78" font-size="11" fill="#7f1d1d">可逆</text>
<text x="36" y="94" font-size="10" fill="#991b1b">∮δQ/T=0</text>
<path d="M 110 80 A 40 40 0 1 1 110 80.001" fill="none" stroke="#0891b2" stroke-width="1.6" stroke-dasharray="5 3"/>
<text x="150" y="50" font-size="11" fill="#0e7490">不可逆</text>
<text x="142" y="118" font-size="10" fill="#0e7490">ΔS ≥ 0</text>
<path d="M 200 50 C 210 80 210 110 200 130" fill="none" stroke="#dc2626" stroke-width="2"/>
<polygon points="200,130 195,121 205,121" fill="#dc2626"/>
<text x="196" y="44" font-size="10" fill="#dc2626">S</text>
<text x="168" y="148" font-size="10" fill="#64748b">熵增原理</text>
</svg>''',
"potentials": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<text x="20" y="30" font-size="11" fill="#1e293b" font-weight="bold">U(S,V)</text>
<text x="160" y="30" font-size="11" fill="#1e293b" font-weight="bold">H(S,P)</text>
<text x="20" y="130" font-size="11" fill="#1e293b" font-weight="bold">F(T,V)</text>
<text x="160" y="130" font-size="11" fill="#1e293b" font-weight="bold">G(T,P)</text>
<line x1="70" y1="26" x2="150" y2="26" stroke="#ea580c" stroke-width="1.8" marker-end="url(#ah)"/>
<text x="84" y="20" font-size="10" fill="#ea580c">+PV</text>
<line x1="180" y1="40" x2="180" y2="116" stroke="#ea580c" stroke-width="1.8" marker-end="url(#ah)"/>
<text x="184" y="80" font-size="10" fill="#ea580c">-TS</text>
<line x1="40" y1="40" x2="40" y2="116" stroke="#ea580c" stroke-width="1.8" marker-end="url(#ah)"/>
<text x="12" y="80" font-size="10" fill="#ea580c">-TS</text>
<line x1="70" y1="126" x2="150" y2="126" stroke="#ea580c" stroke-width="1.8" marker-end="url(#ah)"/>
<text x="84" y="142" font-size="10" fill="#ea580c">+PV</text>
<defs><marker id="ah" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="#ea580c"/></marker></defs>
</svg>''',
"maxwell": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="14" y="14" width="100" height="60" fill="#faf7ff" stroke="#8b5cf6" stroke-width="1.4" rx="6"/>
<text x="22" y="38" font-size="11" fill="#5b21b6">dU=TdS-PdV</text>
<text x="22" y="58" font-size="9" fill="#7c3aed">(∂T/∂V)S=-(∂P/∂S)V</text>
<rect x="126" y="14" width="100" height="60" fill="#f0f9ff" stroke="#0ea5e9" stroke-width="1.4" rx="6"/>
<text x="134" y="38" font-size="11" fill="#0369a1">dH=TdS+VdP</text>
<text x="134" y="58" font-size="9" fill="#0284c7">(∂T/∂P)S=(∂V/∂S)P</text>
<rect x="14" y="86" width="100" height="60" fill="#f0fdf4" stroke="#10b981" stroke-width="1.4" rx="6"/>
<text x="22" y="110" font-size="11" fill="#15803d">dF=-SdT-PdV</text>
<text x="22" y="130" font-size="9" fill="#16a34a">(∂S/∂V)T=(∂P/∂T)V</text>
<rect x="126" y="86" width="100" height="60" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.4" rx="6"/>
<text x="134" y="110" font-size="11" fill="#b45309">dG=-SdT+VdP</text>
<text x="134" y="130" font-size="9" fill="#d97706">(∂S/∂P)T=-(∂V/∂T)P</text>
</svg>''',
"clapeyron": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<text x="210" y="148" font-size="11" fill="#475569">T</text>
<text x="14" y="26" font-size="11" fill="#475569">P</text>
<path d="M 50 120 C 80 90 120 50 200 30" fill="none" stroke="#d97706" stroke-width="2"/>
<circle cx="120" cy="66" r="3.5" fill="#d97706"/>
<text x="126" y="60" font-size="10" fill="#1e293b">T, P</text>
<text x="60" y="40" font-size="10" fill="#d97706">气相</text>
<text x="150" y="110" font-size="10" fill="#d97706">液相</text>
<line x1="120" y1="66" x2="170" y2="48" stroke="#475569" stroke-width="1.2" stroke-dasharray="4 3"/>
<text x="174" y="46" font-size="10" fill="#475569">dp/dT</text>
</svg>''',
"phasetrans": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="120" x2="200" y2="120" stroke="#475569" stroke-width="1.2"/>
<line x1="120" y1="20" x2="120" y2="120" stroke="#ef4444" stroke-width="1.4" stroke-dasharray="5 3"/>
<text x="100" y="140" font-size="11" fill="#475569">T</text>
<text x="126" y="14" font-size="10" fill="#ef4444">Tc</text>
<path d="M 50 110 L 120 110 L 120 50 L 200 50" fill="none" stroke="#dc2626" stroke-width="2"/>
<text x="160" y="44" font-size="9" fill="#dc2626">一级相变 μ 不连续</text>
<path d="M 50 110 C 90 108 110 90 120 70 C 130 50 160 44 200 40" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="5 3"/>
<text x="160" y="30" font-size="9" fill="#7c3aed">二级相变 连续</text>
<text x="20" y="114" font-size="10" fill="#1e293b">μ</text>
</svg>''',
"vanderwaals": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<text x="210" y="148" font-size="11" fill="#475569">V</text>
<text x="14" y="26" font-size="11" fill="#475569">P</text>
<path d="M 50 60 C 70 60 90 70 110 100 C 130 130 150 110 170 80 C 190 50 210 44 220 42" fill="none" stroke="#d97706" stroke-width="2"/>
<line x1="80" y1="92" x2="180" y2="92" stroke="#dc2626" stroke-width="1.4" stroke-dasharray="5 3"/>
<circle cx="120" cy="100" r="3.5" fill="#dc2626"/>
<text x="86" y="86" font-size="9" fill="#dc2626">T<Tc 范德瓦尔斯</text>
<text x="120" y="118" font-size="9" fill="#475569">气液共存</text>
</svg>''',
"critical": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<text x="210" y="148" font-size="11" fill="#475569">ρ</text>
<text x="14" y="26" font-size="11" fill="#475569">T</text>
<path d="M 60 120 C 100 110 130 70 140 40" fill="none" stroke="#dc2626" stroke-width="2"/>
<path d="M 60 120 C 90 122 120 110 140 40" fill="none" stroke="#dc2626" stroke-width="2"/>
<circle cx="140" cy="40" r="5" fill="#dc2626"/>
<text x="146" y="36" font-size="11" fill="#7f1d1d" font-weight="bold">临界点</text>
<text x="146" y="52" font-size="9" fill="#991b1b">(ρc,Tc)</text>
<line x1="140" y1="40" x2="140" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<text x="60" y="100" font-size="10" fill="#d97706">气液共存</text>
</svg>''',
"landau": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="120" y1="140" x2="120" y2="20" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="140" x2="210" y2="140" stroke="#475569" stroke-width="1.2"/>
<text x="124" y="22" font-size="10" fill="#475569">F</text>
<text x="214" y="144" font-size="10" fill="#475569">M</text>
<path d="M 40 60 Q 120 130 200 60" fill="none" stroke="#d97706" stroke-width="2"/>
<text x="150" y="100" font-size="9" fill="#d97706">T>Tc 单阱</text>
<path d="M 40 40 Q 80 100 100 70 Q 120 40 140 70 Q 160 100 200 40" fill="none" stroke="#7c3aed" stroke-width="2" stroke-dasharray="5 3"/>
<text x="150" y="30" font-size="9" fill="#7c3aed">T<Tc 双阱</text>
<circle cx="90" cy="70" r="3" fill="#7c3aed"/>
<circle cx="150" cy="70" r="3" fill="#7c3aed"/>
</svg>''',
"phasespace": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="30" width="180" height="100" fill="#f0fdfa" stroke="#0d9488" stroke-width="1.5" rx="6"/>
<text x="36" y="24" font-size="10" fill="#0f766e">μ 空间 (q, p)</text>
<g fill="#0d9488">
<circle cx="60" cy="60" r="2.5"/><circle cx="90" cy="80" r="2.5"/><circle cx="130" cy="50" r="2.5"/>
<circle cx="170" cy="90" r="2.5"/><circle cx="110" cy="110" r="2.5"/><circle cx="190" cy="70" r="2.5"/>
<circle cx="75" cy="100" r="2.5"/><circle cx="150" cy="100" r="2.5"/>
</g>
<line x1="30" y1="30" x2="210" y2="30" stroke="#94a3b8"/>
<line x1="30" y1="30" x2="30" y2="130" stroke="#94a3b8"/>
<text x="196" y="124" font-size="10" fill="#475569">q</text>
<text x="20" y="34" font-size="10" fill="#475569">p</text>
<text x="60" y="150" font-size="10" fill="#64748b">微观状态数 Ω ∝ 相空间体积</text>
</svg>''',
"boltzmann": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<text x="210" y="148" font-size="11" fill="#475569">E</text>
<text x="14" y="26" font-size="11" fill="#475569">P</text>
<path d="M 40 40 C 80 60 140 110 220 126" fill="none" stroke="#0d9488" stroke-width="2"/>
<text x="120" y="70" font-size="11" fill="#0f766e">P ∝ e^{-βE}</text>
<rect x="36" y="110" width="20" height="20" fill="#0d9488" opacity="0.5"/>
<rect x="76" y="92" width="20" height="38" fill="#0d9488" opacity="0.5"/>
<rect x="116" y="66" width="20" height="64" fill="#0d9488" opacity="0.5"/>
</svg>''',
"maxwelldist": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<text x="210" y="148" font-size="11" fill="#475569">v</text>
<text x="14" y="26" font-size="11" fill="#475569">f(v)</text>
<path d="M 40 128 Q 80 40 120 128" fill="none" stroke="#0d9488" stroke-width="2"/>
<path d="M 40 128 Q 90 30 140 128" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="5 3"/>
<path d="M 40 128 Q 70 60 100 128" fill="none" stroke="#0891b2" stroke-width="1.6" stroke-dasharray="3 3"/>
<text x="120" y="34" font-size="9" fill="#dc2626">高温</text>
<text x="96" y="64" font-size="9" fill="#0d9488">低温</text>
<text x="60" y="150" font-size="10" fill="#64748b">v_p < ⟨v⟩ < v_rms</text>
</svg>''',
"equipartition": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="70" cy="80" r="12" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
<text x="64" y="84" font-size="10" fill="#1e40af">单</text>
<text x="40" y="120" font-size="9" fill="#2563eb">3 平动 → 3/2 kT</text>
<line x1="110" y1="60" x2="130" y2="60" stroke="#dc2626" stroke-width="2"/>
<circle cx="110" cy="60" r="6" fill="#fee2e2" stroke="#dc2626"/>
<circle cx="130" cy="60" r="6" fill="#fee2e2" stroke="#dc2626"/>
<text x="100" y="120" font-size="9" fill="#dc2626">双原子: 3平+2转+2振</text>
<line x1="180" y1="50" x2="200" y2="50" stroke="#7c3aed" stroke-width="2"/>
<line x1="180" y1="50" x2="190" y2="70" stroke="#7c3aed" stroke-width="2"/>
<line x1="200" y1="50" x2="190" y2="70" stroke="#7c3aed" stroke-width="2"/>
<circle cx="180" cy="50" r="5" fill="#ede9fe" stroke="#7c3aed"/>
<circle cx="200" cy="50" r="5" fill="#ede9fe" stroke="#7c3aed"/>
<circle cx="190" cy="70" r="5" fill="#ede9fe" stroke="#7c3aed"/>
<text x="168" y="120" font-size="9" fill="#7c3aed">多原子 f≥6</text>
</svg>''',
"ensemble": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<g fill="#f1f5f9" stroke="#94a3b8" stroke-width="1">
<rect x="14" y="14" width="50" height="34" rx="4"/>
<rect x="74" y="14" width="50" height="34" rx="4"/>
<rect x="134" y="14" width="50" height="34" rx="4"/>
<rect x="194" y="14" width="32" height="34" rx="4"/>
<rect x="14" y="58" width="50" height="34" rx="4"/>
<rect x="74" y="58" width="50" height="34" rx="4"/>
<rect x="134" y="58" width="50" height="34" rx="4"/>
<rect x="194" y="58" width="32" height="34" rx="4"/>
<rect x="14" y="102" width="50" height="34" rx="4"/>
<rect x="74" y="102" width="50" height="34" rx="4"/>
<rect x="134" y="102" width="50" height="34" rx="4"/>
<rect x="194" y="102" width="32" height="34" rx="4"/>
</g>
<text x="22" y="34" font-size="9" fill="#0d9488">V,N,T</text>
<text x="82" y="34" font-size="9" fill="#0d9488">V,N,T</text>
<text x="142" y="34" font-size="9" fill="#0d9488">V,N,T</text>
<text x="30" y="78" font-size="9" fill="#0d9488">V,N,T</text>
<text x="90" y="78" font-size="9" fill="#0d9488">V,N,T</text>
<text x="150" y="78" font-size="9" fill="#0d9488">V,N,T</text>
<text x="60" y="156" font-size="10" fill="#64748b">系综：大量同宏观条件副本</text>
</svg>''',
"canonical": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="14" y="14" width="100" height="132" fill="#e0f2fe" stroke="#0ea5e9" stroke-width="1.6" rx="6"/>
<text x="32" y="34" font-size="11" fill="#0369a1" font-weight="bold">系统</text>
<text x="28" y="52" font-size="10" fill="#075985">E 可变</text>
<text x="28" y="70" font-size="10" fill="#075985">N,V 固定</text>
<rect x="126" y="14" width="100" height="132" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.6" stroke-dasharray="5 4" rx="6"/>
<text x="140" y="34" font-size="11" fill="#b45309" font-weight="bold">热源 T</text>
<text x="140" y="54" font-size="10" fill="#92400e">巨大 Cv</text>
<text x="140" y="72" font-size="10" fill="#92400e">温度恒定</text>
<line x1="114" y1="80" x2="126" y2="80" stroke="#dc2626" stroke-width="2"/>
<text x="100" y="74" font-size="10" fill="#dc2626">热交换</text>
</svg>''',
"grand": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="14" y="14" width="96" height="132" fill="#e0f2fe" stroke="#0ea5e9" stroke-width="1.6" rx="6"/>
<text x="32" y="34" font-size="11" fill="#0369a1" font-weight="bold">系统</text>
<text x="28" y="52" font-size="10" fill="#075985">E,N 可变</text>
<text x="28" y="70" font-size="10" fill="#075985">V 固定</text>
<g fill="#0ea5e9"><circle cx="60" cy="100" r="2"/><circle cx="72" cy="108" r="2"/><circle cx="50" cy="116" r="2"/><circle cx="66" cy="124" r="2"/></g>
<rect x="126" y="14" width="100" height="132" fill="#ede9fe" stroke="#8b5cf6" stroke-width="1.6" stroke-dasharray="5 4" rx="6"/>
<text x="140" y="34" font-size="11" fill="#5b21b6" font-weight="bold">粒子库 μ,T</text>
<text x="140" y="54" font-size="10" fill="#6d28d9">μ 化学势</text>
<g fill="#8b5cf6"><circle cx="160" cy="100" r="2"/><circle cx="172" cy="108" r="2"/><circle cx="150" cy="116" r="2"/><circle cx="186" cy="124" r="2"/><circle cx="198" cy="100" r="2"/></g>
<line x1="110" y1="80" x2="126" y2="80" stroke="#dc2626" stroke-width="2"/>
</svg>''',
"bosefermi": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<text x="210" y="148" font-size="11" fill="#475569">ε</text>
<text x="14" y="26" font-size="11" fill="#475569">n̄</text>
<line x1="34" y1="60" x2="200" y2="60" stroke="#dc2626" stroke-width="2"/>
<text x="206" y="56" font-size="10" fill="#dc2626">玻尔兹曼</text>
<path d="M 60 120 C 90 118 110 110 130 50 C 150 20 180 14 210 12" fill="none" stroke="#7c3aed" stroke-width="2"/>
<text x="160" y="30" font-size="9" fill="#7c3aed">费米</text>
<path d="M 60 30 C 90 32 110 40 130 100 C 150 124 180 128 210 130" fill="none" stroke="#0d9488" stroke-width="2" stroke-dasharray="5 3"/>
<text x="160" y="118" font-size="9" fill="#0d9488">玻色</text>
<line x1="130" y1="60" x2="130" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<text x="130" y="142" font-size="9" fill="#94a3b8">μ</text>
</svg>''',
"planck": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<text x="210" y="148" font-size="11" fill="#475569">λ</text>
<text x="14" y="26" font-size="11" fill="#475569">u</text>
<path d="M 50 128 Q 90 40 130 128" fill="none" stroke="#dc2626" stroke-width="2"/>
<path d="M 50 128 Q 110 30 170 128" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5 3"/>
<path d="M 50 128 Q 150 24 210 128" fill="none" stroke="#0891b2" stroke-width="2" stroke-dasharray="3 3"/>
<text x="78" y="56" font-size="9" fill="#dc2626">T₁</text>
<text x="150" y="50" font-size="9" fill="#f59e0b">T₂>T₁</text>
<text x="180" y="44" font-size="9" fill="#0891b2">T₃</text>
<text x="60" y="152" font-size="10" fill="#64748b">普朗克黑体辐射谱</text>
</svg>''',
"fermi": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<text x="210" y="148" font-size="11" fill="#475569">ε</text>
<text x="14" y="26" font-size="11" fill="#475569">n(ε)</text>
<line x1="34" y1="40" x2="130" y2="40" stroke="#4f46e5" stroke-width="2"/>
<line x1="130" y1="40" x2="130" y2="130" stroke="#4f46e5" stroke-width="2"/>
<line x1="130" y1="130" x2="210" y2="130" stroke="#4f46e5" stroke-width="2"/>
<text x="136" y="28" font-size="10" fill="#4f46e5">T=0</text>
<path d="M 40 40 C 90 40 120 50 130 86 C 140 110 170 128 210 130" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="5 3"/>
<text x="150" y="74" font-size="9" fill="#dc2626">T>0</text>
<line x1="130" y1="40" x2="130" y2="130" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<text x="132" y="142" font-size="10" fill="#4f46e5">ε_F</text>
<text x="40" y="152" font-size="10" fill="#64748b">费米分布与费米能级</text>
</svg>''',
"bec": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<text x="210" y="148" font-size="11" fill="#475569">T</text>
<text x="14" y="26" font-size="11" fill="#475569">N0/N</text>
<path d="M 40 128 C 80 126 110 110 130 60 C 140 30 160 16 180 12" fill="none" stroke="#4f46e5" stroke-width="2"/>
<line x1="130" y1="128" x2="130" y2="20" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<text x="132" y="16" font-size="10" fill="#4f46e5">Tc</text>
<text x="60" y="120" font-size="10" fill="#4f46e5">N0/N≈0</text>
<text x="150" y="30" font-size="10" fill="#4f46e5">N0/N→1</text>
<text x="60" y="152" font-size="10" fill="#64748b">玻色-爱因斯坦凝聚</text>
</svg>''',
"paramagnet": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.4"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.4"/>
<text x="210" y="148" font-size="11" fill="#475569">H/T</text>
<text x="14" y="26" font-size="11" fill="#475569">M</text>
<path d="M 40 128 C 80 126 120 100 150 60 C 170 30 200 22 210 20" fill="none" stroke="#4f46e5" stroke-width="2"/>
<text x="100" y="70" font-size="10" fill="#4f46e5">朗之万 M=NμL(x)</text>
<line x1="40" y1="128" x2="100" y2="96" stroke="#dc2626" stroke-width="1.6" stroke-dasharray="5 3"/>
<text x="50" y="112" font-size="9" fill="#dc2626">居里定律</text>
<line x1="150" y1="60" x2="210" y2="60" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<text x="160" y="54" font-size="9" fill="#94a3b8">饱和</text>
</svg>''',
"brownian": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.2"/>
<path d="M 60 80 L 75 60 L 92 72 L 100 50 L 118 58 L 128 38 L 142 52 L 150 70 L 166 62 L 178 80 L 190 66" fill="none" stroke="#be185d" stroke-width="1.6"/>
<circle cx="60" cy="80" r="3" fill="#be185d"/>
<circle cx="190" cy="66" r="3" fill="#be185d"/>
<line x1="60" y1="80" x2="190" y2="66" stroke="#0891b2" stroke-width="1.2" stroke-dasharray="4 3"/>
<text x="100" y="100" font-size="10" fill="#be185d">随机游走</text>
<text x="100" y="116" font-size="10" fill="#0891b2">⟨x²⟩=2Dt</text>
<text x="60" y="150" font-size="10" fill="#64748b">布朗运动轨迹</text>
</svg>''',
"fluctuation": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="130" x2="224" y2="130" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="130" x2="34" y2="20" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="70" x2="224" y2="70" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<text x="226" y="74" font-size="10" fill="#94a3b8">⟨x⟩</text>
<path d="M 40 70 C 50 50 60 90 72 68 C 84 46 96 88 108 72 C 120 56 132 88 144 70 C 156 52 168 88 180 66 C 192 44 204 88 216 70" fill="none" stroke="#be185d" stroke-width="1.6"/>
<line x1="108" y1="46" x2="108" y2="88" stroke="#dc2626" stroke-width="1" stroke-dasharray="3 3"/>
<text x="112" y="48" font-size="9" fill="#dc2626">√⟨Δx²⟩</text>
<text x="60" y="150" font-size="10" fill="#64748b">热力学量的涨落</text>
</svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

CORE_FORMULAS = [
    ("理想气体状态方程","PV = nRT = Nk_B T","压强体积与温度的关系，理想气体状态方程"),
    ("玻意耳定律","PV = \\text{const}\\quad(T\\text{ 不变})","等温过程中压强与体积成反比"),
    ("盖-吕萨克定律","V/T = \\text{const}\\quad(P\\text{ 不变})","等压过程中体积与温度成正比"),
    ("查理定律","P/T = \\text{const}\\quad(V\\text{ 不变})","等容过程中压强与温度成正比"),
    ("热力学第一定律","dU = \\delta Q + \\delta W","系统内能增量等于吸收的热量与外界对系统做功之和"),
    ("体积功","\\delta W = -P\\,dV","系统体积变化时外界对系统做的功"),
    ("焓的定义","H = U + PV","焓等于内能加压强体积积，等压过程热量等于焓变"),
    ("自由能定义","F = U - TS","亥姆霍兹自由能，等温等容过程的判据"),
    ("吉布斯函数","G = U - TS + PV = H - TS","吉布斯自由能，等温等压过程的判据"),
    ("热力学基本方程","dU = TdS - PdV","内能作为熵与体积的函数的全微分"),
    ("焓的微分","dH = TdS + VdP","焓作为熵与压强的函数的全微分"),
    ("自由能微分","dF = -SdT - PdV","自由能作为温度与体积的函数的全微分"),
    ("吉布斯函数微分","dG = -SdT + VdP","吉布斯函数作为温度与压强的函数的全微分"),
    ("熵的定义","dS = \\frac{\\delta Q_{\\text{rev}}}{T}","可逆过程热量与温度之比等于熵变"),
    ("卡诺效率","\\eta = 1 - \\frac{T_2}{T_1}","工作于 T1,T2 之间可逆卡诺热机的效率"),
    ("克劳修斯不等式","\\oint \\frac{\\delta Q}{T} \\leq 0","任意循环的热温比积分不大于零"),
    ("熵增原理","\\Delta S \\geq 0","绝热或孤立系统的熵永不减少"),
    ("麦克斯韦关系 1","\\left(\\frac{\\partial T}{\\partial V}\\right)_S = -\\left(\\frac{\\partial P}{\\partial S}\\right)_V","由 dU 导出的麦克斯韦关系"),
    ("麦克斯韦关系 2","\\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial P}{\\partial T}\\right)_V","由 dF 导出的麦克斯韦关系"),
    ("麦克斯韦关系 3","\\left(\\frac{\\partial T}{\\partial P}\\right)_S = \\left(\\frac{\\partial V}{\\partial S}\\right)_P","由 dH 导出的麦克斯韦关系"),
    ("麦克斯韦关系 4","\\left(\\frac{\\partial S}{\\partial P}\\right)_T = -\\left(\\frac{\\partial V}{\\partial T}\\right)_P","由 dG 导出的麦克斯韦关系"),
    ("定容热容","C_V = \\left(\\frac{\\partial U}{\\partial T}\\right)_V = T\\left(\\frac{\\partial S}{\\partial T}\\right)_V","等容过程温度升高所吸收的热量"),
    ("定压热容","C_P = \\left(\\frac{\\partial H}{\\partial T}\\right)_P = T\\left(\\frac{\\partial S}{\\partial T}\\right)_P","等压过程温度升高所吸收的热量"),
    ("热容差","C_P - C_V = T\\left(\\frac{\\partial P}{\\partial T}\\right)_V\\left(\\frac{\\partial V}{\\partial T}\\right)_P","定压与定容热容之差"),
    ("绝热指数","\\gamma = \\frac{C_P}{C_V}","定压热容与定容热容之比"),
    ("等温压缩系数","\\kappa_T = -\\frac{1}{V}\\left(\\frac{\\partial V}{\\partial P}\\right)_T","等温下体积随压强的相对变化率"),
    ("体膨胀系数","\\alpha = \\frac{1}{V}\\left(\\frac{\\partial V}{\\partial T}\\right)_P","等压下体积随温度的相对变化率"),
    ("克拉珀龙方程","\\frac{dP}{dT} = \\frac{L}{T\\Delta v}","相平衡曲线斜率与相变潜热及体积变化的关系"),
    ("克劳修斯-克拉珀龙","\\ln\\frac{P_2}{P_1} = -\\frac{L}{R}\\left(\\frac{1}{T_2}-\\frac{1}{T_1}\\right)","气液相变蒸汽压与温度的近似关系"),
    ("范德瓦尔斯方程","\\left(P+\\frac{a}{V_m^2}\\right)(V_m-b) = RT","考虑分子体积与相互作用的实际气体方程"),
    ("玻尔兹曼熵公式","S = k_B \\ln \\Omega","熵与微观状态数的对数成正比"),
    ("等概率原理","\\Omega(E) = g(E)\\,dE","等能面上所有微观态出现概率相等"),
    ("玻尔兹曼分布","P_i \\propto e^{-\\beta E_i},\\quad \\beta=1/(k_B T)","正则系综中系统处于能量 E_i 的概率"),
    ("配分函数","Z = \\sum_i e^{-\\beta E_i}","正则配分函数，所有能级玻尔兹曼因子之和"),
    ("自由能与配分函数","F = -k_B T \\ln Z","亥姆霍兹自由能由配分函数直接给出"),
    ("内能与配分函数","U = -\\frac{\\partial \\ln Z}{\\partial \\beta} = k_B T^2\\frac{\\partial \\ln Z}{\\partial T}","内能由配分函数对温度的导数给出"),
    ("熵与配分函数","S = k_B(\\ln Z + \\beta U)","熵由配分函数与内能共同给出"),
    ("麦克斯韦速度分布","f(\\mathbf{v}) = \\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2} e^{-m v^2/(2k_B T)}","理想气体分子速度的概率分布"),
    ("最概然速率","v_p = \\sqrt{\\frac{2k_B T}{m}}","麦克斯韦速率分布的峰值速率"),
    ("平均速率","\\langle v \\rangle = \\sqrt{\\frac{8k_B T}{\\pi m}}","速率分布的算术平均值"),
    ("方均根速率","v_{\\text{rms}} = \\sqrt{\\frac{3k_B T}{m}}","速率平方平均值的平方根"),
    ("能量均分定理","\\langle \\varepsilon_k \\rangle = \\frac{1}{2}k_B T","每个平方自由度平均分配 kT/2 的能量"),
    ("理想气体内能","U = \\frac{f}{2}Nk_B T","由 f 个自由度决定的理想气体内能"),
    ("单原子热容","C_V = \\frac{3}{2}R","单原子理想气体定容摩尔热容"),
    ("双原子热容","C_V = \\frac{5}{2}R\\ (\\text{常温})","双原子气体常温下平动加转动贡献的热容"),
    ("正则分布","\\rho = \\frac{1}{Z}e^{-\\beta E}","正则系综的概率密度"),
    ("巨正则分布","\\rho = \\frac{1}{\\Xi}e^{-\\beta(E-\\mu N)}","巨正则系综的概率密度"),
    ("巨配分函数","\\Xi = \\sum_{N,E} e^{-\\beta(E-\\mu N)}","巨正则系综的配分函数"),
    ("巨正则压强","P = k_B T \\frac{\\partial \\ln \\Xi}{\\partial V}","由巨配分函数求压强"),
    ("平均粒子数","\\langle N \\rangle = k_B T \\frac{\\partial \\ln \\Xi}{\\partial \\mu}","由巨配分函数求平均粒子数"),
    ("玻色分布","\\bar{n}_i = \\frac{1}{e^{\\beta(\\varepsilon_i-\\mu)}-1}","玻色子在能级 i 的平均占据数"),
    ("费米分布","\\bar{n}_i = \\frac{1}{e^{\\beta(\\varepsilon_i-\\mu)}+1}","费米子在能级 i 的平均占据数"),
    ("普朗克公式","u(\\nu,T) = \\frac{8\\pi h\\nu^3}{c^3}\\frac{1}{e^{h\\nu/k_B T}-1}","黑体辐射的单色能量密度"),
    ("斯特藩-玻尔兹曼定律","u = a T^4,\\quad M = \\sigma T^4","黑体总辐射能量密度与辐出度正比于 T^4"),
    ("维恩位移律","\\lambda_{\\max} T = b","黑体辐射峰值波长与温度成反比"),
    ("费米能量","\\varepsilon_F = \\frac{\\hbar^2}{2m}(3\\pi^2 n)^{2/3}","T=0 时自由电子气的最高占据能级"),
    ("费米温度","T_F = \\frac{\\varepsilon_F}{k_B}","费米能量对应的温度"),
    ("BEC 临界温度","T_c = \\frac{2\\pi\\hbar^2}{m k_B}\\left(\\frac{n}{2.612}\\right)^{2/3}","理想玻色气体发生凝聚的临界温度"),
    ("居里定律","M = C\\frac{H}{T},\\quad \\chi = \\frac{C}{T}","顺磁磁化率与温度成反比"),
    ("居里-外斯定律","\\chi = \\frac{C}{T-T_c}","考虑分子场后的顺磁磁化率"),
    ("泡利顺磁磁化率","\\chi = \\mu_0\\mu_B^2 g(\\varepsilon_F)","金属中自由电子气的泡利顺磁磁化率"),
    ("朗之万函数","L(x) = \\coth x - \\frac{1}{x}","经典顺磁磁化强度的函数"),
    ("涨落基本公式","\\langle (\\Delta x)^2 \\rangle = -\\frac{k_B T}{(\\partial^2 S/\\partial x^2)}","由热力学势二阶导数决定的涨落"),
    ("能量涨落","\\langle (\\Delta E)^2 \\rangle = k_B T^2 C_V","正则系综中能量的涨落"),
    ("温度涨落","\\langle (\\Delta T)^2 \\rangle = \\frac{k_B T^2}{C_V}","系统温度的均方涨落"),
    ("粒子数涨落","\\langle (\\Delta N)^2 \\rangle = k_B T\\left(\\frac{\\partial \\langle N \\rangle}{\\partial \\mu}\\right)","巨正则系综中粒子数的涨落"),
    ("布朗运动位移","\\langle x^2 \\rangle = 2Dt","布朗粒子均方位移与时间成正比"),
    ("爱因斯坦关系","D = \\mu k_B T","扩散系数与迁移率的关系"),
    ("斯托克斯-爱因斯坦","D = \\frac{k_B T}{6\\pi\\eta r}","球形粒子在黏性流体中的扩散系数"),
    ("朗之万方程","m\\frac{dv}{dt} = -\\gamma v + F(t)","布朗粒子运动的随机微分方程"),
    ("涨落耗散定理","\\int_0^\\infty \\langle F(t)F(0)\\rangle dt = 2\\gamma k_B T","随机力关联与耗散系数的关系"),
    ("临界指数 β","\\rho_l - \\rho_g \\propto |T-T_c|^\\beta","序参量在临界点附近随温度的标度"),
    ("临界指数 α","C \\propto |T-T_c|^{-\\alpha}","热容在临界点附近的发散指数"),
    ("临界指数 γ","\\kappa_T \\propto |T-T_c|^{-\\gamma}","等温压缩系数发散指数"),
    ("临界指数 δ","|P-P_c| \\propto |\\rho-\\rho_c|^\\delta","临界等温线的幂指数"),
    ("朗道自由能","F = F_0 + a(T-T_c)M^2 + bM^4","二级相变的朗道自由能展开"),
    ("标度律","\\alpha + 2\\beta + \\gamma = 2","临界指数之间满足的普适关系"),
    ("能斯特定理","\\lim_{T\\to 0} \\Delta S = 0","热力学第三定律：绝对零度时熵变趋于零"),
    ("化学势","\\mu = \\left(\\frac{\\partial G}{\\partial N}\\right)_{T,P}","化学势等于吉布斯函数对粒子数的偏导"),
    ("相平衡条件","\\mu_1 = \\mu_2","两相平衡时化学势相等"),
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
"name": "1.1 热力学系统与状态参量",
"color": "#dc2626",
"desc": "热力学系统分类、平衡态、状态参量与状态方程",
"items": [
{"id":"sm1s1-1","name":"热力学系统与外界","tags":["def","der"],"brief":"按系统与外界的相互作用划分孤立、封闭、开放系统。",
 "fig":"system","figCap":"热力学系统与外界的相互作用",
 "body": wrap(
   defn("热力学系统",p("把研究对象从周围物体中划分出来，称为<strong>热力学系统</strong>；系统以外的部分称为<strong>外界</strong>。按相互作用可分为：孤立系统（与外界无物质和能量交换）、封闭系统（无物质交换但有能量交换）、开放系统（既有物质又有能量交换）。"))+
   der(p("<strong>分类与热力学第一定律推广：</strong>对开放系统，需把物质携带的能量计入第一定律。设流入系统的物质能量为 $\\sum_k \\mu_k dN_k$，则能量守恒推广为：")+
   fml("dU = \\delta Q + \\delta W + \\sum_k \\mu_k dN_k")+
   p("其中 $\\mu_k$ 为第 $k$ 组元的化学势。对孤立系统 $\\delta Q=0,\\delta W=0,dN_k=0$，故 $dU=0$，即孤立系统内能守恒。"))+
   note(p("系统与外界的边界可以是真实的（如容器壁），也可以是假想的；边界特性（绝热/导热、刚性/可动、半透）直接决定系统类型。"))
 )},
{"id":"sm1s1-2","name":"平衡态与状态参量","tags":["def","der"],"brief":"平衡态下系统的宏观性质不随时间变化。",
 "body": wrap(
   defn("平衡态",p("在不受外界影响的条件下，系统的宏观性质不随时间变化的状态称为<strong>平衡态</strong>。此时系统内部不存在宏观的物质流与能量流。"))+
   der(p("<strong>平衡态的判据：</strong>对孤立系统，熵取极大值时达到平衡。设熵为广延量 $S=S(U,V,N)$，由孤立条件 $dU=0,dV=0,dN=0$，对任意虚变动有：")+
   fml("\\delta S = \\frac{\\partial S}{\\partial U}\\delta U + \\frac{\\partial S}{\\partial V}\\delta V + \\frac{\\partial S}{\\partial N}\\delta N \\leq 0")+
   p("由 $\\delta U,\\delta V,\\delta N$ 的任意性与拉格朗日乘子法可得平衡时各部分温度、压强、化学势相等：$T_1=T_2,\\ P_1=P_2,\\ \\mu_1=\\mu_2$。"))+
   note(p("平衡态是热动平衡：微观上分子仍在不停运动，只是宏观统计平均量不变。涨落始终存在。"))
 )},
{"id":"sm1s1-3","name":"状态方程与理想气体","tags":["thm","der"],"brief":"描述平衡态状态参量之间函数关系的方程。",
 "body": wrap(
   thm("理想气体状态方程",p("理想气体在平衡态下，压强 $P$、体积 $V$、物质的量 $n$ 与温度 $T$ 满足：")+
   fml("PV = nRT = Nk_B T")+
   p("其中 $R=8.314\\,\\text{J/(mol·K)}$ 为气体常数，$k_B=R/N_A$ 为玻尔兹曼常数。"))+
   der(p("<strong>由实验定律推导：</strong>玻意耳定律 $PV=f(T)$，盖-吕萨克定律 $V/T=g(P)$，查理定律 $P/T=h(V)$。把三式联立：")+
   fml("\\frac{PV}{T} = \\text{const}\\quad\\Rightarrow\\quad PV = nRT")+
   p("对 $1\\,\\text{mol}$ 气体 $PV_m=RT$；对 $N$ 个分子，$n=N/N_A$，故 $PV=Nk_B T$。"))+
   app(p("<strong>应用：</strong>在常温常压下，实际气体（如空气、氢气）可近似为理想气体，误差通常小于 1%。"))+
   note(p("理想气体的微观模型：分子本身大小可忽略，分子间除碰撞瞬间外无相互作用力。"))
 )},
]},
{
"name": "1.2 热力学第零定律与温度",
"color": "#dc2626",
"desc": "热平衡、第零定律与温度的定义",
"items": [
{"id":"sm1s2-1","name":"热力学第零定律","tags":["thm","der"],"brief":"热平衡的传递性定义了温度。",
 "body": wrap(
   thm("热力学第零定律",p("若两个系统各自与第三个系统达到热平衡，则这两个系统也必处于热平衡。热平衡关系具有传递性。"))+
   der(p("<strong>由状态函数存在性推导：</strong>设系统 A、B 分别与系统 C 热平衡，则 A 与 C、B 与 C 的状态参量满足同一热平衡条件 $f_{AC}=0$、$f_{BC}=0$。消去 C 的参量后可得 A、B 之间的一个状态函数相等：")+
   fml("\\phi_A(P_A,V_A) = \\phi_B(P_B,V_B)")+
   p("这个相等的状态函数就是温度 $T$，即 $\\phi(P,V)=T$。第零定律保证了温度这一态函数的存在。"))+
   note(p("温度是系统内部分子热运动剧烈程度的度量，是最基本的宏观态函数之一。"))
 )},
{"id":"sm1s2-2","name":"温标与理想气体温标","tags":["def","der"],"brief":"用三相点定点建立的经验温标。",
 "body": wrap(
   defn("温标",p("温度的数值表示法称为<strong>温标</strong>。建立温标需要三要素：测温物质、测温属性、固定点。"))+
   der(p("<strong>理想气体温标推导：</strong>以定容气体温度计为例，规定水的三相点温度为 $T_{tr}=273.16\\,\\text{K}$。测温气体压强为 $P$，三相点压强为 $P_{tr}$，则：")+
   fml("T = 273.16\\,\\text{K} \\cdot \\frac{P}{P_{tr}}")+
   p("当气体压强趋于零（即稀薄气体极限）时，各种气体温度计给出相同的温度，与气体种类无关，此极限即<strong>理想气体温标</strong>：")+
   fml("T = 273.16\\,\\text{K} \\cdot \\lim_{P_{tr}\\to 0} \\frac{P}{P_{tr}}")+
   p("该温标与热力学温标在理想气体温标适用范围内完全一致。"))+
   note(p("热力学温标（开尔文温标）由热力学第二定律定义，不依赖于具体测温物质，是最基本的温标。"))
 )},
{"id":"sm1s2-3","name":"热膨胀与状态方程的微分形式","tags":["der","app"],"brief":"体膨胀系数与等温压缩系数。",
 "body": wrap(
   defn("热膨胀系数",p("<strong>体膨胀系数</strong> $\\alpha$ 描述等压下体积随温度的相对变化率，<strong>等温压缩系数</strong> $\\kappa_T$ 描述等温下体积随压强的相对变化率：")+
   fml("\\alpha = \\frac{1}{V}\\left(\\frac{\\partial V}{\\partial T}\\right)_P,\\quad \\kappa_T = -\\frac{1}{V}\\left(\\frac{\\partial V}{\\partial P}\\right)_T"))+
   der(p("<strong>对理想气体的计算：</strong>由 $PV=nRT$，$V=nRT/P$。分别求偏导：")+
   fml("\\left(\\frac{\\partial V}{\\partial T}\\right)_P = \\frac{nR}{P} = \\frac{V}{T} \\implies \\alpha = \\frac{1}{T}")+
   fml("\\left(\\frac{\\partial V}{\\partial P}\\right)_T = -\\frac{nRT}{P^2} = -\\frac{V}{P} \\implies \\kappa_T = \\frac{1}{P}")+
   p("即理想气体体膨胀系数等于热力学温度的倒数，等温压缩系数等于压强的倒数。"))+
   app(p("<strong>应用：</strong>液体温度计利用液体体膨胀随温度近似线性变化测温；双金属片利用两种金属膨胀系数不同制成温控开关。"))
 )},
]},
{
"name": "1.3 热力学第一定律",
"color": "#dc2626",
"desc": "能量守恒、功与热量、内能与焓",
"items": [
{"id":"sm1s3-1","name":"热力学第一定律","tags":["thm","der"],"brief":"能量守恒在热现象中的表达。",
 "body": wrap(
   thm("热力学第一定律",p("系统经过任意过程，其内能增量等于外界传入系统的热量与外界对系统所做功之和：")+
   fml("\\Delta U = Q + W,\\quad \\text{微分形式}\\ dU = \\delta Q + \\delta W")+
   p("对仅有体积功的系统，$\\delta W=-P\\,dV$，故 $dU=\\delta Q-PdV$。"))+
   der(p("<strong>由能量守恒推导：</strong>绝热过程中，系统内能的改变完全由做功决定，焦耳实验测得 $\\Delta U = W_{\\text{绝热}}$，与做功方式无关。对一般过程，热量 $Q$ 与功 $W$ 都是过程量，但其和等于内能（态函数）的变化：")+
   fml("Q + W = \\Delta U")+
   p("由于 $U$ 是态函数，$dU$ 是全微分；而 $\\delta Q,\\delta W$ 不是全微分，故记为 $\\delta$。第一定律本质是能量守恒与转化定律。"))+
   note(p("第一定律宣告第一类永动机（不消耗能量却能不断对外做功的机器）不可能制成。"))
 )},
{"id":"sm1s3-2","name":"准静态过程的功与热量","tags":["der","exa"],"brief":"体积功的计算与过程量。",
 "body": wrap(
   defn("准静态过程",p("过程进行得足够缓慢，使系统每时每刻都近似处于平衡态的过程称为<strong>准静态过程</strong>。此时可在状态图（如 $P$-$V$ 图）上用一条曲线表示。"))+
   der(p("<strong>体积功推导：</strong>设气缸内气体准静态膨胀，活塞面积为 $A$，气体压强为 $P$，移动距离 $dx$，则气体对外做功：")+
   fml("\\delta W' = F\\,dx = PA\\,dx = P\\,dV")+
   p("外界对系统做功为其负值 $\\delta W=-P\\,dV$。系统从状态 1 到状态 2 外界对系统做的总功：")+
   fml("W = -\\int_{V_1}^{V_2} P\\,dV")+
   p("功的大小等于 $P$-$V$ 图上过程曲线下面积，与路径有关，故功是过程量。"))+
   exa(p("<strong>例：</strong>理想气体等温过程 $PV=nRT$，气体对外做功 $W'=\\int P\\,dV = nRT\\ln(V_2/V_1)$；等温膨胀时 $W'>0$，气体对外做功。"))
 )},
{"id":"sm1s3-3","name":"热容与焓","tags":["def","der"],"brief":"定容热容、定压热容与焓的引入。",
 "body": wrap(
   defn("热容",p("系统温度升高 $dT$ 所吸收的热量 $\\delta Q$ 与之比称为热容 $C=\\delta Q/dT$。定容热容 $C_V$ 与定压热容 $C_P$ 分别为等容、等压过程的热容。"))+
   der(p("<strong>焓的引入与定压热容：</strong>等压过程中，系统吸热 $\\delta Q=dU+P\\,dV=d(U+PV)$。定义<strong>焓</strong> $H=U+PV$，则等压过程热量等于焓变 $\\delta Q_P=dH$。故：")+
   fml("C_P = \\left(\\frac{\\partial H}{\\partial T}\\right)_P")+
   p("同理，等容过程 $\\delta Q_V=dU$，故 $C_V=(\\partial U/\\partial T)_V$。对理想气体 $U=U(T)$，$H=U(T)+nRT$，故：")+
   fml("C_P - C_V = \\frac{dH}{dT}-\\frac{dU}{dT} = nR")+
   p("即迈耶公式。"))+
   note(p("对液体和固体，$C_P$ 与 $C_V$ 相差很小，常可近似认为相等；对气体则差别显著。"))
 )},
]},
{
"name": "1.4 热力学第二定律与熵",
"color": "#dc2626",
"desc": "自发过程的方向性、卡诺循环、熵与熵增原理",
"items": [
{"id":"sm1s4-1","name":"热力学第二定律的两种表述","tags":["thm","der"],"brief":"开尔文表述与克劳修斯表述的等价性。",
 "body": wrap(
   thm("热力学第二定律",p("<strong>开尔文表述：</strong>不可能从单一热源吸热使之完全变为有用功而不产生其他影响。<strong>克劳修斯表述：</strong>不可能把热量从低温物体传到高温物体而不产生其他影响。"))+
   der(p("<strong>等价性证明（反证法）：</strong>假设开尔文表述不成立，则可制造一台热机从温度 $T_1$ 的热源吸热 $Q$ 全部变成功 $W=Q$，用这台功驱动一台制冷机把热量 $Q_2$ 从低温 $T_2$ 送到高温 $T_1$。")+
   fml("Q_{\\text{高温净得}} = Q + Q_2,\\quad Q_{\\text{低温失去}} = Q_2")+
   p("整体效果是热量 $Q_2$ 从低温传向高温且无其他影响，违反克劳修斯表述。反之亦然。故两表述等价。"))+
   note(p("第二定律指明了宏观过程的方向性：与热现象有关的实际宏观过程都是不可逆的。第二类永动机（单一热源热机）不可能制成。"))
 )},
{"id":"sm1s4-2","name":"卡诺循环与卡诺定理","tags":["thm","der"],"brief":"可逆卡诺热机的效率最高。",
 "fig":"carnot","figCap":"卡诺循环在 P-V 图上的四个过程",
 "body": wrap(
   thm("卡诺定理",p("工作于两个恒定温度热源之间的所有热机中，可逆卡诺热机效率最高，且其效率只与两热源温度有关，与工作物质无关：")+
   fml("\\eta_C = 1 - \\frac{T_2}{T_1}"))+
   der(p("<strong>卡诺循环效率推导：</strong>卡诺循环由两个等温过程与两个绝热过程组成。理想气体在等温膨胀（$T_1$）中吸热：")+
   fml("Q_1 = nRT_1\\ln\\frac{V_2}{V_1}")+
   p("等温压缩（$T_2$）中放热 $Q_2=nRT_2\\ln(V_3/V_4)$。由绝热过程方程 $TV^{\\gamma-1}=\\text{const}$ 可得 $V_2/V_1=V_3/V_4$，故：")+
   fml("\\eta = 1-\\frac{Q_2}{Q_1} = 1-\\frac{T_2}{T_1}")+
   p("卡诺定理保证了该效率是同温限热机的最高效率，并定义了热力学温标。"))+
   app(p("<strong>应用：</strong>卡诺效率给出了热机效率的理论上限。现代火力发电厂由于温差大，效率可接近 40%–50%，但仍低于卡诺效率。"))
 )},
{"id":"sm1s4-3","name":"熵的定义与熵增原理","tags":["def","der"],"brief":"熵作为态函数与热力学第二定律的数学表达。",
 "fig":"entropy","figCap":"可逆循环熵变与不可逆过程熵增",
 "body": wrap(
   defn("熵",p("对任意可逆循环，克劳修斯证明了 $\\oint \\delta Q/T=0$，故热温比 $\\delta Q_{\\text{rev}}/T$ 是某态函数的全微分。该态函数定义为<strong>熵</strong>：")+
   fml("dS = \\frac{\\delta Q_{\\text{rev}}}{T}"))+
   der(p("<strong>熵增原理推导：</strong>对不可逆循环，由卡诺定理推广得克劳修斯不等式 $\\oint \\delta Q/T \\leq 0$。取一可逆过程使系统由状态 2 回到状态 1，与不可逆过程 1→2 构成循环：")+
   fml("\\int_1^2 \\frac{\\delta Q}{T} + \\int_2^1 \\frac{\\delta Q_{\\text{rev}}}{T} \\leq 0")+
   p("即 $\\int_1^2 \\delta Q/T \\leq \\int_1^2 \\delta Q_{\\text{rev}}/T = S_2-S_1$。故对任意过程：")+
   fml("dS \\geq \\frac{\\delta Q}{T}")+
   p("对绝热系统 $\\delta Q=0$，得 $dS\\geq 0$，即熵增原理：绝热或孤立系统的熵永不减少。"))+
   note(p("熵是系统混乱程度的度量。玻尔兹曼关系 $S=k_B\\ln\\Omega$ 把熵与微观状态数联系起来。"))
 )},
]},
{
"name": "1.5 热力学第三定律",
"color": "#dc2626",
"desc": "能斯特定理、绝对零度不可达到与低温下的热力学性质",
"items": [
{"id":"sm1s5-1","name":"能斯特定理","tags":["thm","der"],"brief":"绝对零度时等温过程熵变趋于零。",
 "body": wrap(
   thm("能斯特定理（热力学第三定律）",p("当温度趋于绝对零度时，等温过程的熵变趋于零：")+
   fml("\\lim_{T\\to 0} (\\Delta S)_T = 0"))+
   der(p("<strong>由低温化学平衡数据归纳：</strong>能斯特研究低温化学反应时发现，温度越低，反应的熵变越小。外推到 $T\\to 0$ 时，所有等温过程的熵变都为零。由熵的热力学表达式 $S=S_0+\\int_0^T C_X/T\\,dT$，当 $T\\to 0$ 时要求 $C_X\\to 0$ 才能保证积分收敛，由此可得：")+
   fml("\\lim_{T\\to 0} C_X = 0")+
   p("这与量子统计结果一致（如德拜 $T^3$ 定律）。"))+
   note(p("第三定律是低温实验规律的总结，与量子力学的零点能概念相一致。"))
 )},
{"id":"sm1s5-2","name":"绝对零度不可达到原理","tags":["thm","der"],"brief":"不可能通过有限步骤达到绝对零度。",
 "body": wrap(
   thm("绝对零度不可达到原理",p("不可能用有限次操作把任何系统的温度降到绝对零度。这是热力学第三定律的另一种表述。"))+
   der(p("<strong>由能斯特定理推导：</strong>考虑用绝热去磁降温。设系统在磁场 $H$ 下等温磁化熵变为 $S(H,T)-S(0,T)$，由能斯特定理，当 $T\\to 0$ 时两熵趋于同一值 $S_0$。绝热去磁时熵不变，温度由 $T_1$ 降至 $T_2$。由于 $T\\to 0$ 时熵曲线 $S(H,T)$ 与 $S(0,T)$ 均趋于同一点，每次降温幅度 $\\Delta T$ 越来越小：")+
   fml("\\Delta T \\to 0\\quad(T\\to 0)")+
   p("因此需要无限多步才能趋近绝对零度，有限步不可能达到 $T=0$。"))+
   note(p("现代低温技术可达 $10^{-10}\\,\\text{K}$ 量级的极低温，但永远无法达到绝对零度。"))
 )},
{"id":"sm1s5-3","name":"低温下的热力学性质","tags":["der","app"],"brief":"热容、膨胀系数等低温极限行为。",
 "body": wrap(
   defn("第三定律的推论",p("由 $\\lim_{T\\to 0}(\\Delta S)_T=0$ 可推出低温下多个热力学量趋于零：$C_P,C_V\\to 0$，$\\alpha,\\kappa_T$ 等膨胀与压缩系数也趋于有限值或零。"))+
   der(p("<strong>由麦克斯韦关系推低温行为：</strong>利用麦克斯韦关系 $(\\partial S/\\partial P)_T=-(\\partial V/\\partial T)_P=-V\\alpha$。当 $T\\to 0$ 时 $(\\partial S/\\partial P)_T\\to 0$，故：")+
   fml("\\lim_{T\\to 0} \\alpha = \\lim_{T\\to 0} \\frac{1}{V}\\left(\\frac{\\partial V}{\\partial T}\\right)_P = 0")+
   p("同理 $C_P-C_V=T(\\partial P/\\partial T)_V(\\partial V/\\partial T)_P\\to 0$，故低温下 $C_P\\to C_V\\to 0$。对非金属晶体，德拜理论给出 $C_V\\propto T^3$；对金属则有 $C_V=\\gamma T+\\beta T^3$。"))+
   app(p("<strong>应用：</strong>绝热去磁制冷利用顺磁盐在低温下的磁化熵变获得 mK 级低温，是低温物理学的基础技术。"))
 )},
]},
]

ch2_sections = [
{
"name": "2.1 自由能与吉布斯函数",
"color": "#ea580c",
"desc": "热力学势的引入、勒让德变换与平衡判据",
"items": [
{"id":"sm2s1-1","name":"勒让德变换与热力学势","tags":["def","der"],"brief":"通过勒让德变换引入各热力学势。",
 "fig":"potentials","figCap":"四个热力学势之间的变换关系",
 "body": wrap(
   defn("热力学势",p("内能 $U(S,V)$ 的自然变量为熵 $S$ 与体积 $V$。通过勒让德变换把不便于实验控制的变量换成便于控制的变量，可得到其他热力学势：焓 $H=U+PV$、自由能 $F=U-TS$、吉布斯函数 $G=U-TS+PV$。"))+
   der(p("<strong>勒让德变换推导：</strong>对内能全微分 $dU=TdS-PdV$，要把变量 $S$ 换为 $T$，减去 $TS$：")+
   fml("d(U-TS) = dU - TdS - SdT = (TdS-PdV) - TdS - SdT = -SdT-PdV")+
   p("定义 $F=U-TS$，得 $dF=-SdT-PdV$，自然变量为 $T,V$。同理定义 $H=U+PV$ 消去 $V$：")+
   fml("dH = dU+PdV+VdP = (TdS-PdV)+PdV+VdP = TdS+VdP")+
   p("定义 $G=H-TS=F+PV$，得 $dG=-SdT+VdP$，自然变量为 $T,P$。"))+
   note(p("勒让德变换保持信息量不变，只是换了一组独立变量，便于不同实验条件下使用。"))
 )},
{"id":"sm2s1-2","name":"自由能与等温等容判据","tags":["thm","der"],"brief":"等温等容下自由能最小是平衡条件。",
 "body": wrap(
   thm("自由能判据",p("等温等容且只有体积功的系统，平衡态的自由能取极小值。任意虚变动满足 $\\delta F\\geq 0$。"))+
   der(p("<strong>由熵增原理推导：</strong>等温等容过程，系统与热源交换热量 $\\delta Q=T\\,dS$（系统吸热）。由熵增原理，系统加热源的总熵变：")+
   fml("dS_{\\text{总}} = dS + dS_{\\text{源}} = dS - \\frac{\\delta Q}{T} = dS - \\frac{TdS+PdV}{T}")+
   p("等容时 $dV=0$，故 $dS_{\\text{总}}=dS-dS=0$？不对，等容时系统吸收热量 $\\delta Q=dU$，热源熵变为 $-\\delta Q/T=-dU/T$。总熵变：")+
   fml("dS_{\\text{总}} = dS - \\frac{dU}{T} = -\\frac{dU-TdS}{T} = -\\frac{dF}{T} \\geq 0")+
   p("故 $dF\\leq 0$，等温等容下系统自发过程朝自由能减小方向进行，平衡时 $F$ 极小。"))+
   note(p("自由能可理解为等温条件下系统对外做功的最大能力：$W_{\\text{max}}=-\\Delta F$。"))
 )},
{"id":"sm2s1-3","name":"吉布斯函数与等温等压判据","tags":["thm","der"],"brief":"等温等压下吉布斯函数最小。",
 "body": wrap(
   thm("吉布斯函数判据",p("等温等压且只有体积功的系统，平衡态的吉布斯函数取极小值。任意虚变动满足 $\\delta G\\geq 0$。"))+
   der(p("<strong>由熵增原理推导：</strong>等温等压过程，系统吸收热量 $\\delta Q=dU+PdV=dH$。热源熵变为 $-\\delta Q/T=-dH/T$。系统与热源总熵变：")+
   fml("dS_{\\text{总}} = dS - \\frac{dH}{T} = \\frac{TdS-(dU+PdV)}{T} = \\frac{TdS-dH}{T} = -\\frac{dG}{T} \\geq 0")+
   p("故 $dG\\leq 0$，等温等压下系统自发过程朝吉布斯函数减小方向进行，平衡时 $G$ 极小。"))+
   app(p("<strong>应用：</strong>化学反应通常在等温等压下进行，用 $\\Delta G$ 作为反应方向与限度的判据；相变（如冰融化）在等温等压下也由 $\\Delta G=0$ 给出平衡条件。"))+
   note(p("吉布斯函数是化学中最重要的热力学势，化学势即偏摩尔吉布斯函数。"))
 )},
]},
{
"name": "2.2 热力学基本方程",
"color": "#ea580c",
"desc": "内能、焓、自由能、吉布斯函数的全微分表达式",
"items": [
{"id":"sm2s2-1","name":"热力学基本方程","tags":["thm","der"],"brief":"四个热力学势的全微分形式。",
 "body": wrap(
   thm("热力学基本方程组",p("对可压缩均匀系统，四个热力学势的全微分（自然变量下）为：")+
   fml("dU = TdS-PdV,\\quad dH = TdS+VdP,\\quad dF = -SdT-PdV,\\quad dG = -SdT+VdP"))+
   der(p("<strong>统一推导：</strong>由第一定律 $dU=\\delta Q+\\delta W$ 与第二定律可逆过程 $\\delta Q=TdS$、体积功 $\\delta W=-PdV$ 得：")+
   fml("dU = TdS-PdV")+
   p("这是最基本的热力学基本方程。对其他势作勒让德变换：$H=U+PV$ 得 $dH=dU+PdV+VdP=TdS+VdP$；$F=U-TS$ 得 $dF=-SdT-PdV$；$G=U-TS+PV$ 得 $dG=-SdT+VdP$。"))+
   note(p("从基本方程可直接读出各热力学势对其自然变量的偏导数，这些导数称为「共轭变量」。"))
 )},
{"id":"sm2s2-2","name":"共轭变量与麦克斯韦关系的由来","tags":["der","note"],"brief":"由全微分的混合偏导相等得到麦克斯韦关系。",
 "body": wrap(
   defn("共轭变量",p("由基本方程可知，内能 $U(S,V)$ 的偏导数为 $(\\partial U/\\partial S)_V=T$、$(\\partial U/\\partial V)_S=-P$。温度 $T$ 与熵 $S$ 共轭，压强 $P$ 与体积 $V$ 共轭（符号相反）。"))+
   der(p("<strong>由全微分条件推导：</strong>若 $U=U(S,V)$ 是态函数，其二阶混合偏导数与求导顺序无关：")+
   fml("\\frac{\\partial^2 U}{\\partial S\\partial V} = \\frac{\\partial^2 U}{\\partial V\\partial S}")+
   p("代入 $\\partial U/\\partial S=T$、$\\partial U/\\partial V=-P$：")+
   fml("\\left(\\frac{\\partial T}{\\partial V}\\right)_S = -\\left(\\frac{\\partial P}{\\partial S}\\right)_V")+
   p("这就是第一个麦克斯韦关系。对其余三个热力学势应用同样的全微分条件，可得到另外三个麦克斯韦关系。"))+
   note(p("麦克斯韦关系把不可直接测量的熵的偏导数转化为可直接测量的状态参量偏导数，是热力学计算的关键工具。"))
 )},
{"id":"sm2s2-3","name":"热力学基本方程的推广（含化学势）","tags":["der","app"],"brief":"开放系统的热力学基本方程。",
 "body": wrap(
   defn("化学势",p("当系统粒子数可变时，内能的自然变量扩展为 $U(S,V,N)$，引入化学势 $\\mu=(\\partial U/\\partial N)_{S,V}$，表示增加一个粒子时内能的增量。"))+
   der(p("<strong>开放系统基本方程：</strong>把内能作为 $S,V,N$ 的函数，全微分为：")+
   fml("dU = TdS - PdV + \\mu dN")+
   p("对其他热力学势作相应推广：$dH=TdS+VdP+\\mu dN$，$dF=-SdT-PdV+\\mu dN$，$dG=-SdT+VdP+\\mu dN$。由吉布斯函数 $G=\\mu N$（广延量）得：")+
   fml("\\mu = \\left(\\frac{\\partial G}{\\partial N}\\right)_{T,P} = \\frac{G}{N}")+
   p("即化学势等于单位物质的量的吉布斯函数（偏摩尔吉布斯函数）。"))+
   app(p("<strong>应用：</strong>化学势是相平衡与化学平衡的核心量。多相平衡时各相化学势相等 $\\mu^\\alpha=\\mu^\\beta$；化学反应平衡时化学势满足计量关系 $\\sum_i \\nu_i\\mu_i=0$。"))
 )},
]},
{
"name": "2.3 麦克斯韦关系",
"color": "#ea580c",
"desc": "四个麦克斯韦关系及其应用",
"items": [
{"id":"sm2s3-1","name":"四个麦克斯韦关系","tags":["thm","der"],"brief":"由四个热力学势全微分导出的导数关系。",
 "fig":"maxwell","figCap":"四个麦克斯韦关系一览",
 "body": wrap(
   thm("麦克斯韦关系",p("由 $U,H,F,G$ 的全微分条件，得到四个麦克斯韦关系：")+
   fml("\\left(\\frac{\\partial T}{\\partial V}\\right)_S=-\\left(\\frac{\\partial P}{\\partial S}\\right)_V,\\quad \\left(\\frac{\\partial S}{\\partial V}\\right)_T=\\left(\\frac{\\partial P}{\\partial T}\\right)_V")+
   fml("\\left(\\frac{\\partial T}{\\partial P}\\right)_S=\\left(\\frac{\\partial V}{\\partial S}\\right)_P,\\quad \\left(\\frac{\\partial S}{\\partial P}\\right)_T=-\\left(\\frac{\\partial V}{\\partial T}\\right)_P"))+
   der(p("<strong>推导（以 dF 为例）：</strong>由 $dF=-SdT-PdV$，$F=F(T,V)$，全微分条件 $\\partial^2 F/\\partial T\\partial V=\\partial^2 F/\\partial V\\partial T$。由 $\\partial F/\\partial T=-S$、$\\partial F/\\partial V=-P$：")+
   fml("\\frac{\\partial}{\\partial V}\\left(-S\\right)\\bigg|_T = \\frac{\\partial}{\\partial T}\\left(-P\\right)\\bigg|_V")+
   fml("\\implies \\left(\\frac{\\partial S}{\\partial V}\\right)_T = \\left(\\frac{\\partial P}{\\partial T}\\right)_V")+
   p("其余三式分别由 $dU,dH,dG$ 的全微分条件同理可得。"))+
   note(p("记忆口诀：把 $T,S$ 与 $P,V$ 配对，求偏导时保持各自的另一个变量不变，注意 $V$ 与 $P$ 间有负号。"))
 )},
{"id":"sm2s3-2","name":"内能对体积的偏导数","tags":["der","app"],"brief":"用麦克斯韦关系求 (∂U/∂V)_T。",
 "body": wrap(
   defn("内能的状态依赖",p("理想气体内能仅与温度有关，即 $(\\partial U/\\partial V)_T=0$；实际气体因分子间相互作用，内能也依赖体积。"))+
   der(p("<strong>由基本方程与麦克斯韦关系推导：</strong>由 $dU=TdS-PdV$，在 $T$ 不变下除以 $dV$：")+
   fml("\\left(\\frac{\\partial U}{\\partial V}\\right)_T = T\\left(\\frac{\\partial S}{\\partial V}\\right)_T - P")+
   p("代入麦克斯韦关系 $(\\partial S/\\partial V)_T=(\\partial P/\\partial T)_V$：")+
   fml("\\left(\\frac{\\partial U}{\\partial V}\\right)_T = T\\left(\\frac{\\partial P}{\\partial T}\\right)_V - P")+
   p("对理想气体 $PV=nRT$，$(\\partial P/\\partial T)_V=nR/V=P/T$，故 $T\\cdot P/T-P=0$，与实验一致；对范德瓦尔斯气体 $(P+a/V_m^2)(V_m-b)=RT$，可算得 $(\\partial U/\\partial V)_T=a/V_m^2>0$，反映分子间吸引力。"))+
   app(p("<strong>应用：</strong>焦耳效应（气体自由膨胀温度变化）由该偏导数决定。理想气体自由膨胀温度不变，实际气体会降温或升温。"))
 )},
{"id":"sm2s3-3","name":"熵对压强的偏导数与节流过程","tags":["der","app"],"brief":"用麦克斯韦关系求焦-汤系数。",
 "body": wrap(
   defn("焦耳-汤姆孙系数",p("节流过程（等焓过程）中温度随压强的变化率称为焦-汤系数 $\\mu_{JT}=(\\partial T/\\partial P)_H$，可正可负。"))+
   der(p("<strong>由 $dH=TdS+VdP$ 推导：</strong>等焓时 $dH=0$，$TdS+VdP=0$。在 $H$ 不变下求 $(\\partial T/\\partial P)_H$，先把 $S$ 视为 $T,P$ 的函数：")+
   fml("0 = T\\left[\\left(\\frac{\\partial S}{\\partial T}\\right)_P dT + \\left(\\frac{\\partial S}{\\partial P}\\right)_T dP\\right] + VdP")+
   p("整理得 $\\mu_{JT}=(\\partial T/\\partial P)_H$。代入麦克斯韦关系 $(\\partial S/\\partial P)_T=-(\\partial V/\\partial T)_P$ 及 $C_P=T(\\partial S/\\partial T)_P$：")+
   fml("\\mu_{JT} = \\frac{1}{C_P}\\left[T\\left(\\frac{\\partial V}{\\partial T}\\right)_P - V\\right]")+
   p("对理想气体 $V=nRT/P$，$\\mu_{JT}=0$；对实际气体，$\\mu_{JT}>0$ 时节流降温（制冷），$\\mu_{JT}<0$ 时升温。"))+
   app(p("<strong>应用：</strong>节流膨胀制冷是工业液化气体的重要方法，林德机即利用焦-汤效应液化空气。"))
 )},
]},
{
"name": "2.4 热力学量的导数关系与应用",
"color": "#ea580c",
"desc": "热容差公式、雅可比行列式与热力学关系网",
"items": [
{"id":"sm2s4-1","name":"热容差公式 C_P - C_V","tags":["thm","der"],"brief":"定压与定容热容之差的普适表达式。",
 "body": wrap(
   thm("热容差公式",p("任意均匀系统的定压热容与定容热容之差为：")+
   fml("C_P - C_V = T\\left(\\frac{\\partial P}{\\partial T}\\right)_V\\left(\\frac{\\partial V}{\\partial T}\\right)_P = \\frac{TV\\alpha^2}{\\kappa_T}"))+
   der(p("<strong>推导：</strong>$C_P-C_V=T[(\\partial S/\\partial T)_P-(\\partial S/\\partial T)_V]$。把 $S(T,P)$ 在 $V$ 不变下展开，利用链式关系：")+
   fml("\\left(\\frac{\\partial S}{\\partial T}\\right)_P = \\left(\\frac{\\partial S}{\\partial T}\\right)_V + \\left(\\frac{\\partial S}{\\partial V}\\right)_T\\left(\\frac{\\partial V}{\\partial T}\\right)_P")+
   p("代入麦克斯韦关系 $(\\partial S/\\partial V)_T=(\\partial P/\\partial T)_V$：")+
   fml("C_P - C_V = T\\left(\\frac{\\partial P}{\\partial T}\\right)_V\\left(\\frac{\\partial V}{\\partial T}\\right)_P")+
   p("用 $\\alpha,\\kappa_T$ 表示并利用 $(\\partial P/\\partial T)_V=\\alpha/\\kappa_T$，得 $C_P-C_V=TV\\alpha^2/\\kappa_T$。由于 $\\kappa_T>0,\\alpha^2\\geq 0$，故 $C_P\\geq C_V$。"))+
   note(p("对理想气体 $\\alpha=1/T,\\kappa_T=1/P$，$C_P-C_V=TV(1/T^2)/(1/P)=PV/T=nR$，回到迈耶公式。"))
 )},
{"id":"sm2s4-2","name":"内能与熵的偏导数矩阵","tags":["der","note"],"brief":"用雅可比行列式统一处理热力学导数。",
 "body": wrap(
   defn("雅可比方法",p("热力学量之间的偏导数可用雅可比行列式 $J(x,y;u,v)=(\\partial x/\\partial u)(\\partial y/\\partial v)-(\\partial x/\\partial v)(\\partial y/\\partial u)$ 表示，便于变换自变量。"))+
   der(p("<strong>应用示例：</strong>把 $(\\partial T/\\partial V)_S$ 用雅可比表示：")+
   fml("\\left(\\frac{\\partial T}{\\partial V}\\right)_S = \\frac{J(T,S;V,S)}{J(V,S;V,S)} \\cdots")+
   p("更直接地，由 $dU=TdS-PdV$ 在 $S$ 不变下得 $(\\partial U/\\partial V)_S=-P$，在 $V$ 不变下得 $(\\partial U/\\partial S)_V=T$。利用循环关系：")+
   fml("\\left(\\frac{\\partial T}{\\partial V}\\right)_S\\left(\\frac{\\partial V}{\\partial S}\\right)_T\\left(\\frac{\\partial S}{\\partial T}\\right)_V = -1")+
   p("可把任一偏导数用其他两个表示。麦克斯韦关系本质上是雅可比行列式的恒等式：$J(T,V;S,V)=-J(P,S;S,V)$。"))+
   note(p("熟练掌握偏导数变换是解决热力学证明题的关键，常见技巧：循环关系、麦克斯韦关系、定义式代入。"))
 )},
{"id":"sm2s4-3","name":"绝热过程方程与绝热指数","tags":["der","app"],"brief":"理想气体绝热过程的 PV 关系。",
 "body": wrap(
   defn("绝热过程",p("系统与外界无热量交换的过程称为绝热过程。可逆绝热过程是等熵过程 $dS=0$。"))+
   der(p("<strong>理想气体绝热方程推导：</strong>由 $dU=C_V dT$ 与 $\\delta Q=0$，第一定律给出 $C_V dT+P dV=0$。代入 $P=nRT/V$：")+
   fml("C_V \\frac{dT}{T} + nR\\frac{dV}{V} = 0")+
   p("积分得 $T V^{\\gamma-1}=\\text{const}$，其中 $\\gamma=C_P/C_V$。再由 $PV=nRT$ 消去 $T$：")+
   fml("PV^\\gamma = \\text{const},\\quad T^{\\gamma}P^{1-\\gamma}=\\text{const}")+
   p("绝热过程曲线比等温线更陡（因 $\\gamma>1$）。"))+
   app(p("<strong>应用：</strong>声波在气体中的传播可近似为绝热过程，声速 $c=\\sqrt{\\gamma P/\\rho}=\\sqrt{\\gamma RT/M}$。汽油机压缩冲程近似绝热压缩使温度升高点火。"))
 )},
]},
]

ch3_sections = [
{
"name": "3.1 相平衡与克拉珀龙方程",
"color": "#d97706",
"desc": "相平衡条件、克拉珀龙方程与克劳修斯-克拉珀龙方程",
"items": [
{"id":"sm3s1-1","name":"相平衡条件","tags":["thm","der"],"brief":"两相平衡时温度、压强、化学势相等。",
 "body": wrap(
   thm("相平衡条件",p("两相 $\\alpha,\\beta$ 平衡时，除热平衡 $T_\\alpha=T_\\beta$ 与力学平衡 $P_\\alpha=P_\\beta$ 外，还需相平衡条件：")+
   fml("\\mu_\\alpha(T,P) = \\mu_\\beta(T,P)"))+
   der(p("<strong>由吉布斯函数极小推导：</strong>设两相物质的量分别为 $n_\\alpha,n_\\beta$，总吉布斯函数 $G=n_\\alpha\\mu_\\alpha+n_\\beta\\mu_\\beta$。等温等压下平衡时 $G$ 取极小，约束 $n_\\alpha+n_\\beta=\\text{const}$。对虚变动 $dn_\\alpha=-dn_\\beta=dn$：")+
   fml("\\delta G = \\mu_\\alpha dn + \\mu_\\beta(-dn) = (\\mu_\\alpha-\\mu_\\beta)dn = 0")+
   p("由 $dn$ 的任意性得 $\\mu_\\alpha=\\mu_\\beta$。若 $\\mu_\\alpha>\\mu_\\beta$，则物质由 $\\alpha$ 相向 $\\beta$ 相转化（$dn<0$）使 $G$ 减小，直到化学势相等。"))+
   note(p("相变的驱动力是化学势差。物质总是由化学势高的相向化学势低的相转变。"))
 )},
{"id":"sm3s1-2","name":"克拉珀龙方程","tags":["thm","der"],"brief":"相平衡曲线的斜率与潜热及体积变化的关系。",
 "fig":"clapeyron","figCap":"气液共存曲线的斜率 dp/dT",
 "body": wrap(
   thm("克拉珀龙方程",p("相平衡曲线的斜率由相变潜热与体积变化决定：")+
   fml("\\frac{dP}{dT} = \\frac{L}{T\\Delta v}")+
   p("其中 $L$ 为摩尔相变潜热，$\\Delta v=v_\\beta-v_\\alpha$ 为摩尔体积变化。"))+
   der(p("<strong>由相平衡条件推导：</strong>沿相平衡曲线，两相化学势始终相等 $\\mu_\\alpha(T,P)=\\mu_\\beta(T,P)$。沿曲线取微分：")+
   fml("d\\mu_\\alpha = d\\mu_\\beta")+
   p("由 $d\\mu=-s\\,dT+v\\,dP$（$s,v$ 为摩尔熵与摩尔体积）：")+
   fml("-s_\\alpha dT + v_\\alpha dP = -s_\\beta dT + v_\\beta dP")+
   p("整理得 $dP/dT=(s_\\beta-s_\\alpha)/(v_\\beta-v_\\alpha)=\\Delta s/\\Delta v$。而相变潜热 $L=T\\Delta s$（可逆等温相变吸热），故：")+
   fml("\\frac{dP}{dT} = \\frac{L}{T\\Delta v}")+
   p("此即克拉珀龙方程，对任意一级相平衡曲线均成立。"))+
   app(p("<strong>应用：</strong>冰融化时体积减小（$\\Delta v<0$），故 $dP/dT<0$，冰的熔点随压强增大而降低，这是冰鞋滑行与冰川流动的原因。"))
 )},
{"id":"sm3s1-3","name":"克劳修斯-克拉珀龙方程","tags":["der","app"],"brief":"气液相变蒸汽压与温度的指数关系。",
 "body": wrap(
   defn("克劳修斯-克拉珀龙近似",p("对气液相变，若气相可视为理想气体且液相体积远小于气相体积（$v_g\\gg v_l$），克拉珀龙方程可简化为克劳修斯-克拉珀龙方程。"))+
   der(p("<strong>由克拉珀龙方程推导：</strong>$\\Delta v\\approx v_g=RT/P$，代入克拉珀龙方程：")+
   fml("\\frac{dP}{dT} = \\frac{L}{T\\cdot RT/P} = \\frac{LP}{RT^2}")+
   p("分离变量并积分（设 $L$ 与温度无关）：")+
   fml("\\int_{P_1}^{P_2}\\frac{dP}{P} = \\frac{L}{R}\\int_{T_1}^{T_2}\\frac{dT}{T^2}")+
   fml("\\ln\\frac{P_2}{P_1} = -\\frac{L}{R}\\left(\\frac{1}{T_2}-\\frac{1}{T_1}\\right)")+
   p("或 $P=P_0 e^{-L/(RT)}$，即蒸汽压随温度指数增长。"))+
   app(p("<strong>应用：</strong>高山上沸点降低（压强低）；高压锅通过提高压强升高沸点加快烹饪；由蒸汽压随温度的变化可测定相变潜热。"))
 )},
]},
{
"name": "3.2 一级相变与二级相变",
"color": "#d97706",
"desc": "按化学势导数连续性的相变分类",
"items": [
{"id":"sm3s2-1","name":"一级相变","tags":["def","der"],"brief":"化学势连续但一阶导数不连续的相变。",
 "fig":"phasetrans","figCap":"一级与二级相变中化学势的行为",
 "body": wrap(
   defn("一级相变",p("相变时两相化学势连续 $\\mu_\\alpha=\\mu_\\beta$，但化学势的一阶导数不连续，即摩尔熵与摩尔体积发生突变：$\\Delta s=s_\\beta-s_\\alpha\\neq 0$，$\\Delta v=v_\\beta-v_\\alpha\\neq 0$。"))+
   der(p("<strong>特征推导：</strong>由 $s=-(\\partial\\mu/\\partial T)_P$、$v=(\\partial\\mu/\\partial P)_T$，一阶导数不连续意味着相变时：")+
   fml("\\Delta s = s_\\beta-s_\\alpha \\neq 0 \\implies L=T\\Delta s \\neq 0")+
   fml("\\Delta v = v_\\beta-v_\\alpha \\neq 0")+
   p("即相变伴随潜热吸收/释放和体积突变。两相可在相变点共存，相变曲线斜率由克拉珀龙方程 $dP/dT=L/(T\\Delta v)$ 给出。常见一级相变：熔化、汽化、升华、大多数晶型转变。"))+
   note(p("一级相变有明显的「过冷」「过热」亚稳态与滞后现象，因新相生成需克服表面能等势垒。"))
 )},
{"id":"sm3s2-2","name":"二级相变","tags":["def","der"],"brief":"化学势及一阶导数连续，二阶导数不连续。",
 "body": wrap(
   defn("二级相变（连续相变）",p("相变时化学势 $\\mu$ 及其一阶导数（$s,v$）连续，但二阶导数不连续，即热容 $C_P$、膨胀系数 $\\alpha$、压缩系数 $\\kappa_T$ 发生突变或发散。无相变潜热与体积突变。"))+
   der(p("<strong>特征推导：</strong>二阶导数不连续：$C_P=T(\\partial s/\\partial T)_P=-T(\\partial^2\\mu/\\partial T^2)_P$ 突变；$\\alpha=(1/v)(\\partial v/\\partial T)_P$ 突变；$\\kappa_T=-(1/v)(\\partial v/\\partial P)_T$ 突变。由厄伦费斯特方程可给出二级相变曲线斜率：")+
   fml("\\frac{dP}{dT} = \\frac{\\Delta C_P}{T v \\Delta \\alpha} = \\frac{\\Delta \\alpha}{\\Delta \\kappa_T}")+
   p("其中 $\\Delta$ 表示相变前后的差值。常见二级相变：铁磁-顺磁转变（居里点）、超导转变、超流转变、合金的有序-无序转变、气液临界点。"))+
   note(p("二级相变无潜热、无体积突变，新相在旧相中连续生长，伴随对称破缺与序参量的出现。"))
 )},
{"id":"sm3s2-3","name":"序参量与对称破缺","tags":["def","der"],"brief":"用序参量刻画相变的有序化程度。",
 "body": wrap(
   defn("序参量",p("在二级相变中，引入一个在高对称相为零、低对称相非零的物理量来描述有序化程度，称为<strong>序参量</strong>。例如铁磁体的磁化强度 $M$、超导体的能隙、气液临界点的密度差 $\\rho_l-\\rho_g$。"))+
   der(p("<strong>序参量与对称破缺：</strong>在临界温度 $T_c$ 以上，系统具有较高对称性（如顺磁相 $M=0$，各向同性）；$T<T_c$ 时对称性自发破缺，序参量取非零值。序参量的温度依赖一般为幂律：")+
   fml("\\eta \\propto |T-T_c|^\\beta\\quad(T\\to T_c)")+
   p("其中 $\\beta$ 为临界指数。在临界点，序参量连续从零变为非零，这是二级相变「连续」的含义。"))+
   note(p("序参量的选择依赖于具体相变的对称性变化，是朗道相变理论与重整化群理论的核心概念。"))
 )},
]},
{
"name": "3.3 气液相变与范德瓦尔斯方程",
"color": "#d97706",
"desc": "范德瓦尔斯等温线、气液共存与麦克斯韦等面积法则",
"items": [
{"id":"sm3s3-1","name":"范德瓦尔斯方程","tags":["def","der"],"brief":"考虑分子体积与吸引力的实际气体方程。",
 "fig":"vanderwaals","figCap":"范德瓦尔斯等温线与气液共存",
 "body": wrap(
   defn("范德瓦尔斯方程",p("对 $1\\,\\text{mol}$ 实际气体，考虑分子本身体积 $b$ 与分子间吸引力 $a$，状态方程修正为：")+
   fml("\\left(P+\\frac{a}{V_m^2}\\right)(V_m-b) = RT"))+
   der(p("<strong>由理想气体方程修正推导：</strong>理想气体 $PV_m=RT$。分子本身有体积，可活动空间减小为 $V_m-b$，故 $P(V_m-b)=RT$。分子间吸引力使器壁所受压强减小，内聚压强（内压强）正比于分子数密度平方 $\\propto 1/V_m^2$，故实际压强为：")+
   fml("P = \\frac{RT}{V_m-b} - \\frac{a}{V_m^2}")+
   p("整理即得范德瓦尔斯方程。其中 $b\\approx 4N_A\\cdot(4\\pi r^3/3)$ 为分子本身体积的 4 倍，$a$ 由分子间吸引力强度决定。"))+
   note(p("范德瓦尔斯方程定性描述了气液相变，但临界点附近定量误差较大，需用更精细的状态方程。"))
 )},
{"id":"sm3s3-2","name":"麦克斯韦等面积法则","tags":["thm","der"],"brief":"由范德瓦尔斯等温线确定气液共存压强。",
 "body": wrap(
   thm("麦克斯韦等面积法则",p("对范德瓦尔斯等温线中 $S$ 形（非物理）部分，气液共存压强 $P_0$ 由水平线与曲线围成的两面积相等确定：")+
   fml("\\int_{V_l}^{V_g}(P-P_0)\\,dV = 0"))+
   der(p("<strong>由相平衡条件推导：</strong>气液平衡时 $\\mu_l=\\mu_g$。由 $d\\mu=-s\\,dT+v\\,dP$，等温下 $\\mu_g-\\mu_l=\\int_l^g v\\,dP$。沿范德瓦尔斯曲线由液态到气态积分：")+
   fml("\\mu_g-\\mu_l = \\int_{P_l}^{P_g} V_m\\,dP = 0")+
   p("分部积分得 $\\int_{V_l}^{V_g} P\\,dV - P_0(V_g-V_l)=0$，即：")+
   fml("\\int_{V_l}^{V_g} (P-P_0)\\,dV = 0")+
   p("几何上即为水平线 $P=P_0$ 与 $S$ 形曲线围成的上下两面积相等。$V_l,V_g$ 为共存液相与气相摩尔体积。"))+
   app(p("<strong>应用：</strong>等面积法则把范德瓦尔斯等温线的非物理振荡段替换为水平气液共存线，得到符合实验的相变行为。"))
 )},
{"id":"sm3s3-3","name":"范德瓦尔斯方程的临界点","tags":["der","thm"],"brief":"由等温线拐点条件确定临界参数。",
 "body": wrap(
   defn("临界点",p("临界点是气液共存曲线的顶点，临界等温线在该点有水平拐点：$(\\partial P/\\partial V)_T=0$ 且 $(\\partial^2 P/\\partial V^2)_T=0$。"))+
   der(p("<strong>由范德瓦尔斯方程求临界参数：</strong>$P=RT/(V_m-b)-a/V_m^2$。在临界点 $(P_c,V_c,T_c)$ 满足：")+
   fml("\\left(\\frac{\\partial P}{\\partial V}\\right)_T = -\\frac{RT_c}{(V_c-b)^2} + \\frac{2a}{V_c^3} = 0")+
   fml("\\left(\\frac{\\partial^2 P}{\\partial V^2}\\right)_T = \\frac{2RT_c}{(V_c-b)^3} - \\frac{6a}{V_c^4} = 0")+
   p("联立解得 $V_c=3b$，$T_c=8a/(27Rb)$，$P_c=a/(27b^2)$。定义对比变量 $P_r=P/P_c,V_r=V/V_c,T_r=T/T_c$，范德瓦尔斯方程化为对应态方程：")+
   fml("\\left(P_r+\\frac{3}{V_r^2}\\right)(3V_r-1) = 8T_r")+
   p("表明所有范德瓦尔斯气体在相同对比态下行为相同（对应态原理）。"))+
   note(p("临界压缩因子 $Z_c=P_cV_c/(RT_c)=3/8=0.375$，实际气体约 0.23–0.30，反映范德瓦尔斯方程的近似性。"))
 )},
]},
{
"name": "3.4 临界现象与临界指数",
"color": "#d97706",
"desc": "临界点附近的幂律行为与普适性",
"items": [
{"id":"sm3s4-1","name":"临界现象与幂律发散","tags":["def","der"],"brief":"临界点附近热力学量的幂律奇异性。",
 "fig":"critical","figCap":"气液共存曲线与临界点",
 "body": wrap(
   defn("临界现象",p("在临界点附近，热力学量（热容、压缩系数、磁化率等）出现幂律发散，序参量按幂律趋于零，这些普遍的幂律行为称为<strong>临界现象</strong>。"))+
   der(p("<strong>幂律形式：</strong>以气液相变为例，定义约化温度 $t=(T-T_c)/T_c$。临界点附近：")+
   fml("C_V \\propto |t|^{-\\alpha}\\ (\\text{热容发散}),\\quad \\kappa_T \\propto |t|^{-\\gamma}\\ (\\text{压缩系数发散})")+
   fml("\\rho_l-\\rho_g \\propto |t|^\\beta\\ (\\text{序参量}),\\quad |P-P_c| \\propto |\\rho-\\rho_c|^\\delta\\ (\\text{临界等温线})")+
   p("指数 $\\alpha,\\beta,\\gamma,\\delta$ 称为<strong>临界指数</strong>。它们与具体物质无关，只与系统的维度、序参量分量数有关，即<strong>普适性</strong>。"))+
   note(p("临界点附近涨落巨大，关联长度 $\\xi\\to\\infty$，这是出现普适幂律的物理根源。"))
 )},
{"id":"sm3s4-2","name":"六个经典临界指数","tags":["def","der"],"brief":"α,β,γ,δ,η,ν 的定义与物理意义。",
 "body": wrap(
   defn("临界指数定义",p("临界点附近主要临界指数：$\\alpha$（热容）、$\\beta$（序参量）、$\\gamma$（响应函数发散）、$\\delta$（临界等温线）、$\\eta$（关联函数衰减）、$\\nu$（关联长度发散）。"))+
   der(p("<strong>各指数含义：</strong>设 $t=(T-T_c)/T_c$，$h$ 为外场（如磁场）：")+
   fml("C \\propto |t|^{-\\alpha},\\quad \\eta_0 \\propto |t|^\\beta,\\quad \\chi \\propto |t|^{-\\gamma}")+
   fml("|h| \\propto |\\eta_0|^\\delta\\ (T=T_c),\\quad \\xi \\propto |t|^{-\\nu},\\quad G(r) \\propto r^{-(d-2+\\eta)}")+
   p("其中 $\\eta_0$ 为序参量，$\\chi$ 为磁化率/压缩系数，$\\xi$ 为关联长度，$G(r)$ 为等时关联函数，$d$ 为空间维度。"))+
   note(p("平均场理论（朗道理论）给出 $\\alpha=0,\\beta=1/2,\\gamma=1,\\delta=3,\\eta=0,\\nu=1/2$，但实验值偏离，需要重整化群修正。"))
 )},
{"id":"sm3s4-3","name":"标度律与普适性","tags":["thm","der"],"brief":"临界指数之间满足的标度关系。",
 "body": wrap(
   thm("标度律",p("临界指数并非完全独立，满足一系列标度关系，如：")+
   fml("\\alpha+2\\beta+\\gamma=2,\\quad \\gamma=\\beta(\\delta-1),\\quad \\gamma=\\nu(2-\\eta),\\quad \\nu d=2-\\alpha"))+
   der(p("<strong>由标度假设推导：</strong>标度假设认为临界点附近自由能的奇异部分是广延量的齐次函数：$f_s(t,h)=|t|^{2-\\alpha}g(h/|t|^\\Delta)$，其中 $\\Delta=\\beta+\\gamma$ 为能隙指数。对 $t$ 求二阶导得热容指数 $\\alpha$，对 $h$ 求导得序参量与磁化率：")+
   fml("\\eta_0 = -\\frac{\\partial f_s}{\\partial h} \\propto |t|^\\beta,\\quad \\chi = \\frac{\\partial \\eta_0}{\\partial h} \\propto |t|^{-\\gamma}")+
   p("由 $\\Delta=\\beta+\\gamma$ 及 $\\delta=\\Delta/\\beta$ 得 $\\gamma=\\beta(\\delta-1)$；由 $f_s\\propto|t|^{2-\\alpha}$ 与 $\\eta_0\\propto|t|^\\beta$ 的关系得 $\\alpha+2\\beta+\\gamma=2$。这些关系在实验上得到很好验证。"))+
   note(p("标度律把 6 个临界指数约化为 2 个独立指数，体现了临界现象的普适性：同一普适类（相同 $d$ 与序参量分量数 $n$）的系统有相同临界指数。"))
 )},
]},
{
"name": "3.5 朗道相变理论",
"color": "#d97706",
"desc": "序参量展开与平均场理论",
"items": [
{"id":"sm3s5-1","name":"朗道自由能展开","tags":["def","der"],"brief":"把自由能展开为序参量的幂级数。",
 "fig":"landau","figCap":"朗道自由能在 T>Tc 与 T<Tc 时的形状",
 "body": wrap(
   defn("朗道理论",p("朗道假定自由能可在临界点附近展开为序参量 $\\eta$ 的幂级数，系数为温度的解析函数。对具有 $\\eta\\to-\\eta$ 对称性的系统：")+
   fml("F(T,\\eta) = F_0(T) + a(T)\\eta^2 + b\\eta^4 + \\cdots"))+
   der(p("<strong>平衡序参量推导：</strong>取 $a(T)=a_0(T-T_c)$（$a_0>0$），$b>0$。平衡时 $\\partial F/\\partial \\eta=0$：")+
   fml("2a(T)\\eta + 4b\\eta^3 = 2\\eta\\big[a_0(T-T_c)+2b\\eta^2\\big] = 0")+
   p("当 $T>T_c$ 时，$a(T)>0$，唯一解 $\\eta=0$（高对称相，$F$ 单阱）。当 $T<T_c$ 时，$a(T)<0$，解为：")+
   fml("\\eta = \\pm\\sqrt{\\frac{a_0(T_c-T)}{2b}} \\propto |T-T_c|^{1/2}")+
   p("故朗道理论给出 $\\beta=1/2$，序参量在 $T_c$ 处连续由零变非零，描述二级相变。"))+
   note(p("朗道理论是平均场理论，忽略了涨落，在四维以上严格成立，三维下与实验有偏差。"))
 )},
{"id":"sm3s5-2","name":"朗道理论的临界指数","tags":["der","thm"],"brief":"由朗道自由能导出平均场临界指数。",
 "body": wrap(
   thm("平均场临界指数",p("朗道理论给出的临界指数为：")+
   fml("\\alpha=0,\\ \\beta=\\frac{1}{2},\\ \\gamma=1,\\ \\delta=3"))+
   der(p("<strong>推导：</strong>由上题 $\\eta\\propto|T-T_c|^{1/2}$ 得 $\\beta=1/2$。外场 $h$ 下自由能加 $-h\\eta$ 项，平衡条件 $a\\eta+2b\\eta^3=h/2$。在 $T=T_c$（$a=0$）时 $2b\\eta^3=h/2$，故 $h\\propto\\eta^3$，$\\delta=3$。磁化率 $\\chi=(\\partial\\eta/\\partial h)_T$，在 $h=0$ 附近对平衡方程求导：")+
   fml("(a+6b\\eta^2)\\frac{\\partial\\eta}{\\partial h} = \\frac{1}{2}")+
   p("$T>T_c$ 时 $\\eta=0$，$\\chi=1/(2a)\\propto(T-T_c)^{-1}$，故 $\\gamma=1$。自由能二阶导数（热容）在 $T_c$ 处有有限跳跃，按对数发散定义 $\\alpha=0$。"))+
   note(p("平均场指数与三维实验值（$\\beta\\approx0.325,\\gamma\\approx1.24$）有偏差，需重整化群修正；但朗道理论定性正确且简洁。"))
 )},
{"id":"sm3s5-3","name":"对称破缺与亚稳态","tags":["der","note"],"brief":"朗道势双阱与自发对称破缺。",
 "body": wrap(
   defn("自发对称破缺",p("当 $T<T_c$ 时，朗道自由能 $F(\\eta)$ 关于 $\\eta=0$ 对称但极小值在 $\\eta=\\pm\\eta_0$，系统自发选择其中一个极小值，原有的 $\\eta\\to-\\eta$ 对称性被破缺，称为<strong>自发对称破缺</strong>。"))+
   der(p("<strong>亚稳态与势垒：</strong>$T<T_c$ 时 $F(\\eta)$ 在 $\\eta=0$ 处有一个局域极大（势垒），$\\eta=\\pm\\eta_0$ 为两个等价极小。若系统初始处于 $\\eta=0$（高对称相），在微小扰动下可隧穿或热激发越过势垒进入极小态。当外场 $h\\neq 0$ 时，自由能变为：")+
   fml("F = F_0 + a\\eta^2 + b\\eta^4 - h\\eta")+
   p("此时两阱不对称，能量较低的阱被优先占据，序参量取与外场同号的值。当外场反转时，序参量可在势阱间跃迁，产生磁滞回线。"))+
   note(p("朗道理论是理解连续相变的基础框架，扩展为金兹堡-朗道理论后可处理空间非均匀序参量与涨落。"))
 )},
]},
]

ch4_sections = [
{
"name": "4.1 等概率原理与微观状态数",
"color": "#0d9488",
"desc": "统计物理基本假设、微观状态数与玻尔兹曼熵公式",
"items": [
{"id":"sm4s1-1","name":"等概率原理","tags":["def","der"],"brief":"孤立系统平衡态所有微观态等概率。",
 "fig":"phasespace","figCap":"μ 空间中的微观状态与相空间体积",
 "body": wrap(
   defn("等概率原理",p("对于处于平衡态的孤立系统，所有可能的微观态出现的概率相等。这是统计物理的基本假设。"))+
   der(p("<strong>与平衡态的关系：</strong>孤立系统能量 $E$ 固定，微观态对应 $\\Gamma$ 空间中能量曲面 $E$ 与 $E+dE$ 之间的相体积。等概率原理意味着系统在该能量壳层内均匀分布，每个微观态概率为 $1/\\Omega(E)$，其中 $\\Omega(E)$ 为能量 $E$ 附近的微观状态数：")+
   fml("\\Omega(E) = \\frac{1}{h^{3N}N!}\\int_{E<H<E+dE} d^{3N}q\\,d^{3N}p")+
   p("这里 $h^{3N}$ 来自量子化（相格大小），$N!$ 来自粒子全同性修正。平衡态即系统在等能面上均匀遍历，对应熵最大。"))+
   note(p("等概率原理无法从更基本原理证明，其正确性由其推论与实验一致而确立。"))
 )},
{"id":"sm4s1-2","name":"微观状态数与玻尔兹曼熵公式","tags":["thm","der"],"brief":"熵等于微观状态数的对数。",
 "body": wrap(
   thm("玻尔兹曼熵公式",p("系统的熵与微观状态数的对数成正比：")+
   fml("S = k_B \\ln \\Omega"))+
   der(p("<strong>由热力学对应关系推导：</strong>对孤立系统，平衡态对应 $\\Omega$ 最大（等概率原理），而热力学上平衡态对应 $S$ 最大。故 $S$ 必为 $\\Omega$ 的单调增函数。熵是广延量，两个子系统总微观状态数 $\\Omega=\\Omega_1\\Omega_2$，要求 $S=S_1+S_2$。唯一满足 $S(\\Omega_1\\Omega_2)=S(\\Omega_1)+S(\\Omega_2)$ 的函数形式为对数：")+
   fml("S = k_B \\ln \\Omega")+
   p("比例常数 $k_B$ 由热力学关系 $1/T=(\\partial S/\\partial E)_V$ 确定，与玻尔兹曼常数一致。"))+
   note(p("玻尔兹曼公式刻在玻尔兹曼墓碑上，是统计物理的标志性公式，把宏观熵与微观无序度联系起来。"))
 )},
{"id":"sm4s1-3","name":"近独立粒子的微观状态数","tags":["der","note"],"brief":"定域、玻尔兹曼、玻色、费米四种微观状态数。",
 "body": wrap(
   defn("近独立粒子系统",p("粒子间相互作用可忽略，系统能量等于各粒子能量之和 $E=\\sum_i n_i\\varepsilon_i$，其中 $n_i$ 为能级 $\\varepsilon_i$ 上的粒子数。"))+
   der(p("<strong>四种统计的微观状态数：</strong>设能级 $\\varepsilon_i$ 简并度为 $g_i$，占据数为 $n_i$。")+
   fml("\\text{定域（玻尔兹曼）}:\\ \\Omega = N!\\prod_i \\frac{g_i^{n_i}}{n_i!}")+
   fml("\\text{玻尔兹曼（可分辨近似）}:\\ \\Omega = \\prod_i \\frac{g_i^{n_i}}{n_i!}")+
   fml("\\text{玻色}:\\ \\Omega = \\prod_i \\frac{(n_i+g_i-1)!}{n_i!(g_i-1)!}")+
   fml("\\text{费米}:\\ \\Omega = \\prod_i \\frac{g_i!}{n_i!(g_i-n_i)!}")+
   p("差异来自粒子是否可分辨与是否受泡利不相容原理限制。定域粒子可分辨（如晶格振动），玻尔兹曼气体不可分辨但非简并，玻色子不限占据数，费米子每态最多一个。"))+
   note(p("经典极限（高温低密度）下，$n_i\\ll g_i$，玻色与费米统计均退化为玻尔兹曼统计。"))
 )},
]},
{
"name": "4.2 玻尔兹曼分布的推导",
"color": "#0d9488",
"desc": "由最概然法导出玻尔兹曼分布",
"items": [
{"id":"sm4s2-1","name":"玻尔兹曼分布","tags":["thm","der"],"brief":"近独立可分辨粒子的最概然分布。",
 "fig":"boltzmann","figCap":"玻尔兹曼分布随能量指数衰减",
 "body": wrap(
   thm("玻尔兹曼分布",p("近独立定域（或非简并）粒子系统平衡态的最概然分布为：")+
   fml("n_i = g_i e^{-\\alpha-\\beta\\varepsilon_i} = N\\frac{g_i e^{-\\varepsilon_i/k_B T}}{Z_1}")+
   p("其中 $Z_1=\\sum_i g_i e^{-\\beta\\varepsilon_i}$ 为单粒子配分函数。"))+
   der(p("<strong>最概然法推导：</strong>定域系统微观状态数 $\\Omega=N!\\prod_i g_i^{n_i}/n_i!$。在约束 $\\sum n_i=N$、$\\sum n_i\\varepsilon_i=E$ 下求 $\\Omega$ 极大。用斯特林近似 $\\ln n!\\approx n\\ln n-n$，对 $\\ln\\Omega$ 求变分并引入拉格朗日乘子 $\\alpha,\\beta$：")+
   fml("\\delta\\left[\\ln\\Omega - \\alpha\\sum n_i - \\beta\\sum n_i\\varepsilon_i\\right] = 0")+
   fml("\\sum_i \\left[\\ln\\frac{g_i}{n_i} - \\alpha - \\beta\\varepsilon_i\\right]\\delta n_i = 0")+
   p("由 $\\delta n_i$ 任意性得 $\\ln(g_i/n_i)-\\alpha-\\beta\\varepsilon_i=0$，即 $n_i=g_i e^{-\\alpha-\\beta\\varepsilon_i}$。由 $\\sum n_i=N$ 定 $\\alpha$，由热力学关系 $\\beta=1/(k_B T)$ 定 $\\beta$。"))+
   note(p("玻尔兹曼分布表明低能级粒子数多于高能级，粒子数随能量指数衰减，衰减速度由温度决定。"))
 )},
{"id":"sm4s2-2","name":"配分函数与热力学量","tags":["der","app"],"brief":"由单粒子配分函数求内能、熵等。",
 "body": wrap(
   defn("单粒子配分函数",p("定义单粒子配分函数 $Z_1=\\sum_i g_i e^{-\\beta\\varepsilon_i}$，它是所有单粒子能级玻尔兹曼因子的加权和，是统计物理的核心计算量。"))+
   der(p("<strong>由配分函数求热力学量：</strong>系统配分函数对 $N$ 个近独立定域粒子 $Z=Z_1^N$（对玻尔兹曼气体需除以 $N!$）。内能：")+
   fml("U = N\\langle\\varepsilon\\rangle = N\\frac{\\sum_i \\varepsilon_i g_i e^{-\\beta\\varepsilon_i}}{Z_1} = -N\\frac{\\partial \\ln Z_1}{\\partial \\beta}")+
   p("熵由玻尔兹曼公式或 $S=k_B(\\ln Z+\\beta U)$ 计算：")+
   fml("S = Nk_B\\left(\\ln Z_1 + \\beta\\langle\\varepsilon\\rangle\\right)")+
   p("自由能 $F=-k_B T\\ln Z$，压强 $P=-\\partial F/\\partial V$。一切热力学量均可由配分函数导出。"))+
   app(p("<strong>应用：</strong>配分函数是统计物理的「桥梁」，把微观能级结构与宏观热力学量联系起来。计算配分函数是统计力学的核心任务。"))
 )},
{"id":"sm4s2-3","name":"β=1/(k_BT) 的热力学证明","tags":["der","note"],"brief":"由热力学温度定义确定拉格朗日乘子。",
 "body": wrap(
   defn("β 的物理意义",p("玻尔兹曼分布中的拉格朗日乘子 $\\beta$ 与热力学温度一一对应，需由热力学关系确定。"))+
   der(p("<strong>由熵的偏导数推导：</strong>由玻尔兹曼分布得系统熵 $S=k_B(\\ln Z+\\beta U)$。对 $U$ 求偏导（$V$ 不变）：")+
   fml("\\left(\\frac{\\partial S}{\\partial U}\\right)_V = k_B\\left[\\frac{\\partial \\ln Z}{\\partial U} + U\\frac{\\partial \\beta}{\\partial U} + \\beta\\right]")+
   p("由于 $\\partial \\ln Z/\\partial U=(\\partial \\ln Z/\\partial\\beta)(\\partial\\beta/\\partial U)=-U\\,\\partial\\beta/\\partial U$，上式前两项抵消，得：")+
   fml("\\left(\\frac{\\partial S}{\\partial U}\\right)_V = k_B\\beta")+
   p("而热力学定义 $1/T=(\\partial S/\\partial U)_V$，故 $\\beta=1/(k_B T)$。"))+
   note(p("此证明建立了统计温度与热力学温度的等价性，是统计力学与热力学自洽性的关键一环。"))
 )},
]},
{
"name": "4.3 麦克斯韦速度分布律",
"color": "#0d9488",
"desc": "由玻尔兹曼分布导出分子速度分布",
"items": [
{"id":"sm4s3-1","name":"麦克斯韦速度分布律","tags":["thm","der"],"brief":"平衡态理想气体分子速度的概率分布。",
 "fig":"maxwelldist","figCap":"麦克斯韦速率分布随温度的变化",
 "body": wrap(
   thm("麦克斯韦速度分布",p("平衡态下理想气体分子速度分量的概率密度为：")+
   fml("f(v_x,v_y,v_z) = \\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2} e^{-m(v_x^2+v_y^2+v_z^2)/(2k_B T)}"))+
   der(p("<strong>由玻尔兹曼分布推导：</strong>平动动能 $\\varepsilon=p^2/(2m)=m(v_x^2+v_y^2+v_z^2)/2$。由玻尔兹曼分布，速度在 $\\mathbf{v}\\sim\\mathbf{v}+d\\mathbf{v}$ 区间的分子数正比于 $e^{-\\beta\\varepsilon}d^3v$。归一化：")+
   fml("f(\\mathbf{v})d^3v = \\frac{1}{Z_1}e^{-mv^2/(2k_B T)}d^3v,\\quad Z_1=\\int e^{-mv^2/(2k_B T)}d^3v = \\left(\\frac{2\\pi k_B T}{m}\\right)^{3/2}")+
   fml("\\implies f(\\mathbf{v}) = \\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2} e^{-mv^2/(2k_B T)}")+
   p("三个速度分量独立且各服从高斯分布，方差为 $k_B T/m$。"))+
   note(p("麦克斯韦分布是玻尔兹曼分布对连续平动能级的特例，是分子动理论的基础。"))
 )},
{"id":"sm4s3-2","name":"麦克斯韦速率分布与特征速率","tags":["der","app"],"brief":"速率分布、最概然/平均/方均根速率。",
 "body": wrap(
   defn("速率分布",p("由速度分布转换到球坐标并对角度积分，得速率分布：")+
   fml("f(v) = 4\\pi\\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2} v^2 e^{-mv^2/(2k_B T)}"))+
   der(p("<strong>三种特征速率推导：</strong>最概然速率 $v_p$ 由 $df/dv=0$ 给出：")+
   fml("\\frac{d}{dv}\\left(v^2 e^{-mv^2/(2k_B T)}\\right)=0 \\implies v_p = \\sqrt{\\frac{2k_B T}{m}}")+
   p("平均速率：")+
   fml("\\langle v\\rangle = \\int_0^\\infty v f(v)dv = \\sqrt{\\frac{8k_B T}{\\pi m}}")+
   p("方均根速率：")+
   fml("v_{\\text{rms}} = \\sqrt{\\langle v^2\\rangle} = \\sqrt{\\frac{3k_B T}{m}}")+
   p("三者大小关系 $v_p < \\langle v\\rangle < v_{\\text{rms}}$，比值 $1:1.128:1.225$。"))+
   app(p("<strong>应用：</strong>速率分布用于计算气体输运系数（粘滞、热导、扩散），分子束实验直接验证了麦克斯韦分布。"))
 )},
{"id":"sm4s3-3","name":"压强公式与温度的统计意义","tags":["der","thm"],"brief":"由分子动理论推导理想气体压强。",
 "body": wrap(
   thm("理想气体压强公式",p("由分子对器壁的冲量可得：")+
   fml("P = \\frac{1}{3}nm\\langle v^2\\rangle = \\frac{2}{3}n\\langle\\varepsilon_k\\rangle")+
   p("其中 $n=N/V$ 为分子数密度，$\\langle\\varepsilon_k\\rangle$ 为平均平动动能。"))+
   der(p("<strong>由分子碰撞推导：</strong>一个分子以速度 $v_x$ 碰撞单位面积器壁，动量改变 $2mv_x$，单位时间碰撞次数为 $n v_x/2$（只计正方向）。对 $v_x>0$ 积分：")+
   fml("P = \\int_{v_x>0} n\\cdot 2mv_x\\cdot v_x f(v_x)dv_x = nm\\int_{-\\infty}^\\infty v_x^2 f(v_x)dv_x = nm\\langle v_x^2\\rangle")+
   p("由各向同性 $\\langle v_x^2\\rangle=\\langle v_y^2\\rangle=\\langle v_z^2\\rangle=\\langle v^2\\rangle/3$，故 $P=nm\\langle v^2\\rangle/3$。结合 $\\langle v^2\\rangle=3k_B T/m$ 得 $P=nk_B T$，与理想气体状态方程一致。由此：")+
   fml("\\langle\\varepsilon_k\\rangle = \\frac{3}{2}k_B T")+
   p("温度是分子平均平动动能的度量。"))+
   note(p("压强公式揭示了压强的微观本质：大量分子对器壁碰撞的平均冲力。"))
 )},
]},
{
"name": "4.4 能量均分定理",
"color": "#0d9488",
"desc": "每个平方自由度平均分配 kT/2 的能量",
"items": [
{"id":"sm4s4-1","name":"能量均分定理","tags":["thm","der"],"brief":"每个平方项自由度平均能量为 kT/2。",
 "fig":"equipartition","figCap":"单原子、双原子与多原子分子的自由度",
 "body": wrap(
   thm("能量均分定理",p("温度 $T$ 下，系统能量表达式中每个独立的平方项自由度的平均能量为 $\\frac{1}{2}k_B T$：")+
   fml("\\langle \\frac{1}{2}a_i x_i^2 \\rangle = \\frac{1}{2}k_B T"))+
   der(p("<strong>由玻尔兹曼分布推导：</strong>设能量中某平方项为 $\\varepsilon_i=\\frac{1}{2}a x^2$，其平均值为：")+
   fml("\\langle \\varepsilon_i \\rangle = \\frac{\\int (\\frac{1}{2}a x^2)e^{-\\beta a x^2/2}dx}{\\int e^{-\\beta a x^2/2}dx}")+
   p("利用高斯积分 $\\int_{-\\infty}^\\infty e^{-\\alpha x^2}dx=\\sqrt{\\pi/\\alpha}$ 与 $\\int x^2 e^{-\\alpha x^2}dx=\\frac{1}{2}\\sqrt{\\pi/\\alpha^3}$：")+
   fml("\\langle \\varepsilon_i \\rangle = \\frac{1}{2}a\\cdot\\frac{1}{2\\beta a} \\cdot 2 = \\frac{1}{2\\beta} = \\frac{1}{2}k_B T")+
   p("即每个平方自由度平均能量 $k_B T/2$。"))+
   note(p("能量均分定理是经典统计的结果，只在高温极限（能级间距远小于 $k_B T$）下成立，低温下量子效应显著，定理失效。"))
 )},
{"id":"sm4s4-2","name":"理想气体热容与自由度","tags":["der","app"],"brief":"由自由度预测气体摩尔热容。",
 "body": wrap(
   defn("自由度",p("分子能量中平方项的数目称为<strong>自由度</strong> $f$。单原子分子 $f=3$（平动）；双原子分子常温下 $f=5$（3 平动+2 转动），高温下 $f=7$（再加 2 振动）；多原子分子 $f\\geq 6$。"))+
   der(p("<strong>由能量均分定理推热容：</strong>每个自由度贡献 $\\frac{1}{2}R$ 摩尔热容。对 $f$ 个自由度：")+
   fml("U_m = \\frac{f}{2}RT,\\quad C_{V,m} = \\frac{f}{2}R")+
   fml("C_{P,m} = C_{V,m}+R = \\frac{f+2}{2}R,\\quad \\gamma = \\frac{C_P}{C_V} = \\frac{f+2}{f}")+
   p("单原子 $f=3$：$C_V=\\frac{3}{2}R,\\gamma=5/3\\approx1.67$；双原子常温 $f=5$：$C_V=\\frac{5}{2}R,\\gamma=7/5=1.4$；多原子 $f=6$：$C_V=3R,\\gamma=4/3\\approx1.33$，与实验基本符合。"))+
   app(p("<strong>应用：</strong>能量均分定理解释了常温下气体热容的实验规律；低温下振动自由度「冻结」，热容下降，这是经典物理无法解释、需量子理论的重要证据。"))
 )},
{"id":"sm4s4-3","name":"能量均分的失败与量子修正","tags":["note","der"],"brief":"低温下自由度冻结与量子热容。",
 "body": wrap(
   defn("自由度冻结",p("当温度 $T$ 低于某自由度的特征温度 $\\Theta$（$k_B\\Theta\\sim$ 能级间距）时，该自由度不能被热激发，对热容无贡献，称为<strong>自由度冻结</strong>。"))+
   der(p("<strong>双原子分子振动热容推导：</strong>振动能级 $\\varepsilon_n=(n+1/2)\\hbar\\omega$，配分函数 $Z_v=e^{-\\beta\\hbar\\omega/2}/(1-e^{-\\beta\\hbar\\omega})$，平均振动能量：")+
   fml("\\langle \\varepsilon_v \\rangle = -\\frac{\\partial \\ln Z_v}{\\partial \\beta} = \\frac{\\hbar\\omega}{2} + \\frac{\\hbar\\omega}{e^{\\Theta_v/T}-1}")+
   p("其中 $\\Theta_v=\\hbar\\omega/k_B$ 为振动特征温度。振动热容：")+
   fml("C_{V,v} = R\\left(\\frac{\\Theta_v}{T}\\right)^2 \\frac{e^{\\Theta_v/T}}{(e^{\\Theta_v/T}-1)^2}")+
   p("当 $T\\gg\\Theta_v$ 时 $C_{V,v}\\to R$（经典结果，2 平方项各 $R/2$）；当 $T\\ll\\Theta_v$ 时 $C_{V,v}\\to 0$（冻结）。"))+
   note(p("经典能量均分定理无法解释低温热容下降，爱因斯坦与德拜的量子热容理论成功解决了这一问题。"))
 )},
]},
{
"name": "4.5 理想气体的热力学函数",
"color": "#0d9488",
"desc": "由配分函数计算理想气体的内能、熵、自由能",
"items": [
{"id":"sm4s5-1","name":"单原子理想气体配分函数","tags":["der","app"],"brief":"由平动能级配分函数求热力学量。",
 "body": wrap(
   defn("平动配分函数",p("单原子分子只有平动自由度，能级 $\\varepsilon=h^2(n_x^2+n_y^2+n_z^2)/(8mL^2)$。宏观系统能级密集，求和可化为积分：")+
   fml("Z_1 = \\frac{V}{h^3}\\int e^{-p^2/(2mk_B T)}d^3p = V\\left(\\frac{2\\pi m k_B T}{h^2}\\right)^{3/2}"))+
   der(p("<strong>系统配分函数与热力学量：</strong>对 $N$ 个不可分辨粒子，系统配分函数 $Z=Z_1^N/N!$。内能：")+
   fml("U = -N\\frac{\\partial \\ln Z_1}{\\partial \\beta} = -N\\frac{\\partial}{\\partial \\beta}\\left[\\frac{3}{2}\\ln\\frac{2\\pi m}{h^2\\beta}\\right] = \\frac{3}{2}Nk_B T")+
   p("自由能（用斯特林近似 $\\ln N!\\approx N\\ln N-N$）：")+
   fml("F = -k_B T\\ln Z = -Nk_B T\\left[\\ln\\frac{V}{N}\\left(\\frac{2\\pi m k_B T}{h^2}\\right)^{3/2}+1\\right]")+
   p("由此可求压强 $P=-\\partial F/\\partial V=Nk_B T/V$，回到理想气体状态方程。"))+
   note(p("配分函数方法是统计物理的标准程序：求能级 → 配分函数 → 热力学量，一切宏观量都可由此得出。"))
 )},
{"id":"sm4s5-2","name":"萨库尔-泰特洛德公式（理想气体熵）","tags":["der","thm"],"brief":"单原子理想气体的绝对熵。",
 "body": wrap(
   thm("萨库尔-泰特洛德公式",p("单原子理想气体的熵为：")+
   fml("S = Nk_B\\left\\{\\ln\\left[\\frac{V}{N}\\left(\\frac{2\\pi m k_B T}{h^2}\\right)^{3/2}\\right]+\\frac{5}{2}\\right\\}"))+
   der(p("<strong>由配分函数推导：</strong>由 $S=k_B(\\ln Z+\\beta U)$，代入 $Z=Z_1^N/N!$、$U=3Nk_B T/2$：")+
   fml("\\ln Z = N\\ln Z_1 - \\ln N! \\approx N\\ln Z_1 - N\\ln N + N")+
   fml("S = k_B(N\\ln Z_1 - N\\ln N + N) + k_B\\beta\\cdot\\frac{3}{2}Nk_B T")+
   fml("= Nk_B\\left[\\ln\\frac{Z_1}{N}+1+\\frac{3}{2}\\right] = Nk_B\\left[\\ln\\left(\\frac{V}{N}\\left(\\frac{2\\pi m k_B T}{h^2}\\right)^{3/2}\\right)+\\frac{5}{2}\\right]")+
   p("该公式正确解释了吉布斯佯谬：引入 $N!$ 因子后熵成为广延量，同种气体等温等压混合熵变为零。"))+
   app(p("<strong>应用：</strong>萨库尔-泰特洛德公式给出了理想气体的绝对熵，与热力学第三定律一致，是量子统计（含 $h$ 与 $N!$）的成功例证。"))
 )},
{"id":"sm4s5-3","name":"双原子理想气体的配分函数","tags":["der","note"],"brief":"平动、转动、振动配分函数的分离。",
 "body": wrap(
   defn("配分函数可分离性",p("双原子分子能量可分解为平动、转动、振动之和 $\\varepsilon=\\varepsilon_t+\\varepsilon_r+\\varepsilon_v$，故单粒子配分函数可分离：")+
   fml("Z_1 = Z_t \\cdot Z_r \\cdot Z_v"))+
   der(p("<strong>各自由度配分函数：</strong>平动 $Z_t=V(2\\pi m k_B T/h^2)^{3/2}$。转动能级 $\\varepsilon_r=J(J+1)\\hbar^2/(2I)$，高温下 $Z_r=8\\pi^2 I k_B T/(\\sigma h^2)$（$\\sigma$ 为对称数，同核 $\\sigma=2$，异核 $\\sigma=1$）。振动：")+
   fml("Z_v = \\frac{e^{-\\beta\\hbar\\omega/2}}{1-e^{-\\beta\\hbar\\omega}}")+
   p("总内能 $U=Nk_B T^2\\partial\\ln Z_1/\\partial T$ 为各自由度贡献之和。常温下转动已激发（$Z_r\\propto T$，贡献 $Nk_B T$），振动未激发，故 $U=\\frac{3}{2}Nk_B T+Nk_B T=\\frac{5}{2}Nk_B T$，$C_V=\\frac{5}{2}Nk_B$。"))+
   note(p("配分函数的可分离性源于能量可加性，这是统计物理计算分子热力学性质的重要简化。"))
 )},
]},
]

ch5_sections = [
{
"name": "5.1 微正则系综",
"color": "#0891b2",
"desc": "孤立系统的统计描述与等概率原理",
"items": [
{"id":"sm5s1-1","name":"系综的概念","tags":["def","der"],"brief":"大量同宏观条件系统副本的集合。",
 "fig":"ensemble","figCap":"系综：大量同宏观条件的系统副本",
 "body": wrap(
   defn("系综",p("系综是大量结构相同、宏观条件相同的系统副本的集合，每个副本代表系统的一个可能微观态。统计平均等于系综平均，这是统计力学的基本方法。"))+
   der(p("<strong>系综平均与时间平均：</strong>宏观量的观测值是时间平均。各态历经假设认为时间平均等于系综平均：")+
   fml("\\bar{A} = \\lim_{T\\to\\infty}\\frac{1}{T}\\int_0^T A(t)dt = \\langle A\\rangle = \\sum_i A_i P_i")+
   p("其中 $P_i$ 为系统处于微观态 $i$ 的概率。引入系综后，时间平均转化为对系综的概率平均，便于数学计算。"))+
   note(p("系综并非真实存在的物理实体，而是为计算统计平均而引入的概念工具。"))
 )},
{"id":"sm5s1-2","name":"微正则系综与等概率分布","tags":["thm","der"],"brief":"孤立系统在等能面上均匀分布。",
 "body": wrap(
   thm("微正则分布",p("孤立系统（$E,V,N$ 固定）的平衡态系综为微正则系综，其概率分布为：")+
   fml("P_i = \\frac{1}{\\Omega(E,V,N)},\\quad E \\leq E_i \\leq E+\\Delta E"))+
   der(p("<strong>由等概率原理推导：</strong>孤立系统能量守恒，只能在能量壳层 $E\\sim E+\\Delta E$ 内的微观态间演化。等概率原理断言所有这些微观态概率相等。设该壳层微观状态数为 $\\Omega(E,V,N)$，则每个态概率为 $1/\\Omega$。熵由玻尔兹曼公式给出：")+
   fml("S(E,V,N) = k_B \\ln \\Omega(E,V,N)")+
   p("由 $S$ 可导出全部热力学量：$1/T=(\\partial S/\\partial E)_V$，$P/T=(\\partial S/\\partial V)_E$，$\\mu/T=-(\\partial S/\\partial N)_E$。"))+
   note(p("微正则系综是最基本的系综，正则与巨正则系综可由其与热源/粒子库耦合导出。"))
 )},
{"id":"sm5s1-3","name":"微正则系综计算理想气体熵","tags":["der","app"],"brief":"由相空间体积计算理想气体熵。",
 "body": wrap(
   defn("微正则配分函数",p("微正则系综的「配分函数」即微观状态数 $\\Omega(E,V,N)$，对经典理想气体等于能量壳层的相体积除以 $h^{3N}N!$。"))+
   der(p("<strong>相空间体积计算：</strong>$\\Gamma$ 空间中能量小于 $E$ 的相体积为：")+
   fml("\\Sigma(E) = \\frac{1}{h^{3N}N!}\\int_{H\\leq E} d^{3N}q\\,d^{3N}p = \\frac{V^N}{h^{3N}N!}\\cdot \\frac{\\pi^{3N/2}}{(3N/2)!}(2mE)^{3N/2}")+
   p("能量壳层体积 $\\Omega=d\\Sigma/dE\\cdot\\Delta E$。取对数并用斯特林近似：")+
   fml("\\ln\\Omega = N\\ln\\frac{V}{N} + \\frac{3N}{2}\\ln\\frac{4\\pi m E}{3Nh^2} + \\frac{5N}{2}")+
   p("代入 $E=3Nk_B T/2$，得 $S=k_B\\ln\\Omega$，与萨库尔-泰特洛德公式一致。"))+
   app(p("<strong>应用：</strong>微正则系综直接联系微观状态数与熵，是理解熵的微观意义的最直接途径。"))
 )},
]},
{
"name": "5.2 正则系综",
"color": "#0891b2",
"desc": "与热源接触的封闭系统的统计描述",
"items": [
{"id":"sm5s2-1","name":"正则系综与正则分布","tags":["thm","der"],"brief":"等温系统按玻尔兹曼因子分布。",
 "fig":"canonical","figCap":"正则系综：系统与大热源接触",
 "body": wrap(
   thm("正则分布",p("与温度 $T$ 的大热源接触、$V,N$ 固定的系统，平衡时处于微观态 $i$（能量 $E_i$）的概率为：")+
   fml("P_i = \\frac{1}{Z}e^{-\\beta E_i},\\quad Z=\\sum_i e^{-\\beta E_i},\\quad \\beta=\\frac{1}{k_B T}"))+
   der(p("<strong>由微正则系综推导：</strong>把系统与热源合起来视为孤立系统，总能量 $E_0=E_i+E_r$。由微正则分布，系统处于态 $i$ 时热源可取 $\\Omega_r(E_0-E_i)$ 个态，故：")+
   fml("P_i \\propto \\Omega_r(E_0-E_i) = e^{S_r(E_0-E_i)/k_B}")+
   p("展开 $S_r(E_0-E_i)\\approx S_r(E_0)-E_i\\cdot(\\partial S_r/\\partial E_r)=S_r(E_0)-E_i/T$：")+
   fml("P_i \\propto e^{-E_i/(k_B T)} = e^{-\\beta E_i}")+
   p("归一化得正则分布。$Z=\\sum_i e^{-\\beta E_i}$ 为正则配分函数。"))+
   note(p("正则系综适用于等温封闭系统，是统计物理中最常用的系综。"))
 )},
{"id":"sm5s2-2","name":"配分函数与热力学量的关系","tags":["der","thm"],"brief":"由正则配分函数求所有热力学量。",
 "body": wrap(
   thm("热力学量公式",p("由正则配分函数 $Z$ 可求出系统所有热力学量：")+
   fml("U = -\\frac{\\partial \\ln Z}{\\partial \\beta},\\quad F = -k_B T\\ln Z,\\quad S = k_B(\\ln Z+\\beta U)"))+
   der(p("<strong>推导：</strong>内能为能量的统计平均：")+
   fml("U = \\langle E\\rangle = \\sum_i E_i P_i = \\frac{1}{Z}\\sum E_i e^{-\\beta E_i} = -\\frac{1}{Z}\\frac{\\partial Z}{\\partial \\beta} = -\\frac{\\partial \\ln Z}{\\partial \\beta}")+
   p("自由能由正则分布与热力学关系 $F=U-TS$ 及 $P_i=e^{(F-E_i)/(k_B T)}$（由 $Z=e^{-\\beta F}$）得 $F=-k_B T\\ln Z$。压强：")+
   fml("P = -\\left(\\frac{\\partial F}{\\partial V}\\right)_T = k_B T\\left(\\frac{\\partial \\ln Z}{\\partial V}\\right)_T")+
   p("熵 $S=-(\\partial F/\\partial T)_V=k_B(\\ln Z+\\beta U)$。"))+
   note(p("配分函数 $Z$ 是正则系综的核心，一旦求出 $Z$，系统全部平衡态热力学性质便确定。"))
 )},
{"id":"sm5s2-3","name":"正则系综的能量涨落","tags":["der","note"],"brief":"能量涨落与热容成正比。",
 "body": wrap(
   defn("能量涨落",p("正则系综中系统能量不固定，围绕平均值 $\\langle E\\rangle$ 涨落，其均方涨落为：")+
   fml("\\langle (\\Delta E)^2\\rangle = \\langle E^2\\rangle - \\langle E\\rangle^2"))+
   der(p("<strong>由配分函数推导：</strong>$\\langle E^2\\rangle=(1/Z)\\partial^2 Z/\\partial\\beta^2$，$\\langle E\\rangle=-(1/Z)\\partial Z/\\partial\\beta$。故：")+
   fml("\\langle E^2\\rangle - \\langle E\\rangle^2 = \\frac{\\partial^2 \\ln Z}{\\partial \\beta^2} = -\\frac{\\partial \\langle E\\rangle}{\\partial \\beta}")+
   fml("= k_B T^2 \\frac{\\partial \\langle E\\rangle}{\\partial T} = k_B T^2 C_V")+
   p("相对涨落 $\\sqrt{\\langle(\\Delta E)^2\\rangle}/\\langle E\\rangle\\propto 1/\\sqrt{N}$，对宏观系统极小（$\\sim 10^{-12}$），故正则系综与微正则系综给出相同的宏观结果。"))+
   note(p("能量涨落公式把宏观可测量热容 $C_V$ 与微观涨落联系起来，是涨落-耗散关系的特例。"))
 )},
]},
{
"name": "5.3 巨正则系综",
"color": "#0891b2",
"desc": "与热源和粒子库接触的开放系统",
"items": [
{"id":"sm5s3-1","name":"巨正则系综与巨正则分布","tags":["thm","der"],"brief":"开放系统按能量与粒子数的联合分布。",
 "fig":"grand","figCap":"巨正则系综：系统与热源及粒子库接触",
 "body": wrap(
   thm("巨正则分布",p("与温度 $T$、化学势 $\\mu$ 的热源/粒子库接触、$V$ 固定的开放系统，处于粒子数 $N$、能量 $E_i$ 态的概率为：")+
   fml("P_{N,i} = \\frac{1}{\\Xi}e^{-\\beta(E_i-\\mu N)},\\quad \\Xi=\\sum_{N,i}e^{-\\beta(E_i-\\mu N)}"))+
   der(p("<strong>由微正则系综推导：</strong>系统+热源+粒子库合为孤立系统。系统取 $N$ 个粒子、能量 $E_i$ 时，库的微观状态数为 $\\Omega_r(E_0-E_i,N_0-N)$，故：")+
   fml("P_{N,i} \\propto \\Omega_r(E_0-E_i,N_0-N) = e^{S_r(E_0-E_i,N_0-N)/k_B}")+
   p("对 $S_r$ 作二元泰勒展开：")+
   fml("S_r(E_0-E_i,N_0-N) \\approx S_r(E_0,N_0) - \\frac{E_i}{T} + \\frac{\\mu N}{T}")+
   p("故 $P_{N,i}\\propto e^{-\\beta(E_i-\\mu N)}$，归一化引入巨配分函数 $\\Xi$。"))+
   note(p("巨正则系综适用于开放系统，粒子数可变，是处理量子统计（玻色/费米分布）的自然框架。"))
 )},
{"id":"sm5s3-2","name":"巨配分函数与热力学量","tags":["der","app"],"brief":"由巨配分函数求压强、平均粒子数等。",
 "body": wrap(
   defn("巨配分函数",p("巨配分函数 $\\Xi=\\sum_{N=0}^\\infty \\sum_i e^{-\\beta(E_i-\\mu N)}=\\sum_N e^{\\beta\\mu N}Z_N(V,T)$，其中 $Z_N$ 为 $N$ 粒子正则配分函数。"))+
   der(p("<strong>热力学量公式：</strong>平均粒子数与内能：")+
   fml("\\langle N\\rangle = \\frac{1}{\\Xi}\\sum N e^{-\\beta(E-\\mu N)} = \\frac{1}{\\beta}\\frac{\\partial \\ln \\Xi}{\\partial \\mu}")+
   fml("U = \\langle E\\rangle = -\\frac{\\partial \\ln \\Xi}{\\partial \\beta} + \\mu\\langle N\\rangle")+
   p("压强由巨势 $\\Omega=-k_B T\\ln\\Xi$ 给出（$\\Omega=-PV$）：")+
   fml("P = \\frac{k_B T}{V}\\ln \\Xi")+
   p("熵 $S=k_B(\\ln\\Xi+\\beta(U-\\mu\\langle N\\rangle))$。"))+
   app(p("<strong>应用：</strong>巨正则系综是推导玻色分布与费米分布的最方便工具，对无相互作用量子气体可直接求出单粒子态的平均占据数。"))
 )},
{"id":"sm5s3-3","name":"粒子数涨落与等温压缩系数","tags":["der","note"],"brief":"粒子数涨落与等温压缩系数的关系。",
 "body": wrap(
   defn("粒子数涨落",p("巨正则系综中粒子数不固定，其均方涨落为：")+
   fml("\\langle (\\Delta N)^2\\rangle = \\langle N^2\\rangle-\\langle N\\rangle^2"))+
   der(p("<strong>由巨配分函数推导：</strong>$\\langle N\\rangle=(1/\\beta)\\partial\\ln\\Xi/\\partial\\mu$，再对 $\\mu$ 求导：")+
   fml("\\langle N^2\\rangle-\\langle N\\rangle^2 = \\frac{1}{\\beta^2}\\frac{\\partial^2 \\ln \\Xi}{\\partial \\mu^2} = \\frac{1}{\\beta}\\frac{\\partial \\langle N\\rangle}{\\partial \\mu}")+
   p("利用热力学关系 $(\\partial\\mu/\\partial N)_{T,V}=-V(\\partial P/\\partial N)_{T,V}/(\\partial N/\\partial V)_{T,\\mu}$ 与 $\\kappa_T$ 定义，可化为：")+
   fml("\\langle (\\Delta N)^2\\rangle = \\frac{k_B T N}{V}\\kappa_T = k_B T\\left(\\frac{\\partial \\langle N\\rangle}{\\partial \\mu}\\right)_{T,V}")+
   p("粒子数涨落与等温压缩系数成正比，临界点附近 $\\kappa_T\\to\\infty$，粒子数涨落发散。"))+
   note(p("涨落公式再次显示宏观量与微观涨落的深刻联系，临界点附近的巨大涨落导致临界乳光现象。"))
 )},
]},
{
"name": "5.4 系综之间的等价性",
"color": "#0891b2",
"desc": "热力学极限下三种系综给出相同宏观结果",
"items": [
{"id":"sm5s4-1","name":"系综等价性原理","tags":["thm","der"],"brief":"热力学极限下各系综等价。",
 "body": wrap(
   thm("系综等价性",p("在热力学极限（$N\\to\\infty,V\\to\\infty,N/V=n$ 固定）下，微正则、正则、巨正则系综给出相同的平衡态热力学量。"))+
   der(p("<strong>由涨落趋于零推导：</strong>正则系综能量相对涨落正比于 $1/\\sqrt{N}$，在热力学极限下趋于零：")+
   fml("\\frac{\\sqrt{\\langle(\\Delta E)^2\\rangle}}{U} = \\frac{\\sqrt{k_B T^2 C_V}}{U} \\propto \\frac{1}{\\sqrt{N}} \\to 0")+
   p("故正则分布在热力学极限下集中于 $E=\\langle E\\rangle$ 附近极窄区间，等价于微正则分布（$E$ 固定）。同理，巨正则系综粒子数涨落 $\\sqrt{\\langle(\\Delta N)^2\\rangle}/N\\propto 1/\\sqrt{N}\\to 0$，等价于正则系综（$N$ 固定）。"))+
   note(p("系综等价性使我们可根据计算方便选择系综：微正则适合熵，正则适合配分函数，巨正则适合量子气体。"))
 )},
{"id":"sm5s4-2","name":"热力学极限与广延性","tags":["der","note"],"brief":"广延量在热力学极限下按 N 线性增长。",
 "body": wrap(
   defn("热力学极限",p("令粒子数 $N$ 和体积 $V$ 同时趋于无穷，而数密度 $n=N/V$ 保持有限的极限过程。只有在此极限下，热力学量才是严格广延的，边界效应可忽略。"))+
   der(p("<strong>广延性验证：</strong>对正则配分函数，近独立粒子 $Z_N=Z_1^N/N!$，利用斯特林公式 $\\ln N!\\approx N\\ln N-N$：")+
   fml("\\ln Z = N\\ln Z_1 - \\ln N! \\approx N\\left(\\ln\\frac{Z_1}{N}+1\\right)")+
   p("故自由能 $F=-k_B T\\ln Z\\propto N$，为广延量。同理巨配分函数 $\\ln\\Xi\\propto V$，压强 $P=k_B T\\ln\\Xi/V$ 为强度量。这些广延性要求在热力学极限下才严格成立。"))+
   note(p("真实系统粒子数 $N\\sim 10^{23}$，已足够接近热力学极限，广延性近似极好。"))
 )},
{"id":"sm5s4-3","name":"系综选择的一般原则","tags":["app","note"],"brief":"根据系统约束与计算便利选择系综。",
 "body": wrap(
   defn("三种基本系综对比",p("微正则系综：$E,V,N$ 固定，孤立系统，分布均匀；正则系综：$T,V,N$ 固定，等温封闭系统，玻尔兹曼分布；巨正则系综：$T,V,\\mu$ 固定，等温开放系统，巨正则分布。"))+
   der(p("<strong>由约束选择系综：</strong>系统的宏观约束决定了自然系综。孤立系统→微正则；等温封闭（如置于恒温槽）→正则；等温等化学势开放（如与大库接触）→巨正则。系综等价性保证了结果与选择无关，故实际计算常选最方便的系综。例如：")+
   fml("\\text{理想气体熵}: 微正则 \\to S=k_B\\ln\\Omega")+
   fml("\\text{内能/自由能}: 正则 \\to F=-k_B T\\ln Z")+
   fml("\\text{玻色/费米分布}: 巨正则 \\to \\bar{n}_i=\\frac{1}{e^{\\beta(\\varepsilon_i-\\mu)}\\pm 1}"))+
   note(p("系综理论的建立是统计力学走向成熟的标志，由吉布斯系统发展，至今仍是平衡态统计物理的标准框架。"))
 )},
]},
{
"name": "5.5 实际气体与配分函数",
"color": "#0891b2",
"desc": "有相互作用气体的配分函数与位力展开",
"items": [
{"id":"sm5s5-1","name":"位形配分函数与相互作用","tags":["der","note"],"brief":"把配分函数分为动能与位形部分。",
 "body": wrap(
   defn("位形配分函数",p("对有相互作用的经典气体，哈密顿量 $H=\\sum p_i^2/(2m)+\\sum_{i<j}u(r_{ij})$。配分函数可分离为动能部分与位形部分：")+
   fml("Z = \\frac{1}{N!h^{3N}}\\int e^{-\\beta H}d^{3N}p\\,d^{3N}r = \\frac{Z_p}{N!}\\cdot Q"))+
   der(p("<strong>动能与位形配分函数：</strong>动能部分积分即理想气体平动配分函数的 $N$ 次方：")+
   fml("Z_p = \\left(\\frac{2\\pi m k_B T}{h^2}\\right)^{3N/2}")+
   p("位形配分函数 $Q=\\int e^{-\\beta\\sum u(r_{ij})}d^{3N}r$ 包含所有相互作用信息。内能 $U=\\frac{3}{2}Nk_B T+\\langle U_{\\text{int}}\\rangle$，其中相互作用能：")+
   fml("\\langle U_{\\text{int}}\\rangle = -\\frac{\\partial \\ln Q}{\\partial \\beta}")+
   p("对实际气体，位形配分函数通常难以精确计算，需用集团展开等近似方法。"))+
   note(p("位形配分函数是联系分子间相互作用势与宏观物态方程的桥梁。"))
 )},
{"id":"sm5s5-2","name":"迈耶集团展开与位力系数","tags":["der","thm"],"brief":"将实际气体状态方程展开为密度的幂级数。",
 "body": wrap(
   thm("迈耶展开",p("实际气体的压强可展开为粒子数密度的幂级数（位力展开）：")+
   fml("\\frac{P}{k_B T} = n + B_2(T)n^2 + B_3(T)n^3 + \\cdots"))+
   der(p("<strong>由集团展开推导：</strong>定义迈耶函数 $f_{ij}=e^{-\\beta u(r_{ij})}-1$，把位形配分函数的指数展开为集团积分。第二位力系数：")+
   fml("B_2(T) = -\\frac{1}{2}\\int f(r)d^3r = \\frac{1}{2}\\int\\left(1-e^{-\\beta u(r)}\\right)d^3r")+
   p("对刚球势，$u(r)=\\infty$（$r<d$），$B_2=2\\pi d^3/3$；对范德瓦尔斯势近似，$B_2=b-a/(RT)$，与范德瓦尔斯方程一致。高阶系数 $B_3,B_4$ 由三分子、四分子集团积分给出。"))+
   app(p("<strong>应用：</strong>位力展开是处理低密度实际气体的系统方法，第二位力系数可由散射实验测定分子间相互作用势。"))
 )},
{"id":"sm5s5-3","name":"非理想气体的内能与热容","tags":["der","app"],"brief":"相互作用对热力学量的修正。",
 "body": wrap(
   defn("相互作用能修正",p("实际气体的内能除平动动能外，还包含分子间相互作用势能 $\\langle U_{\\text{int}}\\rangle$，它依赖于温度和密度。"))+
   der(p("<strong>由配分函数推导内能修正：</strong>$U=-\\partial\\ln Z/\\partial\\beta$，位形部分贡献：")+
   fml("\\langle U_{\\text{int}}\\rangle = \\frac{\\int U_{\\text{int}} e^{-\\beta U_{\\text{int}}}d^{3N}r}{\\int e^{-\\beta U_{\\text{int}}}d^{3N}r}")+
   p("低密度下一阶近似，两分子相互作用平均贡献：")+
   fml("\\langle U_{\\text{int}}\\rangle \\approx \\frac{N^2}{2V}\\int u(r)e^{-\\beta u(r)}d^3r")+
   p("内能 $U=\\frac{3}{2}Nk_B T+\\langle U_{\\text{int}}\\rangle$，$C_V=\\frac{3}{2}Nk_B+\\partial\\langle U_{\\text{int}}\\rangle/\\partial T$。对范德瓦尔斯气体，$\\langle U_{\\text{int}}\\rangle=-aN^2/V$（吸引势），故 $C_V$ 仍与 $V$ 无关，但焦耳系数 $\\mu_J=(\\partial T/\\partial V)_U$ 非零。"))+
   note(p("分子间相互作用使实际气体内能不仅依赖温度还依赖体积，这是与理想气体的关键区别。"))
 )},
]},
]

ch6_sections = [
{
"name": "6.1 玻色分布与费米分布",
"color": "#4f46e5",
"desc": "由最概然法或巨正则系综导出量子统计分布",
"items": [
{"id":"sm6s1-1","name":"玻色分布与费米分布","tags":["thm","der"],"brief":"玻色子与费米子的平均占据数。",
 "fig":"bosefermi","figCap":"玻色、费米、玻尔兹曼分布的对比",
 "body": wrap(
   thm("量子统计分布",p("温度 $T$、化学势 $\\mu$ 下，能级 $\\varepsilon_i$ 的平均粒子数为：")+
   fml("\\bar{n}_i = \\frac{1}{e^{\\beta(\\varepsilon_i-\\mu)}-1}\\ \\text{（玻色）},\\quad \\bar{n}_i = \\frac{1}{e^{\\beta(\\varepsilon_i-\\mu)}+1}\\ \\text{（费米）}"))+
   der(p("<strong>由巨正则系综推导：</strong>对单粒子态 $i$，其巨配分函数可独立计算。玻色子（占据数 $n=0,1,2,\\dots$）：")+
   fml("\\Xi_i = \\sum_{n=0}^\\infty e^{-\\beta n(\\varepsilon_i-\\mu)} = \\frac{1}{1-e^{-\\beta(\\varepsilon_i-\\mu)}}")+
   fml("\\bar{n}_i = -\\frac{\\partial \\ln \\Xi_i}{\\partial(\\beta\\mu)} = \\frac{1}{e^{\\beta(\\varepsilon_i-\\mu)}-1}")+
   p("费米子（泡利原理 $n=0,1$）：")+
   fml("\\Xi_i = 1+e^{-\\beta(\\varepsilon_i-\\mu)},\\quad \\bar{n}_i = \\frac{1}{e^{\\beta(\\varepsilon_i-\\mu)}+1}")+
   p("当 $\\varepsilon_i-\\mu\\gg k_B T$ 时，两者都退化为玻尔兹曼分布 $\\bar{n}_i\\approx e^{-\\beta(\\varepsilon_i-\\mu)}$。"))+
   note(p("玻色分布与费米分布的差异源于粒子全同性与泡利不相容原理，是量子统计的核心结果。"))
 )},
{"id":"sm6s1-2","name":"最概然法推导量子分布","tags":["der","note"],"brief":"由微观状态数极大导出玻色/费米分布。",
 "body": wrap(
   defn("最概然法",p("在玻色/费米微观状态数表达式基础上，由 $\\ln\\Omega$ 极大（约束 $\\sum n_i=N,\\sum n_i\\varepsilon_i=E$）求出最概然分布 $\\{n_i\\}$。"))+
   der(p("<strong>玻色分布推导：</strong>玻色微观状态数 $\\Omega=\\prod_i (n_i+g_i-1)!/[n_i!(g_i-1)!]$。取对数并用斯特林近似：")+
   fml("\\ln\\Omega = \\sum_i\\big[(n_i+g_i-1)\\ln(n_i+g_i-1)-n_i\\ln n_i-(g_i-1)\\ln(g_i-1)\\big]")+
   p("对 $n_i$ 求变分，引入拉格朗日乘子 $\\alpha,\\beta$，令 $\\delta\\ln\\Omega-\\alpha\\delta N-\\beta\\delta E=0$：")+
   fml("\\ln\\frac{n_i+g_i-1}{n_i} - \\alpha - \\beta\\varepsilon_i = 0")+
   p("当 $g_i\\gg 1$ 时，$n_i+g_i-1\\approx n_i+g_i$，解得：")+
   fml("n_i = \\frac{g_i}{e^{\\alpha+\\beta\\varepsilon_i}-1} = \\frac{g_i}{e^{\\beta(\\varepsilon_i-\\mu)}-1}")+
   p("费米分布由 $\\Omega=\\prod g_i!/[n_i!(g_i-n_i)!]$ 同理导出，分母为 $+1$。"))+
   note(p("最概然法与巨正则系综方法给出相同结果，但巨正则法更简洁且自动处理了粒子数涨落。"))
 )},
{"id":"sm6s1-3","name":"经典极限与简并条件","tags":["der","app"],"brief":"高温低密度下量子统计退化为经典统计。",
 "body": wrap(
   defn("简并条件",p("当 $e^{\\alpha}=e^{-\\beta\\mu}\\gg 1$（即粒子数密度低、温度高）时，$e^{\\beta(\\varepsilon_i-\\mu)}\\gg 1$，玻色与费米分布都退化为玻尔兹曼分布。此条件称为<strong>非简并条件</strong>。"))+
   der(p("<strong>定量判据推导：</strong>对理想气体，热德布罗意波长 $\\lambda_T=h/\\sqrt{2\\pi m k_B T}$。数密度 $n=N/V$。非简并条件等价于：")+
   fml("n\\lambda_T^3 \\ll 1")+
   p("即粒子间平均距离远大于热德布罗意波长，粒子波包不重叠，量子效应可忽略。对标准状态下的氦气，$n\\lambda_T^3\\sim 10^{-5}$，经典近似极好；对液氦（$n\\lambda_T^3\\sim 1$）或金属电子气，必须用量子统计。"))+
   app(p("<strong>应用：</strong>常温常压气体满足非简并条件，可用玻尔兹曼统计；低温高密度系统（如液氦、白矮星、金属电子）必须用玻色或费米统计。"))
 )},
]},
{
"name": "6.2 光子气体与黑体辐射",
"color": "#4f46e5",
"desc": "普朗克公式、斯特藩定律与维恩位移律",
"items": [
{"id":"sm6s2-1","name":"光子气体与普朗克公式","tags":["thm","der"],"brief":"黑体辐射的频谱分布。",
 "fig":"planck","figCap":"黑体辐射谱随温度的变化",
 "body": wrap(
   thm("普朗克公式",p("黑体辐射场在频率 $\\nu$ 附近单位体积的能量密度为：")+
   fml("u(\\nu,T) = \\frac{8\\pi h\\nu^3}{c^3}\\frac{1}{e^{h\\nu/k_B T}-1}"))+
   der(p("<strong>由玻色分布推导：</strong>光子是玻色子，化学势 $\\mu=0$（光子数不守恒）。由玻色分布，频率 $\\nu$（能量 $h\\nu$）的平均光子数为 $1/(e^{h\\nu/k_B T}-1)$。单位体积内频率 $\\nu\\sim\\nu+d\\nu$ 的模式数（考虑两个偏振）：")+
   fml("g(\\nu)d\\nu = \\frac{8\\pi\\nu^2}{c^3}d\\nu")+
   p("能量密度为模式数乘以每个模式平均能量 $h\\nu/(e^{h\\nu/k_B T}-1)$：")+
   fml("u(\\nu,T)d\\nu = \\frac{8\\pi h\\nu^3}{c^3}\\frac{1}{e^{h\\nu/k_B T}-1}d\\nu")+
   p("即普朗克公式，成功解释了黑体辐射的全谱分布。"))+
   note(p("普朗克引入能量量子化假设 $E=nh\\nu$，是量子论的开端，标志着物理学新纪元。"))
 )},
{"id":"sm6s2-2","name":"斯特藩-玻尔兹曼定律","tags":["der","app"],"brief":"黑体总辐射能量正比于 T⁴。",
 "body": wrap(
   thm("斯特藩-玻尔兹曼定律",p("黑体单位表面积辐射功率（辐出度）与温度四次方成正比：")+
   fml("M = \\sigma T^4,\\quad \\sigma = \\frac{2\\pi^5 k_B^4}{15 c^2 h^3} \\approx 5.67\\times 10^{-8}\\,\\text{W/(m}^2\\text{K}^4\\text{)}"))+
   der(p("<strong>由普朗克公式积分推导：</strong>总能量密度 $u=\\int_0^\\infty u(\\nu,T)d\\nu$。令 $x=h\\nu/(k_B T)$：")+
   fml("u = \\frac{8\\pi h}{c^3}\\left(\\frac{k_B T}{h}\\right)^4\\int_0^\\infty \\frac{x^3}{e^x-1}dx = \\frac{8\\pi^5 k_B^4}{15 c^3 h^3}T^4 = aT^4")+
   p("其中 $\\int_0^\\infty x^3/(e^x-1)dx=\\pi^4/15$。辐出度 $M=uc/4=\\sigma T^4$。"))+
   app(p("<strong>应用：</strong>斯特藩定律用于测量恒星表面温度、红外测温、热像仪；宇宙微波背景辐射（$T\\approx 2.73\\,\\text{K}$）是大爆炸的遗迹。"))
 )},
{"id":"sm6s2-3","name":"维恩位移律与辐射高温计","tags":["der","app"],"brief":"辐射峰值波长与温度成反比。",
 "body": wrap(
   thm("维恩位移律",p("黑体辐射光谱的峰值波长 $\\lambda_{\\max}$ 与温度成反比：")+
   fml("\\lambda_{\\max} T = b,\\quad b\\approx 2.898\\times 10^{-3}\\,\\text{m·K}"))+
   der(p("<strong>由普朗克公式取极值推导：</strong>用波长表示的普朗克公式 $u(\\lambda,T)\\propto \\lambda^{-5}/(e^{hc/\\lambda k_B T}-1)$。令 $x=hc/(\\lambda k_B T)$，由 $du/d\\lambda=0$ 得超越方程：")+
   fml("5(1-e^{-x}) = x")+
   p("数值解 $x\\approx 4.965$，故 $hc/(\\lambda_{\\max} k_B T)=4.965$，即 $\\lambda_{\\max}T=hc/(4.965 k_B)=b$。温度越高，峰值波长越短（由红到蓝白）。"))+
   app(p("<strong>应用：</strong>通过测量恒星光谱峰值波长估算表面温度：太阳 $\\lambda_{\\max}\\approx 500\\,\\text{nm}$，$T\\approx 5800\\,\\text{K}$；温度也可由颜色判断，「红热」温度低于「白热」。"))
 )},
]},
{
"name": "6.3 金属中的自由电子气",
"color": "#4f46e5",
"desc": "费米-狄拉克统计对金属电子的应用",
"items": [
{"id":"sm6s3-1","name":"自由电子气与费米能量","tags":["def","der"],"brief":"T=0 时电子填满费米球。",
 "fig":"fermi","figCap":"费米分布与费米能级",
 "body": wrap(
   defn("费米能量",p("绝对零度下，电子按泡利原理从最低能级开始填充，最高占据能级称为<strong>费米能量</strong> $\\varepsilon_F$。动量空间中被填充区域为费米球，半径为费米波矢 $k_F$。"))+
   der(p("<strong>由电子数密度推导：</strong>$T=0$ 时费米分布为阶跃函数，$\\varepsilon<\\varepsilon_F$ 占据数为 1，否则为 0。单位体积能量小于 $\\varepsilon_F$ 的态数（考虑自旋简并 2）：")+
   fml("n = \\int_0^{\\varepsilon_F} g(\\varepsilon)d\\varepsilon = 2\\cdot\\frac{V}{h^3}\\cdot\\frac{4}{3}\\pi p_F^3 / V = \\frac{8\\pi}{3h^3}p_F^3")+
   p("由 $p_F=\\hbar k_F$、$\\varepsilon_F=p_F^2/(2m)$，解得：")+
   fml("k_F = (3\\pi^2 n)^{1/3},\\quad \\varepsilon_F = \\frac{\\hbar^2}{2m}(3\\pi^2 n)^{2/3}")+
   p("对典型金属 $n\\sim 10^{29}\\,\\text{m}^{-3}$，$\\varepsilon_F\\sim 5\\,\\text{eV}$，费米温度 $T_F=\\varepsilon_F/k_B\\sim 6\\times 10^4\\,\\text{K}$。"))+
   note(p("即使在室温下，金属中绝大多数电子仍处于 $\\varepsilon<\\varepsilon_F$ 的态，只有费米面附近 $k_B T$ 范围的电子可参与热激发与导电。"))
 )},
{"id":"sm6s3-2","name":"电子气的低温热容","tags":["der","thm"],"brief":"自由电子对热容的线性贡献。",
 "body": wrap(
   thm("电子热容",p("低温下金属自由电子对摩尔热容的贡献为：")+
   fml("C_{V,e} = \\frac{\\pi^2}{2}R\\frac{T}{T_F} = \\gamma T"))+
   der(p("<strong>由费米分布推导：</strong>只有费米面附近 $\\Delta\\varepsilon\\sim k_B T$ 范围的电子可被热激发。被激发电子数占比约 $k_B T/\\varepsilon_F=T/T_F$，每个电子平均能量增加约 $k_B T$，故内能增量：")+
   fml("\\Delta U \\approx N\\frac{T}{T_F}\\cdot k_B T = Nk_B\\frac{T^2}{T_F}")+
   fml("C_{V,e} = \\frac{\\partial U}{\\partial T} \\approx 2Nk_B\\frac{T}{T_F}")+
   p("精确计算给出系数 $\\pi^2/2$。电子热容 $\\propto T$，与晶格热容 $\\propto T^3$（德拜）不同。低温下电子热容主导，高温下晶格热容主导。"))+
   app(p("<strong>应用：</strong>金属低温热容 $C_V=\\gamma T+\\beta T^3$，通过测量可分别确定电子与晶格贡献，验证自由电子气模型。"))
 )},
{"id":"sm6s3-3","name":"泡利顺磁性","tags":["der","app"],"brief":"费米统计导致的弱温度无关顺磁性。",
 "body": wrap(
   thm("泡利顺磁磁化率",p("金属自由电子气的顺磁磁化率近似为常数（与温度无关）：")+
   fml("\\chi = \\mu_0\\mu_B^2 g(\\varepsilon_F)"))+
   der(p("<strong>由自旋分裂推导：</strong>外场 $B$ 使自旋向上/向下电子能级分别移动 $-\\mu_B B$ 和 $+\\mu_B B$。平衡时两者费米能级对齐，自旋向上比向下多 $\\Delta N$：")+
   fml("\\Delta N \\approx \\frac{1}{2}g(\\varepsilon_F)\\cdot 2\\mu_B B = g(\\varepsilon_F)\\mu_B B")+
   p("磁化强度 $M=\\mu_B\\Delta N/V=\\mu_0\\mu_B^2 g(\\varepsilon_F)H$，故 $\\chi=\\mu_0\\mu_B^2 g(\\varepsilon_F)$。由于只有费米面附近电子翻转，磁化率不随温度变化（与经典居里定律 $\\propto 1/T$ 不同）。"))+
   note(p("泡利顺磁性是量子简并效应，是金属电子气的重要特征，解释了碱金属等顺磁金属磁化率几乎不随温度变化的实验事实。"))
 )},
]},
{
"name": "6.4 玻色-爱因斯坦凝聚",
"color": "#4f46e5",
"desc": "玻色子在低温下宏观占据基态的相变",
"items": [
{"id":"sm6s4-1","name":"玻色-爱因斯坦凝聚条件","tags":["thm","der"],"brief":"温度低于 Tc 时宏观粒子数占据基态。",
 "fig":"bec","figCap":"玻色-爱因斯坦凝聚中基态占据数随温度变化",
 "body": wrap(
   thm("BEC 临界温度",p("理想玻色气体发生玻色-爱因斯坦凝聚的临界温度为：")+
   fml("T_c = \\frac{2\\pi\\hbar^2}{m k_B}\\left(\\frac{n}{\\zeta(3/2)}\\right)^{2/3},\\quad \\zeta(3/2)\\approx 2.612"))+
   der(p("<strong>由玻色分布积分推导：</strong>温度 $T$ 时，激发态（$\\varepsilon>0$）上的粒子数密度：")+
   fml("n_{\\text{exc}} = \\frac{1}{V}\\sum_{\\varepsilon>0}\\frac{1}{e^{\\beta(\\varepsilon-\\mu)}-1}")+
   p("化学势 $\\mu\\leq 0$（玻色分布分母必须为正）。当 $\\mu\\to 0^-$ 时激发态粒子数达到极大值。化为积分：")+
   fml("n_{\\text{exc,max}} = \\frac{1}{2\\pi^2}\\left(\\frac{2m}{\\hbar^2}\\right)^{3/2}\\int_0^\\infty\\frac{\\sqrt{\\varepsilon}\\,d\\varepsilon}{e^{\\varepsilon/k_B T}-1} = \\frac{(2\\pi m k_B T)^{3/2}}{h^3}\\zeta(3/2)")+
   p("令 $n_{\\text{exc,max}}=n$，解得 $T_c$。当 $T<T_c$ 时，$n_{\\text{exc}}<n$，多余粒子 $N_0=n-n_{\\text{exc}}$ 全部进入 $\\varepsilon=0$ 基态，形成凝聚。"))+
   note(p("BEC 是量子统计的宏观量子现象，1995 年在铷原子气体中实验实现，开启了冷原子物理研究。"))
 )},
{"id":"sm6s4-2","name":"凝聚分数与热力学性质","tags":["der","app"],"brief":"基态粒子数比例与低温热容行为。",
 "body": wrap(
   defn("凝聚分数",p("温度 $T<T_c$ 时，处于基态的粒子数比例为：")+
   fml("\\frac{N_0}{N} = 1-\\left(\\frac{T}{T_c}\\right)^{3/2}"))+
   der(p("<strong>推导：</strong>$T<T_c$ 时 $\\mu\\approx 0$，激发态粒子数 $N_{\\text{exc}}=N(T/T_c)^{3/2}$，故基态占据数：")+
   fml("N_0 = N - N_{\\text{exc}} = N\\left[1-\\left(\\frac{T}{T_c}\\right)^{3/2}\\right]")+
   p("内能由激发态粒子贡献，$U\\propto\\int_0^\\infty \\varepsilon^{3/2}/(e^{\\varepsilon/k_B T}-1)d\\varepsilon \\propto T^{5/2}$。热容 $C_V\\propto T^{3/2}$，在 $T_c$ 处有一个尖峰（$\\lambda$ 相变）。"))+
   app(p("<strong>应用：</strong>液氦 He-4 在 $2.17\\,\\text{K}$ 发生 $\\lambda$ 相变进入超流态，与 BEC 有关（但液氦有强相互作用，不是理想玻色气体）。超流的无摩擦流动是宏观量子效应。"))
 )},
{"id":"sm6s4-3","name":"光子气体与玻色统计的特殊性","tags":["note","der"],"brief":"光子数不守恒使化学势为零。",
 "body": wrap(
   defn("光子的特殊性",p("光子是玻色子，但光子数不守恒（可被发射和吸收），故无 $\\sum n_i=N$ 约束，拉格朗日乘子 $\\alpha=0$，化学势 $\\mu=-\\alpha/\\beta=0$。"))+
   der(p("<strong>由巨正则系综推导：</strong>对光子气体，总粒子数可变，平衡条件 $\\partial S/\\partial N=0$，而 $\\mu=-T(\\partial S/\\partial N)_{E,V}=0$。故玻色分布中 $\\mu=0$：")+
   fml("\\bar{n}_\\nu = \\frac{1}{e^{h\\nu/k_B T}-1}")+
   p("这就是普朗克分布。声子（晶格振动量子）同样粒子数不守恒，$\\mu=0$，其平均占据数也用玻色分布（$\\mu=0$）描述，由此可得德拜热容定律。"))+
   note(p("化学势为零是粒子数不守恒系统的普遍特征：光子、声子、磁振子等准粒子均满足 $\\mu=0$。"))
 )},
]},
{
"name": "6.5 顺磁性与泡利顺磁性",
"color": "#4f46e5",
"desc": "朗之万顺磁性、居里定律与泡利顺磁性",
"items": [
{"id":"sm6s5-1","name":"朗之万顺磁理论","tags":["thm","der"],"brief":"经典顺磁体的磁化强度与居里定律。",
 "fig":"paramagnet","figCap":"朗之万顺磁磁化曲线",
 "body": wrap(
   thm("居里定律",p("经典顺磁体的磁化率与温度成反比：")+
   fml("\\chi = \\frac{C}{T},\\quad C = \\frac{n\\mu_0\\mu^2}{3k_B}"))+
   der(p("<strong>由玻尔兹曼分布推导：</strong>磁矩 $\\mu$ 在磁场 $B$ 中势能 $-\\mu B\\cos\\theta$。由玻尔兹曼分布，平均磁矩沿场分量：")+
   fml("\\langle\\mu_z\\rangle = \\mu\\frac{\\int \\cos\\theta\\, e^{\\mu B\\cos\\theta/k_B T}d\\Omega}{\\int e^{\\mu B\\cos\\theta/k_B T}d\\Omega} = \\mu L\\left(\\frac{\\mu B}{k_B T}\\right)")+
   p("其中 $L(x)=\\coth x-1/x$ 为朗之万函数。弱场高温极限 $x=\\mu B/(k_B T)\\ll 1$ 时 $L(x)\\approx x/3$：")+
   fml("M = n\\langle\\mu_z\\rangle \\approx n\\mu\\cdot\\frac{\\mu B}{3k_B T} = \\frac{n\\mu^2 B}{3k_B T}")+
   fml("\\chi = \\frac{M}{H} = \\frac{\\mu_0 M}{B} = \\frac{n\\mu_0\\mu^2}{3k_B T} = \\frac{C}{T}")+
   p("即居里定律。强场下 $L(x)\\to 1$，磁化达到饱和 $M\\to n\\mu$。"))+
   app(p("<strong>应用：</strong>居里定律描述了氧气、稀土盐等顺磁物质的磁化率，绝热去磁制冷正是利用顺磁盐磁化熵随温度变化的特性。"))
 )},
{"id":"sm6s5-2","name":"顺磁盐的绝热去磁制冷","tags":["der","app"],"brief":"利用磁熵变获得极低温。",
 "body": wrap(
   defn("绝热去磁制冷",p("先等温磁化使顺磁盐磁矩有序排列（熵减小），再绝热去磁使磁矩无序化，熵不变但温度下降，达到 $10^{-3}\\,\\text{K}$ 量级低温。"))+
   der(p("<strong>由磁熵推导：</strong>顺磁系统的熵分为晶格熵 $S_L$ 与磁熵 $S_M$。等温磁化时外场使磁矩排列有序，磁熵减小 $S_M(M)>S_M(0)$。绝热去磁时总熵不变，磁熵增加由晶格熵减小补偿，温度降低：")+
   fml("S_{\\text{total}}(B,T_1) = S_{\\text{total}}(0,T_2)")+
   fml("S_L(T_1)+S_M(B,T_1) = S_L(T_2)+S_M(0,T_2)")+
   p("在低温下 $S_L\\ll S_M$，近似 $S_M(B,T_1)=S_M(0,T_2)$。由居里定律可估算降温幅度，理论上可趋近绝对零度，但受第三定律限制。"))+
   app(p("<strong>应用：</strong>绝热去磁制冷是实现 mK 级低温的标准方法，广泛用于凝聚态物理、量子计算与精密测量。"))
 )},
{"id":"sm6s5-3","name":"泡利顺磁性与朗之万的差异","tags":["der","note"],"brief":"量子简并电子气的磁化率不随温度变化。",
 "body": wrap(
   defn("泡利顺磁性",p("金属中自由电子气服从费米统计，只有费米面附近电子可翻转自旋，导致磁化率几乎与温度无关，与经典居里定律形成鲜明对比。"))+
   der(p("<strong>对比推导：</strong>经典朗之万理论中所有磁矩都可沿场取向，磁化率 $\\chi\\propto 1/T$。费米统计下，泡利原理限制每个态最多两个电子，$T=0$ 时 $\\varepsilon<\\varepsilon_F$ 全满。外场使自旋向上/向下能带相对移动 $2\\mu_B B$，只有费米面附近 $\\Delta\\varepsilon\\sim\\mu_B B$ 范围的电子翻转：")+
   fml("\\Delta N \\approx \\frac{1}{2}g(\\varepsilon_F)\\cdot 2\\mu_B B,\\quad \\chi = \\mu_0\\mu_B^2 g(\\varepsilon_F)")+
   p("由于 $g(\\varepsilon_F)\\propto n/\\varepsilon_F\\propto n^{2/3}$，泡利磁化率与温度几乎无关。温度修正为 $(T/T_F)^2$ 量级，极弱。"))+
   note(p("泡利顺磁性是金属量子简并性的直接证据，经典统计无法解释金属磁化率的温度无关性。"))
 )},
]},
]

ch7_sections = [
{
"name": "7.1 涨落的基本公式",
"color": "#be185d",
"desc": "热力学量涨落的爱因斯坦公式与基本涨落",
"items": [
{"id":"sm7s1-1","name":"涨落的爱因斯坦公式","tags":["thm","der"],"brief":"由熵偏离平衡的概率给出涨落。",
 "fig":"fluctuation","figCap":"热力学量围绕平均值的涨落",
 "body": wrap(
   thm("爱因斯坦涨落公式",p("系统某热力学量偏离平衡值 $x_0$ 到 $x$ 的概率正比于熵变的指数：")+
   fml("W \\propto e^{\\Delta S/k_B},\\quad \\Delta S = S(x)-S(x_0)"))+
   der(p("<strong>由玻尔兹曼关系推导：</strong>系统熵取 $S$ 时的微观状态数 $\\Omega=e^{S/k_B}$。平衡态熵 $S_0$ 对应最大微观状态数 $\\Omega_0$。偏离平衡的概率：")+
   fml("W = \\frac{\\Omega}{\\Omega_0} = e^{(S-S_0)/k_B} = e^{\\Delta S/k_B}")+
   p("在平衡态附近把熵展开到二阶，设 $x=x_0+\\Delta x$：")+
   fml("\\Delta S = \\frac{1}{2}\\left(\\frac{\\partial^2 S}{\\partial x^2}\\right)_0 (\\Delta x)^2")+
   p("由稳定平衡条件 $(\\partial^2 S/\\partial x^2)_0<0$，故概率为高斯分布：")+
   fml("W(\\Delta x) \\propto e^{-(\\Delta x)^2/(2\\langle(\\Delta x)^2\\rangle)},\\quad \\langle(\\Delta x)^2\\rangle = -\\frac{k_B}{(\\partial^2 S/\\partial x^2)_0}"))+
   note(p("爱因斯坦公式是涨落理论的基础，它把涨落与熵的二阶导数（即稳定性条件）联系起来。"))
 )},
{"id":"sm7s1-2","name":"体积与压强涨落","tags":["der","app"],"brief":"等温下体积涨落与等温压缩系数。",
 "body": wrap(
   defn("体积涨落",p("在等温等压约束下，系统体积围绕平均值涨落。其均方涨落与等温压缩系数成正比。"))+
   der(p("<strong>由爱因斯坦公式推导：</strong>选 $T,V$ 为独立变量，熵展开到二阶。体积涨落相关项：")+
   fml("\\Delta S \\approx \\frac{1}{2}\\left(\\frac{\\partial^2 S}{\\partial V^2}\\right)_T (\\Delta V)^2")+
   p("由麦克斯韦关系 $(\\partial S/\\partial V)_T=(\\partial P/\\partial T)_V$，再求导：")+
   fml("\\left(\\frac{\\partial^2 S}{\\partial V^2}\\right)_T = \\left(\\frac{\\partial^2 P}{\\partial T\\partial V}\\right) = -\\frac{1}{V\\kappa_T T}")+
   fml("\\implies \\langle(\\Delta V)^2\\rangle = -\\frac{k_B}{\\partial^2 S/\\partial V^2} = k_B T V\\kappa_T")+
   p("相对涨落 $\\sqrt{\\langle(\\Delta V)^2\\rangle}/V\\propto 1/\\sqrt{N}$，宏观可忽略；临界点附近 $\\kappa_T\\to\\infty$，体积涨落发散。"))+
   app(p("<strong>应用：</strong>体积涨落导致密度涨落，是光散射（临界乳光）和超声波吸收的微观原因。"))
 )},
{"id":"sm7s1-3","name":"熵与温度涨落","tags":["der","note"],"brief":"熵涨落与温度涨落的关系。",
 "body": wrap(
   defn("温度涨落",p("系统温度围绕平均值的涨落，由热容决定。在能量固定（微正则）的系统中，温度涨落与等容热容成反比。"))+
   der(p("<strong>由能量涨落反推：</strong>正则系综能量涨落 $\\langle(\\Delta E)^2\\rangle=k_B T^2 C_V$。在微正则系综（$E$ 固定）中，能量涨落为零，但温度本身涨落。由 $dE=C_V dT$ 形式对应：")+
   fml("\\langle(\\Delta T)^2\\rangle = \\frac{k_B T^2}{C_V}")+
   p("熵涨落可由 $dS=C_V dT/T+(\\partial P/\\partial T)_V dV$ 在等容下得 $\\Delta S=C_V\\Delta T/T$，故：")+
   fml("\\langle(\\Delta S)^2\\rangle = \\frac{C_V^2}{T^2}\\langle(\\Delta T)^2\\rangle = k_B C_V")+
   p("这些结果表明热容越大，温度涨落越小，系统温度越稳定。"))+
   note(p("涨落的存在意味着热力学量的「确定值」只是统计平均，微观上始终有偏离，只是宏观相对涨落极小。"))
 )},
]},
{
"name": "7.2 能量与温度涨落",
"color": "#be185d",
"desc": "正则系综能量涨落与微正则温度涨落",
"items": [
{"id":"sm7s2-1","name":"正则系综能量涨落","tags":["der","thm"],"brief":"能量涨落正比于热容。",
 "body": wrap(
   thm("能量涨落公式",p("正则系综中能量的均方涨落为：")+
   fml("\\langle(\\Delta E)^2\\rangle = \\langle E^2\\rangle-\\langle E\\rangle^2 = k_B T^2 C_V"))+
   der(p("<strong>由配分函数推导：</strong>$\\langle E\\rangle=-\\partial\\ln Z/\\partial\\beta$，$\\langle E^2\\rangle=\\partial^2\\ln Z/\\partial\\beta^2$。故：")+
   fml("\\langle E^2\\rangle-\\langle E\\rangle^2 = \\frac{\\partial^2\\ln Z}{\\partial\\beta^2} - \\left(\\frac{\\partial\\ln Z}{\\partial\\beta}\\right)^2 = -\\frac{\\partial\\langle E\\rangle}{\\partial\\beta}")+
   p("利用 $\\partial/\\partial\\beta=-k_B T^2\\partial/\\partial T$：")+
   fml("-\\frac{\\partial\\langle E\\rangle}{\\partial\\beta} = k_B T^2\\frac{\\partial\\langle E\\rangle}{\\partial T} = k_B T^2 C_V")+
   p("能量涨落的根源是系统与热源的能量交换，热容越大，系统储能能力越强，涨落越大；但相对涨落 $\\propto 1/\\sqrt{N}\\to 0$。"))+
   note(p("该公式是涨落-耗散定理的原型：响应函数（热容）决定了相应量的涨落。"))
 )},
{"id":"sm7s2-2","name":"微正则系综温度涨落","tags":["der","note"],"brief":"孤立系统的温度涨落由热容决定。",
 "body": wrap(
   defn("微正则温度涨落",p("在微正则系综中能量固定，温度是由熵对能量的导数 $1/T=(\\partial S/\\partial E)_V$ 定义的统计量，围绕平均值涨落。"))+
   der(p("<strong>由 $1/T=(\\partial S/\\partial E)_V$ 推导：</strong>在 $E_0$ 附近展开 $1/T(E)$：")+
   fml("\\frac{1}{T} \\approx \\frac{1}{T_0} + \\left(\\frac{\\partial(1/T)}{\\partial E}\\right)_V (E-E_0)")+
   p("而微正则系综中能量严格固定 $E=E_0$，温度涨落来自对熵曲率的统计。等价地，由正则能量涨落通过系综变换，可证明温度涨落：")+
   fml("\\langle(\\Delta T)^2\\rangle = \\frac{k_B T^2}{C_V}")+
   p("该式表明热容越大，温度涨落越小。对无限大热容（如恒温热源），温度涨落为零，这与热源定义自洽。"))+
   note(p("微正则温度涨落与正则能量涨落通过涨落-耗散定理相联系，反映了不同系综下涨落的对偶性。"))
 )},
{"id":"sm7s2-3","name":"粒子数涨落与等温压缩系数","tags":["der","app"],"brief":"巨正则系综粒子数涨落公式。",
 "body": wrap(
   thm("粒子数涨落公式",p("巨正则系综中粒子数的均方涨落为：")+
   fml("\\langle(\\Delta N)^2\\rangle = k_B T\\left(\\frac{\\partial \\langle N\\rangle}{\\partial \\mu}\\right)_{T,V} = \\frac{k_B T N}{V}\\kappa_T"))+
   der(p("<strong>由巨配分函数推导：</strong>$\\langle N\\rangle=(1/\\beta)\\partial\\ln\\Xi/\\partial\\mu$，$\\langle N^2\\rangle=(1/\\beta^2)\\partial^2\\ln\\Xi/\\partial\\mu^2$。故：")+
   fml("\\langle N^2\\rangle-\\langle N\\rangle^2 = \\frac{1}{\\beta^2}\\frac{\\partial^2\\ln\\Xi}{\\partial\\mu^2} = \\frac{1}{\\beta}\\frac{\\partial\\langle N\\rangle}{\\partial\\mu}")+
   p("利用热力学恒等式 $(\\partial N/\\partial\\mu)_{T,V}=N\\kappa_T/V$（由 $d\\mu=-s\\,dT+v\\,dP$ 等温下 $d\\mu=v\\,dP$，再结合 $\\kappa_T$ 定义），得：")+
   fml("\\langle(\\Delta N)^2\\rangle = \\frac{k_B T N}{V}\\kappa_T")+
   p("临界点附近 $\\kappa_T\\to\\infty$，粒子数涨落发散，导致密度涨落巨大。"))+
   app(p("<strong>应用：</strong>粒子数涨落引起的密度涨落是光散射的来源，临界点附近涨落发散导致临界乳光（气体变浑浊）。"))
 )},
]},
{
"name": "7.3 布朗运动",
"color": "#be185d",
"desc": "朗之万方程、爱因斯坦关系与斯托克斯-爱因斯坦公式",
"items": [
{"id":"sm7s3-1","name":"布朗运动与朗之万方程","tags":["def","der"],"brief":"布朗粒子运动的随机微分方程。",
 "fig":"brownian","figCap":"布朗粒子的随机游走轨迹",
 "body": wrap(
   defn("布朗运动",p("悬浮在液体中的微小颗粒由于受到周围液体分子的随机碰撞，而做的无规则运动，称为布朗运动。它是分子热运动的直接证据。"))+
   der(p("<strong>朗之万方程推导：</strong>布朗粒子受两种力：粘滞阻力 $-\\gamma v$（与速度成正比）和随机涨落力 $F(t)$（由分子碰撞产生）。牛顿第二定律给出：")+
   fml("m\\frac{dv}{dt} = -\\gamma v + F(t)")+
   p("涨落力满足 $\\langle F(t)\\rangle=0$，且不同时刻不相关 $\\langle F(t)F(t')\\rangle=2\\gamma k_B T\\delta(t-t')$。在过阻尼极限（$m$ 小或 $\\gamma$ 大）下忽略惯性项 $m\\,dv/dt$，解为 $v(t)=F(t)/\\gamma$。位移 $x(t)=\\int_0^t v(t')dt'$：")+
   fml("\\langle x^2(t)\\rangle = \\frac{1}{\\gamma^2}\\int_0^t\\int_0^t \\langle F(t_1)F(t_2)\\rangle dt_1 dt_2 = \\frac{2k_B T}{\\gamma}t = 2Dt")+
   p("其中 $D=k_B T/\\gamma$ 为扩散系数。"))+
   note(p("朗之万方程是处理非平衡随机过程的基础，把确定性阻尼与随机涨落统一描述，是涨落耗散定理的具体化。"))
 )},
{"id":"sm7s3-2","name":"爱因斯坦关系与扩散","tags":["thm","der"],"brief":"扩散系数与迁移率的关系。",
 "body": wrap(
   thm("爱因斯坦关系",p("布朗粒子的扩散系数 $D$ 与迁移率 $\\mu$ 满足：")+
   fml("D = \\mu k_B T,\\quad \\mu = \\frac{v_d}{F} = \\frac{1}{\\gamma}"))+
   der(p("<strong>由涨落耗散推导：</strong>在外力 $F$ 下，粒子达到稳态漂移速度 $v_d=F/\\gamma=F\\mu$。由朗之万方程，无外力时位移均方值 $\\langle x^2\\rangle=2Dt=2k_B T t/\\gamma$。另一方面，在外力作用下粒子做漂移叠加扩散运动，达到平衡时粒子流 $J=0$：")+
   fml("J = n\\mu F - D\\frac{dn}{dx} = 0")+
   p("平衡时玻尔兹曼分布 $n(x)\\propto e^{-F x/k_B T}$，故 $dn/dx=-(F/k_B T)n$。代入得 $n\\mu F-Dn F/k_B T=0$，即 $D=\\mu k_B T$。"))+
   app(p("<strong>应用：</strong>爱因斯坦关系把涨落（扩散）与耗散（迁移率）联系起来，是涨落耗散定理的经典形式，广泛应用于电化学、半导体与软物质物理。"))
 )},
{"id":"sm7s3-3","name":"斯托克斯-爱因斯坦公式","tags":["der","app"],"brief":"球形粒子扩散系数与黏滞系数的关系。",
 "body": wrap(
   thm("斯托克斯-爱因斯坦公式",p("半径 $r$ 的球形粒子在黏滞系数 $\\eta$ 的流体中扩散，其扩散系数为："))+
   fml("D = \\frac{k_B T}{6\\pi\\eta r}")+
   der(p("<strong>由斯托克斯定律推导：</strong>低速运动的球形粒子受到的粘滞阻力由斯托克斯定律给出 $F=6\\pi\\eta r v$，故阻尼系数 $\\gamma=6\\pi\\eta r$，迁移率 $\\mu=1/\\gamma=1/(6\\pi\\eta r)$。代入爱因斯坦关系 $D=\\mu k_B T$：")+
   fml("D = \\frac{k_B T}{6\\pi\\eta r}")+
   p("此公式把宏观可测量（扩散系数、黏滞系数）与微观量（粒子半径、温度）联系起来。佩兰通过测量布朗运动位移求 $D$，再用此公式测定阿伏伽德罗常数 $N_A$，验证了分子的真实存在。"))+
   app(p("<strong>应用：</strong>斯托克斯-爱因斯坦公式用于由扩散系数估算大分子（如蛋白质、聚合物）的粒径；佩兰实验因此获得 1926 年诺贝尔物理学奖。"))
 )},
]},
{
"name": "7.4 涨落的相关性与临界乳光",
"color": "#be185d",
"desc": "空间关联函数、关联长度与临界乳光",
"items": [
{"id":"sm7s4-1","name":"空间涨落的关联函数","tags":["def","der"],"brief":"两点密度涨落的空间关联。",
 "body": wrap(
   defn("密度关联函数",p("描述空间中两点密度涨落相关性的函数："))+
   fml("G(\\mathbf{r}_1,\\mathbf{r}_2) = \\langle\\delta n(\\mathbf{r}_1)\\delta n(\\mathbf{r}_2)\\rangle")+
   p("其中 $\\delta n(\\mathbf{r})=n(\\mathbf{r})-\\langle n\\rangle$ 为局域密度涨落。均匀系统中 $G$ 仅依赖于相对距离 $r=|\\mathbf{r}_1-\\mathbf{r}_2|$。")+
   der(p("<strong>长波极限与压缩系数的关系：</strong>对关联函数作傅里叶变换得到结构因子 $S(\\mathbf{q})=\\int G(r)e^{-i\\mathbf{q}\\cdot\\mathbf{r}}d^3r$。在长波极限 $q\\to 0$ 下，结构因子正比于等温压缩系数：")+
   fml("S(0) = n k_B T \\kappa_T")+
   p("这是因为长波密度涨落对应系统整体体积涨落，而体积涨落 $\\langle(\\Delta V)^2\\rangle=k_B T V\\kappa_T$。"))+
   note(p("关联函数刻画了涨落的空间延伸范围，其衰减特征长度为关联长度 $\\xi$。"))
 )},
{"id":"sm7s4-2","name":"关联长度与临界发散","tags":["der","thm"],"brief":"临界点附近关联长度发散。",
 "body": wrap(
   thm("关联长度发散",p("在临界点附近，涨落的关联长度按幂律发散："))+
   fml("\\xi \\propto |T-T_c|^{-\\nu}")+
   p("其中 $\\nu$ 为关联长度临界指数。")+
   der(p("<strong>由奥恩斯坦-泽尔尼克理论推导：</strong>临界点附近，密度关联函数可近似为：")+
   fml("G(r) \\propto \\frac{e^{-r/\\xi}}{r}")+
   p("这是奥恩斯坦-泽尔尼克形式，其中 $\\xi$ 为关联长度。当 $T\\to T_c$ 时，压缩系数 $\\kappa_T\\propto|T-T_c|^{-\\gamma}$ 发散，由 $S(0)=n k_B T\\kappa_T$ 与 $S(0)\\propto\\xi^2$，得：")+
   fml("\\xi \\propto \\sqrt{S(0)} \\propto |T-T_c|^{-\\gamma/2}")+
   p("由标度律 $\\gamma=\\nu(2-\\eta)$，对平均场 $\\eta=0$ 得 $\\xi\\propto|T-T_c|^{-1/2}$，即 $\\nu=1/2$。关联长度发散意味着涨落从微观尺度延伸到宏观尺度。"))+
   note(p("关联长度发散是临界现象的核心特征：在临界点，涨落尺度与观察尺度无关，系统呈现尺度不变性，这是重整化群理论的出发点。"))
 )},
{"id":"sm7s4-3","name":"临界乳光","tags":["app","der"],"brief":"临界点附近光散射增强现象。",
 "body": wrap(
   defn("临界乳光",p("在气液临界点附近，流体因密度涨落巨大而对光产生强烈散射，使原本透明的流体呈现乳白色浑浊的现象，称为临界乳光。"))+
   der(p("<strong>由瑞利散射公式推导：</strong>光散射强度与密度涨落的均方值成正比。由涨落理论，相对密度涨落：")+
   fml("\\frac{\\langle(\\Delta n)^2\\rangle}{n^2} = \\frac{k_B T \\kappa_T}{V}")+
   p("瑞利散射截面 $\\sigma\\propto\\lambda^{-4}\\cdot n^2\\langle(\\Delta n)^2\\rangle$。临界点附近 $\\kappa_T\\to\\infty$，密度涨落发散，散射强度急剧增大，形成临界乳光。由于涨落尺度接近可见光波长，对所有波长散射都很强，故呈乳白色。")+
   fml("I_{\\text{sca}} \\propto \\kappa_T \\to \\infty\\quad(T\\to T_c)")+
   p("1869 年安德鲁斯首先在 $\\text{CO}_2$ 临界点观察到临界乳光。"))+
   app(p("<strong>应用：</strong>临界乳光可用于精确测定临界点参数；超临界流体萃取利用临界点附近密度可调、溶解能力强的特性，广泛用于食品、医药工业。"))+
   note(p("临界乳光是涨落理论最直观的实验验证：肉眼可见的宏观浑浊源于微观密度涨落的发散。"))
 )},
]},
]

CHAPTERS = [
    {"id":"sm-ch1","num":"第一章","title":"热力学基本定律","en":"LAWS OF THERMODYNAMICS",
     "desc":"热力学系统与状态参量、热力学第零定律与温度、热力学第一定律与内能、热力学第二定律与熵及熵增原理、热力学第三定律与绝对零度不可达到。",
     "sections": ch1_sections},
    {"id":"sm-ch2","num":"第二章","title":"热力学势与麦克斯韦关系","en":"THERMODYNAMIC POTENTIALS",
     "desc":"勒让德变换引入自由能与吉布斯函数、四个热力学基本方程、四个麦克斯韦关系及其应用、热容差与热力学量导数关系。",
     "sections": ch2_sections},
    {"id":"sm-ch3","num":"第三章","title":"相变与临界现象","en":"PHASE TRANSITIONS",
     "desc":"相平衡条件与克拉珀龙方程、一级与二级相变、范德瓦尔斯方程与麦克斯韦等面积法则、临界现象与临界指数、朗道相变理论。",
     "sections": ch3_sections},
    {"id":"sm-ch4","num":"第四章","title":"玻尔兹曼统计","en":"BOLTZMANN STATISTICS",
     "desc":"等概率原理与微观状态数、玻尔兹曼分布与配分函数、麦克斯韦速度分布律、能量均分定理、理想气体热力学函数。",
     "sections": ch4_sections},
    {"id":"sm-ch5","num":"第五章","title":"系综理论","en":"ENSEMBLE THEORY",
     "desc":"微正则系综、正则系综与配分函数、巨正则系综与巨配分函数、系综等价性与热力学极限、实际气体位力展开。",
     "sections": ch5_sections},
    {"id":"sm-ch6","num":"第六章","title":"量子统计","en":"QUANTUM STATISTICS",
     "desc":"玻色分布与费米分布、光子气体与普朗克黑体辐射、金属自由电子气与费米能级、玻色-爱因斯坦凝聚、顺磁性与泡利顺磁性。",
     "sections": ch6_sections},
    {"id":"sm-ch7","num":"第七章","title":"涨落理论","en":"FLUCTUATIONS",
     "desc":"涨落的爱因斯坦公式、能量与温度涨落、布朗运动与朗之万方程及斯托克斯-爱因斯坦公式、涨落相关性与临界乳光。",
     "sections": ch7_sections},
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
  body{margin:0;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;color:var(--la-ink);background:radial-gradient(circle at 10% 10%,rgba(220,38,38,.08),transparent 28%),radial-gradient(circle at 90% 10%,rgba(79,70,229,.08),transparent 28%),var(--la-bg);line-height:1.7}
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
  .la-nav-tab.c1{color:#dc2626;border-color:#fecaca}
  .la-nav-tab.c2{color:#ea580c;border-color:#fed7aa}
  .la-nav-tab.c3{color:#d97706;border-color:#fde68a}
  .la-nav-tab.c4{color:#0d9488;border-color:#99f6e4}
  .la-nav-tab.c5{color:#0891b2;border-color:#a5f3fc}
  .la-nav-tab.c6{color:#4f46e5;border-color:#c7d2fe}
  .la-nav-tab.c7{color:#be185d;border-color:#fbcfe8}
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
  .la-phase-title.sm-ch1::before{background:#dc2626}
  .la-phase-title.sm-ch2::before{background:#ea580c}
  .la-phase-title.sm-ch3::before{background:#d97706}
  .la-phase-title.sm-ch4::before{background:#0d9488}
  .la-phase-title.sm-ch5::before{background:#0891b2}
  .la-phase-title.sm-ch6::before{background:#4f46e5}
  .la-phase-title.sm-ch7::before{background:#be185d}
  .la-phase-en{font-size:11px;letter-spacing:.36em;color:#94a3b8;font-weight:700;text-transform:uppercase;margin:0 0 12px 18px;font-style:italic}
  .la-phase-desc{color:var(--la-muted);font-size:14px;margin:0 0 24px 18px;line-height:1.8;max-width:960px}
  .la-domain{margin-bottom:26px;padding:16px 18px 18px 22px;position:relative;background:rgba(255,255,255,.6);border-radius:18px;border:1px solid #e5ebf2}
  .la-domain::before{content:"";position:absolute;left:6px;top:16px;bottom:16px;width:5px;border-radius:5px;background:var(--domain-color,#dc2626);box-shadow:0 0 12px rgba(220,38,38,.25)}
  .la-domain-header{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:12px}
  .la-domain-header h3{margin:0;font-size:17px;color:#1e293b}
  .la-domain-count{font-size:11px;padding:2px 10px;border-radius:999px;background:#eef2ff;color:#4f46e5;font-weight:700}
  .la-domain-desc{font-size:12px;color:#94a3b8}
  .la-domain-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}
  .la-course-card{background:#fff;border:1px solid #e5ebf2;border-radius:14px;padding:14px 16px;cursor:pointer;transition:.22s;box-shadow:var(--la-shadow)}
  .la-course-card:hover{transform:translateY(-3px);border-color:#c7d2fe;box-shadow:0 16px 40px rgba(79,70,229,.12)}
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
<meta name="description" content="热力学与统计物理知识体系：热力学基本定律、热力学势与麦克斯韦关系、相变与临界现象、玻尔兹曼统计、系综理论、量子统计、涨落理论">
<title>热力学与统计物理 · 知识体系</title>
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
    <div class="la-eyebrow">THERMODYNAMICS &amp; STATISTICAL PHYSICS · KNOWLEDGE MAP</div>
    <h1>热力学与统计物理 · 知识体系</h1>
    <p class="la-subtitle">热力学基本定律 · 热力学势与麦克斯韦关系 · 相变与临界现象 · 玻尔兹曼统计 · 系综理论 · 量子统计 · 涨落理论</p>
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
    <div>热力学与统计物理 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于热力学与统计物理核心知识体系整理</div>
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
    with open("/workspace/statistical-mechanics.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated statistical-mechanics.html ({len(html)} chars)")
