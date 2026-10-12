# -*- coding: utf-8 -*-
"""Generate electromagnetism.html with 5 chapters: 静电场/介质静电场/静磁场/介质静磁场/麦克斯韦."""
import json

FIG = {
"pointcharge": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="12" fill="#ef4444"/>
<text x="114" y="84" font-size="12" fill="#fff" font-weight="bold">+</text>
<line x1="120" y1="80" x2="120" y2="30" stroke="#3b82f6" stroke-width="1.5"/>
<polygon points="120,30 114,40 126,40" fill="#3b82f6"/>
<line x1="120" y1="80" x2="170" y2="80" stroke="#3b82f6" stroke-width="1.5"/>
<polygon points="170,80 160,74 160,86" fill="#3b82f6"/>
<line x1="120" y1="80" x2="85" y2="115" stroke="#3b82f6" stroke-width="1.5"/>
<polygon points="85,115 91,105 83,107" fill="#3b82f6"/>
<line x1="120" y1="80" x2="70" y2="55" stroke="#3b82f6" stroke-width="1.5"/>
<polygon points="70,55 76,48 80,58" fill="#3b82f6"/>
<text x="175" y="78" font-size="11" fill="#3b82f6">E</text></svg>''',
"dipole": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="95" cy="80" r="10" fill="#ef4444"/>
<text x="90" y="84" font-size="12" fill="#fff" font-weight="bold">+</text>
<circle cx="145" cy="80" r="10" fill="#3b82f6"/>
<text x="140" y="84" font-size="12" fill="#fff" font-weight="bold">−</text>
<line x1="95" y1="80" x2="145" y2="80" stroke="#475569" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="115" y="74" font-size="10" fill="#475569">d</text>
<line x1="120" y1="40" x2="120" y2="60" stroke="#10b981" stroke-width="2"/>
<polygon points="120,40 114,50 126,50" fill="#10b981"/>
<text x="125" y="42" font-size="11" fill="#10b981">p</text></svg>''',
"gauss": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="14" fill="#ef4444"/>
<text x="114" y="84" font-size="11" fill="#fff" font-weight="bold">q</text>
<circle cx="120" cy="80" r="55" fill="none" stroke="#0ea5e9" stroke-width="2" stroke-dasharray="5 4"/>
<text x="178" y="50" font-size="11" fill="#0ea5e9">S (高斯面)</text>
<line x1="134" y1="80" x2="170" y2="80" stroke="#3b82f6" stroke-width="1.5"/>
<polygon points="170,80 160,74 160,86" fill="#3b82f6"/>
<text x="150" y="72" font-size="10" fill="#3b82f6">dS</text></svg>''',
"capacitor": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="60" y1="40" x2="60" y2="120" stroke="#3b82f6" stroke-width="4"/>
<line x1="180" y1="40" x2="180" y2="120" stroke="#ef4444" stroke-width="4"/>
<text x="45" y="138" font-size="11" fill="#3b82f6">+Q</text>
<text x="170" y="138" font-size="11" fill="#ef4444">−Q</text>
<line x1="90" y1="80" x2="150" y2="80" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
<text x="112" y="72" font-size="10" fill="#10b981">d</text>
<line x1="100" y1="60" x2="140" y2="60" stroke="#f59e0b" stroke-width="1.5"/>
<polygon points="140,60 132,56 132,64" fill="#f59e0b"/>
<text x="110" y="52" font-size="10" fill="#f59e0b">E</text></svg>''',
"biot": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 40 120 Q 120 120 200 120" fill="none" stroke="#475569" stroke-width="3"/>
<circle cx="120" cy="120" r="4" fill="#ef4444"/>
<text x="126" y="116" font-size="10" fill="#ef4444">Idl</text>
<circle cx="170" cy="60" r="4" fill="#3b82f6"/>
<text x="175" y="56" font-size="10" fill="#3b82f6">P</text>
<line x1="120" y1="120" x2="170" y2="60" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="138" y="82" font-size="10" fill="#94a3b8">r</text>
<line x1="170" y1="60" x2="170" y2="35" stroke="#10b981" stroke-width="2"/>
<polygon points="170,35 164,45 176,45" fill="#10b981"/>
<text x="175" y="40" font-size="11" fill="#10b981">dB</text></svg>''',
"solenoid": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 30 80 Q 50 50 70 80 Q 90 110 110 80 Q 130 50 150 80 Q 170 110 190 80 Q 210 50 230 80" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
<line x1="40" y1="80" x2="220" y2="80" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
<polygon points="220,80 210,74 210,86" fill="#10b981"/>
<text x="200" y="70" font-size="11" fill="#10b981">B</text>
<text x="30" y="130" font-size="11" fill="#3b82f6">N 匝, 电流 I</text></svg>''',
"induction": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="120" cy="80" r="50" fill="none" stroke="#3b82f6" stroke-width="2"/>
<line x1="120" y1="80" x2="170" y2="80" stroke="#94a3b8" stroke-width="1.5"/>
<text x="140" y="74" font-size="10" fill="#94a3b8">A</text>
<line x1="80" y1="100" x2="160" y2="100" stroke="#10b981" stroke-width="2"/>
<polygon points="160,100 150,94 150,106" fill="#10b981"/>
<text x="110" y="118" font-size="11" fill="#10b981">B(t)</text>
<path d="M 120 30 A 50 50 0 0 1 170 80" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="4 3"/>
<polygon points="170,80 160,74 162,86" fill="#ef4444"/>
<text x="150" y="55" font-size="10" fill="#ef4444">ε</text></svg>''',
"wave_em": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 10 80 Q 40 30 70 80 T 130 80 T 190 80 T 230 80" fill="none" stroke="#3b82f6" stroke-width="2"/>
<path d="M 10 80 Q 40 130 70 80 T 130 80 T 190 80 T 230 80" fill="none" stroke="#ef4444" stroke-width="2"/>
<text x="20" y="28" font-size="10" fill="#3b82f6">E</text>
<text x="20" y="140" font-size="10" fill="#ef4444">B</text>
<line x1="10" y1="80" x2="230" y2="80" stroke="#10b981" stroke-width="1" stroke-dasharray="6 4" opacity="0.6"/>
<text x="185" y="72" font-size="10" fill="#10b981">传播方向</text></svg>''',
"dielectric": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="30" width="180" height="100" fill="#eef4fb" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="80" y="20" font-size="11" fill="#475569">电介质</text>
<g>
<circle cx="70" cy="70" r="8" fill="none" stroke="#cbd5e1" stroke-width="1"/>
<circle cx="70" cy="70" r="3" fill="#ef4444"/>
<line x1="70" y1="70" x2="78" y2="62" stroke="#3b82f6" stroke-width="1"/>
</g>
<g>
<circle cx="120" cy="90" r="8" fill="none" stroke="#cbd5e1" stroke-width="1"/>
<circle cx="120" cy="90" r="3" fill="#ef4444"/>
<line x1="120" y1="90" x2="128" y2="82" stroke="#3b82f6" stroke-width="1"/>
</g>
<g>
<circle cx="170" cy="70" r="8" fill="none" stroke="#cbd5e1" stroke-width="1"/>
<circle cx="170" cy="70" r="3" fill="#ef4444"/>
<line x1="170" y1="70" x2="178" y2="62" stroke="#3b82f6" stroke-width="1"/>
</g>
<text x="100" y="145" font-size="10" fill="#475569">极化：束缚电荷沿电场方向排列</text></svg>''',
"magnetic_material": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<rect x="30" y="30" width="180" height="100" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="80" y="20" font-size="11" fill="#475569">磁介质</text>
<g>
<circle cx="70" cy="70" r="7" fill="none" stroke="#cbd5e1"/>
<line x1="70" y1="70" x2="76" y2="64" stroke="#3b82f6" stroke-width="1.5"/>
<polygon points="76,64 72,72 80,68" fill="#3b82f6"/>
</g>
<g>
<circle cx="120" cy="90" r="7" fill="none" stroke="#cbd5e1"/>
<line x1="120" y1="90" x2="126" y2="84" stroke="#3b82f6" stroke-width="1.5"/>
<polygon points="126,84 122,92 130,88" fill="#3b82f6"/>
</g>
<g>
<circle cx="170" cy="70" r="7" fill="none" stroke="#cbd5e1"/>
<line x1="170" y1="70" x2="176" y2="64" stroke="#3b82f6" stroke-width="1.5"/>
<polygon points="176,64 172,72 180,68" fill="#3b82f6"/>
</g>
<text x="80" y="145" font-size="10" fill="#475569">磁化：分子磁矩沿磁场方向排列</text></svg>''',
"dipole_field": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="95" cy="80" r="9" fill="#ef4444"/>
<text x="90" y="84" font-size="11" fill="#fff" font-weight="bold">+</text>
<circle cx="145" cy="80" r="9" fill="#3b82f6"/>
<text x="140" y="84" font-size="11" fill="#fff" font-weight="bold">−</text>
<path d="M 95 80 Q 120 30 145 80" fill="none" stroke="#3b82f6" stroke-width="1.2"/>
<path d="M 95 80 Q 120 130 145 80" fill="none" stroke="#3b82f6" stroke-width="1.2"/>
<path d="M 80 60 Q 60 80 80 100" fill="none" stroke="#3b82f6" stroke-width="1.2"/>
<path d="M 160 60 Q 180 80 160 100" fill="none" stroke="#3b82f6" stroke-width="1.2"/>
<polygon points="145,80 138,74 138,86" fill="#3b82f6"/>
<polygon points="95,80 102,74 102,86" fill="#3b82f6"/>
<line x1="120" y1="30" x2="120" y2="50" stroke="#10b981" stroke-width="2"/>
<polygon points="120,30 114,40 126,40" fill="#10b981"/>
<text x="125" y="38" font-size="11" fill="#10b981">p</text></svg>''',
"magnetic_moment": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="120" cy="80" rx="55" ry="30" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
<polygon points="175,80 167,76 167,84" fill="#3b82f6"/>
<text x="155" y="70" font-size="11" fill="#3b82f6">I</text>
<line x1="120" y1="80" x2="120" y2="35" stroke="#10b981" stroke-width="2"/>
<polygon points="120,35 114,45 126,45" fill="#10b981"/>
<text x="125" y="45" font-size="11" fill="#10b981">m</text>
<text x="80" y="130" font-size="10" fill="#475569">载流线圈的磁矩 m = ISn̂</text></svg>''',
"hysteresis": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="80" x2="220" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<line x1="120" y1="20" x2="120" y2="140" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 120 80 Q 160 30 200 50 Q 210 70 190 90 Q 160 130 120 80 Q 80 30 50 50 Q 40 70 60 90 Q 80 130 120 80 Z" fill="none" stroke="#be185d" stroke-width="2"/>
<text x="205" y="76" font-size="10" fill="#475569">H</text>
<text x="108" y="18" font-size="10" fill="#475569">B</text>
<circle cx="120" cy="50" r="2.5" fill="#475569"/>
<circle cx="120" cy="110" r="2.5" fill="#475569"/>
<text x="125" y="48" font-size="9" fill="#475569">Br</text>
<text x="125" y="120" font-size="9" fill="#475569">-Br</text></svg>''',
"mutual_induct": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 40 80 Q 60 50 80 80 Q 100 110 120 80" fill="none" stroke="#3b82f6" stroke-width="2"/>
<path d="M 120 80 Q 140 50 160 80 Q 180 110 200 80" fill="none" stroke="#ef4444" stroke-width="2"/>
<text x="20" y="130" font-size="11" fill="#3b82f6">线圈1 (I₁)</text>
<text x="150" y="130" font-size="11" fill="#ef4444">线圈2</text>
<line x1="80" y1="80" x2="160" y2="80" stroke="#10b981" stroke-width="1.2" stroke-dasharray="4 3"/>
<text x="108" y="72" font-size="10" fill="#10b981">Φ₁₂</text></svg>''',
"em_energy": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="10" y1="80" x2="230" y2="80" stroke="#cbd5e1" stroke-width="1"/>
<path d="M 10 80 Q 40 30 70 80 T 130 80 T 190 80 T 230 80" fill="none" stroke="#3b82f6" stroke-width="2"/>
<path d="M 10 80 Q 40 130 70 80 T 130 80 T 190 80 T 230 80" fill="none" stroke="#ef4444" stroke-width="2"/>
<line x1="70" y1="30" x2="70" y2="130" stroke="#10b981" stroke-width="1.5" stroke-dasharray="3 3"/>
<text x="20" y="26" font-size="10" fill="#3b82f6">E</text>
<text x="20" y="142" font-size="10" fill="#ef4444">B</text>
<text x="75" y="26" font-size="9" fill="#10b981">w=½(εE²+B²/μ)</text></svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

CORE_FORMULAS = [
    ("库仑定律", "\\mathbf{F} = \\frac{1}{4\\pi\\varepsilon_0}\\frac{q_1 q_2}{r^2}\\hat{\\mathbf{r}}", "真空中两点电荷间的作用力"),
    ("电场强度", "\\mathbf{E} = \\frac{\\mathbf{F}}{q_0} = \\frac{1}{4\\pi\\varepsilon_0}\\frac{q}{r^2}\\hat{\\mathbf{r}}", "单位正电荷所受的力"),
    ("电场通量", "\\Phi_e = \\oint_S \\mathbf{E}\\cdot d\\mathbf{S}", "电场穿过闭合曲面的通量"),
    ("高斯定理", "\\oint_S \\mathbf{E}\\cdot d\\mathbf{S} = \\frac{q_{\\text{内}}}{\\varepsilon_0}", "静电场的通量与包围电荷的关系"),
    ("电势", "V_a = \\int_a^{\\infty} \\mathbf{E}\\cdot d\\mathbf{l}", "单位正电荷在 a 点的电势能"),
    ("电场与电势", "\\mathbf{E} = -\\nabla V", "电场是电势的负梯度"),
    ("电容", "C = \\frac{Q}{V}", "导体储存电荷能力的量度"),
    ("电偶极矩", "\\mathbf{p} = q\\mathbf{d}", "等量异号电荷的偶极矩"),
    ("电位移矢量", "\\mathbf{D} = \\varepsilon_0\\mathbf{E} + \\mathbf{P}", "电位移矢量定义"),
    ("介质高斯定理", "\\oint_S \\mathbf{D}\\cdot d\\mathbf{S} = q_{0\\text{内}}", "电位移通量仅与自由电荷有关"),
    ("毕奥-萨伐尔定律", "d\\mathbf{B} = \\frac{\\mu_0}{4\\pi}\\frac{I d\\mathbf{l}\\times\\hat{\\mathbf{r}}}{r^2}", "电流元产生的磁场"),
    ("安培环路定理", "\\oint_L \\mathbf{B}\\cdot d\\mathbf{l} = \\mu_0 I_{\\text{内}}", "磁场的环流与穿过电流的关系"),
    ("洛伦兹力", "\\mathbf{F} = q(\\mathbf{E} + \\mathbf{v}\\times\\mathbf{B})", "带电粒子在电磁场中受的力"),
    ("安培力", "d\\mathbf{F} = I d\\mathbf{l}\\times\\mathbf{B}", "电流元在磁场中受的力"),
    ("磁矩", "\\mathbf{m} = I\\mathbf{S}", "载流线圈的磁矩"),
    ("磁场强度", "\\mathbf{H} = \\frac{\\mathbf{B}}{\\mu_0} - \\mathbf{M}", "磁场强度定义"),
    ("介质安培环路定理", "\\oint_L \\mathbf{H}\\cdot d\\mathbf{l} = I_{0\\text{内}}", "H 的环流仅与传导电流有关"),
    ("法拉第电磁感应", "\\varepsilon = -\\frac{d\\Phi}{dt}", "感应电动势等于磁通量变化率的负值"),
    ("动生电动势", "\\varepsilon = \\int (\\mathbf{v}\\times\\mathbf{B})\\cdot d\\mathbf{l}", "导体运动产生的电动势"),
    ("位移电流", "I_d = \\varepsilon_0\\frac{d\\Phi_e}{dt}", "变化电场等效的电流"),
    ("麦克斯韦方程组(微分)", "\\nabla\\cdot\\mathbf{E}=\\frac{\\rho}{\\varepsilon_0},\\ \\nabla\\cdot\\mathbf{B}=0,\\ \\nabla\\times\\mathbf{E}=-\\frac{\\partial\\mathbf{B}}{\\partial t},\\ \\nabla\\times\\mathbf{B}=\\mu_0\\mathbf{j}+\\mu_0\\varepsilon_0\\frac{\\partial\\mathbf{E}}{\\partial t}", "电磁场的基本方程"),
    ("电磁波速", "c = \\frac{1}{\\sqrt{\\mu_0\\varepsilon_0}}", "真空中电磁波的传播速度"),
    ("电磁波能流密度", "\\mathbf{S} = \\frac{1}{\\mu_0}\\mathbf{E}\\times\\mathbf{B}", "坡印廷矢量"),
    ("电偶极子远场电势", "V = \\frac{\\mathbf{p}\\cdot\\hat{\\mathbf{r}}}{4\\pi\\varepsilon_0 r^2}", "电偶极子在远区的电势"),
    ("电偶极子电场", "E_r=\\frac{2p\\cos\\theta}{4\\pi\\varepsilon_0 r^3},\\ E_\\theta=\\frac{p\\sin\\theta}{4\\pi\\varepsilon_0 r^3}", "偶极子远场电场分量"),
    ("偶极子力矩", "\\boldsymbol{\\tau}=\\mathbf{p}\\times\\mathbf{E}", "电偶极子在均匀电场中受力矩"),
    ("静电场边界条件", "D_{2n}-D_{1n}=\\sigma_f,\\ E_{2t}=E_{1t}", "介质分界面上 D 的法向与 E 的切向跃变"),
    ("磁矩", "\\mathbf{m}=IS\\hat{\\mathbf{n}}", "载流线圈的磁矩"),
    ("磁力矩", "\\boldsymbol{\\tau}=\\mathbf{m}\\times\\mathbf{B}", "载流线圈在磁场中受力矩"),
    ("磁滞回线", "B_r=B(H=0),\\ H_c=|H(B=0)|", "剩磁与矫顽力"),
    ("自感电动势", "\\varepsilon_L=-L\\frac{dI}{dt}", "自感系数与自感电动势"),
    ("互感电动势", "\\varepsilon_{21}=-M\\frac{dI_1}{dt}", "互感系数与互感电动势"),
    ("电磁场能量密度", "w=\\frac{1}{2}\\varepsilon E^2+\\frac{1}{2\\mu}B^2", "电场与磁场能量密度之和"),
    ("连续带电体电场", "\\mathbf{E}=\\frac{1}{4\\pi\\varepsilon_0}\\int\\frac{dq}{r^2}\\hat{\\mathbf{r}}", "由电荷元电场叠加积分"),
    ("均匀带电圆盘轴线电场", "E=\\frac{\\sigma}{2\\varepsilon_0}\\left(1-\\frac{x}{\\sqrt{R^2+x^2}}\\right)", "带电圆盘轴线上电场，R→∞ 得无限大平面场"),
    ("电势叠加原理", "V=\\frac{1}{4\\pi\\varepsilon_0}\\sum_i\\frac{q_i}{r_i}", "多个点电荷电势的代数叠加"),
    ("均匀带电球面电势", "V_{\\text{内}}=\\frac{q}{4\\pi\\varepsilon_0 R},\\ V_{\\text{外}}=\\frac{q}{4\\pi\\varepsilon_0 r}", "球面内部等势，外部同点电荷"),
    ("偶极子非均匀场受力", "\\mathbf{F}=(\\mathbf{p}\\cdot\\nabla)\\mathbf{E}", "电偶极子在非均匀电场中受力"),
    ("电四极子远场电势", "V=\\frac{1}{4\\pi\\varepsilon_0}\\frac{Q(3\\cos^2\\theta-1)}{2r^3}", "线性电四极子远场电势，按 1/r³ 衰减"),
    ("电场力做功", "A_{ab}=q_0\\int_a^b\\mathbf{E}\\cdot d\\mathbf{l}", "静电场力做功与路径无关"),
    ("泊松方程", "\\nabla^2 V=-\\frac{\\rho}{\\varepsilon}", "静电势满足的微分方程"),
    ("束缚电荷体密度", "\\rho'=-\\nabla\\cdot\\mathbf{P}", "极化强度的散度等于束缚电荷体密度的负值"),
    ("介质电场能量密度", "w_e=\\frac{1}{2}\\mathbf{D}\\cdot\\mathbf{E}", "电介质中的电场能量密度"),
    ("电场线折射定律", "\\frac{\\tan\\theta_1}{\\tan\\theta_2}=\\frac{\\varepsilon_1}{\\varepsilon_2}", "电场线在介质界面的折射"),
    ("载流直导线磁场", "B=\\frac{\\mu_0 I}{4\\pi a}(\\sin\\beta_2-\\sin\\beta_1)", "有限长直导线的磁场"),
    ("载流螺线管磁场", "B=\\frac{\\mu_0 nI}{2}(\\cos\\beta_1-\\cos\\beta_2)", "直螺线管轴线上的磁场"),
    ("运动电荷磁场", "\\mathbf{B}=\\frac{\\mu_0}{4\\pi}\\frac{q\\mathbf{v}\\times\\hat{\\mathbf{r}}}{r^2}", "匀速运动点电荷产生的磁场"),
    ("磁场高斯定理", "\\oint_S\\mathbf{B}\\cdot d\\mathbf{S}=0", "穿过闭合曲面的磁通量恒为零"),
    ("平行载流导线作用力", "\\frac{dF}{dl}=\\frac{\\mu_0 I_1 I_2}{2\\pi a}", "单位长度平行载流导线间的作用力"),
    ("拉莫尔进动频率", "\\omega_L=\\gamma B", "磁矩在外磁场中的进动角速度"),
    ("带电粒子回旋半径", "R=\\frac{mv_\\perp}{qB}", "带电粒子在磁场中做圆周运动的半径"),
    ("磁化电流体密度", "\\mathbf{j}'=\\nabla\\times\\mathbf{M}", "磁化强度的旋度等于束缚电流体密度"),
    ("磁路欧姆定律", "\\Phi=\\frac{F_m}{R_m},\\ R_m=\\frac{l}{\\mu S}", "磁通量、磁通势与磁阻的关系"),
    ("静磁场边界条件", "B_{1n}=B_{2n},\\ H_{2t}-H_{1t}=\\alpha_f", "B 法向连续，H 切向跃变"),
    ("楞次定律", "\\varepsilon=-\\frac{d\\Phi}{dt}", "感应电动势阻碍磁通量变化"),
    ("动生电动势", "\\varepsilon=\\int(\\mathbf{v}\\times\\mathbf{B})\\cdot d\\mathbf{l}", "导体运动切割磁力线产生的电动势"),
    ("RL 电路电流增长", "I(t)=\\frac{\\mathcal{E}}{R}(1-e^{-t/\\tau})", "RL 电路接通电源后的暂态电流"),
    ("全电流定律", "\\oint\\mathbf{H}\\cdot d\\mathbf{l}=I_c+\\frac{d\\Phi_D}{dt}", "传导电流与位移电流之和的安培环路定理"),
    ("电偶极辐射功率", "\\bar{P}=\\frac{\\mu_0 p_0^2\\omega^4}{12\\pi c}", "振荡电偶极子的平均辐射功率"),
    ("电磁波动量密度", "\\mathbf{g}=\\frac{1}{c^2}\\mathbf{S}=\\varepsilon_0\\mathbf{E}\\times\\mathbf{B}", "电磁场单位体积的动量"),
    ("光压", "P_{\\text{吸收}}=\\frac{I}{c},\\ P_{\\text{反射}}=\\frac{2I}{c}", "电磁波照射物体产生的辐射压强"),
    ("矢势与标势", "\\mathbf{B}=\\nabla\\times\\mathbf{A},\\ \\mathbf{E}=-\\nabla\\varphi-\\frac{\\partial\\mathbf{A}}{\\partial t}", "用势函数描述电磁场"),
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
#  CHAPTER 1: 静电场
# =====================================================
ch1_sections = [
{
"name": "1.1 库仑定律与电场强度",
"color": "#2563eb",
"desc": "库仑定律、电场强度与叠加原理",
"items": [
{"id":"e1s1-1","name":"库仑定律","tags":["def","thm"],"brief":"真空中两点电荷间的相互作用力。",
 "fig":"pointcharge","figCap":"正点电荷的电场线",
 "body": wrap(
   defn("库仑定律",p("真空中两个静止点电荷 $q_1,q_2$ 之间的相互作用力大小与电量乘积成正比，与距离平方成反比，方向沿连线：")+
   fml("\\mathbf{F} = \\frac{1}{4\\pi\\varepsilon_0}\\frac{q_1 q_2}{r^2}\\hat{\\mathbf{r}}")+
   p("其中 $\\varepsilon_0=8.85\\times10^{-12}\\,\\text{C}^2/(\\text{N}\\cdot\\text{m}^2)$ 为真空介电常数。"))+
   defn("电场强度",p("电场中某点的电场强度等于单位正试探电荷在该点所受的力：$\\mathbf{E}=\\mathbf{F}/q_0$。点电荷的电场：")+
   fml("\\mathbf{E} = \\frac{1}{4\\pi\\varepsilon_0}\\frac{q}{r^2}\\hat{\\mathbf{r}}"))+
   thm("叠加原理",p("多个点电荷产生的电场为各点电荷单独产生电场的矢量和：")+
   fml("\\mathbf{E} = \\sum_i \\mathbf{E}_i = \\frac{1}{4\\pi\\varepsilon_0}\\sum_i \\frac{q_i}{r_i^2}\\hat{\\mathbf{r}}_i"))
 )},
]},
{
"name": "1.2 高斯定理",
"color": "#2563eb",
"desc": "电场的通量定理及其应用",
"items": [
{"id":"e1s2-1","name":"高斯定理","tags":["thm","der"],"brief":"静电场的通量与包围电荷的关系。",
 "fig":"gauss","figCap":"点电荷的高斯面",
 "body": wrap(
   defn("电通量",p("电场穿过曲面 $S$ 的电通量：$\\Phi_e=\\int_S\\mathbf{E}\\cdot d\\mathbf{S}$。"))+
   thm("高斯定理",p("真空中静电场通过任意闭合曲面的电通量等于该曲面包围的电荷代数和除以 $\\varepsilon_0$：")+
   fml("\\oint_S \\mathbf{E}\\cdot d\\mathbf{S} = \\frac{1}{\\varepsilon_0}\\sum_i q_{i\\text{内}}"))+
   der(p("<strong>推导（点电荷情形）：</strong>点电荷 $q$ 位于闭合球面 $S$ 中心，球面上 $E=\\frac{q}{4\\pi\\varepsilon_0 r^2}$ 且沿径向，$\\mathbf{E}\\parallel d\\mathbf{S}$：")+
   fml("\\oint_S \\mathbf{E}\\cdot d\\mathbf{S} = \\oint_S E\\,dS = \\frac{q}{4\\pi\\varepsilon_0 r^2}\\cdot 4\\pi r^2 = \\frac{q}{\\varepsilon_0}")+
   p("对任意闭合曲面，利用立体角可证结果相同；多个电荷由叠加原理得 $\\sum q_{\\text{内}}/\\varepsilon_0$。"))+
   app(p("<strong>应用：</strong>利用对称性求电场。如无限长带电直线 $E=\\frac{\\lambda}{2\\pi\\varepsilon_0 r}$，无限大带电平面 $E=\\frac{\\sigma}{2\\varepsilon_0}$，均匀带电球面内部 $E=0$、外部 $E=\\frac{q}{4\\pi\\varepsilon_0 r^2}$。"))
 )},
]},
{
"name": "1.3 电势与电势能",
"color": "#2563eb",
"desc": "环路定理、电势、电场与电势的关系",
"items": [
{"id":"e1s3-1","name":"电势与电场的梯度关系","tags":["thm","der"],"brief":"静电场是保守场，可引入电势。",
 "body": wrap(
   thm("静电场环路定理",p("静电场沿任意闭合回路的环流为零：$\\oint_L\\mathbf{E}\\cdot d\\mathbf{l}=0$，故静电场是保守场。")+
   fml("\\nabla\\times\\mathbf{E} = 0"))+
   defn("电势",p("选无穷远为零势点，$a$ 点电势：")+
   fml("V_a = \\int_a^{\\infty} \\mathbf{E}\\cdot d\\mathbf{l}")+
   p("点电荷的电势 $V=\\frac{q}{4\\pi\\varepsilon_0 r}$。"))+
   der(p("<strong>电场与电势的关系：</strong>由保守场性质，$\\mathbf{E}$ 可表示为某标量函数的负梯度。设 $V$ 为电势，则：")+
   fml("dV = -\\mathbf{E}\\cdot d\\mathbf{l} = -(E_x dx + E_y dy + E_z dz)")+
   p("而全微分 $dV=\\frac{\\partial V}{\\partial x}dx+\\frac{\\partial V}{\\partial y}dy+\\frac{\\partial V}{\\partial z}dz$，比较得：")+
   fml("E_x=-\\frac{\\partial V}{\\partial x},\\quad E_y=-\\frac{\\partial V}{\\partial y},\\quad E_z=-\\frac{\\partial V}{\\partial z} \\implies \\mathbf{E}=-\\nabla V"))
 )},
]},
{
"name": "1.4 电容与电容器",
"color": "#2563eb",
"desc": "电容的定义与平行板电容器",
"items": [
{"id":"e1s4-1","name":"电容与平行板电容器","tags":["def","der"],"brief":"导体储存电荷的能力。",
 "fig":"capacitor","figCap":"平行板电容器",
 "body": wrap(
   defn("电容",p("孤立导体的电容 $C=Q/V$。电容器的电容 $C=Q/(V_1-V_2)$，仅与几何形状和介质有关。"))+
   der(p("<strong>平行板电容器电容推导：</strong>极板面积 $S$，间距 $d$，带电量 $\\pm Q$，面电荷密度 $\\sigma=Q/S$。忽略边缘效应，极板间电场 $E=\\sigma/\\varepsilon_0=Q/(\\varepsilon_0 S)$。")+
   p("电势差 $V=Ed=Qd/(\\varepsilon_0 S)$，故：")+
   fml("C = \\frac{Q}{V} = \\frac{\\varepsilon_0 S}{d}"))+
   note(p("球形电容器 $C=4\\pi\\varepsilon_0\\frac{R_1 R_2}{R_2-R_1}$；圆柱形电容器单位长度电容 $C/L=\\frac{2\\pi\\varepsilon_0}{\\ln(R_2/R_1)}$。"))
 )},
]},
{
"name": "1.5 电偶极子的电场与力矩",
"color": "#2563eb",
"desc": "电偶极子的远场电势、电场及在外场中的受力矩",
"items": [
{"id":"e1s5-1","name":"电偶极子的远场","tags":["thm","der"],"brief":"电偶极子在远区产生的电势与电场。",
 "fig":"dipole_field","figCap":"电偶极子的电场线分布",
 "body": wrap(
   defn("电偶极子",p("电偶极矩 $\\mathbf{p}=q\\mathbf{d}$，取偶极子中心为原点，$\\mathbf{p}$ 沿 $z$ 轴。远区条件 $r\\gg d$。"))+
   der(p("<strong>远场电势推导：</strong>正、负电荷到场点 $P(r,\\theta)$ 的距离分别为 $r_+\\approx r-\\frac{d}{2}\\cos\\theta$，$r_-\\approx r+\\frac{d}{2}\\cos\\theta$。电势叠加：")+
   fml("V = \\frac{q}{4\\pi\\varepsilon_0}\\left(\\frac{1}{r_+}-\\frac{1}{r_-}\\right) \\approx \\frac{q}{4\\pi\\varepsilon_0}\\frac{d\\cos\\theta}{r^2}")+
   fml("V = \\frac{\\mathbf{p}\\cdot\\hat{\\mathbf{r}}}{4\\pi\\varepsilon_0 r^2} = \\frac{p\\cos\\theta}{4\\pi\\varepsilon_0 r^2}")+
   p("<strong>电场分量：</strong>由 $\\mathbf{E}=-\\nabla V$，球坐标下：")+
   fml("E_r = -\\frac{\\partial V}{\\partial r} = \\frac{2p\\cos\\theta}{4\\pi\\varepsilon_0 r^3},\\quad E_\\theta = -\\frac{1}{r}\\frac{\\partial V}{\\partial\\theta} = \\frac{p\\sin\\theta}{4\\pi\\varepsilon_0 r^3}")+
   p("电场随 $1/r^3$ 衰减，比点电荷的 $1/r^2$ 更快。"))+
   thm("偶极子在外电场中受力矩",p("电偶极子在均匀外场 $\\mathbf{E}$ 中受力为零，但受力矩：")+
   fml("\\boldsymbol{\\tau} = \\mathbf{p}\\times\\mathbf{E}")+
   p("力矩使 $\\mathbf{p}$ 转向 $\\mathbf{E}$ 方向。势能 $U=-\\mathbf{p}\\cdot\\mathbf{E}$。"))
 )},
]},
{
"name": "1.6 电场叠加原理与连续带电体电场",
"color": "#2563eb",
"desc": "电场叠加原理及连续带电体的电场计算",
"items": [
{"id":"e1s6-1","name":"电场叠加原理","tags":["thm"],"brief":"多个点电荷产生的电场为各电荷单独产生电场的矢量和。",
 "body": wrap(
   thm("电场叠加原理",p("当空间存在多个点电荷时，任一点的电场强度等于各点电荷单独存在时在该点产生电场的矢量和：")+
   fml("\\mathbf{E} = \\sum_{i=1}^{n} \\mathbf{E}_i = \\frac{1}{4\\pi\\varepsilon_0}\\sum_{i=1}^{n} \\frac{q_i}{r_i^2}\\hat{\\mathbf{r}}_i"))+
   der(p("<strong>叠加原理的物理意义：</strong>电场是矢量场，满足线性叠加。这一原理是库仑定律与力的独立作用原理的直接推论，是计算任意电荷分布电场的基础。对连续带电体，将电荷分为无数电荷元 $dq$，每个电荷元视为点电荷，则：")+
   fml("\\mathbf{E} = \\int d\\mathbf{E} = \\frac{1}{4\\pi\\varepsilon_0}\\int \\frac{dq}{r^2}\\hat{\\mathbf{r}}")+
   p("其中 $r$ 是电荷元到场点的距离，$\\hat{\\mathbf{r}}$ 由电荷元指向场点。"))
 )},
{"id":"e1s6-2","name":"连续带电体的电场","tags":["def","der"],"brief":"线电荷、面电荷、体电荷分布的电场计算。",
 "body": wrap(
   defn("电荷分布的描述",p("电荷连续分布时，引入电荷密度：线密度 $\\lambda=dq/dl$，面密度 $\\sigma=dq/dS$，体密度 $\\rho=dq/dV$。对应 $dq=\\lambda dl,\\ \\sigma dS,\\ \\rho dV$。"))+
   der(p("<strong>均匀带电直线的电场：</strong>长为 $L$ 的带电直线，线密度 $\\lambda$，中垂线上距直线 $a$ 处。由对称性，平行于直线的分量抵消，垂直分量叠加：")+
   fml("E = \\int_{-L/2}^{L/2} \\frac{1}{4\\pi\\varepsilon_0}\\frac{\\lambda dy}{a^2+y^2}\\cdot\\frac{a}{\\sqrt{a^2+y^2}}")+
   fml("E = \\frac{\\lambda}{4\\pi\\varepsilon_0 a}\\cdot\\frac{L}{\\sqrt{a^2+(L/2)^2}}")+
   p("无限长时 $L\\to\\infty$，$E=\\frac{\\lambda}{2\\pi\\varepsilon_0 a}$。"))
 )},
{"id":"e1s6-3","name":"均匀带电圆环与圆盘的电场","tags":["der"],"brief":"轴对称带电体轴线上的电场分布。",
 "body": wrap(
   der(p("<strong>均匀带电圆环轴线上的电场：</strong>半径 $R$，电量 $q$，轴线上距圆心 $x$ 处。由对称性，垂直轴线分量抵消，平行分量叠加。每个电荷元 $dq$ 到场点距离 $r=\\sqrt{R^2+x^2}$：")+
   fml("E = \\oint \\frac{1}{4\\pi\\varepsilon_0}\\frac{dq}{R^2+x^2}\\cdot\\frac{x}{\\sqrt{R^2+x^2}} = \\frac{1}{4\\pi\\varepsilon_0}\\frac{qx}{(R^2+x^2)^{3/2}}")+
   p("圆心处 $x=0$，$E=0$；远场 $x\\gg R$，$E\\approx\\frac{q}{4\\pi\\varepsilon_0 x^2}$，退化为点电荷。")+
   p("<strong>均匀带电圆盘轴线上的电场：</strong>面密度 $\\sigma$，将圆盘分为无数细圆环，半径 $r$，宽度 $dr$，带电量 $dq=2\\pi r\\sigma dr$：")+
   fml("E = \\int_0^R \\frac{1}{4\\pi\\varepsilon_0}\\frac{2\\pi r\\sigma dr\\cdot x}{(r^2+x^2)^{3/2}} = \\frac{\\sigma}{2\\varepsilon_0}\\left(1-\\frac{x}{\\sqrt{R^2+x^2}}\\right)")+
   p("无限大平面 $R\\to\\infty$，$E=\\frac{\\sigma}{2\\varepsilon_0}$，为匀强电场。"))
 )},
]},
{
"name": "1.7 电场线与电通量",
"color": "#2563eb",
"desc": "电场线的性质与电通量的计算",
"items": [
{"id":"e1s7-1","name":"电场线与电通量","tags":["def","thm"],"brief":"电场线的几何描述与电通量的物理意义。",
 "body": wrap(
   defn("电场线",p("电场线是描述电场分布的几何曲线，规定：(1) 切线方向为该点电场方向；(2) 垂直通过单位面积的电场线数正比于电场强度大小。电场线起始于正电荷，终止于负电荷，不闭合、不相交。"))+
   defn("电通量",p("电场穿过曲面 $S$ 的电通量为电场强度在曲面法向上的分量对面积的积分：")+
   fml("\\Phi_e = \\int_S \\mathbf{E}\\cdot d\\mathbf{S} = \\int_S E\\cos\\theta\\,dS")+
   p("对闭合曲面，规定外法线方向为正方向，$\\Phi_e=\\oint_S\\mathbf{E}\\cdot d\\mathbf{S}$。"))+
   thm("电场线与电通量的关系",p("穿过闭合曲面的电场线净条数（穿出减穿入）正比于电通量。正电荷发出的电场线数为 $q/\\varepsilon_0$，负电荷接收的电场线数为 $|q|/\\varepsilon_0$。电场线的连续性反映了高斯定理。"))
 )},
]},
{
"name": "1.8 电势的计算与叠加",
"color": "#2563eb",
"desc": "电势叠加原理与常见带电体的电势",
"items": [
{"id":"e1s8-1","name":"电势叠加原理","tags":["thm","der"],"brief":"电势为标量，满足代数叠加。",
 "body": wrap(
   thm("电势叠加原理",p("多个点电荷产生的电势等于各点电荷单独产生电势的代数和（标量叠加）：")+
   fml("V = \\sum_i V_i = \\frac{1}{4\\pi\\varepsilon_0}\\sum_i \\frac{q_i}{r_i}"))+
   der(p("<strong>推导：</strong>由电场叠加原理 $\\mathbf{E}=\\sum\\mathbf{E}_i$，电势定义 $V=\\int_a^{\\infty}\\mathbf{E}\\cdot d\\mathbf{l}$，积分是线性的，故：")+
   fml("V = \\int_a^{\\infty}\\sum_i\\mathbf{E}_i\\cdot d\\mathbf{l} = \\sum_i\\int_a^{\\infty}\\mathbf{E}_i\\cdot d\\mathbf{l} = \\sum_i V_i")+
   p("对连续带电体，$V=\\frac{1}{4\\pi\\varepsilon_0}\\int\\frac{dq}{r}$。电势是标量，叠加比电场矢量叠加更简单。"))
 )},
{"id":"e1s8-2","name":"等势面与电势的计算示例","tags":["def","exa"],"brief":"等势面的性质与典型带电体电势。",
 "body": wrap(
   defn("等势面",p("电场中电势相等的点构成的曲面称为等势面。等势面与电场线处处正交；等势面密集处电场强，稀疏处电场弱；沿等势面移动电荷电场力不做功。"))+
   exa(p("<strong>典型带电体的电势：</strong>")+
   p("(1) 点电荷：$V=\\frac{q}{4\\pi\\varepsilon_0 r}$")+
   p("(2) 均匀带电球面（半径 $R$，电量 $q$）：内部 $V=\\frac{q}{4\\pi\\varepsilon_0 R}$（等势），外部 $V=\\frac{q}{4\\pi\\varepsilon_0 r}$")+
   p("(3) 均匀带电球体（半径 $R$，电量 $q$）：内部 $V=\\frac{q}{8\\pi\\varepsilon_0 R^3}(3R^2-r^2)$，外部 $V=\\frac{q}{4\\pi\\varepsilon_0 r}$")+
   p("(4) 无限长带电直线：$V=-\\frac{\\lambda}{2\\pi\\varepsilon_0}\\ln r+C$（取有限远为参考点）"))
 )},
]},
{
"name": "1.9 电场强度与电势的微分关系",
"color": "#2563eb",
"desc": "由电势求电场强度的梯度方法",
"items": [
{"id":"e1s9-1","name":"电场强度与电势的梯度关系","tags":["thm","der"],"brief":"电场是电势的负梯度。",
 "body": wrap(
   thm("电场与电势的关系",p("电场强度等于电势的负梯度：")+
   fml("\\mathbf{E} = -\\nabla V = -\\left(\\frac{\\partial V}{\\partial x}\\mathbf{i}+\\frac{\\partial V}{\\partial y}\\mathbf{j}+\\frac{\\partial V}{\\partial z}\\mathbf{k}\\right)"))+
   der(p("<strong>推导：</strong>在电场中取位移元 $d\\mathbf{l}$，电势变化 $dV=-\\mathbf{E}\\cdot d\\mathbf{l}$。在直角坐标系中 $d\\mathbf{l}=dx\\mathbf{i}+dy\\mathbf{j}+dz\\mathbf{k}$，故：")+
   fml("dV = -(E_x dx + E_y dy + E_z dz)")+
   p("而 $V$ 的全微分为 $dV=\\frac{\\partial V}{\\partial x}dx+\\frac{\\partial V}{\\partial y}dy+\\frac{\\partial V}{\\partial z}dz$，比较系数得：")+
   fml("E_x=-\\frac{\\partial V}{\\partial x},\\quad E_y=-\\frac{\\partial V}{\\partial y},\\quad E_z=-\\frac{\\partial V}{\\partial z}")+
   p("即 $\\mathbf{E}=-\\nabla V$。在球坐标中，$E_r=-\\frac{\\partial V}{\\partial r}$，$E_\\theta=-\\frac{1}{r}\\frac{\\partial V}{\\partial\\theta}$，$E_\\varphi=-\\frac{1}{r\\sin\\theta}\\frac{\\partial V}{\\partial\\varphi}$。"))+
   app(p("<strong>应用：</strong>先求电势（标量叠加较易），再求梯度得电场。如电偶极子电势 $V=\\frac{p\\cos\\theta}{4\\pi\\varepsilon_0 r^2}$，求梯度得 $E_r=\\frac{2p\\cos\\theta}{4\\pi\\varepsilon_0 r^3}$，$E_\\theta=\\frac{p\\sin\\theta}{4\\pi\\varepsilon_0 r^3}$。"))
 )},
]},
{
"name": "1.10 电偶极子与电四极子",
"color": "#2563eb",
"desc": "电偶极子的受力、电四极子的电场",
"items": [
{"id":"e1s10-1","name":"电偶极子在外电场中的受力与能量","tags":["der"],"brief":"非均匀电场中偶极子受力及势能。",
 "body": wrap(
   der(p("<strong>非均匀电场中偶极子受力：</strong>电偶极子 $\\mathbf{p}=q\\mathbf{d}$ 位于非均匀电场中。设正电荷处电场为 $\\mathbf{E}_+$，负电荷处为 $\\mathbf{E}_-$，受力：")+
   fml("\\mathbf{F} = q\\mathbf{E}_+ - q\\mathbf{E}_- = q(\\mathbf{E}_+ - \\mathbf{E}_-)")+
   p("由于 $\\mathbf{d}$ 很小，$\\mathbf{E}_+-\\mathbf{E}_-=(\\mathbf{d}\\cdot\\nabla)\\mathbf{E}$，故：")+
   fml("\\mathbf{F} = (\\mathbf{p}\\cdot\\nabla)\\mathbf{E}")+
   p("在均匀电场中受力为零。")+
   p("<strong>电偶极子的势能：</strong>将偶极子从 $\\mathbf{E}$ 垂直方向转到与 $\\mathbf{E}$ 成 $\\theta$ 角，外力克服力矩做功：")+
   fml("U = -\\mathbf{p}\\cdot\\mathbf{E} = -pE\\cos\\theta")+
   p("当 $\\mathbf{p}$ 与 $\\mathbf{E}$ 平行时势能最小（稳定平衡），反平行时势能最大。"))
 )},
{"id":"e1s10-2","name":"电四极子","tags":["def","der"],"brief":"两个反向偶极子构成的电四极子及其远场电势。",
 "body": wrap(
   defn("电四极子",p("电四极子由两个大小相等、方向相反、相距很近的电偶极子构成，总电荷为零，总偶极矩为零。最简单的线性电四极子由四个电荷 $+q,-2q,+q$ 等间距排列构成。"))+
   der(p("<strong>线性电四极子的远场电势：</strong>四个电荷位于 $z$ 轴上：$+q$ 在 $z=\\pm l$，$-2q$ 在 $z=0$。远场 $r\\gg l$，电势叠加：")+
   fml("V = \\frac{q}{4\\pi\\varepsilon_0}\\left(\\frac{1}{r_1}+\\frac{1}{r_2}-\\frac{2}{r}\\right)")+
   p("其中 $r_1\\approx r-l\\cos\\theta$，$r_2\\approx r+l\\cos\\theta$。展开 $1/r_1,1/r_2$ 到 $l^2$ 阶：")+
   fml("V \\approx \\frac{q l^2}{4\\pi\\varepsilon_0}\\frac{(3\\cos^2\\theta-1)}{r^3} = \\frac{1}{4\\pi\\varepsilon_0}\\frac{Q(3\\cos^2\\theta-1)}{2r^3}")+
   p("其中电四极矩 $Q=2ql^2$。四极子电势按 $1/r^3$ 衰减，电场按 $1/r^4$ 衰减。"))
 )},
]},
{
"name": "1.11 静电场的功与电势能",
"color": "#2563eb",
"desc": "电场力做功的特点与电势能",
"items": [
{"id":"e1s11-1","name":"静电场力做功与电势能","tags":["thm","der"],"brief":"静电场力做功与路径无关，可引入电势能。",
 "body": wrap(
   thm("静电场力做功的特点",p("试验电荷 $q_0$ 在静电场中从 $a$ 移到 $b$，电场力做功仅与始末位置有关，与路径无关：")+
   fml("A_{ab} = q_0\\int_a^b \\mathbf{E}\\cdot d\\mathbf{l}"))+
   der(p("<strong>推导：</strong>点电荷的电场 $\\mathbf{E}=\\frac{q}{4\\pi\\varepsilon_0 r^2}\\hat{\\mathbf{r}}$，电场力做功：")+
   fml("A_{ab} = q_0\\int_a^b \\frac{q}{4\\pi\\varepsilon_0 r^2}\\hat{\\mathbf{r}}\\cdot d\\mathbf{l} = \\frac{q_0 q}{4\\pi\\varepsilon_0}\\int_{r_a}^{r_b}\\frac{dr}{r^2}")+
   fml("A_{ab} = \\frac{q_0 q}{4\\pi\\varepsilon_0}\\left(\\frac{1}{r_a}-\\frac{1}{r_b}\\right)")+
   p("结果只与 $r_a,r_b$ 有关，与路径无关。由叠加原理，任意静电场的电场力做功都与路径无关，故静电场是保守场。"))+
   defn("电势能",p("电荷在电场中具有势能，称为电势能。$q_0$ 在 $a$ 点的电势能 $W_a$ 等于将 $q_0$ 从 $a$ 移到零势能点电场力做的功：$W_a=q_0\\int_a^{\\infty}\\mathbf{E}\\cdot d\\mathbf{l}=q_0 V_a$。电场力做功等于电势能的减少：$A_{ab}=W_a-W_b$。"))
 )},
]},
{
"name": "1.12 静电场的唯一性定理与导体静电平衡",
"color": "#2563eb",
"desc": "静电场边值问题的唯一性与导体静电平衡条件",
"items": [
{"id":"e1s12-1","name":"静电场的唯一性定理","tags":["thm"],"brief":"给定边界条件，静电场的解唯一。",
 "body": wrap(
   thm("唯一性定理",p("在给定区域 $V$ 内，若满足以下条件之一，则区域内的静电场唯一确定：(1) 边界上的电势 $V|_S$ 已知（第一类边界条件）；(2) 边界上的电势法向导数 $\\partial V/\\partial n|_S$ 已知（第二类边界条件）；(3) 部分边界已知 $V$，其余已知 $\\partial V/\\partial n$（混合边界条件）。")+
   fml("\\nabla^2 V = -\\frac{\\rho}{\\varepsilon}"))+
   der(p("<strong>证明思路：</strong>反证法。设有两个解 $V_1,V_2$ 满足同一泊松方程和边界条件，令 $U=V_1-V_2$，则 $\\nabla^2 U=0$（拉普拉斯方程）且 $U$ 在边界上满足齐次条件。由格林第一恒等式可证 $\\int_V|\\nabla U|^2 dV=0$，故 $\\nabla U=0$，$U$ 为常数。若边界 $V$ 已知则 $U=0$；若边界 $\\partial V/\\partial n$ 已知则常数可取零。故解唯一。"))
 )},
{"id":"e1s12-2","name":"导体的静电平衡","tags":["def","thm"],"brief":"导体内部电场为零，电荷分布在表面。",
 "body": wrap(
   defn("静电平衡",p("导体内部没有电荷定向运动的状态称为静电平衡。达到静电平衡的条件是：(1) 导体内部电场强度处处为零；(2) 导体表面外侧电场垂直于表面。"))+
   thm("静电平衡导体的性质",p("(1) 导体是等势体，表面是等势面；(2) 导体内部无净电荷，电荷只分布在表面；(3) 导体表面外侧电场 $E=\\sigma/\\varepsilon_0$，方向垂直表面；(4) 孤立导体表面电荷密度与曲率有关，曲率大处电荷密度大。")+
   p("<strong>空腔导体（静电屏蔽）：</strong>若空腔内无电荷，导体壳外表面电荷分布不影响空腔内部，腔内电场为零。若空腔内有电荷 $q$，则内表面感应出 $-q$，外表面感应出 $+q$（若导体原本不带电）。接地导体壳可屏蔽内部电荷对外的影响。"))
 )},
]},
]

# =====================================================
#  CHAPTER 2: 介质中的静电场
# =====================================================
ch2_sections = [
{
"name": "2.1 电介质的极化",
"color": "#0d9488",
"desc": "电偶极子、极化强度与束缚电荷",
"items": [
{"id":"e2s1-1","name":"电介质极化","tags":["def","der"],"brief":"电介质在电场中产生极化电荷。",
 "fig":"dielectric","figCap":"电介质的极化示意图",
 "body": wrap(
   defn("电偶极矩",p("两个相距 $d$ 的等量异号电荷 $\\pm q$ 构成电偶极子，电偶极矩 $\\mathbf{p}=q\\mathbf{d}$（方向由负电荷指向正电荷）。"))+
   defn("极化强度",p("单位体积内电偶极矩的矢量和：$\\mathbf{P}=\\frac{\\sum\\mathbf{p}_i}{\\Delta V}$。"))+
   der(p("<strong>束缚电荷面密度：</strong>在电介质表面取面元 $d\\mathbf{S}=\\mathbf{n}dS$，极化时穿过面元的束缚电荷 $dq'=\\mathbf{P}\\cdot d\\mathbf{S}$。故束缚电荷面密度：")+
   fml("\\sigma' = \\mathbf{P}\\cdot\\mathbf{n}")+
   p("束缚电荷体密度 $\\rho'=-\\nabla\\cdot\\mathbf{P}$。"))
 )},
]},
{
"name": "2.2 电位移矢量与介质高斯定理",
"color": "#0d9488",
"desc": "D 矢量的引入与介质中的高斯定理",
"items": [
{"id":"e2s2-1","name":"电位移矢量","tags":["thm","der"],"brief":"将束缚电荷吸收进 D 矢量。",
 "body": wrap(
   defn("电位移矢量",p("定义 $\\mathbf{D}=\\varepsilon_0\\mathbf{E}+\\mathbf{P}$。对线性各向同性电介质，$\\mathbf{P}=\\varepsilon_0\\chi_e\\mathbf{E}$，故：")+
   fml("\\mathbf{D} = \\varepsilon_0(1+\\chi_e)\\mathbf{E} = \\varepsilon_0\\varepsilon_r\\mathbf{E} = \\varepsilon\\mathbf{E}")+
   p("其中 $\\varepsilon_r=1+\\chi_e$ 为相对介电常数，$\\varepsilon=\\varepsilon_0\\varepsilon_r$ 为介电常数。"))+
   thm("介质中的高斯定理",p("电位移矢量通过任意闭合曲面的通量等于曲面内自由电荷的代数和：")+
   fml("\\oint_S \\mathbf{D}\\cdot d\\mathbf{S} = \\sum q_{0\\text{内}}"))+
   der(p("<strong>推导：</strong>真空中高斯定理 $\\oint\\mathbf{E}\\cdot d\\mathbf{S}=(q_0+q')/\\varepsilon_0$，其中 $q'=-\\oint\\mathbf{P}\\cdot d\\mathbf{S}$（束缚电荷）。代入：")+
   fml("\\oint\\varepsilon_0\\mathbf{E}\\cdot d\\mathbf{S} = q_0 - \\oint\\mathbf{P}\\cdot d\\mathbf{S}")+
   fml("\\oint(\\varepsilon_0\\mathbf{E}+\\mathbf{P})\\cdot d\\mathbf{S} = q_0 \\implies \\oint\\mathbf{D}\\cdot d\\mathbf{S} = q_0"))
 )},
]},
{
"name": "2.3 静电场的边界条件",
"color": "#0d9488",
"desc": "E 与 D 在介质分界面上的跃变规律",
"items": [
{"id":"e2s3-1","name":"静电场边界条件","tags":["thm","der"],"brief":"D 的法向分量与 E 的切向分量的边界跃变。",
 "body": wrap(
   thm("边界条件",p("在两种介质分界面上，取小扁圆柱高斯面和小矩形环路，可得：")+
   fml("D_{2n}-D_{1n} = \\sigma_f,\\qquad E_{2t}=E_{1t}")+
   p("其中 $\\sigma_f$ 为分界面上自由电荷面密度。若无自由电荷，$D_{1n}=D_{2n}$。"))+
   der(p("<strong>法向分量推导：</strong>跨分界面取扁圆柱高斯面，上下底面积 $\\Delta S$，高 $h\\to 0$。由高斯定理 $\\oint\\mathbf{D}\\cdot d\\mathbf{S}=q_f$：")+
   fml("D_{2n}\\Delta S - D_{1n}\\Delta S = \\sigma_f\\Delta S \\implies D_{2n}-D_{1n}=\\sigma_f")+
   p("<strong>切向分量推导：</strong>跨分界面取小矩形环路，长边 $\\Delta l$ 平行界面，短边 $h\\to 0$。由环路定理 $\\oint\\mathbf{E}\\cdot d\\mathbf{l}=0$：")+
   fml("E_{2t}\\Delta l - E_{1t}\\Delta l = 0 \\implies E_{2t}=E_{1t}"))+
   note(p("对线性介质，$\\mathbf{D}=\\varepsilon\\mathbf{E}$，故 $\\varepsilon_2 E_{2n}=\\varepsilon_1 E_{1n}$（$\\sigma_f=0$ 时），电场线在界面发生折射：$\\frac{\\tan\\theta_1}{\\tan\\theta_2}=\\frac{\\varepsilon_1}{\\varepsilon_2}$。"))
 )},
]},
{
"name": "2.4 极化强度与极化电荷的计算",
"color": "#0d9488",
"desc": "极化强度矢量与束缚电荷的定量关系",
"items": [
{"id":"e2s4-1","name":"极化强度矢量","tags":["def"],"brief":"描述电介质极化程度的宏观物理量。",
 "body": wrap(
   defn("极化强度",p("电介质中单位体积内分子电偶极矩的矢量和称为极化强度：")+
   fml("\\mathbf{P} = \\frac{\\sum_i \\mathbf{p}_i}{\\Delta V}")+
   p("其中 $\\mathbf{p}_i$ 为第 $i$ 个分子的电偶极矩，$\\Delta V$ 为宏观小、微观大的体积元。$\\mathbf{P}$ 的单位为 $\\text{C/m}^2$。对均匀极化，$\\mathbf{P}$ 为常矢量；非均匀极化时 $\\mathbf{P}$ 是位置的函数。"))+
   defn("极化率",p("在线性各向同性电介质中，极化强度与电场强度成正比：$\\mathbf{P}=\\varepsilon_0\\chi_e\\mathbf{E}$，其中 $\\chi_e$ 为电极化率，无量纲。"))
 )},
{"id":"e2s4-2","name":"极化电荷的计算","tags":["der"],"brief":"束缚电荷与极化强度的积分关系。",
 "body": wrap(
   der(p("<strong>束缚电荷面密度：</strong>在电介质表面取面元 $d\\mathbf{S}=\\mathbf{n}dS$，$\\mathbf{n}$ 为外法线方向。极化时，穿过面元的束缚电荷 $dq'=\\mathbf{P}\\cdot d\\mathbf{S}$，故束缚电荷面密度：")+
   fml("\\sigma' = \\frac{dq'}{dS} = \\mathbf{P}\\cdot\\mathbf{n} = P_n")+
   p("<strong>束缚电荷体密度：</strong>在电介质内取任意闭合曲面 $S$，极化时穿出 $S$ 的束缚电荷总量为 $\\oint_S\\mathbf{P}\\cdot d\\mathbf{S}$。由电荷守恒，$S$ 内束缚电荷 $q'=-\\oint_S\\mathbf{P}\\cdot d\\mathbf{S}$。利用高斯定理：")+
   fml("q' = \\int_V \\rho'\\,dV = -\\oint_S\\mathbf{P}\\cdot d\\mathbf{S} = -\\int_V\\nabla\\cdot\\mathbf{P}\\,dV")+
   fml("\\rho' = -\\nabla\\cdot\\mathbf{P}")+
   p("均匀极化时 $\\nabla\\cdot\\mathbf{P}=0$，束缚电荷只分布在表面。"))
 )},
{"id":"e2s4-3","name":"电介质极化的微观机制","tags":["def","der"],"brief":"位移极化与取向极化的微观解释。",
 "body": wrap(
   defn("位移极化",p("无极性分子（如 $\\text{He},\\text{CH}_4$）正负电荷中心重合，固有偶极矩为零。在外电场作用下，正负电荷中心发生相对位移，产生感应偶极矩 $\\mathbf{p}=\\alpha\\mathbf{E}_{\\text{局}}$，其中 $\\alpha$ 为分子极化率。这种极化称为位移极化（电子位移极化为主）。"))+
   defn("取向极化",p("极性分子（如 $\\text{H}_2\\text{O},\\text{HCl}$）具有固有偶极矩 $\\mathbf{p}_0$。无外场时热运动使取向杂乱；外场使偶极矩沿场方向取向排列，产生宏观极化。取向极化与温度有关，温度越高极化越弱（热运动破坏取向）。"))+
   der(p("<strong>极化率与介电常数的关系（克劳修斯-莫索提公式）：</strong>对稀薄气体，局域场近似等于宏观场 $\\mathbf{E}$。单位体积分子数 $N$，极化强度 $P=Np=N\\alpha E$，又 $P=\\varepsilon_0\\chi_e E$，故：")+
   fml("\\chi_e = \\frac{N\\alpha}{\\varepsilon_0},\\qquad \\varepsilon_r = 1+\\frac{N\\alpha}{\\varepsilon_0}")+
   p("对稠密介质需考虑局域场修正，得到克劳修斯-莫索提公式：$\\frac{\\varepsilon_r-1}{\\varepsilon_r+2}=\\frac{N\\alpha}{3\\varepsilon_0}$。"))
 )},
]},
{
"name": "2.5 电介质的极化规律",
"color": "#0d9488",
"desc": "线性与非线性电介质、介电常数",
"items": [
{"id":"e2s5-1","name":"线性各向同性电介质","tags":["def","thm"],"brief":"P、E、D 三者的线性关系。",
 "body": wrap(
   defn("线性各向同性电介质",p("若极化强度与电场强度成正比且方向相同，称为线性各向同性电介质：")+
   fml("\\mathbf{P} = \\varepsilon_0\\chi_e\\mathbf{E}")+
   p("其中 $\\chi_e$ 为电极化率，是与电场无关的常数（对线性介质）。"))+
   thm("D、E、P 的关系",p("由 $\\mathbf{D}=\\varepsilon_0\\mathbf{E}+\\mathbf{P}$，代入线性关系：")+
   fml("\\mathbf{D} = \\varepsilon_0(1+\\chi_e)\\mathbf{E} = \\varepsilon_0\\varepsilon_r\\mathbf{E} = \\varepsilon\\mathbf{E}")+
   p("相对介电常数 $\\varepsilon_r=1+\\chi_e$，介电常数 $\\varepsilon=\\varepsilon_0\\varepsilon_r$。真空中 $\\chi_e=0$，$\\varepsilon_r=1$。"))
 )},
{"id":"e2s5-2","name":"电介质的分类","tags":["def"],"brief":"各向异性、非线性与铁电体。",
 "body": wrap(
   defn("电介质分类",p("(1) <strong>线性各向同性</strong>：$\\mathbf{D}=\\varepsilon\\mathbf{E}$，$\\varepsilon$ 为标量常数。")+
   p("(2) <strong>各向异性</strong>（如晶体）：$D_i=\\sum_j\\varepsilon_{ij}E_j$，介电常数为二阶张量，$\\mathbf{D}$ 与 $\\mathbf{E}$ 一般不同向。")+
   p("(3) <strong>非线性</strong>：$\\varepsilon$ 与 $E$ 有关，存在电光效应等非线性现象。")+
   p("(4) <strong>铁电体</strong>：存在自发极化，$P$ 与 $E$ 有滞回关系（类似铁磁质），如钛酸钡 $\\text{BaTiO}_3$。")+
   p("(5) <strong>压电体</strong>：机械应力产生极化（压电效应），外加电场产生形变（逆压电效应），如石英。"))
 )},
]},
{
"name": "2.6 介质中的电场能量",
"color": "#0d9488",
"desc": "电介质存在时的电场能量密度",
"items": [
{"id":"e2s6-1","name":"电介质中的电场能量","tags":["der"],"brief":"介质中电场能量密度为 ½D·E。",
 "body": wrap(
   der(p("<strong>平行板电容器（充满介质）储能：</strong>极板面积 $S$，间距 $d$，介质介电常数 $\\varepsilon$。电容 $C=\\frac{\\varepsilon S}{d}$。充电至电压 $V$，储能：")+
   fml("W = \\frac{1}{2}CV^2 = \\frac{1}{2}\\frac{\\varepsilon S}{d}(Ed)^2 = \\frac{1}{2}\\varepsilon E^2\\cdot Sd")+
   p("体积 $V_{\\text{体}}=Sd$，故电场能量密度：")+
   fml("w_e = \\frac{W}{V_{\\text{体}}} = \\frac{1}{2}\\varepsilon E^2 = \\frac{1}{2}\\mathbf{D}\\cdot\\mathbf{E}")+
   p("总电场能量 $W=\\int_V w_e\\,dV=\\frac{1}{2}\\int_V\\mathbf{D}\\cdot\\mathbf{E}\\,dV$。此结果对任意电场分布普遍成立。"))+
   note(p("与真空相比，介质中能量密度为 $\\frac{1}{2}\\varepsilon E^2=\\frac{1}{2}\\varepsilon_r\\varepsilon_0 E^2$，比真空大 $\\varepsilon_r$ 倍。这是因为极化过程中介质分子获得势能。"))
 )},
]},
{
"name": "2.7 边界条件的应用",
"color": "#0d9488",
"desc": "电场线折射与导体-介质界面",
"items": [
{"id":"e2s7-1","name":"电场线在介质界面的折射","tags":["der"],"brief":"D的法向连续与E的切向连续导致电场线折射。",
 "body": wrap(
   der(p("<strong>折射定律推导：</strong>设两种介质介电常数分别为 $\\varepsilon_1,\\varepsilon_2$，界面无自由电荷。电场线与法线夹角分别为 $\\theta_1,\\theta_2$。由边界条件：")+
   fml("D_{1n}=D_{2n} \\implies \\varepsilon_1 E_1\\cos\\theta_1 = \\varepsilon_2 E_2\\cos\\theta_2")+
   fml("E_{1t}=E_{2t} \\implies E_1\\sin\\theta_1 = E_2\\sin\\theta_2")+
   p("两式相除，消去 $E_1,E_2$：")+
   fml("\\frac{\\tan\\theta_1}{\\tan\\theta_2} = \\frac{\\varepsilon_1}{\\varepsilon_2}")+
   p("这就是电场线的折射定律。若 $\\varepsilon_2>\\varepsilon_1$，则 $\\theta_2>\\theta_1$，电场线在介电常数大的一侧更偏离法线。"))
 )},
{"id":"e2s7-2","name":"导体与电介质界面","tags":["app"],"brief":"导体表面的边界条件与电场。",
 "body": wrap(
   app(p("<strong>导体-介质界面：</strong>导体内部电场为零，$E_1=0,D_1=0$。设导体为介质 1，介质为介质 2。由边界条件：")+
   fml("D_{2n}-D_{1n}=\\sigma_f \\implies D_{2n}=\\sigma_f")+
   fml("E_{2t}=E_{1t}=0")+
   p("故导体表面外侧电场垂直于表面（切向为零），大小 $E=\\sigma_f/\\varepsilon$。导体表面的自由电荷面密度 $\\sigma_f=D_n=\\varepsilon E_n$。")+
   p("<strong>注意：</strong>导体表面还可能有束缚电荷。极化电荷面密度 $\\sigma'=\\mathbf{P}\\cdot\\mathbf{n}=\\varepsilon_0\\chi_e E_n$。导体表面总面电荷密度为自由电荷与束缚电荷之和。"))
 )},
]},
{
"name": "2.8 电介质中的受力",
"color": "#0d9488",
"desc": "电介质在电场中受到的力",
"items": [
{"id":"e2s8-1","name":"电介质的受力","tags":["der"],"brief":"利用虚功原理求介质受的力。",
 "body": wrap(
   der(p("<strong>平行板电容器中介质的受力：</strong>平行板电容器宽 $b$，极板间距 $d$，插入介电常数 $\\varepsilon$ 的介质深度 $x$。电容可视为两个电容器并联：")+
   fml("C = \\frac{\\varepsilon_0 b(l-x)}{d} + \\frac{\\varepsilon b x}{d} = \\frac{b}{d}[\\varepsilon_0 l + (\\varepsilon-\\varepsilon_0)x]")+
   p("保持电压 $V$ 不变，电场能量 $W=\\frac{1}{2}CV^2$。介质受的力由虚功原理：电源做功 $dW_{\\text{源}}=VdQ=V^2 dC$，能量变化 $dW=\\frac{1}{2}V^2 dC$，故：")+
   fml("F\\,dx = dW_{\\text{源}} - dW = \\frac{1}{2}V^2 dC")+
   fml("F = \\frac{1}{2}V^2\\frac{dC}{dx} = \\frac{b V^2}{2d}(\\varepsilon-\\varepsilon_0)")+
   p("力的方向沿 $x$ 增大方向，即介质被吸入电容器。此力源于介质极化后与电场的相互作用。"))
 )},
]},
]

# =====================================================
#  CHAPTER 3: 静磁场
# =====================================================
ch3_sections = [
{
"name": "3.1 毕奥-萨伐尔定律",
"color": "#059669",
"desc": "电流元产生的磁场与叠加原理",
"items": [
{"id":"e3s1-1","name":"毕奥-萨伐尔定律","tags":["def","der"],"brief":"电流元在空间产生磁场的规律。",
 "fig":"biot","figCap":"电流元 Idl 在 P 点产生 dB",
 "body": wrap(
   defn("毕奥-萨伐尔定律",p("电流元 $I d\\mathbf{l}$ 在距其 $r$ 处的 $P$ 点产生的磁感应强度：")+
   fml("d\\mathbf{B} = \\frac{\\mu_0}{4\\pi}\\frac{I d\\mathbf{l}\\times\\hat{\\mathbf{r}}}{r^2}")+
   p("其中 $\\mu_0=4\\pi\\times10^{-7}\\,\\text{T}\\cdot\\text{m/A}$ 为真空磁导率。"))+
   der(p("<strong>载流直导线的磁场：</strong>设导线长 $L$，$P$ 到导线距离 $a$。积分得：")+
   fml("B = \\frac{\\mu_0 I}{4\\pi a}(\\sin\\beta_2 - \\sin\\beta_1)")+
   p("无限长直导线 $B=\\frac{\\mu_0 I}{2\\pi a}$。")+
   p("<strong>圆电流轴线上磁场：</strong>半径 $R$，轴线上距圆心 $x$ 处：")+
   fml("B = \\frac{\\mu_0 I R^2}{2(R^2+x^2)^{3/2}}")+
   p("圆心处 $B=\\frac{\\mu_0 I}{2R}$。"))
 )},
]},
{
"name": "3.2 安培环路定理",
"color": "#059669",
"desc": "磁场的环流定理及其应用",
"items": [
{"id":"e3s2-1","name":"安培环路定理","tags":["thm","der"],"brief":"磁场的环流与穿过电流的关系。",
 "fig":"solenoid","figCap":"载流螺线管内部均匀磁场",
 "body": wrap(
   thm("安培环路定理",p("真空中磁感应强度沿任意闭合回路的环流等于穿过回路所围面积的电流代数和乘以 $\\mu_0$：")+
   fml("\\oint_L \\mathbf{B}\\cdot d\\mathbf{l} = \\mu_0 \\sum I_{\\text{内}}")+
   p("电流方向与回路绕行方向满足右手螺旋时取正。"))+
   der(p("<strong>长直螺线管内磁场推导：</strong>螺线管单位长度匝数 $n$，电流 $I$。取矩形安培环路，一边在管内平行轴线，其余三边垂直。管内磁场均匀，管外 $B=0$，故：")+
   fml("\\oint \\mathbf{B}\\cdot d\\mathbf{l} = B\\cdot l = \\mu_0 n l I \\implies B = \\mu_0 n I")+
   p("方向沿轴线，由右手定则确定。"))
 )},
]},
{
"name": "3.3 洛伦兹力与安培力",
"color": "#059669",
"desc": "带电粒子和载流导线在磁场中受的力",
"items": [
{"id":"e3s3-1","name":"洛伦兹力与安培力","tags":["def","der"],"brief":"磁场对运动电荷和电流的作用力。",
 "body": wrap(
   defn("洛伦兹力",p("运动电荷 $q$ 在磁场 $\\mathbf{B}$ 中受的力：$\\mathbf{F}=q\\mathbf{v}\\times\\mathbf{B}$。若同时存在电场，$\\mathbf{F}=q(\\mathbf{E}+\\mathbf{v}\\times\\mathbf{B})$。"))+
   defn("安培力",p("电流元 $I d\\mathbf{l}$ 在磁场中受的力：$d\\mathbf{F}=I d\\mathbf{l}\\times\\mathbf{B}$。"))+
   der(p("<strong>安培力与洛伦兹力的关系：</strong>导线中自由电子数密度 $n$，每个电子受洛伦兹力 $f=-e\\mathbf{v}_d\\times\\mathbf{B}$。电流元 $I d\\mathbf{l}=n e v_d S d\\mathbf{l}$（$S$ 为截面积），单位长度受力：")+
   fml("\\frac{d\\mathbf{F}}{dl} = n S (-e)\\mathbf{v}_d\\times\\mathbf{B} = I\\frac{d\\mathbf{l}}{dl}\\times\\mathbf{B}")+
   p("故 $d\\mathbf{F}=I d\\mathbf{l}\\times\\mathbf{B}$，安培力是大量自由电子洛伦兹力的宏观表现。"))+
   note(p("洛伦兹力始终与速度垂直，不做功，只改变速度方向；安培力可以做功，其能量来自电源。"))
 )},
]},
{
"name": "3.4 载流线圈的磁矩与磁力矩",
"color": "#059669",
"desc": "磁矩定义、载流线圈在磁场中受的力矩与做功",
"items": [
{"id":"e3s4-1","name":"磁矩与磁力矩","tags":["def","der"],"brief":"载流线圈的磁矩及其在均匀磁场中受力矩。",
 "fig":"magnetic_moment","figCap":"载流线圈的磁矩方向",
 "body": wrap(
   defn("磁矩",p("载流线圈的磁矩 $\\mathbf{m}=I\\mathbf{S}\\hat{\\mathbf{n}}$，其中 $S$ 为线圈面积，$\\hat{\\mathbf{n}}$ 由右手定则确定（四指沿电流方向，拇指为 $\\hat{\\mathbf{n}}$）。"))+
   der(p("<strong>均匀磁场中载流平面线圈受力矩推导：</strong>设矩形线圈边长 $a,b$，电流 $I$，法向与 $\\mathbf{B}$ 夹角 $\\theta$。两条长为 $a$ 的边受力 $F=IaB$，方向相反，构成力偶。力臂为 $b\\sin\\theta$，故力矩大小：")+
   fml("\\tau = F\\cdot b\\sin\\theta = IabB\\sin\\theta = ISB\\sin\\theta")+
   fml("\\boldsymbol{\\tau} = \\mathbf{m}\\times\\mathbf{B}")+
   p("力矩使线圈法向转向磁场方向。"))+
   der(p("<strong>磁力矩做功：</strong>线圈转动 $d\\theta$ 时，力矩做功 $dA=-\\tau d\\theta$（$\\theta$ 为 $\\mathbf{m}$ 与 $\\mathbf{B}$ 夹角）。磁通量 $\\Phi=BS\\cos\\theta$，故 $d\\Phi=-BS\\sin\\theta\\,d\\theta$：")+
   fml("dA = I\\,d\\Phi")+
   p("线圈从 $\\theta_1$ 转到 $\\theta_2$，外力矩做功 $A=I(\\Phi_2-\\Phi_1)$。"))
 )},
]},
{
"name": "3.5 磁感应强度与磁力线",
"color": "#059669",
"desc": "磁感应强度的定义与磁力线的性质",
"items": [
{"id":"e3s5-1","name":"磁感应强度","tags":["def"],"brief":"描述磁场强弱和方向的物理量。",
 "body": wrap(
   defn("磁感应强度",p("运动电荷在磁场中受力 $\\mathbf{F}=q\\mathbf{v}\\times\\mathbf{B}$，由此定义磁感应强度 $\\mathbf{B}$。$\\mathbf{B}$ 的方向为小磁针 N 极受力方向；大小为 $B=\\frac{F}{qv\\sin\\theta}$，其中 $\\theta$ 为 $\\mathbf{v}$ 与 $\\mathbf{B}$ 夹角。单位为特斯拉（T），$1\\,\\text{T}=1\\,\\text{N/(A}\\cdot\\text{m)}$。"))+
   defn("磁通量",p("穿过曲面 $S$ 的磁通量：$\\Phi=\\int_S\\mathbf{B}\\cdot d\\mathbf{S}$。单位为韦伯（Wb），$1\\,\\text{Wb}=1\\,\\text{T}\\cdot\\text{m}^2$。"))
 )},
{"id":"e3s5-2","name":"磁力线及其性质","tags":["def","thm"],"brief":"磁力线是闭合曲线，与电流互相套连。",
 "body": wrap(
   defn("磁力线",p("磁力线是描述磁场分布的几何曲线：(1) 切线方向为该点磁感应强度方向；(2) 垂直通过单位面积的磁力线数正比于 $B$ 的大小。"))+
   thm("磁力线的性质",p("(1) 磁力线是闭合曲线（无头无尾），这与静电场电场线（起始于正电荷、终止于负电荷）根本不同，反映了磁场的无源性 $\\nabla\\cdot\\mathbf{B}=0$。")+
   p("(2) 磁力线与电流互相套连，方向满足右手螺旋定则。")+
   p("(3) 任意两条磁力线不相交。")+
   p("(4) 磁力线密集处磁场强，稀疏处磁场弱。"))
 )},
]},
{
"name": "3.6 毕奥-萨伐尔定律的应用",
"color": "#059669",
"desc": "载流直导线、圆电流、螺线管的磁场",
"items": [
{"id":"e3s6-1","name":"载流直导线与圆电流的磁场","tags":["der"],"brief":"直导线和圆电流轴线上的磁感应强度。",
 "body": wrap(
   der(p("<strong>有限长载流直导线的磁场：</strong>设导线两端相对于场点 $P$ 的张角为 $\\beta_1,\\beta_2$（从垂线算起），$P$ 到导线距离 $a$。积分毕奥-萨伐尔定律：")+
   fml("B = \\frac{\\mu_0 I}{4\\pi a}(\\sin\\beta_2 - \\sin\\beta_1)")+
   p("无限长直导线 $\\beta_1=-\\pi/2,\\beta_2=\\pi/2$，$B=\\frac{\\mu_0 I}{2\\pi a}$。半无限长 $B=\\frac{\\mu_0 I}{4\\pi a}$。")+
   p("<strong>圆电流轴线上的磁场：</strong>半径 $R$，电流 $I$，轴线上距圆心 $x$ 处：")+
   fml("B = \\frac{\\mu_0 I R^2}{2(R^2+x^2)^{3/2}}")+
   p("圆心处 $x=0$，$B=\\frac{\\mu_0 I}{2R}$。远场 $x\\gg R$，$B\\approx\\frac{\\mu_0}{4\\pi}\\frac{2m}{x^3}$，其中 $m=I\\pi R^2$ 为磁矩，形式与电偶极子电场类似。"))
 )},
{"id":"e3s6-2","name":"载流螺线管的磁场","tags":["der"],"brief":"有限长与无限长螺线管轴线上的磁场。",
 "body": wrap(
   der(p("<strong>载流直螺线管轴线上的磁场：</strong>单位长度匝数 $n$，电流 $I$，长度 $L$，半径 $R$。轴线上任一点的磁场可视为多个圆电流磁场的叠加。设场点到两端的张角为 $\\beta_1,\\beta_2$（从轴线算起）：")+
   fml("B = \\frac{\\mu_0 n I}{2}(\\cos\\beta_1 - \\cos\\beta_2)")+
   p("无限长螺线管 $\\beta_1=0,\\beta_2=\\pi$，$B=\\mu_0 n I$，内部为匀强磁场。半无限长螺线管端面处 $B=\\frac{1}{2}\\mu_0 n I$，为内部的一半。")+
   p("<strong>螺绕环：</strong>细螺绕环（平均半径 $R$，总匝数 $N$）内部磁场 $B=\\frac{\\mu_0 N I}{2\\pi r}$，近似为 $B=\\mu_0 n I$（$n=N/(2\\pi R)$），外部 $B=0$。"))
 )},
]},
{
"name": "3.7 运动电荷的磁场",
"color": "#059669",
"desc": "匀速运动电荷产生的磁场",
"items": [
{"id":"e3s7-1","name":"运动电荷的磁场","tags":["der"],"brief":"匀速运动点电荷产生的磁感应强度。",
 "body": wrap(
   der(p("<strong>由毕奥-萨伐尔定律推导：</strong>电流元 $I d\\mathbf{l}$ 可视为大量运动电荷的集体效应。设导线截面积 $S$，电荷数密度 $n$，每个电荷 $q$ 以漂移速度 $\\mathbf{v}$ 运动，则 $I=nqvS$，$d\\mathbf{l}$ 内电荷数 $dN=nSdl$。电流元产生的磁场：")+
   fml("d\\mathbf{B} = \\frac{\\mu_0}{4\\pi}\\frac{I d\\mathbf{l}\\times\\hat{\\mathbf{r}}}{r^2} = \\frac{\\mu_0}{4\\pi}\\frac{nqvS dl\\,\\hat{\\mathbf{v}}\\times\\hat{\\mathbf{r}}}{r^2}")+
   p("除以 $dN=nSdl$ 得单个运动电荷产生的磁场（非相对论近似 $v\\ll c$）：")+
   fml("\\mathbf{B} = \\frac{\\mu_0}{4\\pi}\\frac{q\\mathbf{v}\\times\\hat{\\mathbf{r}}}{r^2}")+
   p("方向垂直于 $\\mathbf{v}$ 与 $\\mathbf{r}$ 组成的平面。运动电荷的电场 $\\mathbf{E}=\\frac{1}{4\\pi\\varepsilon_0}\\frac{q\\hat{\\mathbf{r}}}{r^2}$，故 $\\mathbf{B}=\\mu_0\\varepsilon_0\\mathbf{v}\\times\\mathbf{E}=\\frac{1}{c^2}\\mathbf{v}\\times\\mathbf{E}$。"))
 )},
]},
{
"name": "3.8 磁场的高斯定理",
"color": "#059669",
"desc": "磁场的无源性与磁通连续",
"items": [
{"id":"e3s8-1","name":"磁场的高斯定理","tags":["thm","der"],"brief":"穿过任意闭合曲面的磁通量为零。",
 "body": wrap(
   thm("磁场的高斯定理",p("磁感应强度通过任意闭合曲面的磁通量恒为零：")+
   fml("\\oint_S \\mathbf{B}\\cdot d\\mathbf{S} = 0")+
   p("其微分形式为 $\\nabla\\cdot\\mathbf{B}=0$，表明磁场是无源场，不存在磁单极子。"))+
   der(p("<strong>推导：</strong>由毕奥-萨伐尔定律，电流元产生的磁场 $d\\mathbf{B}=\\frac{\\mu_0}{4\\pi}\\frac{I d\\mathbf{l}\\times\\hat{\\mathbf{r}}}{r^2}$。$d\\mathbf{B}$ 的方向沿以电流元延长线为轴的圆周切线，磁力线是闭合圆周。对任意闭合曲面，每条磁力线穿入必穿出，故 $\\oint d\\mathbf{B}\\cdot d\\mathbf{S}=0$。叠加得 $\\oint\\mathbf{B}\\cdot d\\mathbf{S}=0$。")+
   p("由高斯公式 $\\oint_S\\mathbf{B}\\cdot d\\mathbf{S}=\\int_V\\nabla\\cdot\\mathbf{B}\\,dV=0$，因 $S$ 任意，故 $\\nabla\\cdot\\mathbf{B}=0$。"))+
   note(p("与电场高斯定理 $\\oint\\mathbf{E}\\cdot d\\mathbf{S}=q/\\varepsilon_0$ 对比：电场有源（电荷），磁场无源（无磁单极）。这是电磁场的基本不对称性。"))
 )},
{"id":"e3s8-2","name":"磁矢势","tags":["def","der"],"brief":"由磁场无源性引入磁矢势 A。",
 "body": wrap(
   defn("磁矢势",p("由 $\\nabla\\cdot\\mathbf{B}=0$，根据矢量分析，无源场必可表示为某矢量场的旋度。引入磁矢势 $\\mathbf{A}$：")+
   fml("\\mathbf{B} = \\nabla\\times\\mathbf{A}")+
   p("$\\mathbf{A}$ 的单位为 $\\text{T}\\cdot\\text{m}$ 或 $\\text{Wb/m}$。$\\mathbf{A}$ 的选择不唯一，具有规范自由度。"))+
   der(p("<strong>安培环路定理的矢势形式：</strong>由 $\\oint_L\\mathbf{B}\\cdot d\\mathbf{l}=\\mu_0 I$，利用斯托克斯定理 $\\oint_L\\mathbf{B}\\cdot d\\mathbf{l}=\\int_S(\\nabla\\times\\mathbf{B})\\cdot d\\mathbf{S}$。而 $\\mathbf{B}=\\nabla\\times\\mathbf{A}$，故：")+
   fml("\\oint_L\\mathbf{A}\\cdot d\\mathbf{l} = \\int_S\\mathbf{B}\\cdot d\\mathbf{S} = \\Phi")+
   p("即磁矢势沿闭合回路的环流等于穿过回路的磁通量。")+
   p("<strong>长直导线的磁矢势：</strong>无限长直导线通电流 $I$，取库仑规范 $\\nabla\\cdot\\mathbf{A}=0$，$\\mathbf{A}$ 沿电流方向（$z$ 轴）：")+
   fml("A_z = -\\frac{\\mu_0 I}{2\\pi}\\ln r + C")+
   p("由 $\\mathbf{B}=\\nabla\\times\\mathbf{A}$ 可验证 $B_\\varphi=\\frac{\\mu_0 I}{2\\pi r}$，与毕奥-萨伐尔定律结果一致。"))
 )},
]},
{
"name": "3.9 安培力的应用",
"color": "#059669",
"desc": "平行载流导线间的作用力与载流回路受力",
"items": [
{"id":"e3s9-1","name":"平行载流导线间的作用力","tags":["der"],"brief":"同向电流相吸，反向电流相斥。",
 "body": wrap(
   der(p("<strong>两根无限长平行载流直导线：</strong>相距 $a$，分别通电流 $I_1,I_2$。导线 1 在导线 2 处产生的磁场 $B_1=\\frac{\\mu_0 I_1}{2\\pi a}$，方向垂直于两导线连线。导线 2 上电流元 $I_2 d\\mathbf{l}$ 受力：")+
   fml("dF = I_2 dl\\cdot B_1 = \\frac{\\mu_0 I_1 I_2}{2\\pi a}dl")+
   p("单位长度受力：")+
   fml("\\frac{dF}{dl} = \\frac{\\mu_0 I_1 I_2}{2\\pi a}")+
   p("同向电流时力为吸引力，反向电流时为排斥力。此式用于定义安培：真空中相距 1 米的两无限长平行导线通以相等电流，当单位长度受力为 $2\\times10^{-7}\\,\\text{N/m}$ 时，电流为 1 安培。"))
 )},
{"id":"e3s9-2","name":"载流回路在磁场中受的力","tags":["der"],"brief":"均匀磁场中载流回路受力为零，非均匀时受力。",
 "body": wrap(
   der(p("<strong>均匀磁场中任意载流闭合回路：</strong>安培力 $\\mathbf{F}=\\oint I d\\mathbf{l}\\times\\mathbf{B}$。由于 $\\mathbf{B}$ 为常矢量：")+
   fml("\\mathbf{F} = I\\left(\\oint d\\mathbf{l}\\right)\\times\\mathbf{B} = 0")+
   p("因为闭合回路的矢量和 $\\oint d\\mathbf{l}=0$。所以均匀磁场中闭合载流回路受力为零，但受力矩（除非 $\\mathbf{m}\\parallel\\mathbf{B}$）。")+
   p("<strong>非均匀磁场中：</strong>载流回路受力不为零。设磁矩 $\\mathbf{m}$，磁场梯度 $\\nabla\\mathbf{B}$，则：")+
   fml("\\mathbf{F} = \\nabla(\\mathbf{m}\\cdot\\mathbf{B})")+
   p("当 $\\mathbf{m}$ 与 $\\mathbf{B}$ 平行时，力指向磁场增强方向；反平行时指向磁场减弱方向。这就是磁偶极子被吸向强磁场区的原因。"))
 )},
]},
{
"name": "3.10 磁矩的进动",
"color": "#059669",
"desc": "磁矩在磁场中的进动与拉莫尔频率",
"items": [
{"id":"e3s10-1","name":"拉莫尔进动","tags":["der"],"brief":"磁矩在外磁场中做进动。",
 "body": wrap(
   der(p("<strong>角动量与磁矩的关系：</strong>微观粒子的磁矩 $\\mathbf{m}$ 与角动量 $\\mathbf{L}$ 成正比：$\\mathbf{m}=\\gamma\\mathbf{L}$，其中 $\\gamma$ 为旋磁比。")+
   p("<strong>进动方程：</strong>磁矩在磁场 $\\mathbf{B}$ 中受力矩 $\\boldsymbol{\\tau}=\\mathbf{m}\\times\\mathbf{B}$。由角动量定理 $\\frac{d\\mathbf{L}}{dt}=\\boldsymbol{\\tau}$：")+
   fml("\\frac{d\\mathbf{m}}{dt} = \\gamma\\frac{d\\mathbf{L}}{dt} = \\gamma(\\mathbf{m}\\times\\mathbf{B})")+
   p("此方程的解为 $\\mathbf{m}$ 绕 $\\mathbf{B}$ 方向做匀速进动，进动角速度（拉莫尔频率）：")+
   fml("\\omega_L = \\gamma B")+
   p("进动方向：对正电荷 $\\gamma>0$，进动方向与 $\\mathbf{B}$ 满足右手螺旋；对电子 $\\gamma<0$，进动方向相反。拉莫尔进动是磁共振（NMR、EPR）的物理基础。"))
 )},
]},
{
"name": "3.11 带电粒子在磁场中的运动",
"color": "#059669",
"desc": "带电粒子在均匀磁场中的螺旋运动",
"items": [
{"id":"e3s11-1","name":"带电粒子在均匀磁场中的运动","tags":["der"],"brief":"洛伦兹力提供向心力，粒子做螺旋运动。",
 "body": wrap(
   der(p("<strong>速度分解：</strong>将带电粒子速度 $\\mathbf{v}$ 分解为平行于 $\\mathbf{B}$ 的分量 $v_\\parallel$ 和垂直分量 $v_\\perp$。平行方向不受力，做匀速直线运动；垂直方向受洛伦兹力 $qv_\\perp B$ 提供向心力：")+
   fml("qv_\\perp B = m\\frac{v_\\perp^2}{R} \\implies R = \\frac{mv_\\perp}{qB}")+
   p("回旋半径（拉莫尔半径）$R=\\frac{mv_\\perp}{qB}$。回旋周期：")+
   fml("T = \\frac{2\\pi R}{v_\\perp} = \\frac{2\\pi m}{qB}")+
   p("回旋频率 $f=qB/(2\\pi m)$，角频率 $\\omega=qB/m$，与速度无关（非相对论）。")+
   p("<strong>螺旋运动：</strong>粒子同时具有 $v_\\parallel$ 和 $v_\\perp$，合运动为螺旋线，螺距：")+
   fml("h = v_\\parallel T = \\frac{2\\pi m v_\\parallel}{qB}")+
   p("磁聚焦原理：从同一点出发的粒子，若 $v_\\parallel$ 相近，经过一个周期后会聚于同一点。"))+
   app(p("<strong>应用：</strong>回旋加速器、磁聚焦、质谱仪、霍尔效应、磁约束（托卡马克）。霍尔电压 $U_H=\\frac{IB}{nqd}$，可用于测量磁场和载流子浓度。"))
 )},
]},
]

# =====================================================
#  CHAPTER 4: 介质中的静磁场
# =====================================================
ch4_sections = [
{
"name": "4.1 磁介质的磁化",
"color": "#0891b2",
"desc": "磁化强度、分子电流与束缚电流",
"items": [
{"id":"e4s1-1","name":"磁介质磁化","tags":["def","der"],"brief":"磁介质在磁场中产生磁化电流。",
 "fig":"magnetic_material","figCap":"磁介质的磁化示意图",
 "body": wrap(
   defn("分子磁矩",p("分子中电子轨道运动和自旋产生的等效磁矩 $\\mathbf{m}_m$。无外场时分子磁矩取向杂乱，宏观不显磁性。"))+
   defn("磁化强度",p("单位体积内分子磁矩的矢量和：$\\mathbf{M}=\\frac{\\sum\\mathbf{m}_i}{\\Delta V}$。"))+
   der(p("<strong>束缚电流面密度：</strong>磁化强度沿介质表面的切向分量等于束缚面电流线密度 $\\mathbf{i}'=\\mathbf{M}\\times\\mathbf{n}$。束缚体电流密度 $\\mathbf{j}'=\\nabla\\times\\mathbf{M}$。")+
   fml("\\mathbf{i}' = \\mathbf{M}\\times\\mathbf{n},\\qquad \\mathbf{j}' = \\nabla\\times\\mathbf{M}"))
 )},
]},
{
"name": "4.2 磁场强度与介质安培环路定理",
"color": "#0891b2",
"desc": "H 矢量的引入与磁介质分类",
"items": [
{"id":"e4s2-1","name":"磁场强度","tags":["def","thm","der"],"brief":"将磁化电流吸收进 H 矢量。",
 "body": wrap(
   defn("磁场强度",p("定义 $\\mathbf{H}=\\frac{\\mathbf{B}}{\\mu_0}-\\mathbf{M}$。对线性各向同性磁介质，$\\mathbf{M}=\\chi_m\\mathbf{H}$，故：")+
   fml("\\mathbf{B} = \\mu_0(1+\\chi_m)\\mathbf{H} = \\mu_0\\mu_r\\mathbf{H} = \\mu\\mathbf{H}")+
   p("其中 $\\mu_r=1+\\chi_m$ 为相对磁导率。"))+
   thm("介质中的安培环路定理",p("磁场强度沿任意闭合回路的环流等于穿过回路的传导电流代数和：")+
   fml("\\oint_L \\mathbf{H}\\cdot d\\mathbf{l} = \\sum I_{0\\text{内}}"))+
   der(p("<strong>推导：</strong>真空中 $\\oint\\mathbf{B}\\cdot d\\mathbf{l}=\\mu_0(I_0+I')$，而磁化电流 $I'=\\oint\\mathbf{M}\\cdot d\\mathbf{l}$。代入：")+
   fml("\\oint\\frac{\\mathbf{B}}{\\mu_0}\\cdot d\\mathbf{l} = I_0 + \\oint\\mathbf{M}\\cdot d\\mathbf{l}")+
   fml("\\oint\\left(\\frac{\\mathbf{B}}{\\mu_0}-\\mathbf{M}\\right)\\cdot d\\mathbf{l} = I_0 \\implies \\oint\\mathbf{H}\\cdot d\\mathbf{l} = I_0"))+
   note(p("<strong>磁介质分类：</strong>顺磁质 $\\chi_m>0$（$\\mu_r>1$），抗磁质 $\\chi_m<0$（$\\mu_r<1$），铁磁质 $\\mu_r\\gg 1$ 且非线性、有磁滞。"))
 )},
]},
{
"name": "4.3 铁磁质与磁滞回线",
"color": "#0891b2",
"desc": "铁磁质的磁化曲线、磁滞回线与磁畴",
"items": [
{"id":"e4s3-1","name":"铁磁质的磁化规律","tags":["def","thm"],"brief":"铁磁质的非线性磁化与磁滞现象。",
 "fig":"hysteresis","figCap":"铁磁质的磁滞回线",
 "body": wrap(
   defn("铁磁质",p("$\\mu_r\\gg 1$（可达 $10^2\\sim10^4$），$B$ 与 $H$ 非线性，存在磁滞和居里温度 $T_c$（高于此温度变为顺磁质）。"))+
   defn("起始磁化曲线",p("从退磁状态（$H=0,B=0$）开始，$B$ 随 $H$ 增加而非线性增大，先缓后陡再趋饱和。饱和磁感应强度为 $B_s$。"))+
   thm("磁滞回线",p("$H$ 减小至零后 $B$ 不为零，剩余磁感应强度 $B_r$（剩磁）。使 $B=0$ 需加反向矫顽力 $H_c$。$B$ 的变化滞后于 $H$，形成闭合回线：")+
   fml("B_r = B(H=0),\\qquad H_c = |H(B=0)|")+
   p("磁滞回线包围的面积等于单位体积反复磁化一周的能量损耗（磁滞损耗）。"))+
   note(p("<strong>磁畴理论：</strong>铁磁质内部分成许多小区域（磁畴），每个磁畴内磁矩自发平行排列。外场使磁畴壁移动和磁矩转向，宏观显示强磁性。硬磁材料（$H_c$ 大）做永磁体，软磁材料（$H_c$ 小）做变压器铁芯。"))
 )},
]},
{
"name": "4.4 磁化强度与磁化电流深入",
"color": "#0891b2",
"desc": "磁化强度的定量描述与磁化电流的计算",
"items": [
{"id":"e4s4-1","name":"磁化强度矢量","tags":["def"],"brief":"描述磁介质磁化程度的宏观物理量。",
 "body": wrap(
   defn("磁化强度",p("磁介质中单位体积内分子磁矩的矢量和称为磁化强度：")+
   fml("\\mathbf{M} = \\frac{\\sum_i \\mathbf{m}_i}{\\Delta V}")+
   p("单位为 A/m。均匀磁化时 $\\mathbf{M}$ 为常矢量；非均匀磁化时 $\\mathbf{M}$ 是位置函数。对线性各向同性磁介质，$\\mathbf{M}=\\chi_m\\mathbf{H}$，其中 $\\chi_m$ 为磁化率。"))+
   defn("顺磁质与抗磁质",p("<strong>顺磁质</strong>：分子具有固有磁矩，外场使其取向排列，$\\chi_m>0$ 且很小（$\\sim10^{-5}$），如铝、氧。<strong>抗磁质</strong>：分子无固有磁矩，外场感应产生反向磁矩，$\\chi_m<0$ 且很小，如铜、铋。"))
 )},
{"id":"e4s4-2","name":"磁化电流的计算","tags":["der"],"brief":"磁化电流密度与磁化强度的关系。",
 "body": wrap(
   der(p("<strong>束缚电流面密度：</strong>在均匀磁化的介质表面，磁化强度 $\\mathbf{M}$ 沿表面的切向分量产生束缚面电流。束缚面电流线密度 $\\mathbf{i}'$（单位长度的电流）为：")+
   fml("\\mathbf{i}' = \\mathbf{M}\\times\\mathbf{n}")+
   p("其中 $\\mathbf{n}$ 为介质表面外法线方向。")+
   p("<strong>束缚电流体密度：</strong>在非均匀磁化介质内部，磁化强度的空间变化产生束缚体电流。取任意闭合回路 $L$，穿过 $L$ 的束缚电流 $I'=\\oint_L\\mathbf{M}\\cdot d\\mathbf{l}$。由斯托克斯定理：")+
   fml("I' = \\oint_L\\mathbf{M}\\cdot d\\mathbf{l} = \\int_S(\\nabla\\times\\mathbf{M})\\cdot d\\mathbf{S} = \\int_S\\mathbf{j}'\\cdot d\\mathbf{S}")+
   fml("\\mathbf{j}' = \\nabla\\times\\mathbf{M}")+
   p("均匀磁化时 $\\nabla\\times\\mathbf{M}=0$，束缚电流只分布在介质表面。"))
 )},
{"id":"e4s4-3","name":"顺磁质与抗磁质的微观机制","tags":["def","der"],"brief":"分子磁矩的来源与磁化的微观解释。",
 "body": wrap(
   defn("分子磁矩的来源",p("分子的磁矩来源于：(1) 电子的轨道磁矩 $\\mathbf{m}_l=-\\frac{e}{2m_e}\\mathbf{L}$；(2) 电子的自旋磁矩 $\\mathbf{m}_s=-\\frac{e}{m_e}\\mathbf{S}$；(3) 原子核的磁矩（很小，可忽略）。分子总磁矩为各电子磁矩的矢量和。"))+
   der(p("<strong>顺磁性的微观机制：</strong>顺磁质分子具有固有磁矩 $\\mathbf{m}_0$。无外场时，热运动使分子磁矩取向杂乱，宏观磁矩为零。外加磁场 $\\mathbf{B}$ 后，每个磁矩受力矩 $\\boldsymbol{\\tau}=\\mathbf{m}\\times\\mathbf{B}$，势能 $U=-\\mathbf{m}\\cdot\\mathbf{B}=-mB\\cos\\theta$。由玻尔兹曼统计，沿 $\\mathbf{B}$ 方向取向的分子数略多，产生沿 $\\mathbf{B}$ 方向的磁化强度。居里定律：")+
   fml("\\chi_m = \\frac{C}{T},\\qquad C=\\frac{N\\mu_0 m_0^2}{3k_B}")+
   p("其中 $N$ 为单位体积分子数，$k_B$ 为玻尔兹曼常数。")+
   p("<strong>抗磁性的微观机制：</strong>外场使电子轨道运动的角速度改变（拉莫尔进动），产生与外场反向的感应磁矩。感应磁矩 $\\Delta\\mathbf{m}=-\\frac{e^2 r^2}{4m_e}\\mathbf{B}$，方向与 $\\mathbf{B}$ 相反，故 $\\chi_m<0$。抗磁性是所有物质的共性，但在顺磁质和铁磁质中被掩盖。"))
 )},
]},
{
"name": "4.5 磁场强度 H 与磁介质分类",
"color": "#0891b2",
"desc": "H 的环路定理应用与三类磁介质",
"items": [
{"id":"e4s5-1","name":"H 的安培环路定理应用","tags":["thm","app"],"brief":"利用对称性由 H 的环路定理求磁场。",
 "body": wrap(
   thm("介质中的安培环路定理",p("磁场强度沿任意闭合回路的环流等于穿过回路的传导电流代数和：")+
   fml("\\oint_L \\mathbf{H}\\cdot d\\mathbf{l} = \\sum I_{0\\text{内}}"))+
   app(p("<strong>充满均匀磁介质的长直螺线管：</strong>单位长度匝数 $n$，传导电流 $I$，介质磁导率 $\\mu$。由对称性，管内 $\\mathbf{H}$ 沿轴线均匀。取矩形安培环路：")+
   fml("\\oint\\mathbf{H}\\cdot d\\mathbf{l} = H l = n l I \\implies H = n I")+
   p("由 $B=\\mu H$，得 $B=\\mu n I=\\mu_r\\mu_0 n I$。与真空相比，磁场增强了 $\\mu_r$ 倍（顺磁质略增强，抗磁质略减弱，铁磁质大幅增强）。"))
 )},
{"id":"e4s5-2","name":"磁介质的分类","tags":["def"],"brief":"顺磁质、抗磁质、铁磁质的特性对比。",
 "body": wrap(
   defn("磁介质分类",p("(1) <strong>顺磁质</strong>：$\\chi_m>0$（$10^{-5}\\sim10^{-3}$），$\\mu_r>1$，$M$ 与 $H$ 同向。分子具有固有磁矩，外场使磁矩取向排列。温度升高磁化减弱（居里定律 $\\chi_m=C/T$）。")+
   p("(2) <strong>抗磁质</strong>：$\\chi_m<0$（$\\sim-10^{-5}$），$\\mu_r<1$，$M$ 与 $H$ 反向。源于外场对电子轨道运动的感应效应，与温度无关。")+
   p("(3) <strong>铁磁质</strong>：$\\chi_m\\gg 1$（$10^2\\sim10^4$），$\\mu_r\\gg 1$，$M$ 与 $H$ 非线性且有磁滞。存在磁畴结构和居里温度。")+
   p("(4) <strong>亚铁磁质/反铁磁质</strong>：相邻原子磁矩反平行排列，亚铁磁质有净磁矩（如铁氧体），反铁磁质净磁矩为零。"))
 )},
]},
{
"name": "4.6 铁磁质的磁滞与磁畴",
"color": "#0891b2",
"desc": "磁滞回线、磁畴理论与居里温度",
"items": [
{"id":"e4s6-1","name":"磁畴与居里温度","tags":["def","thm"],"brief":"铁磁质的微观机制与温度效应。",
 "body": wrap(
   defn("磁畴",p("铁磁质内部存在许多小区域（线度 $10^{-4}\\sim10^{-6}\\,\\text{m}$），称为磁畴。每个磁畴内原子磁矩自发平行排列（交换相互作用），具有很强的磁化强度。无外场时各磁畴取向杂乱，宏观磁矩为零。"))+
   thm("磁化过程",p("外场较弱时，磁畴壁发生可逆位移；外场增强时，磁畴壁不可逆位移（Barkhausen 跳跃）；外场很强时，磁畴磁矩转向外场方向，达到饱和磁化 $M_s$。")+
   p("<strong>居里温度 $T_c$：</strong>温度升高，热运动破坏磁畴内的自发磁化。当 $T>T_c$ 时，磁畴瓦解，铁磁质变为顺磁质，服从居里-外斯定律 $\\chi_m=\\frac{C}{T-T_c}$。铁的 $T_c\\approx770°\\text{C}$。"))+
   note(p("<strong>软磁与硬磁材料：</strong>软磁材料（纯铁、硅钢）$H_c$ 小、磁导率高，用于变压器、电机铁芯；硬磁材料（钕铁硼、铝镍钴）$H_c$ 大、剩磁 $B_r$ 大，用于永磁体。"))
 )},
]},
{
"name": "4.7 磁路定理",
"color": "#0891b2",
"desc": "磁路的欧姆定律与磁路计算",
"items": [
{"id":"e4s7-1","name":"磁路定理","tags":["thm","der"],"brief":"磁路与电路的类比及磁阻概念。",
 "body": wrap(
   defn("磁路",p("磁通通过的闭合路径称为磁路。由于铁磁质磁导率远大于空气，磁通主要集中在铁芯中，类似于电流集中在导体中。"))+
   thm("磁路欧姆定律",p("设铁芯截面积 $S$，平均长度 $l$，磁导率 $\\mu$，线圈匝数 $N$，电流 $I$。由安培环路定理：")+
   fml("\\oint\\mathbf{H}\\cdot d\\mathbf{l} = H l = N I \\implies H = \\frac{N I}{l}")+
   p("磁通 $\\Phi=BS=\\mu H S=\\mu\\frac{NI}{l}S$，整理得：")+
   fml("\\Phi = \\frac{NI}{l/(\\mu S)} = \\frac{F_m}{R_m}")+
   p("其中磁通势 $F_m=NI$（单位：安匝），磁阻 $R_m=\\frac{l}{\\mu S}$（单位：$\\text{H}^{-1}$）。此即磁路欧姆定律，与电路欧姆定律 $I=\\mathcal{E}/R$ 类比。"))+
   der(p("<strong>串联磁路：</strong>磁阻串联 $R_m=\\sum R_{mi}$，磁通处处相等 $\\Phi$ 相同，总磁通势 $F_m=\\sum F_{mi}=\\Phi\\sum R_{mi}$。")+
   p("<strong>并联磁路：</strong>磁阻并联 $1/R_m=\\sum 1/R_{mi}$，各支路磁通势相同，总磁通 $\\Phi=\\sum\\Phi_i$。"))
 )},
{"id":"e4s7-2","name":"变压器原理","tags":["app","der"],"brief":"利用互感和磁路实现电压变换。",
 "body": wrap(
   defn("变压器",p("变压器由闭合铁芯和绕在其上的原、副线圈组成。原线圈匝数 $N_1$，副线圈匝数 $N_2$。利用互感现象将交流电的电压升高或降低。"))+
   der(p("<strong>理想变压器电压比：</strong>理想变压器（无漏磁、无铜损铁损、空载电流可忽略）中，原副线圈的磁通匝链数分别为 $\\Psi_1=N_1\\Phi$，$\\Psi_2=N_2\\Phi$。感应电动势 $\\varepsilon_1=-N_1\\frac{d\\Phi}{dt}$，$\\varepsilon_2=-N_2\\frac{d\\Phi}{dt}$。忽略线圈电阻，端电压 $U_1\\approx|\\varepsilon_1|$，$U_2\\approx|\\varepsilon_2|$，故：")+
   fml("\\frac{U_1}{U_2} = \\frac{N_1}{N_2}")+
   p("<strong>电流比：</strong>理想变压器输入功率等于输出功率 $U_1 I_1=U_2 I_2$，故：")+
   fml("\\frac{I_1}{I_2} = \\frac{N_2}{N_1}")+
   p("匝数多的一侧电压高、电流小，匝数少的一侧电压低、电流大。变压器只能变换交流电，不能变换直流电。"))
 )},
]},
{
"name": "4.8 静磁场的边界条件",
"color": "#0891b2",
"desc": "B 的法向连续与 H 的切向跃变",
"items": [
{"id":"e4s8-1","name":"静磁场边界条件","tags":["thm","der"],"brief":"B的法向分量连续，H的切向分量跃变。",
 "body": wrap(
   thm("边界条件",p("在两种磁介质分界面上：")+
   fml("B_{1n}=B_{2n},\\qquad H_{2t}-H_{1t}=\\alpha_f")+
   p("其中 $\\alpha_f$ 为分界面上传导电流的面密度（方向垂直于 $H$ 的切向分量）。若无传导电流，$H_{1t}=H_{2t}$。"))+
   der(p("<strong>法向分量推导：</strong>跨分界面取扁圆柱高斯面，上下底 $\\Delta S$，高 $h\\to 0$。由 $\\oint\\mathbf{B}\\cdot d\\mathbf{S}=0$：")+
   fml("B_{2n}\\Delta S - B_{1n}\\Delta S = 0 \\implies B_{1n}=B_{2n}")+
   p("<strong>切向分量推导：</strong>跨分界面取小矩形环路，长边 $\\Delta l$ 平行界面，短边 $h\\to 0$。由 $\\oint\\mathbf{H}\\cdot d\\mathbf{l}=I_f$：")+
   fml("H_{2t}\\Delta l - H_{1t}\\Delta l = \\alpha_f\\Delta l \\implies H_{2t}-H_{1t}=\\alpha_f"))+
   note(p("对线性介质 $\\mathbf{B}=\\mu\\mathbf{H}$，无传导电流时 $B$ 线折射满足 $\\frac{\\tan\\theta_1}{\\tan\\theta_2}=\\frac{\\mu_1}{\\mu_2}$。铁磁质 $\\mu\\gg\\mu_0$，$B$ 线几乎垂直于铁磁质表面。"))
 )},
]},
]

# =====================================================
#  CHAPTER 5: 麦克斯韦方程组与电磁波
# =====================================================
ch5_sections = [
{
"name": "5.1 电磁感应",
"color": "#be185d",
"desc": "法拉第电磁感应定律与动生/感生电动势",
"items": [
{"id":"e5s1-1","name":"法拉第电磁感应定律","tags":["thm","der"],"brief":"磁通量变化产生感应电动势。",
 "fig":"induction","figCap":"变化磁场产生感应电动势",
 "body": wrap(
   thm("法拉第电磁感应定律",p("通过回路的磁通量发生变化时，回路中产生的感应电动势等于磁通量变化率的负值：")+
   fml("\\varepsilon = -\\frac{d\\Phi}{dt},\\qquad \\Phi = \\int_S \\mathbf{B}\\cdot d\\mathbf{S}"))+
   der(p("<strong>动生电动势推导：</strong>导体棒在磁场中以速度 $\\mathbf{v}$ 运动，自由电子受洛伦兹力 $\\mathbf{f}=-e\\mathbf{v}\\times\\mathbf{B}$，等效非静电场 $\\mathbf{E}_k=\\mathbf{v}\\times\\mathbf{B}$。电动势：")+
   fml("\\varepsilon = \\int_a^b (\\mathbf{v}\\times\\mathbf{B})\\cdot d\\mathbf{l}")+
   p("<strong>感生电动势：</strong>变化磁场激发涡旋电场 $\\mathbf{E}_i$，$\\oint\\mathbf{E}_i\\cdot d\\mathbf{l}=-\\frac{d\\Phi}{dt}$，即：")+
   fml("\\nabla\\times\\mathbf{E} = -\\frac{\\partial\\mathbf{B}}{\\partial t}"))
 )},
]},
{
"name": "5.2 位移电流与麦克斯韦方程组",
"color": "#be185d",
"desc": "位移电流假设与电磁场基本方程",
"items": [
{"id":"e5s2-1","name":"麦克斯韦方程组","tags":["thm","der"],"brief":"电磁场的完整理论体系。",
 "fig":"wave_em","figCap":"电磁波中 E、B 与传播方向互相垂直",
 "body": wrap(
   defn("位移电流",p("麦克斯韦假设：变化的电场等效于一种电流，称为位移电流。位移电流密度：")+
   fml("\\mathbf{j}_d = \\varepsilon_0\\frac{\\partial\\mathbf{E}}{\\partial t},\\qquad I_d = \\varepsilon_0\\frac{d\\Phi_e}{dt}"))+
   thm("麦克斯韦方程组（微分形式）",p("")+
   fml("\\nabla\\cdot\\mathbf{E} = \\frac{\\rho}{\\varepsilon_0} \\quad (\\text{电场的高斯定理})")+
   fml("\\nabla\\cdot\\mathbf{B} = 0 \\quad (\\text{磁场的高斯定理，无磁单极})")+
   fml("\\nabla\\times\\mathbf{E} = -\\frac{\\partial\\mathbf{B}}{\\partial t} \\quad (\\text{法拉第定律})")+
   fml("\\nabla\\times\\mathbf{B} = \\mu_0\\mathbf{j} + \\mu_0\\varepsilon_0\\frac{\\partial\\mathbf{E}}{\\partial t} \\quad (\\text{含位移电流的安培环路定理})"))+
   der(p("<strong>位移电流引入的必要性：</strong>对充电电容器，传导电流 $I_0$ 在极板间中断。若安培环路定理仅含传导电流，则 $\\oint\\mathbf{H}\\cdot d\\mathbf{l}$ 对不同环路结果矛盾。引入位移电流 $I_d=\\frac{d\\Phi_D}{dt}$ 后，$I_0=I_d$，矛盾消除。"))+
   note(p("麦克斯韦方程组预言了电磁波的存在，并计算出其速度 $c=1/\\sqrt{\\mu_0\\varepsilon_0}$，与光速一致，揭示了光的电磁本质。"))
 )},
]},
{
"name": "5.3 电磁波",
"color": "#be185d",
"desc": "平面电磁波的性质与能流密度",
"items": [
{"id":"e5s3-1","name":"电磁波的传播","tags":["thm","der"],"brief":"变化电磁场互相激发形成电磁波。",
 "body": wrap(
   thm("平面电磁波方程",p("在无电荷、无电流的真空中，由麦克斯韦方程组可推出电场和磁场满足波动方程：")+
   fml("\\nabla^2\\mathbf{E} = \\mu_0\\varepsilon_0\\frac{\\partial^2\\mathbf{E}}{\\partial t^2},\\qquad \\nabla^2\\mathbf{B} = \\mu_0\\varepsilon_0\\frac{\\partial^2\\mathbf{B}}{\\partial t^2}")+
   p("波速 $v=1/\\sqrt{\\mu_0\\varepsilon_0}=c\\approx 3\\times10^8\\,\\text{m/s}$。"))+
   der(p("<strong>推导：</strong>对 $\\nabla\\times\\mathbf{E}=-\\partial\\mathbf{B}/\\partial t$ 两边取旋度：")+
   fml("\\nabla\\times(\\nabla\\times\\mathbf{E}) = -\\frac{\\partial}{\\partial t}(\\nabla\\times\\mathbf{B})")+
   p("利用矢量恒等式 $\\nabla\\times(\\nabla\\times\\mathbf{E})=\\nabla(\\nabla\\cdot\\mathbf{E})-\\nabla^2\\mathbf{E}$，真空中 $\\nabla\\cdot\\mathbf{E}=0$，且 $\\nabla\\times\\mathbf{B}=\\mu_0\\varepsilon_0\\partial\\mathbf{E}/\\partial t$，代入得：")+
   fml("-\\nabla^2\\mathbf{E} = -\\mu_0\\varepsilon_0\\frac{\\partial^2\\mathbf{E}}{\\partial t^2} \\implies \\nabla^2\\mathbf{E} = \\mu_0\\varepsilon_0\\frac{\\partial^2\\mathbf{E}}{\\partial t^2}"))+
   thm("平面电磁波性质",p("(1) 横波：$\\mathbf{E}\\perp\\mathbf{B}\\perp$ 传播方向；(2) $\\mathbf{E}\\times\\mathbf{B}$ 沿传播方向；(3) $E=cB$；(4) 能流密度（坡印廷矢量）：")+
   fml("\\mathbf{S} = \\frac{1}{\\mu_0}\\mathbf{E}\\times\\mathbf{B}"))
 )},
]},
{
"name": "5.4 自感与互感",
"color": "#be185d",
"desc": "自感系数、互感系数及其推导",
"items": [
{"id":"e5s4-1","name":"自感与互感","tags":["def","der"],"brief":"回路自身与回路间的电磁感应。",
 "fig":"mutual_induct","figCap":"两线圈之间的互感",
 "body": wrap(
   defn("自感",p("回路电流 $I$ 产生的穿过自身的磁通量 $\\Phi=L I$，比例系数 $L$ 为自感系数。由法拉第定律，自感电动势：")+
   fml("\\varepsilon_L = -L\\frac{dI}{dt}")+
   der(p("<strong>长直螺线管自感推导：</strong>长度 $l$，匝数 $N$，截面积 $S$，管内 $B=\\mu_0 n I=\\mu_0 N I/l$。总磁链 $\\Psi=N\\Phi=NBS=\\mu_0 N^2 S I/l$，故：")+
   fml("L = \\frac{\\Psi}{I} = \\frac{\\mu_0 N^2 S}{l}")))+
   defn("互感",p("线圈 1 的电流 $I_1$ 产生的穿过线圈 2 的磁通量 $\\Phi_{21}=M_{21}I_1$。互感系数 $M=M_{12}=M_{21}$。互感电动势：")+
   fml("\\varepsilon_{21} = -M\\frac{dI_1}{dt},\\qquad \\varepsilon_{12} = -M\\frac{dI_2}{dt}"))+
   note(p("互感与自感的关系：$M=k\\sqrt{L_1 L_2}$，耦合系数 $0\\le k\\le 1$。无漏磁时 $k=1$。"))
 )},
]},
{
"name": "5.5 电磁场的能量与动量",
"color": "#be185d",
"desc": "电磁场能量密度、能流密度与动量密度",
"items": [
{"id":"e5s5-1","name":"电磁场能量与坡印廷矢量","tags":["thm","der"],"brief":"电磁场的能量密度与能流密度矢量。",
 "fig":"em_energy","figCap":"电磁波携带的电磁场能量",
 "body": wrap(
   thm("电磁场能量密度",p("电磁场单位体积的能量为电场能量密度与磁场能量密度之和：")+
   fml("w = \\frac{1}{2}\\mathbf{E}\\cdot\\mathbf{D} + \\frac{1}{2}\\mathbf{B}\\cdot\\mathbf{H} = \\frac{1}{2}\\varepsilon E^2 + \\frac{1}{2\\mu}B^2"))+
   der(p("<strong>推导（电容器储能）：</strong>平行板电容器储能 $W=\\frac{1}{2}CV^2=\\frac{1}{2}\\varepsilon E^2\\cdot Sd=w_e\\cdot V$，故电场能量密度 $w_e=\\frac{1}{2}\\varepsilon E^2$。类似地，螺线管储能 $W=\\frac{1}{2}LI^2=\\frac{1}{2\\mu}B^2\\cdot V$，故磁场能量密度 $w_m=\\frac{1}{2\\mu}B^2$。"))+
   thm("坡印廷矢量",p("单位时间通过单位面积的电磁场能量（能流密度）为坡印廷矢量：")+
   fml("\\mathbf{S} = \\mathbf{E}\\times\\mathbf{H} = \\frac{1}{\\mu_0}\\mathbf{E}\\times\\mathbf{B}")+
   p("其方向为电磁波传播方向。电磁场的动量密度 $\\mathbf{g}=\\frac{1}{c^2}\\mathbf{S}=\\varepsilon_0\\mathbf{E}\\times\\mathbf{B}$，光压即源于电磁场动量。"))
 )},
]},
{
"name": "5.6 法拉第定律与楞次定律",
"color": "#be185d",
"desc": "感应电动势方向的判断",
"items": [
{"id":"e5s6-1","name":"楞次定律","tags":["thm"],"brief":"感应电流的方向总是阻碍引起感应电流的磁通量变化。",
 "body": wrap(
   thm("楞次定律",p("闭合回路中感应电流的方向，总是使它所激发的磁场阻碍引起感应电流的磁通量的变化。楞次定律是能量守恒定律在电磁感应中的体现。")+
   fml("\\varepsilon = -\\frac{d\\Phi}{dt}")+
   p("负号正是楞次定律的数学表达。若磁通量 $\\Phi$ 增加（$d\\Phi/dt>0$），则 $\\varepsilon<0$，感应电流产生的磁场与原磁场反向，阻碍 $\\Phi$ 增加；反之亦然。"))+
   app(p("<strong>判断步骤：</strong>(1) 判断原磁通量的变化趋势（增或减）；(2) 确定感应电流磁场的方向（阻碍变化）；(3) 由右手定则确定感应电流方向。例如，磁铁 N 极插入线圈，线圈中感应电流产生的磁场阻碍磁通量增加，故靠近磁铁一侧为 N 极。"))
 )},
{"id":"e5s6-2","name":"感应电量","tags":["der"],"brief":"感应电流的总电量只与磁通量变化量有关。",
 "body": wrap(
   der(p("<strong>感应电量的推导：</strong>设回路电阻为 $R$，感应电流 $i=\\varepsilon/R=-\\frac{1}{R}\\frac{d\\Phi}{dt}$。在 $\\Delta t=t_2-t_1$ 时间内，通过回路横截面的感应电量：")+
   fml("q = \\int_{t_1}^{t_2} i\\,dt = -\\frac{1}{R}\\int_{\\Phi_1}^{\\Phi_2} d\\Phi = \\frac{\\Phi_1-\\Phi_2}{R}")+
   p("取绝对值：$q=\\frac{|\\Delta\\Phi|}{R}$。感应电量只与磁通量的变化量 $|\\Delta\\Phi|$ 和回路电阻 $R$ 有关，与磁通量变化的快慢（时间）无关。")+
   p("<strong>应用：</strong>磁通计（冲击电流计）利用感应电量测量磁通量。将探测线圈从磁场中快速拉出（$\\Phi_2=0$），测得电量 $q$，则 $\\Phi_1=qR$，从而求得磁感应强度 $B=\\Phi_1/(NS)$。"))
 )},
]},
{
"name": "5.7 动生电动势",
"color": "#be185d",
"desc": "导体在磁场中运动产生的电动势",
"items": [
{"id":"e5s7-1","name":"动生电动势的计算","tags":["der"],"brief":"导体切割磁力线产生的电动势。",
 "body": wrap(
   der(p("<strong>动生电动势的本质：</strong>导体在磁场中运动时，自由电子受洛伦兹力 $\\mathbf{f}=-e\\mathbf{v}\\times\\mathbf{B}$。洛伦兹力等效于非静电力，对应非静电场 $\\mathbf{E}_k=\\mathbf{v}\\times\\mathbf{B}$。动生电动势为非静电力移动单位正电荷做的功：")+
   fml("\\varepsilon = \\int_a^b \\mathbf{E}_k\\cdot d\\mathbf{l} = \\int_a^b (\\mathbf{v}\\times\\mathbf{B})\\cdot d\\mathbf{l}")+
   p("<strong>直导线切割磁力线：</strong>长 $l$ 的直导线在均匀磁场 $B$ 中以速度 $v$ 垂直切割磁力线（$v\\perp B\\perp l$）：")+
   fml("\\varepsilon = Blv")+
   p("方向由右手定则确定（拇指沿 $\\mathbf{v}$，食指沿 $\\mathbf{B}$，中指指向电动势方向，即电势升高方向）。"))
 )},
{"id":"e5s7-2","name":"交流发电机原理","tags":["app","der"],"brief":"线圈在磁场中转动产生正弦交流电。",
 "body": wrap(
   der(p("<strong>交流发电机：</strong>面积 $S$ 的 $N$ 匝线圈在均匀磁场 $B$ 中以角速度 $\\omega$ 绕垂直于 $B$ 的轴转动。$t$ 时刻线圈法向与 $B$ 夹角 $\\theta=\\omega t$，磁链：")+
   fml("\\Psi = NBS\\cos\\omega t")+
   p("感应电动势：")+
   fml("\\varepsilon = -\\frac{d\\Psi}{dt} = NBS\\omega\\sin\\omega t = \\varepsilon_0\\sin\\omega t")+
   p("其中 $\\varepsilon_0=NBS\\omega$ 为电动势峰值。产生正弦交流电，频率 $f=\\omega/(2\\pi)$。这是交流发电机的基本原理。"))
 )},
]},
{
"name": "5.8 感生电动势与涡旋电场",
"color": "#be185d",
"desc": "变化磁场激发的涡旋电场",
"items": [
{"id":"e5s8-1","name":"涡旋电场","tags":["thm","der"],"brief":"变化磁场激发涡旋电场，其环流等于磁通量变化率的负值。",
 "body": wrap(
   thm("涡旋电场",p("变化的磁场在其周围激发一种非静电性的电场，称为感生电场或涡旋电场。涡旋电场沿任意闭合回路的环流等于穿过回路磁通量变化率的负值：")+
   fml("\\oint_L \\mathbf{E}_i\\cdot d\\mathbf{l} = -\\frac{d\\Phi}{dt} = -\\int_S\\frac{\\partial\\mathbf{B}}{\\partial t}\\cdot d\\mathbf{S}"))+
   der(p("<strong>微分形式：</strong>由斯托克斯定理 $\\oint_L\\mathbf{E}_i\\cdot d\\mathbf{l}=\\int_S(\\nabla\\times\\mathbf{E}_i)\\cdot d\\mathbf{S}$，比较得：")+
   fml("\\nabla\\times\\mathbf{E}_i = -\\frac{\\partial\\mathbf{B}}{\\partial t}")+
   p("<strong>涡旋电场与静电场的区别：</strong>静电场由电荷激发，是保守场（$\\nabla\\times\\mathbf{E}=0$），电场线不闭合；涡旋电场由变化磁场激发，是非保守场（$\\nabla\\times\\mathbf{E}\\neq0$），电场线是闭合曲线。涡旋电场的存在不依赖于导体回路。"))+
   app(p("<strong>电子感应加速器：</strong>利用变化磁场产生的涡旋电场加速电子。要求磁场分布满足 $B_R=\\frac{1}{2}\\bar{B}$（轨道处磁场为平均磁场的一半），使电子在固定半径轨道上被加速。"))
 )},
]},
{
"name": "5.9 自感与互感的深入",
"color": "#be185d",
"desc": "RL 电路暂态过程与互感系数的计算",
"items": [
{"id":"e5s9-1","name":"RL 电路的暂态过程","tags":["der"],"brief":"电流增长和衰减的指数规律。",
 "body": wrap(
   der(p("<strong>电流增长：</strong>RL 电路接电源 $\\mathcal{E}$，由基尔霍夫定律：$\\mathcal{E}=IR+L\\frac{dI}{dt}$。初始条件 $I(0)=0$，解为：")+
   fml("I(t) = \\frac{\\mathcal{E}}{R}\\left(1-e^{-Rt/L}\\right) = I_\\infty\\left(1-e^{-t/\\tau}\\right)")+
   p("时间常数 $\\tau=L/R$。电流指数上升趋近稳态值 $I_\\infty=\\mathcal{E}/R$。")+
   p("<strong>电流衰减：</strong>断开电源后短路，$0=IR+L\\frac{dI}{dt}$，初始 $I(0)=I_0$：")+
   fml("I(t) = I_0 e^{-t/\\tau}")+
   p("时间常数 $\\tau=L/R$ 越大，电流衰减越慢，体现自感阻碍电流变化的特性。"))
 )},
{"id":"e5s9-2","name":"互感系数的计算","tags":["der"],"brief":"由磁通量计算互感系数。",
 "body": wrap(
   der(p("<strong>互感的定义：</strong>线圈 1 通电流 $I_1$，产生穿过线圈 2 的磁通匝链数 $\\Psi_{21}=M I_1$；线圈 2 通电流 $I_2$，产生穿过线圈 1 的磁通匝链数 $\\Psi_{12}=M I_2$。可以证明 $M_{12}=M_{21}=M$。")+
   p("<strong>互感与自感的关系：</strong>$M=k\\sqrt{L_1 L_2}$，其中耦合系数 $0\\le k\\le 1$。$k=1$ 为完全耦合（无漏磁），$k=0$ 为无耦合。")+
   p("<strong>例：两共轴螺线管的互感</strong>。长 $l$，截面积 $S$，匝数分别 $N_1,N_2$，管内磁导率 $\\mu$。线圈 1 产生的磁场 $B=\\mu\\frac{N_1 I_1}{l}$，穿过线圈 2 的磁通匝链数 $\\Psi_{21}=N_2 BS=\\mu\\frac{N_1 N_2 S}{l}I_1$，故：")+
   fml("M = \\frac{\\Psi_{21}}{I_1} = \\frac{\\mu N_1 N_2 S}{l}")+
   p("完全耦合时 $M=\\sqrt{L_1 L_2}$，其中 $L_1=\\frac{\\mu N_1^2 S}{l}$，$L_2=\\frac{\\mu N_2^2 S}{l}$。"))
 )},
]},
{
"name": "5.10 磁场能量与能量密度",
"color": "#be185d",
"desc": "螺线管储能与磁场能量密度",
"items": [
{"id":"e5s10-1","name":"磁场能量密度","tags":["der"],"brief":"磁场能量密度为 ½B·H。",
 "body": wrap(
   der(p("<strong>长直螺线管储能：</strong>自感 $L=\\frac{\\mu N^2 S}{l}$，通电流 $I$ 时储能 $W=\\frac{1}{2}LI^2$。管内磁场 $B=\\mu n I=\\mu\\frac{N I}{l}$，即 $I=\\frac{Bl}{\\mu N}$。代入：")+
   fml("W = \\frac{1}{2}\\cdot\\frac{\\mu N^2 S}{l}\\cdot\\frac{B^2 l^2}{\\mu^2 N^2} = \\frac{1}{2}\\frac{B^2}{\\mu}\\cdot Sl")+
   p("体积 $V=Sl$，故磁场能量密度：")+
   fml("w_m = \\frac{W}{V} = \\frac{1}{2}\\frac{B^2}{\\mu} = \\frac{1}{2}\\mathbf{B}\\cdot\\mathbf{H}")+
   p("总磁场能量 $W_m=\\int_V w_m\\,dV=\\frac{1}{2}\\int_V\\mathbf{B}\\cdot\\mathbf{H}\\,dV$。"))+
   note(p("与电场能量密度 $w_e=\\frac{1}{2}\\mathbf{D}\\cdot\\mathbf{E}$ 对比，电磁场总能量密度 $w=w_e+w_m=\\frac{1}{2}(\\mathbf{E}\\cdot\\mathbf{D}+\\mathbf{B}\\cdot\\mathbf{H})$。磁场能量存储于磁场中，是一种场的能量。"))
 )},
]},
{
"name": "5.11 位移电流的深入",
"color": "#be185d",
"desc": "电容器中的位移电流与全电流定律",
"items": [
{"id":"e5s11-1","name":"位移电流与全电流定律","tags":["der"],"brief":"充电电容器极板间的位移电流。",
 "body": wrap(
   der(p("<strong>平行板电容器充电：</strong>极板面积 $S$，间距 $d$，充电电流 $I_c$。极板间电场 $E=\\sigma/\\varepsilon=Q/(\\varepsilon S)$，电位移 $D=\\sigma=Q/S$。电位移通量 $\\Phi_D=DS=Q$。")+
   p("传导电流 $I_c=\\frac{dQ}{dt}$，而位移电流：")+
   fml("I_d = \\frac{d\\Phi_D}{dt} = \\frac{dQ}{dt} = I_c")+
   p("即极板间的位移电流等于导线中的传导电流，电流在电容器处「连续」。位移电流密度 $\\mathbf{j}_d=\\frac{\\partial\\mathbf{D}}{\\partial t}$。")+
   p("<strong>全电流定律：</strong>传导电流与位移电流之和为全电流，全电流永远连续：")+
   fml("\\oint_L\\mathbf{H}\\cdot d\\mathbf{l} = I_c + I_d = \\int_S\\left(\\mathbf{j}_c+\\frac{\\partial\\mathbf{D}}{\\partial t}\\right)\\cdot d\\mathbf{S}")+
   p("这就是含位移电流的安培环路定理（全电流定律），保证了电流连续性方程。"))
 )},
]},
{
"name": "5.12 麦克斯韦方程组的积分形式",
"color": "#be185d",
"desc": "积分形式的麦克斯韦方程组",
"items": [
{"id":"e5s12-1","name":"麦克斯韦方程组（积分形式）","tags":["thm"],"brief":"电磁场的四个积分方程。",
 "body": wrap(
   thm("麦克斯韦方程组（积分形式）",p("麦克斯韦方程组的积分形式为：")+
   fml("\\oint_S\\mathbf{D}\\cdot d\\mathbf{S} = \\int_V\\rho\\,dV \\quad (\\text{电场的高斯定理})")+
   fml("\\oint_S\\mathbf{B}\\cdot d\\mathbf{S} = 0 \\quad (\\text{磁场的高斯定理})")+
   fml("\\oint_L\\mathbf{E}\\cdot d\\mathbf{l} = -\\int_S\\frac{\\partial\\mathbf{B}}{\\partial t}\\cdot d\\mathbf{S} \\quad (\\text{法拉第电磁感应定律})")+
   fml("\\oint_L\\mathbf{H}\\cdot d\\mathbf{l} = \\int_S\\left(\\mathbf{j}+\\frac{\\partial\\mathbf{D}}{\\partial t}\\right)\\cdot d\\mathbf{S} \\quad (\\text{全电流定律})"))+
   note(p("积分形式适用于有限区域，微分形式适用于场中每一点。两者等价，可通过高斯公式和斯托克斯公式互相转换。介质方程 $\\mathbf{D}=\\varepsilon\\mathbf{E}$，$\\mathbf{B}=\\mu\\mathbf{H}$，$\\mathbf{j}=\\sigma\\mathbf{E}$ 与麦克斯韦方程组共同构成完整的电磁场理论。"))
 )},
]},
{
"name": "5.13 电磁波的产生与辐射",
"color": "#be185d",
"desc": "电偶极辐射与电磁波的发射",
"items": [
{"id":"e5s13-1","name":"电偶极辐射","tags":["der"],"brief":"振荡电偶极子辐射电磁波。",
 "body": wrap(
   der(p("<strong>振荡电偶极子：</strong>电偶极矩随时间做简谐变化 $\\mathbf{p}(t)=p_0\\cos\\omega t\\,\\hat{\\mathbf{z}}$。在远区（$r\\gg\\lambda$），辐射场为球面横波，电场和磁场分量为：")+
   fml("E_\\theta = \\frac{\\mu_0 p_0\\omega^2\\sin\\theta}{4\\pi r}\\cos\\omega\\left(t-\\frac{r}{c}\\right)")+
   fml("B_\\varphi = \\frac{\\mu_0 p_0\\omega^2\\sin\\theta}{4\\pi c r}\\cos\\omega\\left(t-\\frac{r}{c}\\right)")+
   p("其中 $\\theta$ 为位置矢量与偶极子轴的夹角。辐射场按 $1/r$ 衰减，是横波，$\\mathbf{E}\\perp\\mathbf{B}\\perp$ 传播方向。")+
   p("<strong>辐射功率：</strong>平均辐射功率（拉莫尔公式推广）：")+
   fml("\\bar{P} = \\frac{\\mu_0 p_0^2\\omega^4}{12\\pi c}")+
   p("辐射功率与频率的四次方成正比，这就是为什么广播和通信需要高频载波。天线辐射即基于振荡电偶极子原理。"))
 )},
]},
{
"name": "5.14 电磁波谱",
"color": "#be185d",
"desc": "电磁波按波长/频率的分类",
"items": [
{"id":"e5s14-1","name":"电磁波谱","tags":["def"],"brief":"电磁波按频率从低到高的分类。",
 "body": wrap(
   defn("电磁波谱",p("电磁波按波长（或频率）由长到短可分为：")+
   p("<strong>无线电波</strong>：$\\lambda>1\\,\\text{mm}$，$f<3\\times10^{11}\\,\\text{Hz}$，用于通信、广播、雷达。")+
   p("<strong>微波</strong>：$\\lambda=1\\,\\text{mm}\\sim1\\,\\text{m}$，用于雷达、卫星通信、微波炉。")+
   p("<strong>红外线</strong>：$\\lambda=760\\,\\text{nm}\\sim1\\,\\text{mm}$，热效应，用于红外遥感、加热。")+
   p("<strong>可见光</strong>：$\\lambda=400\\sim760\\,\\text{nm}$，人眼可见，红橙黄绿蓝靛紫。")+
   p("<strong>紫外线</strong>：$\\lambda=10\\sim400\\,\\text{nm}$，化学效应、荧光、杀菌。")+
   p("<strong>X 射线</strong>：$\\lambda=0.01\\sim10\\,\\text{nm}$，穿透性强，用于医学透视、晶体衍射。")+
   p("<strong>$\\gamma$ 射线</strong>：$\\lambda<0.01\\,\\text{nm}$，核辐射，能量极高，用于放疗、探伤。")+
   p("所有电磁波在真空中速度均为 $c=3\\times10^8\\,\\text{m/s}$，满足 $c=\\lambda f$。"))
 )},
]},
{
"name": "5.15 电磁波的动量与光压",
"color": "#be185d",
"desc": "电磁场的动量密度与辐射压强",
"items": [
{"id":"e5s15-1","name":"电磁波的动量与光压","tags":["der"],"brief":"电磁波具有动量，照射物体产生光压。",
 "body": wrap(
   der(p("<strong>电磁场动量密度：</strong>电磁场不仅具有能量，还具有动量。动量密度（单位体积动量）为：")+
   fml("\\mathbf{g} = \\frac{1}{c^2}\\mathbf{S} = \\varepsilon_0\\mathbf{E}\\times\\mathbf{B}")+
   p("方向沿波的传播方向。对平面电磁波，$S=w c$（$w$ 为能量密度），故 $g=w/c$。")+
   p("<strong>光压：</strong>电磁波照射物体表面，动量转移产生压强。对完全吸收面，光压 $P=\\frac{S}{c}=\\frac{I}{c}$（$I$ 为光强）；对完全反射面，光压 $P=\\frac{2I}{c}$。")+
   fml("P_{\\text{吸收}} = \\frac{I}{c},\\qquad P_{\\text{反射}} = \\frac{2I}{c}")+
   p("光压在天文上有重要作用，如太阳帆、彗尾背向太阳等。"))
 )},
]},
{
"name": "5.16 电磁场的矢势与标势",
"color": "#be185d",
"desc": "用矢势和标势描述电磁场及规范变换",
"items": [
{"id":"e5s16-1","name":"矢势、标势与规范变换","tags":["def","thm"],"brief":"由势函数描述电磁场，存在规范自由度。",
 "body": wrap(
   defn("矢势与标势",p("由 $\\nabla\\cdot\\mathbf{B}=0$，可引入矢势 $\\mathbf{A}$ 使 $\\mathbf{B}=\\nabla\\times\\mathbf{A}$。代入 $\\nabla\\times\\mathbf{E}=-\\partial\\mathbf{B}/\\partial t$，得 $\\nabla\\times(\\mathbf{E}+\\partial\\mathbf{A}/\\partial t)=0$，故可引入标势 $\\varphi$：")+
   fml("\\mathbf{E} = -\\nabla\\varphi - \\frac{\\partial\\mathbf{A}}{\\partial t}"))+
   thm("规范变换",p("$\\mathbf{A}$ 和 $\\varphi$ 的选择不唯一。对任意标量函数 $\\psi(\\mathbf{r},t)$，做变换：")+
   fml("\\mathbf{A}' = \\mathbf{A}+\\nabla\\psi,\\qquad \\varphi' = \\varphi - \\frac{\\partial\\psi}{\\partial t}")+
   p("$\\mathbf{E}$ 和 $\\mathbf{B}$ 保持不变。这种变换称为规范变换。常用规范：库仑规范 $\\nabla\\cdot\\mathbf{A}=0$，洛伦兹规范 $\\nabla\\cdot\\mathbf{A}+\\mu_0\\varepsilon_0\\frac{\\partial\\varphi}{\\partial t}=0$。"))+
   der(p("<strong>达朗贝尔方程：</strong>在洛伦兹规范下，$\\mathbf{A}$ 和 $\\varphi$ 满足波动方程：")+
   fml("\\nabla^2\\mathbf{A}-\\mu_0\\varepsilon_0\\frac{\\partial^2\\mathbf{A}}{\\partial t^2} = -\\mu_0\\mathbf{j}")+
   fml("\\nabla^2\\varphi-\\mu_0\\varepsilon_0\\frac{\\partial^2\\varphi}{\\partial t^2} = -\\frac{\\rho}{\\varepsilon_0}")+
   p("这表明势以光速 $c=1/\\sqrt{\\mu_0\\varepsilon_0}$ 传播，电磁波是矢势和标势的波动。"))
 )},
]},
]

CHAPTERS = [
    {"id":"e-ch1","num":"第一章","title":"静电场","en":"ELECTROSTATICS",
     "desc":"库仑定律、电场强度、高斯定理、电势与电势能、电容与电容器。",
     "sections": ch1_sections},
    {"id":"e-ch2","num":"第二章","title":"介质中的静电场","en":"DIELECTRICS",
     "desc":"电介质极化、极化强度与束缚电荷、电位移矢量、介质中的高斯定理。",
     "sections": ch2_sections},
    {"id":"e-ch3","num":"第三章","title":"静磁场","en":"MAGNETOSTATICS",
     "desc":"毕奥-萨伐尔定律、安培环路定理、洛伦兹力与安培力、磁矩。",
     "sections": ch3_sections},
    {"id":"e-ch4","num":"第四章","title":"介质中的静磁场","en":"MAGNETIC MEDIA",
     "desc":"磁介质磁化、磁化强度、磁场强度、介质中的安培环路定理、铁磁质。",
     "sections": ch4_sections},
    {"id":"e-ch5","num":"第五章","title":"麦克斯韦方程组与电磁波","en":"MAXWELL & EM WAVES",
     "desc":"法拉第电磁感应定律、位移电流、麦克斯韦方程组、平面电磁波与坡印廷矢量。",
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
  .la-phase-title.e-ch1::before{background:#2563eb}
  .la-phase-title.e-ch2::before{background:#0d9488}
  .la-phase-title.e-ch3::before{background:#059669}
  .la-phase-title.e-ch4::before{background:#0891b2}
  .la-phase-title.e-ch5::before{background:#be185d}
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
<meta name="description" content="电磁学知识体系：静电场、介质中的静电场、静磁场、介质中的静磁场、麦克斯韦方程组与电磁波">
<title>电磁学 · 知识体系</title>
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
    <div class="la-eyebrow">ELECTROMAGNETISM · KNOWLEDGE MAP</div>
    <h1>电磁学 · 知识体系</h1>
    <p class="la-subtitle">静电场 · 介质中的静电场 · 静磁场 · 介质中的静磁场 · 麦克斯韦方程组与电磁波</p>
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
    <div>电磁学 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于电磁学核心知识体系整理</div>
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
    with open("/workspace/electromagnetism.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated electromagnetism.html ({len(html)} chars)")
