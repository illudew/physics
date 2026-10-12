# -*- coding: utf-8 -*-
"""Generate newtonian-mechanics.html with 5 chapters: 运动学/动力学/功能/刚体/振动与波."""
import json

# ---------- SVG figure library ----------
FIG = {
"trajectory": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="140" x2="230" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="10" y1="140" x2="10" y2="10" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M 10 130 Q 120 10 230 100" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
<circle cx="10" cy="130" r="4" fill="#ef4444"/>
<circle cx="120" cy="40" r="4" fill="#ef4444"/>
<circle cx="230" cy="100" r="4" fill="#ef4444"/>
<line x1="120" y1="40" x2="145" y2="35" stroke="#10b981" stroke-width="2"/>
<polygon points="145,35 135,33 138,41" fill="#10b981"/>
<text x="148" y="32" font-size="11" fill="#10b981">v</text>
<text x="215" y="155" font-size="11" fill="#475569">x</text>
<text x="2" y="14" font-size="11" fill="#475569">y</text></svg>''',
"projectile": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="140" x2="230" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="10" y1="140" x2="10" y2="10" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M 10 140 Q 120 10 230 140" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
<line x1="10" y1="140" x2="60" y2="110" stroke="#ef4444" stroke-width="2.5"/>
<polygon points="60,110 50,112 55,120" fill="#ef4444"/>
<text x="62" y="108" font-size="11" fill="#ef4444">v₀</text>
<line x1="10" y1="140" x2="55" y2="140" stroke="#f59e0b" stroke-width="1.5"/>
<polygon points="55,140 47,136 47,144" fill="#f59e0b"/>
<text x="30" y="152" font-size="10" fill="#f59e0b">v₀cosθ</text>
<line x1="10" y1="140" x2="10" y2="115" stroke="#10b981" stroke-width="1.5"/>
<polygon points="10,115 6,123 14,123" fill="#10b981"/>
<text x="-4" y="125" font-size="10" fill="#10b981">v₀sinθ</text>
<text x="55" y="135" font-size="10" fill="#475569">θ</text></svg>''',
"circular": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="55" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="120" cy="80" r="3" fill="#475569"/>
<circle cx="175" cy="80" r="5" fill="#ef4444"/>
<line x1="120" y1="80" x2="175" y2="80" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3 3"/>
<text x="140" y="74" font-size="11" fill="#475569">r</text>
<line x1="175" y1="80" x2="175" y2="40" stroke="#10b981" stroke-width="2.5"/>
<polygon points="175,40 169,50 181,50" fill="#10b981"/>
<text x="180" y="42" font-size="11" fill="#10b981">v</text>
<line x1="175" y1="80" x2="120" y2="80" stroke="#ef4444" stroke-width="2.5"/>
<polygon points="120,80 130,74 130,86" fill="#ef4444"/>
<text x="122" y="72" font-size="11" fill="#ef4444">aₙ</text></svg>''',
"fbd": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="90" y="60" width="60" height="50" rx="6" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
<line x1="120" y1="110" x2="120" y2="150" stroke="#ef4444" stroke-width="2.5"/>
<polygon points="120,150 114,140 126,140" fill="#ef4444"/>
<text x="126" y="145" font-size="11" fill="#ef4444">mg</text>
<line x1="120" y1="60" x2="120" y2="20" stroke="#10b981" stroke-width="2.5"/>
<polygon points="120,20 114,30 126,30" fill="#10b981"/>
<text x="126" y="28" font-size="11" fill="#10b981">N</text>
<line x1="150" y1="85" x2="190" y2="85" stroke="#f59e0b" stroke-width="2.5"/>
<polygon points="190,85 180,79 180,91" fill="#f59e0b"/>
<text x="162" y="78" font-size="11" fill="#f59e0b">F</text></svg>''',
"inclined": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="140" x2="220" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="140" x2="200" y2="40" stroke="#64748b" stroke-width="3"/>
<rect x="100" y="78" width="36" height="26" rx="3" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5" transform="rotate(-30 118 91)"/>
<line x1="118" y1="104" x2="118" y2="138" stroke="#ef4444" stroke-width="2"/>
<polygon points="118,138 112,128 124,128" fill="#ef4444"/>
<text x="122" y="134" font-size="10" fill="#ef4444">mg</text>
<line x1="118" y1="91" x2="100" y2="60" stroke="#10b981" stroke-width="2"/>
<polygon points="100,60 106,70 112,62" fill="#10b981"/>
<text x="82" y="58" font-size="10" fill="#10b981">N</text>
<line x1="118" y1="91" x2="160" y2="115" stroke="#f59e0b" stroke-width="2"/>
<polygon points="160,115 150,110 152,120" fill="#f59e0b"/>
<text x="140" y="125" font-size="10" fill="#f59e0b">f</text></svg>''',
"pendulum": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="120" y1="10" x2="120" y2="130" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="120" y1="10" x2="165" y2="100" stroke="#475569" stroke-width="2"/>
<circle cx="165" cy="100" r="10" fill="#3b82f6"/>
<line x1="165" y1="100" x2="165" y2="135" stroke="#ef4444" stroke-width="2"/>
<polygon points="165,135 159,125 171,125" fill="#ef4444"/>
<text x="170" y="128" font-size="11" fill="#ef4444">mg</text>
<path d="M 120 50 A 40 40 0 0 1 165 100" fill="none" stroke="#94a3b8" stroke-width="1"/>
<text x="122" y="45" font-size="11" fill="#475569">θ</text>
<text x="138" y="60" font-size="10" fill="#64748b">L</text></svg>''',
"wave": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 10 80 Q 40 30 70 80 T 130 80 T 190 80 T 230 80" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
<line x1="70" y1="30" x2="70" y2="80" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3 3"/>
<text x="60" y="55" font-size="10" fill="#ef4444">A</text>
<line x1="10" y1="120" x2="130" y2="120" stroke="#10b981" stroke-width="1.5"/>
<polygon points="10,120 16,116 16,124" fill="#10b981"/>
<polygon points="130,120 124,116 124,124" fill="#10b981"/>
<text x="60" y="115" font-size="10" fill="#10b981">λ</text></svg>''',
"shm": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M 10 80 Q 40 30 70 80 T 130 80 T 190 80 T 230 80" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="70" cy="30" r="4" fill="#ef4444"/>
<circle cx="190" cy="130" r="4" fill="#ef4444"/>
<text x="74" y="26" font-size="10" fill="#ef4444">+A</text>
<text x="194" y="140" font-size="10" fill="#ef4444">-A</text>
<text x="100" y="70" font-size="10" fill="#475569">O</text></svg>''',
"rotation": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="50" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" opacity="0.5"/>
<circle cx="120" cy="80" r="3" fill="#475569"/>
<circle cx="160" cy="80" r="5" fill="#ef4444"/>
<line x1="120" y1="80" x2="160" y2="80" stroke="#94a3b8" stroke-width="1.5"/>
<text x="135" y="74" font-size="10" fill="#475569">r</text>
<path d="M 120 30 A 50 50 0 0 1 170 80" fill="none" stroke="#10b981" stroke-width="2" stroke-dasharray="4 3"/>
<text x="155" y="42" font-size="11" fill="#10b981">ω</text>
<line x1="160" y1="80" x2="160" y2="45" stroke="#3b82f6" stroke-width="2"/>
<polygon points="160,45 154,55 166,55" fill="#3b82f6"/>
<text x="165" y="50" font-size="11" fill="#3b82f6">v</text></svg>''',
"collision": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="100" x2="230" y2="100" stroke="#94a3b8" stroke-width="1.5"/>
<circle cx="70" cy="90" r="18" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
<text x="62" y="94" font-size="11" fill="#1e293b">m₁</text>
<circle cx="170" cy="90" r="18" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
<text x="162" y="94" font-size="11" fill="#1e293b">m₂</text>
<line x1="88" y1="90" x2="110" y2="90" stroke="#3b82f6" stroke-width="2"/>
<polygon points="110,90 102,86 102,94" fill="#3b82f6"/>
<text x="92" y="82" font-size="10" fill="#3b82f6">v₁</text>
<line x1="152" y1="90" x2="130" y2="90" stroke="#f59e0b" stroke-width="2"/>
<polygon points="130,90 138,86 138,94" fill="#f59e0b"/>
<text x="130" y="82" font-size="10" fill="#f59e0b">v₂</text></svg>''',
"com": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="140" x2="230" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="10" y1="140" x2="10" y2="10" stroke="#94a3b8" stroke-width="1.5"/>
<circle cx="70" cy="90" r="10" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
<text x="60" y="112" font-size="10" fill="#1e293b">m₁</text>
<circle cx="170" cy="60" r="14" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
<text x="160" y="85" font-size="10" fill="#1e293b">m₂</text>
<line x1="70" y1="90" x2="170" y2="60" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="4 3"/>
<circle cx="133" cy="72" r="5" fill="#ef4444"/>
<text x="138" y="66" font-size="11" fill="#ef4444" font-weight="bold">C</text>
<text x="138" y="80" font-size="9" fill="#94a3b8">质心</text>
<text x="80" y="105" font-size="9" fill="#64748b">r₁</text>
<text x="145" y="100" font-size="9" fill="#64748b">r₂</text></svg>''',
"oblique": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="120" y1="10" x2="120" y2="150" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3 3"/>
<circle cx="80" cy="80" r="16" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
<text x="72" y="84" font-size="11" fill="#1e293b">m₁</text>
<circle cx="160" cy="80" r="16" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
<text x="152" y="84" font-size="11" fill="#1e293b">m₂</text>
<line x1="55" y1="100" x2="78" y2="82" stroke="#3b82f6" stroke-width="2"/>
<polygon points="78,82 68,84 74,92" fill="#3b82f6"/>
<text x="40" y="108" font-size="10" fill="#3b82f6">v₁</text>
<line x1="96" y1="55" x2="100" y2="68" stroke="#0ea5e9" stroke-width="2"/>
<polygon points="100,68 92,64 96,60" fill="#0ea5e9"/>
<text x="100" y="52" font-size="10" fill="#0ea5e9">v₁'</text>
<line x1="178" y1="62" x2="200" y2="55" stroke="#f59e0b" stroke-width="2"/>
<polygon points="200,55 190,56 194,64" fill="#f59e0b"/>
<text x="200" y="50" font-size="10" fill="#f59e0b">v₂'</text></svg>''',
"beats": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 10 80 Q 35 20 60 80 T 110 80 T 160 80 T 210 80 T 230 80" fill="none" stroke="#3b82f6" stroke-width="1.5" opacity="0.5"/>
<path d="M 10 80 Q 30 30 50 80 Q 70 130 90 80 Q 110 30 130 80 Q 150 130 170 80 Q 190 30 210 80 Q 220 105 230 80" fill="none" stroke="#ef4444" stroke-width="2"/>
<path d="M 10 50 Q 60 50 110 80 Q 160 110 210 80" fill="none" stroke="#10b981" stroke-width="1" stroke-dasharray="5 4"/>
<text x="12" y="45" font-size="10" fill="#10b981">包络</text>
<text x="90" y="155" font-size="10" fill="#64748b">拍周期 T=1/|f₁-f₂|</text></svg>''',
"lissajous": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#e2e8f0" stroke-width="1"/>
<line x1="120" y1="10" x2="120" y2="150" stroke="#e2e8f0" stroke-width="1"/>
<path d="M 120 30 Q 200 50 200 80 Q 200 110 120 130 Q 40 110 40 80 Q 40 50 120 30 Z M 120 50 Q 175 62 175 80 Q 175 98 120 110 Q 65 98 65 80 Q 65 62 120 50 Z" fill="none" stroke="#8b5cf6" stroke-width="2"/>
<circle cx="120" cy="80" r="3" fill="#ef4444"/>
<text x="180" y="40" font-size="11" fill="#8b5cf6">ω_x:ω_y = 2:1</text>
<text x="14" y="25" font-size="10" fill="#64748b">y</text>
<text x="215" y="92" font-size="10" fill="#64748b">x</text></svg>''',
"halfwave": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="120" y1="10" x2="120" y2="150" stroke="#475569" stroke-width="2"/>
<text x="60" y="25" font-size="11" fill="#64748b" font-weight="700">介质1</text>
<text x="160" y="25" font-size="11" fill="#64748b" font-weight="700">介质2</text>
<text x="122" y="22" font-size="9" fill="#475569">界面</text>
<path d="M 20 80 Q 45 50 70 80 Q 95 110 120 80" fill="none" stroke="#3b82f6" stroke-width="2"/>
<text x="30" y="72" font-size="10" fill="#3b82f6">入射</text>
<path d="M 120 80 Q 145 110 170 80 Q 195 50 220 80" fill="none" stroke="#ef4444" stroke-width="2"/>
<text x="130" y="115" font-size="10" fill="#ef4444">反射(反相)</text>
<path d="M 120 80 Q 145 50 170 80 Q 195 110 220 80" fill="none" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="130" y="60" font-size="10" fill="#10b981">透射</text>
<text x="55" y="145" font-size="9" fill="#94a3b8">波疏→波密：反射波相位突变π（半波损失）</text></svg>''',
"inertia_shapes": '''<svg viewBox="0 0 240 180" xmlns="http://www.w3.org/2000/svg">
<g>
<rect x="15" y="20" width="80" height="8" fill="#94a3b8"/>
<line x1="55" y1="20" x2="55" y2="8" stroke="#475569" stroke-width="1.5" stroke-dasharray="2 2"/>
<text x="15" y="50" font-size="10" fill="#1e293b">细杆 中垂轴</text>
<text x="15" y="64" font-size="10" fill="#6366f1">I=¹⁄₁₂mL²</text>
</g>
<g transform="translate(120,0)">
<circle cx="55" cy="24" r="16" fill="none" stroke="#94a3b8" stroke-width="2"/>
<line x1="55" y1="24" x2="55" y2="8" stroke="#475569" stroke-width="1.5" stroke-dasharray="2 2"/>
<text x="15" y="60" font-size="10" fill="#1e293b">圆环 中心轴</text>
<text x="15" y="74" font-size="10" fill="#6366f1">I=mR²</text>
</g>
<g transform="translate(0,90)">
<circle cx="55" cy="24" r="16" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>
<line x1="55" y1="24" x2="55" y2="8" stroke="#475569" stroke-width="1.5" stroke-dasharray="2 2"/>
<text x="15" y="60" font-size="10" fill="#1e293b">圆盘 中心轴</text>
<text x="15" y="74" font-size="10" fill="#6366f1">I=½mR²</text>
</g>
<g transform="translate(120,90)">
<circle cx="55" cy="24" r="16" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>
<line x1="55" y1="24" x2="55" y2="8" stroke="#475569" stroke-width="1.5" stroke-dasharray="2 2"/>
<text x="15" y="60" font-size="10" fill="#1e293b">球体 球心轴</text>
<text x="15" y="74" font-size="10" fill="#6366f1">I=⅖mR²</text>
</g></svg>''',
"rolling": '''<svg viewBox="0 0 240 140" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="110" x2="230" y2="110" stroke="#94a3b8" stroke-width="2"/>
<circle cx="120" cy="80" r="30" fill="#dbeafe" stroke="#3b82f6" stroke-width="2.5"/>
<circle cx="120" cy="80" r="3" fill="#475569"/>
<line x1="120" y1="80" x2="120" y2="110" stroke="#ef4444" stroke-width="2" stroke-dasharray="4 3"/>
<text x="124" y="100" font-size="11" fill="#ef4444">R</text>
<line x1="120" y1="80" x2="180" y2="80" stroke="#10b981" stroke-width="2.5"/>
<polygon points="180,80 170,75 170,85" fill="#10b981"/>
<text x="160" y="72" font-size="11" fill="#10b981">v_C=ωR</text>
<text x="110" y="125" font-size="10" fill="#64748b">P 接触点(v=0)</text>
<path d="M 120 50 A 30 30 0 0 1 150 80" fill="none" stroke="#8b5cf6" stroke-width="2" stroke-dasharray="4 3"/>
<text x="130" y="55" font-size="11" fill="#8b5cf6">ω</text></svg>''',
"phasor": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="120" x2="220" y2="120" stroke="#cbd5e1" stroke-width="1"/>
<line x1="120" y1="10" x2="120" y2="140" stroke="#cbd5e1" stroke-width="1"/>
<line x1="120" y1="120" x2="195" y2="55" stroke="#3b82f6" stroke-width="3"/>
<polygon points="195,55 183,55 190,67" fill="#3b82f6"/>
<circle cx="120" cy="120" r="3" fill="#475569"/>
<circle cx="195" cy="120" r="4" fill="#ef4444"/>
<line x1="195" y1="55" x2="195" y2="120" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="200" y="118" font-size="11" fill="#ef4444">x</text>
<text x="160" y="80" font-size="12" fill="#3b82f6" font-weight="bold">A</text>
<text x="155" y="115" font-size="10" fill="#64748b">ωt+φ</text>
<path d="M 155 120 A 35 35 0 0 1 175 105" fill="none" stroke="#f59e0b" stroke-width="1.5"/>
<text x="215" y="125" font-size="10" fill="#475569">x</text>
<text x="110" y="8" font-size="10" fill="#475569">y</text></svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

# ---------- 核心公式清单 ----------
CORE_FORMULAS = [
    ("速度定义", "\\mathbf{v} = \\frac{d\\mathbf{r}}{dt}", "位置矢量对时间的导数"),
    ("加速度定义", "\\mathbf{a} = \\frac{d\\mathbf{v}}{dt} = \\frac{d^2\\mathbf{r}}{dt^2}", "速度对时间的导数"),
    ("匀变速直线运动", "v = v_0 + at,\\quad x = x_0 + v_0 t + \\tfrac{1}{2}at^2", "加速度恒定的运动学方程"),
    ("速度-位移关系", "v^2 - v_0^2 = 2a(x-x_0)", "不含时间的运动学关系"),
    ("抛体运动轨迹", "y = x\\tan\\theta - \\frac{g x^2}{2 v_0^2 \\cos^2\\theta}", "抛物线轨迹方程"),
    ("向心加速度", "a_n = \\frac{v^2}{r} = \\omega^2 r", "匀速圆周运动的法向加速度"),
    ("牛顿第二定律", "\\mathbf{F} = m\\mathbf{a} = \\frac{d\\mathbf{p}}{dt}", "力等于动量变化率"),
    ("动量", "\\mathbf{p} = m\\mathbf{v}", "质量与速度的乘积"),
    ("冲量", "\\mathbf{I} = \\int_{t_1}^{t_2} \\mathbf{F}\\,dt = \\Delta\\mathbf{p}", "冲量等于动量变化"),
    ("动量守恒", "\\sum m_i \\mathbf{v}_i = \\text{常量} \\quad (\\sum \\mathbf{F}_{ext}=0)", "合外力为零时动量守恒"),
    ("功", "W = \\int_{a}^{b} \\mathbf{F}\\cdot d\\mathbf{r}", "力沿路径的线积分"),
    ("动能", "E_k = \\frac{1}{2} m v^2", "运动物体具有的能量"),
    ("动能定理", "W_{\\text{合}} = \\Delta E_k = \\tfrac{1}{2}mv^2 - \\tfrac{1}{2}mv_0^2", "合外力做功等于动能变化"),
    ("功率", "P = \\mathbf{F}\\cdot\\mathbf{v} = \\frac{dW}{dt}", "做功的快慢"),
    ("重力势能", "E_p = mgh", "重力场中的势能"),
    ("弹性势能", "E_p = \\frac{1}{2} k x^2", "弹簧形变储存的势能"),
    ("机械能守恒", "E_k + E_p = \\text{常量} \\quad (\\text{只有保守力做功})", "动能与势能之和不变"),
    ("转动惯量", "I = \\sum m_i r_i^2 = \\int r^2 dm", "刚体转动惯性的量度"),
    ("转动定律", "M = I\\beta = \\frac{dL}{dt}", "合外力矩等于角动量变化率"),
    ("角动量", "L = I\\omega = \\mathbf{r}\\times m\\mathbf{v}", "转动惯性与角速度的乘积"),
    ("角动量守恒", "L = I\\omega = \\text{常量} \\quad (\\sum M_{ext}=0)", "合外力矩为零时角动量守恒"),
    ("转动动能", "E_k = \\frac{1}{2} I \\omega^2", "刚体转动动能"),
    ("简谐振动方程", "x = A\\cos(\\omega t + \\varphi)", "简谐振动的位移表达式"),
    ("角频率", "\\omega = \\sqrt{\\frac{k}{m}} = 2\\pi f = \\frac{2\\pi}{T}", "弹簧振子的固有角频率"),
    ("单摆周期", "T = 2\\pi\\sqrt{\\frac{L}{g}}", "小角度近似下单摆周期"),
    ("波速", "v = \\lambda f = \\frac{\\lambda}{T}", "波长、频率与波速的关系"),
    ("简谐波方程", "y = A\\cos\\left[\\omega\\left(t - \\frac{x}{v}\\right) + \\varphi\\right]", "沿 x 正方向传播的简谐波"),
    ("驻波方程", "y = 2A\\cos\\frac{2\\pi x}{\\lambda}\\cos\\omega t", "两列反向行波叠加形成驻波"),
    ("质心位置", "\\mathbf{r}_C = \\frac{1}{M}\\sum_i m_i\\mathbf{r}_i", "质点系质心的质量加权平均位置"),
    ("质心运动定理", "\\sum \\mathbf{F}_{\\text{外}} = M\\mathbf{a}_C", "合外力等于总质量乘质心加速度"),
    ("拍频", "f_{\\text{拍}} = |f_1 - f_2|", "两频率相近振动合成的拍频"),
    ("反射系数", "\\frac{A_r}{A_i} = \\frac{Z_1-Z_2}{Z_1+Z_2}", "波在界面反射的振幅比，Z=ρv 为波阻"),
    ("自由落体", "v = gt,\\quad h = \\tfrac{1}{2}gt^2,\\quad v^2 = 2gh", "初速度为零的匀加速直线运动"),
    ("竖直上抛最大高度", "H = \\frac{v_0^2}{2g},\\quad T = \\frac{2v_0}{g}", "竖直上抛的最大高度与总飞行时间"),
    ("切向与法向加速度", "\\mathbf{a} = \\frac{dv}{dt}\\boldsymbol{\\tau} + \\frac{v^2}{\\rho}\\mathbf{n}", "自然坐标系下加速度分解为切向与法向"),
    ("惯性力", "\\mathbf{F}_{\\text{惯}} = -m\\mathbf{a}_0", "平移非惯性系中引入的虚拟力"),
    ("超重与失重", "N = m(g \\pm a)", "加速参考系中的视重"),
    ("阿特伍德机加速度", "a = \\frac{m_1-m_2}{m_1+m_2}g", "绳连接两物体的加速度"),
    ("角动量", "\\mathbf{L} = \\mathbf{r} \\times m\\mathbf{v}", "质点对参考点的角动量"),
    ("力矩与角动量定理", "\\mathbf{M} = \\mathbf{r} \\times \\mathbf{F} = \\frac{d\\mathbf{L}}{dt}", "力矩等于角动量的变化率"),
    ("引力势能", "E_p = -G\\frac{m_1 m_2}{r}", "取无穷远为势能零点"),
    ("保守力与势能", "F = -\\frac{dE_p}{dx}", "一维保守力等于势能负梯度"),
    ("功率", "P = \\frac{dW}{dt} = \\mathbf{F}\\cdot\\mathbf{v}", "单位时间内做的功"),
    ("碰撞动能损失", "\\Delta E_k = \\tfrac{1}{2}\\frac{m_1m_2}{m_1+m_2}(1-e^2)(v_1-v_2)^2", "非弹性碰撞中动能损失与恢复系数关系"),
    ("柯尼希定理", "E_k = \\tfrac{1}{2}M v_C^2 + \\sum_i \\tfrac{1}{2}m_i v_i'^2", "总动能等于质心动能加相对质心动能"),
    ("垂直轴定理", "I_z = I_x + I_y", "薄板刚体对垂直板面轴的转动惯量"),
    ("纯滚动条件", "v_C = \\omega R,\\quad a_C = \\beta R", "滚动而不滑动的运动学关系"),
    ("转动动能", "E_k = \\tfrac{1}{2}I\\omega^2", "刚体绕定轴转动的动能"),
    ("进动角速度", "\\Omega = \\frac{M}{L} = \\frac{mgd}{I\\omega}", "陀螺在重力矩下的进动角速度"),
    ("同频振动合成振幅", "A = \\sqrt{A_1^2+A_2^2+2A_1A_2\\cos(\\varphi_2-\\varphi_1)}", "两同方向同频率振动合成"),
    ("波的强度", "I = \\tfrac{1}{2}\\rho\\omega^2 A^2 v", "平均能流密度，与振幅平方成正比"),
    ("多普勒效应", "f = \\frac{v+v_O}{v-v_S}f_0", "波源与观察者相对运动时的接收频率"),
    ("声强级", "L = 10\\lg\\frac{I}{I_0},\\quad I_0=10^{-12}\\,\\text{W/m}^2", "声强的分贝对数标度"),
]

# ---------- helper functions ----------
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
#  CHAPTER 1: 质点运动学
# =====================================================
ch1_sections = [
# ---- 1.1 位置、位移与速度 ----
{
"name": "1.1 位置矢量与位移",
"color": "#2563eb",
"desc": "位置矢量、位移矢量、速度的定义与性质",
"items": [
{"id":"c1s1-1","name":"位置矢量与位移","tags":["def","der"],"brief":"用矢量描述质点的空间位置及其变化。",
 "fig":"trajectory","figCap":"质点的运动轨迹与位置矢量",
 "body": wrap(
   defn("位置矢量",p("设参考点为原点 $O$，质点在时刻 $t$ 的位置由从 $O$ 指向质点的矢量 $\\mathbf{r}(t)$ 描述，称为<strong>位置矢量</strong>（位矢）。在直角坐标系中：")+
   fml("\\mathbf{r}(t) = x(t)\\,\\mathbf{i} + y(t)\\,\\mathbf{j} + z(t)\\,\\mathbf{k}"))+
   defn("位移矢量",p("质点从位置 $\\mathbf{r}_1$ 到 $\\mathbf{r}_2$ 的<strong>位移</strong>为：")+
   fml("\\Delta\\mathbf{r} = \\mathbf{r}_2 - \\mathbf{r}_1 = \\Delta x\\,\\mathbf{i}+\\Delta y\\,\\mathbf{j}+\\Delta z\\,\\mathbf{k}"))+
   note(p("位移是矢量，只取决于始末位置，与路径无关。路程（标量）是实际轨迹长度，$\\Delta s \\ge |\\Delta\\mathbf{r}|$，仅当单向直线运动时取等号。"))+
   defn("速度",p("速度是位矢对时间的变化率，描述运动的快慢和方向：")+
   fml("\\mathbf{v} = \\lim_{\\Delta t\\to 0}\\frac{\\Delta\\mathbf{r}}{\\Delta t} = \\frac{d\\mathbf{r}}{dt}"))+
   der(p("<strong>速度的分量形式：</strong>将 $\\mathbf{r}=x\\mathbf{i}+y\\mathbf{j}+z\\mathbf{k}$ 代入速度定义，注意 $\\mathbf{i},\\mathbf{j},\\mathbf{k}$ 为常矢量（方向不变）：")+
   fml("\\mathbf{v} = \\frac{dx}{dt}\\mathbf{i}+\\frac{dy}{dt}\\mathbf{j}+\\frac{dz}{dt}\\mathbf{k} = v_x\\mathbf{i}+v_y\\mathbf{j}+v_z\\mathbf{k}")+
   p("速率 $v=|\\mathbf{v}|=\\sqrt{v_x^2+v_y^2+v_z^2}$。瞬时速度的方向沿轨迹切线方向。"))
 )},
{"id":"c1s1-2","name":"加速度","tags":["def","der"],"brief":"速度的变化率，描述速度改变的快慢。",
 "body": wrap(
   defn("加速度",p("加速度是速度对时间的变化率：")+
   fml("\\mathbf{a} = \\lim_{\\Delta t\\to 0}\\frac{\\Delta\\mathbf{v}}{\\Delta t} = \\frac{d\\mathbf{v}}{dt} = \\frac{d^2\\mathbf{r}}{dt^2}"))+
   der(p("<strong>分量形式：</strong>")+
   fml("\\mathbf{a} = \\frac{dv_x}{dt}\\mathbf{i}+\\frac{dv_y}{dt}\\mathbf{j}+\\frac{dv_z}{dt}\\mathbf{k} = a_x\\mathbf{i}+a_y\\mathbf{j}+a_z\\mathbf{k}")+
   p("加速度的方向是速度矢量变化 $\\Delta\\mathbf{v}$ 的极限方向，<strong>不一定</strong>沿速度方向。"))
 )},
]},
# ---- 1.2 匀变速直线运动 ----
{
"name": "1.2 匀变速直线运动",
"color": "#2563eb",
"desc": "加速度恒定的一维运动方程推导",
"items": [
{"id":"c1s2-1","name":"匀变速直线运动公式","tags":["thm","der"],"brief":"由加速度定义积分推出三大运动学公式。",
 "body": wrap(
   thm("匀变速直线运动",p("若质点做直线运动且加速度 $a$ 恒定，初速度 $v_0$，初始位置 $x_0$，则：")+
   fml("v = v_0 + at")+fml("x = x_0 + v_0 t + \\tfrac{1}{2} a t^2")+fml("v^2 - v_0^2 = 2a(x-x_0)"))+
   der(p("<strong>推导（积分法）：</strong>由 $a=\\frac{dv}{dt}$，分离变量 $dv=a\\,dt$，从 $t=0$ 到 $t$ 积分：")+
   fml("\\int_{v_0}^{v} dv = a\\int_0^t dt \\implies v - v_0 = at \\implies v = v_0 + at")+
   p("再由 $v=\\frac{dx}{dt}=v_0+at$，积分得位置：")+
   fml("\\int_{x_0}^{x} dx = \\int_0^t (v_0+at)\\,dt \\implies x-x_0 = v_0 t + \\tfrac{1}{2}at^2")+
   p("<strong>消去 $t$ 得速度-位移关系：</strong>由 $t=\\frac{v-v_0}{a}$ 代入位移公式：")+
   fml("x-x_0 = v_0\\cdot\\frac{v-v_0}{a} + \\tfrac{1}{2}a\\left(\\frac{v-v_0}{a}\\right)^2 = \\frac{v_0(v-v_0)}{a} + \\frac{(v-v_0)^2}{2a}")+
   fml("= \\frac{2v_0(v-v_0)+(v-v_0)^2}{2a} = \\frac{v^2-v_0^2}{2a}")+
   p("整理即得 $v^2-v_0^2=2a(x-x_0)$。"))
 )},
]},
# ---- 1.3 抛体运动 ----
{
"name": "1.3 抛体运动",
"color": "#2563eb",
"desc": "斜抛运动的轨迹、射程与最大高度推导",
"items": [
{"id":"c1s3-1","name":"抛体运动方程与轨迹","tags":["thm","der"],"brief":"将运动分解为水平匀速与竖直匀变速。",
 "fig":"projectile","figCap":"斜抛运动的速度分解与轨迹",
 "body": wrap(
   thm("抛体运动",p("设初速度 $v_0$ 与水平方向成 $\\theta$ 角，忽略空气阻力，则：")+
   fml("x = v_0\\cos\\theta\\cdot t,\\quad y = v_0\\sin\\theta\\cdot t - \\tfrac{1}{2}gt^2")+
   fml("\\text{轨迹：}\\quad y = x\\tan\\theta - \\frac{g x^2}{2 v_0^2\\cos^2\\theta}"))+
   der(p("<strong>运动分解：</strong>水平方向 $a_x=0$（匀速），竖直方向 $a_y=-g$（匀变速）。")+
   p("初速度分量：$v_{0x}=v_0\\cos\\theta$，$v_{0y}=v_0\\sin\\theta$。")+
   fml("x(t) = v_0\\cos\\theta\\cdot t,\\qquad y(t) = v_0\\sin\\theta\\cdot t - \\tfrac{1}{2}gt^2")+
   p("<strong>轨迹方程：</strong>由第一式解出 $t=\\frac{x}{v_0\\cos\\theta}$，代入 $y(t)$：")+
   fml("y = v_0\\sin\\theta\\cdot\\frac{x}{v_0\\cos\\theta} - \\tfrac{1}{2}g\\left(\\frac{x}{v_0\\cos\\theta}\\right)^2 = x\\tan\\theta - \\frac{g x^2}{2v_0^2\\cos^2\\theta}")+
   p("此为抛物线方程，故抛体运动轨迹为抛物线。"))+
   der(p("<strong>射程 $R$：</strong>令 $y=0$，除 $x=0$ 外的解为：")+
   fml("0 = x\\tan\\theta - \\frac{g x^2}{2v_0^2\\cos^2\\theta} \\implies x = \\frac{2v_0^2\\cos^2\\theta\\tan\\theta}{g} = \\frac{v_0^2\\sin 2\\theta}{g}")+
   p("当 $\\theta=45°$ 时射程最大 $R_{\\max}=\\frac{v_0^2}{g}$。")+
   p("<strong>最大高度 $H$：</strong>竖直方向速度为零时 $v_y=v_0\\sin\\theta-gt=0$，$t=\\frac{v_0\\sin\\theta}{g}$，代入 $y(t)$：")+
   fml("H = v_0\\sin\\theta\\cdot\\frac{v_0\\sin\\theta}{g} - \\tfrac{1}{2}g\\left(\\frac{v_0\\sin\\theta}{g}\\right)^2 = \\frac{v_0^2\\sin^2\\theta}{2g}"))
 )},
]},
# ---- 1.4 圆周运动 ----
{
"name": "1.4 圆周运动",
"color": "#2563eb",
"desc": "角量描述、向心加速度、切向加速度",
"items": [
{"id":"c1s4-1","name":"圆周运动的加速度","tags":["thm","der"],"brief":"法向（向心）加速度与切向加速度的推导。",
 "fig":"circular","figCap":"圆周运动的速度与向心加速度",
 "body": wrap(
   defn("角量描述",p("角速度 $\\omega=\\frac{d\\theta}{dt}$，角加速度 $\\beta=\\frac{d\\omega}{dt}$。线量与角量关系：")+
   fml("v = r\\omega,\\quad a_t = r\\beta,\\quad a_n = r\\omega^2"))+
   thm("向心加速度",p("匀速圆周运动中，加速度大小为 $a_n=\\frac{v^2}{r}=\\omega^2 r$，方向指向圆心。"))+
   der(p("<strong>向心加速度推导（矢量法）：</strong>设质点做半径为 $r$ 的匀速圆周运动，$t$ 时刻速度 $\\mathbf{v}$，$t+\\Delta t$ 时刻速度 $\\mathbf{v}'$，二者大小均为 $v$，夹角为 $\\Delta\\theta$。")+
   p("速度变化量 $|\\Delta\\mathbf{v}|=2v\\sin\\frac{\\Delta\\theta}{2}\\approx v\\Delta\\theta$（小角度近似）。")+
   fml("a_n = \\lim_{\\Delta t\\to 0}\\frac{|\\Delta\\mathbf{v}|}{\\Delta t} = \\lim_{\\Delta t\\to 0}\\frac{v\\Delta\\theta}{\\Delta t} = v\\frac{d\\theta}{dt} = v\\omega = \\frac{v^2}{r}")+
   p("当 $\\Delta t\\to 0$ 时，$\\Delta\\mathbf{v}$ 的方向趋于垂直于 $\\mathbf{v}$ 并指向圆心，故 $\\mathbf{a}_n$ 指向圆心。")+
   p("<strong>变速圆周运动：</strong>速度大小也变化，存在切向加速度 $a_t=\\frac{dv}{dt}=r\\beta$（沿切线方向），总加速度：")+
   fml("\\mathbf{a} = \\mathbf{a}_t + \\mathbf{a}_n,\\quad a = \\sqrt{a_t^2+a_n^2}"))
 )},
]},
# ---- 1.5 相对运动 ----
{
"name": "1.5 相对运动",
"color": "#2563eb",
"desc": "伽利略变换下的速度与加速度合成",
"items": [
{"id":"c1s5-1","name":"伽利略速度变换","tags":["thm","der"],"brief":"低速运动参考系间的速度合成法则。",
 "body": wrap(
   thm("伽利略变换",p("设 $S'$ 系相对 $S$ 系以速度 $\\mathbf{u}$ 平动，则质点在两系中的位矢、速度、加速度满足：")+
   fml("\\mathbf{r} = \\mathbf{r}' + \\mathbf{u} t,\\quad \\mathbf{v} = \\mathbf{v}' + \\mathbf{u},\\quad \\mathbf{a} = \\mathbf{a}'"))+
   der(p("<strong>推导：</strong>对 $\\mathbf{r}=\\mathbf{r}'+\\mathbf{u}t$ 求时间导数（$\\mathbf{u}$ 为常矢量）：")+
   fml("\\frac{d\\mathbf{r}}{dt} = \\frac{d\\mathbf{r}'}{dt} + \\mathbf{u} \\implies \\mathbf{v} = \\mathbf{v}' + \\mathbf{u}")+
   p("再求导得加速度：$\\mathbf{a}=\\frac{d\\mathbf{v}}{dt}=\\frac{d\\mathbf{v}'}{dt}=\\mathbf{a}'$，故加速度在伽利略变换下不变——这是牛顿力学的基础。"))+
   note(p("伽利略变换仅适用于低速（$v\\ll c$）情形，高速时需用洛伦兹变换。"))
 )},
]},
# ---- 1.6 参考系与坐标系 ----
{
"name": "1.6 参考系与坐标系",
"color": "#2563eb",
"desc": "参考系的选择与坐标系的建立",
"items": [
{"id":"c1s6-1","name":"参考系与坐标系","tags":["def","note"],"brief":"描述运动必须选定参考系，并建立坐标系定量表示。",
 "body": wrap(
   defn("参考系",p("为描述物体运动而选作标准的另一物体或物体系称为<strong>参考系</strong>。同一运动在不同参考系中的描述不同，运动的描述具有相对性。"))+
   defn("坐标系",p("为定量描述质点的位置，在参考系上建立<strong>坐标系</strong>。常用坐标系：<br>• <strong>直角坐标系</strong>：$(x,y,z)$，单位矢量 $\\mathbf{i},\\mathbf{j},\\mathbf{k}$ 为常矢量。<br>• <strong>平面极坐标系</strong>：$(r,\\theta)$，径向 $\\mathbf{e}_r$ 与横向 $\\mathbf{e}_\\theta$ 随位置变化。<br>• <strong>自然坐标系</strong>：沿轨迹建立切向 $\\boldsymbol{\\tau}$ 与法向 $\\mathbf{n}$。"))+
   note(p("参考系决定运动的定性描述，坐标系决定定量描述。选择合适坐标系可简化求解（圆周运动用极坐标，曲线运动用自然坐标）。"))
 )},
]},
# ---- 1.7 自由落体与竖直抛体运动 ----
{
"name": "1.7 自由落体与竖直抛体运动",
"color": "#2563eb",
"desc": "重力作用下的匀变速直线运动特例",
"items": [
{"id":"c1s7-1","name":"自由落体运动","tags":["thm","der"],"brief":"初速度为零、加速度为 g 的匀加速直线运动。",
 "body": wrap(
   thm("自由落体公式",p("物体由静止开始只受重力作用的运动，加速度 $g\\approx 9.8\\,\\text{m/s}^2$，取向下为正：")+
   fml("v = gt,\\quad h = \\tfrac{1}{2}gt^2,\\quad v^2 = 2gh"))+
   der(p("<strong>推导：</strong>自由落体是初速度 $v_0=0$、加速度 $a=g$ 的匀变速直线运动。代入 $v=v_0+at$、$x=v_0t+\\frac{1}{2}at^2$、$v^2-v_0^2=2ax$：")+
   fml("v = gt,\\qquad h = \\tfrac{1}{2}gt^2,\\qquad v^2 = 2gh"))+
   note(p("自由落体加速度与物体质量无关（伽利略实验），因为重力 $mg$ 产生的加速度 $a=F/m=g$ 与质量无关。"))
 )},
{"id":"c1s7-2","name":"竖直上抛运动","tags":["thm","der"],"brief":"竖直方向匀变速运动的上升与下落全过程。",
 "body": wrap(
   thm("竖直上抛公式",p("以抛出点为原点、向上为正方向，初速度 $v_0$ 向上，加速度 $a=-g$：")+
   fml("v = v_0 - gt,\\quad y = v_0 t - \\tfrac{1}{2}gt^2"))+
   der(p("<strong>最大高度：</strong>最高点 $v=0$，由 $v_0-gt=0$ 得上升时间 $t_{\\text{上}}=\\frac{v_0}{g}$。代入位移公式：")+
   fml("H = v_0\\cdot\\frac{v_0}{g} - \\tfrac{1}{2}g\\left(\\frac{v_0}{g}\\right)^2 = \\frac{v_0^2}{2g}")+
   p("<strong>总飞行时间：</strong>落回抛出点时 $y=0$，$v_0t-\\frac{1}{2}gt^2=0$，解得 $t=\\frac{2v_0}{g}$，故 $T=2t_{\\text{上}}$，上升与下落时间相等。")+
   p("<strong>落地速度：</strong>$v=v_0-g\\cdot\\frac{2v_0}{g}=-v_0$，大小与初速度相等、方向向下。"))
 )},
]},
# ---- 1.8 运动的合成与分解 ----
{
"name": "1.8 运动的合成与分解",
"color": "#2563eb",
"desc": "复杂运动分解为简单分运动的原理与方法",
"items": [
{"id":"c1s8-1","name":"运动的独立性与合成原理","tags":["thm","der"],"brief":"各分运动独立进行，合运动为分运动的矢量叠加。",
 "body": wrap(
   thm("运动的独立性原理",p("一个物体同时参与几个分运动时，各分运动独立进行、互不影响；合运动是各分运动的矢量叠加。"))+
   der(p("<strong>矢量叠加：</strong>位置、位移、速度、加速度都是矢量，满足平行四边形法则：")+
   fml("\\mathbf{r} = \\mathbf{r}_1 + \\mathbf{r}_2,\\quad \\mathbf{v} = \\mathbf{v}_1 + \\mathbf{v}_2,\\quad \\mathbf{a} = \\mathbf{a}_1 + \\mathbf{a}_2")+
   p("直角坐标系中各分量独立求解后再合成。例如抛体运动分解为水平匀速和竖直匀变速两个独立分运动。"))
 )},
{"id":"c1s8-2","name":"抛体运动的另一种分解","tags":["der","exa"],"brief":"将抛体运动分解为沿初速度方向的匀速和自由落体。",
 "body": wrap(
   der(p("<strong>分解方式二：</strong>除水平/竖直分解外，抛体运动还可分解为沿初速度方向的匀速直线运动和竖直方向的自由落体运动。任意时刻 $t$：")+
   fml("\\mathbf{v} = \\mathbf{v}_0 + \\mathbf{g}t,\\qquad \\mathbf{r} = \\mathbf{v}_0 t + \\tfrac{1}{2}\\mathbf{g}t^2")+
   p("第一项 $\\mathbf{v}_0t$ 表示沿初速度方向的匀速位移，第二项 $\\frac{1}{2}\\mathbf{g}t^2$ 表示自由落体位移。"))+
   exa(p("<strong>平抛：</strong>初速度水平 $v_0\\mathbf{i}$，则 $\\mathbf{r}=v_0t\\,\\mathbf{i}-\\frac{1}{2}gt^2\\mathbf{j}$，与水平/竖直分解结果一致。"))
 )},
]},
# ---- 1.9 曲线运动的切向与法向加速度 ----
{
"name": "1.9 曲线运动的切向与法向加速度",
"color": "#2563eb",
"desc": "自然坐标系下曲线运动加速度的分解",
"items": [
{"id":"c1s9-1","name":"切向加速度与法向加速度","tags":["thm","der"],"brief":"加速度分解为沿速度方向和垂直速度方向的分量。",
 "body": wrap(
   defn("自然坐标系",p("以质点所在位置为原点，建立随质点运动的正交坐标系：切向单位矢量 $\\boldsymbol{\\tau}$（沿速度方向）和法向单位矢量 $\\mathbf{n}$（指向轨迹凹侧）。"))+
   thm("加速度的分解",p("曲线运动中加速度可分解为切向分量和法向分量：")+
   fml("\\mathbf{a} = a_t\\,\\boldsymbol{\\tau} + a_n\\,\\mathbf{n},\\quad a_t = \\frac{dv}{dt},\\quad a_n = \\frac{v^2}{\\rho}"))+
   der(p("<strong>推导：</strong>速度 $\\mathbf{v}=v\\boldsymbol{\\tau}$，对时间求导：")+
   fml("\\mathbf{a} = \\frac{d\\mathbf{v}}{dt} = \\frac{dv}{dt}\\boldsymbol{\\tau} + v\\frac{d\\boldsymbol{\\tau}}{dt}")+
   p("$d\\boldsymbol{\\tau}/dt$ 方向沿法向（指向曲率中心），大小为 $v/\\rho$（$\\rho$ 为曲率半径）：")+
   fml("\\frac{d\\boldsymbol{\\tau}}{dt} = \\frac{v}{\\rho}\\mathbf{n} \\implies \\mathbf{a} = \\frac{dv}{dt}\\boldsymbol{\\tau} + \\frac{v^2}{\\rho}\\mathbf{n}")+
   p("切向加速度 $a_t=dv/dt$ 反映速度大小的变化，法向加速度 $a_n=v^2/\\rho$ 反映速度方向的变化。"))
 )},
{"id":"c1s9-2","name":"曲率半径与法向加速度","tags":["der","exa"],"brief":"由轨迹方程求曲率半径，进而求法向加速度。",
 "body": wrap(
   defn("曲率半径",p("曲线在某点的曲率 $\\kappa=\\frac{|d\\boldsymbol{\\tau}|}{ds}=\\frac{1}{\\rho}$，$\\rho$ 为曲率半径。对平面曲线 $y=f(x)$：")+
   fml("\\rho = \\frac{[1+(y')^2]^{3/2}}{|y''|}"))+
   der(p("<strong>抛体轨迹的曲率半径：</strong>轨迹 $y=x\\tan\\theta-\\frac{gx^2}{2v_0^2\\cos^2\\theta}$，求导：")+
   fml("y' = \\tan\\theta - \\frac{gx}{v_0^2\\cos^2\\theta},\\qquad y'' = -\\frac{g}{v_0^2\\cos^2\\theta}")+
   p("抛出点 $x=0$ 处 $y'=\\tan\\theta$：")+
   fml("\\rho_0 = \\frac{(1+\\tan^2\\theta)^{3/2}}{g/(v_0^2\\cos^2\\theta)} = \\frac{v_0^2}{g\\cos\\theta}")+
   p("最高点 $y'=0$：$\\rho_{\\text{顶}}=\\frac{v_0^2\\cos^2\\theta}{g}$。"))
 )},
]},
# ---- 1.10 相对运动的进一步讨论 ----
{
"name": "1.10 相对运动的进一步讨论",
"color": "#2563eb",
"desc": "牵连速度、相对速度与相对加速度",
"items": [
{"id":"c1s10-1","name":"牵连速度与相对速度","tags":["thm","der"],"brief":"绝对速度等于牵连速度与相对速度的矢量和。",
 "body": wrap(
   defn("三种速度",p("<strong>绝对速度</strong> $\\mathbf{v}_{\\text{绝}}$：质点相对静止系 $S$ 的速度。<br><strong>牵连速度</strong> $\\mathbf{v}_{\\text{牵}}$：运动系 $S'$ 相对 $S$ 的速度。<br><strong>相对速度</strong> $\\mathbf{v}_{\\text{相}}$：质点相对 $S'$ 的速度。"))+
   thm("速度合成定理",p("质点的绝对速度等于牵连速度与相对速度的矢量和：")+
   fml("\\mathbf{v}_{\\text{绝}} = \\mathbf{v}_{\\text{牵}} + \\mathbf{v}_{\\text{相}}"))+
   der(p("<strong>推导：</strong>由位矢关系 $\\mathbf{r}_{\\text{绝}} = \\mathbf{r}_{\\text{牵}} + \\mathbf{r}_{\\text{相}}$，对时间求导：")+
   fml("\\frac{d\\mathbf{r}_{\\text{绝}}}{dt} = \\frac{d\\mathbf{r}_{\\text{牵}}}{dt} + \\frac{d\\mathbf{r}_{\\text{相}}}{dt} \\implies \\mathbf{v}_{\\text{绝}} = \\mathbf{v}_{\\text{牵}} + \\mathbf{v}_{\\text{相}}"))
 )},
{"id":"c1s10-2","name":"相对加速度","tags":["thm","der"],"brief":"加速度的合成关系与牵连加速度。",
 "body": wrap(
   thm("加速度合成定理",p("若 $S'$ 相对 $S$ 平动（无转动），则：")+
   fml("\\mathbf{a}_{\\text{绝}} = \\mathbf{a}_{\\text{牵}} + \\mathbf{a}_{\\text{相}}"))+
   der(p("<strong>推导：</strong>对速度合成式求导：")+
   fml("\\frac{d\\mathbf{v}_{\\text{绝}}}{dt} = \\frac{d\\mathbf{v}_{\\text{牵}}}{dt} + \\frac{d\\mathbf{v}_{\\text{相}}}{dt} \\implies \\mathbf{a}_{\\text{绝}} = \\mathbf{a}_{\\text{牵}} + \\mathbf{a}_{\\text{相}}")+
   p("当 $S'$ 相对 $S$ 匀速平动时，$\\mathbf{a}_{\\text{牵}}=0$，故 $\\mathbf{a}_{\\text{绝}}=\\mathbf{a}_{\\text{相}}$，即伽利略变换下加速度不变。"))+
   note(p("若 $S'$ 相对 $S$ 有加速度，则两系中观测到的加速度不同，牛顿定律在非惯性系中不再直接成立，需引入惯性力（见第2章）。"))
 )},
]},
]

# =====================================================
#  CHAPTER 2: 质点动力学
# =====================================================
ch2_sections = [
# ---- 2.1 牛顿三大定律 ----
{
"name": "2.1 牛顿三大定律",
"color": "#0d9488",
"desc": "牛顿运动定律的表述与惯性系",
"items": [
{"id":"c2s1-1","name":"牛顿运动定律","tags":["thm","note"],"brief":"经典力学的三大基本定律。",
 "fig":"fbd","figCap":"自由体受力分析示意",
 "body": wrap(
   defn("第一定律（惯性定律）",p("任何物体都保持静止或匀速直线运动状态，直到外力迫使它改变这种状态为止。")+
   p("数学表达：$\\mathbf{F}=0 \\implies \\mathbf{v}=$ 常矢量。"))+
   defn("第二定律",p("物体动量的变化率与所受合外力成正比，方向沿合外力方向：")+
   fml("\\mathbf{F} = \\frac{d\\mathbf{p}}{dt} = \\frac{d(m\\mathbf{v})}{dt}")+
   p("当质量 $m$ 为常量时，$\\mathbf{F}=m\\mathbf{a}$。"))+
   defn("第三定律（作用与反作用）",p("两个物体间的作用力 $\\mathbf{F}_{12}$ 与反作用力 $\\mathbf{F}_{21}$ 大小相等、方向相反、作用在同一直线上：")+
   fml("\\mathbf{F}_{12} = -\\mathbf{F}_{21}"))+
   note(p("<strong>惯性系：</strong>牛顿第一定律成立的参考系称为惯性系。一切相对惯性系做匀速直线运动的参考系都是惯性系。地球可近似为惯性系。"))+
   note(p("第二定律的原始形式 $\\mathbf{F}=\\frac{d\\mathbf{p}}{dt}$ 比 $\\mathbf{F}=m\\mathbf{a}$ 更普遍，后者仅在质量不变时成立。在相对论中质量随速度变化，但 $\\mathbf{F}=\\frac{d\\mathbf{p}}{dt}$ 仍成立。"))
 )},
]},
# ---- 2.2 常见力 ----
{
"name": "2.2 常见力的分析",
"color": "#0d9488",
"desc": "重力、弹力、摩擦力的规律与受力分析",
"items": [
{"id":"c2s2-1","name":"重力、弹力与摩擦力","tags":["def","exa"],"brief":"力学中三种最基本的力。",
 "fig":"inclined","figCap":"斜面上物体的受力分析",
 "body": wrap(
   defn("重力",p("地球对物体的万有引力（近似），方向竖直向下：$G=mg$，其中 $g\\approx 9.8\\,\\text{m/s}^2$。"))+
   defn("弹力（胡克定律）",p("弹簧在弹性限度内，弹力大小与形变量成正比，方向指向原长位置：")+
   fml("F = -kx")+
   p("负号表示弹力方向与位移方向相反。"))+
   defn("摩擦力",p("<strong>静摩擦力</strong>：$0\\le f_s \\le f_{s\\max}=\\mu_s N$，方向与相对运动趋势相反。<br><strong>滑动摩擦力</strong>：$f_k=\\mu_k N$，方向与相对运动方向相反。"))+
   exa(p("<strong>斜面物体：</strong>倾角 $\\theta$，重力分解为沿斜面分量 $mg\\sin\\theta$ 和垂直斜面分量 $mg\\cos\\theta$。法向力 $N=mg\\cos\\theta$。若物体匀速下滑，则 $\\mu_k=\\tan\\theta$。"))
 )},
]},
# ---- 2.3 动量与冲量 ----
{
"name": "2.3 动量与冲量",
"color": "#0d9488",
"desc": "动量定理与冲量的定义",
"items": [
{"id":"c2s3-1","name":"动量定理","tags":["thm","der"],"brief":"合外力的冲量等于动量的变化。",
 "body": wrap(
   defn("动量",p("质点的动量定义为质量与速度的乘积：$\\mathbf{p}=m\\mathbf{v}$，是矢量。"))+
   defn("冲量",p("力在时间上的积累称为冲量：")+
   fml("\\mathbf{I} = \\int_{t_1}^{t_2} \\mathbf{F}\\,dt"))+
   thm("动量定理",p("质点所受合外力的冲量等于其动量的变化量：")+
   fml("\\mathbf{I} = \\Delta\\mathbf{p} = \\mathbf{p}_2 - \\mathbf{p}_1"))+
   der(p("<strong>推导：</strong>由牛顿第二定律 $\\mathbf{F}=\\frac{d\\mathbf{p}}{dt}$，两边乘以 $dt$ 并从 $t_1$ 到 $t_2$ 积分：")+
   fml("\\int_{t_1}^{t_2} \\mathbf{F}\\,dt = \\int_{\\mathbf{p}_1}^{\\mathbf{p}_2} d\\mathbf{p} = \\mathbf{p}_2 - \\mathbf{p}_1 = \\Delta\\mathbf{p}"))+
   note(p("动量定理是矢量方程，可分解为分量形式：$I_x=\\Delta p_x$，$I_y=\\Delta p_y$，$I_z=\\Delta p_z$。"))
 )},
]},
# ---- 2.4 动量守恒定律 ----
{
"name": "2.4 动量守恒定律",
"color": "#0d9488",
"desc": "系统动量守恒的条件与推导",
"items": [
{"id":"c2s4-1","name":"动量守恒定律","tags":["thm","der"],"brief":"系统不受外力时总动量保持不变。",
 "fig":"collision","figCap":"两体碰撞示意",
 "body": wrap(
   thm("动量守恒定律",p("当系统所受合外力为零时，系统的总动量保持不变：")+
   fml("\\sum_{i} m_i \\mathbf{v}_i = \\text{常量}"))+
   der(p("<strong>推导（两体系统）：</strong>设两质点质量 $m_1,m_2$，相互作用力 $\\mathbf{F}_{12}$ 和 $\\mathbf{F}_{21}$，由牛顿第三定律 $\\mathbf{F}_{12}=-\\mathbf{F}_{21}$。")+
   p("对两质点分别应用牛顿第二定律：")+
   fml("\\mathbf{F}_{12} = \\frac{d\\mathbf{p}_1}{dt},\\qquad \\mathbf{F}_{21} = \\frac{d\\mathbf{p}_2}{dt}")+
   p("两式相加：")+
   fml("\\mathbf{F}_{12}+\\mathbf{F}_{21} = \\frac{d}{dt}(\\mathbf{p}_1+\\mathbf{p}_2)")+
   p("由牛顿第三定律，左边为零，故：")+
   fml("\\frac{d}{dt}(\\mathbf{p}_1+\\mathbf{p}_2)=0 \\implies \\mathbf{p}_1+\\mathbf{p}_2 = \\text{常量}")+
   p("推广到多质点系统，内力成对抵消，合外力为零时总动量守恒。"))
 )},
]},
# ---- 2.5 碰撞 ----
{
"name": "2.5 碰撞问题",
"color": "#0d9488",
"desc": "弹性碰撞、非弹性碰撞与恢复系数",
"items": [
{"id":"c2s5-1","name":"弹性碰撞与恢复系数","tags":["thm","der"],"brief":"碰撞过程的动量与能量分析。",
 "body": wrap(
   defn("恢复系数",p("碰撞后相对速度与碰撞前相对速度之比的负值：")+
   fml("e = \\frac{v_2'-v_1'}{v_1-v_2}")+
   p("$e=1$ 为完全弹性碰撞，$e=0$ 为完全非弹性碰撞，$0<e<1$ 为非弹性碰撞。"))+
   thm("一维弹性碰撞",p("动量守恒 + 动能守恒：")+
   fml("m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'")+
   fml("\\tfrac{1}{2}m_1 v_1^2 + \\tfrac{1}{2}m_2 v_2^2 = \\tfrac{1}{2}m_1 v_1'^2 + \\tfrac{1}{2}m_2 v_2'^2"))+
   der(p("<strong>弹性碰撞速度公式推导：</strong>由动量守恒和动能守恒：")+
   fml("m_1(v_1-v_1') = m_2(v_2'-v_2) \\quad (1)")+
   fml("m_1(v_1^2-v_1'^2) = m_2(v_2'^2-v_2^2) \\implies m_1(v_1-v_1')(v_1+v_1') = m_2(v_2'-v_2)(v_2'+v_2)")+
   p("将 (1) 代入，约去 $m_1(v_1-v_1')=m_2(v_2'-v_2)$（非零情形）：")+
   fml("v_1+v_1' = v_2+v_2' \\implies v_1-v_2 = v_2'-v_1'")+
   p("即弹性碰撞中恢复系数 $e=1$。联立动量守恒解得：")+
   fml("v_1' = \\frac{(m_1-m_2)v_1+2m_2 v_2}{m_1+m_2},\\qquad v_2' = \\frac{(m_2-m_1)v_2+2m_1 v_1}{m_1+m_2}")+
   p("<strong>特例</strong>：若 $m_1=m_2$，则 $v_1'=v_2$，$v_2'=v_1$（速度交换）；若 $m_2\\gg m_1$ 且 $v_2=0$，则 $v_1'\\approx -v_1$，$v_2'\\approx 0$。"))+
   defn("质心系（零动量系）",p("质心系中系统总动量为零。质心速度 $v_C=\\frac{m_1 v_1+m_2 v_2}{m_1+m_2}$。各质点在质心系中的速度为 $u_1=v_1-v_C$，$u_2=v_2-v_C$。")+
   fml("m_1 u_1 + m_2 u_2 = 0"))+
   der(p("<strong>质心系中的弹性碰撞：</strong>由动量守恒 $m_1 u_1+m_2 u_2=m_1 u_1'+m_2 u_2'=0$，得 $u_2=-\\frac{m_1}{m_2}u_1$，$u_2'=-\\frac{m_1}{m_2}u_1'$。代入动能守恒：")+
   fml("\\tfrac{1}{2}m_1 u_1^2+\\tfrac{1}{2}m_2 u_2^2 = \\tfrac{1}{2}m_1 u_1'^2+\\tfrac{1}{2}m_2 u_2'^2")+
   fml("\\tfrac{1}{2}m_1 u_1^2\\left(1+\\frac{m_1}{m_2}\\right) = \\tfrac{1}{2}m_1 u_1'^2\\left(1+\\frac{m_1}{m_2}\\right)")+
   p("故 $u_1'^2=u_1^2$，即碰撞后各质点在质心系中速率不变、仅方向改变。弹性碰撞在质心系中表现为<strong>速度方向反转或偏转</strong>。"))
 )},
{"id":"c2s5-2","name":"斜碰（二维碰撞）","tags":["thm","der"],"brief":"二维弹性碰撞的动量分量守恒与散射角关系。",
 "fig":"oblique","figCap":"二维斜碰示意",
 "body": wrap(
   thm("二维弹性碰撞",p("二维碰撞中动量守恒分解为 x、y 分量，弹性碰撞动能仍守恒：")+
   fml("m_1 v_{1x}+m_2 v_{2x} = m_1 v_{1x}'+m_2 v_{2x}'")+
   fml("m_1 v_{1y}+m_2 v_{2y} = m_1 v_{1y}'+m_2 v_{2y}'"))+
   der(p("<strong>等质量静止靶的散射角关系：</strong>设 $m_1=m_2=m$，靶初始静止 $v_2=0$。动量守恒 $\\mathbf{v}_1=\\mathbf{v}_1'+\\mathbf{v}_2'$，动能守恒 $v_1^2=v_1'^2+v_2'^2$。")+
   p("将动量守恒式两边平方：$v_1^2 = v_1'^2 + v_2'^2 + 2\\mathbf{v}_1'\\cdot\\mathbf{v}_2'$。与动能守恒比较得 $2\\mathbf{v}_1'\\cdot\\mathbf{v}_2'=0$，即：")+
   fml("\\mathbf{v}_1' \\perp \\mathbf{v}_2'")+
   p("故等质量弹性碰撞中，若靶初始静止，则碰后两球速度<strong>互相垂直</strong>。这是台球碰撞的经典结论。"))
 )},
]},
# ---- 2.6 质心运动定理 ----
{
"name": "2.6 质心运动定理",
"color": "#0d9488",
"desc": "质心的定义、质心速度与质心运动定理",
"items": [
{"id":"c2s6-1","name":"质心与质心运动定理","tags":["def","thm","der"],"brief":"系统质心的运动如同一个质点的运动。",
 "fig":"com","figCap":"两质点系统的质心 C",
 "body": wrap(
   defn("质心",p("质点系的质心位置矢量定义为各质元位置的质量加权平均：")+
   fml("\\mathbf{r}_C = \\frac{\\sum_i m_i \\mathbf{r}_i}{\\sum_i m_i} = \\frac{1}{M}\\sum_i m_i \\mathbf{r}_i,\\quad M=\\sum m_i")+
   p("对连续体：$\\mathbf{r}_C = \\frac{1}{M}\\int \\mathbf{r}\\,dm$。"))+
   thm("质心运动定理",p("质点系所受合外力等于总质量乘以质心加速度：")+
   fml("\\sum \\mathbf{F}_{\\text{外}} = M \\mathbf{a}_C = M\\frac{d^2\\mathbf{r}_C}{dt^2}"))+
   der(p("<strong>推导：</strong>对质心定义式求二阶导数：")+
   fml("M\\frac{d^2\\mathbf{r}_C}{dt^2} = \\sum_i m_i \\frac{d^2\\mathbf{r}_i}{dt^2} = \\sum_i m_i \\mathbf{a}_i")+
   p("由牛顿第二定律，$m_i\\mathbf{a}_i = \\mathbf{F}_i^{\\text{外}} + \\sum_{j\\neq i}\\mathbf{F}_{ij}^{\\text{内}}$。对所有质元求和：")+
   fml("\\sum_i m_i\\mathbf{a}_i = \\sum_i \\mathbf{F}_i^{\\text{外}} + \\sum_i\\sum_{j\\neq i}\\mathbf{F}_{ij}^{\\text{内}}")+
   p("内力成对出现（$\\mathbf{F}_{ij}=-\\mathbf{F}_{ji}$），故内力求和为零：")+
   fml("\\sum_i\\sum_{j\\neq i}\\mathbf{F}_{ij}^{\\text{内}} = 0")+
   p("因此 $M\\mathbf{a}_C = \\sum \\mathbf{F}_{\\text{外}}$，即质心的运动只由合外力决定，与内力无关。"))+
   note(p("质心运动定理是质点系动力学的核心：内力不影响质心运动。例如炮弹爆炸时，弹片四散但质心仍沿原抛物线运动。"))
 )},
]},
# ---- 2.7 惯性系与力学相对性原理 ----
{
"name": "2.7 惯性系与力学相对性原理",
"color": "#0d9488",
"desc": "惯性系的定义与伽利略相对性原理",
"items": [
{"id":"c2s7-1","name":"惯性系与力学相对性原理","tags":["def","thm","note"],"brief":"牛顿定律成立的参考系，以及力学规律在惯性系中的等价性。",
 "body": wrap(
   defn("惯性系",p("牛顿第一定律（惯性定律）成立的参考系称为<strong>惯性系</strong>。在惯性系中，不受外力的物体保持静止或匀速直线运动。一切相对惯性系做匀速直线运动的参考系都是惯性系。"))+
   thm("伽利略相对性原理",p("在所有惯性系中，力学定律具有相同的形式，即通过任何力学实验都无法判断所在惯性系是静止还是匀速直线运动。"))+
   note(p("地球因自转和公转严格来说不是惯性系，但在大多数工程问题中可近似为惯性系。太阳参考系比地球参考系更接近惯性系。"))
 )},
]},
# ---- 2.8 非惯性系与惯性力 ----
{
"name": "2.8 非惯性系与惯性力",
"color": "#0d9488",
"desc": "平移非惯性系中的惯性力与超重失重现象",
"items": [
{"id":"c2s8-1","name":"非惯性系与惯性力","tags":["def","thm","der"],"brief":"在加速参考系中引入惯性力使牛顿定律形式上成立。",
 "body": wrap(
   defn("非惯性系",p("相对惯性系做加速运动的参考系称为<strong>非惯性系</strong>。在非惯性系中，牛顿第一、第二定律不直接成立。"))+
   thm("平移惯性力",p("设非惯性系 $S'$ 相对惯性系 $S$ 以加速度 $\\mathbf{a}_0$ 平动，则在 $S'$ 中，质点除受真实力 $\\mathbf{F}$ 外，还受到<strong>惯性力</strong>：")+
   fml("\\mathbf{F}_{\\text{惯}} = -m\\mathbf{a}_0")+
   p("此时牛顿第二定律形式为：$\\mathbf{F} + \\mathbf{F}_{\\text{惯}} = m\\mathbf{a}'$，其中 $\\mathbf{a}'$ 为质点相对 $S'$ 的加速度。"))+
   der(p("<strong>推导：</strong>由加速度合成 $\\mathbf{a} = \\mathbf{a}' + \\mathbf{a}_0$，代入惯性系中的牛顿第二定律 $\\mathbf{F}=m\\mathbf{a}$：")+
   fml("\\mathbf{F} = m(\\mathbf{a}' + \\mathbf{a}_0) \\implies \\mathbf{F} - m\\mathbf{a}_0 = m\\mathbf{a}'")+
   p("将 $-m\\mathbf{a}_0$ 定义为惯性力 $\\mathbf{F}_{\\text{惯}}$，则在 $S'$ 中有 $\\mathbf{F}+\\mathbf{F}_{\\text{惯}}=m\\mathbf{a}'$。惯性力没有施力物体，是参考系加速的效应，不满足牛顿第三定律。"))
 )},
{"id":"c2s8-2","name":"超重与失重","tags":["thm","der","app"],"brief":"加速参考系中视重与实重的差异。",
 "body": wrap(
   defn("视重",p("物体对支持物的压力或对悬挂物的拉力称为<strong>视重</strong>，与物体的实重 $mg$ 不一定相等。"))+
   thm("超重与失重",p("当电梯以加速度 $a$ 向上运动时，物体视重 $N=m(g+a)$，为<strong>超重</strong>；当电梯以加速度 $a$ 向下运动时，视重 $N=m(g-a)$，为<strong>失重</strong>。")+
   fml("N = m(g \\pm a) \\quad \\begin{cases} +a & (\\text{加速上升或减速下降}) \\\\ -a & (\\text{加速下降或减速上升}) \\end{cases}"))+
   der(p("<strong>推导：</strong>取向上为正，物体受重力 $mg$（向下）和支持力 $N$（向上）。由牛顿第二定律：")+
   fml("N - mg = ma \\implies N = m(g+a)")+
   p("当 $a>0$（向上加速）时 $N>mg$，超重；当 $a<0$（向下加速）时 $N<mg$，失重。当 $a=-g$（自由下落）时 $N=0$，<strong>完全失重</strong>。"))+
   app(p("<strong>应用：</strong>航天器在轨道上绕地球做圆周运动时，向心加速度 $a=g$，处于完全失重状态。"))
 )},
]},
# ---- 2.9 约束与连接体 ----
{
"name": "2.9 约束与连接体问题",
"color": "#0d9488",
"desc": "约束力的类型与连接体问题的求解方法",
"items": [
{"id":"c2s9-1","name":"约束与约束力","tags":["def","note"],"brief":"限制物体运动的条件与相应的约束力。",
 "body": wrap(
   defn("约束与约束力",p("限制物体运动的条件称为<strong>约束</strong>，约束对物体的作用力称为<strong>约束力</strong>（或约束反力）。常见约束：")+
   p("• <strong>光滑接触面</strong>：约束力沿法线方向指向物体（法向力 $N$）。<br>• <strong>柔软绳索</strong>：约束力沿绳方向，只能拉不能推（拉力 $T$）。<br>• <strong>光滑铰链</strong>：约束力方向待定，可分解为两个分量。<br>• <strong>固定端</strong>：既有约束力又有约束力偶。"))+
   note(p("约束力是被动力，其大小和方向由主动力和运动状态决定。求解时通常需结合运动方程和约束条件。"))
 )},
{"id":"c2s9-2","name":"连接体问题——阿特伍德机","tags":["exa","der"],"brief":"用不可伸长绳连接的两物体的加速度与绳张力。",
 "body": wrap(
   exa(p("<strong>阿特伍德机：</strong>两物体质量 $m_1,m_2$（$m_1>m_2$）通过轻绳跨过光滑定滑轮连接。求加速度 $a$ 与绳张力 $T$。"))+
   der(p("设 $m_1$ 向下加速、$m_2$ 向上加速，加速度大小均为 $a$（绳不可伸长）。分别对两物体列牛顿第二定律：")+
   fml("m_1 g - T = m_1 a \\quad (m_1,\\text{向下为正})")+
   fml("T - m_2 g = m_2 a \\quad (m_2,\\text{向上为正})")+
   p("两式相加消去 $T$：")+
   fml("(m_1-m_2)g = (m_1+m_2)a \\implies a = \\frac{m_1-m_2}{m_1+m_2}g")+
   p("代回求张力：")+
   fml("T = m_2(g+a) = \\frac{2m_1m_2}{m_1+m_2}g")+
   p("当 $m_1=m_2$ 时 $a=0$，$T=mg$（平衡）；当 $m_2\\to 0$ 时 $a\\to g$，$T\\to 0$。"))
 )},
]},
# ---- 2.10 典型动力学问题 ----
{
"name": "2.10 典型动力学问题",
"color": "#0d9488",
"desc": "斜面问题与圆锥摆的受力分析",
"items": [
{"id":"c2s10-1","name":"斜面问题","tags":["exa","der"],"brief":"光滑与粗糙斜面上物体的运动分析。",
 "body": wrap(
   exa(p("<strong>光滑斜面：</strong>倾角 $\\theta$，物体沿斜面下滑。重力分解为沿斜面分量 $mg\\sin\\theta$ 和垂直分量 $mg\\cos\\theta$。"))+
   der(p("垂直斜面方向无加速度，法向力 $N=mg\\cos\\theta$。沿斜面方向：")+
   fml("mg\\sin\\theta = ma \\implies a = g\\sin\\theta")+
   p("<strong>粗糙斜面：</strong>若物体滑动，受滑动摩擦力 $f=\\mu_k N=\\mu_k mg\\cos\\theta$，方向沿斜面向上：")+
   fml("mg\\sin\\theta - \\mu_k mg\\cos\\theta = ma \\implies a = g(\\sin\\theta - \\mu_k\\cos\\theta)")+
   p("物体静止时，静摩擦力 $f_s=mg\\sin\\theta \\le \\mu_s mg\\cos\\theta$，即恰好不下滑的临界角 $\\theta_c$ 满足 $\\tan\\theta_c=\\mu_s$。"))
 )},
{"id":"c2s10-2","name":"圆锥摆","tags":["exa","der"],"brief":"水平面内匀速圆周运动的向心力来源。",
 "body": wrap(
   exa(p("<strong>圆锥摆：</strong>长 $L$ 的轻绳一端固定，另一端系质量 $m$ 的小球，在水平面内做匀速圆周运动，绳与竖直方向成 $\\theta$ 角。"))+
   der(p("小球受重力 $mg$ 和绳拉力 $T$。竖直方向平衡，水平方向提供向心力：")+
   fml("T\\cos\\theta = mg,\\qquad T\\sin\\theta = m\\frac{v^2}{r} = m\\omega^2 r")+
   p("其中圆周半径 $r=L\\sin\\theta$。由第一式 $T=mg/\\cos\\theta$，代入第二式：")+
   fml("\\frac{mg}{\\cos\\theta}\\sin\\theta = m\\omega^2 L\\sin\\theta \\implies \\omega^2 = \\frac{g}{L\\cos\\theta}")+
   p("故周期 $T=\\frac{2\\pi}{\\omega}=2\\pi\\sqrt{\\frac{L\\cos\\theta}{g}}$。当 $\\theta$ 越大，$\\omega$ 越大、周期越短。"))
 )},
]},
# ---- 2.11 质点的角动量 ----
{
"name": "2.11 质点的角动量",
"color": "#0d9488",
"desc": "角动量、力矩的定义与角动量守恒定律",
"items": [
{"id":"c2s11-1","name":"角动量与力矩","tags":["def","thm","der"],"brief":"质点的角动量与力矩的关系。",
 "body": wrap(
   defn("角动量",p("质点对参考点 $O$ 的角动量定义为位矢与动量的叉积：")+
   fml("\\mathbf{L} = \\mathbf{r} \\times \\mathbf{p} = \\mathbf{r} \\times m\\mathbf{v}")+
   p("大小 $L=mrv\\sin\\theta$（$\\theta$ 为 $\\mathbf{r}$ 与 $\\mathbf{v}$ 的夹角），方向由右手螺旋定则确定。"))+
   defn("力矩",p("力 $\\mathbf{F}$ 对参考点 $O$ 的力矩为位矢与力的叉积：")+
   fml("\\mathbf{M} = \\mathbf{r} \\times \\mathbf{F}")+
   p("大小 $M=rF\\sin\\theta$，方向垂直于 $\\mathbf{r}$ 和 $\\mathbf{F}$ 组成的平面。"))+
   thm("角动量定理",p("质点所受合外力矩等于其角动量的时间变化率：")+
   fml("\\mathbf{M} = \\frac{d\\mathbf{L}}{dt}"))+
   der(p("<strong>推导：</strong>对 $\\mathbf{L}=\\mathbf{r}\\times m\\mathbf{v}$ 求导：")+
   fml("\\frac{d\\mathbf{L}}{dt} = \\frac{d\\mathbf{r}}{dt}\\times m\\mathbf{v} + \\mathbf{r}\\times m\\frac{d\\mathbf{v}}{dt}")+
   fml("= \\mathbf{v}\\times m\\mathbf{v} + \\mathbf{r}\\times\\mathbf{F} = 0 + \\mathbf{r}\\times\\mathbf{F} = \\mathbf{M}")+
   p("其中 $\\mathbf{v}\\times\\mathbf{v}=0$。故 $\\mathbf{M}=\\frac{d\\mathbf{L}}{dt}$。"))
 )},
{"id":"c2s11-2","name":"角动量守恒与开普勒第二定律","tags":["thm","der"],"brief":"有心力场中角动量守恒，推导开普勒第二定律。",
 "body": wrap(
   thm("角动量守恒定律",p("当质点所受合外力矩为零时，质点的角动量保持不变：")+
   fml("\\mathbf{M}=0 \\implies \\mathbf{L}=\\text{常矢量}"))+
   der(p("<strong>推导：</strong>由 $\\mathbf{M}=\\frac{d\\mathbf{L}}{dt}$，若 $\\mathbf{M}=0$，则 $\\frac{d\\mathbf{L}}{dt}=0$，故 $\\mathbf{L}=$ 常矢量。<br>有心力（力的方向始终通过参考点 $O$，如万有引力）的力矩 $\\mathbf{M}=\\mathbf{r}\\times\\mathbf{F}=0$，故有心力场中角动量守恒。"))+
   der(p("<strong>开普勒第二定律推导：</strong>行星绕太阳做椭圆运动，太阳位于焦点，引力为有心力，角动量守恒。在 $dt$ 时间内，位矢扫过的面积：")+
   fml("dA = \\tfrac{1}{2} |\\mathbf{r}\\times d\\mathbf{r}| = \\tfrac{1}{2} |\\mathbf{r}\\times\\mathbf{v}|\\,dt = \\frac{L}{2m}dt")+
   p("故<strong>面积速度</strong>为常量：")+
   fml("\\frac{dA}{dt} = \\frac{L}{2m} = \\text{常量}")+
   p("即行星与太阳的连线在相等时间内扫过相等的面积——开普勒第二定律。"))
 )},
]},
]

# =====================================================
#  CHAPTER 3: 功能关系
# =====================================================
ch3_sections = [
# ---- 3.1 功与功率 ----
{
"name": "3.1 功与功率",
"color": "#059669",
"desc": "功的定义、变力做功、功率",
"items": [
{"id":"c3s1-1","name":"功的定义","tags":["def","der"],"brief":"力对空间的积累效应。",
 "body": wrap(
   defn("恒力的功",p("恒力 $\\mathbf{F}$ 作用下质点发生位移 $\\Delta\\mathbf{r}$，力所做的功为：")+
   fml("W = \\mathbf{F}\\cdot\\Delta\\mathbf{r} = F|\\Delta\\mathbf{r}|\\cos\\theta"))+
   defn("变力的功",p("变力沿曲线做功为力沿路径的线积分：")+
   fml("W = \\int_{a}^{b} \\mathbf{F}\\cdot d\\mathbf{r} = \\int_{a}^{b} F\\cos\\theta\\,ds"))+
   der(p("<strong>分量形式（直角坐标）：</strong>")+
   fml("W = \\int_{x_1}^{x_2} F_x\\,dx + \\int_{y_1}^{y_2} F_y\\,dy + \\int_{z_1}^{z_2} F_z\\,dz"))+
   defn("功率",p("功率是单位时间内做的功：")+
   fml("P = \\frac{dW}{dt} = \\mathbf{F}\\cdot\\mathbf{v}"))
 )},
]},
# ---- 3.2 动能定理 ----
{
"name": "3.2 动能定理",
"color": "#059669",
"desc": "合外力做功等于动能变化的推导",
"items": [
{"id":"c3s2-1","name":"动能定理","tags":["thm","der"],"brief":"功是能量变化的量度。",
 "body": wrap(
   defn("动能",p("质点的动能：$E_k=\\frac{1}{2}mv^2$。"))+
   thm("动能定理",p("合外力对质点做的功等于质点动能的增量：")+
   fml("W_{\\text{合}} = \\Delta E_k = \\tfrac{1}{2}mv^2 - \\tfrac{1}{2}mv_0^2"))+
   der(p("<strong>推导：</strong>由牛顿第二定律 $\\mathbf{F}=m\\mathbf{a}=m\\frac{d\\mathbf{v}}{dt}$，合外力做功：")+
   fml("W = \\int \\mathbf{F}\\cdot d\\mathbf{r} = \\int m\\frac{d\\mathbf{v}}{dt}\\cdot d\\mathbf{r} = \\int m\\,d\\mathbf{v}\\cdot\\frac{d\\mathbf{r}}{dt} = \\int m\\mathbf{v}\\cdot d\\mathbf{v}")+
   p("利用 $\\mathbf{v}\\cdot d\\mathbf{v}=d\\left(\\tfrac{1}{2}v^2\\right)$（因为 $d(v^2)=d(\\mathbf{v}\\cdot\\mathbf{v})=2\\mathbf{v}\\cdot d\\mathbf{v}$）：")+
   fml("W = m\\int_{v_0}^{v} d\\left(\\tfrac{1}{2}v^2\\right) = \\tfrac{1}{2}mv^2 - \\tfrac{1}{2}mv_0^2 = \\Delta E_k"))+
   note(p("动能定理是标量方程，适用于惯性系。合外力做正功动能增加，做负功动能减少。"))
 )},
]},
# ---- 3.3 保守力与势能 ----
{
"name": "3.3 保守力与势能",
"color": "#059669",
"desc": "保守力的判据、势能的定义与计算",
"items": [
{"id":"c3s3-1","name":"保守力与势能","tags":["thm","der"],"brief":"做功与路径无关的力可以引入势能。",
 "body": wrap(
   defn("保守力",p("若力做功只与始末位置有关，与路径无关，则该力为<strong>保守力</strong>。等价判据：沿任意闭合路径做功为零，即 $\\oint\\mathbf{F}\\cdot d\\mathbf{r}=0$。"))+
   defn("势能",p("保守力做功等于势能的减少：")+
   fml("W_{\\text{保}} = E_{p1} - E_{p2} = -\\Delta E_p")+
   p("势能的定义式（取 $r_0$ 为势能零点）：")+
   fml("E_p(\\mathbf{r}) = -\\int_{\\mathbf{r}_0}^{\\mathbf{r}} \\mathbf{F}_{\\text{保}}\\cdot d\\mathbf{r}"))+
   der(p("<strong>重力势能：</strong>取地面 $y=0$ 为零点，重力 $\\mathbf{F}=-mg\\mathbf{j}$：")+
   fml("E_p = -\\int_0^h (-mg)\\,dy = mgh")+
   p("<strong>弹性势能：</strong>取原长 $x=0$ 为零点，弹力 $F=-kx$：")+
   fml("E_p = -\\int_0^x (-kx')\\,dx' = \\tfrac{1}{2}kx^2"))+
   thm("保守力与势能的关系",p("保守力等于势能的负梯度：")+
   fml("\\mathbf{F}_{\\text{保}} = -\\nabla E_p = -\\left(\\frac{\\partial E_p}{\\partial x}\\mathbf{i}+\\frac{\\partial E_p}{\\partial y}\\mathbf{j}+\\frac{\\partial E_p}{\\partial z}\\mathbf{k}\\right)"))
 )},
]},
# ---- 3.4 机械能守恒 ----
{
"name": "3.4 机械能守恒定律",
"color": "#059669",
"desc": "只有保守力做功时机械能守恒的推导",
"items": [
{"id":"c3s4-1","name":"机械能守恒定律","tags":["thm","der"],"brief":"动能与势能之和保持不变。",
 "body": wrap(
   thm("机械能守恒",p("当系统只有保守力做功时，系统的机械能（动能+势能）保持不变：")+
   fml("E = E_k + E_p = \\text{常量}"))+
   der(p("<strong>推导：</strong>将质点所受的力分为保守力 $\\mathbf{F}_{\\text{保}}$ 和非保守力 $\\mathbf{F}_{\\text{非保}}$。由动能定理：")+
   fml("W_{\\text{保}} + W_{\\text{非保}} = \\Delta E_k")+
   p("由保守力做功与势能的关系 $W_{\\text{保}}=-\\Delta E_p$，代入得：")+
   fml("-\\Delta E_p + W_{\\text{非保}} = \\Delta E_k \\implies W_{\\text{非保}} = \\Delta(E_k+E_p)")+
   p("若无非保守力做功（$W_{\\text{非保}}=0$），则 $\\Delta(E_k+E_p)=0$，即 $E_k+E_p=$ 常量。"))+
   note(p("机械能守恒的条件是<strong>只有保守力做功</strong>，而非不受外力。非保守力（如摩擦力）做功会导致机械能转化为其他形式能量（如热能）。"))
 )},
]},
# ---- 3.5 功能原理 ----
{
"name": "3.5 功能原理",
"color": "#059669",
"desc": "系统功能原理与能量转化",
"items": [
{"id":"c3s5-1","name":"系统的功能原理","tags":["thm","note"],"brief":"外力和非保守内力做功改变系统机械能。",
 "body": wrap(
   thm("功能原理",p("系统所受外力做功与非保守内力做功之和等于系统机械能的增量：")+
   fml("W_{\\text{外}} + W_{\\text{非保内}} = \\Delta E = \\Delta(E_k+E_p)"))+
   note(p("与质点动能定理的区别：功能原理将内力分为保守内力和非保守内力，保守内力做功已被势能变化吸收，不再出现在方程左边。")+
   p("若 $W_{\\text{外}}=0$ 且 $W_{\\text{非保内}}=0$，则机械能守恒。若有摩擦力等非保守内力做功，机械能减少，转化为热能等其他形式能量，这就是<strong>能量守恒定律</strong>的体现。"))
 )},
]},
# ---- 3.6 变力做功与功率 ----
{
"name": "3.6 变力做功与功率",
"color": "#059669",
"desc": "变力做功的积分计算与功率、机械效率",
"items": [
{"id":"c3s6-1","name":"变力做功的计算","tags":["thm","der"],"brief":"用积分方法计算变力沿曲线做的功。",
 "body": wrap(
   thm("变力做功",p("变力 $\\mathbf{F}(\\mathbf{r})$ 沿曲线 $C$ 从 $a$ 到 $b$ 做的功为线积分：")+
   fml("W = \\int_{a}^{b} \\mathbf{F}\\cdot d\\mathbf{r} = \\int_{a}^{b} (F_x\\,dx + F_y\\,dy + F_z\\,dz)"))+
   der(p("<strong>例：弹簧弹力做功</strong>。弹力 $F=-kx$（沿 $x$ 方向），从 $x_1$ 到 $x_2$：")+
   fml("W = \\int_{x_1}^{x_2} (-kx)\\,dx = -\\tfrac{1}{2}k(x_2^2 - x_1^2)")+
   p("弹力做功只与始末位置有关，与路径无关，故弹力为保守力。")+
   p("<strong>例：恒力沿曲线做功</strong>。恒力 $\\mathbf{F}$ 沿任意曲线从 $\\mathbf{r}_1$ 到 $\\mathbf{r}_2$：")+
   fml("W = \\int_{\\mathbf{r}_1}^{\\mathbf{r}_2} \\mathbf{F}\\cdot d\\mathbf{r} = \\mathbf{F}\\cdot\\int_{\\mathbf{r}_1}^{\\mathbf{r}_2} d\\mathbf{r} = \\mathbf{F}\\cdot(\\mathbf{r}_2-\\mathbf{r}_1) = \\mathbf{F}\\cdot\\Delta\\mathbf{r}")+
   p("恒力做功只与位移有关，与路径无关。"))
 )},
{"id":"c3s6-2","name":"功率与机械效率","tags":["def","der"],"brief":"功率的定义、平均功率与瞬时功率，机械效率。",
 "body": wrap(
   defn("功率",p("功率是单位时间内做的功，描述做功的快慢：")+
   fml("P = \\frac{dW}{dt} = \\mathbf{F}\\cdot\\mathbf{v}")+
   p("平均功率 $\\bar{P}=\\frac{W}{\\Delta t}$，瞬时功率 $P=\\mathbf{F}\\cdot\\mathbf{v}$。"))+
   der(p("<strong>推导：</strong>由 $dW=\\mathbf{F}\\cdot d\\mathbf{r}$，两边除以 $dt$：")+
   fml("P = \\frac{dW}{dt} = \\mathbf{F}\\cdot\\frac{d\\mathbf{r}}{dt} = \\mathbf{F}\\cdot\\mathbf{v}"))+
   defn("机械效率",p("机械输出的有用功与输入功之比：")+
   fml("\\eta = \\frac{W_{\\text{有用}}}{W_{\\text{输入}}} = \\frac{P_{\\text{有用}}}{P_{\\text{输入}}} \\le 1")+
   p("因摩擦等损耗，实际机械效率 $\\eta<1$。"))
 )},
]},
# ---- 3.7 势能的进一步讨论 ----
{
"name": "3.7 势能的进一步讨论",
"color": "#059669",
"desc": "引力势能、势能曲线与平衡的稳定性",
"items": [
{"id":"c3s7-1","name":"引力势能","tags":["def","der"],"brief":"万有引力场中的势能表达式。",
 "body": wrap(
   defn("引力势能",p("质量分别为 $m_1,m_2$ 的两质点相距 $r$ 时的引力势能为（取无穷远为零点）：")+
   fml("E_p = -G\\frac{m_1 m_2}{r}"))+
   der(p("<strong>推导：</strong>万有引力 $F=G\\frac{m_1m_2}{r^2}$（吸引力，沿 $-\\mathbf{e}_r$ 方向）。质点从 $r$ 移到无穷远，引力做功：")+
   fml("W = \\int_{r}^{\\infty} \\mathbf{F}\\cdot d\\mathbf{r} = \\int_{r}^{\\infty} \\left(-G\\frac{m_1m_2}{r'^2}\\right) dr' = -G m_1 m_2 \\left[-\\frac{1}{r'}\\right]_r^{\\infty}")+
   fml("= -G m_1 m_2 \\left(0 + \\frac{1}{r}\\right) = -\\frac{G m_1 m_2}{r}")+
   p("由势能定义 $E_p(r)-E_p(\\infty)=-\\int_{\\infty}^{r}\\mathbf{F}\\cdot d\\mathbf{r}$，取 $E_p(\\infty)=0$，代入 $\\mathbf{F}=-G\\frac{m_1m_2}{r'^2}\\mathbf{e}_r$：")+
   fml("E_p(r) = -\\int_{\\infty}^{r} \\left(-G\\frac{m_1m_2}{r'^2}\\right) dr' = G m_1 m_2 \\int_{\\infty}^{r} \\frac{dr'}{r'^2} = G m_1 m_2 \\left[-\\frac{1}{r'}\\right]_{\\infty}^{r} = -\\frac{G m_1 m_2}{r}")+
   p("引力势能为负，因取无穷远为零点，两质点相互靠近时势能降低。"))+
   note(p("重力势能 $mgh$ 是引力势能在地面附近的近似：$E_p=-\\frac{GMm}{R+h}\\approx -\\frac{GMm}{R}+mgh$，其中 $g=\\frac{GM}{R^2}$，常数项可略去。"))
 )},
{"id":"c3s7-2","name":"势能曲线与平衡的稳定性","tags":["def","thm","der"],"brief":"由势能曲线判断力与平衡类型。",
 "body": wrap(
   thm("保守力与势能的关系",p("保守力等于势能的负梯度，一维情形：")+
   fml("F = -\\frac{dE_p}{dx}")+
   p("势能曲线 $E_p(x)$ 斜率的负值即为保守力。"))+
   defn("平衡条件",p("质点平衡时合力为零，即 $\\frac{dE_p}{dx}=0$，势能曲线取极值。"))+
   der(p("<strong>平衡的稳定性：</strong>在平衡位置 $x_0$ 处对势能泰勒展开：")+
   fml("E_p(x) = E_p(x_0) + \\tfrac{1}{2}E_p''(x_0)(x-x_0)^2 + \\cdots")+
   p("• 若 $E_p''(x_0)>0$（势能极小），偏离后力指向平衡位置，<strong>稳定平衡</strong>。<br>• 若 $E_p''(x_0)<0$（势能极大），偏离后力远离平衡位置，<strong>不稳定平衡</strong>。<br>• 若 $E_p''(x_0)=0$，需更高阶导数判断。"))+
   exa(p("弹簧振子势能 $E_p=\\frac{1}{2}kx^2$ 在 $x=0$ 处 $E_p''=k>0$，为稳定平衡，对应简谐振动。"))
 )},
]},
# ---- 3.8 能量转化的典型问题 ----
{
"name": "3.8 能量转化的典型问题",
"color": "#059669",
"desc": "摩擦力做功与碰撞中的能量损失",
"items": [
{"id":"c3s8-1","name":"摩擦力做功与能量耗散","tags":["exa","der"],"brief":"摩擦力做功的特点与机械能向热能的转化。",
 "body": wrap(
   defn("摩擦力做功",p("滑动摩擦力 $f=\\mu_k N$，方向与相对运动方向相反。物体在水平面上滑行距离 $s$ 时，摩擦力做功：")+
   fml("W_f = -f\\cdot s = -\\mu_k N s"))+
   der(p("<strong>能量转化：</strong>摩擦力做负功，使物体动能减少：")+
   fml("W_f = \\Delta E_k = -\\tfrac{1}{2}mv_0^2 \\quad (\\text{物体从 } v_0 \\text{ 减速到 } 0)")+
   p("减少的机械能转化为系统的内能（热能）$Q=|W_f|=\\mu_k N s$。<br>注意：摩擦力做功与路径有关，故摩擦力是非保守力，不能引入势能。"))+
   note(p("一对滑动摩擦力（物体与地面之间）做功之和为 $-\\mu_k N s_{\\text{相对}}$，总是负值，系统机械能减少，转化为热能 $Q=\\mu_k N s_{\\text{相对}}$。"))
 )},
{"id":"c3s8-2","name":"碰撞中的能量损失","tags":["thm","der"],"brief":"非弹性碰撞中动能损失与恢复系数的关系。",
 "body": wrap(
   thm("碰撞中的动能损失",p("一维碰撞中，由动量守恒 $m_1v_1+m_2v_2=m_1v_1'+m_2v_2'$ 和恢复系数 $e=\\frac{v_2'-v_1'}{v_1-v_2}$，动能损失为：")+
   fml("\\Delta E_k = \\tfrac{1}{2}\\frac{m_1m_2}{m_1+m_2}(1-e^2)(v_1-v_2)^2"))+
   der(p("<strong>推导：</strong>用质心系。质心速度 $v_C=\\frac{m_1v_1+m_2v_2}{m_1+m_2}$。碰撞前后质心速度不变（动量守恒），质心系中动能 $E_k'=\\frac{1}{2}\\frac{m_1m_2}{m_1+m_2}u^2$，其中 $u=v_1-v_2$ 为相对速度。")+
   p("碰撞前相对速度 $u=v_1-v_2$，碰撞后 $u'=v_1'-v_2'=-e(v_1-v_2)$（由恢复系数定义）。故：")+
   fml("\\Delta E_k = \\tfrac{1}{2}\\frac{m_1m_2}{m_1+m_2}(u^2 - u'^2) = \\tfrac{1}{2}\\frac{m_1m_2}{m_1+m_2}(1-e^2)(v_1-v_2)^2")+
   p("当 $e=1$（完全弹性）$\\Delta E_k=0$；当 $e=0$（完全非弹性）损失最大：$\\Delta E_k=\\frac{1}{2}\\frac{m_1m_2}{m_1+m_2}(v_1-v_2)^2$。"))
 )},
]},
# ---- 3.9 质点系动能定理与柯尼希定理 ----
{
"name": "3.9 质点系动能定理与柯尼希定理",
"color": "#059669",
"desc": "质点系动能定理与总动能的分解",
"items": [
{"id":"c3s9-1","name":"质点系动能定理","tags":["thm","der"],"brief":"所有外力和内力做功之和等于质点系动能变化。",
 "body": wrap(
   thm("质点系动能定理",p("质点系从状态 1 到状态 2，所有外力做功与所有内力做功之和等于系统动能的增量：")+
   fml("W_{\\text{外}} + W_{\\text{内}} = \\Delta E_k = E_{k2} - E_{k1}"))+
   der(p("<strong>推导：</strong>对系内每个质点应用动能定理 $W_i=\\Delta E_{k_i}$，其中 $W_i=W_{i\\text{外}}+W_{i\\text{内}}$ 为第 $i$ 个质点受的外力和内力做功之和。对所有质点求和：")+
   fml("\\sum_i W_i = \\sum_i \\Delta E_{k_i} \\implies \\sum_i W_{i\\text{外}} + \\sum_i W_{i\\text{内}} = \\sum_i \\Delta E_{k_i}")+
   fml("W_{\\text{外}} + W_{\\text{内}} = \\Delta E_k")+
   p("注意：内力做功之和 $W_{\\text{内}}$ 一般不为零（与冲量不同，内力冲量之和为零），因为相互作用力作用点的位移可能不同。"))
 )},
{"id":"c3s9-2","name":"柯尼希定理","tags":["thm","der"],"brief":"质点系总动能等于质心动能加上相对质心的动能。",
 "body": wrap(
   thm("柯尼希定理",p("质点系的总动能等于质心的平动动能加上各质点相对质心运动的动能：")+
   fml("E_k = \\tfrac{1}{2}M v_C^2 + \\sum_i \\tfrac{1}{2}m_i v_i'^2")+
   p("其中 $M=\\sum m_i$ 为总质量，$v_C$ 为质心速度，$v_i'$ 为第 $i$ 个质点相对质心的速度。"))+
   der(p("<strong>推导：</strong>设 $\\mathbf{v}_i = \\mathbf{v}_C + \\mathbf{v}_i'$，则：")+
   fml("E_k = \\sum_i \\tfrac{1}{2}m_i v_i^2 = \\sum_i \\tfrac{1}{2}m_i (\\mathbf{v}_C+\\mathbf{v}_i')\\cdot(\\mathbf{v}_C+\\mathbf{v}_i')")+
   fml("= \\tfrac{1}{2}\\left(\\sum_i m_i\\right)v_C^2 + \\mathbf{v}_C\\cdot\\sum_i m_i\\mathbf{v}_i' + \\sum_i \\tfrac{1}{2}m_i v_i'^2")+
   p("第二项中 $\\sum_i m_i\\mathbf{v}_i'=M\\mathbf{v}_C'$，而质心系中质心速度 $\\mathbf{v}_C'=0$，故第二项为零。因此：")+
   fml("E_k = \\tfrac{1}{2}M v_C^2 + \\sum_i \\tfrac{1}{2}m_i v_i'^2"))
 )},
]},
]

# =====================================================
#  CHAPTER 4: 刚体动力学
# =====================================================
ch4_sections = [
# ---- 4.1 刚体的运动描述 ----
{
"name": "4.1 刚体的运动描述",
"color": "#0891b2",
"desc": "刚体的平动、转动与平面运动",
"items": [
{"id":"c4s1-1","name":"刚体的运动形式","tags":["def","note"],"brief":"刚体运动的基本类型与角量描述。",
 "fig":"rotation","figCap":"刚体绕定轴转动",
 "body": wrap(
   defn("刚体",p("在外力作用下形状和大小都保持不变的物体，即任意两质点间距离不变的质点系。"))+
   defn("平动与转动",p("<strong>平动</strong>：刚体上任意两点连线方向不变，各点运动状态相同，可简化为质点运动。<br><strong>定轴转动</strong>：刚体上各点都绕同一固定轴做圆周运动。"))+
   defn("角量",p("角位移 $\\Delta\\theta$，角速度 $\\omega=\\frac{d\\theta}{dt}$，角加速度 $\\beta=\\frac{d\\omega}{dt}$。"))+
   der(p("<strong>线量与角量关系：</strong>距转轴 $r$ 处质点的线速度、切向加速度、法向加速度：")+
   fml("v = r\\omega,\\quad a_t = r\\beta,\\quad a_n = r\\omega^2"))
 )},
]},
# ---- 4.2 转动惯量 ----
{
"name": "4.2 转动惯量",
"color": "#0891b2",
"desc": "转动惯量的定义、计算与平行轴定理",
"items": [
{"id":"c4s2-1","name":"转动惯量与平行轴定理","tags":["def","thm","der"],"brief":"刚体转动惯性的量度。",
 "body": wrap(
   defn("转动惯量",p("刚体对某轴的转动惯量为各质元质量到转轴距离平方的加权和：")+
   fml("I = \\sum_i m_i r_i^2 = \\int r^2\\,dm"))+
   thm("平行轴定理",p("设 $I_c$ 为刚体对通过质心的轴的转动惯量，$I$ 为对与该轴平行且相距 $d$ 的另一轴的转动惯量，则：")+
   fml("I = I_c + md^2"))+
   der(p("<strong>平行轴定理推导：</strong>设质心轴为 $z_c$，平行轴为 $z$，两轴间距 $d$。对质心系，质元位置 $\\mathbf{r}_i'$，质心系原点在质心，故 $\\sum m_i\\mathbf{r}_i'=0$。")+
   p("对 $z$ 轴，$r_i^2 = (x_i'+d)^2 + y_i'^2 = r_i'^2 + 2dx_i' + d^2$，则：")+
   fml("I = \\sum m_i r_i^2 = \\sum m_i r_i'^2 + 2d\\sum m_i x_i' + d^2\\sum m_i = I_c + 0 + md^2")+
   p("其中 $\\sum m_i x_i'=0$ 是因为质心系中质心在原点。"))+
   exa(p("<strong>圆盘转动惯量推导：</strong>均质圆盘质量 $m$、半径 $R$，面密度 $\\sigma=\\frac{m}{\\pi R^2}$。取半径 $r$、宽度 $dr$ 的细圆环，质量 $dm=\\sigma\\cdot 2\\pi r\\,dr$：")+
   fml("I = \\int r^2\\,dm = \\int_0^R r^2\\cdot \\sigma 2\\pi r\\,dr = 2\\pi\\sigma\\int_0^R r^3\\,dr = 2\\pi\\sigma\\cdot\\frac{R^4}{4} = \\frac{1}{2}\\sigma\\pi R^4")+
   fml("= \\frac{1}{2}\\cdot\\frac{m}{\\pi R^2}\\cdot\\pi R^4 = \\frac{1}{2}mR^2"))+
   app(p("<strong>常见物体转动惯量表：</strong>")+
   fml("\\begin{array}{|l|l|l|} \\hline \\text{物体} & \\text{转轴} & \\text{转动惯量} \\\\ \\hline \\text{细杆} & \\text{过中心垂直轴} & \\frac{1}{12}mL^2 \\\\ \\text{细杆} & \\text{过端点垂直轴} & \\frac{1}{3}mL^2 \\\\ \\text{圆环} & \\text{过中心垂直轴} & mR^2 \\\\ \\text{圆盘/圆柱} & \\text{过中心垂直轴} & \\frac{1}{2}mR^2 \\\\ \\text{实心球} & \\text{过球心} & \\frac{2}{5}mR^2 \\\\ \\text{薄球壳} & \\text{过球心} & \\frac{2}{3}mR^2 \\\\ \\hline \\end{array}")+
   fml("", "由平行轴定理，细杆过端点的 $I=\\frac{1}{12}mL^2+m\\left(\\frac{L}{2}\\right)^2=\\frac{1}{3}mL^2$。"))
 )},
{"id":"c4s2-2","name":"常见物体转动惯量图","tags":["app"],"brief":"细杆、圆环、圆盘、球体的转动惯量与转轴图示。",
 "fig":"inertia_shapes","figCap":"常见刚体的形状、转轴与转动惯量",
 "body": wrap(
   note(p("上图列出四种常见刚体的转动惯量。注意：转动惯量依赖于<strong>转轴位置</strong>，同一物体对不同轴的 $I$ 不同。平行轴定理 $I=I_c+md^2$ 可由过质心轴的 $I_c$ 求出任意平行轴的 $I$。"))
 )},
]},
# ---- 4.3 转动定律 ----
{
"name": "4.3 转动定律",
"color": "#0891b2",
"desc": "力矩、转动定律的推导",
"items": [
{"id":"c4s3-1","name":"力矩与转动定律","tags":["thm","der"],"brief":"刚体转动的牛顿第二定律。",
 "body": wrap(
   defn("力矩",p("力 $\\mathbf{F}$ 对转轴的力矩大小为 $M=rF\\sin\\theta$，矢量式：")+
   fml("\\mathbf{M} = \\mathbf{r}\\times\\mathbf{F}"))+
   thm("转动定律",p("刚体绕定轴转动时，合外力矩等于转动惯量乘以角加速度：")+
   fml("M = I\\beta"))+
   der(p("<strong>推导：</strong>将刚体视为质点系，第 $i$ 个质元受外力 $\\mathbf{F}_i$，切向分量 $F_{it}=m_i a_{it}=m_i r_i\\beta$。对转轴的力矩：")+
   fml("M_i = r_i F_{it} = m_i r_i^2 \\beta")+
   p("对所有质元求和，内力矩成对抵消（牛顿第三定律），仅外力矩贡献：")+
   fml("M_{\\text{合外}} = \\sum_i M_i = \\left(\\sum_i m_i r_i^2\\right)\\beta = I\\beta"))+
   note(p("转动定律 $M=I\\beta$ 与平动的牛顿第二定律 $F=ma$ 形式对应：力矩 $\\leftrightarrow$ 力，转动惯量 $\\leftrightarrow$ 质量，角加速度 $\\leftrightarrow$ 加速度。"))
 )},
]},
# ---- 4.4 角动量与守恒 ----
{
"name": "4.4 角动量与角动量守恒",
"color": "#0891b2",
"desc": "角动量定理与守恒定律",
"items": [
{"id":"c4s4-1","name":"角动量定理与守恒","tags":["thm","der"],"brief":"转动中的动量守恒对应物。",
 "body": wrap(
   defn("角动量",p("质点对转轴的角动量 $L=mrv$（垂直情形）。刚体绕定轴转动的角动量：")+
   fml("L = I\\omega"))+
   thm("角动量定理",p("合外力矩的冲量矩等于角动量的变化：")+
   fml("\\int_{t_1}^{t_2} M\\,dt = \\Delta L = I\\omega_2 - I\\omega_1"))+
   der(p("<strong>角动量定理推导：</strong>由转动定律 $M=I\\beta=I\\frac{d\\omega}{dt}=\\frac{d(I\\omega)}{dt}=\\frac{dL}{dt}$，积分得：")+
   fml("\\int M\\,dt = \\int dL = \\Delta L"))+
   thm("角动量守恒定律",p("当系统所受合外力矩为零时，系统角动量守恒：")+
   fml("L = I\\omega = \\text{常量}"))+
   der(p("<strong>角动量守恒推导：</strong>由 $M=\\frac{dL}{dt}$，若 $M=0$，则 $\\frac{dL}{dt}=0$，即 $L=$ 常量。")+
   p("注意：角动量守恒时 $I$ 和 $\\omega$ 可以各自变化，但乘积不变。例如花样滑冰运动员收回手臂时 $I$ 减小，$\\omega$ 增大。"))
 )},
]},
# ---- 4.5 刚体的平衡 ----
{
"name": "4.5 刚体的平衡",
"color": "#0891b2",
"desc": "刚体平衡的条件与稳定性",
"items": [
{"id":"c4s5-1","name":"刚体的平衡条件","tags":["thm","note"],"brief":"合力为零且合力矩为零。",
 "body": wrap(
   thm("刚体平衡条件",p("刚体处于平衡状态（静止或匀速直线运动 + 匀速转动）的充要条件：")+
   fml("\\sum \\mathbf{F}_i = 0,\\qquad \\sum \\mathbf{M}_i = 0")+
   p("即合外力为零，对任意转轴的合外力矩为零。"))+
   note(p("对平面力系，平衡条件为三个标量方程：")+
   fml("\\sum F_x=0,\\quad \\sum F_y=0,\\quad \\sum M_O=0")+
   p("其中 $O$ 为任意选定的矩心。求解时可灵活选取矩心以简化计算。"))
 )},
]},
# ---- 4.6 刚体的平面运动 ----
{
"name": "4.6 刚体的平面运动",
"color": "#0891b2",
"desc": "刚体平面运动的分解、瞬时转动中心与纯滚动",
"items": [
{"id":"c4s6-1","name":"刚体的平面运动与瞬心","tags":["def","thm","der"],"brief":"平面运动分解为平动加转动，引入瞬心。",
 "body": wrap(
   defn("刚体的平面运动",p("刚体上各点都平行于某一固定平面运动，称为<strong>平面运动</strong>。可分解为随基点的平动和绕基点的转动。"))+
   thm("平面运动的速度合成",p("取基点 $A$，刚体上任一点 $B$ 的速度为：")+
   fml("\\mathbf{v}_B = \\mathbf{v}_A + \\boldsymbol{\\omega} \\times \\mathbf{r}_{AB}")+
   p("其中 $\\mathbf{r}_{AB}$ 是 $B$ 相对 $A$ 的位矢，$\\boldsymbol{\\omega}$ 为角速度（与基点选择无关）。"))+
   defn("瞬时转动中心",p("某瞬时刚体上（或其延拓部分）速度为零的点称为<strong>瞬时转动中心</strong>（瞬心）。该瞬时刚体的运动可看作绕瞬心的纯转动。"))+
   der(p("<strong>瞬心的确定：</strong>已知两点 $A,B$ 的速度方向，过两点分别作速度方向的垂线，交点即为瞬心 $P$。此时 $v_A=\\omega\\cdot PA$，$v_B=\\omega\\cdot PB$。瞬心的速度为零但加速度一般不为零，故瞬心只在该瞬时成立。"))
 )},
{"id":"c4s6-2","name":"纯滚动","tags":["def","thm","der"],"brief":"滚动而不滑动的条件与运动学关系。",
 "body": wrap(
   defn("纯滚动",p("刚体在固定面上滚动而无相对滑动时，接触点的速度为零，称为<strong>纯滚动</strong>（无滑滚动）。"))+
   thm("纯滚动条件",p("半径为 $R$ 的圆轮在水平面上纯滚动时，质心速度与角速度满足：")+
   fml("v_C = \\omega R")+
   p("此时接触点 $P$ 的速度 $v_P=v_C-\\omega R=0$。"))+
   der(p("<strong>推导：</strong>圆轮质心速度 $v_C$ 向右，角速度 $\\omega$ 顺时针。接触点 $P$ 相对质心的速度为 $\\omega R$ 向左，故绝对速度：")+
   fml("v_P = v_C - \\omega R")+
   p("纯滚动时 $v_P=0$，得 $v_C=\\omega R$。对时间求导得质心加速度与角加速度关系：")+
   fml("a_C = \\beta R")+
   note(p("纯滚动时静摩擦力不做功（接触点瞬时速度为零），机械能守恒；有滑动时滑动摩擦力做功，机械能减少。"))
 ))},
]},
# ---- 4.7 转动惯量的进一步计算 ----
{
"name": "4.7 转动惯量的进一步计算",
"color": "#0891b2",
"desc": "垂直轴定理与组合体转动惯量的叠加",
"items": [
{"id":"c4s7-1","name":"垂直轴定理","tags":["thm","der"],"brief":"薄板刚体三个互相垂直轴的转动惯量关系。",
 "body": wrap(
   thm("垂直轴定理",p("对于薄板（平面）刚体，$x,y$ 轴在板面内，$z$ 轴垂直板面，则对 $z$ 轴的转动惯量等于对 $x,y$ 轴转动惯量之和：")+
   fml("I_z = I_x + I_y"))+
   der(p("<strong>推导：</strong>对板面内任一质元 $dm$，到 $z$ 轴的距离 $r^2=x^2+y^2$，故：")+
   fml("I_z = \\int r^2\\,dm = \\int (x^2+y^2)\\,dm = \\int x^2\\,dm + \\int y^2\\,dm = I_y + I_x")+
   p("其中 $I_x=\\int y^2\\,dm$（对 $x$ 轴），$I_y=\\int x^2\\,dm$（对 $y$ 轴）。"))+
   exa(p("<strong>薄圆盘：</strong>过圆心垂直盘面轴 $I_z=\\frac{1}{2}mR^2$。由对称性 $I_x=I_y$，故 $I_x=I_y=\\frac{1}{4}mR^2$。"))
 )},
{"id":"c4s7-2","name":"组合体转动惯量的叠加","tags":["thm","exa","der"],"brief":"由若干部分组成的刚体的转动惯量等于各部分之和。",
 "body": wrap(
   thm("叠加原理",p("组合体对某轴的转动惯量等于各组成部分对同一轴转动惯量之和：")+
   fml("I = \\sum_i I_i")+
   p("若各部分转轴不同，需用平行轴定理统一到同一轴。"))+
   exa(p("<strong>例：钟摆</strong>。质量 $m_1$、长 $L$ 的细杆一端与质量 $m_2$、半径 $R$ 的圆盘固连，求过杆另一端 $O$ 且垂直纸面的轴的转动惯量。"))+
   der(p("细杆对过端点轴：$I_1=\\frac{1}{3}m_1L^2$。<br>圆盘质心在 $L+R$ 处，对过自身质心轴 $I_{2c}=\\frac{1}{2}m_2R^2$，由平行轴定理：")+
   fml("I_2 = I_{2c} + m_2(L+R)^2 = \\tfrac{1}{2}m_2R^2 + m_2(L+R)^2")+
   fml("I = I_1 + I_2 = \\tfrac{1}{3}m_1L^2 + \\tfrac{1}{2}m_2R^2 + m_2(L+R)^2"))
 )},
]},
# ---- 4.8 转动动能与滚动 ----
{
"name": "4.8 转动动能与滚动摩擦",
"color": "#0891b2",
"desc": "刚体的转动动能、滚动的动能与滚动摩擦",
"items": [
{"id":"c4s8-1","name":"刚体的转动动能与滚动动能","tags":["thm","der"],"brief":"纯转动动能与平面运动刚体的总动能。",
 "body": wrap(
   thm("转动动能",p("刚体绕定轴转动的动能为各质元动能之和：")+
   fml("E_k = \\sum_i \\tfrac{1}{2}m_i v_i^2 = \\sum_i \\tfrac{1}{2}m_i (\\omega r_i)^2 = \\tfrac{1}{2}\\left(\\sum_i m_i r_i^2\\right)\\omega^2 = \\tfrac{1}{2}I\\omega^2"))+
   thm("平面运动刚体的动能",p("由柯尼希定理，平面运动刚体的动能等于质心平动动能加上绕质心转动动能：")+
   fml("E_k = \\tfrac{1}{2}M v_C^2 + \\tfrac{1}{2}I_C \\omega^2"))+
   der(p("<strong>纯滚动的动能：</strong>纯滚动时 $v_C=\\omega R$，代入得：")+
   fml("E_k = \\tfrac{1}{2}M v_C^2 + \\tfrac{1}{2}I_C \\frac{v_C^2}{R^2} = \\tfrac{1}{2}v_C^2\\left(M + \\frac{I_C}{R^2}\\right)")+
   p("也可绕瞬心计算：$E_k=\\frac{1}{2}I_P\\omega^2$，由平行轴定理 $I_P=I_C+MR^2$，结果一致。"))
 )},
{"id":"c4s8-2","name":"滚动摩擦","tags":["def","note"],"brief":"滚动阻力的成因与滚动比滑动省力的原因。",
 "body": wrap(
   defn("滚动摩擦",p("滚动时由于接触面形变，法向反力作用点前移，形成阻碍滚动的阻力矩，称为<strong>滚动摩擦</strong>（滚动阻力偶）。"))+
   fml("M_f = \\delta N")+
   p("$\\delta$ 为滚动摩擦系数（具有长度量纲），$N$ 为法向力。使轮子匀速滚动所需水平拉力 $F$ 满足 $FR=\\delta N$，即 $F=\\frac{\\delta}{R}N$。")+
   note(p("通常 $\\delta \\ll R$，故 $F \\ll \\mu_k N$，即滚动比滑动省力得多。这就是车轮、滚珠轴承广泛应用的原因。滚动摩擦不是真正的摩擦力，而是形变产生的阻力偶。"))
 )},
]},
# ---- 4.9 角动量的矢量性与进动 ----
{
"name": "4.9 角动量的矢量性与进动",
"color": "#0891b2",
"desc": "角动量的矢量性质与陀螺进动",
"items": [
{"id":"c4s9-1","name":"角动量的矢量性质","tags":["def","thm","der"],"brief":"角动量矢量的方向与转动定律的矢量形式。",
 "body": wrap(
   defn("角动量矢量",p("刚体绕定轴转动的角动量矢量方向沿转轴，由右手螺旋定则确定：四指沿转动方向，拇指指向为 $\\mathbf{L}$ 方向。")+
   fml("\\mathbf{L} = I\\boldsymbol{\\omega}"))+
   thm("转动定律的矢量形式",p("合外力矩矢量等于角动量矢量的时间变化率：")+
   fml("\\mathbf{M} = \\frac{d\\mathbf{L}}{dt}"))+
   der(p("<strong>说明：</strong>当 $\\mathbf{L}$ 的方向变化时（即使大小不变），也需要力矩。例如匀速圆周运动的质点，角动量大小不变但方向不断变化，所需向心力矩 $\\mathbf{M}=\\mathbf{r}\\times\\mathbf{F}$ 垂直于 $\\mathbf{L}$，使其方向改变。"))+
   note(p("对点的角动量 $\\mathbf{L}=\\mathbf{r}\\times m\\mathbf{v}$ 和力矩 $\\mathbf{M}=\\mathbf{r}\\times\\mathbf{F}$ 都是矢量，满足 $\\mathbf{M}=\\frac{d\\mathbf{L}}{dt}$。当 $\\mathbf{M}\\perp\\mathbf{L}$ 时，$\\mathbf{L}$ 仅改变方向不改变大小，产生进动。"))
 )},
{"id":"c4s9-2","name":"陀螺的进动","tags":["thm","der","app"],"brief":"重力矩作用下陀螺自转轴的进动。",
 "body": wrap(
   defn("进动",p("高速自转的陀螺在重力矩作用下，其自转轴绕竖直轴缓慢转动的现象称为<strong>进动</strong>（旋进）。"))+
   thm("进动角速度",p("设陀螺自转角动量为 $L$，重力矩为 $M$，则进动角速度为：")+
   fml("\\Omega = \\frac{M}{L} = \\frac{mgd}{I\\omega}")+
   p("其中 $d$ 为支点到质心的距离，$\\omega$ 为自转角速度。"))+
   der(p("<strong>推导：</strong>重力矩 $\\mathbf{M}=\\mathbf{r}_C\\times m\\mathbf{g}$ 垂直于自转轴（即垂直于 $\\mathbf{L}$）。由 $\\mathbf{M}=\\frac{d\\mathbf{L}}{dt}$，$d\\mathbf{L}$ 的方向沿 $\\mathbf{M}$，即 $\\mathbf{L}$ 的端点以速率 $M$ 做圆周运动。设 $\\mathbf{L}$ 与竖直轴夹角为 $\\theta$，端点圆周半径为 $L\\sin\\theta$，转动角速度（进动角速度）$\\Omega$ 满足：")+
   fml("\\left|\\frac{d\\mathbf{L}}{dt}\\right| = L\\sin\\theta\\cdot\\Omega = M \\implies \\Omega = \\frac{M}{L\\sin\\theta}")+
   p("当自转角速度很大、$\\theta$ 不大时，近似 $\\Omega\\approx\\frac{mgd}{I\\omega}$。自转越快，进动越慢。"))+
   app(p("<strong>应用：</strong>陀螺的进动解释了岁差（地球自转轴的进动，周期约 26000 年）、炮弹/子弹的飞行稳定性（旋转弹丸保持轴向）。"))
 )},
]},
# ---- 4.10 刚体平衡的应用 ----
{
"name": "4.10 刚体平衡的应用",
"color": "#0891b2",
"desc": "梯子平衡等典型刚体静力学问题",
"items": [
{"id":"c4s10-1","name":"梯子平衡问题","tags":["exa","der"],"brief":"靠墙梯子的受力分析与不滑动条件。",
 "body": wrap(
   exa(p("<strong>梯子平衡：</strong>长 $L$、重 $mg$ 的匀质梯子靠在光滑墙上，地面粗糙（摩擦系数 $\\mu_s$），梯子与地面成 $\\theta$ 角。求人爬到何处梯子开始滑动。"))+
   der(p("梯子受重力 $mg$（作用于中点）、墙的法向力 $N_1$（水平）、地面法向力 $N_2$（竖直）、地面静摩擦力 $f$（水平）。")+
   p("<strong>力平衡：</strong>")+
   fml("\\sum F_x=0: N_1=f,\\qquad \\sum F_y=0: N_2=mg")+
   p("<strong>力矩平衡（取地面接触点为矩心）：</strong>设人爬到距底端 $x$ 处，重 $Mg$：")+
   fml("\\sum M=0: N_1 L\\sin\\theta - mg\\cdot\\tfrac{L}{2}\\cos\\theta - Mg\\cdot x\\cos\\theta = 0")+
   fml("N_1 = \\frac{\\cos\\theta}{L\\sin\\theta}\\left(mg\\cdot\\tfrac{L}{2}+Mgx\\right) = \\left(\\tfrac{mg}{2}+\\frac{Mgx}{L}\\right)\\cot\\theta")+
   p("不滑动条件 $f\\le\\mu_s N_2$，即 $N_1\\le\\mu_s mg$：")+
   fml("\\left(\\tfrac{mg}{2}+\\frac{Mgx}{L}\\right)\\cot\\theta \\le \\mu_s mg")+
   p("解得人能爬到的最大距离 $x_{\\max}$。梯子越陡（$\\theta$ 大）、摩擦系数越大，越安全。"))
 )},
]},
]

# =====================================================
#  CHAPTER 5: 简谐振动与机械波
# =====================================================
ch5_sections = [
# ---- 5.1 简谐振动 ----
{
"name": "5.1 简谐振动",
"color": "#be185d",
"desc": "简谐振动的微分方程、解与能量",
"items": [
{"id":"c5s1-1","name":"简谐振动的运动方程","tags":["thm","der"],"brief":"弹簧振子的运动规律推导。",
 "fig":"shm","figCap":"简谐振动的位移-时间曲线",
 "body": wrap(
   defn("简谐振动",p("物体所受回复力与位移成正比且方向相反时的运动：$F=-kx$。"))+
   thm("简谐振动方程",p("简谐振动的位移随时间变化为：")+
   fml("x = A\\cos(\\omega t + \\varphi)")+
   p("其中 $A$ 为振幅，$\\omega$ 为角频率，$\\varphi$ 为初相位。"))+
   der(p("<strong>微分方程推导：</strong>弹簧振子受回复力 $F=-kx$，由牛顿第二定律：")+
   fml("m\\frac{d^2x}{dt^2} = -kx \\implies \\frac{d^2x}{dt^2} + \\omega^2 x = 0,\\quad \\omega^2=\\frac{k}{m}")+
   p("这是二阶常系数线性齐次微分方程，特征方程 $r^2+\\omega^2=0$，根 $r=\\pm i\\omega$，通解为：")+
   fml("x = C_1\\cos\\omega t + C_2\\sin\\omega t = A\\cos(\\omega t+\\varphi)")+
   p("其中 $A=\\sqrt{C_1^2+C_2^2}$，$\\tan\\varphi=-\\frac{C_2}{C_1}$。初始条件 $x(0)=x_0$，$v(0)=v_0$ 确定 $A$ 和 $\\varphi$：")+
   fml("A=\\sqrt{x_0^2+\\left(\\frac{v_0}{\\omega}\\right)^2},\\quad \\tan\\varphi=-\\frac{v_0}{\\omega x_0}"))+
   der(p("<strong>能量分析：</strong>动能 $E_k=\\frac{1}{2}mv^2$，势能 $E_p=\\frac{1}{2}kx^2$，总机械能：")+
   fml("E = E_k+E_p = \\tfrac{1}{2}m\\omega^2 A^2\\sin^2(\\omega t+\\varphi) + \\tfrac{1}{2}kA^2\\cos^2(\\omega t+\\varphi)")+
   p("利用 $\\omega^2=k/m$，即 $m\\omega^2=k$：")+
   fml("E = \\tfrac{1}{2}kA^2[\\sin^2(\\omega t+\\varphi)+\\cos^2(\\omega t+\\varphi)] = \\tfrac{1}{2}kA^2 = \\text{常量}")+
   p("简谐振动中机械能守恒，动能与势能相互转化。"))
 )},
]},
# ---- 5.2 单摆与复摆 ----
{
"name": "5.2 单摆与复摆",
"color": "#be185d",
"desc": "单摆、复摆的周期公式推导",
"items": [
{"id":"c5s2-1","name":"单摆与复摆周期","tags":["thm","der"],"brief":"小角度近似下的摆动周期。",
 "fig":"pendulum","figCap":"单摆的受力分析",
 "body": wrap(
   thm("单摆周期",p("小角度（$\\theta\\ll 1$ rad）下，单摆周期为：")+
   fml("T = 2\\pi\\sqrt{\\frac{L}{g}}"))+
   der(p("<strong>单摆推导：</strong>摆球受重力和拉力，切向合力 $F_t=-mg\\sin\\theta$。由牛顿第二定律切向分量 $ma_t=-mg\\sin\\theta$，而 $a_t=L\\beta=L\\frac{d^2\\theta}{dt^2}$：")+
   fml("mL\\frac{d^2\\theta}{dt^2} = -mg\\sin\\theta \\implies \\frac{d^2\\theta}{dt^2}+\\frac{g}{L}\\sin\\theta=0")+
   p("小角度时 $\\sin\\theta\\approx\\theta$，化为简谐振动方程 $\\frac{d^2\\theta}{dt^2}+\\omega^2\\theta=0$，其中 $\\omega=\\sqrt{g/L}$，故：")+
   fml("T = \\frac{2\\pi}{\\omega} = 2\\pi\\sqrt{\\frac{L}{g}}"))+
   thm("复摆周期",p("绕水平轴摆动的刚体（复摆），小角度下周期：")+
   fml("T = 2\\pi\\sqrt{\\frac{I}{mgd}}")+
   p("其中 $I$ 为对转轴的转动惯量，$d$ 为质心到转轴距离。"))+
   der(p("<strong>复摆推导：</strong>由转动定律 $M=I\\beta$，重力矩 $M=-mgd\\sin\\theta\\approx -mgd\\theta$：")+
   fml("I\\frac{d^2\\theta}{dt^2} = -mgd\\theta \\implies \\frac{d^2\\theta}{dt^2}+\\frac{mgd}{I}\\theta=0")+
   p("故 $\\omega=\\sqrt{mgd/I}$，$T=2\\pi\\sqrt{I/(mgd)}$。"))
 )},
]},
# ---- 5.3 阻尼与受迫振动 ----
{
"name": "5.3 阻尼振动与受迫振动",
"color": "#be185d",
"desc": "阻尼振动、受迫振动与共振",
"items": [
{"id":"c5s3-1","name":"阻尼振动与共振","tags":["thm","note"],"brief":"阻尼对振动的影响与共振现象。",
 "body": wrap(
   defn("阻尼振动",p("存在粘滞阻力 $f=-\\gamma v$ 时，运动方程为：")+
   fml("m\\frac{d^2x}{dt^2}+\\gamma\\frac{dx}{dt}+kx=0")+
   p("令 $\\beta=\\frac{\\gamma}{2m}$（阻尼因子），$\\omega_0=\\sqrt{k/m}$（固有频率），当 $\\beta<\\omega_0$（欠阻尼）时解为：")+
   fml("x = A_0 e^{-\\beta t}\\cos(\\omega t+\\varphi),\\quad \\omega=\\sqrt{\\omega_0^2-\\beta^2}"))+
   thm("受迫振动与共振",p("受周期性外力 $F=F_0\\cos\\omega_d t$ 作用时，稳态解为同频率简谐振动，振幅为：")+
   fml("A = \\frac{F_0/m}{\\sqrt{(\\omega_0^2-\\omega_d^2)^2+(2\\beta\\omega_d)^2}}")+
   p("当 $\\omega_d=\\sqrt{\\omega_0^2-2\\beta^2}$ 时振幅最大，发生<strong>共振</strong>。"))+
   note(p("共振在工程中既有应用（如乐器共鸣、核磁共振），也需避免（如桥梁共振、建筑抗震）。阻尼越小，共振峰越尖锐。"))
 )},
]},
# ---- 5.4 机械波 ----
{
"name": "5.4 机械波的描述",
"color": "#be185d",
"desc": "波的产生、描述与波方程",
"items": [
{"id":"c5s4-1","name":"机械波与波动方程","tags":["def","thm","der"],"brief":"振动的传播形成波。",
 "fig":"wave","figCap":"简谐波的波形与波长、振幅",
 "body": wrap(
   defn("机械波",p("机械振动在介质中的传播形成机械波。波传播的是振动状态和能量，介质本身不随波迁移。"))+
   defn("波的特征量",p("波长 $\\lambda$、周期 $T$、频率 $f$、波速 $v$ 满足：$v=\\lambda f=\\lambda/T$。"))+
   thm("简谐波方程",p("沿 $x$ 正方向传播的平面简谐波：")+
   fml("y(x,t) = A\\cos\\left[\\omega\\left(t-\\frac{x}{v}\\right)+\\varphi\\right]")+
   p("等价形式：$y=A\\cos(\\omega t-kx+\\varphi)$，其中 $k=\\frac{2\\pi}{\\lambda}$ 为波数。"))+
   der(p("<strong>波动方程推导：</strong>考虑沿绳传播的横波，取线元 $\\Delta x$，两端张力 $T$ 的横向分量差提供恢复力。由牛顿第二定律：")+
   fml("T\\left(\\left.\\frac{\\partial y}{\\partial x}\\right|_{x+\\Delta x}-\\left.\\frac{\\partial y}{\\partial x}\\right|_x\\right) = \\mu\\Delta x\\frac{\\partial^2 y}{\\partial t^2}")+
   p("其中 $\\mu$ 为线密度。左边除以 $\\Delta x$ 取极限得 $T\\frac{\\partial^2 y}{\\partial x^2}$：")+
   fml("\\frac{\\partial^2 y}{\\partial t^2} = \\frac{T}{\\mu}\\frac{\\partial^2 y}{\\partial x^2} = v^2\\frac{\\partial^2 y}{\\partial x^2},\\quad v=\\sqrt{\\frac{T}{\\mu}}")+
   p("这是一维波动方程，简谐波 $y=A\\cos(\\omega t-kx)$ 是其解，代入可验证 $v=\\omega/k$。"))
 )},
]},
# ---- 5.5 波的干涉与驻波 ----
{
"name": "5.5 波的叠加、干涉与驻波",
"color": "#be185d",
"desc": "波的叠加原理、干涉条件、驻波",
"items": [
{"id":"c5s5-1","name":"波的干涉与驻波","tags":["thm","der"],"brief":"两列波叠加产生干涉和驻波。",
 "body": wrap(
   thm("波的叠加原理",p("几列波在同一介质中传播时，各自保持原有特性独立传播；在相遇区域，任一质点的位移为各列波单独引起位移的矢量和。"))+
   thm("干涉条件",p("两列波频率相同、振动方向相同、相位差恒定，叠加后产生稳定的干涉图样。"))+
   der(p("<strong>干涉极值条件：</strong>两列波 $y_1=A_1\\cos(\\omega t-kr_1+\\varphi_1)$，$y_2=A_2\\cos(\\omega t-kr_2+\\varphi_2)$ 叠加，相位差 $\\Delta\\varphi=(\\varphi_2-\\varphi_1)-k(r_2-r_1)$。")+
   p("当 $\\Delta\\varphi=2n\\pi$ 时，合振幅最大 $A=A_1+A_2$（加强）；当 $\\Delta\\varphi=(2n+1)\\pi$ 时，合振幅最小 $A=|A_1-A_2|$（减弱）。")+
   fml("\\Delta r = r_2-r_1 = n\\lambda \\quad(\\text{加强}),\\qquad \\Delta r = (n+\\tfrac{1}{2})\\lambda \\quad(\\text{减弱})"))+
   thm("驻波",p("两列振幅相同、沿相反方向传播的相干波叠加形成驻波：")+
   fml("y = 2A\\cos\\frac{2\\pi x}{\\lambda}\\cos\\omega t"))+
   der(p("<strong>驻波推导：</strong>$y_1=A\\cos(\\omega t-kx)$，$y_2=A\\cos(\\omega t+kx)$，叠加：")+
   fml("y = A[\\cos(\\omega t-kx)+\\cos(\\omega t+kx)] = 2A\\cos(kx)\\cos(\\omega t)")+
   p("其中 $k=2\\pi/\\lambda$。当 $\\cos\\frac{2\\pi x}{\\lambda}=0$ 时 $y=0$（波节）；当 $|\\cos\\frac{2\\pi x}{\\lambda}|=1$ 时振幅最大（波腹）。波节间距 $\\lambda/2$。"))
 )},
]},
# ---- 5.6 振动的合成 ----
{
"name": "5.6 振动的合成",
"color": "#be185d",
"desc": "拍现象、李萨如图形、同方向与垂直方向振动的合成",
"items": [
{"id":"c5s6-1","name":"拍现象","tags":["thm","der"],"brief":"两频率相近的同方向振动合成产生拍。",
 "fig":"beats","figCap":"拍现象：合振动振幅周期性变化（包络）",
 "body": wrap(
   defn("拍",p("两个频率相近、同方向的简谐振动合成时，合振幅周期性变化的现象称为<strong>拍</strong>。"))+
   thm("拍频",p("设两分振动 $y_1=A\\cos\\omega_1 t$，$y_2=A\\cos\\omega_2 t$，且 $|\\omega_1-\\omega_2|\\ll\\omega_1,\\omega_2$，则合振动：")+
   fml("y = 2A\\cos\\left(\\frac{\\omega_1-\\omega_2}{2}t\\right)\\cos\\left(\\frac{\\omega_1+\\omega_2}{2}t\\right)")+
   p("拍频（单位时间内振幅极大出现的次数）：$f_{\\text{拍}}=|f_1-f_2|$，拍周期 $T_{\\text{拍}}=\\frac{1}{|f_1-f_2|}$。"))+
   der(p("<strong>推导：</strong>利用和差化积公式 $\\cos\\alpha+\\cos\\beta=2\\cos\\frac{\\alpha-\\beta}{2}\\cos\\frac{\\alpha+\\beta}{2}$：")+
   fml("y = A\\cos\\omega_1 t + A\\cos\\omega_2 t = 2A\\cos\\frac{\\omega_1-\\omega_2}{2}t\\cdot\\cos\\frac{\\omega_1+\\omega_2}{2}t")+
   p("令 $\\omega_{\\text{avg}}=\\frac{\\omega_1+\\omega_2}{2}$（平均角频率），$\\omega_{\\text{mod}}=\\frac{|\\omega_1-\\omega_2|}{2}$（调制角频率），则 $y=2A\\cos(\\omega_{\\text{mod}}t)\\cos(\\omega_{\\text{avg}}t)$。")+
   p("由于 $\\omega_{\\text{mod}}\\ll\\omega_{\\text{avg}}$，$\\cos(\\omega_{\\text{mod}}t)$ 变化缓慢，可视为<strong>振幅包络</strong>。振幅包络 $|2A\\cos(\\omega_{\\text{mod}}t)|$ 的周期为 $\\frac{\\pi}{\\omega_{\\text{mod}}}=\\frac{2\\pi}{|\\omega_1-\\omega_2|}=\\frac{1}{|f_1-f_2|}$，故拍频 $f_{\\text{拍}}=|f_1-f_2|$。"))+
   app(p("拍的应用：利用拍频校准乐器、测量超声波频率、多普勒测速等。"))
 )},
{"id":"c5s6-2","name":"李萨如图形","tags":["thm","der","app"],"brief":"两个互相垂直的简谐振动合成的轨迹。",
 "fig":"lissajous","figCap":"李萨如图形示例（ω_x:ω_y = 2:1）",
 "body": wrap(
   defn("李萨如图形",p("两个频率成整数比、互相垂直的简谐振动合成时，质点的运动轨迹为封闭曲线，称为<strong>李萨如图形</strong>。"))+
   thm("参数方程",p("设 $x=A_x\\cos(\\omega_x t+\\varphi_x)$，$y=A_y\\cos(\\omega_y t+\\varphi_y)$，则轨迹由参数方程确定。当 $\\omega_x:\\omega_y$ 为有理数时轨迹闭合。"))+
   der(p("<strong>频率比与切点数关系：</strong>在李萨如图中，水平方向切点数 $N_x$ 与垂直方向切点数 $N_y$ 之比等于频率的反比：")+
   fml("\\frac{N_x}{N_y} = \\frac{\\omega_y}{\\omega_x}")+
   p("由此可由已知一个频率测量未知频率。例如图中 $\\omega_x:\\omega_y=2:1$，水平切点数与垂直切点数之比为 $1:2$。"))+
   app(p("应用：示波器观察李萨如图形测量频率、相位差。当两振动频率相同（$\\omega_x=\\omega_y$）时，轨迹为椭圆（特殊情形为直线或圆），椭圆形状由相位差 $\\Delta\\varphi=\\varphi_y-\\varphi_x$ 决定。"))
 )},
]},
# ---- 5.7 波的反射与半波损失 ----
{
"name": "5.7 波的反射与半波损失",
"color": "#be185d",
"desc": "波在介质界面的反射、相位突变与半波损失",
"items": [
{"id":"c5s7-1","name":"半波损失","tags":["thm","der","note"],"brief":"波从波疏介质入射到波密介质时反射波相位突变π。",
 "fig":"halfwave","figCap":"波在界面的反射：波疏→波密时反射波反相",
 "body": wrap(
   defn("半波损失",p("当波从<strong>波疏介质</strong>（波阻 $Z_1=\\rho_1 v_1$ 较小）入射到<strong>波密介质</strong>（$Z_2>Z_1$）界面并反射时，反射波在界面处相位发生 $\\pi$ 的突变，等效于损失了半个波长，称为<strong>半波损失</strong>。"))+
   thm("反射波相位变化",p("设入射波 $y_i=A_i\\cos(\\omega t-k_1 x)$，在 $x=0$ 界面反射。反射波 $y_r=A_r\\cos(\\omega t+k_1 x+\\varphi_r)$，其中：")+
   fml("\\varphi_r = \\begin{cases} 0, & Z_2 < Z_1 \\ (\\text{波密}\\to\\text{波疏}) \\\\ \\pi, & Z_2 > Z_1 \\ (\\text{波疏}\\to\\text{波密}) \\end{cases}"))+
   der(p("<strong>边界条件推导：</strong>在界面 $x=0$ 处，位移连续 $y_i+y_r=y_t$，应力（张力）连续。对弦波，张力与斜率成正比：$T\\frac{\\partial y}{\\partial x}$ 连续。")+
   p("设入射波 $y_i=A_i\\cos(\\omega t-k_1 x)$，反射波 $y_r=A_r\\cos(\\omega t+k_1 x+\\varphi_r)$，透射波 $y_t=A_t\\cos(\\omega t-k_2 x)$。")+
   p("位移连续：$A_i+A_r=A_t$。张力连续：$T_1 k_1(A_i-A_r)=T_2 k_2 A_t$。利用 $Z=\\rho v=T/v$、$k=\\omega/v$，可得反射系数：")+
   fml("\\frac{A_r}{A_i} = \\frac{Z_1-Z_2}{Z_1+Z_2}")+
   p("当 $Z_2>Z_1$（波疏→波密）时，$A_r/A_i<0$，即反射波振幅为负，等效于相位突变 $\\pi$，产生半波损失；当 $Z_2<Z_1$ 时无半波损失。"))+
   note(p("<strong>光的半波损失：</strong>光从光疏介质入射到光密介质表面反射时也有半波损失（相位突变 $\\pi$）。这是薄膜干涉（如牛顿环、劈尖干涉）中额外光程差 $\\lambda/2$ 的来源。"))
 )},
]},
# ---- 5.8 简谐振动的旋转矢量表示 ----
{
"name": "5.8 简谐振动的旋转矢量表示",
"color": "#be185d",
"desc": "用旋转矢量直观表示简谐振动的振幅、角频率与相位",
"items": [
{"id":"c5s8-1","name":"旋转矢量法","tags":["def","der"],"brief":"匀速圆周运动的投影可表示简谐振动。",
 "body": wrap(
   defn("旋转矢量",p("自原点 $O$ 作一长度为振幅 $A$ 的矢量 $\\mathbf{A}$，使其以角速度 $\\omega$ 逆时针匀速转动。$t=0$ 时与 $x$ 轴夹角为初相位 $\\varphi$，则该矢量称为<strong>旋转矢量</strong>。"))+
   thm("投影与位移",p("旋转矢量在 $x$ 轴上的投影即为简谐振动的位移：")+
   fml("x = A\\cos(\\omega t + \\varphi)"))+
   der(p("<strong>推导：</strong>$t$ 时刻矢量 $\\mathbf{A}$ 与 $x$ 轴夹角为 $\\omega t+\\varphi$，其 $x$ 分量：")+
   fml("x = A\\cos(\\omega t + \\varphi)")+
   p("矢量端点的速度大小为 $v=\\omega A$，方向沿切线。其 $x$ 分量为：")+
   fml("v_x = -\\omega A\\sin(\\omega t + \\varphi) = -\\omega A\\cos\\left(\\omega t+\\varphi+\\frac{\\pi}{2}\\right)")+
   p("与简谐振动速度 $v=-A\\omega\\sin(\\omega t+\\varphi)$ 一致。加速度为端点向心加速度的 $x$ 分量：")+
   fml("a_x = -\\omega^2 A\\cos(\\omega t + \\varphi) = -\\omega^2 x")+
   p("正好满足简谐振动微分方程 $a=-\\omega^2 x$。"))+
   note(p("旋转矢量法将代数运算转化为几何运算，便于直观分析相位关系和振动合成。"))
 )},
]},
# ---- 5.9 相位与相位差 ----
{
"name": "5.9 相位与相位差",
"color": "#be185d",
"desc": "相位的物理意义与两个振动的相位差",
"items": [
{"id":"c5s9-1","name":"相位与相位差","tags":["def","thm","der"],"brief":"相位描述振动状态，相位差比较两振动的步调。",
 "body": wrap(
   defn("相位",p("简谐振动 $x=A\\cos(\\omega t+\\varphi)$ 中，$\\omega t+\\varphi$ 称为<strong>相位</strong>，它完全决定了 $t$ 时刻振动的位移、速度和加速度（即振动状态）。$t=0$ 时的相位 $\\varphi$ 为初相位。"))+
   defn("相位差",p("两个同频率简谐振动 $x_1=A_1\\cos(\\omega t+\\varphi_1)$、$x_2=A_2\\cos(\\omega t+\\varphi_2)$ 的相位差为：")+
   fml("\\Delta\\varphi = (\\omega t+\\varphi_2) - (\\omega t+\\varphi_1) = \\varphi_2 - \\varphi_1"))+
   der(p("<strong>相位差的物理意义：</strong>")+
   p("• $\\Delta\\varphi=0$：两振动<strong>同相</strong>，同时到达最大、平衡位置、最小。<br>• $\\Delta\\varphi=\\pi$：两振动<strong>反相</strong>，步调完全相反。<br>• $\\Delta\\varphi>0$：$x_2$ 比 $x_1$ <strong>超前</strong> $\\Delta\\varphi$（或 $x_1$ 落后）。<br>• $\\Delta\\varphi<0$：$x_2$ 比 $x_1$ <strong>落后</strong> $|\\Delta\\varphi|$。")+
   p("相位差也可用时间差表示：$\\Delta t = \\frac{\\Delta\\varphi}{\\omega} = \\frac{\\Delta\\varphi}{2\\pi}T$。"))
 )},
]},
# ---- 5.10 阻尼振动的三种状态 ----
{
"name": "5.10 阻尼振动的三种状态",
"color": "#be185d",
"desc": "欠阻尼、过阻尼与临界阻尼的运动特征",
"items": [
{"id":"c5s10-1","name":"阻尼振动的三种状态","tags":["thm","der"],"brief":"根据阻尼大小分为欠阻尼、过阻尼和临界阻尼。",
 "body": wrap(
   thm("阻尼振动方程",p("阻尼振动方程 $m\\ddot{x}+\\gamma\\dot{x}+kx=0$，令 $\\beta=\\frac{\\gamma}{2m}$（阻尼因子），$\\omega_0=\\sqrt{k/m}$（固有频率），特征方程 $r^2+2\\beta r+\\omega_0^2=0$，根为 $r=-\\beta\\pm\\sqrt{\\beta^2-\\omega_0^2}$。"))+
   der(p("<strong>三种阻尼状态：</strong>")+
   p("• <strong>欠阻尼</strong>（$\\beta<\\omega_0$）：$r=-\\beta\\pm i\\omega$，$\\omega=\\sqrt{\\omega_0^2-\\beta^2}$，解为衰减振动：")+
   fml("x = A_0 e^{-\\beta t}\\cos(\\omega t+\\varphi)")+
   p("• <strong>临界阻尼</strong>（$\\beta=\\omega_0$）：$r=-\\beta$（重根），解为非周期衰减：")+
   fml("x = (C_1+C_2 t)e^{-\\beta t}")+
   p("• <strong>过阻尼</strong>（$\\beta>\\omega_0$）：$r=-\\beta\\pm\\sqrt{\\beta^2-\\omega_0^2}$（两负实根），解为非周期衰减：")+
   fml("x = C_1 e^{r_1 t} + C_2 e^{r_2 t}"))+
   note(p("临界阻尼时系统回到平衡位置的时间最短，常用于精密仪器（如电流表、天平）的阻尼设计，使指针快速稳定不摆动。"))
 )},
]},
# ---- 5.11 同方向同频率简谐振动的合成 ----
{
"name": "5.11 同方向同频率简谐振动的合成",
"color": "#be185d",
"desc": "两个同方向同频率振动合成仍为同频率简谐振动",
"items": [
{"id":"c5s11-1","name":"同方向同频率振动的合成","tags":["thm","der"],"brief":"合成振幅由相位差决定。",
 "body": wrap(
   thm("合成公式",p("两个同方向、同频率的简谐振动 $x_1=A_1\\cos(\\omega t+\\varphi_1)$、$x_2=A_2\\cos(\\omega t+\\varphi_2)$ 合成后仍为同频率简谐振动：")+
   fml("x = x_1+x_2 = A\\cos(\\omega t+\\varphi)"))+
   der(p("<strong>推导（旋转矢量法）：</strong>两旋转矢量 $\\mathbf{A}_1,\\mathbf{A}_2$ 以相同角速度 $\\omega$ 转动，夹角 $\\Delta\\varphi=\\varphi_2-\\varphi_1$ 恒定。合矢量 $\\mathbf{A}=\\mathbf{A}_1+\\mathbf{A}_2$ 也以 $\\omega$ 转动，其投影即合振动。")+
   p("由矢量加法（余弦定理），合成振幅：")+
   fml("A = \\sqrt{A_1^2+A_2^2+2A_1A_2\\cos(\\varphi_2-\\varphi_1)}")+
   p("合振动初相位满足：")+
   fml("\\tan\\varphi = \\frac{A_1\\sin\\varphi_1+A_2\\sin\\varphi_2}{A_1\\cos\\varphi_1+A_2\\cos\\varphi_2}"))+
   der(p("<strong>特例：</strong>")+
   p("• 同相（$\\Delta\\varphi=2k\\pi$）：$A=A_1+A_2$，振幅最大，加强。<br>• 反相（$\\Delta\\varphi=(2k+1)\\pi$）：$A=|A_1-A_2|$，振幅最小，减弱。<br>• 若 $A_1=A_2$ 且反相，则 $A=0$，振动抵消。"))
 )},
]},
# ---- 5.12 波的能量与能流 ----
{
"name": "5.12 波的能量与能流",
"color": "#be185d",
"desc": "波传播时的能量、能量密度与能流密度",
"items": [
{"id":"c5s12-1","name":"波的能量与能流密度","tags":["thm","der"],"brief":"波的能量随波传播，平均能流密度与振幅平方成正比。",
 "body": wrap(
   thm("波的能量密度",p("简谐波 $y=A\\cos(\\omega t-kx)$ 在介质中引起的能量密度（单位体积能量）为：")+
   fml("w = \\tfrac{1}{2}\\rho\\omega^2 A^2\\sin^2(\\omega t-kx)")+
   p("平均能量密度 $\\bar{w}=\\frac{1}{2}\\rho\\omega^2 A^2$。"))+
   der(p("<strong>推导：</strong>取介质中体积元 $\\Delta V$，质量 $\\Delta m=\\rho\\Delta V$。振动速度 $v=\\frac{\\partial y}{\\partial t}=-A\\omega\\sin(\\omega t-kx)$，动能：")+
   fml("\\Delta E_k = \\tfrac{1}{2}\\Delta m\\cdot v^2 = \\tfrac{1}{2}\\rho\\Delta V\\cdot\\omega^2 A^2\\sin^2(\\omega t-kx)")+
   p("势能与动能同相同等（弹性介质中形变与速度同步变化），总能为动能的两倍。能量密度 $w=\\frac{\\Delta E}{\\Delta V}$ 即得上式。"))+
   thm("能流密度（波的强度）",p("单位时间内通过垂直于波传播方向单位面积的平均能量：")+
   fml("I = \\bar{w}\\cdot v = \\tfrac{1}{2}\\rho\\omega^2 A^2 v")+
   p("波的强度与振幅平方、角频率平方成正比。"))
 )},
]},
# ---- 5.13 惠更斯原理与波的衍射 ----
{
"name": "5.13 惠更斯原理与波的衍射",
"color": "#be185d",
"desc": "惠更斯原理与波的衍射现象",
"items": [
{"id":"c5s13-1","name":"惠更斯原理与衍射","tags":["thm","note"],"brief":"介质中波前上每一点都可看作发射子波的波源。",
 "body": wrap(
   thm("惠更斯原理",p("介质中波前上的每一点都可看作发射子波的波源，其后任一时刻这些子波的包络面就是新的波前。"))+
   defn("波的衍射",p("波在传播过程中遇到障碍物或小孔时，偏离直线传播而绕到障碍物后面的现象称为<strong>衍射</strong>（绕射）。"))+
   der(p("<strong>衍射条件：</strong>当障碍物或孔的尺寸与波长相近或更小时，衍射现象明显。由惠更斯原理，小孔处波前上各点发射子波，子波的包络面使波进入几何阴影区。")+
   p("波长越长（相对障碍物尺寸），衍射越显著。例如声波波长较长，能绕过墙壁传播；光波波长很短，通常表现为直线传播。"))+
   note(p("惠更斯原理能解释波的反射、折射和衍射，但不能解释衍射图样的强度分布，后者需用惠更斯-菲涅耳原理（考虑子波的相干叠加）。"))
 )},
]},
# ---- 5.14 多普勒效应 ----
{
"name": "5.14 多普勒效应",
"color": "#be185d",
"desc": "波源或观察者运动时观测频率的变化",
"items": [
{"id":"c5s14-1","name":"多普勒效应","tags":["thm","der"],"brief":"波源与观察者相对运动导致观测频率改变。",
 "body": wrap(
   thm("多普勒公式",p("设波速为 $v$，波源频率为 $f_0$，观察者速度 $v_O$（朝向波源为正），波源速度 $v_S$（朝向观察者为正），则观察者接收到的频率为：")+
   fml("f = \\frac{v+v_O}{v-v_S}f_0"))+
   der(p("<strong>推导：</strong>波源静止时，波长 $\\lambda=v/f_0$。观察者以 $v_O$ 朝向波源运动时，相对波的速度为 $v+v_O$，故接收频率：")+
   fml("f = \\frac{v+v_O}{\\lambda} = \\frac{v+v_O}{v}f_0")+
   p("当波源以 $v_S$ 朝向观察者运动时，波长被压缩为 $\\lambda'=(v-v_S)/f_0$（波源在一个周期内移动 $v_S T$）。此时观察者静止，接收频率：")+
   fml("f = \\frac{v}{\\lambda'} = \\frac{v}{v-v_S}f_0")+
   p("两者同时运动时合并为 $f=\\frac{v+v_O}{v-v_S}f_0$。当波源远离时 $v_S$ 取负，频率降低（红移）；靠近时频率升高（蓝移）。"))+
   app(p("<strong>应用：</strong>交警雷达测速、医学超声多普勒血流检测、天文学中通过谱线红移测定天体退行速度。"))
 )},
]},
# ---- 5.15 声波与声强级 ----
{
"name": "5.15 声波与声强级",
"color": "#be185d",
"desc": "声波的频率范围与声强级的对数标度",
"items": [
{"id":"c5s15-1","name":"声波与声强级","tags":["def","note"],"brief":"可闻声波、超声波、次声波及声强级分贝表示。",
 "body": wrap(
   defn("声波分类",p("• <strong>次声波</strong>：$f<20\\,\\text{Hz}$，人耳听不到。<br>• <strong>可闻声波</strong>：$20\\,\\text{Hz}\\le f\\le 20\\,\\text{kHz}$，人耳可感知。<br>• <strong>超声波</strong>：$f>20\\,\\text{kHz}$，方向性好、穿透能力强。"))+
   defn("声强级",p("由于人耳对声强的响应接近对数，引入声强级（单位：分贝 dB）：")+
   fml("L = 10\\lg\\frac{I}{I_0}")+
   p("其中 $I_0=10^{-12}\\,\\text{W/m}^2$ 为参考声强（人耳听觉阈）。"))+
   note(p("声强级每增加 10 dB，声强增大 10 倍，人耳主观感觉响度约增加一倍。普通交谈约 60 dB，闹市约 80 dB，电锯约 100 dB，长期暴露在 85 dB 以上可能损伤听力。"))
 )},
]},
]

# ---------- CHAPTERS ----------
CHAPTERS = [
    {"id":"m-ch1","num":"第一章","title":"质点运动学","en":"KINEMATICS",
     "desc":"位置、速度、加速度的矢量描述，匀变速直线运动公式，抛体运动轨迹，圆周运动的向心加速度，以及伽利略变换下的相对运动。",
     "sections": ch1_sections},
    {"id":"m-ch2","num":"第二章","title":"质点动力学","en":"DYNAMICS",
     "desc":"牛顿三大定律与惯性系，重力、弹力、摩擦力的分析，动量与冲量，动量守恒定律的推导，以及弹性碰撞与恢复系数。",
     "sections": ch2_sections},
    {"id":"m-ch3","num":"第三章","title":"功能关系","en":"WORK & ENERGY",
     "desc":"功与功率的定义，动能定理的推导，保守力与势能（重力势能、弹性势能），机械能守恒定律，以及系统的功能原理。",
     "sections": ch3_sections},
    {"id":"m-ch4","num":"第四章","title":"刚体动力学","en":"RIGID BODY",
     "desc":"刚体的平动与转动，转动惯量与平行轴定理，转动定律（力矩=转动惯量×角加速度），角动量定理与角动量守恒，刚体平衡条件。",
     "sections": ch4_sections},
    {"id":"m-ch5","num":"第五章","title":"简谐振动与机械波","en":"OSCILLATIONS & WAVES",
     "desc":"简谐振动的微分方程与解，单摆与复摆周期，阻尼振动与受迫振动共振，机械波的波动方程，波的干涉与驻波。",
     "sections": ch5_sections},
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
  .la-nav-tab.c1{color:#1e40af;border-color:#bfdbfe}
  .la-nav-tab.c2{color:#0f766e;border-color:#99f6e4}
  .la-nav-tab.c3{color:#047857;border-color:#a7f3d0}
  .la-nav-tab.c4{color:#0e7490;border-color:#a5f3fc}
  .la-nav-tab.c5{color:#be185d;border-color:#fbcfe8}
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
  .la-phase-title.m-ch1::before{background:#2563eb}
  .la-phase-title.m-ch2::before{background:#0d9488}
  .la-phase-title.m-ch3::before{background:#059669}
  .la-phase-title.m-ch4::before{background:#0891b2}
  .la-phase-title.m-ch5::before{background:#be185d}
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
<meta name="description" content="力学知识体系：质点运动学、质点动力学、功能关系、刚体动力学、简谐振动与机械波">
<title>力学 · 知识体系</title>
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
    <div class="la-eyebrow">NEWTONIAN MECHANICS · KNOWLEDGE MAP</div>
    <h1>力学 · 知识体系</h1>
    <p class="la-subtitle">质点运动学 · 质点动力学 · 功能关系 · 刚体动力学 · 简谐振动与机械波</p>
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
    <div>力学 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于经典力学核心知识体系整理</div>
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
    with open("/workspace/newtonian-mechanics.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated newtonian-mechanics.html ({len(html)} chars)")
