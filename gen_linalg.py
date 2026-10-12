# -*- coding: utf-8 -*-
"""Generate linalg.html with 6 chapters: 线性空间/矩阵/行列式/线性方程组/特征值/线性代数应用."""
import json

# ---------- SVG figure library ----------
FIG = {
"vector": '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="200" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="170" y2="50" stroke="#3b82f6" stroke-width="2.5"/>
<polygon points="170,50 158,56 162,66" fill="#3b82f6"/>
<line x1="20" y1="130" x2="120" y2="90" stroke="#10b981" stroke-width="2" stroke-dasharray="5 3"/>
<text x="175" y="48" font-size="12" fill="#3b82f6">v</text>
<text x="123" y="86" font-size="12" fill="#10b981">u</text></svg>''',
"span": '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="200" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="180" y2="130" stroke="#dbeafe" stroke-width="8" opacity="0.6"/>
<line x1="30" y1="130" x2="60" y2="60" stroke="#3b82f6" stroke-width="2"/>
<line x1="30" y1="130" x2="110" y2="40" stroke="#10b981" stroke-width="2"/>
<text x="185" y="134" font-size="11" fill="#475569">span{v₁,v₂}</text></svg>''',
"basis": '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="200" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="20" y2="60" stroke="#ef4444" stroke-width="2.5"/>
<polygon points="20,60 14,70 26,70" fill="#ef4444"/>
<line x1="20" y1="130" x2="100" y2="130" stroke="#3b82f6" stroke-width="2.5"/>
<polygon points="100,130 90,124 90,136" fill="#3b82f6"/>
<text x="8" y="55" font-size="12" fill="#ef4444">e₂</text>
<text x="103" y="128" font-size="12" fill="#3b82f6">e₁</text></svg>''',
"transform": '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="200" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<rect x="40" y="70" width="50" height="50" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5" opacity="0.7"/>
<line x1="140" y1="130" x2="160" y2="60" stroke="#10b981" stroke-width="1.5"/>
<line x1="160" y1="60" x2="195" y2="45" stroke="#10b981" stroke-width="1.5"/>
<line x1="175" y1="115" x2="195" y2="45" stroke="#10b981" stroke-width="1.5"/>
<line x1="140" y1="130" x2="175" y2="115" stroke="#10b981" stroke-width="1.5"/>
<polygon points="40,70 40,60 50,60" fill="#3b82f6" opacity="0.3"/>
<text x="50" y="100" font-size="11" fill="#3b82f6">原图形</text>
<text x="150" y="80" font-size="11" fill="#10b981">T变换后</text></svg>''',
"det": '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="200" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<rect x="40" y="70" width="60" height="50" fill="#dbeafe" stroke="#3b82f6" stroke-width="1.5" opacity="0.6"/>
<text x="55" y="100" font-size="11" fill="#1e293b">area=det</text>
<line x1="120" y1="130" x2="180" y2="90" stroke="#ef4444" stroke-width="2"/>
<line x1="120" y1="130" x2="150" y2="60" stroke="#10b981" stroke-width="2"/>
<text x="185" y="85" font-size="11" fill="#ef4444">a</text>
<text x="150" y="55" font-size="11" fill="#10b981">b</text></svg>''',
"eigen": '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
<line x1="20" y1="130" x2="200" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="20" y1="130" x2="20" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
<line x1="110" y1="130" x2="110" y2="20" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3 3"/>
<ellipse cx="110" cy="75" rx="70" ry="40" fill="none" stroke="#3b82f6" stroke-width="2"/>
<line x1="40" y1="75" x2="180" y2="75" stroke="#ef4444" stroke-width="2.5"/>
<text x="183" y="72" font-size="11" fill="#ef4444">特征向量方向</text></svg>''',
"svd": '''<svg viewBox="0 0 220 150" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="60" cy="75" rx="35" ry="35" fill="#dbeafe" stroke="#3b82f6" stroke-width="2"/>
<text x="48" y="79" font-size="11" fill="#1e293b">A</text>
<line x1="100" y1="75" x2="130" y2="75" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>
<polygon points="130,75 122,71 122,79" fill="#94a3b8"/>
<ellipse cx="170" cy="75" rx="40" ry="25" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/>
<text x="160" y="79" font-size="11" fill="#1e293b">ΣVᵀ</text>
<text x="90" y="60" font-size="10" fill="#94a3b8">UΣVᵀ</text></svg>''',
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","his":"注 记","note":"备 注"}

# ---------- 核心公式清单 ----------
CORE_FORMULAS = [
    ("线性组合", "\\mathbf{v} = c_1\\mathbf{v}_1 + c_2\\mathbf{v}_2 + \\cdots + c_n\\mathbf{v}_n", "向量用基线性表示"),
    ("内积（欧氏）", "\\langle\\mathbf{u},\\mathbf{v}\\rangle = u_1v_1+u_2v_2+\\cdots+u_nv_n", "欧氏空间的标准内积"),
    ("施密特正交化", "\\mathbf{q}_k = \\mathbf{v}_k - \\sum_{i=1}^{k-1}\\frac{\\langle\\mathbf{v}_k,\\mathbf{q}_i\\rangle}{\\langle\\mathbf{q}_i,\\mathbf{q}_i\\rangle}\\mathbf{q}_i", "将任意基化为正交基"),
    ("矩阵乘法", "(AB)_{ij} = \\sum_{k=1}^{n}a_{ik}b_{kj}", "行乘列的求和定义"),
    ("逆矩阵公式", "A^{-1} = \\frac{1}{\\det A}\\,\\mathrm{adj}(A)", "伴随矩阵法求逆"),
    ("行列式展开", "\\det A = \\sum_{j=1}^{n}a_{ij}A_{ij}", "按第 i 行展开（A_{ij} 为代数余子式）"),
    ("克拉默法则", "x_i = \\frac{\\det A_i}{\\det A}", "n 阶线性方程组的行列式解法"),
    ("秩-零度定理", "\\mathrm{rank}(A) + \\mathrm{nullity}(A) = n", "列空间维数 + 零空间维数 = 列数"),
    ("特征值方程", "A\\mathbf{v} = \\lambda\\mathbf{v}", "特征向量在线性变换下只伸缩不旋转"),
    ("特征多项式", "\\det(A - \\lambda I) = 0", "特征值是特征多项式的根"),
    ("对角化", "A = PDP^{-1},\\quad D = \\mathrm{diag}(\\lambda_1,\\ldots,\\lambda_n)", "可对角化矩阵的谱分解"),
    ("凯莱-哈密顿定理", "p_A(A) = 0", "矩阵满足自身的特征多项式"),
    ("二次型", "Q(\\mathbf{x}) = \\mathbf{x}^T A\\mathbf{x}", "二次齐次多项式的矩阵表示"),
    ("正定矩阵判据", "A \\text{ 正定} \\Leftrightarrow \\forall \\mathbf{x}\\neq 0, \\mathbf{x}^T A\\mathbf{x} > 0", "对称矩阵正定性的定义"),
    ("酉矩阵", "U^*U = I \\Leftrightarrow U^{-1}=U^*", "列向量构成标准正交基"),
    ("厄米矩阵", "A = A^* \\Leftrightarrow a_{ij} = \\overline{a_{ji}}", "共轭转置等于自身"),
    ("辛矩阵", "S^T J S = J,\\quad J = \\begin{pmatrix}0 & I\\\\-I & 0\\end{pmatrix}", "保持辛形式的线性变换"),
    ("奇异值分解", "A = U\\Sigma V^*", "任意矩阵的正交对角化分解"),
    ("LU 分解", "A = LU", "下三角×上三角分解，用于高效解方程组"),
    ("维数公式", "\\dim(W_1+W_2)=\\dim W_1+\\dim W_2-\\dim(W_1\\cap W_2)", "子空间和的维数等于维数和减去交的维数"),
    ("直和判定", "W_1\\oplus W_2 \\Leftrightarrow W_1\\cap W_2=\\{0\\}", "两子空间交为零则和为直和"),
    ("迹的性质", "\\mathrm{tr}(AB)=\\mathrm{tr}(BA)", "矩阵乘积的迹与顺序无关"),
    ("行列式乘法定理", "\\det(AB)=\\det A\\cdot\\det B", "乘积的行列式等于行列式的乘积"),
    ("拉普拉斯展开", "D=\\sum_{i} M_i A_i", "按 k 行(列)展开，子式乘代数余子式求和"),
    ("瑞利商极值", "\\lambda_{\\max}=\\max_{\\|\\mathbf{x}\\|=1}\\mathbf{x}^TA\\mathbf{x}", "实对称矩阵最大特征值为瑞利商最大值"),
    ("代数几何重数不等式", "g_\\lambda\\le a_\\lambda", "特征值的几何重数不超过代数重数"),
    ("合同对角化", "C^TAC=\\mathrm{diag}(d_1,\\ldots,d_n)", "对称矩阵必合同于对角矩阵"),
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
#  CHAPTER 1: 线性空间
# =====================================================
ch1_sections = [
# ---- 1.1 向量空间 ----
{
"name": "1.1 向量空间",
"color": "#2563eb",
"desc": "向量空间的公理、子空间、线性组合与张成空间",
"items": [
{"id":"c1s1-1","name":"向量空间的定义","tags":["def","note"],"brief":"八条公理刻画的代数结构。",
 "fig":"vector","figCap":"向量的几何表示：有向线段",
 "body": wrap(
    defn("向量空间", p("设 $V$ 是非空集合，$\\mathbb{F}$ 是数域。在 $V$ 上定义加法 $+$ 和数乘 $\\cdot$，若满足以下八条公理，则称 $V$ 为 $\\mathbb{F}$ 上的向量空间：<br>(1) 加法交换律 $\\mathbf{u}+\\mathbf{v}=\\mathbf{v}+\\mathbf{u}$；(2) 加法结合律；(3) 存在零向量 $\\mathbf{0}$；(4) 每个 $\\mathbf{v}$ 有负元 $-\\mathbf{v}$；(5) 数乘结合律 $a(b\\mathbf{v})=(ab)\\mathbf{v}$；(6) $1\\cdot\\mathbf{v}=\\mathbf{v}$；(7) 数乘对向量加法分配 $a(\\mathbf{u}+\\mathbf{v})=a\\mathbf{u}+a\\mathbf{v}$；(8) 数乘对数域加法分配 $(a+b)\\mathbf{v}=a\\mathbf{v}+b\\mathbf{v}$。"))
    + note(p("常见向量空间：$\\mathbb{R}^n$（实坐标空间）、$\\mathbb{C}^n$（复坐标空间）、$P_n$（次数不超过 $n$ 的多项式）、$M_{m\\times n}$（$m\\times n$ 矩阵）、$C[a,b]$（$[a,b]$ 上连续函数）。向量空间的元素统称为向量。"))
)},
{"id":"c1s1-2","name":"子空间","tags":["def","thm","der"],"brief":"对加法与数乘封闭的子集。",
 "body": wrap(
    defn("子空间", p("设 $W$ 是向量空间 $V$ 的非空子集。若 $W$ 对 $V$ 中的加法和数乘封闭（即 $\\forall\\mathbf{u},\\mathbf{v}\\in W,\\;a\\in\\mathbb{F}$，有 $\\mathbf{u}+\\mathbf{v}\\in W$，$a\\mathbf{v}\\in W$），则 $W$ 本身构成一个向量空间，称为 $V$ 的子空间。"))
    + thm("子空间判定定理", p("非空子集 $W\\subseteq V$ 是子空间当且仅当 $W$ 对线性组合封闭，即 $\\forall\\mathbf{u},\\mathbf{v}\\in W,\\;a,b\\in\\mathbb{F}$，都有 $a\\mathbf{u}+b\\mathbf{v}\\in W$。"))
    + der(p("<strong>证明：</strong>若 $W$ 是子空间，则由封闭性显然对线性组合封闭。反之，若 $W$ 对线性组合封闭：取 $a=b=1$ 得加法封闭；取 $a=0$ 得 $0\\mathbf{v}=\\mathbf{0}\\in W$（零元存在）；取 $a=-1,b=0$ 得 $-\\mathbf{v}\\in W$（负元存在）；取 $b=0$ 得数乘封闭。其余公理由 $V$ 继承。故 $W$ 是向量空间。"))
)},
{"id":"c1s1-3","name":"线性组合与张成空间","tags":["def","thm"],"brief":"span 是包含给定向量组的最小子空间。",
 "fig":"span","figCap":"两个向量张成的子空间（平面）",
 "body": wrap(
    defn("线性组合与张成空间", p("设 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_k\\in V$，形如 $c_1\\mathbf{v}_1+\\cdots+c_k\\mathbf{v}_k$（$c_i\\in\\mathbb{F}$）的向量称为 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_k$ 的线性组合。所有线性组合构成的集合称为张成空间，记作 $\\mathrm{span}\\{\\mathbf{v}_1,\\ldots,\\mathbf{v}_k\\}$。"))
    + thm("张成空间是子空间", p("$\\mathrm{span}\\{\\mathbf{v}_1,\\ldots,\\mathbf{v}_k\\}$ 是 $V$ 的子空间，且是包含 $\\{\\mathbf{v}_1,\\ldots,\\mathbf{v}_k\\}$ 的最小子空间。"))
)}
]},
# ---- 1.2 线性相关与基 ----
{
"name": "1.2 线性相关与基",
"color": "#0d9488",
"desc": "线性相关性、基与维数、坐标变换",
"items": [
{"id":"c1s2-1","name":"线性相关与线性无关","tags":["def","thm","der"],"brief":"判断向量组是否存在非平凡线性关系。",
 "body": wrap(
    defn("线性相关/无关", p("向量组 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_k$ 称为<strong>线性相关</strong>，若存在不全为零的数 $c_1,\\ldots,c_k$ 使得 $c_1\\mathbf{v}_1+\\cdots+c_k\\mathbf{v}_k=\\mathbf{0}$。否则称为<strong>线性无关</strong>，即 $c_1\\mathbf{v}_1+\\cdots+c_k\\mathbf{v}_k=\\mathbf{0}$ 仅当所有 $c_i=0$。"))
    + thm("线性相关的等价刻画", p("向量组线性相关 $\\Leftrightarrow$ 至少有一个向量可由其余向量线性表示。"))
    + der(p("<strong>证明：</strong>若线性相关，存在不全为零的 $c_i$ 使 $\\sum c_i\\mathbf{v}_i=0$。设 $c_j\\neq 0$，则 $\\mathbf{v}_j=-\\sum_{i\\neq j}(c_i/c_j)\\mathbf{v}_i$，即 $\\mathbf{v}_j$ 可由其余表示。反之，若 $\\mathbf{v}_j=\\sum_{i\\neq j}a_i\\mathbf{v}_i$，则 $\\sum_{i\\neq j}a_i\\mathbf{v}_i-\\mathbf{v}_j=0$，系数不全为零，故线性相关。"))
)},
{"id":"c1s2-2","name":"基与维数","tags":["def","thm","der"],"brief":"极大线性无关组决定空间维数。",
 "fig":"basis","figCap":"标准基 e₁, e₂ 张成平面",
 "body": wrap(
    defn("基与维数", p("向量空间 $V$ 的<strong>基</strong>是 $V$ 中一个线性无关且张成 $V$ 的向量组。基中向量的个数称为 $V$ 的<strong>维数</strong>，记作 $\\dim V$。若 $V$ 不存在有限基，则称 $V$ 是无限维的。"))
    + thm("基的等价定义", p("向量组 $B=\\{\\mathbf{v}_1,\\ldots,\\mathbf{v}_n\\}$ 是 $V$ 的基当且仅当 $V$ 中每个向量都可<strong>唯一</strong>地表示为 $B$ 中向量的线性组合。"))
    + der(p("<strong>证明：</strong>若 $B$ 是基，则 $\\mathrm{span}(B)=V$ 保证表示存在，线性无关保证表示唯一。反之，若每个向量有唯一表示，则 $\\mathrm{span}(B)=V$（存在性），且 $\\sum c_i\\mathbf{v}_i=0$ 是零向量的表示，由唯一性必有 $c_i=0$，故线性无关。"))
    + thm("维数不变性", p("同一向量空间的任意两组基所含向量个数相同。"))
)},
{"id":"c1s2-3","name":"坐标与基变换","tags":["def","thm","der"],"brief":"过渡矩阵联系不同基下的坐标。",
 "body": wrap(
    defn("坐标", p("设 $B=\\{\\mathbf{v}_1,\\ldots,\\mathbf{v}_n\\}$ 是 $V$ 的一组基，$\\mathbf{v}\\in V$ 有唯一表示 $\\mathbf{v}=c_1\\mathbf{v}_1+\\cdots+c_n\\mathbf{v}_n$，则 $(c_1,\\ldots,c_n)^T$ 称为 $\\mathbf{v}$ 在基 $B$ 下的坐标，记作 $[\\mathbf{v}]_B$。"))
    + thm("基变换公式", p("设 $B=\\{\\mathbf{v}_1,\\ldots,\\mathbf{v}_n\\}$ 和 $B'=\\{\\mathbf{v}_1',\\ldots,\\mathbf{v}_n'\\}$ 是 $V$ 的两组基，且 $\\mathbf{v}_j'=\\sum_{i=1}^n p_{ij}\\mathbf{v}_i$，则过渡矩阵 $P=(p_{ij})$ 可逆，且坐标变换满足 $[\\mathbf{v}]_B = P[\\mathbf{v}]_{B'}$。"))
    + der(p("<strong>证明：</strong>设 $\\mathbf{v}=\\sum_j c_j'\\mathbf{v}_j'=\\sum_j c_j'\\sum_i p_{ij}\\mathbf{v}_i=\\sum_i(\\sum_j p_{ij}c_j')\\mathbf{v}_i$。又 $\\mathbf{v}=\\sum_i c_i\\mathbf{v}_i$，由表示唯一得 $c_i=\\sum_j p_{ij}c_j'$，即 $[\\mathbf{v}]_B=P[\\mathbf{v}]_{B'}$。$P$ 可逆是因为 $B'$ 线性无关，故 $P$ 的列线性无关，从而 $\\det P\\neq 0$。"))
)}
]},
# ---- 1.3 内积空间 ----
{
"name": "1.3 内积空间",
"color": "#059669",
"desc": "内积、正交性、施密特正交化、投影",
"items": [
{"id":"c1s3-1","name":"内积的定义","tags":["def","thm","der","note"],"brief":"赋予向量长度与夹角的双线性函数。",
 "body": wrap(
    defn("内积", p("设 $V$ 是 $\\mathbb{F}$ 上的向量空间。函数 $\\langle\\cdot,\\cdot\\rangle:V\\times V\\to\\mathbb{F}$ 称为内积，若满足：(1) 对第一变元线性 $\\langle a\\mathbf{u}+b\\mathbf{v},\\mathbf{w}\\rangle=a\\langle\\mathbf{u},\\mathbf{w}\\rangle+b\\langle\\mathbf{v},\\mathbf{w}\\rangle$；(2) 共轭对称性 $\\langle\\mathbf{u},\\mathbf{v}\\rangle=\\overline{\\langle\\mathbf{v},\\mathbf{u}\\rangle}$；(3) 正定性 $\\langle\\mathbf{v},\\mathbf{v}\\rangle\\ge 0$，等号当且仅当 $\\mathbf{v}=0$。赋予内积的向量空间称为内积空间。"))
    + thm("柯西-施瓦茨不等式", p("对内积空间中任意向量 $\\mathbf{u},\\mathbf{v}$，有 $|\\langle\\mathbf{u},\\mathbf{v}\\rangle|\\le\\|\\mathbf{u}\\|\\|\\mathbf{v}\\|$，等号当且仅当 $\\mathbf{u},\\mathbf{v}$ 线性相关。"))
    + der(p("<strong>证明：</strong>若 $\\mathbf{v}=0$，不等式显然成立。设 $\\mathbf{v}\\neq 0$。对任意实数 $t$，由正定性 $\\langle\\mathbf{u}-t\\mathbf{v},\\mathbf{u}-t\\mathbf{v}\\rangle\\ge 0$。展开：$\\|\\mathbf{u}\\|^2-2t\\,\\mathrm{Re}\\langle\\mathbf{u},\\mathbf{v}\\rangle+t^2\\|\\mathbf{v}\\|^2\\ge 0$。这是关于 $t$ 的二次函数恒非负，故判别式 $\\le 0$：$4(\\mathrm{Re}\\langle\\mathbf{u},\\mathbf{v}\\rangle)^2-4\\|\\mathbf{u}\\|^2\\|\\mathbf{v}\\|^2\\le 0$，即 $(\\mathrm{Re}\\langle\\mathbf{u},\\mathbf{v}\\rangle)^2\\le\\|\\mathbf{u}\\|^2\\|\\mathbf{v}\\|^2$。取 $\\theta$ 使 $e^{i\\theta}\\langle\\mathbf{u},\\mathbf{v}\\rangle=|\\langle\\mathbf{u},\\mathbf{v}\\rangle|$（实数），用 $e^{i\\theta}\\mathbf{u}$ 代 $\\mathbf{u}$ 得 $|\\langle\\mathbf{u},\\mathbf{v}\\rangle|\\le\\|\\mathbf{u}\\|\\|\\mathbf{v}\\|$。等号成立当且仅当判别式为 0，即存在 $t$ 使 $\\mathbf{u}-t\\mathbf{v}=0$，即线性相关。"))
    + note(p("欧氏空间中标准内积：$\\langle\\mathbf{u},\\mathbf{v}\\rangle=u_1v_1+\\cdots+u_nv_n$。向量长度 $\\|\\mathbf{v}\\|=\\sqrt{\\langle\\mathbf{v},\\mathbf{v}\\rangle}$。由柯西-施瓦茨不等式可定义夹角 $\\cos\\theta=\\frac{\\langle\\mathbf{u},\\mathbf{v}\\rangle}{\\|\\mathbf{u}\\|\\|\\mathbf{v}\\|}$。"))
)},
{"id":"c1s3-2","name":"正交与正交基","tags":["def","thm"],"brief":"两两正交的非零向量组必线性无关。",
 "body": wrap(
    defn("正交与标准正交基", p("若 $\\langle\\mathbf{u},\\mathbf{v}\\rangle=0$，称 $\\mathbf{u},\\mathbf{v}$ 正交。一组两两正交的非零向量称为正交向量组；若每个向量长度还为 1，则称为标准正交向量组。由标准正交向量组构成的基称为标准正交基。"))
    + thm("正交向量组线性无关", p("设 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_k$ 为正交向量组，则它们线性无关。"))
    + der(p("<strong>证明：</strong>设 $\\sum_{i=1}^k c_i\\mathbf{v}_i=0$。两边与 $\\mathbf{v}_j$ 作内积：$\\langle\\sum c_i\\mathbf{v}_i,\\mathbf{v}_j\\rangle=\\sum c_i\\langle\\mathbf{v}_i,\\mathbf{v}_j\\rangle=c_j\\|\\mathbf{v}_j\\|^2=0$。因 $\\mathbf{v}_j\\neq 0$，故 $\\|\\mathbf{v}_j\\|^2>0$，得 $c_j=0$。由 $j$ 的任意性，所有 $c_i=0$，故线性无关。"))
)},
{"id":"c1s3-3","name":"施密特正交化","tags":["thm","der","app"],"brief":"将任意基化为标准正交基的算法。",
 "body": wrap(
    thm("Gram-Schmidt 正交化", p("设 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_n$ 是内积空间的一组基，则按如下递推得到正交基 $\\mathbf{q}_1,\\ldots,\\mathbf{q}_n$：<br>$\\mathbf{q}_1=\\mathbf{v}_1$，$\\mathbf{q}_k=\\mathbf{v}_k-\\sum_{i=1}^{k-1}\\frac{\\langle\\mathbf{v}_k,\\mathbf{q}_i\\rangle}{\\langle\\mathbf{q}_i,\\mathbf{q}_i\\rangle}\\mathbf{q}_i$（$k=2,\\ldots,n$）。再单位化 $\\mathbf{e}_i=\\mathbf{q}_i/\\|\\mathbf{q}_i\\|$ 得标准正交基。"))
    + der(p("<strong>正确性证明（归纳法）：</strong>$k=1$ 显然。假设 $\\mathbf{q}_1,\\ldots,\\mathbf{q}_{k-1}$ 两两正交。对 $j<k$，$\\langle\\mathbf{q}_k,\\mathbf{q}_j\\rangle=\\langle\\mathbf{v}_k,\\mathbf{q}_j\\rangle-\\sum_{i<k}\\frac{\\langle\\mathbf{v}_k,\\mathbf{q}_i\\rangle}{\\langle\\mathbf{q}_i,\\mathbf{q}_i\\rangle}\\langle\\mathbf{q}_i,\\mathbf{q}_j\\rangle$。由归纳假设，仅 $i=j$ 项非零，故 $=\\langle\\mathbf{v}_k,\\mathbf{q}_j\\rangle-\\frac{\\langle\\mathbf{v}_k,\\mathbf{q}_j\\rangle}{\\langle\\mathbf{q}_j,\\mathbf{q}_j\\rangle}\\langle\\mathbf{q}_j,\\mathbf{q}_j\\rangle=0$。故 $\\mathbf{q}_k$ 与所有 $\\mathbf{q}_j$（$j<k$）正交。"))
)},
{"id":"c1s3-4","name":"投影与最小二乘","tags":["thm","der","app"],"brief":"正交投影给出最佳逼近。",
 "body": wrap(
    defn("正交投影", p("设 $W$ 是内积空间 $V$ 的有限维子空间，$\\mathbf{v}\\in V$。$\\mathbf{v}$ 在 $W$ 上的正交投影 $\\mathrm{proj}_W\\mathbf{v}$ 是 $W$ 中满足 $\\mathbf{v}-\\mathrm{proj}_W\\mathbf{v}\\perp W$ 的唯一向量。"))
    + thm("最佳逼近定理", p("设 $W$ 是有限维子空间，则 $\\mathrm{proj}_W\\mathbf{v}$ 是 $W$ 中到 $\\mathbf{v}$ 距离最近的向量：$\\|\\mathbf{v}-\\mathrm{proj}_W\\mathbf{v}\\|\\le\\|\\mathbf{v}-\\mathbf{w}\\|$，$\\forall\\mathbf{w}\\in W$。"))
    + der(p("<strong>证明：</strong>设 $\\mathbf{p}=\\mathrm{proj}_W\\mathbf{v}$，则 $\\mathbf{v}-\\mathbf{p}\\perp W$。对任意 $\\mathbf{w}\\in W$，$\\mathbf{v}-\\mathbf{w}=(\\mathbf{v}-\\mathbf{p})+(\\mathbf{p}-\\mathbf{w})$，其中 $\\mathbf{p}-\\mathbf{w}\\in W$，故 $\\mathbf{v}-\\mathbf{p}\\perp\\mathbf{p}-\\mathbf{w}$。由勾股定理：$\\|\\mathbf{v}-\\mathbf{w}\\|^2=\\|\\mathbf{v}-\\mathbf{p}\\|^2+\\|\\mathbf{p}-\\mathbf{w}\\|^2\\ge\\|\\mathbf{v}-\\mathbf{p}\\|^2$，等号当且仅当 $\\mathbf{w}=\\mathbf{p}$。"))
)}
]},
# ---- 1.4 线性相关性判定与极大无关组 ----
{
"name": "1.4 线性相关性判定与极大无关组",
"color": "#0891b2",
"desc": "线性相关性的判定方法、极大线性无关组与向量组的秩",
"items": [
{"id":"c1s4-1","name":"线性相关性的判定方法","tags":["thm","der"],"brief":"用行列式、秩或定义判定向量组的线性相关性。",
 "body": wrap(
    thm("线性相关性的判定", p("设 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_k\\in\\mathbb{F}^n$，以它们为列（行）构成矩阵 $A$。则：<br>(1) 若 $k>n$，向量组必线性相关；<br>(2) 若 $k=n$，线性相关 $\\Leftrightarrow \\det A=0$；线性无关 $\\Leftrightarrow \\det A\\neq 0$；<br>(3) 一般情形，线性相关 $\\Leftrightarrow \\mathrm{rank}(A)<k$；线性无关 $\\Leftrightarrow \\mathrm{rank}(A)=k$。"))
    + der(p("<strong>(1) 的证明：</strong>若 $k>n$，则齐次方程组 $A\\mathbf{x}=\\mathbf{0}$ 有 $n$ 个方程 $k$ 个未知量，未知量个数多于方程个数，必有非零解，故线性相关。<br><strong>(2) 的证明：</strong>$k=n$ 时，$\\mathbf{v}_1,\\ldots,\\mathbf{v}_n$ 线性相关 $\\Leftrightarrow$ 存在不全为零的 $c_i$ 使 $\\sum c_i\\mathbf{v}_i=0$ $\\Leftrightarrow$ $A\\mathbf{c}=0$ 有非零解 $\\Leftrightarrow$ $\\det A=0$（方阵奇异）。<br><strong>(3) 的证明：</strong>一般地，$\\sum c_i\\mathbf{v}_i=0$ 有非零解 $\\Leftrightarrow$ $A$ 的列向量线性相关 $\\Leftrightarrow$ 列秩 $<k$ $\\Leftrightarrow$ $\\mathrm{rank}(A)<k$。"))
)},
{"id":"c1s4-2","name":"极大线性无关组与向量组的秩","tags":["def","thm","der"],"brief":"极大无关组所含向量个数即向量组的秩。",
 "body": wrap(
    defn("极大线性无关组", p("向量组 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_k$ 的一个部分组 $\\mathbf{v}_{i_1},\\ldots,\\mathbf{v}_{i_r}$ 称为极大线性无关组，若它本身线性无关，且再加入原向量组中任一其他向量就线性相关。极大无关组所含向量个数 $r$ 称为向量组的秩，记作 $r(\\mathbf{v}_1,\\ldots,\\mathbf{v}_k)$。"))
    + thm("秩的性质", p("(1) 向量组的秩等于以其为列的矩阵的秩；(2) 等价的向量组有相同的秩；(3) 若向量组 $A$ 可由向量组 $B$ 线性表示，则 $r(A)\\le r(B)$。"))
    + der(p("<strong>(1) 的证明：</strong>以 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_k$ 为列构成矩阵 $A$。$A$ 的列秩就是列向量组的极大无关组所含向量个数，而列秩=秩=$\\mathrm{rank}(A)$。<br><strong>(3) 的证明：</strong>设 $A$ 可由 $B$ 表示，则 $\\mathrm{span}(A)\\subseteq\\mathrm{span}(B)$，故 $\\dim\\mathrm{span}(A)\\le\\dim\\mathrm{span}(B)$，即 $r(A)\\le r(B)$。"))
)}
]},
# ---- 1.5 子空间的交与直和 ----
{
"name": "1.5 子空间的交与直和",
"color": "#0e7490",
"desc": "子空间的交与和、维数公式、直和的判定与商空间",
"items": [
{"id":"c1s5-1","name":"子空间的交与和及维数公式","tags":["def","thm","der"],"brief":"dim(W1+W2)=dimW1+dimW2-dim(W1∩W2)。",
 "body": wrap(
    defn("子空间的交与和", p("设 $W_1,W_2$ 是 $V$ 的子空间。交 $W_1\\cap W_2=\\{\\mathbf{v}:\\mathbf{v}\\in W_1\\text{ 且 }\\mathbf{v}\\in W_2\\}$；和 $W_1+W_2=\\{\\mathbf{w}_1+\\mathbf{w}_2:\\mathbf{w}_1\\in W_1,\\mathbf{w}_2\\in W_2\\}$。两者都是 $V$ 的子空间。"))
    + thm("维数公式", p("$\\dim(W_1+W_2)=\\dim W_1+\\dim W_2-\\dim(W_1\\cap W_2)$。"))
    + der(p("<strong>证明：</strong>设 $\\dim(W_1\\cap W_2)=t$，取其一组基 $\\boldsymbol{\\alpha}_1,\\ldots,\\boldsymbol{\\alpha}_t$。扩充为 $W_1$ 的基 $\\boldsymbol{\\alpha}_1,\\ldots,\\boldsymbol{\\alpha}_t,\\boldsymbol{\\beta}_1,\\ldots,\\boldsymbol{\\beta}_s$（故 $\\dim W_1=t+s$），再扩充为 $W_2$ 的基 $\\boldsymbol{\\alpha}_1,\\ldots,\\boldsymbol{\\alpha}_t,\\boldsymbol{\\gamma}_1,\\ldots,\\boldsymbol{\\gamma}_r$（故 $\\dim W_2=t+r$）。<br><strong>断言：</strong>$\\boldsymbol{\\alpha}_1,\\ldots,\\boldsymbol{\\alpha}_t,\\boldsymbol{\\beta}_1,\\ldots,\\boldsymbol{\\beta}_s,\\boldsymbol{\\gamma}_1,\\ldots,\\boldsymbol{\\gamma}_r$ 是 $W_1+W_2$ 的一组基。<br>张成：任意 $\\mathbf{w}_1+\\mathbf{w}_2\\in W_1+W_2$，$\\mathbf{w}_1$ 可由 $\\alpha,\\beta$ 表示，$\\mathbf{w}_2$ 可由 $\\alpha,\\gamma$ 表示，故和可由 $\\alpha,\\beta,\\gamma$ 表示。<br>线性无关：设 $\\sum a_i\\boldsymbol{\\alpha}_i+\\sum b_j\\boldsymbol{\\beta}_j+\\sum c_k\\boldsymbol{\\gamma}_k=0$。则 $\\sum c_k\\boldsymbol{\\gamma}_k=-\\sum a_i\\boldsymbol{\\alpha}_i-\\sum b_j\\boldsymbol{\\beta}_j\\in W_1$，又 $\\sum c_k\\boldsymbol{\\gamma}_k\\in W_2$，故其属于 $W_1\\cap W_2$，可由 $\\boldsymbol{\\alpha}$ 表示。但 $\\boldsymbol{\\alpha},\\boldsymbol{\\gamma}$ 是 $W_2$ 的基，故 $c_k=0$ 且 $a_i=0$。代回得 $\\sum b_j\\boldsymbol{\\beta}_j=0$，由 $\\boldsymbol{\\beta}$ 线性无关得 $b_j=0$。<br>故 $\\dim(W_1+W_2)=t+s+r=(t+s)+(t+r)-t=\\dim W_1+\\dim W_2-\\dim(W_1\\cap W_2)$。"))
)},
{"id":"c1s5-2","name":"直和及其判定","tags":["def","thm","der"],"brief":"W1∩W2={0} 等价于维数可加。",
 "body": wrap(
    defn("直和", p("设 $W_1,W_2$ 是 $V$ 的子空间。若 $W_1+W_2$ 中每个向量的分解式 $\\mathbf{w}=\\mathbf{w}_1+\\mathbf{w}_2$（$\\mathbf{w}_i\\in W_i$）唯一，则称 $W_1+W_2$ 为直和，记作 $W_1\\oplus W_2$。"))
    + thm("直和的等价条件", p("对 $V$ 的子空间 $W_1,W_2$，以下等价：(1) $W_1+W_2$ 是直和；(2) $W_1\\cap W_2=\\{0\\}$；(3) $\\dim(W_1+W_2)=\\dim W_1+\\dim W_2$；(4) 若 $\\mathbf{w}_1+\\mathbf{w}_2=0$（$\\mathbf{w}_i\\in W_i$），则 $\\mathbf{w}_1=\\mathbf{w}_2=0$。"))
    + der(p("<strong>(1)⇒(2)：</strong>设 $\\mathbf{v}\\in W_1\\cap W_2$，则 $\\mathbf{v}$ 有两种分解：$\\mathbf{v}=\\mathbf{v}+0=0+\\mathbf{v}$。由分解唯一性，$\\mathbf{v}=0$。<br><strong>(2)⇒(1)：</strong>设 $\\mathbf{w}=\\mathbf{w}_1+\\mathbf{w}_2=\\mathbf{w}_1'+\\mathbf{w}_2'$，则 $\\mathbf{w}_1-\\mathbf{w}_1'=\\mathbf{w}_2'-\\mathbf{w}_2\\in W_1\\cap W_2=\\{0\\}$，故 $\\mathbf{w}_1=\\mathbf{w}_1'$，$\\mathbf{w}_2=\\mathbf{w}_2'$。<br><strong>(2)⇔(3)：</strong>由维数公式，$\\dim(W_1+W_2)=\\dim W_1+\\dim W_2-\\dim(W_1\\cap W_2)$。故 $\\dim(W_1+W_2)=\\dim W_1+\\dim W_2$ $\\Leftrightarrow$ $\\dim(W_1\\cap W_2)=0$ $\\Leftrightarrow$ $W_1\\cap W_2=\\{0\\}$。"))
)},
{"id":"c1s5-3","name":"商空间","tags":["def","thm","der"],"brief":"V/W 的维数 = dimV - dimW。",
 "body": wrap(
    defn("商空间", p("设 $W$ 是 $V$ 的子空间。定义等价关系 $\\mathbf{u}\\sim\\mathbf{v}\\Leftrightarrow\\mathbf{u}-\\mathbf{v}\\in W$。$\\mathbf{v}$ 所在的等价类记作 $\\overline{\\mathbf{v}}=\\mathbf{v}+W$，称为 $\\mathbf{v}$ 模 $W$ 的陪集。所有陪集构成的集合 $V/W=\\{\\mathbf{v}+W:\\mathbf{v}\\in V\\}$ 在运算 $(\\mathbf{u}+W)+(\\mathbf{v}+W)=(\\mathbf{u}+\\mathbf{v})+W$，$c(\\mathbf{v}+W)=c\\mathbf{v}+W$ 下构成向量空间，称为 $V$ 关于 $W$ 的商空间。"))
    + thm("商空间的维数", p("若 $V$ 有限维，$W$ 是 $V$ 的子空间，则 $\\dim(V/W)=\\dim V-\\dim W$。"))
    + der(p("<strong>证明：</strong>设 $\\dim W=k$，取 $W$ 的一组基 $\\mathbf{w}_1,\\ldots,\\mathbf{w}_k$，扩充为 $V$ 的基 $\\mathbf{w}_1,\\ldots,\\mathbf{w}_k,\\mathbf{v}_1,\\ldots,\\mathbf{v}_m$（故 $\\dim V=k+m$）。<br><strong>断言：</strong>$\\overline{\\mathbf{v}}_1,\\ldots,\\overline{\\mathbf{v}}_m$ 是 $V/W$ 的一组基。<br>张成：任意 $\\overline{\\mathbf{v}}\\in V/W$，设 $\\mathbf{v}=\\sum a_i\\mathbf{w}_i+\\sum b_j\\mathbf{v}_j$。则 $\\overline{\\mathbf{v}}=\\sum b_j\\overline{\\mathbf{v}}_j$（因 $\\sum a_i\\mathbf{w}_i\\in W$，其陪集为零陪集）。<br>线性无关：设 $\\sum b_j\\overline{\\mathbf{v}}_j=\\overline{0}$，即 $\\sum b_j\\mathbf{v}_j\\in W$。则 $\\sum b_j\\mathbf{v}_j=\\sum a_i\\mathbf{w}_i$，即 $\\sum b_j\\mathbf{v}_j-\\sum a_i\\mathbf{w}_i=0$。由 $\\mathbf{w},\\mathbf{v}$ 线性无关，所有 $b_j=0$。<br>故 $\\dim(V/W)=m=\\dim V-\\dim W$。"))
)}
]},
]

# =====================================================
#  CHAPTER 2: 矩阵
# =====================================================
ch2_sections = [
# ---- 2.1 矩阵的基本运算 ----
{
"name": "2.1 矩阵的基本运算",
"color": "#0d9488",
"desc": "矩阵的定义、加法、数乘、乘法与转置",
"items": [
{"id":"c2s1-1","name":"矩阵的定义与线性运算","tags":["def","note"],"brief":"按行乘列定义的乘法不满足交换律。",
 "body": wrap(
    defn("矩阵与线性运算", p("数域 $\\mathbb{F}$ 上的 $m\\times n$ 矩阵 $A=(a_{ij})$ 是 $m$ 行 $n$ 列的矩形数表。矩阵加法：$(A+B)_{ij}=a_{ij}+b_{ij}$（同型矩阵）；数乘：$(cA)_{ij}=c\\cdot a_{ij}$。所有 $m\\times n$ 矩阵构成向量空间 $M_{m\\times n}$，维数为 $mn$。"))
    + defn("矩阵乘法", p("设 $A$ 为 $m\\times n$，$B$ 为 $n\\times p$，则 $AB$ 为 $m\\times p$ 矩阵，$(AB)_{ij}=\\sum_{k=1}^n a_{ik}b_{kj}$，即 $A$ 的第 $i$ 行与 $B$ 的第 $j$ 列对应元素相乘求和。"))
    + note(p("矩阵乘法一般不满足交换律（$AB\\neq BA$），但满足结合律 $(AB)C=A(BC)$ 和分配律 $A(B+C)=AB+AC$。乘法有零因子：$AB=0$ 不能推出 $A=0$ 或 $B=0$。"))
)},
{"id":"c2s1-2","name":"转置与特殊矩阵","tags":["def","thm","der"],"brief":"对称矩阵、反对称矩阵的性质。",
 "body": wrap(
    defn("转置", p("矩阵 $A=(a_{ij})$ 的转置 $A^T$ 是将 $A$ 的行和列互换得到的矩阵，$(A^T)_{ij}=a_{ji}$。性质：$(A^T)^T=A$，$(A+B)^T=A^T+B^T$，$(cA)^T=cA^T$，$(AB)^T=B^TA^T$。"))
    + defn("对称与反对称", p("若 $A^T=A$，称 $A$ 为对称矩阵；若 $A^T=-A$，称 $A$ 为反对称矩阵。反对称矩阵的对角元必为零。"))
    + thm("方阵的对称-反对称分解", p("任意方阵 $A$ 可唯一分解为对称矩阵与反对称矩阵之和：$A=\\frac{A+A^T}{2}+\\frac{A-A^T}{2}$。"))
    + der(p("<strong>证明：</strong>设 $S=\\frac{A+A^T}{2}$，$K=\\frac{A-A^T}{2}$。则 $S^T=\\frac{A^T+A}{2}=S$（对称），$K^T=\\frac{A^T-A}{2}=-K$（反对称），且 $S+K=A$。唯一性：若 $A=S_1+K_1=S_2+K_2$，则 $S_1-S_2=K_2-K_1$。左边对称，右边反对称，既对称又反对称的矩阵只能是零矩阵，故 $S_1=S_2$，$K_1=K_2$。"))
)},
]},
# ---- 2.2 逆矩阵 ----
{
"name": "2.2 逆矩阵",
"color": "#059669",
"desc": "逆矩阵的定义、存在条件与计算",
"items": [
{"id":"c2s2-1","name":"逆矩阵的定义与性质","tags":["def","thm"],"brief":"可逆矩阵的乘积与转置仍可逆。",
 "body": wrap(
    defn("逆矩阵", p("设 $A$ 为 $n$ 阶方阵。若存在 $n$ 阶方阵 $B$ 使得 $AB=BA=I_n$，则称 $A$ 可逆（非奇异），$B$ 称为 $A$ 的逆矩阵，记作 $A^{-1}$。逆矩阵若存在则唯一。"))
    + thm("逆矩阵的性质", p("(1) $(A^{-1})^{-1}=A$；(2) $(AB)^{-1}=B^{-1}A^{-1}$；(3) $(A^T)^{-1}=(A^{-1})^T$；(4) $(cA)^{-1}=c^{-1}A^{-1}$（$c\\neq 0$）。"))
)},
{"id":"c2s2-2","name":"可逆的等价条件","tags":["thm","der"],"brief":"行列式非零等价于可逆。",
 "body": wrap(
    thm("可逆矩阵的等价刻画", p("对 $n$ 阶方阵 $A$，以下等价：(1) $A$ 可逆；(2) $\\det A\\neq 0$；(3) $A$ 的列向量线性无关；(4) $A$ 的行向量线性无关；(5) $\\mathrm{rank}(A)=n$；(6) 齐次方程 $A\\mathbf{x}=0$ 只有零解；(7) 对任意 $\\mathbf{b}$，$A\\mathbf{x}=\\mathbf{b}$ 有唯一解。"))
    + der(p("<strong>(1)⇒(2)：</strong>若 $A$ 可逆，则 $AA^{-1}=I$，两边取行列式：$\\det A\\cdot\\det(A^{-1})=\\det I=1$，故 $\\det A\\neq 0$。<br><strong>(2)⇒(1)：</strong>若 $\\det A\\neq 0$，构造 $A^{-1}=\\frac{1}{\\det A}\\mathrm{adj}(A)$，其中 $\\mathrm{adj}(A)$ 是伴随矩阵。由行列式展开定理，$A\\cdot\\mathrm{adj}(A)=\\mathrm{adj}(A)\\cdot A=(\\det A)I$，故 $A\\cdot\\frac{1}{\\det A}\\mathrm{adj}(A)=I$，即 $A$ 可逆。其余等价性由秩的定义和线性方程组理论可得。"))
)},
{"id":"c2s2-3","name":"初等变换与初等矩阵","tags":["def","thm","der","app"],"brief":"行初等变换对应左乘初等矩阵。",
 "body": wrap(
    defn("初等变换与初等矩阵", p("三种初等行变换：(1) 交换两行 $r_i\\leftrightarrow r_j$；(2) 某行乘非零数 $c$：$r_i\\leftarrow c r_i$；(3) 某行的倍数加到另一行：$r_i\\leftarrow r_i+kr_j$。对单位矩阵 $I$ 做一次初等变换得到的矩阵称为初等矩阵。"))
    + thm("初等变换与矩阵乘法", p("对矩阵 $A$ 做一次初等行变换等价于左乘相应的初等矩阵；做一次初等列变换等价于右乘相应的初等矩阵。初等矩阵均可逆，其逆仍是同类初等矩阵。"))
    + der(p("<strong>用初等变换求逆的正确性证明：</strong>设对 $[A|I]$ 做了一系列行变换，对应左乘初等矩阵 $P_1,P_2,\\ldots,P_k$。令 $P=P_kP_{k-1}\\cdots P_1$，则整个增广矩阵变为 $P[A|I]=[PA|P]$。若左侧 $PA=I$，则 $P=A^{-1}$（因 $A$ 可逆时，$P$ 是 $A$ 的左逆，而方阵左逆等于右逆）。此时右侧恰为 $P=A^{-1}$。故 $[A|I]\\to[I|A^{-1}]$。"))
    + app(p("<strong>用初等变换求逆：</strong>构造增广矩阵 $[A|I]$，对其做行初等变换将 $A$ 化为 $I$，则右侧 $I$ 同时化为 $A^{-1}$，即 $[A|I]\\xrightarrow{\\text{行变换}}[I|A^{-1}]$。原理：一系列初等矩阵 $P_1,\\ldots,P_k$ 满足 $P_k\\cdots P_1 A=I$，故 $A^{-1}=P_k\\cdots P_1$。"))
)}
]},
# ---- 2.3 矩阵的秩 ----
{
"name": "2.3 矩阵的秩",
"color": "#0891b2",
"desc": "秩的定义、性质与计算",
"items": [
{"id":"c2s3-1","name":"秩的定义","tags":["def","thm"],"brief":"行秩=列秩=非零子式最高阶数。",
 "body": wrap(
    defn("矩阵的秩", p("矩阵 $A$ 的<strong>行秩</strong>是其行向量组的极大线性无关组所含向量个数；<strong>列秩</strong>是列向量组的极大线性无关组所含向量个数。可以证明行秩=列秩，这个公共值称为 $A$ 的秩，记作 $\\mathrm{rank}(A)$ 或 $r(A)$。"))
    + thm("秩的子式刻画", p("$\\mathrm{rank}(A)=r$ 当且仅当 $A$ 存在一个 $r$ 阶非零子式，且所有 $r+1$ 阶子式（若存在）全为零。"))
)},
{"id":"c2s3-2","name":"秩的性质","tags":["thm","der","note"],"brief":"乘积的秩不超过各因子的秩。",
 "body": wrap(
    thm("秩的基本性质", p("(1) $0\\le\\mathrm{rank}(A)\\le\\min(m,n)$；(2) $\\mathrm{rank}(A)=\\mathrm{rank}(A^T)$；(3) $\\mathrm{rank}(kA)=\\mathrm{rank}(A)$（$k\\neq 0$）；(4) $\\mathrm{rank}(A+B)\\le\\mathrm{rank}(A)+\\mathrm{rank}(B)$；(5) $\\mathrm{rank}(AB)\\le\\min(\\mathrm{rank}(A),\\mathrm{rank}(B))$；(6) 若 $P,Q$ 可逆，则 $\\mathrm{rank}(PAQ)=\\mathrm{rank}(A)$。"))
    + der(p("<strong>(5) 的证明：</strong>设 $A$ 为 $m\\times n$，$B$ 为 $n\\times p$。$AB$ 的每一列是 $A$ 的列向量的线性组合（系数为 $B$ 的对应列），故 $AB$ 的列空间 $\\subseteq A$ 的列空间，从而 $\\mathrm{rank}(AB)\\le\\mathrm{rank}(A)$。同理，$AB$ 的每一行是 $B$ 的行向量的线性组合，故 $\\mathrm{rank}(AB)\\le\\mathrm{rank}(B)$。综上 $\\mathrm{rank}(AB)\\le\\min(r(A),r(B))$。"))
)}
]},
# ---- 2.4 分块矩阵 ----
{
"name": "2.4 分块矩阵",
"color": "#0d9488",
"desc": "分块矩阵的运算、分块对角矩阵的行列式与逆",
"items": [
{"id":"c2s4-1","name":"分块矩阵的运算","tags":["def","thm"],"brief":"将矩阵分块后按块运算，规则与普通元素相同。",
 "body": wrap(
    defn("分块矩阵", p("将矩阵 $A$ 用若干横线和纵线分成若干小块，每块是一个小矩阵，称为子矩阵。以子矩阵为元素的形式矩阵称为分块矩阵。分块的目的是简化运算和揭示结构。"))
    + thm("分块矩阵的运算规则", p("(1) 加法：同型矩阵按相同方式分块后，对应块相加；(2) 数乘：每块乘以该数；(3) 乘法：$A$ 的列分块方式与 $B$ 的行分块方式一致时，$(AB)_{ij}=\\sum_k A_{ik}B_{kj}$；(4) 转置：$(A^T)_{ij}=(A_{ji})^T$。"))
)},
{"id":"c2s4-2","name":"分块对角矩阵的行列式与逆","tags":["thm","der"],"brief":"分块对角矩阵的行列式等于各块行列式之积。",
 "body": wrap(
    defn("分块对角矩阵", p("形如 $A=\\mathrm{diag}(A_1,A_2,\\ldots,A_s)=\\begin{pmatrix}A_1&&\\\\&A_2&\\\\&&\\ddots\\\\&&&A_s\\end{pmatrix}$ 的分块矩阵称为分块对角矩阵，其中 $A_i$ 为方阵。"))
    + thm("分块对角矩阵的性质", p("(1) $\\det A=\\prod_{i=1}^s\\det A_i$；(2) $A$ 可逆当且仅当每个 $A_i$ 可逆，且 $A^{-1}=\\mathrm{diag}(A_1^{-1},\\ldots,A_s^{-1})$；(3) $A^k=\\mathrm{diag}(A_1^k,\\ldots,A_s^k)$。"))
    + der(p("<strong>(1) 的证明：</strong>对分块数 $s$ 归纳。$s=1$ 显然。设 $s=2$，$A=\\begin{pmatrix}A_1&0\\\\0&A_2\\end{pmatrix}$。由行列式的完全展开定义，非零项必须取自不同行不同列。由于 $A_1$ 占据前 $m$ 行前 $m$ 列，$A_2$ 占据后 $n$ 行后 $n$ 列，交叉块为零，故非零项只能分别从 $A_1$ 和 $A_2$ 中选取。设 $A_1$ 的展开项符号为 $(-1)^{\\tau}$，$A_2$ 的为 $(-1)^{\\sigma}$，合并后符号为 $(-1)^{\\tau+\\sigma}$（因 $A_2$ 的列编号整体后移 $m$，逆序数增加量为偶数，不改变符号）。故 $\\det A=\\det A_1\\cdot\\det A_2$。一般情形由归纳即得。<br><strong>(2) 的证明：</strong>直接验证 $\\mathrm{diag}(A_1^{-1},\\ldots)\\cdot\\mathrm{diag}(A_1,\\ldots)=I$。"))
)}
]},
# ---- 2.5 矩阵的迹与特殊矩阵 ----
{
"name": "2.5 矩阵的迹与特殊矩阵",
"color": "#059669",
"desc": "矩阵的迹、正交矩阵、幂等矩阵与幂零矩阵",
"items": [
{"id":"c2s5-1","name":"矩阵的迹","tags":["def","thm","der"],"brief":"迹是对角元之和，满足 tr(AB)=tr(BA)。",
 "body": wrap(
    defn("迹", p("$n$ 阶方阵 $A=(a_{ij})$ 的迹定义为其主对角线元素之和：$\\mathrm{tr}(A)=\\sum_{i=1}^n a_{ii}$。"))
    + thm("迹的性质", p("(1) $\\mathrm{tr}(A+B)=\\mathrm{tr}(A)+\\mathrm{tr}(B)$；(2) $\\mathrm{tr}(cA)=c\\,\\mathrm{tr}(A)$；(3) $\\mathrm{tr}(A^T)=\\mathrm{tr}(A)$；(4) $\\mathrm{tr}(AB)=\\mathrm{tr}(BA)$（即使 $AB\\neq BA$）；(5) $\\mathrm{tr}(A)=\\sum_{i=1}^n\\lambda_i$（特征值之和）。"))
    + der(p("<strong>(4) 的证明：</strong>设 $A=(a_{ij})$ 为 $m\\times n$，$B=(b_{ij})$ 为 $n\\times m$。$\\mathrm{tr}(AB)=\\sum_{i=1}^m(AB)_{ii}=\\sum_{i=1}^m\\sum_{k=1}^n a_{ik}b_{ki}$。交换求和顺序：$=\\sum_{k=1}^n\\sum_{i=1}^m b_{ki}a_{ik}=\\sum_{k=1}^n(BA)_{kk}=\\mathrm{tr}(BA)$。"))
)},
{"id":"c2s5-2","name":"正交矩阵","tags":["def","thm","der"],"brief":"列向量构成标准正交基的实方阵。",
 "body": wrap(
    defn("正交矩阵", p("$n$ 阶实方阵 $Q$ 称为正交矩阵，若 $Q^TQ=QQ^T=I$，即 $Q^{-1}=Q^T$。"))
    + thm("正交矩阵的性质", p("(1) $\\det Q=\\pm 1$；(2) $Q$ 的列（行）向量构成 $\\mathbb{R}^n$ 的标准正交基；(3) 正交变换保持内积与长度：$\\langle Q\\mathbf{x},Q\\mathbf{y}\\rangle=\\langle\\mathbf{x},\\mathbf{y}\\rangle$；(4) 正交矩阵的特征值模为 1；(5) 正交矩阵的乘积与逆仍为正交矩阵。"))
    + der(p("<strong>(2) 的证明：</strong>设 $Q=(\\mathbf{q}_1,\\ldots,\\mathbf{q}_n)$（列分块）。$Q^TQ$ 的 $(i,j)$ 元为 $\\mathbf{q}_i^T\\mathbf{q}_j=\\langle\\mathbf{q}_i,\\mathbf{q}_j\\rangle$。$Q^TQ=I$ 意味着 $\\langle\\mathbf{q}_i,\\mathbf{q}_j\\rangle=\\delta_{ij}$，即列向量标准正交。同理 $QQ^T=I$ 意味着行向量标准正交。<br><strong>(3) 的证明：</strong>$\\langle Q\\mathbf{x},Q\\mathbf{y}\\rangle=(Q\\mathbf{x})^T(Q\\mathbf{y})=\\mathbf{x}^TQ^TQ\\mathbf{y}=\\mathbf{x}^TI\\mathbf{y}=\\mathbf{x}^T\\mathbf{y}=\\langle\\mathbf{x},\\mathbf{y}\\rangle$。"))
)},
{"id":"c2s5-3","name":"幂等矩阵与幂零矩阵","tags":["def","thm","der"],"brief":"A²=A 的幂等矩阵特征值为 0 或 1。",
 "body": wrap(
    defn("幂等与幂零", p("若 $A^2=A$，称 $A$ 为幂等矩阵；若存在正整数 $k$ 使 $A^k=0$，称 $A$ 为幂零矩阵，满足 $A^k=0$ 的最小 $k$ 称为幂零指数。"))
    + thm("幂等矩阵的性质", p("(1) 幂等矩阵的特征值只能是 0 或 1；(2) 幂等矩阵可对角化，且 $\\mathrm{rank}(A)=\\mathrm{tr}(A)$；(3) $I-A$ 也是幂等矩阵。"))
    + der(p("<strong>(1) 的证明：</strong>设 $\\lambda$ 是 $A$ 的特征值，$\\mathbf{v}$ 为对应特征向量。$A^2\\mathbf{v}=A(A\\mathbf{v})=A(\\lambda\\mathbf{v})=\\lambda A\\mathbf{v}=\\lambda^2\\mathbf{v}$。又 $A^2=A$，故 $A^2\\mathbf{v}=A\\mathbf{v}=\\lambda\\mathbf{v}$。因此 $\\lambda^2\\mathbf{v}=\\lambda\\mathbf{v}$，因 $\\mathbf{v}\\neq 0$，$\\lambda^2=\\lambda$，即 $\\lambda=0$ 或 $1$。<br><strong>(2) 的证明：</strong>幂等矩阵的极小多项式为 $x(x-1)$（无重根），故可对角化。对角形中 1 的个数即秩，而迹等于特征值之和即 1 的个数，故 $\\mathrm{rank}(A)=\\mathrm{tr}(A)$。"))
)}
]},
]

# =====================================================
#  CHAPTER 3: 行列式
# =====================================================
ch3_sections = [
# ---- 3.1 行列式的定义 ----
{
"name": "3.1 行列式的定义",
"color": "#059669",
"desc": "排列、逆序数与 n 阶行列式的完全展开",
"items": [
{"id":"c3s1-1","name":"排列与逆序数","tags":["def","thm"],"brief":"行列式定义的组合基础。",
 "body": wrap(
    defn("排列与逆序数", p("$1,2,\\ldots,n$ 的一个全排列 $p_1p_2\\cdots p_n$ 称为 $n$ 级排列。排列中若 $p_i>p_j$ 但 $i<j$，称 $(p_i,p_j)$ 为一个逆序。排列中逆序的总数称为逆序数，记作 $\\tau(p_1p_2\\cdots p_n)$。逆序数为偶（奇）数的排列称为偶（奇）排列。"))
    + thm("对换改变排列奇偶性", p("任意排列经过一次对换（交换两个元素），其奇偶性改变。"))
)},
{"id":"c3s1-2","name":"n 阶行列式的定义","tags":["def","note"],"brief":"所有取自不同行不同列元素乘积的代数和。",
 "fig":"det","figCap":"2阶行列式 = 平行四边形有向面积",
 "body": wrap(
    defn("n 阶行列式", p("$n$ 阶方阵 $A=(a_{ij})$ 的行列式定义为：$\\det A=\\sum_{p_1p_2\\cdots p_n}(-1)^{\\tau(p_1p_2\\cdots p_n)}a_{1p_1}a_{2p_2}\\cdots a_{np_n}$，其中求和遍历所有 $n$ 级排列。共有 $n!$ 项。"))
    + note(p("二阶：$\\begin{vmatrix}a&b\\\\c&d\\end{vmatrix}=ad-bc$。三阶可用对角线法则（仅适用于三阶）。$n\\ge 4$ 时对角线法则失效，须用定义或展开定理。几何意义：$\\det A$ 是 $A$ 的列（行）向量张成的平行多面体的有向体积。"))
)}
]},
# ---- 3.2 行列式的性质与展开 ----
{
"name": "3.2 行列式的性质与展开",
"color": "#0891b2",
"desc": "行列式的基本性质、按行按列展开定理",
"items": [
{"id":"c3s2-1","name":"行列式的性质","tags":["thm","der"],"brief":"行列互换不变，换行变号。",
 "body": wrap(
    thm("行列式的基本性质", p("(1) $\\det A^T=\\det A$；(2) 交换两行（列），行列式变号；(3) 某行（列）有公因子 $k$，可提出 $k$；(4) 两行（列）相同，行列式为 0；(5) 两行（列）成比例，行列式为 0；(6) 某行（列）的倍数加到另一行（列），行列式不变；(7) 行列式对行（列）具有可加性。"))
    + der(p("<strong>(6) 的证明：</strong>设将第 $j$ 行的 $k$ 倍加到第 $i$ 行。由性质 (7)（可加性），新行列式 $=\\det A + k\\cdot\\det A'$，其中 $A'$ 是将 $A$ 的第 $i$ 行替换为第 $j$ 行得到的矩阵。$A'$ 有两行相同，由性质 (4)，$\\det A'=0$。故新行列式 $=\\det A$。"))
)},
{"id":"c3s2-2","name":"按行（列）展开定理","tags":["thm","der"],"brief":"降阶计算行列式的核心工具。",
 "body": wrap(
    defn("余子式与代数余子式", p("在 $n$ 阶行列式 $D=\\det A$ 中，划去元素 $a_{ij}$ 所在的第 $i$ 行和第 $j$ 列，剩余元素构成的 $n-1$ 阶行列式称为 $a_{ij}$ 的余子式，记作 $M_{ij}$。$A_{ij}=(-1)^{i+j}M_{ij}$ 称为 $a_{ij}$ 的代数余子式。"))
    + thm("行列式展开定理", p("行列式等于它的任一行（列）的各元素与其代数余子式乘积之和：$D=\\sum_{j=1}^n a_{ij}A_{ij}$（按第 $i$ 行展开），$D=\\sum_{i=1}^n a_{ij}A_{ij}$（按第 $j$ 列展开）。"))
    + der(p("<strong>证明思路：</strong>先证 $D=\\sum_j a_{1j}A_{1j}$（按第一行展开）。将定义中的 $n!$ 项按 $p_1=j$ 分组，每组含 $(n-1)!$ 项。对固定的 $j$，含 $a_{1j}$ 的项为 $a_{1j}\\sum_{p_2\\cdots p_n}(-1)^{\\tau(jp_2\\cdots p_n)}a_{2p_2}\\cdots a_{np_n}$。$\\tau(jp_2\\cdots p_n)=j-1+\\tau(p_2\\cdots p_n)$（其中 $p_2,\\ldots,p_n$ 是 $\\{1,\\ldots,n\\}\\setminus\\{j\\}$ 的排列，其逆序数需重新编号为 $1,\\ldots,n-1$ 的排列），整理后符号为 $(-1)^{1+j}$，系数恰为 $M_{1j}$，故该项 $=a_{1j}(-1)^{1+j}M_{1j}=a_{1j}A_{1j}$。对 $j$ 求和即得。一般行的展开通过交换行转化为第一行情形。"))
    + thm("异乘变零定理", p("某行元素与另一行对应元素的代数余子式乘积之和为零：$\\sum_{j=1}^n a_{ij}A_{kj}=0$（$i\\neq k$）。"))
)}
]},
# ---- 3.3 行列式的计算与应用 ----
{
"name": "3.3 行列式的计算与应用",
"color": "#be185d",
"desc": "行列式计算技巧、伴随矩阵与克拉默法则",
"items": [
{"id":"c3s3-1","name":"行列式的计算","tags":["exa","der","note"],"brief":"化三角形、递推法、范德蒙德行列式。",
 "body": wrap(
    exa(p("<strong>化三角形法：</strong>利用行变换将行列式化为上（下）三角形，其值等于对角线元素之积。"))
    + thm("范德蒙德行列式", p("$V_n=\\begin{vmatrix}1&1&\\cdots&1\\\\x_1&x_2&\\cdots&x_n\\\\x_1^2&x_2^2&\\cdots&x_n^2\\\\\\vdots&\\vdots&&\\vdots\\\\x_1^{n-1}&x_2^{n-1}&\\cdots&x_n^{n-1}\\end{vmatrix}=\\prod_{1\\le i<j\\le n}(x_j-x_i)$。"))
    + der(p("<strong>证明（数学归纳法）：</strong>$n=2$ 时，$V_2=\\begin{vmatrix}1&1\\\\x_1&x_2\\end{vmatrix}=x_2-x_1=\\prod_{1\\le i<j\\le 2}(x_j-x_i)$，成立。<br>假设 $n-1$ 阶成立。对 $n$ 阶，从第 $n$ 行起依次用上一行的 $-x_1$ 倍加到下一行（$r_k\\leftarrow r_k-x_1 r_{k-1}$，$k=n,n-1,\\ldots,2$），第一列除 $a_{11}=1$ 外全为 0。按第一列展开得 $V_n=\\begin{vmatrix}x_2-x_1&x_3-x_1&\\cdots&x_n-x_1\\\\x_2(x_2-x_1)&x_3(x_3-x_1)&\\cdots&x_n(x_n-x_1)\\\\\\vdots&\\vdots&&\\vdots\\\\x_2^{n-2}(x_2-x_1)&x_3^{n-2}(x_3-x_1)&\\cdots&x_n^{n-2}(x_n-x_1)\\end{vmatrix}$。各列提出公因子 $x_j-x_1$（$j=2,\\ldots,n$），得 $V_n=\\prod_{j=2}^n(x_j-x_1)\\cdot V_{n-1}(x_2,\\ldots,x_n)$。由归纳假设 $V_{n-1}=\\prod_{2\\le i<j\\le n}(x_j-x_i)$，故 $V_n=\\prod_{j=2}^n(x_j-x_1)\\cdot\\prod_{2\\le i<j\\le n}(x_j-x_i)=\\prod_{1\\le i<j\\le n}(x_j-x_i)$。"))
    + note(p("范德蒙德行列式非零当且仅当 $x_1,x_2,\\ldots,x_n$ 互不相同。这一事实在多项式插值、特征值互不相同的矩阵对角化中有关键应用。"))
)},
{"id":"c3s3-2","name":"伴随矩阵与克拉默法则","tags":["def","thm","der","app"],"brief":"用行列式表示逆矩阵与方程组的解。",
 "body": wrap(
    defn("伴随矩阵", p("方阵 $A$ 的伴随矩阵 $\\mathrm{adj}(A)$ 是由 $A$ 的各元素代数余子式转置构成的矩阵：$(\\mathrm{adj}(A))_{ij}=A_{ji}$。"))
    + thm("伴随矩阵基本恒等式", p("$A\\cdot\\mathrm{adj}(A)=\\mathrm{adj}(A)\\cdot A=(\\det A)\\cdot I$。"))
    + der(p("<strong>证明：</strong>$(A\\cdot\\mathrm{adj}(A))_{ik}=\\sum_j a_{ij}(\\mathrm{adj}(A))_{jk}=\\sum_j a_{ij}A_{kj}$。当 $i=k$ 时，由展开定理得 $\\det A$；当 $i\\neq k$ 时，由异乘变零定理得 $0$。故 $A\\cdot\\mathrm{adj}(A)=(\\det A)I$。另一边类似。"))
    + thm("克拉默法则", p("若 $n$ 阶线性方程组 $A\\mathbf{x}=\\mathbf{b}$ 的系数行列式 $D=\\det A\\neq 0$，则方程组有唯一解 $x_i=\\frac{D_i}{D}$，其中 $D_i$ 是将 $D$ 的第 $i$ 列替换为 $\\mathbf{b}$ 后得到的行列式。"))
    + der(p("<strong>证明：</strong>由 $D\\neq 0$，$A$ 可逆，解唯一为 $\\mathbf{x}=A^{-1}\\mathbf{b}=\\frac{1}{D}\\mathrm{adj}(A)\\mathbf{b}$。$x_i=\\frac{1}{D}\\sum_j A_{ji}b_j=\\frac{1}{D}D_i$，其中 $D_i=\\sum_j b_j A_{ji}$ 正是将 $D$ 第 $i$ 列换为 $\\mathbf{b}$ 后按第 $i$ 列展开的结果。"))
)}
]},
# ---- 3.4 拉普拉斯展开与行列式的应用 ----
{
"name": "3.4 拉普拉斯展开与行列式的应用",
"color": "#dc2626",
"desc": "拉普拉斯展开定理、行列式的几何意义与乘法定理",
"items": [
{"id":"c3s4-1","name":"拉普拉斯展开定理","tags":["thm","der"],"brief":"按 k 行（列）展开的推广。",
 "body": wrap(
    defn("k 阶子式与余子式", p("在 $n$ 阶行列式 $D$ 中，任取 $k$ 行 $k$ 列（$1\\le k\\le n$），交点处元素构成的 $k$ 阶行列式称为 $D$ 的一个 $k$ 阶子式，记作 $M$。划去这 $k$ 行 $k$ 列后剩余的 $n-k$ 阶行列式称为 $M$ 的余子式。若 $k$ 行的行标为 $i_1<\\cdots<i_k$，$k$ 列的列标为 $j_1<\\cdots<j_k$，则 $(-1)^{\\sum i_t+\\sum j_t}$ 乘以余子式称为 $M$ 的代数余子式，记作 $A$。"))
    + thm("拉普拉斯展开定理", p("在 $n$ 阶行列式 $D$ 中，任意取定 $k$ 行（列），则 $D$ 等于这 $k$ 行（列）中所有 $k$ 阶子式与其代数余子式乘积之和：$D=\\sum_{i=1}^{C_n^k} M_i A_i$。"))
    + der(p("<strong>证明思路：</strong>按行展开定理是 $k=1$ 的特例。对一般 $k$，将行列式的 $n!$ 项按所取 $k$ 行中元素的位置分组。每组对应一个 $k$ 阶子式 $M$，组内各项可分解为 $M$ 的展开项乘以余子式的展开项，符号由所取行列的位置决定。详细证明需对排列作精细分析，核心是将 $n$ 级排列的逆序数分解为 $k$ 级排列与 $n-k$ 级排列逆序数之和再加交叉项 $\\sum i_t+\\sum j_t$ 的奇偶性。"))
    + note(p("拉普拉斯展开在 $k=1$ 时退化为按行（列）展开。取 $k=n$ 时只有一项 $D$ 本身。它在证明分块矩阵行列式公式（如 $\\det\\begin{pmatrix}A&B\\\\0&D\\end{pmatrix}=\\det A\\cdot\\det D$）时非常有用。"))
)},
{"id":"c3s4-2","name":"行列式的几何意义","tags":["thm","der","app"],"brief":"行列式是平行多面体的有向体积。",
 "body": wrap(
    thm("行列式的几何解释", p("设 $A=(\\mathbf{a}_1,\\ldots,\\mathbf{a}_n)$ 为 $n$ 阶实方阵，$\\mathbf{a}_i$ 为列向量。则 $|\\det A|$ 等于 $\\mathbf{a}_1,\\ldots,\\mathbf{a}_n$ 张成的 $n$ 维平行多面体的体积；$\\det A$ 的符号表示定向（右手系为正，左手系为负）。"))
    + der(p("<strong>二维情形：</strong>$\\mathbf{a}_1=(a,c)^T$，$\\mathbf{a}_2=(b,d)^T$ 张成的平行四边形面积为底 $\\times$ 高 $=\\sqrt{a^2+c^2}\\cdot|d-\\frac{bc}{a}|=|ad-bc|=|\\det A|$。<br><strong>三维情形：</strong>三个向量张成的平行六面体体积 $=|\\mathbf{a}_1\\cdot(\\mathbf{a}_2\\times\\mathbf{a}_3)|=|\\det A|$。<br><strong>一般 $n$ 维：</strong>用归纳法。体积函数满足：对每个向量多重线性、反对称、单位立方体体积为 1。行列式恰是满足这三条性质的唯一函数，故体积 $=|\\det A|$。"))
    + app(p("<strong>应用：</strong>(1) 判断向量组线性无关：$\\mathbf{a}_1,\\ldots,\\mathbf{a}_n$ 线性无关 $\\Leftrightarrow$ 张成体积非零 $\\Leftrightarrow$ $\\det A\\neq 0$；(2) 坐标变换中的体积元：$d\\mathbf{x}=|\\det J|\\,d\\mathbf{u}$，其中 $J$ 是雅可比矩阵；(3) 线性变换的面积/体积缩放因子为 $|\\det A|$。"))
)},
{"id":"c3s4-3","name":"行列式与矩阵可逆性","tags":["thm","app"],"brief":"det A≠0 是方阵可逆与方程组唯一解的充要条件。",
 "body": wrap(
    thm("行列式的核心应用", p("对 $n$ 阶方阵 $A$，以下等价：(1) $\\det A\\neq 0$；(2) $A$ 可逆；(3) $A$ 的列（行）向量线性无关；(4) 齐次方程组 $A\\mathbf{x}=0$ 只有零解；(5) 对任意 $\\mathbf{b}$，$A\\mathbf{x}=\\mathbf{b}$ 有唯一解。"))
    + der(p("<strong>证明链：</strong>(1)⇔(2) 由伴随矩阵法：$A^{-1}=\\frac{1}{\\det A}\\mathrm{adj}(A)$ 存在当且仅当 $\\det A\\neq 0$。(2)⇔(3) $A$ 可逆 $\\Leftrightarrow$ 列满秩 $\\Leftrightarrow$ 列向量线性无关。(2)⇒(5) 若 $A$ 可逆，则 $\\mathbf{x}=A^{-1}\\mathbf{b}$ 是唯一解。(5)⇒(4) 取 $\\mathbf{b}=0$ 得唯一解 $\\mathbf{x}=0$。(4)⇒(3) $A\\mathbf{x}=0$ 只有零解意味着列向量线性无关。(3)⇒(1) 列向量线性无关 $\\Leftrightarrow$ $\\mathrm{rank}(A)=n$ $\\Leftrightarrow$ $\\det A\\neq 0$。"))
)},
{"id":"c3s4-4","name":"行列式的乘法定理","tags":["thm","der"],"brief":"det(AB)=det A·det B。",
 "body": wrap(
    thm("行列式乘法定理", p("设 $A,B$ 为 $n$ 阶方阵，则 $\\det(AB)=\\det A\\cdot\\det B$。"))
    + der(p("<strong>证明（初等矩阵法）：</strong>先证对初等矩阵 $E$，$\\det(EA)=\\det E\\cdot\\det A$。<br>(1) 若 $E$ 为交换两行型，则 $\\det E=-1$，$\\det(EA)=-\\det A=\\det E\\cdot\\det A$。<br>(2) 若 $E$ 为某行乘 $c$ 型，则 $\\det E=c$，$\\det(EA)=c\\det A=\\det E\\cdot\\det A$。<br>(3) 若 $E$ 为某行倍加型，则 $\\det E=1$，$\\det(EA)=\\det A=\\det E\\cdot\\det A$。<br>现对一般 $A$：若 $A$ 不可逆，则 $\\det A=0$，且 $AB$ 也不可逆（因 $\\mathrm{rank}(AB)\\le\\mathrm{rank}(A)<n$），故 $\\det(AB)=0=\\det A\\cdot\\det B$。<br>若 $A$ 可逆，则 $A$ 可表为初等矩阵之积 $A=E_1\\cdots E_k$。于是 $\\det(AB)=\\det(E_1\\cdots E_k B)=\\det E_1\\cdots\\det E_k\\cdot\\det B=\\det(E_1\\cdots E_k)\\cdot\\det B=\\det A\\cdot\\det B$。"))
)}
]},
]

# =====================================================
#  CHAPTER 4: 线性方程组
# =====================================================
ch4_sections = [
# ---- 4.1 齐次线性方程组 ----
{
"name": "4.1 齐次线性方程组",
"color": "#0891b2",
"desc": "解的结构、基础解系与零空间",
"items": [
{"id":"c4s1-1","name":"齐次方程组的解空间","tags":["def","thm","der"],"brief":"解集构成子空间（零空间）。",
 "body": wrap(
    defn("齐次线性方程组", p("$A\\mathbf{x}=\\mathbf{0}$，其中 $A$ 为 $m\\times n$ 矩阵。其解集 $N(A)=\\{\\mathbf{x}\\in\\mathbb{F}^n:A\\mathbf{x}=\\mathbf{0}\\}$ 称为 $A$ 的零空间（核）。"))
    + thm("解空间是子空间", p("$N(A)$ 是 $\\mathbb{F}^n$ 的子空间。"))
    + der(p("<strong>证明：</strong>$\\mathbf{0}\\in N(A)$，故非空。若 $\\mathbf{x}_1,\\mathbf{x}_2\\in N(A)$，$c_1,c_2\\in\\mathbb{F}$，则 $A(c_1\\mathbf{x}_1+c_2\\mathbf{x}_2)=c_1A\\mathbf{x}_1+c_2A\\mathbf{x}_2=c_1\\mathbf{0}+c_2\\mathbf{0}=\\mathbf{0}$，故 $c_1\\mathbf{x}_1+c_2\\mathbf{x}_2\\in N(A)$。因此 $N(A)$ 对线性组合封闭，是子空间。"))
    + thm("秩-零度定理", p("$\\dim N(A)+\\mathrm{rank}(A)=n$，即零空间维数（零度）$=n-\\mathrm{rank}(A)$。"))
    + der(p("<strong>证明：</strong>设 $\\mathrm{rank}(A)=r$，$\\dim N(A)=s$。取 $N(A)$ 的一组基 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_s$，扩充为 $\\mathbb{F}^n$ 的基 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_s,\\mathbf{v}_{s+1},\\ldots,\\mathbf{v}_n$。<br><strong>断言：</strong>$A\\mathbf{v}_{s+1},\\ldots,A\\mathbf{v}_n$ 是列空间 $C(A)$ 的一组基。<br>(1) 张成：$C(A)$ 中任意向量 $A\\mathbf{x}$，设 $\\mathbf{x}=\\sum_{i=1}^n c_i\\mathbf{v}_i$，则 $A\\mathbf{x}=\\sum_{i=1}^n c_i A\\mathbf{v}_i=\\sum_{i=s+1}^n c_i A\\mathbf{v}_i$（因 $i\\le s$ 时 $A\\mathbf{v}_i=0$）。<br>(2) 线性无关：设 $\\sum_{i=s+1}^n c_i A\\mathbf{v}_i=0$，则 $A(\\sum_{i=s+1}^n c_i\\mathbf{v}_i)=0$，故 $\\sum_{i=s+1}^n c_i\\mathbf{v}_i\\in N(A)$，可表示为 $\\sum_{i=1}^s d_i\\mathbf{v}_i$。移项得 $\\sum_{i=1}^s d_i\\mathbf{v}_i-\\sum_{i=s+1}^n c_i\\mathbf{v}_i=0$。由 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_n$ 线性无关，所有系数为 0，特别 $c_i=0$（$i>s$）。<br>故 $\\dim C(A)=n-s$，即 $r=n-s$，$r+s=n$。"))
)},
{"id":"c4s1-2","name":"基础解系","tags":["def","thm","der"],"brief":"零空间的基，含 $n-r$ 个向量。",
 "body": wrap(
    defn("基础解系", p("齐次方程组 $A\\mathbf{x}=0$ 的解空间 $N(A)$ 的一组基称为该方程组的基础解系。基础解系含 $n-\\mathrm{rank}(A)$ 个线性无关的解向量。"))
    + thm("基础解系的构造", p("设 $\\mathrm{rank}(A)=r<n$，将 $A$ 化为行简化阶梯形后，有 $n-r$ 个自由变量。分别令一个自由变量为 1、其余为 0，代入求解得 $n-r$ 个解，它们构成基础解系。"))
    + der(p("<strong>证明线性无关：</strong>设所得解为 $\\boldsymbol{\\xi}_1,\\ldots,\\boldsymbol{\\xi}_{n-r}$。每个 $\\boldsymbol{\\xi}_j$ 在第 $j$ 个自由变量位置分量为 1，其他自由变量位置为 0。若 $\\sum c_j\\boldsymbol{\\xi}_j=0$，考察自由变量位置分量：第 $j$ 个自由变量位置得 $c_j=0$。故线性无关。又解空间维数为 $n-r$，故它们构成基。"))
)}
]},
# ---- 4.2 非齐次线性方程组 ----
{
"name": "4.2 非齐次线性方程组",
"color": "#be185d",
"desc": "解的存在性条件与解的结构",
"items": [
{"id":"c4s2-1","name":"解的存在性","tags":["thm","der"],"brief":"系数矩阵秩 = 增广矩阵秩。",
 "body": wrap(
    thm("非齐次方程组解的存在性", p("设 $A$ 为 $m\\times n$，$\\bar{A}=[A|\\mathbf{b}]$ 为增广矩阵。方程组 $A\\mathbf{x}=\\mathbf{b}$ 有解当且仅当 $\\mathrm{rank}(A)=\\mathrm{rank}(\\bar{A})$。"))
    + der(p("<strong>证明：</strong>设 $A=(\\mathbf{a}_1,\\ldots,\\mathbf{a}_n)$（列分块）。$A\\mathbf{x}=\\mathbf{b}$ 有解 $\\Leftrightarrow$ 存在 $x_1,\\ldots,x_n$ 使 $x_1\\mathbf{a}_1+\\cdots+x_n\\mathbf{a}_n=\\mathbf{b}$ $\\Leftrightarrow$ $\\mathbf{b}$ 可由 $A$ 的列向量线性表示 $\\Leftrightarrow$ $\\mathbf{b}\\in\\mathrm{span}(\\mathbf{a}_1,\\ldots,\\mathbf{a}_n)$ $\\Leftrightarrow$ $A$ 与 $\\bar{A}$ 的列空间相同 $\\Leftrightarrow$ $\\mathrm{rank}(A)=\\mathrm{rank}(\\bar{A})$。"))
    + thm("解的个数", p("若 $\\mathrm{rank}(A)\\neq\\mathrm{rank}(\\bar{A})$，无解；若 $\\mathrm{rank}(A)=\\mathrm{rank}(\\bar{A})=n$，有唯一解；若 $\\mathrm{rank}(A)=\\mathrm{rank}(\\bar{A})<n$，有无穷多解。"))
)},
{"id":"c4s2-2","name":"解的结构","tags":["thm","der"],"brief":"特解 + 对应齐次通解。",
 "body": wrap(
    thm("非齐次方程组解的结构", p("设 $\\boldsymbol{\\eta}^*$ 是 $A\\mathbf{x}=\\mathbf{b}$ 的一个特解，$\\boldsymbol{\\xi}_1,\\ldots,\\boldsymbol{\\xi}_{n-r}$ 是对应齐次方程组 $A\\mathbf{x}=0$ 的基础解系，则 $A\\mathbf{x}=\\mathbf{b}$ 的通解为：$\\mathbf{x}=\\boldsymbol{\\eta}^*+c_1\\boldsymbol{\\xi}_1+\\cdots+c_{n-r}\\boldsymbol{\\xi}_{n-r}$。"))
    + der(p("<strong>证明：</strong>设 $\\mathbf{x}$ 是 $A\\mathbf{x}=\\mathbf{b}$ 的任一解。则 $A(\\mathbf{x}-\\boldsymbol{\\eta}^*)=A\\mathbf{x}-A\\boldsymbol{\\eta}^*=\\mathbf{b}-\\mathbf{b}=\\mathbf{0}$，故 $\\mathbf{x}-\\boldsymbol{\\eta}^*\\in N(A)$，可表示为基础解系的线性组合：$\\mathbf{x}-\\boldsymbol{\\eta}^*=c_1\\boldsymbol{\\xi}_1+\\cdots+c_{n-r}\\boldsymbol{\\xi}_{n-r}$，即 $\\mathbf{x}=\\boldsymbol{\\eta}^*+\\sum c_i\\boldsymbol{\\xi}_i$。反之，任意这样的 $\\mathbf{x}$ 都满足 $A\\mathbf{x}=A\\boldsymbol{\\eta}^*+\\sum c_i A\\boldsymbol{\\xi}_i=\\mathbf{b}+0=\\mathbf{b}$。"))
)}
]},
# ---- 4.3 高斯消元法 ----
{
"name": "4.3 高斯消元法",
"color": "#9333ea",
"desc": "行简化阶梯形与消元求解",
"items": [
{"id":"c4s3-1","name":"行简化阶梯形","tags":["def","thm"],"brief":"每个矩阵行等价于唯一的行简化阶梯形。",
 "body": wrap(
    defn("行简化阶梯形 (RREF)", p("满足以下条件的矩阵称为行简化阶梯形：(1) 所有零行在底部；(2) 每个非零行的首非零元（主元）为 1；(3) 主元所在列的其余元素全为 0；(4) 下行主元在上方主元的右侧。"))
    + thm("RREF 的存在唯一性", p("任意矩阵 $A$ 都可通过有限次初等行变换化为行简化阶梯形，且该 RREF 是唯一的（不依赖变换顺序）。"))
)},
{"id":"c4s3-2","name":"高斯-若尔当消元","tags":["exa","app"],"brief":"系统化求解任意线性方程组。",
 "body": wrap(
    app(p("<strong>高斯消元法步骤：</strong>(1) 写出增广矩阵 $\\bar{A}=[A|\\mathbf{b}]$；(2) 用初等行变换化为行简化阶梯形；(3) 若出现 $[0\\cdots 0|c]$（$c\\neq 0$），则无解；(4) 否则，主元列对应基本变量，非主元列对应自由变量，令自由变量为任意参数，写出通解。"))
    + exa(p("<strong>例：</strong>解方程组 $\\begin{cases}x_1+x_2+x_3=6\\\\2x_1+3x_2+x_3=11\\\\3x_1+2x_2+x_3=9\\end{cases}$。增广矩阵 $\\begin{pmatrix}1&1&1&6\\\\2&3&1&11\\\\3&2&1&9\\end{pmatrix}\\xrightarrow{r_2-2r_1,r_3-3r_1}\\begin{pmatrix}1&1&1&6\\\\0&1&-1&-1\\\\0&-1&-2&-9\\end{pmatrix}\\xrightarrow{r_3+r_2}\\begin{pmatrix}1&1&1&6\\\\0&1&-1&-1\\\\0&0&-3&-10\\end{pmatrix}$。回代得 $x_3=\\frac{10}{3},x_2=\\frac{7}{3},x_1=\\frac{1}{3}$。"))
)}
]},
# ---- 4.4 线性方程组的进一步讨论 ----
{
"name": "4.4 线性方程组的进一步讨论",
"color": "#d97706",
"desc": "解的存在唯一性、矩阵方程与西尔维斯特方程",
"items": [
{"id":"c4s4-1","name":"线性方程组解的存在唯一性定理","tags":["thm","der"],"brief":"r(A)=r(Ā)=n 时唯一解。",
 "body": wrap(
    thm("解的存在唯一性定理", p("设 $A$ 为 $m\\times n$ 矩阵，$\\bar{A}=[A|\\mathbf{b}]$。线性方程组 $A\\mathbf{x}=\\mathbf{b}$：<br>(1) 无解 $\\Leftrightarrow$ $\\mathrm{rank}(A)<\\mathrm{rank}(\\bar{A})$；<br>(2) 有唯一解 $\\Leftrightarrow$ $\\mathrm{rank}(A)=\\mathrm{rank}(\\bar{A})=n$；<br>(3) 有无穷多解 $\\Leftrightarrow$ $\\mathrm{rank}(A)=\\mathrm{rank}(\\bar{A})<n$。"))
    + der(p("<strong>证明：</strong>(1) 若 $\\mathrm{rank}(A)<\\mathrm{rank}(\\bar{A})$，将 $\\bar{A}$ 化为行阶梯形后，最后一个非零行形如 $[0\\cdots 0|c]$（$c\\neq 0$），对应矛盾方程 $0=c$，无解。反之若无解，行阶梯形必出现这样的矛盾行，故 $\\mathrm{rank}(\\bar{A})=\\mathrm{rank}(A)+1$。<br>(2) 若 $\\mathrm{rank}(A)=\\mathrm{rank}(\\bar{A})=n$，行阶梯形有 $n$ 个主元，每个变量都是基本变量，回代得唯一解。<br>(3) 若秩 $r<n$，有 $n-r$ 个自由变量，取任意值均得解，故无穷多解。"))
)},
{"id":"c4s4-2","name":"矩阵方程 AX=B 与西尔维斯特方程","tags":["def","thm","der"],"brief":"将多右端项方程组统一为矩阵方程。",
 "body": wrap(
    defn("矩阵方程", p("设 $A$ 为 $m\\times n$，$B$ 为 $m\\times p$，求 $n\\times p$ 矩阵 $X$ 使 $AX=B$，称为矩阵方程。它等价于 $p$ 个线性方程组 $A\\mathbf{x}_j=\\mathbf{b}_j$（$j=1,\\ldots,p$），其中 $X=(\\mathbf{x}_1,\\ldots,\\mathbf{x}_p)$，$B=(\\mathbf{b}_1,\\ldots,\\mathbf{b}_p)$。"))
    + thm("矩阵方程有解的条件", p("$AX=B$ 有解当且仅当 $\\mathrm{rank}(A)=\\mathrm{rank}([A|B])$。若 $A$ 可逆（$m=n$ 且 $\\det A\\neq 0$），则解唯一为 $X=A^{-1}B$。"))
    + der(p("<strong>证明：</strong>$AX=B$ 有解 $\\Leftrightarrow$ 每个 $A\\mathbf{x}_j=\\mathbf{b}_j$ 有解 $\\Leftrightarrow$ 每个 $\\mathbf{b}_j$ 属于 $A$ 的列空间 $C(A)$ $\\Leftrightarrow$ $C(B)\\subseteq C(A)$ $\\Leftrightarrow$ $\\mathrm{rank}(A)=\\mathrm{rank}([A|B])$。当 $A$ 可逆时，$X=A^{-1}B$ 显然是唯一解。"))
    + note(p("<strong>西尔维斯特方程：</strong>$AX+XB=C$（$A$ 为 $m\\times m$，$B$ 为 $n\\times n$，$X,C$ 为 $m\\times n$）。它有唯一解当且仅当 $A$ 与 $-B$ 无公共特征值。该方程在控制论和矩阵论中有重要应用。"))
)}
]},
# ---- 4.5 线性方程组的几何意义 ----
{
"name": "4.5 线性方程组的几何意义",
"color": "#f59e0b",
"desc": "线性流形、解集的几何结构",
"items": [
{"id":"c4s5-1","name":"线性流形与解集的几何","tags":["def","thm"],"brief":"非齐次方程组的解集是平移的子空间。",
 "body": wrap(
    defn("线性流形", p("设 $W$ 是 $V$ 的子空间，$\\mathbf{v}_0\\in V$。集合 $\\mathbf{v}_0+W=\\{\\mathbf{v}_0+\\mathbf{w}:\\mathbf{w}\\in W\\}$ 称为 $V$ 中的一个线性流形（仿射子空间），其维数定义为 $\\dim W$。"))
    + thm("非齐次方程组的解集", p("非齐次方程组 $A\\mathbf{x}=\\mathbf{b}$（有解时）的解集是一个线性流形：$S=\\boldsymbol{\\eta}^*+N(A)$，其中 $\\boldsymbol{\\eta}^*$ 是特解，$N(A)$ 是对应齐次方程组的解空间（零空间）。解集的维数为 $n-\\mathrm{rank}(A)$。"))
    + der(p("<strong>证明：</strong>由解的结构定理，通解为 $\\mathbf{x}=\\boldsymbol{\\eta}^*+\\sum c_i\\boldsymbol{\\xi}_i$，其中 $\\boldsymbol{\\xi}_i$ 是基础解系（$N(A)$ 的基）。故解集 $S=\\{\\boldsymbol{\\eta}^*+\\mathbf{w}:\\mathbf{w}\\in N(A)\\}=\\boldsymbol{\\eta}^*+N(A)$。这是 $N(A)$ 沿 $\\boldsymbol{\\eta}^*$ 平移得到的线性流形，维数 $=\\dim N(A)=n-\\mathrm{rank}(A)$。几何上，齐次方程组的解空间是过原点的平面，非齐次方程组的解集是与之平行的平面。"))
)},
{"id":"c4s5-2","name":"基础解系的进一步性质","tags":["thm","der","note"],"brief":"基础解系含 n-r 个线性无关解。",
 "body": wrap(
    thm("基础解系的性质", p("设 $A$ 为 $m\\times n$ 矩阵，$\\mathrm{rank}(A)=r$。则齐次方程组 $A\\mathbf{x}=0$ 的基础解系恰含 $n-r$ 个线性无关的解向量，且任意 $n-r$ 个线性无关的解都构成基础解系。"))
    + der(p("<strong>证明：</strong>由秩-零度定理，$\\dim N(A)=n-r$，故解空间的基（即基础解系）恰含 $n-r$ 个向量。<br>设 $\\boldsymbol{\\xi}_1,\\ldots,\\boldsymbol{\\xi}_{n-r}$ 是任意 $n-r$ 个线性无关的解。因 $\\dim N(A)=n-r$，且这 $n-r$ 个线性无关向量都在 $N(A)$ 中，它们构成 $N(A)$ 的一组基，故也是基础解系。"))
    + note(p("<strong>求解步骤小结：</strong>(1) 对系数矩阵 $A$ 做初等行变换化为行简化阶梯形；(2) 确定主元列（基本变量）和自由变量（共 $n-r$ 个）；(3) 依次令每个自由变量为 1、其余为 0，回代求解得 $n-r$ 个解向量，即基础解系；(4) 通解为基础解系的任意线性组合。"))
)}
]},
]

# =====================================================
#  CHAPTER 5: 特征值
# =====================================================
ch5_sections = [
# ---- 5.1 特征值与特征向量 ----
{
"name": "5.1 特征值与特征向量",
"color": "#be185d",
"desc": "特征值、特征向量、特征多项式及其性质",
"items": [
{"id":"c5s1-1","name":"特征值与特征向量的定义","tags":["def","thm"],"brief":"变换下只伸缩不旋转的方向。",
 "fig":"eigen","figCap":"特征向量：变换后方向不变",
 "body": wrap(
    defn("特征值与特征向量", p("设 $A$ 为 $n$ 阶方阵。若存在数 $\\lambda$ 和非零向量 $\\mathbf{v}$ 使得 $A\\mathbf{v}=\\lambda\\mathbf{v}$，则称 $\\lambda$ 为 $A$ 的特征值，$\\mathbf{v}$ 为对应于 $\\lambda$ 的特征向量。"))
    + thm("特征值的求法", p("$\\lambda$ 是 $A$ 的特征值当且仅当 $\\det(A-\\lambda I)=0$。多项式 $p_A(\\lambda)=\\det(A-\\lambda I)$ 称为 $A$ 的特征多项式，方程 $p_A(\\lambda)=0$ 称为特征方程。"))
    + der(p("<strong>推导：</strong>$A\\mathbf{v}=\\lambda\\mathbf{v}\\Leftrightarrow(A-\\lambda I)\\mathbf{v}=0$。此齐次方程有非零解 $\\mathbf{v}\\neq 0$ 当且仅当系数矩阵奇异，即 $\\det(A-\\lambda I)=0$。特征值是特征多项式的根，对应特征向量是 $(A-\\lambda I)\\mathbf{x}=0$ 的非零解。"))
)},
{"id":"c5s1-2","name":"特征值的性质","tags":["thm","der"],"brief":"迹=特征值之和，行列式=特征值之积。",
 "body": wrap(
    thm("特征值的基本性质", p("设 $A$ 的特征值为 $\\lambda_1,\\lambda_2,\\ldots,\\lambda_n$（重根按重数计），则：<br>(1) $\\sum_{i=1}^n\\lambda_i=\\mathrm{tr}(A)=\\sum_{i=1}^n a_{ii}$（迹等于特征值之和）；<br>(2) $\\prod_{i=1}^n\\lambda_i=\\det A$（行列式等于特征值之积）；<br>(3) $A$ 可逆当且仅当所有特征值非零；<br>(4) 若 $\\lambda$ 是 $A$ 的特征值，则 $\\lambda^k$ 是 $A^k$ 的特征值，$f(\\lambda)$ 是 $f(A)$ 的特征值。"))
    + der(p("<strong>(1)(2) 的证明：</strong>特征多项式 $p_A(\\lambda)=\\det(A-\\lambda I)=(-1)^n\\lambda^n+(-1)^{n-1}(\\mathrm{tr}\\,A)\\lambda^{n-1}+\\cdots+\\det A$。另一方面，$p_A(\\lambda)=\\prod_{i=1}^n(\\lambda_i-\\lambda)=(-\\lambda)^n+(\\sum\\lambda_i)(-\\lambda)^{n-1}+\\cdots+\\prod\\lambda_i$。比较 $\\lambda^{n-1}$ 系数得 $\\mathrm{tr}\\,A=\\sum\\lambda_i$；比较常数项得 $\\det A=\\prod\\lambda_i$。"))
)},
{"id":"c5s1-3","name":"相似矩阵","tags":["def","thm","der"],"brief":"相似矩阵有相同的特征多项式。",
 "body": wrap(
    defn("相似", p("设 $A,B$ 为 $n$ 阶方阵。若存在可逆矩阵 $P$ 使得 $B=P^{-1}AP$，则称 $A$ 与 $B$ 相似，记作 $A\\sim B$。相似是一种等价关系（自反、对称、传递）。"))
    + thm("相似矩阵的不变量", p("若 $A\\sim B$，则：(1) $\\det A=\\det B$；(2) $\\mathrm{tr}\\,A=\\mathrm{tr}\\,B$；(3) $\\mathrm{rank}(A)=\\mathrm{rank}(B)$；(4) 特征多项式相同 $p_A(\\lambda)=p_B(\\lambda)$，从而特征值相同（含重数）。"))
    + der(p("<strong>(4) 的证明：</strong>设 $B=P^{-1}AP$。$p_B(\\lambda)=\\det(B-\\lambda I)=\\det(P^{-1}AP-\\lambda P^{-1}IP)=\\det(P^{-1}(A-\\lambda I)P)=\\det P^{-1}\\cdot\\det(A-\\lambda I)\\cdot\\det P=\\det(A-\\lambda I)=p_A(\\lambda)$。"))
)}
]},
# ---- 5.2 对角化 ----
{
"name": "5.2 矩阵的对角化",
"color": "#9333ea",
"desc": "可对角化的条件、对称矩阵的正交对角化",
"items": [
{"id":"c5s2-1","name":"可对角化的条件","tags":["thm","der"],"brief":"n 个线性无关特征向量即可对角化。",
 "body": wrap(
    thm("对角化判定定理", p("$n$ 阶方阵 $A$ 可对角化（即存在可逆矩阵 $P$ 使 $P^{-1}AP=D$ 为对角矩阵）当且仅当 $A$ 有 $n$ 个线性无关的特征向量。此时 $P$ 的列是 $A$ 的 $n$ 个线性无关特征向量，$D$ 的对角元是对应的特征值。"))
    + der(p("<strong>证明：</strong>设 $P=(\\mathbf{v}_1,\\ldots,\\mathbf{v}_n)$，$D=\\mathrm{diag}(\\lambda_1,\\ldots,\\lambda_n)$。$P^{-1}AP=D\\Leftrightarrow AP=PD\\Leftrightarrow A(\\mathbf{v}_1,\\ldots,\\mathbf{v}_n)=(\\mathbf{v}_1,\\ldots,\\mathbf{v}_n)D\\Leftrightarrow(A\\mathbf{v}_1,\\ldots,A\\mathbf{v}_n)=(\\lambda_1\\mathbf{v}_1,\\ldots,\\lambda_n\\mathbf{v}_n)\\Leftrightarrow A\\mathbf{v}_i=\\lambda_i\\mathbf{v}_i$。$P$ 可逆当且仅当 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_n$ 线性无关。"))
    + thm("充分条件", p("若 $A$ 有 $n$ 个互不相同的特征值，则 $A$ 可对角化。"))
    + der(p("<strong>证明：</strong>不同特征值对应的特征向量线性无关。设 $\\lambda_1,\\ldots,\\lambda_n$ 互不相同，$\\mathbf{v}_i$ 是对应 $\\lambda_i$ 的特征向量。对 $k$ 归纳证明 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_k$ 线性无关。$k=1$ 显然。设 $\\sum_{i=1}^k c_i\\mathbf{v}_i=0$。用 $A$ 作用：$\\sum c_i\\lambda_i\\mathbf{v}_i=0$。减去 $\\lambda_k$ 倍原式：$\\sum_{i=1}^{k-1}c_i(\\lambda_i-\\lambda_k)\\mathbf{v}_i=0$。由归纳假设 $c_i(\\lambda_i-\\lambda_k)=0$，因 $\\lambda_i\\neq\\lambda_k$，得 $c_i=0$（$i<k$）。代回原式得 $c_k\\mathbf{v}_k=0$，故 $c_k=0$。"))
)},
{"id":"c5s2-2","name":"实对称矩阵的正交对角化","tags":["thm","der"],"brief":"实对称矩阵必有正交特征向量基。",
 "body": wrap(
    thm("实对称矩阵的谱定理", p("设 $A$ 为 $n$ 阶实对称矩阵（$A^T=A$），则：(1) $A$ 的特征值全为实数；(2) 不同特征值对应的特征向量正交；(3) $A$ 可正交对角化，即存在正交矩阵 $Q$（$Q^TQ=I$）使得 $Q^TAQ=\\Lambda=\\mathrm{diag}(\\lambda_1,\\ldots,\\lambda_n)$。"))
    + der(p("<strong>(1) 特征值为实数的证明：</strong>设 $A\\mathbf{v}=\\lambda\\mathbf{v}$，$\\mathbf{v}\\neq 0$。取共轭转置：$\\overline{\\mathbf{v}}^T A^T=\\overline{\\lambda}\\overline{\\mathbf{v}}^T$。因 $A^T=A$ 且 $A$ 实，$\\overline{\\mathbf{v}}^T A=\\overline{\\lambda}\\overline{\\mathbf{v}}^T$。右乘 $\\mathbf{v}$：$\\overline{\\mathbf{v}}^T A\\mathbf{v}=\\overline{\\lambda}\\overline{\\mathbf{v}}^T\\mathbf{v}$。左边 $=\\overline{\\mathbf{v}}^T(\\lambda\\mathbf{v})=\\lambda\\overline{\\mathbf{v}}^T\\mathbf{v}$。故 $\\lambda\\overline{\\mathbf{v}}^T\\mathbf{v}=\\overline{\\lambda}\\overline{\\mathbf{v}}^T\\mathbf{v}$。因 $\\mathbf{v}\\neq 0$，$\\overline{\\mathbf{v}}^T\\mathbf{v}>0$，得 $\\lambda=\\overline{\\lambda}$，即 $\\lambda$ 为实数。"))
    + der(p("<strong>(2) 不同特征值特征向量正交的证明：</strong>设 $A\\mathbf{v}_1=\\lambda_1\\mathbf{v}_1$，$A\\mathbf{v}_2=\\lambda_2\\mathbf{v}_2$，$\\lambda_1\\neq\\lambda_2$。由 $A^T=A$，计算 $\\lambda_1\\mathbf{v}_1^T\\mathbf{v}_2=(A\\mathbf{v}_1)^T\\mathbf{v}_2=\\mathbf{v}_1^T A^T\\mathbf{v}_2=\\mathbf{v}_1^T A\\mathbf{v}_2=\\mathbf{v}_1^T(\\lambda_2\\mathbf{v}_2)=\\lambda_2\\mathbf{v}_1^T\\mathbf{v}_2$。故 $(\\lambda_1-\\lambda_2)\\mathbf{v}_1^T\\mathbf{v}_2=0$。因 $\\lambda_1\\neq\\lambda_2$，得 $\\mathbf{v}_1^T\\mathbf{v}_2=0$，即正交。"))
    + der(p("<strong>(3) 正交对角化的证明思路：</strong>由 (1) 特征值为实数，可取实特征向量。对重特征值，用施密特正交化将其特征子空间的基化为标准正交基；由 (2) 不同特征值的特征向量自动正交。合并所有标准正交特征向量构成正交矩阵 $Q=(\\mathbf{q}_1,\\ldots,\\mathbf{q}_n)$，则 $AQ=Q\\Lambda$，故 $Q^TAQ=\\Lambda$。"))
)}
]},
# ---- 5.3 若尔当标准形与凯莱-哈密顿 ----
{
"name": "5.3 若尔当标准形",
"color": "#7c3aed",
"desc": "若尔当块、若尔当形、凯莱-哈密顿定理",
"items": [
{"id":"c5s3-1","name":"若尔当标准形","tags":["def","thm"],"brief":"任意复矩阵相似于若尔当形。",
 "body": wrap(
    defn("若尔当块与若尔当形", p("若尔当块是形如 $J_k(\\lambda)=\\begin{pmatrix}\\lambda&1&&\\\\&\\lambda&\\ddots&\\\\&&\\ddots&1\\\\&&&\\lambda\\end{pmatrix}$ 的 $k$ 阶方阵。由若干若尔当块构成的准对角矩阵称为若尔当形矩阵。"))
    + thm("若尔当标准形定理", p("任意 $n$ 阶复方阵 $A$ 都相似于一个若尔当形矩阵 $J$，即存在可逆矩阵 $P$ 使得 $P^{-1}AP=J$。除若尔当块的排列顺序外，$J$ 由 $A$ 唯一确定，称为 $A$ 的若尔当标准形。"))
    + note(p("若尔当标准形揭示了线性变换的精细结构：每个若尔当块对应一个特征值和一个广义特征向量链。对角化是若尔当标准形的特例（所有若尔当块均为 1 阶）。"))
)},
{"id":"c5s3-2","name":"凯莱-哈密顿定理","tags":["thm","der","app"],"brief":"矩阵满足自身的特征多项式。",
 "body": wrap(
    thm("凯莱-哈密顿定理", p("设 $A$ 为 $n$ 阶方阵，$p_A(\\lambda)=\\det(A-\\lambda I)$ 为其特征多项式，则 $p_A(A)=0$（零矩阵）。即每个方阵都是其特征多项式的根。"))
    + der(p("<strong>证明（对可对角化情形）：</strong>若 $A$ 可对角化，$A=PDP^{-1}$，$D=\\mathrm{diag}(\\lambda_1,\\ldots,\\lambda_n)$。$p_A(\\lambda)=\\prod(\\lambda_i-\\lambda)$，故 $p_A(A)=P\\,p_A(D)P^{-1}=P\\,\\mathrm{diag}(p_A(\\lambda_1),\\ldots,p_A(\\lambda_n))P^{-1}$。但每个 $\\lambda_i$ 都是 $p_A$ 的根，$p_A(\\lambda_i)=0$，故 $p_A(D)=0$，从而 $p_A(A)=0$。一般情形用若尔当标准形或连续性论证（任意矩阵可用可对角化矩阵逼近）。"))
    + app(p("<strong>应用：</strong>利用凯莱-哈密顿定理可将 $A$ 的高次幂表示为 $I,A,\\ldots,A^{n-1}$ 的线性组合，从而简化计算；也可用于求逆矩阵（当 $\\det A\\neq 0$ 时，由 $p_A(A)=0$ 可解出 $A^{-1}$）。"))
)}
]},
# ---- 5.4 特征值的进一步性质 ----
{
"name": "5.4 特征值的进一步性质",
"color": "#dc2626",
"desc": "代数重数与几何重数、最小多项式、瑞利商、广义特征向量",
"items": [
{"id":"c5s4-1","name":"代数重数与几何重数","tags":["def","thm","der"],"brief":"几何重数≤代数重数。",
 "body": wrap(
    defn("代数重数与几何重数", p("设 $\\lambda$ 是 $A$ 的特征值。$\\lambda$ 作为特征多项式根的重数称为代数重数，记作 $a_\\lambda$；特征子空间 $V_\\lambda=\\{\\mathbf{v}:A\\mathbf{v}=\\lambda\\mathbf{v}\\}$ 的维数称为几何重数，记作 $g_\\lambda$。"))
    + thm("重数不等式", p("对 $A$ 的每个特征值 $\\lambda$，有 $1\\le g_\\lambda\\le a_\\lambda$。$A$ 可对角化当且仅当对所有特征值 $\\lambda$，$g_\\lambda=a_\\lambda$（即各特征子空间维数之和等于 $n$）。"))
    + der(p("<strong>证明 $g_\\lambda\\le a_\\lambda$：</strong>设 $g_\\lambda=k$，取 $V_\\lambda$ 的一组基 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_k$，扩充为 $\\mathbb{F}^n$ 的基 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_k,\\mathbf{v}_{k+1},\\ldots,\\mathbf{v}_n$。令 $P=(\\mathbf{v}_1,\\ldots,\\mathbf{v}_n)$，则 $P^{-1}AP=\\begin{pmatrix}\\lambda I_k&B\\\\0&C\\end{pmatrix}$（前 $k$ 列：$A\\mathbf{v}_i=\\lambda\\mathbf{v}_i$）。特征多项式 $p_A(\\lambda)=\\det(\\lambda I-A)=\\det\\begin{pmatrix}(\\lambda_0-\\lambda)I_k&-B\\\\0&\\lambda I-C\\end{pmatrix}=(\\lambda_0-\\lambda)^k\\det(\\lambda I-C)$，故 $\\lambda$ 的代数重数 $a_\\lambda\\ge k=g_\\lambda$。<br><strong>可对角化条件：</strong>$A$ 可对角化 $\\Leftrightarrow$ 有 $n$ 个线性无关特征向量 $\\Leftrightarrow$ $\\sum g_\\lambda=n$。又 $\\sum a_\\lambda=n$，结合 $g_\\lambda\\le a_\\lambda$，得 $\\sum g_\\lambda=n$ $\\Leftrightarrow$ 每个 $g_\\lambda=a_\\lambda$。"))
)},
{"id":"c5s4-2","name":"最小多项式","tags":["def","thm","der"],"brief":"极小多项式整除特征多项式，无重根即可对角化。",
 "body": wrap(
    defn("最小多项式", p("设 $A$ 为 $n$ 阶方阵。满足 $p(A)=0$ 的首一多项式 $p(\\lambda)$ 中次数最低的称为 $A$ 的最小多项式，记作 $m_A(\\lambda)$。由凯莱-哈密顿定理，最小多项式存在且次数 $\\le n$。"))
    + thm("最小多项式的性质", p("(1) $m_A(\\lambda)$ 整除 $A$ 的任何零化多项式（特别地，$m_A(\\lambda)\\mid p_A(\\lambda)$）；(2) $m_A(\\lambda)$ 与 $p_A(\\lambda)$ 有相同的根（不计重数），即 $A$ 的每个特征值都是 $m_A$ 的根；(3) $A$ 可对角化当且仅当 $m_A(\\lambda)$ 无重根。"))
    + der(p("<strong>(1) 的证明：</strong>设 $f(A)=0$。由多项式除法，$f(\\lambda)=q(\\lambda)m_A(\\lambda)+r(\\lambda)$，其中 $\\deg r<\\deg m_A$ 或 $r=0$。代入 $A$：$0=f(A)=q(A)m_A(A)+r(A)=r(A)$。若 $r\\neq 0$，则 $r$ 是次数低于 $m_A$ 的零化多项式，与最小性矛盾。故 $r=0$，$m_A\\mid f$。<br><strong>(3) 的证明：</strong>若 $A$ 可对角化，$A=PDP^{-1}$，$D=\\mathrm{diag}(\\lambda_1,\\ldots,\\lambda_n)$。$m_A(A)=0$ $\\Leftrightarrow$ $m_A(D)=0$ $\\Leftrightarrow$ $m_A(\\lambda_i)=0$ 对所有 $i$。最小的这样的多项式是 $\\prod_{\\lambda\\text{ 互异}}(\\lambda-\\lambda)$，无重根。反之，若 $m_A$ 无重根，则 $m_A(\\lambda)=\\prod(\\lambda-\\lambda_i)$（$\\lambda_i$ 互异）。由 $(A-\\lambda_1 I)\\cdots(A-\\lambda_k I)=0$ 可证明 $V$ 是各特征子空间的直和，故 $A$ 可对角化。"))
)},
{"id":"c5s4-3","name":"瑞利商与特征值的极值性质","tags":["def","thm","der"],"brief":"实对称矩阵的最大/最小特征值由瑞利商的极值刻画。",
 "body": wrap(
    defn("瑞利商", p("设 $A$ 为 $n$ 阶实对称矩阵，非零向量 $\\mathbf{x}\\in\\mathbb{R}^n$。$A$ 关于 $\\mathbf{x}$ 的瑞利商定义为 $R(\\mathbf{x})=\\frac{\\mathbf{x}^TA\\mathbf{x}}{\\mathbf{x}^T\\mathbf{x}}$。"))
    + thm("瑞利商的极值定理", p("设实对称矩阵 $A$ 的特征值为 $\\lambda_1\\ge\\lambda_2\\ge\\cdots\\ge\\lambda_n$。则：<br>(1) $\\lambda_1=\\max_{\\mathbf{x}\\neq 0}R(\\mathbf{x})=\\max_{\\|\\mathbf{x}\\|=1}\\mathbf{x}^TA\\mathbf{x}$；<br>(2) $\\lambda_n=\\min_{\\mathbf{x}\\neq 0}R(\\mathbf{x})=\\min_{\\|\\mathbf{x}\\|=1}\\mathbf{x}^TA\\mathbf{x}$；<br>(3) 极值在对应特征向量处取得。"))
    + der(p("<strong>证明 (1)(2)：</strong>由谱定理，$A=Q\\Lambda Q^T$，$\\Lambda=\\mathrm{diag}(\\lambda_1,\\ldots,\\lambda_n)$，$Q$ 正交。令 $\\mathbf{y}=Q^T\\mathbf{x}$，则 $\\|\\mathbf{y}\\|=\\|\\mathbf{x}\\|$，且 $R(\\mathbf{x})=\\frac{\\mathbf{y}^T\\Lambda\\mathbf{y}}{\\mathbf{y}^T\\mathbf{y}}=\\frac{\\sum\\lambda_i y_i^2}{\\sum y_i^2}$。因 $\\lambda_1\\ge\\lambda_i$，$\\sum\\lambda_i y_i^2\\le\\lambda_1\\sum y_i^2$，故 $R(\\mathbf{x})\\le\\lambda_1$。取 $\\mathbf{x}=\\mathbf{q}_1$（对应 $\\lambda_1$ 的单位特征向量），则 $R(\\mathbf{q}_1)=\\lambda_1$，故最大值为 $\\lambda_1$。同理最小值为 $\\lambda_n$。"))
)},
{"id":"c5s4-4","name":"广义特征向量与若尔当链","tags":["def","thm"],"brief":"不可对角化矩阵的精细结构由广义特征向量链刻画。",
 "body": wrap(
    defn("广义特征向量", p("设 $\\lambda$ 是 $A$ 的特征值。若非零向量 $\\mathbf{v}$ 满足 $(A-\\lambda I)^k\\mathbf{v}=0$ 对某个正整数 $k$ 成立，则称 $\\mathbf{v}$ 为对应于 $\\lambda$ 的广义特征向量。满足该式的最小 $k$ 称为 $\\mathbf{v}$ 的指数。普通特征向量是指数为 1 的广义特征向量。"))
    + thm("若尔当链", p("设 $\\mathbf{v}_k$ 是指数为 $k$ 的广义特征向量。定义 $\\mathbf{v}_{k-1}=(A-\\lambda I)\\mathbf{v}_k$，$\\mathbf{v}_{k-2}=(A-\\lambda I)\\mathbf{v}_{k-1}$，…，$\\mathbf{v}_1=(A-\\lambda I)\\mathbf{v}_2$。则 $\\mathbf{v}_1,\\ldots,\\mathbf{v}_k$ 构成若尔当链，其中 $\\mathbf{v}_1$ 是普通特征向量，且 $(A-\\lambda I)\\mathbf{v}_i=\\mathbf{v}_{i-1}$（$i\\ge 2$），$(A-\\lambda I)\\mathbf{v}_1=0$。"))
    + der(p("<strong>链的线性无关性：</strong>设 $\\sum_{i=1}^k c_i\\mathbf{v}_i=0$。用 $(A-\\lambda I)^{k-1}$ 作用：左边 $=c_k(A-\\lambda I)^{k-1}\\mathbf{v}_k+0+\\cdots+0=c_k\\mathbf{v}_1$（因 $(A-\\lambda I)^{k-1}\\mathbf{v}_i=0$ 当 $i<k$，而 $(A-\\lambda I)^{k-1}\\mathbf{v}_k=\\mathbf{v}_1$）。故 $c_k\\mathbf{v}_1=0$，$\\mathbf{v}_1\\neq 0$ 得 $c_k=0$。再用 $(A-\\lambda I)^{k-2}$ 作用得 $c_{k-1}=0$，依此类推，所有 $c_i=0$。故若尔当链线性无关。"))
)}
]},
]

# =====================================================
#  CHAPTER 6: 线性代数应用
# =====================================================
ch6_sections = [
# ---- 6.1 二次型 ----
{
"name": "6.1 二次型",
"color": "#9333ea",
"desc": "二次型的矩阵表示、合同变换、正定二次型",
"items": [
{"id":"c6s1-1","name":"二次型及其矩阵","tags":["def","thm"],"brief":"二次齐次多项式与对称矩阵一一对应。",
 "body": wrap(
    defn("二次型", p("$n$ 元二次齐次多项式 $Q(\\mathbf{x})=\\sum_{i=1}^n\\sum_{j=1}^n a_{ij}x_ix_j$（$a_{ij}=a_{ji}$）称为 $n$ 元二次型。其矩阵形式为 $Q(\\mathbf{x})=\\mathbf{x}^T A\\mathbf{x}$，其中 $A=(a_{ij})$ 为对称矩阵，称为二次型的矩阵。二次型与对称矩阵一一对应。"))
    + defn("标准形与规范形", p("若存在可逆线性变换 $\\mathbf{x}=C\\mathbf{y}$ 使 $Q(\\mathbf{x})=d_1y_1^2+\\cdots+d_ny_n^2$，称为标准形；进一步化为 $y_1^2+\\cdots+y_p^2-y_{p+1}^2-\\cdots-y_{p+q}^2$，称为规范形，其中正项个数 $p$ 为正惯性指数，负项个数 $q$ 为负惯性指数。"))
)},
{"id":"c6s1-2","name":"合同变换与惯性定理","tags":["thm","der"],"brief":"惯性指数是合同变换下的不变量。",
 "body": wrap(
    defn("合同", p("设 $A,B$ 为 $n$ 阶对称矩阵。若存在可逆矩阵 $C$ 使得 $B=C^TAC$，则称 $A$ 与 $B$ 合同。合同是对称矩阵集合上的等价关系。"))
    + thm("惯性定理", p("二次型经任意可逆线性变换化为标准形后，正项个数 $p$ 和负项个数 $q$ 都是唯一确定的，不依赖于所用的变换。"))
    + der(p("<strong>证明思路：</strong>设二次型 $Q$ 经两个不同变换分别化为标准形 $y_1^2+\\cdots+y_p^2-y_{p+1}^2-\\cdots-y_{p+q}^2$ 和 $z_1^2+\\cdots+z_{p'}^2-z_{p'+1}^2-\\cdots-z_{p'+q'}^2$。假设 $p>p'$，考虑方程组 $y_1=\\cdots=y_p=0$ 和 $z_{p'+1}=\\cdots=z_n=0$。前一组有 $p$ 个方程，后一组有 $n-p'$ 个方程，共 $p+n-p'<n$ 个方程，故有非零解。但代入 $Q$ 的两个表达式得 $Q\\le 0$ 且 $Q\\ge 0$，故 $Q=0$，进而推出所有变量为零，矛盾。故 $p=p'$。同理 $q=q'$。"))
)},
{"id":"c6s1-3","name":"正定二次型","tags":["def","thm","der"],"brief":"正定矩阵的多种等价刻画。",
 "body": wrap(
    defn("正定矩阵", p("设 $A$ 为 $n$ 阶实对称矩阵。若对任意非零向量 $\\mathbf{x}\\in\\mathbb{R}^n$ 都有 $\\mathbf{x}^TA\\mathbf{x}>0$，则称 $A$ 正定，对应的二次型 $Q(\\mathbf{x})=\\mathbf{x}^TA\\mathbf{x}$ 称为正定二次型。"))
    + thm("正定的等价条件", p("对 $n$ 阶实对称矩阵 $A$，以下等价：(1) $A$ 正定；(2) $A$ 的所有特征值 $>0$；(3) $A$ 的正惯性指数 $=n$；(4) $A$ 的所有顺序主子式 $>0$；(5) 存在可逆矩阵 $C$ 使 $A=C^TC$（即 $A$ 合同于单位矩阵）。"))
    + der(p("<strong>(1)⇒(2)：</strong>设 $\\lambda$ 是 $A$ 的特征值，$\\mathbf{v}$ 为对应特征向量。则 $\\mathbf{v}^TA\\mathbf{v}=\\lambda\\mathbf{v}^T\\mathbf{v}$。由正定，$\\mathbf{v}^TA\\mathbf{v}>0$，又 $\\mathbf{v}^T\\mathbf{v}>0$，故 $\\lambda>0$。<br><strong>(2)⇒(1)：</strong>若所有特征值 $>0$，由谱定理 $A=Q\\Lambda Q^T$，$\\Lambda=\\mathrm{diag}(\\lambda_1,\\ldots,\\lambda_n)$。对任意 $\\mathbf{x}\\neq 0$，令 $\\mathbf{y}=Q^T\\mathbf{x}\\neq 0$，则 $\\mathbf{x}^TA\\mathbf{x}=\\mathbf{y}^T\\Lambda\\mathbf{y}=\\sum\\lambda_i y_i^2>0$（因 $\\mathbf{y}\\neq 0$，至少一个 $y_i\\neq 0$）。"))
    + der(p("<strong>(1)⇒(4) 西尔维斯特判据（顺序主子式全正）：</strong>设 $A_k$ 为 $A$ 的 $k$ 阶顺序主子矩阵。对任意非零 $\\mathbf{x}_k=(x_1,\\ldots,x_k)^T$，补零为 $\\mathbf{x}=(x_1,\\ldots,x_k,0,\\ldots,0)^T\\neq 0$。因 $A$ 正定，$0<\\mathbf{x}^TA\\mathbf{x}=\\mathbf{x}_k^T A_k \\mathbf{x}_k$，故 $A_k$ 正定，从而 $\\det A_k>0$（正定矩阵行列式为正，由特征值全正与行列式=特征值之积）。<br><strong>(4)⇒(1)：</strong>对 $n$ 归纳。$n=1$ 显然。设 $n-1$ 成立。因 $\\det A_n>0$，$A$ 可逆。用分块高斯消元：$A=\\begin{pmatrix}A_{n-1}&\\mathbf{a}\\\\\\mathbf{a}^T&a_{nn}\\end{pmatrix}$，存在可逆矩阵 $P$ 使 $P^TAP=\\begin{pmatrix}A_{n-1}&0\\\\0&d\\end{pmatrix}$（合同变换），其中 $d=a_{nn}-\\mathbf{a}^TA_{n-1}^{-1}\\mathbf{a}$。由 $\\det A=\\det A_{n-1}\\cdot d>0$ 且 $\\det A_{n-1}>0$，得 $d>0$。由归纳 $A_{n-1}$ 正定，又 $d>0$，故 $P^TAP$ 正定，从而 $A$ 正定。"))
)},
{"id":"c6s1-4","name":"化二次型为标准形的方法","tags":["thm","der","app"],"brief":"配方法与正交变换法化二次型为标准形。",
 "body": wrap(
    thm("化二次型为标准形", p("任意二次型 $Q(\\mathbf{x})=\\mathbf{x}^TA\\mathbf{x}$（$A$ 对称）都可经可逆线性变换化为标准形 $d_1y_1^2+\\cdots+d_ny_n^2$。常用方法：(1) 配方法（拉格朗日）；(2) 正交变换法（$A$ 实对称时）；(3) 初等变换法。"))
    + der(p("<strong>正交变换法（实对称矩阵）：</strong>由谱定理，实对称矩阵 $A$ 可正交对角化：$Q^TAQ=\\Lambda=\\mathrm{diag}(\\lambda_1,\\ldots,\\lambda_n)$，其中 $Q$ 为正交矩阵。令 $\\mathbf{x}=Q\\mathbf{y}$，则 $Q(\\mathbf{x})=\\mathbf{y}^TQ^TAQ\\mathbf{y}=\\mathbf{y}^T\\Lambda\\mathbf{y}=\\sum_{i=1}^n\\lambda_i y_i^2$。这是标准形，且系数恰为 $A$ 的特征值。正交变换保持向量长度和夹角，故几何上是将二次曲面旋转到主轴方向。<br><strong>配方法（一般对称矩阵）：</strong>若 $a_{11}\\neq 0$，将含 $x_1$ 的项配成完全平方：$Q=a_{11}(x_1+\\frac{a_{12}}{a_{11}}x_2+\\cdots+\\frac{a_{1n}}{a_{11}}x_n)^2+Q_1(x_2,\\ldots,x_n)$，其中 $Q_1$ 是 $n-1$ 元二次型。若所有平方项系数为 0 但有交叉项，先作变换 $x_1=y_1+y_2, x_2=y_1-y_2$ 产生平方项，再继续。递归进行即得标准形。"))
    + app(p("<strong>几何应用：</strong>二次型 $\\mathbf{x}^TA\\mathbf{x}=c$ 表示二次曲面（椭球面、双曲面等）。正交变换法将其化为标准形 $\\lambda_1y_1^2+\\cdots+\\lambda_ny_n^2=c$，可直接看出曲面类型：特征值全正为椭球，有正有负为双曲，有零为柱面。"))
)}
]},
# ---- 6.2 特殊矩阵 ----
{
"name": "6.2 特殊矩阵",
"color": "#7c3aed",
"desc": "酉矩阵、厄米矩阵、辛矩阵、正规矩阵",
"items": [
{"id":"c6s2-1","name":"酉矩阵","tags":["def","thm","der"],"brief":"保持内积的复矩阵。",
 "body": wrap(
    defn("酉矩阵", p("$n$ 阶复方阵 $U$ 称为酉矩阵，若 $U^*U=UU^*=I$，其中 $U^*=\\overline{U^T}$ 为共轭转置。等价地，$U^{-1}=U^*$。实酉矩阵即正交矩阵（$Q^TQ=I$）。"))
    + thm("酉矩阵的性质", p("(1) $|\\det U|=1$；(2) $U$ 的列（行）向量构成 $\\mathbb{C}^n$ 的标准正交基；(3) 酉矩阵保持内积：$\\langle U\\mathbf{x},U\\mathbf{y}\\rangle=\\langle\\mathbf{x},\\mathbf{y}\\rangle$；(4) 酉矩阵的特征值模为 1（$|\\lambda|=1$）。"))
    + der(p("<strong>(3) 的证明：</strong>$\\langle U\\mathbf{x},U\\mathbf{y}\\rangle=(U\\mathbf{y})^T\\overline{U\\mathbf{x}}=\\mathbf{y}^TU^T\\overline{U}\\overline{\\mathbf{x}}=\\mathbf{y}^T\\overline{U^*U}\\overline{\\mathbf{x}}=\\mathbf{y}^T\\overline{I}\\overline{\\mathbf{x}}=\\mathbf{y}^T\\overline{\\mathbf{x}}=\\langle\\mathbf{x},\\mathbf{y}\\rangle$。<br><strong>(4) 的证明：</strong>设 $U\\mathbf{v}=\\lambda\\mathbf{v}$，则 $\\|U\\mathbf{v}\\|^2=\\|\\lambda\\mathbf{v}\\|^2=|\\lambda|^2\\|\\mathbf{v}\\|^2$。又 $\\|U\\mathbf{v}\\|^2=\\langle U\\mathbf{v},U\\mathbf{v}\\rangle=\\langle\\mathbf{v},\\mathbf{v}\\rangle=\\|\\mathbf{v}\\|^2$。故 $|\\lambda|^2=1$，$|\\lambda|=1$。"))
)},
{"id":"c6s2-2","name":"厄米矩阵","tags":["def","thm","der"],"brief":"自共轭的复矩阵，特征值全为实数。",
 "body": wrap(
    defn("厄米矩阵", p("$n$ 阶复方阵 $A$ 称为厄米矩阵（自共轭矩阵），若 $A^*=A$，即 $a_{ij}=\\overline{a_{ji}}$。实厄米矩阵即实对称矩阵。"))
    + thm("厄米矩阵的性质", p("(1) 厄米矩阵的特征值全为实数；(2) 不同特征值对应的特征向量正交；(3) 厄米矩阵可酉对角化，即存在酉矩阵 $U$ 使 $U^*AU=\\Lambda$ 为实对角矩阵（谱定理）。"))
    + der(p("<strong>(1) 的证明：</strong>设 $A\\mathbf{v}=\\lambda\\mathbf{v}$，$\\mathbf{v}\\neq 0$。则 $\\mathbf{v}^*A\\mathbf{v}=\\lambda\\mathbf{v}^*\\mathbf{v}$。取共轭转置：$\\overline{\\mathbf{v}^*A\\mathbf{v}}=\\mathbf{v}^*A^*\\mathbf{v}=\\mathbf{v}^*A\\mathbf{v}$，故 $\\mathbf{v}^*A\\mathbf{v}$ 为实数。又 $\\mathbf{v}^*\\mathbf{v}>0$，故 $\\lambda=\\frac{\\mathbf{v}^*A\\mathbf{v}}{\\mathbf{v}^*\\mathbf{v}}$ 为实数。"))
)},
{"id":"c6s2-3","name":"辛矩阵","tags":["def","thm","der"],"brief":"保持辛形式的线性变换。",
 "body": wrap(
    defn("辛矩阵", p("设 $J=\\begin{pmatrix}0&I_n\\\\-I_n&0\\end{pmatrix}$ 为 $2n$ 阶标准辛矩阵。$2n$ 阶方阵 $S$ 称为辛矩阵，若 $S^TJS=J$（等价地 $SJS^T=J$）。"))
    + thm("辛矩阵的性质", p("(1) 辛矩阵可逆，$S^{-1}=-JS^TJ$；(2) $\\det S=1$（辛矩阵的行列式恒为 1）；(3) 辛矩阵的特征值满足：若 $\\lambda$ 是特征值，则 $\\lambda^{-1}$、$\\overline{\\lambda}$、$\\overline{\\lambda}^{-1}$ 也都是特征值；(4) 辛矩阵的集合构成辛群 $\\mathrm{Sp}(2n,\\mathbb{F})$。"))
    + der(p("<strong>(2) 的证明：</strong>由 $S^TJS=J$，两边取行列式：$\\det(S^TJS)=\\det S^T\\cdot\\det J\\cdot\\det S=(\\det S)^2\\det J=\\det J$。因 $\\det J=1$（可通过交换 $n$ 次行将 $J$ 化为 $I_{2n}$ 或直接计算），故 $(\\det S)^2=1$，$\\det S=\\pm 1$。进一步利用 Pfaffian 或具体构造可证 $\\det S=+1$。"))
)},
{"id":"c6s2-4","name":"正规矩阵","tags":["def","thm"],"brief":"可酉对角化的复矩阵的刻画。",
 "body": wrap(
    defn("正规矩阵", p("$n$ 阶复方阵 $A$ 称为正规矩阵，若 $A^*A=AA^*$。厄米矩阵、酉矩阵、反对称厄米矩阵都是正规矩阵。"))
    + thm("正规矩阵的谱定理", p("复方阵 $A$ 可酉对角化（即存在酉矩阵 $U$ 使 $U^*AU$ 为对角矩阵）当且仅当 $A$ 是正规矩阵。"))
    + note(p("正规矩阵是可酉对角化矩阵的最广类。厄米矩阵 $\\Rightarrow$ 特征值为实数；酉矩阵 $\\Rightarrow$ 特征值在单位圆上；正规矩阵 $\\Rightarrow$ 特征值可为任意复数，但总有完备的正交特征向量组。"))
)}
]},
# ---- 6.3 矩阵分解 ----
{
"name": "6.3 矩阵分解",
"color": "#0891b2",
"desc": "LU 分解、QR 分解、奇异值分解 SVD",
"items": [
{"id":"c6s3-1","name":"LU 分解","tags":["def","thm","app"],"brief":"将矩阵分解为下三角×上三角。",
 "body": wrap(
    defn("LU 分解", p("设 $A$ 为 $n$ 阶方阵。若存在下三角矩阵 $L$（对角元为 1）和上三角矩阵 $U$ 使得 $A=LU$，则称 $A$ 有 LU 分解。"))
    + thm("LU 分解存在条件", p("若 $A$ 的各阶顺序主子式均非零，则 $A$ 有唯一的 LU 分解。否则需引入行交换，得到带置换的 LU 分解 $PA=LU$（$P$ 为置换矩阵）。"))
    + app(p("<strong>应用：解方程组 $A\\mathbf{x}=\\mathbf{b}$。</strong>由 $PA=LU$，方程组化为 $LU\\mathbf{x}=P\\mathbf{b}$。分两步：(1) 解 $L\\mathbf{y}=P\\mathbf{b}$（前代，$L$ 为单位下三角，$O(n^2)$）；(2) 解 $U\\mathbf{x}=\\mathbf{y}$（回代，$U$ 为上三角，$O(n^2)$）。总复杂度 $O(n^3)$（分解）+$O(n^2)$（求解），适合多次求解同一系数矩阵的方程组。"))
)},
{"id":"c6s3-2","name":"QR 分解","tags":["def","thm","der","app"],"brief":"正交×上三角，由施密特正交化得到。",
 "body": wrap(
    defn("QR 分解", p("设 $A$ 为 $m\\times n$ 矩阵（$m\\ge n$）。$A$ 的 QR 分解是 $A=QR$，其中 $Q$ 是 $m\\times n$ 列正交矩阵（$Q^*Q=I_n$），$R$ 是 $n\\times n$ 上三角矩阵。"))
    + thm("QR 分解的存在性", p("任意 $m\\times n$ 矩阵 $A$ 都有 QR 分解。若 $A$ 列满秩且要求 $R$ 的对角元为正，则分解唯一。"))
    + der(p("<strong>施密特法构造 QR：</strong>设 $A=(\\mathbf{a}_1,\\ldots,\\mathbf{a}_n)$。对列向量组做施密特正交化得到标准正交向量组 $\\mathbf{q}_1,\\ldots,\\mathbf{q}_n$。由正交化过程，每个 $\\mathbf{a}_k$ 可表示为 $\\mathbf{q}_1,\\ldots,\\mathbf{q}_k$ 的线性组合：$\\mathbf{a}_k=r_{1k}\\mathbf{q}_1+\\cdots+r_{kk}\\mathbf{q}_k$（$r_{kk}>0$）。令 $Q=(\\mathbf{q}_1,\\ldots,\\mathbf{q}_n)$，$R=(r_{ij})$（$r_{ij}=0$ 当 $i>j$），则 $A=QR$。"))
    + app(p("<strong>应用：</strong>QR 分解用于最小二乘法求解（$A\\mathbf{x}\\approx\\mathbf{b}$ 的最小二乘解可由 $R\\mathbf{x}=Q^T\\mathbf{b}$ 直接求解）和 QR 算法求特征值。"))
)},
{"id":"c6s3-3","name":"奇异值分解 (SVD)","tags":["def","thm","der","app"],"brief":"任意矩阵的正交对角化分解。",
 "fig":"svd","figCap":"SVD: A = UΣV*，将单位球映射为椭球",
 "body": wrap(
    defn("奇异值分解", p("设 $A$ 为 $m\\times n$ 复矩阵。$A$ 的奇异值分解为 $A=U\\Sigma V^*$，其中 $U$ 是 $m$ 阶酉矩阵，$V$ 是 $n$ 阶酉矩阵，$\\Sigma$ 是 $m\\times n$ 对角矩阵，对角元 $\\sigma_1\\ge\\sigma_2\\ge\\cdots\\ge\\sigma_r>0=\\sigma_{r+1}=\\cdots$ 为 $A$ 的奇异值，$r=\\mathrm{rank}(A)$。"))
    + thm("SVD 的存在性", p("任意 $m\\times n$ 矩阵 $A$ 都有奇异值分解。$A$ 的奇异值是 $A^*A$（或 $AA^*$）的特征值的正平方根。"))
    + der(p("<strong>构造性证明：</strong>$A^*A$ 是 $n$ 阶半正定厄米矩阵，可酉对角化：$A^*A=V\\Lambda V^*$，$\\Lambda=\\mathrm{diag}(\\lambda_1,\\ldots,\\lambda_n)$，$\\lambda_i\\ge 0$。设 $\\sigma_i=\\sqrt{\\lambda_i}$。令 $r$ 为非零 $\\sigma_i$ 的个数。对 $i=1,\\ldots,r$，定义 $\\mathbf{u}_i=\\frac{1}{\\sigma_i}A\\mathbf{v}_i$，可验证 $\\mathbf{u}_1,\\ldots,\\mathbf{u}_r$ 标准正交，且 $A\\mathbf{v}_i=\\sigma_i\\mathbf{u}_i$。将 $\\mathbf{u}_1,\\ldots,\\mathbf{u}_r$ 扩充为 $\\mathbb{C}^m$ 的标准正交基 $\\mathbf{u}_1,\\ldots,\\mathbf{u}_m$，令 $U=(\\mathbf{u}_1,\\ldots,\\mathbf{u}_m)$。则 $AV=U\\Sigma$，即 $A=U\\Sigma V^*$。"))
    + app(p("<strong>应用：</strong>(1) 低秩近似：用前 $k$ 个奇异值重建 $A_k=\\sum_{i=1}^k\\sigma_i\\mathbf{u}_i\\mathbf{v}_i^*$，是 Frobenius 范数下最优的秩 $k$ 逼近（Eckart-Young 定理）；(2) 主成分分析 (PCA)；(3) 图像压缩与数据降维；(4) 求伪逆 $A^+=V\\Sigma^+U^*$。"))
)}
]},
# ---- 6.4 综合应用 ----
{
"name": "6.4 综合应用",
"color": "#be185d",
"desc": "线性变换、主成分分析、最小二乘",
"items": [
{"id":"c6s4-1","name":"线性变换与矩阵","tags":["app","thm"],"brief":"线性变换在基下的矩阵表示。",
 "body": wrap(
    thm("线性变换的矩阵表示", p("设 $T:V\\to W$ 是有限维向量空间之间的线性映射，$B_V=\\{\\mathbf{v}_1,\\ldots,\\mathbf{v}_n\\}$ 和 $B_W=\\{\\mathbf{w}_1,\\ldots,\\mathbf{w}_m\\}$ 分别是 $V,W$ 的基。$T$ 的矩阵 $A=(a_{ij})$ 定义为 $T(\\mathbf{v}_j)=\\sum_{i=1}^m a_{ij}\\mathbf{w}_i$。则 $[T(\\mathbf{x})]_{B_W}=A[\\mathbf{x}]_{B_V}$。"))
    + app(p("<strong>几何意义：</strong>矩阵乘法对应线性变换的复合。$2\\times 2$ 矩阵可表示平面上的旋转、缩放、剪切、反射等变换。例如旋转矩阵 $R_\\theta=\\begin{pmatrix}\\cos\\theta&-\\sin\\theta\\\\\\sin\\theta&\\cos\\theta\\end{pmatrix}$ 是正交矩阵，特征值为 $e^{\\pm i\\theta}$。"))
)},
{"id":"c6s4-2","name":"主成分分析 (PCA)","tags":["app","der"],"brief":"用协方差矩阵的特征向量找主成分。",
 "body": wrap(
    defn("PCA 原理", p("设数据矩阵 $X$（$n$ 行 $d$ 列，已中心化），协方差矩阵 $C=\\frac{1}{n}X^TX$（$d\\times d$ 对称半正定）。PCA 找 $C$ 的特征值 $\\lambda_1\\ge\\cdots\\ge\\lambda_d$ 及对应正交特征向量 $\\mathbf{w}_1,\\ldots,\\mathbf{w}_d$，$\\mathbf{w}_k$ 称为第 $k$ 主成分方向，数据在 $\\mathbf{w}_k$ 上的投影方差为 $\\lambda_k$。"))
    + der(p("<strong>为什么特征向量给出最大方差方向：</strong>我们要找单位向量 $\\mathbf{w}$ 最大化投影方差 $\\mathrm{Var}(X\\mathbf{w})=\\mathbf{w}^TC\\mathbf{w}$。在约束 $\\|\\mathbf{w}\\|=1$ 下，由拉格朗日乘数法，极值点满足 $C\\mathbf{w}=\\lambda\\mathbf{w}$，即 $\\mathbf{w}$ 是 $C$ 的特征向量。方差值 $\\mathbf{w}^TC\\mathbf{w}=\\lambda$，故最大方差方向是最大特征值对应的特征向量。前 $k$ 个主成分累计解释方差比为 $\\frac{\\sum_{i=1}^k\\lambda_i}{\\sum_{i=1}^d\\lambda_i}$。"))
)},
{"id":"c6s4-3","name":"最小二乘法","tags":["app","thm","der"],"brief":"超定方程组的最优近似解。",
 "body": wrap(
    thm("最小二乘解", p("设 $A$ 为 $m\\times n$ 矩阵（$m>n$），$\\mathbf{b}\\in\\mathbb{R}^m$。超定方程组 $A\\mathbf{x}=\\mathbf{b}$ 一般无解。最小二乘解 $\\hat{\\mathbf{x}}$ 是使 $\\|A\\mathbf{x}-\\mathbf{b}\\|^2$ 最小的 $\\mathbf{x}$，满足法方程 $A^TA\\hat{\\mathbf{x}}=A^T\\mathbf{b}$。若 $A$ 列满秩，则 $\\hat{\\mathbf{x}}=(A^TA)^{-1}A^T\\mathbf{b}$。"))
    + der(p("<strong>推导：</strong>$f(\\mathbf{x})=\\|A\\mathbf{x}-\\mathbf{b}\\|^2=(A\\mathbf{x}-\\mathbf{b})^T(A\\mathbf{x}-\\mathbf{b})=\\mathbf{x}^TA^TA\\mathbf{x}-2\\mathbf{b}^TA\\mathbf{x}+\\mathbf{b}^T\\mathbf{b}$。对 $\\mathbf{x}$ 求梯度并令其为零：$\\nabla f=2A^TA\\mathbf{x}-2A^T\\mathbf{b}=0$，得 $A^TA\\mathbf{x}=A^T\\mathbf{b}$。若 $A$ 列满秩，则 $A^TA$ 正定可逆，解唯一。几何上，$A\\hat{\\mathbf{x}}$ 是 $\\mathbf{b}$ 在 $A$ 的列空间上的正交投影。"))
)}
]},
# ---- 6.5 二次型的合同对角化与分类 ----
{
"name": "6.5 二次型的合同对角化与分类",
"color": "#7c3aed",
"desc": "半正定与负定、合同变换化标准形、二次型的分类",
"items": [
{"id":"c6s5-1","name":"半正定与负定二次型","tags":["def","thm","der"],"brief":"特征值全非负则半正定，全负则负定。",
 "body": wrap(
    defn("半正定与负定", p("设 $A$ 为 $n$ 阶实对称矩阵。若对任意 $\\mathbf{x}$，$\\mathbf{x}^TA\\mathbf{x}\\ge 0$，称 $A$ 半正定；若对任意非零 $\\mathbf{x}$，$\\mathbf{x}^TA\\mathbf{x}<0$，称 $A$ 负定。"))
    + thm("半正定的等价条件", p("对实对称矩阵 $A$，以下等价：(1) $A$ 半正定；(2) $A$ 的所有特征值 $\\ge 0$；(3) $A$ 的正惯性指数 $=\\mathrm{rank}(A)$；(4) 存在矩阵 $C$ 使 $A=C^TC$；(5) $A$ 的所有主子式 $\\ge 0$。"))
    + der(p("<strong>(1)⇔(2)：</strong>由谱定理 $A=Q\\Lambda Q^T$。$\\mathbf{x}^TA\\mathbf{x}=\\sum\\lambda_i y_i^2$（$\\mathbf{y}=Q^T\\mathbf{x}$）。对任意 $\\mathbf{x}\\neq 0$ 有 $\\mathbf{y}\\neq 0$。$\\sum\\lambda_i y_i^2\\ge 0$ 对所有 $\\mathbf{y}$ 成立 $\\Leftrightarrow$ 所有 $\\lambda_i\\ge 0$（若有 $\\lambda_j<0$，取 $\\mathbf{y}=\\mathbf{e}_j$ 得负值）。<br><strong>(2)⇒(4)：</strong>若特征值 $\\ge 0$，令 $\\Sigma^{1/2}=\\mathrm{diag}(\\sqrt{\\lambda_1},\\ldots,\\sqrt{\\lambda_n})$，则 $A=Q\\Lambda Q^T=Q\\Sigma^{1/2}\\Sigma^{1/2}Q^T=(\\Sigma^{1/2}Q^T)^T(\\Sigma^{1/2}Q^T)=C^TC$，其中 $C=\\Sigma^{1/2}Q^T$。"))
)},
{"id":"c6s5-2","name":"合同变换化二次型为标准形","tags":["thm","der"],"brief":"用可逆线性变换（合同）化二次型为平方和。",
 "body": wrap(
    thm("合同对角化定理", p("任意 $n$ 阶对称矩阵 $A$ 都合同于一个对角矩阵，即存在可逆矩阵 $C$ 使 $C^TAC=\\mathrm{diag}(d_1,\\ldots,d_n)$。等价地，任意二次型都可经可逆线性变换化为标准形。"))
    + der(p("<strong>证明（归纳法）：</strong>$n=1$ 显然。设 $n-1$ 成立。对 $n$ 阶对称矩阵 $A$：<br>若 $A$ 有非零对角元，不妨设 $a_{11}\\neq 0$（否则可通过合同变换交换行列使某个非零元到对角）。令 $C_1=\\begin{pmatrix}1&-\\frac{\\mathbf{a}^T}{a_{11}}\\\\0&I_{n-1}\\end{pmatrix}$，其中 $\\mathbf{a}=(a_{12},\\ldots,a_{1n})^T$。则 $C_1^TAC_1=\\begin{pmatrix}a_{11}&0\\\\0&A_1\\end{pmatrix}$，其中 $A_1$ 是 $n-1$ 阶对称矩阵。由归纳假设，存在可逆 $C_2$ 使 $C_2^TA_1C_2$ 为对角矩阵。令 $C=C_1\\begin{pmatrix}1&0\\\\0&C_2\\end{pmatrix}$，则 $C^TAC$ 为对角矩阵。<br>若 $A$ 所有对角元为 0 但 $A\\neq 0$，设 $a_{12}\\neq 0$。令 $C_1$ 为将第 2 列加到第 1 列（同时第 2 行加到第 1 行）的初等矩阵，则 $C_1^TAC_1$ 的 $(1,1)$ 元为 $2a_{12}\\neq 0$，化为已证情形。"))
)},
{"id":"c6s5-3","name":"二次型的分类与惯性指数","tags":["def","thm","app"],"brief":"按惯性指数将二次型分为正定、负定、半正定、半负定、不定。",
 "body": wrap(
    defn("二次型的分类", p("设二次型 $Q(\\mathbf{x})=\\mathbf{x}^TA\\mathbf{x}$ 的正惯性指数为 $p$，负惯性指数为 $q$，秩为 $r=p+q$。则：<br>(1) $p=n$（$q=0$）：正定；<br>(2) $q=n$（$p=0$）：负定；<br>(3) $p=r<n$（$q=0$）：半正定；<br>(4) $q=r<n$（$p=0$）：半负定；<br>(5) $p>0$ 且 $q>0$：不定。"))
    + thm("惯性定理再述", p("二次型的正惯性指数 $p$ 和负惯性指数 $q$ 是合同变换下的不变量，与所选的可逆线性变换无关。$p-q$ 称为符号差。"))
    + app(p("<strong>几何分类（二元二次型）：</strong>$Q(x,y)=ax^2+2bxy+cy^2$，矩阵 $A=\\begin{pmatrix}a&b\\\\b&c\\end{pmatrix}$。<br>(1) $\\det A=ac-b^2>0$ 且 $a>0$：正定（椭圆型）；<br>(2) $\\det A>0$ 且 $a<0$：负定；<br>(3) $\\det A<0$：不定（双曲型）；<br>(4) $\\det A=0$：半正定或半负定（抛物型）。这与二次曲线 $ax^2+2bxy+cy^2=1$ 的分类完全对应。"))
)}
]},
]

# =====================================================
#  CHAPTERS assembly
# =====================================================
CHAPTERS = [
    {"id":"l-ch1","num":"第一章","title":"线性空间","en":"LINEAR SPACES",
     "desc":"从向量空间的公理出发，建立子空间、线性相关、基与维数的概念，并引入内积空间中的正交性与投影理论。",
     "sections": ch1_sections},
    {"id":"l-ch2","num":"第二章","title":"矩阵","en":"MATRICES",
     "desc":"矩阵的线性运算与乘法、转置与对称矩阵、逆矩阵的存在条件与计算、初等变换与矩阵的秩。",
     "sections": ch2_sections},
    {"id":"l-ch3","num":"第三章","title":"行列式","en":"DETERMINANTS",
     "desc":"从排列逆序数出发定义 n 阶行列式，系统推导行列式的性质与按行（列）展开定理，以及伴随矩阵、克拉默法则等应用。",
     "sections": ch3_sections},
    {"id":"l-ch4","num":"第四章","title":"线性方程组","en":"LINEAR SYSTEMS",
     "desc":"齐次与非齐次线性方程组解的结构、基础解系、解的存在唯一性判据，以及高斯消元法的系统化求解。",
     "sections": ch4_sections},
    {"id":"l-ch5","num":"第五章","title":"特征值","en":"EIGENVALUES",
     "desc":"特征值与特征向量的定义与求法、特征多项式与迹-行列式关系、相似与对角化、实对称矩阵的谱定理、若尔当标准形与凯莱-哈密顿定理。",
     "sections": ch5_sections},
    {"id":"l-ch6","num":"第六章","title":"线性代数应用","en":"APPLICATIONS",
     "desc":"二次型与正定性、酉矩阵/厄米矩阵/辛矩阵/正规矩阵等特殊矩阵、LU/QR/SVD 三大矩阵分解，以及 PCA、最小二乘、线性变换等综合应用。",
     "sections": ch6_sections},
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
  .la-nav-tab.c6{color:#9333ea;border-color:#e9d5ff}
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
  .la-phase-title.la-ch1::before{background:#2563eb}
  .la-phase-title.la-ch2::before{background:#0d9488}
  .la-phase-title.la-ch3::before{background:#059669}
  .la-phase-title.la-ch4::before{background:#0891b2}
  .la-phase-title.la-ch5::before{background:#be185d}
  .la-phase-title.la-ch6::before{background:#9333ea}
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
<meta name="description" content="线性代数知识体系：线性空间、矩阵、行列式、线性方程组、特征值、线性代数应用">
<title>线性代数 · 知识体系</title>
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
    <div class="la-eyebrow">LINEAR ALGEBRA · KNOWLEDGE MAP</div>
    <h1>线性代数 · 知识体系</h1>
    <p class="la-subtitle">线性空间 · 矩阵 · 行列式 · 线性方程组 · 特征值 · 线性代数应用</p>
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
    <div>线性代数 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于线性代数核心知识体系整理</div>
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
    with open("/workspace/linear-algebra.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated linear-algebra.html ({len(html)} chars)")
