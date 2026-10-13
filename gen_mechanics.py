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
# -*- coding: utf-8 -*-
ch1_sections = [
# ---- 1.1 空间、时间与参考系 ----
{
"name": "1.1 空间、时间与参考系",
"color": "#2563eb",
"desc": "空间与时间的绝对性、质点模型，以及描述运动所需的参考系与坐标系",
"items": [
{"id":"c1s1-1","name":"空间、时间与质点模型","tags":["def","der","note"],"brief":"力学以绝对空间、绝对时间和质点模型为基础，运动描述具有相对性。",
 "body": wrap(
   defn("空间与时间",p("经典力学中，空间是物质存在与运动的广延形式，时间是描述运动持续性与先后次序的参量。二者被认为相互独立、绝对、均匀，其度量与观测者的运动状态无关：")+
   fml("\\text{长度 } \\Delta l,\\qquad \\text{时间间隔 } \\Delta t"))+
   defn("质点",p("当物体的形状与大小在所研究的问题中可以忽略时，可将其抽象为具有全部质量而无体积的几何点，称为<strong>质点</strong>。"))+
   der(p("<strong>质点模型的合理性依据：</strong>设物体的线度为 $L$，所研究运动涉及的特征距离为 $d$。")+
   p("当线度远小于特征距离时，物体上各点运动状态的差别相对整体位移为高阶小量：")+
   fml("\\frac{L}{d} \\to 0 \\implies \\text{各点运动差异可忽略，视为质点}")+
   p("进一步，任何有限大小的物体都可看作由大量质点组成的<strong>质点系</strong>，刚体即其中质点间距离不变的质点系，故质点力学是全部力学的基础。"))+
   exa(p("<strong>例：</strong>研究地球绕太阳公转时，地球半径约 $6.4\\times10^{3}\\,\\text{km}$ 远小于日地距离约 $1.5\\times10^{8}\\,\\text{km}$，$L/d \\sim 10^{-5}$，故地球可视为质点；而研究地球自转时则不可。"))+
   note(p("运动的描述具有<strong>相对性</strong>：同一运动在不同参考系中观测到的轨迹、位移、速度可以完全不同，因此描述运动必须首先指明参考系。"))
 )},
{"id":"c1s1-2","name":"参考系与坐标系","tags":["def","der","exa"],"brief":"描述运动须选定参考系，并在其上建立坐标系定量表示位置。",
 "body": wrap(
   defn("参考系与坐标系",p("为描述物体运动而选作标准的另一物体或物体系，称为<strong>参考系</strong>；在参考系上为实现定量描述而引入的数学框架，称为<strong>坐标系</strong>。"))+
   der(p("<strong>从参考系到坐标系：</strong>仅有参考系只能定性判断物体是否运动、朝何方向运动；要给出位置的具体数值，必须建立坐标系。")+
   p("常用坐标系及其适用情形：")+
   fml("\\text{直角坐标 } (x,y,z);\\quad \\text{平面极坐标 } (r,\\theta);\\quad \\text{自然坐标 } (s,\\rho)")+
   p("坐标系的选择只影响计算的繁简，不改变运动本身；同一矢量在不同坐标系下分量不同，但矢量整体保持不变。"))+
   exa(p("<strong>例：</strong>描述卫星绕地球的运动，取地心为坐标原点。椭圆轨道用平面极坐标 $(r,\\theta)$ 最自然，$r$ 随 $\\theta$ 变化；圆轨道则用自然坐标，曲率半径 $\\rho$ 恒等于轨道半径。"))+
   note(p("参考系决定运动的<strong>定性</strong>描述，坐标系决定运动的<strong>定量</strong>表示。"))
 )},
]},
# ---- 1.2 质点的直线运动 ----
{
"name": "1.2 质点的直线运动",
"color": "#1d4ed8",
"desc": "匀速与匀变速直线运动，运动学公式的积分推导及常用推论",
"items": [
{"id":"c1s2-1","name":"匀速直线运动","tags":["def","der","exa"],"brief":"速度恒定的一维运动，位移与时间成正比。",
 "body": wrap(
   defn("匀速直线运动",p("质点沿直线运动，且速度的大小与方向均不随时间改变，称为<strong>匀速直线运动</strong>。取轨迹为 $x$ 轴，速度为常数 $v$：")+
   fml("\\frac{dx}{dt} = v = \\text{const}"))+
   der(p("<strong>运动方程的推导：</strong>由 $\\dfrac{dx}{dt}=v$，分离变量后在时间区间 $[0,t]$ 上积分：")+
   fml("\\int_{x_0}^{x} dx = \\int_0^t v\\,dt \\implies x - x_0 = v\\,t")+
   p("由于被积函数为常数，积分即得一次函数形式的运动方程：")+
   fml("x = x_0 + v\\,t")+
   p("其中 $x_0$ 为 $t=0$ 的位置，由初条件确定。"))+
   exa(p("<strong>例：</strong>汽车以 $v = 20\\,\\text{m/s}$ 匀速行驶，$5\\,\\text{s}$ 内的位移为 $\\Delta x = v t = 100\\,\\text{m}$，与起点的具体位置无关。"))
 )},
{"id":"c1s2-2","name":"匀变速直线运动公式","tags":["thm","der","app"],"brief":"加速度恒定时，由两次积分推出三大运动学公式。",
 "body": wrap(
   thm("匀变速直线运动",p("若质点做直线运动且加速度 $a$ 恒定，初速度 $v_0$、初位置 $x_0$，则其速度、位置与速度-位移关系为：")+
   fml("v = v_0 + at,\\quad x = x_0 + v_0 t + \\tfrac{1}{2} a t^2,\\quad v^2 - v_0^2 = 2a(x-x_0)"))+
   der(p("<strong>第一步：由加速度定义求速度。</strong>由 $a = \\dfrac{dv}{dt}$ 分离变量得 $dv = a\\,dt$，从 $t=0$ 到 $t$ 积分，$a$ 为常数可提出积分号：")+
   fml("\\int_{v_0}^{v} dv = a\\int_0^t dt \\implies v - v_0 = at \\implies v = v_0 + at")+
   p("<strong>第二步：由速度定义求位置。</strong>将 $v = v_0 + at$ 代入 $\\dfrac{dx}{dt}$，再积分一次：")+
   fml("\\int_{x_0}^{x} dx = \\int_0^t (v_0 + at)\\,dt \\implies x - x_0 = v_0 t + \\tfrac{1}{2} a t^2")+
   p("<strong>第三步：消去时间得速度-位移关系。</strong>由第一式解出 $t = \\dfrac{v-v_0}{a}$ 并代入第二式：")+
   fml("x - x_0 = v_0 \\cdot \\frac{v-v_0}{a} + \\frac{1}{2}a\\left(\\frac{v-v_0}{a}\\right)^2 = \\frac{2v_0(v-v_0) + (v-v_0)^2}{2a} = \\frac{v^2 - v_0^2}{2a}")+
   p("整理即得 $v^2 - v_0^2 = 2a(x-x_0)$。三式中只有两式独立，第三式可由前两式消去 $t$ 得到。"))+
   app(p("<strong>应用：</strong>匀加速启动的列车、匀减速刹车的汽车均可用此三式联立求解（已知五量之二求其余）。当 $a = 0$ 时三式退化为匀速直线运动。"))
 )},
{"id":"c1s2-3","name":"匀变速运动的推论与图象","tags":["thm","der","exa"],"brief":"平均速度公式、逐差公式与 v-t 图象的物理意义。",
 "body": wrap(
   thm("匀变速运动的推论",p("对匀变速直线运动，设一段时间内初、末速度为 $v_0, v_t$，位移为 $x$，历时 $t$，取连续相等时间间隔 $T$ 的相邻位移为 $x_n, x_{n+1}$，则：")+
   fml("\\bar{v} = \\frac{v_0 + v_t}{2},\\qquad x = \\frac{v_0 + v_t}{2}\\,t,\\qquad \\Delta x = x_{n+1} - x_n = a T^2"))+
   der(p("<strong>平均速度公式的推导：</strong>由 $x = v_0 t + \\tfrac{1}{2}at^2$ 与 $a = \\dfrac{v_t - v_0}{t}$ 消去 $a$：")+
   fml("x = v_0 t + \\frac{1}{2}\\cdot\\frac{v_t - v_0}{t}\\cdot t^2 = \\frac{2v_0 + v_t - v_0}{2}\\,t = \\frac{v_0 + v_t}{2}\\,t")+
   p("即平均速度等于初、末速度的算术平均。")+
   p("<strong>逐差公式的推导：</strong>第 $n$ 段结束时 $t_n = nT$，位移为 $x_n = v_0 (nT) + \\tfrac{1}{2}a(nT)^2$，故相邻两段位移之差：")+
   fml("\\Delta x = x_{n+1} - x_n = \\tfrac{1}{2}a\\left[(n+1)^2 - n^2\\right]T^2 = aT^2")+
   p("差值恒为 $aT^2$，与 $n$ 无关，故常用于纸带实验测定加速度。"))+
   exa(p("<strong>v-t 图象：</strong>图线与时间轴所围的面积等于位移，图线斜率等于加速度。匀变速运动的图线为直线、斜率恒定，直观验证了 $a$ 不变；匀加速时面积为梯形，正是 $\\dfrac{v_0+v_t}{2}\\,t$。"))
 )},
]},
# ---- 1.3 曲线运动与位移 ----
{
"name": "1.3 曲线运动与位移",
"color": "#3b82f6",
"desc": "一般曲线运动中的位移矢量、元位移与路程的关系",
"items": [
{"id":"c1s3-1","name":"曲线运动与位移矢量","tags":["def","der","exa"],"brief":"位移是始末位置的矢量差，与路径形状无关。",
 "body": wrap(
   defn("位移矢量",p("质点从位置 $A$（位矢 $\\mathbf{r}_1$）运动到位置 $B$（位矢 $\\mathbf{r}_2$），其<strong>位移</strong>定义为位矢的增量：")+
   fml("\\Delta \\mathbf{r} = \\mathbf{r}_2 - \\mathbf{r}_1"))+
   der(p("<strong>有限位移与元位移：</strong>位移只由始、末位置决定，与所走的路径形状无关。")+
   p("把过程无限细分，每个无限小步骤对应的位移称为<strong>元位移</strong> $d\\mathbf{r}$；沿轨迹对元位移矢量求和（积分），得总位移：")+
   fml("\\Delta \\mathbf{r} = \\int_{A}^{B} d\\mathbf{r} = \\mathbf{r}_2 - \\mathbf{r}_1")+
   p("该积分只依赖积分端点，不依赖积分路径，从数学上说明了位移的位置依赖性。"))+
   exa(p("<strong>例：</strong>质点沿半径 $R$ 的半圆从 $(R,0)$ 运动到 $(-R,0)$，位移大小为 $|\\Delta\\mathbf{r}| = 2R$，方向沿 $-x$ 轴。无论走上半圆还是下半圆，位移完全相同。"))
 )},
{"id":"c1s3-2","name":"路程与位移的关系","tags":["def","der","note"],"brief":"路程为轨迹长度，恒不小于位移的大小。",
 "body": wrap(
   defn("路程",p("质点沿轨迹实际经过的路径长度称为<strong>路程</strong> $s$。它是标量，且随运动进行单调不减。"))+
   der(p("<strong>位移大小与路程的比较：</strong>将轨迹分割为无限多个元段，每段的弧长为 $ds = |d\\mathbf{r}|$，而该段位移是弧首尾相连的<strong>弦</strong>。")+
   p("弦长不超过对应弧长，故对每一元段有 $|d\\mathbf{r}| \\le ds$；对整条路径积分并取模：")+
   fml("|\\Delta \\mathbf{r}| = \\left| \\int_{A}^{B} d\\mathbf{r} \\right| \\le \\int_{A}^{B} |d\\mathbf{r}| = \\int_{A}^{B} ds = s")+
   p("等号当且仅当质点始终沿同一方向做直线运动时成立。"))+
   exa(p("<strong>例：</strong>运动员沿 $400\\,\\text{m}$ 环形跑道跑完一整圈回到起点，位移 $\\Delta \\mathbf{r} = \\mathbf{0}$，而路程 $s = 400\\,\\text{m}$，二者相差最大；若沿直线单向跑 $400\\,\\text{m}$，则位移大小恰等于路程。"))+
   note(p("位移是<strong>矢量</strong>、只依赖始末位置；路程是<strong>标量</strong>、依赖具体路径。二者量纲相同，但物理含义不同，不可混用。"))
 )},
]},
# ---- 1.4 速度与速率 ----
{
"name": "1.4 速度与速率",
"color": "#0ea5e9",
"desc": "平均速度与瞬时速度的极限定义，速率与平均速率的区别",
"items": [
{"id":"c1s4-1","name":"平均速度与瞬时速度","tags":["def","der","exa"],"brief":"速度为位矢对时间的变化率，方向沿轨迹切线。",
 "body": wrap(
   defn("平均速度与瞬时速度",p("<strong>平均速度</strong>定义为位移与所用时间之比：")+
   fml("\\bar{\\mathbf{v}} = \\frac{\\Delta \\mathbf{r}}{\\Delta t}")+
   p("<strong>瞬时速度</strong>是 $\\Delta t \\to 0$ 时平均速度的极限：")+
   fml("\\mathbf{v} = \\lim_{\\Delta t \\to 0} \\frac{\\Delta \\mathbf{r}}{\\Delta t} = \\frac{d\\mathbf{r}}{dt}"))+
   der(p("<strong>瞬时速度沿轨迹切线的证明：</strong>当 $\\Delta t \\to 0$ 时，$\\Delta \\mathbf{r}$ 趋于元位移 $d\\mathbf{r}$。")+
   p("元位移是轨迹上无限相邻两点间的弦，在极限下弦与弧重合，方向与轨迹切线一致；其大小趋于弧长微元：")+
   fml("\\left|\\frac{d\\mathbf{r}}{dt}\\right| = \\lim_{\\Delta t\\to 0}\\frac{|\\Delta \\mathbf{r}|}{\\Delta t} = \\lim_{\\Delta t \\to 0}\\frac{ds}{\\Delta t} = \\frac{ds}{dt}")+
   p("因此瞬时速度的方向沿轨迹切线并指向运动前方，大小等于路程对时间的导数。"))+
   exa(p("<strong>例：</strong>质点做半径 $R$ 的匀速圆周运动，$\\mathbf{v}$ 的大小恒为 $R\\omega$，方向不断改变且始终沿切线，故平均速度与瞬时速度方向一般不同。"))
 )},
{"id":"c1s4-2","name":"速率与平均速率","tags":["def","der","note"],"brief":"速率是速度大小，平均速率一般大于平均速度的大小。",
 "body": wrap(
   defn("速率与平均速率",p("<strong>速率</strong>是瞬时速度的大小，为标量：")+
   fml("v = |\\mathbf{v}| = \\frac{ds}{dt}")+
   p("<strong>平均速率</strong>定义为路程与时间之比：")+
   fml("\\bar{v}_{s} = \\frac{s}{\\Delta t}"))+
   der(p("<strong>二者关系的推导：</strong>由上一节 $|\\Delta \\mathbf{r}| \\le s$，两边同除以 $\\Delta t$：")+
   fml("\\frac{|\\Delta \\mathbf{r}|}{\\Delta t} \\le \\frac{s}{\\Delta t} \\implies |\\bar{\\mathbf{v}}| \\le \\bar{v}_{s}")+
   p("取极限 $\\Delta t \\to 0$ 时等号成立，故瞬时速率恰等于瞬时速度的大小 $v=\\left|\\dfrac{d\\mathbf{r}}{dt}\\right|=\\dfrac{ds}{dt}$；但平均速率一般严格大于平均速度的大小。"))+
   exa(p("<strong>例：</strong>汽车以 $v = 10\\,\\text{m/s}$ 沿直线往返，去程与回程用时相同，全程位移为零，故平均速度大小 $|\\bar{\\mathbf{v}}| = 0$，而平均速率 $\\bar{v}_{s} = 10\\,\\text{m/s}$。"))+
   note(p("<strong>注意：</strong>匀速直线运动中 $|\\bar{\\mathbf{v}}| = \\bar{v}_{s}$；往返运动或闭合路径（如绕行一周回到原点）则 $\\bar{\\mathbf{v}} = \\mathbf{0}$，而 $\\bar{v}_{s} \\ne 0$。"))
 )},
]},
# ---- 1.5 加速度 ----
{
"name": "1.5 加速度",
"color": "#0284c7",
"desc": "平均加速度与瞬时加速度，以及加速度的切向与法向分解",
"items": [
{"id":"c1s5-1","name":"平均加速度与瞬时加速度","tags":["def","der","exa"],"brief":"加速度为速度对时间的变化率，方向未必沿速度方向。",
 "body": wrap(
   defn("平均加速度与瞬时加速度",p("<strong>平均加速度</strong>为速度增量与时间之比：")+
   fml("\\bar{\\mathbf{a}} = \\frac{\\Delta \\mathbf{v}}{\\Delta t}")+
   p("<strong>瞬时加速度</strong>为 $\\Delta t \\to 0$ 的极限：")+
   fml("\\mathbf{a} = \\lim_{\\Delta t \\to 0} \\frac{\\Delta \\mathbf{v}}{\\Delta t} = \\frac{d\\mathbf{v}}{dt} = \\frac{d^2 \\mathbf{r}}{dt^2}"))+
   der(p("<strong>加速度方向的分析：</strong>$\\Delta \\mathbf{v}$ 由平行四边形法则给出，$\\mathbf{a}$ 的方向是 $\\Delta \\mathbf{v}$ 的极限方向。")+
   p("将速度写成大小与方向之积 $\\mathbf{v} = v\\,\\boldsymbol{\\tau}$（$\\boldsymbol{\\tau}$ 为单位切矢量），按乘积法则求导：")+
   fml("\\mathbf{a} = \\frac{d}{dt}(v\\boldsymbol{\\tau}) = \\frac{dv}{dt}\\boldsymbol{\\tau} + v\\frac{d\\boldsymbol{\\tau}}{dt}")+
   p("第一项 $\\dfrac{dv}{dt}\\boldsymbol{\\tau}$ 沿速度方向，反映速度<strong>大小</strong>的变化；第二项反映速度<strong>方向</strong>的变化。可见一般运动的加速度并不沿速度方向。"))+
   exa(p("<strong>例：</strong>匀速圆周运动中 $\\dfrac{dv}{dt}=0$，加速度完全来自 $v\\dfrac{d\\boldsymbol{\\tau}}{dt}$，指向圆心；匀变速直线运动中 $\\dfrac{d\\boldsymbol{\\tau}}{dt}=0$，$\\mathbf{a}$ 与速度共线。"))
 )},
{"id":"c1s5-2","name":"加速度的切向与法向分解","tags":["thm","der","note"],"brief":"加速度可沿轨迹切向与法向分解为两个正交分量。",
 "body": wrap(
   thm("加速度的分解",p("一般曲线运动中，加速度可沿轨迹切向与法向分解为两个正交分量：")+
   fml("\\mathbf{a} = a_t \\boldsymbol{\\tau} + a_n \\mathbf{n},\\qquad a_t = \\frac{dv}{dt},\\qquad a_n = v\\frac{d\\boldsymbol{\\tau}}{dt}\\cdot\\mathbf{n}"))+
   der(p("<strong>推导：</strong>由 $\\mathbf{a} = \\dfrac{dv}{dt}\\boldsymbol{\\tau} + v\\dfrac{d\\boldsymbol{\\tau}}{dt}$，第一项已沿切向。")+
   p("第二项中 $\\boldsymbol{\\tau}$ 是单位矢量，由 $|\\boldsymbol{\\tau}| = 1$ 恒成立可证 $\\boldsymbol{\\tau}\\cdot\\dfrac{d\\boldsymbol{\\tau}}{dt} = 0$，即 $\\dfrac{d\\boldsymbol{\\tau}}{dt}$ 垂直于 $\\boldsymbol{\\tau}$，因而沿法向 $\\mathbf{n}$：")+
   fml("\\mathbf{a} = \\underbrace{\\frac{dv}{dt}}_{\\text{切向}}\\boldsymbol{\\tau} + \\underbrace{v\\frac{d\\boldsymbol{\\tau}}{dt}\\cdot\\mathbf{n}}_{\\text{法向}}\\mathbf{n}")+
   p("故切向分量 $a_t = \\dfrac{dv}{dt}$ 只改变速率，法向分量只改变速度方向。法向分量的显式表达式将在自然坐标系一节中给出。"))+
   exa(p("<strong>例（变速圆周运动）：</strong>汽车沿半径 $R$ 的弯道加速行驶，切向分量 $a_t = \\dfrac{dv}{dt}$ 使其越来越快，法向分量 $a_n$ 指向圆心维持转弯，总加速度斜指向轨迹凹侧。"))+
   note(p("总加速度大小 $a = \\sqrt{a_t^2 + a_n^2}$，与速度的夹角满足 $\\tan\\varphi = a_n / a_t$。加速度既不沿速度方向，也未必指向空间中的某个固定方向。"))
 )},
]},
# ---- 1.6 坐标系的运用与直角坐标系 ----
{
"name": "1.6 坐标系的运用与直角坐标系",
"color": "#0369a1",
"desc": "直角坐标系中位置、速度、加速度的分量表示与积分求解",
"items": [
{"id":"c1s6-1","name":"直角坐标系中的位置、速度与加速度","tags":["def","der","app"],"brief":"以常单位矢量分解，运动学矢量方程解耦为标量方程。",
 "body": wrap(
   defn("直角坐标系分解",p("取单位矢量 $\\mathbf{i}, \\mathbf{j}, \\mathbf{k}$ 为<strong>常矢量</strong>（大小与方向均不随时间变化），则位置矢量为：")+
   fml("\\mathbf{r}(t) = x(t)\\,\\mathbf{i} + y(t)\\,\\mathbf{j} + z(t)\\,\\mathbf{k}"))+
   der(p("<strong>速度分量：</strong>对 $\\mathbf{r}$ 求时间导数，因 $\\mathbf{i},\\mathbf{j},\\mathbf{k}$ 为常矢量可提到导数之外：")+
   fml("\\mathbf{v} = \\frac{d\\mathbf{r}}{dt} = \\frac{dx}{dt}\\mathbf{i} + \\frac{dy}{dt}\\mathbf{j} + \\frac{dz}{dt}\\mathbf{k} = v_x\\mathbf{i} + v_y\\mathbf{j} + v_z\\mathbf{k}")+
   p("<strong>加速度分量：</strong>对 $\\mathbf{v}$ 再求导一次：")+
   fml("\\mathbf{a} = \\frac{d\\mathbf{v}}{dt} = \\frac{d^2x}{dt^2}\\mathbf{i} + \\frac{d^2y}{dt^2}\\mathbf{j} + \\frac{d^2z}{dt^2}\\mathbf{k} = a_x\\mathbf{i} + a_y\\mathbf{j} + a_z\\mathbf{k}")+
   p("由于各分量方程相互独立，矢量运动学问题被<strong>解耦</strong>为三个独立的一维标量方程，可分别积分求解。"))+
   app(p("<strong>应用（抛体运动）：</strong>取 $a_x = 0$、$a_y = -g$，两分量分别积分得 $x = v_0\\cos\\theta\\,t$、$y = v_0\\sin\\theta\\,t - \\tfrac{1}{2}gt^2$，消去 $t$ 即得抛物线轨迹方程。"))
 )},
{"id":"c1s6-2","name":"由加速度积分求运动","tags":["thm","der","exa"],"brief":"给定加速度与初条件，通过两次积分唯一确定运动。",
 "body": wrap(
   thm("运动学第二类问题",p("已知加速度 $\\mathbf{a}(t)$ 及初位置 $\\mathbf{r}_0$、初速度 $\\mathbf{v}_0$，运动由两次积分唯一确定：")+
   fml("\\mathbf{v}(t) = \\mathbf{v}_0 + \\int_0^t \\mathbf{a}\\,dt,\\qquad \\mathbf{r}(t) = \\mathbf{r}_0 + \\int_0^t \\mathbf{v}(t')\\,dt'"))+
   der(p("<strong>推导：</strong>由 $\\dfrac{d\\mathbf{v}}{dt} = \\mathbf{a}$，在时间区间 $[0,t]$ 上积分：")+
   fml("\\int_{\\mathbf{v}_0}^{\\mathbf{v}} d\\mathbf{v} = \\int_0^t \\mathbf{a}\\,dt \\implies \\mathbf{v}(t) = \\mathbf{v}_0 + \\int_0^t \\mathbf{a}\\,dt")+
   p("再由 $\\dfrac{d\\mathbf{r}}{dt} = \\mathbf{v}$ 积分一次：")+
   fml("\\mathbf{r}(t) = \\mathbf{r}_0 + \\int_0^t \\mathbf{v}(t')\\,dt'")+
   p("初条件 $\\mathbf{r}_0, \\mathbf{v}_0$ 正是二阶微分方程的两个积分常数，故给定它们后运动被唯一确定。"))+
   exa(p("<strong>例：</strong>对 $\\mathbf{a} = a\\,\\mathbf{i}$ 的匀加速运动，两次积分得 $\\mathbf{v} = (v_0 + at)\\mathbf{i}$、$\\mathbf{r} = \\mathbf{r}_0 + \\left(v_0 t + \\tfrac{1}{2}at^2\\right)\\mathbf{i}$，与匀变速直线运动公式一致。"))
 )},
]},
# ---- 1.7 极坐标系 ----
{
"name": "1.7 极坐标系",
"color": "#38bdf8",
"desc": "平面极坐标中径向与横向单位矢量随时间变化，导出速度与加速度的完整分解",
"items": [
{"id":"c1s7-1","name":"平面极坐标系中的速度","tags":["def","der","exa"],"brief":"径向与横向单位矢量随时间旋转，速度含径向与横向两分量。",
 "body": wrap(
   defn("平面极坐标",p("以原点为极点，用径向距离 $r$ 与极角 $\\theta$ 描述位置。引入径向单位矢量 $\\mathbf{e}_r$（沿位矢向外）与横向单位矢量 $\\mathbf{e}_\\theta$（与 $\\mathbf{e}_r$ 正交，指向 $\\theta$ 增大的方向）：")+
   fml("\\mathbf{r} = r\\,\\mathbf{e}_r"))+
   der(p("<strong>第一步：单位矢量的时间导数。</strong>把单位矢量用直角坐标表示：$\\mathbf{e}_r = \\cos\\theta\\,\\mathbf{i} + \\sin\\theta\\,\\mathbf{j}$，$\\mathbf{e}_\\theta = -\\sin\\theta\\,\\mathbf{i} + \\cos\\theta\\,\\mathbf{j}$。对时间求导并利用 $\\dot{\\theta}$：")+
   fml("\\frac{d\\mathbf{e}_r}{dt} = \\dot{\\theta}\\,\\mathbf{e}_\\theta,\\qquad \\frac{d\\mathbf{e}_\\theta}{dt} = -\\dot{\\theta}\\,\\mathbf{e}_r")+
   p("<strong>第二步：对位矢求导。</strong>由 $\\mathbf{r} = r\\mathbf{e}_r$，按乘积法则并代入上式：")+
   fml("\\mathbf{v} = \\frac{d\\mathbf{r}}{dt} = \\dot{r}\\,\\mathbf{e}_r + r\\frac{d\\mathbf{e}_r}{dt} = \\dot{r}\\,\\mathbf{e}_r + r\\dot{\\theta}\\,\\mathbf{e}_\\theta")+
   p("故速度的径向分量 $v_r = \\dot{r}$，横向分量 $v_\\theta = r\\dot{\\theta}$。"))+
   exa(p("<strong>例（圆周运动）：</strong>$r = R$ 恒定，$\\dot{r} = 0$，故 $\\mathbf{v} = R\\dot{\\theta}\\,\\mathbf{e}_\\theta = R\\omega\\,\\mathbf{e}_\\theta$，方向沿横向、大小 $R\\omega$，与自然坐标结果一致。"))
 )},
{"id":"c1s7-2","name":"平面极坐标系中的加速度","tags":["thm","der","app"],"brief":"加速度含径向与横向分量，横向含科里奥利型耦合项。",
 "body": wrap(
   thm("极坐标加速度",p("在平面极坐标中，加速度分解为径向与横向两个分量：")+
   fml("\\mathbf{a} = \\left(\\ddot{r} - r\\dot{\\theta}^2\\right)\\mathbf{e}_r + \\left(r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta}\\right)\\mathbf{e}_\\theta"))+
   der(p("<strong>推导：</strong>对 $\\mathbf{v} = \\dot{r}\\mathbf{e}_r + r\\dot{\\theta}\\mathbf{e}_\\theta$ 再求时间导数，逐项微分。")+
   p("第一项 $\\dfrac{d}{dt}(\\dot{r}\\mathbf{e}_r) = \\ddot{r}\\mathbf{e}_r + \\dot{r}\\dfrac{d\\mathbf{e}_r}{dt} = \\ddot{r}\\mathbf{e}_r + \\dot{r}\\dot{\\theta}\\mathbf{e}_\\theta$。")+
   p("第二项按乘积法则：$\\dfrac{d}{dt}(r\\dot{\\theta}\\mathbf{e}_\\theta) = \\dot{r}\\dot{\\theta}\\mathbf{e}_\\theta + r\\ddot{\\theta}\\mathbf{e}_\\theta + r\\dot{\\theta}\\dfrac{d\\mathbf{e}_\\theta}{dt}$，代入 $\\dfrac{d\\mathbf{e}_\\theta}{dt} = -\\dot{\\theta}\\mathbf{e}_r$ 得：")+
   fml("\\frac{d}{dt}(r\\dot{\\theta}\\mathbf{e}_\\theta) = \\dot{r}\\dot{\\theta}\\mathbf{e}_\\theta + r\\ddot{\\theta}\\mathbf{e}_\\theta - r\\dot{\\theta}^2\\mathbf{e}_r")+
   p("合并 $\\mathbf{e}_r$ 与 $\\mathbf{e}_\\theta$ 分量：")+
   fml("a_r = \\ddot{r} - r\\dot{\\theta}^2,\\qquad a_\\theta = r\\ddot{\\theta} + 2\\dot{r}\\dot{\\theta}")+
   p("其中 $-r\\dot{\\theta}^2$ 为向心项，$2\\dot{r}\\dot{\\theta}$ 为科里奥利型耦合项。"))+
   app(p("<strong>应用（匀速圆周运动）：</strong>$r = R$、$\\dot{r} = 0$、$\\dot{\\theta} = \\omega$ 恒定，故 $a_r = -R\\omega^2$、$a_\\theta = 0$，即加速度指向圆心、大小为 $R\\omega^2 = v^2/R$。"))
 )},
]},
# ---- 1.8 自然坐标系 ----
{
"name": "1.8 自然坐标系",
"color": "#60a5fa",
"desc": "沿轨迹建立切向与法向单位矢量，严格导出 a_t=dv/dt 与 a_n=v²/ρ",
"items": [
{"id":"c1s8-1","name":"自然坐标系与切向加速度","tags":["def","der","note"],"brief":"以弧长参数化轨迹，切向加速度等于速率的变化率。",
 "body": wrap(
   defn("自然坐标系",p("以质点在轨迹上的位置为原点，沿运动方向取切向单位矢量 $\\boldsymbol{\\tau}$，指向轨迹凹侧取法向单位矢量 $\\mathbf{n}$，二者正交。以弧长 $s$ 作为位形参数：")+
   fml("\\mathbf{v} = v\\,\\boldsymbol{\\tau},\\qquad v = \\frac{ds}{dt}"))+
   der(p("<strong>切向加速度的推导：</strong>对 $\\mathbf{v} = v\\boldsymbol{\\tau}$ 求导得 $\\mathbf{a} = \\dfrac{dv}{dt}\\boldsymbol{\\tau} + v\\dfrac{d\\boldsymbol{\\tau}}{dt}$。")+
   p("将 $\\mathbf{a}$ 沿切向 $\\boldsymbol{\\tau}$ 投影，因 $\\dfrac{d\\boldsymbol{\\tau}}{dt}\\perp\\boldsymbol{\\tau}$（单位矢量的导数与其自身垂直），其切向分量为零：")+
   fml("a_t = \\mathbf{a}\\cdot\\boldsymbol{\\tau} = \\frac{dv}{dt} = \\frac{dv}{ds}\\cdot\\frac{ds}{dt} = \\frac{d^2 s}{dt^2}")+
   p("即切向加速度等于速率对时间的导数：$a_t>0$ 时速率增大，$a_t<0$ 时速率减小。"))+
   exa(p("<strong>例：</strong>质点沿曲线运动，速率 $v = 2t\\,\\text{m/s}$，则 $a_t = \\dfrac{dv}{dt} = 2\\,\\text{m/s}^2$，方向恒沿轨迹切向，其数值与轨迹的弯曲程度无关。"))+
   note(p("自然坐标系的分量方向随质点位置不断改变，故其单位矢量对时间的导数不为零；这正是法向加速度的来源，也是它区别于直角坐标系的根本特点。"))
 )},
{"id":"c1s8-2","name":"法向加速度与曲率半径","tags":["thm","der","exa"],"brief":"由切矢量转向的几何关系推出 a_n=v²/ρ，并给出曲率半径公式。",
 "body": wrap(
   thm("法向加速度",p("曲线运动中法向加速度的大小为")+
   fml("a_n = \\frac{v^2}{\\rho}")+
   p("方向指向曲率中心，其中 $\\rho$ 为轨迹在该点的曲率半径。"))+
   der(p("<strong>第一步：切矢量增量与曲率。</strong>$\\boldsymbol{\\tau}$ 为单位矢量，质点沿轨迹走过弧长 $ds$ 后切向转过角 $d\\varphi$，由几何关系 $|d\\boldsymbol{\\tau}| = d\\varphi$，且 $d\\boldsymbol{\\tau}$ 的方向沿法向 $\\mathbf{n}$：")+
   fml("\\frac{d\\boldsymbol{\\tau}}{ds} = \\frac{d\\varphi}{ds}\\,\\mathbf{n} = \\frac{1}{\\rho}\\,\\mathbf{n}")+
   p("其中曲率 $\\kappa = \\dfrac{d\\varphi}{ds} = \\dfrac{1}{\\rho}$，$\\rho$ 即曲率半径。")+
   p("<strong>第二步：化为对时间的导数。</strong>由链式法则 $\\dfrac{d\\boldsymbol{\\tau}}{dt} = \\dfrac{d\\boldsymbol{\\tau}}{ds}\\dfrac{ds}{dt}$：")+
   fml("\\frac{d\\boldsymbol{\\tau}}{dt} = \\frac{1}{\\rho}\\,\\mathbf{n}\\cdot v = \\frac{v}{\\rho}\\,\\mathbf{n}")+
   p("<strong>第三步：代回加速度表达式。</strong>")+
   fml("\\mathbf{a} = \\frac{dv}{dt}\\boldsymbol{\\tau} + v\\frac{d\\boldsymbol{\\tau}}{dt} = \\frac{dv}{dt}\\boldsymbol{\\tau} + \\frac{v^2}{\\rho}\\mathbf{n}")+
   p("故 $a_n = \\dfrac{v^2}{\\rho}$，方向指向曲率中心（轨迹凹侧）。"))+
   exa(p("<strong>平面曲线 $y=f(x)$ 的曲率半径：</strong>")+
   fml("\\rho = \\frac{\\left[1+(y')^2\\right]^{3/2}}{|y''|}")+
   p("例如抛物线顶点处 $y'=0$，$\\rho = 1/|y''|$；圆周上任一点带入该式恒给出 $\\rho = R$，与 $a_n = v^2/R$ 自洽。"))
 )},
]},
# ---- 1.9 相对运动与伽利略变换 ----
{
"name": "1.9 相对运动与伽利略变换",
"color": "#1e40af",
"desc": "平动参考系间的位矢、速度、加速度变换与伽利略不变性",
"items": [
{"id":"c1s9-1","name":"伽利略变换与相对速度","tags":["thm","der","exa"],"brief":"两平动参考系间位矢与速度的矢量合成关系。",
 "body": wrap(
   thm("伽利略变换",p("设参考系 $S'$ 相对 $S$ 以速度 $\\mathbf{u}$ 平动，且 $t=0$ 时两系原点重合，则同一质点在两系中的位矢与速度满足：")+
   fml("\\mathbf{r} = \\mathbf{r}' + \\mathbf{u} t,\\qquad \\mathbf{v} = \\mathbf{v}' + \\mathbf{u}"))+
   der(p("<strong>速度关系的推导：</strong>对位矢关系 $\\mathbf{r} = \\mathbf{r}' + \\mathbf{u}t$ 求时间导数。")+
   p("由于两系仅相对平动，$\\mathbf{u}$ 为常矢量，故 $\\dfrac{d(\\mathbf{u}t)}{dt} = \\mathbf{u}$：")+
   fml("\\frac{d\\mathbf{r}}{dt} = \\frac{d\\mathbf{r}'}{dt} + \\mathbf{u} \\implies \\mathbf{v} = \\mathbf{v}' + \\mathbf{u}")+
   p("即<strong>绝对速度</strong> $\\mathbf{v}$ 等于<strong>相对速度</strong> $\\mathbf{v}'$ 与<strong>牵连速度</strong> $\\mathbf{u}$ 的矢量和。"))+
   exa(p("<strong>例（雨中行车）：</strong>雨相对地面竖直下落，速度为 $\\mathbf{v}'$，车以 $\\mathbf{u}$ 前进。车上观测到的雨速 $\\mathbf{v} = \\mathbf{v}' + \\mathbf{u}$ 偏离竖直方向，其倾角满足 $\\tan\\alpha = u / v'$，这就是行车时雨看起来斜向扑来的原因。"))
 )},
{"id":"c1s9-2","name":"相对加速度与伽利略不变性","tags":["thm","der","note"],"brief":"平动参考系间加速度相同，牛顿定律在惯性系中形式不变。",
 "body": wrap(
   thm("加速度变换",p("若 $S'$ 相对 $S$ 以恒定速度 $\\mathbf{u}$ 平动，则质点在两系中的加速度相等：")+
   fml("\\mathbf{a} = \\mathbf{a}'"))+
   der(p("<strong>推导：</strong>对速度关系 $\\mathbf{v} = \\mathbf{v}' + \\mathbf{u}$ 再求一次时间导数。")+
   p("因 $\\mathbf{u}$ 恒定，$\\dfrac{d\\mathbf{u}}{dt} = \\mathbf{0}$，于是：")+
   fml("\\mathbf{a} = \\frac{d\\mathbf{v}}{dt} = \\frac{d\\mathbf{v}'}{dt} + \\frac{d\\mathbf{u}}{dt} = \\mathbf{a}' + \\mathbf{0} = \\mathbf{a}'")+
   p("即加速度在伽利略变换下<strong>不变</strong>。由于力与质量也不随惯性系改变，$\\mathbf{F} = m\\mathbf{a}$ 的形式在所有惯性系中相同，这是经典力学相对性原理的基础。"))+
   exa(p("<strong>例：</strong>在匀速行驶的车厢内释放小球，车内与地面两系测得小球加速度均为竖直向下的 $\\mathbf{g}$，即都看到自由落体，这是所有惯性系力学规律相同的直接体现。"))+
   note(p("若 $S'$ 相对 $S$ 存在加速度 $\\mathbf{a}_0$，则 $\\mathbf{a} = \\mathbf{a}' + \\mathbf{a}_0$，两系观测的加速度不同，$S'$ 为非惯性系，牛顿定律须引入惯性力修正（见第二章）。此外伽利略变换仅适用于 $v \\ll c$ 的低速情形，高速时须改用洛伦兹变换。"))
 )},
]},
]
ch2_sections = [
# ---- 2.1 惯性定律与惯性参考系 ----
{
"name": "2.1 惯性定律与惯性参考系",
"color": "#7c3aed",
"desc": "从伽利略理想实验到牛顿第一定律，说明惯性的物理内涵并界定惯性参考系。",
"items": [
{"id":"c2s1-1","name":"惯性定律（牛顿第一定律）","tags":["thm","der"],"brief":"不受外力时物体保持静止或匀速直线运动，即一切物体都具有惯性。",
 "fig":"trajectory","figCap":"无外力作用时质点做匀速直线运动",
 "body": wrap(
   thm("牛顿第一定律（惯性定律）",p("任何物体都保持静止或沿一条直线做匀速运动的状态，直到其他物体的作用迫使它改变这种状态为止。其内容可概括为：物体不受外力（或所受合外力为零）时 $\\vec{a}=0$，速度保持不变。")+
   p("定律揭示了两层含义：其一，一切物体都具有保持原有运动状态不变的属性，这种属性称为<strong>惯性</strong>；其二，力是<em>改变</em>物体运动状态（产生加速度）的原因，而不是<em>维持</em>运动的原因。"))+
   der(p("<strong>第一步：</strong>合外力为零时加速度为零，由加速度的定义")+
   fml("\\vec{a}=\\frac{d\\vec{v}}{dt}=\\vec{0}")+
   p("<strong>第二步：</strong>对时间积分一次，得到速度增量为零，故速度是常矢量：")+
   fml("\\vec{v}(t)-\\vec{v}(0)=\\int_0^t \\vec{a}\\,dt=\\vec{0}\\;\\Longrightarrow\\;\\vec{v}(t)=\\vec{v}(0)=\\text{常矢量}")+
   p("<strong>第三步：</strong>把常速度再积分一次，得到位置随时间线性变化：")+
   fml("\\vec{r}(t)=\\vec{r}(0)+\\vec{v}(0)\\,t")+
   p("位置矢量随时间线性变化即匀速直线运动；若 $\\vec{v}(0)=\\vec{0}$，则质点保持静止。可见惯性定律与加速度为零时的运动方程完全自洽。"))+
   app(p("<strong>应用：</strong>汽车突然刹车时乘客身体前倾，是因为乘客仍保持原来的运动状态；安全带正是通过外力强制改变乘客运动状态，从而减小伤害。"))+
   note(p("惯性定律不能由其他定律推出，它是牛顿力学的逻辑起点。其实验基础是伽利略斜面理想实验：小球从斜面滚下再滚上另一斜面时总回到近似相同的高度，把第二个斜面逐渐放平，小球将永远运动下去。"))
 )},
{"id":"c2s1-2","name":"惯性参考系","tags":["def","der"],"brief":"惯性定律成立的参考系；一切相对惯性系做匀速平动的参考系都是惯性系。",
 "body": wrap(
   defn("惯性参考系",p("<strong>惯性参考系</strong>是指惯性定律（牛顿第一定律）在其内部成立的参考系。在惯性系中，不受外力的物体保持静止或匀速直线运动，并且可以找到使 $\\vec{F}=m\\vec{a}$ 普遍成立的描述方式。")+
   p("相对某一惯性系静止或做匀速直线平动的参考系也是惯性系；相对惯性系做加速运动的参考系称为<strong>非惯性系</strong>。"))+
   der(p("<strong>命题：</strong>相对惯性系做匀速平动的参考系仍是惯性系。设 $S$ 为惯性系，$S'$ 相对 $S$ 以恒定速度 $\\vec{u}$ 运动，两系的伽利略变换为")+
   fml("\\vec{r}'=\\vec{r}-\\vec{u}\\,t,\\qquad t'=t")+
   p("对时间求一阶导数，得到速度变换关系：")+
   fml("\\vec{v}'=\\frac{d\\vec{r}'}{dt}=\\vec{v}-\\vec{u}")+
   p("再求一阶导数。由于 $\\vec{u}$ 为常矢量，$\\dfrac{d\\vec{u}}{dt}=\\vec{0}$，故两系中加速度完全相同：")+
   fml("\\vec{a}'=\\frac{d\\vec{v}'}{dt}=\\frac{d\\vec{v}}{dt}=\\vec{a}")+
   p("于是若在 $S$ 中某质点不受外力即 $\\vec{a}=\\vec{0}$，则在 $S'$ 中同样有 $\\vec{a}'=\\vec{0}$，惯性定律在 $S'$ 中也成立，故 $S'$ 也是惯性系。"))+
   exa(p("<strong>例：</strong>相对地面做匀速直线运动的火车、匀速航行的轮船、匀速飞行的飞机，都可当作惯性系处理；而正在加速、减速或转弯的车辆则是非惯性系。"))+
   note(p("地球因自转和绕日公转严格而言不是惯性系，但在一般工程与实验室问题中，自转与公转引起的加速度远小于可观测精度，可近似当作惯性系。太阳参考系比地球参考系更接近理想惯性系。"))
 )},
]},
# ---- 2.2 力与加速度·惯性质量·牛顿第二定律 ----
{
"name": "2.2 力与加速度·惯性质量·牛顿第二定律",
"color": "#6d28d9",
"desc": "力的定义、量度与矢量性，惯性质量的意义，以及牛顿第二定律的矢量形式与普遍形式。",
"items": [
{"id":"c2s2-1","name":"力·力的量度·力的矢量性","tags":["def","der"],"brief":"力是物体间的相互作用，是改变运动状态的原因，为矢量，可由测力计或加速度量度。",
 "fig":"fbd","figCap":"质点的自由体受力分析：多个力合成后产生加速度",
 "body": wrap(
   defn("力",p("<strong>力</strong>是物体与物体之间的相互作用，其效果是使受力物体产生加速度或发生形变。力是矢量，具有大小、方向和作用点三个要素。力的国际单位是牛顿，$1\\,\\text{N}=1\\,\\text{kg}\\cdot\\text{m/s}^2$。")+
   p("力的两种量度方式：一是<strong>静力效应</strong>，用弹簧测力计等依据形变（胡克定律）直接测量；二是<strong>动力效应</strong>，通过它使标准质量产生的加速度来量度。"))+
   der(p("<strong>力的矢量性（独立作用原理的矢量合成）：</strong>实验表明，多个力同时作用于一个质点时，其效果等于各力单独作用效果的矢量叠加。设第 $i$ 个力单独作用时产生加速度 $\\vec{a}_i$，则合力 $\\vec{F}=\\sum_i\\vec{F}_i$ 产生的加速度满足")+
   fml("\\vec{a}=\\sum_i \\vec{a}_i=\\sum_i \\frac{\\vec{F}_i}{m}=\\frac{1}{m}\\sum_i\\vec{F}_i=\\frac{\\vec{F}}{m}")+
   p("这说明力必须按矢量（平行四边形）法则合成，合力产生的是一个加速度，而不是各分力各自维持一种运动。合力的矢量表达式为")+
   fml("\\vec{F}=\\vec{F}_1+\\vec{F}_2+\\cdots+\\vec{F}_n")+
   p("由此得到力的独立作用原理：各分力对加速度的贡献相互独立、可矢量相加。"))+
   exa(p("<strong>例：</strong>一质点受两个互相垂直的力 $F_1=3\\,\\text{N}$、$F_2=4\\,\\text{N}$ 作用，合力大小 $F=\\sqrt{3^2+4^2}=5\\,\\text{N}$，方向与 $F_1$ 成 $\\arctan(4/3)\\approx 53^\\circ$。若质点质量 $m=2\\,\\text{kg}$，则加速度 $a=F/m=2.5\\,\\text{m/s}^2$，方向沿合力方向。"))
 )},
{"id":"c2s2-2","name":"惯性质量与牛顿第二定律","tags":["def","thm","der"],"brief":"惯性质量是惯性的量度；牛顿第二定律 F=ma，普遍形式为 F=dp/dt。",
 "body": wrap(
   defn("惯性质量",p("物体保持原有运动状态不变的性质称为<strong>惯性</strong>，其量度称为<strong>惯性质量</strong> $m$。在相同外力作用下，惯性质量大的物体加速度小，即 $a\\propto 1/m$，故质量是物体惯性大小的量度。")+
   p("惯性质量可用两物体相互作用时的加速度之比来定义：$m_1/m_2=|\\vec{a}_2|/|\\vec{a}_1|$。"))+
   thm("牛顿第二定律",p("物体动量的时间变化率等于它所受的合外力，方向沿合外力方向：")+
   fml("\\vec{F}=\\frac{d\\vec{p}}{dt}=\\frac{d(m\\vec{v})}{dt}")+
   p("当质量 $m$ 为常量时，简化为常见的矢量形式：")+
   fml("\\vec{F}=m\\vec{a}")+
   p("它是矢量方程，可沿任一方向投影为标量方程 $F_x=ma_x$、$F_y=ma_y$、$F_z=ma_z$。"))+
   der(p("<strong>第一步（用相互作用定义质量）：</strong>设两质点 $m_1$、$m_2$ 在光滑水平面上相互作用，除彼此作用力外不受其他外力。实验发现二者加速度方向相反，且在任意实验条件下加速度大小之比为恒定常数，记")+
   fml("\\frac{a_2}{a_1}=\\frac{m_1}{m_2}=\\mu_{12}")+
   p("取 $m_2$ 为单位质量（标准千克），即可由加速度之比测定 $m_1$，这给出了惯性质量的定量定义。")+
   p("<strong>第二步（由动量变化率化简）：</strong>把力定义为动量变化率 $\\vec{F}=\\dfrac{d\\vec{p}}{dt}$。质量不变时，$\\vec{p}=m\\vec{v}$，由乘积求导法则")+
   fml("\\vec{F}=\\frac{d(m\\vec{v})}{dt}=m\\frac{d\\vec{v}}{dt}+\\vec{v}\\frac{dm}{dt}=m\\vec{a}")+
   p("（其中 $\\dfrac{dm}{dt}=0$）。故质量不变时得到 $\\vec{F}=m\\vec{a}$，若质量可变（变质量系统、相对论）则应保留普遍形式 $\\vec{F}=\\dfrac{d\\vec{p}}{dt}$。"))+
   exa(p("<strong>例：</strong>质量 $m=1\\,\\text{kg}$ 的物体在水平方向受 $F=6\\,\\text{N}$ 的合力，则 $a=F/m=6\\,\\text{m/s}^2$。若改用同样的力作用于 $m=3\\,\\text{kg}$ 的物体，则 $a=2\\,\\text{m/s}^2$，恰为前者的三分之一，体现了质量越大惯性越大的特点。"))+
   note(p("在相对论中 $\\vec{p}=\\gamma m_0\\vec{v}$，动量形式 $\\vec{F}=\\dfrac{d\\vec{p}}{dt}$ 仍然成立，而 $\\vec{F}=m\\vec{a}$ 不再普遍成立，因此普遍形式比 $\\vec{F}=m\\vec{a}$ 更为基本。"))
 )},
]},
# ---- 2.3 力学中常见的力与作用力反作用力 ----
{
"name": "2.3 力学中常见的力与作用力反作用力",
"color": "#8b5cf6",
"desc": "万有引力与重力、弹性力、接触作用力（含摩擦力概述），以及作用与反作用定律。",
"items": [
{"id":"c2s3-1","name":"万有引力与重力","tags":["def","der"],"brief":"任意两质点间的引力遵循平方反比律；地球表面附近重力 G=mg。",
 "body": wrap(
   defn("万有引力",p("任何两个质点之间都存在相互吸引的力，称为<strong>万有引力</strong>，其大小为")+
   fml("F=G\\frac{m_1 m_2}{r^2}")+
   p("其中 $G\\approx 6.67\\times10^{-11}\\,\\text{N}\\cdot\\text{m}^2/\\text{kg}^2$ 为引力常量，$r$ 为两质点间距离，方向沿两质点的连线。"))+
   defn("重力",p("地球表面附近的物体所受地球引力（近似）称为<strong>重力</strong>，$\\vec{G}=m\\vec{g}$，方向竖直向下，$g$ 为重力加速度。"))+
   der(p("<strong>第一步：</strong>设地球质量 $M$、半径 $R$，地面附近质量为 $m$ 的物体所受地球引力由万有引力定律给出：")+
   fml("F=G\\frac{Mm}{R^2}")+
   p("<strong>第二步：</strong>把该引力等同于重力 $F=mg$，两边约去 $m$：")+
   fml("mg=G\\frac{Mm}{R^2}\\;\\Longrightarrow\\;g=\\frac{GM}{R^2}")+
   p("可见 $g$ 与物体质量无关，只由地球质量与半径决定。")+
   p("<strong>第三步（数值代入）：</strong>取 $M\\approx 5.97\\times10^{24}\\,\\text{kg}$、$R\\approx 6.37\\times10^{6}\\,\\text{m}$：")+
   fml("g=\\frac{6.67\\times10^{-11}\\times5.97\\times10^{24}}{(6.37\\times10^{6})^2}\\approx 9.8\\,\\text{m/s}^2")+
   p("在距地面高度 $h$ 处，$g(h)=\\dfrac{GM}{(R+h)^2}=g\\left(\\dfrac{R}{R+h}\\right)^2$，随高度增大而减小。"))+
   app(p("<strong>应用：</strong>由 $g=GM/R^2$ 可测量天体质量；人造卫星的环绕速度与周期也由万有引力提供向心力导出，例如近地卫星的环绕速度 $v=\\sqrt{GM/R}\\approx 7.9\\,\\text{km/s}$。"))+
   note(p("重力是地球引力的一个分力，另一分力提供物体随地球自转所需的向心力；但因自转影响很小，通常近似认为重力等于地球引力且方向指向地心。深度为 $d$ 处的引力加速度近似为 $g\\,(1-d/R)$。"))
 )},
{"id":"c2s3-2","name":"弹性力与接触作用力","tags":["def","der"],"brief":"弹性形变产生的恢复力，弹簧满足胡克定律 F=-kx；接触力含正压力与摩擦力。",
 "body": wrap(
   defn("弹性力",p("<strong>弹性力</strong>是发生弹性形变的物体企图恢复原状而对与它接触的物体施加的力。常见的弹性力包括弹簧的弹力、绳的拉力、支持面的正压力等，其方向总是垂直于接触面或沿着绳索。"))+
   defn("胡克定律",p("在弹性限度内，弹簧的弹力大小与形变量成正比，方向指向平衡位置：")+
   fml("\\vec{F}=-k\\vec{x}")+
   p("式中 $k$ 为劲度系数（单位 $\\text{N/m}$），$\\vec{x}$ 为相对平衡位置的位移，负号表示弹力方向与位移相反，即恢复力。"))+
   defn("接触作用力",p("相互接触的物体之间的相互作用力统称<strong>接触力</strong>，包括垂直于接触面的正压力 $N$ 与沿接触面切向的<strong>摩擦力</strong>。摩擦力又分为静摩擦力与滑动摩擦力，其详细规律见 2.6 节。"))+
   der(p("<strong>推导弹簧的等效劲度系数。</strong>设有劲度系数为 $k_1$、$k_2$ 的两根轻弹簧。<br><strong>串联：</strong>两弹簧受力相同均为 $F$，形变量分别为 $x_1=F/k_1$、$x_2=F/k_2$，总形变 $x=x_1+x_2$，等效劲度系数 $k=F/x$ 满足")+
   fml("\\frac{1}{k}=\\frac{x}{F}=\\frac{1}{k_1}+\\frac{1}{k_2}\\;\\Longrightarrow\\;k=\\frac{k_1 k_2}{k_1+k_2}")+
   p("<strong>并联：</strong>两弹簧形变量相同均为 $x$，各受力 $F_1=k_1 x$、$F_2=k_2 x$，合力 $F=F_1+F_2=(k_1+k_2)x$，故")+
   fml("k=k_1+k_2")+
   p("这两式与电阻（电容）的串并联规律恰好相反，可用于分析组合弹簧的振动与静力学问题。"))+
   exa(p("<strong>例：</strong>一轻绳两端各系质量 $m_1$、$m_2$ 的物体跨过光滑定滑轮，绳中张力处处相等。绳的拉力即弹性力的一种，其大小由动力学方程而非简单形变决定。"))
 )},
{"id":"c2s3-3","name":"作用力与反作用力（牛顿第三定律）","tags":["thm","der"],"brief":"作用力与反作用力等大反向、作用在不同物体上；由此可导出动量守恒。",
 "body": wrap(
   thm("牛顿第三定律",p("两个物体之间的作用力 $\\vec{F}_{12}$ 与反作用力 $\\vec{F}_{21}$ 总是大小相等、方向相反，且沿同一条直线，分别作用在两个不同的物体上：")+
   fml("\\vec{F}_{12}=-\\vec{F}_{21}")+
   p("作用力与反作用力同时产生、同时消失，属于同一种性质的力，但分别作用于不同物体，因而不能相互抵消。"))+
   der(p("<strong>第一步：</strong>把相互作用的两质点视为一个系统，$\\vec{F}_{12}$ 是 $m_1$ 对 $m_2$ 的力，$\\vec{F}_{21}$ 是 $m_2$ 对 $m_1$ 的力。对两质点分别用牛顿第二定律：")+
   fml("\\frac{d\\vec{p}_1}{dt}=\\vec{F}_{21},\\qquad \\frac{d\\vec{p}_2}{dt}=\\vec{F}_{12}")+
   p("<strong>第二步：</strong>两式相加，右边由第三定律 $\\vec{F}_{12}+\\vec{F}_{21}=\\vec{0}$：")+
   fml("\\frac{d\\vec{p}_1}{dt}+\\frac{d\\vec{p}_2}{dt}=\\frac{d}{dt}(\\vec{p}_1+\\vec{p}_2)=\\vec{0}")+
   p("<strong>第三步：</strong>对时间积分，得系统总动量守恒：")+
   fml("\\vec{p}_1+\\vec{p}_2=\\text{常矢量}")+
   p("推广到由多个质点组成的系统，内力总是成对出现并相互抵消，只要系统所受合外力为零，总动量就守恒。"))+
   exa(p("<strong>例（反冲）：</strong>静止的炮车质量为 $M$，水平射出质量 $m$、速度为 $v$ 的炮弹，则炮车反冲速度 $V$ 由动量守恒 $mv+MV=0$ 得 $V=-mv/M$，方向与炮弹相反。"))
 )},
]},
# ---- 2.4 力的合成与分解·算法举例 ----
{
"name": "2.4 力的合成与分解·算法举例",
"color": "#a855f7",
"desc": "平行四边形法则、正交分解法则，以及力的合成与分解的典型算法与例题。",
"items": [
{"id":"c2s4-1","name":"力的合成：平行四边形法则","tags":["def","der"],"brief":"两个共点力用平行四边形法则求合力，合力大小由余弦定理给出。",
 "fig":"fbd","figCap":"两共点力 F1、F2 的平行四边形合成",
 "body": wrap(
   defn("力的合成与平行四边形法则",p("求几个力的合力称为<strong>力的合成</strong>。作用于同一点的两个力 $\\vec{F}_1$、$\\vec{F}_2$ 的合力，由以这两个力为邻边所作的平行四边形的对角线表示，这称为<strong>平行四边形法则</strong>。")+
   p("合力也可用三角形法则把两力首尾相接得到，且与相加次序无关：$\\vec{F}_1+\\vec{F}_2=\\vec{F}_2+\\vec{F}_1$。"))+
   der(p("<strong>第一步（正交分解）：</strong>设两力夹角为 $\\theta$。沿 $\\vec{F}_1$ 方向及其垂直方向分解，$\\vec{F}_2$ 的分量为")+
   fml("F_{2x}=F_2\\cos\\theta,\\qquad F_{2y}=F_2\\sin\\theta")+
   p("<strong>第二步（求分量）：</strong>故合力分量为 $F_x=F_1+F_2\\cos\\theta$、$F_y=F_2\\sin\\theta$，合力大小")+
   fml("F=\\sqrt{F_x^2+F_y^2}=\\sqrt{(F_1+F_2\\cos\\theta)^2+(F_2\\sin\\theta)^2}")+
   p("<strong>第三步（化简）：</strong>利用 $\\cos^2\\theta+\\sin^2\\theta=1$，得到与余弦定理一致的合力公式：")+
   fml("F=\\sqrt{F_1^2+F_2^2+2F_1F_2\\cos\\theta}")+
   p("合力与 $\\vec{F}_1$ 的夹角 $\\varphi$ 满足 $\\tan\\varphi=\\dfrac{F_2\\sin\\theta}{F_1+F_2\\cos\\theta}$。当 $\\theta=0$ 时 $F=F_1+F_2$（最大），当 $\\theta=180^\\circ$ 时 $F=|F_1-F_2|$（最小）。"))+
   exa(p("<strong>例：</strong>两小孩分别用 $F_1=50\\,\\text{N}$、$F_2=50\\,\\text{N}$ 沿夹角 $60^\\circ$ 方向拉一小车，则合力 $F=\\sqrt{50^2+50^2+2\\times50\\times50\\times\\cos60^\\circ}=50\\sqrt{3}\\approx 86.6\\,\\text{N}$，方向沿两力夹角的角平分线。"))
 )},
{"id":"c2s4-2","name":"力的分解与正交分解算法","tags":["def","der"],"brief":"把力按作用效果或选定坐标轴分解；正交分解是动力学问题的标准算法。",
 "body": wrap(
   defn("力的分解",p("由一个力求它的几个等效分力称为<strong>力的分解</strong>，它是合成的逆运算。若无附加条件，一个力可分解为无穷多对分力；通常按力的<strong>实际作用效果</strong>（沿运动方向与垂直方向）或按<strong>选定的两个互相垂直方向</strong>进行分解。"))+
   der(p("<strong>正交分解算法步骤：</strong>① 选取合适的直角坐标系，一般使某坐标轴与加速度方向共线，以简化方程；② 把每个力 $\\vec{F}_i$ 分解为 $x$、$y$ 分量；")+
   p("③ 分别沿两轴写出牛顿第二定律的分量方程：")+
   fml("\\sum_i F_{i,x}=m a_x,\\qquad \\sum_i F_{i,y}=m a_y")+
   p("空间问题再补充 $z$ 分量方程 $\\sum_i F_{i,z}=m a_z$。写分量方程时需规定各轴正方向，力与该轴方向一致取正、相反取负。")+
   p("④ 结合约束方程（如绳不可伸长、接触面法向不分离）联立求解未知量；⑤ 检验结果的量纲与极限情形。"))+
   exa(p("<strong>例（斜面正交分解）：</strong>倾角 $\\theta$ 的光滑斜面上放质量 $m$ 的物体，取 $x$ 轴沿斜面向下、$y$ 轴垂直斜面向上。重力分解为 $mg\\sin\\theta$（沿 $x$）与 $-mg\\cos\\theta$（沿 $y$）。由 $y$ 方向平衡得正压力 $N=mg\\cos\\theta$；由 $x$ 方向")+
   fml("mg\\sin\\theta=m a\\;\\Longrightarrow\\;a=g\\sin\\theta"))
 )},
]},
# ---- 2.5 质点动力学问题与约束运动 ----
{
"name": "2.5 质点动力学问题与约束运动",
"color": "#9333ea",
"desc": "用隔离法（自由体图）求解动力学问题的规范步骤，以及约束运动的约束方程。",
"items": [
{"id":"c2s5-1","name":"隔离法与动力学问题求解步骤","tags":["def","der"],"brief":"把研究对象单独隔离、画出全部受力，再列牛顿方程联立求解。",
 "fig":"inclined","figCap":"隔离体受力分析（自由体图）",
 "body": wrap(
   defn("隔离法",p("<strong>隔离法</strong>是把所研究的物体（或物体系中的某一物体）从周围环境中单独分离出来，只画出作用于它的一切外力，得到隔离体受力图（自由体图），再对每个隔离体应用牛顿第二定律的方法。研究物体系时，可以逐体隔离，也可以整体隔离。"))+
   der(p("<strong>动力学问题的规范求解步骤：</strong>① 明确研究对象，选定隔离体；② 画出全部外力（重力、弹力、摩擦力、绳张力等），不画它施于别的物体的力；③ 选定坐标系，常取加速度方向为一坐标轴；")+
   p("④ 逐个隔离体写出牛顿第二定律的分量方程；⑤ 补充约束方程（绳长不变、接触不分离、滑轮两侧张力关系等）；⑥ 联立解方程并讨论结果。")+
   p("设系统有 $k$ 个隔离体，隔离后一般得到 $k$ 个矢量方程：")+
   fml("\\vec{F}_1+\\sum \\vec{f}_1=m_1\\vec{a}_1,\\qquad \\vec{F}_2+\\sum \\vec{f}_2=m_2\\vec{a}_2")+
   p("其中 $\\vec{f}$ 为相互作用力（内力），它在一对隔离体中以等大反向的形式出现，正是牛顿第三定律的体现；配合约束方程即可确定全部未知量。"))+
   exa(p("<strong>例（阿特伍德机）：</strong>轻绳跨过光滑定滑轮，两端系质量 $m_1>m_2$ 的物体。分别隔离两物体，设 $m_1$ 向下、$m_2$ 向上加速，绳张力为 $T$，则")+
   fml("m_1 g-T=m_1 a,\\qquad T-m_2 g=m_2 a")+
   p("两式相加消去 $T$：")+
   fml("(m_1-m_2)g=(m_1+m_2)a\\;\\Longrightarrow\\;a=\\frac{m_1-m_2}{m_1+m_2}g,\\qquad T=\\frac{2m_1m_2}{m_1+m_2}g"))
 )},
{"id":"c2s5-2","name":"约束运动与约束方程","tags":["def","der"],"brief":"受几何或运动学限制的运动，其约束条件用约束方程表示，约束力是被动力。",
 "body": wrap(
   defn("约束与约束方程",p("限制物体运动（位置或速度）的几何或运动学条件称为<strong>约束</strong>，其数学表达式称为<strong>约束方程</strong>。实现约束的相互作用力称为<strong>约束力</strong>（如正压力、绳张力、轨道支持力），它是被动力，由主动力与运动状态共同决定，常需借助约束方程求出。"))+
   der(p("<strong>几种典型约束方程：</strong>")+
   p("① <strong>单斜面约束：</strong>质点沿倾角 $\\theta$ 的斜面运动，坐标满足")+
   fml("y=x\\tan\\theta\\quad\\text{或}\\quad x\\sin\\theta-y\\cos\\theta=0")+
   p("② <strong>不可伸长绳约束：</strong>绳两端沿绳方向的位置变化之和为零。对跨过定滑轮的绳，两段绳的伸长量满足 $\\Delta l_1+\\Delta l_2=0$，故两端加速度大小相等：")+
   fml("a_1=a_2")+
   p("③ <strong>接触面不分离约束：</strong>物体与支持面保持接触，法向相对加速度为零，正压力 $N\\ge 0$；当 $N=0$ 时物体即将脱离接触面。")+
   p("④ <strong>沿绳方向速度约束：</strong>绳不可伸长时，绳两端沿绳方向的速度分量相等，即两端绳长变化率之和为零。"))+
   exa(p("<strong>例（约束降维）：</strong>质量 $m$ 的小环套在光滑的竖直大圆环上，若圆环静止，小环只能沿圆环滑动，约束方程为 $x^2+y^2=R^2$。取切向与法向坐标后，法向由圆环支持力提供，切向由重力的切向分量决定运动，约束方程把二维问题降为一维问题求解。"))
 )},
]},
# ---- 2.6 摩擦力 ----
{
"name": "2.6 摩擦力",
"color": "#c084fc",
"desc": "干摩擦的静摩擦与滑动摩擦规律、湿摩擦（粘滞阻力）的特点及其运动分析。",
"items": [
{"id":"c2s6-1","name":"干摩擦：静摩擦与滑动摩擦","tags":["def","der"],"brief":"干摩擦满足 f≤μN 与 f=μN，最大静摩擦决定是否开始滑动。",
 "fig":"inclined","figCap":"斜面上的物体：重力分量与摩擦力的平衡",
 "body": wrap(
   defn("干摩擦",p("两个干燥固体表面接触且有相对运动或相对运动趋势时，接触面上产生的阻碍作用称为<strong>干摩擦</strong>，分为两种：<br><strong>静摩擦力</strong> $f_s$：物体有相对运动趋势但尚未滑动，其取值满足")+
   fml("0\\le f_s\\le f_{s\\max}=\\mu_s N")+
   p("方向与相对运动趋势方向相反，其大小由平衡条件确定。<br><strong>滑动摩擦力</strong> $f_k$：物体已相对滑动，大小为 $f_k=\\mu_k N$，方向与相对滑动方向相反，其大小近似与接触面积和相对速度无关。")+
   p("通常 $\\mu_s>\\mu_k$，即推动物体所需的最大静摩擦略大于滑动后的摩擦。"))+
   der(p("<strong>第一步（斜面受力分析）：</strong>物体置于倾角 $\\theta$ 的斜面上，受重力 $mg$、正压力 $N$ 与静摩擦力 $f_s$。垂直斜面方向平衡：")+
   fml("N=mg\\cos\\theta")+
   p("<strong>第二步（沿斜面平衡）：</strong>为避免下滑所需的静摩擦力为")+
   fml("f_s=mg\\sin\\theta")+
   p("<strong>第三步（应用静摩擦条件）：</strong>不滑动的条件 $f_s\\le \\mu_s N$ 给出")+
   fml("mg\\sin\\theta\\le \\mu_s mg\\cos\\theta\\;\\Longrightarrow\\;\\tan\\theta\\le \\mu_s")+
   p("故临界角 $\\theta_c=\\arctan\\mu_s$。当 $\\theta>\\theta_c$ 时物体开始下滑，此时滑动摩擦力 $f_k=\\mu_k mg\\cos\\theta$，沿斜面的加速度为")+
   fml("a=g(\\sin\\theta-\\mu_k\\cos\\theta)"))+
   app(p("<strong>应用：</strong>传送带靠静摩擦力带动物料，汽车靠轮胎与地面间的静摩擦力获得驱动力与制动力；刹车距离即由滑动摩擦力 $f_k=\\mu_k mg$ 决定的减速度 $a=\\mu_k g$ 计算。"))+
   note(p("静摩擦力的方向总是阻碍<strong>相对运动趋势</strong>而非运动本身，故它既可以是阻力也可以是动力。同一物体的静摩擦力大小可在 $[0,\\mu_s N]$ 内随外力连续变化。"))
 )},
{"id":"c2s6-2","name":"湿摩擦（粘滞阻力）及其特点","tags":["def","der"],"brief":"流体阻力与速度有关：f=-kv 或 -kv²，导致速度趋于终极速度。",
 "body": wrap(
   defn("湿摩擦（粘滞阻力）",p("物体在气体或液体中运动时，与流体介质相互作用而受到的阻碍力称为<strong>湿摩擦</strong>或<strong>粘滞阻力</strong>。其大小与物体相对流体的速度有关：低速时近似与速度成正比 $f=-kv$（斯托克斯阻力），较高速绕流时近似与速度平方成正比 $f=-kv^2$，方向始终与相对速度相反。"))+
   der(p("<strong>第一步（列方程）：</strong>物体在流体中竖直下落，受重力 $mg$ 与竖直向上的阻力 $f=kv^2$，由牛顿第二定律")+
   fml("mg-kv^2=m\\frac{dv}{dt}")+
   p("下落过程中 $v$ 增大、阻力增大、加速度减小。令终极速度满足 $v_T^2=mg/k$，则方程化为")+
   fml("\\frac{dv}{dt}=g\\left(1-\\frac{v^2}{v_T^2}\\right)")+
   p("<strong>第二步（分离变量积分）：</strong>")+
   fml("\\int_0^v\\frac{dv'}{1-(v'/v_T)^2}=\\int_0^t g\\,dt")+
   p("左侧积分为 $v_T\\operatorname{artanh}(v/v_T)$，故得速度随时间的变化：")+
   fml("v(t)=v_T\\tanh\\!\\left(\\frac{g\\,t}{v_T}\\right)")+
   p("<strong>第三步（取极限）：</strong>当 $t\\to\\infty$ 时 $v\\to v_T$，速度渐近趋于终极速度而不再增大。若阻力为线性形式 $f=kv$，同样可得 $v(t)=\\dfrac{mg}{k}\\left(1-e^{-kt/m}\\right)$，终极速度 $v_T=mg/k$。"))+
   app(p("<strong>应用：</strong>雨滴、跳伞者与沉降实验中的微粒在达到终极速度后做匀速运动。雨滴因 $v_T\\propto\\sqrt{mg/k}$，半径增大时终极速度增大，故大雨滴比小雨滴落得更快。"))+
   note(p("湿摩擦与干摩擦的关键区别：干摩擦力与速度无关且有最大静摩擦；湿摩擦力随速度变化、无静摩擦、速度为零时阻力为零。因此湿摩擦不能像干摩擦那样简单地取定值，而必须在运动方程中保留速度因子。"))
 )},
]},
# ---- 2.7 平动参考系与伽利略相对性原理 ----
{
"name": "2.7 平动参考系与伽利略相对性原理",
"color": "#a78bfa",
"desc": "伽利略变换与相对性原理，以及平动非惯性系中的平动惯性力 F_惯=-m a_0。",
"items": [
{"id":"c2s7-1","name":"伽利略相对性原理","tags":["thm","der"],"brief":"一切惯性系中力学规律形式相同，伽利略变换下加速度不变。",
 "body": wrap(
   thm("伽利略相对性原理",p("在所有惯性参考系中，力学定律具有相同的形式；也就是说，无法通过任何力学实验判断所在的惯性系是静止还是在做匀速直线运动。联系两个惯性系的坐标变换为<strong>伽利略变换</strong>：")+
   fml("\\vec{r}'=\\vec{r}-\\vec{u}t,\\qquad t'=t")+
   p("其中 $\\vec{u}$ 为两惯性系的相对速度。"))+
   der(p("<strong>第一步（速度变换）：</strong>对伽利略变换的位置式求一阶导数，得到")+
   fml("\\vec{v}'=\\frac{d\\vec{r}'}{dt}=\\vec{v}-\\vec{u}")+
   p("<strong>第二步（加速度变换）：</strong>再求导一次，因为 $\\vec{u}$ 恒定，$\\dfrac{d\\vec{u}}{dt}=\\vec{0}$，故")+
   fml("\\vec{a}'=\\frac{d\\vec{v}'}{dt}=\\frac{d\\vec{v}}{dt}=\\vec{a}")+
   p("<strong>第三步（形式不变性）：</strong>加速度在两惯性系中完全相同，而力只依赖于相互作用（相对位置与相对速度）也与参考系无关，于是 $\\vec{F}=m\\vec{a}$ 变为 $\\vec{F}=m\\vec{a}'$，形式不变。故一切惯性系中力学规律相同，不存在特殊的绝对静止参考系。"))+
   exa(p("<strong>例：</strong>在匀速直线飞行的飞机中抛下一物体，机舱内的观察者看到物体做竖直自由落体，与地面上静止电梯中的观察者看到的力学现象完全一致；二者所处的惯性系无法用力学实验区分。"))
 )},
{"id":"c2s7-2","name":"平动非惯性系与平动惯性力","tags":["def","thm","der"],"brief":"在加速平动的非惯性系中引入惯性力 F_惯=-m a_0 后，牛顿定律仍保持 F+F_惯=m a'。",
 "body": wrap(
   defn("平动非惯性系",p("相对惯性系做加速平动（平动加速度 $\\vec{a}_0$）的参考系称为<strong>平动非惯性系</strong>。在其中牛顿第二定律不能直接写成 $\\vec{F}=m\\vec{a}'$ 的形式，需要引入<strong>惯性力</strong>这一虚拟力加以修正。"))+
   thm("平动惯性力",p("在相对惯性系以加速度 $\\vec{a}_0$ 平动的非惯性系中，为使牛顿第二定律形式上成立，对每个质量为 $m$ 的质点附加惯性力：")+
   fml("\\vec{F}_{\\text{惯}}=-m\\vec{a}_0")+
   p("于是质点的动力学方程写作")+
   fml("\\vec{F}+\\vec{F}_{\\text{惯}}=m\\vec{a}'")+
   p("其中 $\\vec{F}$ 为真实力，$\\vec{a}'$ 为质点相对非惯性系的加速度。惯性力没有施力物体，不满足牛顿第三定律，是参考系加速的体现。"))+
   der(p("<strong>第一步（加速度合成）：</strong>设质点相对惯性系 $S$ 的加速度为 $\\vec{a}$，相对非惯性系 $S'$ 的加速度为 $\\vec{a}'$，两系间满足")+
   fml("\\vec{a}=\\vec{a}'+\\vec{a}_0")+
   p("<strong>第二步（代入惯性系牛顿方程）：</strong>在惯性系 $S$ 中 $\\vec{F}=m\\vec{a}$ 成立，把加速度合成式代入：")+
   fml("\\vec{F}=m(\\vec{a}'+\\vec{a}_0)=m\\vec{a}'+m\\vec{a}_0")+
   p("<strong>第三步（移项定义惯性力）：</strong>把 $-m\\vec{a}_0$ 记为惯性力 $\\vec{F}_{\\text{惯}}$：")+
   fml("\\vec{F}-m\\vec{a}_0=m\\vec{a}'\\;\\Longrightarrow\\;\\vec{F}+\\vec{F}_{\\text{惯}}=m\\vec{a}'")+
   p("这样在非惯性系中，只要把惯性力也算作一种力，牛顿第二定律在形式上重新成立。"))+
   app(p("<strong>应用（超重与失重）：</strong>在竖直加速的电梯中取向上为正，设电梯加速度大小为 $a$。物体受重力 $-mg$、支持力 $N$，以及惯性力 $-ma$。相对电梯静止时 $a'=0$：")+
   fml("N-mg-ma=0\\;\\Longrightarrow\\;N=m(g+a)")+
   p("加速度向上时 $N>mg$ 为<strong>超重</strong>；加速度向下时 $N=m(g-a)<mg$ 为<strong>失重</strong>；自由下落 $a=g$ 时 $N=0$，为完全失重。"))
 )},
]},
# ---- 2.8 转动参考系·科里奥利力 ----
{
"name": "2.8 转动参考系·科里奥利力",
"color": "#7e22ce",
"desc": "转动参考系中的离心惯性力、科里奥利加速度与科里奥利力，以及地球自转的力学效应。",
"items": [
{"id":"c2s8-1","name":"离心惯性力","tags":["def","der"],"brief":"以角速度 ω 转动的参考系中，质点受到沿径向向外的离心惯性力 mω²r。",
 "fig":"circular","figCap":"转动参考系中质点受到的离心惯性力",
 "body": wrap(
   defn("离心惯性力",p("在以角速度 $\\omega$ 匀速转动的参考系中，距转轴 $r$、质量为 $m$ 的静止质点，会额外感受到一个沿径向向外、大小为 $m\\omega^2 r$ 的惯性力，称为<strong>离心惯性力</strong>：")+
   fml("\\vec{F}_{\\text{cf}}=m\\omega^2 r\\,\\hat{r}")+
   p("它并非真实相互作用，而是参考系转动带来的效果，可使物体相对转动系有向外运动的趋势。"))+
   der(p("<strong>第一步：</strong>考虑一个在惯性系中以角速度 $\\omega$ 做匀速圆周运动、半径为 $r$ 的质点，惯性系中它受真实力提供向心力：")+
   fml("\\vec{F}=-m\\omega^2 r\\,\\hat{r}")+
   p("<strong>第二步：</strong>换到随质点一起转动的非惯性系中观察，质点在此系中保持静止，即 $\\vec{a}'=\\vec{0}$。要使牛顿第二定律在此系中成立，须补入一个惯性力：")+
   fml("\\vec{F}+\\vec{F}_{\\text{惯}}=m\\vec{a}'=\\vec{0}")+
   p("<strong>第三步：</strong>解出该惯性力")+
   fml("\\vec{F}_{\\text{惯}}=-\\vec{F}=m\\omega^2 r\\,\\hat{r}")+
   p("其方向沿半径向外、与向心力方向相反，大小 $m\\omega^2 r$，即离心惯性力。它随 $\\omega$ 和 $r$ 的增大而增大，是离心分离、离心机与旋转液体表面成抛物面等现象的动力学基础。"))+
   exa(p("<strong>例：</strong>离心机转子半径 $r=0.1\\,\\text{m}$，转速 $3000\\,\\text{r/min}$，则 $\\omega=2\\pi\\times3000/60\\approx 314\\,\\text{rad/s}$，质量 $m=1\\,\\text{g}$ 的微粒所受离心惯性力 $F=m\\omega^2 r\\approx 10^{-3}\\times314^2\\times0.1\\approx 9.9\\,\\text{N}$，约为其重力的上千倍，从而实现快速分离。"))
 )},
{"id":"c2s8-2","name":"科里奥利加速度与科里奥利力","tags":["def","thm","der"],"brief":"转动参考系中运动的质点多出 2ω×v' 的科里奥利加速度与相应的科里奥利力。",
 "body": wrap(
   defn("科里奥利力",p("在转动参考系中运动的质点，除离心惯性力外，还受到一个与相对速度 $\\vec{v}'$ 和转动角速度 $\\vec{\\omega}$ 都垂直的惯性力，称为<strong>科里奥利力</strong>：")+
   fml("\\vec{F}_{\\text{Cor}}=-2m\\vec{\\omega}\\times\\vec{v}'")+
   p("其中 $\\vec{\\omega}$ 为转动参考系相对惯性系的角速度矢量（方向由右手螺旋定则确定），$\\vec{v}'$ 为质点相对转动系的速度。"))+
   thm("科里奥利加速度",p("质点相对惯性系的加速度 $\\vec{a}$ 与相对转动系加速度 $\\vec{a}'$ 之间满足")+
   fml("\\vec{a}=\\vec{a}'+2\\vec{\\omega}\\times\\vec{v}'+\\vec{\\omega}\\times(\\vec{\\omega}\\times\\vec{r})")+
   p("式中 $2\\vec{\\omega}\\times\\vec{v}'$ 为<strong>科里奥利加速度</strong>，$\\vec{\\omega}\\times(\\vec{\\omega}\\times\\vec{r})=-\\omega^2\\vec{r}_{\\perp}$ 为向心加速度项，对应离心惯性力。"))+
   der(p("<strong>第一步（转动系求导公式）：</strong>任一矢量在惯性系中的时间导数与在转动系中的导数满足")+
   fml("\\left(\\frac{d\\vec{A}}{dt}\\right)_S=\\left(\\frac{d\\vec{A}}{dt}\\right)_{S'}+\\vec{\\omega}\\times\\vec{A}")+
   p("取 $\\vec{A}=\\vec{r}$，得速度关系：")+
   fml("\\vec{v}=\\vec{v}'+\\vec{\\omega}\\times\\vec{r}")+
   p("<strong>第二步（再对速度求导）：</strong>把同一变换作用于 $\\vec{v}$，并注意 $\\vec{v}'$ 是随系转动的矢量：")+
   fml("\\vec{a}=\\vec{a}'+2\\vec{\\omega}\\times\\vec{v}'+\\vec{\\omega}\\times(\\vec{\\omega}\\times\\vec{r})+\\frac{d\\vec{\\omega}}{dt}\\times\\vec{r}")+
   p("对匀速转动 $\\dfrac{d\\vec{\\omega}}{dt}=\\vec{0}$，得到含科里奥利项的加速度合成式。")+
   p("<strong>第三步（移项得惯性力）：</strong>代入惯性系的牛顿第二定律 $\\vec{F}=m\\vec{a}$，并把相对加速度项移到左边：")+
   fml("m\\vec{a}'=\\vec{F}-2m\\vec{\\omega}\\times\\vec{v}'+m\\omega^2\\vec{r}_{\\perp}")+
   p("右边后两项恰为科里奥利力与离心惯性力。科里奥利力垂直于 $\\vec{\\omega}$ 与 $\\vec{v}'$ 张成的平面且不做功（始终垂直于相对速度），只改变相对运动的方向。"))+
   app(p("<strong>应用：</strong>北半球河流右岸冲刷更重、气旋呈逆时针旋转、运动物体发生横向偏转，都是科里奥利力作用的结果。因 $F_{\\text{Cor}}\\propto v'$，静止物体不受科里奥利力。"))
 )},
{"id":"c2s8-3","name":"地球自转的力学效应：傅科摆与落体偏东","tags":["def","der","app"],"brief":"科里奥利力的两个经典可观测效应，直接证明地球在自转。",
 "body": wrap(
   defn("地球自转的力学效应",p("由于地球自转，地面参考系是一个转动非惯性系，其中水平运动的物体受到科里奥利力 $\\vec{F}_{\\text{Cor}}=-2m\\vec{\\omega}\\times\\vec{v}'$ 的作用。这一惯性力导致<strong>傅科摆</strong>摆面缓慢旋转与<strong>落体偏东</strong>等可观测现象，成为地球自转的直接证据。"))+
   der(p("<strong>第一步（本地坐标系与角速度分解）：</strong>取地面坐标系：$x$ 轴指向东，$y$ 轴指向北，$z$ 轴竖直向上。设纬度为 $\\lambda$，地球自转角速度矢量 $\\vec{\\omega}$ 的北向水平分量为 $\\omega\\cos\\lambda$、竖直分量为 $\\omega\\sin\\lambda$。")+
   p("<strong>第二步（求科里奥利力）：</strong>自由落体的相对速度近似为 $\\vec{v}'=-v_z\\hat{z}$，只有 $\\vec{\\omega}$ 的水平分量参与叉积：")+
   fml("\\vec{\\omega}\\times\\vec{v}'=(\\omega\\cos\\lambda\\,\\hat{y})\\times(-v_z\\hat{z})=-\\omega\\cos\\lambda\\,v_z\\,\\hat{x}")+
   p("故科里奥利力沿东向（$+x$）为正，大小为 $2m\\omega\\cos\\lambda\\,v_z$，对应的向东加速度")+
   fml("a_x=2\\omega\\cos\\lambda\\;v_z=2\\omega\\cos\\lambda\\,g\\,t")+
   p("<strong>第三步（两次积分求偏移）：</strong>对时间积分一次得向东速度 $v_x=\\omega\\cos\\lambda\\,g\\,t^2$，再积分一次得向东偏移：")+
   fml("x=\\frac{1}{3}\\omega\\cos\\lambda\\,g\\,t^3")+
   p("用下落高度 $h=\\tfrac{1}{2}gt^2$ 消去 $t$，得落体偏东量 $x=\\dfrac{1}{3}\\omega\\cos\\lambda\\sqrt{\\dfrac{8h^3}{g}}$。例如在纬度 $\\lambda=45^\\circ$、$h=100\\,\\text{m}$ 时，偏移量约为 $1.5\\,\\text{cm}$。"))+
   app(p("<strong>应用（傅科摆）：</strong>摆锤在水平面内振动时，科里奥利力使其振动平面缓慢转动。北半球摆面顺时针旋转的角速度为 $\\omega\\sin\\lambda$，旋转周期 $T=\\dfrac{2\\pi}{\\omega\\sin\\lambda}$，在北极处 $T$ 恰为一个恒星日；在赤道处 $\\lambda=0$，摆面不旋转。"))+
   note(p("十九世纪初德国矿井中的落体实验，其观测到的向东偏移与科里奥利力的预言量级相符，成为地球自转的间接验证。此外 $\\vec{\\omega}$ 的竖直分量还会使竖直落体产生极微小的水平偏转，属于更高阶的效应。"))
 )},
]},
]
ch3_sections = [
# ---- 3.1 动量定理与动量守恒 ----
{
"name": "3.1 动量定理与动量守恒",
"color": "#c2410c",
"desc": "冲量、动量定理与动量守恒定律",
"items": [
{"id":"c3s1-1","name":"冲量与动量定理","tags":["thm","der"],"brief":"合外力的冲量等于质点动量的增量。",
 "body": wrap(
   defn("动量与冲量",p("质点的动量为 $\\mathbf{p}=m\\mathbf{v}$。力对时间的积累效应称为冲量，定义为 $\\mathbf{I}=\\int_{t_1}^{t_2}\\mathbf{F}\\,dt$。"))+
   thm("动量定理",p("质点所受合外力的冲量等于其动量的增量：")+
   fml("\\mathbf{I}=\\int_{t_1}^{t_2}\\mathbf{F}\\,dt=\\mathbf{p}_2-\\mathbf{p}_1=m\\mathbf{v}_2-m\\mathbf{v}_1"))+
   der(p("<strong>第一步：</strong>由牛顿第二定律的动量形式，力等于动量对时间的变化率：")+
   fml("\\mathbf{F}=\\frac{d\\mathbf{p}}{dt}")+
   p("<strong>第二步：</strong>两边同乘 $dt$，得元冲量 $\\mathbf{F}\\,dt=d\\mathbf{p}$，再对时间积分：")+
   fml("\\int_{t_1}^{t_2}\\mathbf{F}\\,dt=\\int_{\\mathbf{p}_1}^{\\mathbf{p}_2}d\\mathbf{p}=\\mathbf{p}_2-\\mathbf{p}_1")+
   p("<strong>第三步：</strong>在直角坐标下写成分量式，各分量独立成立：")+
   fml("I_x=\\int_{t_1}^{t_2}F_x\\,dt=mv_{2x}-mv_{1x},\\quad I_y=\\cdots,\\quad I_z=\\cdots")+
   p("矢量式与三个标量分量式完全等价。") )+
   exa(p("缓冲与冲击：当动量变化量 $\\Delta p$ 一定时，延长作用时间 $\\Delta t$ 可减小平均冲力 $\\bar{F}=\\frac{\\Delta p}{\\Delta t}$，故跳落时屈膝、汽车安全气囊能显著降低冲击力。"))+
   note(p("动量定理是矢量方程，可用于瞬时冲击这类力随时间变化剧烈、难以直接求加速度的过程。"))
 )},
{"id":"c3s1-2","name":"动量守恒定律","tags":["thm","der"],"brief":"合外力为零时系统的总动量保持不变。",
 "fig":"collision","figCap":"两体碰撞中系统总动量守恒",
 "body": wrap(
   thm("动量守恒定律",p("当系统所受合外力为零（或远小于内力、可忽略）时，系统的总动量保持不变：")+
   fml("\\sum_i m_i\\mathbf{v}_i=\\text{常量},\\qquad \\text{当 }\\sum\\mathbf{F}_{\\text{外}}=0"))+
   der(p("<strong>推导：</strong>对由 $n$ 个质点组成的系统，第 $i$ 个质点受外力 $\\mathbf{F}_i^{\\text{外}}$ 与内力 $\\mathbf{F}_i^{\\text{内}}$，应用动量定理：")+
   fml("\\mathbf{F}_i^{\\text{外}}+\\mathbf{F}_i^{\\text{内}}=\\frac{d\\mathbf{p}_i}{dt}")+
   p("对所有质点求和。内力按牛顿第三定律成对出现、等大反向，两两抵消，故内力之和为零：")+
   fml("\\sum_i\\mathbf{F}_i^{\\text{内}}=0")+
   p("于是合外力等于系统总动量的变化率：")+
   fml("\\sum_i\\mathbf{F}_i^{\\text{外}}=\\sum_i\\frac{d\\mathbf{p}_i}{dt}=\\frac{d}{dt}\\sum_i\\mathbf{p}_i")+
   p("当 $\\sum_i\\mathbf{F}_i^{\\text{外}}=0$ 时，$\\frac{d}{dt}\\sum_i\\mathbf{p}_i=0$，积分得 $\\sum_i\\mathbf{p}_i=\\text{常量}$。") )+
   app(p("碰撞、爆炸、火箭反冲等问题中内力远大于外力，可按动量守恒处理。动量守恒是矢量式，可对各方向分量独立使用，其适用范围比牛顿第二定律更广。"))
 )},
]},
# ---- 3.2 质点动量矩定理与角动量守恒 ----
{
"name": "3.2 质点动量矩定理与角动量守恒",
"color": "#ea580c",
"desc": "角动量、力矩、动量矩定理与角动量守恒",
"items": [
{"id":"c3s2-1","name":"质点的角动量与力矩","tags":["def","der"],"brief":"角动量与力矩的定义及其微商关系。",
 "fig":"circular","figCap":"质点作圆周运动时相对圆心的角动量",
 "body": wrap(
   defn("角动量",p("质点相对固定点 $O$ 的角动量定义为位置矢量与动量的叉乘：")+
   fml("\\mathbf{L}=\\mathbf{r}\\times\\mathbf{p}=\\mathbf{r}\\times m\\mathbf{v}"))+
   defn("力矩",p("力 $\\mathbf{F}$ 相对同一点 $O$ 的力矩定义为：")+
   fml("\\mathbf{M}=\\mathbf{r}\\times\\mathbf{F}")+
   p("其大小为 $M=rF\\sin\\theta$，方向由右手螺旋定则确定，$\\theta$ 为 $\\mathbf{r}$ 与 $\\mathbf{F}$ 的夹角。"))+
   der(p("<strong>推导角动量定理：</strong>对 $\\mathbf{L}=\\mathbf{r}\\times\\mathbf{p}$ 求时间导数，用乘积法则：")+
   fml("\\frac{d\\mathbf{L}}{dt}=\\frac{d\\mathbf{r}}{dt}\\times\\mathbf{p}+\\mathbf{r}\\times\\frac{d\\mathbf{p}}{dt}")+
   p("第一项中 $\\frac{d\\mathbf{r}}{dt}=\\mathbf{v}$ 与 $\\mathbf{p}=m\\mathbf{v}$ 平行，叉乘为零；第二项用牛顿第二定律 $\\frac{d\\mathbf{p}}{dt}=\\mathbf{F}$：")+
   fml("\\frac{d\\mathbf{L}}{dt}=\\mathbf{r}\\times\\mathbf{F}=\\mathbf{M}")+
   p("即质点对固定点 $O$ 的角动量对时间的微商，等于所受合力对该点的力矩。") )+
   exa(p("匀速圆周运动：质点以速率 $v$ 沿半径 $r$ 的圆运动，$\\mathbf{r}\\perp\\mathbf{v}$，故 $L=mvr=mr^2\\omega$，方向沿转轴方向且恒定。"))
 )},
{"id":"c3s2-2","name":"质点动量矩定理与守恒","tags":["thm","der"],"brief":"合外力矩为零时角动量守恒。",
 "body": wrap(
   thm("动量矩定理（角动量定理）",p("质点对固定点 $O$ 的角动量对时间的导数，等于合外力对该点的力矩：")+
   fml("\\frac{d\\mathbf{L}}{dt}=\\mathbf{M}=\\mathbf{r}\\times\\mathbf{F}"))+
   thm("角动量守恒定律",p("当质点所受合力相对某固定点的力矩为零时，质点对该点的角动量守恒：")+
   fml("\\mathbf{M}=0\\implies \\mathbf{L}=\\mathbf{r}\\times m\\mathbf{v}=\\text{常量}"))+
   der(p("<strong>守恒条件的推导：</strong>由动量矩定理 $\\frac{d\\mathbf{L}}{dt}=\\mathbf{M}$ 出发。")+
   p("<strong>情形一：</strong>若 $\\mathbf{M}=0$，则 $\\frac{d\\mathbf{L}}{dt}=0$，$\\mathbf{L}$ 为常矢量，其大小与方向均不变。")+
   p("<strong>情形二：</strong>若力 $\\mathbf{F}$ 始终通过固定点 $O$（即有心力，$\\mathbf{F}\\parallel\\mathbf{r}$），则 $\\mathbf{M}=\\mathbf{r}\\times\\mathbf{F}=0$，角动量同样守恒。两种情形统一记作：")+
   fml("\\mathbf{M}=0\\implies \\frac{d\\mathbf{L}}{dt}=0\\implies \\mathbf{L}=\\text{常矢量}")+
   p("由 $\\mathbf{L}$ 方向恒定，可知 $\\mathbf{r}$ 与 $\\mathbf{v}$ 始终位于垂直于 $\\mathbf{L}$ 的平面内，故运动为平面运动；由 $L$ 大小恒定可得面积速度守恒：")+
   fml("\\frac{dS}{dt}=\\frac{1}{2}|\\mathbf{r}\\times\\mathbf{v}|=\\frac{L}{2m}=\\text{常量}")+
   p("这正是开普勒第二定律的实质。") )+
   app(p("行星绕日运动、电子绕核运动、绳子被拉短时角动量守恒（$mvr=\\text{常量}$，故 $r$ 减小则 $v$ 增大）等，都是角动量守恒的典型应用。"))
 )},
]},
# ---- 3.3 功与功率 ----
{
"name": "3.3 功与功率",
"color": "#f97316",
"desc": "功的定义、变力做功的线积分与功率",
"items": [
{"id":"c3s3-1","name":"功的定义与变力做功","tags":["def","der"],"brief":"力对空间的积累效应。",
 "body": wrap(
   defn("恒力的功",p("恒力 $\\mathbf{F}$ 作用下质点发生位移 $\\Delta\\mathbf{r}$，力做的功等于力与位移的点乘：")+
   fml("W=\\mathbf{F}\\cdot\\Delta\\mathbf{r}=F|\\Delta\\mathbf{r}|\\cos\\theta"))+
   defn("变力的功",p("变力沿曲线做功等于力沿路径的线积分：")+
   fml("W=\\int_{a}^{b}\\mathbf{F}\\cdot d\\mathbf{r}=\\int_{a}^{b}F\\cos\\theta\\,ds"))+
   der(p("<strong>第一步（微元求和）：</strong>把路径分成无穷多小段，第 $i$ 段位移 $d\\mathbf{r}_i$ 上力近似恒定，其元功为：")+
   fml("dW=\\mathbf{F}\\cdot d\\mathbf{r}=F\\,ds\\cos\\theta")+
   p("<strong>第二步（取极限成积分）：</strong>沿整条路径求和并取极限，得线积分：")+
   fml("W=\\lim_{n\\to\\infty}\\sum_i\\mathbf{F}_i\\cdot d\\mathbf{r}_i=\\int_{a}^{b}\\mathbf{F}\\cdot d\\mathbf{r}")+
   p("<strong>第三步（化为坐标分量）：</strong>把 $d\\mathbf{r}=dx\\,\\mathbf{i}+dy\\,\\mathbf{j}+dz\\,\\mathbf{k}$ 代入，得三个分量的积分之和：")+
   fml("W=\\int_{x_1}^{x_2}F_x\\,dx+\\int_{y_1}^{y_2}F_y\\,dy+\\int_{z_1}^{z_2}F_z\\,dz")+
   p("功是标量，有正负：$\\theta<90^\\circ$ 做正功，$\\theta>90^\\circ$ 做负功，$\\theta=90^\\circ$ 不做功。") )+
   exa(p("弹簧弹力做功：弹力 $F=-kx$ 沿 $x$ 方向，从 $x_1$ 拉到 $x_2$，$W=\\int_{x_1}^{x_2}(-kx)\\,dx=-\\tfrac{1}{2}k(x_2^2-x_1^2)$。做功只与始末位置有关、与路径无关，说明弹力是保守力。"))
 )},
{"id":"c3s3-2","name":"功率","tags":["def","der"],"brief":"做功的快慢：平均功率与瞬时功率。",
 "body": wrap(
   defn("功率",p("功率是单位时间内所做的功，描述做功的快慢：")+
   fml("P=\\frac{dW}{dt}")+
   p("平均功率 $\\bar{P}=\\frac{W}{\\Delta t}$，瞬时功率 $P=\\lim_{\\Delta t\\to 0}\\frac{\\Delta W}{\\Delta t}$。"))+
   der(p("<strong>推导瞬时功率公式：</strong>由元功 $dW=\\mathbf{F}\\cdot d\\mathbf{r}$，两边同除以 $dt$：")+
   fml("P=\\frac{dW}{dt}=\\mathbf{F}\\cdot\\frac{d\\mathbf{r}}{dt}=\\mathbf{F}\\cdot\\mathbf{v}")+
   p("写成分量形式：")+
   fml("P=F_x v_x+F_y v_y+F_z v_z")+
   p("对转动情形，把元功 $dW=M\\,d\\theta$ 代入定义，得力矩的功率 $P=M\\omega$。") )+
   app(p("汽车行驶时发动机牵引力功率 $P=Fv$。额定功率一定时牵引力与速度成反比，故上坡或起步需降速以增大牵引力；机械效率 $\\eta=\\frac{P_{\\text{有用}}}{P_{\\text{输入}}}\\le 1$。"))
 )},
]},
# ---- 3.4 势能与保守力场 ----
{
"name": "3.4 势能与保守力场",
"color": "#f59e0b",
"desc": "保守力判据、势能定义与由势能求力",
"items": [
{"id":"c3s4-1","name":"保守力及其判据","tags":["def","der"],"brief":"做功与路径无关的力称为保守力。",
 "body": wrap(
   defn("保守力",p("若力做功只取决于始末位置、与路径无关，则称该力为保守力。等价表述为沿任意闭合路径一周做功为零：")+
   fml("\\oint_L\\mathbf{F}\\cdot d\\mathbf{r}=0"))+
   der(p("<strong>判据等价性的推导：</strong>设沿路径 1 从 $A$ 到 $B$ 做功 $W_{AB}^{(1)}$，沿路径 2 从 $B$ 回到 $A$ 做功记为 $W_{BA}^{(2)}$。因沿路径反向积分变号，$W_{BA}^{(2)}=-W_{AB}^{(2)}$。")+
   p("若做功与路径无关，则 $W_{AB}^{(1)}=W_{AB}^{(2)}$，于是绕闭合回路一周积分为零：")+
   fml("\\oint\\mathbf{F}\\cdot d\\mathbf{r}=W_{AB}^{(1)}+W_{BA}^{(2)}=W_{AB}^{(1)}-W_{AB}^{(2)}=0")+
   p("反之，若任意闭合路径积分均为零，则两条路径做功相等，即做功与路径无关。综上：")+
   fml("\\oint_L\\mathbf{F}\\cdot d\\mathbf{r}=0\\iff W \\text{ 与路径无关}")+
   p("在直角坐标下，$\\oint\\mathbf{F}\\cdot d\\mathbf{r}=0$ 等价于 $\\nabla\\times\\mathbf{F}=0$，即保守力场是无旋场。") )+
   app(p("重力、弹力、静电力、万有引力都是保守力，可以引入相应的势能；摩擦力、空气阻力沿闭合路径做功不为零，是非保守力，不能引入势能。"))
 )},
{"id":"c3s4-2","name":"势能与常见势能表达式","tags":["def","der"],"brief":"保守力做功等于势能减少；重力、弹性、引力势能。",
 "body": wrap(
   defn("势能",p("保守力做功等于势能的减少量：")+
   fml("W_{\\text{保}}=E_{p1}-E_{p2}=-\\Delta E_p")+
   p("以参考点 $\\mathbf{r}_0$ 为零势能点，则任意位置 $\\mathbf{r}$ 处的势能为：")+
   fml("E_p(\\mathbf{r})=-\\int_{\\mathbf{r}_0}^{\\mathbf{r}}\\mathbf{F}_{\\text{保}}\\cdot d\\mathbf{r}"))+
   der(p("<strong>重力势能：</strong>取地面 $y=0$ 为零点，重力 $\\mathbf{F}=-mg\\mathbf{j}$，物体升高 $h$：")+
   fml("E_p=-\\int_0^h(-mg)\\,dy=mg h")+
   p("<strong>弹性势能：</strong>取原长 $x=0$ 为零点，弹力 $F=-kx$：")+
   fml("E_p=-\\int_0^x(-kx')\\,dx'=\\tfrac{1}{2}kx^2")+
   p("<strong>引力势能：</strong>取无穷远为零点，万有引力指向原点 $\\mathbf{F}=-G\\frac{m_1m_2}{r^2}\\mathbf{e}_r$：")+
   fml("E_p=-\\int_{\\infty}^{r}\\left(-G\\frac{m_1m_2}{r'^2}\\right)dr'=-G\\frac{m_1m_2}{r}")+
   p("引力势能为负值，表明两质点靠近时势能降低、系统更稳定。") )+
   exa(p("在地面附近 $h\\ll R$ 时，$E_p=-\\frac{GMm}{R+h}\\approx-\\frac{GMm}{R}+mgh$，与重力势能 $mgh$ 只相差一个常数项，舍弃常数即得 $mgh$。"))
 )},
{"id":"c3s4-3","name":"由势能求保守力","tags":["thm","der"],"brief":"保守力等于势能的负梯度。",
 "body": wrap(
   thm("保守力与势能的关系",p("在保守场中，力等于势能的负梯度：")+
   fml("\\mathbf{F}=-\\nabla E_p=-\\left(\\frac{\\partial E_p}{\\partial x}\\mathbf{i}+\\frac{\\partial E_p}{\\partial y}\\mathbf{j}+\\frac{\\partial E_p}{\\partial z}\\mathbf{k}\\right)"))+
   der(p("<strong>第一步（一维情形）：</strong>保守力做功等于势能减少，$dW=F\\,dx=-dE_p$，故：")+
   fml("F=-\\frac{dE_p}{dx}")+
   p("<strong>第二步（推广到三维）：</strong>沿任意方向 $d\\mathbf{r}$ 移动，势能的全微分为：")+
   fml("dE_p=\\nabla E_p\\cdot d\\mathbf{r}")+
   p("<strong>第三步（比较两式）：</strong>另一方面由势能定义 $dE_p=-\\mathbf{F}\\cdot d\\mathbf{r}$。因 $d\\mathbf{r}$ 任意，两式恒等即要求：")+
   fml("\\mathbf{F}=-\\nabla E_p")+
   p("反之，已知势能函数，对坐标求偏导即可得各分量力。") )+
   app(p("弹簧势能 $E_p=\\tfrac{1}{2}kx^2$，则 $F=-\\frac{dE_p}{dx}=-kx$，恢复力总指向平衡位置。由此提供了研究平衡与稳定性的工具：$\\frac{dE_p}{dx}=0$ 给出平衡点，$\\frac{d^2E_p}{dx^2}>0$ 为稳定平衡。"))
 )},
]},
# ---- 3.5 动能与动能定理 ----
{
"name": "3.5 动能与动能定理",
"color": "#d97706",
"desc": "动能、动能定理及其应用",
"items": [
{"id":"c3s5-1","name":"动能与动能定理","tags":["def","thm","der"],"brief":"合外力做功等于动能的增量。",
 "body": wrap(
   defn("动能",p("质点的动能定义为：")+
   fml("E_k=\\frac{1}{2}mv^2"))+
   thm("动能定理",p("合外力对质点做的功等于质点动能的增量：")+
   fml("W_{\\text{合}}=\\Delta E_k=\\tfrac{1}{2}mv^2-\\tfrac{1}{2}mv_0^2"))+
   der(p("<strong>第一步：</strong>由牛顿第二定律 $\\mathbf{F}=m\\frac{d\\mathbf{v}}{dt}$，合外力做功为：")+
   fml("W=\\int\\mathbf{F}\\cdot d\\mathbf{r}=\\int m\\frac{d\\mathbf{v}}{dt}\\cdot d\\mathbf{r}")+
   p("<strong>第二步：</strong>将 $d\\mathbf{r}=\\mathbf{v}\\,dt$ 代入，得：")+
   fml("W=\\int m\\frac{d\\mathbf{v}}{dt}\\cdot\\mathbf{v}\\,dt=\\int m\\mathbf{v}\\cdot d\\mathbf{v}")+
   p("<strong>第三步：</strong>利用 $\\mathbf{v}\\cdot d\\mathbf{v}=d\\left(\\tfrac{1}{2}v^2\\right)$，因为 $d(v^2)=d(\\mathbf{v}\\cdot\\mathbf{v})=2\\mathbf{v}\\cdot d\\mathbf{v}$：")+
   fml("W=m\\int_{v_0}^{v}d\\left(\\tfrac{1}{2}v^2\\right)=\\tfrac{1}{2}mv^2-\\tfrac{1}{2}mv_0^2=\\Delta E_k")+
   p("动能定理是标量方程，适用于惯性系，正功使动能增加、负功使动能减少。") )+
   exa(p("物体在摩擦力作用下滑行距离 $s$ 后停下：$-\\mu mg s=0-\\tfrac{1}{2}mv_0^2$，解得滑行距离 $s=\\frac{v_0^2}{2\\mu g}$。"))
 )},
{"id":"c3s5-2","name":"多个力做功与动能定理的应用","tags":["thm","der","app"],"brief":"合力的功等于各分力功的代数和。",
 "body": wrap(
   thm("功的代数和",p("合力的功等于各分力做功的代数和，且等于动能的增量：")+
   fml("W_{\\text{合}}=\\sum_k W_k=\\Delta E_k"))+
   der(p("<strong>第一步：</strong>设质点受若干力 $\\mathbf{F}_1,\\mathbf{F}_2,\\cdots$，把合力代入功的定义并对积分线性分解：")+
   fml("W_{\\text{合}}=\\int\\left(\\sum_k\\mathbf{F}_k\\right)\\cdot d\\mathbf{r}=\\sum_k\\int\\mathbf{F}_k\\cdot d\\mathbf{r}=\\sum_k W_k")+
   p("<strong>第二步：</strong>由动能定理，各分力功的代数和等于动能增量 $\\sum_k W_k=\\Delta E_k$。")+
   p("<strong>第三步：</strong>在曲线运动中，垂直于速度的力不做功：")+
   fml("dW=F\\cos\\theta\\,ds=0\\quad(\\theta=90^\\circ)")+
   p("因此绳张力、光滑面支持力等若始终垂直速度，可完全不计其功，使问题大为简化。") )+
   app(p("用动能定理处理变力、曲线运动问题，常比直接积分牛顿定律更简便。例如物体沿光滑曲面下滑、绳索张力变化的问题，只需求出重力所做的功，即可求出末速度。"))
 )},
]},
# ---- 3.6 机械能守恒定律与功能原理 ----
{
"name": "3.6 机械能守恒定律与功能原理",
"color": "#b45309",
"desc": "机械能守恒定律与功能原理",
"items": [
{"id":"c3s6-1","name":"机械能守恒定律","tags":["thm","der"],"brief":"只有保守力做功时机械能守恒。",
 "body": wrap(
   thm("机械能守恒定律",p("当系统内只有保守力做功（无外力做功或外力不做功、且无非保守内力做功）时，系统的机械能保持不变：")+
   fml("E=E_k+E_p=\\text{常量}"))+
   der(p("<strong>第一步：</strong>把作用力分为保守力与非保守力，由动能定理：")+
   fml("W_{\\text{保}}+W_{\\text{非保}}=\\Delta E_k")+
   p("<strong>第二步：</strong>由保守力做功与势能关系 $W_{\\text{保}}=-\\Delta E_p$，代入上式：")+
   fml("-\\Delta E_p+W_{\\text{非保}}=\\Delta E_k\\implies W_{\\text{非保}}=\\Delta(E_k+E_p)=\\Delta E")+
   p("<strong>第三步：</strong>若 $W_{\\text{非保}}=0$，则 $\\Delta E=0$，即 $E_k+E_p$ 恒定，展开为：")+
   fml("\\tfrac{1}{2}mv_1^2+E_{p1}=\\tfrac{1}{2}mv_2^2+E_{p2}")+
   p("由此可在两位置之间直接建立速度与高度的关系，而无须求解运动过程。") )+
   exa(p("自由落体：由 $\\tfrac{1}{2}mv^2=mgh$ 得 $v=\\sqrt{2gh}$；单摆摆动、过山车等理想情形均可用机械能守恒求速率。"))
 )},
{"id":"c3s6-2","name":"功能原理","tags":["thm","der"],"brief":"外力与非保守内力做功之和等于机械能增量。",
 "body": wrap(
   thm("功能原理",p("系统机械能的增量，等于外力做功与非保守内力做功之和：")+
   fml("W_{\\text{外}}+W_{\\text{非保内}}=\\Delta E=\\Delta(E_k+E_p)"))+
   der(p("<strong>第一步：</strong>对系统应用动能定理 $W_{\\text{外}}+W_{\\text{内}}=\\Delta E_k$，并把内力功分为保守内力功与非保守内力功：")+
   fml("W_{\\text{外}}+W_{\\text{保内}}+W_{\\text{非保内}}=\\Delta E_k")+
   p("<strong>第二步：</strong>用 $W_{\\text{保内}}=-\\Delta E_p$ 把保守内力功用势能变化表示：")+
   fml("W_{\\text{外}}+W_{\\text{非保内}}=\\Delta E_k+\\Delta E_p=\\Delta E")+
   p("与动能定理的区别在于：功能原理已把保守内力（重力、弹力等）的作用吸收进势能变化，故方程左侧不再出现保守内力功。") )+
   app(p("摩擦力做功 $W_{\\text{非保内}}=-f\\,s_{\\text{相对}}<0$，系统机械能减少并转化为内能 $Q=f\\,s_{\\text{相对}}$。功能原理是能量守恒定律在力学中的具体体现。"))
 )},
]},
# ---- 3.7 有心力与有效势能 ----
{
"name": "3.7 有心力与有效势能",
"color": "#fb923c",
"desc": "有心力的守恒量、运动方程与有效势能",
"items": [
{"id":"c3s7-1","name":"有心力场中的守恒量与基本方程","tags":["def","der"],"brief":"有心力下角动量与能量守恒，运动为平面运动。",
 "body": wrap(
   defn("有心力",p("若力的作用线始终通过某一固定点 $O$，且大小只与到 $O$ 的距离有关，即 $\\mathbf{F}=F(r)\\mathbf{e}_r$，则称该力为有心力，$O$ 称为力心。"))+
   der(p("<strong>守恒量一（角动量）：</strong>有心力对力心的力矩 $\\mathbf{M}=\\mathbf{r}\\times\\mathbf{F}$，因 $\\mathbf{F}\\parallel\\mathbf{r}$ 故 $\\mathbf{M}=0$：")+
   fml("\\frac{d\\mathbf{L}}{dt}=0\\implies \\mathbf{L}=mr^2\\dot{\\theta}=\\text{常量}")+
   p("<strong>守恒量二（能量）：</strong>有心力是保守力，势能只依赖 $r$，故机械能守恒：")+
   fml("E=\\tfrac{1}{2}m\\left(\\dot{r}^2+r^2\\dot{\\theta}^2\\right)+V(r)=\\text{常量}")+
   p("<strong>运动方程：</strong>由 $\\mathbf{L}$ 方向不变可知运动限定在垂直于 $\\mathbf{L}$ 的平面内。按牛顿第二定律 $\\mathbf{F}=m\\mathbf{a}$，径向分量为：")+
   fml("m\\left(\\ddot{r}-r\\dot{\\theta}^2\\right)=F(r)")+
   p("角向分量为零，恰对应 $\\frac{d}{dt}\\left(mr^2\\dot{\\theta}\\right)=0$，即角动量守恒。")+
   p("这两个守恒量把三维运动降为平面内可积的问题。") )+
   exa(p("行星绕日运动是典型有心力问题：太阳引力通过力心，角动量守恒给出面积速度 $\\dot{S}=\\frac{L}{2m}$ 恒定，即开普勒第二定律。"))
 )},
{"id":"c3s7-2","name":"有效势能","tags":["thm","der"],"brief":"用角动量消去角运动，化为径向一维问题。",
 "body": wrap(
   thm("有效势能",p("利用角动量守恒 $L=mr^2\\dot{\\theta}$ 消去 $\\dot{\\theta}$ 后，径向运动可等效为一维问题，其有效势能为：")+
   fml("V_{\\text{eff}}(r)=V(r)+\\frac{L^2}{2mr^2}"))+
   der(p("<strong>第一步：</strong>把守恒总能量中的角向动能用 $L$ 表示。由 $\\dot{\\theta}=\\frac{L}{mr^2}$：")+
   fml("\\tfrac{1}{2}mr^2\\dot{\\theta}^2=\\tfrac{1}{2}mr^2\\left(\\frac{L}{mr^2}\\right)^2=\\frac{L^2}{2mr^2}")+
   p("<strong>第二步：</strong>代入总能量表达式，得到纯粹关于 $r$ 的一维形式：")+
   fml("E=\\tfrac{1}{2}m\\dot{r}^2+\\frac{L^2}{2mr^2}+V(r)=\\tfrac{1}{2}m\\dot{r}^2+V_{\\text{eff}}(r)")+
   p("<strong>第三步：</strong>对 $r$ 求导可复原径向力方程：")+
   fml("m\\ddot{r}=-\\frac{dV_{\\text{eff}}}{dr}=F(r)+\\frac{L^2}{mr^3}")+
   p("其中 $\\frac{L^2}{mr^3}=mr\\dot{\\theta}^2$ 即等效的离心力项。由 $E=V_{\\text{eff}}(r)$ 的根可得运动的转折点（近日点与远日点），$r$ 被限制在 $V_{\\text{eff}}\\le E$ 的区间内。") )+
   exa(p("引力场 $V(r)=-\\frac{GMm}{r}$ 的有效势能在 $r_0=\\frac{L^2}{GMm^2}$ 处取极小值。当 $E<0$ 时质点被束缚在 $r_1\\le r\\le r_2$ 之间作椭圆运动；当 $E\\ge 0$ 时轨道开放，分别对应抛物线或双曲线轨道。"))
 )},
]},
# ---- 3.8 两体问题与质心运动定理 ----
{
"name": "3.8 两体问题与质心运动定理",
"color": "#fbbf24",
"desc": "两体问题化归单质点问题与质心运动定理",
"items": [
{"id":"c3s8-1","name":"两体问题化归单质点问题","tags":["thm","der"],"brief":"用相对坐标与约化质量把两体问题化为单体问题。",
 "body": wrap(
   thm("两体问题化归单质点问题",p("两体系统只受彼此相互作用的内部保守力时，其相对运动可等效为质量为约化质量 $\\mu$ 的单一质点在有心力场中的运动：")+
   fml("\\mu\\ddot{\\mathbf{r}}=\\mathbf{F}(r),\\qquad \\mu=\\frac{m_1 m_2}{m_1+m_2}")+
   p("其中 $\\mathbf{r}=\\mathbf{r}_1-\\mathbf{r}_2$ 为相对位置矢量。"))+
   der(p("<strong>第一步：</strong>两质点 $m_1,m_2$ 只受彼此作用力 $\\mathbf{F}_{12}=-\\mathbf{F}_{21}=\\mathbf{F}$，牛顿方程为：")+
   fml("m_1\\ddot{\\mathbf{r}}_1=\\mathbf{F},\\qquad m_2\\ddot{\\mathbf{r}}_2=-\\mathbf{F}")+
   p("<strong>第二步（质心运动）：</strong>质心 $\\mathbf{r}_C=\\frac{m_1\\mathbf{r}_1+m_2\\mathbf{r}_2}{M}$，其中 $M=m_1+m_2$。两式相加得 $M\\ddot{\\mathbf{r}}_C=0$，故质心作匀速直线运动，与相对运动解耦。")+
   p("<strong>第三步（相对运动）：</strong>由 $\\mathbf{r}_1=\\mathbf{r}_C+\\frac{m_2}{M}\\mathbf{r}$、$\\mathbf{r}_2=\\mathbf{r}_C-\\frac{m_1}{M}\\mathbf{r}$ 求二阶导：")+
   fml("\\ddot{\\mathbf{r}}=\\ddot{\\mathbf{r}}_1-\\ddot{\\mathbf{r}}_2=\\frac{\\mathbf{F}}{m_1}+\\frac{\\mathbf{F}}{m_2}=\\mathbf{F}\\left(\\frac{1}{m_1}+\\frac{1}{m_2}\\right)=\\frac{\\mathbf{F}}{\\mu}")+
   p("即 $\\mu\\ddot{\\mathbf{r}}=\\mathbf{F}(r)$，两体问题化归单个等效质点（约化质量 $\\mu$）在有心力中的运动。") )+
   app(p("质心平动由外力决定，相对运动由内部相互作用决定。当 $m_1\\gg m_2$ 时 $\\mu\\approx m_2$，问题退化为单体问题，如地球绕太阳的运动；双星、氢原子等则必须用约化质量处理。"))
 )},
{"id":"c3s8-2","name":"质心运动定理","tags":["thm","der"],"brief":"合外力等于总质量乘质心加速度。",
 "fig":"com","figCap":"两质点系统的质心 C 与位矢",
 "body": wrap(
   thm("质心运动定理",p("质点系所受合外力等于系统总质量与质心加速度的乘积：")+
   fml("\\sum_i\\mathbf{F}_i^{\\text{外}}=M\\frac{d^2\\mathbf{r}_C}{dt^2}=M\\mathbf{a}_C"))+
   der(p("<strong>第一步：</strong>质心定义为 $\\mathbf{r}_C=\\frac{1}{M}\\sum_i m_i\\mathbf{r}_i$，对时间求二阶导：")+
   fml("M\\ddot{\\mathbf{r}}_C=\\sum_i m_i\\ddot{\\mathbf{r}}_i=\\sum_i\\mathbf{F}_i")+
   p("<strong>第二步：</strong>把每个质点的受力分为外力与内力 $\\mathbf{F}_i=\\mathbf{F}_i^{\\text{外}}+\\mathbf{F}_i^{\\text{内}}$，求和时内力按牛顿第三定律两两抵消：")+
   fml("\\sum_i\\mathbf{F}_i^{\\text{内}}=0")+
   p("<strong>第三步：</strong>于是：")+
   fml("M\\mathbf{a}_C=\\sum_i\\mathbf{F}_i^{\\text{外}}")+
   p("这表明质心的运动如同一个集中了全部质量、承受全部外力的质点，与内力无关。") )+
   app(p("抛出的旋转物体（如陀螺、哑铃）运动复杂，但其质心仍沿抛物线运动；爆炸后各碎片的运动虽杂乱，质心却继续原来的轨迹。系统合外力为零时质心保持静止或匀速直线运动，这是解决爆炸、反冲问题的关键。"))
 )},
]},
# ---- 3.9 碰撞 ----
{
"name": "3.9 碰撞",
"color": "#92400e",
"desc": "对心正碰的恢复系数与能量损失、斜碰",
"items": [
{"id":"c3s9-1","name":"对心正碰与恢复系数","tags":["def","thm","der"],"brief":"碰撞的动量守恒、恢复系数与动能损失。",
 "fig":"collision","figCap":"两球对心正碰的速度示意",
 "body": wrap(
   defn("恢复系数",p("两球对心正碰时，碰后与碰前相对速度之比定义为恢复系数：")+
   fml("e=\\frac{v_2'-v_1'}{v_1-v_2}")+
   p("$e=1$ 为完全弹性碰撞，$e=0$ 为完全非弹性碰撞（碰后共速），$0<e<1$ 为一般非弹性碰撞。"))+
   thm("碰后速度与动能损失",p("由动量守恒与恢复系数可解出碰后速度，动能损失为：")+
   fml("\\Delta E_k=\\tfrac{1}{2}\\frac{m_1m_2}{m_1+m_2}(1-e^2)(v_1-v_2)^2"))+
   der(p("<strong>第一步（动量守恒）：</strong>")+
   fml("m_1 v_1+m_2 v_2=m_1 v_1'+m_2 v_2'")+
   p("<strong>第二步（恢复系数）：</strong>")+
   fml("v_2'-v_1'=e(v_1-v_2)")+
   p("联立两式，解得碰后速度：")+
   fml("v_1'=\\frac{m_1-em_2}{m_1+m_2}v_1+\\frac{(1+e)m_2}{m_1+m_2}v_2,\\qquad v_2'=\\frac{(1+e)m_1}{m_1+m_2}v_1+\\frac{m_2-em_1}{m_1+m_2}v_2")+
   p("<strong>第三步（能量损失）：</strong>用质心系最简洁。质心速度 $v_C=\\frac{m_1v_1+m_2v_2}{M}$，相对速度 $u=v_1-v_2$。质心系动能为 $E_k'=\\frac{1}{2}\\mu u^2$，其中 $\\mu=\\frac{m_1m_2}{M}$；碰后相对速度 $u'=eu$：")+
   fml("\\Delta E_k=\\tfrac{1}{2}\\mu\\left(u^2-u'^2\\right)=\\tfrac{1}{2}\\frac{m_1m_2}{m_1+m_2}(1-e^2)(v_1-v_2)^2")+
   p("$e=1$ 时 $\\Delta E_k=0$，动能守恒；$e=0$ 时损失最大。") )+
   exa(p("等质量完全弹性正碰（$m_1=m_2$，$e=1$）：由公式得 $v_1'=v_2$，$v_2'=v_1$，两球恰好交换速度。"))
 )},
{"id":"c3s9-2","name":"斜碰（二维碰撞）","tags":["thm","der"],"brief":"二维碰撞的动量分量守恒与散射。",
 "fig":"oblique","figCap":"二维斜碰中两球的速度方向",
 "body": wrap(
   thm("斜碰的动量守恒",p("光滑小球二维碰撞时，取两球连心线为法向 $n$、垂直方向为切向 $t$。相互作用只沿法向，故切向速度不变，法向动量守恒：")+
   fml("m_1 v_{1n}+m_2 v_{2n}=m_1 v_{1n}'+m_2 v_{2n}',\\qquad v_{1t}=v_{1t}',\\ v_{2t}=v_{2t}'"))+
   der(p("<strong>第一步（切向速度不变）：</strong>光滑球间相互作用沿连心线（法向），故每个球在切向不受力：")+
   fml("\\int F_t\\,dt=0\\implies \\Delta v_t=0")+
   p("<strong>第二步（法向）：</strong>沿法向同时应用动量守恒与恢复系数：")+
   fml("e=\\frac{v_{2n}'-v_{1n}'}{v_{1n}-v_{2n}}")+
   p("<strong>第三步（质心系与实验室系）：</strong>在质心系中两球反向散射，速率按恢复系数缩放 $u'=eu$；再作伽利略变换回到实验室系，即得散射角分布。")+
   p("对等质量完全弹性斜碰，碰后两球运动方向互相垂直：")+
   fml("\\mathbf{v}_1'\\cdot\\mathbf{v}_2'=0\\quad(m_1=m_2,\\ e=1)") )+
   app(p("台球碰撞、粒子散射（如卢瑟福散射）都是斜碰问题。实验上通过测量散射角的分布来推断相互作用力的性质，这是核物理与粒子物理的重要分析手段。"))
 )},
]},
# ---- 3.10 质点系的动量矩定理与守恒 ----
{
"name": "3.10 质点系的动量矩定理与守恒",
"color": "#c2410c",
"desc": "对定点与对质心的动量矩定理与守恒",
"items": [
{"id":"c3s10-1","name":"质点系对定点的动量矩定理","tags":["thm","der"],"brief":"系统角动量的变化率等于外力对定点的总力矩。",
 "body": wrap(
   thm("对定点的动量矩定理",p("质点系对某固定点 $O$ 的总角动量对时间的导数，等于所有外力对 $O$ 点的力矩之矢量和：")+
   fml("\\frac{d\\mathbf{L}_O}{dt}=\\sum_i\\mathbf{M}_i^{\\text{外}}=\\sum_i\\mathbf{r}_i\\times\\mathbf{F}_i^{\\text{外}}"))+
   der(p("<strong>第一步：</strong>总角动量 $\\mathbf{L}_O=\\sum_i\\mathbf{r}_i\\times\\mathbf{p}_i$，对其求导：")+
   fml("\\frac{d\\mathbf{L}_O}{dt}=\\sum_i\\left(\\frac{d\\mathbf{r}_i}{dt}\\times\\mathbf{p}_i+\\mathbf{r}_i\\times\\frac{d\\mathbf{p}_i}{dt}\\right)")+
   p("<strong>第二步：</strong>第一项中 $\\frac{d\\mathbf{r}_i}{dt}=\\mathbf{v}_i$ 与 $\\mathbf{p}_i=m_i\\mathbf{v}_i$ 平行，叉乘为零；第二项用 $\\frac{d\\mathbf{p}_i}{dt}=\\mathbf{F}_i^{\\text{外}}+\\mathbf{F}_i^{\\text{内}}$：")+
   fml("\\frac{d\\mathbf{L}_O}{dt}=\\sum_i\\mathbf{r}_i\\times\\mathbf{F}_i^{\\text{外}}+\\sum_i\\mathbf{r}_i\\times\\mathbf{F}_i^{\\text{内}}")+
   p("<strong>第三步：</strong>内力力矩之和为零。因为相互作用力 $\\mathbf{F}_{ij}=-\\mathbf{F}_{ji}$ 且沿两点连线（有心力），有：")+
   fml("\\mathbf{r}_i\\times\\mathbf{F}_{ij}+\\mathbf{r}_j\\times\\mathbf{F}_{ji}=(\\mathbf{r}_i-\\mathbf{r}_j)\\times\\mathbf{F}_{ij}=0")+
   p("于是得对定点的动量矩定理：")+
   fml("\\frac{d\\mathbf{L}_O}{dt}=\\sum_i\\mathbf{r}_i\\times\\mathbf{F}_i^{\\text{外}}=M_O^{\\text{外}}")+
   p("当外力对 $O$ 点的总力矩为零时，$\\mathbf{L}_O$ 守恒。") )+
   exa(p("行星运动中太阳引力过力心（过日心），对日心的力矩恒为零，故行星对日心的角动量守恒，直接给出面积速度守恒。"))
 )},
{"id":"c3s10-2","name":"质点系对质心的动量矩定理","tags":["thm","der"],"brief":"在质心系中对质心的动量矩定理与定点形式相同。",
 "body": wrap(
   thm("对质心的动量矩定理",p("质点系相对质心 $C$ 的角动量的变化率，等于外力对质心的总力矩：")+
   fml("\\frac{d\\mathbf{L}_C}{dt}=\\sum_i\\mathbf{r}_i'\\times\\mathbf{F}_i^{\\text{外}}=M_C^{\\text{外}}")+
   p("其中 $\\mathbf{r}_i'$ 为质点相对质心的位矢，$\\mathbf{L}_C=\\sum_i\\mathbf{r}_i'\\times m_i\\mathbf{v}_i'$。"))+
   der(p("<strong>第一步：</strong>设 $\\mathbf{r}_i=\\mathbf{r}_C+\\mathbf{r}_i'$，$\\mathbf{v}_i=\\mathbf{v}_C+\\mathbf{v}_i'$，对 $\\mathbf{L}_C=\\sum_i\\mathbf{r}_i'\\times m_i\\mathbf{v}_i'$ 求导：")+
   fml("\\frac{d\\mathbf{L}_C}{dt}=\\sum_i\\frac{d\\mathbf{r}_i'}{dt}\\times m_i\\mathbf{v}_i'+\\sum_i\\mathbf{r}_i'\\times m_i\\frac{d\\mathbf{v}_i'}{dt}")+
   p("<strong>第二步：</strong>第一项中 $\\frac{d\\mathbf{r}_i'}{dt}=\\mathbf{v}_i'$ 与动量平行，为零。第二项用 $m_i\\ddot{\\mathbf{r}}_i'=m_i\\ddot{\\mathbf{r}}_i-m_i\\ddot{\\mathbf{r}}_C=\\mathbf{F}_i^{\\text{外}}+\\mathbf{F}_i^{\\text{内}}-m_i\\mathbf{a}_C$：")+
   fml("\\frac{d\\mathbf{L}_C}{dt}=\\sum_i\\mathbf{r}_i'\\times\\mathbf{F}_i^{\\text{外}}+\\sum_i\\mathbf{r}_i'\\times\\mathbf{F}_i^{\\text{内}}-\\left(\\sum_i m_i\\mathbf{r}_i'\\right)\\times\\mathbf{a}_C")+
   p("<strong>第三步：</strong>内力矩成对抵消；又由质心定义 $\\sum_i m_i\\mathbf{r}_i'=0$，末项为零，故：")+
   fml("\\frac{d\\mathbf{L}_C}{dt}=\\sum_i\\mathbf{r}_i'\\times\\mathbf{F}_i^{\\text{外}}=M_C^{\\text{外}}")+
   p("这说明质心系虽是平动非惯性系，但对质心的动量矩定理与惯性系中对定点的形式完全相同，可直接使用。") )+
   app(p("当外力对质心的力矩为零时，系统对质心的角动量守恒。自由旋转的物体、舞台演员改变姿态、转台实验等都可用此定理分析，这为研究平动与转动耦合问题提供了便利。"))
 )},
]},
# ---- 3.11 质点系的动能定理与柯尼希定理 ----
{
"name": "3.11 质点系的动能定理与柯尼希定理",
"color": "#ea580c",
"desc": "质点系动能定理、柯尼希定理与参考系选择",
"items": [
{"id":"c3s11-1","name":"质点系动能定理","tags":["thm","der"],"brief":"外力功与内力功之和等于系统动能增量。",
 "body": wrap(
   thm("质点系动能定理",p("系统从状态 1 到状态 2 的过程中，所有外力做功与所有内力做功之和，等于系统动能的增量：")+
   fml("W_{\\text{外}}+W_{\\text{内}}=\\Delta E_k"))+
   der(p("<strong>第一步：</strong>对第 $i$ 个质点应用动能定理 $W_{i\\text{外}}+W_{i\\text{内}}=\\Delta E_{k_i}$。")+
   p("<strong>第二步：</strong>对所有质点求和，外力功与内力功各自累加：")+
   fml("\\sum_i W_{i\\text{外}}+\\sum_i W_{i\\text{内}}=\\sum_i\\Delta E_{k_i}\\implies W_{\\text{外}}+W_{\\text{内}}=\\Delta E_k")+
   p("<strong>第三步（内力的特殊性）：</strong>内力冲量之和为零，但内力做功之和一般不为零，因为相互作用力的两个作用点位移可以不同。对刚体，任意两质点间距离不变，内力做功之和恒为零，故对刚体有：")+
   fml("W_{\\text{外}}=\\Delta E_k\\quad(\\text{刚体})") )+
   app(p("人与地面摩擦、汽车引擎、绳索连接体等问题中，若把引擎、肌肉视为系统内部，则必须计入内力做功；若作为外力处理，则动能变化由外力功与内力功共同决定，二者应保持一致。"))
 )},
{"id":"c3s11-2","name":"柯尼希定理","tags":["thm","der"],"brief":"总动能等于质心动能加相对质心动能。",
 "body": wrap(
   thm("柯尼希定理",p("质点系的总动能，等于质心平动动能与各质点相对质心运动动能之和：")+
   fml("E_k=\\tfrac{1}{2}M v_C^2+\\sum_i\\tfrac{1}{2}m_i v_i'^2=E_{k,c}+E_{k,\\text{rel}}")+
   p("其中 $M=\\sum_i m_i$，$v_C$ 为质心速率，$v_i'$ 为第 $i$ 个质点相对质心的速率。"))+
   der(p("<strong>第一步：</strong>设 $\\mathbf{v}_i=\\mathbf{v}_C+\\mathbf{v}_i'$，代入总动能：")+
   fml("E_k=\\sum_i\\tfrac{1}{2}m_i v_i^2=\\sum_i\\tfrac{1}{2}m_i(\\mathbf{v}_C+\\mathbf{v}_i')\\cdot(\\mathbf{v}_C+\\mathbf{v}_i')")+
   p("<strong>第二步：</strong>展开并整理：")+
   fml("E_k=\\tfrac{1}{2}\\left(\\sum_i m_i\\right)v_C^2+\\mathbf{v}_C\\cdot\\sum_i m_i\\mathbf{v}_i'+\\sum_i\\tfrac{1}{2}m_i v_i'^2")+
   p("<strong>第三步：</strong>中间项 $\\sum_i m_i\\mathbf{v}_i'=M\\mathbf{v}_C'$，而质心系中质心速度 $\\mathbf{v}_C'=0$，故该项为零，得：")+
   fml("E_k=\\tfrac{1}{2}M v_C^2+\\sum_i\\tfrac{1}{2}m_i v_i'^2")+
   p("第一项为质心动能，随参考系改变；第二项为相对质心的内禀动能，与参考系无关。") )+
   exa(p("两体系统的相对质心动能为 $E_{k,\\text{rel}}=\\frac{1}{2}\\mu u^2$（$\\mu$ 为约化质量，$u$ 为相对速度）。碰撞中损失的动能全部来自相对质心动能，而质心动能不变，这正是用质心系分析碰撞与散射的优越之处。"))
 )},
]},
]
# -*- coding: utf-8 -*-
# 第四章 刚体力学 —— ch4_sections
ch4_sections = [
# ---- 4.1 刚体与自由度 ----
{
"name": "4.1 刚体与自由度",
"color": "#0891b2",
"desc": "刚体模型、自由度与刚体内力做功为零",
"items": [
{"id":"c4s1-1","name":"刚体与自由度","tags":["def","thm","der"],"brief":"刚体模型、六个自由度与内力做功之和为零。",
 "fig":"com","figCap":"刚体的质心与内部相互作用",
 "body": wrap(
   defn("刚体",p("在力的作用下，其内部任意两质点间距离都保持不变的质点系，称为<strong>刚体</strong>。它是忽略了形变的理想模型，是质点系的一种特殊情形。"))+
   defn("自由度",p("确定刚体空间位形所需的独立坐标数目称为<strong>自由度</strong>。刚体位置由其质心的 3 个平动坐标（$x,y,z$）与描述姿态的 3 个转动坐标（如欧拉角）确定，故自由刚体共有 6 个自由度。"))+
   thm("刚体内力做功之和为零",p("刚体内部任意一对内力所作功的代数和恒为零，即 $\\sum dW_{\\text{内}}=0$。"))+
   der(
     p("取刚体内任意两质点 $i,j$，二者间沿连线方向作用一对内力 $\\mathbf{F}_{ij}$ 与 $\\mathbf{F}_{ji}$。由牛顿第三定律，$\\mathbf{F}_{ij}=-\\mathbf{F}_{ji}$，且两力都沿 $ij$ 连线方向。")+
     p("在任意微小运动过程中，两质点的位移分别为 $d\\mathbf{r}_i$ 与 $d\\mathbf{r}_j$。由于刚体两质点间的距离保持不变，它们在连线方向的位移投影必然相等：")+
     fml("d\\mathbf{r}_i\\cdot\\hat{\\mathbf{e}}_{ij}=d\\mathbf{r}_j\\cdot\\hat{\\mathbf{e}}_{ij}")+
     p("于是这一对内力所作的元功之和为：")+
     fml("dW_{ij}=\\mathbf{F}_{ij}\\cdot d\\mathbf{r}_i+\\mathbf{F}_{ji}\\cdot d\\mathbf{r}_j=\\mathbf{F}_{ij}\\cdot(d\\mathbf{r}_i-d\\mathbf{r}_j)=0")+
     p("对刚体内所有内力对求和，即得 $\\sum dW_{\\text{内}}=0$。")+
     p("这说明刚体的内力不改变刚体的总动能，因此分析刚体动力学与能量时只需考虑外力及其做功。")+
     app(p("<strong>意义：</strong>刚体动能的改变完全由外力做功决定，这一结论是后面动量矩、动能定理只出现外力量的基础。若物体可变形（如绳、弹簧），内力可做功，能量关系须另作处理。")))
 )},
]},
# ---- 4.2 施于刚体的力系的简化 ----
{
"name": "4.2 施于刚体的力系的简化",
"color": "#06b6d4",
"desc": "滑移矢量、共点力系、平行力系与力系简化方法",
"items": [
{"id":"c4s2-1","name":"力系的简化","tags":["def","thm","der"],"brief":"滑移矢量、共点与平行力系的合成及一般力系的简化。",
 "fig":"fbd","figCap":"作用于刚体的力系",
 "body": wrap(
   defn("滑移矢量",p("作用在刚体上的力，只要大小与方向不变，可沿其作用线滑移到任意位置而不改变对刚体的作用效果。具有这种性质的量称为<strong>滑移矢量</strong>。"))+
   defn("共点力系",p("各力作用线相交于同一点的力系称为<strong>共点力系</strong>（汇交力系），其效果等价于作用于该点的一个合力。"))+
   defn("平行力系",p("各力作用线彼此平行的力系称为<strong>平行力系</strong>，可合成为一个合力。"))+
   thm("力系简化定理",p("任意空间力系一般可简化为作用于任选点 $O$ 的一个合力 $\\mathbf{F}$ 与一个附加力偶矩 $\\mathbf{M}_O$：")+
   fml("\\mathbf{F}=\\sum_i \\mathbf{F}_i,\\qquad \\mathbf{M}_O=\\sum_i \\mathbf{r}_i\\times\\mathbf{F}_i"))+
   der(
     p("<strong>第一步（力偶）：</strong>一对大小相等、方向相反但不共线的力，其合力为零，只对刚体产生转动效应，其力偶矩为")+
     fml("\\mathbf{M}=\\mathbf{r}\\times\\mathbf{F}")+
     p("力偶矩与矩心的选取无关，是一个自由矢量，只取决于力的大小与两力作用线的间距（力偶臂）。")+
     p("<strong>第二步（滑移合理性）：</strong>将作用点沿作用线平移位移 $\\mathbf{r}_{\\parallel}$，因 $\\mathbf{r}_{\\parallel}$ 与 $\\mathbf{F}$ 平行，附加力偶矩 $\\mathbf{r}_{\\parallel}\\times\\mathbf{F}=0$，故作用效果不变。")+
     p("<strong>第三步（平行力系的合力作用点）：</strong>设各力都平行于单位矢量 $\\hat{\\mathbf{e}}$，即 $\\mathbf{F}_i=F_i\\hat{\\mathbf{e}}$，合力 $\\mathbf{F}=\\left(\\sum F_i\\right)\\hat{\\mathbf{e}}$。由合力矩定理 $\\mathbf{r}_C\\times\\mathbf{F}=\\sum_i \\mathbf{r}_i\\times\\mathbf{F}_i$，得合力作用点")+
     fml("\\mathbf{r}_C=\\frac{\\sum_i F_i\\mathbf{r}_i}{\\sum_i F_i}")+
     p("这正是平行力系的合成公式，当力为重力时即为质心（重心）公式。")+
     app(p("<strong>简化方法小结：</strong>① 汇交力系用几何法或解析法合成一个过汇交点的合力；② 平行力系合成为一个合力，作用点由上式确定；③ 一般力系向任一点 $O$ 平移，得合力 $\\mathbf{F}$ 与附加力偶 $\\mathbf{M}_O$；若再满足 $\\mathbf{F}\\cdot\\mathbf{M}_O=0$，则可进一步化为一个单一合力（力螺旋的退化情形）。")))
 )},
]},
# ---- 4.3 刚体的平衡与稳定性·桁架 ----
{
"name": "4.3 刚体的平衡与稳定性·桁架",
"color": "#0e7490",
"desc": "平衡条件、稳定性判据与桁架的节点法、截面法",
"items": [
{"id":"c4s3-1","name":"平衡条件与稳定性","tags":["thm","der","app"],"brief":"合力与合力矩为零，及势能判据。",
 "fig":"inclined","figCap":"刚体在约束下的平衡",
 "body": wrap(
   thm("刚体平衡条件",p("刚体保持平衡（静止或匀速平动且匀速转动）的充要条件是合外力与对任意点的合外力矩同时为零：")+
   fml("\\sum_i \\mathbf{F}_i=0,\\qquad \\sum_i \\mathbf{M}_i=0"))+
   der(
     p("<strong>必要性：</strong>若 $\\sum\\mathbf{F}\\neq0$，由质心运动定理 $\\sum\\mathbf{F}=m\\mathbf{a}_c$，质心必有加速度，刚体不可能保持平衡。")+
     p("若对某点 $O$ 的合外力矩 $\\sum\\mathbf{M}_O\\neq0$，由动量矩定理 $\\sum\\mathbf{M}_O=\\dfrac{d\\mathbf{L}_O}{dt}$，刚体的角动量将发生变化，刚体将转动，同样不能保持平衡。因此平衡必须同时满足两个条件。")+
     p("<strong>充分性：</strong>当 $\\sum\\mathbf{F}=0$ 且 $\\sum\\mathbf{M}_O=0$ 时，$\\mathbf{a}_c=0$，且系统角动量守恒；若初始静止，则永远静止，即为平衡状态。")+
     p("对平面一般力系，上述矢量方程化为三个独立的标量方程：")+
     fml("\\sum F_x=0,\\quad \\sum F_y=0,\\quad \\sum M_{O}=0")+
     p("其中矩心 $O$ 可以任取，选取不同的矩心常常能大幅简化求解。"))+
   thm("平衡稳定性判据",p("在保守力场中，平衡位置由势能取极值给出；稳定性由势能二阶导数判定：")+
     fml("\\frac{dU}{dq}=0\\ (\\text{平衡}),\\quad \\frac{d^2U}{dq^2}>0\\ (\\text{稳定}),\\quad \\frac{d^2U}{dq^2}<0\\ (\\text{不稳定})"))+
   der(
     p("<strong>稳定性推导：</strong>将势能在平衡位置 $q_0$ 附近作泰勒展开（一次项因平衡条件为零）：")+
     fml("U(q)=U(q_0)+\\frac{1}{2}\\left.\\frac{d^2U}{dq^2}\\right|_{q_0}(q-q_0)^2+\\cdots")+
     p("当系统发生微小偏离 $\\delta q=q-q_0$ 时，势能变化 $\\Delta U\\approx\\frac{1}{2}U''(q_0)\\,\\delta q^2$。若 $U''(q_0)>0$，偏离使势能增加，系统受到指向平衡位置的恢复力，偏离后被拉回，故为<strong>稳定平衡</strong>。")+
     p("若 $U''(q_0)<0$，偏离使势能减小，系统远离平衡位置，为<strong>不稳定平衡</strong>。几何上即：重心最低（势能极小）是稳定平衡。")+
     app(p("不倒翁、悬挂的钟摆（势能极小）是稳定平衡；倒立的杆、放在凸面上的球（势能极大）是不稳定平衡。工程上通过降低重心提高稳定性。")))
 )},
{"id":"c4s3-2","name":"桁架：节点法与截面法","tags":["def","thm","der","exa"],"brief":"理想桁架的内力分析方法。",
 "body": wrap(
   defn("桁架",p("由若干直杆在两端用铰链连接、且几何形状不变的杆系结构，称为<strong>桁架</strong>。理想桁架中各杆只受两端铰链的力，称为二力杆，杆内力沿杆轴方向。"))+
   thm("节点法与截面法",p("<strong>节点法：</strong>逐个取节点为隔离体，由汇交力系平衡 $\\sum F_x=0,\\ \\sum F_y=0$ 求各杆内力。<br><strong>截面法：</strong>用假想截面把桁架截为两部分，取其一为隔离体，由平面力系平衡求被截杆件的内力。"))+
   der(
     p("<strong>节点法步骤：</strong>理想桁架每个节点受到汇聚于该节点的各杆内力及可能的支座反力，构成一个平面汇交力系，可列出 2 个平衡方程。对 $n$ 个节点共可列出 $2n$ 个方程，恰好求解静定桁架的全部杆内力。")+
     p("第一步：先对整体用 $\\sum F_x=0,\\ \\sum F_y=0,\\ \\sum M=0$ 求出支座反力。")+
     p("第二步：从只含两根未知内力的节点入手，逐点写出 $\\sum F_x=0,\\ \\sum F_y=0$ 求解，再转向下一个节点。")+
     p("<strong>截面法步骤：</strong>当只需少数几根杆的内力时，用一个截面切开至多三根待求杆，把被切杆内力当作外力加在所取部分上，由平衡方程直接解出目标杆内力：")+
     fml("\\sum M_O=0\\ \\Rightarrow\\ \\text{直接解出 }F_{\\text{目标}}")+
     p("截面法的优点是不必逐节点求解，可以一步得到所需杆的内力。")+
     exa(p("<strong>零力杆：</strong>若某节点只连接两根杆且节点上没有外力作用，则该两杆均为零力杆（内力为零）。识别并删去零力杆可以显著简化计算。这也说明桁架中存在不承担载荷的杆件。")))
 )},
]},
# ---- 4.4 刚体的平动 ----
{
"name": "4.4 刚体的平动",
"color": "#155e75",
"desc": "平动刚体的运动学与动力学，可简化为质点",
"items": [
{"id":"c4s4-1","name":"刚体的平动","tags":["def","thm","der","app"],"brief":"平动刚体各点运动相同，可取质心等效。",
 "body": wrap(
   defn("平动",p("刚体运动时，其上任意两点连线的方向在空间中始终保持不变，这种运动称为<strong>平动</strong>（平移）。平动可以是直线运动，也可以是曲线运动。"))+
   thm("平动刚体可视为质点",p("刚体作平动时，各点的位移、速度、加速度完全相同，其动力学可归结为质心的质点问题：")+
   fml("\\mathbf{a}_i=\\mathbf{a}_c=\\frac{\\sum\\mathbf{F}}{m}"))+
   der(
     p("<strong>运动学推导：</strong>取刚体上任意两点 $A,B$，其位矢满足 $\\mathbf{r}_A=\\mathbf{r}_B+\\mathbf{r}_{AB}$。平动时矢量 $\\mathbf{r}_{AB}$ 的大小与方向都不随时间变化，故 $\\dfrac{d\\mathbf{r}_{AB}}{dt}=0$。")+
     p("对时间求导即得 $\\mathbf{v}_A=\\mathbf{v}_B$；再求导得 $\\mathbf{a}_A=\\mathbf{a}_B$。可见平动刚体上所有点的运动状态完全一致。")+
     p("<strong>动力学推导：</strong>由质心运动定理 $\\sum\\mathbf{F}=m\\mathbf{a}_c$，而 $\\mathbf{a}_i=\\mathbf{a}_c$，所以各点产生相同的加速度。因此平动刚体的运动学与动力学都等价于一个质量为 $m$、位于质心的质点。")+
     app(p("<strong>例：</strong>沿直线滑行的滑块、电梯的升降、平动的车厢，都可直接当作质点分析。若刚体既平动又绕质心转动（如掷出的飞盘、转体的人体），则须分解为质心平动与绕质心转动两部分分别处理。")))
 )},
]},
# ---- 4.5 刚体的定轴转动 ----
{
"name": "4.5 刚体的定轴转动（运动学与动力学基本方程）",
"color": "#0d9488",
"desc": "角量描述、线量与角量关系及转动定律",
"items": [
{"id":"c4s5-1","name":"定轴转动的运动学","tags":["def","der","app"],"brief":"角速度、角加速度及线量与角量的关系。",
 "fig":"rotation","figCap":"刚体绕定轴转动",
 "body": wrap(
   defn("定轴转动与角量",p("刚体绕一条固定不动的直线——转轴转动，称为<strong>定轴转动</strong>。用角量描述：角坐标 $\\theta$、角速度 $\\omega=\\dot\\theta$、角加速度 $\\alpha=\\dot\\omega=\\ddot\\theta$。"))+
   der(
     p("<strong>线量与角量关系：</strong>距转轴 $r$ 处的质元作半径为 $r$ 的圆周运动。弧长与角位移的关系为 $s=r\\theta$，对时间求导得线速度：")+
     fml("v=\\frac{ds}{dt}=r\\frac{d\\theta}{dt}=r\\omega")+
     p("再对时间求导得切向加速度（改变速率大小）：")+
     fml("a_t=\\frac{dv}{dt}=r\\alpha")+
     p("同时速度方向不断改变，产生法向（向心）加速度：")+
     fml("a_n=\\frac{v^2}{r}=r\\omega^2")+
     p("因此距轴 $r$ 处质元的总加速度大小为")+
     fml("a=\\sqrt{a_t^2+a_n^2}=r\\sqrt{\\alpha^2+\\omega^4}")+
     p("其方向与半径的夹角为 $\\arctan(a_t/a_n)=\\arctan(\\alpha/\\omega^2)$。")+
     app(p("<strong>匀角加速转动：</strong>当 $\\alpha=$ 常量时，角量公式与匀加速直线运动一一对应：")+
     fml("\\omega=\\omega_0+\\alpha t,\\quad \\theta=\\omega_0 t+\\frac{1}{2}\\alpha t^2,\\quad \\omega^2=\\omega_0^2+2\\alpha\\theta")))
 )},
{"id":"c4s5-2","name":"转动定律","tags":["def","thm","der","app"],"brief":"力矩、转动惯量与角加速度的关系 M=Jα。",
 "body": wrap(
   defn("力矩",p("力 $\\mathbf{F}$ 对转轴的<strong>力矩</strong>等于力的作用点相对轴的位矢与力的矢量积：")+
   fml("\\mathbf{M}=\\mathbf{r}\\times\\mathbf{F},\\qquad M=rF\\sin\\theta"))+
   thm("转动定律",p("刚体绕定轴转动时，作用在刚体上的合外力矩等于转动惯量与角加速度之积：")+
   fml("M=J\\alpha"))+
   der(
     p("<strong>推导：</strong>把刚体视为质点系。第 $i$ 个质元受外力 $\\mathbf{F}_i$，其沿切向的分量提供切向加速度 $a_{it}=r_i\\alpha$：")+
     fml("F_{it}=m_i r_i\\alpha")+
     p("该切向力对转轴的力矩为 $M_i=r_i F_{it}=m_i r_i^2\\alpha$。对全部质元求和，内力矩因成对出现、大小相等方向相反而互相抵消，只剩外力矩：")+
     fml("M=\\sum_i M_i=\\left(\\sum_i m_i r_i^2\\right)\\alpha=J\\alpha")+
     p("其中 $J=\\sum_i m_i r_i^2$ 为刚体对该轴的转动惯量。写成矢量形式即")+
     fml("\\mathbf{M}=J\\boldsymbol{\\alpha}")+
     app(p("<strong>对应关系：</strong>转动定律与平动的牛顿第二定律 $F=ma$ 完全对应：力矩对应力，转动惯量对应质量，角加速度对应加速度。转动惯量是刚体转动惯性大小的量度，转轴不同则 $J$ 不同。")))
 )},
]},
# ---- 4.6 转动惯量的计算·惯量张量与惯量主轴 ----
{
"name": "4.6 转动惯量的计算·惯量张量与惯量主轴",
"color": "#14b8a6",
"desc": "转动惯量定义、平行轴与垂直轴定理、惯量张量与主轴",
"items": [
{"id":"c4s6-1","name":"转动惯量与轴定理","tags":["def","thm","der","exa","app"],"brief":"转动惯量的定义与计算，平行轴、垂直轴定理。",
 "fig":"inertia_shapes","figCap":"常见刚体对典型轴的转动惯量",
 "body": wrap(
   defn("转动惯量",p("刚体对某定轴的<strong>转动惯量</strong>定义为各质元质量与其到该轴距离平方乘积之和：")+
   fml("J=\\sum_i m_i r_i^2=\\int r^2\\,dm"))+
   thm("平行轴定理",p("设 $J_c$ 为刚体对过质心的轴的转动惯量，则对与该轴平行且相距 $d$ 的另一轴的转动惯量为：")+
   fml("J=J_c+md^2"))+
   thm("垂直轴定理",p("对厚度可忽略的薄板，若 $x,y$ 轴在板面内、$z$ 轴垂直于板面且三轴交于同一点，则：")+
   fml("J_z=J_x+J_y"))+
   der(
     p("<strong>平行轴定理推导：</strong>取质心为原点，质心轴为 $z_c$，平行轴 $z$ 与 $z_c$ 相距 $d$。质元 $(x_i',y_i')$ 到 $z$ 轴的距离平方为")+
     fml("r_i^2=(x_i'+d)^2+y_i'^2=r_i'^2+2d x_i'+d^2")+
     p("乘以质量并求和，利用质心系中 $\\sum m_i x_i'=0$：")+
     fml("J=\\sum m_i r_i^2=\\sum m_i r_i'^2+2d\\sum m_i x_i'+d^2\\sum m_i=J_c+md^2")+
     p("<strong>垂直轴定理推导：</strong>薄板中质元 $(x_i,y_i)$ 到 $x,y,z$ 三轴的距离平方分别为 $y_i^2,\\ x_i^2,\\ x_i^2+y_i^2$，故")+
     fml("J_z=\\sum m_i(x_i^2+y_i^2)=\\sum m_i x_i^2+\\sum m_i y_i^2=J_x+J_y"))+
   exa(p("<strong>圆盘对中心轴的转动惯量：</strong>质量 $m$、半径 $R$，面密度 $\\sigma=m/(\\pi R^2)$。取半径 $r$、宽 $dr$ 的细圆环，$dm=\\sigma\\cdot 2\\pi r\\,dr$：")+
     fml("J=\\int_0^R r^2\\sigma 2\\pi r\\,dr=2\\pi\\sigma\\frac{R^4}{4}=\\frac{1}{2}\\sigma\\pi R^4=\\frac{1}{2}mR^2")+
     p("由垂直轴定理，圆盘对直径轴的转动惯量 $J_x=J_y=\\frac{1}{2}J_z=\\frac{1}{4}mR^2$。")+
     app(p("<strong>常用结果：</strong>细杆过中心轴 $\\frac{1}{12}mL^2$、过端点轴 $\\frac{1}{3}mL^2$；圆环 $mR^2$；圆盘/圆柱 $\\frac{1}{2}mR^2$；实心球 $\\frac{2}{5}mR^2$；薄球壳 $\\frac{2}{3}mR^2$。组合体的转动惯量等于各部分对同一轴的转动惯量之和。")))
 )},
{"id":"c4s6-2","name":"惯量张量与惯量主轴","tags":["def","der","app"],"brief":"一般转轴的惯量张量描述与对角化求得主轴。",
 "body": wrap(
   defn("惯量张量",p("对一般取向的转轴，刚体的转动惯量由<strong>惯量张量</strong> $\\mathbf{J}$ 描述，其分量为：")+
   fml("J_{xx}=\\int(y^2+z^2)\\,dm,\\qquad J_{xy}=-\\int xy\\,dm,\\qquad \\cdots"))+
   der(
     p("角动量与角速度的关系为 $\\mathbf{L}=\\mathbf{J}\\boldsymbol{\\omega}$，其中 $\\mathbf{J}$ 是对称的 3×3 惯量张量。展开为：")+
     fml("\\mathbf{L}=\\begin{pmatrix} J_{xx} & J_{xy} & J_{xz} \\\\ J_{yx} & J_{yy} & J_{yz} \\\\ J_{zx} & J_{zy} & J_{zz} \\end{pmatrix}\\begin{pmatrix} \\omega_x \\\\ \\omega_y \\\\ \\omega_z \\end{pmatrix}")+
     p("对角元 $J_{xx}=\\int(y^2+z^2)dm$ 是绕坐标轴的转动惯量；非对角元（惯量积）$J_{xy}=-\\int xy\\,dm$ 反映质量分布相对于坐标面的不对称性。")+
     p("由于 $\\mathbf{J}$ 是实对称矩阵，必可通过一次正交变换（即选取合适的坐标轴）将其对角化，使所有惯量积为零：")+
     fml("\\mathbf{J}'=\\mathrm{diag}(J_1,J_2,J_3)")+
     p("使惯量积为零的三个互相垂直的特征方向称为<strong>惯量主轴</strong>，对应的 $J_1,J_2,J_3$ 称为主转动惯量。在主轴坐标系中角动量与角速度平行：")+
     fml("\\mathbf{L}=J\\boldsymbol{\\omega}")+
     app(p("<strong>对称性与主轴：</strong>具有对称性的物体，其对称轴就是惯量主轴。例如均质长方体的三条棱方向、圆柱的轴与其任意两条直径方向都是主轴。因此在主轴系中描述刚体转动最为简洁，欧拉动力学方程正是建立在主轴坐标系中。")))
 )},
]},
# ---- 4.7 刚体定轴转动的能量、约束反力与动平衡 ----
{
"name": "4.7 刚体定轴转动的能量、约束反力与动平衡",
"color": "#22d3ee",
"desc": "转动动能定理、轴上的约束反力与动平衡条件",
"items": [
{"id":"c4s7-1","name":"转动的动能定理","tags":["thm","der","app"],"brief":"转动动能与力矩做功的动能定理。",
 "body": wrap(
   thm("转动动能定理",p("刚体绕定轴转动的动能为 $E_k=\\frac{1}{2}J\\omega^2$；合外力矩的功等于转动动能的增量：")+
   fml("W=\\int_{\\theta_1}^{\\theta_2}M\\,d\\theta=\\frac{1}{2}J\\omega_2^2-\\frac{1}{2}J\\omega_1^2"))+
   der(
     p("<strong>动能表达式推导：</strong>把刚体分解为质元，第 $i$ 个质元速率为 $v_i=r_i\\omega$，其动能为 $\\frac{1}{2}m_i v_i^2=\\frac{1}{2}m_i r_i^2\\omega^2$。求和得")+
     fml("E_k=\\sum_i \\frac{1}{2}m_i r_i^2\\omega^2=\\frac{1}{2}\\left(\\sum_i m_i r_i^2\\right)\\omega^2=\\frac{1}{2}J\\omega^2")+
     p("<strong>动能定理推导：</strong>力矩 $M$ 使刚体转过 $d\\theta$，元功为 $dW=M\\,d\\theta$。由动能定理 $dW=dE_k$，即")+
     fml("M\\,d\\theta=J\\omega\\,d\\omega")+
     p("两端对时间积分即得动能定理的积分形式。相反，若把 $M\\,d\\theta=J\\omega d\\omega$ 两边对时间求导，$M\\omega=J\\omega\\alpha$，即回到转动定律 $M=J\\alpha$，可见二者是一致的。")+
     app(p("<strong>复摆（物理摆）：</strong>将转动定律与能量结合，$\\frac{1}{2}J\\dot\\theta^2+mgl(1-\\cos\\theta)=E$。小角度时 $\\ddot\\theta+\\dfrac{mgl}{J}\\theta=0$，作简谐振动，周期 $T=2\\pi\\sqrt{\\dfrac{J}{mgl}}$，其中 $l$ 为质心到轴的距离。")))
 )},
{"id":"c4s7-2","name":"约束反力与动平衡","tags":["def","der","app"],"brief":"转动轴上的静反力与动反力，动平衡条件。",
 "body": wrap(
   defn("约束反力",p("刚体作定轴转动时，转轴对刚体的约束反力包含两部分：由重力等静载荷引起的<strong>静反力</strong>，以及由转动惯性力引起的<strong>动反力</strong>。"))+
   der(
     p("<strong>动反力推导：</strong>取轴上某支承为原点，质元 $i$ 的惯性力为 $-m_i\\mathbf{a}_i$。其切向分量由角加速度产生，法向分量 $-m_i r_i\\omega^2\\hat{\\mathbf{r}}_i$ 指向轴。轴承受的附加动反力为这些惯性力的合力：")+
     fml("\\mathbf{N}_{\\text{动}}=-\\sum_i m_i\\mathbf{a}_i")+
     p("即使刚体匀速转动（$\\alpha=0$），法向惯性力依然存在，会使轴承受周期性反力，从而引起振动和磨损。")+
     p("<strong>动平衡条件：</strong>若刚体的惯量主轴与转轴重合，即质心落在轴上且质量分布关于转轴对称，则各质元的惯性力对轴的横向合力与力矩均为零，动反力消失：")+
     fml("\\sum_i m_i\\mathbf{r}_i=0,\\qquad J_{xy}=J_{xz}=0")+
     p("满足上述条件的转动称为<strong>动平衡</strong>，此时转轴即为惯量主轴。")+
     app(p("<strong>应用：</strong>汽轮机转子、电机转子、车轮等高速旋转部件必须进行动平衡，否则交变惯性力会引起强烈振动甚至破坏。工程上通过在高转速下配重，使转轴穿过质心并成为惯量主轴。磨床、离心机的精平衡也基于同一原理。")))
 )},
]},
# ---- 4.8 刚体的平面平行运动与滚动摩擦 ----
{
"name": "4.8 刚体的平面平行运动与滚动摩擦",
"color": "#164e63",
"desc": "平面运动的分解、瞬心法与滚动摩擦",
"items": [
{"id":"c4s8-1","name":"平面平行运动与瞬心","tags":["def","thm","der","exa"],"brief":"平面运动的速度分解、瞬心与动力学方程。",
 "fig":"inclined","figCap":"斜面滚动的刚体",
 "body": wrap(
   defn("平面平行运动",p("刚体运动时，其上各点都在平行于某一固定平面的平面内运动，称为<strong>平面平行运动</strong>（平面运动），可分解为随基点的平动和绕基点的转动。"))+
   thm("速度分解与瞬心",p("取刚体上基点 $A$，任一点 $B$ 的速度为：")+
   fml("\\mathbf{v}_B=\\mathbf{v}_A+\\boldsymbol{\\omega}\\times\\mathbf{r}_{AB}")+
   p("其中角速度 $\\boldsymbol{\\omega}$ 与基点的选择无关。瞬时速度为零的点称为<strong>瞬时转动中心</strong>（瞬心 $P$），该瞬时刚体可看作绕瞬心作纯转动。"))+
   der(
     p("<strong>瞬心的确定：</strong>已知刚体上两点 $A,B$ 的速度方向，过两点分别作速度方向的垂线，其交点即为瞬心 $P$。此时 $v_A=\\omega\\cdot PA$、$v_B=\\omega\\cdot PB$，暂态几何关系由此确定角速度。")+
     p("<strong>动力学方程：</strong>平面运动由两条方程完整描述——质心运动定理与绕质心的转动定律：")+
     fml("\\sum\\mathbf{F}=m\\mathbf{a}_c,\\qquad \\sum\\mathbf{M}_c=J_c\\boldsymbol{\\alpha}")+
     p("<strong>质心加速度 $\\mathbf{a}_c$：</strong>由 $\\mathbf{a}_c=\\sum\\mathbf{F}/m$ 直接求得。求刚体上某点 $B$ 的加速度时用")+
     fml("\\mathbf{a}_B=\\mathbf{a}_A+\\boldsymbol{\\alpha}\\times\\mathbf{r}_{AB}-\\omega^2\\mathbf{r}_{AB}")+
     p("<strong>角加速度方程：</strong>对质心取矩得 $\\sum\\mathbf{M}_c=J_c\\alpha$。若瞬心到质心的距离在该瞬时保持不变，也可对瞬心取矩，形式仍为 $M_P=J_P\\alpha$。")+
     exa(p("<strong>圆柱沿斜面纯滚动：</strong>设静摩擦力为 $f$，由平动方程 $mg\\sin\\theta-f=ma$、绕质心方程 $fR=J_c\\alpha=\\frac{1}{2}mR^2\\alpha$ 及纯滚动条件 $a=R\\alpha$，联立解得")+
     fml("a=\\frac{g\\sin\\theta}{1+J_c/(mR^2)}=\\frac{2}{3}g\\sin\\theta")+
     p("其中 $J_c/(mR^2)$ 的数值决定了滚动物体下滑加速度的大小。")))
 )},
{"id":"c4s8-2","name":"滚动摩擦","tags":["def","der","app"],"brief":"滚动摩擦力偶矩的成因、纯滚动能量与滚滑比较。",
 "fig":"rolling","figCap":"圆轮在水平面上的滚动",
 "body": wrap(
   defn("滚动摩擦",p("刚体在面上滚动时，因接触面发生形变，法向反力的作用点向前方偏移，形成一个阻碍滚动的力偶矩，称为<strong>滚动摩擦力偶矩</strong>：")+
   fml("M_f=\\mu_r N"))+
   der(
     p("其中 $\\mu_r$ 为滚动摩擦系数，量纲为长度；$N$ 为法向正压力。可见滚动阻力在本质上是力偶而非力，其效果是阻碍滚动的发生。")+
     p("使圆轮匀速滚动所需施加的水平拉力 $F$，满足其力矩与滚动阻力矩平衡 $F\\cdot R=\\mu_r N$，于是")+
     fml("F=\\frac{\\mu_r}{R}N\\ll \\mu_k N")+
     p("<strong>纯滚动与能量：</strong>纯滚动（无滑滚动）时接触点速度为零，静摩擦力不做功，只提供使刚体转动所需的力矩，故机械能守恒。半径 $R$ 的圆轮滚下高度 $h$ 后：")+
     fml("mgh=\\frac{1}{2}mv_c^2+\\frac{1}{2}J_c\\omega^2,\\qquad v_c=R\\omega")+
     p("<strong>滚滑条件：</strong>静摩擦力不超过最大静摩擦，$f\\le\\mu_s N$。若所需摩擦力超过此限，则轮子发生打滑，既有滚动又有滑动，此时滑动摩擦力做功使机械能减少。")+
     app(p("<strong>应用：</strong>因为 $\\mu_r\\ll\\mu_s$，滚动摩擦远小于滑动摩擦，这正是轮子、滚珠轴承被广泛采用的原因——用滚动代替滑动能大幅降低阻力，提高机械效率。")))
 )},
]},
# ---- 4.9 刚体的定点运动 ----
{
"name": "4.9 刚体的定点运动（欧拉情形、对称重刚体、回转仪）",
"color": "#0e7490",
"desc": "无外力矩的欧拉情形、对称重刚体的进动与章动、陀螺仪",
"items": [
{"id":"c4s9-1","name":"无外力矩的欧拉情形","tags":["def","thm","der","app"],"brief":"自由转动的欧拉动力学方程与稳定性。",
 "body": wrap(
   defn("欧拉情形",p("刚体绕固定点 $O$ 转动、且对 $O$ 点的外力矩为零，这种自由转动称为<strong>欧拉情形</strong>。此时刚体对 $O$ 点的动量矩守恒，$\\mathbf{L}=\\text{const}$。"))+
   thm("欧拉动力学方程",p("在随刚体转动的惯量主轴坐标系中，欧拉方程为：")+
   fml("\\begin{cases} J_1\\dot\\omega_1+(J_3-J_2)\\omega_2\\omega_3=M_1 \\\\ J_2\\dot\\omega_2+(J_1-J_3)\\omega_3\\omega_1=M_2 \\\\ J_3\\dot\\omega_3+(J_2-J_1)\\omega_1\\omega_2=M_3 \\end{cases}"))+
   der(
     p("<strong>推导：</strong>在惯性系中 $\\mathbf{L}$ 大小方向都不变，即 $\\dfrac{d\\mathbf{L}}{dt}\\Big|_{\\text{惯}}=\\mathbf{M}=0$。但刚体转动时惯量主轴随之转动，故在主轴（体坐标系）中 $\\mathbf{L}=\\mathbf{J}\\boldsymbol{\\omega}$ 的分量会变化。")+
     p("利用矢量在惯性系与体坐标系中导数的变换关系")+
     fml("\\frac{d\\mathbf{L}}{dt}\\Big|_{\\text{惯}}=\\frac{d\\mathbf{L}}{dt}\\Big|_{\\text{体}}+\\boldsymbol{\\omega}\\times\\mathbf{L}")+
     p("令外矩 $\\mathbf{M}=0$，并把 $\\mathbf{L}=\\mathbf{J}\\boldsymbol{\\omega}$ 在主轴分量 $L_i=J_i\\omega_i$ 代入上式，即得欧拉动力学方程。")+
     p("<strong>稳定性：</strong>当 $J_1=J_2=J_3$（球对称）时 $\\boldsymbol{\\omega}$ 恒定，刚体作匀速转动；当 $J_1=J_2\\ne J_3$（旋转对称）时，自由转动绕对称轴（最大或最小惯量轴）稳定，绕中间惯量轴则不稳定。")+
     app(p("<strong>网球拍定理（中间轴定理）：</strong>绕最大和最小主转动惯量轴的自由转动是稳定的，而绕中间轴的自由转动不稳定，会发生周期性翻转。这一现象在航天器姿态控制与日常生活中（抛接的网球拍、旋转的书本）都能观察到。")))
 )},
{"id":"c4s9-2","name":"对称重刚体与回转仪","tags":["def","der","app"],"brief":"旋转对称重刚体的欧拉角描述、进动章动与陀螺仪。",
 "body": wrap(
   defn("对称重刚体",p("旋转对称刚体（$J_1=J_2=J_\\perp$，$J_3=J_\\parallel$）在重力作用下绕固定点运动，称为<strong>对称重刚体</strong>（拉格朗日–泊松情形），是最常见的陀螺模型。"))+
   der(
     p("<strong>欧拉角描述：</strong>取对称轴为 $z_3$，用欧拉角 $(\\phi,\\theta,\\psi)$ 描述：$\\phi$ 为进动角、$\\theta$ 为章动角、$\\psi$ 为自转角。")+
     p("<strong>两个守恒量：</strong>重力矩只绕水平轴作用，故对铅直方向的分量守恒；又对称轴上无重力矩分量，自转角动量守恒：")+
     fml("J_3(\\dot\\psi+\\dot\\phi\\cos\\theta)=L_3=\\text{const},\\qquad \\omega_3=\\dot\\psi+\\dot\\phi\\cos\\theta")+
     p("再加上机械能守恒，即得章动方程。$\\theta$ 在两个上下限之间周期性往复，表现为对称轴在圆锥面上作<strong>章动</strong>。")+
     p("<strong>快陀螺进动：</strong>当自转很快时，近似地 $\\mathbf{L}\\approx J_3\\omega_3\\hat{\\mathbf{z}}_3$，由 $\\mathbf{M}=\\boldsymbol{\\Omega}\\times\\mathbf{L}$ 解出进动角速度：")+
     fml("\\Omega_{\\text{进}}=\\frac{M}{J_3\\omega_3}=\\frac{mgl}{J_3\\omega_3}")+
     p("其中 $M=mgl\\sin\\theta$ 为重力对支点的力矩。外矩越大或自转越慢，进动越快。")+
     app(p("<strong>回转仪（陀螺仪）：</strong>高速自转的转子在受外力矩时，其轴按 $\\mathbf{M}=\\boldsymbol{\\Omega}\\times\\mathbf{L}$ 进动，而不是顺着力矩方向倾倒。这一特性使其能抵抗转轴方向的改变，因而被用于惯性导航、稳定平台、陀螺罗盘和炮弹的旋转稳定；自行车、陀螺保持直立也是同一道理。")))
 )},
]},
]
ch5_sections = [
# ---- 5.1 一个自由度的谐振动 ----
{
"name": "5.1 一个自由度的谐振动",
"color": "#be185d",
"desc": "简谐振动微分方程与解、能量、旋转矢量法与单摆复摆",
"items": [
{"id":"c5s1-1","name":"简谐振动微分方程与解","tags":["def","der","exa"],"brief":"由回复力导出简谐振动方程与初始条件公式。",
 "fig":"shm","figCap":"简谐振动的位移-时间曲线",
 "body": wrap(
   defn("简谐振动",p("质点所受合外力总与位移成正比、方向相反，即 $F=-kx$，这种振动称为<strong>简谐振动</strong>（SHM）。")+
   fml("F=-kx"))+
   der(p("取 x 轴沿振动方向、原点取在平衡位置，由牛顿第二定律 $F=ma=m\\ddot{x}$ 有：")+
   fml("m\\frac{d^2x}{dt^2}=-kx")+
   p("两边除以 m，令 $\\omega^2=k/m$，得其标准形式——二阶常系数线性齐次方程：")+
   fml("\\frac{d^2x}{dt^2}+\\omega^2 x=0,\\qquad \\omega=\\sqrt{\\frac{k}{m}}")+
   p("其特征方程为 $r^2+\\omega^2=0$，特征根 $r=\\pm i\\omega$。由线性微分方程理论，通解是两个线性无关解的叠加：")+
   fml("x=C_1\\cos\\omega t+C_2\\sin\\omega t")+
   p("令 $C_1=A\\cos\\varphi$、$C_2=-A\\sin\\varphi$，把上式合成为单一余弦项：")+
   fml("x=A\\cos(\\omega t+\\varphi)")+
   p("其中振幅 $A=\\sqrt{C_1^2+C_2^2}$、初相 $\\varphi$ 由初始条件 $x(0)=x_0$、$v(0)=v_0$ 确定：")+
   fml("A=\\sqrt{x_0^2+\\left(\\frac{v_0}{\\omega}\\right)^2},\\qquad \\tan\\varphi=-\\frac{v_0}{\\omega x_0}")+
   p("周期与频率只由系统参数决定：$T=\\frac{2\\pi}{\\omega}=2\\pi\\sqrt{\\frac{m}{k}}$、$f=1/T$，故简谐振动是等时的，与振幅无关。"))+
   exa(p("弹簧振子 $m=0.1\\,\\text{kg}$、$k=10\\,\\text{N/m}$，则 $\\omega=\\sqrt{k/m}=10\\,\\text{rad/s}$，$T=2\\pi/\\omega\\approx0.628\\,\\text{s}$。"))
 )},
{"id":"c5s1-2","name":"简谐振动的能量与旋转矢量法","tags":["thm","der","exa"],"brief":"机械能守恒与相量投影的等价性。",
 "fig":"phasor","figCap":"旋转矢量（相量）在 x 轴上的投影即为振动位移",
 "body": wrap(
   thm("简谐振动的能量",p("动能与势能随时间交替变化，总机械能守恒：")+
   fml("E=E_k+E_p=\\tfrac{1}{2}kA^2=\\text{const}"))+
   der(p("<strong>（1）能量推导。</strong>由 $v=\\dot{x}=-A\\omega\\sin(\\omega t+\\varphi)$，动能：")+
   fml("E_k=\\tfrac{1}{2}mv^2=\\tfrac{1}{2}mA^2\\omega^2\\sin^2(\\omega t+\\varphi)=\\tfrac{1}{2}kA^2\\sin^2(\\omega t+\\varphi)")+
   p("势能 $E_p=\\tfrac{1}{2}kx^2=\\tfrac{1}{2}kA^2\\cos^2(\\omega t+\\varphi)$，两式相加并用 $m\\omega^2=k$：")+
   fml("E=\\tfrac{1}{2}kA^2[\\sin^2(\\omega t+\\varphi)+\\cos^2(\\omega t+\\varphi)]=\\tfrac{1}{2}kA^2")+
   p("<strong>（2）旋转矢量（相量）法。</strong>自原点作长 $A$ 的矢量 $\\mathbf{A}$，以角速度 $\\omega$ 逆时针匀速转动，$t=0$ 时与 $x$ 轴成角 $\\varphi$。$t$ 时刻它与 $x$ 轴夹角为 $\\omega t+\\varphi$，其 x 投影为：")+
   fml("x=A\\cos(\\omega t+\\varphi)")+
   p("矢量端点做半径 A 的匀速圆周运动，线速度 $\\omega A$ 沿切向，其 x 分量 $v_x=-\\omega A\\sin(\\omega t+\\varphi)$ 恰为振动速度；向心加速度 $\\omega^2A$ 的 x 分量为 $-\\omega^2A\\cos(\\omega t+\\varphi)=-\\omega^2x$，恰好给出振动微分方程。"))+
   exa(p("用相量法合成 $x_1=3\\cos\\omega t$ 与 $x_2=4\\cos(\\omega t+\\pi/2)$：两矢量互相垂直，$A=\\sqrt{3^2+4^2}=5$，$\\tan\\varphi=4/3$，故 $x=5\\cos(\\omega t+53.1^\\circ)$。"))+
   note(p("旋转矢量法把三角恒等运算化为矢量合成，是分析相位差、振动合成与干涉的简便工具。"))
 )},
{"id":"c5s1-3","name":"单摆与复摆","tags":["thm","der","app"],"brief":"小角近似下单摆、复摆的周期公式。",
 "fig":"pendulum","figCap":"单摆的切向回复力分析",
 "body": wrap(
   thm("单摆周期",p("摆长 $l$、摆球质量 $m$ 的单摆，在小角近似下做简谐振动，周期为：")+
   fml("T=2\\pi\\sqrt{\\frac{l}{g}}"))+
   der(p("摆球受重力与绳张力，切向回复力 $F_t=-mg\\sin\\theta$，切向加速度 $a_t=l\\ddot{\\theta}$，由牛顿第二定律：")+
   fml("ml\\frac{d^2\\theta}{dt^2}=-mg\\sin\\theta")+
   p("约去 m、l 得 $\\ddot{\\theta}+\\frac{g}{l}\\sin\\theta=0$；当 $\\theta\\ll1$ 时 $\\sin\\theta\\approx\\theta$，方程线性化为简谐振动方程：")+
   fml("\\ddot{\\theta}+\\frac{g}{l}\\theta=0\\ \\Rightarrow\\ \\omega=\\sqrt{\\frac{g}{l}},\\quad T=\\frac{2\\pi}{\\omega}=2\\pi\\sqrt{\\frac{l}{g}}")+
   p("可见周期只由 l 与 g 决定，与摆球质量和（小角）振幅无关，这正是单摆测重力加速度的原理。"))+
   thm("复摆周期",p("质量为 $m$、绕固定水平轴转动的刚体，转轴到质心距离为 $d$、对轴转动惯量为 $I$，小角摆动周期为：")+
   fml("T=2\\pi\\sqrt{\\frac{I}{mgd}}"))+
   der(p("重力作用线到转轴的距离为 $d\\sin\\theta$，重力矩 $M=-mgd\\sin\\theta$；由转动定律 $M=I\\ddot{\\theta}$：")+
   fml("I\\ddot{\\theta}=-mgd\\sin\\theta")+
   p("在小角近似 $\\sin\\theta\\approx\\theta$ 下化为 $\\ddot{\\theta}+\\frac{mgd}{I}\\theta=0$，故 $\\omega=\\sqrt{mgd/I}$、$T=2\\pi\\sqrt{I/(mgd)}$。")+
   p("定义等效摆长 $L=I/(md)$，则复摆与摆长为 L 的单摆等价。由平行轴定理 $I=I_C+md^2$ 得 $T=2\\pi\\sqrt{(I_C+md^2)/(mgd)}$，微调 $d$ 使周期极小即为可逆摆测 g 的原理。"))+
   app(p("单摆与复摆是测定重力加速度的标准装置；复摆模型还用于分析摆钟、地震仪摆系与刚体转动惯量的实验测量。"))
 )},
]},
# ---- 5.2 阻尼振动 ----
{
"name": "5.2 阻尼振动",
"color": "#db2777",
"desc": "阻尼振动方程、欠阻尼衰减规律与三种阻尼状态",
"items": [
{"id":"c5s2-1","name":"阻尼振动方程与欠阻尼衰减","tags":["thm","der","exa"],"brief":"存在粘滞阻力时的运动方程与指数衰减解。",
 "body": wrap(
   thm("阻尼振动方程",p("振子在正比于速度的阻尼力 $f=-\\gamma\\dot{x}$ 作用下，运动方程为：")+
   fml("m\\ddot{x}+\\gamma\\dot{x}+kx=0"))+
   der(p("令阻尼因子 $\\beta=\\gamma/(2m)$、固有角频率 $\\omega_0=\\sqrt{k/m}$，方程化为标准形式：")+
   fml("\\ddot{x}+2\\beta\\dot{x}+\\omega_0^2 x=0")+
   p("设试探解 $x=e^{rt}$，代入得特征方程与其根：")+
   fml("r^2+2\\beta r+\\omega_0^2=0\\ \\Rightarrow\\ r=-\\beta\\pm\\sqrt{\\beta^2-\\omega_0^2}")+
   p("当 $\\beta<\\omega_0$（欠阻尼）时根为共轭复根 $r=-\\beta\\pm i\\omega$，其中 $\\omega=\\sqrt{\\omega_0^2-\\beta^2}$。取实系数线性方程解的实部，得衰减振动：")+
   fml("x=A_0e^{-\\beta t}\\cos(\\omega t+\\varphi)")+
   p("其振幅按指数衰减，振动周期 $T=2\\pi/\\omega=2\\pi/\\sqrt{\\omega_0^2-\\beta^2}$ 略大于无阻尼周期。相邻两次同方向极值之比为定值，取对数得对数减缩：")+
   fml("\\delta=\\ln\\frac{A(t)}{A(t+T)}=\\beta T")+
   p("$\\delta$ 可由振幅衰减曲线直接测定，从而反推阻尼因子。"))+
   exa(p("若初始振幅 $A_0=5\\,\\text{cm}$、$\\beta=0.5\\,\\text{s}^{-1}$，则经 $t=2\\,\\text{s}$ 后振幅为 $5e^{-1}\\approx1.84\\,\\text{cm}$。"))
 )},
{"id":"c5s2-2","name":"三种阻尼状态","tags":["thm","der","app"],"brief":"欠阻尼、临界阻尼与过阻尼的解与特征。",
 "body": wrap(
   thm("阻尼振动的三种状态",p("按 $\\beta$ 与 $\\omega_0$ 之比，由特征根 $r_{1,2}=-\\beta\\pm\\sqrt{\\beta^2-\\omega_0^2}$ 的虚实与重根情况，运动分三类。"))+
   der(p("<strong>（1）欠阻尼 $\\beta<\\omega_0$：</strong>共轭复根，解为衰减振动：")+
   fml("x=A_0e^{-\\beta t}\\cos(\\omega t+\\varphi),\\qquad \\omega=\\sqrt{\\omega_0^2-\\beta^2}")+
   p("<strong>（2）临界阻尼 $\\beta=\\omega_0$：</strong>特征方程有重根 $r=-\\beta$，两个线性无关解为 $e^{-\\beta t}$ 与 $te^{-\\beta t}$，故：")+
   fml("x=(C_1+C_2 t)e^{-\\beta t}")+
   p("<strong>（3）过阻尼 $\\beta>\\omega_0$：</strong>两个不等负实根 $r_{1,2}=-\\beta\\pm\\sqrt{\\beta^2-\\omega_0^2}$，解为两单调衰减项之和：")+
   fml("x=C_1e^{r_1t}+C_2e^{r_2t}")+
   p("后两种情形均不出现往复振动，质点单调地趋于平衡位置；三种状态由过阻尼、临界阻尼到欠阻尼，回到平衡的形态由缓慢趋近、最快不振荡过渡到衰减振荡。"))+
   app(p("临界阻尼使系统最快回到平衡又不过冲，广泛用于电流表、分析天平的指针阻尼、汽车减振器与闭门器的设计。"))
 )},
]},
# ---- 5.3 受迫振动与共振·频谱分析 ----
{
"name": "5.3 受迫振动与共振·频谱分析",
"color": "#ec4899",
"desc": "周期性外力下的稳态解、共振条件与谐波频谱",
"items": [
{"id":"c5s3-1","name":"受迫振动的稳态解","tags":["thm","der","app"],"brief":"稳态振幅与相位滞后公式。",
 "body": wrap(
   thm("受迫振动",p("阻尼振子在周期性外力 $F=F_0\\cos\\omega_d t$ 驱动下的运动方程为：")+
   fml("m\\ddot{x}+\\gamma\\dot{x}+kx=F_0\\cos\\omega_d t"))+
   der(p("两边除以 m，用 $\\beta=\\gamma/(2m)$、$\\omega_0^2=k/m$、$f_0=F_0/m$：")+
   fml("\\ddot{x}+2\\beta\\dot{x}+\\omega_0^2 x=f_0\\cos\\omega_d t")+
   p("这是二阶线性非齐次方程，其解由随时间衰减的暂态解（齐次解）与稳态解之和组成。设稳态解为与驱动同频率的简谐振动：")+
   fml("x=A\\cos(\\omega_d t+\\varphi_d)")+
   p("把它代入方程，令 $\\sin\\omega_d t$ 与 $\\cos\\omega_d t$ 的系数分别相等，可解出稳态振幅与相位滞后：")+
   fml("A=\\frac{f_0}{\\sqrt{(\\omega_0^2-\\omega_d^2)^2+(2\\beta\\omega_d)^2}},\\qquad \\tan\\varphi_d=\\frac{2\\beta\\omega_d}{\\omega_0^2-\\omega_d^2}")+
   p("可见稳态振动的频率由驱动频率决定，与初始条件无关；振幅与滞后相位则由驱动频率和系统参数共同决定，系统把激励“外来的频率”复制为自身的稳态运动。"))+
   app(p("用复振幅法可快速求解：令驱动力 $F=F_0e^{i\\omega_d t}$、稳态 $x=Xe^{i\\omega_d t}$，代入得复振幅 $X=f_0/[(\\omega_0^2-\\omega_d^2)+i2\\beta\\omega_d]$，其模即振幅 A、辐角即相位滞后。"))
 )},
{"id":"c5s3-2","name":"共振与频谱分析","tags":["thm","der","app"],"brief":"共振频率的极值条件与周期力的谐波分解。",
 "body": wrap(
   thm("共振",p("受迫振动的稳态振幅随驱动频率变化，当驱动频率接近某一特征值时振幅达到极大，称为<strong>共振</strong>。"))+
   der(p("对振幅表达式 $A(\\omega_d)=f_0/\\sqrt{(\\omega_0^2-\\omega_d^2)^2+(2\\beta\\omega_d)^2}$，振幅极大等价于分母极小。令分母对 $\\omega_d^2$ 的导数为零：")+
   fml("\\frac{d}{d(\\omega_d^2)}\\left[(\\omega_0^2-\\omega_d^2)^2+4\\beta^2\\omega_d^2\\right]=0")+
   p("解得共振频率与共振时的极大振幅：")+
   fml("\\omega_r=\\sqrt{\\omega_0^2-2\\beta^2},\\qquad A_{\\max}=\\frac{f_0}{2\\beta\\sqrt{\\omega_0^2-\\beta^2}}")+
   p("阻尼越小，共振峰越尖锐、峰值越高（$A_{\\max}\\propto1/\\beta$）；共振时相位滞后约为 $\\pi/2$。")+
   p("<strong>频谱分析。</strong>由傅里叶定理，任意周期性驱动力可分解为一系列简谐分量之和：")+
   fml("F(t)=a_0+\\sum_{n=1}^{\\infty}(a_n\\cos n\\omega t+b_n\\sin n\\omega t)")+
   p("由于方程是线性的，系统的总响应等于各谐波分量响应的叠加；把各分量的振幅按频率排列即得激励的<strong>频谱</strong>。系统对不同频率的放大倍数不同，从而对信号起滤波与整形作用。"))+
   app(p("工程上以幅频特性曲线 $A(\\omega_d)$ 表征系统对不同频率激励的响应；为避免共振破坏，隔振设计常使系统固有频率远高于或远低于激励频率。"))
 )},
]},
# ---- 5.4 谐振动的合成 ----
{
"name": "5.4 谐振动的合成",
"color": "#f472b6",
"desc": "同向同频、同向异频（拍）、垂直振动的合成",
"items": [
{"id":"c5s4-1","name":"同方向同频率振动的合成","tags":["thm","der","exa"],"brief":"合成仍为同频简谐振动，振幅由相位差决定。",
 "body": wrap(
   thm("同方向同频率合成",p("两个同方向、同频率的简谐振动合成为一个同频率的简谐振动：")+
   fml("x=x_1+x_2=A\\cos(\\omega t+\\varphi)"))+
   der(p("设 $x_1=A_1\\cos(\\omega t+\\varphi_1)$、$x_2=A_2\\cos(\\omega t+\\varphi_2)$。将两式展开并合并同类项：")+
   fml("x=(A_1\\cos\\varphi_1+A_2\\cos\\varphi_2)\\cos\\omega t-(A_1\\sin\\varphi_1+A_2\\sin\\varphi_2)\\sin\\omega t")+
   p("记 $X=A_1\\cos\\varphi_1+A_2\\cos\\varphi_2$、$Y=A_1\\sin\\varphi_1+A_2\\sin\\varphi_2$，则 $x=X\\cos\\omega t-Y\\sin\\omega t=A\\cos(\\omega t+\\varphi)$，于是：")+
   fml("A=\\sqrt{X^2+Y^2}=\\sqrt{A_1^2+A_2^2+2A_1A_2\\cos(\\varphi_2-\\varphi_1)},\\qquad \\tan\\varphi=\\frac{Y}{X}")+
   p("由旋转矢量法可直接理解：两矢量以相同角速度转动、夹角 $\\Delta\\varphi=\\varphi_2-\\varphi_1$ 恒定，故合矢量也匀速转动、大小不变。当 $\\Delta\\varphi=2n\\pi$ 时 $A=A_1+A_2$（同相加强）；当 $\\Delta\\varphi=(2n+1)\\pi$ 时 $A=|A_1-A_2|$（反相减弱）。"))+
   exa(p("等幅 $A_1=A_2=A$ 时 $A_{\\text{合}}=2A\\cos\\frac{\\Delta\\varphi}{2}$；当 $\\Delta\\varphi=2\\pi/3$ 时 $A_{\\text{合}}=2A\\cos(\\pi/3)=A$。"))
 )},
{"id":"c5s4-2","name":"同方向不同频率的合成·拍","tags":["def","thm","der","app"],"brief":"两相近频率同向振动叠加产生的拍。",
 "fig":"beats","figCap":"拍：合振幅周期性变化（缓变包络）",
 "body": wrap(
   defn("拍",p("两个频率相近、振动方向相同的简谐振动叠加时，合振幅发生周期性强弱变化的现象称为<strong>拍</strong>。"))+
   thm("拍频",p("设等幅两振动 $x_1=A\\cos\\omega_1t$、$x_2=A\\cos\\omega_2t$，且 $|\\omega_1-\\omega_2|\\ll\\omega_1,\\omega_2$，则合振动为：")+
   fml("x=2A\\cos\\frac{\\omega_1-\\omega_2}{2}t\\cdot\\cos\\frac{\\omega_1+\\omega_2}{2}t"))+
   der(p("利用和差化积 $\\cos\\alpha+\\cos\\beta=2\\cos\\frac{\\alpha-\\beta}{2}\\cos\\frac{\\alpha+\\beta}{2}$，直接得：")+
   fml("x=A(\\cos\\omega_1t+\\cos\\omega_2t)=2A\\cos\\left(\\frac{\\omega_1-\\omega_2}{2}t\\right)\\cos\\left(\\frac{\\omega_1+\\omega_2}{2}t\\right)")+
   p("记平均角频率 $\\bar{\\omega}=\\frac{\\omega_1+\\omega_2}{2}$、调制角频率 $\\omega_m=\\frac{|\\omega_1-\\omega_2|}{2}$，则 $x=[2A\\cos\\omega_m t]\\cos\\bar{\\omega}t$。由于 $\\omega_m\\ll\\bar{\\omega}$，$2A\\cos\\omega_m t$ 是缓变的振幅包络，$\\cos\\bar{\\omega}t$ 是快速载波。")+
   p("包络的绝对值 $|2A\\cos\\omega_m t|$ 的周期为 $T_m=\\pi/\\omega_m=2\\pi/|\\omega_1-\\omega_2|$，故单位时间内振幅极大出现的次数（拍频）为：")+
   fml("f_{\\text{拍}}=|f_1-f_2|"))+
   app(p("拍可用于校准乐器（待校音与标准音并听，拍消失即同频）、测量未知频率、无线电混频与超声多普勒测速。"))
 )},
{"id":"c5s4-3","name":"互相垂直振动的合成·李萨如图形","tags":["thm","der","app"],"brief":"垂直振动合成的轨迹与频率比关系。",
 "fig":"lissajous","figCap":"李萨如图形（频率比 2:1）",
 "body": wrap(
   thm("垂直振动的合成",p("设质点同时参与两个互相垂直的简谐振动 $x=A_x\\cos(\\omega_x t+\\varphi_x)$、$y=A_y\\cos(\\omega_y t+\\varphi_y)$，其轨迹由这两个参数方程共同决定。"))+
   der(p("<strong>（1）同频 $\\omega_x=\\omega_y=\\omega$：</strong>消去时间参量 $\\omega t$ 得一般二次曲线。取 $\\varphi_x=0$、$\\varphi_y=\\varphi$ 时：")+
   fml("\\frac{x^2}{A_x^2}+\\frac{y^2}{A_y^2}-\\frac{2xy}{A_xA_y}\\cos\\varphi=\\sin^2\\varphi")+
   p("当 $\\varphi=0$ 或 $\\pi$ 时轨迹退化为直线段；当 $\\varphi=\\pm\\pi/2$ 时为正椭圆（$A_x=A_y$ 时为圆）；其余相位为斜椭圆。")+
   p("<strong>（2）异频且为有理比 $\\omega_x:\\omega_y=n:m$：</strong>轨迹闭合，称为<strong>李萨如图形</strong>。闭合要求 $\\omega_xT=2n\\pi$ 与 $\\omega_yT=2m\\pi$ 同时成立，故频率比必须是有理数轨迹才可能封闭。")+
   p("对闭合曲线，水平方向切点数 $N_x$ 与竖直方向切点数 $N_y$ 之比等于频率的反比：")+
   fml("\\frac{N_x}{N_y}=\\frac{\\omega_y}{\\omega_x}"))+
   app(p("在示波器上用李萨如图形可精确测频：已知 $f_x$，由切点数得 $f_y=\\frac{N_x}{N_y}f_x$；同频时椭圆形状还可用于比较两信号的相位差。"))
 )},
]},
# ---- 5.5 两个自由度的振动 ----
{
"name": "5.5 两个自由度的振动",
"color": "#9d174d",
"desc": "耦合振子的简正模与简正坐标、能量交换",
"items": [
{"id":"c5s5-1","name":"耦合振子与简正模","tags":["def","thm","der","exa"],"brief":"两自由度系统的两个简正频率。",
 "body": wrap(
   defn("简正模",p("描写系统位形所需的独立坐标个数称为<strong>自由度</strong>。多自由度系统中，各质点以同一频率做简谐振动、整体同步的振动模式称为<strong>简正模</strong>，其频率称为<strong>简正频率</strong>。"))+
   thm("两耦合振子的简正模",p("两个相同振子（质量 m、弹簧 k）用弱耦合弹簧 $k_c$ 相连，其两个简正频率为：")+
   fml("\\omega_1=\\sqrt{\\frac{k}{m}},\\qquad \\omega_2=\\sqrt{\\frac{k+2k_c}{m}}"))+
   der(p("设两振子位移为 $x_1,x_2$，中间耦合弹簧对它们提供方向相反的额外力。对两个振子分别用牛顿第二定律：")+
   fml("m\\ddot{x}_1=-kx_1+k_c(x_2-x_1)")+
   fml("m\\ddot{x}_2=-kx_2-k_c(x_2-x_1)")+
   p("把两式相加、相减，引入<strong>简正坐标</strong> $q_1=x_1+x_2$、$q_2=x_1-x_2$，耦合项恰好抵消：")+
   fml("\\ddot{q}_1+\\frac{k}{m}q_1=0,\\qquad \\ddot{q}_2+\\frac{k+2k_c}{m}q_2=0")+
   p("两方程完全解耦，$q_1,q_2$ 各自独立地做简谐振动，其角频率即两个简正频率：")+
   fml("\\omega_1=\\sqrt{\\frac{k}{m}},\\qquad \\omega_2=\\sqrt{\\frac{k+2k_c}{m}}")+
   p("$q_1$ 对应两振子同向运动：耦合弹簧不变形，故频率与单振子相同；$q_2$ 对应两振子反向运动：耦合弹簧被压缩或拉伸 2 倍，附加恢复力更大，故频率更高。一般运动是两个简正模的线性叠加。"))+
   exa(p("当 $k_c\\ll k$ 时 $\\omega_1\\approx\\omega_2$，两简正模频率相近，叠加后表现为能量在两振子间周期性转移（拍），这正是耦合摆、双 LC 回路能量交换的一般机制。"))
 )},
]},
# ---- 5.6 一维波的形成与波动方程 ----
{
"name": "5.6 一维波的形成与波动方程",
"color": "#e11d48",
"desc": "波的形成、简谐波解析式与一维波动方程",
"items": [
{"id":"c5s6-1","name":"波的形成与简谐波表达式","tags":["def","der","exa"],"brief":"相位滞后给出简谐波函数。",
 "fig":"wave","figCap":"简谐波的波形、波长与振幅",
 "body": wrap(
   defn("机械波",p("机械振动在弹性介质中的传播称为<strong>机械波</strong>。介质中各质点只在平衡位置附近振动，并不随波迁移，波传播的是振动状态与能量。"))+
   defn("波的特征量",p("波长 $\\lambda$ 为一个完整波形所占的空间长度，周期 $T$ 为质点完成一次全振动的时间，频率 $f=1/T$，波速 $v$ 由介质性质决定，四者满足：")+
   fml("v=\\frac{\\lambda}{T}=\\lambda f"))+
   der(p("设原点处质点做简谐振动 $y_0=A\\cos(\\omega t+\\varphi)$。波以速度 v 沿 x 正方向传播，距原点 x 处的质点要等 $\\Delta t=x/v$ 后才开始振动，即其相位比原点落后 $\\omega\\Delta t=\\omega x/v$：")+
   fml("y(x,t)=A\\cos\\left[\\omega\\left(t-\\frac{x}{v}\\right)+\\varphi\\right]")+
   p("引入波数 $k=\\frac{2\\pi}{\\lambda}=\\frac{\\omega}{v}$，得常用的两种等价形式：")+
   fml("y=A\\cos(\\omega t-kx+\\varphi)=A\\cos\\left[2\\pi\\left(\\frac{t}{T}-\\frac{x}{\\lambda}\\right)+\\varphi\\right]")+
   p("可见 $t$ 增大时相位相同的点向 $+x$ 移动，故 $\\cos(\\omega t-kx)$ 表示沿 $+x$ 传播的波；把 x 换成 $-x$ 即 $\\cos(\\omega t+kx)$ 表示沿 $-x$ 传播的波。"))+
   exa(p("绳波 $A=0.02\\,\\text{m}$、$T=0.2\\,\\text{s}$、$\\lambda=0.4\\,\\text{m}$，则 $v=\\lambda/T=2\\,\\text{m/s}$，波数 $k=2\\pi/\\lambda=5\\pi\\,\\text{rad/m}$。"))
 )},
{"id":"c5s6-2","name":"一维波动方程","tags":["thm","der","app"],"brief":"绳上横波与固体弹性介质的波动方程。",
 "body": wrap(
   thm("一维波动方程",p("一维波函数 $y(x,t)$ 满足二阶偏微分方程：")+
   fml("\\frac{\\partial^2y}{\\partial x^2}=\\frac{1}{v^2}\\frac{\\partial^2y}{\\partial t^2}"))+
   der(p("<strong>（1）绳上横波。</strong>取绳上长 $\\Delta x$ 的线元，线密度 $\\mu$、张力 $F$ 的方向沿切线。线元所受横向合力为两端张力的横向分量之差：")+
   fml("F_y=F\\left[\\left.\\frac{\\partial y}{\\partial x}\\right|_{x+\\Delta x}-\\left.\\frac{\\partial y}{\\partial x}\\right|_{x}\\right]\\approx F\\frac{\\partial^2y}{\\partial x^2}\\Delta x")+
   p("由牛顿第二定律 $F_y=\\mu\\Delta x\\,\\frac{\\partial^2y}{\\partial t^2}$，约去 $\\Delta x$ 得：")+
   fml("\\frac{\\partial^2y}{\\partial t^2}=\\frac{F}{\\mu}\\frac{\\partial^2y}{\\partial x^2},\\qquad v=\\sqrt{\\frac{F}{\\mu}}")+
   p("<strong>（2）固体弹性介质。</strong>长棒中的纵向弹性波由胡克定律可知应力与应变 $\\partial u/\\partial x$ 成正比，得纵波、横波波速：")+
   fml("v_{\\parallel}=\\sqrt{\\frac{E}{\\rho}},\\qquad v_{\\perp}=\\sqrt{\\frac{G}{\\rho}}")+
   p("其中 E 为杨氏模量、G 为切变模量、$\\rho$ 为密度，纵波、横波分别按此波速传播；可见波速只取决于介质的弹性与惯性，与波源无关。")+
   p("<strong>验证：</strong>把 $y=A\\cos(\\omega t-kx)$ 代入波动方程，左端为 $-k^2y$、右端为 $-(\\omega^2/v^2)y$，得 $v=\\omega/k$；事实上只要写成 $f(x\\mp vt)$ 形式即为解，这正是达朗贝尔解。"))+
   app(p("波动方程是各类线性波的普遍方程：绳、弦、弹性杆中的机械波，气体中的声波乃至真空中的电磁波都满足它，只是波速表达式不同。"))
 )},
]},
# ---- 5.7 波的能量、能流密度与波强 ----
{
"name": "5.7 波的能量、能流密度与波强",
"color": "#f43f5e",
"desc": "能量密度、能流密度与波强的平方律",
"items": [
{"id":"c5s7-1","name":"波的能量密度与能流密度","tags":["thm","der","exa"],"brief":"行波能量密度与强度的推导。",
 "body": wrap(
   thm("波的能量密度",p("简谐波 $y=A\\cos(\\omega t-kx)$ 传播时，介质体元同时获得动能与弹性势能，其能量密度（单位体积能量）为：")+
   fml("w=\\rho\\omega^2A^2\\sin^2(\\omega t-kx)"))+
   der(p("取体积元 $\\Delta V$、质量 $\\Delta m=\\rho\\Delta V$，其振动速度 $v_y=\\frac{\\partial y}{\\partial t}=-\\omega A\\sin(\\omega t-kx)$。动能：")+
   fml("\\Delta E_k=\\tfrac{1}{2}\\Delta m\\,v_y^2=\\tfrac{1}{2}\\rho\\Delta V\\,\\omega^2A^2\\sin^2(\\omega t-kx)")+
   p("体元的线应变 $\\partial y/\\partial x=-kA\\sin(\\omega t-kx)$，弹性势能与其平方成正比，可证 $\\Delta E_p=\\Delta E_k$：行波中动能与势能同相位、等值变化，这是它与孤立振子（动能势能此消彼长）的根本差别。")+
   p("于是总能量 $\\Delta E=\\Delta E_k+\\Delta E_p=2\\Delta E_k$，能量密度：")+
   fml("w=\\frac{\\Delta E}{\\Delta V}=\\rho\\omega^2A^2\\sin^2(\\omega t-kx)")+
   p("对时间取平均，因 $\\overline{\\sin^2}=1/2$，得平均能量密度 $\\bar{w}=\\tfrac{1}{2}\\rho\\omega^2A^2$。"))+
   thm("能流密度与波强",p("单位时间通过垂直于传播方向单位面积的能量称为<strong>能流密度</strong>，其时间平均值即<strong>波的强度</strong>：")+
   fml("I=\\bar{w}\\,v=\\tfrac{1}{2}\\rho\\omega^2A^2v"))+
   der(p("在 $\\Delta t$ 内通过面积 S 的能量等于长为 $v\\Delta t$ 的柱体内的能量 $\\Delta E=\\bar{w}Sv\\Delta t$，故 $I=\\Delta E/(S\\Delta t)=\\bar{w}v$，得 $I=\\tfrac{1}{2}\\rho\\omega^2A^2v$，即强度与振幅平方、频率平方、波速成正比。")+
   p("对球面波，总功率守恒 $I\\cdot4\\pi r^2=\\text{const}$，故 $I\\propto1/r^2$、振幅 $A\\propto1/r$——这正是声波、光波在自由空间强度随距离平方衰减的原因。")+
   p("对不损耗的平面波，振幅不随距离衰减；若介质有吸收，则强度按指数衰减 $I=I_0e^{-\\alpha x}$，$\\alpha$ 为吸收系数。"))+
   exa(p("空气中声波取 $\\rho=1.29\\,\\text{kg/m}^3$、$v=340\\,\\text{m/s}$、$f=440\\,\\text{Hz}$、$A=10^{-5}\\,\\text{m}$，则 $I\\approx\\tfrac12\\times1.29\\times(2\\pi\\times440)^2\\times(10^{-5})^2\\times340\\approx0.17\\,\\text{W/m}^2$。"))
 )},
]},
# ---- 5.8 一维波传播的问题 ----
{
"name": "5.8 一维波传播的问题（特征阻抗、反射、驻波）",
"color": "#fb7185",
"desc": "特征阻抗、反射透射系数、驻波与半波损失",
"items": [
{"id":"c5s8-1","name":"特征阻抗与反射、透射系数","tags":["def","thm","der","exa"],"brief":"由界面连续条件导出反射透射系数。",
 "body": wrap(
   defn("特征阻抗",p("对一维绳（弦）波，张力 F、线密度 $\\mu$，定义<strong>特征阻抗</strong> $Z=F/v=\\sqrt{F\\mu}$；一般介质中取 $Z=\\rho v$，反映介质对波传播的阻碍程度。"))+
   thm("反射与透射系数",p("波由阻抗 $Z_1$ 的介质垂直入射到阻抗 $Z_2$ 的界面，振幅反射系数与透射系数为：")+
   fml("r=\\frac{A_r}{A_i}=\\frac{Z_1-Z_2}{Z_1+Z_2},\\qquad t=\\frac{A_t}{A_i}=\\frac{2Z_1}{Z_1+Z_2}"))+
   der(p("在界面 $x=0$ 处必须满足位移连续与力连续两个条件。设入射、反射、透射波分别为 $y_i=A_i\\cos(\\omega t-k_1x)$、$y_r=A_r\\cos(\\omega t+k_1x)$、$y_t=A_t\\cos(\\omega t-k_2x)$。")+
   p("位移连续 $y_i+y_r=y_t$（取 $x=0$）给出：")+
   fml("A_i+A_r=A_t")+
   p("对绳波横向力正比于 $F\\,\\partial y/\\partial x$，力连续要求 $F_1\\partial(y_i+y_r)/\\partial x=F_2\\,\\partial y_t/\\partial x$（在 $x=0$）。利用 $Fk=\\omega F/v=\\omega Z$：")+
   fml("Z_1(A_i-A_r)=Z_2A_t")+
   p("联立两式消去 $A_t$（或 $A_r$），立即求出 r 与 t：")+
   fml("r=\\frac{Z_1-Z_2}{Z_1+Z_2},\\qquad t=1+r=\\frac{2Z_1}{Z_1+Z_2}"))+
   exa(p("绳末端固定（$Z_2\\to\\infty$）：$r=-1$，反射波与入射波反相，界面合位移恒为零，形成波节；绳末端自由（$Z_2\\to0$）：$r=+1$，反射波同相，界面合位移加倍，形成波腹。"))
 )},
{"id":"c5s8-2","name":"驻波与半波损失","tags":["thm","der","app"],"brief":"反向传播相干波叠加的驻波与半波损失。",
 "fig":"halfwave","figCap":"界面反射：波疏入射波密时反射波反相",
 "body": wrap(
   thm("驻波",p("两列振幅、频率相同而传播方向相反的相干波叠加形成<strong>驻波</strong>：")+
   fml("y=2A\\cos(kx)\\cos(\\omega t)"))+
   der(p("设右行波 $y_1=A\\cos(\\omega t-kx)$、左行波 $y_2=A\\cos(\\omega t+kx+\\delta)$，$\\delta$ 为界面反射引入的相位。先取 $\\delta=0$，用和差化积：")+
   fml("y=y_1+y_2=A[\\cos(\\omega t-kx)+\\cos(\\omega t+kx)]=2A\\cos(kx)\\cos(\\omega t)")+
   p("此式不再含 $\\omega t-kx$ 形式的行波相位，各点振幅 $|2A\\cos(kx)|$ 只随位置而变，故称驻波。$\\cos(kx)=0$ 处永远静止，为<strong>波节</strong>：")+
   fml("x_n=\\left(n+\\tfrac12\\right)\\frac{\\lambda}{2}")+
   p("$|\\cos(kx)|=1$ 处振幅最大，为<strong>波腹</strong> $x=n\\tfrac{\\lambda}{2}$；相邻波节（或波腹）间距均为 $\\lambda/2$，相邻波节与波腹间距为 $\\lambda/4$。")+
   p("<strong>半波损失。</strong>当 $Z_2>Z_1$（波疏入射到波密）时 $r<0$，反射波在界面反相 $\\pi$，即 $\\delta=\\pi$，此时：")+
   fml("y=A[\\cos(\\omega t-kx)-\\cos(\\omega t+kx)]=2A\\sin(kx)\\sin(\\omega t)")+
   p("由 $\\sin(kx)$ 在 $x=0$ 为零知界面处为波节，等效于反射波多走了半个波长，故称<strong>半波损失</strong>。反之 $Z_2<Z_1$（波密入射到波疏）时无半波损失，界面为波腹。"))+
   app(p("驻波广泛用于弦乐器（弦长为半波长的整数倍）、管乐器（开管两端为波腹、闭管一端为波节）与激光谐振腔；半波损失则是牛顿环、薄膜干涉附加光程差 $\\lambda/2$ 的来源。"))
 )},
]},
# ---- 5.9 多普勒效应、色散与群速 ----
{
"name": "5.9 多普勒效应、色散与群速",
"color": "#831843",
"desc": "频率的观测变化、相速群速与色散",
"items": [
{"id":"c5s9-1","name":"多普勒效应","tags":["thm","der","app"],"brief":"波源或观察者运动引起接收频率变化。",
 "body": wrap(
   thm("多普勒效应",p("设介质中波速为 $v$、波源频率为 $f_0$、观察者速度 $v_O$（朝向波源为正）、波源速度 $v_S$（朝向观察者为正），则接收频率为：")+
   fml("f=\\frac{v+v_O}{v-v_S}f_0"))+
   der(p("<strong>（1）只有观察者运动。</strong>波源静止时波长 $\\lambda=v/f_0$ 不变。观察者以 $v_O$ 迎波运动，相对波的速度为 $v+v_O$，单位时间接收的波数为：")+
   fml("f'=\\frac{v+v_O}{\\lambda}=\\frac{v+v_O}{v}f_0")+
   p("<strong>（2）只有波源运动。</strong>观察者静止。波源每完成一次振动向观察者移动 $v_ST$，使波长压缩为 $\\lambda'=vT-v_ST=(v-v_S)/f_0$，故接收频率：")+
   fml("f'=\\frac{v}{\\lambda'}=\\frac{v}{v-v_S}f_0")+
   p("<strong>（3）两者同时运动。</strong>把（2）得到的压缩波长代入（1）的接收公式，即得一般式：")+
   fml("f=\\frac{v+v_O}{v-v_S}f_0")+
   p("波源靠近（$v_S>0$）时 f 升高，远离时 f 降低；观察者靠近（$v_O>0$）时 f 升高。"))+
   app(p("应用：交通雷达测速、医学超声多普勒测血流、天文谱线红移测天体退行速度、卫星导航与天气雷达测风。"))
 )},
{"id":"c5s9-2","name":"色散与群速","tags":["def","thm","der","app"],"brief":"相速、群速的关系与波包传播。",
 "body": wrap(
   defn("色散",p("波的相速度 $v_p=\\omega/k$ 随频率（或波数）改变的现象称为<strong>色散</strong>，相应介质称为色散介质，此时不同频率成分的传播速度不同。"))+
   thm("相速与群速",p("相速度 $v_p=\\omega/k$ 描写单色波等相位面的传播速度；群速度 $v_g=\\frac{d\\omega}{dk}$ 描写波包（振幅包络）整体的传播速度，即能量与信息传播的速度。"))+
   der(p("考虑两个频率相近的单色波叠加成波包 $y=\\cos(\\omega_1t-k_1x)+\\cos(\\omega_2t-k_2x)$，用和差化积：")+
   fml("y=2\\cos(\\Delta\\omega\\,t-\\Delta k\\,x)\\cos(\\bar{\\omega}t-\\bar{k}x)")+
   p("其中 $\\Delta\\omega=\\frac{\\omega_1-\\omega_2}{2}$、$\\Delta k=\\frac{k_1-k_2}{2}$ 为缓变调制量，$\\bar{\\omega},\\bar{k}$ 为平均值。前一个余弦是慢变的包络，在 $\\Delta\\omega\\,t-\\Delta k\\,x=\\text{const}$ 条件下传播，速度为：")+
   fml("v_g=\\frac{\\Delta\\omega}{\\Delta k}\\ \\longrightarrow\\ \\frac{d\\omega}{dk}")+
   p("利用 $\\omega=v_pk$，可得相速与群速的关系：")+
   fml("v_g=\\frac{d\\omega}{dk}=v_p+k\\frac{dv_p}{dk}=v_p-\\lambda\\frac{dv_p}{d\\lambda}")+
   p("无色散时 $dv_p/d\\lambda=0$，则 $v_g=v_p$；有色散时二者不同，且波包在传播中会展宽、变形。"))+
   app(p("群速度是波包、能量与信号实际的传播速度，也是光纤中脉冲的传输速度；材料色散使不同频率成分速度不同，导致脉冲展宽，是限制光纤传输容量与距离的关键因素。"))
 )},
]},
# ---- 5.10 空间波·惠更斯原理·衍射反射折射 ----
{
"name": "5.10 空间波·惠更斯原理·衍射反射折射",
"color": "#be185d",
"desc": "波面波前、惠更斯原理与波的衍射反射折射",
"items": [
{"id":"c5s10-1","name":"波面、波前与惠更斯原理","tags":["def","thm","der","app"],"brief":"用子波包络作图确定新波前并导出折射定律。",
 "body": wrap(
   defn("波面与波线",p("振动相位相同的点连成的面称为<strong>波面</strong>（等相面），最前面的波面称为<strong>波前</strong>；垂直于波面、指示传播方向的有向线称为<strong>波射线</strong>（波线）。球面波的波面为同心球面，平面波的波面为平行平面。"))+
   thm("惠更斯原理",p("波前上的每一点都可看作发射球面子波的<strong>新波源</strong>，其后任一时刻这些子波的<strong>包络面</strong>就是该时刻的新波前。"))+
   der(p("设 $t$ 时刻波前为 S，其上各点发出的子波以介质波速 v 传播，$\\Delta t$ 后每个子波半径均为 $v\\Delta t$；作所有子球的公切面 S'，即 $t+\\Delta t$ 时刻的波前。这就是惠更斯作图法。")+
   p("<strong>用它导出折射定律：</strong>平面波以入射角 $\\theta_1$ 射到界面，波前先后到达界面的不同点，各点发出的子波在另一介质中以 $v_2$ 传播。由同一波前上不同点到达界面的时间差相同，两介质中波前在相同 $\\Delta t$ 内推进的几何关系给出：")+
   fml("\\frac{\\sin\\theta_1}{v_1}=\\frac{\\sin\\theta_2}{v_2}\\ \\Rightarrow\\ \\frac{\\sin\\theta_1}{\\sin\\theta_2}=\\frac{v_1}{v_2}=n_{21}")+
   p("这正是斯涅尔折射定律，$n_{21}=v_1/v_2$ 为第二介质相对第一介质的折射率。反射情形取 $v_2=v_1$，即得反射角等于入射角。"))+
   app(p("惠更斯作图法是推导反射定律、折射定律以及分析平面波、球面波传播的基础；据此还可说明波在界面处反射、折射时波前与波线方向的变化。"))
 )},
{"id":"c5s10-2","name":"波的衍射","tags":["def","thm","der","app"],"brief":"衍射显著的条件与惠更斯解释。",
 "body": wrap(
   defn("波的衍射",p("波在传播中遇到障碍物、孔或缝时，波前发生畸变、偏离直线而绕到障碍物后方传播的现象称为<strong>衍射</strong>（绕射）。"))+
   thm("衍射显著的条件",p("当障碍物或缝的尺寸 a 与波长 $\\lambda$ 相近或更小（$a\\lesssim\\lambda$）时衍射明显；当 $a\\gg\\lambda$ 时波近似沿直线传播。"))+
   der(p("由惠更斯原理，波到达宽为 a 的缝时，缝上各点成为子波源，各自向各方向发射子波，其后各子波在缝后空间叠加形成非均匀的强度分布。")+
   p("用缝上不同点到观察方向的波程差判断强弱。设缝上下边缘两点射向衍射角 $\\theta$ 方向的波程差为：")+
   fml("\\Delta=a\\sin\\theta")+
   p("当 $\\Delta\\ll\\lambda$ 时各子波近似同相，缝后相当于一个新的点波源，波以球面波向各方向扩展，衍射最强；当 $a\\gg\\lambda$ 时除零级方向外各子波大部分相互抵消，波近似直线传播。")+
   p("由于 $v=\\lambda f$，波速一定时波长越长（频率越低）衍射越强。故声波（波长可达米量级）易绕过障碍物，而光波（波长约 $0.5\\,\\mu\\text{m}$）的衍射需借助狭缝、光栅才能明显观察。"))+
   app(p("衍射的应用：声学中利用低频声波绕射实现隔墙闻声；光学中单缝、圆孔衍射决定成像系统的分辨极限（瑞利判据）；X 射线晶体衍射用于测定晶体结构。"))
 )},
]},
# ---- 5.11 波的干涉 ----
{
"name": "5.11 波的干涉",
"color": "#db2777",
"desc": "波的叠加原理、相干条件与干涉花样",
"items": [
{"id":"c5s11-1","name":"叠加原理与相干条件·干涉花样","tags":["thm","def","der","exa"],"brief":"相位差决定干涉强弱，波程差给出极值条件。",
 "body": wrap(
   thm("波的叠加原理",p("几列波在同一介质中相遇时，各自保持原有的频率、振幅与传播方向独立传播；在相遇区域，任一质点的合位移等于各列波单独存在时在该点所引起位移的矢量和。"))+
   defn("相干条件",p("频率相同、振动方向相同（或相近）、相位差恒定（不随时间变化）的两列波能产生稳定的干涉图样，称为<strong>相干波</strong>，上述条件称为<strong>相干条件</strong>。"))+
   der(p("设两相干波源 $S_1,S_2$ 的初相为 $\\varphi_1,\\varphi_2$，到空间某点 P 的距离为 $r_1,r_2$，两波在 P 点的振动分别为：")+
   fml("y_1=A_1\\cos(\\omega t-kr_1+\\varphi_1),\\qquad y_2=A_2\\cos(\\omega t-kr_2+\\varphi_2)")+
   p("二者同频、同振动方向，故在 P 点的相位差恒定：")+
   fml("\\Delta\\varphi=(\\varphi_2-\\varphi_1)-k(r_2-r_1)=(\\varphi_2-\\varphi_1)-\\frac{2\\pi}{\\lambda}\\Delta r")+
   p("由同方向同频合成公式，P 点合振幅为：")+
   fml("A=\\sqrt{A_1^2+A_2^2+2A_1A_2\\cos\\Delta\\varphi}")+
   p("当 $\\Delta\\varphi=2n\\pi$ 时 $A=A_1+A_2$（干涉加强），当 $\\Delta\\varphi=(2n+1)\\pi$ 时 $A=|A_1-A_2|$（干涉减弱）。若 $\\varphi_1=\\varphi_2$，条件简化为由<strong>波程差</strong>决定：")+
   fml("\\Delta r=r_2-r_1=n\\lambda,\\qquad \\Delta r=\\left(n+\\tfrac12\\right)\\lambda")+
   p("分别对应干涉相长（亮纹）与相消（暗纹）。由于 $\\Delta\\varphi$ 只与位置有关且恒定，空间各点强弱交替、位置固定，形成稳定的<strong>干涉花样</strong>。"))+
   exa(p("双缝干涉：两缝相距 d、屏到缝距离 D，屏上距中心 $y$ 处的波程差 $\\Delta r\\approx yd/D$；亮纹位置 $y=n\\lambda D/d$，相邻亮纹间距 $\\Delta y=\\lambda D/d$。"))
 )},
]},
]
CHAPTERS = [
    {"id":"m-ch1","num":"第一章","title":"质点运动学","en":"KINEMATICS",
     "desc":"空间与时间、参考系与坐标系；直线运动与曲线运动的位移、速度、速率、加速度的矢量描述；直角坐标系、极坐标系、自然坐标系中位置、速度与加速度的分量表达；相对运动与伽利略变换。",
     "sections": ch1_sections},
    {"id":"m-ch2","num":"第二章","title":"质点动力学","en":"DYNAMICS",
     "desc":"惯性定律与惯性参考系；力、力的量度、惯性质量与牛顿第二定律；万有引力、弹性力、摩擦力与作用力反作用力；力的合成与分解、约束运动；干摩擦与湿摩擦；平动参考系与伽利略相对性原理、平动惯性力；转动参考系中的离心惯性力与科里奥利力及地球自转效应。",
     "sections": ch2_sections},
    {"id":"m-ch3","num":"第三章","title":"运动定理","en":"THEOREMS OF MOTION",
     "desc":"动量定理与动量守恒；质点动量矩（角动量）定理与守恒；功、功率与保守力、势能；动能定理、机械能守恒定律与功能原理；有心力与有效势能；两体问题与质心运动定理；碰撞；质点系的动量矩定理与守恒、动能定理与柯尼希定理。",
     "sections": ch3_sections},
    {"id":"m-ch4","num":"第四章","title":"刚体力学","en":"RIGID BODY MECHANICS",
     "desc":"刚体与自由度、力系的简化；刚体的平衡与稳定性、桁架；平动与定轴转动的动力学基本方程；转动惯量计算、惯量张量与惯量主轴；定轴转动的能量、约束反力与动平衡；平面平行运动与滚动摩擦；定点运动与回转仪。",
     "sections": ch4_sections},
    {"id":"m-ch5","num":"第五章","title":"振动与波","en":"OSCILLATIONS & WAVES",
     "desc":"单自由度谐振动、阻尼振动、受迫振动与共振、频谱分析；谐振动的合成与两自由度振动；一维波的形成与波动方程、波的能量与能流密度；特征阻抗、反射、驻波、多普勒效应与色散群速；空间波与惠更斯原理、衍射反射折射；波的叠加原理与干涉。",
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
<meta name="description" content="力学知识体系：质点运动学、质点动力学与非惯性参考系、运动定理、刚体力学、振动与波">
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
    <p class="la-subtitle">质点运动学 · 质点动力学 · 运动定理 · 刚体力学 · 振动与波</p>
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
