# -*- coding: utf-8 -*-
"""Generate computational-physics.html with 7 chapters: 多项式插值/数值微分/数值积分/方程求根/矩阵计算/ODE/PDE."""
import json

FIG = {
"lagrange_interp": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="16" x2="24" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 40 120 Q 105 24 190 86" fill="none" stroke="#2563eb" stroke-width="2"/>
<g fill="#1e40af">
<circle cx="40" cy="120" r="3.2"/><circle cx="112" cy="42" r="3.2"/><circle cx="190" cy="86" r="3.2"/>
</g>
<line x1="40" y1="120" x2="40" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2"/>
<line x1="112" y1="42" x2="112" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2"/>
<line x1="190" y1="86" x2="190" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2"/>
<text x="32" y="146" font-size="10" fill="#475569">x0</text>
<text x="106" y="146" font-size="10" fill="#475569">x1</text>
<text x="184" y="146" font-size="10" fill="#475569">x2</text>
<text x="30" y="24" font-size="10" fill="#2563eb">L2(x)</text>
<text x="60" y="34" font-size="10" fill="#64748b">二次拉格朗日插值</text>
</svg>''',
"newton_divdiff": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<g stroke="#7c3aed" stroke-width="1" fill="none">
<rect x="16" y="20" width="64" height="24"/><rect x="16" y="52" width="64" height="24"/>
<rect x="16" y="84" width="64" height="24"/><rect x="16" y="116" width="64" height="24"/>
<rect x="96" y="36" width="64" height="24"/><rect x="96" y="68" width="64" height="24"/>
<rect x="96" y="100" width="64" height="24"/>
<rect x="176" y="68" width="56" height="24"/>
</g>
<text x="24" y="36" font-size="10" fill="#334155">f[x0]</text>
<text x="24" y="68" font-size="10" fill="#334155">f[x1]</text>
<text x="24" y="100" font-size="10" fill="#334155">f[x2]</text>
<text x="24" y="132" font-size="10" fill="#334155">f[x3]</text>
<text x="104" y="52" font-size="10" fill="#7c3aed">f[x0,x1]</text>
<text x="104" y="84" font-size="10" fill="#7c3aed">f[x1,x2]</text>
<text x="104" y="116" font-size="10" fill="#7c3aed">f[x2,x3]</text>
<text x="182" y="84" font-size="10" fill="#5b21b6">f[x0..x2]</text>
</svg>''',
"hermite_interp": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="16" x2="24" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 36 116 C 80 40 130 130 200 60" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="90" cy="70" r="3.4" fill="#1e40af"/>
<line x1="52" y1="106" x2="128" y2="34" stroke="#c2410c" stroke-width="2"/>
<line x1="90" y1="70" x2="90" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2"/>
<text x="94" y="66" font-size="10" fill="#c2410c">切线斜率 f'(x0)</text>
<text x="40" y="126" font-size="10" fill="#3b82f6">H(x) 同时匹配函数值与导数值</text>
<text x="84" y="146" font-size="10" fill="#475569">x0</text>
</svg>''',
"cubic_spline": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="20" y1="16" x2="20" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 34 112 Q 60 60 92 62" fill="none" stroke="#2563eb" stroke-width="2"/>
<path d="M 92 62 Q 124 64 150 84" fill="none" stroke="#0ea5e9" stroke-width="2"/>
<path d="M 150 84 Q 176 104 214 96" fill="none" stroke="#1d4ed8" stroke-width="2"/>
<g fill="#1e40af">
<circle cx="34" cy="112" r="3.2"/><circle cx="92" cy="62" r="3.2"/><circle cx="150" cy="84" r="3.2"/><circle cx="214" cy="96" r="3.2"/>
</g>
<text x="26" y="146" font-size="10" fill="#475569">x0</text>
<text x="86" y="146" font-size="10" fill="#475569">x1</text>
<text x="144" y="146" font-size="10" fill="#475569">x2</text>
<text x="208" y="146" font-size="10" fill="#475569">x3</text>
<text x="70" y="26" font-size="10" fill="#2563eb">三次样条：节点处一阶、二阶导连续</text>
</svg>''',
"runge": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="80" x2="228" y2="80" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="16" x2="24" y2="144" stroke="#475569" stroke-width="1.2"/>
<path d="M 40 80 Q 70 40 100 74 Q 130 108 160 74 Q 190 40 214 80" fill="none" stroke="#2563eb" stroke-width="1.6"/>
<path d="M 34 96 L 48 30 L 70 96 L 92 40 L 116 100 L 140 36 L 164 100 L 188 42 L 210 92 L 220 60" fill="none" stroke="#ef4444" stroke-width="1.5"/>
<text x="34" y="24" font-size="10" fill="#ef4444">高次插值振荡</text>
<text x="36" y="100" font-size="10" fill="#2563eb">f(x)=1/(1+25x²)</text>
<text x="160" y="150" font-size="10" fill="#64748b">等距节点 ⟹ 龙格现象</text>
</svg>''',
"fwd_diff": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="16" x2="24" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 40 120 Q 110 80 200 40" fill="none" stroke="#7c3aed" stroke-width="2"/>
<circle cx="80" cy="98" r="3.2" fill="#5b21b6"/><circle cx="130" cy="76" r="3.2" fill="#5b21b6"/>
<line x1="80" y1="98" x2="130" y2="76" stroke="#c2410c" stroke-width="2"/>
<line x1="80" y1="98" x2="150" y2="64" stroke="#0ea5e9" stroke-width="1.4" stroke-dasharray="4 3"/>
<line x1="80" y1="98" x2="80" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2"/>
<line x1="130" y1="76" x2="130" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2"/>
<text x="66" y="146" font-size="10" fill="#475569">x</text>
<text x="122" y="146" font-size="10" fill="#475569">x+h</text>
<text x="132" y="70" font-size="10" fill="#c2410c">前向差商</text>
<text x="140" y="56" font-size="10" fill="#0ea5e9">真切线</text>
</svg>''',
"central_diff": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="16" x2="24" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 40 124 Q 120 74 210 44" fill="none" stroke="#7c3aed" stroke-width="2"/>
<circle cx="70" cy="102" r="3.2" fill="#5b21b6"/><circle cx="120" cy="80" r="3.4" fill="#c2410c"/><circle cx="170" cy="62" r="3.2" fill="#5b21b6"/>
<line x1="70" y1="102" x2="170" y2="62" stroke="#c2410c" stroke-width="2"/>
<line x1="90" y1="96" x2="150" y2="72" stroke="#0ea5e9" stroke-width="1.4" stroke-dasharray="4 3"/>
<line x1="120" y1="80" x2="120" y2="132" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2"/>
<text x="110" y="146" font-size="10" fill="#475569">x</text>
<text x="60" y="118" font-size="10" fill="#475569">x−h</text>
<text x="164" y="58" font-size="10" fill="#475569">x+h</text>
<text x="126" y="72" font-size="10" fill="#c2410c">中心差商 O(h²)</text>
</svg>''',
"richardson": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="136" x2="228" y2="136" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="16" x2="30" y2="136" stroke="#475569" stroke-width="1.2"/>
<polyline points="40,36 90,76 140,106 190,126" fill="none" stroke="#7c3aed" stroke-width="2"/>
<polyline points="40,30 90,60 140,90 190,120" fill="none" stroke="#c2410c" stroke-width="2"/>
<text x="180" y="26" font-size="10" fill="#7c3aed">斜率≈1</text>
<text x="180" y="112" font-size="10" fill="#c2410c">斜率≈2</text>
<text x="188" y="152" font-size="10" fill="#475569">log h</text>
<text x="14" y="30" font-size="10" fill="#475569">log E</text>
<text x="46" y="120" font-size="10" fill="#64748b">外推后误差阶数提高</text>
</svg>''',
"trapezoid": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 34 120 Q 120 20 210 96" fill="none" stroke="#0d9488" stroke-width="2"/>
<g fill="#ccfbf1" stroke="#14b8a6" stroke-width="1">
<polygon points="34,120 76,120 76,64 34,112"/><polygon points="76,120 118,120 118,44 76,64"/>
<polygon points="118,120 160,120 160,44 118,44"/><polygon points="160,120 202,120 202,88 160,44"/>
</g>
<text x="40" y="146" font-size="10" fill="#475569">x0</text>
<text x="192" y="146" font-size="10" fill="#475569">xn</text>
<text x="70" y="26" font-size="10" fill="#0d9488">梯形法：折线近似曲线</text>
</svg>''',
"simpson": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 34 118 Q 120 24 210 92" fill="none" stroke="#0d9488" stroke-width="1.4" stroke-dasharray="4 3"/>
<path d="M 34 118 Q 82 46 128 84" fill="none" stroke="#14b8a6" stroke-width="2.4"/>
<path d="M 128 84 Q 174 110 210 92" fill="none" stroke="#0f766e" stroke-width="2.4"/>
<g fill="#0f766e"><circle cx="34" cy="118" r="3.2"/><circle cx="82" cy="66" r="3.2"/><circle cx="128" cy="84" r="3.2"/><circle cx="168" cy="100" r="3.2"/><circle cx="210" cy="92" r="3.2"/></g>
<text x="40" y="146" font-size="10" fill="#475569">x0</text>
<text x="200" y="146" font-size="10" fill="#475569">x2</text>
<text x="60" y="26" font-size="10" fill="#0d9488">辛普森法：抛物线近似，误差 O(h⁴)</text>
</svg>''',
"newton_cotes": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="110" x2="228" y2="110" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="20" x2="24" y2="110" stroke="#475569" stroke-width="1.2"/>
<g stroke="#14b8a6" stroke-width="1.4">
<line x1="44" y1="70" x2="44" y2="110"/><line x1="80" y1="52" x2="80" y2="110"/><line x1="116" y1="44" x2="116" y2="110"/>
<line x1="152" y1="52" x2="152" y2="110"/><line x1="188" y1="70" x2="188" y2="110"/>
</g>
<g fill="#0d9488"><circle cx="44" cy="70" r="3"/><circle cx="80" cy="52" r="3"/><circle cx="116" cy="44" r="3"/><circle cx="152" cy="52" r="3"/><circle cx="188" cy="70" r="3"/></g>
<text x="36" y="126" font-size="10" fill="#475569">x0</text>
<text x="180" y="126" font-size="10" fill="#475569">xn</text>
<text x="60" y="24" font-size="10" fill="#0d9488">等距节点：权重 C_i 为柯特斯系数</text>
</svg>''',
"romberg": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<g stroke="#0d9488" stroke-width="1" fill="none">
<rect x="20" y="18" width="52" height="26"/><rect x="20" y="52" width="52" height="26"/><rect x="20" y="86" width="52" height="26"/>
<rect x="84" y="52" width="52" height="26"/><rect x="84" y="86" width="52" height="26"/>
<rect x="148" y="86" width="52" height="26"/>
</g>
<text x="26" y="35" font-size="10" fill="#334155">R(0,0)</text>
<text x="26" y="69" font-size="10" fill="#334155">R(1,0)</text>
<text x="26" y="103" font-size="10" fill="#334155">R(2,0)</text>
<text x="90" y="69" font-size="10" fill="#0d9488">R(1,1)</text>
<text x="90" y="103" font-size="10" fill="#0d9488">R(2,1)</text>
<text x="154" y="103" font-size="10" fill="#0f766e">R(2,2)</text>
<text x="52" y="140" font-size="10" fill="#64748b">龙贝格三角表：逐列 Richardson 外推</text>
</svg>''',
"gauss_quad": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="16" x2="24" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 34 124 Q 120 30 210 108" fill="none" stroke="#059669" stroke-width="2"/>
<line x1="74" y1="76" x2="74" y2="132" stroke="#10b981" stroke-width="1.4"/>
<line x1="160" y1="72" x2="160" y2="132" stroke="#10b981" stroke-width="1.4"/>
<g fill="#047857"><circle cx="74" cy="76" r="3.4"/><circle cx="160" cy="72" r="3.4"/></g>
<text x="58" y="146" font-size="10" fill="#475569">−1/√3</text>
<text x="146" y="146" font-size="10" fill="#475569">+1/√3</text>
<text x="30" y="26" font-size="10" fill="#059669">高斯点不取端点，2 点即精确积分三次多项式</text>
</svg>''',
"monte_carlo": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="20" width="120" height="120" fill="#f0fdf4" stroke="#059669" stroke-width="1.2"/>
<path d="M 30 140 Q 90 30 150 90 L 150 140 Z" fill="#d1fae5" opacity="0.7"/>
<g fill="#065f46">
<circle cx="48" cy="60" r="2"/><circle cx="70" cy="100" r="2"/><circle cx="92" cy="52" r="2"/><circle cx="110" cy="118" r="2"/>
<circle cx="60" cy="128" r="2"/><circle cx="126" cy="70" r="2"/><circle cx="84" cy="86" r="2"/><circle cx="46" cy="106" r="2"/>
</g>
<g fill="#ef4444">
<circle cx="140" cy="40" r="2"/><circle cx="126" cy="30" r="2"/><circle cx="142" cy="126" r="2"/><circle cx="58" cy="36" r="2"/><circle cx="100" cy="24" r="2"/>
</g>
<text x="158" y="70" font-size="10" fill="#059669">命中数/总数</text>
<text x="158" y="86" font-size="10" fill="#059669">≈ 面积</text>
<text x="34" y="18" font-size="10" fill="#64748b">蒙特卡洛：随机投点估计积分，误差 O(N⁻¹ᐟ²)</text>
</svg>''',
"bisection": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="80" x2="228" y2="80" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="16" x2="24" y2="144" stroke="#475569" stroke-width="1.2"/>
<path d="M 40 132 Q 120 76 200 28" fill="none" stroke="#c2410c" stroke-width="2"/>
<circle cx="118" cy="80" r="3.4" fill="#9a3412"/>
<line x1="60" y1="20" x2="60" y2="140" stroke="#ea580c" stroke-width="1" stroke-dasharray="4 3"/>
<line x1="180" y1="20" x2="180" y2="140" stroke="#ea580c" stroke-width="1" stroke-dasharray="4 3"/>
<line x1="120" y1="20" x2="120" y2="140" stroke="#f97316" stroke-width="1.4"/>
<text x="52" y="34" font-size="10" fill="#ea580c">a</text>
<text x="172" y="34" font-size="10" fill="#ea580c">b</text>
<text x="112" y="34" font-size="10" fill="#f97316">中点</text>
<text x="120" y="96" font-size="10" fill="#9a3412">根</text>
<text x="40" y="152" font-size="10" fill="#64748b">每次迭代区间减半，误差 ≤ (b−a)/2ⁿ</text>
</svg>''',
"fixed_point": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="16" x2="24" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="126" x2="200" y2="26" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/>
<path d="M 40 122 Q 90 92 130 66 Q 160 48 190 34" fill="none" stroke="#ea580c" stroke-width="2"/>
<g stroke="#c2410c" stroke-width="1" fill="none">
<line x1="60" y1="110" x2="60" y2="104"/><line x1="60" y1="104" x2="86" y2="104"/><line x1="86" y1="104" x2="86" y2="92"/><line x1="86" y1="92" x2="104" y2="92"/>
<line x1="104" y1="92" x2="104" y2="84"/><line x1="104" y1="84" x2="118" y2="84"/>
</g>
<circle cx="150" cy="58" r="3.2" fill="#9a3412"/>
<text x="152" y="54" font-size="10" fill="#9a3412">不动点 x*=g(x*)</text>
<text x="40" y="146" font-size="10" fill="#64748b">蛛网图：|g'(x)|&lt;1 时收敛</text>
</svg>''',
"newton_root": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="80" x2="228" y2="80" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="16" x2="24" y2="144" stroke="#475569" stroke-width="1.2"/>
<path d="M 40 130 Q 110 70 170 40 Q 196 28 212 34" fill="none" stroke="#c2410c" stroke-width="2"/>
<circle cx="60" cy="112" r="3.4" fill="#9a3412"/>
<line x1="60" y1="112" x2="140" y2="80" stroke="#ea580c" stroke-width="2"/>
<line x1="140" y1="80" x2="140" y2="80" stroke="#ea580c" stroke-width="2"/>
<circle cx="140" cy="80" r="3.2" fill="#f97316"/>
<line x1="140" y1="80" x2="196" y2="80" stroke="#ea580c" stroke-width="1.6"/>
<line x1="60" y1="112" x2="60" y2="80" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2"/>
<text x="54" y="76" font-size="10" fill="#475569">x0</text>
<text x="134" y="76" font-size="10" fill="#f97316">x1</text>
<text x="60" y="146" font-size="10" fill="#64748b">牛顿法：沿切线逼近，二次收敛</text>
</svg>''',
"secant": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="80" x2="228" y2="80" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="16" x2="24" y2="144" stroke="#475569" stroke-width="1.2"/>
<path d="M 40 132 Q 120 74 200 30" fill="none" stroke="#c2410c" stroke-width="2"/>
<circle cx="60" cy="116" r="3.2" fill="#9a3412"/><circle cx="130" cy="70" r="3.2" fill="#9a3412"/>
<line x1="60" y1="116" x2="130" y2="70" stroke="#f97316" stroke-width="2"/>
<line x1="130" y1="70" x2="186" y2="80" stroke="#f97316" stroke-width="1.4" stroke-dasharray="4 3"/>
<circle cx="186" cy="80" r="3.2" fill="#f97316"/>
<text x="54" y="130" font-size="10" fill="#475569">x₋₁</text>
<text x="124" y="64" font-size="10" fill="#475569">x0</text>
<text x="180" y="94" font-size="10" fill="#f97316">x1</text>
<text x="40" y="146" font-size="10" fill="#64748b">割线法：用两点割线代替切线，免去求导</text>
</svg>''',
"newton_system": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="24" y="16" width="204" height="124" fill="none" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 40 40 Q 120 96 200 60" fill="none" stroke="#c2410c" stroke-width="2"/>
<path d="M 60 24 Q 96 100 140 138" fill="none" stroke="#ea580c" stroke-width="2"/>
<circle cx="116" cy="72" r="4" fill="#9a3412"/>
<text x="122" y="68" font-size="10" fill="#9a3412">解 (x*,y*)</text>
<text x="160" y="54" font-size="10" fill="#c2410c">f(x,y)=0</text>
<text x="60" y="134" font-size="10" fill="#ea580c">g(x,y)=0</text>
<text x="30" y="152" font-size="10" fill="#64748b">牛顿法用雅可比矩阵 J 做二维线性化</text>
</svg>''',
"lu_decomp": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<g stroke="#be185d" stroke-width="1.2" fill="none">
<rect x="14" y="50" width="46" height="60"/><rect x="94" y="50" width="46" height="60"/><rect x="176" y="50" width="46" height="60"/>
</g>
<line x1="64" y1="80" x2="90" y2="80" stroke="#475569" stroke-width="1.6"/><polygon points="94,80 84,76 84,84" fill="#475569"/>
<line x1="144" y1="80" x2="172" y2="80" stroke="#475569" stroke-width="1.6"/><polygon points="176,80 166,76 166,84" fill="#475569"/>
<text x="20" y="74" font-size="12" fill="#9d174d">L</text>
<text x="20" y="92" font-size="9" fill="#be185d">下三角</text>
<text x="100" y="74" font-size="12" fill="#9d174d">U</text>
<text x="100" y="92" font-size="9" fill="#be185d">上三角</text>
<text x="182" y="74" font-size="12" fill="#9d174d">A</text>
<text x="182" y="92" font-size="9" fill="#be185d">系数阵</text>
<text x="30" y="132" font-size="10" fill="#64748b">Doolittle：A = L·U，对角元 L_ii=1</text>
<text x="30" y="146" font-size="10" fill="#64748b">消元一次，回代解多个右端项</text>
</svg>''',
"tridiagonal": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="30" width="180" height="100" fill="#fff1f2" stroke="#be185d" stroke-width="1"/>
<g stroke="#fbcfe8" stroke-width="1">
<line x1="30" y1="50" x2="210" y2="50"/><line x1="30" y1="70" x2="210" y2="70"/><line x1="30" y1="90" x2="210" y2="90"/><line x1="30" y1="110" x2="210" y2="110"/>
<line x1="60" y1="30" x2="60" y2="130"/><line x1="90" y1="30" x2="90" y2="130"/><line x1="120" y1="30" x2="120" y2="130"/><line x1="150" y1="30" x2="150" y2="130"/><line x1="180" y1="30" x2="180" y2="130"/>
</g>
<g fill="#be185d">
<rect x="90" y="50" width="28" height="18"/><rect x="62" y="70" width="26" height="18"/><rect x="92" y="70" width="26" height="18"/><rect x="120" y="70" width="26" height="18"/>
<rect x="92" y="90" width="26" height="18"/><rect x="120" y="90" width="26" height="18"/><rect x="150" y="90" width="26" height="18"/>
</g>
<text x="34" y="146" font-size="10" fill="#64748b">三对角带状矩阵：仅主对角与上下次对角非零</text>
</svg>''',
"qr": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="130" x2="220" y2="130" stroke="#475569" stroke-width="1"/>
<line x1="30" y1="130" x2="30" y2="24" stroke="#475569" stroke-width="1"/>
<line x1="30" y1="130" x2="150" y2="50" stroke="#be185d" stroke-width="2"/><polygon points="150,50 138,50 142,60" fill="#be185d"/>
<line x1="30" y1="130" x2="120" y2="130" stroke="#db2777" stroke-width="2"/>
<line x1="30" y1="130" x2="60" y2="76" stroke="#9d174d" stroke-width="2"/><polygon points="60,76 50,84 60,88" fill="#9d174d"/>
<path d="M 96 130 A 66 66 0 0 0 78 96" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="150" y="44" font-size="10" fill="#be185d">a1</text>
<text x="100" y="146" font-size="10" fill="#db2777">q1</text>
<text x="52" y="70" font-size="10" fill="#9d174d">q2</text>
<text x="120" y="60" font-size="10" fill="#64748b">正交化 + 归一化 A=QR</text>
</svg>''',
"jacobi_gs": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="136" x2="228" y2="136" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="16" x2="30" y2="136" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="28" x2="210" y2="28" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 3"/>
<polyline points="40,124 70,90 100,62 130,44 160,34 190,30" fill="none" stroke="#be185d" stroke-width="2"/>
<polyline points="40,124 70,104 100,88 130,74 160,64 190,56" fill="none" stroke="#db2777" stroke-width="2"/>
<text x="150" y="24" font-size="10" fill="#94a3b8">精确解</text>
<text x="150" y="46" font-size="10" fill="#be185d">Gauss-Seidel</text>
<text x="150" y="72" font-size="10" fill="#db2777">Jacobi</text>
<text x="36" y="150" font-size="10" fill="#64748b">迭代误差随步数指数下降（谱半径决定速率）</text>
</svg>''',
"power_iter": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="130" x2="220" y2="130" stroke="#475569" stroke-width="1"/>
<line x1="30" y1="130" x2="30" y2="24" stroke="#475569" stroke-width="1"/>
<line x1="30" y1="130" x2="180" y2="40" stroke="#9d174d" stroke-width="2.2"/><polygon points="180,40 168,42 172,52" fill="#9d174d"/>
<line x1="30" y1="130" x2="150" y2="66" stroke="#db2777" stroke-width="1.6" opacity="0.8"/><polygon points="150,66 139,68 142,77" fill="#db2777"/>
<line x1="30" y1="130" x2="120" y2="96" stroke="#f472b6" stroke-width="1.4" opacity="0.8"/><polygon points="120,96 110,97 112,105" fill="#f472b6"/>
<text x="176" y="34" font-size="10" fill="#9d174d">主特征向量</text>
<text x="110" y="112" font-size="10" fill="#64748b">v^(k) 反复乘 A 后对齐主方向</text>
</svg>''',
"euler_rk": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="16" x2="30" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 36 116 Q 130 70 214 34" fill="none" stroke="#0891b2" stroke-width="2"/>
<polyline points="36,116 74,96 112,80 150,66 188,54 214,46" fill="none" stroke="#ef4444" stroke-width="1.6"/>
<polyline points="36,116 74,92 112,72 150,56 188,42 214,32" fill="none" stroke="#0ea5e9" stroke-width="1.8"/>
<circle cx="74" cy="92" r="2.6" fill="#0ea5e9"/><circle cx="112" cy="72" r="2.6" fill="#0ea5e9"/>
<text x="150" y="28" font-size="10" fill="#0891b2">精确解</text>
<text x="150" y="86" font-size="10" fill="#ef4444">欧拉法 O(h)</text>
<text x="150" y="60" font-size="10" fill="#0ea5e9">RK4 O(h⁴)</text>
</svg>''',
"linear_multistep": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="116" x2="228" y2="116" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="20" x2="24" y2="116" stroke="#475569" stroke-width="1.2"/>
<path d="M 34 108 Q 120 60 210 30" fill="none" stroke="#0891b2" stroke-width="1.6" stroke-dasharray="4 3"/>
<g fill="#0e7490"><circle cx="50" cy="100" r="3"/><circle cx="90" cy="84" r="3"/><circle cx="130" cy="66" r="3"/><circle cx="170" cy="48" r="3"/></g>
<circle cx="200" cy="36" r="4" fill="#ef4444"/>
<line x1="50" y1="100" x2="170" y2="48" stroke="#22d3ee" stroke-width="1.2"/>
<text x="40" y="112" font-size="10" fill="#0e7490">y_{n-3}</text>
<text x="80" y="112" font-size="10" fill="#0e7490">y_{n-2}</text>
<text x="120" y="112" font-size="10" fill="#0e7490">y_{n-1}</text>
<text x="160" y="112" font-size="10" fill="#0e7490">y_n</text>
<text x="192" y="30" font-size="10" fill="#ef4444">y_{n+1}</text>
<text x="30" y="150" font-size="10" fill="#64748b">Adams 多步法：用历史点拟合多项式外推</text>
</svg>''',
"stiff": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="16" x2="30" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 36 26 C 46 110 70 126 210 128" fill="none" stroke="#0891b2" stroke-width="2"/>
<path d="M 36 40 C 120 90 150 108 210 126" fill="none" stroke="#0284c7" stroke-width="1.8" stroke-dasharray="4 3"/>
<text x="60" y="30" font-size="10" fill="#0891b2">快模式 e^{−100t}</text>
<text x="110" y="88" font-size="10" fill="#0284c7">慢模式 e^{−t}</text>
<text x="40" y="150" font-size="10" fill="#64748b">刚性：快模式迫使显式方法步长极小</text>
</svg>''',
"bvp": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="120" x2="228" y2="120" stroke="#475569" stroke-width="1.2"/>
<line x1="24" y1="16" x2="24" y2="120" stroke="#475569" stroke-width="1.2"/>
<path d="M 34 110 Q 120 40 214 96" fill="none" stroke="#0891b2" stroke-width="2"/>
<g fill="#0e7490">
<circle cx="34" cy="110" r="3"/><circle cx="70" cy="76" r="3"/><circle cx="106" cy="58" r="3"/><circle cx="142" cy="56" r="3"/><circle cx="178" cy="72" r="3"/><circle cx="214" cy="96" r="3"/>
</g>
<line x1="34" y1="110" x2="34" y2="120" stroke="#94a3b8" stroke-width="1"/><line x1="214" y1="96" x2="214" y2="120" stroke="#94a3b8" stroke-width="1"/>
<text x="26" y="134" font-size="10" fill="#c2410c">y(a)=α</text>
<text x="190" y="134" font-size="10" fill="#c2410c">y(b)=β</text>
<text x="60" y="26" font-size="10" fill="#0891b2">边值问题：离散为三对角线性方程组</text>
</svg>''',
"heat_grid": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="140" x2="228" y2="140" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="16" x2="30" y2="140" stroke="#475569" stroke-width="1.2"/>
<g stroke="#cbd5e1" stroke-width="1">
<line x1="30" y1="40" x2="220" y2="40"/><line x1="30" y1="70" x2="220" y2="70"/><line x1="30" y1="100" x2="220" y2="100"/>
<line x1="80" y1="20" x2="80" y2="140"/><line x1="130" y1="20" x2="130" y2="140"/><line x1="180" y1="20" x2="180" y2="140"/>
</g>
<g fill="#0891b2">
<circle cx="80" cy="100" r="3"/><circle cx="80" cy="40" r="3"/><circle cx="130" cy="70" r="3"/><circle cx="80" cy="70" r="3"/><circle cx="130" cy="100" r="3"/>
</g>
<line x1="80" y1="70" x2="80" y2="100" stroke="#ef4444" stroke-width="1.4"/>
<line x1="80" y1="70" x2="80" y2="40" stroke="#ef4444" stroke-width="1.4"/>
<line x1="80" y1="70" x2="30" y2="70" stroke="#ef4444" stroke-width="1.4"/>
<line x1="80" y1="70" x2="130" y2="70" stroke="#ef4444" stroke-width="1.4"/>
<text x="196" y="150" font-size="10" fill="#475569">x</text>
<text x="16" y="26" font-size="10" fill="#475569">t</text>
<text x="94" y="66" font-size="10" fill="#ef4444">显式/隐式格式</text>
</svg>''',
"wave_grid": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="140" x2="228" y2="140" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="16" x2="30" y2="140" stroke="#475569" stroke-width="1.2"/>
<g stroke="#cbd5e1" stroke-width="1">
<line x1="30" y1="40" x2="220" y2="40"/><line x1="30" y1="70" x2="220" y2="70"/><line x1="30" y1="100" x2="220" y2="100"/>
<line x1="80" y1="20" x2="80" y2="140"/><line x1="130" y1="20" x2="130" y2="140"/><line x1="180" y1="20" x2="180" y2="140"/>
</g>
<line x1="30" y1="140" x2="180" y2="40" stroke="#06b6d4" stroke-width="1.6"/>
<line x1="80" y1="140" x2="220" y2="40" stroke="#06b6d4" stroke-width="1.6"/>
<text x="150" y="34" font-size="10" fill="#06b6d4">特征线 x±ct=const</text>
<text x="36" y="152" font-size="10" fill="#64748b">波动方程依赖域由 CFL 条件约束</text>
</svg>''',
"laplace_grid": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="140" x2="228" y2="140" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="16" x2="30" y2="140" stroke="#475569" stroke-width="1.2"/>
<g stroke="#cbd5e1" stroke-width="1">
<line x1="30" y1="40" x2="200" y2="40"/><line x1="30" y1="70" x2="200" y2="70"/><line x1="30" y1="100" x2="200" y2="100"/>
<line x1="70" y1="20" x2="70" y2="140"/><line x1="110" y1="20" x2="110" y2="140"/><line x1="150" y1="20" x2="150" y2="140"/><line x1="190" y1="20" x2="190" y2="140"/>
</g>
<circle cx="110" cy="70" r="3.6" fill="#4f46e5"/>
<g fill="#7c3aed"><circle cx="110" cy="40" r="3"/><circle cx="110" cy="100" r="3"/><circle cx="70" cy="70" r="3"/><circle cx="150" cy="70" r="3"/></g>
<line x1="110" y1="70" x2="110" y2="40" stroke="#7c3aed" stroke-width="1.2"/><line x1="110" y1="70" x2="110" y2="100" stroke="#7c3aed" stroke-width="1.2"/>
<line x1="110" y1="70" x2="70" y2="70" stroke="#7c3aed" stroke-width="1.2"/><line x1="110" y1="70" x2="150" y2="70" stroke="#7c3aed" stroke-width="1.2"/>
<text x="36" y="152" font-size="10" fill="#64748b">五点差分：中心值 = 四邻均值</text>
</svg>''',
"stability": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="80" x2="228" y2="80" stroke="#475569" stroke-width="1"/>
<line x1="126" y1="16" x2="126" y2="144" stroke="#475569" stroke-width="1"/>
<circle cx="126" cy="80" r="46" fill="none" stroke="#4f46e5" stroke-width="2"/>
<line x1="126" y1="80" x2="158" y2="48" stroke="#7c3aed" stroke-width="1.6"/>
<circle cx="158" cy="48" r="3.4" fill="#7c3aed"/>
<circle cx="126" cy="80" r="2.4" fill="#475569"/>
<text x="160" y="42" font-size="10" fill="#7c3aed">放大因子 g</text>
<text x="130" y="66" font-size="10" fill="#4f46e5">|g| ≤ 1</text>
<text x="30" y="150" font-size="10" fill="#64748b">von Neumann：|g(θ)|≤1 对一切 θ 成立才稳定</text>
</svg>''',
"euler_modified": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<line x1="30" y1="16" x2="30" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 36 116 Q 130 70 214 34" fill="none" stroke="#0891b2" stroke-width="2"/>
<polyline points="36,116 90,88 145,60 214,34" fill="none" stroke="#06b6d4" stroke-width="1.8"/>
<line x1="36" y1="116" x2="90" y2="102" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/>
<line x1="63" y1="109" x2="90" y2="88" stroke="#ef4444" stroke-width="1.4"/>
<text x="150" y="28" font-size="10" fill="#0891b2">精确解</text>
<text x="96" y="100" font-size="10" fill="#ef4444">预估-校正</text>
<text x="30" y="152" font-size="10" fill="#64748b">改进欧拉法：两步预报再校正，精度 O(h²)</text>
</svg>''',
"monte_carlo_pi": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="50" y="20" width="120" height="120" fill="#f0fdf4" stroke="#059669" stroke-width="1.2"/>
<circle cx="110" cy="80" r="60" fill="none" stroke="#10b981" stroke-width="1.4"/>
<g fill="#065f46"><circle cx="80" cy="60" r="2"/><circle cx="100" cy="100" r="2"/><circle cx="130" cy="70" r="2"/><circle cx="90" cy="120" r="2"/><circle cx="120" cy="110" r="2"/></g>
<g fill="#ef4444"><circle cx="60" cy="30" r="2"/><circle cx="160" cy="30" r="2"/><circle cx="160" cy="130" r="2"/><circle cx="60" cy="130" r="2"/></g>
<text x="176" y="60" font-size="10" fill="#059669">N内/N总</text>
<text x="176" y="76" font-size="10" fill="#059669">≈ π/4</text>
<text x="60" y="154" font-size="10" fill="#64748b">随机投点估计 π，误差 ~ N⁻¹ᐟ²</text>
</svg>''',
"rect_rule": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="24" y1="132" x2="228" y2="132" stroke="#475569" stroke-width="1.2"/>
<path d="M 34 118 Q 120 26 210 92" fill="none" stroke="#0d9488" stroke-width="2"/>
<g fill="#ccfbf1" stroke="#14b8a6" stroke-width="1">
<rect x="34" y="72" width="44" height="60"/><rect x="78" y="52" width="44" height="80"/>
<rect x="122" y="54" width="44" height="78"/><rect x="166" y="76" width="44" height="56"/>
</g>
<text x="40" y="146" font-size="10" fill="#475569">x0</text>
<text x="196" y="146" font-size="10" fill="#475569">xn</text>
<text x="60" y="26" font-size="10" fill="#0d9488">矩形法：中点高度×宽度</text>
</svg>''',
"convergence_order": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="34" y1="136" x2="228" y2="136" stroke="#475569" stroke-width="1.2"/>
<line x1="34" y1="16" x2="34" y2="136" stroke="#475569" stroke-width="1.2"/>
<polyline points="46,40 96,72 146,100 196,124" fill="none" stroke="#c2410c" stroke-width="2"/>
<polyline points="46,36 96,58 146,82 196,108" fill="none" stroke="#ea580c" stroke-width="2"/>
<polyline points="46,32 96,52 146,72 196,92" fill="none" stroke="#f97316" stroke-width="2"/>
<text x="120" y="146" font-size="10" fill="#475569">迭代次数 n</text>
<text x="8" y="30" font-size="10" fill="#475569">误差</text>
<text x="150" y="66" font-size="10" fill="#f97316">二次收敛</text>
<text x="150" y="86" font-size="10" fill="#ea580c">超线性</text>
<text x="150" y="112" font-size="10" fill="#c2410c">线性</text>
</svg>''',
"heat_explicit": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="28" y1="140" x2="228" y2="140" stroke="#475569" stroke-width="1.2"/>
<line x1="28" y1="16" x2="28" y2="140" stroke="#475569" stroke-width="1.2"/>
<g stroke="#cbd5e1" stroke-width="1">
<line x1="28" y1="40" x2="220" y2="40"/><line x1="28" y1="70" x2="220" y2="70"/><line x1="28" y1="100" x2="220" y2="100"/>
<line x1="80" y1="20" x2="80" y2="140"/><line x1="130" y1="20" x2="130" y2="140"/><line x1="180" y1="20" x2="180" y2="140"/>
</g>
<circle cx="80" cy="100" r="3.4" fill="#0891b2"/><circle cx="80" cy="70" r="3.4" fill="#06b6d4"/>
<circle cx="30" cy="70" r="2.8" fill="#94a3b8"/><circle cx="130" cy="70" r="2.8" fill="#94a3b8"/><circle cx="80" cy="40" r="2.8" fill="#94a3b8"/>
<line x1="80" y1="100" x2="30" y2="70" stroke="#ef4444" stroke-width="1.2"/><line x1="80" y1="100" x2="130" y2="70" stroke="#ef4444" stroke-width="1.2"/>
<line x1="80" y1="100" x2="80" y2="70" stroke="#ef4444" stroke-width="1.4" stroke-dasharray="3 2"/>
<text x="34" y="152" font-size="10" fill="#64748b">显式格式：u_j^{n+1} 由上一层四邻显式表出</text>
</svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

CORE_FORMULAS = [
    ("拉格朗日插值多项式", "L_n(x)=\\sum_{i=0}^{n} y_i\\prod_{j\\neq i}\\frac{x-x_j}{x_i-x_j}", "过 n+1 个节点的唯一 n 次插值多项式"),
    ("拉格朗日基函数", "l_i(x)=\\prod_{j\\neq i}\\frac{x-x_j}{x_i-x_j}", "满足 l_i(x_j)=δ_{ij} 的基函数"),
    ("插值余项", "R_n(x)=\\frac{f^{(n+1)}(\\xi)}{(n+1)!}\\prod_{i=0}^{n}(x-x_i)", "插值误差的拉格朗日余项公式"),
    ("牛顿均差插值", "N_n(x)=f[x_0]+\\sum_{k=1}^{n}f[x_0,\\dots,x_k]\\prod_{i=0}^{k-1}(x-x_i)", "用差商表示的插值多项式"),
    ("一阶差商", "f[x_i,x_j]=\\frac{f(x_j)-f(x_i)}{x_j-x_i}", "差商的递推起点"),
    ("差商递推", "f[x_0,\\dots,x_k]=\\frac{f[x_1,\\dots,x_k]-f[x_0,\\dots,x_{k-1}]}{x_k-x_0}", "高阶差商的递推关系"),
    ("埃尔米特插值基", "H(x)=\\sum_i\\left[y_i\\alpha_i(x)+y_i'\\beta_i(x)\\right]", "同时匹配函数值与导数值"),
    ("三次样条导数连续", "S_i'(x_{i+1})=S_{i+1}'(x_{i+1}),\\ S_i''(x_{i+1})=S_{i+1}''(x_{i+1})", "样条节点处一阶二阶导连续条件"),
    ("样条弯矩方程", "\\mu_i M_{i-1}+2M_i+\\lambda_i M_{i+1}=d_i", "三弯矩方程，M_i 为节点二阶导"),
    ("自然样条边界", "M_0=M_n=0", "两端二阶导为零的样条边界条件"),
    ("前向差商", "f'(x_i)\\approx\\frac{f(x_{i+1})-f(x_i)}{h}", "一阶前向差商，截断误差 O(h)"),
    ("后向差商", "f'(x_i)\\approx\\frac{f(x_i)-f(x_{i-1})}{h}", "一阶后向差商，截断误差 O(h)"),
    ("中心差商", "f'(x_i)\\approx\\frac{f(x_{i+1})-f(x_{i-1})}{2h}", "中心差商，截断误差 O(h²)"),
    ("二阶中心差商", "f''(x_i)\\approx\\frac{f(x_{i+1})-2f(x_i)+f(x_{i-1})}{h^2}", "二阶导数中心差分，误差 O(h²)"),
    ("差分截断误差", "E=\\frac{h^2}{6}f'''(\\xi)+\\frac{h^4}{120}f^{(5)}(\\xi)", "中心差商的泰勒展开余项"),
    ("理查森外推", "R_j^{(k)}=\\frac{2^kR_j^{(k-1)}-R_{j-1}^{(k-1)}}{2^k-1}", "消除低阶误差项的逐级外推"),
    ("梯形公式", "T_1=\\frac{b-a}{2}\\left[f(a)+f(b)\\right]", "两端点的加权平均"),
    ("复合梯形公式", "T_n=\\frac{h}{2}\\left[f(a)+2\\sum_{i=1}^{n-1}f(x_i)+f(b)\\right]", "n 个等距子区间的梯形求和"),
    ("梯形余项", "E_T=-\\frac{(b-a)}{12}h^2 f''(\\xi)", "复合梯形公式的截断误差 O(h²)"),
    ("辛普森公式", "S=\\frac{h}{3}\\left[f(x_0)+4f(x_1)+f(x_2)\\right]", "三点抛物线积分，误差 O(h⁴)"),
    ("复合辛普森公式", "S_n=\\frac{h}{3}\\left[f_0+f_n+4\\!\\sum_{i\\text{奇}}f_i+2\\!\\sum_{i\\text{偶}}f_i\\right]", "偶数等分的复合辛普森求和"),
    ("辛普森余项", "E_S=-\\frac{b-a}{180}h^4 f^{(4)}(\\xi)", "辛普森法截断误差 O(h⁴)"),
    ("牛顿-柯特斯系数", "C_i^{(n)}=\\frac{1}{n}\\int_0^n\\prod_{j\\neq i}\\frac{t-j}{i-j}\\,dt", "等距节点的插值型求积权重"),
    ("柯特斯系数和", "\\sum_{i=0}^{n}C_i^{(n)}=1", "柯特斯系数归一化条件"),
    ("龙贝格递推", "R_{k,j}=\\frac{4^jR_{k,j-1}-R_{k-1,j-1}}{4^j-1}", "龙贝格积分表逐列外推公式"),
    ("中点法", "M=f\\!\\left(\\frac{a+b}{2}\\right)(b-a)", "单点求积，误差 O(h²)"),
    ("高斯-勒让德求积", "\\int_{-1}^{1}f(x)\\,dx\\approx\\sum_{i=1}^{n}w_i f(x_i)", "n 点高斯求积可达 2n−1 次精度"),
    ("两点高斯节点与权重", "x_{1,2}=\\mp\\frac{1}{\\sqrt{3}},\\quad w_{1,2}=1", "两点高斯-勒让德公式"),
    ("三点高斯权重", "w_{1,3}=\\frac{5}{9},\\ w_2=\\frac{8}{9},\\ x_{1,3}=\\mp\\sqrt{\\frac{3}{5}},\\ x_2=0", "三点高斯-勒让德公式"),
    ("勒让德正交性", "\\int_{-1}^{1}P_m(x)P_n(x)\\,dx=\\frac{2}{2n+1}\\delta_{mn}", "高斯点即勒让德多项式零点"),
    ("蒙特卡洛积分", "\\int_a^b f(x)\\,dx\\approx(b-a)\\frac{1}{N}\\sum_{i=1}^N f(x_i)", "随机抽样估计积分值"),
    ("蒙特卡洛误差", "\\sigma_I=\\frac{(b-a)\\sigma_f}{\\sqrt{N}}", "误差随 N^{−1/2} 下降"),
    ("二分法误差界", "|x_n-x^*|\\le\\frac{b-a}{2^{n+1}}", "n 次二分后根的误差上界"),
    ("不动点迭代", "x_{k+1}=g(x_k)\\ \\Rightarrow\\ x^*=g(x^*)", "把 f(x)=0 改写为不动点形式"),
    ("不动点收敛条件", "|g'(x)|\\le L<1", "压缩映射保证唯一不动点与收敛"),
    ("迭代误差估计", "|x_k-x^*|\\le\\frac{L}{1-L}|x_k-x_{k-1}|", "用相邻迭代差估计误差"),
    ("牛顿迭代公式", "x_{k+1}=x_k-\\frac{f(x_k)}{f'(x_k)}", "沿切线方向的迭代，二次收敛"),
    ("牛顿法误差关系", "e_{k+1}=\\frac{f''(\\xi)}{2f'(x^*)}e_k^2", "牛顿法的二次收敛误差关系"),
    ("割线法迭代", "x_{k+1}=x_k-\\frac{f(x_k)(x_k-x_{k-1})}{f(x_k)-f(x_{k-1})}", "用两点的差商代替导数"),
    ("割线法收敛阶", "p=\\frac{1+\\sqrt{5}}{2}\\approx1.618", "割线法为超线性收敛"),
    ("抛物线法迭代", "x_{k+1}=x_k-\\frac{2c}{b\\pm\\sqrt{b^2-4ac}}", "Muller 法用二次插值求根"),
    ("非线性方程组牛顿法", "\\mathbf{x}^{(k+1)}=\\mathbf{x}^{(k)}-J^{-1}(\\mathbf{x}^{(k)})\\mathbf{F}(\\mathbf{x}^{(k)})", "J 为雅可比矩阵"),
    ("高斯消元回代", "x_i=\\frac{1}{a_{ii}}\\left(b_i-\\sum_{j>i}a_{ij}x_j\\right)", "上三角方程组的回代求解"),
    ("Doolittle 分解", "l_{ij}=\\frac{a_{ij}-\\sum_{k\\lt j}l_{ik}u_{kj}}{u_{jj}}", "LU 分解中 L 元素的计算公式"),
    ("LU 分解求解", "A=LU,\\ Ly=b,\\ Ux=y", "一次分解多次求解右端项"),
    ("列主元消元", "|a_{pk}|=\\max_i|a_{ik}|", "选取主元以控制舍入误差"),
    ("追赶法", "c_i'=\\frac{c_i}{b_i-a_i c_{i-1}'},\\ d_i'=\\frac{d_i-a_i d_{i-1}'}{b_i-a_i c_{i-1}'}", "三对角方程组的 Thomas 算法前推"),
    ("追赶法回代", "x_n=d_n',\\ x_i=d_i'-c_i'x_{i+1}", "Thomas 算法回代公式"),
    ("矩阵条件数", "\\kappa(A)=\\|A\\|\\,\\|A^{-1}\\|", "衡量方程组对扰动敏感程度"),
    ("Gram-Schmidt 正交化", "q_k=\\frac{a_k-\\sum_{j\\lt k}(a_k^{\\top}q_j)q_j}{\\|a_k-\\sum_{j\\lt k}(a_k^{\\top}q_j)q_j\\|}", "逐步构造正交基"),
    ("Householder 变换", "H=I-2\\frac{vv^{\\top}}{v^{\\top}v}", "反射矩阵，把向量映到坐标轴"),
    ("QR 分解", "A=QR,\\ Q^{\\top}Q=I", "正交三角分解，最小二乘基础"),
    ("Jacobi 迭代", "x_i^{(k+1)}=\\frac{1}{a_{ii}}\\left(b_i-\\sum_{j\\neq i}a_{ij}x_j^{(k)}\\right)", "对角占优时收敛的简单迭代"),
    ("Gauss-Seidel 迭代", "x_i^{(k+1)}=\\frac{1}{a_{ii}}\\left(b_i-\\sum_{j\\lt i}a_{ij}x_j^{(k+1)}-\\sum_{j>i}a_{ij}x_j^{(k)}\\right)", "用最新分量加速收敛"),
    ("迭代收敛条件", "\\rho(M)<1", "迭代矩阵谱半径小于 1 保证收敛"),
    ("幂法", "v^{(k+1)}=\\frac{Av^{(k)}}{\\|Av^{(k)}\\|},\\ \\lambda_1\\approx v^{(k)\\top}Av^{(k)}", "求主特征值与主特征向量"),
    ("幂法收敛比", "\\left|\\frac{\\lambda_2}{\\lambda_1}\\right|^k", "收敛速度由次主特征值之比决定"),
    ("瑞利商", "R(x)=\\frac{x^{\\top}Ax}{x^{\\top}x}", "对称矩阵特征值的变分估计"),
    ("反幂法", "A v=\\mu v,\\ \\mu=\\frac{1}{\\lambda}", "求最接近给定值的特征值"),
    ("欧拉法", "y_{n+1}=y_n+hf(x_n,y_n)", "最简单的一阶显式方法，误差 O(h)"),
    ("改进欧拉法", "y_{n+1}=y_n+\\frac{h}{2}\\left[f(x_n,y_n)+f(x_{n+1},y_n+hf_n)\\right]", "预估-校正，二阶精度"),
    ("二阶龙格-库塔", "y_{n+1}=y_n+\\frac{h}{2}(k_1+k_2)", "k1=f(x_n,y_n)，k2=f(x_n+h,y_n+hk1)"),
    ("经典四阶 RK4", "y_{n+1}=y_n+\\frac{h}{6}(k_1+2k_2+2k_3+k_4)", "k 由四次斜率加权，精度 O(h⁴)"),
    ("局部截断误差", "\\tau_n=\\frac{1}{h}(y_{n+1}-y(x_{n+1}))", "单步方法相容性与阶数的度量"),
    ("Adams-Bashforth 四阶", "y_{n+1}=y_n+\\frac{h}{24}(55f_n-59f_{n-1}+37f_{n-2}-9f_{n-3})", "显式线性多步法"),
    ("Adams-Moulton 三阶", "y_{n+1}=y_n+\\frac{h}{12}(5f_{n+1}+8f_n-f_{n-1})", "隐式线性多步法，作校正步"),
    ("方法绝对稳定", "|R(z)|\\le1,\\ z=\\lambda h", "稳定域包含左半平面则 A 稳定"),
    ("刚性方程特征", "\\left|\\mathrm{Re}\\,\\lambda_{\\max}\\right|\\gg\\left|\\mathrm{Re}\\,\\lambda_{\\min}\\right|", "特征值模差异悬殊导致刚性"),
    ("向后欧拉法", "y_{n+1}=y_n+hf(x_{n+1},y_{n+1})", "隐式一阶方法，A 稳定"),
    ("Crank-Nicolson", "y_{n+1}=y_n+\\frac{h}{2}(f_n+f_{n+1})", "二阶隐式方法，梯形法用于 ODE"),
    ("边值问题差分", "\\frac{y_{i+1}-2y_i+y_{i-1}}{h^2}=f(x_i)", "两点边值问题离散为三对角方程"),
    ("热方程显式格式", "u_i^{n+1}=u_i^n+r\\left(u_{i+1}^n-2u_i^n+u_{i-1}^n\\right)", "r=aΔt/Δx² 为网格比"),
    ("热方程隐式格式", "-ru_{i+1}^{n+1}+(1+2r)u_i^{n+1}-ru_{i-1}^{n+1}=u_i^n", "无条件稳定的隐式格式"),
    ("波动方程显式格式", "u_i^{n+1}=2u_i^n-u_i^{n-1}+\\mu^2\\left(u_{i+1}^n-2u_i^n+u_{i-1}^n\\right)", "三步显式，μ=cΔt/Δx"),
    ("CFL 条件", "\\frac{c\\,\\Delta t}{\\Delta x}\\le1", "波动方程显式格式的稳定性条件"),
    ("五点差分格式", "u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u_{ij}=h^2f_{ij}", "拉普拉斯/泊松方程的五点格式"),
    ("von Neumann 因子", "g(\\theta)=1-4r\\sin^2\\frac{\\theta}{2}", "热方程显式格式的放大因子"),
    ("显式热方程稳定条件", "r=\\frac{a\\,\\Delta t}{\\Delta x^2}\\le\\frac{1}{2}", "由 |g|≤1 导出的步长限制"),
    ("离散误差与相容性", "\\tau_{ij}=\\frac{u_{i+1,j}-2u_{ij}+u_{i-1,j}}{\\Delta x^2}-\\frac{\\partial^2 u}{\\partial x^2}\\to0", "截断误差趋于零即格式相容"),
    ("Lax 等价定理", "相容 + 稳定 \\iff 收敛", "线性初值问题数值格式的基本定理"),
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
"name": "1.1 拉格朗日插值",
"color": "#2563eb",
"desc": "插值问题、拉格朗日基函数与插值多项式的构造",
"items": [
{"id":"cp1s1-1","name":"插值问题与存在唯一性","tags":["def","thm","der"],"brief":"给定节点函数值求过点多项式，解存在且唯一。",
 "fig":"lagrange_interp","figCap":"过三个节点的二次拉格朗日插值多项式",
 "body": wrap(
   defn("插值问题", p("给定 $n+1$ 个互异节点 $x_0\\lt x_1\\lt\\dots\\lt x_n$ 及相应函数值 $y_i=f(x_i)$，求次数不超过 $n$ 的多项式 $P(x)$，使其满足")+
   fml("P(x_i)=y_i,\\qquad i=0,1,\\dots,n"))+
   thm("存在唯一性定理", p("满足上述插值条件的次数不超过 $n$ 的多项式存在且唯一。"))+
   der(p("<strong>化为线性方程组：</strong>设 $P(x)=a_0+a_1x+\\dots+a_nx^n$，插值条件给出关于系数 $a_k$ 的 $n+1$ 阶线性方程组：")+
   fml("\\begin{pmatrix}1&x_0&\\cdots&x_0^n\\\\ \\vdots&&\\vdots\\\\ 1&x_n&\\cdots&x_n^n\\end{pmatrix}\\begin{pmatrix}a_0\\\\ \\vdots\\\\ a_n\\end{pmatrix}=\\begin{pmatrix}y_0\\\\ \\vdots\\\\ y_n\\end{pmatrix}")+
   p("其系数矩阵为范德蒙矩阵，行列式为节点两两之差之积：")+
   fml("\\det V=\\prod_{0\\le i\\lt j\\le n}(x_j-x_i)\\neq0")+
   p("因节点互异，行列式非零，方程组有唯一解，故插值多项式存在且唯一。"))+
   note(p("该唯一性说明拉格朗日形式与牛顿形式给出的是同一个多项式，只是表达方式不同。"))
 )},
{"id":"cp1s1-2","name":"拉格朗日基函数与插值公式","tags":["def","der"],"brief":"用基函数张成插值多项式空间。",
 "body": wrap(
   defn("拉格朗日基函数", p("定义 $n+1$ 个 $n$ 次多项式作为基函数")+
   fml("l_i(x)=\\prod_{j=0,\\,j\\neq i}^{n}\\frac{x-x_j}{x_i-x_j}"))+
   der(p("<strong>基函数的性质：</strong>每个 $l_i(x)$ 为 $n$ 次多项式，且在节点上满足克罗内克条件：")+
   fml("l_i(x_j)=\\delta_{ij}=\\begin{cases}1,&i=j\\\\0,&i\\neq j\\end{cases}")+
   p("当 $j\\neq i$ 时分子含因子 $x_j-x_j=0$，故为零；当 $j=i$ 时分子分母相同，故为 1。")+
   p("<strong>构造插值多项式：</strong>取基函数线性组合")+
   fml("L_n(x)=\\sum_{i=0}^{n}y_i\\,l_i(x)")+
   p("代入节点 $x_j$，由克罗内克条件立即得 $L_n(x_j)=y_j$，故 $L_n$ 即为所求的插值多项式。"))+
   exa(p("<strong>一次插值：</strong>两节点时 $l_0(x)=\\frac{x-x_1}{x_0-x_1}$，$l_1(x)=\\frac{x-x_0}{x_1-x_0}$，即常见的线性插值。"))+
   note(p("基函数一经构造即可复用于不同函数值，是理解整体插值与重心插值的基础。"))
 )},
{"id":"cp1s1-3","name":"拉格朗日插值的计算与例题","tags":["exa","der"],"brief":"通过算例掌握拉格朗日插值的计算流程。",
 "body": wrap(
   exa(p("<strong>例：</strong>已知 $f(1)=2,\\ f(2)=3,\\ f(3)=6$，求二次插值多项式并估算 $f(2.5)$。")+
   fml("l_0=\\frac{(x-2)(x-3)}{2},\\quad l_1=-(x-1)(x-3),\\quad l_2=\\frac{(x-1)(x-2)}{2}"))+
   der(p("<strong>代入求和：</strong>按 $L_2(x)=\\sum y_i l_i$ 展开：")+
   fml("L_2(x)=(x-2)(x-3)-3(x-1)(x-3)+3(x-1)(x-2)")+
   p("逐项展开：$(x^2-5x+6)-3(x^2-4x+3)+3(x^2-3x+2)$，合并同类项得：")+
   fml("L_2(x)=x^2-2x+3")+
   p("代 $x=1,2,3$ 分别得 $2,3,6$，验证插值条件成立；代 $x=2.5$ 得 $f(2.5)\\approx4.25$。"))+
   note(p("<strong>复杂度：</strong>直接计算每个基函数需 $O(n)$ 次乘法，$n+1$ 个基函数共 $O(n^2)$；实际编程常用重心公式或秦九韶式优化。"))
 )},
]},
{
"name": "1.2 牛顿插值与差商",
"color": "#0ea5e9",
"desc": "差商定义与性质、牛顿插值公式及其余项",
"items": [
{"id":"cp1s2-1","name":"差商的定义与性质","tags":["def","der"],"brief":"差商是函数值组合，具有对称性与递推性。",
 "fig":"newton_divdiff","figCap":"差商表：逐列递推计算各阶差商",
 "body": wrap(
   defn("差商", p("称 $f[x_i]=\\frac{f(x_i)}{1!}$ 为零阶差商；一阶差商定义为")+
   fml("f[x_i,x_j]=\\frac{f(x_j)-f(x_i)}{x_j-x_i}")+
   p("一般 $k$ 阶差商由 $k-1$ 阶差商递推定义：")+
   fml("f[x_0,\\dots,x_k]=\\frac{f[x_1,\\dots,x_k]-f[x_0,\\dots,x_{k-1}]}{x_k-x_0}"))+
   der(p("<strong>对称性：</strong>可以证明差商与节点排列次序无关。以二阶差商为例，按两种次序展开：")+
   fml("f[x_0,x_1,x_2]=\\frac{f[x_1,x_2]-f[x_0,x_1]}{x_2-x_0}")+
   p("代入一阶差商并通分，分子化简为")+
   fml("\\frac{f(x_2)}{(x_2-x_0)(x_2-x_1)}+\\frac{f(x_1)}{(x_1-x_0)(x_1-x_2)}+\\frac{f(x_0)}{(x_0-x_1)(x_0-x_2)}")+
   p("该式对节点完全对称，交换任意两个节点表达式不变，故差商对称。"))+
   note(p("对称性使差商可看作「均差」，也是数值微分与牛顿插值余项的理论基础。"))
 )},
{"id":"cp1s2-2","name":"牛顿插值公式与余项","tags":["thm","der"],"brief":"用差商逐次添加节点构造插值多项式。",
 "body": wrap(
   thm("牛顿插值公式", p("以 $x_0$ 为起点，用差商表示插值多项式：")+
   fml("N_n(x)=f[x_0]+\\sum_{k=1}^{n}f[x_0,\\dots,x_k]\\prod_{i=0}^{k-1}(x-x_i)"))+
   der(p("<strong>推导：</strong>由差商定义，对任一节点 $x$ 与 $x_0$：")+
   fml("f(x)=f[x_0]+(x-x_0)f[x_0,x]")+
   p("再对 $f[x_0,x]$ 应用差商定义：")+
   fml("f[x_0,x]=f[x_0,x_1]+(x-x_1)f[x_0,x_1,x]")+
   p("如此逐步展开到 $n$ 阶，得到")+
   fml("f(x)=N_n(x)+\\left(\\prod_{i=0}^{n}(x-x_i)\\right)f[x_0,\\dots,x_n,x]")+
   p("其中 $N_n$ 即为插值多项式，余项为 $R_n(x)=\\prod_{i=0}^n(x-x_i)\\,f[x_0,\\dots,x_n,x]$。"))+
   note(p("牛顿形式的优点是<strong>便于增加节点</strong>：新增节点时只需追加一项，无需重算全部。"))
 )},
{"id":"cp1s2-3","name":"差商表的计算与例题","tags":["exa","der"],"brief":"列表递推计算各阶差商。",
 "body": wrap(
   exa(p("<strong>例：</strong>已知 $f(0)=1,\\ f(1)=2,\\ f(2)=5,\\ f(3)=10$，用差商表写出牛顿插值多项式。")+
   fml("f[x_0,x_1]=1,\\ f[x_1,x_2]=3,\\ f[x_2,x_3]=5"))+
   der(p("<strong>逐列计算：</strong>一阶差商为 $1,3,5$；二阶差商：")+
   fml("f[x_0,x_1,x_2]=\\frac{3-1}{2-0}=1,\\quad f[x_1,x_2,x_3]=\\frac{5-3}{3-1}=1")+
   p("三阶差商：")+
   fml("f[x_0,x_1,x_2,x_3]=\\frac{1-1}{3-0}=0")+
   p("故插值多项式为 $N_3(x)=1+1\\cdot x+1\\cdot x(x-1)+0=x^2+1$，恰好是数据的精确规律。"))+
   note(p("<strong>编程提示：</strong>差商表沿对角线保存即可，空间 $O(n)$，时间 $O(n^2)$；与拉格朗日插值结果完全一致。"))
 )},
]},
{
"name": "1.3 埃尔米特插值",
"color": "#3b82f6",
"desc": "同时匹配函数值与导数值的重节点插值",
"items": [
{"id":"cp1s3-1","name":"埃尔米特插值问题","tags":["def","thm","der"],"brief":"插值条件同时包含函数值与一阶导数。",
 "fig":"hermite_interp","figCap":"埃尔米特插值曲线在节点处与函数相切",
 "body": wrap(
   defn("埃尔米特插值", p("给定节点 $x_0,\\dots,x_n$ 上的函数值 $y_i$ 与导数值 $y_i'$，求次数不超过 $2n+1$ 的多项式 $H(x)$，满足")+
   fml("H(x_i)=y_i,\\quad H'(x_i)=y_i',\\qquad i=0,\\dots,n"))+
   thm("存在唯一性", p("上述 $2n+2$ 个插值条件的埃尔米特插值多项式存在且唯一。"))+
   der(p("<strong>构造思路（基函数法）：</strong>仿照拉格朗日基函数，取 $2n+2$ 个基函数，要求")+
   fml("\\alpha_i(x_j)=\\delta_{ij},\\ \\alpha_i'(x_j)=0,\\quad \\beta_i(x_j)=0,\\ \\beta_i'(x_j)=\\delta_{ij}")+
   p("借助拉格朗日基函数 $l_i$ 可构造：")+
   fml("\\alpha_i(x)=\\left[1-2l_i'(x_i)(x-x_i)\\right]l_i^2(x),\\quad \\beta_i(x)=(x-x_i)l_i^2(x)")+
   p("则 $H(x)=\\sum_i\\left[y_i\\alpha_i(x)+y_i'\\beta_i(x)\\right]$ 满足全部插值条件，且次数不超过 $2n+1$。"))+
   note(p("埃尔米特插值充分利用了导数信息，其逼近精度通常高于同节点数的拉格朗日插值。"))
 )},
{"id":"cp1s3-2","name":"重节点差商与埃尔米特公式","tags":["thm","der"],"brief":"把导数条件吸收进差商，得到紧凑公式。",
 "body": wrap(
   defn("重节点差商", p("定义重节点差商 $f[x_i,x_i]=f'(x_i)$，从而把导数条件并入差商体系。"))+
   der(p("<strong>推导：</strong>在牛顿插值公式中令节点重复出现，即把 $x_0,\\dots,x_n$ 扩充为每节点出现两次的序列，由差商定义")+
   fml("f[x_i,x_i]=\\lim_{x\\to x_i}\\frac{f(x)-f(x_i)}{x-x_i}=f'(x_i)")+
   p("于是埃尔米特插值可写为与牛顿插值同构的形式：")+
   fml("H_{2n+1}(x)=\\sum_{k=0}^{2n+1}f[\\underbrace{x_0,\\dots,x_0}_{},\\dots]\\prod_{i}(x-x_i)")+
   p("其中重复节点处自动取导数值，余项为")+
   fml("R_{2n+1}(x)=\\frac{f^{(2n+2)}(\\xi)}{(2n+2)!}\\prod_{i=0}^{n}(x-x_i)^2"))+
   note(p("余项含 $(x-x_i)^2$ 因子，说明误差在节点附近比普通插值衰减更快。"))
 )},
{"id":"cp1s3-3","name":"两点三次埃尔米特插值","tags":["exa","der"],"brief":"最常用的三次埃尔米特插值，用于分段与有限元。",
 "body": wrap(
   exa(p("<strong>例：</strong>区间 $[x_0,x_1]$ 上给定 $y_0,y_0',y_1,y_1'$，求三次埃尔米特插值多项式。")+
   fml("H_3(x)=y_0\\alpha_0+y_0'\\beta_0+y_1\\alpha_1+y_1'\\beta_1"))+
   der(p("<strong>推导：</strong>令 $t=\\frac{x-x_0}{h}$，$h=x_1-x_0$，则四次基函数为")+
   fml("\\alpha_0=1-3t^2+2t^3,\\quad \\alpha_1=3t^2-2t^3")+
   p("以及")+
   fml("\\beta_0=h\\,t(1-t)^2,\\quad \\beta_1=h\\,t^2(t-1)")+
   p("它们满足 $\\alpha_0(0)=1,\\alpha_0'(0)=0,\\alpha_0(1)=0,\\alpha_0'(1)=0$ 等端点条件，代入即得插值多项式。"))+
   app(p("<strong>应用：</strong>三次埃尔米特插值被广泛用于分段插值、有限元法的形函数与计算机图形学中的曲线插值，因其能保证一阶光滑且计算简单。"))
 )},
]},
{
"name": "1.4 样条插值",
"color": "#1d4ed8",
"desc": "分段低次插值，保证节点处光滑，避免龙格现象",
"items": [
{"id":"cp1s4-1","name":"三次样条与连续性条件","tags":["def","der"],"brief":"分段三次多项式，节点处一二阶导连续。",
 "fig":"cubic_spline","figCap":"三次样条：分段三次多项式在节点处光滑拼接",
 "body": wrap(
   defn("三次样条函数", p("给定节点 $a=x_0\\lt x_1\\lt\\dots\\lt x_n=b$ 与函数值 $y_i$，若分段函数 $S(x)$ 在每个子区间 $[x_i,x_{i+1}]$ 上都是三次多项式，且整体具有二阶连续导数，则称 $S$ 为三次样条。"))+
   der(p("<strong>自由度分析：</strong>共有 $n$ 段，每段 4 个系数，共 $4n$ 个未知数。插值条件 $S(x_i)=y_i$ 有 $n+1$ 条；内节点 $x_1,\\dots,x_{n-1}$ 处要求")+
   fml("S(x_i^-)=S(x_i^+),\\quad S'(x_i^-)=S'(x_i^+),\\quad S''(x_i^-)=S''(x_i^+)")+
   p("共 $3(n-1)$ 条。合计 $4n-2$ 条约束，尚缺 2 个条件，需给出两个边界条件。")+
   p("常见边界：<strong>自然样条</strong> $S''(x_0)=S''(x_n)=0$；<strong>固定边界</strong>给定端部一阶导。"))+
   note(p("样条以分段低次多项式换取整体光滑，能有效抑制高次插值的振荡。"))
 )},
{"id":"cp1s4-2","name":"三弯矩方程","tags":["thm","der"],"brief":"将样条求解化为关于节点二阶导的三对角方程组。",
 "body": wrap(
   thm("三弯矩方程", p("记节点二阶导 $M_i=S''(x_i)$，则内节点满足")+
   fml("\\mu_iM_{i-1}+2M_i+\\lambda_iM_{i+1}=d_i,\\qquad i=1,\\dots,n-1")+
   p("其中 $h_i=x_i-x_{i-1}$，$\\mu_i=\\frac{h_i}{h_i+h_{i+1}}$，$\\lambda_i=1-\\mu_i$。"))+
   der(p("<strong>推导：</strong>在 $[x_i,x_{i+1}]$ 上 $S''$ 为线性函数，由线性插值得")+
   fml("S''(x)=\\frac{x_{i+1}-x}{h_{i+1}}M_i+\\frac{x-x_i}{h_{i+1}}M_{i+1}")+
   p("积分两次并用 $S(x_i)=y_i,S(x_{i+1})=y_{i+1}$ 定常数，得该段表达式。")+
   p("再对相邻两段求导并在节点处令 $S'(x_i^-)=S'(x_i^+)$，整理得：")+
   fml("\\frac{h_i}{6}M_{i-1}+\\frac{h_i+h_{i+1}}{3}M_i+\\frac{h_{i+1}}{6}M_{i+1}=\\frac{y_{i+1}-y_i}{h_{i+1}}-\\frac{y_i-y_{i-1}}{h_i}")+
   p("两边同乘 $\\frac{6}{h_i+h_{i+1}}$ 即得三弯矩方程的标准形式。"))+
   note(p("三弯矩方程是严格对角占优的三对角方程组，用追赶法可 $O(n)$ 求解。"))
 )},
{"id":"cp1s4-3","name":"边界条件与样条求解","tags":["der","exa"],"brief":"给出边界条件后求解三对角方程组得到样条。",
 "body": wrap(
   der(p("<strong>自然边界：</strong>令 $M_0=M_n=0$，则内节点方程为 $n-1$ 阶三对角方程组：")+
   fml("\\begin{pmatrix}2&\\lambda_1&&\\\\ \\mu_2&2&\\lambda_2&\\\\ &\\ddots&\\ddots&\\ddots\\\\ &&\\mu_{n-1}&2\\end{pmatrix}\\begin{pmatrix}M_1\\\\ \\vdots\\\\ M_{n-1}\\end{pmatrix}=\\begin{pmatrix}d_1\\\\ \\vdots\\\\ d_{n-1}\\end{pmatrix}")+
   p("系数矩阵严格对角占优，追赶法稳定且唯一可解。")+
   p("<strong>固定边界：</strong>若给定 $S'(x_0)=y_0'$，则补充方程")+
   fml("2M_0+M_1=\\frac{6}{h_1}\\left(\\frac{y_1-y_0}{h_1}-y_0'\\right)")+
   p("右端类似处理即可。"))+
   exa(p("<strong>例：</strong>对 $\\sin$ 表在 $[0,\\pi]$ 上作自然样条，节点加密时最大误差按 $O(h^4)$ 下降，远优于等距高次插值。"))+
   note(p("样条是工程数据拟合的事实标准，可用于曲线插值、路径规划与图像重采样。"))
 )},
]},
{
"name": "1.5 插值误差与龙格现象",
"color": "#2563eb",
"desc": "插值余项、收敛性与切比雪夫节点",
"items": [
{"id":"cp1s5-1","name":"插值余项定理","tags":["thm","der"],"brief":"插值误差由节点乘积与高阶导数决定。",
 "body": wrap(
   thm("插值余项", p("设 $f\\in C^{n+1}[a,b]$，$L_n$ 为过 $n+1$ 个互异节点的插值多项式，则对任意 $x\\in[a,b]$ 存在 $\\xi\\in(a,b)$ 使")+
   fml("R_n(x)=f(x)-L_n(x)=\\frac{f^{(n+1)}(\\xi)}{(n+1)!}\\prod_{i=0}^{n}(x-x_i)"))+
   der(p("<strong>推导：</strong>固定 $x\\neq x_i$，构造辅助函数")+
   fml("\\varphi(t)=f(t)-L_n(t)-K\\prod_{i=0}^{n}(t-x_i)")+
   p("选取 $K$ 使 $\\varphi(x)=0$。则 $\\varphi$ 在 $x_0,\\dots,x_n,x$ 共 $n+2$ 个点为零。")+
   p("由罗尔定理逐次求导，$\\varphi^{(n+1)}$ 至少有一个零点 $\\xi$，且 $L_n^{(n+1)}=0$，$\\left[\\prod(t-x_i)\\right]^{(n+1)}=(n+1)!$：")+
   fml("0=\\varphi^{(n+1)}(\\xi)=f^{(n+1)}(\\xi)-K\\,(n+1)!")+
   p("解得 $K=\\frac{f^{(n+1)}(\\xi)}{(n+1)!}$，代回即得余项公式。"))+
   note(p("误差上界 $|R_n|\\le\\frac{M_{n+1}}{(n+1)!}\\max\\prod|x-x_i|$，其中 $M_{n+1}=\\max|f^{(n+1)}|$。"))
 )},
{"id":"cp1s5-2","name":"龙格现象","tags":["exa","note"],"brief":"等距节点高次插值在区间边缘剧烈振荡。",
 "fig":"runge","figCap":"龙格函数 1/(1+25x²) 的等距高次插值振荡",
 "body": wrap(
   exa(p("<strong>龙格函数：</strong>$f(x)=\\frac{1}{1+25x^2}$，在 $[-1,1]$ 上取等距节点作 $n$ 次插值多项式，随 $n$ 增大误差在端点附近发散。"))+
   der(p("<strong>误差机制：</strong>由余项 $R_n(x)=\\frac{f^{(n+1)}(\\xi)}{(n+1)!}\\prod(x-x_i)$，等距节点时节点乘积 $\\prod|x-x_i|$ 在区间中央小、在端点附近迅速增大，量级约为：")+
   fml("\\max_{x}\\prod_{i=0}^{n}|x-x_i|\\sim\\frac{n!}{4^{n+1}}")+
   p("而龙格函数的高阶导数 $f^{(n+1)}$ 增长极快，两者竞争的结果是边界处误差不收敛，出现剧烈振荡。")+
   p("因此<strong>提高插值次数并不能提高精度</strong>，这就是龙格现象。"))+
   note(p("<strong>对策：</strong>改用分段低次插值（样条）或选用切比雪夫节点集中节点于端点附近。"))
 )},
{"id":"cp1s5-3","name":"切比雪夫节点与收敛性","tags":["der","app"],"brief":"选用切比雪夫节点可最小化最大节点乘积。",
 "body": wrap(
   defn("切比雪夫节点", p("在 $[-1,1]$ 上取")+
   fml("x_k=\\cos\\frac{2k+1}{2n+2}\\pi,\\qquad k=0,\\dots,n"))+
   der(p("<strong>最小零偏差性质：</strong>节点乘积 $\\omega(x)=\\prod(x-x_i)$ 是首项系数为 1 的 $n+1$ 次多项式。切比雪夫多项式 $T_{n+1}$ 的归一化形式在首一多项式类中极大范数最小：")+
   fml("\\min_{a_k}\\max_{x\\in[-1,1]}\\left|x^{n+1}+\\dots\\right|=\\frac{1}{2^{n}}\\max|T_{n+1}(x)|=\\frac{1}{2^{n}}")+
   p("当节点取 $T_{n+1}$ 的零点即切比雪夫节点时达到该下界，故")+
   fml("\\max_x\\left|\\prod_{i=0}^{n}(x-x_i)\\right|=\\frac{1}{2^{n}}")+
   p("相比等距节点的 $\\frac{n!}{4^{n+1}}$ 显著减小，误差随 $n$ 稳定收敛。"))+
   app(p("<strong>应用：</strong>切比雪夫节点用于谱方法、函数逼近与数值积分的节点选取，能在不增加节点数的情况下大幅提高精度。"))
 )},
]},
]
ch2_sections = [
{
"name": "2.1 差商近似与截断误差",
"color": "#7c3aed",
"desc": "用差商近似导数，并通过泰勒展开分析截断误差",
"items": [
{"id":"cp2s1-1","name":"一阶差商与泰勒展开","tags":["def","der"],"brief":"前向差商误差为一阶，源于泰勒展开的截断。",
 "fig":"fwd_diff","figCap":"前向差商用割线斜率近似切线斜率",
 "body": wrap(
   defn("数值微分", p("用函数在离散点上的值近似导数的方法。最基本的形式是前向差商")+
   fml("D^+f(x)=\\frac{f(x+h)-f(x)}{h}"))+
   der(p("<strong>泰勒展开：</strong>将 $f(x+h)$ 在 $x$ 处展开：")+
   fml("f(x+h)=f(x)+hf'(x)+\\frac{h^2}{2}f''(x)+\\frac{h^3}{6}f'''(\\xi)")+
   p("代入前向差商定义：")+
   fml("D^+f(x)=\\frac{f(x+h)-f(x)}{h}=f'(x)+\\frac{h}{2}f''(x)+O(h^2)")+
   p("故截断误差为")+
   fml("E=D^+f(x)-f'(x)=\\frac{h}{2}f''(\\xi)=O(h)"))+
   note(p("前向差商只有一阶精度；类似可得后向差商 $\\frac{f(x)-f(x-h)}{h}=f'(x)-\\frac{h}{2}f''(x)+O(h^2)$，误差同为 $O(h)$。"))
 )},
{"id":"cp2s1-2","name":"中心差商与二阶精度","tags":["der","thm"],"brief":"对称差商消除一阶误差项，达到二阶精度。",
 "fig":"central_diff","figCap":"中心差商以对称的两点消去 O(h) 误差项",
 "body": wrap(
   thm("中心差商公式", p("若 $f$ 充分光滑，则")+
   fml("f'(x)=\\frac{f(x+h)-f(x-h)}{2h}-\\frac{h^2}{6}f'''(\\xi)"))+
   der(p("<strong>泰勒展开相加：</strong>分别展开 $f(x\\pm h)$：")+
   fml("f(x+h)=f(x)+hf'+\\frac{h^2}{2}f''+\\frac{h^3}{6}f'''+O(h^4)")+
   p("以及")+
   fml("f(x-h)=f(x)-hf'+\\frac{h^2}{2}f''-\\frac{h^3}{6}f'''+O(h^4)")+
   p("两式相减，偶数阶项与 $hf'$ 之外的偶次项抵消：")+
   fml("f(x+h)-f(x-h)=2hf'(x)+\\frac{h^3}{3}f'''(x)+O(h^5)")+
   p("两边除以 $2h$ 即得中心差商，截断误差为 $O(h^2)$。"))+
   note(p("中心差商是最常用的数值微分公式，精度比单侧差商高一个数量级。"))
 )},
{"id":"cp2s1-3","name":"二阶导数的差商近似","tags":["der","exa"],"brief":"用三点差分近似二阶导数。",
 "body": wrap(
   der(p("<strong>推导：</strong>将 $f(x\\pm h)$ 的泰勒展开相加，奇数阶项抵消：")+
   fml("f(x+h)+f(x-h)=2f(x)+h^2f''(x)+\\frac{h^4}{12}f^{(4)}(x)+O(h^6)")+
   p("整理得二阶中心差商：")+
   fml("f''(x)=\\frac{f(x+h)-2f(x)+f(x-h)}{h^2}-\\frac{h^2}{12}f^{(4)}(\\xi)")+
   p("截断误差为 $O(h^2)$。"))+
   exa(p("<strong>例：</strong>$f(x)=e^x$，取 $h=0.1$ 在 $x=0$ 处用中心差商估 $f''$：$\\frac{e^{0.1}-2+e^{-0.1}}{0.01}\\approx1.00083$，与真值 1 相差约 $8.3\\times10^{-4}$，与 $\\frac{h^2}{12}$ 量级一致。"))+
   note(p("该格式是求解微分方程边值问题与偏微分方程离散化的基本单元。"))
 )},
]},
{
"name": "2.2 高阶数值微分",
"color": "#8b5cf6",
"desc": "高阶导数差分公式与待定系数法",
"items": [
{"id":"cp2s2-1","name":"待定系数法构造差分公式","tags":["der","thm"],"brief":"用泰勒展开匹配阶数得到任意精度差分。",
 "body": wrap(
   thm("待定系数法", p("设 $f'(x)\\approx\\frac{1}{h}\\sum_{k}a_k f(x+kh)$，通过泰勒展开令低阶误差项系数为零来确定 $a_k$。"))+
   der(p("<strong>以五点公式为例：</strong>取节点 $x-2h,x-h,x,x+h,x+2h$，设")+
   fml("f'(x)\\approx\\frac{a_{-2}f_{-2}+a_{-1}f_{-1}+a_0f_0+a_1f_1+a_2f_2}{h}")+
   p("将各 $f(x+kh)$ 展开并整理 $h^j f^{(j)}(x)$ 的系数，要求 $j=0$ 项为零（消去常数项）、$j=1$ 项系数为 1、$j=2,3,4$ 项为零：")+
   fml("\\sum_k a_k=0,\\quad\\sum_k k a_k=1,\\quad\\sum_k k^j a_k=0\\ (j=2,3,4)")+
   p("解得 $a_1=-a_{-1}=\\frac{8}{12}$，$a_2=-a_{-2}=-\\frac{1}{12}$，于是")+
   fml("f'(x)\\approx\\frac{f_{-2}-8f_{-1}+8f_1-f_2}{12h}+O(h^4)"))+
   note(p("待定系数法通用性强，可构造任意阶精度的差分公式，也可用于非等距节点。"))
 )},
{"id":"cp2s2-2","name":"插值型求导公式","tags":["der","note"],"brief":"对插值多项式求导得到数值微分公式。",
 "body": wrap(
   der(p("<strong>思路：</strong>先构造插值多项式 $L_n(x)$，再用 $L_n'(x)$ 近似 $f'(x)$。由插值余项")+
   fml("f(x)=L_n(x)+\\frac{f^{(n+1)}(\\xi)}{(n+1)!}\\prod_{i=0}^n(x-x_i)")+
   p("两边求导：")+
   fml("f'(x)=L_n'(x)+\\frac{f^{(n+1)}(\\xi)}{(n+1)!}\\frac{d}{dx}\\prod_{i=0}^n(x-x_i)+\\dots")+
   p("在节点处求值时，乘积项导数一般不为零，故插值型求导在节点处的误差阶通常低于插值本身的误差阶。")+
   p("例如两点线性插值求导只能给出一阶精度的差商公式。"))+
   note(p("导数放大高频误差，因此数值微分是不稳定问题：插值精度越高，节点处求导误差未必越好。"))
 )},
{"id":"cp2s2-3","name":"非等距节点的数值微分","tags":["der","app"],"brief":"节点不等距时用差商形式处理。",
 "body": wrap(
   der(p("<strong>三点非等距公式：</strong>设节点 $x_0,x_1,x_2$ 间距 $h_1=x_1-x_0$，$h_2=x_2-x_1$。由二次插值多项式求导可得")+
   fml("f'(x_0)\\approx-\\frac{2h_1+h_2}{h_1(h_1+h_2)}f_0+\\frac{h_1+h_2}{h_1h_2}f_1-\\frac{h_1}{h_2(h_1+h_2)}f_2")+
   p("当 $h_1=h_2=h$ 时退化为标准中心差商。")+
   p("<strong>更实用的写法：</strong>用牛顿差商形式，$f'(x_0)\\approx f[x_0,x_1]+(x_0-x_1)f[x_0,x_1,x_2]$，对任意节点间距都成立。"))+
   app(p("<strong>应用：</strong>实验数据常为不等间隔采样，此时应使用非等距差分或先做局部多项式拟合再求导，以避免插值网格假设带来的系统误差。"))
 )},
]},
{
"name": "2.3 理查森外推",
"color": "#6d28d9",
"desc": "通过不同步长的组合消除低阶误差项",
"items": [
{"id":"cp2s3-1","name":"理查森外推原理","tags":["thm","der"],"brief":"组合两个步长的结果以消去 O(h²) 误差。",
 "fig":"richardson","figCap":"理查森外推使误差阶数逐级提高",
 "body": wrap(
   thm("理查森外推", p("若近似公式具有误差展开 $F(h)=F_0+c_1h^{p_1}+c_2h^{p_2}+\\dots$，则组合不同步长的结果可消去低阶误差项。"))+
   der(p("<strong>推导：</strong>以中心差商为例，其误差为偶数次幂：")+
   fml("D(h)=f'(x)+c_1h^2+c_2h^4+O(h^6)")+
   p("取步长 $h/2$：")+
   fml("D(h/2)=f'(x)+\\frac{c_1}{4}h^2+\\frac{c_2}{16}h^4+O(h^6)")+
   p("用 $4D(h/2)-D(h)$ 消去 $h^2$ 项：")+
   fml("\\frac{4D(h/2)-D(h)}{3}=f'(x)-\\frac{c_2}{4}h^4+O(h^6)")+
   p("误差从 $O(h^2)$ 提高到 $O(h^4)$。"))+
   note(p("一般外推公式为 $R_{k}=R_{k-1}+\\frac{R_{k-1}-R_{k-2}}{2^{p}-1}$，其中 $p$ 为被消去项的次数。"))
 )},
{"id":"cp2s3-2","name":"外推算法与递推表","tags":["der","exa"],"brief":"逐级外推构成三角表。",
 "body": wrap(
   der(p("<strong>递推公式：</strong>记 $T_{k,0}=D(h/2^k)$，则第 $j$ 级外推为")+
   fml("T_{k,j}=\\frac{2^{2j}T_{k,j-1}-T_{k-1,j-1}}{2^{2j}-1},\\qquad j=1,\\dots,k")+
   p("每外推一级消去一个误差项，$T_{k,j}$ 的精度为 $O(h^{2j+2})$。")+
   p("外推表按列从左到右、从上到下计算。"))+
   exa(p("<strong>例：</strong>取 $h=0.1,0.05$ 计算中心差商得 $D(h)=1.0008$，$D(h/2)=1.0002$，外推后")+
   fml("\\frac{4\\times1.0002-1.0008}{3}=1.0000")+
   p("误差由 $8\\times10^{-4}$ 降到毫米级以下，效果显著。"))+
   note(p("外推对舍入误差敏感，步长过小时反而会放大噪声，需配合误差平衡分析。"))
 )},
{"id":"cp2s3-3","name":"理查森外推在数值微分中的应用","tags":["app","der"],"brief":"外推提高数值微分精度并估计误差。",
 "body": wrap(
   der(p("<strong>二阶导数外推：</strong>二阶中心差商误差为")+
   fml("D_2(h)=f''(x)+\\frac{h^2}{12}f^{(4)}(x)+O(h^4)")+
   p("同样可做外推：")+
   fml("\\frac{4D_2(h/2)-D_2(h)}{3}=f''(x)+O(h^4)")+
   p("每做一次外推精度提高两阶。"))+
   app(p("<strong>应用：</strong>理查森外推是龙贝格积分的理论基础，也用于常微分方程数值解的误差估计（如步长加倍法），以及在有限差分中构造高阶紧致格式。"))+
   note(p("外推还可作为误差估计器：$|T_{k,j}-T_{k,j-1}|$ 即可作为精度的实用判据。"))
 )},
]},
{
"name": "2.4 数值微分的误差分析与步长选择",
"color": "#a855f7",
"desc": "截断误差与舍入误差的平衡及最优步长",
"items": [
{"id":"cp2s4-1","name":"截断误差与舍入误差的平衡","tags":["der","note"],"brief":"总误差由截断与舍入两部分组成，存在最优步长。",
 "body": wrap(
   der(p("<strong>总误差分析：</strong>以中心差商为例，截断误差为 $\\frac{h^2}{6}|f'''(x)|$，而计算 $f(x\\pm h)-f(x-h)$ 时的舍入误差约为 $\\frac{\\varepsilon}{h}$（$\\varepsilon$ 为机器精度）。总误差上界为")+
   fml("E(h)\\approx\\frac{h^2}{6}M+\\frac{\\varepsilon}{h}")+
   p("对 $h$ 求导并令其为零：")+
   fml("\\frac{dE}{dh}=\\frac{h}{3}M-\\frac{\\varepsilon}{h^2}=0\\ \\Rightarrow\\ h^*=\\left(\\frac{3\\varepsilon}{M}\\right)^{1/3}")+
   p("此时最小误差量级为 $O(\\varepsilon^{2/3})$，远差于函数求值的机器精度。"))+
   note(p("这表明数值微分是不适定的：无法通过减小步长无限提高精度，必须折中选取步长。"))
 )},
{"id":"cp2s4-2","name":"最优步长的估计","tags":["exa","der"],"brief":"由误差平衡条件给出最优步长公式。",
 "body": wrap(
   exa(p("<strong>例：</strong>双精度 $\\varepsilon\\approx10^{-16}$，$M=|f'''|\\approx1$，则中心差商最优步长")+
   fml("h^*\\approx(3\\times10^{-16})^{1/3}\\approx7\\times10^{-6}")+
   p("此时误差约为 $10^{-11}$ 量级，而理论上截断误差可达 $10^{-16}$，可见舍入误差占主导。"))+
   der(p("<strong>前向差商的对比：</strong>前向差商误差为 $\\frac{h}{2}M+\\frac{2\\varepsilon}{h}$，令导数为零得")+
   fml("h^*=\\sqrt{\\frac{4\\varepsilon}{M}}\\approx2\\times10^{-8}")+
   p("最优误差量级为 $O(\\sqrt{\\varepsilon})\\approx10^{-8}$，明显劣于中心差商的 $O(\\varepsilon^{2/3})$。"))+
   note(p("精度越高（误差阶数 $p$ 越大）的公式，其最优步长越大、可达精度越高。"))
 )},
{"id":"cp2s4-3","name":"噪声数据的微分与正则化","tags":["app","note"],"brief":"实测数据含噪声时需平滑或正则化。",
 "body": wrap(
   der(p("<strong>噪声放大：</strong>设测量值含独立噪声 $\\eta_i$，方差为 $\\sigma^2$，则中心差商的方差为")+
   fml("\\mathrm{Var}(D)=\\frac{1}{4h^2}(\\sigma^2+\\sigma^2)=\\frac{\\sigma^2}{2h^2}")+
   p("噪声标准差被放大为 $\\frac{\\sigma}{\\sqrt{2}h}$，$h$ 越小放大越严重。"))+
   app(p("<strong>处理方法：</strong>先对数据做局部多项式拟合（Savitzky-Golay 平滑），或用 Tikhonov 正则化求解 $\\min\\|Dx-f\\|^2+\\alpha\\|x\\|^2$，在保真与平滑之间折中。"))+
   note(p("实际工程中，数值微分几乎总与平滑滤波联合使用；单纯微分放大噪声是数据处理的常见陷阱。"))
 )},
]},
]
ch3_sections = [
{
"name": "3.1 梯形法与辛普森法",
"color": "#0d9488",
"desc": "从插值出发构造梯形与辛普森求积公式",
"items": [
{"id":"cp3s1-1","name":"梯形公式","tags":["der","def"],"brief":"用一次插值近似被积函数得到梯形面积。",
 "fig":"trapezoid","figCap":"梯形法用折线近似曲线，面积由若干梯形求和",
 "body": wrap(
   defn("插值型求积", p("用插值多项式替代被积函数：$\\int_a^b f(x)\\,dx\\approx\\int_a^b L_n(x)\\,dx$，得到插值型求积公式。"))+
   der(p("<strong>梯形公式推导：</strong>取 $n=1$，节点 $a,b$，线性插值：")+
   fml("L_1(x)=\\frac{x-b}{a-b}f(a)+\\frac{x-a}{b-a}f(b)")+
   p("在 $[a,b]$ 上积分，令 $h=b-a$：")+
   fml("\\int_a^b L_1\\,dx=\\frac{h}{2}\\left[f(a)+f(b)\\right]")+
   p("即梯形公式 $T_1$。其几何意义是以弦代弧，面积为上底加下底乘高除以二。"))+
   der(p("<strong>余项：</strong>由插值余项积分得")+
   fml("E_T=\\int_a^b\\frac{f''(\\xi(x))}{2}(x-a)(x-b)\\,dx=-\\frac{h^3}{12}f''(\\eta)=-\\frac{b-a}{12}h^2f''(\\eta)")+
   p("可见梯形公式对一次多项式精确（$f''=0$），代数精度为 1。"))+
   note(p("梯形公式简单稳健，是龙贝格积分与外推算法的起点。"))
 )},
{"id":"cp3s1-2","name":"辛普森公式","tags":["der","thm"],"brief":"三点抛物线插值积分，代数精度达到 3。",
 "fig":"simpson","figCap":"辛普森法用抛物线弧近似曲线",
 "body": wrap(
   thm("辛普森公式", p("取三点 $x_0=a,x_1=a+h,x_2=a+2h=b$，则")+
   fml("S=\\frac{h}{3}\\left[f(x_0)+4f(x_1)+f(x_2)\\right]"))+
   der(p("<strong>推导：</strong>过三点的二次插值多项式 $L_2$，令 $t=\\frac{x-x_1}{h}$，则 $L_2$ 的积分可写为牛顿-柯特斯形式：")+
   fml("\\int_{x_0}^{x_2}L_2\\,dx=2h\\left[C_0f_0+C_1f_1+C_2f_2\\right]")+
   p("由柯特斯系数公式解得 $C_0=C_2=\\frac{1}{6}$，$C_1=\\frac{2}{3}$，于是")+
   fml("\\int_{x_0}^{x_2}L_2\\,dx=\\frac{h}{3}\\left[f_0+4f_1+f_2\\right]")+
   p("<strong>余项：</strong>由三点插值余项积分（注意 $f^{(4)}$ 为中值）可得")+
   fml("E_S=-\\frac{h^5}{90}f^{(4)}(\\eta)=-\\frac{b-a}{180}h^4f^{(4)}(\\eta)")+
   p("尽管只用了二次插值，辛普森公式对三次多项式也精确，代数精度为 3。"))+
   note(p("辛普森公式精度高、实现简单，是工程中最常用的定积分公式之一。"))
 )},
{"id":"cp3s1-3","name":"复合求积公式","tags":["der","exa"],"brief":"将区间等分后逐段求和以提高精度。",
 "fig":"rect_rule","figCap":"复合求积：将区间细分后在每个子区间应用基本公式",
 "body": wrap(
   der(p("<strong>复合梯形：</strong>把 $[a,b]$ 等分为 $n$ 段，每段用梯形公式并求和，注意内点被计算两次：")+
   fml("T_n=\\frac{h}{2}\\left[f(a)+2\\sum_{i=1}^{n-1}f(x_i)+f(b)\\right]")+
   p("余项为 $E_T=-\\frac{(b-a)}{12}h^2f''(\\eta)=O(h^2)$。")+
   p("<strong>复合辛普森：</strong>要求 $n$ 为偶数，每两段用一次辛普森公式：")+
   fml("S_n=\\frac{h}{3}\\left[f_0+f_n+4\\!\\sum_{i\\text{ 奇}}f_i+2\\!\\sum_{i\\text{ 偶}}f_i\\right]")+
   p("余项 $E_S=-\\frac{(b-a)}{180}h^4f^{(4)}(\\eta)=O(h^4)$。"))+
   exa(p("<strong>例：</strong>计算 $\\int_0^1 e^{-x^2}dx$，取 $n=4$ 的复合辛普森得 $0.746855$，与真值 $0.746824$ 之差约 $3\\times10^{-5}$；加密到 $n=8$ 误差降至约 $2\\times10^{-6}$，符合 $O(h^4)$ 收敛。"))+
   note(p("当被积函数光滑时优先选复合辛普森；若函数只有有限阶导数，则按其光滑度选择相应阶公式。"))
 )},
]},
{
"name": "3.2 牛顿-柯特斯公式",
"color": "#14b8a6",
"desc": "等距节点的插值型求积公式族及其代数精度",
"items": [
{"id":"cp3s2-1","name":"牛顿-柯特斯公式","tags":["def","der"],"brief":"等距节点的插值型求积，权重为柯特斯系数。",
 "fig":"newton_cotes","figCap":"等距节点上的插值型求积权重分布",
 "body": wrap(
   defn("牛顿-柯特斯公式", p("将 $[a,b]$ 等分为 $n$ 段，节点 $x_i=a+ih$，用 $n$ 次插值多项式积分得到")+
   fml("I_n=(b-a)\\sum_{i=0}^{n}C_i^{(n)}f(x_i)"))+
   der(p("<strong>柯特斯系数：</strong>令 $x=a+th$，$t\\in[0,n]$，拉格朗日基函数化为")+
   fml("l_i(x)=\\prod_{j\\neq i}\\frac{t-j}{i-j}")+
   p("于是权重")+
   fml("C_i^{(n)}=\\frac{1}{n}\\int_0^n\\prod_{j\\neq i}\\frac{t-j}{i-j}\\,dt")+
   p("这些系数之和为 1（因常数函数的积分精确），且关于中点对称。"))+
   note(p("$n=1$ 为梯形，$n=2$ 为辛普森，$n=4$ 为柯特斯公式；$n\\ge8$ 时系数出现负值，数值不稳定。"))
 )},
{"id":"cp3s2-2","name":"柯特斯系数与稳定性","tags":["der","note"],"brief":"高阶牛顿-柯特斯公式不稳定。",
 "body": wrap(
   der(p("<strong>系数举例：</strong>由柯特斯系数公式计算：")+
   fml("n=1:\\ \\tfrac{1}{2},\\tfrac{1}{2};\\quad n=2:\\ \\tfrac{1}{6},\\tfrac{2}{3},\\tfrac{1}{6};\\quad n=4:\\ \\tfrac{7}{90},\\tfrac{32}{90},\\tfrac{12}{90},\\tfrac{32}{90},\\tfrac{7}{90}")+
   p("这些系数非负，求和恰为 1，故对称求和稳定。但对于 $n\\ge8$，某些 $C_i^{(n)}$ 变为负值：")+
   fml("\\sum_i|C_i^{(n)}|>1")+
   p("误差传播因子 $\\Lambda=\\sum|C_i|$ 增大，数据的小扰动被放大，故高阶牛顿-柯特斯公式数值不稳定。"))+
   note(p("实际中只用 $n\\le4$ 的低阶公式，或采用<strong>复合</strong>低阶公式以兼顾精度与稳定。"))
 )},
{"id":"cp3s2-3","name":"代数精度","tags":["def","der"],"brief":"求积公式精确成立的多项式最高次数。",
 "body": wrap(
   defn("代数精度", p("若求积公式对所有次数不超过 $m$ 的多项式精确成立，而对某个 $m+1$ 次多项式不精确，则称其代数精度为 $m$。"))+
   der(p("<strong>判定：</strong>牛顿-柯特斯公式由 $n$ 次插值构造，至少对 $n$ 次多项式精确（$R\\equiv0$），故代数精度 $\\ge n$。")+
   p("当 $n$ 为偶数时结论更强：由余项 $E=C h^{n+3}f^{(n+2)}(\\eta)$，因奇数次导数的对称积分抵消，代数精度提高到 $n+1$。")+
   fml("n\\ \\text{偶}:\\ m=n+1;\\qquad n\\ \\text{奇}:\\ m=n")+
   p("例如辛普森（$n=2$）精度为 3，柯特斯（$n=4$）精度为 5，而梯形（$n=1$）精度为 1。"))+
   note(p("高斯求积通过放弃等距条件，用 $n$ 个节点达到 $2n-1$ 次代数精度，是精度最优的方案。"))
 )},
]},
{
"name": "3.3 龙贝格积分",
"color": "#0f766e",
"desc": "以梯形公式为基础，经理查森外推得到高阶积分公式",
"items": [
{"id":"cp3s3-1","name":"龙贝格算法原理","tags":["der","thm"],"brief":"梯形序列的误差为 h² 的偶次幂，可逐级外推。",
 "fig":"romberg","figCap":"龙贝格三角表：逐列 Richardson 外推",
 "body": wrap(
   thm("欧拉-麦克劳林展开", p("复合梯形公式的误差可按 $h$ 的偶次幂展开：")+
   fml("T(h)=I+c_1h^2+c_2h^4+c_3h^6+\\dots"))+
   der(p("<strong>递推构造：</strong>记 $R_{k,0}=T(h/2^k)$。由于误差仅含 $h^2,h^4,\\dots$ 项，按理查森外推消去 $h^2$ 项：")+
   fml("R_{k,1}=\\frac{4R_{k,0}-R_{k-1,0}}{3}")+
   p("继续消去 $h^4$ 项：")+
   fml("R_{k,j}=\\frac{4^jR_{k,j-1}-R_{k-1,j-1}}{4^j-1}")+
   p("每外推一级精度提高两阶，$R_{k,j}$ 的误差为 $O(h^{2j+2})$。"))+
   note(p("龙贝格积分只需计算梯形序列，其余由递推得到，实现极为简洁。"))
 )},
{"id":"cp3s3-2","name":"龙贝格递推表与计算","tags":["exa","der"],"brief":"按三角表逐列计算积分近似值。",
 "body": wrap(
   exa(p("<strong>例：</strong>用龙贝格法计算 $\\int_0^1\\frac{4}{1+x^2}dx=\\pi$。")+
   fml("R_{0,0}=T(1)=3.0,\\quad R_{1,0}=T(1/2)=3.1,\\quad R_{2,0}=T(1/4)=3.131176"))+
   der(p("<strong>逐列外推：</strong>第一列外推：")+
   fml("R_{1,1}=\\frac{4\\times3.1-3.0}{3}=3.133333,\\quad R_{2,1}=\\frac{4\\times3.131176-3.1}{3}=3.141569")+
   p("第二列外推：")+
   fml("R_{2,2}=\\frac{16\\times3.141569-3.133333}{15}=3.141593")+
   p("$R_{2,2}$ 已达 $3.141593$，与 $\\pi=3.14159265$ 吻合到小数点后 6 位，而原始梯形值只有 3 位有效数字。"))+
   note(p("<strong>停止准则：</strong>当 $|R_{k,k}-R_{k-1,k-1}|<\\varepsilon$ 时停止，通常取相邻对角元素之差作为误差估计。"))
 )},
{"id":"cp3s3-3","name":"龙贝格积分的收敛性","tags":["der","note"],"brief":"对角序列快速收敛，且可作误差估计。",
 "body": wrap(
   der(p("<strong>收敛速度：</strong>对充分光滑的函数，龙贝格对角元素 $R_{k,k}$ 的误差为 $O(h^{2k+2})=O(4^{-(k+1)})$，即每增加一行，有效位数约翻倍。")+
   fml("|R_{k,k}-I|\\le C\\,4^{-k}")+
   p("因此通常迭代几行即可达到机器精度。")+
   p("<strong>误差估计：</strong>由外推结构，相邻对角元素之差可作为误差判据：")+
   fml("|R_{k,k}-I|\\approx\\frac{1}{4^{k}-1}|R_{k,k}-R_{k,k-1}|"))+
   note(p("龙贝格法要求 $f$ 有足够阶连续导数；对奇异积分或被积函数不光滑的情形会退化，应改用自适应或高斯方法。"))
 )},
]},
{
"name": "3.4 高斯求积",
"color": "#059669",
"desc": "节点与权重自由选取的最优代数精度求积方法",
"items": [
{"id":"cp3s4-1","name":"高斯求积的思想","tags":["def","der"],"brief":"通过自由选节点使代数精度达到 2n−1。",
 "fig":"gauss_quad","figCap":"高斯节点位于区间内部，2 点公式即可精确积分三次多项式",
 "body": wrap(
   defn("高斯求积", p("形如 $\\int_{-1}^{1}f(x)dx\\approx\\sum_{i=1}^{n}w_if(x_i)$ 的公式，节点 $x_i$ 与权重 $w_i$ 都待定，共 $2n$ 个自由度。"))+
   der(p("<strong>代数精度的极限：</strong>要求公式对 $1,x,\\dots,x^{2n-1}$ 精确，得到 $2n$ 个方程：")+
   fml("\\sum_{i=1}^n w_ix_i^k=\\int_{-1}^{1}x^k\\,dx=\\begin{cases}\\frac{2}{k+1},&k\\ \\text{偶}\\\\0,&k\\ \\text{奇}\\end{cases}")+
   p("可解出节点与权重，且代数精度达到 $2n-1$，这是 $n$ 点求积的精度上限（再高则需增加节点）。")+
   p("<strong>正交多项式观点：</strong>可证明最优节点恰为 $n$ 次勒让德多项式 $P_n$ 的零点。"))+
   note(p("高斯公式不使用端点，对端点奇异的积分（如 $\\int_0^1 x^{-1/2}dx$）常配合变换使用。"))
 )},
{"id":"cp3s4-2","name":"高斯-勒让德节点与权重","tags":["der","exa"],"brief":"两点与三点高斯-勒让德公式。",
 "body": wrap(
   der(p("<strong>两点公式：</strong>设对称节点 $\\pm a$，权重 $w$（对称性使两权重相等）。由 $k=0$：")+
   fml("2w=2\\Rightarrow w=1")+
   p("由 $k=2$：")+
   fml("2wa^2=\\frac{2}{3}\\Rightarrow a^2=\\frac{1}{3}\\Rightarrow a=\\frac{1}{\\sqrt{3}}")+
   p("故两点公式为")+
   fml("\\int_{-1}^1f(x)dx\\approx f\\!\\left(-\\tfrac{1}{\\sqrt{3}}\\right)+f\\!\\left(\\tfrac{1}{\\sqrt{3}}\\right)")+
   p("代数精度为 3。"))+
   exa(p("<strong>三点公式：</strong>节点 $0,\\pm\\sqrt{3/5}$，权重 $\\frac{8}{9},\\frac{5}{9},\\frac{5}{9}$，对 5 次多项式精确。"))+
   note(p("一般区间 $[a,b]$ 作变量替换 $x=\\frac{b-a}{2}t+\\frac{a+b}{2}$，$dx=\\frac{b-a}{2}dt$ 即可直接套用。"))
 )},
{"id":"cp3s4-3","name":"高斯求积的误差与应用","tags":["der","app"],"brief":"误差公式与常见变体。",
 "body": wrap(
   der(p("<strong>误差公式：</strong>$n$ 点高斯-勒让德公式的余项为")+
   fml("E_n=\\frac{2^{2n+1}(n!)^4}{(2n+1)[(2n)!]^3}f^{(2n)}(\\eta)")+
   p("与牛顿-柯特斯不同，当 $f\\in C^\\infty$ 时误差随 $n$ 指数下降（几何收敛），收敛极快。")+
   p("<strong>变体：</strong>带权积分 $\\int w(x)f(x)dx$ 可选用相应正交多项式零点：切比雪夫零点对应 $w=1/\\sqrt{1-x^2}$，拉盖尔对应 $e^{-x}$，埃尔米特对应 $e^{-x^2}$。"))+
   app(p("<strong>应用：</strong>高斯求积广泛用于有限元单元积分、谱方法、粒子物理蒙特卡洛前的确定性积分，以及任何需要高精度定积分的场景。"))
 )},
]},
{
"name": "3.5 蒙特卡洛积分",
"color": "#10b981",
"desc": "基于随机抽样的积分方法，适用于高维与复杂区域",
"items": [
{"id":"cp3s5-1","name":"随机抽样与期望","tags":["def","der"],"brief":"用样本均值估计积分值。",
 "fig":"monte_carlo","figCap":"蒙特卡洛：在区域中随机投点估计面积（积分）",
 "body": wrap(
   defn("蒙特卡洛积分", p("设 $X$ 在 $[a,b]$ 上均匀分布，则")+
   fml("I=\\int_a^bf(x)dx=(b-a)\\,\\mathbb{E}[f(X)]"))+
   der(p("<strong>估计量：</strong>抽取 $N$ 个独立均匀样本 $x_i$，用样本均值代替期望：")+
   fml("\\hat{I}_N=\\frac{b-a}{N}\\sum_{i=1}^{N}f(x_i)")+
   p("由大数定律 $\\hat{I}_N\\to I$（依概率 1）。该估计是无偏的，因为")+
   fml("\\mathbb{E}[\\hat{I}_N]=\\frac{b-a}{N}\\cdot N\\,\\mathbb{E}[f]=(b-a)\\mathbb{E}[f]=I"))+
   note(p("蒙特卡洛方法对维数不敏感，是求解高维积分的首选方法。"))
 )},
{"id":"cp3s5-2","name":"蒙特卡洛误差估计","tags":["der","exa"],"brief":"误差按 N^(−1/2) 收敛，与维数无关。",
 "fig":"monte_carlo_pi","figCap":"用随机投点估计 π：落入圆内的比例近似 π/4",
 "body": wrap(
   der(p("<strong>方差：</strong>由独立同分布，估计量方差为")+
   fml("\\mathrm{Var}(\\hat{I}_N)=\\frac{(b-a)^2}{N}\\sigma_f^2,\\qquad \\sigma_f^2=\\mathrm{Var}(f(X))")+
   p("标准差即误差量级：")+
   fml("\\sigma_{\\hat{I}}=\\frac{(b-a)\\sigma_f}{\\sqrt{N}}=O(N^{-1/2})"))+
   exa(p("<strong>例（估计 π）：</strong>在单位正方形随机投点，命中四分之一圆的比例 $p$ 满足 $p=\\frac{\\pi}{4}$，故 $\\pi\\approx4\\frac{N_{\\text{内}}}{N}$。投 $10^6$ 个点，误差约为 $\\frac{1.6}{\\sqrt{10^6}}\\approx1.6\\times10^{-3}$。"))+
   note(p("误差 $O(N^{-1/2})$ 收敛慢，但<strong>与维数无关</strong>：一维与一百维的收敛率相同，这正是它适合高维的原因。"))
 )},
{"id":"cp3s5-3","name":"方差缩减方法","tags":["app","der"],"brief":"通过抽样技巧降低方差以提高效率。",
 "body": wrap(
   der(p("<strong>重要性抽样：</strong>若被积函数在某个区域贡献大，可按密度 $p(x)$ 抽样并用")+
   fml("I=\\int\\frac{f(x)}{p(x)}p(x)dx\\approx\\frac{1}{N}\\sum_i\\frac{f(x_i)}{p(x_i)},\\quad x_i\\sim p")+
   p("选取 $p\\propto|f|$ 可使方差显著减小。<strong>对偶变量法</strong>利用 $f(x)+f(1-x)$ 的负相关降低方差；<strong>分层抽样</strong>把区域切分为若干层分别抽样。")+
   p("<strong>控制变量法：</strong>用已知均值的 $g$ 修正：$\\hat{I}=\\overline{f-\\beta(g-\\mathbb{E}g)}$，最优 $\\beta=\\mathrm{Cov}(f,g)/\\mathrm{Var}(g)$。"))+
   app(p("<strong>应用：</strong>蒙特卡洛用于高维数值积分、统计物理中的配分函数计算、金融衍生品定价与粒子输运模拟，方差缩减是其实用化的关键。"))
 )},
]},
]
ch4_sections = [
{
"name": "4.1 二分法",
"color": "#c2410c",
"desc": "基于介值定理的区间收缩方法，稳健但收敛慢",
"items": [
{"id":"cp4s1-1","name":"介值定理与二分法","tags":["def","der"],"brief":"利用连续函数变号性质，逐次对分区间。",
 "fig":"bisection","figCap":"二分法：每次取中点，保留含根的子区间",
 "body": wrap(
   defn("二分法", p("设 $f$ 在 $[a,b]$ 上连续且 $f(a)f(b)<0$，由介值定理 $(a,b)$ 内至少有一个根。取中点 $c=\\frac{a+b}{2}$，保留含根的一半区间并迭代。"))+
   der(p("<strong>迭代格式：</strong>")+
   fml("c_k=\\frac{a_k+b_k}{2},\\quad [a_{k+1},b_{k+1}]=\\begin{cases}[a_k,c_k],&f(a_k)f(c_k)<0\\\\ [c_k,b_k],&f(a_k)f(c_k)>0\\end{cases}")+
   p("每步区间长度减半：")+
   fml("b_{k+1}-a_{k+1}=\\frac{b_k-a_k}{2}=\\frac{b_0-a_0}{2^{k+1}}")+
   p("迭代 $n$ 次后，中点与真根的距离不超过区间半长。"))+
   note(p("二分法只要求连续性，不需要导数，因此对病态函数仍然收敛，是最可靠的兜底方法。"))
 )},
{"id":"cp4s1-2","name":"二分法误差界与收敛速度","tags":["thm","der"],"brief":"线性收敛，误差按 1/2 递减。",
 "fig":"convergence_order","figCap":"不同方法的误差衰减：线性、超线性与二次收敛",
 "body": wrap(
   thm("误差估计", p("第 $n$ 次迭代的近似根 $x_n$ 满足")+
   fml("|x_n-x^*|\\le\\frac{b-a}{2^{n+1}}"))+
   der(p("<strong>推导：</strong>每一步区间长度均为上一次的一半，真根始终在区间内，故误差不超过区间长：")+
   fml("|x_n-x^*|\\le\\frac{b_n-a_n}{2}=\\frac{b-a}{2^{n+1}}")+
   p("若要求精度 $\\varepsilon$，所需迭代次数为")+
   fml("n\\ge\\log_2\\frac{b-a}{\\varepsilon}")+
   p("例如 $\\frac{b-a}{\\varepsilon}=10^6$ 时需 $n\\ge20$ 次迭代。")+
   p("<strong>收敛阶：</strong>误差序列 $e_{n+1}\\approx\\frac{1}{2}e_n$，为线性收敛，收敛阶 $p=1$，收敛常数为 $1/2$。"))+
   exa(p("<strong>例：</strong>$[0,1]$ 上求根，精度 $10^{-6}$，需 $n\\approx\\log_2 10^6\\approx20$ 次迭代。"))+
   note(p("收敛速度慢是二分法的主要缺点，实际常先用二分法定位，再用牛顿法快速精化。"))
 )},
{"id":"cp4s1-3","name":"二分法的实现与局限","tags":["app","note"],"brief":"实现要点与适用场景。",
 "body": wrap(
   der(p("<strong>终止准则：</strong>可选用三种之一：区间长度 $b-a<\\varepsilon$；函数值 $|f(c)|<\\varepsilon$；或相对误差 $\\frac{b-a}{\\max(1,|c|)}<\\varepsilon$。")+
   p("注意只凭 $|f(c)|<\\varepsilon$ 判断有时会误判（函数在小邻域内变化极缓），宜结合区间长度判据。"))+
   app(p("<strong>应用：</strong>二分法用于初值定位、根的存在性验证、以及牛顿法失效时的安全回退（如 Brent 方法将二分与割线/反二次插值结合，兼具速度与可靠性）。"))+
   note(p("二分法无法求偶重根（$f$ 不变号）；此时可对 $f'(x)=0$ 作二分，或用 $f(x)/f'(x)$ 变换。"))
 )},
]},
{
"name": "4.2 不动点迭代与收敛性",
"color": "#ea580c",
"desc": "将方程改写为不动点形式，用压缩映射分析收敛",
"items": [
{"id":"cp4s2-1","name":"不动点迭代格式","tags":["def","der"],"brief":"把 f(x)=0 改写成 x=g(x) 后迭代。",
 "fig":"fixed_point","figCap":"不动点迭代的蛛网图：g 与直线 y=x 的交点为不动点",
 "body": wrap(
   defn("不动点迭代", p("把 $f(x)=0$ 改写为等价形式 $x=g(x)$，构造迭代 $x_{k+1}=g(x_k)$。若 $x^*=g(x^*)$，则 $x^*$ 称为 $g$ 的不动点，也是 $f$ 的根。"))+
   der(p("<strong>收敛性直观：</strong>迭代误差")+
   fml("e_{k+1}=x_{k+1}-x^*=g(x_k)-g(x^*)=g'(\\xi_k)(x_k-x^*)")+
   p("由中值定理，$\\xi_k$ 介于 $x_k$ 与 $x^*$ 之间。若 $|g'(x)|\\le L<1$，则")+
   fml("|e_{k+1}|\\le L|e_k|")+
   p("误差按公比 $L$ 线性下降，故 $g$ 为压缩映射时迭代收敛。"))+
   note(p("改写形式不唯一：例如 $x^2-2=0$ 可写为 $g(x)=\\frac{1}{2}(x+\\frac{2}{x})$（收敛）或 $g(x)=2/x$（不收敛），故需检验 $|g'|<1$。"))
 )},
{"id":"cp4s2-2","name":"压缩映射定理","tags":["thm","der"],"brief":"压缩映射存在唯一不动点且迭代收敛。",
 "body": wrap(
   thm("压缩映射原理", p("若 $g$ 把闭区间 $[a,b]$ 映到自身，且存在 $L<1$ 使对一切 $x,y\\in[a,b]$ 有 $|g(x)-g(y)|\\le L|x-y|$，则 $g$ 在 $[a,b]$ 上存在唯一不动点 $x^*$，且对任意初值迭代 $x_{k+1}=g(x_k)$ 收敛到 $x^*$。"))+
   der(p("<strong>收敛性证明：</strong>由压缩性递推：")+
   fml("|x_{k+1}-x_k|=|g(x_k)-g(x_{k-1})|\\le L|x_k-x_{k-1}|\\le\\dots\\le L^k|x_1-x_0|")+
   p("对任意 $m>n$，由三角不等式与几何级数求和：")+
   fml("|x_m-x_n|\\le\\sum_{i=n}^{m-1}L^i|x_1-x_0|\\le\\frac{L^n}{1-L}|x_1-x_0|")+
   p("因 $L<1$，右端随 $n\\to\\infty$ 趋于零，故 $\\{x_k\\}$ 为柯西列，在闭区间内收敛到 $x^*$。")+
   p("唯一性：若有两个不动点 $x^*,y^*$，则 $|x^*-y^*|=|g(x^*)-g(y^*)||\\le L|x^*-y^*|$，因 $L<1$ 只能 $x^*=y^*$。"))+
   note(p("误差估计 $|x_k-x^*|\\le\\frac{L}{1-L}|x_k-x_{k-1}|$，可直接用于编程中的停止判据。"))
 )},
{"id":"cp4s2-3","name":"局部收敛与收敛阶","tags":["der","exa"],"brief":"g'(x*)≠0 时线性收敛，g'(x*)=0 时更高阶。",
 "body": wrap(
   der(p("<strong>局部收敛定理：</strong>若 $g$ 在不动点 $x^*$ 附近连续可微，则 $|g'(x^*)|<1$ 时局部收敛；$|g'(x^*)|>1$ 时发散。")+
   p("<strong>收敛阶：</strong>若 $g'(x^*)\\neq0$，则 $e_{k+1}\\approx g'(x^*)e_k$，线性收敛。")+
   p("若 $g'(x^*)=0$ 而 $g''(x^*)\\neq0$，则")+
   fml("e_{k+1}=\\frac{g''(x^*)}{2}e_k^2+O(e_k^3)")+
   p("为二次收敛。例如把 $x=g(x)$ 改为牛顿形式 $g(x)=x-\\frac{f(x)}{f'(x)}$ 恰好使 $g'(x^*)=0$。"))+
   exa(p("<strong>例：</strong>解 $x=e^{-x}$，取 $g(x)=e^{-x}$，$|g'(x^*)|=|e^{-x^*}|=x^*\\approx0.567<1$，迭代收敛；而 $g(x)=-\\ln x$ 的 $|g'|=1/x^*\\approx1.76>1$，迭代发散。"))+
   note(p("构造迭代格式时应尽量使 $g'(x^*)$ 接近零，以加快收敛。"))
 )},
]},
{
"name": "4.3 牛顿迭代法",
"color": "#f97316",
"desc": "利用切线线性化的二次收敛方法",
"items": [
{"id":"cp4s3-1","name":"牛顿迭代公式","tags":["thm","der"],"brief":"用切线零点作为下一次近似。",
 "fig":"newton_root","figCap":"牛顿法：从 x0 出发沿切线逼近根",
 "body": wrap(
   thm("牛顿迭代公式", p("设 $f$ 可微，$f'(x_k)\\neq0$，则")+
   fml("x_{k+1}=x_k-\\frac{f(x_k)}{f'(x_k)}"))+
   der(p("<strong>推导：</strong>在当前近似 $x_k$ 处作泰勒展开并保留线性项：")+
   fml("f(x)\\approx f(x_k)+f'(x_k)(x-x_k)")+
   p("令线性化函数为零，解出 $x$：")+
   fml("0=f(x_k)+f'(x_k)(x-x_k)\\ \\Rightarrow\\ x=x_k-\\frac{f(x_k)}{f'(x_k)}")+
   p("把该 $x$ 作为下一次近似 $x_{k+1}$ 即得牛顿迭代公式；几何上是切线与 $x$ 轴交点的横坐标。"))+
   note(p("牛顿法也可由不动点迭代 $g(x)=x-\\frac{f}{f'}$ 导出，其 $g'(x^*)=0$ 正是二次收敛的来源。"))
 )},
{"id":"cp4s3-2","name":"牛顿法的二次收敛性","tags":["thm","der"],"brief":"误差按平方衰减，收敛极快。",
 "body": wrap(
   thm("二次收敛定理", p("若 $f$ 二阶连续可微，$f(x^*)=0$，$f'(x^*)\\neq0$，则牛顿法在 $x^*$ 附近二次收敛，且")+
   fml("e_{k+1}=\\frac{f''(x^*)}{2f'(x^*)}e_k^2+O(e_k^3)"))+
   der(p("<strong>推导：</strong>由泰勒展开 $f(x^*)=0$：")+
   fml("0=f(x_k)+f'(x_k)(x^*-x_k)+\\frac{f''(\\xi)}{2}(x^*-x_k)^2")+
   p("即")+
   fml("x^*-x_k=-\\frac{f(x_k)}{f'(x_k)}-\\frac{f''(\\xi)}{2f'(x_k)}(x^*-x_k)^2")+
   p("两边减去 $\\frac{f(x_k)}{f'(x_k)}$ 并注意 $x_{k+1}=x_k-\\frac{f(x_k)}{f'(x_k)}$：")+
   fml("e_{k+1}=\\frac{f''(\\xi)}{2f'(x_k)}e_k^2")+
   p("当 $x_k\\to x^*$ 时系数趋于 $\\frac{f''(x^*)}{2f'(x^*)}$，故误差按平方衰减。"))+
   note(p("由 $e_{k+1}\\approx Ce_k^2$ 可知：当 $e_k<0.1$ 时，下一次误差约为 $0.01C$，有效位数近似翻倍。"))
 )},
{"id":"cp4s3-3","name":"牛顿法的收敛条件与变形","tags":["der","app"],"brief":"初值选取、重根处理与阻尼牛顿法。",
 "body": wrap(
   der(p("<strong>收敛条件：</strong>牛顿法只是局部收敛：要求初值 $x_0$ 足够接近根，且 $f'(x^*)\\neq0$。若 $f'(x^*)=0$（重根），收敛降为线性，此时改用")+
   fml("x_{k+1}=x_k-m\\frac{f(x_k)}{f'(x_k)}")+
   p("（$m$ 为根的重数）可恢复二次收敛。")+
   p("<strong>阻尼牛顿法：</strong>为扩大收敛域，取步长 $\\lambda_k\\in(0,1]$：")+
   fml("x_{k+1}=x_k-\\lambda_k\\frac{f(x_k)}{f'(x_k)}")+
   p("用线搜索确保 $|f(x_{k+1})|<|f(x_k)|$，可显著增强全局收敛性。"))+
   app(p("<strong>应用：</strong>牛顿法广泛用于求解非线性方程、优化问题（$\\nabla f=0$）、幂流计算，并与拟牛顿法结合处理大规模问题。"))
 )},
]},
{
"name": "4.4 割线法与抛物线法",
"color": "#9a3412",
"desc": "不求导数的高效迭代方法",
"items": [
{"id":"cp4s4-1","name":"割线法","tags":["der","thm"],"brief":"用两点割线代替切线，免去导数计算。",
 "fig":"secant","figCap":"割线法：用两点的割线零点作为新近似",
 "body": wrap(
   thm("割线法迭代", p("用差商 $\\frac{f(x_k)-f(x_{k-1})}{x_k-x_{k-1}}$ 近似 $f'(x_k)$，得")+
   fml("x_{k+1}=x_k-\\frac{f(x_k)(x_k-x_{k-1})}{f(x_k)-f(x_{k-1})}"))+
   der(p("<strong>推导：</strong>过两点 $(x_{k-1},f_{k-1})$、$(x_k,f_k)$ 作割线，其方程为零：")+
   fml("f_k+\\frac{f_k-f_{k-1}}{x_k-x_{k-1}}(x-x_k)=0")+
   p("解出 $x$ 并把该零点作为 $x_{k+1}$，即得割线法公式。它可看作牛顿法用差商替代导数的离散版本。"))+
   note(p("割线法每步只算一次函数值（复用上一步），效率高于牛顿法（需同时算 $f$ 与 $f'$）。"))
 )},
{"id":"cp4s4-2","name":"割线法的收敛阶","tags":["der","exa"],"brief":"收敛阶为黄金比例 1.618，属超线性收敛。",
 "body": wrap(
   der(p("<strong>收敛阶：</strong>设误差 $e_k$，可证割线法满足")+
   fml("e_{k+1}=C\\,e_k e_{k-1}")+
   p("设 $e_{k+1}\\sim e_k^{p}$，则 $e_k e_{k-1}\\sim e_k^{1+1/p}$，于是")+
   fml("p=1+\\frac{1}{p}\\ \\Rightarrow\\ p^2-p-1=0\\ \\Rightarrow\\ p=\\frac{1+\\sqrt{5}}{2}\\approx1.618")+
   p("即黄金比例，属超线性收敛，快于线性（二分法）而慢于二次（牛顿法）。")+
   p("<strong>效率比较：</strong>每步计算量上割线法只求 1 次函数值，牛顿法求 1 次函数值加 1 次导数值，故割线法的「效率指数」约为 $1.618$，通常优于牛顿法。"))+
   exa(p("<strong>例：</strong>解 $x^3-x-1=0$，取 $x_0=1,x_1=2$，迭代 5 步即得 $1.324718$，与真根相差不足 $10^{-6}$。"))+
   note(p("割线法仍需两个好的初值，且可能在迭代中因分母过小而失稳，实际常加保护。"))
 )},
{"id":"cp4s4-3","name":"抛物线法","tags":["der","app"],"brief":"用二次插值（Muller 法）逼近根，可求复根。",
 "body": wrap(
   der(p("<strong>Muller 法：</strong>过最近三点作二次插值多项式，取其靠近当前点的零点作为新近似。由二次方程 $a\\tau^2+b\\tau+c=0$（$\\tau=x-x_k$）解得")+
   fml("x_{k+1}=x_k-\\frac{2c}{b\\pm\\sqrt{b^2-4ac}}")+
   p("其中 $a,b,c$ 由三点差分表达，符号选取使分母绝对值较大以保证稳定。")+
   p("<strong>收敛阶：</strong>Muller 法收敛阶约为 $1.84$，高于割线法，且因二次方程可有复根，故能<strong>求复根</strong>。"))+
   app(p("<strong>应用：</strong>抛物线法用于多项式求根（可与降阶法配合逐个求出全部根），在数值线性代数中求特征多项式的根也有应用。"))
 )},
]},
{
"name": "4.5 非线性方程组的迭代法",
"color": "#d97706",
"desc": "把牛顿法推广到多维方程组",
"items": [
{"id":"cp4s5-1","name":"非线性方程组与雅可比矩阵","tags":["def","der"],"brief":"多变量牛顿法用雅可比矩阵做线性化。",
 "fig":"newton_system","figCap":"两个非线性方程对应曲线的交点即方程组的解",
 "body": wrap(
   defn("非线性方程组", p("求解 $\\mathbf{F}(\\mathbf{x})=\\mathbf{0}$，其中 $\\mathbf{F}=(f_1,\\dots,f_n)^{\\top}$，$\\mathbf{x}=(x_1,\\dots,x_n)^{\\top}$。"))+
   der(p("<strong>多元泰勒展开：</strong>在 $\\mathbf{x}^{(k)}$ 处展开，保留一阶项：")+
   fml("\\mathbf{F}(\\mathbf{x})\\approx\\mathbf{F}(\\mathbf{x}^{(k)})+J(\\mathbf{x}^{(k)})(\\mathbf{x}-\\mathbf{x}^{(k)})")+
   p("其中雅可比矩阵")+
   fml("J=\\begin{pmatrix}\\frac{\\partial f_1}{\\partial x_1}&\\cdots&\\frac{\\partial f_1}{\\partial x_n}\\\\ \\vdots&&\\vdots\\\\ \\frac{\\partial f_n}{\\partial x_1}&\\cdots&\\frac{\\partial f_n}{\\partial x_n}\\end{pmatrix}")+
   p("令线性化模型为零即得迭代格式，可见多维牛顿法是一维公式的自然推广。"))+
   note(p("雅可比矩阵刻画了方程组在一点处的局部线性行为，是判断解的存在性与收敛性的核心工具。"))
 )},
{"id":"cp4s5-2","name":"牛顿迭代法解方程组","tags":["der","exa"],"brief":"每步解一个线性方程组。",
 "body": wrap(
   der(p("<strong>迭代格式：</strong>令 $\\mathbf{F}(\\mathbf{x}^{(k)})+J(\\mathbf{x}^{(k)})(\\mathbf{x}^{(k+1)}-\\mathbf{x}^{(k)})=\\mathbf{0}$，得")+
   fml("\\mathbf{x}^{(k+1)}=\\mathbf{x}^{(k)}-J^{-1}(\\mathbf{x}^{(k)})\\mathbf{F}(\\mathbf{x}^{(k)})")+
   p("实际计算中不显式求逆，而是解线性方程组")+
   fml("J(\\mathbf{x}^{(k)})\\Delta\\mathbf{x}^{(k)}=-\\mathbf{F}(\\mathbf{x}^{(k)}),\\qquad \\mathbf{x}^{(k+1)}=\\mathbf{x}^{(k)}+\\Delta\\mathbf{x}^{(k)}")+
   p("可用 LU 分解求解，每步代价为 $O(n^3)$。")+
   p("<strong>收敛性：</strong>在多变量情形同样可证二次收敛（要求 $J(\\mathbf{x}^*)$ 非奇异）。"))+
   exa(p("<strong>例：</strong>解 $\\begin{cases}x^2+y^2=4\\\\ xy=1\\end{cases}$，取初值 $(1,1)$，两三次迭代即收敛到 $(x,y)\\approx(1.93,0.518)$。"))+
   note(p("多维牛顿法对初值敏感，需要好的初始猜测，常与阻尼或信赖域方法结合。"))
 )},
{"id":"cp4s5-3","name":"拟牛顿法与简化","tags":["app","der"],"brief":"避免每步重算雅可比与分解。",
 "body": wrap(
   der(p("<strong>简化牛顿法：</strong>固定迭代矩阵 $J(\\mathbf{x}^{(0)})$ 不变，则只需一次 LU 分解，每步代价降为 $O(n^2)$，但收敛降为线性：")+
   fml("\\mathbf{x}^{(k+1)}=\\mathbf{x}^{(k)}-J^{-1}(\\mathbf{x}^{(0)})\\mathbf{F}(\\mathbf{x}^{(k)})")+
   p("<strong>拟牛顿思想：</strong>用低秩修正逐步逼近雅可比（或其逆），如 Broyden 公式")+
   fml("B_{k+1}=B_k+\\frac{(\\mathbf{y}_k-B_k\\mathbf{s}_k)\\mathbf{s}_k^{\\top}}{\\mathbf{s}_k^{\\top}\\mathbf{s}_k}")+
   p("其中 $\\mathbf{s}_k=\\mathbf{x}^{(k+1)}-\\mathbf{x}^{(k)}$，$\\mathbf{y}_k=\\mathbf{F}(\\mathbf{x}^{(k+1)})-\\mathbf{F}(\\mathbf{x}^{(k)})$，保持超线性收敛且避免重新求导。"))+
   app(p("<strong>应用：</strong>拟牛顿法是大规模非线性方程组与无约束优化的主流方法（L-BFGS），在机器学习参数估计、结构分析与电路仿真中广泛使用。"))
 )},
]},
]
ch5_sections = [
{
"name": "5.1 高斯消元与LU分解",
"color": "#be185d",
"desc": "直接法求解线性方程组：消元、LU 分解与主元选取",
"items": [
{"id":"cp5s1-1","name":"高斯消元法","tags":["def","der"],"brief":"通过行变换把方程组化为上三角后回代求解。",
 "body": wrap(
   defn("高斯消元法", p("对线性方程组 $A\\mathbf{x}=\\mathbf{b}$ 作初等行变换，把 $A$ 化为上三角矩阵，再自下而上回代求解。"))+
   der(p("<strong>消元过程：</strong>第 $k$ 步用主元 $a_{kk}^{(k)}$ 消去其下方元素，乘子为")+
   fml("m_{ik}=\\frac{a_{ik}^{(k)}}{a_{kk}^{(k)}},\\qquad a_{ij}^{(k+1)}=a_{ij}^{(k)}-m_{ik}a_{kj}^{(k)}")+
   p("右端项同步更新 $b_i^{(k+1)}=b_i^{(k)}-m_{ik}b_k^{(k)}$。经 $n-1$ 步后得到上三角方程组。")+
   p("<strong>回代：</strong>")+
   fml("x_i=\\frac{1}{a_{ii}}\\left(b_i-\\sum_{j=i+1}^{n}a_{ij}x_j\\right),\\qquad i=n,\\dots,1"))+
   note(p("消元阶段代价约为 $\\frac{1}{3}n^3$ 次乘法，回代阶段为 $O(n^2)$，故总复杂度 $O(n^3)$。"))
 )},
{"id":"cp5s1-2","name":"LU分解（Doolittle）","tags":["thm","der"],"brief":"把系数矩阵分解为下三角与上三角之积。",
 "fig":"lu_decomp","figCap":"LU 分解：A 分解为单位下三角 L 与上三角 U 的乘积",
 "body": wrap(
   thm("LU 分解", p("若 $A$ 的各阶顺序主子式非零，则存在唯一的单位下三角矩阵 $L$（$l_{ii}=1$）与上三角矩阵 $U$，使 $A=LU$。"))+
   der(p("<strong>Doolittle 递推：</strong>由 $A=LU$ 的第 $(i,j)$ 个元素，利用 $L$ 的下三角结构与 $U$ 的上三角结构：")+
   fml("a_{ij}=\\sum_{k=1}^{\\min(i,j)}l_{ik}u_{kj}")+
   p("先算 $U$ 的第 $i$ 行（$j\\ge i$）：")+
   fml("u_{ij}=a_{ij}-\\sum_{k=1}^{i-1}l_{ik}u_{kj}")+
   p("再算 $L$ 的第 $j$ 列（$i>j$）：")+
   fml("l_{ij}=\\frac{1}{u_{jj}}\\left(a_{ij}-\\sum_{k=1}^{j-1}l_{ik}u_{kj}\\right)")+
   p("按 $i,j$ 交替递增的顺序即可求出全部元素。求解时先解 $L\\mathbf{y}=\\mathbf{b}$（前代），再解 $U\\mathbf{x}=\\mathbf{y}$（回代）。"))+
   note(p("LU 分解一次可复用于多个右端项，适合 $A$ 不变、$\\mathbf{b}$ 变化的重复求解。"))
 )},
{"id":"cp5s1-3","name":"列主元与数值稳定性","tags":["der","app"],"brief":"选主元避免小主元导致的误差放大。",
 "body": wrap(
   der(p("<strong>小主元的危害：</strong>若主元 $a_{kk}$ 很小，乘子 $m_{ik}$ 很大，舍入误差被剧烈放大。例如 $\\varepsilon$ 很小时方程组")+
   fml("\\begin{pmatrix}\\varepsilon&1\\\\1&1\\end{pmatrix}\\begin{pmatrix}x_1\\\\x_2\\end{pmatrix}=\\begin{pmatrix}1\\\\2\\end{pmatrix}")+
   p("不选主元时 $m=\\frac{1}{\\varepsilon}$，回代结果严重失真。")+
   p("<strong>列主元消元：</strong>在第 $k$ 列中选取绝对值最大的元素作为主元：")+
   fml("|a_{pk}|=\\max_{i\\ge k}|a_{ik}|")+
   p("交换第 $p$ 行与第 $k$ 行后再消元，可保证乘子 $|m_{ik}|\\le1$，误差增长因子得到控制。"))+
   app(p("<strong>应用：</strong>实际线性方程组求解器（LAPACK、MATLAB 反斜杠）默认使用列主元 LU 分解；对称正定矩阵可用 Cholesky 分解 $A=LL^{\\top}$ 更高效稳定。"))
 )},
]},
{
"name": "5.2 三对角方程组的追赶法",
"color": "#db2777",
"desc": "Thomas 算法：三对角线性方程组的 O(n) 高效解法",
"items": [
{"id":"cp5s2-1","name":"三对角方程组","tags":["def","der"],"brief":"仅主对角与上下次对角非零的稀疏方程组。",
 "fig":"tridiagonal","figCap":"三对角矩阵：非零元素仅集中在三条对角线上",
 "body": wrap(
   defn("三对角方程组", p("形如")+
   fml("a_ix_{i-1}+b_ix_i+c_ix_{i+1}=d_i,\\qquad i=1,\\dots,n")+
   p("其中 $a_1=c_n=0$。矩阵为三对角带状矩阵，每行至多 3 个非零元。"))+
   der(p("<strong>来源：</strong>一维边值问题的差分格式、三次样条的三弯矩方程、隐式差分格式均化为三对角方程组。")+
   fml("\\begin{pmatrix}b_1&c_1&&\\\\ a_2&b_2&c_2&\\\\ &\\ddots&\\ddots&\\ddots\\\\ &&a_n&b_n\\end{pmatrix}\\begin{pmatrix}x_1\\\\ \\vdots\\\\ x_n\\end{pmatrix}=\\begin{pmatrix}d_1\\\\ \\vdots\\\\ d_n\\end{pmatrix}")+
   p("由于其稀疏结构，可用追赶法在 $O(n)$ 时间内求解，而通用高斯消元需 $O(n^3)$。"))+
   note(p("当 $|b_i|\\ge|a_i|+|c_i|$ 且严格不等号对某行成立时，矩阵严格对角占优，追赶法无需选主元即稳定。"))
 )},
{"id":"cp5s2-2","name":"追赶法（Thomas 算法）","tags":["thm","der"],"brief":"消元与前代合并，递推求出各未知数。",
 "body": wrap(
   thm("追赶法", p("记消元后的系数为 $c_i',d_i'$，则")+
   fml("c_i'=\\frac{c_i}{b_i-a_ic_{i-1}'},\\qquad d_i'=\\frac{d_i-a_id_{i-1}'}{b_i-a_ic_{i-1}'}")+
   p("回代 $x_n=d_n'$，$x_i=d_i'-c_i'x_{i+1}$。"))+
   der(p("<strong>推导：</strong>第一式 $b_1x_1+c_1x_2=d_1$ 可写为 $x_1=d_1'-c_1'x_2$，其中 $c_1'=c_1/b_1$，$d_1'=d_1/b_1$。")+
   p("代入第二式消去 $x_1$：")+
   fml("a_2(d_1'-c_1'x_2)+b_2x_2+c_2x_3=d_2")+
   p("整理得 $(b_2-a_2c_1')x_2+c_2x_3=d_2-a_2d_1'$，即")+
   fml("x_2=\\frac{d_2-a_2d_1'}{b_2-a_2c_1'}-\\frac{c_2}{b_2-a_2c_1'}x_3")+
   p("与递推式 $x_2=d_2'-c_2'x_3$ 对比即得 $c_2',d_2'$ 的表达式，依次类推。"))+
   note(p("该算法只需一趟前推（追）与一趟回代（赶），故称追赶法；存储用三个一维数组即可。"))
 )},
{"id":"cp5s2-3","name":"追赶法的稳定性与算例","tags":["exa","der"],"brief":"对角占优时算法稳定，复杂度 O(n)。",
 "body": wrap(
   der(p("<strong>稳定性：</strong>由 $|b_i|\\ge|a_i|+|c_i|$ 可归纳证明分母 $|b_i-a_ic_{i-1}'|\\ge|b_i|-|a_i||c_{i-1}'|>0$，且 $|c_i'|=\\left|\\frac{c_i}{b_i-a_ic_{i-1}'}\\right|\\le1$，故前推过程不会出现小主元，算法数值稳定。"))+
   exa(p("<strong>例：</strong>求解隐式热传导方程得到的 $n=100$ 三对角方程组，追赶法只需约 $5n=500$ 次运算，而通用消元需约 $3\\times10^5$ 次，效率相差数百倍。"))+
   app(p("<strong>应用：</strong>追赶法用于一维热传导、扩散方程的隐式求解、样条插值、以及任何三对角或分块三对角系统的快速求解，是科学计算的基本工具。"))
 )},
]},
{
"name": "5.3 QR分解法",
"color": "#ec4899",
"desc": "正交三角分解及其在最小二乘中的应用",
"items": [
{"id":"cp5s3-1","name":"Gram-Schmidt 正交化","tags":["der","def"],"brief":"逐列构造正交基得到 QR 分解。",
 "fig":"qr","figCap":"QR 分解：把列向量正交化并归一化",
 "body": wrap(
   defn("QR 分解", p("把矩阵 $A$ 分解为 $A=QR$，其中 $Q$ 列正交（$Q^{\\top}Q=I$），$R$ 上三角。"))+
   der(p("<strong>Gram-Schmidt 推导：</strong>设 $A=[\\mathbf{a}_1,\\dots,\\mathbf{a}_n]$。逐个正交化：")+
   fml("\\mathbf{q}_1=\\frac{\\mathbf{a}_1}{\\|\\mathbf{a}_1\\|}")+
   p("对 $k\\ge2$，先减去在已有正交基上的投影：")+
   fml("\\mathbf{v}_k=\\mathbf{a}_k-\\sum_{j\\lt k}(\\mathbf{a}_k^{\\top}\\mathbf{q}_j)\\mathbf{q}_j,\\qquad \\mathbf{q}_k=\\frac{\\mathbf{v}_k}{\\|\\mathbf{v}_k\\|}")+
   p("记 $r_{jk}=\\mathbf{a}_k^{\\top}\\mathbf{q}_j$，$r_{kk}=\\|\\mathbf{v}_k\\|$，则 $\\mathbf{a}_k=\\sum_{j\\le k}r_{jk}\\mathbf{q}_j$，写成矩阵即 $A=QR$。"))+
   note(p("经典 Gram-Schmidt 数值上易失正交性，实际用改进版（MGS）或 Householder 变换更稳定。"))
 )},
{"id":"cp5s3-2","name":"Householder 变换","tags":["thm","der"],"brief":"用反射矩阵逐步把矩阵化为上三角。",
 "body": wrap(
   thm("Householder 反射", p("对向量 $\\mathbf{x}$，令 $\\mathbf{v}=\\mathbf{x}+\\mathrm{sign}(x_1)\\|\\mathbf{x}\\|\\mathbf{e}_1$，则")+
   fml("H=I-2\\frac{\\mathbf{v}\\mathbf{v}^{\\top}}{\\mathbf{v}^{\\top}\\mathbf{v}}")+
   p("为正交对称矩阵，且 $H\\mathbf{x}=-\\mathrm{sign}(x_1)\\|\\mathbf{x}\\|\\mathbf{e}_1$，即把 $\\mathbf{x}$ 反射到第一个坐标轴。"))+
   der(p("<strong>化为上三角：</strong>对 $A$ 的每一列构造 $H_k$ 消去对角线以下元素：")+
   fml("H_{n-1}\\cdots H_1A=R")+
   p("令 $Q=H_1\\cdots H_{n-1}$（正交矩阵之积仍正交），则 $A=QR$。")+
   p("<strong>优点：</strong>Householder 变换数值稳定，正交性不退化，是求解 QR 分解的标准方法，运算量约 $\\frac{2}{3}n^3$。"))+
   note(p("对超定方程组的 QR 求解精度通常优于法方程 $A^{\\top}A\\mathbf{x}=A^{\\top}\\mathbf{b}$，因后者使条件数平方放大。"))
 )},
{"id":"cp5s3-3","name":"QR 分解用于最小二乘","tags":["app","der"],"brief":"用 QR 分解求解超定线性最小二乘问题。",
 "body": wrap(
   der(p("<strong>最小二乘问题：</strong>对超定方程组 $A\\mathbf{x}\\approx\\mathbf{b}$（$A$ 为 $m\\times n$，$m>n$），最小化 $\\|A\\mathbf{x}-\\mathbf{b}\\|_2^2$。")+
   p("作 QR 分解 $A=QR$，把 $Q$ 分块 $Q=[Q_1,Q_2]$（$Q_1$ 取前 $n$ 列）：")+
   fml("\\|A\\mathbf{x}-\\mathbf{b}\\|^2=\\|R_1\\mathbf{x}-Q_1^{\\top}\\mathbf{b}\\|^2+\\|Q_2^{\\top}\\mathbf{b}\\|^2")+
   p("第二个范数与 $\\mathbf{x}$ 无关，故只需解上三角方程组 $R_1\\mathbf{x}=Q_1^{\\top}\\mathbf{b}$。")+
   p("这比解正规方程 $A^{\\top}A\\mathbf{x}=A^{\\top}\\mathbf{b}$ 数值稳定得多（条件数由 $\\kappa^2$ 降为 $\\kappa$）。"))+
   app(p("<strong>应用：</strong>QR 用于数据拟合、参数估计、图像重建与数值线性代数中的特征值 QR 算法，是最小二乘的标准解法。"))
 )},
]},
{
"name": "5.4 迭代法求解线性方程组",
"color": "#9d174d",
"desc": "Jacobi、Gauss-Seidel 与收敛性分析",
"items": [
{"id":"cp5s4-1","name":"雅可比迭代法","tags":["def","der"],"brief":"用上一轮的全部分量更新当前分量。",
 "body": wrap(
   defn("Jacobi 迭代", p("从第 $i$ 个方程解出 $x_i$，右侧全部用上一轮值：")+
   fml("x_i^{(k+1)}=\\frac{1}{a_{ii}}\\left(b_i-\\sum_{j\\neq i}a_{ij}x_j^{(k)}\\right)"))+
   der(p("<strong>矩阵形式：</strong>把 $A=D+L+U$（$D$ 对角、$L,U$ 严格下上三角），则")+
   fml("D\\mathbf{x}^{(k+1)}=\\mathbf{b}-(L+U)\\mathbf{x}^{(k)}\\ \\Rightarrow\\ \\mathbf{x}^{(k+1)}=B_J\\mathbf{x}^{(k)}+D^{-1}\\mathbf{b}")+
   p("其中迭代矩阵 $B_J=-D^{-1}(L+U)$。误差满足")+
   fml("\\mathbf{e}^{(k)}=B_J^k\\mathbf{e}^{(0)}")+
   p("故迭代收敛当且仅当 $\\rho(B_J)<1$（谱半径小于 1）。"))+
   note(p("Jacobi 法各分量可并行更新，适合并行计算；当 $A$ 严格对角占优时必收敛。"))
 )},
{"id":"cp5s4-2","name":"高斯-赛德尔迭代法","tags":["der"],"brief":"利用已更新的分量加速收敛。",
 "fig":"jacobi_gs","figCap":"Jacobi 与 Gauss-Seidel 迭代误差衰减对比",
 "body": wrap(
   der(p("<strong>迭代格式：</strong>更新 $x_i$ 时，$j\\lt i$ 的分量已用新值：")+
   fml("x_i^{(k+1)}=\\frac{1}{a_{ii}}\\left(b_i-\\sum_{j\\lt i}a_{ij}x_j^{(k+1)}-\\sum_{j>i}a_{ij}x_j^{(k)}\\right)")+
   p("矩阵形式：$(D+L)\\mathbf{x}^{(k+1)}=\\mathbf{b}-U\\mathbf{x}^{(k)}$，迭代矩阵")+
   fml("B_{GS}=-(D+L)^{-1}U")+
   p("<strong>优势：</strong>通常 $\\rho(B_{GS})<\\rho(B_J)$，收敛更快（约为 Jacobi 的两倍速度），且无需额外存储。")+
   p("<strong>收敛条件：</strong>$A$ 严格对角占优（或对称正定）时 Gauss-Seidel 收敛。"))+
   note(p("SOR（超松弛）在 Gauss-Seidel 基础上引入松弛因子 $\\omega$，$1<\\omega<2$ 时收敛更快，$\\omega=1$ 退化为 Gauss-Seidel。"))
 )},
{"id":"cp5s4-3","name":"迭代法的收敛性","tags":["thm","der"],"brief":"谱半径与对角占优是对角收敛的判据。",
 "body": wrap(
   thm("收敛性定理", p("迭代 $\\mathbf{x}^{(k+1)}=B\\mathbf{x}^{(k)}+\\mathbf{c}$ 对任意初值收敛当且仅当 $\\rho(B)<1$；此时收敛速度为 $O(\\rho(B)^k)$。"))+
   der(p("<strong>证明要点：</strong>误差递推 $\\mathbf{e}^{(k+1)}=B\\mathbf{e}^{(k)}$，故 $\\mathbf{e}^{(k)}=B^k\\mathbf{e}^{(0)}$。由 Jordan 标准形，$B^k\\to0$ 当且仅当所有特征值模小于 1。")+
   p("<strong>对角占优判据：</strong>若 $|a_{ii}|>\\sum_{j\\neq i}|a_{ij}|$，可证 $\\rho(B_J)<1$ 与 $\\rho(B_{GS})<1$，两种迭代均收敛。")+
   fml("|a_{ii}|>\\sum_{j\\neq i}|a_{ij}|\\ \\Rightarrow\\ \\text{Jacobi 与 GS 都收敛}")+
   p("<strong>谱半径比较：</strong>对正定三对角矩阵可证 $\\rho(B_{GS})=\\rho(B_J)^2$，故 GS 收敛速度是 Jacobi 的两倍。"))+
   app(p("<strong>应用：</strong>大规模稀疏线性方程组（如离散化后的泊松方程）常用迭代法或 Krylov 子空间方法（CG、GMRES），避免直接法的高存储与高计算量。"))
 )},
]},
{
"name": "5.5 矩阵特征值问题",
"color": "#e11d48",
"desc": "幂法、反幂法与 QR 算法",
"items": [
{"id":"cp5s5-1","name":"幂法","tags":["der","thm"],"brief":"迭代求主特征值与主特征向量。",
 "fig":"power_iter","figCap":"幂法：反复乘 A 后向量逐渐对齐主特征方向",
 "body": wrap(
   thm("幂法", p("若 $A$ 有唯一模最大的特征值 $|\\lambda_1|>|\\lambda_2|\\ge\\dots$，则对几乎任意 $\\mathbf{v}^{(0)}$，迭代")+
   fml("\\mathbf{v}^{(k+1)}=\\frac{A\\mathbf{v}^{(k)}}{\\|A\\mathbf{v}^{(k)}\\|}")+
   p("收敛到主特征向量，且 $\\lambda_1\\approx(\\mathbf{v}^{(k)})^{\\top}A\\mathbf{v}^{(k)}$。"))+
   der(p("<strong>推导：</strong>把初值按特征向量展开 $\\mathbf{v}^{(0)}=\\sum_i c_i\\mathbf{u}_i$，则")+
   fml("A^k\\mathbf{v}^{(0)}=\\sum_i c_i\\lambda_i^k\\mathbf{u}_i=\\lambda_1^k\\left(c_1\\mathbf{u}_1+\\sum_{i\\ge2}c_i\\left(\\frac{\\lambda_i}{\\lambda_1}\\right)^k\\mathbf{u}_i\\right)")+
   p("因 $|\\lambda_i/\\lambda_1|<1$，第二项随 $k$ 趋于零，故方向收敛到 $\\mathbf{u}_1$，归一化后即得主特征向量。"))+
   note(p("收敛速度由比值 $|\\lambda_2/\\lambda_1|$ 决定；当两个特征值模接近时收敛很慢，可用原点位移加速。"))
 )},
{"id":"cp5s5-2","name":"反幂法与瑞利商","tags":["der","app"],"brief":"求最接近给定值的特征值。",
 "body": wrap(
   der(p("<strong>反幂法：</strong>对 $A-\\sigma I$ 应用幂法。若 $\\sigma$ 接近某特征值 $\\lambda_k$，则 $(A-\\sigma I)^{-1}$ 的主特征值为 $\\frac{1}{\\lambda_k-\\sigma}$（模最大），故迭代")+
   fml("\\mathbf{v}^{(k+1)}=\\frac{(A-\\sigma I)^{-1}\\mathbf{v}^{(k)}}{\\|\\cdot\\|}")+
   p("收敛到该特征向量，且特征值由 $\\lambda_k\\approx\\sigma+\\frac{1}{\\mu}$（$\\mu$ 为 $\\mathbf{v}^{\\top}(A-\\sigma I)^{-1}\\mathbf{v}$）给出。")+
   p("<strong>瑞利商：</strong>对对称矩阵，")+
   fml("R(\\mathbf{x})=\\frac{\\mathbf{x}^{\\top}A\\mathbf{x}}{\\mathbf{x}^{\\top}\\mathbf{x}}")+
   p("在特征向量处取极值；带瑞利商位移的反幂法可实现三次收敛。"))+
   app(p("<strong>应用：</strong>反幂法用于求最接近给定值的特征值，配合位移可逐个求出全部特征值，是结构模态分析与稳定性分析的重要工具。"))
 )},
{"id":"cp5s5-3","name":"QR 算法","tags":["der","app"],"brief":"通过反复 QR 分解求全部特征值。",
 "body": wrap(
   der(p("<strong>基本 QR 算法：</strong>令 $A_0=A$，反复作 QR 分解并交换乘法顺序：")+
   fml("A_k=Q_kR_k,\\qquad A_{k+1}=R_kQ_k")+
   p("由于 $A_{k+1}=Q_k^{\\top}A_kQ_k$，迭代保持相似变换，特征值不变。")+
   p("<strong>收敛性：</strong>在适当条件下 $A_k$ 趋于上三角（Schur 形），对角线元素即为特征值。")+
   p("<strong>加速技巧：</strong>先化为上 Hessenberg 形（减少运算量），再引入位移（Wilkinson 位移）使收敛加快，通常几次迭代即收敛。"))+
   app(p("<strong>应用：</strong>QR 算法是计算一般矩阵全部特征值的标准方法（LAPACK 中 dgeev 内核）；对称矩阵则用更快的三对角化加 QR 或 divide-and-conquer。"))
 )},
]},
]
ch6_sections = [
{
"name": "6.1 欧拉法与改进欧拉法",
"color": "#0891b2",
"desc": "初值问题的最简单数值解法与精度改进",
"items": [
{"id":"cp6s1-1","name":"欧拉法","tags":["def","der"],"brief":"用差商近似导数得到最简显式格式。",
 "fig":"euler_rk","figCap":"欧拉法与 RK4：步长相同但精度差别显著",
 "body": wrap(
   defn("初值问题", p("一阶常微分方程初值问题")+
   fml("y'=f(x,y),\\qquad y(x_0)=y_0"))+
   der(p("<strong>欧拉法推导：</strong>在 $x_n$ 处用前向差商近似导数：")+
   fml("\\frac{y(x_{n+1})-y(x_n)}{h}\\approx f(x_n,y(x_n))")+
   p("以 $y_n$ 近似 $y(x_n)$，解出 $y_{n+1}$：")+
   fml("y_{n+1}=y_n+hf(x_n,y_n)")+
   p("几何上是从 $(x_n,y_n)$ 沿斜率 $f$ 的方向前进 $h$，即折线法。"))+
   note(p("欧拉法是最简单的单步显式方法，但精度低（$O(h)$）、稳定性差，主要用于教学与算法分析。"))
 )},
{"id":"cp6s1-2","name":"欧拉法的误差与稳定性","tags":["der","thm"],"brief":"局部误差 O(h²)、整体误差 O(h)，条件稳定。",
 "body": wrap(
   der(p("<strong>截断误差：</strong>由泰勒展开")+
   fml("y(x_{n+1})=y(x_n)+hy'(x_n)+\\frac{h^2}{2}y''(\\xi)")+
   p("与欧拉法对比，局部截断误差为")+
   fml("\\tau_{n+1}=\\frac{h^2}{2}y''(\\xi)=O(h^2)")+
   p("累积 $n\\sim1/h$ 步后整体误差为 $O(h)$，故欧拉法是一阶方法。")+
   p("<strong>稳定性：</strong>对模型方程 $y'=\\lambda y$（$\\mathrm{Re}\\,\\lambda<0$），欧拉法给出 $y_{n+1}=(1+\\lambda h)y_n$，稳定要求")+
   fml("|1+\\lambda h|\\le1\\ \\Rightarrow\\ h\\le\\frac{2}{|\\lambda|}")+
   p("即欧拉法<strong>条件稳定</strong>，步长受稳定性限制。"))+
   note(p("当 $|\\lambda|$ 很大（刚性）时，$h$ 被压得极小，欧拉法效率极低，须改用隐式方法。"))
 )},
{"id":"cp6s1-3","name":"改进欧拉法（预估-校正）","tags":["der","thm"],"brief":"用梯形公式的显式实现，达到二阶精度。",
 "fig":"euler_modified","figCap":"改进欧拉法：先用欧拉法预报，再用梯形校正",
 "body": wrap(
   thm("改进欧拉法", p("先用欧拉法预报，再用梯形公式校正：")+
   fml("\\bar{y}_{n+1}=y_n+hf(x_n,y_n)")+
   fml("y_{n+1}=y_n+\\frac{h}{2}\\left[f(x_n,y_n)+f(x_{n+1},\\bar{y}_{n+1})\\right]"))+
   der(p("<strong>推导：</strong>对 $y'=f$ 在 $[x_n,x_{n+1}]$ 上积分并梯形近似：")+
   fml("y(x_{n+1})=y(x_n)+\\int_{x_n}^{x_{n+1}}f\\,dx\\approx y_n+\\frac{h}{2}(f_n+f_{n+1})")+
   p("因 $f_{n+1}$ 含未知的 $y_{n+1}$，先用欧拉法预估，再代入校正，故称预估-校正法。")+
   p("它等价于二阶 Runge-Kutta 方法，局部误差 $O(h^3)$，整体 $O(h^2)$。"))+
   note(p("改进欧拉法每步计算两次函数值，但精度提高一阶，是性价比很高的入门方法。"))
 )},
]},
{
"name": "6.2 龙格-库塔方法",
"color": "#0ea5e9",
"desc": "通过多阶段斜率加权获得高阶精度",
"items": [
{"id":"cp6s2-1","name":"二阶龙格-库塔方法","tags":["der","thm"],"brief":"用两次斜率加权匹配泰勒展开到 h² 项。",
 "body": wrap(
   thm("一般二阶 RK", p("形如")+
   fml("y_{n+1}=y_n+h(\\alpha_1k_1+\\alpha_2k_2),\\quad k_1=f(x_n,y_n),\\ k_2=f(x_n+ph,y_n+phk_1)")+
   p("选择参数使局部误差为 $O(h^3)$，可得一族二阶方法。"))+
   der(p("<strong>阶条件：</strong>把 $k_2$ 泰勒展开：")+
   fml("k_2=f+h(pf_x+pf_yf)+O(h^2)")+
   p("代入并整理，要求 $h$ 与 $h^2$ 项与精确解 $y+hy'+\\frac{h^2}{2}y''$ 一致，得约束")+
   fml("\\alpha_1+\\alpha_2=1,\\qquad \\alpha_2p=\\frac{1}{2}")+
   p("例如取 $\\alpha_2=\\frac{1}{2},p=1$ 得改进欧拉法；取 $\\alpha_2=1,p=\\frac{1}{2}$ 得中点法。"))+
   note(p("二阶方法不止一个，但它们在 $O(h^3)$ 精度下等价；选择时兼顾稳定性与实现便利。"))
 )},
{"id":"cp6s2-2","name":"经典四阶龙格-库塔","tags":["der","thm"],"brief":"四段斜率加权，最常用的高阶单步方法。",
 "body": wrap(
   thm("RK4 公式", p("")+
   fml("y_{n+1}=y_n+\\frac{h}{6}(k_1+2k_2+2k_3+k_4)")+
   p("其中")+
   fml("k_1=f(x_n,y_n),\\quad k_2=f(x_n+\\tfrac{h}{2},y_n+\\tfrac{h}{2}k_1)")+
   fml("k_3=f(x_n+\\tfrac{h}{2},y_n+\\tfrac{h}{2}k_2),\\quad k_4=f(x_n+h,y_n+hk_3)"))+
   der(p("<strong>阶条件：</strong>把四个 $k_i$ 展开成 $h$ 的幂级数，代入加权和，令 $h^1,h^2,h^3$ 的系数与精确解的泰勒展开完全一致。")+
   p("这给出 4 个阶段、8 个参数的一组非线性方程，经典解取 $\\frac{1}{6},\\frac{1}{3},\\frac{1}{3},\\frac{1}{6}$ 权重，误差为 $O(h^4)$（局部 $O(h^5)$）。")+
   p("RK4 每步需 4 次函数求值，但精度远高于同计算量的低阶方法。"))+
   note(p("RK4 是工程仿真最常用的通用求解器，对多数非刚性问题兼具精度与效率。"))
 )},
{"id":"cp6s2-3","name":"自适应步长与嵌入方法","tags":["der","app"],"brief":"用嵌入式低阶方法估计误差并调节步长。",
 "body": wrap(
   der(p("<strong>嵌入思想：</strong>RK-Fehlberg 45 用 6 次函数求值同时得到 4 阶与 5 阶解 $y_{n+1}^{(4)},y_{n+1}^{(5)}$，两者之差作为误差估计：")+
   fml("\\text{err}=|y_{n+1}^{(5)}-y_{n+1}^{(4)}|")+
   p("按误差调节步长：")+
   fml("h_{new}=h\\left(\\frac{\\text{tol}}{\\text{err}}\\right)^{1/5}")+
   p("误差超过容差则缩小步长重算，远小于容差则放大步长以提高效率。")+
   p("这使方法能在解变化剧烈处自动取小步、平缓处取大步。"))+
   app(p("<strong>应用：</strong>MATLAB 的 ode45、Python SciPy 的 solve_ivp(RK45) 都基于嵌入 RK 对，是求解非刚性 ODE 的默认选择。"))
 )},
]},
{
"name": "6.3 线性多步法",
"color": "#06b6d4",
"desc": "利用历史多点信息构造高精度格式",
"items": [
{"id":"cp6s3-1","name":"Adams-Bashforth 方法","tags":["der","thm"],"brief":"对历史斜率做外推得到显式多步格式。",
 "fig":"linear_multistep","figCap":"线性多步法：利用若干历史点拟合多项式外推下一步",
 "body": wrap(
   thm("四阶 Adams-Bashforth", p("")+
   fml("y_{n+1}=y_n+\\frac{h}{24}(55f_n-59f_{n-1}+37f_{n-2}-9f_{n-3})"))+
   der(p("<strong>推导：</strong>在 $[x_n,x_{n+1}]$ 上积分 $y'=f$：")+
   fml("y_{n+1}=y_n+\\int_{x_n}^{x_{n+1}}f(x,y)\\,dx")+
   p("用过 $x_n,x_{n-1},x_{n-2},x_{n-3}$ 四点的三次插值多项式近似 $f$（外推），积分该多项式得权重 $\\frac{55}{24},-\\frac{59}{24},\\frac{37}{24},-\\frac{9}{24}$。")+
   p("局部误差为 $O(h^5)$，整体 $O(h^4)$，但需前 4 个初值（可用 RK4 启动）。"))+
   note(p("特点：每步只算一次函数值，比同阶 RK4 省算力；但需要额外存储历史值，且显式多步法稳定性域较小。"))
 )},
{"id":"cp6s3-2","name":"Adams-Moulton 与预估-校正","tags":["der","app"],"brief":"隐式多步法配合显式预估构成高效格式。",
 "body": wrap(
   der(p("<strong>隐式 Adams-Moulton：</strong>若插值节点包含 $x_{n+1}$，得到隐式格式，如三阶：")+
   fml("y_{n+1}=y_n+\\frac{h}{12}(5f_{n+1}+8f_n-f_{n-1})")+
   p("隐式格式精度更高、稳定域更大，但右端含未知 $y_{n+1}$，须迭代求解。")+
   p("<strong>预估-校正：</strong>先用 Adams-Bashforth 预估 $y_{n+1}^{(0)}$，代入隐式公式校正：")+
   fml("y_{n+1}=y_n+\\frac{h}{12}\\left(5f(x_{n+1},y_{n+1}^{(0)})+8f_n-f_{n-1}\\right)")+
   p("两者阶数相同，误差可用 $y_{n+1}-y_{n+1}^{(0)}$ 估计，用于变步长控制。"))+
   app(p("<strong>应用：</strong>预估-校正（如 Adams-Bashforth-Moulton）在对函数求值昂贵的仿真中很高效，因每步仅需一次新函数求值。"))
 )},
{"id":"cp6s3-3","name":"相容性、收敛性与阶","tags":["thm","der"],"brief":"多步法的相容性与线性稳定性分析。",
 "body": wrap(
   thm("相容性条件", p("线性多步法 $\\sum_{j=0}^{k}\\alpha_jy_{n+j}=h\\sum_{j=0}^{k}\\beta_jf_{n+j}$ 相容的条件为")+
   fml("\\sum_{j}\\alpha_j=0,\\qquad \\sum_{j}j\\alpha_j=\\sum_{j}\\beta_j"))+
   der(p("<strong>推导：</strong>把精确解代入并作泰勒展开，要求 $h^0$ 与 $h^1$ 项为零，即得上述两式。")+
   p("阶数 $p$ 的进一步条件为高阶矩匹配：")+
   fml("\\sum_j j^m\\alpha_j=m\\sum_j j^{m-1}\\beta_j,\\qquad m=0,1,\\dots,p")+
   p("局部误差的首个非零项即给出阶数。"))+
   app(p("<strong>零稳定性（Dahlquist 条件）：</strong>第一特征多项式 $\\rho(\\xi)=\\sum\\alpha_j\\xi^j$ 的根须满足 $|\\xi_i|\\le1$ 且单根在 $|\\xi_i|=1$ 上。相容与零稳定共同保证多步法收敛。"))
 )},
]},
{
"name": "6.4 刚性方程与稳定性",
"color": "#0284c7",
"desc": "刚性问题的特征与隐式方法",
"items": [
{"id":"cp6s4-1","name":"刚性方程","tags":["def","der"],"brief":"快慢模式时间尺度差异巨大。",
 "fig":"stiff","figCap":"刚性方程：快模式迅速衰减，慢模式决定解的整体走向",
 "body": wrap(
   defn("刚性方程", p("若方程组的雅可比矩阵特征值满足")+
   fml("\\left|\\mathrm{Re}\\,\\lambda_{\\max}\\right|\\gg\\left|\\mathrm{Re}\\,\\lambda_{\\min}\\right|")+
   p("则称方程是刚性的。快模式（大 $|\\lambda|$）迅速衰减，慢模式主导解的长期行为。"))+
   der(p("<strong>例：</strong>系统")+
   fml("y_1'=-100y_1,\\qquad y_2'=-y_2")+
   p("特征值 $-100$ 与 $-1$，刚性比 $100$。精确解中 $e^{-100x}$ 项很快消失，但显式方法仍受其稳定性约束：")+
   fml("h\\le\\frac{2}{100}=0.02")+
   p("即使解已由慢模式 $e^{-x}$ 主导，步长仍被快模式限制，导致效率极低。"))+
   note(p("刚性问题广泛存在于化学反应动力学、电路瞬态、传热与控制系统中。"))
 )},
{"id":"cp6s4-2","name":"绝对稳定性与A稳定","tags":["thm","der"],"brief":"稳定域包含左半平面即 A 稳定。",
 "body": wrap(
   thm("A 稳定", p("若方法的绝对稳定区域包含整个左半复平面 $\\mathrm{Re}(\\lambda h)<0$，则称该方法是 A 稳定的。"))+
   der(p("<strong>稳定域分析：</strong>对模型方程 $y'=\\lambda y$，方法给出 $y_{n+1}=R(z)y_n$（$z=\\lambda h$），稳定要求 $|R(z)|\\le1$。")+
   p("显式方法的 $R(z)$ 为多项式，$|z|\\to\\infty$ 时 $|R(z)|\\to\\infty$，故<strong>显式方法不可能是 A 稳定</strong>的。")+
   p("隐式 Euler 的放大因子 $R(z)=\\frac{1}{1-z}$，对 $\\mathrm{Re}(z)<0$ 恒有")+
   fml("|R(z)|=\\frac{1}{|1-z|}\\le1")+
   p("故隐式 Euler 是 A 稳定的，可在大步长下求解刚性问题。"))+
   note(p("Dahlquist 定理指出：A 稳定方法中精度最高只到二阶，隐式 Euler 与梯形法（Crank-Nicolson）是常用的 A 稳定方法。"))
 )},
{"id":"cp6s4-3","name":"隐式方法求解刚性问题","tags":["der","app"],"brief":"隐式格式需解非线性方程，但步长不受刚性限制。",
 "body": wrap(
   der(p("<strong>向后 Euler：</strong>")+
   fml("y_{n+1}=y_n+hf(x_{n+1},y_{n+1})")+
   p("对线性 $f=\\lambda y$ 可直接解出 $y_{n+1}=\\frac{y_n}{1-\\lambda h}$；对非线性 $f$ 需用牛顿法解隐式方程。")+
   p("<strong>梯形法（Crank-Nicolson）：</strong>")+
   fml("y_{n+1}=y_n+\\frac{h}{2}\\left[f_n+f_{n+1}\\right]")+
   p("二阶精度且 A 稳定，但可能对刚性分量产生振荡（非 L 稳定）。")+
   p("<strong>L 稳定：</strong>要求 $|R(z)|\\to0$（$\\mathrm{Re}(z)\\to-\\infty$），如向后 Euler、BDF2，能有效阻尼快模式。"))+
   app(p("<strong>应用：</strong>刚性求解器（如 MATLAB ode15s、SciPy BDF/Radau、CVODE）基于 BDF 或隐式 Runge-Kutta，是化学反应与电路仿真的标准工具。"))
 )},
]},
{
"name": "6.5 边值问题的数值解法",
"color": "#22d3ee",
"desc": "差分法与打靶法求解两点边值问题",
"items": [
{"id":"cp6s5-1","name":"差分法","tags":["der","def"],"brief":"把微分方程离散为三对角线性方程组。",
 "fig":"bvp","figCap":"边值问题：用差分格式在网格上离散，凑成三对角方程组",
 "body": wrap(
   defn("两点边值问题", p("")+
   fml("y''=f(x,y,y'),\\qquad y(a)=\\alpha,\\ y(b)=\\beta"))+
   der(p("<strong>离散化：</strong>取网格 $x_i=a+ih$，$h=\\frac{b-a}{n}$，用二阶中心差商：")+
   fml("y''(x_i)\\approx\\frac{y_{i+1}-2y_i+y_{i-1}}{h^2}")+
   p("若 $f=f(x)$ 与 $y'$ 无关，得线性方程组")+
   fml("-\\frac{1}{h^2}y_{i-1}+\\frac{2}{h^2}y_i-\\frac{1}{h^2}y_{i+1}=-f(x_i)")+
   p("这是一个严格对角占优的三对角方程组，可用追赶法 $O(n)$ 求解。")+
   p("若含 $y'$，用中心差商 $y_i'\\approx\\frac{y_{i+1}-y_{i-1}}{2h}$ 同样得三对角（或拟三对角）系统。"))+
   note(p("差分法简单直接、精度 $O(h^2)$，是边值问题最常用的数值方法。"))
 )},
{"id":"cp6s5-2","name":"打靶法","tags":["der","app"],"brief":"把边值问题转化为初值问题的求根。",
 "body": wrap(
   der(p("<strong>基本思想：</strong>猜测初始斜率 $s=y'(a)$，把边值问题当作初值问题求解，得到依赖 $s$ 的终端值 $y(b;s)$，再求根使")+
   fml("\\phi(s)=y(b;s)-\\beta=0")+
   p("用牛顿法迭代更新：")+
   fml("s_{k+1}=s_k-\\frac{\\phi(s_k)}{\\phi'(s_k)}")+
   p("其中 $\\phi'(s)=\\frac{\\partial y(b;s)}{\\partial s}$ 可由变分方程数值求出。"))+
   app(p("<strong>应用：</strong>打靶法把成熟的初值问题求解器（RK4、ode45）直接用于边值问题，适合非线性与复杂边界；但对解的敏感性高时（长期积分放大误差）稳定性差，此时宜用多重打靶法或配点法。"))
 )},
{"id":"cp6s5-3","name":"有限元与配点法简介","tags":["app","note"],"brief":"基于弱形式或配点的边值问题数值方法。",
 "body": wrap(
   der(p("<strong>有限元弱形式：</strong>两边界值问题 $-(pu')'+qu=f$，乘测试函数 $v$（$v(a)=v(b)=0$）并分部积分：")+
   fml("\\int_a^b\\left(pu'v'+quv\\right)dx=\\int_a^bfv\\,dx")+
   p("在有限维子空间中取 $u_h=\\sum u_j\\phi_j$，得线性方程组 $KU=F$，$K_{ij}=\\int(p\\phi_i'\\phi_j'+q\\phi_i\\phi_j)dx$。")+
   p("<strong>配点法：</strong>强制残差在若干配点为零，使用谱方法基函数时可达指数收敛。"))+
   app(p("<strong>应用：</strong>有限元是结构力学、传热与电磁场仿真的核心方法；谱配点法用于高精度流体与波动问题。"))
 )},
]},
]
ch7_sections = [
{
"name": "7.1 差分格式与网格",
"color": "#4f46e5",
"desc": "偏微分方程的网格离散、截断误差与相容性",
"items": [
{"id":"cp7s1-1","name":"网格与差分算子","tags":["def","der"],"brief":"在时空网格上用差分代替偏导数。",
 "fig":"heat_grid","figCap":"时空网格：用相邻节点值构造差分算子",
 "body": wrap(
   defn("网格离散", p("把空间区域划分为节点 $x_i=i\\Delta x$，时间分为 $t_n=n\\Delta t$，用 $u_i^n$ 近似 $u(x_i,t_n)$。"))+
   der(p("<strong>差分算子：</strong>空间二阶导用中心差分：")+
   fml("\\frac{\\partial^2u}{\\partial x^2}\\Big|_{i,n}\\approx\\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{\\Delta x^2}")+
   p("时间一阶导可用前向、后向或中心差分：")+
   fml("\\frac{\\partial u}{\\partial t}\\approx\\frac{u_i^{n+1}-u_i^n}{\\Delta t},\\qquad\\frac{\\partial u}{\\partial t}\\approx\\frac{u_i^{n+1}-u_i^{n-1}}{2\\Delta t}")+
   p("选择不同的时间、空间差分组合即得到显式或隐式格式。"))+
   note(p("差分格式的关键是保证相容性（$\\Delta t,\\Delta x\\to0$ 时截断误差趋于零）与稳定性。"))
 )},
{"id":"cp7s1-2","name":"截断误差与相容性","tags":["der","thm"],"brief":"用泰勒展开计算格式的截断误差。",
 "body": wrap(
   thm("截断误差", p("把精确解代入差分格式得到的余项称为截断误差，若 $\\Delta t,\\Delta x\\to0$ 时截断误差趋于零，则格式相容。"))+
   der(p("<strong>以热方程显式格式为例：</strong>$u_t=au_{xx}$。由泰勒展开：")+
   fml("\\frac{u_i^{n+1}-u_i^n}{\\Delta t}=u_t+\\frac{\\Delta t}{2}u_{tt}+O(\\Delta t^2)")+
   fml("\\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{\\Delta x^2}=u_{xx}+\\frac{\\Delta x^2}{12}u_{xxxx}+O(\\Delta x^4)")+
   p("代入格式并把 $u_t$ 换成 $au_{xx}$，得局部截断误差")+
   fml("\\tau=\\frac{\\Delta t}{2}u_{tt}-\\frac{a\\Delta x^2}{12}u_{xxxx}=O(\\Delta t)+O(\\Delta x^2)"))+
   note(p("该格式时间一阶、空间二阶精度，故记作 $O(\\Delta t)+O(\\Delta x^2)$，相容性满足。"))
 )},
{"id":"cp7s1-3","name":"显式与隐式格式","tags":["der","note"],"brief":"显式便于计算但受稳定性限制，隐式稳定但需求解方程组。",
 "body": wrap(
   der(p("<strong>显式格式：</strong>用当前时刻值显式表出下一个时刻，如")+
   fml("u_i^{n+1}=u_i^n+r\\left(u_{i+1}^n-2u_i^n+u_{i-1}^n\\right),\\quad r=\\frac{a\\Delta t}{\\Delta x^2}")+
   p("无需解方程组，实现简单，但条件稳定（$r\\le\\frac{1}{2}$）。")+
   p("<strong>隐式格式：</strong>右端用 $n+1$ 时刻值：")+
   fml("-ru_{i+1}^{n+1}+(1+2r)u_i^{n+1}-ru_{i-1}^{n+1}=u_i^n")+
   p("每步需解三对角方程组（追赶法 $O(N)$），但无条件稳定，可大步长推进。"))+
   note(p("选择格式需在精度、稳定性与每步计算量之间折中；实际问题常采用 Crank-Nicolson（二阶无条件稳定）。"))
 )},
]},
{
"name": "7.2 抛物型方程（热传导）",
"color": "#6366f1",
"desc": "热传导方程的显式、隐式与 Crank-Nicolson 格式及稳定性",
"items": [
{"id":"cp7s2-1","name":"热方程显式格式","tags":["der","def"],"brief":"时间前向、空间中心差分，条件稳定。",
 "fig":"heat_explicit","figCap":"显式热方程格式：新时刻值由上一层三个相邻点显式表出",
 "body": wrap(
   defn("热传导方程", p("")+
   fml("\\frac{\\partial u}{\\partial t}=a\\frac{\\partial^2u}{\\partial x^2}"))+
   der(p("<strong>显式格式：</strong>时间用前向差分、空间用中心差分：")+
   fml("\\frac{u_i^{n+1}-u_i^n}{\\Delta t}=a\\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{\\Delta x^2}")+
   p("解出 $u_i^{n+1}$，令网格比 $r=\\frac{a\\Delta t}{\\Delta x^2}$：")+
   fml("u_i^{n+1}=ru_{i-1}^n+(1-2r)u_i^n+ru_{i+1}^n")+
   p("每个新值都是上一层三点的加权平均（当 $r\\le\\frac12$ 时权重非负），符合热传导的物理直觉。"))+
   note(p("显式格式实现简单、可并行，但稳定性条件 $r\\le\\frac12$ 使步长受限，$\\Delta x$ 减半时 $\\Delta t$ 需减为四分之一。"))
 )},
{"id":"cp7s2-2","name":"隐式与 Crank-Nicolson 格式","tags":["der","thm"],"brief":"无条件稳定格式，可用大步长。",
 "body": wrap(
   der(p("<strong>向后 Euler（全隐式）：</strong>时间后向差分：")+
   fml("\\frac{u_i^{n+1}-u_i^n}{\\Delta t}=a\\frac{u_{i+1}^{n+1}-2u_i^{n+1}+u_{i-1}^{n+1}}{\\Delta x^2}")+
   p("整理为三对角方程组：")+
   fml("-ru_{i+1}^{n+1}+(1+2r)u_i^{n+1}-ru_{i-1}^{n+1}=u_i^n")+
   p("无条件稳定，但时间一阶精度。")+
   p("<strong>Crank-Nicolson：</strong>空间导数取 $n$ 与 $n+1$ 时刻的平均：")+
   fml("\\frac{u_i^{n+1}-u_i^n}{\\Delta t}=\\frac{a}{2}\\left(\\delta_{xx}u_i^{n+1}+\\delta_{xx}u_i^{n}\\right)")+
   p("其中 $\\delta_{xx}u_i=\\frac{u_{i+1}-2u_i+u_{i-1}}{\\Delta x^2}$，得到无条件稳定且时间二阶精度的格式。"))+
   note(p("Crank-Nicolson 每步解三对角方程组，是热传导问题最常用的格式；但对不连续初值可能产生振荡。"))
 )},
{"id":"cp7s2-3","name":"稳定性与网格比","tags":["thm","der"],"brief":"显式格式要求 r≤1/2。",
 "body": wrap(
   thm("显式格式稳定条件", p("热方程显式格式稳定的充要条件为")+
   fml("r=\\frac{a\\Delta t}{\\Delta x^2}\\le\\frac{1}{2}"))+
   der(p("<strong>推导（矩阵/范数法）：</strong>格式可写为 $u^{n+1}=Au^n$，其中 $A$ 三对角、对角元 $1-2r$、次对角元 $r$。由 Gershgorin 圆盘定理，$A$ 的特征值满足")+
   fml("|\\lambda-1+2r|\\le2r\\ \\Rightarrow\\ 1-4r\\le\\lambda\\le1")+
   p("要求 $|\\lambda|\\le1$，只需 $1-4r\\ge-1$，即")+
   fml("4r\\le2\\ \\Rightarrow\\ r\\le\\frac{1}{2}")+
   p("故 $r\\le\\frac12$ 时数值解不放大误差，格式稳定。"))+
   note(p("违反稳定性条件时数值解会出现锯齿状高频振荡并迅速发散，是初学者最常见的错误。"))
 )},
]},
{
"name": "7.3 双曲型方程（波动）",
"color": "#4338ca",
"desc": "波动方程差分格式、CFL 条件与数值色散",
"items": [
{"id":"cp7s3-1","name":"一阶双曲方程与 CFL 条件","tags":["der","thm"],"brief":"对流方程显式格式的 Courant 条件。",
 "fig":"wave_grid","figCap":"波动方程特征线：数值依赖域须覆盖解析依赖域",
 "body": wrap(
   defn("对流方程", p("")+
   fml("\\frac{\\partial u}{\\partial t}+c\\frac{\\partial u}{\\partial x}=0,\\qquad c>0"))+
   der(p("<strong>显式迎风格式：</strong>用一侧差分保证依赖域正确：")+
   fml("\\frac{u_i^{n+1}-u_i^n}{\\Delta t}=-c\\frac{u_i^n-u_{i-1}^n}{\\Delta x}")+
   p("即 $u_i^{n+1}=u_i^n-\\nu(u_i^n-u_{i-1}^n)$，$\\nu=\\frac{c\\Delta t}{\\Delta x}$。")+
   p("<strong>CFL 条件：</strong>由 von Neumann 分析或依赖域论证，稳定要求")+
   fml("0\\le\\nu=\\frac{c\\Delta t}{\\Delta x}\\le1")+
   p("其物理含义是<strong>数值依赖域必须包含解析依赖域</strong>：信息传播速度 $c$ 对应特征线斜率，时间步长不能大于信息跨越一个网格间距所需时间。"))+
   note(p("CFL（Courant-Friedrichs-Lewy）条件是一切显式双曲型格式的必要稳定条件。"))
 )},
{"id":"cp7s3-2","name":"二阶波动方程的显式格式","tags":["der","thm"],"brief":"时间和空间都用中心差分的三层格式。",
 "body": wrap(
   thm("波动方程显式格式", p("对 $u_{tt}=c^2u_{xx}$，时间空间均用中心差分：")+
   fml("\\frac{u_i^{n+1}-2u_i^n+u_i^{n-1}}{\\Delta t^2}=c^2\\frac{u_{i+1}^n-2u_i^n+u_{i-1}^n}{\\Delta x^2}")+
   p("整理得")+
   fml("u_i^{n+1}=2u_i^n-u_i^{n-1}+\\mu^2\\left(u_{i+1}^n-2u_i^n+u_{i-1}^n\\right),\\quad \\mu=\\frac{c\\Delta t}{\\Delta x}"))+
   der(p("<strong>启动：</strong>三层格式需要前两个时间层，第二层由初值 $u(x,0)$ 与 $u_t(x,0)$ 用二阶公式构造：")+
   fml("u_i^1=u_i^0+\\Delta t\\,v(x_i)+\\frac{\\mu^2}{2}\\left(u_{i+1}^0-2u_i^0+u_{i-1}^0\\right)")+
   p("其中 $v=u_t(x,0)$。格式的条件为 $\\mu\\le1$，即 CFL 条件。"))+
   note(p("当 $\\mu=1$ 时该格式精确（无数值色散），是理论上最优的选择。"))
 )},
{"id":"cp7s3-3","name":"数值色散与耗散","tags":["der","note"],"brief":"离散格式引起的相速度误差与振幅衰减。",
 "body": wrap(
   der(p("<strong>数值色散：</strong>把离散平面波 $u_i^n=e^{i(\\omega n\\Delta t-k i\\Delta x)}$ 代入格式，可解出数值相速度 $c_{num}$ 与波数 $k$ 有关：")+
   fml("\\frac{c_{num}}{c}=\\frac{\\sin(k\\Delta x)}{k\\Delta x}\\ （\\text{当 }\\mu=1）")+
   p("短波（$k\\Delta x$ 大）的数值相速度偏小，导致不同波数分量以不同速度传播，波形在传播中变形，称为数值色散。")+
   p("<strong>数值耗散：</strong>某些格式（如 Lax-Friedrichs、迎风）会引入额外阻尼，使波幅衰减，表现为解的「抹平」效应。"))+
   note(p("数值色散与耗散是离散误差在波传播问题中的两种主要表现；高阶或紧致格式能减小色散，但需权衡计算量与稳定性。"))
 )},
]},
{
"name": "7.4 椭圆型方程（拉普拉斯）",
"color": "#7c3aed",
"desc": "拉普拉斯/泊松方程的五点差分与迭代求解",
"items": [
{"id":"cp7s4-1","name":"五点差分格式","tags":["der","def"],"brief":"二维拉普拉斯算子的五点离散。",
 "fig":"laplace_grid","figCap":"五点差分格式：中心节点值为四邻节点值的平均",
 "body": wrap(
   defn("泊松方程", p("")+
   fml("-\\left(\\frac{\\partial^2u}{\\partial x^2}+\\frac{\\partial^2u}{\\partial y^2}\\right)=f(x,y)"))+
   der(p("<strong>离散化：</strong>对 $x,y$ 方向都用二阶中心差分：")+
   fml("\\frac{u_{i+1,j}-2u_{ij}+u_{i-1,j}}{\\Delta x^2}+\\frac{u_{i,j+1}-2u_{ij}+u_{i,j-1}}{\\Delta y^2}=f_{ij}")+
   p("取正方形网格 $\\Delta x=\\Delta y=h$，整理得五点格式：")+
   fml("u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u_{ij}=h^2f_{ij}")+
   p("当 $f=0$（拉普拉斯方程）时，中心值等于四邻平均：")+
   fml("u_{ij}=\\frac{1}{4}\\left(u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}\\right)"))+
   note(p("五点格式的截断误差为 $O(h^2)$；该线性系统是稀疏的（每行至多 5 个非零元），适合迭代求解。"))
 )},
{"id":"cp7s4-2","name":"迭代法求解椭圆型方程","tags":["der","app"],"brief":"Jacobi、Gauss-Seidel 与 SOR 迭代。",
 "body": wrap(
   der(p("<strong>Jacobi 迭代：</strong>")+
   fml("u_{ij}^{(k+1)}=\\frac{1}{4}\\left(u_{i+1,j}^{(k)}+u_{i-1,j}^{(k)}+u_{i,j+1}^{(k)}+u_{i,j-1}^{(k)}-h^2f_{ij}\\right)")+
   p("<strong>Gauss-Seidel：</strong>用已更新的值，收敛约为 Jacobi 的两倍。")+
   p("<strong>SOR 超松弛：</strong>引入松弛因子 $\\omega$（$1<\\omega<2$）加速：")+
   fml("u_{ij}^{(k+1)}=(1-\\omega)u_{ij}^{(k)}+\\omega\\,u_{ij}^{GS}")+
   p("对 $N\\times N$ 网格，最优因子 $\\omega_{opt}=\\frac{2}{1+\\sin(\\pi/N)}$，收敛速度由 $O(N^2)$ 次迭代改善到 $O(N)$ 次。"))+
   app(p("<strong>应用：</strong>椭圆型方程用于静电场、稳态传热与势流问题；大规模问题用多重网格或 Krylov 方法（CG）求解更高效。"))
 )},
{"id":"cp7s4-3","name":"边界条件的处理","tags":["der","note"],"brief":"Dirichlet 与 Neumann 边界的离散处理。",
 "body": wrap(
   der(p("<strong>Dirichlet 边界：</strong>边界值已知，直接代入即可；边界节点方程无需组装，作为已知项移到右端。")+
   p("<strong>Neumann 边界：</strong>给定法向导数 $\\frac{\\partial u}{\\partial n}=g$。以一维为例，在边界 $x_0$ 用中心差商引入虚拟节点 $x_{-1}$：")+
   fml("\\frac{u_1-u_{-1}}{2h}=g\\ \\Rightarrow\\ u_{-1}=u_1-2hg")+
   p("把虚拟节点代入内部方程消去，即得含边界导数的修正方程。")+
   p("<strong>处理要点：</strong>Neumann 问题需满足相容性条件（净通量为零），否则解不存在；离散系统为奇异，须固定一个参考值。"))+
   note(p("边界条件处理不当是椭圆型问题数值解出现阶数降低或振荡的主要原因，尤其对曲线边界需注意。"))
 )},
]},
{
"name": "7.5 稳定性与收敛性",
"color": "#818cf8",
"desc": "冯·诺依曼稳定性分析、Lax 等价定理与收敛性",
"items": [
{"id":"cp7s5-1","name":"von Neumann 稳定性分析","tags":["thm","der"],"brief":"用傅里叶模式分析放大因子判断稳定性。",
 "fig":"stability","figCap":"von Neumann 分析：放大因子须落在单位圆内",
 "body": wrap(
   thm("von Neumann 条件", p("设误差按傅里叶模式 $\\varepsilon_i^n=g^n e^{ik i\\Delta x}$ 传播，则格式稳定的充要条件是放大因子满足")+
   fml("|g(\\theta)|\\le1,\\qquad \\forall\\,\\theta=k\\Delta x"))+
   der(p("<strong>热方程显式格式分析：</strong>代入 $u_i^n=g^ne^{ii\\theta}$：")+
   fml("g=1+r\\left(e^{i\\theta}-2+e^{-i\\theta}\\right)=1+2r(\\cos\\theta-1)=1-4r\\sin^2\\frac{\\theta}{2}")+
   p("要求 $|g|\\le1$，下界条件 $g\\ge-1$ 给出")+
   fml("1-4r\\sin^2\\frac{\\theta}{2}\\ge-1\\ \\Rightarrow\\ r\\le\\frac{1}{2\\sin^2(\\theta/2)}")+
   p("对最不利的 $\\theta=\\pi$（$\\sin^2=1$）得 $r\\le\\frac12$，即显式热方程格式的稳定条件。"))+
   note(p("von Neumann 分析简单有效，适用于线性常系数格式；对变系数或非线性问题只能给出局部或必要的稳定性判据。"))
 )},
{"id":"cp7s5-2","name":"矩阵方法与稳定性准则","tags":["der","note"],"brief":"用放大矩阵的谱半径刻画稳定性。",
 "body": wrap(
   der(p("<strong>矩阵稳定性：</strong>把格式写为 $\\mathbf{u}^{n+1}=M\\mathbf{u}^n$，则稳定性要求")+
   fml("\\rho(M)\\le1")+
   p("若 $M$ 正规（如对称矩阵），则 $\\|M\\|_2=\\rho(M)$，等价于所有特征值模不超过 1。对热方程显式格式，$M$ 对称三对角，特征值")+
   fml("\\lambda_j=1-4r\\sin^2\\frac{j\\pi}{2N}")+
   p("最大模由 $j=N$ 给出 $|1-4r|\\le1$，同样得 $r\\le\\frac12$。"))+
   note(p("<strong>其他准则：</strong>对非线性问题用能量法（证明离散能量不增长），对双曲问题用 CFL 条件（依赖域），三者互为补充。"))
 )},
{"id":"cp7s5-3","name":"Lax 等价定理与收敛性","tags":["thm","note"],"brief":"相容加稳定等价于收敛。",
 "body": wrap(
   thm("Lax 等价定理", p("对适定的线性初值问题，若数值格式相容，则稳定性与收敛性等价：")+
   fml("\\text{相容}+\\text{稳定}\\iff\\text{收敛}"))+
   der(p("<strong>意义：</strong>它把难以直接验证的收敛性问题（真实解与数值解之差）转化为较易验证的稳定性问题。")+
   p("收敛指当 $\\Delta x,\\Delta t\\to0$ 时数值解趋于真解；相容指截断误差趋于零；稳定性指误差不随时间步无限增长。")+
   p("因此数值分析的标准流程是：先验证相容性（泰勒展开），再验证稳定性（von Neumann/矩阵/能量法），最后由 Lax 定理断言收敛。"))+
   note(p("Lax 定理要求问题是适定的线性问题；非线性问题需借助更精细的稳定性与紧性论证。"))
 )},
]},
]
CHAPTERS = [
    {"id":"cp-ch1","num":"第一章","title":"多项式插值","en":"POLYNOMIAL INTERPOLATION",
     "desc":"插值问题的存在唯一性、拉格朗日插值与基函数、牛顿插值与差商、埃尔米特插值、三次样条与三弯矩方程、插值余项、龙格现象与切比雪夫节点。",
     "sections": ch1_sections},
    {"id":"cp-ch2","num":"第二章","title":"数值微分","en":"NUMERICAL DIFFERENTIATION",
     "desc":"差商近似与泰勒展开截断误差、前向与中心差商、二阶导数差分、高阶差分与待定系数法、插值型求导、理查森外推、误差平衡与最优步长、噪声数据的正则化微分。",
     "sections": ch2_sections},
    {"id":"cp-ch3","num":"第三章","title":"数值积分","en":"NUMERICAL INTEGRATION",
     "desc":"梯形公式与辛普森公式、复合求积与误差、牛顿-柯特斯公式与柯特斯系数、代数精度、龙贝格积分与 Richardson 外推、高斯求积与高斯-勒让德节点、蒙特卡洛积分与方差缩减。",
     "sections": ch3_sections},
    {"id":"cp-ch4","num":"第四章","title":"数值求解一元方程","en":"ROOT FINDING",
     "desc":"二分法与误差界、不动点迭代与压缩映射、收敛阶、牛顿迭代法与二次收敛、割线法与抛物线法、非线性方程组与雅可比矩阵、拟牛顿法。",
     "sections": ch4_sections},
    {"id":"cp-ch5","num":"第五章","title":"数值求解矩阵问题","en":"MATRIX COMPUTATIONS",
     "desc":"高斯消元与列主元、LU 分解与 Doolittle 递推、三对角方程组的追赶法、Gram-Schmidt 与 Householder QR 分解、最小二乘、Jacobi 与 Gauss-Seidel 迭代、幂法与瑞利商、QR 算法。",
     "sections": ch5_sections},
    {"id":"cp-ch6","num":"第六章","title":"数值求解常微分方程","en":"NUMERICAL ODE",
     "desc":"欧拉法与误差稳定性、改进欧拉法、二阶与四阶龙格-库塔、自适应步长、Adams 线性多步法、预估-校正、刚性方程与 A 稳定、隐式方法、边值问题的差分法与打靶法。",
     "sections": ch6_sections},
    {"id":"cp-ch7","num":"第七章","title":"数值求解偏微分方程","en":"NUMERICAL PDE",
     "desc":"网格与差分算子、截断误差与相容性、显式与隐式格式、热方程与 Crank-Nicolson、波动方程与 CFL 条件、数值色散与耗散、五点差分与迭代求解、von Neumann 稳定性分析与 Lax 等价定理。",
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
  .la-phase-title.cp-ch1::before{background:#2563eb}
  .la-phase-title.cp-ch2::before{background:#7c3aed}
  .la-phase-title.cp-ch3::before{background:#0d9488}
  .la-phase-title.cp-ch4::before{background:#c2410c}
  .la-phase-title.cp-ch5::before{background:#be185d}
  .la-phase-title.cp-ch6::before{background:#0891b2}
  .la-phase-title.cp-ch7::before{background:#4f46e5}
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
<meta name="description" content="计算物理知识体系：多项式插值、数值微分、数值积分、方程求根、矩阵计算、常微分方程、偏微分方程">
<title>计算物理 · 知识体系</title>
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
    <div class="la-eyebrow">COMPUTATIONAL PHYSICS · KNOWLEDGE MAP</div>
    <h1>计算物理 · 知识体系</h1>
    <p class="la-subtitle">多项式插值 · 数值微分 · 数值积分 · 方程求根 · 矩阵计算 · 常微分方程 · 偏微分方程</p>
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
    <div>计算物理 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于数值分析核心算法体系整理</div>
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
    with open("/workspace/computational-physics.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated computational-physics.html ({len(html)} chars)")
