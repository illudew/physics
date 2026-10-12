# -*- coding: utf-8 -*-
"""Generate calculus.html with 8 chapters: 一元微分/微分定理/一元积分/微分方程/多元微分/重积分/积分定理/无穷级数."""
import json

# ---------- SVG figure library ----------
FIG = {
"limit": '''<svg viewBox="0 0 220 140" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="120" x2="200" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="120" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M30 110 Q 110 30 190 60" fill="none" stroke="#3b82f6" stroke-width="2"/>
<line x1="110" y1="30" x2="110" y2="120" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="4 3"/>
<circle cx="110" cy="55" r="4" fill="#ef4444"/>
<text x="115" y="50" font-size="11" fill="#ef4444">L</text>
<text x="108" y="135" font-size="11" fill="#475569">a</text></svg>''',
"derivative": '''<svg viewBox="0 0 220 160" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="140" x2="200" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="140" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M30 130 Q 100 40 190 90" fill="none" stroke="#3b82f6" stroke-width="2"/>
<circle cx="100" cy="75" r="4" fill="#ef4444"/>
<line x1="50" y1="120" x2="170" y2="30" stroke="#10b981" stroke-width="2"/>
<text x="105" y="70" font-size="11" fill="#ef4444">P</text>
<text x="160" y="26" font-size="10" fill="#10b981">切线</text></svg>''',
"integral": '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="200" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M30 120 Q 110 30 190 100" fill="none" stroke="#3b82f6" stroke-width="2"/>
<path d="M50 130 L50 108 L90 90 L90 130 Z" fill="#dbeafe" opacity="0.7"/>
<path d="M90 130 L90 90 L130 70 L130 130 Z" fill="#bfdbfe" opacity="0.7"/>
<path d="M130 130 L130 70 L170 85 L170 130 Z" fill="#93c5fd" opacity="0.7"/>
<text x="205" y="134" font-size="11" fill="#475569">x</text></svg>''',
"taylor": '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="200" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M30 120 Q 110 20 190 110" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
<path d="M40 115 L100 40 L160 50" fill="none" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="5 3"/>
<path d="M50 122 Q 110 55 180 80" fill="none" stroke="#10b981" stroke-width="1.8" stroke-dasharray="4 2"/>
<text x="155" y="48" font-size="10" fill="#ef4444">n=1</text>
<text x="165" y="78" font-size="10" fill="#10b981">n=3</text></svg>''',
"series": '''<svg viewBox="0 0 220 140" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="120" x2="200" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="120" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<rect x="30" y="100" width="22" height="20" fill="#dbeafe" stroke="#3b82f6"/>
<rect x="52" y="80" width="22" height="40" fill="#bfdbfe" stroke="#3b82f6"/>
<rect x="74" y="65" width="22" height="55" fill="#93c5fd" stroke="#3b82f6"/>
<rect x="96" y="55" width="22" height="65" fill="#60a5fa" stroke="#3b82f6"/>
<rect x="118" y="48" width="22" height="72" fill="#3b82f6" stroke="#2563eb"/>
<rect x="140" y="43" width="22" height="77" fill="#2563eb" stroke="#1d4ed8"/>
<path d="M30 100 Q 100 50 190 40" fill="none" stroke="#ef4444" stroke-width="2"/>
<text x="195" y="42" font-size="10" fill="#ef4444">S_n</text></svg>''',
"multivar": '''<svg viewBox="0 0 200 160" xmlns="http://www.w3.org/2000/svg">
<line x1="100" y1="20" x2="100" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="140" x2="180" y2="140" stroke="#94a3b8" stroke-width="1.5"/>
<ellipse cx="100" cy="90" rx="60" ry="35" fill="#dbeafe" stroke="#3b82f6" stroke-width="2" opacity="0.6"/>
<ellipse cx="100" cy="80" rx="50" ry="28" fill="none" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4 3"/>
<circle cx="100" cy="90" r="4" fill="#ef4444"/>
<text x="106" y="88" font-size="11" fill="#ef4444">(x₀,y₀)</text></svg>''',
"green": '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
<path d="M50 120 Q 30 60 110 50 Q 190 40 170 110 Q 160 130 50 120 Z" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
<path d="M50 120 Q 30 60 110 50" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="5 3"/>
<text x="100" y="90" font-size="14" fill="#1e293b">D</text>
<text x="120" y="60" font-size="11" fill="#ef4444">∂D</text></svg>''',
"gradient": '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="200" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M40 110 Q 100 60 180 90" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="4 3"/>
<path d="M40 95 Q 100 45 180 75" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="4 3"/>
<path d="M40 80 Q 100 30 180 60" fill="none" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="4 3"/>
<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#ef4444"/></marker></defs>
<line x1="100" y1="80" x2="140" y2="40" stroke="#ef4444" stroke-width="2.5" marker-end="url(#arr)"/>
<circle cx="100" cy="80" r="3.5" fill="#ef4444"/>
<text x="145" y="38" font-size="11" fill="#ef4444">∇f</text>
<text x="60" y="124" font-size="10" fill="#3b82f6">等值线</text></svg>''',
"riemann": '''<svg viewBox="0 0 220 130" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="110" x2="200" y2="110" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="110" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<path d="M30 100 Q 80 30 140 50 Q 180 60 195 45" fill="none" stroke="#3b82f6" stroke-width="2"/>
<rect x="30" y="80" width="15" height="30" fill="#dbeafe" stroke="#93c5fd"/>
<rect x="45" y="58" width="15" height="52" fill="#bfdbfe" stroke="#93c5fd"/>
<rect x="60" y="40" width="15" height="70" fill="#93c5fd" stroke="#93c5fd"/>
<rect x="75" y="33" width="15" height="77" fill="#60a5fa" stroke="#93c5fd"/>
<rect x="90" y="42" width="15" height="68" fill="#93c5fd" stroke="#93c5fd"/>
<rect x="105" y="52" width="15" height="58" fill="#bfdbfe" stroke="#93c5fd"/>
<rect x="120" y="48" width="15" height="62" fill="#93c5fd" stroke="#93c5fd"/>
<text x="75" y="28" font-size="11" fill="#ef4444">f(ξ_i)</text>
<text x="55" y="124" font-size="10" fill="#475569">Δx_i</text></svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

# ---------- 核心公式清单 ----------
CORE_FORMULAS = [
    ("导数定义", "f'(x) = \\lim_{\\Delta x\\to 0}\\frac{f(x+\\Delta x)-f(x)}{\\Delta x}", "瞬时变化率的严格定义"),
    ("微分", "df = f'(x)\\,dx", "函数增量的线性主部"),
    ("链式法则", "\\frac{dy}{dx} = \\frac{dy}{du}\\cdot\\frac{du}{dx}", "复合函数求导的核心"),
    ("拉格朗日中值定理", "f(b)-f(a) = f'(\\xi)(b-a),\\quad \\xi\\in(a,b)", "导数与函数增量的桥梁"),
    ("泰勒公式", "f(x) = \\sum_{k=0}^{n}\\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k + R_n(x)", "用多项式逼近函数"),
    ("牛顿-莱布尼茨公式", "\\int_a^b f(x)\\,dx = F(b)-F(a)", "微分与积分的统一"),
    ("分部积分", "\\int u\\,dv = uv - \\int v\\,du", "积分的核心技巧之一"),
    ("格林公式", "\\oint_{\\partial D} P\\,dx+Q\\,dy = \\iint_D\\left(\\frac{\\partial Q}{\\partial x}-\\frac{\\partial P}{\\partial y}\\right)d\\sigma", "平面曲线积分与二重积分的转化"),
    ("高斯公式", "\\mathop{\\oint\\!\\!\\!\\!\\!\\int}_{\\partial\\Omega}\\vec F\\cdot d\\vec S = \\iiint_\\Omega \\nabla\\cdot\\vec F\\,dV", "通量与散度的体积分"),
    ("斯托克斯公式", "\\oint_{\\partial\\Sigma}\\vec F\\cdot d\\vec r = \\iint_\\Sigma (\\nabla\\times\\vec F)\\cdot d\\vec S", "环量与旋度的面积分"),
    ("傅里叶系数", "a_n = \\frac{1}{\\pi}\\int_{-\\pi}^{\\pi}f(x)\\cos nx\\,dx,\\; b_n = \\frac{1}{\\pi}\\int_{-\\pi}^{\\pi}f(x)\\sin nx\\,dx", "函数的三角级数展开（余弦+正弦系数）"),
    ("欧拉积分（Γ函数）", "\\Gamma(s) = \\int_0^{+\\infty} x^{s-1}e^{-x}\\,dx", "阶乘的解析延拓"),
    ("拉格朗日乘数法", "\\nabla f = \\lambda\\nabla g", "条件极值的必要条件"),
    ("二阶常系数齐次方程解", "y''+py'+qy=0 \\Rightarrow \\text{由特征方程 } r^2+pr+q=0 \\text{ 决定}", "常微分方程基础解法"),
    ("全微分条件", "\\frac{\\partial P}{\\partial y} = \\frac{\\partial Q}{\\partial x} \\Leftrightarrow P\\,dx+Q\\,dy \\text{ 为全微分}", "曲线积分与路径无关的判据"),
    ("幂级数收敛半径", "R = \\lim_{n\\to\\infty}\\left|\\frac{a_n}{a_{n+1}}\\right|", "幂级数收敛域的确定"),
    ("旋转体体积（圆盘法）", "V = \\pi\\int_a^b f^2(x)\\,dx", "曲线绕 x 轴旋转的体积"),
    ("曲面面积", "S = \\iint_D\\sqrt{1+z_x^2+z_y^2}\\,d\\sigma", "曲面 z=z(x,y) 的面积"),
    ("曲线弧长", "s = \\int_a^b\\sqrt{1+y'^2}\\,dx", "平面曲线的长度"),
    ("极限的 ε-δ 定义", "\\lim_{x\\to x_0}f(x)=A \\Leftrightarrow \\forall\\varepsilon>0,\\exists\\delta>0,\\,0<|x-x_0|<\\delta\\Rightarrow|f(x)-A|<\\varepsilon", "函数极限的严格定义"),
    ("两个重要极限", "\\lim_{x\\to 0}\\frac{\\sin x}{x}=1,\\quad \\lim_{x\\to\\infty}\\left(1+\\frac{1}{x}\\right)^x=e", "微积分中最基础的两个极限"),
    ("莱布尼茨公式", "(uv)^{(n)} = \\sum_{k=0}^{n}\\binom{n}{k}u^{(n-k)}v^{(k)}", "两个函数乘积的高阶导数"),
    ("柯西中值定理", "\\frac{f(b)-f(a)}{g(b)-g(a)} = \\frac{f'(\\xi)}{g'(\\xi)},\\quad \\xi\\in(a,b)", "拉格朗日中值定理的推广"),
    ("洛必达法则", "\\lim\\frac{f(x)}{g(x)} = \\lim\\frac{f'(x)}{g'(x)}", "0/0 或 ∞/∞ 型不定式极限"),
    ("第二换元积分法", "\\int f(x)\\,dx = \\int f(\\psi(t))\\psi'(t)\\,dt,\\quad x=\\psi(t)", "含根式积分的常用代换"),
    ("参数方程求导", "\\frac{dy}{dx} = \\frac{\\psi'(t)}{\\varphi'(t)},\\quad x=\\varphi(t),y=\\psi(t)", "参数方程表示的曲线的切线斜率"),
    ("方向导数", "\\frac{\\partial f}{\\partial l} = \\nabla f\\cdot\\vec l^0 = |\\nabla f|\\cos\\theta", "沿方向 l 的变化率，梯度方向最大"),
    ("梯度", "\\nabla f = (f_x,f_y,f_z),\\quad \\frac{\\partial f}{\\partial l}\\bigg|_{\\max}=|\\nabla f|", "函数增长最快的方向与速率"),
    ("二重积分换元法", "\\iint_D f(x,y)\\,d\\sigma = \\iint_{D'} f(x(u,v),y(u,v))\\,|J|\\,du\\,dv", "雅可比行列式 |J| 为面积伸缩系数"),
    ("球坐标体积元素", "dV = r^2\\sin\\varphi\\,dr\\,d\\varphi\\,d\\theta", "球坐标系下的体积元素"),
    ("曲率", "\\kappa = \\frac{|y''|}{(1+y'^2)^{3/2}}", "曲线弯曲程度的度量"),
    ("一般斯托克斯定理", "\\int_{\\partial M} \\omega = \\int_M d\\omega", "边界积分等于内部外微分的积分（统一形式）"),
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
#  CHAPTER 1: 一元微分
# =====================================================
ch1_sections = [
# ---- 1.1 极限与连续 ----
{
"name": "1.1 极限与连续",
"color": "#2563eb",
"desc": "数列极限、函数极限、无穷小与连续函数",
"items": [
{"id":"c1s1-1","name":"数列极限","tags":["def","thm","exa"],"brief":"ε-N 语言的严格定义。",
 "body": wrap(
    defn("数列极限", p("设 $\\{x_n\\}$ 为数列，$a$ 为常数。若对任意 $\\varepsilon>0$，存在正整数 $N$，使得当 $n>N$ 时恒有 $|x_n-a|<\\varepsilon$，则称 $a$ 为数列 $\\{x_n\\}$ 的极限，记作 $\\lim_{n\\to\\infty}x_n=a$。"))
    + thm("收敛数列的性质", p("(1) 唯一性：收敛数列极限唯一；(2) 有界性：收敛数列必有界；(3) 保号性：若 $\\lim x_n=a>0$，则存在 $N$，当 $n>N$ 时 $x_n>0$；(4) 子列收敛性：收敛数列的任何子列收敛于同一极限。"))
    + exa(p("<strong>证明 $\\lim_{n\\to\\infty}\\frac{1}{n}=0$：</strong>对任意 $\\varepsilon>0$，取 $N=\\lfloor 1/\\varepsilon\\rfloor+1$，则当 $n>N$ 时 $|1/n-0|=1/n<1/N<\\varepsilon$，故极限为 0。"))
)},
{"id":"c1s1-2","name":"函数极限","tags":["def","thm","der","note"],"brief":"ε-δ 语言与左右极限。",
 "body": wrap(
    defn("函数极限", p("设 $f(x)$ 在 $x_0$ 的某去心邻域内有定义，$A$ 为常数。若对任意 $\\varepsilon>0$，存在 $\\delta>0$，使得当 $0<|x-x_0|<\\delta$ 时恒有 $|f(x)-A|<\\varepsilon$，则称 $A$ 为 $f(x)$ 当 $x\\to x_0$ 时的极限，记作 $\\lim_{x\\to x_0}f(x)=A$。"))
    + thm("极限存在准则", p("<strong>夹逼准则：</strong>若在 $x_0$ 的某去心邻域内 $g(x)\\le f(x)\\le h(x)$，且 $\\lim g(x)=\\lim h(x)=A$，则 $\\lim f(x)=A$。<br><strong>单调有界准则：</strong>单调有界数列必有极限。"))
    + der(p("<strong>第一重要极限 $\\lim_{x\\to 0}\\frac{\\sin x}{x}=1$ 的证明：</strong>当 $0<x<\\pi/2$ 时，由几何关系 $\\sin x<x<\\tan x$，得 $\\cos x<\\frac{\\sin x}{x}<1$。又 $\\lim_{x\\to 0}\\cos x=1$，由夹逼准则即得。"))
    + note(p("函数极限 $\\lim_{x\\to x_0}f(x)$ 存在 $\\Leftrightarrow$ 左右极限都存在且相等：$\\lim_{x\\to x_0^-}f(x)=\\lim_{x\\to x_0^+}f(x)$。"))
)},
{"id":"c1s1-3","name":"无穷小与无穷大","tags":["def","thm","app"],"brief":"阶的比较与等价无穷小替换。",
 "body": wrap(
    defn("无穷小的阶", p("设 $\\alpha,\\beta$ 是同一极限过程中的无穷小。若 $\\lim\\frac{\\beta}{\\alpha}=0$，称 $\\beta$ 是 $\\alpha$ 的高阶无穷小（$\\beta=o(\\alpha)$）；若极限为非零常数，称同阶；若极限为 1，称等价（$\\beta\\sim\\alpha$）。"))
    + thm("等价无穷小替换定理", p("在乘除运算中，等价无穷小可互相替换。设 $\\alpha\\sim\\alpha'$，$\\beta\\sim\\beta'$，则 $\\lim\\frac{\\beta}{\\alpha}=\\lim\\frac{\\beta'}{\\alpha'}$。<br><strong>注意：</strong>加减运算中一般不能随意替换。"))
    + app(p("常用等价无穷小（$x\\to 0$）：$\\sin x\\sim x$，$\\tan x\\sim x$，$\\arcsin x\\sim x$，$\\arctan x\\sim x$，$1-\\cos x\\sim\\frac{x^2}{2}$，$e^x-1\\sim x$，$\\ln(1+x)\\sim x$，$(1+x)^\\alpha-1\\sim\\alpha x$。"))
)},
{"id":"c1s1-4","name":"连续函数","tags":["def","thm","app"],"brief":"连续定义、间断点分类、闭区间连续函数性质。",
 "body": wrap(
    defn("连续", p("函数 $f(x)$ 在 $x_0$ 连续 $\\Leftrightarrow$ $\\lim_{x\\to x_0}f(x)=f(x_0)$。等价地，$\\lim_{\\Delta x\\to 0}\\Delta y=0$。若 $f$ 在区间内每点连续，则称 $f$ 在该区间连续。"))
    + defn("间断点分类", p("<strong>第一类间断点：</strong>左右极限都存在。可去间断点（左右极限相等但不等于函数值或函数无定义）、跳跃间断点（左右极限不相等）。<br><strong>第二类间断点：</strong>左右极限至少有一个不存在，如无穷间断点、振荡间断点。"))
    + thm("闭区间连续函数的性质", p("设 $f$ 在 $[a,b]$ 连续：(1) <strong>有界性定理：</strong>$f$ 在 $[a,b]$ 有界；(2) <strong>最值定理：</strong>$f$ 取到最大值和最小值；(3) <strong>零点定理：</strong>若 $f(a)f(b)<0$，则存在 $\\xi\\in(a,b)$ 使 $f(\\xi)=0$；(4) <strong>介值定理：</strong>$f$ 可取到 $f(a)$ 与 $f(b)$ 之间的一切值。"))
)},
]
},
# ---- 1.2 导数与微分 ----
{
"name": "1.2 导数与微分",
"color": "#3b82f6",
"desc": "导数定义、几何意义、微分定义与可微条件",
"items": [
{"id":"c1s2-1","name":"导数的定义","tags":["def","thm","der","exa"],"brief":"瞬时变化率与切线斜率。",
 "body": wrap(
    defn("导数", p("函数 $y=f(x)$ 在 $x_0$ 处的导数定义为")+
    fml("f'(x_0) = \\lim_{\\Delta x\\to 0}\\frac{f(x_0+\\Delta x)-f(x_0)}{\\Delta x} = \\lim_{x\\to x_0}\\frac{f(x)-f(x_0)}{x-x_0}",
        "若极限存在，称 $f$ 在 $x_0$ 可导。导数的几何意义是曲线 $y=f(x)$ 在 $(x_0,f(x_0))$ 处切线的斜率。"))
    + der(p("<strong>可导与连续的关系：</strong>若 $f$ 在 $x_0$ 可导，则 $f$ 在 $x_0$ 连续。<br>证明：由 $\\lim_{\\Delta x\\to 0}\\frac{\\Delta y}{\\Delta x}=f'(x_0)$ 存在，故 $\\frac{\\Delta y}{\\Delta x}=f'(x_0)+\\alpha$（$\\alpha\\to 0$），于是 $\\Delta y=f'(x_0)\\Delta x+\\alpha\\Delta x\\to 0$，即 $f$ 连续。<br><strong>逆命题不成立</strong>：连续未必可导，如 $f(x)=|x|$ 在 $x=0$ 连续但不可导（左右导数不等）。"))
    + exa(p("用定义求 $f(x)=x^2$ 的导数：$f'(x)=\\lim_{\\Delta x\\to 0}\\frac{(x+\\Delta x)^2-x^2}{\\Delta x}=\\lim_{\\Delta x\\to 0}(2x+\\Delta x)=2x$。"))
)},
{"id":"c1s2-2","name":"微分","tags":["def","thm","app"],"brief":"增量的线性主部与可微条件。",
 "body": wrap(
    defn("微分", p("若函数增量 $\\Delta y=f(x_0+\\Delta x)-f(x_0)$ 可表示为 $\\Delta y=A\\Delta x+o(\\Delta x)$（$A$ 与 $\\Delta x$ 无关），则称 $f$ 在 $x_0$ 可微，$A\\Delta x$ 称为微分，记作 $dy=A\\Delta x=A\\,dx$。"))
    + thm("可微与可导等价", p("一元函数中，$f$ 在 $x_0$ 可微 $\\Leftrightarrow$ $f$ 在 $x_0$ 可导，且 $A=f'(x_0)$。故 $dy=f'(x_0)\\,dx$。"))
    + app(p("<strong>微分的应用：</strong>当 $|\\Delta x|$ 很小时，$\\Delta y\\approx dy=f'(x_0)\\Delta x$，即 $f(x_0+\\Delta x)\\approx f(x_0)+f'(x_0)\\Delta x$。<br>例：$\\sqrt{1.02}=\\sqrt{1+0.02}\\approx\\sqrt{1}+\\frac{1}{2\\sqrt{1}}\\cdot 0.02=1.01$。"))
)},
{"id":"c1s2-3","name":"求导法则","tags":["thm","der"],"brief":"四则运算、复合函数、反函数求导。",
 "body": wrap(
    thm("求导四则运算", p("若 $u,v$ 可导，则 $(u\\pm v)'=u'\\pm v'$，$(uv)'=u'v+uv'$，$\\left(\\frac{u}{v}\\right)'=\\frac{u'v-uv'}{v^2}$（$v\\ne 0$）。"))
    + thm("链式法则（复合函数求导）", p("若 $y=f(u)$，$u=g(x)$ 都可导，则")+
    fml("\\frac{dy}{dx} = \\frac{dy}{du}\\cdot\\frac{du}{dx} = f'(g(x))\\cdot g'(x)",
        "推广到多层复合：$\\frac{dy}{dx}=\\frac{dy}{du_1}\\frac{du_1}{du_2}\\cdots\\frac{du_n}{dx}$。"))
    + der(p("<strong>反函数求导：</strong>若 $y=f(x)$ 可导且 $f'(x)\\ne 0$，其反函数 $x=\\varphi(y)$ 可导，则")+
    fml("\\varphi'(y) = \\frac{1}{f'(x)} = \\frac{1}{f'(\\varphi(y))}",
        "例：$y=\\arcsin x$，则 $x=\\sin y$，$\\frac{dx}{dy}=\\cos y=\\sqrt{1-x^2}$，故 $(\\arcsin x)'=\\frac{1}{\\sqrt{1-x^2}}$。"))
)},
]
},
# ---- 1.3 初等函数的导数 ----
{
"name": "1.3 初等函数的导数",
"color": "#0ea5e9",
"desc": "基本求导公式、隐函数与参数方程求导",
"items": [
{"id":"c1s3-1","name":"基本求导公式","tags":["def","app"],"brief":"幂指对三角反三角的导数。",
 "body": wrap(
    defn("基本初等函数导数表", p("")+
    fml("(x^\\mu)' = \\mu x^{\\mu-1},\\quad (\\sin x)'=\\cos x,\\quad (\\cos x)'=-\\sin x",
        "$(\\tan x)'=\\sec^2 x$，$(\\cot x)'=-\\csc^2 x$，$(\\sec x)'=\\sec x\\tan x$，$(\\csc x)'=-\\csc x\\cot x$。")+
    fml("(e^x)'=e^x,\\quad (a^x)'=a^x\\ln a,\\quad (\\ln x)'=\\frac{1}{x},\\quad (\\log_a x)'=\\frac{1}{x\\ln a}",
        "$(\\arcsin x)'=\\frac{1}{\\sqrt{1-x^2}}$，$(\\arccos x)'=-\\frac{1}{\\sqrt{1-x^2}}$，$(\\arctan x)'=\\frac{1}{1+x^2}$，$(\\operatorname{arccot} x)'=-\\frac{1}{1+x^2}$。"))
    + app(p("所有初等函数的导数都可由基本公式经四则运算、复合、反函数求导得到。"))
)},
{"id":"c1s3-2","name":"隐函数求导","tags":["thm","der","exa"],"brief":"对 F(x,y)=0 求导。",
 "body": wrap(
    defn("隐函数", p("由方程 $F(x,y)=0$ 确定的函数 $y=y(x)$ 称为隐函数。其导数可通过方程两边对 $x$ 求导，将 $y$ 视为 $x$ 的函数（用链式法则），然后解出 $y'$。"))
    + exa(p("<strong>例：</strong>求由 $x^2+y^2=R^2$ 确定的隐函数的导数。<br>两边对 $x$ 求导：$2x+2y\\cdot y'=0$，解得 $y'=-\\frac{x}{y}$。<br>几何意义：圆上点 $(x,y)$ 处切线斜率为 $-x/y$。"))
    + der(p("<strong>隐函数存在定理（简述）：</strong>若 $F(x,y)$ 在 $(x_0,y_0)$ 邻域内有连续偏导数，$F(x_0,y_0)=0$，$F_y(x_0,y_0)\\ne 0$，则在 $x_0$ 邻域内存在唯一可导隐函数 $y=y(x)$ 满足 $F(x,y(x))=0$，且")+
    fml("\\frac{dy}{dx} = -\\frac{F_x}{F_y}"))
)},
{"id":"c1s3-3","name":"参数方程与对数求导法","tags":["thm","der","exa"],"brief":"x=x(t), y=y(t) 的导数；取对数化积为和。",
 "body": wrap(
    thm("参数方程求导", p("若参数方程 $x=\\varphi(t)$，$y=\\psi(t)$ 可导且 $\\varphi'(t)\\ne 0$，则")+
    fml("\\frac{dy}{dx} = \\frac{\\psi'(t)}{\\varphi'(t)} = \\frac{dy/dt}{dx/dt}"))
    + der(p("<strong>推导：</strong>由微分形式 $dy=\\psi'(t)dt$，$dx=\\varphi'(t)dt$，故 $\\frac{dy}{dx}=\\frac{\\psi'(t)dt}{\\varphi'(t)dt}=\\frac{\\psi'(t)}{\\varphi'(t)}$。"))
    + exa(p("<strong>对数求导法：</strong>对幂指函数 $y=u(x)^{v(x)}$ 或多个因式乘除的函数，先取对数再求导。<br>例：$y=x^x$，取对数 $\\ln y=x\\ln x$，两边求导 $\\frac{y'}{y}=\\ln x+1$，故 $y'=x^x(\\ln x+1)$。"))
)},
]
},
# ---- 1.4 高阶导数 ----
{
"name": "1.4 高阶导数",
"color": "#8b5cf6",
"desc": "高阶导数定义、莱布尼茨公式、常用高阶导数",
"items": [
{"id":"c1s4-1","name":"高阶导数与莱布尼茨公式","tags":["def","thm","der","exa"],"brief":"逐阶求导与乘积高阶导数。",
 "body": wrap(
    defn("高阶导数", p("$f$ 的 $n$ 阶导数定义为 $(n-1)$ 阶导数的导数：$f^{(n)}(x)=(f^{(n-1)})'(x)$。一阶导数 $f'$，二阶 $f''$，三阶 $f^{(3)}$。"))
    + thm("莱布尼茨公式", p("若 $u,v$ 有 $n$ 阶导数，则")+
    fml("(uv)^{(n)} = \\sum_{k=0}^{n}\\binom{n}{k}u^{(n-k)}v^{(k)}",
        "其中 $\\binom{n}{k}=\\frac{n!}{k!(n-k)!}$ 为二项式系数。此公式与二项式定理形式相似。"))
    + der(p("<strong>常用高阶导数：</strong>")+
    fml("(e^{ax})^{(n)}=a^n e^{ax},\\quad (\\sin x)^{(n)}=\\sin\\left(x+\\frac{n\\pi}{2}\\right),\\quad (\\cos x)^{(n)}=\\cos\\left(x+\\frac{n\\pi}{2}\\right)",
        "$(x^\\mu)^{(n)}=\\mu(\\mu-1)\\cdots(\\mu-n+1)x^{\\mu-n}$，$(\\frac{1}{x+a})^{(n)}=\\frac{(-1)^n n!}{(x+a)^{n+1}}$，$(\\ln x)^{(n)}=\\frac{(-1)^{n-1}(n-1)!}{x^n}$。"))
)},
{"id":"c1s4-2","name":"高阶导数的应用与可导阶数","tags":["app","note"],"brief":"加速度、曲率、光滑函数。",
 "body": wrap(
    app(p("<strong>物理应用：</strong>位移 $s(t)$ 的一阶导数为速度 $v=s'$，二阶导数为加速度 $a=s''$。<br><strong>曲率：</strong>曲线 $y=f(x)$ 的曲率 $\\kappa=\\frac{|y''|}{(1+y'^2)^{3/2}}$，曲率半径 $\\rho=1/\\kappa$。"))
    + note(p("<strong>可导阶数：</strong>函数未必任意阶可导。$f(x)=x|x|$ 一阶可导但二阶不可导（在 $x=0$）。若 $f$ 有任意阶连续导数，称 $f$ 为 $C^\\infty$ 光滑函数。<strong>解析函数</strong>是更强的概念，要求函数可展开为收敛的幂级数（见第八章）。"))
)},
]
},
# ---- 1.5 极限理论深入 ----
{
"name": "1.5 极限理论深入",
"color": "#1d4ed8",
"desc": "极限运算法则的ε-δ证明、第二重要极限、等价无穷小严格推导",
"items": [
{"id":"c1s5-1","name":"极限运算法则及其证明","tags":["thm","der"],"brief":"和差积商极限法则的严格证明。",
 "body": wrap(
    thm("极限的四则运算法则", p("设 $\\lim f(x)=A$，$\\lim g(x)=B$（同一极限过程），则：<br>(1) $\\lim[f(x)\\pm g(x)]=A\\pm B$；<br>(2) $\\lim[f(x)\\cdot g(x)]=A\\cdot B$；<br>(3) $\\lim\\frac{f(x)}{g(x)}=\\frac{A}{B}$（要求 $B\\ne 0$）。"))
    + der(p("<strong>乘积法则的 ε-δ 证明：</strong>第一步，由 $\\lim f=A$，取 $\\varepsilon=1$，存在 $\\delta_1>0$，当 $0<|x-x_0|<\\delta_1$ 时 $|f(x)-A|<1$，故 $|f(x)|\\le|f(x)-A|+|A|<|A|+1$，即 $f$ 在 $x_0$ 局部有界。<br>第二步，对任意 $\\varepsilon>0$，由 $\\lim f=A$ 存在 $\\delta_2$ 使 $|f(x)-A|<\\frac{\\varepsilon}{2(|B|+1)}$；由 $\\lim g=B$ 存在 $\\delta_3$ 使 $|g(x)-B|<\\frac{\\varepsilon}{2(|A|+1)}$。取 $\\delta=\\min(\\delta_1,\\delta_2,\\delta_3)$，则当 $0<|x-x_0|<\\delta$ 时：")+
    fml("|f(x)g(x)-AB| = |f(x)g(x)-f(x)B+f(x)B-AB| \\le |f(x)|\\cdot|g(x)-B|+|B|\\cdot|f(x)-A| < (|A|+1)\\cdot\\frac{\\varepsilon}{2(|A|+1)}+|B|\\cdot\\frac{\\varepsilon}{2(|B|+1)} < \\frac{\\varepsilon}{2}+\\frac{\\varepsilon}{2}=\\varepsilon",
        "故 $\\lim[f(x)\\cdot g(x)]=AB$。$\\blacksquare$<br>商法则由 $f/g=f\\cdot(1/g)$ 及先证 $\\lim(1/g)=1/B$ 推出：$\\left|\\frac{1}{g(x)}-\\frac{1}{B}\\right|=\\frac{|g(x)-B|}{|g(x)||B|}$，由 $g\\to B\\ne 0$ 知 $g$ 局部有 $|g|>|B|/2$，故可任意小。"))
    + der(p("<strong>夹逼准则证明（函数情形）：</strong>若在 $x_0$ 去心邻域内 $g(x)\\le f(x)\\le h(x)$，且 $\\lim g=\\lim h=A$，则对任意 $\\varepsilon>0$，存在 $\\delta$ 使 $|g-A|<\\varepsilon$ 且 $|h-A|<\\varepsilon$，即 $A-\\varepsilon<g(x)$ 且 $h(x)<A+\\varepsilon$。于是 $A-\\varepsilon<g(x)\\le f(x)\\le h(x)<A+\\varepsilon$，即 $|f(x)-A|<\\varepsilon$。$\\blacksquare$"))
)},
{"id":"c1s5-2","name":"第二重要极限与等价无穷小","tags":["thm","der","exa"],"brief":"(1+1/n)^n→e 与常用等价无穷小的推导。",
 "body": wrap(
    thm("第二重要极限", p("")+
    fml("\\lim_{n\\to\\infty}\\left(1+\\frac{1}{n}\\right)^n = e,\\qquad \\lim_{x\\to\\infty}\\left(1+\\frac{1}{x}\\right)^x = e,\\qquad \\lim_{x\\to 0}(1+x)^{1/x}=e",
        "其中 $e\\approx 2.718281828\\cdots$ 是自然对数的底，由欧拉命名。"))
    + der(p("<strong>数列极限证明：</strong>设 $a_n=(1+1/n)^n$。由二项式定理展开：")+
    fml("a_n = \\sum_{k=0}^n\\binom{n}{k}\\frac{1}{n^k} = 1+1+\\frac{1}{2!}\\left(1-\\frac{1}{n}\\right)+\\frac{1}{3!}\\left(1-\\frac{1}{n}\\right)\\left(1-\\frac{2}{n}\\right)+\\cdots+\\frac{1}{n!}\\prod_{j=1}^{n-1}\\left(1-\\frac{j}{n}\\right)",
        "当 $n$ 增大时，每一项的因子 $(1-j/n)$ 增大，且项数也增加（多出正项），故 $\\{a_n\\}$ 单调递增。另一方面，$a_n<1+1+\\frac{1}{2!}+\\frac{1}{3!}+\\cdots+\\frac{1}{n!}<1+1+\\frac{1}{2}+\\frac{1}{2^2}+\\cdots+\\frac{1}{2^{n-1}}<1+2=3$，有上界。由单调有界准则，$\\lim a_n$ 存在，记为 $e$。"))
    + der(p("<strong>常用等价无穷小推导（$x\\to 0$）：</strong><br>(1) $\\ln(1+x)\\sim x$：$\\lim_{x\\to 0}\\frac{\\ln(1+x)}{x}=\\lim_{x\\to 0}\\ln(1+x)^{1/x}=\\ln e=1$。<br>(2) $e^x-1\\sim x$：令 $t=e^x-1$，则 $x=\\ln(1+t)$，$\\lim\\frac{e^x-1}{x}=\\lim_{t\\to 0}\\frac{t}{\\ln(1+t)}=1$。<br>(3) $(1+x)^\\alpha-1\\sim\\alpha x$：$(1+x)^\\alpha-1=e^{\\alpha\\ln(1+x)}-1\\sim\\alpha\\ln(1+x)\\sim\\alpha x$。<br>(4) $1-\\cos x\\sim x^2/2$：$\\lim\\frac{1-\\cos x}{x^2/2}=\\lim\\frac{2\\sin^2(x/2)}{x^2/2}=\\lim\\left(\\frac{\\sin(x/2)}{x/2}\\right)^2=1$。"))
    + exa(p("<strong>例：</strong>求 $\\lim_{x\\to 0}\\frac{\\tan x-\\sin x}{x^3}$。<br>正解：$\\tan x-\\sin x=\\sin x(\\sec x-1)=\\sin x\\cdot\\frac{1-\\cos x}{\\cos x}\\sim x\\cdot\\frac{x^2/2}{1}=\\frac{x^3}{2}$，故极限为 $1/2$。<br><strong>典型错误：</strong>分别替换 $\\tan x\\sim x$、$\\sin x\\sim x$ 得 $x-x=0$。加减运算中一般不能替换等价无穷小！"))
)},
]
},
# ---- 1.6 求导法则的证明 ----
{
"name": "1.6 求导法则的证明",
"color": "#2563eb",
"desc": "乘积法则、商法则、链式法则的严格证明",
"items": [
{"id":"c1s6-1","name":"乘积与商求导法则的证明","tags":["thm","der","exa"],"brief":"(uv)' 与 (u/v)' 的推导。",
 "body": wrap(
    thm("乘积法则", p("若 $u(x),v(x)$ 在 $x$ 处可导，则 $(uv)'=u'v+uv'$。"))
    + der(p("<strong>证明：</strong>设 $y=u(x)v(x)$，给 $x$ 以增量 $\\Delta x$，则 $u,v$ 各有增量 $\\Delta u,\\Delta v$：")+
    fml("\\Delta y = (u+\\Delta u)(v+\\Delta v)-uv = u\\Delta v+v\\Delta u+\\Delta u\\,\\Delta v",
        "故 $\\frac{\\Delta y}{\\Delta x}=u\\frac{\\Delta v}{\\Delta x}+v\\frac{\\Delta u}{\\Delta x}+\\Delta u\\frac{\\Delta v}{\\Delta x}$。令 $\\Delta x\\to 0$，由 $u$ 可导知 $\\Delta u\\to 0$，$\\frac{\\Delta u}{\\Delta x}\\to u'$，$\\frac{\\Delta v}{\\Delta x}\\to v'$，故 $y'=uv'+vu'+0\\cdot v'=u'v+uv'$。$\\blacksquare$"))
    + thm("商法则", p("若 $u,v$ 可导且 $v(x)\\ne 0$，则 $\\left(\\frac{u}{v}\\right)'=\\frac{u'v-uv'}{v^2}$。"))
    + der(p("<strong>证明：</strong>设 $y=u/v$，则 $\\Delta y=\\frac{u+\\Delta u}{v+\\Delta v}-\\frac{u}{v}=\\frac{v\\Delta u-u\\Delta v}{v(v+\\Delta v)}$，故")+
    fml("\\frac{\\Delta y}{\\Delta x} = \\frac{v\\frac{\\Delta u}{\\Delta x}-u\\frac{\\Delta v}{\\Delta x}}{v(v+\\Delta v)} \\xrightarrow{\\Delta x\\to 0} \\frac{vu'-uv'}{v^2}",
        "其中用到 $\\Delta v\\to 0$（$v$ 可导必连续）。$\\blacksquare$"))
    + exa(p("<strong>例：</strong>$(\\tan x)'=\\left(\\frac{\\sin x}{\\cos x}\\right)'=\\frac{\\cos x\\cdot\\cos x-\\sin x\\cdot(-\\sin x)}{\\cos^2 x}=\\frac{1}{\\cos^2 x}=\\sec^2 x$。"))
)},
{"id":"c1s6-2","name":"链式法则的证明","tags":["thm","der","exa"],"brief":"复合函数求导的严格证明。",
 "body": wrap(
    thm("链式法则", p("若 $y=f(u)$ 在 $u_0$ 可导，$u=g(x)$ 在 $x_0$ 可导，且 $u_0=g(x_0)$，则复合函数 $y=f(g(x))$ 在 $x_0$ 可导，且")+
    fml("\\frac{dy}{dx}\\bigg|_{x=x_0} = f'(u_0)\\cdot g'(x_0)"))
    + der(p("<strong>证明：</strong>由 $f$ 在 $u_0$ 可导，有 $\\Delta y=f'(u_0)\\Delta u+\\alpha\\Delta u$，其中 $\\alpha\\to 0$（当 $\\Delta u\\to 0$）。补充定义 $\\alpha=0$ 当 $\\Delta u=0$，则上式对 $\\Delta u=0$ 也成立。两边除以 $\\Delta x$：")+
    fml("\\frac{\\Delta y}{\\Delta x} = f'(u_0)\\frac{\\Delta u}{\\Delta x}+\\alpha\\frac{\\Delta u}{\\Delta x}",
        "令 $\\Delta x\\to 0$。由 $g$ 可导知 $\\Delta u\\to 0$，从而 $\\alpha\\to 0$；又 $\\frac{\\Delta u}{\\Delta x}\\to g'(x_0)$。故 $\\frac{dy}{dx}=f'(u_0)g'(x_0)+0\\cdot g'(x_0)=f'(u_0)g'(x_0)$。$\\blacksquare$"))
    + der(p("<strong>反函数求导推导：</strong>设 $y=f(x)$ 严格单调可导且 $f'(x)\\ne 0$，反函数 $x=\\varphi(y)$。由 $\\frac{\\Delta x}{\\Delta y}=\\frac{1}{\\Delta y/\\Delta x}$，令 $\\Delta y\\to 0$（此时 $\\Delta x\\to 0$），得 $\\varphi'(y)=\\frac{1}{f'(x)}$。<br>例：$y=\\arcsin x$，则 $x=\\sin y$，$\\frac{dx}{dy}=\\cos y=\\sqrt{1-\\sin^2 y}=\\sqrt{1-x^2}$，故 $(\\arcsin x)'=\\frac{1}{\\sqrt{1-x^2}}$。"))
    + exa(p("<strong>例（多层复合）：</strong>求 $y=e^{\\sin^2 x}$ 的导数。令 $y=e^u$，$u=v^2$，$v=\\sin x$，则 $\\frac{dy}{dx}=\\frac{dy}{du}\\cdot\\frac{du}{dv}\\cdot\\frac{dv}{dx}=e^u\\cdot 2v\\cdot\\cos x=e^{\\sin^2 x}\\cdot 2\\sin x\\cos x=e^{\\sin^2 x}\\sin 2x$。"))
)},
]
},
]
print(f"Ch1: {sum(len(s['items']) for s in ch1_sections)} items")

# =====================================================
#  CHAPTER 2: 微分定理
# =====================================================
ch2_sections = [
# ---- 2.1 微分中值定理 ----
{
"name": "2.1 微分中值定理",
"color": "#0d9488",
"desc": "罗尔、拉格朗日、柯西中值定理及其证明",
"items": [
{"id":"c2s1-1","name":"罗尔定理","tags":["thm","der","exa","note"],"brief":"闭区间连续、开区间可导、端点值相等。",
 "body": wrap(
    thm("罗尔定理", p("若 $f(x)$ 满足：(1) 在 $[a,b]$ 连续；(2) 在 $(a,b)$ 可导；(3) $f(a)=f(b)$，则存在 $\\xi\\in(a,b)$ 使得 $f'(\\xi)=0$。"))
    + der(p("<strong>证明：</strong>由最值定理，$f$ 在 $[a,b]$ 取到最大值 $M$ 和最小值 $m$。<br>若 $M=m$，则 $f$ 为常数，$f'\\equiv 0$，任意 $\\xi$ 都满足。<br>若 $M>m$，由 $f(a)=f(b)$，至少有一个最值在内部 $\\xi\\in(a,b)$ 取到。不妨设 $f(\\xi)=M$，则 $f(\\xi+\\Delta x)\\le f(\\xi)$，故")+
    fml("f'_+(\\xi)=\\lim_{\\Delta x\\to 0^+}\\frac{f(\\xi+\\Delta x)-f(\\xi)}{\\Delta x}\\le 0,\\quad f'_-(\\xi)=\\lim_{\\Delta x\\to 0^-}\\frac{f(\\xi+\\Delta x)-f(\\xi)}{\\Delta x}\\ge 0",
        "由可导性 $f'_+(\\xi)=f'_-(\\xi)=f'(\\xi)$，故 $f'(\\xi)=0$。$\\blacksquare$"))
    + note(p("罗尔定理的几何意义：满足条件的曲线在 $(a,b)$ 内至少有一条水平切线。"))
)},
{"id":"c2s1-2","name":"拉格朗日中值定理","tags":["thm","der","app"],"brief":"最常用的中值定理，导数与增量的桥梁。",
 "body": wrap(
    thm("拉格朗日中值定理", p("若 $f$ 在 $[a,b]$ 连续、在 $(a,b)$ 可导，则存在 $\\xi\\in(a,b)$ 使得")+
    fml("f(b)-f(a) = f'(\\xi)(b-a) \\quad\\Longleftrightarrow\\quad f'(\\xi)=\\frac{f(b)-f(a)}{b-a}"))
    + der(p("<strong>证明（构造辅助函数）：</strong>设辅助函数 $\\varphi(x)=f(x)-\\frac{f(b)-f(a)}{b-a}(x-a)$。<br>验证 $\\varphi(a)=f(a)$，$\\varphi(b)=f(a)$，故 $\\varphi(a)=\\varphi(b)$。$\\varphi$ 在 $[a,b]$ 连续、$(a,b)$ 可导。<br>由罗尔定理，存在 $\\xi$ 使 $\\varphi'(\\xi)=0$，即 $f'(\\xi)-\\frac{f(b)-f(a)}{b-a}=0$。$\\blacksquare$"))
    + app(p("<strong>推论1：</strong>若 $f$ 在区间 $I$ 上 $f'\\equiv 0$，则 $f$ 在 $I$ 上为常数。<br><strong>推论2：</strong>若 $f,g$ 在 $I$ 上 $f'=g'$，则 $f(x)=g(x)+C$。<br><strong>单调性判据：</strong>$f$ 在 $I$ 上单调递增 $\\Leftrightarrow$ $f'\\ge 0$；严格递增 $\\Leftarrow$ $f'>0$。"))
    + note(p("<strong>几何意义：</strong>拉格朗日中值定理表明：连接曲线两端点 $(a,f(a))$ 与 $(b,f(b))$ 的<strong>割线斜率</strong> $\\frac{f(b)-f(a)}{b-a}$，必等于曲线在某点 $\\xi$ 处的<strong>切线斜率</strong> $f'(\\xi)$。即曲线上至少存在一点，其切线与两端点连线平行。"))
)},
{"id":"c2s1-3","name":"柯西中值定理","tags":["thm","der","note"],"brief":"两个函数的中值定理，洛必达法则的基础。",
 "body": wrap(
    thm("柯西中值定理", p("若 $f,g$ 在 $[a,b]$ 连续、$(a,b)$ 可导，且 $g'(x)\\ne 0$（$x\\in(a,b)$），则存在 $\\xi\\in(a,b)$ 使得")+
    fml("\\frac{f(b)-f(a)}{g(b)-g(a)} = \\frac{f'(\\xi)}{g'(\\xi)}"))
    + der(p("<strong>证明：</strong>构造辅助函数 $\\varphi(x)=f(x)-\\frac{f(b)-f(a)}{g(b)-g(a)}g(x)$。<br>验证 $\\varphi(a)=\\varphi(b)=\\frac{f(a)g(b)-f(b)g(a)}{g(b)-g(a)}$，由罗尔定理得证。<br>注意 $g(b)-g(a)\\ne 0$（否则由罗尔定理 $g'$ 有零点，矛盾）。"))
    + note(p("拉格朗日中值定理是柯西中值定理取 $g(x)=x$ 的特例。柯西定理是洛必达法则的理论基础。<br><strong>几何意义：</strong>将 $(g(t),f(t))$ 视为参数方程表示的曲线，则 $\\frac{f(b)-f(a)}{g(b)-g(a)}$ 是两端点连线的斜率，$\\frac{f'(\\xi)}{g'(\\xi)}$ 是曲线上某点切线的斜率——二者相等。"))
)},
]
},
# ---- 2.2 泰勒公式 ----
{
"name": "2.2 泰勒公式",
"color": "#059669",
"desc": "用多项式逼近函数，麦克劳林展开",
"items": [
{"id":"c2s2-1","name":"泰勒中值定理","tags":["thm","der","exa"],"brief":"带拉格朗日余项的泰勒公式。",
 "body": wrap(
    thm("泰勒定理", p("若 $f$ 在含 $x_0$ 的区间内有直到 $n+1$ 阶导数，则对该区间内任意 $x$，有")+
    fml("f(x) = \\sum_{k=0}^{n}\\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k + R_n(x)",
        "其中余项 $R_n(x)=\\frac{f^{(n+1)}(\\xi)}{(n+1)!}(x-x_0)^{n+1}$，$\\xi$ 介于 $x_0$ 与 $x$ 之间（拉格朗日余项）。"))
    + der(p("<strong>证明思路（多次应用柯西中值定理）：</strong>设 $R_n(x)=f(x)-\\sum_{k=0}^n\\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k$，$Q_n(x)=(x-x_0)^{n+1}$。<br>则 $R_n(x_0)=R_n'(x_0)=\\cdots=R_n^{(n)}(x_0)=0$，$Q_n(x_0)=\\cdots=Q_n^{(n)}(x_0)=0$。<br>反复应用柯西中值定理 $n+1$ 次，得 $\\frac{R_n(x)}{Q_n(x)}=\\frac{R_n^{(n+1)}(\\xi)}{Q_n^{(n+1)}(\\xi)}=\\frac{f^{(n+1)}(\\xi)}{(n+1)!}$，即得余项公式。"))
    + exa(p("<strong>$e^x$ 的麦克劳林展开（$x_0=0$）：</strong>$(e^x)^{(n)}=e^x$，故")+
    fml("e^x = 1+x+\\frac{x^2}{2!}+\\cdots+\\frac{x^n}{n!}+\\frac{e^\\xi}{(n+1)!}x^{n+1},\\quad \\xi\\in(0,x)"))
)},
{"id":"c2s2-2","name":"常用麦克劳林展开","tags":["exa","app"],"brief":"基本初等函数的幂级数展开。",
 "body": wrap(
    exa(p("")+
    fml("\\sin x = x-\\frac{x^3}{3!}+\\frac{x^5}{5!}-\\cdots+(-1)^n\\frac{x^{2n+1}}{(2n+1)!}+o(x^{2n+2})",
        "$\\cos x = 1-\\frac{x^2}{2!}+\\frac{x^4}{4!}-\\cdots+(-1)^n\\frac{x^{2n}}{(2n)!}+o(x^{2n+1})$")+
    fml("\\ln(1+x) = x-\\frac{x^2}{2}+\\frac{x^3}{3}-\\cdots+(-1)^{n-1}\\frac{x^n}{n}+o(x^n)",
        "$(1+x)^\\alpha = 1+\\alpha x+\\frac{\\alpha(\\alpha-1)}{2!}x^2+\\cdots+\\binom{\\alpha}{n}x^n+o(x^n)$")+
    fml("\\arctan x = x-\\frac{x^3}{3}+\\frac{x^5}{5}-\\cdots+(-1)^n\\frac{x^{2n+1}}{2n+1}+o(x^{2n+2})"))
    + app(p("<strong>应用：</strong>(1) 求极限：用泰勒展开替换函数，保留到合适阶数；(2) 近似计算：取前若干项近似函数值；(3) 证明不等式。"))
)},
]
},
# ---- 2.3 洛必达法则 ----
{
"name": "2.3 洛必达法则",
"color": "#10b981",
"desc": "不定式极限的系统求法",
"items": [
{"id":"c2s3-1","name":"洛必达法则","tags":["thm","der","app","note"],"brief":"0/0 与 ∞/∞ 型不定式。",
 "body": wrap(
    thm("洛必达法则（$0/0$ 型）", p("若 (1) $\\lim_{x\\to a}f(x)=\\lim_{x\\to a}g(x)=0$；(2) $f',g'$ 在 $a$ 的去心邻域存在且 $g'\\ne 0$；(3) $\\lim_{x\\to a}\\frac{f'(x)}{g'(x)}$ 存在（或为 $\\infty$），则")+
    fml("\\lim_{x\\to a}\\frac{f(x)}{g(x)} = \\lim_{x\\to a}\\frac{f'(x)}{g'(x)}"))
    + der(p("<strong>证明：</strong>补充定义 $f(a)=g(a)=0$（不影响极限），则 $f,g$ 在 $a$ 连续。对 $x$ 接近 $a$，在 $[a,x]$（或 $[x,a]$）上用柯西中值定理：")+
    fml("\\frac{f(x)}{g(x)} = \\frac{f(x)-f(a)}{g(x)-g(a)} = \\frac{f'(\\xi)}{g'(\\xi)},\\quad \\xi\\text{ 介于 }a,x\\text{ 之间}",
        "当 $x\\to a$ 时 $\\xi\\to a$，故 $\\lim\\frac{f(x)}{g(x)}=\\lim\\frac{f'(\\xi)}{g'(\\xi)}=\\lim\\frac{f'(x)}{g'(x)}$。$\\blacksquare$"))
    + app(p("<strong>其他不定式：</strong>$\\infty/\\infty$ 型同样适用；$0\\cdot\\infty$、$\\infty-\\infty$、$0^0$、$1^\\infty$、$\\infty^0$ 型需先转化为 $0/0$ 或 $\\infty/\\infty$ 型。<br>例：$\\lim_{x\\to 0}\\frac{\\sin x}{x}=\\lim_{x\\to 0}\\frac{\\cos x}{1}=1$。"))
    + note(p("<strong>使用注意：</strong>(1) 必须先验证是 $0/0$ 或 $\\infty/\\infty$ 型；(2) 若 $\\lim\\frac{f'}{g'}$ 不存在（非无穷），不能说明原极限不存在；(3) 可连续使用，但每次都要验证条件；(4) 与等价无穷小替换结合可简化计算。"))
)},
]
},
# ---- 2.4 极值与凸性 ----
{
"name": "2.4 极值与凸性",
"color": "#14b8a6",
"desc": "极值判定、函数凸性、拐点与作图",
"items": [
{"id":"c2s4-1","name":"函数的极值","tags":["def","thm","der"],"brief":"极值的必要与充分条件。",
 "body": wrap(
    defn("极值", p("若 $f$ 在 $x_0$ 某邻域内有定义，且对该邻域内任意 $x\\ne x_0$ 都有 $f(x)<f(x_0)$（或 $f(x)>f(x_0)$），则称 $f(x_0)$ 为极大值（或极小值），$x_0$ 为极值点。"))
    + thm("极值判据", p("<strong>必要条件（费马定理）：</strong>若 $f$ 在 $x_0$ 可导且取极值，则 $f'(x_0)=0$。使 $f'(x_0)=0$ 的点称为驻点。<br><strong>第一充分条件：</strong>若 $f'$ 在 $x_0$ 两侧变号，则 $x_0$ 为极值点（左正右负为极大，左负右正为极小）。<br><strong>第二充分条件：</strong>若 $f'(x_0)=0$，$f''(x_0)$ 存在，则 $f''(x_0)>0$ 为极小，$f''(x_0)<0$ 为极大。"))
    + der(p("<strong>第二充分条件证明（极小情形）：</strong>$f''(x_0)=\\lim_{x\\to x_0}\\frac{f'(x)-f'(x_0)}{x-x_0}=\\lim_{x\\to x_0}\\frac{f'(x)}{x-x_0}>0$。<br>由保号性，在 $x_0$ 附近 $\\frac{f'(x)}{x-x_0}>0$，故 $x<x_0$ 时 $f'(x)<0$，$x>x_0$ 时 $f'(x)>0$，由第一充分条件知 $x_0$ 为极小值点。"))
)},
{"id":"c2s4-2","name":"凸性与拐点","tags":["def","thm","app"],"brief":"曲线凹凸性的判定与拐点。",
 "body": wrap(
    defn("凸性", p("设 $f$ 在区间 $I$ 连续。若对 $I$ 上任意 $x_1,x_2$ 及 $t\\in[0,1]$，有 $f(tx_1+(1-t)x_2)\\le tf(x_1)+(1-t)f(x_2)$，则称 $f$ 在 $I$ 上是<strong>凸函数</strong>（下凸）；反向不等式为凹函数（上凸）。"))
    + thm("凸性判定", p("若 $f$ 在 $I$ 上二阶可导，则 $f$ 为凸函数 $\\Leftrightarrow$ $f''(x)\\ge 0$（$x\\in I$）；严格凸 $\\Leftarrow$ $f''>0$。<br><strong>拐点：</strong>曲线凹凸性发生改变的点。若 $f''(x_0)=0$ 且 $f''$ 在 $x_0$ 两侧变号，则 $(x_0,f(x_0))$ 为拐点。"))
    + app(p("<strong>詹森不等式：</strong>若 $f$ 为凸函数，则 $f\\left(\\sum t_i x_i\\right)\\le\\sum t_i f(x_i)$（$t_i\\ge 0$，$\\sum t_i=1$）。这是凸性最有用的应用，在概率论（期望的琴生不等式）和优化中广泛使用。"))
)},
]
},
# ---- 2.5 泰勒公式的余项与函数作图 ----
{
"name": "2.5 泰勒公式的余项与函数作图",
"color": "#0d9488",
"desc": "皮亚诺余项、余项估计、函数作图的一般步骤",
"items": [
{"id":"c2s5-1","name":"泰勒公式的余项形式","tags":["thm","der","exa"],"brief":"拉格朗日余项、皮亚诺余项、积分余项。",
 "body": wrap(
    thm("三种余项形式", p("泰勒公式 $f(x)=\\sum_{k=0}^n\\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k+R_n(x)$ 有三种常用余项：<br>(1) <strong>拉格朗日余项：</strong>$R_n(x)=\\frac{f^{(n+1)}(\\xi)}{(n+1)!}(x-x_0)^{n+1}$，$\\xi$ 介于 $x_0,x$ 之间；<br>(2) <strong>皮亚诺余项：</strong>$R_n(x)=o((x-x_0)^n)$（$x\\to x_0$），只需 $f^{(n)}(x_0)$ 存在；<br>(3) <strong>积分余项：</strong>$R_n(x)=\\frac{1}{n!}\\int_{x_0}^x f^{(n+1)}(t)(x-t)^n\\,dt$。"))
    + der(p("<strong>积分余项推导：</strong>由牛顿-莱布尼茨公式 $f(x)-f(x_0)=\\int_{x_0}^x f'(t)\\,dt$。对 $n=1$，分部积分：$\\int_{x_0}^x f'(t)\\,dt=[f'(t)(t-x)]_{x_0}^x-\\int_{x_0}^x f''(t)(t-x)\\,dt=f'(x_0)(x-x_0)+\\int_{x_0}^x f''(t)(x-t)\\,dt$。反复分部积分 $n$ 次，即得积分余项。<br><strong>拉格朗日余项由积分余项推出：</strong>由积分第一中值定理，$\\int_{x_0}^x f^{(n+1)}(t)(x-t)^n\\,dt=f^{(n+1)}(\\xi)\\int_{x_0}^x(x-t)^n\\,dt=f^{(n+1)}(\\xi)\\cdot\\frac{(x-x_0)^{n+1}}{n+1}$，故 $R_n=\\frac{f^{(n+1)}(\\xi)}{(n+1)!}(x-x_0)^{n+1}$。"))
    + exa(p("<strong>例（余项估计）：</strong>用 $e^x$ 的麦克劳林展开计算 $e$，取 $n=9$：$e\\approx\\sum_{k=0}^9\\frac{1}{k!}$。余项 $R_9=\\frac{e^\\xi}{10!}$（$0<\\xi<1$），$e^\\xi<e<3$，故 $|R_9|<\\frac{3}{10!}=\\frac{3}{3628800}\\approx 8.3\\times 10^{-7}$，精度达百万分之一。"))
)},
{"id":"c2s5-2","name":"函数作图的一般步骤","tags":["thm","app","exa"],"brief":"利用导数系统描绘函数图像。",
 "body": wrap(
    thm("作图步骤", p("<strong>(1)</strong> 确定定义域、奇偶性、周期性；<br><strong>(2)</strong> 求一阶导数 $f'$，确定驻点和不可导点，判断单调性与极值；<br><strong>(3)</strong> 求二阶导数 $f''$，确定凹凸性与拐点；<br><strong>(4)</strong> 求渐近线（水平、铅直、斜）；<br><strong>(5)</strong> 描点作图（极值点、拐点、与坐标轴交点等）。"))
    + der(p("<strong>渐近线求法：</strong><br>(1) <strong>水平渐近线：</strong>若 $\\lim_{x\\to+\\infty}f(x)=c$（或 $x\\to-\\infty$），则 $y=c$ 为水平渐近线。<br>(2) <strong>铅直渐近线：</strong>若 $\\lim_{x\\to a}f(x)=\\infty$，则 $x=a$ 为铅直渐近线（$a$ 通常为间断点）。<br>(3) <strong>斜渐近线：</strong>若 $\\lim_{x\\to\\infty}\\frac{f(x)}{x}=k\\ne 0$ 且 $\\lim_{x\\to\\infty}[f(x)-kx]=b$，则 $y=kx+b$ 为斜渐近线。"))
    + exa(p("<strong>例：</strong>作 $y=\\frac{x^3}{x^2-1}$ 的图像。<br>定义域 $x\\ne\\pm 1$，奇函数。$y'=\\frac{x^2(x^2-3)}{(x^2-1)^2}$，驻点 $x=0,\\pm\\sqrt{3}$。$y''=\\frac{2x(x^2+3)}{(x^2-1)^3}$。<br>极大值 $y(\\sqrt{3})=\\frac{3\\sqrt{3}}{2}$，极小值 $y(-\\sqrt{3})=-\\frac{3\\sqrt{3}}{2}$，拐点 $(0,0)$。<br>渐近线：$x=\\pm 1$（铅直），$y=x$（斜渐近线，$k=1,b=0$）。据此可画出完整图像。"))
)},
]
},
]
print(f"Ch2: {sum(len(s['items']) for s in ch2_sections)} items")

# =====================================================
#  CHAPTER 3: 一元积分
# =====================================================
ch3_sections = [
# ---- 3.1 不定积分 ----
{
"name": "3.1 不定积分",
"color": "#0d9488",
"desc": "原函数、基本积分表、换元法与分部积分法",
"items": [
{"id":"c3s1-1","name":"不定积分的概念","tags":["def","thm"],"brief":"原函数与不定积分。",
 "body": wrap(
    defn("原函数与不定积分", p("若 $F'(x)=f(x)$，则 $F(x)$ 称为 $f(x)$ 的一个原函数。$f$ 的全体原函数 $F(x)+C$ 称为 $f$ 的不定积分，记作 $\\int f(x)\\,dx=F(x)+C$。"))
    + thm("原函数存在定理", p("若 $f$ 在区间 $I$ 连续，则 $f$ 在 $I$ 上一定存在原函数。（这是微积分基本定理的推论，见 3.3）"))
)},
{"id":"c3s1-2","name":"换元积分法","tags":["thm","der","exa"],"brief":"第一类与第二类换元法。",
 "body": wrap(
    thm("第一类换元法（凑微分法）", p("若 $\\int f(u)\\,du=F(u)+C$，且 $u=\\varphi(x)$ 可导，则")+
    fml("\\int f(\\varphi(x))\\varphi'(x)\\,dx = \\int f(u)\\,du = F(\\varphi(x))+C",
        "关键：将被积函数凑成 $f(\\varphi(x))\\varphi'(x)$ 的形式。"))
    + thm("第二类换元法", p("设 $x=\\psi(t)$ 单调可导且 $\\psi'(t)\\ne 0$，则")+
    fml("\\int f(x)\\,dx = \\int f(\\psi(t))\\psi'(t)\\,dt",
        "常用于含根式的积分：$\\sqrt{a^2-x^2}$ 令 $x=a\\sin t$；$\\sqrt{a^2+x^2}$ 令 $x=a\\tan t$；$\\sqrt{x^2-a^2}$ 令 $x=a\\sec t$。"))
    + exa(p("<strong>例：</strong>$\\int\\frac{dx}{1+e^x}$，令 $t=e^x$，$dx=\\frac{dt}{t}$，则 $\\int\\frac{dt}{t(1+t)}=\\int(\\frac{1}{t}-\\frac{1}{1+t})dt=\\ln t-\\ln(1+t)+C=x-\\ln(1+e^x)+C$。"))
)},
{"id":"c3s1-3","name":"分部积分法","tags":["thm","der","exa"],"brief":"乘积积分的核心方法。",
 "body": wrap(
    thm("分部积分公式", p("由 $(uv)'=u'v+uv'$，两边积分得")+
    fml("\\int u\\,dv = uv - \\int v\\,du",
        "选择 $u$ 的优先顺序：反三角、对数、幂函数、指数、三角（LIATE 法则），将排在前的选作 $u$。"))
    + der(p("<strong>推导：</strong>由乘积求导法则 $d(uv)=v\\,du+u\\,dv$，即 $u\\,dv=d(uv)-v\\,du$。两边积分：$\\int u\\,dv=uv-\\int v\\,du$。"))
    + exa(p("<strong>例：</strong>$\\int x e^x\\,dx$，取 $u=x$，$dv=e^x dx$，则 $du=dx$，$v=e^x$，故 $\\int x e^x dx=xe^x-\\int e^x dx=xe^x-e^x+C$。"))
)},
]
},
# ---- 3.2 定积分 ----
{
"name": "3.2 定积分",
"color": "#059669",
"desc": "黎曼和定义、牛顿-莱布尼茨公式",
"items": [
{"id":"c3s2-1","name":"定积分的定义","tags":["def","thm","note"],"brief":"黎曼和与可积条件。",
 "body": wrap(
    defn("定积分（黎曼积分）", p("将 $[a,b]$ 任意分割为 $n$ 个小区间 $[x_{i-1},x_i]$，在每个区间取点 $\\xi_i\\in[x_{i-1},x_i]$，作黎曼和 $\\sum_{i=1}^n f(\\xi_i)\\Delta x_i$。若当 $\\lambda=\\max\\Delta x_i\\to 0$ 时极限存在且与分割和取法无关，则称此极限为 $f$ 在 $[a,b]$ 上的定积分：")+
    fml("\\int_a^b f(x)\\,dx = \\lim_{\\lambda\\to 0}\\sum_{i=1}^n f(\\xi_i)\\Delta x_i"))
    + thm("可积条件", p("<strong>充分条件：</strong>$f$ 在 $[a,b]$ 连续 $\\Rightarrow$ $f$ 可积；$f$ 在 $[a,b]$ 有界且只有有限个间断点 $\\Rightarrow$ $f$ 可积。<br><strong>必要条件：</strong>$f$ 在 $[a,b]$ 有界。"))
    + note(p("定积分的几何意义：当 $f(x)\\ge 0$ 时，$\\int_a^b f(x)\\,dx$ 表示曲线 $y=f(x)$ 与 $x=a,x=b$ 及 $x$ 轴围成的面积。"))
)},
{"id":"c3s2-2","name":"微积分基本定理","tags":["thm","der","app"],"brief":"牛顿-莱布尼茨公式，微分与积分的统一。",
 "body": wrap(
    thm("牛顿-莱布尼茨公式", p("若 $f$ 在 $[a,b]$ 连续，$F$ 是 $f$ 的一个原函数，则")+
    fml("\\int_a^b f(x)\\,dx = F(b)-F(a) = F(x)\\big|_a^b"))
    + der(p("<strong>证明：</strong>设变上限积分 $\\Phi(x)=\\int_a^x f(t)\\,dt$。先证 $\\Phi'(x)=f(x)$（见 3.3）。<br>故 $\\Phi$ 是 $f$ 的一个原函数，而任意两个原函数相差常数，故 $\\Phi(x)=F(x)+C$。<br>代入 $x=a$：$\\Phi(a)=0=F(a)+C$，故 $C=-F(a)$，$\\Phi(x)=F(x)-F(a)$。<br>令 $x=b$：$\\int_a^b f(t)\\,dt=\\Phi(b)=F(b)-F(a)$。$\\blacksquare$"))
    + app(p("牛顿-莱布尼茨公式将定积分的计算转化为求原函数，建立了微分与积分的联系，是微积分学的核心定理。"))
)},
]
},
# ---- 3.3 定积分性质与应用 ----
{
"name": "3.3 定积分性质",
"color": "#10b981",
"desc": "积分性质、积分中值定理、变上限积分",
"items": [
{"id":"c3s3-1","name":"定积分性质","tags":["thm","app"],"brief":"线性、区间可加、保号性、估值。",
 "body": wrap(
    thm("定积分基本性质", p("(1) 线性：$\\int_a^b[\\alpha f+\\beta g]\\,dx=\\alpha\\int_a^b f\\,dx+\\beta\\int_a^b g\\,dx$；<br>(2) 区间可加：$\\int_a^b f\\,dx=\\int_a^c f\\,dx+\\int_c^b f\\,dx$；<br>(3) 保号性：若 $f\\ge 0$ 则 $\\int_a^b f\\,dx\\ge 0$；<br>(4) 估值定理：若 $m\\le f(x)\\le M$，则 $m(b-a)\\le\\int_a^b f\\,dx\\le M(b-a)$；<br>(5) 绝对可积：$\\left|\\int_a^b f\\,dx\\right|\\le\\int_a^b |f|\\,dx$。"))
    + app(p("性质常用于比较积分大小、估计积分值、证明积分不等式。"))
)},
{"id":"c3s3-2","name":"变上限积分与积分中值定理","tags":["thm","der","app"],"brief":"微积分第一基本定理。",
 "body": wrap(
    thm("微积分第一基本定理", p("若 $f$ 在 $[a,b]$ 连续，则变上限积分 $\\Phi(x)=\\int_a^x f(t)\\,dt$ 在 $[a,b]$ 可导，且")+
    fml("\\Phi'(x) = \\frac{d}{dx}\\int_a^x f(t)\\,dt = f(x)"))
    + der(p("<strong>证明：</strong>$\\frac{\\Phi(x+h)-\\Phi(x)}{h}=\\frac{1}{h}\\int_x^{x+h}f(t)\\,dt$。由积分中值定理，存在 $\\xi$ 介于 $x,x+h$ 之间，使 $\\int_x^{x+h}f(t)\\,dt=f(\\xi)h$。当 $h\\to 0$ 时 $\\xi\\to x$，由 $f$ 连续得 $f(\\xi)\\to f(x)$。故 $\\Phi'(x)=f(x)$。"))
    + thm("积分中值定理", p("若 $f$ 在 $[a,b]$ 连续，则存在 $\\xi\\in[a,b]$ 使得 $\\int_a^b f(x)\\,dx=f(\\xi)(b-a)$。$f(\\xi)$ 称为 $f$ 在 $[a,b]$ 上的平均值。"))
)},
]
},
# ---- 3.4 定积分的几何应用 ----
{
"name": "3.4 定积分的几何应用",
"color": "#14b8a6",
"desc": "平面图形面积、旋转体体积、弧长、旋转体侧面积",
"items": [
{"id":"c3s4-1","name":"平面图形的面积","tags":["thm","der","exa"],"brief":"直角坐标与极坐标下的面积公式。",
 "body": wrap(
    thm("直角坐标下的面积", p("<strong>X 型：</strong>由 $y=f_1(x),y=f_2(x)$（$f_2\\ge f_1$）及 $x=a,x=b$ 围成的面积")+
    fml("A = \\int_a^b [f_2(x)-f_1(x)]\\,dx",
        "<strong>Y 型：</strong>$A=\\int_c^d [\\varphi_2(y)-\\varphi_1(y)]\\,dy$。"))
    + thm("极坐标下的面积", p("由曲线 $r=r(\\theta)$ 及射线 $\\theta=\\alpha,\\theta=\\beta$ 围成的曲边扇形面积")+
    fml("A = \\frac{1}{2}\\int_\\alpha^\\beta r^2(\\theta)\\,d\\theta"))
    + der(p("<strong>极坐标面积公式推导：</strong>将 $[\\alpha,\\beta]$ 分割，第 $i$ 个小曲边扇形用半径为 $r(\\theta_i)$、圆心角为 $\\Delta\\theta_i$ 的圆扇形近似，面积 $\\Delta A_i\\approx\\frac{1}{2}r^2(\\theta_i)\\Delta\\theta_i$。取极限即得 $A=\\frac{1}{2}\\int_\\alpha^\\beta r^2(\\theta)\\,d\\theta$。"))
    + exa(p("<strong>例：</strong>求心形线 $r=a(1+\\cos\\theta)$ 围成的面积。$A=\\frac{1}{2}\\int_0^{2\\pi}a^2(1+\\cos\\theta)^2\\,d\\theta=\\frac{a^2}{2}\\int_0^{2\\pi}(1+2\\cos\\theta+\\cos^2\\theta)\\,d\\theta=\\frac{a^2}{2}\\cdot 3\\pi=\\frac{3\\pi a^2}{2}$。"))
)},
{"id":"c3s4-2","name":"旋转体的体积","tags":["thm","der","exa"],"brief":"圆盘法与柱壳法。",
 "body": wrap(
    thm("圆盘法（绕 $x$ 轴）", p("曲线 $y=f(x)$（$a\\le x\\le b$）绕 $x$ 轴旋转一周的体积")+
    fml("V = \\pi\\int_a^b f^2(x)\\,dx",
        "若在两条曲线 $y=f_1(x),y=f_2(x)$ 之间，则 $V=\\pi\\int_a^b[f_2^2(x)-f_1^2(x)]\\,dx$。"))
    + der(p("<strong>圆盘法推导：</strong>垂直于 $x$ 轴切取厚度为 $dx$ 的薄片，近似为半径 $f(x)$、高 $dx$ 的圆柱，体积 $dV=\\pi f^2(x)\\,dx$，积分得总体积。"))
    + thm("柱壳法（绕 $y$ 轴）", p("曲线 $y=f(x)$（$a\\le x\\le b$）绕 $y$ 轴旋转的体积")+
    fml("V = 2\\pi\\int_a^b x\\,f(x)\\,dx",
        "柱壳半径为 $x$，高度为 $f(x)$，厚度 $dx$，侧面积 $2\\pi x\\cdot f(x)$，体积 $dV=2\\pi x f(x)\\,dx$。"))
    + exa(p("<strong>例：</strong>求 $y=x^2$，$x=0,1$，$y=0$ 围成图形绕 $x$ 轴旋转的体积。$V=\\pi\\int_0^1 x^4\\,dx=\\frac{\\pi}{5}$。<br>绕 $y$ 轴旋转（柱壳法）：$V=2\\pi\\int_0^1 x\\cdot x^2\\,dx=2\\pi\\cdot\\frac{1}{4}=\\frac{\\pi}{2}$。"))
)},
{"id":"c3s4-3","name":"平面曲线的弧长与旋转体侧面积","tags":["thm","der","exa"],"brief":"弧长公式与旋转曲面面积公式。",
 "body": wrap(
    thm("弧长公式", p("")+
    fml("\\text{参数方程 }x=\\varphi(t),y=\\psi(t):\\quad s = \\int_\\alpha^\\beta\\sqrt{\\varphi'(t)^2+\\psi'(t)^2}\\,dt",
        "直角坐标 $y=y(x)$：$s=\\int_a^b\\sqrt{1+y'^2}\\,dx$；极坐标 $r=r(\\theta)$：$s=\\int_\\alpha^\\beta\\sqrt{r^2+r'^2}\\,d\\theta$。"))
    + der(p("<strong>弧长公式推导：</strong>弧微分 $ds=\\sqrt{(dx)^2+(dy)^2}$。参数方程下 $dx=\\varphi'(t)dt$，$dy=\\psi'(t)dt$，故 $ds=\\sqrt{\\varphi'(t)^2+\\psi'(t)^2}\\,dt$。弧长是弧微分的积分。"))
    + thm("旋转体侧面积", p("曲线 $y=f(x)$（$a\\le x\\le b$，$f(x)\\ge 0$）绕 $x$ 轴旋转所得曲面的面积")+
    fml("S = 2\\pi\\int_a^b f(x)\\sqrt{1+f'^2(x)}\\,dx",
        "参数方程形式：$S=2\\pi\\int_\\alpha^\\beta \\psi(t)\\sqrt{\\varphi'(t)^2+\\psi'(t)^2}\\,dt$。"))
    + der(p("<strong>侧面积公式推导：</strong>在弧长 $ds$ 上截取一小段，绕 $x$ 轴旋转得圆台侧面，侧面积近似为 $2\\pi f(x)\\cdot ds$（圆台侧面积 $=\\pi(r_1+r_2)l\\approx 2\\pi f(x)ds$），故 $dS=2\\pi f(x)\\sqrt{1+f'^2(x)}\\,dx$。"))
    + exa(p("<strong>例：</strong>求半径为 $R$ 的球面面积。上半圆 $y=\\sqrt{R^2-x^2}$ 绕 $x$ 轴旋转。$y'=-\\frac{x}{y}$，$\\sqrt{1+y'^2}=\\frac{R}{y}$。$S=2\\pi\\int_{-R}^R y\\cdot\\frac{R}{y}\\,dx=2\\pi R\\int_{-R}^R dx=4\\pi R^2$。"))
)},
]
},
# ---- 3.5 反常积分 ----
{
"name": "3.5 反常积分",
"color": "#14b8a6",
"desc": "无穷限与无界函数反常积分，收敛判别",
"items": [
{"id":"c3s5-1","name":"反常积分的定义","tags":["def","thm","exa"],"brief":"无穷限与瑕积分。",
 "body": wrap(
    defn("无穷限反常积分", p("$\\int_a^{+\\infty}f(x)\\,dx=\\lim_{b\\to+\\infty}\\int_a^b f(x)\\,dx$，若极限存在则称反常积分收敛，否则发散。类似定义 $\\int_{-\\infty}^b$ 和 $\\int_{-\\infty}^{+\\infty}$。"))
    + defn("无界函数反常积分（瑕积分）", p("若 $f$ 在 $x=a$ 无界（瑕点），则 $\\int_a^b f(x)\\,dx=\\lim_{\\varepsilon\\to 0^+}\\int_{a+\\varepsilon}^b f(x)\\,dx$。"))
    + exa(p("<strong>p 积分：</strong>$\\int_1^{+\\infty}\\frac{dx}{x^p}$ 当 $p>1$ 收敛，$p\\le 1$ 发散。<br>$\\int_0^1\\frac{dx}{x^p}$ 当 $p<1$ 收敛，$p\\ge 1$ 发散。"))
)},
{"id":"c3s5-2","name":"反常积分收敛判别法","tags":["thm","app"],"brief":"比较判别法、狄利克雷与阿贝尔判别。",
 "body": wrap(
    thm("比较判别法", p("设 $0\\le f(x)\\le g(x)$（$x\\ge a$）。若 $\\int_a^{+\\infty}g\\,dx$ 收敛，则 $\\int_a^{+\\infty}f\\,dx$ 收敛；若 $\\int_a^{+\\infty}f\\,dx$ 发散，则 $\\int_a^{+\\infty}g\\,dx$ 发散。<br><strong>极限形式：</strong>若 $\\lim_{x\\to+\\infty}\\frac{f(x)}{g(x)}=l$（$0<l<\\infty$），则两积分同敛散。"))
    + thm("狄利克雷判别法", p("若 $F(A)=\\int_a^A f(x)\\,dx$ 有界，$g(x)$ 单调趋于 0（$x\\to+\\infty$），则 $\\int_a^{+\\infty}f(x)g(x)\\,dx$ 收敛。"))
    + app(p("<strong>绝对收敛与条件收敛：</strong>若 $\\int |f|\\,dx$ 收敛，则 $\\int f\\,dx$ 收敛（绝对收敛）；若 $\\int f\\,dx$ 收敛但 $\\int |f|\\,dx$ 发散，称为条件收敛。狄利克雷判别常用于证明条件收敛。"))
)},
]
},
# ---- 3.6 有理函数积分与积分技巧 ----
{
"name": "3.6 有理函数积分与积分技巧",
"color": "#059669",
"desc": "部分分式分解、有理函数积分、可有理化的积分",
"items": [
{"id":"c3s6-1","name":"有理函数的积分","tags":["thm","der","exa"],"brief":"部分分式分解法。",
 "body": wrap(
    thm("部分分式分解", p("有理函数 $R(x)=\\frac{P(x)}{Q(x)}$（真分式）可分解为四类简单分式之和：<br>(1) $\\frac{A}{x-a}$；(2) $\\frac{A}{(x-a)^k}$；(3) $\\frac{Bx+C}{x^2+px+q}$（$p^2-4q<0$）；(4) $\\frac{Bx+C}{(x^2+px+q)^k}$。<br>其中 $A,B,C$ 为待定系数。"))
    + der(p("<strong>待定系数法：</strong>设分解式后通分，分子多项式恒等，比较同次幂系数或代入特殊 $x$ 值求解。<br>例如 $\\frac{1}{x^2-1}=\\frac{A}{x-1}+\\frac{B}{x+1}$，通分后分子 $1=A(x+1)+B(x-1)$。令 $x=1$ 得 $A=1/2$；令 $x=-1$ 得 $B=-1/2$。故 $\\frac{1}{x^2-1}=\\frac{1}{2}\\left(\\frac{1}{x-1}-\\frac{1}{x+1}\\right)$。"))
    + exa(p("<strong>例：</strong>求 $\\int\\frac{dx}{x^3+1}$。<br>$x^3+1=(x+1)(x^2-x+1)$，设 $\\frac{1}{x^3+1}=\\frac{A}{x+1}+\\frac{Bx+C}{x^2-x+1}$。通分比较得 $A=1/3$，$B=-1/3$，$C=2/3$。<br>$\\int\\frac{dx}{x^3+1}=\\frac{1}{3}\\ln|x+1|-\\frac{1}{6}\\ln(x^2-x+1)+\\frac{1}{\\sqrt{3}}\\arctan\\frac{2x-1}{\\sqrt{3}}+C$。<br>其中 $\\int\\frac{-x/3+2/3}{x^2-x+1}dx$ 需拆为含分子分母导数的项与配方后 $\\arctan$ 的项。"))
)},
{"id":"c3s6-2","name":"可化为有理函数的积分","tags":["thm","exa","app"],"brief":"三角有理式与简单无理函数的积分。",
 "body": wrap(
    thm("三角有理式的积分", p("对 $\\int R(\\sin x,\\cos x)\\,dx$，用<strong>万能代换</strong> $t=\\tan\\frac{x}{2}$，则")+
    fml("\\sin x=\\frac{2t}{1+t^2},\\quad \\cos x=\\frac{1-t^2}{1+t^2},\\quad dx=\\frac{2}{1+t^2}\\,dt",
        "化为 $t$ 的有理函数积分。虽万能，但计算量大，应优先考虑更简便的代换。"))
    + thm("简单无理函数的积分", p("<br>(1) $\\int R(x,\\sqrt[n]{ax+b})\\,dx$：令 $t=\\sqrt[n]{ax+b}$；<br>(2) $\\int R(x,\\sqrt{ax^2+bx+c})\\,dx$：先配方化为 $\\sqrt{u^2\\pm a^2}$ 或 $\\sqrt{a^2-u^2}$，再用三角代换；<br>(3) $\\int R(x,\\sqrt{\\frac{ax+b}{cx+d}})\\,dx$：令 $t=\\sqrt{\\frac{ax+b}{cx+d}}$。"))
    + exa(p("<strong>例：</strong>求 $\\int\\frac{\\sin x}{\\sin x+\\cos x}\\,dx$。<br>方法一（万能代换）：令 $t=\\tan\\frac{x}{2}$，计算较繁。<br>方法二（技巧）：$\\frac{\\sin x}{\\sin x+\\cos x}=\\frac{1}{2}\\cdot\\frac{(\\sin x+\\cos x)-(\\cos x-\\sin x)}{\\sin x+\\cos x}=\\frac{1}{2}-\\frac{1}{2}\\cdot\\frac{(\\sin x+\\cos x)'}{\\sin x+\\cos x}$。<br>故积分 $=\\frac{x}{2}-\\frac{1}{2}\\ln|\\sin x+\\cos x|+C$。这展示了凑微分技巧的威力。"))
    + app(p("<strong>积分技巧总结：</strong>(1) 优先考虑能否直接用基本公式；(2) 看能否凑微分；(3) 考虑分部积分（特别是反三角、对数、乘积）；(4) 含根式用三角代换或倒代换；(5) 有理函数用部分分式；(6) 三角有理式考虑万能代换或恒等变形。"))
)},
]
},
]
print(f"Ch3: {sum(len(s['items']) for s in ch3_sections)} items")

# =====================================================
#  CHAPTER 4: 微分方程
# =====================================================
ch4_sections = [
# ---- 4.1 一阶微分方程 ----
{
"name": "4.1 一阶微分方程",
"color": "#c2410c",
"desc": "可分离变量、齐次、一阶线性、伯努利方程",
"items": [
{"id":"c4s1-1","name":"可分离变量方程","tags":["def","thm","exa"],"brief":"dy/dx=f(x)g(y) 型。",
 "body": wrap(
    defn("可分离变量方程", p("形如 $\\frac{dy}{dx}=f(x)g(y)$ 的一阶方程称为可分离变量方程。"))
    + thm("解法", p("分离变量得 $\\frac{dy}{g(y)}=f(x)\\,dx$，两边积分：")+
    fml("\\int \\frac{dy}{g(y)} = \\int f(x)\\,dx + C",
        "得到隐式通解。若 $g(y_0)=0$，则 $y=y_0$ 也是解（可能不在通解中）。"))
    + exa(p("<strong>例：</strong>$\\frac{dy}{dx}=\\frac{y}{x}$。分离变量 $\\frac{dy}{y}=\\frac{dx}{x}$，积分得 $\\ln|y|=\\ln|x|+C_1$，即 $y=Cx$。"))
)},
{"id":"c4s1-2","name":"一阶线性微分方程","tags":["def","thm","der","exa"],"brief":"y'+P(x)y=Q(x) 的通解公式。",
 "body": wrap(
    defn("一阶线性微分方程", p("形如 $y'+P(x)y=Q(x)$ 的方程称为一阶线性微分方程。当 $Q(x)\\equiv 0$ 时称为齐次线性方程，否则称为非齐次线性方程。$P(x),Q(x)$ 为已知连续函数。"))
    + thm("一阶线性方程通解公式", p("方程 $y'+P(x)y=Q(x)$ 的通解为")+
    fml("y = e^{-\\int P(x)\\,dx}\\left(\\int Q(x)e^{\\int P(x)\\,dx}\\,dx + C\\right)"))
    + der(p("<strong>推导（常数变易法）：</strong>先解齐次方程 $y'+P(x)y=0$，得 $y=Ce^{-\\int P(x)\\,dx}$。<br>将常数 $C$ 变易为函数 $C(x)$，代入非齐次方程：")+
    fml("C'(x)e^{-\\int P\\,dx} - C(x)P(x)e^{-\\int P\\,dx} + P(x)C(x)e^{-\\int P\\,dx} = Q(x)",
        "化简得 $C'(x)=Q(x)e^{\\int P(x)\\,dx}$，积分得 $C(x)=\\int Q(x)e^{\\int P\\,dx}\\,dx+C$，代回即得通解。"))
)},
{"id":"c4s1-3","name":"齐次方程与伯努利方程","tags":["def","thm","exa"],"brief":"可化为变量分离或线性的方程。",
 "body": wrap(
    defn("齐次方程", p("形如 $\\frac{dy}{dx}=\\varphi\\left(\\frac{y}{x}\\right)$ 的一阶方程称为<strong>齐次方程</strong>。其右端是以 $\\frac{y}{x}$ 为变量的函数。"))
    + thm("齐次方程的解法", p("令 $u=\\frac{y}{x}$（即 $y=ux$），则 $\\frac{dy}{dx}=u+x\\frac{du}{dx}$，代入原方程得 $x\\frac{du}{dx}=\\varphi(u)-u$，这是可分离变量方程。解出 $u(x)$ 后回代 $y=xu(x)$ 即得通解。"))
    + defn("伯努利方程", p("形如 $y'+P(x)y=Q(x)y^n$（$n\\ne 0,1$）的方程称为<strong>伯努利方程</strong>。当 $n=0$ 时为线性方程，$n=1$ 时为可分离变量方程。"))
    + thm("伯努利方程的解法", p("令 $z=y^{1-n}$，则 $z'=(1-n)y^{-n}y'$，方程两边乘 $(1-n)y^{-n}$ 后化为一阶线性方程：")+
    fml("z' + (1-n)P(x)z = (1-n)Q(x)"))
    + exa(p("<strong>例：</strong>$y'-y=xy^2$。令 $z=y^{-1}$，则 $z'=-y^{-2}y'$，方程化为 $-z'-z=x$，即 $z'+z=-x$。由通解公式 $z=e^{-x}(\\int -xe^x dx+C)=e^{-x}(-xe^x+e^x+C)=-x+1+Ce^{-x}$，故 $y=\\frac{1}{1-x+Ce^{-x}}$。"))
)},
]
},
# ---- 4.2 可降阶高阶方程 ----
{
"name": "4.2 可降阶高阶方程",
"color": "#ea580c",
"desc": "不显含 y、不显含 x 的高阶方程",
"items": [
{"id":"c4s2-1","name":"可降阶的高阶方程","tags":["def","thm","exa"],"brief":"三种特殊类型的降阶方法。",
 "body": wrap(
    defn("类型一：$y^{(n)}=f(x)$", p("右端仅含自变量 $x$ 的 $n$ 阶方程。"))
    + thm("类型一解法", p("直接积分 $n$ 次，每次积分引入一个任意常数。"))
    + defn("类型二：$y''=f(x,y')$（不显含 $y$）", p("方程中不显含未知函数 $y$。"))
    + thm("类型二解法", p("令 $p=y'$，则 $y''=p'$，方程化为一阶方程 $p'=f(x,p)$。解出 $p(x)$ 后再积分得 $y=\\int p(x)\\,dx+C$。"))
    + defn("类型三：$y''=f(y,y')$（不显含 $x$）", p("方程中不显含自变量 $x$。"))
    + thm("类型三解法", p("令 $p=y'$，视 $p$ 为 $y$ 的函数，则 $y''=\\frac{dp}{dx}=\\frac{dp}{dy}\\cdot\\frac{dy}{dx}=p\\frac{dp}{dy}$，方程化为一阶方程 $p\\frac{dp}{dy}=f(y,p)$。"))
    + exa(p("<strong>例（类型三）：</strong>$y''+\\omega^2 y=0$。令 $p=y'$，则 $y''=p\\frac{dp}{dy}$，方程为 $p\\frac{dp}{dy}+\\omega^2 y=0$，即 $p\\,dp=-\\omega^2 y\\,dy$。积分得 $\\frac{1}{2}p^2=-\\frac{1}{2}\\omega^2 y^2+C_1$，即 $p=\\pm\\sqrt{C_1-\\omega^2 y^2}$。分离变量积分：$\\frac{dy}{\\sqrt{C_1-\\omega^2 y^2}}=\\pm dx$，得 $\\arcsin(\\frac{\\omega y}{\\sqrt{C_1}})=\\pm\\omega x+C_2$，即 $y=A\\sin(\\omega x+\\varphi)$。"))
)},
]
},
# ---- 4.3 高阶线性微分方程 ----
{
"name": "4.3 高阶线性微分方程",
"color": "#f97316",
"desc": "二阶常系数线性方程的解法",
"items": [
{"id":"c4s3-1","name":"线性方程解的结构","tags":["thm","note"],"brief":"齐次与非齐次解的叠加。",
 "body": wrap(
    thm("解的结构定理", p("<strong>齐次线性方程：</strong>$y^{(n)}+a_1(x)y^{(n-1)}+\\cdots+a_n(x)y=0$ 的 $n$ 个线性无关解 $y_1,\\dots,y_n$ 构成基本解组，通解为 $y=C_1 y_1+\\cdots+C_n y_n$。<br><strong>非齐次线性方程：</strong>通解 = 对应齐次方程通解 + 非齐次方程一个特解：$y=\\bar y+y^*$。"))
    + note(p("判断 $n$ 个解线性无关可用朗斯基行列式 $W(y_1,\\dots,y_n)=\\det(y_i^{(j-1)})$：$W\\ne 0$ $\\Leftrightarrow$ 线性无关。"))
)},
{"id":"c4s3-2","name":"二阶常系数齐次线性方程","tags":["thm","der","exa"],"brief":"特征方程法。",
 "body": wrap(
    thm("特征方程法", p("方程 $y''+py'+qy=0$（$p,q$ 为常数）的特征方程为 $r^2+pr+q=0$，设根为 $r_1,r_2$：<br>(1) <strong>两个不相等实根</strong> $r_1\\ne r_2$：通解 $y=C_1 e^{r_1 x}+C_2 e^{r_2 x}$；<br>(2) <strong>两个相等实根</strong> $r_1=r_2=r$：通解 $y=(C_1+C_2 x)e^{rx}$；<br>(3) <strong>一对共轭复根</strong> $r=\\alpha\\pm\\beta i$：通解 $y=e^{\\alpha x}(C_1\\cos\\beta x+C_2\\sin\\beta x)$。"))
    + der(p("<strong>重根情形推导：</strong>若 $r_1=r_2=r$，则 $y_1=e^{rx}$ 是一个解。用降阶法设 $y_2=u(x)e^{rx}$，代入方程得 $u''=0$，故 $u=x$（取非常数解），$y_2=xe^{rx}$。朗斯基行列式 $W(e^{rx},xe^{rx})=e^{2rx}\\ne 0$，故两解线性无关。"))
)},
{"id":"c4s3-3","name":"二阶常系数非齐次线性方程","tags":["thm","exa"],"brief":"待定系数法求特解。",
 "body": wrap(
    thm("待定系数法", p("方程 $y''+py'+qy=f(x)$。根据 $f(x)$ 的形式设特解：<br>(1) $f(x)=P_m(x)e^{\\lambda x}$：设 $y^*=x^k Q_m(x)e^{\\lambda x}$，$k$ 为 $\\lambda$ 是特征根的重数；<br>(2) $f(x)=e^{\\alpha x}[P_l(x)\\cos\\beta x+P_n(x)\\sin\\beta x]$：设 $y^*=x^k e^{\\alpha x}[R_m\\cos\\beta x+S_m\\sin\\beta x]$，$k$ 为 $\\alpha+\\beta i$ 是特征根的重数。"))
    + exa(p("<strong>例：</strong>$y''-3y'+2y=e^x$。特征方程 $r^2-3r+2=0$，根 $r_1=1,r_2=2$。$\\lambda=1$ 是单根，设 $y^*=Axe^x$。代入得 $A=-1$，故 $y^*=-xe^x$。通解 $y=C_1 e^x+C_2 e^{2x}-xe^x$。"))
)},
]
},
# ---- 4.4 微分方程应用 ----
{
"name": "4.4 微分方程应用",
"color": "#fb923c",
"desc": "RLC电路、弹簧振子、人口模型",
"items": [
{"id":"c4s4-1","name":"弹簧振子与阻尼振动","tags":["exa","app"],"brief":"二阶常系数方程的物理原型。",
 "body": wrap(
    exa(p("<strong>弹簧振子：</strong>质量 $m$ 的物体连在弹簧常数 $k$ 的弹簧上，阻尼系数 $c$，运动方程为")+
    fml("m\\ddot x + c\\dot x + kx = 0 \\quad\\Longleftrightarrow\\quad \\ddot x + 2\\beta\\dot x + \\omega_0^2 x = 0",
        "其中 $2\\beta=c/m$，$\\omega_0^2=k/m$。特征方程 $r^2+2\\beta r+\\omega_0^2=0$。"))
    + app(p("<strong>三种情形：</strong><br>(1) 欠阻尼（$\\beta<\\omega_0$）：$x=Ae^{-\\beta t}\\cos(\\omega t+\\varphi)$，$\\omega=\\sqrt{\\omega_0^2-\\beta^2}$，振幅衰减的振动；<br>(2) 临界阻尼（$\\beta=\\omega_0$）：$x=(C_1+C_2 t)e^{-\\beta t}$，最快回到平衡位置不振荡；<br>(3) 过阻尼（$\\beta>\\omega_0$）：$x=C_1 e^{r_1 t}+C_2 e^{r_2 t}$，缓慢回到平衡。"))
)},
{"id":"c4s4-2","name":"RLC 电路与人口模型","tags":["exa","app"],"brief":"电路方程与指数/逻辑增长。",
 "body": wrap(
    exa(p("<strong>RLC 串联电路：</strong>由基尔霍夫电压定律，$L\\frac{di}{dt}+Ri+\\frac{q}{C}=E(t)$，即")+
    fml("L\\ddot q + R\\dot q + \\frac{1}{C}q = E(t)",
        "这是二阶常系数线性方程，与弹簧振子方程数学结构完全相同（机电类比：$L\\leftrightarrow m$，$R\\leftrightarrow c$，$1/C\\leftrightarrow k$）。"))
    + app(p("<strong>马尔萨斯人口模型：</strong>$\\frac{dN}{dt}=rN$，解 $N=N_0 e^{rt}$，指数增长。<br><strong>逻辑增长模型（Logistic）：</strong>$\\frac{dN}{dt}=rN(1-\\frac{N}{K})$，分离变量解得 $N=\\frac{K}{1+(\\frac{K}{N_0}-1)e^{-rt}}$，呈 S 型曲线，$K$ 为环境容量。"))
)},
]
},
# ---- 4.5 欧拉方程与解的存在唯一性 ----
{
"name": "4.5 欧拉方程与解的存在唯一性",
"color": "#c2410c",
"desc": "欧拉方程、常数变易法、皮卡存在唯一性定理",
"items": [
{"id":"c4s5-1","name":"欧拉方程","tags":["thm","der","exa"],"brief":"变系数方程中可化为常系数的特例。",
 "body": wrap(
    defn("欧拉方程", p("形如")+
    fml("x^n y^{(n)}+a_1 x^{n-1}y^{(n-1)}+\\cdots+a_{n-1}xy'+a_n y = f(x)",
        "的变系数线性方程称为<strong>欧拉方程</strong>。其特点是 $x^k$ 的幂次与导数阶数相同。"))
    + der(p("<strong>解法（自变量代换）：</strong>令 $x=e^t$（即 $t=\\ln x$，$x>0$），则 $\\frac{dy}{dx}=\\frac{1}{x}\\frac{dy}{dt}$，$\\frac{d^2y}{dx^2}=\\frac{1}{x^2}\\left(\\frac{d^2y}{dt^2}-\\frac{dy}{dt}\\right)$，$\\frac{d^3y}{dx^3}=\\frac{1}{x^3}\\left(\\frac{d^3y}{dt^3}-3\\frac{d^2y}{dt^2}+2\\frac{dy}{dt}\\right)$，等等。代入后化为以 $t$ 为自变量的<strong>常系数</strong>线性方程，求解后回代 $t=\\ln x$。<br>对二阶欧拉方程 $x^2 y''+axy'+by=0$，也可直接设 $y=x^r$，代入得特征方程 $r(r-1)+ar+b=0$，解得 $r$ 后写出通解。"))
    + exa(p("<strong>例：</strong>解 $x^2 y''+xy'-y=0$。设 $y=x^r$，特征方程 $r(r-1)+r-1=r^2-1=0$，$r=\\pm 1$。通解 $y=C_1 x+\\frac{C_2}{x}$。"))
)},
{"id":"c4s5-2","name":"常数变易法与解的存在唯一性","tags":["thm","der","app"],"brief":"非齐次方程的通解求法与皮卡定理。",
 "body": wrap(
    thm("常数变易法（一阶线性）", p("对 $y'+P(x)y=Q(x)$，先求齐次解 $y=Ce^{-\\int P\\,dx}$，将 $C$ 改为 $C(x)$ 代入非齐次方程，得 $C'(x)=Q(x)e^{\\int P\\,dx}$，故")+
    fml("y = e^{-\\int P\\,dx}\\left(\\int Q(x)e^{\\int P\\,dx}\\,dx + C\\right)",
        "这就是通解公式。常数变易法的思想是：把齐次解中的常数视为待定函数，使其满足非齐次方程。"))
    + thm("常数变易法（二阶非齐次）", p("设 $y''+P(x)y'+Q(x)y=f(x)$ 的齐次通解为 $Y=C_1 y_1+C_2 y_2$，令非齐次特解 $y^*=C_1(x)y_1+C_2(x)y_2$，其中 $C_1',C_2'$ 满足方程组：")+
    fml("\\begin{cases} C_1' y_1 + C_2' y_2 = 0 \\\\ C_1' y_1' + C_2' y_2' = f(x) \\end{cases}",
        "由朗斯基行列式 $W(y_1,y_2)\\ne 0$ 可唯一解出 $C_1',C_2'$，积分得 $C_1,C_2$。"))
    + thm("皮卡存在唯一性定理", p("若 $f(x,y)$ 在矩形区域 $R:\\,|x-x_0|\\le a,\\,|y-y_0|\\le b$ 上连续，且关于 $y$ 满足利普希茨条件 $|f(x,y_1)-f(x,y_2)|\\le L|y_1-y_2|$，则初值问题 $y'=f(x,y),\\,y(x_0)=y_0$ 在 $|x-x_0|\\le h$ 上存在唯一解（$h=\\min(a,b/M)$，$M=\\max_R|f|$）。"))
    + app(p("<strong>皮卡迭代：</strong>唯一性定理的证明构造皮卡迭代序列 $y_{n+1}(x)=y_0+\\int_{x_0}^x f(t,y_n(t))\\,dt$，证明其一致收敛到解。这是数值求解微分方程（如改进欧拉法、龙格-库塔法）的理论基础。"))
)},
]
},
]
print(f"Ch4: {sum(len(s['items']) for s in ch4_sections)} items")

# =====================================================
#  CHAPTER 5: 多元微分
# =====================================================
ch5_sections = [
# ---- 5.1 多元函数极限与连续 ----
{
"name": "5.1 多元函数极限与连续",
"color": "#7c3aed",
"desc": "重极限、累次极限、连续性",
"items": [
{"id":"c5s1-1","name":"多元函数的极限","tags":["def","thm","note"],"brief":"重极限与累次极限的区别。",
 "body": wrap(
    defn("二重极限", p("设 $z=f(x,y)$ 在 $(x_0,y_0)$ 的去心邻域有定义。若对任意 $\\varepsilon>0$，存在 $\\delta>0$，当 $0<\\sqrt{(x-x_0)^2+(y-y_0)^2}<\\delta$ 时 $|f(x,y)-A|<\\varepsilon$，则称 $A$ 为 $f$ 在 $(x_0,y_0)$ 的二重极限，记作 $\\lim_{(x,y)\\to(x_0,y_0)}f(x,y)=A$。"))
    + thm("重极限存在的条件", p("二重极限存在 $\\Leftrightarrow$ 点 $(x,y)$ 以<strong>任意方式</strong>趋于 $(x_0,y_0)$ 时，$f(x,y)$ 都趋于同一常数 $A$。<br>若沿两条不同路径极限不同，则重极限不存在。"))
    + note(p("<strong>重极限与累次极限的关系：</strong>累次极限 $\\lim_{x\\to x_0}\\lim_{y\\to y_0}f(x,y)$ 是先固定 $x$ 令 $y\\to y_0$，再令 $x\\to x_0$。<br>重极限存在时累次极限未必存在；两个累次极限存在且相等时重极限也未必存在。但重极限和累次极限都存在时，三者相等。"))
)},
{"id":"c5s1-2","name":"多元连续函数","tags":["def","thm","app"],"brief":"连续定义与闭区域连续函数性质。",
 "body": wrap(
    defn("连续", p("$f(x,y)$ 在 $(x_0,y_0)$ 连续 $\\Leftrightarrow$ $\\lim_{(x,y)\\to(x_0,y_0)}f(x,y)=f(x_0,y_0)$。"))
    + thm("有界闭区域上连续函数的性质", p("与一元函数类似：有界性、最值定理、介值定理。多元初等函数在其定义域内连续。"))
)},
]
},
# ---- 5.2 偏导数与全微分 ----
{
"name": "5.2 偏导数与全微分",
"color": "#8b5cf6",
"desc": "偏导数、全微分、可微条件",
"items": [
{"id":"c5s2-1","name":"偏导数","tags":["def","thm","der"],"brief":"固定其他变量对一个变量求导。",
 "body": wrap(
    defn("偏导数", p("$z=f(x,y)$ 对 $x$ 的偏导数定义为")+
    fml("\\frac{\\partial f}{\\partial x} = \\lim_{\\Delta x\\to 0}\\frac{f(x+\\Delta x,y)-f(x,y)}{\\Delta x}",
        "即固定 $y$，将 $f$ 视为 $x$ 的一元函数求导。几何意义：曲面 $z=f(x,y)$ 被平面 $y=y_0$ 截得的曲线在 $x=x_0$ 处的切线斜率。"))
    + thm("混合偏导数相等", p("若 $f_{xy}$ 和 $f_{yx}$ 在区域 $D$ 内连续，则在 $D$ 内 $f_{xy}=f_{yx}$。"))
    + der(p("<strong>推导思路：</strong>考虑增量 $\\Delta f=f(x+h,y+k)-f(x+h,y)-f(x,y+k)+f(x,y)$，用两种方式应用一元中值定理，一种得到 $f_{xy}$，另一种得到 $f_{yx}$，由连续性二者相等。"))
)},
{"id":"c5s2-2","name":"全微分","tags":["def","thm","der","note"],"brief":"可微的定义与充分条件。",
 "body": wrap(
    defn("全微分", p("若 $z=f(x,y)$ 的全增量 $\\Delta z=f(x+\\Delta x,y+\\Delta y)-f(x,y)$ 可表示为")+
    fml("\\Delta z = A\\Delta x + B\\Delta y + o(\\rho),\\quad \\rho=\\sqrt{(\\Delta x)^2+(\\Delta y)^2}",
        "则称 $f$ 在 $(x,y)$ 可微，$dz=A\\Delta x+B\\Delta y$ 为全微分。"))
    + thm("可微的必要与充分条件", p("<strong>必要条件：</strong>若 $f$ 可微，则 $f_x,f_y$ 存在，且 $dz=f_x\\,dx+f_y\\,dy$。<br><strong>充分条件：</strong>若 $f_x,f_y$ 在 $(x,y)$ 连续，则 $f$ 在 $(x,y)$ 可微。"))
    + der(p("<strong>必要条件证明：</strong>在 $\\Delta z=A\\Delta x+B\\Delta y+o(\\rho)$ 中令 $\\Delta y=0$，得 $\\Delta z_x=A\\Delta x+o(|\\Delta x|)$，故 $f_x=\\lim_{\\Delta x\\to 0}\\frac{\\Delta z_x}{\\Delta x}=A$。同理 $f_y=B$。"))
    + note(p("多元函数中，偏导数存在不能推出连续，也不能推出可微；偏导数连续才能推出可微。这是与一元函数（可导$\\Rightarrow$连续，可导$\\Leftrightarrow$可微）的重要区别。"))
    + note(p("<strong>几何意义：</strong>若 $z=f(x,y)$ 在 $(x_0,y_0)$ 可微，则曲面 $z=f(x,y)$ 在点 $(x_0,y_0,f(x_0,y_0))$ 处存在<strong>切平面</strong>，其方程为")+
    fml("z - z_0 = f_x(x_0,y_0)(x-x_0) + f_y(x_0,y_0)(y-y_0)",
        "全微分 $dz=f_x\\,dx+f_y\\,dy$ 正是切平面上的增量，是曲面增量 $\\Delta z$ 的线性主部（最佳线性逼近）。"))
)},
]
},
# ---- 5.3 复合函数与隐函数微分 ----
{
"name": "5.3 复合函数与隐函数微分",
"color": "#a855f7",
"desc": "链式法则、隐函数求导、雅可比行列式",
"items": [
{"id":"c5s3-1","name":"多元复合函数求导","tags":["thm","der","exa"],"brief":"链式法则的各种情形。",
 "body": wrap(
    thm("链式法则", p("若 $z=f(u,v)$，$u=u(x,y)$，$v=v(x,y)$ 都可微，则")+
    fml("\\frac{\\partial z}{\\partial x} = \\frac{\\partial z}{\\partial u}\\frac{\\partial u}{\\partial x} + \\frac{\\partial z}{\\partial v}\\frac{\\partial v}{\\partial x},\\quad \\frac{\\partial z}{\\partial y} = \\frac{\\partial z}{\\partial u}\\frac{\\partial u}{\\partial y} + \\frac{\\partial z}{\\partial v}\\frac{\\partial v}{\\partial y}",
        "口诀：<strong>连线相乘，分线相加</strong>。"))
    + exa(p("<strong>极坐标变换：</strong>$z=f(x,y)$，$x=r\\cos\\theta$，$y=r\\sin\\theta$。则")+
    fml("\\frac{\\partial z}{\\partial r} = \\frac{\\partial z}{\\partial x}\\cos\\theta + \\frac{\\partial z}{\\partial y}\\sin\\theta,\\quad \\frac{\\partial z}{\\partial\\theta} = -\\frac{\\partial z}{\\partial x}r\\sin\\theta + \\frac{\\partial z}{\\partial y}r\\cos\\theta"))
)},
{"id":"c5s3-2","name":"隐函数与雅可比行列式","tags":["thm","der"],"brief":"隐函数存在定理与雅可比。",
 "body": wrap(
    thm("隐函数存在定理", p("设 $F(x,y,z)$ 在 $(x_0,y_0,z_0)$ 邻域有连续偏导数，$F(x_0,y_0,z_0)=0$，$F_z(x_0,y_0,z_0)\\ne 0$，则方程 $F(x,y,z)=0$ 在 $(x_0,y_0)$ 邻域唯一确定隐函数 $z=z(x,y)$，且")+
    fml("\\frac{\\partial z}{\\partial x} = -\\frac{F_x}{F_z},\\quad \\frac{\\partial z}{\\partial y} = -\\frac{F_y}{F_z}"))
    + thm("雅可比行列式", p("设 $u=u(x,y)$，$v=v(x,y)$，雅可比行列式")+
    fml("J = \\frac{\\partial(u,v)}{\\partial(x,y)} = \\begin{vmatrix}u_x & u_y \\\\ v_x & v_y\\end{vmatrix}",
        "若 $J\\ne 0$，则变换 $(x,y)\\leftrightarrow(u,v)$ 可逆，且 $\\frac{\\partial(x,y)}{\\partial(u,v)}=\\frac{1}{J}$。"))
)},
]
},
# ---- 5.4 多元极值与条件极值 ----
{
"name": "5.4 多元极值与条件极值",
"color": "#c026d3",
"desc": "无条件极值、拉格朗日乘数法",
"items": [
{"id":"c5s4-1","name":"多元函数极值","tags":["def","thm","der"],"brief":"极值的必要与充分条件。",
 "body": wrap(
    defn("极值", p("若 $f$ 在 $(x_0,y_0)$ 某邻域内 $f(x,y)\\le f(x_0,y_0)$（或 $\\ge$），则 $f(x_0,y_0)$ 为极大（小）值。"))
    + thm("极值判据", p("<strong>必要条件：</strong>$f$ 在 $(x_0,y_0)$ 可微且取极值 $\\Rightarrow$ $f_x(x_0,y_0)=f_y(x_0,y_0)=0$（驻点）。<br><strong>充分条件：</strong>设 $f$ 在驻点 $(x_0,y_0)$ 有二阶连续偏导数，记 $A=f_{xx}$，$B=f_{xy}$，$C=f_{yy}$，$\\Delta=AC-B^2$：<br>(1) $\\Delta>0$ 且 $A>0$：极小值；<br>(2) $\\Delta>0$ 且 $A<0$：极大值；<br>(3) $\\Delta<0$：不是极值（鞍点）；<br>(4) $\\Delta=0$：无法判断。"))
)},
{"id":"c5s4-2","name":"条件极值与拉格朗日乘数法","tags":["thm","der","exa"],"brief":"带约束的极值问题。",
 "body": wrap(
    thm("拉格朗日乘数法", p("求 $f(x,y)$ 在约束 $\\varphi(x,y)=0$ 下的极值，构造拉格朗日函数")+
    fml("L(x,y,\\lambda) = f(x,y) + \\lambda\\,\\varphi(x,y)",
        "解方程组 $L_x=0$，$L_y=0$，$L_\\lambda=0$（即 $\\varphi=0$），得可能的极值点。"))
    + der(p("<strong>几何解释：</strong>在约束曲线 $\\varphi=0$ 上，$f$ 取极值的点处，$f$ 的梯度与 $\\varphi$ 的梯度平行，即 $\\nabla f=\\lambda\\nabla\\varphi$（$\\lambda$ 为比例常数）。这正是拉格朗日乘数法的来源。"))
    + exa(p("<strong>例：</strong>求 $f(x,y)=xy$ 在 $x+y=1$ 下的极值。$L=xy+\\lambda(x+y-1)$。$L_x=y+\\lambda=0$，$L_y=x+\\lambda=0$，得 $x=y=-\\lambda$。由 $x+y=1$ 得 $x=y=1/2$，极值 $f=1/4$（最大值）。"))
)},
]
},
# ---- 5.5 方向导数与梯度 ----
{
"name": "5.5 方向导数与梯度",
"color": "#7c3aed",
"desc": "方向导数定义、梯度的几何意义、梯度与方向导数的关系",
"items": [
{"id":"c5s5-1","name":"方向导数","tags":["def","thm","der"],"brief":"沿任意方向的变化率。",
 "body": wrap(
    defn("方向导数", p("设 $z=f(x,y)$ 在点 $P_0(x_0,y_0)$ 某邻域有定义，$\\vec l$ 为从 $P_0$ 出发的射线，方向余弦为 $(\\cos\\alpha,\\cos\\beta)$。若极限")+
    fml("\\frac{\\partial f}{\\partial l}\\bigg|_{P_0} = \\lim_{\\rho\\to 0^+}\\frac{f(x_0+\\rho\\cos\\alpha,y_0+\\rho\\cos\\beta)-f(x_0,y_0)}{\\rho}",
        "存在，则称其为 $f$ 在 $P_0$ 沿方向 $\\vec l$ 的<strong>方向导数</strong>。"))
    + thm("方向导数计算公式", p("若 $f$ 在 $P_0$ 可微，则 $f$ 在 $P_0$ 沿任意方向 $\\vec l$ 的方向导数存在，且")+
    fml("\\frac{\\partial f}{\\partial l} = f_x\\cos\\alpha + f_y\\cos\\beta",
        "三元函数：$\\frac{\\partial f}{\\partial l}=f_x\\cos\\alpha+f_y\\cos\\beta+f_z\\cos\\gamma$。"))
    + der(p("<strong>推导：</strong>由 $f$ 可微，$\\Delta f=f_x\\Delta x+f_y\\Delta y+o(\\rho)$，其中 $\\Delta x=\\rho\\cos\\alpha$，$\\Delta y=\\rho\\cos\\beta$。两边除以 $\\rho$ 并令 $\\rho\\to 0^+$，得 $\\frac{\\partial f}{\\partial l}=f_x\\cos\\alpha+f_y\\cos\\beta$。<br><strong>注意：</strong>可微是充分条件。偏导数存在但不可微时，方向导数公式不一定成立。"))
)},
{"id":"c5s5-2","name":"梯度及其性质","tags":["def","thm","app"],"brief":"梯度的定义、方向与模的意义。",
 "body": wrap(
    defn("梯度", p("函数 $f(x,y)$ 在点 $P_0$ 的梯度是一个向量，定义为")+
    fml("\\mathrm{grad}\\,f = \\nabla f = \\left(\\frac{\\partial f}{\\partial x},\\frac{\\partial f}{\\partial y}\\right)",
        "三元函数：$\\nabla f=(f_x,f_y,f_z)$。梯度方向是函数增长最快的方向。"))
    + thm("梯度与方向导数的关系", p("$\\frac{\\partial f}{\\partial l}=\\nabla f\\cdot\\vec l^0=|\\nabla f|\\cos\\theta$，其中 $\\vec l^0$ 为 $\\vec l$ 的单位向量，$\\theta$ 为 $\\nabla f$ 与 $\\vec l$ 的夹角。<br>故：<br>(1) 当 $\\theta=0$（$\\vec l$ 与梯度同向），方向导数最大，值为 $|\\nabla f|$；<br>(2) 当 $\\theta=\\pi$（反向），方向导数最小，值为 $-|\\nabla f|$；<br>(3) 当 $\\theta=\\pi/2$（正交），方向导数为 0。"))
    + der(p("<strong>梯度的几何意义：</strong>设曲面 $z=f(x,y)$，等值线 $f(x,y)=c$ 在 $P_0$ 处的切线方向为等值线方向。沿等值线方向，$f$ 值不变，故方向导数为 0，即 $\\nabla f\\cdot\\vec\\tau=0$。这说明<strong>梯度方向垂直于等值线的切线，即沿等值线的法线方向</strong>。梯度指向函数值增大的一侧。")+
    fml("\\nabla f \\perp \\text{等值线（面）的切线}",
        "在物理中，温度场的梯度方向指向温度升高最快的方向；电场强度是电势的负梯度 $\\vec E=-\\nabla\\varphi$，指向电势降低最快的方向。"))
    + app(p("<strong>梯度的应用：</strong>(1) <strong>最速下降法</strong>（优化）：沿 $-\\nabla f$ 方向迭代寻找最小值；(2) <strong>等高线图</strong>：梯度垂直于等高线，密集处梯度大（地形陡峭）；(3) <strong>法向量</strong>：曲面 $F(x,y,z)=0$ 在点处的法向量为 $\\nabla F$。"))
)},
]
},
]
print(f"Ch5: {sum(len(s['items']) for s in ch5_sections)} items")

# =====================================================
#  CHAPTER 6: 多元积分
# =====================================================
ch6_sections = [
# ---- 6.1 二重积分 ----
{
"name": "6.1 二重积分",
"color": "#0891b2",
"desc": "定义、几何意义、直角坐标与极坐标计算",
"items": [
{"id":"c6s1-1","name":"二重积分的概念与几何意义","tags":["def","thm","note"],"brief":"曲顶柱体体积与二重积分。",
 "body": wrap(
    defn("二重积分", p("将区域 $D$ 任意分割为 $n$ 个小区域 $\\Delta\\sigma_i$，在每个小区域取点 $(\\xi_i,\\eta_i)$，作和 $\\sum f(\\xi_i,\\eta_i)\\Delta\\sigma_i$。若当各小区域直径最大值 $\\lambda\\to 0$ 时极限存在，则称此极限为 $f$ 在 $D$ 上的二重积分：")+
    fml("\\iint_D f(x,y)\\,d\\sigma = \\lim_{\\lambda\\to 0}\\sum_{i=1}^n f(\\xi_i,\\eta_i)\\Delta\\sigma_i"))
    + thm("几何意义", p("当 $f(x,y)\\ge 0$ 时，$\\iint_D f(x,y)\\,d\\sigma$ 表示以 $D$ 为底、曲面 $z=f(x,y)$ 为顶的<strong>曲顶柱体体积</strong>。<br>当 $f\\equiv 1$ 时，$\\iint_D d\\sigma$ 表示区域 $D$ 的<strong>面积</strong>。<br>当 $f$ 变号时，积分表示 $xOy$ 面上下方体积的代数和。"))
    + thm("可积条件", p("$f$ 在有界闭区域 $D$ 上连续 $\\Rightarrow$ $f$ 在 $D$ 上可积。"))
)},
{"id":"c6s1-2","name":"二重积分的计算","tags":["thm","der","exa"],"brief":"化为累次积分，极坐标变换。",
 "body": wrap(
    thm("直角坐标下化为累次积分", p("<strong>X 型区域</strong>（$a\\le x\\le b$，$\\varphi_1(x)\\le y\\le\\varphi_2(x)$）：")+
    fml("\\iint_D f(x,y)\\,d\\sigma = \\int_a^b\\left[\\int_{\\varphi_1(x)}^{\\varphi_2(x)} f(x,y)\\,dy\\right]dx",
        "<strong>Y 型区域</strong>（$c\\le y\\le d$，$\\psi_1(y)\\le x\\le\\psi_2(y)$）：$\\iint_D f\\,d\\sigma=\\int_c^d\\int_{\\psi_1(y)}^{\\psi_2(y)}f\\,dx\\,dy$。"))
    + thm("极坐标变换", p("令 $x=r\\cos\\theta$，$y=r\\sin\\theta$，面积元素 $d\\sigma=r\\,dr\\,d\\theta$（雅可比 $J=r$），则")+
    fml("\\iint_D f(x,y)\\,d\\sigma = \\int_\\alpha^\\beta\\int_{r_1(\\theta)}^{r_2(\\theta)} f(r\\cos\\theta,r\\sin\\theta)\\,r\\,dr\\,d\\theta",
        "极坐标适用于圆形、扇形、环形区域或被积函数含 $x^2+y^2$ 的情形。"))
    + der(p("<strong>面积元素 $d\\sigma=r\\,dr\\,d\\theta$ 的推导：</strong>在极坐标下，用 $r=$ 常数（同心圆）和 $\\theta=$ 常数（射线）分割区域。小区域近似为矩形，其径向边长为 $dr$，切向边长为 $r\\,d\\theta$（弧长 = 半径 × 圆心角），故面积 $d\\sigma=dr\\cdot r\\,d\\theta=r\\,dr\\,d\\theta$。<br>用雅可比验证：$J=\\frac{\\partial(x,y)}{\\partial(r,\\theta)}=\\begin{vmatrix}\\cos\\theta & -r\\sin\\theta \\\\ \\sin\\theta & r\\cos\\theta\\end{vmatrix}=r\\cos^2\\theta+r\\sin^2\\theta=r$，故 $d\\sigma=|J|\\,dr\\,d\\theta=r\\,dr\\,d\\theta$。"))
    + exa(p("<strong>例（高斯积分）：</strong>$I=\\iint_D e^{-x^2-y^2}\\,d\\sigma$，$D:x^2+y^2\\le a^2$。极坐标下 $I=\\int_0^{2\\pi}d\\theta\\int_0^a e^{-r^2}r\\,dr=2\\pi\\cdot\\frac{1}{2}(1-e^{-a^2})=\\pi(1-e^{-a^2})$。<br>令 $a\\to\\infty$，全平面积分为 $\\pi$，而它又等于 $\\left(\\int_{-\\infty}^{\\infty}e^{-x^2}dx\\right)^2$，故得著名的<strong>高斯积分</strong> $\\int_{-\\infty}^{\\infty}e^{-x^2}dx=\\sqrt{\\pi}$。"))
)},
]
},
# ---- 6.2 三重积分 ----
{
"name": "6.2 三重积分",
"color": "#06b6d4",
"desc": "定义、几何意义、直角/柱/球坐标",
"items": [
{"id":"c6s2-1","name":"三重积分的概念与计算","tags":["def","thm","exa"],"brief":"体积元素与三种坐标系。",
 "body": wrap(
    defn("三重积分", p("$\\iiint_\\Omega f(x,y,z)\\,dV=\\lim_{\\lambda\\to 0}\\sum f(\\xi_i,\\eta_i,\\zeta_i)\\Delta V_i$。<br>几何意义：当 $f\\equiv 1$ 时表示空间区域 $\\Omega$ 的<strong>体积</strong>；当 $f=\\rho(x,y,z)$ 为体密度时表示物体的<strong>质量</strong>。"))
    + thm("直角坐标", p("$dV=dx\\,dy\\,dz$，可化为先一后二（先 $z$ 后 $xy$）或先二后一的累次积分。"))
    + thm("柱坐标变换", p("$x=r\\cos\\theta$，$y=r\\sin\\theta$，$z=z$，$dV=r\\,dr\\,d\\theta\\,dz$。雅可比 $J=r$。适用于圆柱对称区域。"))
    + thm("球坐标变换", p("$x=r\\sin\\varphi\\cos\\theta$，$y=r\\sin\\varphi\\sin\\theta$，$z=r\\cos\\varphi$，$dV=r^2\\sin\\varphi\\,dr\\,d\\varphi\\,d\\theta$。雅可比 $J=r^2\\sin\\varphi$。适用于球对称区域。"))
    + der(p("<strong>球坐标体积元素推导：</strong>球坐标中，用 $r,\\varphi,\\theta$ 三组坐标面分割空间，小区域近似为长方体：径向边长 $dr$，纬度方向弧长 $r\\,d\\varphi$，经度方向弧长 $r\\sin\\varphi\\,d\\theta$，故")+
    fml("dV = dr\\cdot r\\,d\\varphi\\cdot r\\sin\\varphi\\,d\\theta = r^2\\sin\\varphi\\,dr\\,d\\varphi\\,d\\theta",
        "雅可比验证：$J=\\frac{\\partial(x,y,z)}{\\partial(r,\\varphi,\\theta)}=r^2\\sin\\varphi$（计算行列式可得）。"))
    + exa(p("<strong>例（球体体积）：</strong>$\\Omega:x^2+y^2+z^2\\le R^2$。球坐标下 $V=\\int_0^{2\\pi}d\\theta\\int_0^\\pi\\sin\\varphi\\,d\\varphi\\int_0^R r^2\\,dr=2\\pi\\cdot 2\\cdot\\frac{R^3}{3}=\\frac{4}{3}\\pi R^3$。"))
)},
]
},
# ---- 6.3 曲线积分 ----
{
"name": "6.3 曲线积分",
"color": "#0e7490",
"desc": "第一类（对弧长）与第二类（对坐标）曲线积分",
"items": [
{"id":"c6s3-1","name":"第一类曲线积分（对弧长）","tags":["def","thm","exa"],"brief":"数量函数沿曲线的积分。",
 "body": wrap(
    defn("第一类曲线积分", p("设 $L$ 为光滑曲线，$f(x,y)$ 在 $L$ 上有界。定义")+
    fml("\\int_L f(x,y)\\,ds = \\lim_{\\lambda\\to 0}\\sum_{i=1}^n f(\\xi_i,\\eta_i)\\Delta s_i",
        "其中 $\\Delta s_i$ 为第 $i$ 小段弧长。<strong>几何/物理意义：</strong>线密度为 $f$ 的曲线形构件的质量；当 $f\\equiv 1$ 时为曲线 $L$ 的<strong>弧长</strong>。"))
    + thm("计算公式", p("若 $L$ 由参数方程 $x=\\varphi(t),y=\\psi(t)$（$\\alpha\\le t\\le\\beta$）给出，则")+
    fml("\\int_L f(x,y)\\,ds = \\int_\\alpha^\\beta f(\\varphi(t),\\psi(t))\\sqrt{\\varphi'(t)^2+\\psi'(t)^2}\\,dt",
        "<strong>注意：</strong>对弧长积分的下限必须小于上限（$\\alpha<\\beta$），与曲线方向无关。若 $L:y=y(x)$（$a\\le x\\le b$），则 $\\int_L f\\,ds=\\int_a^b f(x,y(x))\\sqrt{1+y'^2}\\,dx$。"))
    + exa(p("<strong>例：</strong>计算 $\\int_L x\\,ds$，$L$ 为 $y=x^2$ 上从 $(0,0)$ 到 $(1,1)$ 的弧。$ds=\\sqrt{1+4x^2}\\,dx$，故 $\\int_0^1 x\\sqrt{1+4x^2}\\,dx=\\frac{1}{12}(1+4x^2)^{3/2}\\big|_0^1=\\frac{1}{12}(5\\sqrt{5}-1)$。"))
)},
{"id":"c6s3-2","name":"第二类曲线积分（对坐标）","tags":["def","thm","exa"],"brief":"向量函数沿有向曲线的积分。",
 "body": wrap(
    defn("第二类曲线积分", p("设 $L$ 为有向光滑曲线，$P(x,y),Q(x,y)$ 在 $L$ 上有界。定义")+
    fml("\\int_L P\\,dx+Q\\,dy = \\lim_{\\lambda\\to 0}\\sum_{i=1}^n [P(\\xi_i,\\eta_i)\\Delta x_i + Q(\\xi_i,\\eta_i)\\Delta y_i]",
        "<strong>物理意义：</strong>力 $\\vec F=(P,Q)$ 沿有向曲线 $L$ 所做的功 $W=\\int_L P\\,dx+Q\\,dy$。"))
    + thm("计算公式", p("若 $L$ 由参数方程 $x=\\varphi(t),y=\\psi(t)$ 给出，起点对应 $t=\\alpha$，终点对应 $t=\\beta$，则")+
    fml("\\int_L P\\,dx+Q\\,dy = \\int_\\alpha^\\beta [P(\\varphi,\\psi)\\varphi'(t)+Q(\\varphi,\\psi)\\psi'(t)]\\,dt",
        "<strong>注意：</strong>对坐标积分的上下限由曲线方向决定（起点到终点），下限可以大于上限。<strong>反向变号：</strong>$\\int_{L^-}P\\,dx+Q\\,dy=-\\int_L P\\,dx+Q\\,dy$。"))
    + thm("两类曲线积分的关系", p("$\\int_L P\\,dx+Q\\,dy=\\int_L (P\\cos\\alpha+Q\\cos\\beta)\\,ds$，其中 $(\\cos\\alpha,\\cos\\beta)$ 为曲线 $L$ 在点处的单位切向量（指向曲线方向）。"))
)},
]
},
# ---- 6.4 曲面积分 ----
{
"name": "6.4 曲面积分",
"color": "#0891b2",
"desc": "第一类（对面积）与第二类（对坐标）曲面积分",
"items": [
{"id":"c6s4-1","name":"第一类曲面积分（对面积）","tags":["def","thm","exa"],"brief":"数量函数在曲面上的积分。",
 "body": wrap(
    defn("第一类曲面积分", p("设 $\\Sigma$ 为光滑曲面，$f(x,y,z)$ 在 $\\Sigma$ 上有界。定义")+
    fml("\\iint_\\Sigma f(x,y,z)\\,dS = \\lim_{\\lambda\\to 0}\\sum_{i=1}^n f(\\xi_i,\\eta_i,\\zeta_i)\\Delta S_i",
        "<strong>几何/物理意义：</strong>面密度为 $f$ 的曲面的质量；当 $f\\equiv 1$ 时为曲面 $\\Sigma$ 的<strong>面积</strong>。"))
    + thm("计算公式", p("若 $\\Sigma:z=z(x,y)$，$(x,y)\\in D_{xy}$，则曲面面积元素")+
    fml("dS = \\sqrt{1+z_x^2+z_y^2}\\,d\\sigma",
        "故 $\\iint_\\Sigma f\\,dS=\\iint_{D_{xy}} f(x,y,z(x,y))\\sqrt{1+z_x^2+z_y^2}\\,d\\sigma$。"))
    + exa(p("<strong>例（球面面积）：</strong>求半径为 $R$ 的球面面积。上半球面 $z=\\sqrt{R^2-x^2-y^2}$，$z_x=-\\frac{x}{z},z_y=-\\frac{y}{z}$，$\\sqrt{1+z_x^2+z_y^2}=\\frac{R}{z}=\\frac{R}{\\sqrt{R^2-x^2-y^2}}$。<br>$S=2\\iint_{x^2+y^2\\le R^2}\\frac{R}{\\sqrt{R^2-x^2-y^2}}d\\sigma=2R\\int_0^{2\\pi}d\\theta\\int_0^R\\frac{r}{\\sqrt{R^2-r^2}}dr=2R\\cdot 2\\pi\\cdot R=4\\pi R^2$。"))
)},
{"id":"c6s4-2","name":"第二类曲面积分（对坐标）","tags":["def","thm","exa"],"brief":"向量场穿过有向曲面的通量。",
 "body": wrap(
    defn("第二类曲面积分", p("设 $\\Sigma$ 为有向光滑曲面，$\\vec F=(P,Q,R)$。第二类曲面积分")+
    fml("\\iint_\\Sigma P\\,dy\\,dz+Q\\,dz\\,dx+R\\,dx\\,dy",
        "<strong>物理意义：</strong>向量场 $\\vec F$ 穿过有向曲面 $\\Sigma$ 的<strong>通量</strong>（如流量、电通量、磁通量）。"))
    + thm("两类曲面积分的关系", p("")+
    fml("\\iint_\\Sigma \\vec F\\cdot d\\vec S = \\iint_\\Sigma (P\\cos\\alpha+Q\\cos\\beta+R\\cos\\gamma)\\,dS",
        "其中 $(\\cos\\alpha,\\cos\\beta,\\cos\\gamma)$ 为曲面 $\\Sigma$ 法向量的方向余弦，法向与曲面的侧一致。"))
    + thm("计算（投影法）", p("若 $\\Sigma:z=z(x,y)$ 取上侧，则 $\\iint_\\Sigma R\\,dx\\,dy=\\iint_{D_{xy}}R(x,y,z(x,y))\\,d\\sigma$（取下侧则加负号）。类似处理 $P\\,dy\\,dz$ 和 $Q\\,dz\\,dx$。"))
)},
]
},
# ---- 6.5 多元积分的几何与物理应用 ----
{
"name": "6.5 多元积分的几何与物理应用",
"color": "#22d3ee",
"desc": "面积、体积、曲面面积、弧长、质心、转动惯量",
"items": [
{"id":"c6s5-1","name":"几何量计算","tags":["thm","der","exa"],"brief":"面积、体积、曲面面积、弧长公式与推导。",
 "body": wrap(
    thm("平面区域面积", p("$A=\\iint_D d\\sigma$。极坐标下 $A=\\frac{1}{2}\\int_\\alpha^\\beta r^2(\\theta)\\,d\\theta$（极坐标扇形面积公式）。"))
    + thm("空间立体体积", p("<strong>柱体法：</strong>$V=\\iint_D [f_2(x,y)-f_1(x,y)]\\,d\\sigma$（两曲面之间）；<br><strong>切片法：</strong>$V=\\iiint_\\Omega dV=\\int_{c}^{d} A(z)\\,dz$（$A(z)$ 为高度 $z$ 处截面面积）。"))
    + der(p("<strong>曲面面积公式推导：</strong>设曲面 $\\Sigma:z=z(x,y)$，$(x,y)\\in D$。在点 $(x,y)$ 处，曲面的法向量为 $\\vec n=(-z_x,-z_y,1)$，其与 $z$ 轴夹角 $\\gamma$ 满足 $\\cos\\gamma=\\frac{1}{\\sqrt{1+z_x^2+z_y^2}}$。<br>小曲面块 $\\Delta S$ 在 $xOy$ 面上投影为 $\\Delta\\sigma$，由 $\\Delta\\sigma=\\Delta S\\cos\\gamma$ 得 $\\Delta S=\\frac{\\Delta\\sigma}{\\cos\\gamma}=\\sqrt{1+z_x^2+z_y^2}\\,\\Delta\\sigma$，故")+
    fml("S = \\iint_D \\sqrt{1+z_x^2+z_y^2}\\,d\\sigma"))
    + thm("曲线弧长", p("参数方程 $x=\\varphi(t),y=\\psi(t)$（$\\alpha\\le t\\le\\beta$）的弧长")+
    fml("s = \\int_\\alpha^\\beta \\sqrt{\\varphi'(t)^2+\\psi'(t)^2}\\,dt",
        "直角坐标 $y=y(x)$：$s=\\int_a^b\\sqrt{1+y'^2}\\,dx$；极坐标 $r=r(\\theta)$：$s=\\int_\\alpha^\\beta\\sqrt{r^2+r'^2}\\,d\\theta$。"))
    + exa(p("<strong>例：</strong>求球面 $x^2+y^2+z^2=R^2$ 被柱面 $x^2+y^2=Rx$ 截下部分（维维安尼体）的表面积。由对称性只算上半部分并乘 2。$z=\\sqrt{R^2-x^2-y^2}$，$\\sqrt{1+z_x^2+z_y^2}=\\frac{R}{\\sqrt{R^2-x^2-y^2}}$。投影区域 $D:(x-R/2)^2+y^2\\le(R/2)^2$，极坐标 $r\\le R\\cos\\theta$。<br>$S=2\\iint_D\\frac{R}{\\sqrt{R^2-r^2}}r\\,dr\\,d\\theta=2R\\int_{-\\pi/2}^{\\pi/2}d\\theta\\int_0^{R\\cos\\theta}\\frac{r}{\\sqrt{R^2-r^2}}dr=2R\\int_{-\\pi/2}^{\\pi/2}R(1-\\sin\\theta)d\\theta=2R^2(\\pi-2)$。"))
)},
{"id":"c6s5-2","name":"物理量计算","tags":["thm","exa"],"brief":"质心、转动惯量、引力。",
 "body": wrap(
    thm("质心（重心）", p("设面密度 $\\rho(x,y)$，则平面薄板质心")+
    fml("\\bar x = \\frac{\\iint_D x\\rho\\,d\\sigma}{\\iint_D \\rho\\,d\\sigma},\\quad \\bar y = \\frac{\\iint_D y\\rho\\,d\\sigma}{\\iint_D \\rho\\,d\\sigma}",
        "空间物体质心：$\\bar x=\\frac{\\iiint_\\Omega x\\rho\\,dV}{\\iiint_\\Omega\\rho\\,dV}$，$\\bar y,\\bar z$ 类似。均匀物体质心即为形心。"))
    + thm("转动惯量", p("平面薄板对 $x$ 轴、$y$ 轴、原点的转动惯量")+
    fml("I_x = \\iint_D y^2\\rho\\,d\\sigma,\\quad I_y = \\iint_D x^2\\rho\\,d\\sigma,\\quad I_O = \\iint_D (x^2+y^2)\\rho\\,d\\sigma = I_x+I_y",
        "空间物体对 $z$ 轴：$I_z=\\iiint_\\Omega (x^2+y^2)\\rho\\,dV$；对 $x$ 轴：$I_x=\\iiint_\\Omega(y^2+z^2)\\rho\\,dV$。"))
    + thm("引力", p("物体对单位质量质点的引力分量：$F_x=G\\iiint_\\Omega\\frac{(x-x_0)\\rho}{r^3}\\,dV$，$F_y,F_z$ 类似，其中 $r=\\sqrt{(x-x_0)^2+(y-y_0)^2+(z-z_0)^2}$，$G$ 为引力常数。"))
)},
]
},
# ---- 6.6 含参积分与欧拉积分 ----
{
"name": "6.6 含参积分与欧拉积分",
"color": "#0e7490",
"desc": "含参常义/反常积分，Γ函数与Β函数",
"items": [
{"id":"c6s6-1","name":"含参积分","tags":["def","thm","app"],"brief":"积分号下求导与求积分。",
 "body": wrap(
    defn("含参积分", p("设 $I(x)=\\int_a^b f(x,t)\\,dt$，若 $f$ 及 $f_x$ 连续，则")+
    fml("I'(x) = \\int_a^b \\frac{\\partial f}{\\partial x}(x,t)\\,dt",
        "即<strong>积分号下求导</strong>。这是计算复杂积分的有力工具。"))
    + app(p("<strong>例（费曼积分法）：</strong>计算 $I=\\int_0^1\\frac{x^a-1}{\\ln x}\\,dx$。引入 $I(a)=\\int_0^1\\frac{x^a-1}{\\ln x}\\,dx$，则 $I'(a)=\\int_0^1 x^a\\,dx=\\frac{1}{a+1}$，故 $I(a)=\\ln(a+1)+C$。由 $I(0)=0$ 得 $C=0$，故 $I=\\ln(a+1)$。取 $a=1$ 得 $\\int_0^1\\frac{x-1}{\\ln x}\\,dx=\\ln 2$。"))
)},
{"id":"c6s6-2","name":"欧拉积分（Γ函数与Β函数）","tags":["def","thm","app"],"brief":"阶乘的解析延拓。",
 "body": wrap(
    defn("Γ函数与Β函数", p("")+
    fml("\\Gamma(s) = \\int_0^{+\\infty} x^{s-1}e^{-x}\\,dx\\quad (s>0),\\qquad B(p,q) = \\int_0^1 x^{p-1}(1-x)^{q-1}\\,dx\\quad (p,q>0)"))
    + thm("Γ函数性质", p("(1) 递推：$\\Gamma(s+1)=s\\Gamma(s)$；(2) $\\Gamma(n+1)=n!$（$n$ 为正整数），故 Γ 函数是阶乘的解析延拓；(3) $\\Gamma(\\frac{1}{2})=\\sqrt{\\pi}$；(4) 余元公式：$\\Gamma(s)\\Gamma(1-s)=\\frac{\\pi}{\\sin\\pi s}$。"))
    + der(p("<strong>递推公式推导：</strong>对 $\\Gamma(s+1)=\\int_0^{+\\infty}x^s e^{-x}\\,dx$ 分部积分，取 $u=x^s$，$dv=e^{-x}dx$：")+
    fml("\\Gamma(s+1) = \\left[-x^s e^{-x}\\right]_0^{+\\infty} + s\\int_0^{+\\infty}x^{s-1}e^{-x}\\,dx = 0 + s\\Gamma(s) = s\\Gamma(s)",
        "其中 $\\left[-x^s e^{-x}\\right]_0^{+\\infty}=0$（$x\\to+\\infty$ 时 $e^{-x}$ 衰减快于任何多项式；$x\\to 0^+$ 时 $x^s\\to 0$）。<br>由此 $\\Gamma(n+1)=n\\Gamma(n)=n(n-1)\\cdots 1\\cdot\\Gamma(1)=n!$（因 $\\Gamma(1)=\\int_0^\\infty e^{-x}dx=1$）。"))
    + thm("Γ与Β的关系", p("$B(p,q)=\\frac{\\Gamma(p)\\Gamma(q)}{\\Gamma(p+q)}$。")+
    fml("\\Gamma(s+1) = s\\Gamma(s),\\quad \\Gamma\\left(\\frac{1}{2}\\right)=\\sqrt{\\pi}",
        "例：$\\int_0^{+\\infty}e^{-x^2}\\,dx=\\frac{1}{2}\\Gamma(\\frac{1}{2})=\\frac{\\sqrt{\\pi}}{2}$，即高斯积分。"))
    + app(p("Γ 函数在概率论（Gamma 分布、$\\chi^2$ 分布）、统计学、数论中广泛应用。"))
)},
]
},
# ---- 6.7 重积分的换元法与对称性 ----
{
"name": "6.7 重积分的换元法与对称性",
"color": "#0891b2",
"desc": "重积分一般换元公式、雅可比行列式、积分对称性",
"items": [
{"id":"c6s7-1","name":"重积分的换元法","tags":["thm","der","exa"],"brief":"一般换元公式与雅可比行列式。",
 "body": wrap(
    thm("二重积分换元法", p("设 $f$ 在 $D$ 连续，变换 $T:\\,x=x(u,v),\\,y=y(u,v)$ 将 $uOv$ 平面上的区域 $D'$ 一一映射到 $xOy$ 平面上的 $D$，且 $x,y$ 有一阶连续偏导数，雅可比行列式 $J=\\frac{\\partial(x,y)}{\\partial(u,v)}\\ne 0$，则")+
    fml("\\iint_D f(x,y)\\,d\\sigma = \\iint_{D'} f(x(u,v),y(u,v))\\,|J|\\,du\\,dv"))
    + der(p("<strong>雅可比行列式的几何意义：</strong>$|J|$ 是坐标变换下的<strong>面积伸缩系数</strong>。在 $(u,v)$ 处取小矩形 $\\Delta u\\times\\Delta v$，其像在 $xOy$ 平面上近似为平行四边形，边长向量为 $\\vec r_u\\Delta u=(x_u,y_u)\\Delta u$ 和 $\\vec r_v\\Delta v=(x_v,y_v)\\Delta v$，面积为 $|\\vec r_u\\times\\vec r_v|\\Delta u\\Delta v=|J|\\Delta u\\Delta v$。故 $d\\sigma=|J|\\,du\\,dv$。"))
    + thm("三重积分换元法", p("变换 $x=x(u,v,w),y=y(u,v,w),z=z(u,v,w)$，雅可比 $J=\\frac{\\partial(x,y,z)}{\\partial(u,v,w)}$，则")+
    fml("\\iiint_\\Omega f(x,y,z)\\,dV = \\iiint_{\\Omega'} f(x(u,v,w),y(u,v,w),z(u,v,w))\\,|J|\\,du\\,dv\\,dw"))
    + exa(p("<strong>常见变换的雅可比：</strong><br>极坐标 $(x,y)=(r\\cos\\theta,r\\sin\\theta)$：$J=r$；<br>柱坐标 $(x,y,z)=(r\\cos\\theta,r\\sin\\theta,z)$：$J=r$；<br>球坐标 $(x,y,z)=(r\\sin\\varphi\\cos\\theta,r\\sin\\varphi\\sin\\theta,r\\cos\\varphi)$：$J=r^2\\sin\\varphi$。<br><strong>例：</strong>求椭球体 $\\frac{x^2}{a^2}+\\frac{y^2}{b^2}+\\frac{z^2}{c^2}\\le 1$ 的体积。作广义球坐标变换 $x=ar\\sin\\varphi\\cos\\theta$，$y=br\\sin\\varphi\\sin\\theta$，$z=cr\\cos\\varphi$，则 $J=abc\\,r^2\\sin\\varphi$。$V=\\int_0^{2\\pi}d\\theta\\int_0^\\pi\\sin\\varphi\\,d\\varphi\\int_0^1 abc\\,r^2\\,dr=abc\\cdot 2\\pi\\cdot 2\\cdot\\frac{1}{3}=\\frac{4}{3}\\pi abc$。"))
)},
{"id":"c6s7-2","name":"重积分的对称性","tags":["thm","app","exa"],"brief":"利用奇偶性与对称性简化积分。",
 "body": wrap(
    thm("奇偶对称性", p("设积分区域 $D$ 关于 $x$ 轴对称，$f(x,y)$ 关于 $y$ 为奇（偶）函数：<br>若 $f(x,-y)=-f(x,y)$（奇函数），则 $\\iint_D f\\,d\\sigma=0$；<br>若 $f(x,-y)=f(x,y)$（偶函数），则 $\\iint_D f\\,d\\sigma=2\\iint_{D_1}f\\,d\\sigma$（$D_1$ 为 $D$ 在 $y\\ge 0$ 的部分）。<br>关于 $y$ 轴对称时同理（看 $f$ 关于 $x$ 的奇偶性）。"))
    + thm("轮换对称性", p("若积分区域 $D$ 关于 $y=x$ 对称（即 $(x,y)\\in D\\Rightarrow(y,x)\\in D$），则")+
    fml("\\iint_D f(x,y)\\,d\\sigma = \\iint_D f(y,x)\\,d\\sigma",
        "特别地，$\\iint_D x^2\\,d\\sigma=\\iint_D y^2\\,d\\sigma=\\frac{1}{2}\\iint_D(x^2+y^2)\\,d\\sigma$。"))
    + der(p("<strong>轮换对称性证明：</strong>作变换 $(x,y)\\mapsto(y,x)$，此变换的雅可比 $J=\\begin{vmatrix}0&1\\\\1&0\\end{vmatrix}=-1$，$|J|=1$，且 $D'=D$，故 $\\iint_D f(x,y)\\,d\\sigma=\\iint_D f(y,x)\\,|J|\\,d\\sigma=\\iint_D f(y,x)\\,d\\sigma$。"))
    + exa(p("<strong>例：</strong>计算 $\\iint_D(x^2+y^2)\\,d\\sigma$，$D:x^2+y^2\\le 1$。由轮换对称性 $\\iint_D x^2=\\iint_D y^2$，故原式 $=2\\iint_D x^2\\,d\\sigma=\\iint_D(x^2+y^2)\\,d\\sigma$。极坐标下 $=\\int_0^{2\\pi}d\\theta\\int_0^1 r^2\\cdot r\\,dr=2\\pi\\cdot\\frac{1}{4}=\\frac{\\pi}{2}$。"))
)},
]
},
]
print(f"Ch6: {sum(len(s['items']) for s in ch6_sections)} items")

# =====================================================
#  CHAPTER 7: 积分定理
# =====================================================
ch7_sections = [
# ---- 7.1 格林公式 ----
{
"name": "7.1 格林公式",
"color": "#be185d",
"desc": "平面曲线积分与二重积分的转化",
"items": [
{"id":"c7s1-1","name":"格林公式","tags":["thm","der","app"],"brief":"闭路曲线积分化为二重积分。",
 "body": wrap(
    thm("格林公式", p("设 $D$ 为平面有界闭区域，边界 $L$ 为分段光滑曲线，取正向（逆时针）。若 $P,Q$ 在 $D$ 上有一阶连续偏导数，则")+
    fml("\\oint_L P\\,dx+Q\\,dy = \\iint_D\\left(\\frac{\\partial Q}{\\partial x}-\\frac{\\partial P}{\\partial y}\\right)d\\sigma"))
    + der(p("<strong>证明：</strong>只需证 $\\oint_L P\\,dx=-\\iint_D\\frac{\\partial P}{\\partial y}\\,d\\sigma$，另一式类似。<br>设 $D$ 为 X 型区域：$a\\le x\\le b$，$y_1(x)\\le y\\le y_2(x)$。则")+
    fml("\\iint_D\\frac{\\partial P}{\\partial y}\\,d\\sigma = \\int_a^b\\left[\\int_{y_1(x)}^{y_2(x)}\\frac{\\partial P}{\\partial y}\\,dy\\right]dx = \\int_a^b [P(x,y_2(x))-P(x,y_1(x))]\\,dx",
        "而曲线积分 $\\oint_L P\\,dx$ 沿下边界 $y=y_1(x)$（$x$ 从 $a$ 到 $b$）为 $\\int_a^b P(x,y_1(x))\\,dx$，沿上边界 $y=y_2(x)$（$x$ 从 $b$ 到 $a$）为 $\\int_b^a P(x,y_2(x))\\,dx=-\\int_a^b P(x,y_2(x))\\,dx$，左右边界 $dx=0$。<br>故 $\\oint_L P\\,dx=\\int_a^b P(x,y_1)\\,dx-\\int_a^b P(x,y_2)\\,dx=-\\int_a^b[P(x,y_2)-P(x,y_1)]\\,dx=-\\iint_D\\frac{\\partial P}{\\partial y}\\,d\\sigma$。一般区域可分割为若干 X 型区域，相邻边界线积分抵消。$\\blacksquare$"))
    + app(p("<strong>面积公式：</strong>取 $P=-y,Q=x$，得 $A=\\frac{1}{2}\\oint_L x\\,dy-y\\,dx$。这是用曲线积分计算区域面积的方法。"))
)},
{"id":"c7s1-2","name":"平面曲线积分与路径无关","tags":["thm","der","app"],"brief":"四个等价条件与原函数。",
 "body": wrap(
    thm("等价条件", p("设 $D$ 为单连通区域，$P,Q$ 在 $D$ 内有一阶连续偏导数，则下列四个条件等价：<br>(1) 对 $D$ 内任意闭曲线 $L$，$\\oint_L P\\,dx+Q\\,dy=0$；<br>(2) $\\int_L P\\,dx+Q\\,dy$ 在 $D$ 内与路径无关，只与起点终点有关；<br>(3) $P\\,dx+Q\\,dy$ 是某函数 $u(x,y)$ 的全微分，即 $du=P\\,dx+Q\\,dy$；<br>(4) 在 $D$ 内处处有 $\\frac{\\partial P}{\\partial y}=\\frac{\\partial Q}{\\partial x}$。"))
    + der(p("<strong>原函数求法：</strong>若 $P\\,dx+Q\\,dy$ 为全微分，则原函数")+
    fml("u(x,y) = \\int_{(x_0,y_0)}^{(x,y)} P\\,dx+Q\\,dy = \\int_{x_0}^x P(t,y_0)\\,dt + \\int_{y_0}^y Q(x,t)\\,dt",
        "此时 $\\int_{A}^{B}P\\,dx+Q\\,dy=u(B)-u(A)$，类似于一元函数的牛顿-莱布尼茨公式。"))
    + app(p("这是场论中保守场的数学刻画：保守力场做功与路径无关，只取决于起止位置（势能差）。"))
)},
]
},
# ---- 7.2 高斯公式 ----
{
"name": "7.2 高斯公式（散度定理）",
"color": "#db2777",
"desc": "闭曲面积分与三重积分的转化，通量与散度",
"items": [
{"id":"c7s2-1","name":"高斯公式","tags":["thm","der","exa"],"brief":"散度定理的完整表述与证明。",
 "body": wrap(
    thm("高斯公式", p("设 $\\Omega$ 为空间有界闭区域，边界 $\\Sigma$ 为分片光滑闭曲面，取外侧。若 $P,Q,R$ 在 $\\Omega$ 上有一阶连续偏导数，则")+
    fml("\\mathop{\\oint\\!\\!\\!\\!\\!\\int}_\\Sigma P\\,dy\\,dz+Q\\,dz\\,dx+R\\,dx\\,dy = \\iiint_\\Omega\\left(\\frac{\\partial P}{\\partial x}+\\frac{\\partial Q}{\\partial y}+\\frac{\\partial R}{\\partial z}\\right)dV",
        "用向量形式表示：$\\mathop{\\oint\\!\\!\\!\\!\\!\\int}_\\Sigma\\vec F\\cdot d\\vec S=\\iiint_\\Omega\\nabla\\cdot\\vec F\\,dV$，其中 $\\vec F=(P,Q,R)$，$\\nabla\\cdot\\vec F$ 为散度。"))
    + der(p("<strong>证明：</strong>只需证 $\\mathop{\\oint\\!\\!\\!\\!\\!\\int}_\\Sigma R\\,dx\\,dy=\\iiint_\\Omega\\frac{\\partial R}{\\partial z}\\,dV$，其余两式类似。<br>设 $\\Omega$ 为 $xy$ 型区域（母线平行 $z$ 轴），其边界曲面分为上底 $\\Sigma_2:z=z_2(x,y)$（上侧）、下底 $\\Sigma_1:z=z_1(x,y)$（下侧）、侧面 $\\Sigma_3$。<br>对三重积分用先一后二：")+
    fml("\\iiint_\\Omega\\frac{\\partial R}{\\partial z}\\,dV = \\iint_D\\left[\\int_{z_1(x,y)}^{z_2(x,y)}\\frac{\\partial R}{\\partial z}\\,dz\\right]d\\sigma = \\iint_D [R(x,y,z_2)-R(x,y,z_1)]\\,d\\sigma",
        "而曲面积分中，侧面 $\\Sigma_3$ 的法向量垂直于 $z$ 轴，故 $\\iint_{\\Sigma_3}R\\,dx\\,dy=0$；上底取上侧为 $+\\iint_D R(x,y,z_2)\\,d\\sigma$，下底取下侧为 $-\\iint_D R(x,y,z_1)\\,d\\sigma$。<br>故 $\\mathop{\\oint\\!\\!\\!\\!\\!\\int}_\\Sigma R\\,dx\\,dy=\\iint_D[R(x,y,z_2)-R(x,y,z_1)]\\,d\\sigma$，与三重积分相等。一般区域可分割为若干 $xy$ 型区域。$\\blacksquare$"))
    + exa(p("<strong>例：</strong>求 $\\mathop{\\oint\\!\\!\\!\\!\\!\\int}_\\Sigma x^3\\,dy\\,dz+y^3\\,dz\\,dx+z^3\\,dx\\,dy$，$\\Sigma$ 为球面 $x^2+y^2+z^2=R^2$ 外侧。<br>由高斯公式：$=\\iiint_\\Omega 3(x^2+y^2+z^2)\\,dV=3\\int_0^{2\\pi}d\\theta\\int_0^\\pi\\sin\\varphi\\,d\\varphi\\int_0^R r^2\\cdot r^2\\,dr=3\\cdot 2\\pi\\cdot 2\\cdot\\frac{R^5}{5}=\\frac{12\\pi R^5}{5}$。"))
)},
{"id":"c7s2-2","name":"散度的物理意义","tags":["def","thm","app"],"brief":"通量密度与无源场。",
 "body": wrap(
    defn("散度", p("向量场 $\\vec F=(P,Q,R)$ 在点 $M$ 处的散度")+
    fml("\\mathrm{div}\\,\\vec F = \\nabla\\cdot\\vec F = \\frac{\\partial P}{\\partial x}+\\frac{\\partial Q}{\\partial y}+\\frac{\\partial R}{\\partial z}",
        "散度是标量，表示单位体积内穿出的通量（通量密度）。$\\mathrm{div}\\,\\vec F>0$ 表示该点有源（流出），$<0$ 表示有汇（流入），$=0$ 表示无源。"))
    + thm("散度的极限定义", p("$\\mathrm{div}\\,\\vec F(M)=\\lim_{\\Omega\\to M}\\frac{1}{V}\\mathop{\\oint\\!\\!\\!\\!\\!\\int}_{\\partial\\Omega}\\vec F\\cdot d\\vec S$，其中 $V$ 为包含 $M$ 的小区域 $\\Omega$ 的体积。"))
    + app(p("<strong>无源场（螺线场）：</strong>若 $\\nabla\\cdot\\vec F\\equiv 0$，则穿出任意闭曲面的通量为零，场线闭合。稳恒磁场是无源场（$\\nabla\\cdot\\vec B=0$）。<br><strong>高斯公式的物理意义：</strong>穿出闭曲面的总通量等于内部所有源的散度之体积分——这正是静电学高斯定理和流体连续性方程的数学基础。"))
)},
]
},
# ---- 7.3 斯托克斯公式 ----
{
"name": "7.3 斯托克斯公式",
"color": "#ec4899",
"desc": "空间曲线积分与曲面积分的转化，环量与旋度",
"items": [
{"id":"c7s3-1","name":"斯托克斯公式","tags":["thm","der","exa"],"brief":"旋度定理的完整表述。",
 "body": wrap(
    thm("斯托克斯公式", p("设 $\\Sigma$ 为光滑有界曲面，边界 $\\Gamma$ 为分段光滑闭曲线，$\\Gamma$ 的正向与 $\\Sigma$ 的侧符合右手定则。若 $P,Q,R$ 有一阶连续偏导数，则")+
    fml("\\oint_\\Gamma P\\,dx+Q\\,dy+R\\,dz = \\iint_\\Sigma\\begin{vmatrix}dy\\,dz & dz\\,dx & dx\\,dy \\\\ \\frac{\\partial}{\\partial x} & \\frac{\\partial}{\\partial y} & \\frac{\\partial}{\\partial z} \\\\ P & Q & R\\end{vmatrix}",
        "用旋度表示：$\\oint_\\Gamma\\vec F\\cdot d\\vec r=\\iint_\\Sigma(\\nabla\\times\\vec F)\\cdot d\\vec S$。"))
    + der(p("<strong>证明思路：</strong>先对特殊曲面（$z=z(x,y)$ 型）证明 $\\oint_\\Gamma P\\,dx=\\iint_\\Sigma(\\frac{\\partial P}{\\partial z}dz\\,dx-\\frac{\\partial P}{\\partial y}dx\\,dy)$，利用格林公式将边界线积分化为投影区域上的二重积分，再还原为曲面积分。对 $Q,R$ 同理，合并即得。一般曲面可分割为若干此类曲面片，相邻边界线积分抵消。<br><strong>格林公式是特例：</strong>当 $\\Sigma$ 为 $xy$ 平面上的区域 $D$（$z=0$，$d\\vec S=dx\\,dy\\,\\vec k$），斯托克斯公式退化为 $\\oint_{\\partial D}P\\,dx+Q\\,dy=\\iint_D(\\frac{\\partial Q}{\\partial x}-\\frac{\\partial P}{\\partial y})d\\sigma$，即格林公式。"))
    + app(p("<strong>几何/物理意义：</strong>沿闭曲线的<strong>环量</strong>等于穿过以该曲线为边界的曲面的<strong>旋度通量</strong>。格林公式是斯托克斯公式在 $z=0$ 平面的特例。"))
)},
{"id":"c7s3-2","name":"旋度的物理意义","tags":["def","thm","app"],"brief":"环量密度与无旋场。",
 "body": wrap(
    defn("旋度", p("向量场 $\\vec F=(P,Q,R)$ 的旋度")+
    fml("\\mathrm{rot}\\,\\vec F = \\nabla\\times\\vec F = \\left(\\frac{\\partial R}{\\partial y}-\\frac{\\partial Q}{\\partial z},\\frac{\\partial P}{\\partial z}-\\frac{\\partial R}{\\partial x},\\frac{\\partial Q}{\\partial x}-\\frac{\\partial P}{\\partial y}\\right)",
        "旋度是向量，方向为使环量密度最大的方向，大小为最大环量密度。"))
    + thm("旋度与环量密度", p("在点 $M$ 处，沿方向 $\\vec n$ 的环量密度为 $(\\nabla\\times\\vec F)\\cdot\\vec n$。旋度方向即涡旋轴方向，大小表示旋转强度。"))
    + app(p("<strong>无旋场（保守场）：</strong>若 $\\nabla\\times\\vec F\\equiv 0$，则沿任意闭曲线的环量为零，曲线积分与路径无关，存在势函数 $u$ 使 $\\vec F=\\nabla u$。引力场、静电场是无旋场。<br><strong>有旋场：</strong>如稳恒电流的磁场（$\\nabla\\times\\vec B=\\mu_0\\vec J$），存在涡旋结构。"))
)},
]
},
# ---- 7.4 场论：梯度、散度、旋度与势场 ----
{
"name": "7.4 场论：梯度、散度、旋度与势场",
"color": "#f472b6",
"desc": "nabla算子、三大积分定理统一、调和场",
"items": [
{"id":"c7s4-1","name":"梯度、散度、旋度的统一","tags":["def","thm","app"],"brief":"nabla算子与三大积分定理。",
 "body": wrap(
    defn("nabla 算子", p("$\\nabla=\\left(\\frac{\\partial}{\\partial x},\\frac{\\partial}{\\partial y},\\frac{\\partial}{\\partial z}\\right)$。对数量场 $u$：梯度 $\\nabla u$ 是向量；对向量场 $\\vec F$：散度 $\\nabla\\cdot\\vec F$ 是标量，旋度 $\\nabla\\times\\vec F$ 是向量。"))
    + thm("三大积分定理的向量形式", p("<strong>高斯公式：</strong>$\\mathop{\\oint\\!\\!\\!\\!\\!\\int}_{\\partial\\Omega}\\vec F\\cdot d\\vec S=\\iiint_\\Omega\\nabla\\cdot\\vec F\\,dV$（通量=散度体积分）；<br><strong>斯托克斯公式：</strong>$\\oint_{\\partial\\Sigma}\\vec F\\cdot d\\vec r=\\iint_\\Sigma(\\nabla\\times\\vec F)\\cdot d\\vec S$（环量=旋度通量）；<br><strong>梯度定理：</strong>$\\int_A^B\\nabla u\\cdot d\\vec r=u(B)-u(A)$（曲线积分=端点势差）。"))
    + app(p("三大定理揭示了微积分的统一结构：<strong>边界上的积分 = 内部微分运算的积分</strong>。这是微分流形上斯托克斯定理的特例，也是整个向量分析的核心。"))
)},
{"id":"c7s4-2","name":"势场与调和场","tags":["thm","app"],"brief":"保守场、无源场、调和场。",
 "body": wrap(
    thm("保守场（有势场）", p("若 $\\nabla\\times\\vec F=0$（无旋），则 $\\vec F$ 为保守场，存在势函数 $u$ 使 $\\vec F=\\nabla u$。曲线积分 $\\int_A^B\\vec F\\cdot d\\vec r=u(B)-u(A)$ 与路径无关。"))
    + thm("无源场（管形场）", p("若 $\\nabla\\cdot\\vec F=0$，则 $\\vec F$ 为无源场，存在向量势 $\\vec A$ 使 $\\vec F=\\nabla\\times\\vec A$。穿出任意闭曲面的通量为零。"))
    + thm("调和场", p("若 $\\vec F$ 既无源又无旋（$\\nabla\\cdot\\vec F=0$ 且 $\\nabla\\times\\vec F=0$），则 $\\vec F=\\nabla u$，且势函数 $u$ 满足拉普拉斯方程 $\\Delta u=\\nabla\\cdot\\nabla u=0$。$u$ 称为调和函数。"))
    + app(p("<strong>调和函数的性质：</strong>调和函数在区域内部不能取到最大值（除非为常数），具有平均值性质。稳态温度分布、静电势、不可压缩无旋流体的速度势都是调和函数的实例。"))
)},
]
},
# ---- 7.5 外微分与一般斯托克斯定理 ----
{
"name": "7.5 外微分与一般斯托克斯定理",
"color": "#be185d",
"desc": "微分形式、外微分算子、统一的斯托克斯定理",
"items": [
{"id":"c7s5-1","name":"微分形式与外微分","tags":["def","thm"],"brief":"从向量场到微分形式的统一语言。",
 "body": wrap(
    defn("微分形式", p("在 $\\mathbb{R}^3$ 中：<br><strong>0-形式</strong>：标量函数 $f$；<br><strong>1-形式</strong>：$\\omega=P\\,dx+Q\\,dy+R\\,dz$（对应向量场 $\\vec F=(P,Q,R)$）；<br><strong>2-形式</strong>：$\\omega=P\\,dy\\wedge dz+Q\\,dz\\wedge dx+R\\,dx\\wedge dy$（对应向量场的通量）；<br><strong>3-形式</strong>：$\\omega=f\\,dx\\wedge dy\\wedge dz$（对应体积密度）。"))
    + thm("外微分算子 d", p("外微分 $d$ 将 $k$-形式变为 $(k+1)$-形式，满足：<br>(1) $d^2=0$（$d$ 作用两次为零）；<br>(2) 线性：$d(\\alpha+\\beta)=d\\alpha+d\\beta$；<br>(3) 莱布尼茨法则：$d(\\alpha\\wedge\\beta)=d\\alpha\\wedge\\beta+(-1)^k\\alpha\\wedge d\\beta$（$\\alpha$ 为 $k$-形式）。")+
    fml("df = f_x\\,dx+f_y\\,dy+f_z\\,dz\\quad(\\text{0-形式}\\to\\text{1-形式，对应梯度 }\\nabla f)",
        "对 1-形式 $\\omega=Pdx+Qdy+Rdz$：$d\\omega=(R_y-Q_z)dy\\wedge dz+(P_z-R_x)dz\\wedge dx+(Q_x-P_y)dx\\wedge dy$，对应旋度 $\\nabla\\times\\vec F$；<br>对 2-形式 $\\omega=Pdy\\wedge dz+Qdz\\wedge dx+Rdx\\wedge dy$：$d\\omega=(P_x+Q_y+R_z)dx\\wedge dy\\wedge dz$，对应散度 $\\nabla\\cdot\\vec F$。"))
    + app(p("<strong>$d^2=0$ 的物理意义：</strong>$d^2 f=0$ 对应 $\\nabla\\times(\\nabla f)=0$（梯度场无旋）；$d^2\\omega=0$（对 1-形式）对应 $\\nabla\\cdot(\\nabla\\times\\vec F)=0$（旋度场无源）。这两个向量恒等式是 $d^2=0$ 的体现。"))
)},
{"id":"c7s5-2","name":"一般斯托克斯定理","tags":["thm","app","note"],"brief":"三大积分定理的统一形式。",
 "body": wrap(
    thm("一般斯托克斯定理", p("设 $M$ 为 $n$ 维定向流形，$\\partial M$ 为其边界（带诱导定向），$\\omega$ 为 $(n-1)$-形式，则")+
    fml("\\int_{\\partial M} \\omega = \\int_M d\\omega",
        "这是微积分基本定理在高维的最一般形式。"))
    + app(p("<strong>三大定理作为特例：</strong><br>(1) <strong>梯度定理</strong>：$M$ 为曲线（1 维），$\\omega=f$（0-形式），$\\int_A^B df=f(B)-f(A)$（牛顿-莱布尼茨）；<br>(2) <strong>格林公式</strong>：$M$ 为平面区域（2 维），$\\omega=Pdx+Qdy$（1-形式），$\\oint_{\\partial M}Pdx+Qdy=\\iint_M(Q_x-P_y)d\\sigma$；<br>(3) <strong>高斯公式</strong>：$M$ 为空间区域（3 维），$\\omega=Pdy\\wedge dz+Qdz\\wedge dx+Rdx\\wedge dy$（2-形式），$\\mathop{\\oint}_{\\partial M}\\vec F\\cdot d\\vec S=\\iiint_M\\nabla\\cdot\\vec F\\,dV$；<br>(4) <strong>斯托克斯公式</strong>：$M$ 为空间曲面（2 维），$\\omega=Pdx+Qdy+Rdz$（1-形式），$\\oint_{\\partial M}\\vec F\\cdot d\\vec r=\\iint_M(\\nabla\\times\\vec F)\\cdot d\\vec S$。"))
    + note(p("一般斯托克斯定理揭示了微积分的深刻统一性：<strong>边界上的积分等于内部外微分的积分</strong>。它是微分几何、拓扑学（德拉姆上同调）、理论物理（规范场论）的基础工具。理解这一定理，就把握了从一元微积分到高维微积分的全部精髓。"))
)},
]
},
]
print(f"Ch7: {sum(len(s['items']) for s in ch7_sections)} items")

# =====================================================
#  CHAPTER 8: 无穷级数
# =====================================================
ch8_sections = [
# ---- 8.1 数项级数 ----
{
"name": "8.1 数项级数",
"color": "#be185d",
"desc": "收敛定义、正项级数判别、交错级数",
"items": [
{"id":"c8s1-1","name":"数项级数的概念与性质","tags":["def","thm","note"],"brief":"部分和收敛、收敛必要条件。",
 "body": wrap(
    defn("级数收敛", p("级数 $\\sum_{n=1}^{\\infty}u_n$ 的前 $n$ 项和 $S_n=\\sum_{k=1}^n u_k$ 称为部分和。若 $\\lim_{n\\to\\infty}S_n=S$ 存在，则称级数收敛，$S$ 为其和；否则发散。"))
    + thm("收敛的必要条件", p("若 $\\sum u_n$ 收敛，则 $\\lim_{n\\to\\infty}u_n=0$。<br><strong>注意：</strong>$u_n\\to 0$ 不是充分条件，如调和级数 $\\sum\\frac{1}{n}$ 发散（虽 $u_n\\to 0$）。"))
    + note(p("<strong>基本性质：</strong>(1) 收敛级数线性组合仍收敛；(2) 去掉、添加、改变有限项不改变敛散性；(3) 收敛级数加括号后仍收敛且和不变（逆命题不成立）。"))
)},
{"id":"c8s1-2","name":"正项级数判别法","tags":["thm","app","exa"],"brief":"比较、比值、根值、积分判别法。",
 "body": wrap(
    thm("正项级数判别法", p("设 $u_n\\ge 0$：<br><strong>比较判别法：</strong>若 $0\\le u_n\\le v_n$，$\\sum v_n$ 收敛 $\\Rightarrow$ $\\sum u_n$ 收敛；$\\sum u_n$ 发散 $\\Rightarrow$ $\\sum v_n$ 发散。<br><strong>比值判别法（达朗贝尔）：</strong>$\\lim\\frac{u_{n+1}}{u_n}=\\rho$，$\\rho<1$ 收敛，$\\rho>1$ 发散，$\\rho=1$ 不定。<br><strong>根值判别法（柯西）：</strong>$\\lim\\sqrt[n]{u_n}=\\rho$，结论同比值法。<br><strong>积分判别法：</strong>若 $f(x)$ 在 $[1,+\\infty)$ 非负递减，则 $\\sum_{n=1}^\\infty f(n)$ 与 $\\int_1^{+\\infty}f(x)\\,dx$ 同敛散。"))
    + app(p("<strong>p 级数：</strong>$\\sum_{n=1}^\\infty\\frac{1}{n^p}$ 当 $p>1$ 收敛，$p\\le 1$ 发散。这是比较判别法最常用的参照级数。<br>例：$\\sum\\frac{1}{n^2}$ 收敛（$p=2>1$），$\\sum\\frac{1}{n}$ 发散（调和级数，$p=1$）。"))
)},
{"id":"c8s1-3","name":"交错级数与绝对收敛","tags":["thm","app"],"brief":"莱布尼茨判别法、绝对与条件收敛。",
 "body": wrap(
    thm("莱布尼茨判别法", p("若交错级数 $\\sum(-1)^{n-1}u_n$（$u_n>0$）满足：(1) $\\{u_n\\}$ 单调递减；(2) $\\lim u_n=0$，则级数收敛，且其和 $S\\le u_1$，余项 $|R_n|\\le u_{n+1}$。"))
    + thm("绝对收敛与条件收敛", p("若 $\\sum |u_n|$ 收敛，则 $\\sum u_n$ 收敛（<strong>绝对收敛</strong>）；若 $\\sum u_n$ 收敛但 $\\sum |u_n|$ 发散，称为<strong>条件收敛</strong>。<br>绝对收敛级数满足交换律（任意重排和不变）；条件收敛级数重排后可收敛于任意值（黎曼重排定理）。"))
    + app(p("<strong>例：</strong>$\\sum\\frac{(-1)^{n-1}}{n}$ 由莱布尼茨判别法收敛，但 $\\sum\\frac{1}{n}$ 发散，故为条件收敛。其和为 $\\ln 2$。"))
)},
]
},
# ---- 8.2 幂级数 ----
{
"name": "8.2 幂级数",
"color": "#db2777",
"desc": "收敛半径、函数展开、运算性质",
"items": [
{"id":"c8s2-1","name":"幂级数的收敛半径","tags":["def","thm","exa"],"brief":"阿贝尔定理与收敛半径计算。",
 "body": wrap(
    defn("幂级数", p("形如 $\\sum_{n=0}^{\\infty}a_n(x-x_0)^n$ 的级数称为幂级数。令 $x_0=0$，则为 $\\sum a_n x^n$。"))
    + thm("阿贝尔定理", p("若幂级数在 $x=x_1$（$x_1\\ne 0$）收敛，则在一切 $|x|<|x_1|$ 处绝对收敛；若在 $x=x_2$ 发散，则在一切 $|x|>|x_2|$ 处发散。"))
    + thm("收敛半径", p("收敛半径 $R$ 为幂级数收敛区间的半径，计算方法：")+
    fml("R = \\lim_{n\\to\\infty}\\left|\\frac{a_n}{a_{n+1}}\\right| = \\frac{1}{\\lim\\sqrt[n]{|a_n|}}",
        "收敛区间为 $(-R,R)$，端点 $x=\\pm R$ 处需单独判断敛散性。"))
    + exa(p("<strong>例：</strong>$\\sum\\frac{x^n}{n}$，$R=\\lim\\frac{1/n}{1/(n+1)}=1$。在 $x=-1$ 处为 $\\sum\\frac{(-1)^n}{n}$（条件收敛），在 $x=1$ 处为 $\\sum\\frac{1}{n}$（发散）。收敛域为 $[-1,1)$。"))
)},
{"id":"c8s2-2","name":"函数展开为幂级数","tags":["thm","app"],"brief":"泰勒级数与麦克劳林级数。",
 "body": wrap(
    thm("泰勒级数", p("若 $f$ 在 $x_0$ 邻域内任意阶可导，则幂级数")+
    fml("\\sum_{n=0}^{\\infty}\\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n",
        "称为 $f$ 在 $x_0$ 处的泰勒级数。当 $x_0=0$ 时称为麦克劳林级数。$f$ 能展开为泰勒级数的充要条件是 $\\lim_{n\\to\\infty}R_n(x)=0$（余项趋于零）。"))
    + app(p("<strong>常用展开（麦克劳林）：</strong>")+
    fml("e^x=\\sum_{n=0}^\\infty\\frac{x^n}{n!}\\ (|x|<\\infty),\\quad \\sin x=\\sum_{n=0}^\\infty\\frac{(-1)^n x^{2n+1}}{(2n+1)!},\\quad \\cos x=\\sum_{n=0}^\\infty\\frac{(-1)^n x^{2n}}{(2n)!}",
        "$\\frac{1}{1-x}=\\sum_{n=0}^\\infty x^n\\ (|x|<1)$，$\\ln(1+x)=\\sum_{n=1}^\\infty\\frac{(-1)^{n-1}x^n}{n}\\ (|x|<1)$，$(1+x)^\\alpha=\\sum_{n=0}^\\infty\\binom{\\alpha}{n}x^n$。"))
)},
]
},
# ---- 8.3 傅里叶级数 ----
{
"name": "8.3 傅里叶级数",
"color": "#ec4899",
"desc": "三角函数系、傅里叶系数、收敛定理",
"items": [
{"id":"c8s3-1","name":"傅里叶级数的概念","tags":["def","thm","app"],"brief":"周期函数的三角级数展开。",
 "body": wrap(
    defn("傅里叶系数", p("设 $f(x)$ 以 $2\\pi$ 为周期，则其傅里叶级数为 $\\frac{a_0}{2}+\\sum_{n=1}^\\infty(a_n\\cos nx+b_n\\sin nx)$，其中系数")+
    fml("a_n = \\frac{1}{\\pi}\\int_{-\\pi}^{\\pi}f(x)\\cos nx\\,dx,\\quad b_n = \\frac{1}{\\pi}\\int_{-\\pi}^{\\pi}f(x)\\sin nx\\,dx"))
    + der(p("<strong>系数公式推导（利用三角函数系正交性）：</strong>三角函数系 $\\{1,\\cos x,\\sin x,\\cos 2x,\\sin 2x,\\dots\\}$ 在 $[-\\pi,\\pi]$ 上正交，即任意两个不同函数的乘积积分为零：")+
    fml("\\int_{-\\pi}^{\\pi}\\cos mx\\cos nx\\,dx = \\begin{cases}0, & m\\ne n \\\\ \\pi, & m=n\\ge 1 \\\\ 2\\pi, & m=n=0\\end{cases},\\quad \\int_{-\\pi}^{\\pi}\\sin mx\\sin nx\\,dx = \\begin{cases}0, & m\\ne n \\\\ \\pi, & m=n\\end{cases}",
        "且 $\\int_{-\\pi}^{\\pi}\\cos mx\\sin nx\\,dx=0$。将 $f(x)\\sim\\frac{a_0}{2}+\\sum(a_n\\cos nx+b_n\\sin nx)$ 两边乘 $\\cos mx$ 并在 $[-\\pi,\\pi]$ 积分，由正交性，右端仅 $n=m$ 项非零：$\\int f(x)\\cos mx\\,dx=a_m\\pi$，故 $a_m=\\frac{1}{\\pi}\\int f(x)\\cos mx\\,dx$。同理得 $b_m$。"))
    + thm("收敛定理（狄利克雷条件）", p("若 $f$ 在 $[-\\pi,\\pi]$ 满足：(1) 连续或只有有限个第一类间断点；(2) 只有有限个极值点，则傅里叶级数收敛，且和为")+
    fml("S(x) = \\frac{f(x^-)+f(x^+)}{2}",
        "在连续点处 $S(x)=f(x)$；在间断点处 $S(x)$ 为左右极限的平均值。"))
    + app(p("<strong>奇偶函数的傅里叶级数：</strong>若 $f$ 为奇函数，则 $a_n=0$，只有正弦项（正弦级数）；若 $f$ 为偶函数，则 $b_n=0$，只有余弦项（余弦级数）。<br>傅里叶级数是信号处理、频谱分析、偏微分方程分离变量法的数学基础。"))
)},
]
},
# ---- 8.4 级数应用 ----
{
"name": "8.4 级数应用",
"color": "#f472b6",
"desc": "函数逼近、解析函数、级数解微分方程",
"items": [
{"id":"c8s4-1","name":"级数的应用","tags":["app","exa","note"],"brief":"近似计算、欧拉公式、级数解。",
 "body": wrap(
    app(p("<strong>近似计算：</strong>利用幂级数展开可计算函数值和定积分。例：$e=\\sum_{n=0}^\\infty\\frac{1}{n!}$，取前 10 项即可得到高精度值。")+
    fml("\\pi = 4\\arctan 1 = 4\\sum_{n=0}^\\infty\\frac{(-1)^n}{2n+1}",
        "虽然该级数收敛慢，但可加速或用更快的公式（如马青公式）。"))
    + app(p("<strong>欧拉公式：</strong>由 $e^x$、$\\sin x$、$\\cos x$ 的幂级数展开，形式上可得")+
    fml("e^{ix} = \\cos x + i\\sin x",
        "令 $x=\\pi$ 得著名的欧拉恒等式 $e^{i\\pi}+1=0$，联系了数学中最重要的五个常数。"))
    + app(p("<strong>微分方程的级数解：</strong>某些变系数微分方程（如勒让德方程、贝塞尔方程）无法用初等函数求解，但可设解为幂级数 $y=\\sum a_n x^n$ 代入方程，递推求出系数。这是特殊函数理论的基础。"))
    + note(p("级数是分析学的核心工具：它将复杂函数表示为简单函数（多项式、三角函数）的叠加，是函数逼近、数值计算、信号处理和现代物理学的基础。"))
)},
]
},
# ---- 8.5 函数项级数与一致收敛 ----
{
"name": "8.5 函数项级数与一致收敛",
"color": "#be185d",
"desc": "函数列与函数项级数的一致收敛、魏尔斯特拉斯判别法、逐项积分与求导",
"items": [
{"id":"c8s5-1","name":"一致收敛的概念与判别","tags":["def","thm","der"],"brief":"逐点收敛与一致收敛的区别。",
 "body": wrap(
    defn("一致收敛", p("设函数列 $\\{f_n(x)\\}$ 在区间 $I$ 上逐点收敛于 $f(x)$。若对任意 $\\varepsilon>0$，存在与 $x$ 无关的正整数 $N$，使得当 $n>N$ 时，对一切 $x\\in I$ 都有 $|f_n(x)-f(x)|<\\varepsilon$，则称 $\\{f_n\\}$ 在 $I$ 上<strong>一致收敛</strong>于 $f$，记作 $f_n\\rightrightarrows f$。"))
    + thm("一致收敛的柯西准则", p("$\\{f_n\\}$ 在 $I$ 上一致收敛 $\\Leftrightarrow$ 对任意 $\\varepsilon>0$，存在 $N$，当 $m,n>N$ 时，对一切 $x\\in I$ 有 $|f_m(x)-f_n(x)|<\\varepsilon$。"))
    + thm("魏尔斯特拉斯 M 判别法", p("对函数项级数 $\\sum u_n(x)$，若存在收敛的正项级数 $\\sum M_n$，使得对一切 $x\\in I$ 有 $|u_n(x)|\\le M_n$，则 $\\sum u_n(x)$ 在 $I$ 上一致收敛且绝对收敛。"))
    + der(p("<strong>一致收敛 vs 逐点收敛：</strong>逐点收敛的 $N$ 可依赖于 $x$；一致收敛要求存在公共的 $N$ 对所有 $x$ 适用。例：$f_n(x)=x^n$ 在 $[0,1)$ 逐点收敛于 0，但不一致收敛（当 $x$ 接近 1 时需 $n$ 很大才能使 $x^n<\\varepsilon$）。而在 $[0,a]$（$a<1$）上一致收敛。<br>一致收敛保证了极限运算与积分、求导运算的可交换性。"))
)},
{"id":"c8s5-2","name":"一致收敛级数的性质","tags":["thm","app"],"brief":"和函数的连续性、逐项积分、逐项求导。",
 "body": wrap(
    thm("连续性定理", p("若 $u_n(x)$ 都在 $I$ 上连续，且 $\\sum u_n(x)$ 在 $I$ 上一致收敛于 $S(x)$，则 $S(x)$ 在 $I$ 上连续。即：<br>$\\lim_{x\\to x_0}S(x)=S(x_0)$，或 $\\lim_{x\\to x_0}\\sum u_n(x)=\\sum u_n(x_0)=\\sum\\lim_{x\\to x_0}u_n(x)$（极限与求和可交换）。"))
    + thm("逐项积分定理", p("若 $u_n(x)$ 在 $[a,b]$ 连续，$\\sum u_n(x)$ 在 $[a,b]$ 一致收敛于 $S(x)$，则")+
    fml("\\int_a^b S(x)\\,dx = \\sum_{n=1}^\\infty\\int_a^b u_n(x)\\,dx",
        "即积分与求和可交换。"))
    + thm("逐项求导定理", p("若 $u_n(x)$ 在 $I$ 上有连续导数，$\\sum u_n(x)$ 在 $I$ 上逐点收敛，且 $\\sum u_n'(x)$ 在 $I$ 上一致收敛，则 $\\sum u_n(x)$ 在 $I$ 上一致收敛，且可逐项求导：")+
    fml("\\left(\\sum_{n=1}^\\infty u_n(x)\\right)' = \\sum_{n=1}^\\infty u_n'(x)"))
    + app(p("<strong>应用：</strong>一致收敛理论是幂级数在收敛区间内可逐项积分、逐项求导的理论基础。例如 $\\frac{1}{1-x}=\\sum_{n=0}^\\infty x^n$ 在 $(-1,1)$ 内闭一致收敛，逐项积分得 $-\\ln(1-x)=\\sum_{n=1}^\\infty\\frac{x^n}{n}$；逐项求导得 $\\frac{1}{(1-x)^2}=\\sum_{n=1}^\\infty n x^{n-1}$。"))
    + note(p("一致收敛是分析学中保证运算可交换的关键条件。没有一致收敛，和函数可能不连续、不可逐项积分或求导。这一理论由魏尔斯特拉斯严格建立，是现代分析学的基石。"))
)},
]
},
]
print(f"Ch8: {sum(len(s['items']) for s in ch8_sections)} items")

# =====================================================
#  ASSEMBLE CHAPTERS & GENERATE HTML
# =====================================================
CHAPTERS = [
    {"id":"c-ch1","num":"第一章","title":"一元微分","en":"ONE-VARIABLE DIFFERENTIAL CALCULUS",
     "desc":"从极限与连续出发，建立导数与微分的概念，掌握求导法则与高阶导数，为整个微积分奠定基础。",
     "sections": ch1_sections},
    {"id":"c-ch2","num":"第二章","title":"微分定理","en":"DIFFERENTIAL THEOREMS",
     "desc":"微分中值定理（罗尔、拉格朗日、柯西）是微分学的理论核心，泰勒公式提供函数的多项式逼近，洛必达法则处理不定式，极值与凸性刻画函数形态。",
     "sections": ch2_sections},
    {"id":"c-ch3","num":"第三章","title":"一元积分","en":"ONE-VARIABLE INTEGRAL CALCULUS",
     "desc":"不定积分的计算技巧（换元法、分部积分），定积分的黎曼定义与牛顿-莱布尼茨公式，以及反常积分的收敛判别。",
     "sections": ch3_sections},
    {"id":"c-ch4","num":"第四章","title":"微分方程","en":"DIFFERENTIAL EQUATIONS",
     "desc":"一阶方程的可分离变量、齐次、线性、伯努利解法，可降阶高阶方程，二阶常系数线性方程的特征方程法，以及弹簧振子、RLC 电路、人口模型等应用。",
     "sections": ch4_sections},
    {"id":"c-ch5","num":"第五章","title":"多元微分","en":"MULTIVARIABLE DIFFERENTIAL CALCULUS",
     "desc":"将微分学推广到多元函数：重极限与累次极限、偏导数与全微分、复合函数链式法则、隐函数与雅可比行列式、多元极值与拉格朗日乘数法。",
     "sections": ch5_sections},
    {"id":"c-ch6","num":"第六章","title":"多元积分","en":"MULTIPLE INTEGRALS",
     "desc":"二重积分、三重积分、曲线积分、曲面积分的概念与计算，多元积分在面积、体积、曲面面积、弧长、质心、转动惯量中的应用，以及含参积分与欧拉积分（Γ、Β函数）。",
     "sections": ch6_sections},
    {"id":"c-ch7","num":"第七章","title":"积分定理","en":"INTEGRAL THEOREMS",
     "desc":"格林公式、高斯公式、斯托克斯公式三大积分定理的完整表述与证明，以及梯度、散度、旋度与势场理论。",
     "sections": ch7_sections},
    {"id":"c-ch8","num":"第八章","title":"无穷级数","en":"INFINITE SERIES",
     "desc":"数项级数的收敛判别（比较、比值、根值、莱布尼茨），幂级数的收敛半径与函数展开，傅里叶级数的三角展开，以及级数在近似计算、欧拉公式、微分方程中的应用。",
     "sections": ch8_sections},
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
  .la-nav-tab.c6{color:#0e7490;border-color:#a5f3fc}
  .la-nav-tab.c7{color:#be185d;border-color:#fbcfe8}
  .la-nav-tab.c8{color:#9333ea;border-color:#e9d5ff}
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
  .la-phase-title.la-ch6::before{background:#0891b2}
  .la-phase-title.la-ch7::before{background:#be185d}
  .la-phase-title.la-ch8::before{background:#9333ea}
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
<meta name="description" content="微积分知识体系：一元微分、微分定理、一元积分、微分方程、多元微分、重积分、积分定理、无穷级数">
<title>微积分 · 知识体系</title>
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
    <div class="la-eyebrow">CALCULUS · KNOWLEDGE MAP</div>
    <h1>微积分 · 知识体系</h1>
    <p class="la-subtitle">一元微分 · 微分定理 · 一元积分 · 微分方程 · 多元微分 · 重积分 · 积分定理 · 无穷级数</p>
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
    <div>微积分 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于同济大学《高等数学》知识体系整理</div>
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
    with open("/workspace/calculus.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated calculus.html ({len(html)} chars)")

