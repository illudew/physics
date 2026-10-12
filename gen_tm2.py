# -*- coding: utf-8 -*-
"""Regenerate theoretical-mechanics.html with expanded derivations and restructured chapters."""
import json

# ---------- SVG figure library ----------
FIG = {
"pendulum": '''<svg viewBox="0 0 120 160" xmlns="http://www.w3.org/2000/svg">
<line x1="60" y1="10" x2="60" y2="130" stroke="#475569" stroke-width="2"/>
<circle cx="60" cy="135" r="18" fill="#60a5fa" stroke="#2563eb" stroke-width="2"/>
<path d="M60 10 L40 10 L60 25 Z" fill="#94a3b8"/></svg>''',
"double_pendulum": '''<svg viewBox="0 0 160 200" xmlns="http://www.w3.org/2000/svg">
<line x1="80" y1="10" x2="80" y2="80" stroke="#475569" stroke-width="2"/>
<circle cx="80" cy="85" r="14" fill="#60a5fa" stroke="#2563eb" stroke-width="2"/>
<line x1="80" y1="85" x2="110" y2="160" stroke="#475569" stroke-width="2"/>
<circle cx="110" cy="165" r="14" fill="#34d399" stroke="#059669" stroke-width="2"/>
<path d="M80 10 L60 10 L80 25 Z" fill="#94a3b8"/></svg>''',
"central_force": '''<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
<circle cx="100" cy="80" r="8" fill="#f59e0b"/>
<ellipse cx="100" cy="80" rx="70" ry="40" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="160" cy="80" r="7" fill="#ef4444"/>
<line x1="100" y1="80" x2="160" y2="80" stroke="#94a3b8" stroke-dasharray="4 3"/></svg>''',
"rigid_body": '''<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="100" cy="80" rx="60" ry="40" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
<line x1="40" y1="80" x2="160" y2="80" stroke="#ef4444" stroke-width="2" stroke-dasharray="5 3"/>
<circle cx="100" cy="80" r="4" fill="#1e293b"/>
<text x="105" y="70" font-size="11" fill="#1e293b">ω</text></svg>''',
"euler_angles": '''<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="120" x2="180" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="100" y1="20" x2="100" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="100" y1="120" x2="160" y2="60" stroke="#3b82f6" stroke-width="2.5"/>
<line x1="100" y1="120" x2="40" y2="60" stroke="#10b981" stroke-width="2.5"/>
<path d="M130 120 A30 30 0 0 0 116 94" fill="none" stroke="#f59e0b" stroke-width="2"/>
<text x="125" y="100" font-size="11" fill="#f59e0b">φ</text></svg>''',
"phase_space": '''<svg viewBox="0 0 180 140" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="120" x2="170" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="120" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<ellipse cx="95" cy="70" rx="55" ry="35" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="150" cy="70" r="3" fill="#ef4444"/>
<text x="155" y="74" font-size="11" fill="#ef4444">H=E</text></svg>''',
"poisson": '''<svg viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg">
<circle cx="60" cy="60" r="35" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="140" cy="60" r="35" fill="none" stroke="#10b981" stroke-width="2"/>
<text x="50" y="64" font-size="11" fill="#2563eb">f</text>
<text x="130" y="64" font-size="11" fill="#059669">g</text>
<text x="92" y="55" font-size="11" fill="#ef4444">{f,g}</text></svg>''',
"kepler": '''<svg viewBox="0 0 220 140" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="110" cy="70" rx="90" ry="45" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="60" cy="70" r="10" fill="#f59e0b"/>
<circle cx="150" cy="80" r="7" fill="#3b82f6"/>
<line x1="60" y1="70" x2="150" y2="80" stroke="#94a3b8" stroke-dasharray="4 3"/>
<text x="60" y="55" font-size="10" fill="#f59e0b">太阳</text>
<text x="150" y="100" font-size="10" fill="#3b82f6">行星</text></svg>''',
"foucault": '''<svg viewBox="0 0 160 180" xmlns="http://www.w3.org/2000/svg">
<line x1="80" y1="10" x2="80" y2="100" stroke="#475569" stroke-width="1.5"/>
<circle cx="80" cy="105" r="12" fill="#60a5fa" stroke="#2563eb" stroke-width="2"/>
<ellipse cx="80" cy="105" rx="50" ry="20" fill="none" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4 3"/>
<path d="M80 10 L60 10 L80 25 Z" fill="#94a3b8"/>
<text x="100" y="70" font-size="10" fill="#10b981">摆动面旋转</text></svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

# 核心公式清单（从全部知识点中梳理）
CORE_FORMULAS = [
    ("欧拉-拉格朗日方程", "\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha} - \\frac{\\partial L}{\\partial q_\\alpha} = 0", "第一章 · 拉格朗日力学的基本运动方程"),
    ("最小作用量原理", "\\delta S = 0,\\qquad S = \\int_{t_1}^{t_2} L(q,\\dot q,t)\\,dt", "真实运动使作用量取极值"),
    ("诺特定理", "Q = \\sum_\\alpha p_\\alpha(\\Delta q_\\alpha - \\dot q_\\alpha\\,\\Delta t) + L\\,\\Delta t - F = \\text{常数}", "连续对称性 $\\Leftrightarrow$ 守恒量"),
    ("勒让德变换", "H = \\sum_\\alpha p_\\alpha \\dot q_\\alpha - L,\\qquad p_\\alpha = \\frac{\\partial L}{\\partial\\dot q_\\alpha}", "从拉格朗日到哈密顿的桥梁"),
    ("哈密顿正则方程", "\\dot q_\\alpha = \\frac{\\partial H}{\\partial p_\\alpha},\\qquad \\dot p_\\alpha = -\\frac{\\partial H}{\\partial q_\\alpha}", "哈密顿力学的运动方程"),
    ("泊松括号", "\\{f,g\\} = \\sum_\\alpha\\left(\\frac{\\partial f}{\\partial q_\\alpha}\\frac{\\partial g}{\\partial p_\\alpha} - \\frac{\\partial f}{\\partial p_\\alpha}\\frac{\\partial g}{\\partial q_\\alpha}\\right)", "李代数结构的基础"),
    ("守恒判据", "\\frac{df}{dt} = \\{f,H\\} + \\frac{\\partial f}{\\partial t},\\qquad f\\text{ 守恒} \\Leftrightarrow \\{f,H\\}=0", "泊松括号判断守恒量"),
    ("哈密顿-雅可比方程", "H\\!\\left(q,\\frac{\\partial S}{\\partial q},t\\right) + \\frac{\\partial S}{\\partial t} = 0", "化偏微分方程为常微分方程"),
    ("正则变换条件", "\\sum p_\\alpha\\,dq_\\alpha - H\\,dt = \\sum P_\\alpha\\,dQ_\\alpha - K\\,dt + dF", "母函数生成正则变换"),
    ("小振动本征值方程", "\\det(V - \\omega^2 A) = 0", "简正频率的广义本征值问题"),
    ("欧拉动力学方程", "I_1\\dot\\omega_1 - (I_2-I_3)\\omega_2\\omega_3 = N_1", "刚体定点转动的基本方程"),
    ("广义势能（电磁场）", "U = q\\phi - q\\vec v\\cdot\\vec A", "洛伦兹力的速度相关势能"),
    ("科里奥利力", "\\vec F_C = -2m\\,\\vec\\omega\\times\\vec v'", "转动参考系中的惯性力"),
    ("傅科摆进动角速度", "\\Omega = \\omega\\sin\\lambda", "纬度 $\\lambda$ 处的进动速率"),
    ("拉格朗日函数不唯一性", "L' = L + \\frac{df}{dt} \\quad\\Rightarrow\\quad \\text{运动方程不变}", "规范不变性"),
    ("龙格-楞次矢量", "\\vec A = \\vec p\\times\\vec L - mk\\,\\hat r = \\text{常数}", "开普勒问题的隐藏对称性（$SO(4)$）"),
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
#  CHAPTER 1: 拉格朗日力学 (诺特定理保留在此)
# =====================================================
ch1_sections = [

# ---- 1.1 约束与广义坐标 ----
{
"name": "1.1 约束与广义坐标",
"color": "#2563eb",
"desc": "完整约束、非完整约束、广义坐标、虚位移与理想约束",
"items": [
{"id":"tm-c1s1-1","name":"约束的概念","tags":["def","exa"],"brief":"对运动的限制，纯运动学概念。",
 "body": wrap(
    defn("约束", p("约束是对运动的限制，是一个纯运动学的概念。对于 $n$ 个质点组成的体系，约束方程限制了质点坐标之间的关系。约束不涉及力和质量，仅从几何或运动学角度限制可能的运动。"))
    + exa(p("<strong>单摆：</strong>约束方程 $x^2+y^2=L^2$，质点被限制在半径为 $L$ 的圆周上运动。<br><strong>光滑球形碗内小球：</strong>$x^2+y^2+z^2=R^2$，小球被限制在球面上。<br><strong>轻杆连接两质点：</strong>$(x_1-x_2)^2+(y_1-y_2)^2+(z_1-z_2)^2=L^2$。<br><strong>刚体：</strong>任意两点间距固定，$|\\vec r_i-\\vec r_j|=$ 常数，对所有 $i,j$。"))
)},
{"id":"tm-c1s1-2","name":"完整约束","tags":["def","thm","exa"],"brief":"仅含坐标与时间的约束。",
 "body": wrap(
    defn("完整约束", p("约束条件只和体系各质点的坐标 $\\vec r_i$ 及时间 $t$ 相关的约束称为完整约束（full constraint），其约束方程为")+
    fml("f_j(\\vec r_1,\\vec r_2,\\dots,\\vec r_n,t)=0,\\quad 1\\le j\\le k",
        "由 $k$ 个约束方程可消去 $k$ 个不独立坐标，独立坐标数目由 $3n$ 减为 $3n-k$，即系统自由度 $s=3n-k$。"))
    + thm("几何意义", p("约束方程在 $3n$ 维欧几里得空间中确定了一个 $3n-k$ 维高维曲面（流形），系统的构型点被限制在此曲面上运动。"))
    + exa(p("<strong>刚体：</strong>$N$ 个质点构成的刚体在欧几里得空间 $\\mathbb R^{3N}$ 中，约束曲面为 $\\mathbb R^3\\times SO(3)$，其中 $SO(3)=\\{M|M^T M=I_3,\\det M=1\\}$ 为三维特殊正交群，描述刚体的取向。"))
)},
{"id":"tm-c1s1-3","name":"广义坐标","tags":["def","exa","note"],"brief":"确定体系构型的独立坐标。",
 "body": wrap(
    defn("广义坐标", p("确定一个力学体系构型所需要的独立坐标称为广义坐标，记为 $q_1,q_2,\\dots,q_s$，其中 $s$ 为自由度。广义坐标的选取不唯一，只要能唯一确定系统构型即可。"))
    + exa(p("<strong>球面上运动的小球：</strong>广义坐标为球角 $(\\theta,\\varphi)$。<br><strong>刚体：</strong>广义坐标为质心位置 $(x_0,y_0,z_0)$ 及三个欧拉角 $(\\varphi,\\theta,\\psi)$。<br><strong>平面双摆：</strong>广义坐标为两个摆角 $(\\theta_1,\\theta_2)$。"))
    + note(p("广义坐标与系统构型不一定全局一一对应。例如球面坐标在 $\\theta=0$ 和 $\\theta=\\pi$ 处存在奇点，因此高维曲面通常需要用多个坐标系（图册，atlas）覆盖。"))
)},
{"id":"tm-c1s1-4","name":"非完整约束","tags":["def","thm","exa"],"brief":"含速度且不可积的约束。",
 "body": wrap(
    defn("非完整约束", p("形如 $f(\\vec r_1,\\dots,\\vec r_n,\\dot{\\vec r}_1,\\dots,\\dot{\\vec r}_n,t)=0$，且不能通过积分化为 $g(\\vec r_1,\\dots,\\vec r_n,t)=0$ 形式的约束称为非完整约束。其特点是无法减少独立坐标数目，系统自由度 $s$ 小于独立坐标数。"))
    + thm("线性约束可积的充要条件", p("线性微分约束 $\\sum_i(A_i dx_i+B_i dy_i+C_i dz_i)+D\\,dt=0$ 为完整约束的充要条件是可化为全微分形式，即存在 $\\Phi$ 和 $F$ 使左边 $=\\Phi\\,dF$。用微分形式语言等价地，设 $\\omega$ 为左边的微分形式，则")+
    fml("\\omega\\wedge d\\omega = 0",
        "这是弗罗贝尼乌斯（Frobenius）可积性条件。"))
    + exa(p("<strong>$x\\dot x+y\\dot y=0$ 是完整约束：</strong>因 $x\\dot x+y\\dot y=\\frac{d(x^2+y^2)}{2dt}=0$，积分得 $x^2+y^2=$ 常数。<br><strong>平面纯滚动圆盘是非完整约束：</strong>接触点速度为零给出 $\\dot x-r\\dot\\varphi\\sin\\theta=0$，$\\dot y+r\\dot\\varphi\\cos\\theta=0$，这两个方程不可积，系统有 5 个坐标但仅 3 个自由度。"))
)},
{"id":"tm-c1s1-5","name":"虚位移与理想约束","tags":["def","thm","der","exa"],"brief":"固定时刻约束允许的无穷小位移；约束力虚功和为零。",
 "body": wrap(
    defn("虚位移", p("固定时刻 $t$，约束所允许的无穷小位移称为虚位移，记为 $(\\delta\\vec r_1,\\delta\\vec r_2,\\dots,\\delta\\vec r_n)$。虚位移与真实位移 $d\\vec r_i$ 的区别在于：虚位移中 $\\delta t=0$，而真实位移中 $dt\\neq 0$。几何上，构型 $P$ 处所有虚位移张成的线性空间是 $3n-k$ 维流形在 $P$ 点的切空间。"))
    + defn("理想约束", p("约束力虚功和恒为零的约束称为理想约束：")+
    fml("\\sum_{i=1}^{n} \\vec F_{Ni}\\cdot\\delta\\vec r_i = 0",
        "几何意义：约束力沿高维曲面的法向（对完整约束），而虚位移沿切向，故虚功为零。"))
    + der(p("对于刚性轻杆连接的两质点，约束力沿杆方向：$\\vec F_{N1}=\\lambda(\\vec r_1-\\vec r_2)$，$\\vec F_{N2}=-\\lambda(\\vec r_1-\\vec r_2)$。则约束力虚功和为")+
    fml("\\vec F_{N1}\\cdot\\delta\\vec r_1+\\vec F_{N2}\\cdot\\delta\\vec r_2 = \\lambda(\\vec r_1-\\vec r_2)\\cdot(\\delta\\vec r_1-\\delta\\vec r_2) = \\frac{\\lambda}{2}\\delta[(\\vec r_1-\\vec r_2)^2] = 0",
        "最后一步利用了刚性约束 $|\\vec r_1-\\vec r_2|=$ 常数，故其变分为零。"))
    + exa(p("理想约束实例：光滑曲面（约束力法向，虚位移切向）、刚性轻杆、刚体（内力虚功和为零）、光滑接触表面、纯滚动（完全粗糙）接触。"))
)},
{"id":"tm-c1s1-6","name":"约束力与拉格朗日乘子法","tags":["thm","der","app","exa"],"brief":"求非理想约束或约束力的方法。",
 "body": wrap(
    thm("拉格朗日乘子法", p("若需求约束力，或约束为非完整约束（不能消去坐标），可使用拉格朗日乘子法。设约束方程为 $f_j(q,t)=0$（$j=1,\\dots,k$），引入 $k$ 个拉格朗日乘子 $\\lambda_j$，构造修正的拉格朗日函数")+
    fml("\\tilde L = L + \\sum_{j=1}^{k}\\lambda_j f_j(q,t)",
        "此时将 $q_\\alpha$ 和 $\\lambda_j$ 都视为独立变量，对它们应用欧拉-拉格朗日方程。"))
    + der(p("<strong>推导：</strong>对 $q_\\alpha$ 的欧拉-拉格朗日方程：")+
    fml("\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha}-\\frac{\\partial L}{\\partial q_\\alpha} = \\sum_j\\lambda_j\\frac{\\partial f_j}{\\partial q_\\alpha}",
        "右边 $\\sum_j\\lambda_j\\frac{\\partial f_j}{\\partial q_\\alpha}$ 即为约束力的广义分量。<br>对 $\\lambda_j$ 的欧拉-拉格朗日方程（注意 $\\lambda_j$ 不含 $\\dot q$）：$\\frac{\\partial\\tilde L}{\\partial\\lambda_j}=f_j=0$，即恢复约束方程。<br>这样共有 $s+k$ 个方程，可同时解出 $s$ 个 $q_\\alpha(t)$ 和 $k$ 个 $\\lambda_j(t)$。"))
    + der(p("<strong>约束力的物理意义：</strong>对完整约束 $f_j(q,t)=0$，约束力沿约束曲面法向，其大小由 $\\lambda_j$ 给出。具体地，约束力对第 $i$ 个质点的分量为")+
    fml("\\vec F_{Ni} = \\sum_j \\lambda_j\\nabla_i f_j",
        '其中 $\\nabla_i$ 为对 $\\vec r_i$ 的梯度。<br>对粒子被限制在曲面 $f(\\vec r)=0$ 上的情形，$\\nabla f$ 沿曲面法向，约束力 $\\vec F_N=\\lambda\\nabla f$ 也沿法向，与"约束力沿约束面法向"的几何图像一致。'))
    + exa(p("<strong>单摆（求张力）：</strong>约束 $f=x^2+y^2-L^2=0$，引入乘子 $\\lambda$。修正拉氏量 $\\tilde L=\\frac{1}{2}m(\\dot x^2+\\dot y^2)+mgy+\\lambda(x^2+y^2-L^2)$。<br>对 $\\lambda$：$x^2+y^2=L^2$（约束）。<br>对 $x$：$m\\ddot x=2\\lambda x$。对 $y$：$m\\ddot y=mg+2\\lambda y$。<br>用极坐标 $x=L\\sin\\theta$，$y=-L\\cos\\theta$，代入得 $\\lambda=\\frac{m}{2L}(g\\cos\\theta-L\\dot\\theta^2)$。<br>张力 $T=-2\\lambda L=m(L\\dot\\theta^2-g\\cos\\theta)=mg\\cos\\theta+mL\\dot\\theta^2$（向心分量 + 切向重力分量），与牛顿法分析一致。"))
    + app(p("拉格朗日乘子法的优点：<br>(1) 不必显式消去约束，可用于任意约束（包括非完整约束）；<br>(2) 可同时求运动和约束力；<br>(3) 在电磁场、流体力学、相对论中均有应用（如规范场的乘子法）。"))
)},
],
},

# ---- 1.2 达朗贝尔方程与拉格朗日方程 ----
{
"name": "1.2 达朗贝尔方程与拉格朗日方程",
"color": "#0d9488",
"desc": "从牛顿力学到拉格朗日力学的核心推导",
"items": [
{"id":"tm-c1s2-1","name":"达朗贝尔方程","tags":["thm","der","note"],"brief":"消去约束力后的动力学方程。",
 "body": wrap(
    thm("达朗贝尔方程", p("对理想约束体系，由牛顿第二定律 $m_i\\ddot{\\vec r}_i=\\vec F_i+\\vec F_{Ni}$，将 $\\vec F_{Ni}$ 移到左边")+
    fml("\\vec F_i + \\vec F_{Ni} - m_i\\ddot{\\vec r}_i = 0",
        "考虑虚位移 $\\delta\\vec r_i$ 并对所有质点求和：$\\sum_i(\\vec F_i+\\vec F_{Ni}-m_i\\ddot{\\vec r}_i)\\cdot\\delta\\vec r_i=0$。"))
    + der(p("利用理想约束条件 $\\sum_i\\vec F_{Ni}\\cdot\\delta\\vec r_i=0$，约束力项消失，得达朗贝尔方程：")+
    fml("\\sum_{i=1}^{n}\\left(\\vec F_i - m_i\\ddot{\\vec r}_i\\right)\\cdot\\delta\\vec r_i = 0",
        "若约束为理想完整约束，独立虚位移数目为 $3n-k=s$，故上式含 $s$ 个独立标量方程。"))
    + note(p("达朗贝尔方程实现了从含约束力的牛顿方程到不含约束力方程的转化。$-m_i\\ddot{\\vec r}_i$ 可视为\"惯性力\"，达朗贝尔原理将动力学问题转化为静力学平衡问题。"))
)},
{"id":"tm-c1s2-2","name":"经典拉格朗日关系","tags":["thm","der"],"brief":"广义坐标与速度的偏导互换关系。",
 "body": wrap(
    thm("经典拉格朗日关系", p("设坐标变换为 $\\vec r_i=\\vec r_i(q_1,\\dots,q_s,t)$。将广义坐标 $q_\\alpha$ 与广义速度 $\\dot q_\\alpha$ 视为独立变量，则有两个基本关系")+
    fml("\\frac{\\partial\\dot{\\vec r}_i}{\\partial\\dot q_\\alpha} = \\frac{\\partial\\vec r_i}{\\partial q_\\alpha},\\qquad \\frac{d}{dt}\\frac{\\partial\\vec r_i}{\\partial q_\\alpha} = \\frac{\\partial\\dot{\\vec r}_i}{\\partial q_\\alpha}"))
    + der(p("由链式法则，速度为")+
    fml("\\dot{\\vec r}_i = \\sum_{\\alpha=1}^{s}\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\dot q_\\alpha + \\frac{\\partial\\vec r_i}{\\partial t}",
        "对 $\\dot q_\\alpha$ 求偏导，右边只有第一项含 $\\dot q_\\alpha$，故 $\\frac{\\partial\\dot{\\vec r}_i}{\\partial\\dot q_\\alpha}=\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}$。<br>对 $q_\\alpha$ 求偏导：$\\frac{\\partial\\dot{\\vec r}_i}{\\partial q_\\alpha}=\\sum_\\beta\\frac{\\partial^2\\vec r_i}{\\partial q_\\alpha\\partial q_\\beta}\\dot q_\\beta+\\frac{\\partial^2\\vec r_i}{\\partial q_\\alpha\\partial t}$。<br>另一方面，$\\frac{d}{dt}\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}=\\sum_\\beta\\frac{\\partial}{\\partial q_\\beta}\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\dot q_\\beta+\\frac{\\partial}{\\partial t}\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}$。<br>由于混合偏导可交换（$\\frac{\\partial^2\\vec r_i}{\\partial q_\\alpha\\partial q_\\beta}=\\frac{\\partial^2\\vec r_i}{\\partial q_\\beta\\partial q_\\alpha}$），两式相等。"))
)},
{"id":"tm-c1s2-3","name":"广义力","tags":["def","thm","der"],"brief":"主动力在广义坐标方向的投影，从达朗贝尔原理导出。",
 "body": wrap(
    defn("广义力", p("对应广义坐标 $q_\\alpha$ 的广义力定义为主动力在 $q_\\alpha$ 方向的投影：")+
    fml("Q_\\alpha = \\sum_{i=1}^{n} \\vec F_i \\cdot \\frac{\\partial\\vec r_i}{\\partial q_\\alpha}"))
    + der(p("<strong>推导（从达朗贝尔原理出发）：</strong>达朗贝尔原理为 $\\sum_i(\\vec F_i-m_i\\ddot{\\vec r}_i)\\cdot\\delta\\vec r_i=0$。代入虚位移 $\\delta\\vec r_i=\\sum_\\alpha\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\delta q_\\alpha$，交换求和顺序：")+
    fml("\\sum_\\alpha\\left[\\sum_i(\\vec F_i - m_i\\ddot{\\vec r}_i)\\cdot\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\right]\\delta q_\\alpha = 0",
        "由于 $\\delta q_\\alpha$ 独立任意，故各系数分别为零：$\\sum_i\\vec F_i\\cdot\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}-\\sum_i m_i\\ddot{\\vec r}_i\\cdot\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}=0$。第一项即广义力 $Q_\\alpha=\\sum_i\\vec F_i\\cdot\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}$。"))
    + thm("保守力的广义力", p("若所有主动力均为保守力，$\\vec F_i=-\\nabla_i V$，则")+
    fml("Q_\\alpha = -\\sum_i \\nabla_i V \\cdot \\frac{\\partial\\vec r_i}{\\partial q_\\alpha} = -\\frac{\\partial V}{\\partial q_\\alpha}",
        "这里利用了链式法则 $\\frac{\\partial V}{\\partial q_\\alpha}=\\sum_i\\nabla_i V\\cdot\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}$。"))
)},
{"id":"tm-c1s2-4","name":"欧拉-拉格朗日方程","tags":["def","thm","der","exa","app"],"brief":"理想完整保守体系的运动方程。",
 "body": wrap(
    defn("拉格朗日函数", p("拉格朗日函数定义为动能减势能：")+
    fml("L = T - V"))
    + thm("欧拉-拉格朗日方程", p("对于理想、完整约束且主动力均为保守力的体系，运动方程为")+
    fml("\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha} - \\frac{\\partial L}{\\partial q_\\alpha} = 0,\\qquad 1\\le\\alpha\\le s",
        "其中 $s=3n-k$ 为自由度。这是 $s$ 个二阶常微分方程。"))
    + der(p("<strong>推导步骤：</strong><br>(1) 由达朗贝尔方程 $\\sum_i(\\vec F_i-m_i\\ddot{\\vec r}_i)\\cdot\\delta\\vec r_i=0$。<br>(2) 代入 $\\delta\\vec r_i=\\sum_\\alpha\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\delta q_\\alpha$，交换求和顺序得 $\\sum_\\alpha\\left[\\sum_i(\\vec F_i-m_i\\ddot{\\vec r}_i)\\cdot\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\right]\\delta q_\\alpha=0$。<br>(3) 第一项 $\\sum_i\\vec F_i\\cdot\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}=Q_\\alpha$。<br>(4) 第二项用分部积分：$\\sum_i m_i\\ddot{\\vec r}_i\\cdot\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}=\\frac{d}{dt}\\sum_i m_i\\dot{\\vec r}_i\\cdot\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}-\\sum_i m_i\\dot{\\vec r}_i\\cdot\\frac{d}{dt}\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}$。<br>(5) 利用经典拉格朗日关系，$\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}=\\frac{\\partial\\dot{\\vec r}_i}{\\partial\\dot q_\\alpha}$，$\\frac{d}{dt}\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}=\\frac{\\partial\\dot{\\vec r}_i}{\\partial q_\\alpha}$。<br>(6) 故第二项 $=\\frac{d}{dt}\\frac{\\partial T}{\\partial\\dot q_\\alpha}-\\frac{\\partial T}{\\partial q_\\alpha}$，其中 $T=\\frac{1}{2}\\sum_i m_i\\dot{\\vec r}_i^2$。<br>(7) 得到一般形式的拉格朗日方程：$\\frac{d}{dt}\\frac{\\partial T}{\\partial\\dot q_\\alpha}-\\frac{\\partial T}{\\partial q_\\alpha}=Q_\\alpha$。<br>(8) 对保守力 $Q_\\alpha=-\\frac{\\partial V}{\\partial q_\\alpha}$，且 $V$ 不含 $\\dot q_\\alpha$，代入 $L=T-V$ 即得欧拉-拉格朗日方程。"))
    + exa(p("<strong>质点+悬挂重物体系：</strong>取 $R,\\varphi$ 为广义坐标，动能 $T=\\frac{1}{2}(m+m')\\dot R^2+\\frac{1}{2}mR^2\\dot\\varphi^2$，势能 $V=-m'g(R-l)$，故 $L=\\frac{1}{2}(m+m')\\dot R^2+\\frac{1}{2}mR^2\\dot\\varphi^2-m'g(R-l)$。代入拉格朗日方程：<br>对 $R$：$\\frac{d}{dt}[(m+m')\\dot R]-mR\\dot\\varphi^2+m'g=0$ $\\Rightarrow$ $(m+m')\\ddot R-mR\\dot\\varphi^2+m'g=0$。<br>对 $\\varphi$：$\\frac{d}{dt}(mR^2\\dot\\varphi)=0$ $\\Rightarrow$ 角动量守恒。"))
    + app(p("拉格朗日方程无需分析约束力，只需写出 $T$ 和 $V$ 即可，极大简化了多自由度系统的求解。"))
)},
{"id":"tm-c1s2-5","name":"拉格朗日函数的不唯一性","tags":["thm","der"],"brief":"全导数项不改变运动方程。",
 "body": wrap(
    thm("规范不变性", p("设 $L'=L+\\frac{df}{dt}$，其中 $f=f(q_1,\\dots,q_s,t)$ 为任意可微函数。若 $q_\\alpha(t)$ 是 $L$ 对应的欧拉-拉格朗日方程的解，则它也是 $L'$ 对应的方程的解。"))
    + der(p("计算全导数 $\\frac{df}{dt}=\\sum_\\alpha\\frac{\\partial f}{\\partial q_\\alpha}\\dot q_\\alpha+\\frac{\\partial f}{\\partial t}$。<br>对 $\\dot q_\\alpha$ 求偏导：$\\frac{\\partial}{\\partial\\dot q_\\alpha}\\frac{df}{dt}=\\frac{\\partial f}{\\partial q_\\alpha}$（因为 $\\frac{\\partial f}{\\partial q_\\alpha}$ 和 $\\frac{\\partial f}{\\partial t}$ 都不含 $\\dot q_\\alpha$）。<br>计算：$\\frac{d}{dt}\\frac{\\partial}{\\partial\\dot q_\\alpha}\\frac{df}{dt}-\\frac{\\partial}{\\partial q_\\alpha}\\frac{df}{dt}=\\frac{d}{dt}\\frac{\\partial f}{\\partial q_\\alpha}-\\left(\\sum_\\beta\\frac{\\partial^2 f}{\\partial q_\\alpha\\partial q_\\beta}\\dot q_\\beta+\\frac{\\partial^2 f}{\\partial q_\\alpha\\partial t}\\right)$。<br>而 $\\frac{d}{dt}\\frac{\\partial f}{\\partial q_\\alpha}=\\sum_\\beta\\frac{\\partial^2 f}{\\partial q_\\beta\\partial q_\\alpha}\\dot q_\\beta+\\frac{\\partial^2 f}{\\partial t\\partial q_\\alpha}$。<br>由于混合偏导可交换，两式相等，故 $\\frac{d}{dt}\\frac{\\partial}{\\partial\\dot q_\\alpha}\\frac{df}{dt}-\\frac{\\partial}{\\partial q_\\alpha}\\frac{df}{dt}=0$。因此 $L'$ 与 $L$ 给出相同的运动方程。"))
)},
{"id":"tm-c1s2-6","name":"循环坐标与守恒量","tags":["def","thm","der","app"],"brief":"拉格朗日函数中不显含的坐标对应守恒量。",
 "body": wrap(
    defn("循环坐标", p("若拉格朗日函数 $L$ 不显含某个广义坐标 $q_\\alpha$（即 $\\frac{\\partial L}{\\partial q_\\alpha}=0$），则称 $q_\\alpha$ 为循环坐标（cyclic coordinate）或可遗坐标。"))
    + thm("守恒定理", p("循环坐标对应的广义动量守恒：")+
    fml("p_\\alpha = \\frac{\\partial L}{\\partial\\dot q_\\alpha} = \\text{常数}",
        "由拉格朗日方程 $\\dot p_\\alpha=\\frac{\\partial L}{\\partial q_\\alpha}=0$，故 $p_\\alpha$ 不随时间变化。"))
    + der(p("<strong>推导：</strong>由欧拉-拉格朗日方程 $\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha}-\\frac{\\partial L}{\\partial q_\\alpha}=0$。若 $q_\\alpha$ 为循环坐标，则 $\\frac{\\partial L}{\\partial q_\\alpha}=0$，代入方程得 $\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha}=0$，即 $\\frac{d}{dt}p_\\alpha=0$，故 $p_\\alpha$ 为常数。$\\blacksquare$"))
    + der(p("<strong>能量守恒的推导：</strong>若 $L$ 不显含时间（$\\frac{\\partial L}{\\partial t}=0$），计算 $\\frac{dL}{dt}$：")+
    fml("\\frac{dL}{dt} = \\sum_\\alpha\\frac{\\partial L}{\\partial q_\\alpha}\\dot q_\\alpha + \\sum_\\alpha\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\ddot q_\\alpha + \\frac{\\partial L}{\\partial t}",
        "由欧拉-拉格朗日方程 $\\frac{\\partial L}{\\partial q_\\alpha}=\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha}=\\dot p_\\alpha$，代入得 $\\frac{dL}{dt}=\\sum_\\alpha\\dot p_\\alpha\\dot q_\\alpha+\\sum_\\alpha p_\\alpha\\ddot q_\\alpha=\\frac{d}{dt}\\sum_\\alpha p_\\alpha\\dot q_\\alpha$。故 $\\frac{d}{dt}(L-\\sum p_\\alpha\\dot q_\\alpha)=0$，即 $H=\\sum p_\\alpha\\dot q_\\alpha-L$ 守恒。"))
    + app(p("<strong>中心力场：</strong>$\\varphi$ 为循环坐标 $\\Rightarrow$ 角动量 $p_\\varphi=$ 常数。<br><strong>空间平移不变性：</strong>$x$ 为循环坐标 $\\Rightarrow$ 动量守恒。<br><strong>时间平移不变性：</strong>$L$ 不显含 $t$ $\\Rightarrow$ 能量守恒（见诺特定理）。"))
)},
],
},

# ---- 1.3 变分法与最小作用量原理 ----
{
"name": "1.3 变分法与最小作用量原理",
"color": "#7c3aed",
"desc": "泛函、变分、欧拉-拉格朗日方程、最小作用量原理",
"items": [
{"id":"tm-c1s3-1","name":"泛函的定义","tags":["def","exa"],"brief":"以函数为自变量的映射。",
 "body": wrap(
    defn("泛函", p("设 $\\mathcal F$ 为某函数空间，泛函是从 $\\mathcal F$ 到 $\\mathbb R$ 的映射 $J: \\mathcal F\\to\\mathbb R$，即对每个函数 $x(t)$ 赋一个实数 $J[x(t)]$。泛函可视为多元函数在无穷维空间的推广。"))
    + exa(p("<strong>最速落径问题：</strong>求连接两点的曲线使质点沿其下滑时间最短，$T[y(x)]=\\int_{x_1}^{x_2}\\sqrt{\\frac{1+y'^2}{2gy}}\\,dx$。<br><strong>作用量泛函：</strong>$S[q(t)]=\\int_{t_1}^{t_2}L(q,\\dot q,t)\\,dt$，这是力学中最重要的泛函。<br><strong>弧长泛函：</strong>$L[y]=\\int_{x_1}^{x_2}\\sqrt{1+y'^2}\\,dx$，极值为直线。"))
)},
{"id":"tm-c1s3-2","name":"泛函的变分","tags":["def","thm","der"],"brief":"泛函增量的线性主部，含推导。",
 "body": wrap(
    defn("变分", p("自变函数的增量 $\\delta x(t)=\\tilde x(t)-x(t)$，在端点处 $\\delta x(t_1)=\\delta x(t_2)=0$。泛函的增量 $\\Delta J=J[x+\\delta x]-J[x]$ 可分解为线性主部与高阶小量")+
    fml("\\Delta J = \\delta J + o(\\|\\delta x\\|)",
        "其中线性主部 $\\delta J$ 称为泛函的变分。$\\|\\delta x\\|$ 为函数空间中的范数。"))
    + thm("变分的计算公式", p("若 $J[x]=\\int_{t_1}^{t_2}F(x,\\dot x,t)\\,dt$，则变分为")+
    fml("\\delta J = \\int_{t_1}^{t_2}\\left(\\frac{\\partial F}{\\partial x}\\delta x + \\frac{\\partial F}{\\partial\\dot x}\\delta\\dot x\\right)dt",
        "变分与微分运算可交换：$\\delta\\dot x=\\frac{d}{dt}\\delta x$。"))
    + der(p("<strong>推导：</strong>将 $x+\\delta x$ 和 $\\dot x+\\delta\\dot x$ 代入泛函，对 $F$ 在 $(x,\\dot x,t)$ 处泰勒展开：")+
    fml("F(x+\\delta x,\\dot x+\\delta\\dot x,t) = F(x,\\dot x,t) + \\frac{\\partial F}{\\partial x}\\delta x + \\frac{\\partial F}{\\partial\\dot x}\\delta\\dot x + o(\\|\\delta x\\|)",
        "积分后取线性主部（略去高阶项），即得 $\\delta J=\\int_{t_1}^{t_2}\\left(\\frac{\\partial F}{\\partial x}\\delta x+\\frac{\\partial F}{\\partial\\dot x}\\delta\\dot x\\right)dt$。$\\blacksquare$"))
)},
{"id":"tm-c1s3-3","name":"欧拉-拉格朗日方程（变分法）","tags":["thm","der"],"brief":"泛函取极值的必要条件。",
 "body": wrap(
    thm("欧拉-拉格朗日方程", p("泛函 $J[x]=\\int_{t_1}^{t_2}F(x,\\dot x,t)\\,dt$ 在端点固定条件下取极值的必要条件（$\\delta J=0$）为")+
    fml("\\frac{\\partial F}{\\partial x} - \\frac{d}{dt}\\frac{\\partial F}{\\partial\\dot x} = 0"))
    + der(p("<strong>完整推导：</strong><br>变分为 $\\delta J=\\int_{t_1}^{t_2}\\left(\\frac{\\partial F}{\\partial x}\\delta x+\\frac{\\partial F}{\\partial\\dot x}\\delta\\dot x\\right)dt$。<br>对第二项分部积分：$\\int_{t_1}^{t_2}\\frac{\\partial F}{\\partial\\dot x}\\frac{d}{dt}\\delta x\\,dt = \\left[\\frac{\\partial F}{\\partial\\dot x}\\delta x\\right]_{t_1}^{t_2} - \\int_{t_1}^{t_2}\\frac{d}{dt}\\frac{\\partial F}{\\partial\\dot x}\\delta x\\,dt$。<br>端点固定 $\\delta x(t_1)=\\delta x(t_2)=0$，故边界项为零。代入得")+
    fml("\\delta J = \\int_{t_1}^{t_2}\\left(\\frac{\\partial F}{\\partial x} - \\frac{d}{dt}\\frac{\\partial F}{\\partial\\dot x}\\right)\\delta x\\,dt = 0")
    + p("由于 $\\delta x(t)$ 在 $(t_1,t_2)$ 内任意，由变分法基本引理，被积函数必须恒为零，即得欧拉-拉格朗日方程。"))
)},
{"id":"tm-c1s3-4","name":"最小作用量原理","tags":["def","thm","der","app"],"brief":"真实运动使作用量取极值。",
 "body": wrap(
    defn("哈密顿作用量", p("对于拉格朗日函数 $L(q,\\dot q,t)$，定义作用量泛函")+
    fml("S[q(t)] = \\int_{t_1}^{t_2} L(q_\\alpha,\\dot q_\\alpha,t)\\,dt",
        "其中 $q_\\alpha(t)$ 为真实运动的广义坐标。"))
    + thm("哈密顿最小作用量原理", p("对于完整理想约束体系，在 $t_1$ 到 $t_2$ 时刻从位形 $q_\\alpha^{(1)}$ 到 $q_\\alpha^{(2)}$ 的所有可能运动中，真实运动使作用量取极值（变分为零）：")+
    fml("\\delta S = 0",
        "边界条件：$\\delta q_\\alpha(t_1)=\\delta q_\\alpha(t_2)=0$。"))
    + der(p("<strong>完整推导（变分 $\\delta S=0$ $\\Leftrightarrow$ 拉格朗日方程）：</strong><br>作用量变分为")+
    fml("\\delta S = \\int_{t_1}^{t_2}\\left(\\frac{\\partial L}{\\partial q_\\alpha}\\delta q_\\alpha + \\frac{\\partial L}{\\partial\\dot q_\\alpha}\\delta\\dot q_\\alpha\\right)dt",
        "对第二项分部积分：$\\int_{t_1}^{t_2}\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\frac{d}{dt}\\delta q_\\alpha\\,dt = \\left[\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\delta q_\\alpha\\right]_{t_1}^{t_2} - \\int_{t_1}^{t_2}\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\delta q_\\alpha\\,dt$。<br>由边界条件 $\\delta q(t_1)=\\delta q(t_2)=0$，边界项为零。")+
    fml("\\delta S = \\int_{t_1}^{t_2}\\left(\\frac{\\partial L}{\\partial q_\\alpha} - \\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\right)\\delta q_\\alpha\\,dt = 0",
        "由于 $\\delta q_\\alpha(t)$ 在 $(t_1,t_2)$ 内任意，由变分法基本引理，被积函数恒为零：")+
    fml("\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha} - \\frac{\\partial L}{\\partial q_\\alpha} = 0",
        "即拉格朗日方程。反之，若 $q(t)$ 满足拉格朗日方程，则 $\\delta S=0$。故最小作用量原理与拉格朗日方程等价。"))
    + thm("拉格朗日函数的不唯一性", p("若 $L'=L+\\frac{dF(q,t)}{dt}$，则 $L'$ 与 $L$ 导出相同的拉格朗日方程。因为")+
    fml("\\delta\\int_{t_1}^{t_2}\\frac{dF}{dt}\\,dt = \\delta F(q(t_2),t_2) - \\delta F(q(t_1),t_1) = 0",
        "由边界条件 $\\delta q(t_1)=\\delta q(t_2)=0$，故附加全导数项不影响变分。"))
    + app(p("最小作用量原理是力学的第一性原理。它表明真实运动是所有可能运动中使作用量取极值的那个。这个原理可以推广到场论（电磁场、引力场、量子场论），是现代物理学的基础。"))
)},
{"id":"tm-c1s3-5","name":"最速落径问题","tags":["exa","der"],"brief":"变分法的经典应用。",
 "body": wrap(
    exa(p("求从 $(0,0)$ 到 $(x_2,y_2)$ 的曲线，使质点从静止出发在重力作用下沿曲线下滑时间最短。这是历史上第一个变分法问题（由约翰·伯努利于 1696 年提出）。"))
    + der(p("由能量守恒 $\\frac{1}{2}mv^2=mgy$，得 $v=\\sqrt{2gy}$。弧长元 $ds=\\sqrt{1+y'^2}\\,dx$，故时间泛函为")+
    fml("T = \\int_{0}^{x_2} \\frac{ds}{v} = \\int_{0}^{x_2}\\sqrt{\\frac{1+y'^2}{2gy}}\\,dx",
        "被积函数 $F(y,y')=\\sqrt{\\frac{1+y'^2}{2gy}}$ 不显含 $x$，故可利用首次积分 $F-y'\\frac{\\partial F}{\\partial y'}=$ 常数。计算得 $\\frac{1}{\\sqrt{2gy(1+y'^2)}}=$ 常数，即 $y(1+y'^2)=2R$（常数）。<br>令 $y'=\\cot\\frac{\\theta}{2}$，则 $1+y'^2=\\csc^2\\frac{\\theta}{2}$，$y=2R\\sin^2\\frac{\\theta}{2}=R(1-\\cos\\theta)$。<br>$dx=\\frac{dy}{y'}=\\frac{R\\sin\\theta\\,d\\theta}{\\cot(\\theta/2)}=2R\\sin^2\\frac{\\theta}{2}\\,d\\theta=R(1-\\cos\\theta)\\,d\\theta$，积分得 $x=R(\\theta-\\sin\\theta)$。<br>故解为参数方程 $x=R(\\theta-\\sin\\theta)$，$y=R(1-\\cos\\theta)$，即<strong>旋轮线（摆线）</strong>。"))
)},
],
},

# ---- 1.4 诺特定理（保留在第一章） ----
{
"name": "1.4 诺特定理",
"color": "#c2410c",
"desc": "对称性与守恒量、动量/角动量/能量定理、诺特定理",
"items": [
{"id":"tm-c1s4-1","name":"对称性与守恒量","tags":["def","thm","der"],"brief":"诺特定理的前置概念，含三大守恒定律推导。",
 "body": wrap(
    defn("对称性变换", p("若变换 $q\\to q'$ 使拉格朗日函数不变（或差一全导数项），则称该变换为系统的对称性变换。对称性意味着系统在某种操作下具有不变性。"))
    + thm("三大守恒定律", p("<strong>动量守恒：</strong>空间平移不变性 $\\Rightarrow$ 总动量守恒。<br><strong>角动量守恒：</strong>空间旋转不变性 $\\Rightarrow$ 总角动量守恒。<br><strong>能量守恒：</strong>时间平移不变性 $\\Rightarrow$ 能量守恒。"))
    + der(p("<strong>动量守恒的推导：</strong>设 $L$ 在空间平移 $\\vec r_i\\to\\vec r_i+\\delta\\vec\\varepsilon$ 下不变。由 $\\frac{\\partial L}{\\partial\\vec r_i}=0$，欧拉-拉格朗日方程给出 $\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot{\\vec r}_i}=0$，即 $\\vec p_i$ 守恒，总动量 $\\vec P=\\sum_i\\vec p_i$ 守恒。"))
    + der(p("<strong>角动量守恒的推导：</strong>设 $L$ 在绕 $\\hat n$ 轴旋转 $\\delta\\theta$ 下不变。$\\delta\\vec r_i=\\delta\\theta\\,\\hat n\\times\\vec r_i$，由 $\\frac{\\partial L}{\\partial\\vec r_i}\\cdot\\delta\\vec r_i=0$ 得 $\\sum_i\\vec p_i\\cdot(\\hat n\\times\\vec r_i)=0$，即 $\\hat n\\cdot\\sum_i\\vec r_i\\times\\vec p_i=\\hat n\\cdot\\vec L=0$ 的导数，故 $\\vec L$ 守恒。"))
    + der(p("<strong>能量守恒的推导：</strong>设 $L$ 不显含时间。计算 $\\frac{d}{dt}\\left(\\sum_\\alpha p_\\alpha\\dot q_\\alpha - L\\right)$：由 $\\frac{dL}{dt}=\\sum\\dot p_\\alpha\\dot q_\\alpha+\\sum p_\\alpha\\ddot q_\\alpha=\\frac{d}{dt}\\sum p_\\alpha\\dot q_\\alpha$（详见循环坐标条目），故 $\\frac{dH}{dt}=0$，能量 $H$ 守恒。"))
)},
{"id":"tm-c1s4-2","name":"诺特定理","tags":["def","thm","der","app"],"brief":"连续对称性对应守恒量。",
 "body": wrap(
    defn("对称性变换", p("考虑含连续参数 $\\varepsilon$ 的无穷小变换 $t\\to t'=t+\\varepsilon\\,\\Delta t(q,t)$，$q_\\alpha\\to q_\\alpha'=q_\\alpha+\\varepsilon\\,\\Delta q_\\alpha(q,t)$。若此变换使作用量不变或仅差一边界项，即")+
    fml("S[q'(t')] = S[q(t)] + \\varepsilon\\left[F(q(t_f),t_f)-F(q(t_i),t_i)\\right]",
        "则称该变换为系统的<strong>对称性变换</strong>，$F(q,t)$ 为相应的边界项函数。"))
    + thm("诺特定理", p("系统的每一个连续对称性变换都对应一个守恒量：")+
    fml("Q = \\sum_\\alpha \\frac{\\partial L}{\\partial\\dot q_\\alpha}\\left(\\Delta q_\\alpha - \\dot q_\\alpha\\,\\Delta t\\right) + L\\,\\Delta t - F = \\text{常数}",
        "其中 $\\bar{\\Delta}q_\\alpha \\equiv \\Delta q_\\alpha - \\dot q_\\alpha\\,\\Delta t$ 称为<strong>演化变分</strong>，即在变换后的新时间处坐标的实质性变化。"))
    + der(p("<strong>完整推导：</strong><br><strong>第一步：</strong>定义演化变分 $\\bar{\\Delta}q_\\alpha=\\Delta q_\\alpha-\\dot q_\\alpha\\Delta t$。它表示在固定时刻 $t'$ 处，新旧坐标之差中扣除时间变换带来的漂移后的实质变化。"))
    + der(p("<strong>第二步：</strong>在无穷小变换下，作用量变为")+
    fml("S[q'(t')] = \\int_{t_i}^{t_f}\\left[L + \\varepsilon\\left(\\sum_\\alpha\\frac{\\partial L}{\\partial q_\\alpha}\\bar{\\Delta}q_\\alpha + \\sum_\\alpha\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\frac{d}{dt}\\bar{\\Delta}q_\\alpha + \\frac{d}{dt}(\\Delta t\\,L)\\right)\\right]dt",
        "其中第一项 $\\sum\\frac{\\partial L}{\\partial q_\\alpha}\\bar{\\Delta}q_\\alpha+\\sum\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\dot{\\bar{\\Delta}}q_\\alpha$ 为拉氏量在固定 $t$ 处的变化，第三项 $\\frac{d}{dt}(\\Delta t\\,L)$ 来自积分测度 $dt'=dt(1+\\varepsilon\\dot{\\Delta}t)$ 的变化。"))
    + der(p("<strong>第三步：</strong>对真实运动，利用欧拉-拉格朗日方程 $\\frac{\\partial L}{\\partial q_\\alpha}=\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_\\alpha}$，将前两项合并为全导数：")+
    fml("\\sum_\\alpha\\frac{\\partial L}{\\partial q_\\alpha}\\bar{\\Delta}q_\\alpha + \\sum_\\alpha\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\dot{\\bar{\\Delta}}q_\\alpha = \\frac{d}{dt}\\sum_\\alpha\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\bar{\\Delta}q_\\alpha",
        "故 $\\delta S=\\varepsilon\\int\\frac{d}{dt}\\left[\\sum_\\alpha\\frac{\\partial L}{\\partial\\dot q_\\alpha}\\bar{\\Delta}q_\\alpha+\\Delta t\\,L\\right]dt=\\varepsilon\\left[\\sum_\\alpha p_\\alpha\\bar{\\Delta}q_\\alpha+\\Delta t\\,L\\right]_{t_i}^{t_f}$。"))
    + der(p("<strong>第四步：</strong>由对称性假设 $\\delta S=\\varepsilon[F(t_f)-F(t_i)]$，比较得")+
    fml("\\frac{d}{dt}\\left[\\sum_\\alpha p_\\alpha\\bar{\\Delta}q_\\alpha+\\Delta t\\,L-F\\right]=0",
        "即 $Q=\\sum_\\alpha p_\\alpha(\\Delta q_\\alpha-\\dot q_\\alpha\\Delta t)+\\Delta t\\,L-F$ 为守恒量。$\\blacksquare$"))
    + app(p("<strong>空间平移 $\\Delta\\vec r=\\vec\\varepsilon,\\Delta t=0$：</strong>$Q=\\sum\\vec p\\cdot\\vec\\varepsilon=\\vec\\varepsilon\\cdot\\vec P$，故 $\\vec P$ 守恒。<br><strong>空间转动（绕 $\\hat n$ 轴）$\\Delta\\vec r=\\varepsilon\\hat n\\times\\vec r,\\Delta t=0$：</strong>$Q=\\sum\\vec p\\cdot(\\hat n\\times\\vec r)=\\hat n\\cdot\\sum\\vec r\\times\\vec p=\\hat n\\cdot\\vec L$，故 $\\vec L$ 守恒。<br><strong>时间平移 $\\Delta t=1,\\Delta q=0$：</strong>$Q=L-\\sum p_\\alpha\\dot q_\\alpha=-H$，故 $H$（能量）守恒。<br>这三大守恒定律分别对应时空的均匀性和各向同性。"))
)},
],
},
]

print(f"Ch1: {sum(len(s['items']) for s in ch1_sections)} items")

# =====================================================
#  CHAPTER 2: 哈密顿力学
# =====================================================
ch2_sections = [

# ---- 2.1 勒让德变换与哈密顿量 ----
{
"name": "2.1 勒让德变换与哈密顿量",
"color": "#2563eb",
"desc": "勒让德变换、哈密顿量、正则变量",
"items": [
{"id":"tm-c2s1-1","name":"勒让德变换","tags":["def","thm","der"],"brief":"自变量与函数形式同时变换。",
 "body": wrap(
    defn("勒让德变换", p("设 $y=f(x)$ 为下凸函数（$f''>0$），令 $p=\\frac{df}{dx}$。由凸性可反解 $x=x(p)$，定义勒让德变换")+
    fml("g(p) = x\\,p - f(x)\\big|_{x=x(p)}",
        "函数 $f(x)$ 到 $g(p)$ 的变换将自变量从 $x$ 变为 $p$，函数形式从 $f$ 变为 $g$。"))
    + thm("全微分与对合性", p("$g(p)$ 的全微分为 $dg = x\\,dp$。做两次勒让德变换回到原函数：$g^*(x)=f(x)$。"))
    + der(p("$dg=x\\,dp+p\\,dx-df=x\\,dp+p\\,dx-p\\,dx=x\\,dp$。<br>对 $g(p)$ 再做勒让德变换：令 $z=\\frac{dg}{dp}=x$，则 $h(z)=z\\cdot p-g(p)\\big|_{p=p(z)}=xp-(xp-f(x))=f(x)=f(z)$。故两次变换还原。"))
    + thm("几何意义", p("$y=f(x)$ 的图像为曲线，$y=px$ 为过原点斜率为 $p$ 的直线。斜率为 $p$ 且与 $f(x)$ 相切的切线在纵轴上的截距为 $px(p)-f(x(p))=g(p)$。因此<strong>勒让德变换的几何意义是切线在纵轴上的截距</strong>。"))
)},
{"id":"tm-c2s1-2","name":"正则变量与哈密顿量","tags":["def","thm","der"],"brief":"从拉格朗日函数到哈密顿量。",
 "body": wrap(
    defn("广义动量", p("对每个广义速度 $\\dot q_\\alpha$，定义相应的广义动量（正则动量）")+
    fml("p_\\alpha = \\frac{\\partial L}{\\partial\\dot q_\\alpha},\\qquad 1\\le\\alpha\\le s"))
    + defn("哈密顿量", p("对每个广义速度做勒让德变换，引入哈密顿量")+
    fml("H(p_\\alpha,q_\\alpha,t) = \\sum_{\\alpha=1}^{s} p_\\alpha\\dot q_\\alpha - L(q_\\alpha,\\dot q_\\alpha,t)",
        "其中 $\\dot q_\\alpha$ 通过反解 $p_\\alpha=\\partial L/\\partial\\dot q_\\alpha$ 表示为 $q,p,t$ 的函数。"))
    + thm("哈密顿量的偏导数", p("对 $H$ 求全微分：$dH=\\sum(\\dot q_\\alpha\\,dp_\\alpha+p_\\alpha\\,d\\dot q_\\alpha)-\\sum(\\frac{\\partial L}{\\partial q_\\alpha}dq_\\alpha+\\frac{\\partial L}{\\partial\\dot q_\\alpha}d\\dot q_\\alpha)-\\frac{\\partial L}{\\partial t}dt$。利用 $p_\\alpha=\\partial L/\\partial\\dot q_\\alpha$ 消去 $d\\dot q_\\alpha$ 项，得")+
    fml("dH = \\sum_\\alpha\\dot q_\\alpha\\,dp_\\alpha - \\sum_\\alpha\\frac{\\partial L}{\\partial q_\\alpha}dq_\\alpha - \\frac{\\partial L}{\\partial t}dt",
        "比较系数得：$\\dot q_\\alpha=\\frac{\\partial H}{\\partial p_\\alpha}$，$\\frac{\\partial H}{\\partial q_\\alpha}=-\\frac{\\partial L}{\\partial q_\\alpha}$，$\\frac{\\partial H}{\\partial t}=-\\frac{\\partial L}{\\partial t}$。"))
)},
{"id":"tm-c2s1-3","name":"哈密顿量的例子","tags":["exa","der","app"],"brief":"电磁场粒子、谐振子、单摆。",
 "body": wrap(
    exa(p("<strong>一维谐振子：</strong>$L=\\frac{1}{2}m\\dot x^2-\\frac{1}{2}m\\omega^2 x^2$，正则动量 $p=m\\dot x$，故")+
    fml("H = p\\dot x - L = \\frac{p^2}{m} - \\left(\\frac{p^2}{2m}-\\frac{1}{2}m\\omega^2 x^2\\right) = \\frac{p^2}{2m} + \\frac{1}{2}m\\omega^2 x^2 = T+V = E"))
    + exa(p("<strong>单摆：</strong>$L=\\frac{1}{2}mR^2\\dot\\theta^2+mgR\\cos\\theta$，$p_\\theta=mR^2\\dot\\theta$，故 $H=\\frac{p_\\theta^2}{2mR^2}-mgR\\cos\\theta$，正则动量 $p_\\theta$ 为角动量。"))
    + app(p("当 $L$ 不显含时间且势能不含速度时，$H=T+V=E$ 即为总能量。但当 $L$ 显含时间或坐标变换显含时间时，$H$ 不一定等于总机械能。"))
)},
{"id":"tm-c2s1-4","name":"哈密顿量与总能量的关系","tags":["thm","der","app","note"],"brief":"$H$ 何时等于总机械能的判据与推导。",
 "body": wrap(
    thm("判据", p("哈密顿量 $H$ 等于总机械能 $E=T+V$ 当且仅当：(1) 拉格朗日函数不显含时间 $\\frac{\\partial L}{\\partial t}=0$；(2) 约束方程不含时间（即坐标变换 $\\vec r_i=\\vec r_i(q)$ 不显含 $t$）。"))
    + der(p("<strong>推导：</strong>由动能定义 $T=\\frac{1}{2}\\sum_i m_i\\dot{\\vec r}_i^2$，对完整稳定约束 $\\vec r_i=\\vec r_i(q_1,\\dots,q_s)$（不含 $t$），速度 $\\dot{\\vec r}_i=\\sum_\\alpha\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\dot q_\\alpha$，故")+
    fml("T = \\frac{1}{2}\\sum_{\\alpha,\\beta}\\left(\\sum_i m_i\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\cdot\\frac{\\partial\\vec r_i}{\\partial q_\\beta}\\right)\\dot q_\\alpha\\dot q_\\beta = \\frac{1}{2}\\sum_{\\alpha\\beta}A_{\\alpha\\beta}(q)\\dot q_\\alpha\\dot q_\\beta",
        "即 $T$ 是广义速度的<strong>二次齐次函数</strong>（仅含 $\\dot q^2$ 项，无常数项和一次项）。由欧拉齐次函数定理："))
    + der(fml("\\sum_\\alpha \\dot q_\\alpha\\frac{\\partial T}{\\partial\\dot q_\\alpha} = 2T",
        "由于 $V$ 不含 $\\dot q$，$\\frac{\\partial L}{\\partial\\dot q_\\alpha}=\\frac{\\partial T}{\\partial\\dot q_\\alpha}$，故")+
    fml("H = \\sum_\\alpha p_\\alpha\\dot q_\\alpha - L = \\sum_\\alpha\\dot q_\\alpha\\frac{\\partial T}{\\partial\\dot q_\\alpha} - (T-V) = 2T - (T-V) = T + V = E",
        "故 $H$ 即为总机械能。<br><strong>反之</strong>，若约束显含时间 $\\vec r_i=\\vec r_i(q,t)$，则 $\\dot{\\vec r}_i=\\sum_\\alpha\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\dot q_\\alpha+\\frac{\\partial\\vec r_i}{\\partial t}$，动能含 $\\dot q$ 的一次项和常数项，不再是齐次函数，$H\\neq T+V$。"))
    + app(p("<strong>电磁场中带电粒子：</strong>$L=\\frac{1}{2}m\\vec v^2-q\\phi+q\\vec A\\cdot\\vec v$，$\\sum p_\\alpha\\dot q_\\alpha=m\\vec v^2+q\\vec A\\cdot\\vec v$，故 $H=m\\vec v^2+q\\vec A\\cdot\\vec v-\\frac{1}{2}m\\vec v^2+q\\phi-q\\vec A\\cdot\\vec v=\\frac{1}{2}m\\vec v^2+q\\phi$。机械能 $E=\\frac{1}{2}m\\vec v^2+q\\phi$，故 $H=E$，但此时势能含速度。<br><strong>转动参考系：</strong>坐标变换含时间，$H\\neq T+V$。"))
    + note(p("$H$ 守恒要求 $\\frac{\\partial L}{\\partial t}=0$；$H=E$（总机械能）要求约束不含时间。两者是<strong>不同的条件</strong>：可出现 $H$ 守恒但 $H\\neq E$（含时约束），或 $H=E$ 但 $H$ 不守恒（$L$ 显含时间）。"))
)},
],
},

# ---- 2.2 哈密顿正则方程 ----
{
"name": "2.2 哈密顿正则方程",
"color": "#0d9488",
"desc": "正则方程、相空间、哈密顿流",
"items": [
{"id":"tm-c2s2-1","name":"哈密顿正则方程","tags":["def","thm","der"],"brief":"哈密顿形式的运动方程。",
 "body": wrap(
    thm("正则方程", p("利用欧拉-拉格朗日方程 $\\dot p_\\alpha=\\frac{\\partial L}{\\partial q_\\alpha}$ 及勒让德变换关系 $\\frac{\\partial H}{\\partial q_\\alpha}=-\\frac{\\partial L}{\\partial q_\\alpha}$，得哈密顿正则方程")+
    fml("\\dot q_\\alpha = \\frac{\\partial H}{\\partial p_\\alpha},\\qquad \\dot p_\\alpha = -\\frac{\\partial H}{\\partial q_\\alpha},\\qquad 1\\le\\alpha\\le s",
        "共 $2s$ 个一阶微分方程，替代拉格朗日力学中的 $s$ 个二阶方程。"))
    + der(p("由广义动量定义 $p_\\alpha=\\frac{\\partial L}{\\partial\\dot q_\\alpha}$ 及欧拉-拉格朗日方程 $\\frac{d}{dt}p_\\alpha=\\frac{\\partial L}{\\partial q_\\alpha}$。<br>再利用勒让德变换的偏导关系 $\\dot q_\\alpha=\\frac{\\partial H}{\\partial p_\\alpha}$ 和 $\\frac{\\partial H}{\\partial q_\\alpha}=-\\frac{\\partial L}{\\partial q_\\alpha}$。<br>因此 $\\dot p_\\alpha=\\frac{\\partial L}{\\partial q_\\alpha}=-\\frac{\\partial H}{\\partial q_\\alpha}$，即得正则方程。"))
)},
{"id":"tm-c2s2-2","name":"相空间","tags":["def","thm","app"],"brief":"正则变量张成的空间。",
 "body": wrap(
    defn("相空间", p("以 $s$ 个广义坐标 $q_\\alpha$ 和 $s$ 个广义动量 $p_\\alpha$ 为坐标的 $2s$ 维空间称为相空间（$\\Gamma$ 空间）。系统的运动状态对应相空间中的一点，运动轨迹为相轨道。"))
    + defn("哈密顿流", p("正则方程在相空间中定义了一个矢量场 $X_H=(\\frac{\\partial H}{\\partial p},-\\frac{\\partial H}{\\partial q})$，称为哈密顿矢量场。其积分曲线即系统的运动轨迹，构成哈密顿流。"))
    + thm("刘维尔定理", p("哈密顿流保持相空间体积元不变：相空间中区域的体积在运动中守恒。等价地，哈密顿矢量场的散度为零：$\\nabla\\cdot X_H=\\sum(\\frac{\\partial^2 H}{\\partial q_\\alpha\\partial p_\\alpha}-\\frac{\\partial^2 H}{\\partial p_\\alpha\\partial q_\\alpha})=0$。"))
    + app(p("相空间方法是统计力学的基础，哈密顿流的保体积性是刘维尔定理的核心，也是微正则系综的理论基础。"))
)},
{"id":"tm-c2s2-3","name":"正则方程的例子","tags":["exa","der"],"brief":"从正则方程求解运动。",
 "body": wrap(
    exa(p("<strong>一维谐振子：</strong>$H=\\frac{p^2}{2m}+\\frac{1}{2}m\\omega^2 x^2$。正则方程为")+
    fml("\\dot x = \\frac{\\partial H}{\\partial p} = \\frac{p}{m},\\qquad \\dot p = -\\frac{\\partial H}{\\partial x} = -m\\omega^2 x",
        "消去 $p$：由第一式 $\\ddot x=\\dot p/m=-\\omega^2 x$，得 $\\ddot x+\\omega^2 x=0$，解为简谐振动。"))
    + der(p("<strong>中心力场：</strong>$H=\\frac{1}{2m}(p_r^2+\\frac{p_\\varphi^2}{r^2})+V(r)$。<br>对 $\\varphi$：$\\dot\\varphi=\\frac{\\partial H}{\\partial p_\\varphi}=\\frac{p_\\varphi}{mr^2}$，$\\dot p_\\varphi=-\\frac{\\partial H}{\\partial\\varphi}=0$ $\\Rightarrow$ $p_\\varphi=l$ 守恒（角动量守恒）。<br>对 $r$：$\\dot r=\\frac{p_r}{m}$，$\\dot p_r=-\\frac{\\partial H}{\\partial r}=\\frac{p_\\varphi^2}{mr^3}-V'(r)$ $\\Rightarrow$ $m\\ddot r=\\frac{l^2}{mr^3}-V'(r)$。"))
)},
],
},

# ---- 2.3 泊松括号 ----
{
"name": "2.3 泊松括号",
"color": "#7c3aed",
"desc": "泊松括号的定义、性质、辛形式、正则量子化",
"items": [
{"id":"tm-c2s3-1","name":"泊松括号的定义","tags":["def","thm"],"brief":"相空间标量场的时间演化。",
 "body": wrap(
    defn("泊松括号", p("设 $f(q,p,t)$ 和 $g(q,p,t)$ 为相空间上的标量场，它们的泊松括号定义为")+
    fml("\\{f,g\\} = \\sum_{\\alpha=1}^{s}\\left(\\frac{\\partial f}{\\partial q_\\alpha}\\frac{\\partial g}{\\partial p_\\alpha} - \\frac{\\partial f}{\\partial p_\\alpha}\\frac{\\partial g}{\\partial q_\\alpha}\\right)"))
    + thm("时间演化", p("任意力学量 $f(q,p,t)$ 沿运动轨迹的时间导数为")+
    fml("\\frac{df}{dt} = \\frac{\\partial f}{\\partial t} + \\{f,H\\}",
        "推导：$\\frac{df}{dt}=\\frac{\\partial f}{\\partial t}+\\sum_\\alpha(\\frac{\\partial f}{\\partial q_\\alpha}\\dot q_\\alpha+\\frac{\\partial f}{\\partial p_\\alpha}\\dot p_\\alpha)=\\frac{\\partial f}{\\partial t}+\\sum_\\alpha(\\frac{\\partial f}{\\partial q_\\alpha}\\frac{\\partial H}{\\partial p_\\alpha}-\\frac{\\partial f}{\\partial p_\\alpha}\\frac{\\partial H}{\\partial q_\\alpha})=\\frac{\\partial f}{\\partial t}+\\{f,H\\}$。<br>特别地，$\\dot q_\\alpha=\\{q_\\alpha,H\\}$，$\\dot p_\\alpha=\\{p_\\alpha,H\\}$。"))
)},
{"id":"tm-c2s3-2","name":"泊松括号的性质","tags":["thm","der"],"brief":"双线性、反对称、莱布尼茨法则、雅可比恒等式及其证明。",
 "body": wrap(
    thm("泊松括号的四条基本性质", p("<strong>1. 反对称性：</strong>$\\{f,g\\}=-\\{g,f\\}$<br><strong>2. 双线性：</strong>$\\{af+bg,h\\}=a\\{f,h\\}+b\\{g,h\\}$<br><strong>3. 莱布尼茨法则：</strong>$\\{fg,h\\}=f\\{g,h\\}+\\{f,h\\}g$<br><strong>4. 雅可比恒等式：</strong>$\\{f,\\{g,h\\}\\}+\\{g,\\{h,f\\}\\}+\\{h,\\{f,g\\}\\}=0$"))
    + thm("基本泊松括号", p("$\\{q_\\alpha,q_\\beta\\}=0$，$\\{p_\\alpha,p_\\beta\\}=0$，$\\{q_\\alpha,p_\\beta\\}=\\delta_{\\alpha\\beta}$。"))
    + der(p("<strong>反对称性的证明（用辛形式）：</strong>由 $\\{g,f\\}=(\\nabla g)^T J(\\nabla f)$，取转置得 $\\{g,f\\}=(\\nabla g)^T J(\\nabla f)=((\\nabla f)^T J^T(\\nabla g))^T$。由于 $J^T=-J$（辛矩阵反对称），故 $\\{g,f\\}=-(\\nabla f)^T J(\\nabla g)=-\\{f,g\\}$。"))
    + der(p("<strong>莱布尼茨法则的证明：</strong>由 $\\{fg,h\\}=(\\nabla(fg))^T J(\\nabla h)$，利用 $\\nabla(fg)=f\\nabla g+g\\nabla f$（乘积的梯度分解），得")+
    fml("\\{fg,h\\} = (f\\nabla g + g\\nabla f)^T J\\nabla h = f(\\nabla g)^T J\\nabla h + g(\\nabla f)^T J\\nabla h = f\\{g,h\\} + g\\{f,h\\}",
        "即 $\\{fg,h\\}=f\\{g,h\\}+g\\{f,h\\}=f\\{g,h\\}+\\{f,h\\}g$（最后一步用反对称性）。"))
    + der(p("<strong>雅可比恒等式的证明（用辛形式 $J$）：</strong>记 $\\xi_a$（$1\\le a\\le 2s$）为统一正则坐标，则 $\\{f,g\\}=(\\nabla f)^T J(\\nabla g)=\\sum_{a,b}J_{ab}\\frac{\\partial f}{\\partial\\xi_a}\\frac{\\partial g}{\\partial\\xi_b}$。对嵌套泊松括号展开：")+
    fml("\\{f,\\{g,h\\}\\} = \\sum_{a,b}J_{ab}\\frac{\\partial f}{\\partial\\xi_a}\\frac{\\partial}{\\partial\\xi_b}\\left(\\sum_{c,d}J_{cd}\\frac{\\partial g}{\\partial\\xi_c}\\frac{\\partial h}{\\partial\\xi_d}\\right)",
        "展开后分为两类项：一类对 $g$ 求导（$\\frac{\\partial^2 g}{\\partial\\xi_b\\partial\\xi_c}$），一类对 $h$ 求导（$\\frac{\\partial^2 h}{\\partial\\xi_b\\partial\\xi_d}$）：")+
    fml("\\{f,\\{g,h\\}\\} = \\sum_{a,b,c,d}J_{ab}J_{cd}\\frac{\\partial f}{\\partial\\xi_a}\\frac{\\partial^2 g}{\\partial\\xi_b\\partial\\xi_c}\\frac{\\partial h}{\\partial\\xi_d} + \\sum_{a,b,c,d}J_{ab}J_{cd}\\frac{\\partial f}{\\partial\\xi_a}\\frac{\\partial g}{\\partial\\xi_c}\\frac{\\partial^2 h}{\\partial\\xi_b\\partial\\xi_d}",
        "将雅可比恒等式左端的三项全部展开，第一类（含 $\\partial^2 g$ 的项）合并后利用 $J_{ab}J_{cd}+J_{ac}J_{db}+J_{ad}J_{bc}$ 的对称性可以证明恒等于零。具体地，含 $\\frac{\\partial^2 g}{\\partial\\xi_b\\partial\\xi_c}\\frac{\\partial f}{\\partial\\xi_a}\\frac{\\partial h}{\\partial\\xi_d}$ 的项来自三个嵌套括号，其系数之和为 $J_{ab}J_{cd}+J_{bc}J_{ad}+J_{ca}J_{bd}$。")+
    fml("J_{ab}J_{cd} + J_{bc}J_{ad} + J_{ca}J_{bd} = 0",
        "上式利用了 $J$ 的反对称性 $J_{ab}=-J_{ba}$ 和分量指标的重排。同理含 $\\frac{\\partial^2 h}{\\partial\\xi_b\\partial\\xi_d}$ 的项也合并为零。故雅可比恒等式成立。$\\blacksquare$"))
    + thm("李代数结构", p("泊松括号满足反对称性、双线性和雅可比恒等式，故相空间上的光滑函数在泊松括号下构成<strong>李代数</strong>（Lie algebra）。莱布尼茨法则进一步说明它是一个<strong>泊松代数</strong>。这一代数结构是经典力学与量子力学的共同基础。"))
)},
{"id":"tm-c2s3-3","name":"辛形式","tags":["def","thm","der"],"brief":"泊松括号的几何表述与辛矩阵。",
 "body": wrap(
    defn("辛矩阵与辛形式", p("引入 $2s\\times 2s$ 矩阵 $J=\\begin{pmatrix}0&I_s\\\\-I_s&0\\end{pmatrix}$，其中 $I_s$ 为 $s\\times s$ 单位矩阵。由 $J$ 可定义两个 $2s$ 维矢量 $u$ 与 $v$ 之间的<strong>辛形式</strong>（反对称内积）：")+
    fml("\\omega(u,v) = u^T J v",
        "由于 $J^T=-J$，有 $\\omega(u,v)=-\\omega(v,u)$，故 $\\omega$ 是反对称的。"))
    + der(p("<strong>泊松括号的辛形式推导：</strong>统一记正则坐标为 $\\xi_a$（$1\\le a\\le s$ 时 $\\xi_a=q_a$，$s+1\\le a\\le 2s$ 时 $\\xi_a=p_{a-s}$），$\\nabla f=(\\frac{\\partial f}{\\partial\\xi_1},\\dots,\\frac{\\partial f}{\\partial\\xi_{2s}})^T$。展开辛形式：")+
    fml("(\\nabla f)^T J (\\nabla g) = \\sum_{b,c=1}^{2s}\\frac{\\partial f}{\\partial\\xi_b}J_{bc}\\frac{\\partial g}{\\partial\\xi_c}",
        "将 $b,c$ 按 $1\\le b,c\\le s$（$q$ 部分）和 $s+1\\le b,c\\le 2s$（$p$ 部分）分四种情况展开。由 $J$ 的结构，$J_{\\alpha,\\delta}=0$（$q$-$q$ 块），$J_{\\alpha,s+\\delta}=\\delta_{\\alpha\\delta}$（$q$-$p$ 块），$J_{s+\\alpha,\\delta}=-\\delta_{\\alpha\\delta}$（$p$-$q$ 块），$J_{s+\\alpha,s+\\delta}=0$（$p$-$p$ 块）。代入得：")+
    fml("\\{f,g\\} = \\sum_{\\alpha=1}^{s}\\left(\\frac{\\partial f}{\\partial q_\\alpha}\\frac{\\partial g}{\\partial p_\\alpha} - \\frac{\\partial f}{\\partial p_\\alpha}\\frac{\\partial g}{\\partial q_\\alpha}\\right) = (\\nabla f)^T J (\\nabla g)",
        "这正是泊松括号的定义。故<strong>泊松括号 = 辛形式下的内积</strong>。"))
    + thm("正则方程的辛形式", p("令 $\\xi=(q_1,\\dots,q_s,p_1,\\dots,p_s)^T$，正则方程可写为紧凑形式")+
    fml("\\dot\\xi = J\\nabla H(\\xi)",
        "即 $\\dot q_\\alpha=\\frac{\\partial H}{\\partial p_\\alpha}$，$\\dot p_\\alpha=-\\frac{\\partial H}{\\partial q_\\alpha}$。$J$ 满足 $J^T=-J$，$J^2=-I$，$\\det J=1$。"))
    + app(p("辛形式是哈密顿力学的几何基础。相空间在辛形式下成为一个<strong>辛流形</strong>，哈密顿流是其上的哈密顿矢量场 $X_H=J\\nabla H$ 的积分曲线。这一观点是辛几何与辛拓扑的出发点。"))
)},
{"id":"tm-c2s3-4","name":"守恒量的判定","tags":["thm","der","app"],"brief":"用泊松括号判断守恒，含推导。",
 "body": wrap(
    thm("守恒判据", p("若力学量 $f(q,p,t)$ 不显含时间（$\\frac{\\partial f}{\\partial t}=0$），则 $f$ 为守恒量当且仅当")+
    fml("\\{f,H\\} = 0",
        "即 $f$ 与哈密顿量的泊松括号为零。"))
    + der(p("<strong>推导：</strong>对 $f(q,p,t)$ 求全导数，由链式法则：")+
    fml("\\frac{df}{dt} = \\sum_\\alpha\\frac{\\partial f}{\\partial q_\\alpha}\\dot q_\\alpha + \\sum_\\alpha\\frac{\\partial f}{\\partial p_\\alpha}\\dot p_\\alpha + \\frac{\\partial f}{\\partial t}",
        "代入正则方程 $\\dot q_\\alpha=\\frac{\\partial H}{\\partial p_\\alpha}$，$\\dot p_\\alpha=-\\frac{\\partial H}{\\partial q_\\alpha}$：")+
    fml("\\frac{df}{dt} = \\sum_\\alpha\\left(\\frac{\\partial f}{\\partial q_\\alpha}\\frac{\\partial H}{\\partial p_\\alpha} - \\frac{\\partial f}{\\partial p_\\alpha}\\frac{\\partial H}{\\partial q_\\alpha}\\right) + \\frac{\\partial f}{\\partial t} = \\{f,H\\} + \\frac{\\partial f}{\\partial t}",
        "若 $\\frac{\\partial f}{\\partial t}=0$，则 $\\frac{df}{dt}=\\{f,H\\}$。故 $f$ 守恒 $\\Leftrightarrow$ $\\frac{df}{dt}=0$ $\\Leftrightarrow$ $\\{f,H\\}=0$。$\\blacksquare$"))
    + app(p("若 $H$ 不含时，则 $\\{H,H\\}=0$，故能量 $H$ 守恒。<br>角动量各分量满足 $\\{L_x,L_y\\}=L_z$，$\\{L_y,L_z\\}=L_x$，$\\{L_z,L_x\\}=L_y$，构成 $so(3)$ 李代数。<br>若 $\\{L_x,H\\}=0$，则 $L_x$ 守恒。"))
)},
{"id":"tm-c2s3-5","name":"正则量子化","tags":["thm","der","app","note"],"brief":"从泊松括号到量子对易子的对应，含推导。",
 "body": wrap(
    thm("正则量子化规则", p("量子力学中，经典泊松括号对应量子对易子：")+
    fml("\\{f,g\\}_{cl} \\longrightarrow \\frac{1}{i\\hbar}[\\hat f,\\hat g]",
        "其中 $[\\hat f,\\hat g]=\\hat f\\hat g-\\hat g\\hat f$ 为量子对易子。"))
    + der(p("<strong>推导（对应关系的自洽性验证）：</strong>需要验证泊松括号的代数性质在量子层面被保持。<br><strong>（1）反对称性：</strong>$[\\hat f,\\hat g]=-\\hat g\\hat f+\\hat f\\hat g=-[\\hat g,\\hat f]$，与 $\\{f,g\\}=-\\{g,f\\}$ 对应。$\\surd$<br><strong>（2）双线性：</strong>对易子显然满足 $[a\\hat f+b\\hat g,\\hat h]=a[\\hat f,\\hat h]+b[\\hat g,\\hat h]$，与泊松括号双线性对应。$\\surd$<br><strong>（3）莱布尼茨法则：</strong>$[\\hat f\\hat g,\\hat h]=\\hat f[\\hat g,\\hat h]+[\\hat f,\\hat h]\\hat g$（直接展开即可验证），与 $\\{fg,h\\}=f\\{g,h\\}+\\{f,h\\}g$ 对应。$\\surd$<br><strong>（4）雅可比恒等式：</strong>对易子满足 $[\\hat f,[\\hat g,\\hat h]]+[\\hat g,[\\hat h,\\hat f]]+[\\hat h,[\\hat f,\\hat g]]=0$（直接展开可验证），与泊松括号的雅可比恒等式对应。$\\surd$<br>故对应 $\\{\\cdot,\\cdot\\}\\to\\frac{1}{i\\hbar}[\\cdot,\\cdot]$ 保持李代数结构。"))
    + app(p("基本泊松括号 $\\{q,p\\}=1$ 对应量子对易关系 $[\\hat q,\\hat p]=i\\hbar$，这是海森堡正则对易关系的来源。哈密顿正则方程 $\\dot f=\\{f,H\\}$ 对应海森堡方程 $\\frac{d\\hat f}{dt}=\\frac{1}{i\\hbar}[\\hat f,\\hat H]$。"))
    + note(p("正则量子化是从经典力学到量子力学的桥梁，泊松括号的代数结构（李代数）在量子层面被保持为算子代数。这一对应关系是狄拉克提出的，是量子力学形式化的重要支柱。"))
)},
],
},

# ---- 2.4 正则变换 ----
{
"name": "2.4 正则变换",
"color": "#c2410c",
"desc": "正则变换的定义、充分条件、辛变换",
"items": [
{"id":"tm-c2s4-1","name":"正则变换的概念","tags":["def","thm","app"],"brief":"保持正则方程形式的变换，哈密顿力学中的对称性变换。",
 "body": wrap(
    defn("正则变换", p("若变换 $(q,p)\\to(Q,P)$ 使正则方程形式不变，即存在新哈密顿量 $K(Q,P,t)$ 使")+
    fml("\\dot Q_\\alpha = \\frac{\\partial K}{\\partial P_\\alpha},\\qquad \\dot P_\\alpha = -\\frac{\\partial K}{\\partial Q_\\alpha}",
        "则称该变换为正则变换。正则变换是哈密顿力学中的对称性变换，相当于在相空间中做坐标变换。"))
    + thm("正则变换的意义", p("正则变换的目的是通过选择合适的变量，使新哈密顿量 $K$ 更简单（如 $K=0$ 或 $K$ 仅含部分变量），从而简化求解。若 $K\\equiv 0$，则 $\\dot Q=\\dot P=0$，新变量全部为常数，运动方程立即解出。"))
    + app(p("正则变换保持相空间体积不变（刘维尔定理），保持泊松括号不变，保持辛形式不变。它是哈密顿-雅可比理论的基础。"))
)},
{"id":"tm-c2s4-2","name":"正则变换的充分条件","tags":["thm","der"],"brief":"母函数与全微分条件。",
 "body": wrap(
    thm("正则变换条件", p("变换 $(q,p)\\to(Q,P)$ 为正则变换的充要条件是存在函数 $F$，使得")+
    fml("\\sum_\\alpha p_\\alpha dq_\\alpha - \\sum_\\alpha P_\\alpha dQ_\\alpha + (K-H)dt = dF",
        "即左边为某个函数 $F$ 的全微分。$F$ 称为正则变换的母函数（generating function）。"))
    + der(p("由哈密顿最小作用量原理，变换前后作用量的变分条件应等价。原作用量变分为 $\\delta\\int(\\sum p_\\alpha\\dot q_\\alpha-H)dt=0$，变换后为 $\\delta\\int(\\sum P_\\alpha\\dot Q_\\alpha-K)dt=0$。<br>两被积函数之差应为全导数 $\\frac{dF}{dt}$，即 $\\sum p_\\alpha\\dot q_\\alpha-H-(\\sum P_\\alpha\\dot Q_\\alpha-K)=\\frac{dF}{dt}$。<br>两边乘 $dt$ 得 $\\sum p_\\alpha dq_\\alpha-\\sum P_\\alpha dQ_\\alpha+(K-H)dt=dF$。"))
)},
{"id":"tm-c2s4-3","name":"辛变换与辛矩阵","tags":["def","thm","der"],"brief":"正则变换的矩阵表述，保辛形式不变。",
 "body": wrap(
    defn("辛变换", p("设变换 $\\xi_a\\to\\eta_a$ 的雅可比矩阵为 $M_{ab}=\\frac{\\partial\\eta_a}{\\partial\\xi_b}$。若满足")+
    fml("M J M^T = J \\quad\\text{即}\\quad \\sum_{b,c}M_{ab}J_{bc}M_{dc}=J_{ad}",
        "则称该变换为<strong>辛变换</strong>，矩阵 $M$ 称为<strong>辛矩阵</strong>。"))
    + thm("辛矩阵与正交矩阵的类比", p("<strong>正交矩阵</strong> $R$ 满足 $RR^T=I$，即 $RIR^T=I$，保持单位矩阵（欧氏度规）不变。<br><strong>辛矩阵</strong> $M$ 满足 $MJM^T=J$，保持辛形式 $J$ 不变。<br><strong>洛伦兹变换</strong> $\\Lambda$ 满足 $\\Lambda G\\Lambda^T=G$，保持闵氏度规 $G$ 不变。<br>这三类变换构成了统一的模式：保某度规不变的变换。"))
    + der(p("<strong>辛变换 $\\Rightarrow$ 正则变换的推导：</strong>设变换保辛形式不变，即 $MJM^T=J$。将正则坐标与动量分开讨论辛变换等式的四个部分。<br><strong>(i)</strong> $1\\le a,d\\le s$（$q$-$q$）：$J_{ad}=0$，$\\xi_a=q_\\alpha$，$\\xi_d=q_\\beta$，故 $\\{Q_\\alpha,Q_\\beta\\}_{q,p}=0=\\{q_\\alpha,q_\\beta\\}$。<br><strong>(ii)</strong> $1\\le a\\le s$，$s+1\\le d\\le 2s$（$q$-$p$）：$J_{ad}=\\delta_{\\alpha\\beta}$，$\\xi_a=q_\\alpha$，$\\xi_d=p_\\beta$，故 $\\{Q_\\alpha,P_\\beta\\}_{q,p}=\\delta_{\\alpha\\beta}=\\{q_\\alpha,p_\\beta\\}$。<br><strong>(iii)</strong> $s+1\\le a\\le 2s$，$1\\le d\\le s$（$p$-$q$）：$J_{ad}=-\\delta_{\\alpha\\beta}$，故 $\\{P_\\alpha,Q_\\beta\\}=-\\delta_{\\alpha\\beta}$。<br><strong>(iv)</strong> $s+1\\le a,d\\le 2s$（$p$-$p$）：$J_{ad}=0$，故 $\\{P_\\alpha,P_\\beta\\}=0$。<br>这证明了辛变换保持基本泊松括号不变，即新变量 $(Q,P)$ 仍满足正则关系，故变换为正则变换。"))
    + thm("辛矩阵的性质", p("辛矩阵构成一个群（辛群 $Sp(2s,\\mathbb{R})$）：<br>$\\det M=\\pm 1$，进一步可证 $\\det M=+1$。<br>$M_1,M_2$ 为辛矩阵，则 $M_1M_2$ 也是辛矩阵。<br>$M$ 为辛矩阵，则 $M^{-1}$ 也是辛矩阵。<br>辛变换保持相空间体积不变（刘维尔定理的矩阵表述）。"))
)},
{"id":"tm-c2s4-4","name":"正则变换的例子","tags":["exa","der"],"brief":"一维谐振子的作用量-角变量。",
 "body": wrap(
    exa(p("<strong>一维谐振子：</strong>$H=\\frac{p^2}{2m}+\\frac{1}{2}m\\omega^2 q^2$。引入作用量变量 $J$ 和角变量 $w$，做正则变换"))
    + der(p("令 $q=\\sqrt{\\frac{2J}{m\\omega}}\\sin(2\\pi w)$，$p=\\sqrt{2m\\omega J}\\cos(2\\pi w)$。<br>验证正则性：$\\frac{\\partial(q,p)}{\\partial(J,w)}=\\begin{pmatrix}\\frac{\\partial q}{\\partial J}&\\frac{\\partial q}{\\partial w}\\\\ \\frac{\\partial p}{\\partial J}&\\frac{\\partial p}{\\partial w}\\end{pmatrix}$，可验证 $M^T J M=J$。<br>新哈密顿量 $K=H=\\frac{2m\\omega J\\cos^2(2\\pi w)}{2m}+\\frac{1}{2}m\\omega^2\\cdot\\frac{2J}{m\\omega}\\sin^2(2\\pi w)=\\omega J(\\cos^2+\\sin^2)=\\omega J$。<br>$K$ 不显含 $w$，故正则方程给出 $\\dot w=\\frac{\\partial K}{\\partial J}=\\omega$，$\\dot J=-\\frac{\\partial K}{\\partial w}=0$。<br>故 $J$ 守恒（作用量），$w=\\omega t+w_0$（角变量线性增长），频率为 $\\omega$。"))
)},
],
},

# ---- 2.5 母函数与哈密顿-雅科比方程 ----
{
"name": "2.5 母函数与哈密顿-雅科比方程",
"color": "#be185d",
"desc": "四类母函数、哈密顿-雅科比方程、分离变量法",
"items": [
{"id":"tm-c2s5-1","name":"四类母函数","tags":["def","thm","der","exa"],"brief":"四种形式的正则变换母函数及其推导。",
 "body": wrap(
    thm("第一类母函数 $F_1(q,Q,t)$", p("由全微分条件 $\\sum p_\\alpha dq_\\alpha-\\sum P_\\alpha dQ_\\alpha+(\\tilde H-H)dt=dF_1$，若 $F_1$ 以 $q,Q,t$ 为自变量，则比较系数得：")+
    fml("p_\\alpha=\\frac{\\partial F_1}{\\partial q_\\alpha},\\quad P_\\alpha=-\\frac{\\partial F_1}{\\partial Q_\\alpha},\\quad \\tilde H=H+\\frac{\\partial F_1}{\\partial t}",
        "给定 $F_1(q,Q,t)$，由第一式可解出 $Q=Q(q,p,t)$，由第二式得 $P=P(q,Q,t)$，从而完成正则变换。"))
    + der(p("<strong>勒让德变换导出其他三类母函数：</strong>对微分等式两边做勒让德变换，可替换自变量。<br><strong>第二类 $F_2(q,P,t)$：</strong>两端加 $d(\\sum P_\\alpha Q_\\alpha)$，得 $\\sum p_\\alpha dq_\\alpha+\\sum Q_\\alpha dP_\\alpha+(\\tilde H-H)dt=dF_2$，其中")+
    fml("F_2(q,P,t)=F_1(q,Q,t)+\\sum_\\alpha P_\\alpha Q_\\alpha",
        "$p_\\alpha=\\frac{\\partial F_2}{\\partial q_\\alpha},\\quad Q_\\alpha=\\frac{\\partial F_2}{\\partial P_\\alpha},\\quad \\tilde H=H+\\frac{\\partial F_2}{\\partial t}$"))
    + der(p("<strong>第三类 $F_3(p,Q,t)$：</strong>对 $F_1$ 等式两端减 $d(\\sum p_\\alpha q_\\alpha)$，得 $-\\sum q_\\alpha dp_\\alpha-\\sum P_\\alpha dQ_\\alpha+(\\tilde H-H)dt=dF_3$，其中")+
    fml("F_3(p,Q,t)=F_1(q,Q,t)-\\sum_\\alpha p_\\alpha q_\\alpha",
        "$q_\\alpha=-\\frac{\\partial F_3}{\\partial p_\\alpha},\\quad P_\\alpha=-\\frac{\\partial F_3}{\\partial Q_\\alpha},\\quad \\tilde H=H+\\frac{\\partial F_3}{\\partial t}$"))
    + der(p("<strong>第四类 $F_4(p,P,t)$：</strong>同时做勒让德变换 $q\\to p$ 和 $Q\\to P$，得 $-\\sum q_\\alpha dp_\\alpha+\\sum Q_\\alpha dP_\\alpha+(\\tilde H-H)dt=dF_4$，其中")+
    fml("F_4(p,P,t)=F_1(q,Q,t)-\\sum_\\alpha p_\\alpha q_\\alpha+\\sum_\\alpha P_\\alpha Q_\\alpha",
        "$q_\\alpha=-\\frac{\\partial F_4}{\\partial p_\\alpha},\\quad Q_\\alpha=\\frac{\\partial F_4}{\\partial P_\\alpha},\\quad \\tilde H=H+\\frac{\\partial F_4}{\\partial t}$"))
    + thm("母函数存在的充要条件", p("<strong>定理：</strong>变换为正则变换 $\\Leftrightarrow$ 存在母函数。<br>充分性已由上述推导证明（给定母函数即可构造正则变换）。必要性需要高维斯托克斯公式，此处从略。<br>注意：四类母函数中 $\\tilde H$ 相同，因为勒让德变换只换了自变量，不改变 $\\tilde H$ 的值。"))
    + exa(p("<strong>恒等变换：</strong>取 $F_2=\\sum q_\\alpha P_\\alpha$，则 $p_\\alpha=P_\\alpha$，$Q_\\alpha=q_\\alpha$，$\\tilde H=H$，即恒等变换。<br><strong>平移变换：</strong>取 $F_2=\\sum(q_\\alpha+a_\\alpha)P_\\alpha$，则 $Q_\\alpha=q_\\alpha+a_\\alpha$，$P_\\alpha=p_\\alpha$，即坐标平移。"))
)},
{"id":"tm-c2s5-2","name":"哈密顿-雅科比方程","tags":["def","thm","der","app"],"brief":"使新哈密顿量为零的正则变换。",
 "body": wrap(
    defn("哈密顿主函数", p("取母函数 $F_2=S(q,P,t)$，要求新哈密顿量 $K=H+\\frac{\\partial S}{\\partial t}=0$。由于 $p_\\alpha=\\frac{\\partial S}{\\partial q_\\alpha}$，代入得")+
    fml("H\\left(q_1,\\dots,q_s,\\frac{\\partial S}{\\partial q_1},\\dots,\\frac{\\partial S}{\\partial q_s},t\\right) + \\frac{\\partial S}{\\partial t} = 0",
        "此即<strong>哈密顿-雅科比方程</strong>，$S(q,P,t)$ 称为哈密顿主函数。这是关于 $S$ 的一阶非线性偏微分方程。"))
    + thm("完全解", p("若能求得含 $s$ 个独立常数 $\\alpha_1,\\dots,\\alpha_s$ 的完全解 $S(q,\\alpha,t)$，则系统的运动可由")+
    fml("\\beta_i = \\frac{\\partial S}{\\partial\\alpha_i},\\qquad p_i = \\frac{\\partial S}{\\partial q_i}",
        "其中 $\\beta_i$ 为另外 $s$ 个常数。"))
    + der(p("由于 $K=0$，新正则变量 $Q_i=\\beta_i$（常数）和 $P_i=\\alpha_i$（常数）。<br>由 $Q_i=\\frac{\\partial F_2}{\\partial P_i}=\\frac{\\partial S}{\\partial\\alpha_i}=\\beta_i$，反解出 $q_i(t)$。<br>由 $p_i=\\frac{\\partial F_2}{\\partial q_i}=\\frac{\\partial S}{\\partial q_i}$，得到动量。<br>这样就将求解 $2s$ 个一阶常微分方程的问题转化为求解一个偏微分方程。"))
    + app(p("哈密顿-雅科比方程是求解力学系统最有力的方法之一，尤其适用于可分离变量的系统。"))
)},
{"id":"tm-c2s5-3","name":"分离变量法","tags":["thm","der","app","exa"],"brief":"将HJ方程分解为常微分方程，含谐振子实例。",
 "body": wrap(
    thm("不含时哈密顿量的分离", p("若 $H$ 不显含时间，则 $S=-Et+W(q)$，其中 $E$ 为能量常数。$W$ 满足")+
    fml("H\\left(q,\\frac{\\partial W}{\\partial q}\\right) = E",
        "$W(q)$ 称为哈密顿特征函数。若 $W$ 可分离为各坐标函数之和 $W=\\sum_i W_i(q_i)$，则方程分解为 $s$ 个常微分方程。"))
    + der(p("<strong>可分离变量条件：</strong>HJ方程能否分离取决于坐标系选择。Stäckel 条件给出了一个系统在何种正交曲线坐标下可分离的判据：度量系数 $h_i$ 与势能 $V$ 满足特定的可分性条件。常见可分离坐标系：笛卡尔、极坐标、抛物坐标、椭圆坐标（对应不同的对称性）。"))
    + der(p("<strong>谐振子的 HJ 解（一维）：</strong>$H=\\frac{p^2}{2m}+\\frac{1}{2}m\\omega^2 q^2$。设 $S=-Et+W(q)$，则 HJ 方程为")+
    fml("\\frac{1}{2m}\\left(\\frac{dW}{dq}\\right)^2 + \\frac{1}{2}m\\omega^2 q^2 = E",
        "解出 $\\frac{dW}{dq}=\\sqrt{2mE-m^2\\omega^2 q^2}=m\\omega\\sqrt{\\frac{2E}{m\\omega^2}-q^2}$。<br>令 $q_0=\\sqrt{\\frac{2E}{m\\omega^2}}$（振幅），则 $W(q)=\\int_0^q m\\omega\\sqrt{q_0^2-x^2}\\,dx=m\\omega\\int_0^q\\sqrt{q_0^2-x^2}\\,dx$。<br>代入 $x=q_0\\sin\\varphi$，$dx=q_0\\cos\\varphi\\,d\\varphi$：$\\sqrt{q_0^2-x^2}=q_0\\cos\\varphi$，故"))
    + der(fml("W(q) = m\\omega q_0^2 \\int_0^{\\arcsin(q/q_0)}\\cos^2\\varphi\\,d\\varphi = \\frac{m\\omega q_0^2}{2}\\left[\\arcsin\\frac{q}{q_0}+\\frac{q}{q_0}\\sqrt{1-\\frac{q^2}{q_0^2}}\\right]",
        "由 $\\beta=\\partial S/\\partial E=-t+\\partial W/\\partial E$。计算 $\\frac{\\partial W}{\\partial E}=\\frac{\\partial W}{\\partial q_0}\\frac{dq_0}{dE}=\\frac{1}{\\omega}\\arcsin\\frac{q}{q_0}$（利用 $q_0=\\sqrt{2E/m\\omega^2}$）。<br>故 $\\beta=-t+\\frac{1}{\\omega}\\arcsin\\frac{q}{q_0}$，反解得")+
    fml("q(t) = q_0\\sin\\big[\\omega(t-\\beta)\\big] = \\sqrt{\\frac{2E}{m\\omega^2}}\\sin(\\omega t+\\delta)",
        "其中 $\\delta=-\\omega\\beta$。这正是经典谐振子解，由 HJ 方程完整解出。同时 $p=\\partial S/\\partial q=m\\omega\\sqrt{q_0^2-q^2}=m\\omega q_0\\cos(\\omega t+\\delta)$，与 $\\dot q$ 一致。"))
    + app(p("<strong>中心力场</strong>：$W(r,\\theta,\\varphi)=W_r(r)+W_\\theta(\\theta)+W_\\varphi(\\varphi)$ 可分别求解各坐标，分离常数对应角动量的各分量。<br><strong>抛物坐标</strong>：库仑势 $V=-k/r$ 在抛物坐标 $(\\xi,\\eta)$ 下可分离，用于研究氢原子和卢瑟福散射。<br><strong>椭圆坐标</strong>：双中心 $1/r$ 问题（如 $H_2^+$ 分子）在椭圆坐标下可分离。"))
)},
{"id":"tm-c2s5-4","name":"作用量-角变量","tags":["def","thm","der","app"],"brief":"周期运动的描述与量子化条件。",
 "body": wrap(
    defn("作用量-角变量", p("对周期运动系统，定义作用量变量")+
    fml("J_i = \\oint p_i\\,dq_i = \\oint \\frac{\\partial W}{\\partial q_i}\\,dq_i",
        "积分沿一个周期完成。由 HJ 理论，$J_i$ 是新动量（常数），对应的角变量 $w_i$ 以频率 $\\nu_i=\\dot w_i$ 线性增长。"))
    + thm("频率公式", p("系统的振动频率由作用量给出：")+
    fml("\\nu_i = \\dot w_i = \\frac{\\partial H}{\\partial J_i}",
        "这是绝热不变量的核心结果，也是旧量子论的玻尔-索末菲量子化条件 $\\oint p_i\\,dq_i=n_i h$ 的来源。"))
    + der(p("<strong>谐振子的作用量：</strong>由 $p=m\\omega\\sqrt{q_0^2-q^2}$，积分一个周期：")+
    fml("J = \\oint p\\,dq = 2\\int_{-q_0}^{q_0} m\\omega\\sqrt{q_0^2-q^2}\\,dq = m\\omega\\pi q_0^2 = \\frac{2\\pi E}{\\omega}",
        "（利用 $\\int_{-q_0}^{q_0}\\sqrt{q_0^2-q^2}\\,dq=\\frac{\\pi q_0^2}{2}$，且 $E=\\frac{1}{2}m\\omega^2 q_0^2$）。<br>由 $E=\\frac{\\omega J}{2\\pi}$，频率 $\\nu=\\partial H/\\partial J=\\omega/2\\pi$，与运动学结果一致。"))
    + app(p("作用量-角变量方法是处理周期运动（行星轨道、谐振子、摆）的利器，也是绝热不变量和旧量子论的数学基础。在等离子体物理和加速器物理中仍有重要应用。"))
)},
],
},

# ---- 2.6 无穷小正则变换与守恒量 ----
{
"name": "2.6 无穷小正则变换与守恒量",
"color": "#059669",
"desc": "无穷小正则变换、生成元、哈密顿力学诺特定理",
"items": [
{"id":"tm-c2s6-1","name":"无穷小正则变换","tags":["def","thm","der"],"brief":"无限接近恒等的正则变换。",
 "body": wrap(
    defn("无穷小正则变换", p("考虑无穷小参数 $\\varepsilon$，变换 $q\\to q+\\delta q$，$p\\to p+\\delta p$，其中 $\\delta q,\\delta p$ 为 $\\varepsilon$ 的一阶小量。若该变换为正则变换，则称为无穷小正则变换。"))
    + thm("生成元", p("任何无穷小正则变换都由一个生成元函数 $G(q,p,t)$ 生成：")+
    fml("\\delta q_\\alpha = \\varepsilon\\frac{\\partial G}{\\partial p_\\alpha},\\qquad \\delta p_\\alpha = -\\varepsilon\\frac{\\partial G}{\\partial q_\\alpha}",
        "即 $\\delta q=\\varepsilon\\{q,G\\}$，$\\delta p=\\varepsilon\\{p,G\\}$。"))
    + der(p("取母函数 $F_2=\\sum q_\\alpha P_\\alpha+\\varepsilon G(q,P,t)$。由 $p_\\alpha=\\frac{\\partial F_2}{\\partial q_\\alpha}=P_\\alpha+\\varepsilon\\frac{\\partial G}{\\partial q_\\alpha}$，故 $P_\\alpha=p_\\alpha-\\varepsilon\\frac{\\partial G}{\\partial q_\\alpha}$。<br>由 $Q_\\alpha=\\frac{\\partial F_2}{\\partial P_\\alpha}=q_\\alpha+\\varepsilon\\frac{\\partial G}{\\partial P_\\alpha}\\approx q_\\alpha+\\varepsilon\\frac{\\partial G}{\\partial p_\\alpha}$（$P\\approx p$）。<br>因此 $\\delta q_\\alpha=\\varepsilon\\frac{\\partial G}{\\partial p_\\alpha}$，$\\delta p_\\alpha=P_\\alpha-p_\\alpha=-\\varepsilon\\frac{\\partial G}{\\partial q_\\alpha}$。"))
)},
{"id":"tm-c2s6-2","name":"连续正则变换","tags":["thm","der"],"brief":"有限变换由生成元指数化得到。",
 "body": wrap(
    thm("连续变换", p("有限参数的连续正则变换可由无穷小变换复合得到。设生成元为 $G$，参数为 $u$，则变换可表示为")+
    fml("\\xi(u) = e^{u\\{\\cdot,G\\}}\\xi(0)",
        "其中 $\\{\\cdot,G\\}$ 为泊松括号算子。"))
    + der(p("由 $\\frac{d\\xi}{du}=\\{\\xi,G\\}$，迭代展开：$\\xi(u)=\\xi(0)+u\\{\\xi,G\\}+\\frac{u^2}{2!}\\{\\{\\xi,G\\},G\\}+\\cdots=\\sum_{n=0}^\\infty\\frac{u^n}{n!}\\{\\xi,G\\}^{(n)}$，其中 $\\{\\xi,G\\}^{(n)}$ 表示 $n$ 重泊松括号。这就是指数形式。"))
)},
{"id":"tm-c2s6-3","name":"哈密顿力学中的诺特定理","tags":["def","thm","der","app"],"brief":"对称性与守恒量在哈密顿框架中的表述。",
 "body": wrap(
    defn("对称性变换", p("若连续变换使哈密顿量不变（$\\delta H=0$），则称该变换为对称性变换。")+
    fml("\\delta H = \\varepsilon\\{H,G\\} = 0",
        "其中 $G$ 为变换的生成元。"))
    + thm("诺特定理（哈密顿形式）", p("若 $G$ 生成的连续变换是对称性变换（即 $\\{H,G\\}=0$），则 $G$ 为守恒量：")+
    fml("\\{H,G\\} = 0 \\Rightarrow \\frac{dG}{dt} = 0",
        "反之，若 $G$ 为守恒量（$\\{H,G\\}=0$），则 $G$ 生成的变换是对称性变换。对称性与守恒量一一对应。"))
    + der(p("由 $\\frac{dG}{dt}=\\frac{\\partial G}{\\partial t}+\\{G,H\\}$。若 $G$ 不显含时间，则 $\\frac{dG}{dt}=\\{G,H\\}=-\\{H,G\\}$。<br>对称性要求 $\\delta H=\\varepsilon\\{H,G\\}=0$，故 $\\{H,G\\}=0$，因此 $\\frac{dG}{dt}=0$，$G$ 守恒。"))
    + app(p("<strong>动量守恒：</strong>$G=p_x$ 生成 $x$ 方向平移 $\\delta x=\\varepsilon$，$\\{H,p_x\\}=-\\frac{\\partial H}{\\partial x}=0$（$H$ 不含 $x$）$\\Rightarrow$ 动量守恒。<br><strong>角动量守恒：</strong>$G=L_z$ 生成绕 $z$ 轴转动，$\\{H,L_z\\}=0$ $\\Rightarrow$ 角动量守恒。<br><strong>能量守恒：</strong>$G=H$ 生成时间平移，$\\{H,H\\}=0$ $\\Rightarrow$ 能量守恒。"))
)},
{"id":"tm-c2s6-4","name":"哈密顿最小作用量原理","tags":["def","thm","der"],"brief":"相空间中的作用量变分原理。",
 "body": wrap(
    defn("哈密顿作用量", p("在哈密顿力学中，作用量泛函为")+
    fml("S[q(t),p(t)] = \\int_{t_i}^{t_f}\\left(\\sum_\\alpha p_\\alpha\\dot q_\\alpha - H(q,p,t)\\right)dt",
        "注意自变量为正则坐标 $q(t)$ 和正则动量 $p(t)$，二者独立变分。"))
    + thm("哈密顿最小作用量原理", p("在所有 $q_\\alpha(t_i)$ 和 $q_\\alpha(t_f)$ 固定的运动中，真实运动（满足正则方程的运动）使作用量取极值：")+
    fml("\\delta S = 0",
        "边界条件：$\\delta q_\\alpha(t_i)=\\delta q_\\alpha(t_f)=0$，但 $\\delta p_\\alpha(t_i)$ 和 $\\delta p_\\alpha(t_f)$ 可任意。"))
    + der(p("<strong>完整推导：</strong>对 $S$ 取变分：")+
    fml("\\delta S = \\int_{t_i}^{t_f}\\left(\\dot q_\\alpha\\,\\delta p_\\alpha + p_\\alpha\\,\\delta\\dot q_\\alpha - \\frac{\\partial H}{\\partial q_\\alpha}\\delta q_\\alpha - \\frac{\\partial H}{\\partial p_\\alpha}\\delta p_\\alpha\\right)dt",
        "对 $p_\\alpha\\,\\delta\\dot q_\\alpha$ 分部积分：$\\int p_\\alpha\\frac{d}{dt}\\delta q_\\alpha\\,dt = [p_\\alpha\\delta q_\\alpha]_{t_i}^{t_f} - \\int\\dot p_\\alpha\\delta q_\\alpha\\,dt$。由边界条件 $\\delta q(t_i)=\\delta q(t_f)=0$，边界项为零。")+
    fml("\\delta S = \\int_{t_i}^{t_f}\\left[\\left(\\dot q_\\alpha - \\frac{\\partial H}{\\partial p_\\alpha}\\right)\\delta p_\\alpha - \\left(\\dot p_\\alpha + \\frac{\\partial H}{\\partial q_\\alpha}\\right)\\delta q_\\alpha\\right]dt = 0",
        "由于 $\\delta q_\\alpha(t)$ 和 $\\delta p_\\alpha(t)$ 在 $(t_i,t_f)$ 内任意独立取值，被积函数中两组系数必须分别为零：")+
    fml("\\dot q_\\alpha = \\frac{\\partial H}{\\partial p_\\alpha},\\qquad \\dot p_\\alpha = -\\frac{\\partial H}{\\partial q_\\alpha}",
        "这正是哈密顿正则方程。<br>反之，若 $q(t),p(t)$ 满足正则方程，则 $\\delta S=0$。故哈密顿最小作用量原理与正则方程等价。"))
    + app(p("拉格朗日形式中 $S=\\int L\\,dt$ 仅对 $q(t)$ 变分，而哈密顿形式中 $p(t)$ 与 $q(t)$ 独立变分，体现了相空间的辛结构。两种形式通过勒让德变换 $H=\\sum p\\dot q - L$ 等价。"))
)},
],
},
]

print(f"Ch2: {sum(len(s['items']) for s in ch2_sections)} items")

# =====================================================
#  CHAPTER 3: 力学经典问题 (含电磁场、非惯性系)
# =====================================================
ch3_sections = [

# ---- 3.1 微振动与简正坐标 ----
{
"name": "3.1 微振动与简正坐标",
"color": "#2563eb",
"desc": "平衡位置、稳定平衡、小振动方程、简正坐标",
"items": [
{"id":"tm-c3s1-1","name":"平衡位置","tags":["def","thm","der"],"brief":"广义力为零的位置，含充要条件推导。",
 "body": wrap(
    defn("平衡位置", p("若 $\\vec q(t)=\\vec q_0$ 是系统动力学方程的解（即系统静止于 $\\vec q_0$），则 $\\vec q_0$ 称为系统的一个平衡位置。"))
    + thm("平衡位置的充要条件", p("对于约束和势能均不显含时间的系统，$\\vec q_0$ 为平衡位置的充要条件是广义力为零：")+
    fml("\\frac{\\partial U}{\\partial q_\\alpha}\\bigg|_{\\vec q=\\vec q_0} = 0,\\qquad \\alpha=1,\\dots,s",
        "即势能在平衡位置处取极值。"))
    + der(p("<strong>推导：</strong>对不显含时系统，约束不含时故 $\\vec r_i=\\vec r_i(\\vec q)$（不含 $t$），速度 $\\dot{\\vec r}_i=\\sum_\\alpha\\frac{\\partial\\vec r_i}{\\partial q_\\alpha}\\dot q_\\alpha$，动能为 $T=\\frac{1}{2}\\sum_{\\alpha\\beta}A_{\\alpha\\beta}(\\vec q)\\dot q_\\alpha\\dot q_\\beta$（纯二次型，无一次项和零次项）。<br>欧拉-拉格朗日方程：$\\frac{d}{dt}\\frac{\\partial T}{\\partial\\dot q_\\alpha}-\\frac{\\partial T}{\\partial q_\\alpha}=-\\frac{\\partial U}{\\partial q_\\alpha}$。<br><strong>必要性：</strong>若 $\\vec q_0$ 为平衡位置，则 $\\dot q=0$，故 $\\frac{\\partial T}{\\partial\\dot q_\\alpha}={\\sum_\\beta A_{\\alpha\\beta}\\dot q_\\beta}=0$，$\\frac{d}{dt}\\frac{\\partial T}{\\partial\\dot q_\\alpha}=0$。又 $\\frac{\\partial T}{\\partial q_\\alpha}=\\frac{1}{2}\\sum_{\\beta\\gamma}\\frac{\\partial A_{\\beta\\gamma}}{\\partial q_\\alpha}\\dot q_\\beta\\dot q_\\gamma=0$。故 $\\frac{\\partial U}{\\partial q_\\alpha}=0$。<br><strong>充分性：</strong>若 $\\frac{\\partial U}{\\partial q_\\alpha}|_{\\vec q_0}=0$，则 $\\vec q(t)=\\vec q_0$（$\\dot q=0$）满足方程，故为平衡位置。$\\blacksquare$"))
)},
{"id":"tm-c3s1-2","name":"平衡的分类","tags":["def","thm","der"],"brief":"稳定、不稳定、随遇平衡及稳定条件推导。",
 "body": wrap(
    defn("稳定平衡", p("对处于平衡位置的系统，若经历任意小扰动后运动完全局限于平衡位置附近，则称稳定平衡。严格定义：$\\forall\\varepsilon>0,\\exists\\delta>0$，使初始 $|\\vec q(t_0)-\\vec q_0|<\\delta$ 且 $|\\vec p(t_0)|<\\delta$ 时，恒有 $|\\vec q(t)-\\vec q_0|<\\varepsilon$。"))
    + thm("稳定平衡的充分条件", p("保守系统在平衡位置 $\\vec q_0$ 处稳定的充分条件是势能取严格极小值：")+
    fml("U(\\vec q_0) \\text{ 为严格极小值 } \\Rightarrow \\text{ 稳定平衡}"))
    + der(p("<strong>推导：</strong>由能量守恒 $E=T+U$。初始时刻系统在 $\\vec q_0$ 附近，$T(t_0)\\le\\frac{1}{2}\\delta^2$（动能有界），$U(\\vec q(t_0))\\ge U(\\vec q_0)$（$\\vec q_0$ 为极小值）。故 $E\\ge U(\\vec q_0)$。<br>设 $U$ 在 $\\vec q_0$ 处严格极小，则在 $\\vec q_0$ 的某邻域外 $U>U(\\vec q_0)+\\eta$（$\\eta>0$）。<br>若 $T(t_0)<\\eta/2$，则 $E<U(\\vec q_0)+\\eta$。运动过程中 $T=E-U\\ge 0$，故 $U\\le E<U(\\vec q_0)+\\eta$，即 $\\vec q$ 不会离开 $\\vec q_0$ 的邻域。故稳定。"))
    + der(p("<strong>小振动近似的依据：</strong>在稳定平衡处 $\\frac{\\partial U}{\\partial q_\\alpha}|_{\\vec q_0}=0$，将 $U$ 在 $\\vec q_0$ 处泰勒展开：")+
    fml("U(\\vec q) = U(\\vec q_0) + \\frac{1}{2}\\sum_{\\alpha\\beta}V_{\\alpha\\beta}\\eta_\\alpha\\eta_\\beta + O(\\eta^3)",
        "其中 $V_{\\alpha\\beta}=\\frac{\\partial^2 U}{\\partial q_\\alpha\\partial q_\\beta}|_{\\vec q_0}$ 为势能 Hessian 矩阵。$U$ 取极小值要求 $V_{\\alpha\\beta}$ 正定，这保证简正频率 $\\omega_i^2>0$（实频率），系统做稳定的小振动。"))
    + defn("不稳定与随遇平衡", p("<strong>不稳定平衡：</strong>$V_{\\alpha\\beta}$ 有负本征值（势能极大值方向），扰动后系统远离平衡位置。<br><strong>随遇平衡：</strong>势能在某方向为常数（$V$ 有零本征值），扰动后系统处于新的平衡位置。"))
)},
{"id":"tm-c3s1-3","name":"小振动方程","tags":["def","thm","der"],"brief":"在稳定平衡附近的线性化运动。",
 "body": wrap(
    thm("小振动方程", p("在稳定平衡位置附近，将势能展开到二阶")+
    fml("U(\\vec q) \\approx U(\\vec q_0) + \\frac{1}{2}\\sum_{\\alpha\\beta} V_{\\alpha\\beta}\\eta_\\alpha\\eta_\\beta",
        "其中 $\\eta_\\alpha=q_\\alpha-q_{0\\alpha}$ 为偏离平衡的位移，$V_{\\alpha\\beta}=\\frac{\\partial^2 U}{\\partial q_\\alpha\\partial q_\\beta}\\big|_{\\vec q_0}$ 为势能矩阵（Hessian）。"))
    + thm("动能与运动方程", p("动能在平衡附近近似为 $T=\\frac{1}{2}\\sum_{\\alpha\\beta}A_{\\alpha\\beta}\\dot\\eta_\\alpha\\dot\\eta_\\beta$（$A_{\\alpha\\beta}$ 为常数质量矩阵）。由拉格朗日方程得线性运动方程")+
    fml("\\sum_\\beta A_{\\alpha\\beta}\\ddot\\eta_\\beta + \\sum_\\beta V_{\\alpha\\beta}\\eta_\\beta = 0",
        "这是一个二阶线性齐次常微分方程组，可写为矩阵形式 $A\\ddot{\\eta}+V\\eta=0$。"))
    + der(p("由 $L=T-V$ 代入欧拉-拉格朗日方程：$\\frac{d}{dt}\\frac{\\partial T}{\\partial\\dot\\eta_\\alpha}-\\frac{\\partial T}{\\partial\\eta_\\alpha}=-\\frac{\\partial V}{\\partial\\eta_\\alpha}$。由于 $T$ 关于 $\\dot\\eta$ 二次且系数在平衡附近取常数，$\\frac{\\partial T}{\\partial\\eta_\\alpha}\\approx 0$，故得 $\\sum_\\beta A_{\\alpha\\beta}\\ddot\\eta_\\beta=-\\sum_\\beta V_{\\alpha\\beta}\\eta_\\beta$。"))
)},
{"id":"tm-c3s1-4","name":"简正频率与简正坐标","tags":["def","thm","der","app"],"brief":"广义本征值问题与简正坐标的求解步骤。",
 "body": wrap(
    defn("简正频率", p("设简谐解形式 $\\eta_\\alpha=a_\\alpha\\cos(\\omega t+\\phi)$，代入小振动方程得广义本征值问题")+
    fml("\\det(V - \\omega^2 A) = 0",
        "解得的 $s$ 个正根 $\\omega_i^2$（$i=1,\\dots,s$）称为简正频率的平方，对应的本征矢量 $\\vec a^{(i)}$ 为简正模式。"))
    + thm("简正坐标", p("通过线性变换 $\\eta_\\alpha=\\sum_i C_{\\alpha i}Q_i$（其中 $C$ 的列为本征矢量，并归一化使 $C^T A C=I$），可将运动方程解耦为")+
    fml("\\ddot Q_i + \\omega_i^2 Q_i = 0,\\qquad i=1,\\dots,s",
        "$Q_i$ 称为简正坐标，每个简正坐标以单一频率 $\\omega_i$ 做简谐振动。"))
    + der(p("<strong>推导：</strong>由于 $A$ 和 $V$ 均为实对称矩阵且 $A$ 正定，可通过广义本征值问题同时对角化 $A$ 和 $V$：$C^T A C=I$，$C^T V C=\\Omega^2=\\text{diag}(\\omega_1^2,\\dots,\\omega_s^2)$。<br>代入 $A\\ddot\\eta+V\\eta=0$，左乘 $C^T$ 得 $C^T A C\\ddot Q+C^T V C Q=\\ddot Q+\\Omega^2 Q=0$，即各 $Q_i$ 独立振动。"))
    + der(p("<strong>寻找简正坐标的一般方法（四步法）：</strong><br><strong>第一步：</strong>利用小振动近似，将动能与势能写为二次型形式：$T=\\frac{1}{2}\\dot\\eta^T A\\dot\\eta$，$V=\\frac{1}{2}\\eta^T B\\eta$（$B=V$ 为势能矩阵）。<br><strong>第二步：</strong>用正交矩阵 $C_1$ 将势能矩阵对角化：$B=C_1 D_1 C_1^T$，其中 $D_1=\\text{diag}(\\lambda_1,\\dots,\\lambda_s)$。定义新坐标 $\\vec x=C_1^T\\vec\\eta$，则 $V=\\frac{1}{2}\\vec x^T D_1\\vec x$。<br><strong>第三步：</strong>进一步用对角矩阵 $D_1^{-1/2}=\\text{diag}(1/\\sqrt{\\lambda_1},\\dots,1/\\sqrt{\\lambda_s})$ 变换 $\\vec y=D_1^{-1/2}\\vec x$，使 $V=\\frac{1}{2}\\vec y^T\\vec y$（势能化为平方和），此时 $T=\\frac{1}{2}\\dot{\\vec y}^T E\\dot{\\vec y}$（$E$ 仍为一般对称矩阵）。<br><strong>第四步：</strong>用正交矩阵 $C_2$ 将动能矩阵 $E$ 对角化：$E=C_2 D_2 C_2^T$，定义简正坐标 $\\vec z=C_2^T\\vec y$。则")+
    fml("T = \\frac{1}{2}\\dot{\\vec z}^T D_2\\dot{\\vec z},\\qquad V = \\frac{1}{2}\\vec z^T\\vec z",
        "拉格朗日量 $L=\\sum_i\\frac{1}{2}(\\mu_i\\dot z_i^2-z_i^2)$，方程 $\\mu_i\\ddot z_i+z_i=0$，频率 $\\omega_i=1/\\sqrt{\\mu_i}$。"))
    + app(p("<strong>物理意义：</strong>简正坐标使耦合的微分方程完全解耦，每个简正模式是独立的简谐振动。一般运动为各简正模式的线性叠加：$\\eta_\\alpha(t)=\\sum_i C_{\\alpha i}A_i\\sin(\\omega_i t+\\alpha_i)$。广义坐标到简正坐标的总变换为 $\\vec\\eta=C_1 D_1^{-1/2} C_2\\,\\vec z$。"))
)},
{"id":"tm-c3s1-5","name":"双单摆","tags":["exa","der"],"brief":"两个自由度耦合振动的经典例子。",
 "body": wrap(
    exa(p("双单摆由两根轻杆和两个质点组成，质量均为 $m$，杆长均为 $l$。取两杆与竖直方向夹角 $\\theta_1,\\theta_2$ 为广义坐标。"))
    + der(p("小角度近似下，动能和势能为")+
    fml("T = \\frac{1}{2}ml^2(2\\dot\\theta_1^2+\\dot\\theta_2^2+2\\dot\\theta_1\\dot\\theta_2),\\qquad V = \\frac{1}{2}mgl(2\\theta_1^2+\\theta_2^2)")
    + p("质量矩阵和势能矩阵为 $A=ml^2\\begin{pmatrix}2&1\\\\1&1\\end{pmatrix}$，$V=mgl\\begin{pmatrix}2&0\\\\0&1\\end{pmatrix}$。<br>本征值方程 $\\det(V-\\omega^2 A)=0$：")+
    fml("\\det\\begin{pmatrix}2mgl-2ml^2\\omega^2 & -ml^2\\omega^2 \\\\ -ml^2\\omega^2 & mgl-ml^2\\omega^2\\end{pmatrix}=0")
    + p("展开：$(2g-2l\\omega^2)(g-l\\omega^2)-l^2\\omega^4=0$ $\\Rightarrow$ $l^2\\omega^4-4gl\\omega^2+2g^2=0$。<br>解得")+
    fml("\\omega_1^2 = \\frac{g}{l}(2+\\sqrt{2}),\\qquad \\omega_2^2 = \\frac{g}{l}(2-\\sqrt{2})")
    + p("对应本征矢量：$\\omega_1$ 对应 $\\theta_1=-\\theta_2/\\sqrt{2}$（反相），$\\omega_2$ 对应 $\\theta_1=\\theta_2/\\sqrt{2}$（同相）。"))
)},
],
},

# ---- 3.2 中心势场与开普勒问题 ----
{
"name": "3.2 中心势场与开普勒问题",
"color": "#0d9488",
"desc": "两体问题约化、中心势场、开普勒定律",
"items": [
{"id":"tm-c3s2-1","name":"两体问题的单体约化","tags":["def","thm","der"],"brief":"将两体问题化为单体问题。",
 "body": wrap(
    thm("质心与相对运动", p("两体系统的运动可分解为质心的匀速运动和相对运动。设两质点质量为 $m_1,m_2$，位矢为 $\\vec r_1,\\vec r_2$，引入质心坐标 $\\vec R$ 和相对坐标 $\\vec r=\\vec r_2-\\vec r_1$。"))
    + fml("\\mu = \\frac{m_1 m_2}{m_1+m_2}",
        "$\\mu$ 称为约化质量。系统拉格朗日函数为 $L=\\frac{1}{2}(m_1+m_2)\\dot{\\vec R}^2 + \\frac{1}{2}\\mu\\dot{\\vec r}^2 - V(|\\vec r|)$。")
    + der(p("由 $\\vec R=\\frac{m_1\\vec r_1+m_2\\vec r_2}{m_1+m_2}$，$\\vec r=\\vec r_2-\\vec r_1$，反解得 $\\vec r_1=\\vec R-\\frac{m_2}{M}\\vec r$，$\\vec r_2=\\vec R+\\frac{m_1}{M}\\vec r$（$M=m_1+m_2$）。<br>动能 $T=\\frac{1}{2}m_1\\dot{\\vec r}_1^2+\\frac{1}{2}m_2\\dot{\\vec r}_2^2=\\frac{1}{2}M\\dot{\\vec R}^2+\\frac{1}{2}\\mu\\dot{\\vec r}^2$。<br>质心运动 $\\ddot{\\vec R}=0$（匀速），可分离。相对运动等价于一个质量为 $\\mu$ 的质点在中心势场 $V(r)$ 中的运动。"))
)},
{"id":"tm-c3s2-2","name":"中心势场的守恒量","tags":["thm","der","app"],"brief":"角动量守恒与有效势能。",
 "body": wrap(
    thm("角动量守恒", p("中心势场 $V(r)$ 中，$\\varphi$ 为循环坐标，故角动量守恒")+
    fml("L = \\mu r^2\\dot\\varphi = \\text{常数}"))
    + thm("有效势能", p("由能量守恒 $E=\\frac{1}{2}\\mu(\\dot r^2+r^2\\dot\\varphi^2)+V(r)$，利用角动量守恒消去 $\\dot\\varphi=L/\\mu r^2$，得径向运动方程")+
    fml("\\frac{1}{2}\\mu\\dot r^2 + V_{\\text{eff}}(r) = E,\\qquad V_{\\text{eff}}(r) = V(r) + \\frac{L^2}{2\\mu r^2}",
        "$\\frac{L^2}{2\\mu r^2}$ 称为离心势能。径向运动等效于在有效势 $V_{\\text{eff}}(r)$ 中的一维运动。"))
    + der(p("由 $E=\\frac{1}{2}\\mu\\dot r^2+\\frac{L^2}{2\\mu r^2}+V(r)$，整理得 $\\frac{1}{2}\\mu\\dot r^2=E-V_{\\text{eff}}(r)$。<br>对 $t$ 求导：$\\mu\\dot r\\ddot r=-V_{\\text{eff}}'(r)\\dot r$，消去 $\\dot r$ 得 $\\mu\\ddot r=-\\frac{dV_{\\text{eff}}}{dr}=-V'(r)+\\frac{L^2}{\\mu r^3}$。<br>这与从拉格朗日方程得到的径向方程一致。"))
    + app(p("有效势方法将二维中心力场问题简化为一维径向运动问题。有效势的极值点对应圆轨道。"))
)},
{"id":"tm-c3s2-3","name":"开普勒问题的轨道方程","tags":["thm","der","app"],"brief":"平方反比引力的圆锥曲线轨道。",
 "body": wrap(
    thm("轨道方程", p("对于万有引力势 $V(r)=-\\frac{k}{r}$（$k=Gm_1m_2$），引入 $u=1/r$，由比耐公式得轨道方程")+
    fml("\\frac{1}{r} = \\frac{\\mu k}{L^2}\\left(1+e\\cos(\\varphi-\\varphi_0)\\right)",
        "这是圆锥曲线方程，其中偏心率 $e=\\sqrt{1+\\frac{2EL^2}{\\mu k^2}}$。"))
    + der(p("由角动量守恒 $\\dot\\varphi=L/\\mu r^2=Lu^2/\\mu$。<br>径向方程 $\\mu\\ddot r=-\\frac{k}{r^2}+\\frac{L^2}{\\mu r^3}$。<br>利用 $\\frac{d}{dt}=\\dot\\varphi\\frac{d}{d\\varphi}=\\frac{Lu^2}{\\mu}\\frac{d}{d\\varphi}$，则 $\\dot r=\\frac{dr}{d\\varphi}\\dot\\varphi=-\\frac{L}{\\mu}\\frac{du}{d\\varphi}$。<br>$\\ddot r=\\frac{d}{dt}\\dot r=\\frac{Lu^2}{\\mu}\\frac{d}{d\\varphi}(-\\frac{L}{\\mu}\\frac{du}{d\\varphi})=-\\frac{L^2u^2}{\\mu^2}\\frac{d^2u}{d\\varphi^2}$。<br>代入径向方程：$-\\frac{L^2u^2}{\\mu}\\frac{d^2u}{d\\varphi^2}=-ku^2+\\frac{L^2u^3}{\\mu}$。<br>两边除以 $-\\frac{L^2u^2}{\\mu}$：$\\frac{d^2u}{d\\varphi^2}+u=\\frac{\\mu k}{L^2}$。<br>解为 $u=\\frac{\\mu k}{L^2}+A\\cos(\\varphi-\\varphi_0)$，即轨道方程。<br>由能量确定振幅 $A$：$e=\\frac{AL^2}{\\mu k}=\\sqrt{1+\\frac{2EL^2}{\\mu k^2}}$。"))
    + app(p("<strong>椭圆轨道：</strong>$e<1$（$E<0$），对应行星运动。<br><strong>抛物线：</strong>$e=1$（$E=0$）。<br><strong>双曲线：</strong>$e>1$（$E>0$），对应散射。"))
)},
{"id":"tm-c3s2-4","name":"开普勒定律","tags":["thm","der","app"],"brief":"行星运动三大定律的理论推导。",
 "body": wrap(
    thm("开普勒三大定律", p("<strong>第一定律（轨道定律）：</strong>行星沿椭圆轨道绕太阳运动，太阳位于椭圆的一个焦点上。<br><strong>第二定律（面积定律）：</strong>行星与太阳的连线在相等时间内扫过相等面积。<br><strong>第三定律（周期定律）：</strong>行星公转周期的平方与椭圆半长轴的立方成正比：$T^2\\propto a^3$。"))
    + der(p("<strong>面积定律：</strong>极坐标面积元 $dA=\\frac{1}{2}r^2d\\varphi$，故 $\\frac{dA}{dt}=\\frac{1}{2}r^2\\dot\\varphi=\\frac{L}{2\\mu}=$ 常数，由角动量守恒直接得出。<br><strong>第三定律：</strong>椭圆面积 $A=\\pi ab$，由 $\\frac{dA}{dt}=L/2\\mu$，周期 $T=\\frac{2\\pi ab\\mu}{L}$。<br>椭圆参数：半长轴 $a=\\frac{p}{1-e^2}=\\frac{L^2/\\mu k}{1-e^2}$，半短轴 $b=a\\sqrt{1-e^2}$。<br>由 $e^2=1+2EL^2/\\mu k^2$，得 $1-e^2=-2EL^2/\\mu k^2$，故 $a=\\frac{L^2/\\mu k}{-2EL^2/\\mu k^2}=\\frac{k}{-2E}$。<br>$b=a\\sqrt{1-e^2}=a\\sqrt{-2EL^2/\\mu k^2}$。<br>$T=2\\pi ab\\mu/L=2\\pi a\\cdot a\\sqrt{-2EL^2/\\mu k^2}\\cdot\\mu/L=2\\pi a^{3/2}\\sqrt{-2E\\mu/k^2}$。<br>代入 $-2E=k/a$：$T=2\\pi a^{3/2}\\sqrt{\\mu/k}$，故")+
    fml("T^2 = \\frac{4\\pi^2\\mu}{k}a^3",
        "这就是开普勒第三定律。对太阳系，$\\mu\\approx m_{\\text{行星}}$，$k=Gm_\\odot m_{\\text{行星}}$，故 $T^2=\\frac{4\\pi^2}{Gm_\\odot}a^3$，与行星质量无关。"))
    + app(p("开普勒定律是牛顿万有引力定律的实验基础，也是经典力学的伟大胜利。第三定律还被用于测定天体质量。"))
)},
{"id":"tm-c3s2-5","name":"用哈密顿-雅科比方程解开普勒问题","tags":["exa","der"],"brief":"HJ方法的经典应用。",
 "body": wrap(
    exa(p("对于中心势场 $V(r)=-k/r$，哈密顿量为 $H=\\frac{1}{2\\mu}(p_r^2+\\frac{p_\\theta^2}{r^2}+\\frac{p_\\varphi^2}{r^2\\sin^2\\theta})-\\frac{k}{r}$。"))
    + der(p("HJ 方程可分离变量：$S=-Et+\\alpha_\\varphi\\varphi+W_r(r)+W_\\theta(\\theta)$。<br>代入 HJ 方程得三个分离方程：<br>(1) $p_\\varphi=\\alpha_\\varphi$（绕 $z$ 轴角动量守恒）<br>(2) $p_\\theta^2+\\frac{\\alpha_\\varphi^2}{\\sin^2\\theta}=\\alpha_\\theta^2$（总角动量平方）<br>(3) $\\frac{1}{2\\mu}(p_r^2+\\frac{\\alpha_\\theta^2}{r^2})-\\frac{k}{r}=E$<br>积分 $W_r=\\int\\sqrt{2\\mu(E+\\frac{k}{r})-\\frac{\\alpha_\\theta^2}{r^2}}\\,dr$，$W_\\theta=\\int\\sqrt{\\alpha_\\theta^2-\\frac{\\alpha_\\varphi^2}{\\sin^2\\theta}}\\,d\\theta$。<br>由 $\\beta_i=\\partial S/\\partial\\alpha_i$ 可求得运动方程的解，结果与拉格朗日方法一致，得到椭圆轨道和开普勒方程。"))
)},
{"id":"tm-c3s2-6","name":"龙格-楞次矢量","tags":["def","thm","der","app","note"],"brief":"开普勒问题的额外守恒量与隐藏对称性。",
 "body": wrap(
    defn("龙格-楞次矢量", p("对平方反比中心力场 $V(r)=-k/r$，存在一个额外的守恒矢量——龙格-楞次矢量：")+
    fml("\\vec A = \\vec p\\times\\vec L - m k\\,\\hat r = \\vec p\\times\\vec L - m k\\,\\frac{\\vec r}{r}",
        "$\\vec A$ 沿椭圆长轴方向，指向近日点，其大小 $|\\vec A|=mk\\,e$（$e$ 为偏心率）。"))
    + thm("守恒性", p("对 $V(r)=-k/r$，$\\vec A$ 在运动过程中守恒：$\\frac{d\\vec A}{dt}=0$。"))
    + der(p("<strong>推导（守恒性）：</strong>由 $\\vec A=\\vec p\\times\\vec L-mk\\hat r$，对 $t$ 求导：")+
    fml("\\frac{d\\vec A}{dt} = \\dot{\\vec p}\\times\\vec L + \\vec p\\times\\dot{\\vec L} - mk\\frac{d\\hat r}{dt}",
        "对中心力，$\\dot{\\vec L}=0$。又 $\\dot{\\vec p}=\\vec F=-\\frac{k}{r^2}\\hat r$（引力）。代入：")+
    fml("\\dot{\\vec p}\\times\\vec L = -\\frac{k}{r^2}\\hat r\\times(\\vec r\\times\\vec p) = -\\frac{mk}{r^2}\\hat r\\times(\\vec r\\times\\dot{\\vec r})",
        "由 $\\vec r\\times(\\vec r\\times\\dot{\\vec r})=\\vec r(\\vec r\\cdot\\dot{\\vec r})-\\dot{\\vec r}\\,r^2=\\vec r(r\\dot r)-r^2\\dot{\\vec r}$（利用 $\\vec r\\cdot\\dot{\\vec r}=r\\dot r$），故")+
    fml("\\hat r\\times(\\vec r\\times\\dot{\\vec r}) = \\frac{1}{r}\\vec r(r\\dot r)-\\frac{r^2}{r}\\dot{\\vec r} = r\\dot r\\,\\hat r - r\\dot{\\vec r} = -r^2\\frac{d\\hat r}{dt}",
        "（最后一步利用 $\\frac{d\\hat r}{dt}=\\frac{\\dot{\\vec r}}{r}-\\frac{\\vec r\\dot r}{r^2}$，故 $r\\frac{d\\hat r}{dt}=\\dot{\\vec r}-\\dot r\\hat r$，即 $-r^2\\frac{d\\hat r}{dt}=r\\dot r\\hat r-r\\dot{\\vec r}$。）<br>故 $\\dot{\\vec p}\\times\\vec L=-\\frac{mk}{r^2}(-r^2\\frac{d\\hat r}{dt})=mk\\frac{d\\hat r}{dt}$，正好抵消第三项 $-mk\\frac{d\\hat r}{dt}$。故 $\\frac{d\\vec A}{dt}=0$。$\\blacksquare$"))
    + thm("轨道几何与 $\\vec A$ 的关系", p("利用 $\\vec A\\cdot\\vec r = (\\vec p\\times\\vec L)\\cdot\\vec r - mkr = (\\vec r\\times\\vec p)\\cdot\\vec L - mkr = L^2-mkr$，故")+
    fml("r = \\frac{L^2}{mk+|\\vec A|\\cos\\theta} = \\frac{L^2/mk}{1+e\\cos\\theta}",
        "其中 $e=|\\vec A|/(mk)$ 为偏心率，这正是圆锥曲线方程。$\\vec A$ 直接给出轨道参数。"))
    + app(p('<strong>隐藏对称性：</strong>角动量 $\\vec L$ 给出 3 个守恒量，加上能量 $E$ 和 $\\vec A$ 的 3 个分量（受约束 $\\vec A\\cdot\\vec L=0$ 实际独立 2 个），共 7 个独立守恒量。这超出了"一般中心势场"应有的 5 个守恒量（$E$、$\\vec L$）。多出的 2 个守恒量对应于 $SO(4)$ 隐藏对称性，使所有椭圆轨道闭合（贝特朗定理），并解释氢原子能级的"偶然简并"。'))
    + note(p("龙格-楞次矢量是 19 世纪由 Runge 和 Lenz 重新发现的经典结果，但其深层对称性意义直到 20 世纪 70 年代才被完全理解。它属于动力系统的隐藏对称性，类似规范势的几何相，是经典力学中深邃而优美的现象。"))
)},
],
},

# ---- 3.3 刚体运动学 ----
{
"name": "3.3 刚体运动学",
"color": "#7c3aed",
"desc": "自由度、欧拉角、角速度、欧拉运动学方程",
"items": [
{"id":"tm-c3s3-1","name":"刚体运动的自由度","tags":["def","thm"],"brief":"刚体有6个自由度。",
 "body": wrap(
    defn("刚体", p("刚体是任意两点间距固定不变的质点系。刚体的一般运动可分解为质心的平动和绕质心的转动。"))
    + thm("自由度", p("刚体的自由度为 6：3 个平动自由度（质心位置 $x_0,y_0,z_0$）+ 3 个转动自由度（取向，如三个欧拉角）。")+
    fml("\\text{独立坐标数} = 3n - (3n-6) = 6",
        "$n$ 个质点有 $3n$ 个坐标，刚体约束给出 $3n-6$ 个独立约束方程（每对质点一个距离约束，但并非全部独立）。"))
)},
{"id":"tm-c3s3-2","name":"欧拉角","tags":["def","thm","exa"],"brief":"描述刚体取向的三个角。",
 "body": wrap(
    defn("欧拉角", p("刚体的取向可用三个欧拉角 $(\\varphi,\\theta,\\psi)$ 描述，通过三次连续转动实现（zxz 约定）：")+
    fml("R = R_z(\\psi)\\,R_x(\\theta)\\,R_z(\\varphi)",
        "先绕固定 $z$ 轴转 $\\varphi$（进动角），再绕节线（$x'$ 轴）转 $\\theta$（章动角），最后绕刚体 $z''$ 轴转 $\\psi$（自转角）。"))
    + thm("适用范围", p("欧拉角在 $\\theta=0$ 或 $\\pi$ 处存在奇点（万向锁），此时 $\\varphi$ 和 $\\psi$ 不可区分。在这些奇异性附近需使用其他参数化（如四元数或罗德里格斯参数）。"))
)},
{"id":"tm-c3s3-3","name":"刚体的角速度","tags":["def","thm","der"],"brief":"从转动矩阵导出角速度矢量。",
 "body": wrap(
    defn("角速度矩阵", p("刚体定点转动由转动矩阵 $R(t)$ 描述，$R^TR=I$，$\\det R=1$。刚体上位矢 $\\vec r_i(t)=R(t)\\vec r_i(0)$。定义角速度矩阵")+
    fml("\\Omega(t) = \\dot R(t)\\,R^{-1}(t) = \\dot R(t)\\,R^T(t)"))
    + der(p("<strong>角速度矩阵的反对称性：</strong>由 $R^TR=I$，对时间求导得 $\\dot R^TR+R^T\\dot R=\\frac{d}{dt}(R^TR)=0$。故")+
    fml("\\Omega + \\Omega^T = \\dot R R^T + (\\dot R R^T)^T = \\dot R R^T + R\\dot R^T = \\frac{d}{dt}(RR^T) = 0",
        "故 $\\Omega$ 是<strong>反对称矩阵</strong>。"))
    + der(p("<strong>从反对称矩阵到角速度矢量：</strong>任何 $3\\times 3$ 反对称矩阵可写为")+
    fml("\\Omega = \\begin{pmatrix}0&-\\omega_3&\\omega_2\\\\\\omega_3&0&-\\omega_1\\\\-\\omega_2&\\omega_1&0\\end{pmatrix}",
        "可直接验证 $\\Omega\\vec r=\\vec\\omega\\times\\vec r$，其中 $\\vec\\omega=(\\omega_1,\\omega_2,\\omega_3)^T$。<br>故 $\\dot{\\vec r}_i=\\dot R\\vec r_i(0)=\\dot R R^{-1}R\\vec r_i(0)=\\Omega\\vec r_i=\\vec\\omega\\times\\vec r_i$。<br>这就从转动矩阵导出了<strong>角速度矢量</strong> $\\vec\\omega$。"))
    + thm("欧拉角分解", p("用欧拉角 $(\\varphi,\\theta,\\psi)$ 时，角速度可分解为三个转动贡献：")+
    fml("\\vec\\omega = \\dot\\varphi\\,\\hat z_0 + \\dot\\theta\\,\\hat{ON} + \\dot\\psi\\,\\hat z",
        "在<strong>刚体主轴坐标系</strong>中的分量为：")+
    fml("\\omega_1 = \\dot\\varphi\\sin\\theta\\sin\\psi + \\dot\\theta\\cos\\psi")+
    fml("\\omega_2 = \\dot\\varphi\\sin\\theta\\cos\\psi - \\dot\\theta\\sin\\psi")+
    fml("\\omega_3 = \\dot\\varphi\\cos\\theta + \\dot\\psi",
        "推导：$\\hat z''=(0,0,1)$，$\\hat{ON}=(\\cos\\psi,\\sin\\psi,0)$，$\\hat z_0=(\\sin\\theta\\sin\\psi,\\sin\\theta\\cos\\psi,\\cos\\theta)$。代入 $\\vec\\omega=\\dot\\varphi\\hat z_0+\\dot\\theta\\hat{ON}+\\dot\\psi\\hat z''$ 即得。"))
)},
{"id":"tm-c3s3-4","name":"欧拉运动学方程","tags":["thm","der"],"brief":"角速度到欧拉角速率的逆变换。",
 "body": wrap(
    thm("欧拉运动学方程", p("由角速度分量反解欧拉角速率，得欧拉运动学方程")+
    fml("\\dot\\varphi = \\frac{\\omega_1\\sin\\psi+\\omega_2\\cos\\psi}{\\sin\\theta}")
    + fml("\\dot\\theta = \\omega_1\\cos\\psi - \\omega_2\\sin\\psi")
    + fml("\\dot\\psi = \\omega_3 - (\\omega_1\\sin\\psi+\\omega_2\\cos\\psi)\\cot\\theta"))
    + der(p("由 $\\omega_1=\\dot\\varphi\\sin\\theta\\sin\\psi+\\dot\\theta\\cos\\psi$ 和 $\\omega_2=\\dot\\varphi\\sin\\theta\\cos\\psi-\\dot\\theta\\sin\\psi$，<br>第一式乘 $\\sin\\psi$ 加第二式乘 $\\cos\\psi$：$\\omega_1\\sin\\psi+\\omega_2\\cos\\psi=\\dot\\varphi\\sin\\theta$ $\\Rightarrow$ $\\dot\\varphi$。<br>第一式乘 $\\cos\\psi$ 减第二式乘 $\\sin\\psi$：$\\omega_1\\cos\\psi-\\omega_2\\sin\\psi=\\dot\\theta$。<br>由 $\\omega_3=\\dot\\varphi\\cos\\theta+\\dot\\psi$ $\\Rightarrow$ $\\dot\\psi=\\omega_3-\\dot\\varphi\\cos\\theta$，代入 $\\dot\\varphi$ 得结果。<br>注意 $\\theta=0,\\pi$ 时方程退化（万向锁）。"))
)},
],
},

# ---- 3.4 刚体动力学 ----
{
"name": "3.4 刚体动力学",
"color": "#c2410c",
"desc": "转动惯量张量、惯量主轴、欧拉动力学方程、陀螺",
"items": [
{"id":"tm-c3s4-1","name":"转动惯量张量","tags":["def","thm","der"],"brief":"描述刚体转动惯性的二阶张量，从角动量导出。",
 "body": wrap(
    defn("转动惯量张量", p("刚体绕定点 $O$ 转动，$\\vec r_i$ 为第 $i$ 个质点相对 $O$ 的位矢。角速度 $\\vec\\omega$，速度 $\\vec v_i=\\vec\\omega\\times\\vec r_i$。总角动量为")+
    fml("\\vec L = \\sum_i \\vec r_i\\times m_i\\vec v_i = \\sum_i m_i\\vec r_i\\times(\\vec\\omega\\times\\vec r_i)",
        "利用矢量叉积恒等式推导。"))
    + der(p("<strong>推导：</strong>利用矢量叉积恒等式 $\\vec A\\times(\\vec B\\times\\vec C)=(\\vec A\\cdot\\vec C)\\vec B-(\\vec A\\cdot\\vec B)\\vec C$，有")+
    fml("\\vec r_i\\times(\\vec\\omega\\times\\vec r_i) = (\\vec r_i\\cdot\\vec r_i)\\vec\\omega - (\\vec r_i\\cdot\\vec\\omega)\\vec r_i = r_i^2\\vec\\omega - (\\vec r_i\\cdot\\vec\\omega)\\vec r_i",
        "写成矩阵形式：$r_i^2\\vec\\omega-(\\vec r_i\\cdot\\vec\\omega)\\vec r_i=(r_i^2 I_3-\\vec r_i\\vec r_i^T)\\vec\\omega$，其中 $I_3$ 为 $3\\times3$ 单位矩阵，$\\vec r_i\\vec r_i^T$ 为外积（并矢）。")+
    fml("\\vec L = \\sum_i m_i(r_i^2 I_3 - \\vec r_i\\vec r_i^T)\\vec\\omega = I\\vec\\omega",
        "定义<strong>转动惯量张量</strong> $I=\\sum_i m_i(r_i^2 I_3-\\vec r_i\\vec r_i^T)$，连续情形 $I=\\int\\rho(\\vec r)(r^2I_3-\\vec r\\vec r^T)\\,dV$。"))
    + thm("张量分量", p("展开各分量，$I$ 为 $3\\times3$ 实对称矩阵：")+
    fml("I = \\begin{pmatrix}\\sum m(y^2+z^2) & -\\sum mxy & -\\sum mxz \\\\ -\\sum mxy & \\sum m(z^2+x^2) & -\\sum myz \\\\ -\\sum mxz & -\\sum myz & \\sum m(x^2+y^2)\\end{pmatrix}",
        "对角元 $I_{xx}=\\sum m(y^2+z^2)$ 为绕 $x$ 轴的转动惯量，非对角元 $I_{xy}=-\\sum mxy$ 为惯量积。由 $I_{ij}=I_{ji}$ 知 $I$ 实对称。"))
    + thm("动能与角动量", p("转动动能 $T=\\frac{1}{2}\\vec\\omega^T I\\vec\\omega=\\frac{1}{2}\\vec\\omega\\cdot\\vec L$。角动量 $\\vec L=I\\vec\\omega$。一般情况下 $\\vec L$ 与 $\\vec\\omega$ 不同向（仅当 $\\vec\\omega$ 沿惯量主轴时二者同向）。"))
)},
{"id":"tm-c3s4-2","name":"惯量主轴","tags":["def","thm","der"],"brief":"使惯量张量对角化的坐标系。",
 "body": wrap(
    defn("惯量主轴", p("若坐标系的三个轴是惯量张量的本征矢量方向，则称为惯量主轴。在主轴坐标系中，惯量张量对角化：")+
    fml("I = \\begin{pmatrix} I_1 & 0 & 0 \\\\ 0 & I_2 & 0 \\\\ 0 & 0 & I_3 \\end{pmatrix}",
        "$I_1,I_2,I_3$ 称为主转动惯量。此时 $L_i=I_i\\omega_i$，$T=\\frac{1}{2}(I_1\\omega_1^2+I_2\\omega_2^2+I_3\\omega_3^2)$。"))
    + thm("对称刚体分类", p("<strong>球对称陀螺：</strong>$I_1=I_2=I_3$（如均匀球体）。<br><strong>对称陀螺：</strong>$I_1=I_2\\neq I_3$（如旋转对称体）。<br><strong>不对称陀螺：</strong>$I_1\\neq I_2\\neq I_3$（任意刚体）。"))
    + der(p("惯量张量是实对称矩阵，由线性代数的谱定理，可通过正交变换（转动坐标系）对角化。本征值即为主转动惯量，本征矢量方向为惯量主轴。对每个刚体，至少存在三个相互垂直的惯量主轴。"))
)},
{"id":"tm-c3s4-3","name":"欧拉动力学方程","tags":["def","thm","der"],"brief":"刚体转动的动力学方程。",
 "body": wrap(
    thm("欧拉动力学方程", p("在刚体主轴坐标系中，刚体转动的动力学方程为")+
    fml("I_1\\dot\\omega_1 + (I_3-I_2)\\omega_2\\omega_3 = N_1")
    + fml("I_2\\dot\\omega_2 + (I_1-I_3)\\omega_3\\omega_1 = N_2")
    + fml("I_3\\dot\\omega_3 + (I_2-I_1)\\omega_1\\omega_2 = N_3",
        "其中 $N_1,N_2,N_3$ 为外力矩在主轴系的分量。"))
    + der(p("由角动量定理 $\\frac{d\\vec L}{dt}=\\vec N$。利用转动系中时间导数关系 $(\\frac{d\\vec L}{dt})_{in}=(\\frac{d\\vec L}{dt})_{rot}+\\vec\\omega\\times\\vec L$。<br>在主轴系中 $L_i=I_i\\omega_i$，故 $(\\frac{d\\vec L}{dt})_{rot}=(I_1\\dot\\omega_1,I_2\\dot\\omega_2,I_3\\dot\\omega_3)$。<br>$\\vec\\omega\\times\\vec L=(\\omega_2 L_3-\\omega_3 L_2,\\omega_3 L_1-\\omega_1 L_3,\\omega_1 L_2-\\omega_2 L_1)=(\\omega_2 I_3\\omega_3-\\omega_3 I_2\\omega_2,\\dots)=((I_3-I_2)\\omega_2\\omega_3,(I_1-I_3)\\omega_3\\omega_1,(I_2-I_1)\\omega_1\\omega_2)$。<br>代入角动量定理各分量即得欧拉动力学方程。"))
)},
{"id":"tm-c3s4-4","name":"欧拉陀螺","tags":["exa","thm","der"],"brief":"无力矩对称刚体的自由转动。",
 "body": wrap(
    defn("欧拉陀螺", p("不受外力矩（$\\vec N=0$）的刚体定点转动。对于对称欧拉陀螺（$I_1=I_2\\neq I_3$），运动可解析求解。"))
    + thm("自由对称陀螺的解", p("欧拉方程在 $\\vec N=0$ 时为")+
    fml("I_1\\dot\\omega_1+(I_3-I_1)\\omega_2\\omega_3=0,\\quad I_1\\dot\\omega_2+(I_1-I_3)\\omega_3\\omega_1=0,\\quad I_3\\dot\\omega_3=0")
    + p("解得 $\\omega_3=$ 常数，且 $\\omega_1,\\omega_2$ 以频率 $\\Omega=\\frac{|I_3-I_1|}{I_1}\\omega_3$ 绕 $z''$ 轴进动。刚体对称轴在空间中绕固定角动量方向做规则进动。"))
    + der(p("由第三式 $\\dot\\omega_3=0$，故 $\\omega_3=$ 常数。<br>令 $\\Omega=\\frac{I_3-I_1}{I_1}\\omega_3$，前两式为 $\\dot\\omega_1+\\Omega\\omega_2=0$，$\\dot\\omega_2-\\Omega\\omega_1=0$。<br>令 $\\omega_\\pm=\\omega_1\\pm i\\omega_2$，则 $\\dot\\omega_\\pm=\\mp i\\Omega\\omega_\\pm$，解得 $\\omega_\\pm=A_\\pm e^{\\mp i\\Omega t}$。<br>即 $\\omega_1=A\\cos(\\Omega t+\\phi)$，$\\omega_2=A\\sin(\\Omega t+\\phi)$，角速度矢量在刚体中绕 $z''$ 轴以角频率 $\\Omega$ 进动。"))
)},
{"id":"tm-c3s4-5","name":"拉格朗日陀螺","tags":["exa","der","app"],"brief":"对称重刚体的定点运动。",
 "body": wrap(
    defn("拉格朗日陀螺", p("对称陀螺（$I_1=I_2\\neq I_3$）在重力作用下绕固定点的运动，重心在对称轴上距定点 $l$ 处。这是可积系统（三个守恒量）。"))
    + thm("守恒量", p("拉格朗日陀螺有三个守恒量：<br><strong>能量：</strong>$E=\\frac{1}{2}I_1(\\dot\\theta^2+\\dot\\varphi^2\\sin^2\\theta)+\\frac{1}{2}I_3(\\dot\\psi+\\dot\\varphi\\cos\\theta)^2+Mgl\\cos\\theta$<br><strong>角动量 $z$ 分量：</strong>$p_\\varphi=I_1\\dot\\varphi\\sin^2\\theta+I_3(\\dot\\psi+\\dot\\varphi\\cos\\theta)\\cos\\theta=$ 常数<br><strong>角动量 $z''$ 分量：</strong>$p_\\psi=I_3(\\dot\\psi+\\dot\\varphi\\cos\\theta)=$ 常数"))
    + der(p("拉格朗日函数为")+
    fml("L = \\frac{1}{2}I_1(\\dot\\theta^2+\\dot\\varphi^2\\sin^2\\theta) + \\frac{1}{2}I_3(\\dot\\psi+\\dot\\varphi\\cos\\theta)^2 - Mgl\\cos\\theta")
    + p("$\\varphi$ 和 $\\psi$ 为循环坐标，故 $p_\\varphi=L_z$ 和 $p_\\psi=L_{z''}=I_3(\\dot\\psi+\\dot\\varphi\\cos\\theta)$ 守恒。<br>由 $L$ 不显含 $t$，能量 $E$ 守恒。"))
    + der(p("<strong>约化为有效一维问题：</strong>由 $p_\\psi=I_3(\\dot\\psi+\\dot\\varphi\\cos\\theta)=L_{z''}$，得 $\\dot\\psi=\\frac{L_{z''}}{I_3}-\\dot\\varphi\\cos\\theta$。代入 $p_\\varphi$ 表达式并解出 $\\dot\\varphi$：")+
    fml("\\dot\\varphi = \\frac{L_z - L_{z''}\\cos\\theta}{I_1\\sin^2\\theta}",
        "将 $\\dot\\varphi$ 和 $\\dot\\psi$ 用守恒量表示后，能量化为仅含 $\\theta,\\dot\\theta$ 的形式：")+
    fml("E = \\frac{1}{2}I_1\\dot\\theta^2 + \\frac{(L_z-L_{z''}\\cos\\theta)^2}{2I_1\\sin^2\\theta} + \\frac{L_{z''}^2}{2I_3} + Mgl\\cos\\theta",
        "定义有效势 $V_{eff}(\\theta)=\\frac{(L_z-L_{z''}\\cos\\theta)^2}{2I_1\\sin^2\\theta}+Mgl\\cos\\theta$，问题约化为 $\\theta$ 的有效一维运动。"))
    + app(p("拉格朗日陀螺的运动表现为进动（$\\varphi$ 变化）、章动（$\\theta$ 周期性变化）和自转（$\\psi$ 变化）的合成，是陀螺仪表和地球进动的理论基础。"))
)},
{"id":"tm-c3s4-6","name":"惯量椭球与潘索描述","tags":["def","thm","der","note"],"brief":"欧拉陀螺运动的几何描述与证明。",
 "body": wrap(
    defn("惯量椭球", p("在主轴坐标系中，由 $I_1x^2+I_2y^2+I_3z^2=1$ 定义的椭球称为惯量椭球。其物理意义：若将椭球面上的点视为角速度 $\\vec\\omega$，则对应能量 $T=\\frac{1}{2}(I_1\\omega_1^2+I_2\\omega_2^2+I_3\\omega_3^2)=\\frac{1}{2}$。惯量椭球与刚体位形一一对应，且形状与刚体形状相似。"))
    + thm("潘索描述", p("自由刚体（$\\vec N=0$）的运动等价于惯量椭球在<strong>固定不变平面</strong>上的无滑动纯滚动。该平面垂直于角动量方向 $\\vec L$，距转动中心 $O$ 的距离为 $d=\\frac{\\sqrt{2E}}{|\\vec L|}$。"))
    + der(p("<strong>潘索定理的证明：</strong>设惯量椭球与角速度方向在某时刻交于点 $P$（$\\overrightarrow{OP}$ 沿瞬时转轴方向），则 $P$ 点的瞬时速度为零（因为 $P$ 在转轴上）。<br><strong>(i) 切平面垂直于 $\\vec L$：</strong>令 $f=I_1x^2+I_2y^2+I_3z^2$，则 $\\nabla f=(2I_1x,2I_2y,2I_3z)$。在 $P$ 点（$\\overrightarrow{OP}=\\vec\\omega/\\sqrt{2E}$），$\\nabla f\\propto(I_1\\omega_1,I_2\\omega_2,I_3\\omega_3)=\\vec L$。故椭球在 $P$ 点的切平面法向平行于 $\\vec L$，即切平面 $\\perp\\vec L$。"))
    + der(p("<strong>(ii) $P$ 到 $O$ 在 $\\vec L$ 方向的投影为常数：</strong>")+
    fml("\\overrightarrow{OP}\\cdot\\frac{\\vec L}{|\\vec L|} = \\frac{\\vec\\omega}{\\sqrt{2E}}\\cdot\\frac{\\vec L}{|\\vec L|} = \\frac{\\vec\\omega\\cdot\\vec L}{\\sqrt{2E}\\,|\\vec L|} = \\frac{2E}{\\sqrt{2E}\\,|\\vec L|} = \\frac{\\sqrt{2E}}{|\\vec L|}",
        "其中利用了 $E=\\frac{1}{2}\\vec\\omega\\cdot\\vec L$。由于 $E$ 和 $\\vec L$ 均为守恒量，此投影距离为常数 $d=\\frac{\\sqrt{2E}}{|\\vec L|}$。"))
    + der(p("<strong>(iii) 纯滚动：</strong>由 (i)(ii) 知切平面垂直于 $\\vec L$ 且距 $O$ 为常数 $d$，故该平面在运动过程中固定不变。又因接触点 $P$ 在转轴上，其瞬时速度为零，故椭球在该固定平面上做无滑动纯滚动。$\\blacksquare$"))
    + note(p("角速度矢量端点在惯量椭球上描出的曲线称为<strong>本体极迹</strong>（polhode），在不变平面上描出的曲线称为<strong>空间极迹</strong>（herpolhode）。本体极迹是封闭曲线，空间极迹通常不封闭。"))
)},
{"id":"tm-c3s4-7","name":"刚体绕主轴转动的稳定性","tags":["thm","der","app","exa"],"brief":"中间轴定理（网球拍定理）及其推导。",
 "body": wrap(
    thm("主轴转动稳定性定理", p("自由刚体绕最大或最小主转动惯量轴的转动是稳定的，绕中间主转动惯量轴的转动是不稳定的。设 $I_1<I_2<I_3$，则绕 $I_1$ 或 $I_3$ 轴的小扰动稳定，绕 $I_2$ 轴不稳定。"))
    + der(p("<strong>推导（线性稳定性分析）：</strong>考虑绕主轴 1 转动，初始角速度 $\\vec\\omega=(\\omega_{10},0,0)$。设小扰动 $\\omega_2,\\omega_3$ 为一阶小量，由欧拉方程（$\\vec N=0$）：")+
    fml("I_1\\dot\\omega_1 + (I_3-I_2)\\omega_2\\omega_3 = 0,\\quad I_2\\dot\\omega_2 + (I_1-I_3)\\omega_3\\omega_1 = 0,\\quad I_3\\dot\\omega_3 + (I_2-I_1)\\omega_1\\omega_2 = 0",
        "对绕轴 1 转动 $\\omega_1\\approx\\omega_{10}$（常数），第二第三式对 $\\omega_2,\\omega_3$ 线性化：")+
    fml("I_2\\dot\\omega_2 = (I_3-I_1)\\omega_{10}\\omega_3,\\qquad I_3\\dot\\omega_3 = -(I_2-I_1)\\omega_{10}\\omega_2",
        "两式消元得 $\\ddot\\omega_2 = -\\Omega_1^2\\omega_2$，其中")+
    fml("\\Omega_1^2 = \\frac{(I_3-I_1)(I_2-I_1)}{I_2 I_3}\\omega_{10}^2",
        "若 $I_1$ 为最小（$I_1<I_2<I_3$），则 $\\Omega_1^2>0$，扰动 $\\omega_2,\\omega_3$ 做简谐振动，绕轴 1 转动<strong>稳定</strong>。<br>同理对绕轴 3（最大惯量），$\\Omega_3^2>0$，转动<strong>稳定</strong>。<br>对绕轴 2（中间惯量），$\\Omega_2^2=\\frac{(I_1-I_2)(I_3-I_2)}{I_1 I_3}\\omega_{20}^2<0$（一个因子正一个负），特征值为实数，扰动指数增长，转动<strong>不稳定</strong>。$\\blacksquare$"))
    + exa(p("<strong>网球拍定理：</strong>抛一网球拍到空中并令其绕长轴或短轴自转，运动稳定；若令其绕中间轴自转，运动剧烈翻转，绕轴方向不可预测。这是中间轴不稳定的直观演示。<br><strong>地球自转：</strong>地球近似扁椭球（$I_1=I_2<I_3$），绕最大惯量轴（自转轴）稳定，因此地球自转方向稳定不变。<br><strong>卫星姿态控制：</strong>卫星设计需使其自转轴为最大惯量轴，以保证姿态稳定。"))
    + app(p("刚体转动的稳定性分析是天体力学（自转稳定）、航天器姿态控制、陀螺仪设计的基础。"))
)},
],
},

# ---- 3.5 电磁场中的拉格朗日函数 (从第一章移入) ----
{
"name": "3.5 电磁场中的拉格朗日函数",
"color": "#be185d",
"desc": "广义势能、洛伦兹力的拉格朗日表述、规范变换",
"items": [
{"id":"tm-c3s5-1","name":"广义势能","tags":["def","thm","der"],"brief":"含速度的势能推广，从洛伦兹力导出。",
 "body": wrap(
    defn("广义势能", p("若存在函数 $U(q,\\dot q,t)$ 使得广义力可写为")+
    fml("Q_\\alpha = -\\frac{\\partial U}{\\partial q_\\alpha} + \\frac{d}{dt}\\frac{\\partial U}{\\partial\\dot q_\\alpha}",
        "则 $U$ 称为广义势能（速度相关势能）。此时拉格朗日函数仍为 $L=T-U$，拉格朗日方程形式不变。"))
    + thm("与保守力的关系", p("当 $U$ 不含 $\\dot q$ 时，$\\frac{\\partial U}{\\partial\\dot q_\\alpha}=0$，广义力退化为 $Q_\\alpha=-\\frac{\\partial U}{\\partial q_\\alpha}$，即保守力情形。"))
    + der(p("<strong>从洛伦兹力导出广义势能：</strong>洛伦兹力 $\\vec F=q(\\vec E+\\vec v\\times\\vec B)$ 显含速度，不能写成通常势能的负梯度。引入标势 $\\phi$ 和矢势 $\\vec A$：")+
    fml("\\vec E = -\\nabla\\phi - \\frac{\\partial\\vec A}{\\partial t},\\qquad \\vec B = \\nabla\\times\\vec A",
        "则洛伦兹力可写为 $\\vec F=q(-\\nabla\\phi-\\frac{\\partial\\vec A}{\\partial t}+\\vec v\\times(\\nabla\\times\\vec A))$。")+
    fml("\\vec v\\times(\\nabla\\times\\vec A) = \\nabla(\\vec v\\cdot\\vec A) - (\\vec v\\cdot\\nabla)\\vec A",
        "（关键恒等式，其中 $\\nabla$ 对空间求导，$\\vec v$ 是独立变量），代入洛伦兹力：")+
    fml("\\vec F = q\\left[-\\nabla\\phi - \\frac{\\partial\\vec A}{\\partial t} + \\nabla(\\vec v\\cdot\\vec A) - (\\vec v\\cdot\\nabla)\\vec A\\right]",
        "注意 $\\nabla\\phi$ 和 $\\nabla(\\vec v\\cdot\\vec A)$ 都是对 $\\vec r$ 求梯度（固定 $\\vec v$），故合并：")+
    fml("\\vec F = q\\left[-\\nabla(\\phi - \\vec v\\cdot\\vec A) - \\frac{\\partial\\vec A}{\\partial t} - (\\vec v\\cdot\\nabla)\\vec A\\right]",
        "而 $\\frac{d\\vec A}{dt}=\\frac{\\partial\\vec A}{\\partial t}+(\\vec v\\cdot\\nabla)\\vec A$（全导数），故 $-\\frac{\\partial\\vec A}{\\partial t}-(\\vec v\\cdot\\nabla)\\vec A=-\\frac{d\\vec A}{dt}$。又 $\\frac{\\partial}{\\partial\\vec v}(\\vec v\\cdot\\vec A)=\\vec A$，$\\frac{d}{dt}\\frac{\\partial}{\\partial\\vec v}(\\vec v\\cdot\\vec A)=\\frac{d\\vec A}{dt}$。重新整理得：")+
    fml("\\vec F = -\\nabla(q\\phi - q\\vec v\\cdot\\vec A) + \\frac{d}{dt}\\frac{\\partial}{\\partial\\vec v}(q\\vec v\\cdot\\vec A)",
        "即 $\\vec F=-\\nabla U+\\frac{d}{dt}\\frac{\\partial U}{\\partial\\vec v}$，其中广义势能为 $U=q\\phi-q\\vec v\\cdot\\vec A$。$\\blacksquare$"))
)},
{"id":"tm-c3s5-2","name":"带电粒子在电磁场中的拉格朗日函数","tags":["def","thm","der","app"],"brief":"洛伦兹力的拉格朗日表述。",
 "body": wrap(
    thm("电磁场的势", p("带电粒子在电磁场中受洛伦兹力 $\\vec F=q(\\vec E+\\vec v\\times\\vec B)$。引入标势 $\\phi$ 和矢势 $\\vec A$：")+
    fml("\\vec E = -\\nabla\\phi - \\frac{\\partial\\vec A}{\\partial t},\\qquad \\vec B = \\nabla\\times\\vec A"))
    + thm("广义势能与拉格朗日函数", p("电磁场的广义势能为")+
    fml("U = q\\phi - q\\vec A\\cdot\\vec v",
        "拉格朗日函数为 $L=\\frac{1}{2}m\\vec v^2 - q\\phi + q\\vec A\\cdot\\vec v$。"))
    + der(p("<strong>验证：</strong>广义动量 $p_i=\\frac{\\partial L}{\\partial v_i}=mv_i+qA_i$。<br>拉格朗日方程 $\\frac{d}{dt}(mv_i+qA_i)-\\frac{\\partial}{\\partial x_i}(-q\\phi+q\\vec A\\cdot\\vec v)=0$。<br>展开：$m\\dot v_i+q\\frac{dA_i}{dt}+q\\frac{\\partial\\phi}{\\partial x_i}-q\\vec v\\cdot\\frac{\\partial\\vec A}{\\partial x_i}=0$。<br>$\\frac{dA_i}{dt}=\\frac{\\partial A_i}{\\partial t}+\\sum_j v_j\\frac{\\partial A_i}{\\partial x_j}$。<br>整理：$m\\dot v_i=-q(\\frac{\\partial\\phi}{\\partial x_i}+\\frac{\\partial A_i}{\\partial t})+q\\sum_j v_j(\\frac{\\partial A_j}{\\partial x_i}-\\frac{\\partial A_i}{\\partial x_j})$。<br>右边第一项 $=qE_i$，第二项 $=q(\\vec v\\times\\vec B)_i$（由 $\\vec B=\\nabla\\times\\vec A$）。<br>故 $m\\dot{\\vec v}=q(\\vec E+\\vec v\\times\\vec B)$，即洛伦兹力方程。"))
    + app(p("该形式在量子力学和场论中有重要应用。正则动量 $\\vec p=m\\vec v+q\\vec A$ 而非机械动量 $m\\vec v$，这在 Aharonov-Bohm 效应中得到验证。"))
)},
{"id":"tm-c3s5-3","name":"规范变换","tags":["def","thm","der"],"brief":"势的变换不改变物理。",
 "body": wrap(
    defn("规范变换", p("电磁场的势可做如下变换而不改变 $\\vec E$ 和 $\\vec B$：")+
    fml("\\vec A \\to \\vec A' = \\vec A + \\nabla\\chi,\\qquad \\phi \\to \\phi' = \\phi - \\frac{\\partial\\chi}{\\partial t}",
        "其中 $\\chi(\\vec r,t)$ 为任意标量函数。这是因为 $\\nabla\\times(\\nabla\\chi)=0$，$\\frac{\\partial}{\\partial t}(\\nabla\\chi)=\\nabla(\\frac{\\partial\\chi}{\\partial t})$。"))
    + thm("拉格朗日函数的规范变换", p("变换后拉格朗日函数变为")+
    fml("L' = \\frac{1}{2}m\\vec v^2 - q\\phi' + q\\vec A'\\cdot\\vec v = L + q\\left(\\frac{\\partial\\chi}{\\partial t}+\\vec v\\cdot\\nabla\\chi\\right) = L + q\\frac{d\\chi}{dt}"))
    + der(p("由于 $\\frac{d\\chi}{dt}=\\frac{\\partial\\chi}{\\partial t}+\\vec v\\cdot\\nabla\\chi$ 是全导数，根据拉格朗日函数的不唯一性，运动方程不变。这表明物理规律与规范选择无关（规范不变性）。"))
)},
],
},

# ---- 3.6 非惯性系与傅科摆 (从第一章移入) ----
{
"name": "3.6 非惯性系与傅科摆",
"color": "#059669",
"desc": "非惯性系、科里奥利力、离心力、傅科摆",
"items": [
{"id":"tm-c3s6-1","name":"非惯性系","tags":["def","thm","app"],"brief":"加速参考系中的惯性力。",
 "body": wrap(
    defn("非惯性系", p("相对惯性系做加速运动的参考系称为非惯性系。在非惯性系中，牛顿第一定律不成立，需引入惯性力才能保持牛顿第二定律的形式。"))
    + thm("加速平动参考系", p("设非惯性系以加速度 $\\vec a$ 相对惯性系平动，则在非惯性系中质点受力为 $\\vec F'=\\vec F-m\\vec a$，其中 $-m\\vec a$ 为平移惯性力。"))
    + app(p("电梯加速上升时人感觉变重（超重），减速时感觉变轻（失重）；汽车刹车时人前倾。"))
)},
{"id":"tm-c3s6-2","name":"转动参考系","tags":["thm","der","app"],"brief":"角速度为ω的转动参考系。",
 "body": wrap(
    thm("转动参考系的加速度关系", p("设转动参考系以角速度 $\\vec\\omega$ 绕定点转动，则惯性系中加速度 $\\vec a$ 与转动系中加速度 $\\vec a'$ 的关系为")+
    fml("\\vec a = \\vec a' + 2\\vec\\omega\\times\\vec v' + \\vec\\omega\\times(\\vec\\omega\\times\\vec r') + \\dot{\\vec\\omega}\\times\\vec r'"))
    + der(p("对任意矢量 $\\vec A$，惯性系与转动系中的时间导数关系为")+
    fml("\\left(\\frac{d\\vec A}{dt}\\right)_{in} = \\left(\\frac{d\\vec A}{dt}\\right)_{rot} + \\vec\\omega\\times\\vec A")
    + p("对位置矢量 $\\vec r$ 应用：$\\vec v_{in}=\\vec v'+\\vec\\omega\\times\\vec r'$。<br>对速度矢量再应用一次：$\\vec a_{in}=(\\frac{d\\vec v'}{dt})_{rot}+\\vec\\omega\\times\\vec v'+\\vec\\omega\\times(\\vec v'+\\vec\\omega\\times\\vec r')+\\dot{\\vec\\omega}\\times\\vec r'$<br>$=\\vec a'+2\\vec\\omega\\times\\vec v'+\\vec\\omega\\times(\\vec\\omega\\times\\vec r')+\\dot{\\vec\\omega}\\times\\vec r'$。"))
    + app(p("由此得两种主要惯性力：<strong>科里奥利力</strong> $\\vec F_C=-2m\\vec\\omega\\times\\vec v'$，<strong>离心力</strong> $\\vec F_{cf}=-m\\vec\\omega\\times(\\vec\\omega\\times\\vec r')$。"))
)},
{"id":"tm-c3s6-3","name":"科里奥利力与离心力","tags":["def","thm","der","app"],"brief":"转动参考系中的两个惯性力及其推导。",
 "body": wrap(
    thm("转动参考系的运动方程", p("在转动参考系中，质点的运动方程为")+
    fml("m\\vec a' = \\vec F_{real} - 2m\\vec\\omega\\times\\vec v' - m\\vec\\omega\\times(\\vec\\omega\\times\\vec r') - m\\dot{\\vec\\omega}\\times\\vec r'",
        "右边第一项为真实力，后三项为惯性力。"))
    + der(p("<strong>推导（从转动系导数关系出发）：</strong>对任意矢量 $\\vec A$，惯性系与转动系中的时间导数关系为 $\\left(\\frac{d\\vec A}{dt}\\right)_{in}=\\left(\\frac{d\\vec A}{dt}\\right)_{rot}+\\vec\\omega\\times\\vec A$。<br><strong>第一次应用</strong>（位置 $\\vec r$）：$\\vec v_{in}=\\vec v'+\\vec\\omega\\times\\vec r'$，即惯性系中的速度 = 转动系中速度 + 牵连速度。<br><strong>第二次应用</strong>（速度 $\\vec v_{in}$）：")+
    fml("\\vec a_{in} = \\left(\\frac{d\\vec v_{in}}{dt}\\right)_{rot} + \\vec\\omega\\times\\vec v_{in} = \\vec a' + \\vec\\omega\\times\\vec v' + \\vec\\omega\\times(\\vec v' + \\vec\\omega\\times\\vec r') + \\dot{\\vec\\omega}\\times\\vec r'",
        "其中 $\\left(\\frac{d\\vec v'}{dt}\\right)_{rot}=\\vec a'$ 为转动系中加速度，$\\vec\\omega\\times\\vec v'$ 出现两次（一次来自对 $\\vec v'$ 的导数变换，一次来自对 $\\vec\\omega\\times\\vec r'$ 的导数变换），合并为 $2\\vec\\omega\\times\\vec v'$。故")+
    fml("\\vec a_{in} = \\vec a' + 2\\vec\\omega\\times\\vec v' + \\vec\\omega\\times(\\vec\\omega\\times\\vec r') + \\dot{\\vec\\omega}\\times\\vec r'",
        "代入 $m\\vec a_{in}=\\vec F_{real}$，移项得 $m\\vec a'=\\vec F_{real}-2m\\vec\\omega\\times\\vec v'-m\\vec\\omega\\times(\\vec\\omega\\times\\vec r')-m\\dot{\\vec\\omega}\\times\\vec r'$。"))
    + defn("科里奥利力", p("$\\vec F_C=-2m\\vec\\omega\\times\\vec v'$，与质点相对速度成正比。<br>由于 $\\vec F_C\\perp\\vec v'$，科里奥利力对运动物体不做功，只改变速度方向不改变大小。"))
    + defn("离心力", p("$\\vec F_{cf}=-m\\vec\\omega\\times(\\vec\\omega\\times\\vec r')$。利用 $\\vec\\omega\\times(\\vec\\omega\\times\\vec r')=\\vec\\omega(\\vec\\omega\\cdot\\vec r')-\\omega^2\\vec r'$，当 $\\vec r'\\perp\\vec\\omega$ 时，$\\vec F_{cf}=m\\omega^2\\vec r'$（沿径向外指）。"))
    + thm("重力的修正", p("地球表面有效重力 $\\vec g$ 是真实引力 $\\vec g_0$ 与离心力的合力：$\\vec g=\\vec g_0-\\vec\\omega\\times(\\vec\\omega\\times\\vec R)$。赤道处离心力最大（$\\omega^2 R$），故赤道重力略小于两极。"))
    + app(p("地球自转导致：北半球河流右岸冲刷严重、气旋逆时针旋转；傅科摆进动；赤道处重力略小于两极；大气环流的形成。"))
)},
{"id":"tm-c3s6-4","name":"傅科摆","tags":["exa","der","app"],"brief":"验证地球自转的经典实验。",
 "body": wrap(
    exa(p("傅科摆是验证地球自转的著名实验（傅科于 1851 年在巴黎先贤祠演示）。长摆悬挂于北半球纬度 $\\lambda$ 处，由于科里奥利力，摆的振动面会缓慢旋转。"))
    + der(p("设摆长 $l\\gg$ 振幅，摆锤在水平面内运动，坐标 $(x,y)$。科里奥利力的水平分量为 $\\vec F_C=-2m\\vec\\omega\\times\\vec v$，其中 $\\vec\\omega$ 的竖直分量为 $\\omega\\sin\\lambda$。<br>水平方向运动方程：")+
    fml("\\ddot x = -\\frac{g}{l}x + 2\\omega\\sin\\lambda\\,\\dot y,\\qquad \\ddot y = -\\frac{g}{l}y - 2\\omega\\sin\\lambda\\,\\dot x")
    + p("令复变量 $z=x+iy$，方程化为 $\\ddot z+\\omega_0^2 z+2i\\Omega\\dot z=0$，其中 $\\omega_0=\\sqrt{g/l}$，$\\Omega=\\omega\\sin\\lambda$。<br>设解 $z=Ae^{-i\\Omega t}e^{\\pm i\\sqrt{\\omega_0^2+\\Omega^2}t}$。由于 $\\Omega\\ll\\omega_0$，近似为 $z=(Ae^{i\\omega_0 t}+Be^{-i\\omega_0 t})e^{-i\\Omega t}$。<br>这表示摆动面以角速度 $\\Omega=\\omega\\sin\\lambda$ 绕竖直轴旋转：")+
    fml("\\Omega = \\omega\\sin\\lambda",
        "北半球从上往下看为顺时针，南半球为逆时针。"))
    + app(p("在巴黎（$\\lambda\\approx49^\\circ$），傅科摆约 32 小时转一圈；在北极（$\\lambda=90^\\circ$），周期为 24 小时；在赤道（$\\lambda=0$），不进动。"))
)},
{"id":"tm-c3s6-5","name":"落体偏东效应","tags":["exa","der","app"],"brief":"自由落体向东偏转，地球自转的实证。",
 "body": wrap(
    exa(p("在地球表面（纬度 $\\lambda$）从高 $h$ 处释放物体，物体落地时不正对正下方，而偏东一小段距离。这是科里奥利力的直接可观测效应之一。"))
    + der(p("取当地坐标系：$x$ 向东、$y$ 向南、$z$ 向上。地球自转角速度 $\\vec\\omega=(0,\\omega\\cos\\lambda,\\omega\\sin\\lambda)$。自由落体初速 $\\vec v=(0,0,-gt)$，故科里奥利加速度为")+
    fml("\\vec a_C = -2\\vec\\omega\\times\\vec v = (2\\omega g t\\cos\\lambda,\\,0,\\,0)",
        "只考虑水平方向 $x$，物体从静止落下，$t$ 时刻东向加速度为 $2\\omega g t\\cos\\lambda$。<br>积分一次（初速为 0）：东向速度 $v_x=\\omega g t^2\\cos\\lambda$。<br>再积分：东向位移")+
    fml("x(t) = \\frac{1}{3}\\omega g t^3\\cos\\lambda",
        "落地时间 $t=\\sqrt{2h/g}$，故偏东距离为")+
    fml("\\Delta x = \\frac{1}{3}\\omega g\\cos\\lambda\\left(\\frac{2h}{g}\\right)^{3/2} = \\frac{2\\sqrt{2}}{3}\\omega\\cos\\lambda\\,\\frac{h^{3/2}}{\\sqrt{g}}",
        "注意：上述为最低阶近似。高阶项还包含向南的偏转（$\\sim\\omega^2$）和向东修正（$\\sim\\omega^3$）。"))
    + app(p("<strong>数值：</strong>赤道处从 $h=100$ 米下落，$\\Delta x\\approx 2.2$ cm。1803 年德国汉堡实验（$h=76$ m）首次观测到偏东 $9$ mm，与理论一致。"))
    + note(p('落体偏东的物理原因：高处物体随地球自转的线速度大于地面处，因此下落时由于惯性保持较大的东向速度，落到地面时已超前于正下方。这与"地球静止不动，物体受东向力"的解释等价。'))
)},
{"id":"tm-c3s6-6","name":"潮汐力","tags":["def","thm","der","app"],"brief":"引潮力的非惯性系解释与潮汐成因。",
 "body": wrap(
    defn("潮汐力", p("在天体力学中，由于引力场在空间各点的不均匀性引起的变形力称为潮汐力（引潮力）。在地球-月球系统中，地球表面的海水在月球引力与地心处引力的差作用下产生潮汐。"))
    + thm("引潮力公式", p("取地球-月球连线为 $x$ 轴，地心为原点，月球位于 $(D,0,0)$。地球内一点 $\\vec r=(x,y,z)$ 处月球引力为 $\\vec F_g=-\\frac{Gm_1 M(\\vec r-\\vec D)}{|\\vec r-\\vec D|^3}$（$\\vec D=(D,0,0)$）。在随地球质心加速的平动非惯性系中，需加上惯性力 $-m_1\\vec a_{cm}=m_1\\frac{GM\\vec D}{D^3}$。"))
    + der(p("<strong>推导（一阶近似）：</strong>地心处月球的引力为 $\\vec F_0=-\\frac{Gm_1 M}{D^2}\\hat x$，对应加速度 $\\vec a_{cm}=-\\frac{GM}{D^2}\\hat x$。在非惯性系中，单位质量海水受月球引力与惯性力之差（引潮力）为")+
    fml("\\vec f_{tide} = -\\frac{GM(\\vec r-\\vec D)}{|\\vec r-\\vec D|^3} + \\frac{GM\\vec D}{D^3}",
        "在 $r\\ll D$ 近似下展开，利用 $|\\vec r-\\vec D|^{-3}\\approx D^{-3}(1+3x/D)$，保留一阶：")+
    fml("\\vec f_{tide} \\approx \\frac{GM}{D^3}\\,(2x,\\,-y,\\,-z)",
        "可见：在 $x$ 方向（地月连线方向）引潮力为正且加倍，将海水拉离地球（涨潮）；在垂直方向 $y,z$ 引潮力为负且减半，将海水压向地球（落潮）。"))
    + der(p("<strong>潮汐隆起的物理解释：</strong>在朝月侧，月球引力比地心处强（更靠近月球），海水被拉离地心；在背月侧，月球引力比地心处弱，地心-背月侧海水相对地心被甩出。两侧同时涨潮，地球自转使各地一日两次涨潮。"))
    + app(p("<strong>太阳潮汐：</strong>太阳引潮力约为月球的一半（$\\frac{M_\\odot}{D_\\odot^3}/\\frac{M_M}{D_M^3}\\approx 0.46$），故朔望日大潮（日月合力），上下弦小潮。<br><strong>潮汐锁定：</strong>月球由于地球潮汐力矩的作用已锁定自转周期与公转周期一致（一面永远朝向地球）。<br><strong>潮汐耗散：</strong>地球潮汐摩擦使地球自转减慢（日长每世纪增加约 1.7 ms），地月距离增大。"))
)},
],
},
]

print(f"Ch3: {sum(len(s['items']) for s in ch3_sections)} items")

# =====================================================
#  ASSEMBLE CHAPTERS & GENERATE HTML
# =====================================================
CHAPTERS = [
    {"id":"tm-ch1","num":"第一章","title":"拉格朗日力学","en":"LAGRANGIAN MECHANICS",
     "desc":"从约束与广义坐标出发，经达朗贝尔方程到欧拉-拉格朗日方程，再以变分法与最小作用量原理重构力学，最后讨论诺特定理。",
     "sections": ch1_sections},
    {"id":"tm-ch2","num":"第二章","title":"哈密顿力学","en":"HAMILTONIAN MECHANICS",
     "desc":"通过勒让德变换从拉格朗日力学过渡到哈密顿力学，研究正则方程、泊松括号、正则变换与母函数、哈密顿-雅科比方程，以及无穷小变换与诺特定理。",
     "sections": ch2_sections},
    {"id":"tm-ch3","num":"第三章","title":"力学经典问题","en":"CLASSICAL PROBLEMS",
     "desc":"应用拉格朗日与哈密顿力学求解经典问题：微振动与简正坐标、中心势场中的开普勒问题、刚体运动学与动力学、电磁场中的拉格朗日函数、非惯性系与傅科摆。",
     "sections": ch3_sections},
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
                item_strs.append(
                    f"{{id:'{it['id']}',name:{json.dumps(it['name'],ensure_ascii=False)},"
                    f"tags:{tags_js},brief:{json.dumps(fix_lt_text(it['brief']),ensure_ascii=False)},"
                    f"body:`{body_esc}`}}"
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
  .la-nav-tab.c4{color:#c2410c;border-color:#fed7aa}
  .la-nav-tab.c5{color:#6d28d9;border-color:#ddd6fe}
  .la-nav-tab.c6{color:#be185d;border-color:#fbcfe8}
  .la-toolbar{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:16px 0 8px}
  button{border:1px solid #d5deea;background:#fff;color:var(--la-ink);border-radius:999px;padding:9px 14px;font:inherit;cursor:pointer;transition:.2s ease}
  button:hover{transform:translateY(-1px);box-shadow:0 8px 20px rgba(20,36,60,.08)}
  .la-engagement-bar{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:10px 0 0}
  .la-stat-item{display:inline-flex;align-items:center;gap:6px;padding:9px 18px;background:#fff;border:1px solid #d5deea;border-radius:999px;font-size:14px;font-weight:600;color:#475569}
  .la-stat-value{color:#2563eb;font-weight:800}
  .la-stat-link{cursor:pointer;text-decoration:none;color:#475569;transition:.2s ease}
  .la-stat-link:hover{background:#eef2ff;border-color:#c7d2fe;transform:translateY(-1px);box-shadow:0 8px 20px rgba(20,36,60,.08)}
  .la-stat-link:hover .la-stat-value{color:#4f46e5}
  .la-legend{margin:26px auto 0;max-width:1100px;background:rgba(255,255,255,.8);border:1px solid #dde5ef;border-radius:20px;padding:16px 22px;display:flex;gap:14px;flex-wrap:wrap;justify-content:center;box-shadow:var(--la-shadow)}
  .la-legend-title{font-size:12px;font-weight:800;letter-spacing:.16em;color:#94a3b8;align-self:center;margin-right:6px}
  .la-arc-badge{display:inline-flex;align-items:center;font-size:10px;font-weight:800;padding:3px 8px;border-radius:6px;letter-spacing:.03em;white-space:nowrap}
  .la-arc-def{background:#dbeafe;color:#1e40af}
  .la-arc-thm{background:#d1fae5;color:#065f46}
  .la-arc-der{background:#ede9fe;color:#5b21b6}
  .la-arc-exa{background:#cffafe;color:#155e75}
  .la-arc-app{background:#ffedd5;color:#9a3412}
  .la-arc-his{background:#f1f5f9;color:#475569}
  .la-arc-note{background:#fee2e2;color:#b91c1c}
  .la-roadmap{margin-top:30px;background:rgba(255,255,255,.74);border:1px solid rgba(189,201,218,.7);box-shadow:var(--la-shadow);border-radius:28px;padding:34px}
  .la-phase-title{font-size:24px;font-weight:800;margin:60px 0 4px;display:flex;align-items:center;gap:12px;color:#1e293b;letter-spacing:-.01em}
  .la-phase-title:first-child{margin-top:0}
  .la-phase-title::before{content:"";display:block;width:6px;height:30px;border-radius:4px;background:#2563eb;flex-shrink:0}
  .la-phase-title.la-ch1::before{background:#2563eb}
  .la-phase-title.la-ch2::before{background:#0d9488}
  .la-phase-title.la-ch3::before{background:#059669}
  .la-phase-title.la-ch4::before{background:#c2410c}
  .la-phase-title.la-ch5::before{background:#7c3aed}
  .la-phase-title.la-ch6::before{background:#be185d}
  .la-phase-en{font-size:11px;letter-spacing:.36em;color:#94a3b8;font-weight:700;text-transform:uppercase;margin:0 0 12px 18px;font-style:italic}
  .la-phase-desc{color:var(--la-muted);font-size:14px;margin:0 0 24px 18px;line-height:1.8;max-width:960px}
  .la-domain{margin-bottom:26px;padding:16px 18px 18px 22px;position:relative;background:rgba(255,255,255,.6);border-radius:18px;border:1px solid #e5ebf2}
  .la-domain::before{content:"";position:absolute;left:6px;top:16px;bottom:16px;width:5px;border-radius:5px;background:var(--domain-color,#2563eb);box-shadow:0 0 12px rgba(37,99,235,.25)}
  .la-domain-header{display:flex;align-items:center;gap:10px;margin-bottom:14px;padding-left:6px;flex-wrap:wrap}
  .la-domain-header h3{margin:0;font-size:18px;color:#1e293b}
  .la-domain-count{font-size:11px;padding:3px 10px;border-radius:999px;background:#f1f5f9;color:#64748b;font-weight:600}
  .la-domain-desc{font-size:12px;color:#94a3b8;margin-left:auto;font-style:italic}
  .la-domain-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}
  .la-course-card{background:#fff;border:1px solid #dbe3ee;border-radius:14px;padding:14px;cursor:pointer;transition:.25s;position:relative;overflow:hidden}
  .la-course-card:hover{transform:translateY(-3px);box-shadow:0 10px 20px rgba(25,44,75,.1);border-color:#aabbd0}
  .la-course-card h4{margin:0 0 8px;font-size:14.5px;line-height:1.35;color:#1e293b}
  .la-course-card p{margin:0;font-size:11.5px;color:var(--la-muted);line-height:1.6}
  .la-arc-badges{display:flex;flex-wrap:wrap;gap:3px;margin-bottom:8px}
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
  .la-fml{margin:16px 0;padding:14px 18px;background:linear-gradient(135deg,#f8fafc,#eef4fb);border-left:4px solid #93b4e8;border-radius:10px;overflow-x:auto;font-size:16px}
  .la-fml .note{display:block;font-size:12.5px;color:#8496ad;margin-top:8px;line-height:1.6;font-family:system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
  .la-fml mjx-container[display="true"]{margin:0 !important}
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
  .la-kp-ext{border-left:3px solid #ec4899;background:#fdf2f8}
  .la-kp-sec p:last-child{margin-bottom:0}
  .la-modal-close{margin-top:22px;background:#0f172a;color:white;border-color:#0f172a;padding:10px 20px;font-weight:bold}
  .la-footer{padding:34px 0 50px;color:var(--la-muted);text-align:center;font-size:13px;line-height:1.9}
  .la-core-fmls{{margin:40px 0 20px;padding:28px 24px;background:linear-gradient(135deg,#f0f4ff,#faf7ff);border:1px solid #e0e7ff;border-radius:18px}}
  .la-core-fmls h3{{font-size:18px;color:#1e293b;margin:0 0 20px;text-align:center;letter-spacing:.04em}}
  .la-core-fmls h3 .la-core-count{{display:inline-block;background:#6366f1;color:#fff;font-size:13px;padding:2px 10px;border-radius:20px;margin-left:8px;vertical-align:middle}}
  .la-core-item{{display:flex;gap:12px;margin:0 0 14px;padding:12px 16px;background:#fff;border-radius:12px;border-left:3px solid #6366f1;align-items:flex-start}}
  .la-core-num{{flex-shrink:0;width:26px;height:26px;border-radius:50%;background:#6366f1;color:#fff;font-size:13px;display:flex;align-items:center;justify-content:center;font-weight:bold}}
  .la-core-body{{flex:1;min-width:0}}
  .la-core-body .la-core-name{{font-size:14px;font-weight:600;color:#1e293b;margin-bottom:4px}}
  .la-core-body .la-fml{{margin:6px 0 0;padding:8px 14px;font-size:15px}}
  .la-back-top{{display:inline-block;margin-top:20px;padding:10px 28px;background:#1e293b;color:#fff;border:none;border-radius:25px;font-size:14px;cursor:pointer;letter-spacing:.04em;transition:background .2s}}
  .la-back-top:hover{{background:#334155}}
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
<meta name="description" content="理论力学知识体系：拉格朗日力学、哈密顿力学、力学经典问题">
<title>理论力学 · 知识体系</title>
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
    <div class="la-eyebrow">THEORETICAL MECHANICS · KNOWLEDGE MAP</div>
    <h1>理论力学 · 知识体系</h1>
    <p class="la-subtitle">拉格朗日力学 · 哈密顿力学 · 力学经典问题</p>
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
    <div>理论力学 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于南开大学物理学院理论力学讲义整理</div>
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
    with open("/workspace/theoretical-mechanics.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated theoretical-mechanics.html ({len(html)} chars)")
