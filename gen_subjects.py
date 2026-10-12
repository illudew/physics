# -*- coding: utf-8 -*-
"""全部学科的知识内容数据。由 gen.py 渲染为 HTML。"""
from gen import write_subject

def item(id, name, tags, brief, body, fig=None, figCap=None):
    d = {"id": id, "name": name, "tags": tags, "brief": brief, "body": body}
    if fig: d["fig"] = fig
    if figCap: d["figCap"] = figCap
    return d

SUBJECTS = []

# ============================================================
# 1. 初等数学 elementary-math
# ============================================================
SUBJECTS.append({
  "filename":"elementary-math.html",
  "title":"初等数学",
  "eyebrow":"ELEMENTARY MATHEMATICS",
  "subtitle":"反三角函数 · 极坐标 · 向量叉乘 · 数列 · 不等式 · 解析几何",
  "meta_desc":"初等数学知识体系：反三角函数、极坐标、向量、数列、不等式、解析几何",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"三角函数与反三角","en":"TRIGONOMETRY","sub":"角度与弧度、三角恒等式","desc":"三角函数是初等数学的核心工具。本章复习角度制与弧度制、基本恒等式、和差化积与反三角函数。","sections":[
      {"name":"1.1 角度与弧度","color":"#2563eb","desc":"两种度量方式的换算","items":[
        item("la-k1-1","弧度制",["def","exa"],"$180^\\circ = \\pi$ 弧度，弧长 $l=r\\theta$。","<p><strong>定义</strong>　在半径为 $r$ 的圆中，弧长等于半径的圆心角为 1 弧度（rad）。</p><div class=\"la-fml\">$$\\theta(\\text{rad}) = \\frac{\\pi}{180^\\circ}\\theta(^\\circ)$$</div><p>常见换算：$30^\\circ=\\pi/6$，$45^\\circ=\\pi/4$，$60^\\circ=\\pi/3$，$90^\\circ=\\pi/2$。</p>"),
        item("la-k1-2","基本恒等式",["thm"],"$\\sin^2\\theta+\\cos^2\\theta=1$，商数与倒数关系。","<p><strong>定理</strong>　对任意角 $\\theta$：</p><div class=\"la-fml\">$$\\sin^2\\theta+\\cos^2\\theta=1,\\quad \\tan\\theta=\\frac{\\sin\\theta}{\\cos\\theta},\\quad \\cot\\theta=\\frac{\\cos\\theta}{\\sin\\theta}$$</div>"),
      ]},
      {"name":"1.2 和差角与倍角","color":"#7c3aed","desc":"三角恒等变换的核心公式","items":[
        item("la-k1-3","和差角公式",["thm","der"],"$\\sin(\\alpha\\pm\\beta)=\\sin\\alpha\\cos\\beta\\pm\\cos\\alpha\\sin\\beta$。","<p><strong>推导</strong>　利用单位圆上两点距离可证：</p><div class=\"la-fml\">$$\\cos(\\alpha-\\beta)=\\cos\\alpha\\cos\\beta+\\sin\\alpha\\sin\\beta$$</div><p>由此推出和差角正弦、余弦、正切公式。</p>"),
        item("la-k1-4","二倍角与半角",["thm"],"$\\sin2\\theta=2\\sin\\theta\\cos\\theta$，$\\cos2\\theta=\\cos^2\\theta-\\sin^2\\theta$。","<p>令 $\\alpha=\\beta=\\theta$ 即得二倍角公式。半角公式：</p><div class=\"la-fml\">$$\\sin\\frac{\\theta}{2}=\\pm\\sqrt{\\frac{1-\\cos\\theta}{2}},\\quad \\cos\\frac{\\theta}{2}=\\pm\\sqrt{\\frac{1+\\cos\\theta}{2}}$$</div>"),
      ]},
      {"name":"1.3 反三角函数","color":"#0f766e","desc":"三角方程的解与主值","items":[
        item("la-k1-5","反正弦与反余弦",["def"],"$\\arcsin x\\in[-\\pi/2,\\pi/2]$，$\\arccos x\\in[0,\\pi]$。","<p><strong>定义</strong>　$y=\\arcsin x$ 是 $y=\\sin x$ 在 $[-\\pi/2,\\pi/2]$ 上的反函数；$y=\\arccos x$ 是 $y=\\cos x$ 在 $[0,\\pi]$ 上的反函数。</p><div class=\"la-fml\">$$\\arcsin x+\\arccos x=\\frac{\\pi}{2}\\quad(|x|\\le 1)$$</div>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"向量与极坐标","en":"VECTORS & POLAR","sub":"向量运算、坐标系转换","desc":"向量是描述物理量的基本语言。本章复习向量的加减、点积、叉乘，以及极坐标与直角坐标的换算。","sections":[
      {"name":"2.1 向量代数","color":"#2563eb","desc":"线性运算、点积、叉乘","items":[
        item("la-k2-1","向量的线性运算",["def","exa"],"加法满足平行四边形法则，数乘缩放长度。","<p><strong>定义</strong>　向量 $\\boldsymbol{a}=(a_1,a_2,a_3)$，数乘 $\\lambda\\boldsymbol{a}=(\\lambda a_1,\\lambda a_2,\\lambda a_3)$。</p><div class=\"la-fml\">$$|\\lambda\\boldsymbol{a}|=|\\lambda|\\,|\\boldsymbol{a}|$$</div>"),
        item("la-k2-2","点积与叉乘",["def","thm"],"$\\boldsymbol{a}\\cdot\\boldsymbol{b}=|a||b|\\cos\\theta$，叉乘垂直于两向量。","<p><strong>点积</strong>：$\\boldsymbol{a}\\cdot\\boldsymbol{b}=a_1b_1+a_2b_2+a_3b_3$，结果为标量。</p><p><strong>叉乘</strong>：$\\boldsymbol{a}\\times\\boldsymbol{b}=(a_2b_3-a_3b_2,\\,a_3b_1-a_1b_3,\\,a_1b_2-a_2b_1)$，方向由右手定则确定。</p><div class=\"la-fml\">$$|\\boldsymbol{a}\\times\\boldsymbol{b}|=|a||b|\\sin\\theta$$</div>"),
      ]},
      {"name":"2.2 极坐标","color":"#7c3aed","desc":"平面点的另一种表示","items":[
        item("la-k2-3","极坐标与直角坐标",["def","exa"],"$x=r\\cos\\theta$，$y=r\\sin\\theta$。","<p>极坐标用 $(r,\\theta)$ 表示平面点，与直角坐标互换：</p><div class=\"la-fml\">$$r=\\sqrt{x^2+y^2},\\quad \\theta=\\arctan\\frac{y}{x}$$</div>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"数列与不等式","en":"SEQUENCES & INEQUALITIES","sub":"等差等比数列、均值不等式","desc":"数列是函数的离散形式，不等式是估计与证明的工具。","sections":[
      {"name":"3.1 数列","color":"#0f766e","desc":"等差、等比与求和","items":[
        item("la-k3-1","等差数列",["def","thm"],"$a_n=a_1+(n-1)d$，$S_n=\\frac{n(a_1+a_n)}{2}$。","<p>公差为 $d$ 的等差数列，通项与前 $n$ 项和：</p><div class=\"la-fml\">$$a_n=a_1+(n-1)d,\\quad S_n=na_1+\\frac{n(n-1)}{2}d$$</div>"),
        item("la-k3-2","等比数列",["def","thm"],"$a_n=a_1q^{n-1}$，$S_n=a_1\\frac{1-q^n}{1-q}$。","<p>公比为 $q$ 的等比数列。当 $|q|<1$ 时无穷级数收敛：</p><div class=\"la-fml\">$$S=\\lim_{n\\to\\infty}S_n=\\frac{a_1}{1-q}$$</div>"),
      ]},
      {"name":"3.2 重要不等式","color":"#c2410c","desc":"均值不等式与柯西","items":[
        item("la-k3-3","均值不等式",["thm"],"$\\frac{a+b}{2}\\ge\\sqrt{ab}\\ge\\frac{2ab}{a+b}$。","<p>对正数 $a,b$，调和平均 $\\le$ 几何平均 $\\le$ 算术平均：</p><div class=\"la-fml\">$$\\frac{2}{\\frac{1}{a}+\\frac{1}{b}}\\le\\sqrt{ab}\\le\\frac{a+b}{2}$$</div>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"解析几何","en":"ANALYTIC GEOMETRY","sub":"直线、圆锥曲线","desc":"用代数方法研究几何图形。直线、圆、椭圆、双曲线、抛物线。","sections":[
      {"name":"4.1 直线与圆","color":"#2563eb","desc":"直线方程与圆的方程","items":[
        item("la-k4-1","直线方程",["def","exa"],"点斜式 $y-y_0=k(x-x_0)$，一般式 $Ax+By+C=0$。","<p>斜率 $k=\\tan\\alpha$，两点 $(x_1,y_1),(x_2,y_2)$ 连线斜率：</p><div class=\"la-fml\">$$k=\\frac{y_2-y_1}{x_2-x_1}$$</div>"),
        item("la-k4-2","圆的方程",["def","thm"],"$(x-a)^2+(y-b)^2=r^2$。","<p>圆心 $(a,b)$、半径 $r$ 的圆。一般方程 $x^2+y^2+Dx+Ey+F=0$，圆心 $(-D/2,-E/2)$。</p>"),
      ]},
      {"name":"4.2 圆锥曲线","color":"#7c3aed","desc":"椭圆、双曲线、抛物线","items":[
        item("la-k4-3","椭圆",["def","thm"],"$\\frac{x^2}{a^2}+\\frac{y^2}{b^2}=1$，离心率 $e=c/a<1$。","<p>到两焦点距离之和为定值 $2a$ 的点轨迹。$c^2=a^2-b^2$。</p>"),
        item("la-k4-4","双曲线与抛物线",["def"],"双曲线 $e>1$，抛物线 $e=1$。","<p>双曲线：$\\frac{x^2}{a^2}-\\frac{y^2}{b^2}=1$，$c^2=a^2+b^2$。抛物线：$y^2=2px$，焦点 $(p/2,0)$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 2. 微积分（高等数学） advanced-math
# ============================================================
SUBJECTS.append({
  "filename":"advanced-math.html",
  "title":"微积分",
  "eyebrow":"CALCULUS",
  "subtitle":"极限 · 导数 · 积分 · 微分方程 · 多元微积分 · 无穷级数",
  "meta_desc":"微积分知识体系：极限、导数、积分、微分方程、多元微积分、无穷级数",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"极限与连续","en":"LIMITS & CONTINUITY","sub":"极限定义、收敛准则、连续函数","desc":"微积分的基石是极限。本章建立数列极限与函数极限的严格定义，讨论连续性与闭区间上连续函数的性质。","sections":[
      {"name":"1.1 极限","color":"#2563eb","desc":"$\\varepsilon$-$\\delta$ 语言","items":[
        item("la-k1-1","数列极限",["def","thm"],"$\\forall\\varepsilon>0,\\exists N,\\forall n>N:|a_n-A|<\\varepsilon$。","<p><strong>定义</strong>　数列 $\\{a_n\\}$ 收敛于 $A$：对任意 $\\varepsilon>0$，存在正整数 $N$，当 $n>N$ 时 $|a_n-A|<\\varepsilon$。</p>"),
        item("la-k1-2","两个重要极限",["thm","exa"],"$\\lim_{x\\to0}\\frac{\\sin x}{x}=1$，$\\lim_{x\\to\\infty}(1+\\frac1x)^x=e$。","<p>这两个极限是导数定义的基础。第二个定义了自然常数 $e\\approx2.71828$。</p>"),
      ]},
      {"name":"1.2 连续","color":"#7c3aed","desc":"连续函数的性质","items":[
        item("la-k1-3","函数连续",["def","thm"],"$\\lim_{x\\to a}f(x)=f(a)$。","<p>函数在 $a$ 连续要求：极限存在、$f(a)$ 有定义、二者相等。闭区间上连续函数有最值定理、介值定理、零点定理。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"导数与微分","en":"DERIVATIVES","sub":"导数定义、求导法则、微分中值定理","desc":"导数刻画瞬时变化率，微分中值定理连接导数与函数值。","sections":[
      {"name":"2.1 导数","color":"#2563eb","desc":"变化率与切线斜率","items":[
        item("la-k2-1","导数定义",["def"],"$f'(x)=\\lim_{\\Delta x\\to0}\\frac{f(x+\\Delta x)-f(x)}{\\Delta x}$。","<p>导数即切线斜率。基本求导公式：$(x^n)'=nx^{n-1}$，$(\\sin x)'=\\cos x$，$(e^x)'=e^x$，$(\\ln x)'=1/x$。</p>"),
        item("la-k2-2","求导法则",["thm"],"$(uv)'=u'v+uv'$，$(u/v)'=(u'v-uv')/v^2$，链式法则。","<p>链式法则：若 $y=f(u),u=g(x)$，则 $y'=f'(u)\\cdot g'(x)$。</p>"),
      ]},
      {"name":"2.2 中值定理","color":"#0f766e","desc":"罗尔、拉格朗日、柯西","items":[
        item("la-k2-3","拉格朗日中值定理",["thm"],"$\\exists\\xi\\in(a,b):f(b)-f(a)=f'(\\xi)(b-a)$。","<p>若 $f$ 在 $[a,b]$ 连续、$(a,b)$ 可导，则存在 $\\xi$ 使切线平行于割线。罗尔定理是其 $f(a)=f(b)$ 的特例。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"积分","en":"INTEGRALS","sub":"不定积分、定积分、牛顿-莱布尼茨公式","desc":"积分是微分的逆运算。牛顿-莱布尼茨公式将定积分与原函数联系起来。","sections":[
      {"name":"3.1 不定积分","color":"#7c3aed","desc":"原函数与积分公式","items":[
        item("la-k3-1","不定积分",["def","exa"],"$\\int f(x)\\,dx=F(x)+C$，$F'=f$。","<p>基本公式：$\\int x^n dx=\\frac{x^{n+1}}{n+1}+C$，$\\int \\frac1x dx=\\ln|x|+C$，$\\int e^x dx=e^x+C$。</p>"),
        item("la-k3-2","换元与分部积分",["thm","der"],"$\\int f(g(x))g'(x)dx=\\int f(u)du$，$\\int u\\,dv=uv-\\int v\\,du$。","<p>换元积分用于复合函数，分部积分用于乘积：选择 $u$ 按 LIATE 法则（对数、反三角、代数、三角、指数）。</p>"),
      ]},
      {"name":"3.2 定积分","color":"#c2410c","desc":"黎曼和与微积分基本定理","items":[
        item("la-k3-3","牛顿-莱布尼茨公式",["thm"],"$\\int_a^b f(x)dx=F(b)-F(a)$。","<p>微积分基本定理：若 $F'=f$，则定积分等于原函数的差值。这是微分与积分的桥梁。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"微分方程","en":"DIFFERENTIAL EQUATIONS","sub":"一阶、二阶常微分方程","desc":"微分方程描述变化规律。本章覆盖可分离变量、一阶线性、二阶常系数线性方程。","sections":[
      {"name":"4.1 一阶方程","color":"#2563eb","desc":"可分离变量与一阶线性","items":[
        item("la-k4-1","可分离变量",["def","exa"],"$\\frac{dy}{dx}=f(x)g(y)\\Rightarrow\\int\\frac{dy}{g(y)}=\\int f(x)dx$。","<p>形如 $y'=f(x)g(y)$ 的方程可分离变量后两边积分。</p>"),
        item("la-k4-2","一阶线性方程",["thm","der"],"$y'+P(x)y=Q(x)$，积分因子 $\\mu=e^{\\int Pdx}$。","<p>通解公式：</p><div class=\"la-fml\">$$y=e^{-\\int Pdx}\\left(\\int Qe^{\\int Pdx}dx+C\\right)$$</div>"),
      ]},
      {"name":"4.2 二阶常系数线性","color":"#0f766e","desc":"齐次与非齐次","items":[
        item("la-k4-3","二阶常系数齐次",["thm"],"$y''+py'+qy=0$，特征方程 $r^2+pr+q=0$。","<p>根据特征根 $r_1,r_2$：</p><ul><li>两不等实根：$y=C_1e^{r_1x}+C_2e^{r_2x}$</li><li>重根：$y=(C_1+C_2x)e^{rx}$</li><li>共轭复根 $\\alpha\\pm i\\beta$：$y=e^{\\alpha x}(C_1\\cos\\beta x+C_2\\sin\\beta x)$</li></ul>"),
      ]},
    ]},
    {"id":"la-ch5","num":"第五章","title":"多元微积分与级数","en":"MULTIVARIABLE & SERIES","sub":"偏导数、重积分、级数收敛","desc":"将微积分推广到多元函数，并引入无穷级数作为函数表示工具。","sections":[
      {"name":"5.1 多元函数微分","color":"#7c3aed","desc":"偏导数、全微分、链式法则","items":[
        item("la-k5-1","偏导数",["def"],"$f_x=\\frac{\\partial f}{\\partial x}$，固定其他变量对 $x$ 求导。","<p>偏导数 $f_x$ 刻画函数沿 $x$ 方向的变化率。混合偏导在连续时相等：$f_{xy}=f_{yx}$。</p>"),
        item("la-k5-2","全微分",["def","thm"],"$dz=\\frac{\\partial z}{\\partial x}dx+\\frac{\\partial z}{\\partial y}dy$。","<p>全微分是多元函数线性增量的主部。可微要求偏导数存在且连续。</p>"),
      ]},
      {"name":"5.2 无穷级数","color":"#c2410c","desc":"数项级数、幂级数、泰勒级数","items":[
        item("la-k5-3","级数收敛",["def","thm"],"$\\sum a_n$ 收敛 $\\iff$ 部分和 $S_n$ 收敛。","<p>判别法：比值判别 $\\lim|a_{n+1}/a_n|$，根值判别 $\\lim\\sqrt[n]{|a_n|}$，比较判别，莱布尼茨交错级数判别。</p>"),
        item("la-k5-4","泰勒级数",["thm","app"],"$f(x)=\\sum_{n=0}^\\infty\\frac{f^{(n)}(a)}{n!}(x-a)^n$。","<p>常用展开：$e^x=\\sum x^n/n!$，$\\sin x=\\sum(-1)^n x^{2n+1}/(2n+1)!$，$\\frac1{1-x}=\\sum x^n$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 3. 概率论与数理统计 probability-statistics
# ============================================================
SUBJECTS.append({
  "filename":"probability-statistics.html",
  "title":"概率论与数理统计",
  "eyebrow":"PROBABILITY & STATISTICS",
  "subtitle":"随机事件 · 随机变量 · 分布 · 数字特征 · 参数估计 · 假设检验",
  "meta_desc":"概率论与数理统计知识体系：随机事件、随机变量、分布、数字特征、参数估计、假设检验",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"概率论基础","en":"PROBABILITY FOUNDATIONS","sub":"随机事件、概率公理化、条件概率","desc":"概率是不确定性的数学语言。本章从古典概型出发，建立概率的公理化定义，讨论条件概率、独立性与全概率公式。","sections":[
      {"name":"1.1 概率公理","color":"#2563eb","desc":"柯尔莫哥洛夫公理","items":[
        item("la-k1-1","概率公理",["def","thm"],"非负性、规范性、可列可加性。","<p><strong>定义</strong>　概率 $P$ 是样本空间 $\\Omega$ 上事件域到 $[0,1]$ 的映射，满足：$P(A)\\ge0$，$P(\\Omega)=1$，对互斥事件 $P(\\bigcup A_i)=\\sum P(A_i)$。</p>"),
        item("la-k1-2","条件概率与独立性",["def","thm"],"$P(A|B)=P(AB)/P(B)$，独立 $P(AB)=P(A)P(B)$。","<p>全概率公式：$P(B)=\\sum P(A_i)P(B|A_i)$。贝叶斯公式：$P(A_i|B)=\\frac{P(A_i)P(B|A_i)}{P(B)}$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"随机变量与分布","en":"RANDOM VARIABLES","sub":"分布函数、常见分布","desc":"随机变量将随机事件数值化。本章讨论离散型与连续型随机变量及其分布。","sections":[
      {"name":"2.1 离散型分布","color":"#7c3aed","desc":"二项、泊松、几何","items":[
        item("la-k2-1","二项分布",["def","thm"],"$X\\sim B(n,p)$，$P(X=k)=C_n^k p^k(1-p)^{n-k}$。","<p>$n$ 次独立伯努利试验中成功次数。期望 $np$，方差 $np(1-p)$。</p>"),
        item("la-k2-2","泊松分布",["def","thm"],"$P(X=k)=\\frac{\\lambda^k}{k!}e^{-\\lambda}$，$E(X)=\\lambda$。","<p>稀有事件计数模型。当 $n$ 大 $p$ 小时，$B(n,p)\\approx P(np)$。</p>"),
      ]},
      {"name":"2.2 连续型分布","color":"#0f766e","desc":"均匀、指数、正态","items":[
        item("la-k2-3","正态分布",["def","thm","app"],"$f(x)=\\frac1{\\sqrt{2\\pi}\\sigma}e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$。","<p>$X\\sim N(\\mu,\\sigma^2)$，标准化 $Z=(X-\\mu)/\\sigma\\sim N(0,1)$。中心极限定理使正态分布无处不在。</p>"),
        item("la-k2-4","指数分布",["def","thm"],"$f(x)=\\lambda e^{-\\lambda x}(x>0)$，无记忆性。","<p>等待时间模型。$P(X>s+t|X>s)=P(X>t)$。期望 $1/\\lambda$。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"数字特征","en":"MOMENTS","sub":"期望、方差、协方差、矩","desc":"数字特征概括分布的关键信息：中心位置、离散程度、相关关系。","sections":[
      {"name":"3.1 期望与方差","color":"#c2410c","desc":"均值与波动","items":[
        item("la-k3-1","数学期望",["def","thm"],"$E(X)=\\int x f(x)dx$，线性性 $E(aX+b)=aE(X)+b$。","<p>期望即加权平均。对函数 $g(X)$，$E[g(X)]=\\int g(x)f(x)dx$。</p>"),
        item("la-k3-2","方差",["def","thm"],"$D(X)=E[(X-EX)^2]=E(X^2)-(EX)^2$。","<p>方差刻画离散程度。$D(aX+b)=a^2D(X)$。标准差 $\\sigma=\\sqrt{D(X)}$。</p>"),
      ]},
      {"name":"3.2 协方差与相关系数","color":"#7c3aed","desc":"两个变量的线性关系","items":[
        item("la-k3-3","相关系数",["def","thm"],"$\\rho=\\frac{\\text{Cov}(X,Y)}{\\sigma_X\\sigma_Y}$，$|\\rho|\\le1$。","<p>$\\text{Cov}(X,Y)=E(XY)-E(X)E(Y)$。$\\rho=\\pm1$ 表示完全线性相关。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"数理统计","en":"MATHEMATICAL STATISTICS","sub":"抽样分布、参数估计、假设检验","desc":"数理统计从样本推断总体。本章覆盖参数估计与假设检验。","sections":[
      {"name":"4.1 参数估计","color":"#2563eb","desc":"点估计与区间估计","items":[
        item("la-k4-1","矩估计与极大似然",["def","der"],"矩估计用样本矩代替总体矩；MLE 最大化似然函数。","<p>极大似然估计：$\\hat\\theta=\\arg\\max L(\\theta)=\\arg\\max\\prod f(x_i;\\theta)$。</p>"),
      ]},
      {"name":"4.2 假设检验","color":"#0f766e","desc":"显著性检验","items":[
        item("la-k4-2","假设检验",["def","thm"],"原假设 $H_0$ vs 备择 $H_1$，$p$ 值判断。","<p>第一类错误（弃真）概率为显著性水平 $\\alpha$。当 $p<\\alpha$ 拒绝 $H_0$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 4. 群论 group-theory
# ============================================================
SUBJECTS.append({
  "filename":"group-theory.html",
  "title":"群论",
  "eyebrow":"GROUP THEORY",
  "subtitle":"群的定义 · 子群 · 同态 · 表示论 · 对称性",
  "meta_desc":"群论知识体系：群的定义、子群、同态、表示论、对称性",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"群的基本概念","en":"GROUPS","sub":"群公理、子群、陪集","desc":"群是描述对称性的代数结构。本章建立群的公理体系，讨论子群、陪集与拉格朗日定理。","sections":[
      {"name":"1.1 群公理","color":"#2563eb","desc":"封闭性、结合律、单位元、逆元","items":[
        item("la-k1-1","群的定义",["def","exa"],"$(G,\\cdot)$ 满足封闭、结合、单位元、逆元。","<p><strong>定义</strong>　群 $G$ 是一个集合配以二元运算 $\\cdot$，满足：封闭性、结合律、存在单位元 $e$、每个元素有逆元 $g^{-1}$。</p><p>例子：整数加法群 $\\mathbb{Z}$，$n$ 阶循环群 $\\mathbb{Z}_n$，对称群 $S_n$。</p>"),
        item("la-k1-2","子群与陪集",["def","thm"],"$H\\le G$，左陪集 $gH=\\{gh|h\\in H\\}$。","<p>子群对运算封闭且含逆元。拉格朗日定理：有限群 $|G|=[G:H]\\cdot|H|$，子群阶整除群阶。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"同态与正规子群","en":"HOMOMORPHISMS","sub":"群同态、商群、同构定理","desc":"同态保持群运算。正规子群使商群成为群，同构定理揭示群的结构。","sections":[
      {"name":"2.1 同态","color":"#7c3aed","desc":"保持运算的映射","items":[
        item("la-k2-1","群同态",["def","thm"],"$\\phi(ab)=\\phi(a)\\phi(b)$，核 $\\ker\\phi$，像 $\\text{Im}\\phi$。","<p>同构第一定理：$G/\\ker\\phi\\cong\\text{Im}\\phi$。核是正规子群。</p>"),
        item("la-k2-2","正规子群与商群",["def","thm"],"$N\\triangleleft G$ 若 $gNg^{-1}=N$，商群 $G/N$。","<p>正规子群的左陪集与右陪集重合，可定义商群乘法 $(aN)(bN)=abN$。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"群作用与表示","en":"ACTIONS & REPRESENTATIONS","sub":"群作用、轨道、表示论","desc":"群通过作用于集合来体现对称性。表示论将群元素映射为矩阵。","sections":[
      {"name":"3.1 群作用","color":"#0f766e","desc":"置换表示","items":[
        item("la-k3-1","群作用",["def","thm"],"$G\\times X\\to X$，轨道-稳定化子定理。","<p>轨道 $\\mathcal{O}_x=\\{g\\cdot x|g\\in G\\}$，稳定化子 $G_x=\\{g|g\\cdot x=x\\}$。$|\\mathcal{O}_x|=[G:G_x]$。</p>"),
      ]},
      {"name":"3.2 表示论","color":"#c2410c","desc":"线性表示、特征标","items":[
        item("la-k3-2","群表示",["def","thm"],"$\\rho:G\\to GL(V)$，特征标 $\\chi(g)=\\text{tr}\\rho(g)$。","<p>不可约表示是表示的基本砖块。特征标正交关系：$\\frac1{|G|}\\sum_g\\chi_i(g)\\overline{\\chi_j(g)}=\\delta_{ij}$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 5. 数学物理方法 mathematical-methods
# ============================================================
SUBJECTS.append({
  "filename":"mathematical-methods.html",
  "title":"数学物理方法",
  "eyebrow":"MATHEMATICAL METHODS",
  "subtitle":"复变函数 · 积分变换 · 偏微分方程 · 特殊函数",
  "meta_desc":"数学物理方法知识体系：复变函数、积分变换、偏微分方程、特殊函数",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"复变函数","en":"COMPLEX ANALYSIS","sub":"解析函数、复积分、留数","desc":"复变函数是物理中强大的计算工具。本章讨论解析性、柯西定理与留数计算。","sections":[
      {"name":"1.1 解析函数","color":"#2563eb","desc":"柯西-黎曼条件","items":[
        item("la-k1-1","解析函数",["def","thm"],"$u_x=v_y$，$u_y=-v_x$，解析 $\\iff$ 可微且 C-R 条件。","<p>$f(z)=u(x,y)+iv(x,y)$ 在区域内可微 $\\iff$ $u,v$ 可微且满足 C-R 方程。解析函数无限次可微。</p>"),
        item("la-k1-2","柯西积分公式",["thm"],"$f^{(n)}(z_0)=\\frac{n!}{2\\pi i}\\oint_C\\frac{f(z)}{(z-z_0)^{n+1}}dz$。","<p>若 $f$ 在围道 $C$ 内解析，则 $f(z_0)=\\frac1{2\\pi i}\\oint\\frac{f(z)}{z-z_0}dz$。解析函数由边界值完全确定。</p>"),
      ]},
      {"name":"1.2 留数定理","color":"#7c3aed","desc":"奇点与留数计算","items":[
        item("la-k1-3","留数定理",["thm","app"],"$\\oint_C f(z)dz=2\\pi i\\sum\\text{Res}(f,a_k)$。","<p>一阶极点留数：$\\text{Res}(f,a)=\\lim_{z\\to a}(z-a)f(z)$。留数定理可计算大量实积分。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"积分变换","en":"INTEGRAL TRANSFORMS","sub":"傅里叶、拉普拉斯变换","desc":"积分变换将微分方程化为代数方程，是求解 PDE 的利器。","sections":[
      {"name":"2.1 傅里叶变换","color":"#0f766e","desc":"频域分析","items":[
        item("la-k2-1","傅里叶变换",["def","thm"],"$\\tilde f(k)=\\int_{-\\infty}^\\infty f(x)e^{-ikx}dx$。","<p>逆变换：$f(x)=\\frac1{2\\pi}\\int\\tilde f(k)e^{ikx}dk$。微分性质：$\\mathcal{F}[f']=ik\\tilde f$。</p>"),
        item("la-k2-2","卷积定理",["thm"],"$\\mathcal{F}[f*g]=\\tilde f\\cdot\\tilde g$。","<p>卷积 $(f*g)(x)=\\int f(x-y)g(y)dy$。时域卷积对应频域乘积。</p>"),
      ]},
      {"name":"2.2 拉普拉斯变换","color":"#c2410c","desc":"初值问题求解","items":[
        item("la-k2-3","拉普拉斯变换",["def","app"],"$F(s)=\\int_0^\\infty f(t)e^{-st}dt$。","<p>微分性质：$\\mathcal{L}[f']=sF(s)-f(0)$。将 ODE 初值问题化为代数方程。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"偏微分方程","en":"PDEs","sub":"分离变量、波动方程、热方程","desc":"三类典型方程：波动、热传导、拉普拉斯方程，用分离变量法求解。","sections":[
      {"name":"3.1 分离变量法","color":"#2563eb","desc":"将 PDE 化为 ODE","items":[
        item("la-k3-1","分离变量",["def","der"],"设 $u(x,t)=X(x)T(t)$，代入 PDE 分离出本征值问题。","<p>以波动方程 $u_{tt}=a^2u_{xx}$ 为例，代入得 $T''/a^2T=X''/X=-\\lambda$，分别求解常微分方程。</p>"),
        item("la-k3-2","本征函数展开",["thm","app"],"解为 $\\sum C_n\\sin\\frac{n\\pi x}{L}\\cos\\frac{n\\pi at}{L}$。","<p>利用初始条件确定系数 $C_n$，即傅里叶正弦展开。</p>"),
      ]},
      {"name":"3.2 格林函数","color":"#7c3aed","desc":"点源响应","items":[
        item("la-k3-3","格林函数",["def","thm"],"$LG(x,x')=\\delta(x-x')$，解为 $\\int Gf\\,dx'$。","<p>格林函数是算子 $L$ 在点源 $\\delta$ 下的响应。非齐次方程 $Lu=f$ 的解由卷积给出。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 6. 特殊函数 special-functions
# ============================================================
SUBJECTS.append({
  "filename":"special-functions.html",
  "title":"特殊函数",
  "eyebrow":"SPECIAL FUNCTIONS",
  "subtitle":"勒让德 · 贝塞尔 · 球谐函数 · 伽马函数 · 椭圆积分",
  "meta_desc":"特殊函数知识体系：勒让德、贝塞尔、球谐函数、伽马函数、椭圆积分",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"勒让德函数","en":"LEGENDRE","sub":"勒让德方程、多项式、递推","desc":"勒让德多项式出现在球坐标拉普拉斯方程中。本章讨论其生成函数、正交性与递推关系。","sections":[
      {"name":"1.1 勒让德多项式","color":"#2563eb","desc":"罗德里格斯公式与生成函数","items":[
        item("la-k1-1","勒让德多项式",["def","thm"],"$P_n(x)=\\frac1{2^n n!}\\frac{d^n}{dx^n}(x^2-1)^n$。","<p>满足 $(1-x^2)y''-2xy'+n(n+1)y=0$。前几例：$P_0=1$，$P_1=x$，$P_2=\\frac12(3x^2-1)$。</p>"),
        item("la-k1-2","正交归一",["thm"],"$\\int_{-1}^1 P_mP_n dx=\\frac{2}{2n+1}\\delta_{mn}$。","<p>勒让德多项式在 $[-1,1]$ 上正交，可展开任意平方可积函数。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"贝塞尔函数","en":"BESSEL","sub":"贝塞尔方程、递推、渐近","desc":"贝塞尔函数在柱坐标中出现，描述径向振荡。本章讨论第一类、第二类贝塞尔函数及其性质。","sections":[
      {"name":"2.1 贝塞尔函数","color":"#7c3aed","desc":"级数解与递推","items":[
        item("la-k2-1","第一类贝塞尔函数",["def","thm"],"$J_n(x)=\\sum_{k=0}^\\infty\\frac{(-1)^k}{k!(k+n)!}\\left(\\frac x2\\right)^{2k+n}$。","<p>满足 $x^2y''+xy'+(x^2-n^2)y=0$。递推：$J_{n-1}+J_{n+1}=\\frac{2n}{x}J_n$。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"球谐函数与伽马","en":"SPHERICAL HARMONICS","sub":"球谐函数、伽马函数","desc":"球谐函数是球面上的正交基，伽马函数是阶乘的解析延拓。","sections":[
      {"name":"3.1 球谐函数","color":"#0f766e","desc":"角向本征函数","items":[
        item("la-k3-1","球谐函数",["def","thm"],"$Y_l^m(\\theta,\\phi)=N_{lm}P_l^m(\\cos\\theta)e^{im\\phi}$。","<p>是角动量 $L^2,L_z$ 的共同本征函数：$L^2Y_l^m=l(l+1)Y_l^m$，$L_zY_l^m=mY_l^m$。正交归一 $\\int Y_{l'}^*{}^{m'}Y_l^m d\\Omega=\\delta_{ll'}\\delta_{mm'}$。</p>"),
      ]},
      {"name":"3.2 伽马函数","color":"#c2410c","desc":"阶乘的延拓","items":[
        item("la-k3-2","伽马函数",["def","thm"],"$\\Gamma(z)=\\int_0^\\infty t^{z-1}e^{-t}dt$，$\\Gamma(n+1)=n!$。","<p>性质：$\\Gamma(z+1)=z\\Gamma(z)$，$\\Gamma(1/2)=\\sqrt\\pi$，余元公式 $\\Gamma(z)\\Gamma(1-z)=\\pi/\\sin\\pi z$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 7. 矢量分析 vector-analysis
# ============================================================
SUBJECTS.append({
  "filename":"vector-analysis.html",
  "title":"矢量分析",
  "eyebrow":"VECTOR CALCULUS",
  "subtitle":"梯度 · 散度 · 旋度 · 高斯定理 · 斯托克斯定理",
  "meta_desc":"矢量分析知识体系：梯度、散度、旋度、高斯定理、斯托克斯定理",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"矢量场微分","en":"VECTOR DIFFERENTIAL","sub":"梯度、散度、旋度","desc":"矢量分析研究标量场与矢量场的微分运算。梯度、散度、旋度是三个基本算子。","sections":[
      {"name":"1.1 梯度","color":"#2563eb","desc":"标量场的方向导数","items":[
        item("la-k1-1","梯度",["def","thm"],"$\\nabla\\phi=(\\partial_x\\phi,\\partial_y\\phi,\\partial_z\\phi)$。","<p>梯度指向标量场增长最快的方向，其模为最大方向导数。$\\nabla\\phi\\cdot\\hat{n}$ 是沿 $\\hat{n}$ 方向的方向导数。</p>"),
      ]},
      {"name":"1.2 散度与旋度","color":"#7c3aed","desc":"矢量场的源与涡","items":[
        item("la-k1-2","散度",["def","thm"],"$\\nabla\\cdot\\boldsymbol{A}=\\partial_x A_x+\\partial_y A_y+\\partial_z A_z$。","<p>散度描述矢量场的“源”强度。$\\nabla\\cdot\\boldsymbol{A}>0$ 为源，$<0$ 为汇。</p>"),
        item("la-k1-3","旋度",["def","thm"],"$\\nabla\\times\\boldsymbol{A}$，描述场的旋转。","<p>旋度方向沿旋转轴，模为旋转强度。$\\nabla\\times\\boldsymbol{A}=0$ 的场为保守场，可表为标量梯度。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"积分定理","en":"INTEGRAL THEOREMS","sub":"高斯、斯托克斯、格林","desc":"积分定理将场的体积分、面积分、线积分联系起来，是电磁场理论的基础。","sections":[
      {"name":"2.1 高斯散度定理","color":"#0f766e","desc":"体积分与面积分","items":[
        item("la-k2-1","高斯定理",["thm"],"$\\int_V\\nabla\\cdot\\boldsymbol{A}\\,dV=\\oint_S\\boldsymbol{A}\\cdot d\\boldsymbol{S}$。","<p>矢量场的散度在体积内的积分等于其穿过闭合曲面的通量。这是电磁场高斯定律的数学基础。</p>"),
      ]},
      {"name":"2.2 斯托克斯定理","color":"#c2410c","desc":"面积分与线积分","items":[
        item("la-k2-2","斯托克斯定理",["thm"],"$\\int_S(\\nabla\\times\\boldsymbol{A})\\cdot d\\boldsymbol{S}=\\oint_C\\boldsymbol{A}\\cdot d\\boldsymbol{l}$。","<p>旋度穿过曲面的通量等于矢量沿闭合曲线的环量。法拉第定律的数学基础。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 8. 计算物理 computational-physics
# ============================================================
SUBJECTS.append({
  "filename":"computational-physics.html",
  "title":"计算物理",
  "eyebrow":"COMPUTATIONAL PHYSICS",
  "subtitle":"数值微分 · 数值积分 · 线性方程组 · ODE 求解 · 蒙特卡洛",
  "meta_desc":"计算物理知识体系：数值微分、数值积分、线性方程组、ODE求解、蒙特卡洛",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"数值微分与积分","en":"NUMERICAL CALCULUS","sub":"差分、求积公式","desc":"用离散近似连续运算。本章介绍有限差分与牛顿-科茨求积公式。","sections":[
      {"name":"1.1 数值微分","color":"#2563eb","desc":"有限差分","items":[
        item("la-k1-1","有限差分",["def","der"],"前向 $f'(x)\\approx[f(x+h)-f(x)]/h$，中心差分二阶精度。","<p>中心差分：$f'(x)\\approx\\frac{f(x+h)-f(x-h)}{2h}+O(h^2)$。截断误差与舍入误差需平衡。</p>"),
      ]},
      {"name":"1.2 数值积分","color":"#7c3aed","desc":"梯形、辛普森","items":[
        item("la-k1-2","辛普森公式",["thm","der"],"$\\int_a^b f\\,dx\\approx\\frac{h}{3}[f_0+4f_1+2f_2+\\cdots+4f_{n-1}+f_n]$。","<p>梯形公式 $O(h^2)$，辛普森公式 $O(h^4)$。高斯求积用最优节点达更高精度。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"线性方程组与矩阵","en":"LINEAR SYSTEMS","sub":"直接法与迭代法","desc":"求解 $A\\boldsymbol{x}=\\boldsymbol{b}$。直接法（高斯消元、LU）与迭代法（雅可比、共轭梯度）。","sections":[
      {"name":"2.1 直接法","color":"#0f766e","desc":"高斯消元与 LU 分解","items":[
        item("la-k2-1","高斯消元",["def","der"],"行变换化上三角，回代求解。","<p>LU 分解将 $A=LU$，则解 $Ly=b$ 与 $Ux=y$。复杂度 $O(n^3)$。</p>"),
      ]},
      {"name":"2.2 迭代法","color":"#c2410c","desc":"雅可比、高斯-赛德尔、CG","items":[
        item("la-k2-2","共轭梯度法",["thm","app"],"适用于对称正定矩阵，$n$ 步内精确收敛。","<p>CG 法利用 Krylov 子空间，对大型稀疏矩阵效率远高于直接法。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"ODE 与蒙特卡洛","en":"ODE & MONTE CARLO","sub":"龙格-库塔、随机采样","desc":"常微分方程数值求解与蒙特卡洛随机方法。","sections":[
      {"name":"3.1 ODE 求解","color":"#2563eb","desc":"欧拉、龙格-库塔","items":[
        item("la-k3-1","四阶龙格-库塔",["def","thm"],"RK4 精度 $O(h^4)$，每步计算 4 个斜率。","<p>$y_{n+1}=y_n+\\frac h6(k_1+2k_2+2k_3+k_4)$，$k_i$ 为各点斜率。经典且稳健。</p>"),
      ]},
      {"name":"3.2 蒙特卡洛","color":"#7c3aed","desc":"随机采样积分","items":[
        item("la-k3-2","蒙特卡洛积分",["def","thm","app"],"$\\int f\\,dx\\approx\\frac1N\\sum f(x_i)$，误差 $O(N^{-1/2})$。","<p>高维积分中蒙特卡洛优于网格法。Metropolis-Hastings 与 MCMC 可采样复杂分布。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 9. 理论力学 theoretical-mechanics
# ============================================================
SUBJECTS.append({
  "filename":"theoretical-mechanics.html",
  "title":"理论力学",
  "eyebrow":"THEORETICAL MECHANICS",
  "subtitle":"拉格朗日方程 · 哈密顿原理 · 正则方程 · 刚体 · 微振动 · 散射",
  "meta_desc":"理论力学知识体系：约束与广义坐标、拉格朗日方程、哈密顿原理、正则方程、泊松括号、刚体转动、微振动、散射理论",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"拉格朗日力学","en":"LAGRANGIAN MECHANICS","sub":"广义坐标、拉氏方程、变分原理","desc":"从牛顿力学到拉格朗日力学，用能量（动能减势能）而非力描述系统运动。广义坐标的引入使约束力自动消去。","sections":[
      {"name":"1.1 约束与广义坐标","color":"#2563eb","desc":"自由度、完整约束","items":[
        item("la-k1-1","约束的分类",["def"],"完整约束 $f(q_1,\\dots,q_n,t)=0$；非完整约束含速度不可积。","<p><strong>完整约束</strong>可表示为坐标与时间的代数方程，减少自由度。<strong>非完整约束</strong>（如 rolling without slipping）含速度项且不可积，需用拉格朗日乘子法。约束数为 $k$，自由度 $s=3N-k$。</p>"),
        item("la-k1-2","广义坐标",["def","app"],"$q_1,\\dots,q_s$ 为独立描述系统位形的 $s$ 个变量。","<p>广义坐标可以是角度、长度或其他合适变量。笛卡尔坐标 $\\boldsymbol r_i=\\boldsymbol r_i(q_1,\\dots,q_s,t)$。选择合适的广义坐标可大幅简化问题。</p>"),
        item("la-k1-3","拉格朗日量",["def","thm"],"$L=T-V$，拉氏方程：$\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_i}-\\frac{\\partial L}{\\partial q_i}=Q_i$。","<p>主动力有势时 $Q_i=0$，得欧拉-拉格朗日方程：</p><div class=\"la-fml\">$$\\frac{d}{dt}\\frac{\\partial L}{\\partial\\dot q_i}-\\frac{\\partial L}{\\partial q_i}=0$$</div><p>$L$ 是 $q,\\dot q,t$ 的函数。此方程对任意广义坐标协变，无需分析约束力。</p>"),
      ]},
      {"name":"1.2 最小作用量原理","color":"#7c3aed","desc":"哈密顿原理、变分法","items":[
        item("la-k1-4","哈密顿原理",["thm","his"],"$\\delta S=0$，作用量 $S=\\int_{t_1}^{t_2} L(q,\\dot q,t)\\,dt$。","<p>真实运动使作用量取极值（变分为零）。这是力学的变分原理表述，比牛顿定律更基本、更普适，可推广到场论。</p><div class=\"la-fml\">$$\\delta S=\\delta\\int_{t_1}^{t_2}L\\,dt=0$$</div>"),
        item("la-k1-5","循环坐标与守恒律",["thm","der"],"若 $\\partial L/\\partial q_i=0$，则 $p_i=\\partial L/\\partial\\dot q_i$ 守恒。","<p>循环坐标（不出现于 $L$ 中的坐标）对应守恒动量。空间均匀性→动量守恒；各向同性→角动量守恒；时间均匀性→能量守恒（诺特定理）。</p>"),
        item("la-k1-6","能量函数",["def","thm"],"$h=\\sum p_i\\dot q_i-L$，当 $\\partial L/\\partial t=0$ 时 $h$ 守恒。","<p>若势能不含速度且变换不显含时间，$h=E=T+V$ 即机械能。能量守恒是时间平移对称性的结果。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"哈密顿力学","en":"HAMILTONIAN MECHANICS","sub":"正则方程、泊松括号、正则变换","desc":"哈密顿力学以广义坐标和广义动量为独立变量，在相空间中描述运动，方程更对称优美。","sections":[
      {"name":"2.1 正则方程","color":"#2563eb","desc":"勒让德变换","items":[
        item("la-k2-1","哈密顿量",["def","thm"],"$H(q,p,t)=\\sum p_i\\dot q_i-L$，正则方程：$\\dot q_i=\\frac{\\partial H}{\\partial p_i}$，$\\dot p_i=-\\frac{\\partial H}{\\partial q_i}$。","<p>通过勒让德变换将 $L(q,\\dot q,t)$ 换为 $H(q,p,t)$。正则方程是 $2s$ 个一阶方程，比拉氏方程（$s$ 个二阶）更对称。$H$ 守恒当且仅当 $\\partial H/\\partial t=0$。</p>"),
        item("la-k2-2","相空间与刘维尔定理",["thm","der"],"相空间体积元不变：$\\sum(\\partial\\dot q_i/\\partial q_i+\\partial\\dot p_i/\\partial p_i)=0$。","<p>刘维尔定理：哈密顿系统的相空间密度沿轨道不变。这是统计力学的基础，也意味着哈密顿流保持相空间体积（不可压缩）。</p>"),
      ]},
      {"name":"2.2 泊松括号","color":"#7c3aed","desc":"运动方程的括号形式","items":[
        item("la-k2-3","泊松括号定义",["def","thm"],"$\\{f,g\\}=\\sum_i\\left(\\frac{\\partial f}{\\partial q_i}\\frac{\\partial g}{\\partial p_i}-\\frac{\\partial f}{\\partial p_i}\\frac{\\partial g}{\\partial q_i}\\right)$。","<p>泊松括号满足反对称性、双线性、雅可比恒等式，构成李代数。任意力学量的时间演化：</p><div class=\"la-fml\">$$\\frac{df}{dt}=\\{f,H\\}+\\frac{\\partial f}{\\partial t}$$</div>"),
        item("la-k2-4","基本泊松括号",["thm","der"],"$\\{q_i,q_j\\}=0$，$\\{p_i,p_j\\}=0$，$\\{q_i,p_j\\}=\\delta_{ij}$。","<p>这些是量子力学正则对易关系 $[\\hat q_i,\\hat p_j]=i\\hbar\\delta_{ij}$ 的经典对应。狄拉克指出：经典泊松括号 → 量子对易子。</p>"),
        item("la-k2-5","正则变换",["def","thm"],"保持正则方程形式的变换 $(q,p)\\to(Q,P)$，满足 $\\sum p_i dq_i-\\sum P_i dQ_i=dF$。","<p>生成函数 $F$ 有四种基本形式。正则变换可简化哈密顿量，是求解力学问题的强大工具（如作用量-角变量）。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"刚体力学","en":"RIGID BODY DYNAMICS","sub":"惯量张量、欧拉方程、陀螺","desc":"刚体是特殊的质点系，内部距离不变。转动用惯量张量和欧拉方程描述。","sections":[
      {"name":"3.1 惯量张量","color":"#2563eb","desc":"转动惯量与惯量主轴","items":[
        item("la-k3-1","惯量张量",["def","thm"],"$I_{ij}=\\int\\rho(r^2\\delta_{ij}-x_ix_j)\\,dV$，对称二阶张量。","<p>刚体转动动能 $T=\\frac12\\sum I_{ij}\\omega_i\\omega_j$。通过正交变换可将 $I_{ij}$ 对角化，得到三个主转动惯量 $I_1,I_2,I_3$ 和惯量主轴。</p>"),
        item("la-k3-2","平行轴定理",["thm","der"],"$I=I_{cm}+Md^2$。","<p>刚体对任意轴的转动惯量等于对过质心平行轴的转动惯量加上 $Md^2$（$d$ 为两轴距离）。用于简化计算。</p>"),
      ]},
      {"name":"3.2 欧拉方程与陀螺","color":"#7c3aed","desc":"定点转动","items":[
        item("la-k3-3","欧拉方程",["def","thm"],"$I_1\\dot\\omega_1-(I_2-I_3)\\omega_2\\omega_3=M_1$（循环置换）。","<p>在惯量主轴坐标系中，刚体定点转动的动力学方程。无外力矩时（$M=0$）欧拉陀螺可解析求解，能量和角动量守恒。</p>"),
        item("la-k3-4","对称陀螺的进动",["thm","app","exa"],"$\\dot\\phi=\\frac{L_z-I_3\\omega_3\\cos\\theta}{I_1\\sin^2\\theta}$。","<p>对称陀螺（$I_1=I_2\\neq I_3$）在重力场中运动：自转轴绕竖直轴进动，同时可能章动。快速自转的陀螺表现为规则进动。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"微振动","en":"SMALL OSCILLATIONS","sub":"简正模、本征频率","desc":"系统在稳定平衡位置附近的小振动可解耦为独立的简正模。","sections":[
      {"name":"4.1 简正模理论","color":"#0f766e","desc":"广义本征值问题","items":[
        item("la-k4-1","简正模方程",["def","thm","der"],"$\\det(K-\\omega^2 M)=0$ 确定本征频率。","<p>小振动时，势能在平衡位置展开 $V=V_0+\\frac12\\sum K_{ij}q_iq_j$，动能 $T=\\frac12\\sum M_{ij}\\dot q_i\\dot q_j$。运动方程 $M\\ddot q+Kq=0$。设 $q=a e^{i\\omega t}$，得广义本征值问题 $(K-\\omega^2 M)a=0$。</p>"),
        item("la-k4-2","简正坐标",["thm","der"],"通过本征向量构造简正坐标 $\\xi$，使 $L=\\sum\\frac12(\\dot\\xi_i^2-\\omega_i^2\\xi_i^2)$。","<p>简正坐标下系统解耦为 $s$ 个独立简谐振子。每个简正模以单一频率振动，是系统的集体模式。</p>"),
      ]},
      {"name":"4.2 耦合振子与非线性","color":"#c2410c","desc":"实例与推广","items":[
        item("la-k4-3","双耦合振子",["exa","app"],"两个弹簧振子耦合后出现对称模与反对称模。","<p>等质量双振子用弹簧耦合：对称模（同相）频率较低，反对称模（反相）频率较高。能量在两振子间周期性转移（拍现象）。</p>"),
        item("la-k4-4","非线性振动",["def","app"],"达芬方程 $\\ddot x+\\omega_0^2 x+\\alpha x^3=f\\cos\\Omega t$。","<p>非线性恢复力导致频率随振幅变化、次谐波/超谐波共振、混沌等现象。摄动法（林德斯泰特-庞加莱）可求近似解。</p>"),
      ]},
    ]},
    {"id":"la-ch5","num":"第五章","title":"散射理论","en":"SCATTERING THEORY","sub":"散射截面、卢瑟福散射","desc":"两体碰撞问题转化为单体等效问题，散射截面是实验可测量。","sections":[
      {"name":"5.1 散射截面","color":"#2563eb","desc":"微分散射截面","items":[
        item("la-k5-1","微分散射截面",["def","thm"],"$\\sigma(\\theta)=\\frac{b}{\\sin\\theta}\\left|\\frac{db}{d\\theta}\\right|$。","<p>瞄准距离 $b$ 与散射角 $\\theta$ 的关系决定截面。总截面 $\\sigma_{tot}=\\int\\sigma(\\theta)\\,d\\Omega$。两体问题约化为约化质量 $\\mu$ 的单体散射。</p>"),
        item("la-k5-2","卢瑟福散射",["exa","his","thm"],"$\\sigma(\\theta)=\\left(\\frac{k}{4E}\\right)^2\\csc^4(\\theta/2)$。","<p>库仑势 $V=k/r$ 的散射。$\\alpha$ 粒子被金核散射的实验验证了原子核式结构模型。小角度截面发散，是长程力的特征。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 10. 流体力学 fluid-mechanics
# ============================================================
SUBJECTS.append({
  "filename":"fluid-mechanics.html",
  "title":"流体力学",
  "eyebrow":"FLUID MECHANICS",
  "subtitle":"连续性方程 · 欧拉方程 · Navier-Stokes · 伯努利 · 势流 · 湍流",
  "meta_desc":"流体力学知识体系：连续性方程、欧拉方程、Navier-Stokes方程、伯努利定理、势流、边界层、湍流",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"流体基本方程","en":"FLUID FUNDAMENTALS","sub":"连续性、欧拉、NS","desc":"流体作为连续介质，其运动由质量、动量、能量守恒方程描述。本章建立流体力学的基本方程组。","sections":[
      {"name":"1.1 连续性方程","color":"#2563eb","desc":"质量守恒","items":[
        item("la-k1-1","连续性方程",["def","thm"],"$\\frac{\\partial\\rho}{\\partial t}+\\nabla\\cdot(\\rho\\boldsymbol v)=0$。","<p>质量守恒的微分形式。对控制体 $V$，流入质量等于质量增加率。不可压缩流体 $\\rho=$ 常数，方程简化为 $\\nabla\\cdot\\boldsymbol v=0$（速度场无散）。</p>"),
        item("la-k1-2","物质导数",["def","thm"],"$\\frac{D}{Dt}=\\frac{\\partial}{\\partial t}+\\boldsymbol v\\cdot\\nabla$。","<p>物质导数（随体导数）= 局部导数 + 对流导数。描述随流体微团运动时物理量的变化率，是拉格朗日观点与欧拉观点的桥梁。</p>"),
      ]},
      {"name":"1.2 运动方程","color":"#7c3aed","desc":"欧拉方程与NS方程","items":[
        item("la-k1-3","欧拉方程",["def","thm"],"$\\rho\\frac{D\\boldsymbol v}{Dt}=-\\nabla p+\\rho\\boldsymbol f$。","<p>理想流体（无粘）的动量方程。展开为：$\\rho(\\partial_t\\boldsymbol v+\\boldsymbol v\\cdot\\nabla\\boldsymbol v)=-\\nabla p+\\rho\\boldsymbol f$。对流项 $\\boldsymbol v\\cdot\\nabla\\boldsymbol v$ 使方程非线性。</p>"),
        item("la-k1-4","Navier-Stokes 方程",["def","thm"],"$\\rho\\frac{D\\boldsymbol v}{Dt}=-\\nabla p+\\mu\\nabla^2\\boldsymbol v+\\rho\\boldsymbol f$。","<p>引入粘性应力 $\\mu\\nabla^2\\boldsymbol v$（牛顿流体）。NS 方程是流体力学的核心。其解析解极少，三维光滑解的存在性是千禧年难题之一。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"伯努利方程与势流","en":"BERNOULLI & POTENTIAL FLOW","sub":"能量积分、无旋流动","desc":"伯努利方程是定常无粘流的能量积分；势流理论给出无旋流动的解析解法。","sections":[
      {"name":"2.1 伯努利方程","color":"#0f766e","desc":"沿流线守恒","items":[
        item("la-k2-1","伯努利方程",["thm","der"],"$\\frac12\\rho v^2+p+\\rho gz=\\text{const}$（沿流线）。","<p>定常、无粘、不可压缩、沿流线成立。三项分别为动能、压强能、势能。应用：文丘里管、皮托管、喷雾器。</p><div class=\"la-fml\">$$\\frac{v^2}{2g}+\\frac{p}{\\rho g}+z=H$$</div>"),
        item("la-k2-2","托里拆利定律",["exa","app"],"小孔出流速度 $v=\\sqrt{2gh}$。","<p>伯努利方程的直接应用。大容器液面下 $h$ 处小孔出流速度等于自由下落 $h$ 的速度。实际有收缩系数和流量系数修正。</p>"),
      ]},
      {"name":"2.2 势流理论","color":"#c2410c","desc":"无旋流动、速度势","items":[
        item("la-k2-3","速度势与流函数","def","$\\boldsymbol v=\\nabla\\phi$，$\\nabla^2\\phi=0$（拉普拉斯方程）。","<p>无旋流动 $\\nabla\\times\\boldsymbol v=0$ 时存在速度势 $\\phi$。二维流动还可引入流函数 $\\psi$，与 $\\phi$ 构成共轭调和函数（复变函数方法）。</p>"),
        item("la-k2-4","基本解与叠加","thm","点源、点涡、偶极子等基本解可叠加构造复杂流动。","<p>拉普拉斯方程线性，基本解可叠加。均匀流+偶极子=绕圆柱无环量流动（达朗贝尔佯谬：阻力为零）。加环量后产生升力（库塔-儒可夫斯基定理）。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"边界层与湍流","en":"BOUNDARY LAYER & TURBULENCE","sub":"雷诺数、湍流模型","desc":"粘性在边界层内起重要作用；高雷诺数时流动转捩为湍流。","sections":[
      {"name":"3.1 边界层理论","color":"#2563eb","desc":"普朗特边界层","items":[
        item("la-k3-1","边界层厚度",["def","thm"],"$\\delta\\sim\\sqrt{\\nu x/U_0}$（层流），$\\delta\\sim x(Re_x)^{-1/5}$（湍流）。","<p>高雷诺数时粘性仅在物面附近薄边界层内重要。层内速度从物面零值迅速增至外流值。边界层方程由普朗特提出，是NS方程的近似。</p>"),
        item("la-k3-2","边界层分离","app","逆压梯度导致边界层分离，形成尾涡区。","<p>当 $dp/dx>0$（逆压梯度），流体动能不足以克服压强升高，边界层脱离物面。分离后阻力剧增（压差阻力），升力下降（失速）。</p>"),
      ]},
      {"name":"3.2 湍流","color":"#7c3aed","desc":"雷诺数与湍流模型","items":[
        item("la-k3-3","雷诺数",["def","thm","app"],"$Re=\\frac{\\rho vL}{\\mu}=\\frac{\\text{惯性力}}{\\text{粘性力}}$。","<p>雷诺数是流动相似的关键参数。$Re<Re_c$ 层流，$Re>Re_c$ 湍流。圆管 $Re_c\\approx2300$，平板 $Re_c\\approx5\\times10^5$。湍流需用雷诺平均（RANS）、大涡模拟（LES）或直接数值模拟（DNS）。</p>"),
        item("la-k3-4","雷诺平均NS方程","thm","$\\overline{\\rho\\frac{D\\bar v_i}{Dt}}=-\\partial_i\\bar p+\\mu\\nabla^2\\bar v_i-\\partial_j(\\overline{\\rho v_i'v_j'})$。","<p>将速度分解为平均加脉动，对NS方程取平均得RANS。多出的雷诺应力项 $-\\rho\\overline{v_i'v_j'}$ 需用湍流模型封闭（$k-\\varepsilon$、SST 等）。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 11. 固体力学 solid-mechanics
# ============================================================
SUBJECTS.append({
  "filename":"solid-mechanics.html",
  "title":"固体力学",
  "eyebrow":"SOLID MECHANICS",
  "subtitle":"应力 · 应变 · 胡克定律 · 梁弯曲 · 本构关系 · 有限元",
  "meta_desc":"固体力学知识体系：应力张量、应变张量、胡克定律、梁弯曲理论、本构关系、有限元方法",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"应力与应变","en":"STRESS & STRAIN","sub":"张量描述、主应力","desc":"固体在外力下的变形用应力张量和应变张量描述，它们是二阶对称张量。","sections":[
      {"name":"1.1 应力张量","color":"#2563eb","desc":"面力与应力、主应力","items":[
        item("la-k1-1","应力张量",["def","thm"],"$\\sigma_{ij}$ 为二阶对称张量，$\\sigma_{ij}=\\sigma_{ji}$。","<p>应力 $\\sigma_{ij}$ 表示 $j$ 方向面元单位面积上 $i$ 方向的力。正应力 $\\sigma_{ii}$，剪应力 $\\sigma_{ij}(i\\neq j)$。平衡方程：$\\partial_j\\sigma_{ij}+f_i=0$。</p>"),
        item("la-k1-2","主应力与应力不变量",["thm","der"],"$\\det(\\sigma_{ij}-\\sigma\\delta_{ij})=0$ 解出主应力 $\\sigma_1,\\sigma_2,\\sigma_3$。","<p>应力张量可通过正交变换对角化，得到三个主应力（无剪应力方向）。三个应力不变量 $I_1=\\sigma_{kk}$，$I_2=\\frac12(\\sigma_{ii}\\sigma_{jj}-\\sigma_{ij}\\sigma_{ij})$，$I_3=\\det\\sigma$ 与坐标选择无关。</p>"),
      ]},
      {"name":"1.2 应变张量","color":"#7c3aed","desc":"小变形、应变协调","items":[
        item("la-k1-3","应变张量",["def","thm"],"$\\varepsilon_{ij}=\\frac12(\\partial_i u_j+\\partial_j u_i)$。","<p>小变形下应变是位移梯度的对称部分。正应变 $\\varepsilon_{ii}$，剪应变 $\\varepsilon_{ij}(i\\neq j)$。体积应变 $\\varepsilon_{kk}=\\nabla\\cdot\\boldsymbol u$（膨胀率）。转动张量 $\\omega_{ij}=\\frac12(\\partial_i u_j-\\partial_j u_i)$。</p>"),
        item("la-k1-4","应变协调方程",["thm","der"],"$\\partial_{kl}\\varepsilon_{ij}+\\partial_{ij}\\varepsilon_{kl}-\\partial_{ik}\\varepsilon_{jl}-\\partial_{jl}\\varepsilon_{ik}=0$。","<p>六个应变分量由三个位移分量导出，需满足协调方程（Saint-Venant 条件），否则对应位移场不存在。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"本构关系","en":"CONSTITUTIVE RELATIONS","sub":"胡克定律、弹性常数","desc":"应力与应变的关系由本构方程描述。线弹性体满足广义胡克定律。","sections":[
      {"name":"2.1 广义胡克定律","color":"#0f766e","desc":"各向同性弹性","items":[
        item("la-k2-1","广义胡克定律",["def","thm"],"$\\sigma_{ij}=C_{ijkl}\\varepsilon_{kl}$，各向同性：$\\sigma_{ij}=\\lambda\\varepsilon_{kk}\\delta_{ij}+2\\mu\\varepsilon_{ij}$。","<p>各向同性弹性体仅需两个独立常数：拉梅常数 $\\lambda,\\mu$（$\\mu$ 即剪切模量 $G$）。杨氏模量 $E=\\mu(3\\lambda+2\\mu)/(\\lambda+\\mu)$，泊松比 $\\nu=\\lambda/(2(\\lambda+\\mu))$。体积模量 $K=\\lambda+2\\mu/3$。</p>"),
        item("la-k2-2","应力-应变关系换算",["thm","der"],"$E=2G(1+\\nu)=3K(1-2\\nu)$。","<p>弹性常数之间的关系。$\\nu$ 取值范围 $[-1,0.5]$，$\\nu=0.5$ 为不可压缩。金属 $\\nu\\approx0.3$，橡胶 $\\nu\\approx0.49$。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"梁弯曲理论","en":"BEAM BENDING","sub":"欧拉-伯努利梁","desc":"梁的弯曲是工程结构的基本问题，用欧拉-伯努利梁理论描述。","sections":[
      {"name":"3.1 欧拉-伯努利梁","color":"#2563eb","desc":"梁弯曲微分方程","items":[
        item("la-k3-1","梁弯曲方程",["def","thm"],"$EI\\frac{d^4w}{dx^4}=q(x)$。","<p>小挠度梁的控制方程。$EI$ 为抗弯刚度，$w(x)$ 为挠度，$q(x)$ 为分布载荷。边界条件：简支 $w=M=0$，固支 $w=\\theta=0$，自由 $M=V=0$。</p>"),
        item("la-k3-2","弯曲正应力",["thm","der"],"$\\sigma=-\\frac{My}{I}$，最大应力在离中性轴最远处。","<p>弯曲时正应力沿截面线性分布，中性轴处为零。矩形截面最大应力 $\\sigma_{max}=6M/(bh^2)$。设计梁截面时应增大截面模量 $W=I/y_{max}$。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"有限元方法","en":"FINITE ELEMENT METHOD","sub":"变分原理、离散化","desc":"有限元法将连续体离散为单元，在单元内插值，组装刚度矩阵求解。","sections":[
      {"name":"4.1 有限元原理","color":"#7c3aed","desc":"弱形式与形函数","items":[
        item("la-k4-1","变分原理",["thm","der"],"最小势能原理：$\\delta\\Pi=0$，$\\Pi=U-W$。","<p>总势能 $\\Pi$=应变能 $U$ - 外力功 $W$。真实位移使总势能取极小值。这是有限元法的理论基础，也可由虚功原理导出。</p>"),
        item("la-k4-2","有限元离散",["def","app"],"$\\boldsymbol u=N\\boldsymbol u_e$，组装 $K\\boldsymbol u=\\boldsymbol F$。","<p>单元内位移用形函数 $N$ 插值，节点位移 $\\boldsymbol u_e$ 为未知量。单元刚度矩阵 $K_e=\\int B^T DB\\,dV$，整体刚度矩阵由单元刚度组装。解方程得位移，再求应力。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 12. 计算流体力学 cfd
# ============================================================
SUBJECTS.append({
  "filename":"cfd.html",
  "title":"计算流体力学",
  "eyebrow":"COMPUTATIONAL FLUID DYNAMICS",
  "subtitle":"有限差分 · 有限体积 · 有限元 · 谱方法 · 湍流模型 · 网格生成",
  "meta_desc":"计算流体力学知识体系：有限差分法、有限体积法、有限元法、谱方法、湍流模型、网格生成",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"离散化方法","en":"DISCRETIZATION METHODS","sub":"FDM、FVM、FEM、谱方法","desc":"将 NS 方程在空间和时间上离散为代数方程组。本章介绍四大离散方法。","sections":[
      {"name":"1.1 有限差分法","color":"#2563eb","desc":"导数的差商近似","items":[
        item("la-k1-1","有限差分格式",["def","thm"],"$\\partial_x u\\approx(u_{i+1}-u_{i-1})/(2\\Delta x)$（中心差分）。","<p>FDM 用差商近似偏导数。前向/后向差分一阶精度，中心差分二阶精度。高阶格式（紧致差分、WENO）精度更高但更复杂。需处理边界条件。</p>"),
        item("la-k1-2","有限体积法",["def","thm","app"],"对控制体积分，数值通量 $F_{i+1/2}$ 近似面通量。","<p>FVM 天然满足守恒律，是 CFD 主流方法。关键是数值通量格式：中心格式需人工粘性，迎风格式（Roe、HLLC、AUSM）自动捕捉激波。</p>"),
      ]},
      {"name":"1.2 有限元与谱方法","color":"#7c3aed","desc":"加权余量法","items":[
        item("la-k1-3","有限元法",["def","thm"],"加权余量法，Galerkin 法取权函数=形函数。","<p>FEM 用分片多项式近似解，对非结构网格适应性好。稳定化 FEM（SUPG、Galerkin 最小二乘）可处理对流占优问题。谱元法是高阶 FEM。</p>"),
        item("la-k1-4","谱方法","def","全局光滑基函数（傅里叶、切比雪夫），指数收敛。","<p>谱方法对光滑解有指数收敛精度，但对复杂几何和间断解适应性差。常用于湍流 DNS 和地球物理流体。伪谱法用物理空间计算非线性项，避免卷积。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"时间推进与稳定性","en":"TIME INTEGRATION","sub":"显式、隐式、CFL","desc":"时间离散方法及其稳定性条件。","sections":[
      {"name":"2.1 时间离散格式","color":"#0f766e","desc":"显式与隐式","items":[
        item("la-k2-1","CFL 条件",["def","thm"],"$\\Delta t\\le C\\Delta x/|v|$，显式格式稳定性条件。","<p>CFL 数限制显式格式时间步长。显式格式（Runge-Kutta）每步便宜但步长受 CFL 限制。隐式格式（LU-SGS、Newton-Krylov）可放大步长但每步更贵，适合定常问题。</p>"),
        item("la-k2-2","Runge-Kutta 方法","thm","显式 RK4 四阶精度，每步四次函数求值。","<p>多阶段 RK 方法通过组合多个斜率获得高阶精度。TVD-RK（保总变差衰减）用于双曲型方程，避免振荡。隐式 RK 用于刚性问题。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"湍流模型","en":"TURBULENCE MODELING","sub":"RANS、LES、DNS","desc":"湍流计算需建模。RANS 用雷诺平均，LES 解大涡模小涡，DNS 直接求解。","sections":[
      {"name":"3.1 RANS 模型","color":"#2563eb","desc":"$k-\\varepsilon$、$k-\\omega$、SST","items":[
        item("la-k3-1","$k-\\varepsilon$ 模型",["def","app"],"两方程模型，$\\mu_t=\\rho C_\\mu k^2/\\epsilon$。","<p>工业界最常用的湍流模型。$k$ 为湍动能，$\\varepsilon$ 为耗散率。标准 $k-\\varepsilon$ 对充分发展湍流效果好，对近壁和分离流精度差。RNG $k-\\varepsilon$ 改善了旋转和分离流。</p>"),
        item("la-k3-2","SST $k-\\omega$ 模型",["app"],"近壁用 $k-\\omega$，远场用 $k-\\varepsilon$，混合函数过渡。","<p>SST 模型结合了 $k-\\omega$（近壁好）和 $k-\\varepsilon$（远场好）的优点，对边界层分离和逆压梯度预测准确，是航空航天 CFD 的首选。</p>"),
      ]},
      {"name":"3.2 LES 与 DNS","color":"#7c3aed","desc":"大涡模拟与直接数值模拟","items":[
        item("la-k3-3","大涡模拟（LES）",["def","app"],"直接解大尺度涡，亚格子尺度用 SGS 模型（Smagorinsky、WALE）。","<p>LES 过滤掉小尺度涡，对大涡直接求解。比 RANS 精度高，比 DNS 便宜。壁面附近需壁模（WMLES）或解析壁面（WRLES）。</p>"),
        item("la-k3-4","直接数值模拟（DNS）",["thm"],"不建模，直接求解所有尺度湍流，$\\Delta x<\\eta$（Kolmogorov 尺度）。","<p>DNS 不引入湍流模型，直接求解 NS 方程所有尺度。网格数 $N\\sim Re^{9/4}$，计算量极大，仅用于低雷诺数基础研究和模型验证。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 13. 电磁学 electromagnetism
# ============================================================
SUBJECTS.append({
  "filename":"electromagnetism.html",
  "title":"电磁学",
  "eyebrow":"ELECTROMAGNETISM",
  "subtitle":"静电场 · 静磁场 · 电磁感应 · 麦克斯韦方程组 · 电磁波 · 电路",
  "meta_desc":"电磁学知识体系：静电场、高斯定律、电势、静磁场、安培定律、电磁感应、麦克斯韦方程组、电磁波、交流电路",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"静电场","en":"ELECTROSTATICS","sub":"库仑定律、高斯定律、电势","desc":"静电场由静止电荷产生。本章从库仑定律出发，讨论电场、电势与导体。","sections":[
      {"name":"1.1 电场与高斯定律","color":"#2563eb","desc":"场的通量与源","items":[
        item("la-k1-1","库仑定律",["def","thm"],"$\\boldsymbol F=\\frac{1}{4\\pi\\varepsilon_0}\\frac{q_1q_2}{r^2}\\hat{\\boldsymbol r}$。","<p>点电荷间作用力沿连线方向，同种电荷相斥，异种相吸。电场定义为单位试探电荷受力：$\\boldsymbol E=\\boldsymbol F/q_0$。连续电荷分布：$\\boldsymbol E=\\frac{1}{4\\pi\\varepsilon_0}\\int\\frac{\\rho\\,dV}{r^2}\\hat{\\boldsymbol r}$。</p>"),
        item("la-k1-2","高斯定律",["thm"],"$\\oint\\boldsymbol E\\cdot d\\boldsymbol S=Q_{\\text{enc}}/\\varepsilon_0$，微分形式 $\\nabla\\cdot\\boldsymbol E=\\rho/\\varepsilon_0$。","<p>通过任意闭合曲面的电通量等于面内总电荷除以 $\\varepsilon_0$。高斯定律是静电场的基本方程之一。对球对称、柱对称、面对称电荷分布，可便捷求电场。</p>"),
      ]},
      {"name":"1.2 电势与导体","color":"#7c3aed","desc":"保守场的标量势","items":[
        item("la-k1-3","电势",["def","thm"],"$\\boldsymbol E=-\\nabla\\varphi$，$\\varphi=\\frac{1}{4\\pi\\varepsilon_0}\\int\\frac{\\rho}{r}dV$。","<p>静电场无旋（$\\nabla\\times\\boldsymbol E=0$），可表为电势梯度。电势满足泊松方程 $\\nabla^2\\varphi=-\\rho/\\varepsilon_0$，无电荷区为拉普拉斯方程 $\\nabla^2\\varphi=0$。</p>"),
        item("la-k1-4","导体与电容",["def","app"],"导体内部 $E=0$，表面为等势面；电容 $C=Q/V$。","<p>静电平衡时导体内部电场为零，电荷只分布在表面。电容器储存电荷和能量 $U=\\frac12 CV^2$。平行板电容 $C=\\varepsilon_0 A/d$，加电介质后 $C=\\varepsilon_r\\varepsilon_0 A/d$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"静磁场","en":"MAGNETOSTATICS","sub":"毕奥-萨伐尔、安培定律、磁介质","desc":"稳恒电流产生磁场。本章讨论磁场的计算、安培环路定律与磁介质。","sections":[
      {"name":"2.1 磁场定律","color":"#0f766e","desc":"电流的磁效应","items":[
        item("la-k2-1","毕奥-萨伐尔定律",["def","thm"],"$d\\boldsymbol B=\\frac{\\mu_0}{4\\pi}\\frac{I\\,d\\boldsymbol l\\times\\hat{\\boldsymbol r}}{r^2}$。","<p>电流元 $I\\,d\\boldsymbol l$ 在空间产生的磁场。磁场是无源场：$\\nabla\\cdot\\boldsymbol B=0$（无磁单极）。磁场线闭合，与电场线从正电荷出发不同。</p>"),
        item("la-k2-2","安培定律",["thm"],"$\\oint\\boldsymbol B\\cdot d\\boldsymbol l=\\mu_0 I_{\\text{enc}}$，$\\nabla\\times\\boldsymbol B=\\mu_0\\boldsymbol J$。","<p>磁场沿闭合回路的环量正比于穿过回路的电流。对长直导线 $B=\\mu_0 I/(2\\pi r)$，螺线管内部 $B=\\mu_0 nI$。安培定律仅适用于稳恒电流。</p>"),
      ]},
      {"name":"2.2 磁力与磁介质","color":"#c2410c","desc":"洛伦兹力、磁矩","items":[
        item("la-k2-3","洛伦兹力",["def","thm","app"],"$\\boldsymbol F=q(\\boldsymbol E+\\boldsymbol v\\times\\boldsymbol B)$。","<p>运动电荷在电磁场中受力。磁场力始终与速度垂直，不做功，只改变方向。载流导线受力 $d\\boldsymbol F=I\\,d\\boldsymbol l\\times\\boldsymbol B$。带电粒子在均匀磁场中做圆周运动，回旋频率 $\\omega_c=qB/m$。</p>"),
        item("la-k2-4","磁介质","def","$\\boldsymbol B=\\mu_0(\\boldsymbol H+\\boldsymbol M)$，$\\boldsymbol M$ 为磁化强度。","<p>磁介质磁化后产生附加磁场。顺磁质 $\\chi_m>0$，抗磁质 $\\chi_m<0$，铁磁质 $\\chi_m\\gg0$ 且有磁滞。磁导率 $\\mu=\\mu_0\\mu_r$。铁磁材料有居里温度，高于此温度失去铁磁性。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"电磁感应","en":"ELECTROMAGNETIC INDUCTION","sub":"法拉第定律、自感互感","desc":"变化的磁场产生电场。本章讨论法拉第电磁感应定律及其应用。","sections":[
      {"name":"3.1 法拉第定律","color":"#2563eb","desc":"感应电动势","items":[
        item("la-k3-1","法拉第电磁感应定律",["def","thm"],"$\\mathcal{E}=-\\frac{d\\Phi_B}{dt}$，$\\nabla\\times\\boldsymbol E=-\\partial_t\\boldsymbol B$。","<p>感应电动势等于磁通量变化率的负值。负号体现楞次定律：感应电流方向总是阻碍引起感应的磁通量变化。动生电动势源于洛伦兹力，感生电动势源于涡旋电场。</p>"),
        item("la-k3-2","自感与互感",["def","app"],"$L=\\Phi/I$，$\\mathcal{E}_L=-L\\,dI/dt$；$M=\\Phi_{21}/I_1$。","<p>自感 $L$ 描述回路自身电流变化产生的感应电动势。互感 $M$ 描述两回路间的磁耦合。电感储存能量 $U=\\frac12 LI^2$。变压器利用互感原理工作。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"麦克斯韦方程组与电磁波","en":"MAXWELL & EM WAVES","sub":"位移电流、电磁波","desc":"麦克斯韦引入位移电流，统一电与磁，预言电磁波。","sections":[
      {"name":"4.1 麦克斯韦方程组","color":"#7c3aed","desc":"电磁理论的统一","items":[
        item("la-k4-1","麦克斯韦方程组",["thm","his"],"$\\nabla\\cdot\\boldsymbol E=\\rho/\\varepsilon_0$，$\\nabla\\cdot\\boldsymbol B=0$，$\\nabla\\times\\boldsymbol E=-\\partial_t\\boldsymbol B$，$\\nabla\\times\\boldsymbol B=\\mu_0\\boldsymbol J+\\mu_0\\varepsilon_0\\partial_t\\boldsymbol E$。","<p>麦克斯韦引入位移电流 $\\mu_0\\varepsilon_0\\partial_t\\boldsymbol E$，使方程组自洽并预言电磁波。真空中光速 $c=1/\\sqrt{\\mu_0\\varepsilon_0}\\approx3\\times10^8\\,\\text{m/s}$，光即电磁波。</p>"),
      ]},
      {"name":"4.2 电磁波","color":"#0f766e","desc":"横波、能流","items":[
        item("la-k4-2","平面电磁波",["thm","der"],"$\\boldsymbol E=\\boldsymbol E_0\\cos(\\boldsymbol k\\cdot\\boldsymbol r-\\omega t)$，$\\boldsymbol k\\cdot\\boldsymbol E=0$，$B=E/c$。","<p>电磁波是横波，$\\boldsymbol E\\perp\\boldsymbol B\\perp\\boldsymbol k$。能流由坡印廷矢量 $\\boldsymbol S=\\boldsymbol E\\times\\boldsymbol H$ 描述。电磁波谱：无线电→微波→红外→可见光→紫外→X射线→$\\gamma$ 射线。</p>"),
      ]},
    ]},
    {"id":"la-ch5","num":"第五章","title":"交流电路","en":"AC CIRCUITS","sub":"相量法、谐振","desc":"交流电路用相量法分析，谐振电路有重要应用。","sections":[
      {"name":"5.1 相量法与谐振","color":"#c2410c","desc":"复数阻抗","items":[
        item("la-k5-1","复数阻抗",["def","thm","app"],"$\\tilde Z=\\tilde V/\\tilde I$，$Z_R=R$，$Z_L=j\\omega L$，$Z_C=1/(j\\omega C)$。","<p>正弦稳态电路用相量法，将微分方程化为代数方程。复数阻抗可直接串并联计算。功率因数 $\\cos\\phi$ 反映有功与视在功率之比。</p>"),
        item("la-k5-2","串联谐振",["thm","app"],"$\\omega_0=1/\\sqrt{LC}$ 时阻抗最小，电流最大。","<p>RLC 串联电路在 $\\omega_0$ 处发生谐振，感抗等于容抗，电路呈纯电阻性。品质因数 $Q=\\omega_0 L/R$ 决定谐振曲线锐度。应用：收音机选台、滤波器。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 14. 电动力学 electrodynamics
# ============================================================
SUBJECTS.append({
  "filename":"electrodynamics.html",
  "title":"电动力学",
  "eyebrow":"ELECTRODYNAMICS",
  "subtitle":"电磁场方程 · 势与规范 · 电磁波 · 辐射 · 散射 · 相对论电动力学",
  "meta_desc":"电动力学知识体系：麦克斯韦方程组、势与规范变换、电磁波传播与散射、偶极辐射、相对论协变形式",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"电磁场的普遍规律","en":"ELECTROMAGNETIC FIELD","sub":"能量动量张量、边值问题","desc":"从麦克斯韦方程组出发，讨论电磁场的能量、动量、应力张量及边值问题。","sections":[
      {"name":"1.1 能量与动量","color":"#2563eb","desc":"坡印廷矢量、麦克斯韦应力张量","items":[
        item("la-k1-1","坡印廷矢量与能量守恒",["def","thm"],"$\\boldsymbol S=\\frac1{\\mu_0}\\boldsymbol E\\times\\boldsymbol B$，能量密度 $u=\\frac12(\\varepsilon_0 E^2+B^2/\\mu_0)$。","<p>能量守恒方程：$\\partial_t u+\\nabla\\cdot\\boldsymbol S=-\\boldsymbol J\\cdot\\boldsymbol E$。坡印廷矢量表示能流密度。电磁场具有能量，可与电荷交换能量。</p>"),
        item("la-k1-2","动量与应力张量",["thm","der"],"动量密度 $\\boldsymbol g=\\varepsilon_0\\boldsymbol E\\times\\boldsymbol B$，麦克斯韦应力张量 $T_{ij}=\\varepsilon_0 E_iE_j+\\frac1{\\mu_0}B_iB_j-\\frac12\\delta_{ij}(\\varepsilon_0 E^2+B^2/\\mu_0)$。","<p>电磁场也具有动量。动量守恒：$\\partial_t g_i+\\partial_j T_{ij}=-f_i$。电磁压力和张力由应力张量描述，可解释辐射压和静电力。</p>"),
      ]},
      {"name":"1.2 势与规范","color":"#7c3aed","desc":"矢势与标势、规范变换","items":[
        item("la-k1-3","规范变换",["def","thm"],"$\\boldsymbol B=\\nabla\\times\\boldsymbol A$，$\\boldsymbol E=-\\nabla\\varphi-\\partial_t\\boldsymbol A$。","<p>由于 $\\nabla\\cdot\\boldsymbol B=0$，可引入矢势 $\\boldsymbol A$。规范变换 $\\boldsymbol A\\to\\boldsymbol A+\\nabla\\chi$，$\\varphi\\to\\varphi-\\partial_t\\chi$ 不改变场 $\\boldsymbol E,\\boldsymbol B$。规范自由度是电动力学的重要对称性。</p>"),
        item("la-k1-4","库仑规范与洛伦兹规范",["def","app"],"库仑规范 $\\nabla\\cdot\\boldsymbol A=0$；洛伦兹规范 $\\nabla\\cdot\\boldsymbol A+\\mu_0\\varepsilon_0\\partial_t\\varphi=0$。","<p>库仑规范下 $\\nabla^2\\varphi=-\\rho/\\varepsilon_0$（瞬时库仑势），适合静磁问题。洛伦兹规范下势满足波动方程，适合辐射问题，且具有洛伦兹协变性。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"电磁波的传播与散射","en":"WAVE PROPAGATION & SCATTERING","sub":"平面波、反射折射、色散","desc":"电磁波在介质中的传播、反射、折射和散射。","sections":[
      {"name":"2.1 平面电磁波","color":"#0f766e","desc":"波动方程、横波性","items":[
        item("la-k2-1","平面波解",["def","thm"],"$\\boldsymbol E=\\boldsymbol E_0\\cos(\\boldsymbol k\\cdot\\boldsymbol r-\\omega t)$，$\\boldsymbol k\\cdot\\boldsymbol E=0$，$B=E/c$。","<p>真空中波动方程 $\\nabla^2\\boldsymbol E-\\frac1{c^2}\\partial_t^2\\boldsymbol E=0$。电磁波是横波，$\\boldsymbol E\\perp\\boldsymbol B\\perp\\boldsymbol k$，三者构成右手系。波速 $v=\\omega/k=c$。</p>"),
        item("la-k2-2","反射与折射",["thm","app"],"菲涅尔公式给出反射、折射系数。","<p>电磁波入射到介质界面时发生反射和折射。斯涅尔定律 $n_1\\sin\\theta_1=n_2\\sin\\theta_2$。菲涅尔公式描述 s 偏振和 p 偏振的反射率/透射率。布儒斯特角下 p 偏振反射为零。</p>"),
      ]},
      {"name":"2.2 色散与吸收","color":"#c2410c","desc":"色散介质、趋肤深度","items":[
        item("la-k2-3","色散关系",["def","thm"],"$\\omega=\\omega(k)$，相速 $v_p=\\omega/k$，群速 $v_g=d\\omega/dk$。","<p>介质中折射率随频率变化即色散。正常色散 $dn/d\\omega>0$，反常色散在吸收带附近。群速是能量传播速度。波包在色散介质中展宽。</p>"),
        item("la-k2-4","导体中的电磁波",["thm","app"],"趋肤深度 $\\delta=\\sqrt{2/(\\omega\\mu_0\\sigma)}$。","<p>电磁波进入导体后指数衰减，趋肤深度为振幅衰减到 $1/e$ 的距离。高频时电流集中在导体表面（趋肤效应），用于电磁屏蔽和感应加热。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"电磁辐射","en":"RADIATION","sub":"偶极辐射、天线","desc":"加速电荷辐射电磁波。本章讨论电偶极辐射和多极辐射。","sections":[
      {"name":"3.1 偶极辐射","color":"#2563eb","desc":"电偶极辐射场","items":[
        item("la-k3-1","电偶极辐射",["def","thm","der"],"辐射功率 $P=\\frac{\\mu_0}{12\\pi c}|\\ddot{\\boldsymbol p}|^2$（拉莫尔公式）。","<p>振荡电偶极子辐射功率正比于频率四次方 $P\\propto\\omega^4$。辐射场 $B\\propto\\ddot p\\sin\\theta/r$，$E=cB$。辐射是横波，角分布 $\\propto\\sin^2\\theta$。这是天线辐射的基本机制。</p>"),
        item("la-k3-2","多极辐射",["thm","der"],"电偶极、磁偶极、电四极辐射逐级递减。","<p>若电偶极矩为零（如正负电荷对称振荡），需考虑磁偶极和电四极辐射。辐射功率依次为 $P_{md}/P_{ed}\\sim(v/c)^2$，$P_{eq}/P_{ed}\\sim(v/c)^2$。原子跃迁多为电偶极辐射。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"相对论电动力学","en":"RELATIVISTIC ELECTRODYNAMICS","sub":"四维形式、协变方程","desc":"电动力学天然满足狭义相对论，可用四维张量统一表述。","sections":[
      {"name":"4.1 协变形式","color":"#7c3aed","desc":"四维势、电磁场张量","items":[
        item("la-k4-1","电磁场张量",["def","thm"],"$F_{\\mu\\nu}=\\partial_\\mu A_\\nu-\\partial_\\nu A_\\mu$，反对称二阶张量。","<p>四维势 $A^\\mu=(\\varphi/c,\\boldsymbol A)$。电磁场张量 $F_{\\mu\\nu}$ 的六个独立分量对应 $\\boldsymbol E$ 和 $\\boldsymbol B$。麦克斯韦方程组可写为协变形式：$\\partial_\\mu F^{\\mu\\nu}=\\mu_0 J^\\nu$ 和 $\\partial_\\lambda F_{\\mu\\nu}+\\partial_\\mu F_{\\nu\\lambda}+\\partial_\\nu F_{\\lambda\\mu}=0$。</p>"),
        item("la-k4-2","洛伦兹力协变形式",["thm"],"$\\frac{dp^\\mu}{d\\tau}=qF^{\\mu\\nu}u_\\nu$。","<p>洛伦兹力的四维形式。在不同惯性系中，电场和磁场相互转化。例如，静止电荷在一个参考系中只有电场，在另一参考系中既有电场又有磁场。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 15. 电路 circuits
# ============================================================
SUBJECTS.append({
  "filename":"circuits.html",
  "title":"电路",
  "eyebrow":"CIRCUIT ANALYSIS",
  "subtitle":"基尔霍夫定律 · 电阻电路 · 一阶二阶电路 · 正弦稳态 · 三相电路",
  "meta_desc":"电路知识体系：基尔霍夫定律、电阻电路、一阶二阶电路、正弦稳态、三相电路",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"电路基本定律","en":"CIRCUIT LAWS","sub":"欧姆定律、基尔霍夫定律","desc":"电路分析的基础是欧姆定律与基尔霍夫两大定律。","sections":[
      {"name":"1.1 基本定律","color":"#2563eb","desc":"KCL 与 KVL","items":[
        item("la-k1-1","基尔霍夫定律",["def","thm"],"KCL：$\\sum I=0$（节点）；KVL：$\\sum U=0$（回路）。","<p>KCL 是电荷守恒的体现，流入等于流出。KVL 是能量守恒的体现，回路电压和为零。</p>"),
        item("la-k1-2","等效变换",["thm","der"],"串并联、星三角、戴维南/诺顿等效。","<p>戴维南定理：任何线性有源二端网络可等效为电压源 $U_{oc}$ 串联内阻 $R_{eq}$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"动态与正弦电路","en":"DYNAMIC & AC","sub":"一阶、二阶、相量法","desc":"含电容电感的动态电路与正弦稳态分析。","sections":[
      {"name":"2.1 动态电路","color":"#7c3aed","desc":"RC、RL、RLC","items":[
        item("la-k2-1","一阶电路",["def","thm"],"时间常数 $\\tau=RC$ 或 $L/R$，全响应=零输入+零状态。","<p>三要素法：$f(t)=f(\\infty)+[f(0_+)-f(\\infty)]e^{-t/\\tau}$。</p>"),
        item("la-k2-2","相量法",["def","thm"],"正弦量用相量 $\\dot{U}=U\\angle\\varphi$ 表示，微分变 $j\\omega$。","<p>相量法将时域微分方程化为频域代数方程。阻抗 $Z=R+jX$，导纳 $Y=1/Z$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 16. 模拟电子技术 analog-electronics
# ============================================================
SUBJECTS.append({
  "filename":"analog-electronics.html",
  "title":"模拟电子技术",
  "eyebrow":"ANALOG ELECTRONICS",
  "subtitle":"二极管 · BJT · 场效应管 · 放大器 · 运放 · 反馈",
  "meta_desc":"模拟电子技术知识体系：二极管、BJT、场效应管、放大器、运放、反馈",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"半导体器件","en":"SEMICONDUCTOR DEVICES","sub":"二极管、BJT、MOSFET","desc":"模拟电路的基本器件。本章讨论 PN 结二极管、双极型晶体管与场效应管。","sections":[
      {"name":"1.1 二极管与 BJT","color":"#2563eb","desc":"非线性器件","items":[
        item("la-k1-1","PN 结二极管",["def","thm"],"$I=I_s(e^{V/V_T}-1)$，正向导通约 0.7V。","<p>二极管单向导电。用于整流、限幅、稳压。肖特基二极管速度更快。</p>"),
        item("la-k1-2","BJT 三极管",["def","thm"],"工作于放大区时 $I_C=\\beta I_B$。","<p>BJT 有 NPN 与 PNP 两种。放大区条件：发射结正偏、集电结反偏。$\\beta$ 为电流放大系数。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"放大器与运放","en":"AMPLIFIERS & OP-AMPS","sub":"小信号模型、反馈","desc":"晶体管放大器的小信号分析与运算放大器应用。","sections":[
      {"name":"2.1 放大器","color":"#7c3aed","desc":"增益、输入输出阻抗","items":[
        item("la-k2-1","共射放大器",["def","thm","der"],"电压增益 $A_v=-\\beta R_C/r_{be}$。","<p>共射极放大器反相放大，既有电压增益又有电流增益。输入电阻 $r_{be}$，输出电阻 $R_C$。</p>"),
      ]},
      {"name":"2.2 运放与反馈","color":"#0f766e","desc":"理想运放、负反馈","items":[
        item("la-k2-2","理想运放",["def","thm"],"虚短 $v_+=v_-$，虚断 $i_+=i_-=0$。","<p>负反馈组态：电压串联、电压并联、电流串联、电流并联。反相放大器 $A_v=-R_f/R_1$，同相 $A_v=1+R_f/R_1$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 17. 数字电子技术 digital-electronics
# ============================================================
SUBJECTS.append({
  "filename":"digital-electronics.html",
  "title":"数字电子技术",
  "eyebrow":"DIGITAL ELECTRONICS",
  "subtitle":"逻辑代数 · 门电路 · 组合逻辑 · 触发器 · 时序逻辑",
  "meta_desc":"数字电子技术知识体系：逻辑代数、门电路、组合逻辑、触发器、时序逻辑",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"逻辑代数与门电路","en":"LOGIC & GATES","sub":"布尔代数、基本门","desc":"数字电路以二值逻辑为基础。本章介绍布尔代数与基本逻辑门。","sections":[
      {"name":"1.1 逻辑代数","color":"#2563eb","desc":"布尔运算","items":[
        item("la-k1-1","基本逻辑",["def","thm"],"与 AND、或 OR、非 NOT，摩根律 $\\overline{AB}=\\bar A+\\bar B$。","<p>布尔代数中变量取 0 或 1。基本运算：$A\\cdot B$（与）、$A+B$（或）、$\\bar A$（非）。</p>"),
      ]},
      {"name":"1.2 门电路","color":"#7c3aed","desc":"TTL、CMOS","items":[
        item("la-k1-2","CMOS 反相器",["def","app"],"NMOS+PMOS 互补结构，静态功耗极低。","<p>CMOS 是数字集成电路的主流。噪声容限大，速度与电源电压相关。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"组合与时序逻辑","en":"COMBINATIONAL & SEQUENTIAL","sub":"译码器、触发器、状态机","desc":"组合逻辑无记忆，时序逻辑有记忆。本章讨论常见逻辑部件。","sections":[
      {"name":"2.1 组合逻辑","color":"#0f766e","desc":"编码器、译码器","items":[
        item("la-k2-1","组合逻辑电路",["def","thm"],"输出仅取决于当前输入，无反馈。","<p>常用部件：编码器、译码器、数据选择器 MUX、加法器。可用卡诺图化简。</p>"),
      ]},
      {"name":"2.2 时序逻辑","color":"#c2410c","desc":"触发器、状态机","items":[
        item("la-k2-2","D 触发器",["def","thm"],"$Q^{n+1}=D$，边沿触发。","<p>D 触发器是最常用的存储元件。寄存器、计数器、有限状态机均由其构成。建立/保持时间约束决定最高时钟频率。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 18. 集成电路 integrated-circuits
# ============================================================
SUBJECTS.append({
  "filename":"integrated-circuits.html",
  "title":"集成电路",
  "eyebrow":"INTEGRATED CIRCUITS",
  "subtitle":"MOS 工艺 · 数字 IC · 模拟 IC · 版图 · 流片",
  "meta_desc":"集成电路知识体系：MOS工艺、数字IC、模拟IC、版图、流片",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"MOS 管与工艺","en":"MOS & PROCESS","sub":"MOSFET、工艺基础","desc":"集成电路以 MOSFET 为基本器件。本章讨论 MOS 管原理与工艺流程。","sections":[
      {"name":"1.1 MOSFET 原理","color":"#2563eb","desc":"场效应晶体管","items":[
        item("la-k1-1","MOS 管工作原理",["def","thm"],"栅压控制沟道，$I_D$ 工作于线性区或饱和区。","<p>增强型 NMOS：$V_{GS}>V_{th}$ 时反型层形成。饱和区 $I_D=\\frac12\\mu_n C_{ox}\\frac{W}{L}(V_{GS}-V_{th})^2$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"数字与模拟 IC","en":"DIGITAL & ANALOG IC","sub":"逻辑门、放大器","desc":"数字 IC 追求速度与功耗，模拟 IC 追求精度与线性度。","sections":[
      {"name":"2.1 数字 IC","color":"#7c3aed","desc":"逻辑门设计","items":[
        item("la-k2-1","CMOS 逻辑门",["def","app"],"与非门、或非门由 PMOS 上拉网络与 NMOS 下拉网络组成。","<p>CMOS 静态功耗近零。动态功耗 $P=\\alpha C_L V_{DD}^2 f$，是数字芯片功耗主因。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 19. 热学 thermal-physics
# ============================================================
SUBJECTS.append({
  "filename":"thermal-physics.html",
  "title":"热学",
  "eyebrow":"THERMAL PHYSICS",
  "subtitle":"温度 · 热力学定律 · 气体动理论 · 相变 · 输运过程",
  "meta_desc":"热学知识体系：温度与热平衡、热力学四大定律、理想气体、麦克斯韦分布、相变、热传导",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"温度与热力学定律","en":"TEMPERATURE & THERMODYNAMIC LAWS","sub":"热平衡、四大定律","desc":"热学研究热现象的宏观规律。本章从温度出发，讨论热力学四大定律及其应用。","sections":[
      {"name":"1.1 温度与热平衡","color":"#2563eb","desc":"热力学第零定律、温标","items":[
        item("la-k1-1","热力学第零定律",["def","thm"],"两系统分别与第三系统热平衡，则彼此热平衡。","<p>第零定律为温度的定义提供了依据：温度是决定系统是否热平衡的状态函数。热平衡时两系统温度相等。温标的建立需要测温物质和测温属性。</p>"),
        item("la-k1-2","热力学第一定律",["def","thm"],"$\\Delta U=Q+W$，能量守恒与转化。","<p>系统内能增量等于吸收的热量 $Q$ 与外界对系统做功 $W$ 之和。符号约定：$Q>0$ 吸热，$W>0$ 外界对系统做功。第一定律表明第一类永动机不可能实现。</p>"),
      ]},
      {"name":"1.2 第二与第三定律","color":"#7c3aed","desc":"熵、熵增原理","items":[
        item("la-k1-3","热力学第二定律",["def","thm","his"],"克劳修斯/开尔文表述，熵增原理 $dS\\ge\\delta Q/T$。","<p>克劳修斯表述：热量不能自发从低温传到高温。开尔文表述：不可能从单一热源吸热完全变成功。熵增原理：孤立系统熵不减 $\\Delta S\\ge0$。熵 $S=k_B\\ln\\Omega$ 连接宏观与微观。第二类永动机不可能。</p>"),
        item("la-k1-4","热力学第三定律",["def","thm"],"绝对零度不可达到，$\\lim_{T\\to0}\\Delta S=0$。","<p>能斯特定理：温度趋于绝对零度时，等温过程的熵变趋于零。绝对零度只能无限趋近而不能达到。第三定律给出了熵的零点。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"热力学势与过程","en":"THERMODYNAMIC POTENTIALS","sub":"自由能、吉布斯函数","desc":"引入热力学势，方便处理不同约束下的热力学过程。","sections":[
      {"name":"2.1 热力学势","color":"#0f766e","desc":"F、G、H","items":[
        item("la-k2-1","自由能与吉布斯函数",["def","thm"],"$F=U-TS$，$G=H-TS=U-TS+PV$。","<p>等温等容过程中平衡态对应自由能极小；等温等压过程对应吉布斯函数极小。焓 $H=U+PV$ 用于等压过程。这些势是勒让德变换的结果。</p>"),
        item("la-k2-2","麦克斯韦关系",["thm","der"],"由 $dU=TdS-PdV$ 等全微分条件导出。","<p>麦克斯韦关系将可测量（如 $\\partial P/\\partial T|_V$）与不可直接测量联系起来。例如 $(\\partial S/\\partial V)_T=(\\partial P/\\partial T)_V$。共有四组关系。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"气体动理论","en":"KINETIC THEORY OF GASES","sub":"理想气体、麦克斯韦分布","desc":"从微观分子运动解释宏观热性质，建立宏观量与微观量的联系。","sections":[
      {"name":"3.1 理想气体","color":"#2563eb","desc":"状态方程与微观解释","items":[
        item("la-k3-1","理想气体状态方程",["def","thm"],"$PV=nRT$，分子平均平动动能 $\\bar\\varepsilon_k=\\frac32 k_B T$。","<p>压强来源于分子对器壁的碰撞：$P=\\frac13 nm\\bar{v^2}$。温度是分子平均平动动能的度量。理想气体内能仅与温度有关 $U=\\frac{i}{2}nRT$（$i$ 为自由度）。</p>"),
        item("la-k3-2","能量均分定理",["thm","der"],"每个自由度平均动能 $\\frac12 k_B T$。","<p>在温度 $T$ 的热平衡下，分子每个平方自由度（平动、转动）的平均能量为 $\\frac12 k_B T$。单原子分子 $i=3$，双原子分子常温 $i=5$（3 平动+2 转动）。</p>"),
      ]},
      {"name":"3.2 麦克斯韦速率分布","color":"#7c3aed","desc":"速率分布律","items":[
        item("la-k3-3","麦克斯韦速率分布律",["def","thm","der"],"$f(v)=4\\pi\\left(\\frac{m}{2\\pi k_B T}\\right)^{3/2}v^2 e^{-mv^2/(2k_B T)}$。","<p>平衡态下气体分子速率分布。最概然速率 $v_p=\\sqrt{2k_B T/m}$，平均速率 $\\bar v=\\sqrt{8k_B T/\\pi m}$，方均根速率 $v_{rms}=\\sqrt{3k_B T/m}$。三者之比 $1:1.128:1.225$。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"相变与输运","en":"PHASE TRANSITIONS & TRANSPORT","sub":"相图、热传导","desc":"物质不同相之间的转变，以及非平衡态的输运过程。","sections":[
      {"name":"4.1 相变","color":"#c2410c","desc":"相图、克拉珀龙方程","items":[
        item("la-k4-1","相变与相图","def","$P-T$ 相图上，三相点、临界点、相平衡曲线。","<p>一级相变有潜热和体积突变（固-液-气）。二级相变无潜热，比热等发散（如铁磁-顺磁、超导）。临界点附近出现临界乳光等临界现象。</p>"),
        item("la-k4-2","克拉珀龙方程",["thm","der"],"$\\frac{dP}{dT}=\\frac{L}{T\\Delta V}$。","<p>相平衡曲线的斜率由相变潜热 $L$ 和体积变化 $\\Delta V$ 决定。水的固-液平衡线斜率为负（冰融化体积减小），这是冰刀滑冰的原理。</p>"),
      ]},
      {"name":"4.2 输运过程","color":"#0f766e","desc":"热传导、粘滞、扩散","items":[
        item("la-k4-3","热传导定律",["def","app"],"傅里叶定律 $q=-\\kappa\\nabla T$。","<p>热流密度与温度梯度成正比，负号表示热量从高温流向低温。热导率 $\\kappa$ 取决于材料。气体 $\\kappa\\propto\\sqrt{T}$，金属热导率与电导率满足维德曼-弗兰兹定律。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 20. 热力学与统计物理 statistical-mechanics
# ============================================================
SUBJECTS.append({
  "filename":"statistical-mechanics.html",
  "title":"热力学与统计物理",
  "eyebrow":"STATISTICAL MECHANICS",
  "subtitle":"系综理论 · 玻尔兹曼统计 · 配分函数 · 玻色-费米统计 · 相变",
  "meta_desc":"统计物理知识体系：微正则/正则/巨正则系综、配分函数、玻尔兹曼分布、玻色-爱因斯坦与费米-狄拉克统计、相变理论",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"系综理论","en":"ENSEMBLE THEORY","sub":"微正则、正则、巨正则","desc":"统计物理用系综描述系统的微观状态分布。本章介绍三大系综及其配分函数。","sections":[
      {"name":"1.1 系综与配分函数","color":"#2563eb","desc":"统计分布、热力学量","items":[
        item("la-k1-1","微正则系综",["def","thm"],"等概率原理，孤立系统各微观态等概率。","<p>孤立系统（$N,V,E$ 固定）所有可达微观态等概率出现。熵 $S=k_B\\ln\\Omega(E,V,N)$，其中 $\\Omega$ 为微观态数。这是统计物理的基本假设（等概率原理）。</p>"),
        item("la-k1-2","正则系综",["def","thm"],"$P_s\\propto e^{-\\beta E_s}$，配分函数 $Z=\\sum_s e^{-\\beta E_s}$。","<p>与热源接触的系统（$N,V,T$ 固定），玻尔兹曼分布。自由能 $F=-k_BT\\ln Z$。内能 $U=-\\partial\\ln Z/\\partial\\beta$，压强 $P=k_BT\\partial\\ln Z/\\partial V$，熵 $S=(U-F)/T$。</p>"),
        item("la-k1-3","巨正则系综",["def","thm"],"$P_{N,s}\\propto e^{-\\beta(E_s-\\mu N)}$，巨配分函数 $\\Xi=\\sum_N e^{\\beta\\mu N}Z_N$。","<p>与热源和粒子源接触的开放系统（$V,T,\\mu$ 固定）。巨势 $\\Omega=-k_BT\\ln\\Xi=-PV$。平均粒子数 $\\bar N=k_BT\\partial\\ln\\Xi/\\partial\\mu$。巨正则系综在处理量子统计时最方便。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"玻尔兹曼统计","en":"BOLTZMANN STATISTICS","sub":"近独立粒子、麦克斯韦-玻尔兹曼分布","desc":"经典可分辨粒子（近独立）的统计，适用于高温低密度情形。","sections":[
      {"name":"2.1 近独立粒子系统","color":"#7c3aed","desc":"MB 分布、配分函数","items":[
        item("la-k2-1","麦克斯韦-玻尔兹曼分布",["def","thm","der"],"$n_i=g_i e^{-\\beta(\\varepsilon_i-\\mu)}$，配分函数 $Z_1=\\sum_i g_i e^{-\\beta\\varepsilon_i}$。","<p>经典可分辨粒子在能级上的分布。单粒子配分函数 $Z_1$，系统配分函数 $Z=Z_1^N/N!$（修正全同性）。经典极限条件：$e^\\alpha=e^{-\\beta\\mu}\\gg1$ 即热德布罗意波长远小于粒子间距。</p>"),
        item("la-k2-2","理想气体的配分函数",["thm","der","app"],"$Z_1=V(2\\pi mk_BT/h^2)^{3/2}$，$PV=nRT$。","<p>由配分函数可导出理想气体状态方程、内能 $U=\\frac32 Nk_BT$、熵（萨库尔-泰特洛德公式）。配分函数是连接微观与宏观的桥梁。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"量子统计","en":"QUANTUM STATISTICS","sub":"玻色-爱因斯坦、费米-狄拉克","desc":"全同粒子的统计：玻色子服从玻色-爱因斯坦分布，费米子服从费米-狄拉克分布。","sections":[
      {"name":"3.1 量子分布函数","color":"#0f766e","desc":"BE 与 FD 分布","items":[
        item("la-k3-1","玻色-爱因斯坦分布",["def","thm"],"$f_{BE}(\\varepsilon)=\\frac{1}{e^{\\beta(\\varepsilon-\\mu)}-1}$。","<p>玻色子（整数自旋）不满足泡利不相容，同一态可容纳任意粒子数。低温下发生玻色-爱因斯坦凝聚（BEC），大量粒子占据基态。光子和声子化学势 $\\mu=0$，服从普朗克分布。</p>"),
        item("la-k3-2","费米-狄拉克分布",["def","thm"],"$f_{FD}(\\varepsilon)=\\frac{1}{e^{\\beta(\\varepsilon-\\mu)}+1}$。","<p>费米子（半整数自旋）满足泡利不相容，每个态最多一个粒子。$T=0$ 时 $\\mu=\\varepsilon_F$（费米能），$f=1$（$\\varepsilon<\\varepsilon_F$）或 $0$（$\\varepsilon>\\varepsilon_F$）。费米面概念是金属电子论的基础。</p>"),
      ]},
      {"name":"3.2 量子统计应用","color":"#c2410c","desc":"黑体辐射、电子气","items":[
        item("la-k3-3","黑体辐射（普朗克公式）",["thm","his","app"],"$u(\\omega,T)=\\frac{\\hbar\\omega^3}{\\pi^2 c^3}\\frac{1}{e^{\\hbar\\omega/k_BT}-1}$。","<p>光子气体的统计。普朗克公式成功解释了黑体辐射谱，标志着量子论的诞生。高频（$\\hbar\\omega\\gg k_BT$）维恩位移，低频（$\\hbar\\omega\\ll k_BT$）瑞利-金斯。斯特藩-玻尔兹曼定律 $U\\propto T^4$。</p>"),
        item("la-k3-4","自由电子气",["thm","app"],"费米能 $\\varepsilon_F=\\frac{\\hbar^2}{2m}(3\\pi^2 n)^{2/3}$。","<p>金属中自由电子形成简并费米气体。$T=0$ 时电子填满至费米面。比热 $C_V\\propto T$（而非经典的 $\\frac32 k_B$ 常数），因只有费米面附近 $k_BT$ 范围内电子可被激发。泡利顺磁与朗道抗磁性。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"相变理论","en":"PHASE TRANSITION THEORY","sub":"伊辛模型、临界现象","desc":"相变是合作现象，统计物理提供了微观解释。本章介绍伊辛模型和临界现象。","sections":[
      {"name":"4.1 伊辛模型","color":"#2563eb","desc":"合作现象","items":[
        item("la-k4-1","伊辛模型",["def","thm","app"],"$H=-J\\sum_{\\langle ij\\rangle}\\sigma_i\\sigma_j-h\\sum_i\\sigma_i$。","<p>伊辛模型描述自旋 $\\sigma_i=\\pm1$ 的合作系统。一维无有限温度相变，二维（昂萨格解）有相变，三维需数值方法。临界点附近出现自发磁化，描述铁磁-顺磁相变。</p>"),
        item("la-k4-2","临界指数与标度律",["thm","der"],"$\\chi\\propto|T-T_c|^{-\\gamma}$，$M\\propto(T_c-T)^{\\beta}$。","<p>临界点附近热力学量呈幂律行为，由临界指数刻画。标度律将各指数联系起来（如 $\\alpha+2\\beta+\\gamma=2$）。普适性：临界指数仅取决于空间维数和序参量分量数，与微观细节无关。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 21. 光学 optics
# ============================================================
SUBJECTS.append({
  "filename":"optics.html",
  "title":"光学",
  "eyebrow":"OPTICS",
  "subtitle":"几何光学 · 干涉 · 衍射 · 偏振 · 傅里叶光学 · 激光",
  "meta_desc":"光学知识体系：几何光学、费马原理、干涉、衍射、偏振、傅里叶光学、激光",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"几何光学","en":"GEOMETRICAL OPTICS","sub":"折射、反射、成像","desc":"光在波长可忽略时沿直线传播。本章讨论反射折射定律与透镜成像。","sections":[
      {"name":"1.1 基本定律","color":"#2563eb","desc":"费马原理、斯涅尔定律","items":[
        item("la-k1-1","反射与折射定律",["def","thm"],"$n_1\\sin\\theta_1=n_2\\sin\\theta_2$（斯涅尔定律）；反射角=入射角。","<p>费马原理：光沿光程极值路径传播。由费马原理可导出反射和折射定律。全反射：$n_1>n_2$ 且 $\\theta_1>\\theta_c=\\arcsin(n_2/n_1)$ 时无折射光，应用于光纤通信。</p>"),
        item("la-k1-2","薄透镜成像",["def","thm","app"],"$\\frac1s+\\frac1{s'}=\\frac1f$，横向放大率 $m=-s'/s$。","<p>薄透镜公式（高斯形式）。凸透镜 $f>0$，凹透镜 $f<0$。透镜制造者公式 $1/f=(n-1)(1/R_1-1/R_2)$。组合透镜 $1/f=\\sum1/f_i$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"光的干涉","en":"INTERFERENCE","sub":"相干叠加、分波前/分振幅","desc":"两束或多束相干光叠加产生明暗相间的干涉条纹。","sections":[
      {"name":"2.1 双缝与薄膜干涉","color":"#7c3aed","desc":"杨氏实验、牛顿环","items":[
        item("la-k2-1","杨氏双缝干涉",["def","thm","his"],"明纹 $d\\sin\\theta=m\\lambda$，暗纹 $d\\sin\\theta=(m+1/2)\\lambda$。","<p>杨氏双缝实验（1801）首次证明光的波动性。条纹间距 $\\Delta y=\\lambda D/d$。需相干光源，光程差决定明暗。时间相干性（相干长度）和空间相干性限制可见度。</p>"),
        item("la-k2-2","薄膜干涉",["thm","app"],"光程差 $\\Delta=2nd\\cos\\theta+\\lambda/2$（半波损失）。","<p>薄膜上下表面反射光干涉。增透膜利用相消干涉减少反射。牛顿环是等厚干涉，可测量透镜曲率半径。迈克尔逊干涉仪用分振幅法实现精密测量。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"光的衍射","en":"DIFFRACTION","sub":"菲涅耳、夫琅禾费","desc":"光绕过障碍物偏离直线传播的现象。本章讨论夫琅禾费衍射和衍射光栅。","sections":[
      {"name":"3.1 单缝与圆孔衍射","color":"#0f766e","desc":"惠更斯-菲涅耳原理","items":[
        item("la-k3-1","单缝夫琅禾费衍射",["def","thm"],"暗纹 $a\\sin\\theta=m\\lambda$，光强 $I=I_0(\\sin\\alpha/\\alpha)^2$。","<p>衍射是光的波动性的体现。中央明纹最亮最宽，为两侧明纹宽度的两倍。缝越窄，衍射越显著。圆孔衍射产生艾里斑，角半径 $\\theta=1.22\\lambda/D$，决定光学仪器分辨率。</p>"),
        item("la-k3-2","衍射光栅",["def","thm","app"],"主极大 $d\\sin\\theta=m\\lambda$，光栅方程。","<p>光栅由大量等间距狭缝组成。主极大位置由光栅方程决定。光栅色散 $D=d\\theta/d\\lambda=m/(d\\cos\\theta)$，分辨本领 $R=mN$。光栅光谱仪用于光谱分析。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"光的偏振","en":"POLARIZATION","sub":"横波特性、偏振器件","desc":"光是横波，电场矢量的振动方向即偏振方向。本章讨论偏振态和偏振器件。","sections":[
      {"name":"4.1 偏振态与马吕斯定律","color":"#c2410c","desc":"线/圆/椭圆偏振","items":[
        item("la-k4-1","马吕斯定律",["def","thm"],"$I=I_0\\cos^2\\theta$。","<p>线偏振光通过检偏器后强度按马吕斯定律变化。自然光通过偏振片后强度减半。布儒斯特角 $\\theta_B=\\arctan(n_2/n_1)$ 下反射光完全线偏振（s 偏振）。</p>"),
        item("la-k4-2","波片与圆偏振",["def","app"],"$\\lambda/4$ 波片将线偏振转为圆偏振。","<p>波片利用晶体双折射产生 o 光和 e 光的相位差。$\\lambda/4$ 波片产生 $\\pi/2$ 相位差，$\\lambda/2$ 波片产生 $\\pi$ 相位差。圆偏振光由两束等幅垂直线偏振光相位差 $\\pi/2$ 合成。</p>"),
      ]},
    ]},
    {"id":"la-ch5","num":"第五章","title":"傅里叶光学与激光","en":"FOURIER OPTICS & LASER","sub":"空间滤波、受激辐射","desc":"用傅里叶变换分析光学系统；激光基于受激辐射放大。","sections":[
      {"name":"5.1 傅里叶光学","color":"#2563eb","desc":"阿贝成像理论","items":[
        item("la-k5-1","阿贝成像原理",["thm","his"],"透镜后焦面为物的空间频谱，两次傅里叶变换完成成像。","<p>阿贝（1873）指出成像分两步：物光波在透镜后焦面形成空间频谱（衍射），各频谱分量再叠加（干涉）形成像。$\\lambda/4$ 显微镜分辨率极限由数值孔径决定。空间滤波可改变像的结构。</p>"),
      ]},
      {"name":"5.2 激光原理","color":"#7c3aed","desc":"受激辐射、谐振腔","items":[
        item("la-k5-2","激光产生条件",["def","thm","app"],"粒子数反转 + 光学谐振腔 + 增益大于损耗。","<p>爱因斯坦受激辐射理论预言激光。粒子数反转使受激辐射超过吸收。谐振腔提供正反馈和选模。激光特性：高单色性、高方向性、高亮度、高相干性。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 22. 光学系统设计 optical-design
# ============================================================
SUBJECTS.append({
  "filename":"optical-design.html",
  "title":"光学系统设计",
  "eyebrow":"OPTICAL DESIGN",
  "subtitle":"像差理论 · 透镜设计 · 镜头组 · Zemax",
  "meta_desc":"光学系统设计知识体系：像差理论、透镜设计、镜头组、Zemax",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"像差理论","en":"ABERRATION THEORY","sub":"七种像差","desc":"实际光学系统偏离理想成像的偏差称为像差。本章讨论五类单色像差与两类色差。","sections":[
      {"name":"1.1 单色像差","color":"#2563eb","desc":"赛德尔五像差","items":[
        item("la-k1-1","球差与彗差",["def","thm"],"球差：轴上点宽光束成像不完善；彗差：轴外点不对称。","<p>球差由透镜边缘与中心焦距不同引起。彗差使轴外物点成彗星状拖尾。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"透镜组设计","en":"LENS DESIGN","sub":"组合消像差","desc":"通过多片透镜组合校正像差。","sections":[
      {"name":"2.1 组合透镜","color":"#7c3aed","desc":"消色差双胶合","items":[
        item("la-k2-1","消色差双胶合镜",["def","thm"],"正负透镜不同色散材料胶合，消去初级色差。","<p>冕牌玻璃正透镜+火石玻璃负透镜，使两种波长焦距重合。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 23. 激光原理 laser-principles
# ============================================================
SUBJECTS.append({
  "filename":"laser-principles.html",
  "title":"激光原理",
  "eyebrow":"LASER PRINCIPLES",
  "subtitle":"受激辐射 · 粒子数反转 · 光放大 · 谐振腔 · 调Q锁模",
  "meta_desc":"激光原理知识体系：受激辐射、粒子数反转、光放大、谐振腔、调Q锁模",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"光与物质相互作用","en":"LIGHT-MATTER","sub":"受激辐射、爱因斯坦系数","desc":"激光基于受激辐射。本章讨论爱因斯坦三过程与粒子数反转。","sections":[
      {"name":"1.1 受激辐射","color":"#2563eb","desc":"爱因斯坦系数","items":[
        item("la-k1-1","爱因斯坦三过程",["def","thm"],"自发辐射 $A_{21}$、受激辐射 $B_{21}\\rho(\\nu)$、受激吸收 $B_{12}\\rho(\\nu)$。","<p>受激辐射产生与入射光同频率、同相位、同方向的光子，是激光相干放大的基础。$B_{12}=B_{21}$。</p>"),
        item("la-k1-2","粒子数反转",["def","thm"],"$N_2>N_1$，光增益条件。","<p>热平衡下 $N_2<N_1$（玻尔兹曼分布）。需通过泵浦实现反转，使光通过介质被放大。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"谐振腔与激光特性","en":"CAVITY & PROPERTIES","sub":"光学谐振腔、模式","desc":"谐振腔提供正反馈与模式选择，使激光具有高方向性、单色性与相干性。","sections":[
      {"name":"2.1 谐振腔","color":"#7c3aed","desc":"法布里-珀罗腔","items":[
        item("la-k2-1","光学谐振腔",["def","thm"],"两反射镜构成，纵模频率间隔 $\\Delta\\nu=c/2L$。","<p>谐振腔选频与正反馈。增益介质+谐振腔+泵浦源构成激光器三要素。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 24. 非线性光学 nonlinear-optics
# ============================================================
SUBJECTS.append({
  "filename":"nonlinear-optics.html",
  "title":"非线性光学",
  "eyebrow":"NONLINEAR OPTICS",
  "subtitle":"极化率 · 倍频 · 和频差频 · 四波混频 · 光孤子",
  "meta_desc":"非线性光学知识体系：极化率、倍频、和频差频、四波混频、光孤子",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"非线性极化","en":"NONLINEAR POLARIZATION","sub":"极化率张量","desc":"强光下介质极化与电场呈非线性关系。本章从极化率展开出发。","sections":[
      {"name":"1.1 非线性极化率","color":"#2563eb","desc":"$P=\\epsilon_0(\\chi^{(1)}E+\\chi^{(2)}E^2+\\chi^{(3)}E^3+\\cdots)$","items":[
        item("la-k1-1","二阶与三阶非线性",["def","thm"],"$\\chi^{(2)}$ 产生倍频、和频；$\\chi^{(3)}$ 产生四波混频、克尔效应。","<p>二阶非线性需非中心对称介质。三阶非线性普遍存在，强激光下显著。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"非线性过程","en":"NONLINEAR PROCESSES","sub":"倍频、相位匹配","desc":"常见非线性光学过程及相位匹配条件。","sections":[
      {"name":"2.1 倍频与相位匹配","color":"#7c3aed","desc":"二次谐波","items":[
        item("la-k2-1","二次谐波产生",["def","thm"],"$\\omega_3=2\\omega_1$，需相位匹配 $n(\\omega_3)=n(\\omega_1)$。","<p>相位匹配保证非线性极化波与辐射波同步。利用双折射晶体的寻常/非常光折射率可调。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 25. 发光物理 luminescence
# ============================================================
SUBJECTS.append({
  "filename":"luminescence.html",
  "title":"发光物理",
  "eyebrow":"LUMINESCENCE",
  "subtitle":"电子跃迁 · 激发态 · 发光机理 · LED · 荧光磷光",
  "meta_desc":"发光物理知识体系：电子跃迁、激发态、发光机理、LED、荧光磷光",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"发光基本原理","en":"LUMINESCENCE BASICS","sub":"激发与辐射跃迁","desc":"发光是物质吸收能量后以光辐射形式释放的过程。本章讨论电子跃迁与发光类型。","sections":[
      {"name":"1.1 电子跃迁","color":"#2563eb","desc":"吸收、自发辐射、受激辐射","items":[
        item("la-k1-1","辐射跃迁",["def","thm"],"电子从激发态回到基态并发射光子 $h\\nu=E_2-E_1$。","<p>荧光（自旋允许跃迁，寿命 ns）与磷光（自旋禁阻，寿命 $\\mu$s-s）。无辐射跃迁以热形式释放能量。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"发光材料与器件","en":"MATERIALS & DEVICES","sub":"LED、激光器","desc":"半导体发光二极管与激光器的工作原理。","sections":[
      {"name":"2.1 LED 与 LD","color":"#7c3aed","desc":"电致发光","items":[
        item("la-k2-1","发光二极管 LED",["def","app"],"PN 结注入载流子复合发光，$h\\nu\\approx E_g$。","<p>LED 电光转换效率高。半导体激光器（LD）在 LED 基础上加谐振腔实现受激辐射放大。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 26. 声学 acoustics
# ============================================================
SUBJECTS.append({
  "filename":"acoustics.html",
  "title":"声学",
  "eyebrow":"ACOUSTICS",
  "subtitle":"声波方程 · 声速 · 反射折射 · 超声 · 噪声",
  "meta_desc":"声学知识体系：声波方程、声速、反射折射、超声、噪声",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"声波基本理论","en":"SOUND WAVES","sub":"波动方程、声速","desc":"声波是弹性介质中传播的机械波。本章从流体方程推导声波方程。","sections":[
      {"name":"1.1 声波方程","color":"#2563eb","desc":"小振幅声波","items":[
        item("la-k1-1","声波方程",["def","thm","der"],"$\\nabla^2 p-\\frac1{c^2}\\partial_t^2 p=0$，$c=\\sqrt{\\partial p/\\partial\\rho}$。","<p>由连续性方程、运动方程、物态方程线性化得到。空气中声速约 340 m/s。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"声学应用","en":"ACOUSTIC APPLICATIONS","sub":"超声、噪声控制","desc":"声学在成像、通信、降噪中的应用。","sections":[
      {"name":"2.1 超声与声纳","color":"#7c3aed","desc":"高频声波","items":[
        item("la-k2-1","超声成像",["def","app"],"利用回波时间与强度重建体内图像。","<p>B 超、彩超广泛用于医学。声纳利用水中声波探测目标。主动降噪利用声波相消干涉。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 27. 原子物理学 atomic-physics
# ============================================================
SUBJECTS.append({
  "filename":"atomic-physics.html",
  "title":"原子物理学",
  "eyebrow":"ATOMIC PHYSICS",
  "subtitle":"原子模型 · 玻尔理论 · 量子数 · 精细结构 · 塞曼效应 · 跃迁",
  "meta_desc":"原子物理知识体系：卢瑟福模型、玻尔理论、量子数、自旋轨道耦合、精细结构、塞曼效应、跃迁选择定则",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"原子结构与玻尔模型","en":"ATOMIC STRUCTURE & BOHR MODEL","sub":"卢瑟福散射、玻尔假设","desc":"从卢瑟福散射实验到玻尔量子化模型，建立原子的量子化描述。","sections":[
      {"name":"1.1 玻尔模型","color":"#2563eb","desc":"氢原子能级","items":[
        item("la-k1-1","玻尔假设",["def","thm","his"],"定态假设、角动量量子化 $L=n\\hbar$、跃迁辐射 $h\\nu=E_m-E_n$。","<p>玻尔（1913）提出三条假设，成功解释氢原子光谱。氢原子能级 $E_n=-\\frac{me^4}{8\\varepsilon_0^2h^2n^2}=-\\frac{13.6}{n^2}$ eV。玻尔半径 $a_0=\\frac{4\\pi\\varepsilon_0\\hbar^2}{me^2}\\approx0.529\\,\\text{\\AA}$。里德伯公式 $1/\\lambda=R(1/n_1^2-1/n_2^2)$。</p>"),
        item("la-k1-2","弗兰克-赫兹实验",["def","thm","his"],"汞原子能级量子化，电流随加速电压周期性下降。","<p>弗兰克-赫兹实验（1914）直接证实了原子能级的量子化：电子与汞原子碰撞只损失 4.9 eV，证明原子内部能量是量子化的。这是玻尔理论的第一个实验验证。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"量子数与精细结构","en":"QUANTUM NUMBERS & FINE STRUCTURE","sub":"n,l,m,s 与自旋轨道耦合","desc":"原子状态由四个量子数描述。自旋轨道耦合产生精细结构。","sections":[
      {"name":"2.1 四个量子数","color":"#7c3aed","desc":"n,l,m_l,m_s","items":[
        item("la-k2-1","量子数与壳层结构",["def","thm"],"主量子数 $n$、角量子数 $l$、磁量子数 $m_l$、自旋 $m_s=\\pm1/2$。","<p>$l=0,1,2,3\\dots$ 对应 s,p,d,f 轨道。$m_l=-l,-l+1,\\dots,l$。泡利不相容原理：每个量子态最多容纳一个电子（考虑自旋则两个）。壳层按 $n$ 划分，子壳层按 $l$ 划分，决定元素周期表。</p>"),
        item("la-k2-2","自旋轨道耦合",["def","thm"],"$\\Delta E_{SO}\\propto\\boldsymbol L\\cdot\\boldsymbol S$，产生精细结构。","<p>电子自旋磁矩与轨道运动产生的磁场相互作用。$\\boldsymbol J=\\boldsymbol L+\\boldsymbol S$，$j=l\\pm1/2$。精细结构使能级分裂为两条。钠黄线（589nm）双线（D1=589.6nm, D2=589.0nm）即源于此。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"塞曼效应与跃迁","en":"ZEEMAN EFFECT & TRANSITIONS","sub":"外场分裂、选择定则","desc":"外磁场下原子能级进一步分裂，产生塞曼效应。跃迁满足选择定则。","sections":[
      {"name":"3.1 塞曼效应","color":"#0f766e","desc":"磁场中的能级分裂","items":[
        item("la-k3-1","塞曼效应",["def","thm","his"],"$\\Delta E=m_j g_j\\mu_B B$，谱线分裂。","<p>外磁场中原子磁矩与磁场相互作用使能级分裂。朗德 $g$ 因子 $g=1+\\frac{j(j+1)+s(s+1)-l(l+1)}{2j(j+1)}$。正常塞曼效应（单态，$S=0,g=1$）谱线分裂为三条；反常塞曼效应（$S\\neq0$）分裂更复杂。</p>"),
      ]},
      {"name":"3.2 辐射跃迁选择定则","color":"#c2410c","desc":"电偶极跃迁","items":[
        item("la-k3-2","选择定则",["def","thm","der"],"$\\Delta l=\\pm1$，$\\Delta j=0,\\pm1$（$j=0\\to j=0$ 禁戒），$\\Delta m_j=0,\\pm1$。","<p>电偶极跃迁的选择定则由角动量守恒和宇称守恒决定。违反选择定则的跃迁称为禁戒跃迁，概率极小。原子光谱的谱线结构由能级和选择定则共同决定。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 28. 量子力学 quantum-mechanics
# ============================================================
SUBJECTS.append({
  "filename":"quantum-mechanics.html",
  "title":"量子力学",
  "eyebrow":"QUANTUM MECHANICS",
  "subtitle":"波函数 · 薛定谔方程 · 算符 · 表象 · 自旋 · 微扰 · 散射",
  "meta_desc":"量子力学知识体系：波函数与概率诠释、薛定谔方程、力学量算符、不确定关系、表象变换、自旋角动量、微扰论、散射",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"波函数与薛定谔方程","en":"WAVE FUNCTION & SCHRÖDINGER","sub":"态叠加、概率诠释、定态","desc":"量子力学用波函数描述系统状态，薛定谔方程支配其演化。这是量子力学的核心。","sections":[
      {"name":"1.1 波函数假设","color":"#2563eb","desc":"概率幅、态叠加","items":[
        item("la-k1-1","波函数与概率诠释",["def","thm","his"],"$|\\psi(\\boldsymbol r,t)|^2$ 为概率密度，归一化 $\\int|\\psi|^2d^3r=1$。","<p>玻恩（1926）提出：波函数是概率幅，其模平方给出粒子在空间出现的概率密度。态叠加原理：若 $\\psi_1,\\psi_2$ 是可能态，则 $\\psi=c_1\\psi_1+c_2\\psi_2$ 也是可能态。这是量子干涉的根源。</p>"),
        item("la-k1-2","薛定谔方程",["def","thm","his"],"$i\\hbar\\frac{\\partial\\psi}{\\partial t}=\\hat H\\psi$，$\\hat H=-\\frac{\\hbar^2}{2m}\\nabla^2+V(\\boldsymbol r)$。","<p>薛定谔（1926）提出的非相对论量子力学基本方程。定态方程 $\\hat H\\psi=E\\psi$ 的解是能量本征态。时间演化由幺正算符 $U(t)=e^{-i\\hat Ht/\\hbar}$ 描述。概率守恒由连续性方程表达。</p>"),
      ]},
      {"name":"1.2 定态问题","color":"#7c3aed","desc":"无限深势阱、谐振子","items":[
        item("la-k1-3","一维无限深势阱",["def","thm","der"],"$E_n=\\frac{n^2\\pi^2\\hbar^2}{2ma^2}$，$\\psi_n=\\sqrt{2/a}\\sin(n\\pi x/a)$。","<p>粒子被限制在 $[0,a]$ 内。能量量子化，基态能量不为零（零点能）。波函数在边界为零（节点数 $n-1$）。这是量子力学最简单的精确可解模型。</p>"),
        item("la-k1-4","简谐振子",["def","thm","der"],"$E_n=(n+1/2)\\hbar\\omega$，$\\psi_n$ 用厄米多项式表示。","<p>谐振子是量子力学最重要的模型之一。能量等间距 $\\Delta E=\\hbar\\omega$，零点能 $E_0=\\hbar\\omega/2$。用产生湮灭算符 $a^\\dagger,a$ 求解极为简洁，$[a,a^\\dagger]=1$，$H=\\hbar\\omega(a^\\dagger a+1/2)$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"力学量算符与表象","en":"OPERATORS & REPRESENTATIONS","sub":"厄米算符、对易关系、不确定关系","desc":"力学量对应厄米算符，其本征值为测量结果。表象变换是量子力学的重要工具。","sections":[
      {"name":"2.1 算符与对易关系","color":"#2563eb","desc":"厄米算符、正则对易","items":[
        item("la-k2-1","算符假设",["def","thm"],"力学量用厄米算符表示，本征值实数，本征态正交完备。","<p>位置 $\\hat x=x$，动量 $\\hat p=-i\\hbar\\partial_x$。厄米算符 $\\hat A^\\dagger=\\hat A$，其本征值为实数，对应可测量。测量后系统坍缩到对应本征态。期望值 $\\langle A\\rangle=\\langle\\psi|\\hat A|\\psi\\rangle$。</p>"),
        item("la-k2-2","不确定关系",["thm","der"],"$\\Delta x\\Delta p\\ge\\hbar/2$。","<p>海森堡不确定关系：对易子不为零的力学量不能同时精确测量。一般形式 $\\Delta A\\Delta B\\ge\\frac12|\\langle[\\hat A,\\hat B]\\rangle|$。能量时间不确定关系 $\\Delta E\\Delta t\\ge\\hbar/2$ 有不同物理含义。</p>"),
      ]},
      {"name":"2.2 表象变换","color":"#7c3aed","desc":"坐标表象、动量表象","items":[
        item("la-k2-3","表象与幺正变换",["def","thm"],"不同表象通过幺正变换联系，物理结果不变。","<p>坐标表象中 $\\hat p=-i\\hbar\\nabla$；动量表象中 $\\hat x=i\\hbar\\partial_p$。表象变换即基底变换。$S$ 矩阵将不同表象联系起来：$|\\psi\\rangle_{p'}=S|\\psi\\rangle_x$。狄拉克符号 $|\\psi\\rangle$ 不依赖表象。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"角动量与自旋","en":"ANGULAR MOMENTUM & SPIN","sub":"对易关系、泡利矩阵","desc":"角动量是量子力学的核心概念。电子自旋是内禀角动量。","sections":[
      {"name":"3.1 角动量理论","color":"#0f766e","desc":"$J^2,J_z$ 共同本征态","items":[
        item("la-k3-1","角动量对易关系",["def","thm"],"$[J_i,J_j]=i\\hbar\\epsilon_{ijk}J_k$，$J^2|jm\\rangle=j(j+1)\\hbar^2|jm\\rangle$。","<p>角动量由对易关系定义（不限于轨道角动量）。$J_z|jm\\rangle=m\\hbar|jm\\rangle$，$m=-j,-j+1,\\dots,j$。升降算符 $J_\\pm=J_x\\pm iJ_y$，$J_\\pm|jm\\rangle=\\sqrt{(j\\mp m)(j\\pm m+1)}\\hbar|j,m\\pm1\\rangle$。</p>"),
      ]},
      {"name":"3.2 电子自旋","color":"#c2410c","desc":"自旋 1/2、泡利矩阵","items":[
        item("la-k3-2","泡利矩阵与自旋",["def","thm","his"],"$\\sigma_x=\\begin{pmatrix}0&1\\\\1&0\\end{pmatrix},\\sigma_y=\\begin{pmatrix}0&-i\\\\i&0\\end{pmatrix},\\sigma_z=\\begin{pmatrix}1&0\\\\0&-1\\end{pmatrix}$。","<p>电子自旋 $s=1/2$，由乌伦贝克和古兹米特（1925）提出。自旋角动量 $\\boldsymbol S=\\frac\\hbar2\\boldsymbol\\sigma$。泡利矩阵满足 $[\\sigma_i,\\sigma_j]=2i\\epsilon_{ijk}\\sigma_k$，$\\sigma_i^2=I$。自旋态是二维旋量。斯特恩-盖拉赫实验证实了空间量子化。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"近似方法与散射","en":"APPROXIMATION & SCATTERING","sub":"微扰论、变分法、散射截面","desc":"大多数量子系统无法精确求解，需用近似方法。散射理论处理碰撞问题。","sections":[
      {"name":"4.1 微扰论","color":"#2563eb","desc":"定态微扰、含时微扰","items":[
        item("la-k4-1","非简并定态微扰",["def","thm","der"],"一级能量修正 $E_n^{(1)}=\\langle n|H'|n\\rangle$。","<p>哈密顿量 $H=H_0+H'$，$H'$ 为小微扰。能级 $E_n=E_n^{(0)}+E_n^{(1)}+E_n^{(2)}+\\cdots$，二级修正 $E_n^{(2)}=\\sum_{m\\neq n}|\\langle m|H'|n\\rangle|^2/(E_n^{(0)}-E_m^{(0)})$。简并情况需另行处理（简并微扰论）。</p>"),
        item("la-k4-2","含时微扰与跃迁",["thm","der"],"费米黄金规则 $\\Gamma=\\frac{2\\pi}{\\hbar}|\\langle f|H'|i\\rangle|^2\\rho(E_f)$。","<p>含时微扰论计算量子跃迁概率。费米黄金规则给出单位时间跃迁概率，与末态态密度 $\\rho$ 成正比。应用：原子光吸收/发射、散射过程。</p>"),
      ]},
      {"name":"4.2 散射理论","color":"#7c3aed","desc":"散射振幅、分波法","items":[
        item("la-k4-3","散射振幅与截面",["def","thm"],"$\\sigma(\\theta)=|f(\\theta)|^2$，$f(\\theta)=-\\frac{2m}{\\hbar^2}\\int V(r)e^{i(\\boldsymbol k-\\boldsymbol k')\\cdot\\boldsymbol r}d^3r$（玻恩近似）。","<p>散射振幅 $f(\\theta)$ 决定微分散射截面。低能用分波法（相移 $\\delta_l$），高能用玻恩近似。全截面 $\\sigma=\\frac{4\\pi}{k^2}\\sum(2l+1)\\sin^2\\delta_l$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 29. 量子计算 quantum-computing
# ============================================================
SUBJECTS.append({
  "filename":"quantum-computing.html",
  "title":"量子计算",
  "eyebrow":"QUANTUM COMPUTING",
  "subtitle":"量子比特 · 量子门 · 量子线路 · Shor · Grover · 纠错",
  "meta_desc":"量子计算知识体系：量子比特、量子门、量子线路、Shor、Grover、纠错",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"量子比特与量子门","en":"QUBITS & GATES","sub":"叠加、纠缠、门操作","desc":"量子计算利用叠加与纠缠实现并行。本章介绍量子比特与基本量子门。","sections":[
      {"name":"1.1 量子比特","color":"#2563eb","desc":"布洛赫球","items":[
        item("la-k1-1","量子比特",["def","thm"],"$|\\psi\\rangle=\\alpha|0\\rangle+\\beta|1\\rangle$，$|\\alpha|^2+|\\beta|^2=1$。","<p>测量以 $|\\alpha|^2$ 概率得 0，$|\\beta|^2$ 得 1。多比特可纠缠，Bell 态 $|\\Phi^+\\rangle=(|00\\rangle+|11\\rangle)/\\sqrt2$。</p>"),
      ]},
      {"name":"1.2 量子门","color":"#7c3aed","desc":"幺正变换","items":[
        item("la-k1-2","基本量子门",["def","thm"],"Hadamard $H$、Pauli $X,Y,Z$、CNOT，均为幺正矩阵。","<p>量子门是幺正操作 $U$，满足 $U^\\dagger U=I$。$H|0\\rangle=(|0\\rangle+|1\\rangle)/\\sqrt2$ 产生叠加态。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"量子算法","en":"QUANTUM ALGORITHMS","sub":"Shor、Grover","desc":"量子算法在特定问题上指数或多项式超越经典。","sections":[
      {"name":"2.1 著名算法","color":"#0f766e","desc":"指数加速","items":[
        item("la-k2-1","Shor 与 Grover 算法",["thm","app"],"Shor 分解大数 $O((\\log N)^3)$；Grover 搜索 $O(\\sqrt N)$。","<p>Shor 算法用量子相位估计求周期，威胁 RSA 加密。Grover 对未排序数据库搜索提供平方加速。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 30. 原子核物理 nuclear-physics
# ============================================================
SUBJECTS.append({
  "filename":"nuclear-physics.html",
  "title":"原子核物理",
  "eyebrow":"NUCLEAR PHYSICS",
  "subtitle":"核结构 · 核力 · 衰变 · 裂变聚变 · 核模型",
  "meta_desc":"原子核物理知识体系：核的基本性质、结合能、核力、放射性衰变、裂变聚变、核结构模型",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"原子核的基本性质","en":"NUCLEAR PROPERTIES","sub":"大小、质量、结合能、核力","desc":"原子核由质子和中子组成。本章讨论核的大小、质量、结合能与核力。","sections":[
      {"name":"1.1 结合能与核力","color":"#2563eb","desc":"质量亏损、强相互作用","items":[
        item("la-k1-1","结合能",["def","thm"],"$B=(Zm_p+Nm_n-M_{核})c^2$，比结合能 $B/A$ 衡量核稳定性。","<p>质量亏损 $\\Delta m=Zm_p+Nm_n-M_{核}$ 转化为结合能。比结合能曲线在 $A\\approx56$（铁）处最大，约 8.8 MeV。比结合能大的核更稳定。重核裂变和轻核聚变都向比结合能更大的方向进行，释放能量。</p>"),
        item("la-k1-2","核力",["def","thm"],"短程、强吸引、电荷无关、饱和性。","<p>核力是强相互作用的剩余效应，力程约 2 fm。核力比电磁力强约 100 倍，但仅在核子间极短距离内起作用。核力具有饱和性（每个核子只与邻近核子作用），这解释了结合能近似正比于 $A$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"放射性衰变","en":"RADIOACTIVE DECAY","sub":"α/β/γ 衰变、衰变定律","desc":"不稳定核通过衰变释放能量，转变为更稳定的核。","sections":[
      {"name":"2.1 衰变类型与规律","color":"#7c3aed","desc":"三种主要衰变","items":[
        item("la-k2-1","衰变定律",["def","thm"],"$N(t)=N_0e^{-\\lambda t}$，半衰期 $T_{1/2}=\\ln2/\\lambda$，平均寿命 $\\tau=1/\\lambda$。","<p>放射性衰变是统计过程，单个核的衰变时刻随机，但大量核的衰变服从指数规律。衰变常数 $\\lambda$ 与外界条件（温度、压力等）无关，由核内部结构决定。</p>"),
        item("la-k2-2","α、β、γ 衰变",["def","thm","app"],"α：$^4_2$He；β：$n\\to p+e^-+\\bar\\nu_e$；γ：核退激发射光子。","<p>α 衰变放出氦核，发生在重核（$A>140$）。β 衰变中中子转为质子（β⁻）或质子转为中子（β⁺/电子俘获），并放出中微子。γ 衰变是激发态核跃迁到低能态，放出光子，不改变核素。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"核裂变与核聚变","en":"FISSION & FUSION","sub":"核能释放","desc":"重核裂变和轻核聚变都释放巨大能量，是核能利用的基础。","sections":[
      {"name":"3.1 裂变与聚变","color":"#0f766e","desc":"核能应用","items":[
        item("la-k3-1","核裂变",["def","thm","app"],"重核（如 U-235）裂变为两个中等质量核，释放约 200 MeV。","<p>裂变由中子诱发，产生 2-3 个中子，可引发链式反应。核电站利用可控链式反应发电（$E=mc^2$，质量亏损约 0.1%）。原子弹使用临界质量实现不可控裂变。</p>"),
        item("la-k3-2","核聚变",["def","thm","app"],"轻核（D+T）聚变为较重核，释放约 17.6 MeV。","<p>聚变是太阳和恒星的能量来源。D-T 反应：$^2_1$H+$^3_1$H$\\to^4_2$He+n+17.6 MeV。可控核聚变需高温（>10⁸ K）、高密度和约束（劳森判据），是未来清洁能源的希望。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"核结构模型","en":"NUCLEAR MODELS","sub":"液滴模型、壳模型","desc":"核结构模型从不同角度描述原子核的性质。","sections":[
      {"name":"4.1 核模型","color":"#c2410c","desc":"集体与单粒子模型","items":[
        item("la-k4-1","液滴模型",["def","thm","app"],"结合能半经验公式 $B=a_V A-a_S A^{2/3}-a_C Z^2/A^{1/3}-a_A(A-2Z)^2/A+\\delta$。","<p>液滴模型将核视为带电液滴，解释了结合能的整体趋势和裂变的发生。魏扎克半经验公式较好地拟合了核素结合能。</p>"),
        item("la-k4-2","壳模型",["def","thm","app"],"核子在平均势场中独立运动，存在幻数（2,8,20,28,50,82,126）。","<p>壳模型类比原子的电子壳层，核子在平均场中填充能级。幻数对应的核特别稳定。壳模型成功解释了核的自旋和宇称，以及幻数的存在。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 31. 基础物理实验 basic-physics-lab
# ============================================================
SUBJECTS.append({
  "filename":"basic-physics-lab.html",
  "title":"基础物理实验",
  "eyebrow":"BASIC PHYSICS LAB",
  "subtitle":"误差分析 · 力学实验 · 电磁学实验 · 光学实验",
  "meta_desc":"基础物理实验知识体系：误差分析、力学实验、电磁学实验、光学实验",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"误差与数据处理","en":"ERROR ANALYSIS","sub":"误差、不确定度","desc":"实验测量不可避免有误差。本章讨论误差分类与不确定度评定。","sections":[
      {"name":"1.1 误差理论","color":"#2563eb","desc":"系统误差与随机误差","items":[
        item("la-k1-1","误差与不确定度",["def","thm"],"绝对误差 $\\Delta x$，相对误差 $E=\\Delta x/x$。","<p>系统误差可修正，随机误差用统计方法处理。标准不确定度 $u_A=\\sigma/\\sqrt n$（A 类），$u_B$ 来自仪器（B 类）。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"典型实验","en":"TYPICAL EXPERIMENTS","sub":"力、电、光","desc":"基础物理实验涵盖力学、电磁学、光学。","sections":[
      {"name":"2.1 力学与电磁学","color":"#7c3aed","desc":"常用实验","items":[
        item("la-k2-1","密立根油滴与霍尔效应",["def","app"],"测量元电荷与载流子类型浓度。","<p>密立根油滴实验测定 $e=1.602\\times10^{-19}$ C。霍尔效应测半导体载流子参数。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 32. 近代物理实验 modern-physics-lab
# ============================================================
SUBJECTS.append({
  "filename":"modern-physics-lab.html",
  "title":"近代物理实验",
  "eyebrow":"MODERN PHYSICS LAB",
  "subtitle":"卢瑟福散射 · 弗兰克-赫兹 · 光电效应 · 塞曼 · 核磁共振",
  "meta_desc":"近代物理实验知识体系：卢瑟福散射、弗兰克-赫兹、光电效应、塞曼、核磁共振",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"量子现象验证","en":"QUANTUM PHENOMENA","sub":"原子能级、量子化","desc":"近代物理实验验证微观世界的量子规律。","sections":[
      {"name":"1.1 原子能级实验","color":"#2563eb","desc":"量子化的直接证据","items":[
        item("la-k1-1","弗兰克-赫兹实验",["def","thm","his"],"汞原子能级量子化，电流随加速电压周期性下降。","<p>电子与汞原子碰撞只损失 4.9 eV，证明原子内部能量是量子化的。</p>"),
        item("la-k1-2","光电效应",["def","thm"],"$E_k=h\\nu-W$，爱因斯坦方程。","<p>光电子动能与光强无关，只与频率有关。证明光具有粒子性（光子）。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"磁共振与散射","en":"RESONANCE & SCATTERING","sub":"NMR、卢瑟福","desc":"磁共振与散射实验探索微观结构。","sections":[
      {"name":"2.1 核磁共振","color":"#7c3aed","desc":"自旋共振","items":[
        item("la-k2-1","NMR",["def","thm","app"],"共振条件 $\\hbar\\omega=\\gamma\\hbar B$，化学位移分析结构。","<p>核磁矩在磁场中能级分裂，射频共振激发。广泛用于医学成像（MRI）与化学结构分析。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 33. 固体物理 solid-state-physics
# ============================================================
SUBJECTS.append({
  "filename":"solid-state-physics.html",
  "title":"固体物理",
  "eyebrow":"SOLID STATE PHYSICS",
  "subtitle":"晶体结构 · 倒易空间 · 声子 · 能带理论 · 费米面 · 输运",
  "meta_desc":"固体物理知识体系：晶体结构、倒易空间与衍射、晶格振动与声子、能带理论、费米面、金属与半导体输运",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"晶体结构与倒易空间","en":"CRYSTAL STRUCTURE & RECIPROCAL SPACE","sub":"布拉维格子、倒格子、衍射","desc":"晶体由原子周期性排列构成。本章讨论晶体结构、倒易空间和 X 射线衍射。","sections":[
      {"name":"1.1 晶体结构","color":"#2563eb","desc":"周期性、布拉维格子","items":[
        item("la-k1-1","布拉维格子与基元",["def","thm"],"14 种布拉维格子，原胞体积 $\\Omega=\\boldsymbol a_1\\cdot(\\boldsymbol a_2\\times\\boldsymbol a_3)$。","<p>晶体结构 = 布拉维格子 + 基元。常见结构：简单立方(SC)、体心立方(BCC)、面心立方(FCC)、密排六方(HCP)。配位数：SC=6，BCC=8，FCC=12。堆积密度 FCC/HCP=74% 最密排。</p>"),
        item("la-k1-2","倒易空间与衍射",["def","thm"],"倒格矢 $\\boldsymbol b_i=2\\pi\\boldsymbol a_j\\times\\boldsymbol a_k/\\Omega$。","<p>倒格子与正格子互为傅里叶对偶。第一布里渊区是倒空间的 Wigner-Seitz 原胞。X 射线衍射条件（劳厄条件）$\\Delta\\boldsymbol k=\\boldsymbol G$，等价于布拉格方程 $2d\\sin\\theta=n\\lambda$。衍射实验测定晶体结构。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"晶格振动与声子","en":"LATTICE VIBRATIONS & PHONONS","sub":"简谐近似、色散关系","desc":"原子在平衡位置附近振动，量子化为声子。声子决定热学性质。","sections":[
      {"name":"2.1 声子色散","color":"#7c3aed","desc":"声学支与光学支","items":[
        item("la-k2-1","一维单原子链",["def","thm","der"],"色散 $\\omega=\\sqrt{4K/m}|\\sin(qa/2)|$。","<p>简谐近似下，原子链振动形成格波。色散关系在布里渊区边界 $q=\\pi/a$ 处最大，长波极限 $\\omega=v_s q$（声学波，声速 $v_s=a\\sqrt{K/m}$）。量子化后称为声子，是玻色子。</p>"),
        item("la-k2-2","声子统计与热容",["thm","app"],"德拜模型 $C_V=9Nk_B(T/\\Theta_D)^3\\int_0^{x_D}\\frac{x^4e^x}{(e^x-1)^2}dx$。","<p>声子服从玻色-爱因斯坦分布。爱因斯坦模型假设单一频率，德拜模型用连续介质近似。高温 $C_V\\to3R$（杜隆-珀替定律），低温 $C_V\\propto T^3$（德拜 $T^3$ 定律）。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"能带理论","en":"BAND THEORY","sub":"布洛赫定理、近自由电子、紧束缚","desc":"周期势中电子形成能带。能带理论是固体电子学的基础。","sections":[
      {"name":"3.1 布洛赫定理","color":"#0f766e","desc":"周期势中的电子","items":[
        item("la-k3-1","布洛赫定理",["def","thm"],"$\\psi_{\\boldsymbol k}(\\boldsymbol r)=e^{i\\boldsymbol k\\cdot\\boldsymbol r}u_{\\boldsymbol k}(\\boldsymbol r)$，$u_{\\boldsymbol k}$ 具有晶格周期性。","<p>周期势中电子波函数为调幅平面波（布洛赫波）。能量 $E_n(\\boldsymbol k)$ 形成能带，在布里渊区内连续，带间有能隙。近自由电子近似在弱周期势下给出带隙；紧束缚近似从原子轨道线性组合出发。</p>"),
        item("la-k3-2","导体、半导体、绝缘体",["def","thm","app"],"能带填充决定导电性。","<p>价带全满且带隙大（>3eV）= 绝缘体；带隙小（~1eV）= 半导体；价带半满或导带有电子 = 导体。费米能级 $E_F$ 位于带隙中（半导体/绝缘体）或带内（导体）。</p>"),
      ]},
      {"name":"3.2 费米面与有效质量","color":"#c2410c","desc":"$k$ 空间等能面","items":[
        item("la-k3-3","费米面",["def","thm"],"$E(\\boldsymbol k)=E_F$ 在 $k$ 空间的等能面。","<p>费米面是 $T=0$ 时电子占据态与空态的分界。金属费米面的形状决定输运性质（如德哈斯-范阿尔芬效应可测量费米面）。有效质量 $m^*=\\hbar^2/(d^2E/dk^2)$ 描述电子对外力的响应。</p>"),
      ]},
    ]},
    {"id":"la-ch4","num":"第四章","title":"固体输运性质","en":"TRANSPORT PROPERTIES","sub":"电导率、热导率","desc":"电子和声子的输运决定固体的导电和导热性质。","sections":[
      {"name":"4.1 金属导电","color":"#2563eb","desc":"德鲁德模型、玻尔兹曼输运","items":[
        item("la-k4-1","德鲁德模型",["def","thm","app"],"$\\sigma=ne^2\\tau/m^*$，电流密度 $\\boldsymbol j=\\sigma\\boldsymbol E$。","<p>经典自由电子气模型。电子在外电场下加速，被散射（平均自由时间 $\\tau$）。欧姆定律的微观解释。维德曼-弗兰兹定律 $\\kappa/\\sigma=LT$，洛伦兹数 $L=\\pi^2k_B^2/(3e^2)$。</p>"),
        item("la-k4-2","霍尔效应",["def","thm","app"],"霍尔电压 $V_H=IB/(nqd)$，霍尔系数 $R_H=1/(nq)$。","<p>载流子在磁场中受洛伦兹力偏转，形成横向电场。霍尔系数符号确定载流子类型（电子/空穴），大小确定载流子浓度。量子霍尔效应 $R_H=h/(\\nu e^2)$ 是拓扑态的标志。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 34. 材料物理 materials-physics
# ============================================================
SUBJECTS.append({
  "filename":"materials-physics.html",
  "title":"材料物理",
  "eyebrow":"MATERIALS PHYSICS",
  "subtitle":"晶体缺陷 · 扩散 · 相变 · 力学性能 · 功能材料",
  "meta_desc":"材料物理知识体系：晶体缺陷、扩散、相变、力学性能、功能材料",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"晶体缺陷","en":"CRYSTAL DEFECTS","sub":"点、线、面缺陷","desc":"实际晶体存在各种缺陷，决定材料性能。","sections":[
      {"name":"1.1 点缺陷与位错","color":"#2563eb","desc":"空位、间隙、位错","items":[
        item("la-k1-1","位错",["def","thm"],"刃型位错与螺型位错，柏氏矢量 $\\boldsymbol b$。","<p>位错是线缺陷，是材料塑性变形的载体。位错滑移导致屈服，位错强化（加工硬化）提高强度。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"扩散与相变","en":"DIFFUSION & PHASE","sub":"菲克定律、成核生长","desc":"原子扩散与相变是材料制备的基础。","sections":[
      {"name":"2.1 扩散","color":"#7c3aed","desc":"菲克定律","items":[
        item("la-k2-1","菲克定律",["def","thm"],"$J=-D\\partial c/\\partial x$，$\\partial c/\\partial t=D\\partial^2 c/\\partial x^2$。","<p>扩散系数 $D=D_0e^{-Q/RT}$，温度依赖显著。扩散控制固相反应与相变动力学。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 35. 超导物理 superconductivity
# ============================================================
SUBJECTS.append({
  "filename":"superconductivity.html",
  "title":"超导物理",
  "eyebrow":"SUPERCONDUCTIVITY",
  "subtitle":"零电阻 · 迈斯纳效应 · BCS · 高温超导 · 约瑟夫森",
  "meta_desc":"超导物理知识体系：零电阻、迈斯纳效应、BCS、高温超导、约瑟夫森",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"超导基本现象","en":"SUPERCONDUCTING PHENOMENA","sub":"零电阻、迈斯纳","desc":"超导体在临界温度下电阻消失并排斥磁通。","sections":[
      {"name":"1.1 零电阻与迈斯纳","color":"#2563eb","desc":"超导态特征","items":[
        item("la-k1-1","迈斯纳效应",["def","thm"],"$\\boldsymbol B=0$ 内部，完全抗磁性。","<p>超导体不仅零电阻，还将内部磁场完全排出（迈斯纳效应），这是独立于零电阻的特征。$T<T_c$ 时发生。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"BCS 理论","en":"BCS THEORY","sub":"库珀对、能隙","desc":"BCS 理论解释常规超导：电子配对形成库珀对。","sections":[
      {"name":"2.1 库珀对","color":"#7c3aed","desc":"电子-声子相互作用","items":[
        item("la-k2-1","BCS 理论",["def","thm"],"电子通过声子交换形成库珀对，凝聚为超导基态。","<p>库珀对（自旋相反、动量相反）是玻色子，发生玻色凝聚。能隙 $\\Delta\\approx1.76k_BT_c$。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 36. 纳米物理 nanophysics
# ============================================================
SUBJECTS.append({
  "filename":"nanophysics.html",
  "title":"纳米物理",
  "eyebrow":"NANOPHYSICS",
  "subtitle":"量子限域 · 量子点 · 碳纳米管 · 石墨烯 · 纳米器件",
  "meta_desc":"纳米物理知识体系：量子限域效应、量子点与态密度、碳纳米管、纳米器件、近场光学",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"量子限域与低维体系","en":"QUANTUM CONFINEMENT & LOW-DIMENSIONAL","sub":"0D、1D、2D、态密度","desc":"当材料尺寸缩小到纳米量级（~德布罗意波长或激子玻尔半径），量子效应主导性质。","sections":[
      {"name":"1.1 量子限域效应","color":"#2563eb","desc":"态密度离散化","items":[
        item("la-k1-1","量子限域与态密度",["def","thm"],"能隙随尺寸减小而增大，$\\Delta E\\propto1/L^2$；态密度随维度变化。","<p>三维块体（DOS $\\propto\\sqrt{E}$）→二维量子阱（台阶型）→一维量子线（$\\propto1/\\sqrt{E}$ 奇点）→零维量子点（离散 $\\delta$ 函数）。量子限域使能带变为离散能级，量子点因此被称为\"人造原子\"。</p>"),
        item("la-k1-2","量子点与应用",["def","app"],"量子点荧光发射波长由尺寸调控；用于显示、生物标记、单光子源。","<p>量子点的荧光波长随尺寸减小而蓝移（量子限域效应）。CdSe、InP 量子点广泛用于 QLED 显示。量子点还可作为单光子源用于量子通信，以及量子比特用于量子计算。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"碳纳米材料与纳米器件","en":"CARBON NANOMATERIALS & DEVICES","sub":"碳纳米管、纳米器件","desc":"碳纳米管、富勒烯等纳米碳材料具有独特的力学和电学性质。","sections":[
      {"name":"2.1 碳纳米管与纳米器件","color":"#7c3aed","desc":"手性、场效应","items":[
        item("la-k2-1","碳纳米管",["def","thm","app"],"单层石墨烯卷成管，导电性由手性指数 $(n,m)$ 决定。","<p>碳纳米管（CNT）按手性分为金属型（$n-m$ 为 3 的倍数）或半导体型。单壁 CNT 力学强度极高（杨氏模量 ~1 TPa），电学性能优异，可用于场效应晶体管、复合材料、透明电极。</p>"),
        item("la-k2-2","纳米器件与近场效应",["def","app"],"单电子晶体管、纳米线器件、近场光学。","<p>纳米尺度器件出现库仑阻塞（单电子晶体管）、弹道输运、量子干涉等效应。近场扫描光学显微镜（NSOM）突破衍射极限，分辨率达 ~10 nm。纳米机电系统（NEMS）用于超高灵敏度传感。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 37. 拓扑物态 topological-matter
# ============================================================
SUBJECTS.append({
  "filename":"topological-matter.html",
  "title":"拓扑物态",
  "eyebrow":"TOPOLOGICAL MATTER",
  "subtitle":"拓扑绝缘体 · 拓扑半金属 · 陈数 · 边缘态 · 量子反常霍尔",
  "meta_desc":"拓扑物态知识体系：拓扑绝缘体、陈数与Z2不变量、边缘态、拓扑半金属、量子反常霍尔效应",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"拓扑绝缘体","en":"TOPOLOGICAL INSULATORS","sub":"体绝缘、表面金属、陈数","desc":"拓扑绝缘体体内绝缘，表面存在受拓扑保护的金属态，是凝聚态物理的重大突破。","sections":[
      {"name":"1.1 拓扑不变量与量子霍尔","color":"#2563eb","desc":"陈数、Z2、边缘态","items":[
        item("la-k1-1","陈数与 TKNN 不变量",["def","thm"],"$C=\\frac1{2\\pi}\\int_{BZ}\\boldsymbol F\\cdot d\\boldsymbol S$，整数拓扑不变量。","<p>陈数刻画能带的拓扑性质。Thouless-Kohmoto-Nightingale-den Nijs（TKNN）证明整数量子霍尔效应的霍尔电导 $\\sigma_H=Ce^2/h$ 由陈数 $C$ 决定。非零陈数对应无能隙边缘态，边缘态数目等于陈数。</p>"),
        item("la-k1-2","拓扑绝缘体与 Z2 不变量",["def","thm","his"],"Z2 不变量区分时间反演不变的拓扑平庸与非平庸绝缘体。","<p>二维拓扑绝缘体（量子自旋霍尔态）具有一对自旋相反的边缘态，由 Z2 拓扑不变量刻画。三维拓扑绝缘体（如 Bi₂Se₃）具有单个狄拉克锥型表面态。时间反演对称性保护这些态不受非磁性杂质散射。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"拓扑半金属与量子反常霍尔","en":"TOPOLOGICAL SEMIMETALS & QAH","sub":"外尔半金属、狄拉克半金属","desc":"拓扑半金属在能带交叉点处具有受拓扑保护的表面态（费米弧）。","sections":[
      {"name":"2.1 拓扑半金属","color":"#7c3aed","desc":"外尔点、费米弧","items":[
        item("la-k2-1","外尔半金属与狄拉克半金属",["def","thm","app"],"外尔点是动量空间的磁单极子，表面有费米弧。","<p>外尔半金属（如 TaAs）的能带在动量空间外尔点处交叉，低能激发为外尔费米子。外尔点成对出现（手性相反），对应表面态费米弧。狄拉克半金属（如 Cd₃As₂）有四重简并狄拉克点。这些材料可实现手征反常等新奇输运效应。</p>"),
        item("la-k2-2","量子反常霍尔效应",["def","thm","his"],"磁性掺杂拓扑绝缘体实现零磁场下量子化霍尔电导。","<p>量子反常霍尔效应（QAHE）在无外磁场时实现 $\\sigma_H=ne^2/h$。薛其坤团队（2013）在 Cr 掺杂 (Bi,Sb)₂Te₃ 薄膜中首次观测到 QAHE。QAHE 是无耗散边缘态的体现，有望用于低功耗电子学和拓扑量子计算。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 38. 二维材料 2d-materials
# ============================================================
SUBJECTS.append({
  "filename":"2d-materials.html",
  "title":"二维材料",
  "eyebrow":"2D MATERIALS",
  "subtitle":"石墨烯 · MoS2 · 黑磷 · 异质结 · 器件",
  "meta_desc":"二维材料知识体系：石墨烯狄拉克锥、过渡金属硫化物MoS2、黑磷、范德华异质结、二维器件",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"石墨烯与类石墨烯材料","en":"GRAPHENE & BEYOND","sub":"狄拉克锥、MoS₂、黑磷","desc":"二维材料是单原子层厚度的材料，具有块体不具备的新奇性质。Geim 和 Novoselov 于 2004 年剥离出石墨烯。","sections":[
      {"name":"1.1 石墨烯","color":"#2563eb","desc":"线性色散、零带隙","items":[
        item("la-k1-1","石墨烯电子结构",["def","thm"],"线性色散 $E=\\pm\\hbar v_F|\\boldsymbol k|$，$v_F\\approx c/300$。","<p>石墨烯是单层碳原子构成的蜂窝晶格。K 点附近电子行为如无质量狄拉克费米子，导带与价带在狄拉克点接触（零带隙）。载流子迁移率极高（$>10^5\\,\\text{cm}^2/\\text{Vs}$），室温弹道输运，热导率极高。</p>"),
        item("la-k1-2","过渡金属硫化物与黑磷",["def","app"],"MoS₂ 单层为直接带隙半导体；黑磷有可调直接带隙。","<p>MoS₂、WSe₂ 等过渡金属硫化物（TMDC）单层从体相间接带隙变为直接带隙（~1.8 eV），适于光电器件。黑磷（磷烯）具有面内各向异性和可由层数调节的直接带隙（0.3-2 eV），填补石墨烯与 TMDC 之间的能隙空白。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"范德华异质结与二维器件","en":"VDW HETEROSTRUCTURES & DEVICES","sub":"莫尔超晶格、器件","desc":"通过层间堆垛不同二维材料可构建范德华异质结，出现莫尔超晶格与强关联效应。","sections":[
      {"name":"2.1 异质结与器件","color":"#7c3aed","desc":"莫尔、扭转电子学","items":[
        item("la-k2-1","范德华异质结与莫尔超晶格",["def","thm","his"],"不同层间堆垛形成莫尔条纹，产生平带与强关联效应。","<p>二维材料通过范德华力结合，可任意堆垛构建异质结。两层石墨烯以小角度扭转（魔角 ~1.1°）形成莫尔超晶格，出现平带，实现超导与关联绝缘态（曹原等，2018）。扭转电子学（twistronics）成为新研究方向。</p>"),
        item("la-k2-2","二维器件应用",["def","app"],"场效应晶体管、光电器件、柔性电子。","<p>二维材料薄、透明、柔性，适于下一代电子学。MoS₂ 晶体管可实现 1 nm 沟道。二维材料光探测器响应快、灵敏度高。石墨烯用于透明电极、高频晶体管、传感器。异质结太阳能电池和发光二极管也被广泛研究。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 39. 低温物理 low-temperature-physics
# ============================================================
SUBJECTS.append({
  "filename":"low-temperature-physics.html",
  "title":"低温物理",
  "eyebrow":"LOW TEMPERATURE PHYSICS",
  "subtitle":"液氦 · 超流 · 玻色-爱因斯坦凝聚 · 极低温技术",
  "meta_desc":"低温物理知识体系：液氦相变、超流He II、二流体模型、玻色-爱因斯坦凝聚、极低温制冷技术",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"液氦与超流","en":"HELIUM & SUPERFLUIDITY","sub":"λ相变、超流、二流体","desc":"液氦在低温下发生超流相变，展现宏观量子现象。超流是玻色-爱因斯坦凝聚的直接体现。","sections":[
      {"name":"1.1 超流 He II","color":"#2563eb","desc":"零粘滞、量子化涡旋","items":[
        item("la-k1-1","超流 He II 与二流体模型",["def","thm","his"],"$T<T_\\lambda=2.17$ K 时 He-4 超流，零粘滞、熵为零。","<p>He-4 在 $T_\\lambda$ 发生二级相变（λ 相变），从正常流体 He I 变为超流体 He II。Tisza-Landau 二流体模型：He II 由正常流体（$\\rho_n$，携带熵）和超流体（$\\rho_s$，零熵零粘滞）组成。超流组分可无摩擦流动，表现为爬膜效应、喷泉效应。</p>"),
        item("la-k1-2","量子化涡旋与 He-3 超流",["def","thm"],"环流量子 $\\kappa=h/(2m_4)$；He-3 有超流 A/B 相。","<p>超流 He II 中的涡旋环流量子化 $\\oint\\mathbf{v}\\cdot d\\mathbf{l}=n\\kappa$。He-3（费米子）在 mK 温度下通过 Cooper 配对发生超流，有 A 相（各向异性 p 波）和 B 相（各向同性），是拓扑超流候选。Kapitza 因发现超流获 1978 年诺贝尔奖。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"玻色-爱因斯坦凝聚与制冷技术","en":"BEC & REFRIGERATION","sub":"BEC、激光冷却、稀释制冷","desc":"冷原子气体可实现玻色-爱因斯坦凝聚。极低温技术是现代凝聚态物理的基础。","sections":[
      {"name":"2.1 BEC 与制冷","color":"#7c3aed","desc":"激光冷却、稀释制冷机","items":[
        item("la-k2-1","玻色-爱因斯坦凝聚（BEC）",["def","thm","his"],"$T<T_c$ 时宏观数目的玻色子占据基态。","<p>玻色-爱因斯坦凝聚是玻色子在低温下发生的相变，宏观数目粒子占据单粒子基态。Cornell、Wieman、Ketterle（1995）在铷原子气中首次实现 BEC，获 2001 年诺贝尔奖。BEC 是研究量子多体物理的理想平台，可实现原子激光、超冷分子等。</p>"),
        item("la-k2-2","极低温制冷技术",["def","app"],"激光冷却 $\\sim\\mu$K，稀释制冷机 $\\sim$mK。","<p>激光冷却（Doppler 冷却、偏振梯度冷却）将原子冷却到 $\\mu$K 量级。磁光阱（MOT）俘获冷原子。稀释制冷机利用 He-3/He-4 混合物相变，可达 ~10 mK，是量子计算和超导实验的核心设备。绝热去磁制冷可达更低温度。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 40. 材料制备技术 materials-preparation
# ============================================================
SUBJECTS.append({
  "filename":"materials-preparation.html",
  "title":"材料制备技术",
  "eyebrow":"MATERIALS PREPARATION",
  "subtitle":"烧结 · 薄膜沉积 · 单晶生长 · CVD · MBE",
  "meta_desc":"材料制备技术知识体系：粉末冶金与烧结、化学气相沉积CVD、物理气相沉积PVD、分子束外延MBE、单晶生长",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"薄膜与单晶生长","en":"THIN FILMS & CRYSTAL GROWTH","sub":"CVD、PVD、MBE","desc":"薄膜制备是半导体与材料科学的核心工艺，决定器件性能。","sections":[
      {"name":"1.1 气相沉积技术","color":"#2563eb","desc":"CVD、PVD、MBE","items":[
        item("la-k1-1","化学气相沉积（CVD）",["def","app"],"气相前驱体在基片上反应沉积薄膜。","<p>CVD 利用前驱体气体在加热基片上发生化学反应沉积薄膜。包括常压 CVD（APCVD）、低压 CVD（LPCVD）、等离子体增强 CVD（PECVD）、金属有机 CVD（MOCVD）。CVD 适合台阶覆盖好的薄膜，如 SiO₂、Si₃N₄、多晶硅。</p>"),
        item("la-k1-2","分子束外延（MBE）与 PVD",["def","app"],"MBE 精度达单原子层；PVD 包括溅射和蒸发。","<p>MBE 在超高真空下蒸发源形成分子束，逐层外延生长，精度达单原子层，用于高质量半导体异质结（如 GaAs/AlGaAs）和量子阱。PVD 包括磁控溅射（高沉积率、低损伤）和电子束蒸发，用于金属薄膜和介质薄膜。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"烧结与单晶生长","en":"SINTERING & SINGLE CRYSTAL GROWTH","sub":"陶瓷烧结、提拉法","desc":"粉末冶金烧结制备块体材料；单晶生长获得高质量晶体。","sections":[
      {"name":"2.1 烧结与单晶","color":"#7c3aed","desc":"致密化、晶体生长","items":[
        item("la-k2-1","粉末冶金与烧结",["def","app"],"粉末压实后高温烧结实现致密化。","<p>粉末冶金包括混粉、成型（压制）、烧结。烧结通过扩散、蒸发-凝聚、粘性流动等机制使粉末颗粒结合、致密化。热压烧结、放电等离子烧结（SPS）可加速致密化。广泛用于陶瓷、硬质合金、粉末冶金零件。</p>"),
        item("la-k2-2","单晶生长技术",["def","app"],"提拉法（Czochralski）、区熔法、布里奇曼法。","<p>Czochralski 提拉法生长大尺寸单晶（如 Si 锭、蓝宝石、LiNbO₃）。区熔法（FZ）制备高纯硅单晶。布里奇曼法用于化合物半导体（GaAs、CdTe）。水热法生长 ZnO、石英单晶。单晶质量直接影响器件性能。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 41. 材料测试技术 materials-characterization
# ============================================================
SUBJECTS.append({
  "filename":"materials-characterization.html",
  "title":"材料测试技术",
  "eyebrow":"MATERIALS CHARACTERIZATION",
  "subtitle":"XRD · SEM · TEM · AFM · XPS · Raman",
  "meta_desc":"材料测试技术知识体系：X射线衍射XRD、扫描电镜SEM、透射电镜TEM、原子力显微镜AFM、XPS、拉曼光谱",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"结构表征","en":"STRUCTURAL CHARACTERIZATION","sub":"XRD、TEM、SEM","desc":"X 射线衍射与电子显微术分析材料晶体结构与形貌。","sections":[
      {"name":"1.1 XRD 与电子显微","color":"#2563eb","desc":"晶体结构、形貌","items":[
        item("la-k1-1","X 射线衍射（XRD）",["def","thm","app"],"布拉格方程 $2d\\sin\\theta=n\\lambda$。","<p>XRD 通过衍射花样测定晶体结构、晶格常数、物相、晶粒尺寸、应变。粉末 XRD 用于物相定性定量分析；高分辨 XRD 用于外延薄膜应变分析。Scherrer 公式 $D=K\\lambda/(\\beta\\cos\\theta)$ 估算晶粒尺寸。</p>"),
        item("la-k1-2","电子显微镜（SEM/TEM）",["def","app"],"TEM 原子分辨率；SEM 表面形貌。","<p>扫描电镜（SEM）用聚焦电子束扫描样品，二次电子/背散射电子成像，观察表面形貌与成分分布，分辨率 ~1 nm。透射电镜（TEM）电子穿透薄样品成像，可达原子分辨率（~0.1 nm），可分析晶体结构、缺陷、成分（EDS、EELS）。球差校正 TEM 进一步提升分辨率。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"成分、表面与光谱分析","en":"COMPOSITION, SURFACE & SPECTROSCOPY","sub":"XPS、AFM、Raman","desc":"X 射线光电子能谱分析成分与化学态；拉曼光谱分析振动模式；AFM 表征表面形貌。","sections":[
      {"name":"2.1 表面与光谱分析","color":"#7c3aed","desc":"化学态、形貌、振动","items":[
        item("la-k2-1","XPS 与 AFM",["def","app"],"XPS 分析表面元素与化学态；AFM 测量表面形貌。","<p>X 射线光电子能谱（XPS/ESCA）利用光电效应测量电子结合能，分析表面（~10 nm）元素组成与化学态（价态）。原子力显微镜（AFM）用微悬臂探针扫描表面，可获得原子级分辨率形貌，也可测量力学、电学、磁学性质。</p>"),
        item("la-k2-2","拉曼光谱与其他谱学",["def","app"],"拉曼散射分析分子振动；紫外-可见-红外光谱分析能带。","<p>拉曼光谱基于非弹性散射，提供分子振动、晶体结构、应力、缺陷信息，是二维材料（石墨烯、MoS₂）的重要表征手段。紫外-可见吸收光谱确定带隙；红外光谱分析化学键；光致发光（PL）光谱研究载流子复合与缺陷态。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 42. 半导体物理 semiconductor-physics
# ============================================================
SUBJECTS.append({
  "filename":"semiconductor-physics.html",
  "title":"半导体物理",
  "eyebrow":"SEMICONDUCTOR PHYSICS",
  "subtitle":"能带 · 载流子 · 掺杂 · PN 结 · MOS · 输运",
  "meta_desc":"半导体物理知识体系：能带、载流子、掺杂、PN结、MOS、输运",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"半导体能带与载流子","en":"BANDS & CARRIERS","sub":"本征、掺杂、载流子浓度","desc":"半导体的导电性由能带与载流子决定。本章讨论本征与掺杂半导体。","sections":[
      {"name":"1.1 载流子浓度","color":"#2563eb","desc":"本征与非本征","items":[
        item("la-k1-1","载流子浓度",["def","thm"],"$n_i=\\sqrt{N_cN_v}e^{-E_g/2kT}$，$n_0p_0=n_i^2$。","<p>本征载流子浓度 $n_i$ 由带隙 $E_g$ 决定。掺杂引入施主/受主，改变费米能级与多数载流子浓度。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"PN 结与 MOS","en":"PN JUNCTION & MOS","sub":"耗尽层、能带弯曲","desc":"PN 结是半导体器件的核心。MOS 结构是现代晶体管基础。","sections":[
      {"name":"2.1 PN 结","color":"#7c3aed","desc":"整流特性","items":[
        item("la-k2-1","PN 结 I-V",["def","thm"],"$I=I_0(e^{qV/kT}-1)$，肖克莱方程。","<p>正向偏置注入少数载流子，电流指数增长；反向偏置电流几乎为零（击穿除外）。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 43. 半导体材料 semiconductor-materials
# ============================================================
SUBJECTS.append({
  "filename":"semiconductor-materials.html",
  "title":"半导体材料",
  "eyebrow":"SEMICONDUCTOR MATERIALS",
  "subtitle":"硅 · 锗 · 砷化镓 · 氮化镓 · 碳化硅",
  "meta_desc":"半导体材料知识体系：元素半导体Si/Ge、化合物半导体GaAs/InP、宽禁带GaN/SiC、有机半导体、氧化物半导体",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"半导体材料分类","en":"SEMICONDUCTOR MATERIALS","sub":"元素、化合物、宽禁带","desc":"半导体材料分元素半导体与化合物半导体，是电子工业的基石。","sections":[
      {"name":"1.1 元素与化合物半导体","color":"#2563eb","desc":"Si、GaAs、GaN","items":[
        item("la-k1-1","材料代际与特性",["def","thm","app"],"Si 第一代，GaAs 第二代，GaN/SiC 第三代（宽禁带）。","<p>Si（$E_g=1.12$ eV）工艺成熟，用于逻辑与存储集成电路。GaAs（$E_g=1.42$ eV）电子迁移率高，用于高频、微波、光电器件。InP 用于长波长光通信激光器。GaN/SiC 宽禁带（3.4/3.3 eV）用于大功率、高频、高温器件和蓝光 LED。</p>"),
        item("la-k1-2","有机与氧化物半导体",["def","app"],"有机半导体柔性透明；氧化物半导体高迁移率。","<p>有机半导体（如 P3HT、ITIC）用于有机发光二极管（OLED）、有机太阳能电池（OPV）、有机场效应晶体管（OFET），具有柔性、可印刷等优势。氧化物半导体（如 a-IGZO）高迁移率、低关断电流，用于平板显示背板和透明电子学。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"半导体物性与缺陷","en":"MATERIAL PROPERTIES & DEFECTS","sub":"能带、迁移率、缺陷","desc":"半导体的电学、光学性质由能带结构和缺陷决定。","sections":[
      {"name":"2.1 物性与缺陷工程","color":"#7c3aed","desc":"迁移率、载流子、缺陷","items":[
        item("la-k2-1","载流子输运与迁移率",["def","thm"],"$\\mu=q\\tau/m^*$，受晶格散射和电离杂质散射限制。","<p>载流子迁移率 $\\mu$ 决定器件速度。散射机制：声学声子散射（$\\mu\\propto T^{-3/2}$）、电离杂质散射（$\\mu\\propto T^{3/2}$）、光学声子散射等。GaN/AlGaN 异质结的二维电子气迁移率极高，用于 HEMT。</p>"),
        item("la-k2-2","半导体缺陷与掺杂",["def","app"],"点缺陷、位错、掺杂调控载流子。","<p>半导体缺陷包括点缺陷（空位、间隙、反位）、线缺陷（位错）、面缺陷（晶界、堆垛层错）。缺陷作为深能级俘获载流子，降低寿命和迁移率。掺杂（施主/受主）精确调控载流子浓度。半绝缘 GaAs 利用 EL2 深能级实现高阻。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 44. 半导体器件 semiconductor-devices
# ============================================================
SUBJECTS.append({
  "filename":"semiconductor-devices.html",
  "title":"半导体器件",
  "eyebrow":"SEMICONDUCTOR DEVICES",
  "subtitle":"二极管 · BJT · MOSFET · HEMT · 光电探测器",
  "meta_desc":"半导体器件知识体系：PN结二极管、BJT双极型晶体管、MOSFET场效应晶体管、HEMT高电子迁移率晶体管、光电探测器、太阳能电池",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"晶体管器件","en":"TRANSISTORS","sub":"BJT、MOSFET、HEMT","desc":"晶体管是电子电路的核心放大与开关器件，是信息时代的基础。","sections":[
      {"name":"1.1 场效应与双极型晶体管","color":"#2563eb","desc":"MOSFET、BJT、HEMT","items":[
        item("la-k1-1","MOSFET 工作原理",["def","thm"],"栅压调制沟道，$I_D$ 分线性区与饱和区。","<p>MOSFET 是数字集成电路的基本单元。栅压控制半导体表面反型层形成沟道。线性区 $I_D\\approx\\mu C_{ox}\\frac{W}{L}[(V_{GS}-V_{TH})V_{DS}-\\frac12 V_{DS}^2]$；饱和区 $I_D\\approx\\frac12\\mu C_{ox}\\frac{W}{L}(V_{GS}-V_{TH})^2$。亚阈值摆幅 $S$ 决定关断电流，是低功耗设计关键。</p>"),
        item("la-k1-2","BJT 与 HEMT",["def","thm","app"],"BJT 电流放大；HEMT 利用二维电子气实现高频。","<p>双极型晶体管（BJT）利用少数载流子注入实现电流放大（$\\beta=I_C/I_B$），用于模拟电路。高电子迁移率晶体管（HEMT）利用调制掺杂异质结（如 AlGaN/GaN）形成高迁移率二维电子气，用于毫米波、太赫兹高频放大和功率器件。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"光电器件与新兴器件","en":"OPTOELECTRONIC & EMERGING DEVICES","sub":"LED、激光器、探测器、太阳能电池","desc":"半导体光电器件实现光电转换，包括 LED、激光器、光电探测器和太阳能电池。","sections":[
      {"name":"2.1 光电器件","color":"#7c3aed","desc":"发光、探测、光伏","items":[
        item("la-k2-1","LED 与半导体激光器",["def","thm","app"],"PN 结注入载流子复合发光；激光器有谐振腔实现受激辐射。","<p>发光二极管（LED）利用 PN 结注入电子-空穴对，辐射复合发光。GaN 基蓝光 LED（2014 诺奖）使白光 LED 成为主流照明。半导体激光器（LD）在 LED 基础上加入光学谐振腔，实现受激辐射，用于光通信、光盘、激光加工。</p>"),
        item("la-k2-2","光电探测器与太阳能电池",["def","thm","app"],"光生伏特效应；光伏效率受 Shockley-Queisser 极限限制。","<p>光电探测器（PD）吸收光子产生电子-空穴对，在内建电场下分离形成光电流。PIN、APD、SPAD 用于不同灵敏度需求。太阳能电池利用光伏效应发电，单结效率受 Shockley-Queisser 极限（~33%）限制。多结、钙钛矿、量子点电池提升效率。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 45. 半导体工艺 semiconductor-process
# ============================================================
SUBJECTS.append({
  "filename":"semiconductor-process.html",
  "title":"半导体工艺",
  "eyebrow":"SEMICONDUCTOR PROCESS",
  "subtitle":"光刻 · 刻蚀 · 离子注入 · 薄膜沉积 · CMP · 封装",
  "meta_desc":"半导体工艺知识体系：光刻EUV、干法刻蚀、离子注入、薄膜沉积CVD/PVD/ALD、化学机械抛光CMP、封装测试",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"前道工艺","en":"FRONT-END OF LINE","sub":"光刻、刻蚀、离子注入","desc":"前道工艺在晶圆上制造晶体管，是集成电路制造的核心。","sections":[
      {"name":"1.1 光刻与刻蚀","color":"#2563eb","desc":"图形转移","items":[
        item("la-k1-1","光刻技术",["def","app"],"曝光+显影将掩模图形转移到光刻胶。","<p>光刻是图形转移的核心。光源从 g 线（436 nm）、i 线（365 nm）、KrF（248 nm）、ArF（193 nm）到 EUV（13.5 nm）。分辨率 $R=k_1\\lambda/NA$。浸没式光刻增加 NA。EUV 是 7 nm 及以下先进节点的关键技术，采用激光等离子体光源。</p>"),
        item("la-k1-2","刻蚀与离子注入",["def","app"],"干法刻蚀各向异性；离子注入精确掺杂。","<p>刻蚀将光刻胶图形转移到下层薄膜。湿法刻蚀各向同性，用于去除；干法（反应离子刻蚀 RIE、ICP）各向异性，用于精细图形。离子注入将掺杂离子加速注入半导体，精确控制剂量和深度，注入后退火激活掺杂并修复损伤。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"薄膜、平坦化与后道封装","en":"FILMS, CMP & BACK-END","sub":"ALD、CMP、互连、封装","desc":"薄膜沉积、化学机械抛光、金属互连和封装测试构成完整工艺链。","sections":[
      {"name":"2.1 后道工艺与封装","color":"#7c3aed","desc":"ALD、CMP、Cu互连","items":[
        item("la-k2-1","薄膜沉积与平坦化",["def","app"],"ALD 原子级精度；CMP 全局平坦化。","<p>原子层沉积（ALD）通过自限制表面反应实现单原子层精度沉积，台阶覆盖极佳，用于高 k 介质（HfO₂）和阻挡层。化学机械抛光（CMP）结合化学腐蚀和机械研磨实现晶圆全局平坦化，是多层互连工艺的基础。</p>"),
        item("la-k2-2","金属互连与封装测试",["def","app"],"Cu 互连低阻；先进封装提升集成度。","<p>金属互连从 Al 发展到 Cu（大马士革工艺），降低电阻。低 k 介质降低互连电容。后道工艺（BEOL）构建多层金属互连。封装包括传统引线键合、倒装焊、硅通孔（TSV）、晶圆级封装（WLP）、扇出型封装（FOWLP）、Chiplet 等，提升集成度与性能。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 46. 相对论 relativity
# ============================================================
SUBJECTS.append({
  "filename":"relativity.html",
  "title":"相对论",
  "eyebrow":"RELATIVITY",
  "subtitle":"狭义相对论 · 洛伦兹变换 · 时空结构 · 广义相对论 · 引力波",
  "meta_desc":"相对论知识体系：狭义相对论基本原理、洛伦兹变换、钟慢尺缩、质能关系、闵可夫斯基时空、广义相对论、爱因斯坦场方程、引力波",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"狭义相对论","en":"SPECIAL RELATIVITY","sub":"基本原理、洛伦兹变换","desc":"狭义相对论基于光速不变原理与相对性原理，统一了时间和空间。","sections":[
      {"name":"1.1 基本原理与洛伦兹变换","color":"#2563eb","desc":"光速不变、时空变换","items":[
        item("la-k1-1","洛伦兹变换",["def","thm","his"],"$x'=\\gamma(x-vt)$，$t'=\\gamma(t-vx/c^2)$，$\\gamma=1/\\sqrt{1-v^2/c^2}$。","<p>爱因斯坦（1905）基于两条基本假设：①相对性原理（物理定律在所有惯性系中形式相同）；②光速不变原理（真空中光速在所有惯性系中相同）。洛伦兹变换取代伽利略变换。逆变换只需将 $v\\to-v$。</p>"),
        item("la-k1-2","相对论效应",["thm","der","app"],"钟慢 $\\Delta t'=\\gamma\\Delta\\tau$，尺缩 $L=L_0/\\gamma$。","<p>运动时钟变慢（时间膨胀），$\\Delta\\tau$ 为固有时间。运动物体沿运动方向收缩（长度收缩），$L_0$ 为固有长度。同时性是相对的：在一个参考系中同时的事件，在另一参考系中可能不同时。</p>"),
      ]},
      {"name":"1.2 相对论动力学","color":"#7c3aed","desc":"质能关系、四维动量","items":[
        item("la-k1-3","质能关系",["def","thm","his"],"$E=mc^2$，$E^2=(pc)^2+(m_0c^2)^2$。","<p>相对论能量 $E=\\gamma m_0 c^2$，动量 $p=\\gamma m_0 v$。静能 $E_0=m_0c^2$。质能等价是核能利用的理论基础。无质量粒子（光子）$E=pc$。四维动量 $p^\\mu=(E/c,\\boldsymbol p)$，模长不变 $p^\\mu p_\\mu=m_0^2c^2$。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"闵可夫斯基时空","en":"MINKOWSKI SPACETIME","sub":"时空图、光锥、因果性","desc":"闵可夫斯基将时间和空间统一为四维时空，用几何方式描述相对论。","sections":[
      {"name":"2.1 时空结构","color":"#0f766e","desc":"时空间隔、光锥","items":[
        item("la-k2-1","时空间隔",["def","thm"],"$ds^2=c^2dt^2-dx^2-dy^2-dz^2$，洛伦兹不变量。","<p>时空间隔在洛伦兹变换下不变。$ds^2>0$ 类时（有因果关系），$ds^2=0$ 类光（光锥上），$ds^2<0$ 类空（无因果关系）。光锥将时空分为因果关联区和非关联区。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"广义相对论","en":"GENERAL RELATIVITY","sub":"等效原理、爱因斯坦方程","desc":"引力是时空弯曲的几何效应，由物质和能量的分布决定。","sections":[
      {"name":"3.1 等效原理与场方程","color":"#2563eb","desc":"引力即几何","items":[
        item("la-k3-1","等效原理",["def","thm","his"],"局部引力场与加速参考系等效（弱等效原理）。","<p>爱因斯坦等效原理：在足够小的时空区域内，引力效应与加速度效应不可区分。自由下落参考系中引力消失。这将引力几何化，是广义相对论的基石。</p>"),
        item("la-k3-2","爱因斯坦场方程",["def","thm","his"],"$G_{\\mu\\nu}+\\Lambda g_{\\mu\\nu}=\\frac{8\\pi G}{c^4}T_{\\mu\\nu}$。","<p>左边爱因斯坦张量 $G_{\\mu\\nu}=R_{\\mu\\nu}-\\frac12 Rg_{\\mu\\nu}$ 描述时空曲率，右边能量动量张量 $T_{\\mu\\nu}$ 描述物质分布。惠勒：\"物质告诉时空如何弯曲，时空告诉物质如何运动。\"$\\Lambda$ 为宇宙学常数。</p>"),
      ]},
      {"name":"3.2 广义相对论的检验","color":"#7c3aed","desc":"经典检验、引力波","items":[
        item("la-k3-3","经典实验验证",["thm","his","app"],"水星近日点进动、光线引力偏折、引力红移。","<p>广义相对论的三大经典检验：①水星近日点每百年进动 43\"；②日食时星光在太阳附近偏折 1.75\"；③引力红移（庞德-雷布卡实验）。2015 年 LIGO 首次直接探测到引力波，验证了广义相对论的预言。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 47. 宇宙学 cosmology
# ============================================================
SUBJECTS.append({
  "filename":"cosmology.html",
  "title":"宇宙学",
  "eyebrow":"COSMOLOGY",
  "subtitle":"大爆炸 · 膨胀 · CMB · 暗物质 · 暗能量 · 暴涨",
  "meta_desc":"宇宙学知识体系：哈勃定律、弗里德曼方程、热大爆炸、宇宙微波背景、原初核合成、暗物质、暗能量、暴涨",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"膨胀宇宙","en":"EXPANDING UNIVERSE","sub":"哈勃定律、弗里德曼方程","desc":"宇宙在膨胀，起源于大爆炸。本章讨论宇宙学基本方程和宇宙学原理。","sections":[
      {"name":"1.1 弗里德曼方程","color":"#2563eb","desc":"宇宙动力学","items":[
        item("la-k1-1","弗里德曼方程",["def","thm"],"$\\left(\\frac{\\dot a}{a}\\right)^2=\\frac{8\\pi G}{3}\\rho-\\frac{kc^2}{a^2}+\\frac{\\Lambda c^2}{3}$。","<p>基于宇宙学原理（均匀各向同性）和广义相对论。尺度因子 $a(t)$ 描述宇宙膨胀。$\\rho$ 为物质能量密度，$k$ 为空间曲率（$k=0$ 平坦，$k=\\pm1$ 弯曲），$\\Lambda$ 为宇宙学常数（暗能量）。哈勃参数 $H=\\dot a/a$。</p>"),
        item("la-k1-2","哈勃定律",["def","thm","his"],"$v=H_0 d$，星系退行速度与距离成正比。","<p>哈勃（1929）发现星系光谱红移与距离成正比，表明宇宙在膨胀。当前哈勃常数 $H_0\\approx70\\,\\text{km/s/Mpc}$。哈勃时间 $1/H_0\\approx140$ 亿年，与宇宙年龄 138 亿年接近。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"热大爆炸","en":"HOT BIG BANG","sub":"CMB、核合成、暴涨","desc":"早期宇宙炽热致密，经历核合成与复合，留下微波背景辐射。","sections":[
      {"name":"2.1 CMB 与原初核合成","color":"#7c3aed","desc":"早期宇宙遗迹","items":[
        item("la-k2-1","宇宙微波背景辐射",["def","thm","his"],"$T\\approx2.725$ K 黑体谱，各向异性 $\\sim10^{-5}$。","<p>CMB 是复合期（$z\\sim1100$，$T\\sim3000$ K）光子与物质脱耦后自由传播至今的遗迹，是大爆炸的直接证据。COBE、WMAP、Planck 卫星精确测量了 CMB 的各向异性，支持 $\\Lambda$CDM 模型。</p>"),
        item("la-k2-2","原初核合成",["thm","der","app"],"大爆炸后 3 分钟内形成 H、He、Li 等轻元素。","<p>宇宙温度降至 1 MeV 以下时，中子和质子结合形成轻核。预言的 He-4 丰度（~25%）、氘、Li-7 与观测一致，是大爆炸理论的关键证据。</p>"),
      ]},
      {"name":"2.2 暴涨理论","color":"#0f766e","desc":"指数膨胀","items":[
        item("la-k2-3","宇宙暴涨",["def","thm"],"极早期宇宙经历 $a\\propto e^{Ht}$ 的指数膨胀。","<p>古斯（1981）提出暴涨理论，解释了视界问题（为何宇宙均匀）和平性问题（为何 $k\\approx0$）。暴涨期间量子涨落被拉伸为宇宙大尺度结构的种子。暴涨预言近标度不变的原初功率谱，与 CMB 观测一致。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"暗物质与暗能量","en":"DARK MATTER & DARK ENERGY","sub":"未知成分","desc":"宇宙中约 95% 的能量由不发光的暗物质和暗能量构成。","sections":[
      {"name":"3.1 暗物质与暗能量","color":"#c2410c","desc":"宇宙主要成分","items":[
        item("la-k3-1","暗物质",["def","thm","app"],"占宇宙约 27%，引力效应明显但不发光。","<p>暗物质证据：星系旋转曲线、引力透镜、星系团动力学。冷暗物质（CDM）模型成功解释大尺度结构。候选者：WIMP、轴子等，但尚未直接探测到。</p>"),
        item("la-k3-2","暗能量",["def","thm","his"],"占宇宙约 68%，驱动宇宙加速膨胀。","<p>1998 年 Ia 型超新星观测发现宇宙加速膨胀，暗示存在负压的暗能量。最简单的解释是宇宙学常数 $\\Lambda$。暗能量本质未知，是物理学最大谜团之一。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 48. 黑洞物理 black-hole-physics
# ============================================================
SUBJECTS.append({
  "filename":"black-hole-physics.html",
  "title":"黑洞物理",
  "eyebrow":"BLACK HOLE PHYSICS",
  "subtitle":"事件视界 · 史瓦西解 · 克尔黑洞 · 霍金辐射 · 黑洞热力学",
  "meta_desc":"黑洞物理知识体系：事件视界、史瓦西解、克尔黑洞、霍金辐射、贝肯斯坦-霍金熵、信息悖论",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"经典黑洞解","en":"CLASSICAL BLACK HOLES","sub":"史瓦西、克尔、RN","desc":"广义相对论预言黑洞。本章讨论经典黑洞解与事件视界。","sections":[
      {"name":"1.1 黑洞解","color":"#2563eb","desc":"球对称与旋转黑洞","items":[
        item("la-k1-1","史瓦西黑洞",["def","thm","his"],"$r_s=\\frac{2GM}{c^2}$，事件视界。","<p>史瓦西（1916）求得球对称真空解。在 $r=r_s$ 处坐标奇异性即事件视界，任何物质（包括光）一旦越过视界无法逃逸。奇点在 $r=0$。黑洞无毛定理：稳态黑洞仅由质量 $M$、电荷 $Q$、角动量 $J$ 三个参数描述。</p>"),
        item("la-k1-2","克尔黑洞",["def","thm"],"旋转黑洞，$a=J/(Mc)$，内外视界。","<p>克尔（1963）求得旋转黑洞解。旋转黑洞有能层（ergosphere），其内粒子必须随黑洞旋转。彭罗斯过程可从克尔黑洞提取旋转能。最大旋转 $a=GM/c^2$（极端克尔黑洞）。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"霍金辐射与黑洞热力学","en":"HAWKING RADIATION & THERMODYNAMICS","sub":"量子黑洞","desc":"黑洞具有温度与熵，通过霍金辐射蒸发。这是量子引力的重要窗口。","sections":[
      {"name":"2.1 霍金辐射与熵","color":"#7c3aed","desc":"量子效应","items":[
        item("la-k2-1","霍金辐射",["def","thm","his"],"$T_H=\\frac{\\hbar c^3}{8\\pi GMk_B}$，$S_{BH}=\\frac{k_B c^3 A}{4\\hbar G}$。","<p>霍金（1974）证明黑洞并非完全黑，而是以温度 $T_H$ 辐射热谱。视界附近虚粒子对中负能粒子落入黑洞，正能粒子逃逸。贝肯斯坦-霍金熵与视界面积 $A$ 成正比，是信息论与引力的深刻联系。</p>"),
        item("la-k2-2","黑洞热力学与信息悖论",["thm","der"],"黑洞力学四定律类比热力学四定律。","<p>视界面积不减类比熵增（热力学第二定律）。霍金辐射使黑洞蒸发，若蒸发完全则信息丢失，与量子力学幺正性矛盾（信息悖论）。候选解决方案：全息原理、AdS/CFT 对偶、火墙假说等。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 49. 粒子物理 particle-physics
# ============================================================
SUBJECTS.append({
  "filename":"particle-physics.html",
  "title":"粒子物理",
  "eyebrow":"PARTICLE PHYSICS",
  "subtitle":"夸克 · 轻子 · 规范玻色子 · 标准模型 · 希格斯 · 中微子",
  "meta_desc":"粒子物理知识体系：三代费米子、规范玻色子、标准模型、希格斯机制、电弱统一、量子色动力学、中微子振荡",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"基本粒子与标准模型","en":"STANDARD MODEL","sub":"三代费米子、规范玻色子","desc":"物质由三代夸克与轻子构成，相互作用由规范玻色子传递。标准模型是粒子物理的核心。","sections":[
      {"name":"1.1 标准模型粒子","color":"#2563eb","desc":"费米子与玻色子","items":[
        item("la-k1-1","标准模型粒子谱",["def","thm"],"6 夸克 + 6 轻子 + 规范玻色子 + 希格斯玻色子。","<p>三代夸克（u/d, c/s, t/b）与三代轻子（e/$\\nu_e$, $\\mu$/$\\nu_\\mu$, $\\tau$/$\\nu_\\tau$）。规范玻色子：光子 $\\gamma$（电磁）、$W^\\pm/Z^0$（弱）、胶子 $g$（强）。希格斯玻色子赋予质量。所有粒子已被实验发现（2012 年发现希格斯）。</p>"),
        item("la-k1-2","夸克与色荷",["def","thm"],"夸克有 3 色，禁闭在强子中。","<p>夸克带分数电荷（u 型 +2/3e，d 型 -1/3e）和色荷（红、绿、蓝）。由于色禁闭，自由夸克无法直接观测，只能以介子（qq̄）或重子（qqq）形式存在。质子=uud，中子=udd。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"基本相互作用","en":"FUNDAMENTAL INTERACTIONS","sub":"电弱统一、QCD","desc":"四种基本相互作用中，电磁与弱力已统一为电弱相互作用，强力由 QCD 描述。","sections":[
      {"name":"2.1 电弱统一与希格斯机制","color":"#7c3aed","desc":"自发对称破缺","items":[
        item("la-k2-1","希格斯机制",["def","thm","his"],"自发对称破缺赋予 W/Z 质量，光子保持无质量。","<p>希格斯场真空期望值破缺 $SU(2)_L\\times U(1)_Y\\to U(1)_{EM}$。$W^\\pm$ 和 $Z^0$ 获得质量（约 80/91 GeV），光子无质量。温伯格角 $\\theta_W$ 联系电磁与弱作用耦合常数。2012 年 LHC 发现希格斯玻色子（125 GeV）。</p>"),
        item("la-k2-2","量子色动力学（QCD）",["def","thm"],"$SU(3)_C$ 规范理论，渐近自由与色禁闭。","<p>QCD 是强相互作用的规范理论。渐近自由：高能（短程）下耦合变弱，可用微扰论（如深度非弹性散射）。色禁闭：低能下耦合变强，夸克禁闭在强子内。格点 QCD 用数值方法处理非微扰区域。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"中微子与超出标准模型","en":"NEUTRINOS & BEYOND SM","sub":"中微子振荡、新物理","desc":"中微子振荡表明中微子有质量，超出标准模型。暗物质、暗能量等也需要新物理。","sections":[
      {"name":"3.1 中微子与新物理","color":"#0f766e","desc":"中微子振荡、B 物理","items":[
        item("la-k3-1","中微子振荡",["def","thm","his"],"$\\nu_\\alpha\\leftrightarrow\\nu_\\beta$ 振荡，证明中微子有质量。","<p>中微子味本征态与质量本征态不重合，导致振荡。振荡概率由混合角（PMNS 矩阵）和质量平方差决定。大气中微子、太阳中微子、反应堆中微子实验证实了振荡现象。标准模型需扩展以容纳中微子质量。</p>"),
        item("la-k3-2","超出标准模型的线索",["def","app"],"暗物质、暗能量、正反物质不对称、引力量子化。","<p>标准模型无法解释：暗物质、暗能量、宇宙中正反物质不对称、引力的量子化、中微子质量起源。候选理论：超对称（SUSY）、大统一理论（GUT）、弦论等。LHC 正在寻找新物理的迹象。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 50. 规范场论 gauge-theory
# ============================================================
SUBJECTS.append({
  "filename":"gauge-theory.html",
  "title":"规范场论",
  "eyebrow":"GAUGE THEORY",
  "subtitle":"规范对称性 · Yang-Mills · 自发破缺 · 重整化 · 反常",
  "meta_desc":"规范场论知识体系：局域规范对称性、杨-米尔斯理论、规范协变导数、自发对称破缺、重整化、手征反常",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"规范对称性与 Yang-Mills 理论","en":"GAUGE SYMMETRY & YANG-MILLS","sub":"局域对称、规范场、场强","desc":"规范场论以局域对称性为基础，杨-米尔斯理论是非阿贝尔规范场的核心，是标准模型的数学框架。","sections":[
      {"name":"1.1 规范协变导数与场强","color":"#2563eb","desc":"非阿贝尔规范场","items":[
        item("la-k1-1","规范协变导数",["def","thm"],"$D_\\mu=\\partial_\\mu-ig A_\\mu^a T^a$，场强 $F_{\\mu\\nu}^a=\\partial_\\mu A_\\nu^a-\\partial_\\nu A_\\mu^a+gf^{abc}A_\\mu^bA_\\nu^c$。","<p>要求拉氏量在局域规范变换 $\\psi(x)\\to U(x)\\psi(x)$ 下不变，需引入规范场 $A_\\mu=A_\\mu^aT^a$。非阿贝尔群（$[T^a,T^b]=if^{abc}T^c$）的场强含自相互作用项 $gf^{abc}A^bA^c$，这是 QCD 渐近自由和色禁闭的根源。</p>"),
        item("la-k1-2","Yang-Mills 拉氏量",["def","thm"],"$\\mathcal{L}_{YM}=-\\frac14 F_{\\mu\\nu}^aF^{a\\mu\\nu}$。","<p>杨-米尔斯拉氏量是非阿贝尔规范场的动能项。在阿贝尔情况（QED）退化为 $-\\frac14 F_{\\mu\\nu}F^{\\mu\\nu}$。规范场 $A_\\mu$ 无质量项（显式质量项破坏规范不变性），需通过希格斯机制获得质量。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"自发对称破缺与重整化","en":"SSB & RENORMALIZATION","sub":"希格斯机制、可重整性","desc":"自发对称破缺通过希格斯机制赋予规范场质量；'t Hooft 证明规范理论可重整化。","sections":[
      {"name":"2.1 希格斯机制与重整化","color":"#7c3aed","desc":"质量产生、可重整","items":[
        item("la-k2-1","希格斯机制",["def","thm","app"],"标量场真空期望值破缺规范对称，规范场获得质量。","<p>引入标量场 $\\phi$，其势 $V(\\phi)$ 在非零 $\\phi_0$ 处取极小值（真空期望值）。规范场吃掉 Goldstone 模获得质量（$M_A=g\\phi_0$）。这是电弱统一中 W/Z 质量的来源，不破坏规范不变性。</p>"),
        item("la-k2-2","规范理论的可重整化",["thm","his"],"'t Hooft（1971）证明自发破缺的规范理论可重整化。","<p>可重整化意味着紫外发散可用有限个裸参数吸收，预言有限。这证明了标准模型的量子自洽性。't Hooft 因此获 1999 年诺贝尔奖。反常自由（各代费米子贡献相消）是规范理论量子自洽的必要条件。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 51. 量子场论 quantum-field-theory
# ============================================================
SUBJECTS.append({
  "filename":"quantum-field-theory.html",
  "title":"量子场论",
  "eyebrow":"QUANTUM FIELD THEORY",
  "subtitle":"正则量子化 · 路径积分 · 费曼图 · 重整化 · 有效场论",
  "meta_desc":"量子场论知识体系：正则量子化、路径积分、费曼图与费曼规则、重整化、有效场论、QED精确检验",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"场的量子化","en":"QUANTIZATION OF FIELDS","sub":"正则量子化、路径积分","desc":"将场视为无穷多简谐振子的集合并量子化。路径积分提供了另一种量子化方式。","sections":[
      {"name":"1.1 正则量子化","color":"#2563eb","desc":"产生湮灭算符","items":[
        item("la-k1-1","标量场量子化",["def","thm"],"$\\phi(\\boldsymbol x,t)=\\int\\frac{d^3k}{(2\\pi)^3}\\frac1{\\sqrt{2\\omega_k}}(a_ke^{-ikx}+a_k^\\dagger e^{ikx})$。","<p>实标量场展开为产生/湮灭算符。$a_k^\\dagger$ 产生动量 $\\boldsymbol k$、能量 $\\omega_k=\\sqrt{k^2+m^2}$ 的粒子。对易关系 $[a_k,a_{k'}^\\dagger]=(2\\pi)^3\\delta^3(\\boldsymbol k-\\boldsymbol k')$。真空态 $|0\\rangle$ 被所有 $a_k$ 湮灭。</p>"),
        item("la-k1-2","路径积分量子化",["def","thm"],"$Z=\\int\\mathcal{D}\\phi\\,e^{iS[\\phi]/\\hbar}$，$S=\\int\\mathcal{L}\\,d^4x$。","<p>费曼路径积分：所有场构型的加权求和。关联函数由路径积分直接计算。路径积分自然处理规范对称性（Faddeev-Popov）和约束，比正则量子化更方便，是现代量子场论的标准框架。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"费曼图与重整化","en":"FEYNMAN DIAGRAMS & RENORMALIZATION","sub":"微扰论、紫外发散","desc":"用费曼图计算散射振幅，重整化消除紫外发散，得到有限的物理预言。","sections":[
      {"name":"2.1 费曼规则","color":"#7c3aed","desc":"微扰展开","items":[
        item("la-k2-1","费曼图与 S 矩阵",["def","thm","app"],"顶点~耦合常数，内线~传播子，外线~偏振矢量。","<p>S 矩阵 $\\langle f|S|i\\rangle$ 展开为费曼图级数。每个图对应一个解析表达式（费曼规则）。QED 中电子反常磁矩的计算精度达 $10^{-10}$，与实验高度吻合，是物理学最精确的预言。</p>"),
        item("la-k2-2","重整化",["def","thm"],"抵消紫外发散，用有限个裸参数吸收发散。","<p>圈图积分在高动量（紫外）发散。可重整化理论中发散可吸收进裸质量、裸耦合等，物理量有限。重整化群（Wilson）研究耦合常数随能标的跑动。QCD 的渐近自由 $\\alpha_s(\\mu)\\to0$ as $\\mu\\to\\infty$ 即由重整化群方程描述。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"有效场论","en":"EFFECTIVE FIELD THEORY","sub":"低能有效描述","desc":"有效场论在某能标下描述物理，忽略更高能标自由度。","sections":[
      {"name":"3.1 有效场论方法","color":"#0f766e","desc":"Wilson 有效作用量","items":[
        item("la-k3-1","有效场论",["def","thm","app"],"拉氏量含所有对称性允许的算符，按维度排序。","<p>有效场论（EFT）思想：不必知道完整理论，在某能标下用最一般的有效拉氏量描述物理。算符系数由低能实验拟合。费米弱作用理论是 EFT 的经典例子，高能下被电弱理论取代。手征微扰论是 QCD 的低能 EFT。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 52. 弦理论 string-theory
# ============================================================
SUBJECTS.append({
  "filename":"string-theory.html",
  "title":"弦理论",
  "eyebrow":"STRING THEORY",
  "subtitle":"弦振动 · 10维时空 · 超对称 · D膜 · M理论 · AdS/CFT",
  "meta_desc":"弦理论知识体系：弦的振动谱、玻色弦与超弦、10维时空、D膜、M理论、AdS/CFT对偶",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"玻色弦与超弦","en":"BOSONIC & SUPERSTRINGS","sub":"弦的量子化、时空维数","desc":"基本粒子是一维弦的不同振动模式。弦理论是量子引力的主要候选。","sections":[
      {"name":"1.1 弦的量子化","color":"#2563eb","desc":"振动谱、反常相消","items":[
        item("la-k1-1","弦的振动模式",["def","thm"],"弦的不同振动模式对应不同质量/自旋的粒子。","<p>弦是一维延展物体，其振动产生无穷多粒子态。最低能模式对应无质量粒子（引力子、规范玻色子等）和有质量激发态。弦的张力 $T=1/(2\\pi\\alpha')$，$\\sqrt{\\alpha'}$ 为弦长标度（~普朗克长度）。</p>"),
        item("la-k1-2","时空维数与超对称",["def","thm"],"自洽要求 $D=26$（玻色弦）或 $D=10$（超弦）。","<p>量子反常相消要求特定时空维数。玻色弦 $D=26$，但含快子（质量虚数，不稳定）。超弦引入超对称，$D=10$，消除快子并包含费米子。五种超弦理论：I、IIA、IIB、SO(32) 杂弦、$E_8\\times E_8$ 杂弦。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"D膜、M理论与对偶","en":"D-BRANES, M-THEORY & DUALITIES","sub":"对偶性、统一","desc":"D膜是弦的端点附着的物体。M理论统一五种超弦。AdS/CFT 对偶是弦论最重要的成果。","sections":[
      {"name":"2.1 D膜与M理论","color":"#7c3aed","desc":"非微扰对象、11维统一","items":[
        item("la-k2-1","D膜",["def","thm","app"],"开弦端点附着的 $p$ 维超曲面。","<p>D膜（Dirichlet 膜）是非微扰对象，开弦端点被限制在其上。D膜上的低能理论是超对称规范理论。D膜是弦论与规范理论的桥梁，也用于构造粒子物理模型和黑洞熵的微观计算。</p>"),
        item("la-k2-2","M理论与弦对偶",["def","thm"],"11 维 M 理论统一五种超弦；S/T/U 对偶。","<p>五种超弦通过对偶性联系：S 对偶（强弱耦合互换）、T 对偶（大小半径互换）、U 对偶（S+T）。强耦合下 IIA 弦论展现第 11 维，即 M 理论。M 理论的低能极限是 11 维超引力。所有弦论可能是同一理论的不同相。</p>"),
      ]},
      {"name":"2.2 AdS/CFT 对偶","color":"#0f766e","desc":"全息原理","items":[
        item("la-k2-3","AdS/CFT 对应",["def","thm","his"],"$AdS_5\\times S^5$ 上 IIB 弦论 = 4 维 $\\mathcal{N}=4$ SYM。","<p>马尔达西那（1997）发现：反德西特空间上的引力理论与其边界上的共形场论等价。这是全息原理的具体实现，提供了用规范理论研究量子引力的工具，也用于研究强耦合 QCD（ AdS/QCD）和凝聚态（AdS/CMT）。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 53. 量子引力 quantum-gravity
# ============================================================
SUBJECTS.append({
  "filename":"quantum-gravity.html",
  "title":"量子引力",
  "eyebrow":"QUANTUM GRAVITY",
  "subtitle":"圈量子引力 · 自旋网络 · 渐近安全 · 正则量子化 · 全息",
  "meta_desc":"量子引力知识体系：圈量子引力、自旋网络与自旋泡沫、渐近安全、正则量子引力、全息原理",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"量子引力的主要途径","en":"APPROACHES TO QUANTUM GRAVITY","sub":"圈量子引力、弦论、渐近安全","desc":"统一量子力学与广义相对论是物理学终极问题。主要途径包括圈量子引力、弦论、渐近安全等。","sections":[
      {"name":"1.1 圈量子引力","color":"#2563eb","desc":"背景无关量子化","items":[
        item("la-k1-1","自旋网络与自旋泡沫",["def","thm"],"空间由自旋网络描述，面积与体积算子离散化。","<p>圈量子引力（LQG）以 Ashtekar 联络为基本变量，背景无关地量子化引力。自旋网络是态的基，面积与体积算子有离散谱（面积隙 ~普朗克面积）。自旋泡沫描述自旋网络的时间演化。预言大爆炸奇点可能被大反弹取代。</p>"),
        item("la-k1-2","其他量子引力途径",["def","app"],"渐近安全、因果集、因果动力学三角剖分。","<p>渐近安全（Weinberg）假设引力耦合常数在紫外有非高斯不动点，从而可量子化。因果集理论将时空建模为离散因果偏序集。因果动力学三角剖分用数值方法模拟时空量子涨落。这些途径都尚缺实验验证。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"全息原理与量子引力","en":"HOLOGRAPHIC PRINCIPLE","sub":"AdS/CFT、黑洞熵","desc":"全息原理：$D$ 维量子引力理论等价于 $D-1$ 维边界上的量子场论。","sections":[
      {"name":"2.1 全息原理","color":"#7c3aed","desc":"信息与面积","items":[
        item("la-k2-1","全息原理",["def","thm"],"区域内最大信息熵与边界面积成正比：$S\\leq A/(4l_P^2)$。","<p>'t Hooft 和 Susskind 提出全息原理：$D$ 维空间中区域的信息可完全编码在其 $D-1$ 维边界上。贝肯斯坦界和黑洞熵是其物理基础。AdS/CFT 对偶是全息原理最严格的实现。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 54. 共形场论 conformal-field-theory
# ============================================================
SUBJECTS.append({
  "filename":"conformal-field-theory.html",
  "title":"共形场论",
  "eyebrow":"CONFORMAL FIELD THEORY",
  "subtitle":"共形对称性 · 算子积展开 · 中心荷 · 临界点 · 2D CFT",
  "meta_desc":"共形场论知识体系：共形对称性、Virasoro 代数、算子积展开 OPE、中心荷、临界现象、二维 CFT",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"共形对称性与二维 CFT","en":"CONFORMAL SYMMETRY & 2D CFT","sub":"标度不变、共形群、Virasoro","desc":"共形场论在标度变换下不变，描述连续相变和 AdSCFT 边界。二维共形群无限维，给出极强约束。","sections":[
      {"name":"1.1 二维 CFT 结构","color":"#2563eb","desc":"Virasoro 代数、OPE","items":[
        item("la-k1-1","共形群与 Virasoro 代数",["def","thm"],"$[L_m,L_n]=(m-n)L_{m+n}+\\frac{c}{12}m(m^2-1)\\delta_{m+n,0}$。","<p>二维共形变换分解为全纯与反全纯两部分，生成无限维 Virasoro 代数。中心荷 $c$ 是 CFT 的基本参数：自由玻色子 $c=1$，Ising 模型 $c=1/2$。应力张量 $T(z)$ 是共形对称性的生成元。</p>"),
        item("la-k1-2","初级场与 OPE",["def","thm"],"初级场按 $(h,\\bar{h})$ 变换；算子积展开 $\\phi_i\\phi_j\\sim\\sum_k C_{ijk}z^{h_k-h_i-h_j}\\phi_k$。","<p>初级场（primary fields）在共形变换下有简单变换性质。算子积展开（OPE）将两算子的乘积展开为局域算子之和。共形维度 $h,\\bar{h}$ 决定关联函数形式。CFT 的所有信息编码在 $c$、初级场谱和 OPE 系数中。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"CFT 与临界现象","en":"CFT & CRITICAL PHENOMENA","sub":"临界指数、标度律","desc":"连续相变的临界点由共形场论描述，临界指数与共形维度对应。","sections":[
      {"name":"2.1 临界现象的 CFT 描述","color":"#7c3aed","desc":"标度不变、临界指数","items":[
        item("la-k2-1","临界现象与标度律",["def","thm","app"],"临界点处关联长度发散，系统标度不变。","<p>在连续相变的临界点，关联长度 $\\xi\\to\\infty$，系统具有标度不变性，即共形对称性。临界指数（$\\alpha,\\beta,\\gamma,\\delta,\\eta,\\nu$）满足标度律。二维 Ising、Potts、XY 模型等可用 CFT 精确求解，给出普适类。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 55. 拓扑量子场论 tqft
# ============================================================
SUBJECTS.append({
  "filename":"tqft.html",
  "title":"拓扑量子场论",
  "eyebrow":"TOPOLOGICAL QFT",
  "subtitle":"拓扑不变量 · Chern-Simons · 拓扑序 · 量子计算",
  "meta_desc":"拓扑量子场论知识体系：TQFT 公理、Chern-Simons 理论、纽结不变量、拓扑序、任意子与拓扑量子计算",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"TQFT 与 Chern-Simons 理论","en":"TQFT & CHERN-SIMONS","sub":"拓扑不变量、纽结","desc":"拓扑量子场论的相关函数只依赖流形拓扑。Chern-Simons 理论是三维 TQFT 的核心。","sections":[
      {"name":"1.1 TQFT 与 Chern-Simons","color":"#2563eb","desc":"与度量无关","items":[
        item("la-k1-1","TQFT 定义",["def","thm"],"配分函数 $Z(M)$ 是流形 $M$ 的拓扑不变量。","<p>TQFT 的作用量不含度规，关联函数在同胚下不变。Atiyah 给出 TQFT 的公理化定义：从配边范畴到向量空间范畴的函子。TQFT 为拓扑不变量（如 Donaldson 不变量、Seiberg-Witten 不变量）提供场论描述。</p>"),
        item("la-k1-2","Chern-Simons 理论",["def","thm"],"$S=\\frac{k}{4\\pi}\\int_M \\mathrm{Tr}(A\\wedge dA+\\frac23 A\\wedge A\\wedge A)$，与纽结的 Jones 多项式相关。","<p>三维 Chern-Simons 理论是最著名的 TQFT。Witten 证明带 Wilson 线的 Chern-Simons 配分函数给出纽结的 Jones 多项式。规范群 $G$ 与等级 $k$ 决定理论。Chern-Simons 也出现在分数霍尔效应的有效描述中。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"拓扑序与拓扑量子计算","en":"TOPOLOGICAL ORDER & QUANTUM COMPUTING","sub":"任意子、容错量子计算","desc":"拓扑序是超越 Landau 对称破缺的新物态。任意子可用于拓扑量子计算，具有天然容错性。","sections":[
      {"name":"2.1 拓扑序与任意子","color":"#7c3aed","desc":"分数统计、辫子群","items":[
        item("la-k2-1","拓扑序与任意子",["def","thm","app"],"拓扑序由长程纠缠刻画；任意子分数统计，交换由辫子群描述。","<p>拓扑序（Wen）是超越 Landau 对称破缺范式的新物态分类，由基态简并度与边界态表征。二维系统中的任意子（anyon）具有介于玻色与费米之间的分数统计，交换相位由辫子群表示给出。阿贝尔与非阿贝尔任意子均可实现。</p>"),
        item("la-k2-2","拓扑量子计算",["def","thm"],"非阿贝尔任意子的编织操作实现容错量子门。","<p>非阿贝尔任意子的世界线编织对应酉变换，可实现量子门。由于信息存储在拓扑非平凡的编织中，局域噪声不影响计算结果，提供天然容错性。$\\nu=5/2$ 分数量子霍尔态中的 Majorana 零模是候选非阿贝尔任意子。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 56. 天体物理学 astrophysics
# ============================================================
SUBJECTS.append({
  "filename":"astrophysics.html",
  "title":"天体物理学",
  "eyebrow":"ASTROPHYSICS",
  "subtitle":"恒星结构 · 恒星演化 · 星系动力学 · 致密星 · 活动星系核",
  "meta_desc":"天体物理学知识体系：恒星结构方程、恒星演化、主序、红巨星、超新星、白矮星中子星黑洞、星系动力学、活动星系核",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"恒星结构与演化","en":"STELLAR STRUCTURE & EVOLUTION","sub":"流体静力学平衡、核反应、演化轨迹","desc":"恒星是自引力流体球，核反应提供能量。恒星结构方程与演化轨迹是天体物理的基础。","sections":[
      {"name":"1.1 恒星结构方程","color":"#2563eb","desc":"流体静力学平衡、能量传输","items":[
        item("la-k1-1","流体静力学平衡",["def","thm"],"$\\frac{dP}{dr}=-\\frac{GM(r)\\rho}{r^2}$，$\\frac{dM}{dr}=4\\pi r^2\\rho$。","<p>压强梯度抵抗引力收缩。四个恒星结构方程：质量连续、流体静力学平衡、能量守恒、能量传输（辐射扩散或对流）。状态方程和不透明度使方程组闭合。主序星靠氢聚变维持平衡。</p>"),
        item("la-k1-2","核反应与能量产生",["def","thm","app"],"pp 链与 CNO 循环将氢聚变为氦。","<p>低质量恒星以质子-质子链为主：$4p\\to ^4\\text{He}+2e^++2\\nu_e+2\\gamma$。大质量恒星以 CNO 循环为主。氦燃烧（三α过程）产生碳和氧。更高质量恒星逐级聚变直至铁，铁之后聚变吸热，导致核心坍缩。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"恒星演化终点与致密星","en":"STELLAR ENDPOINTS & COMPACT OBJECTS","sub":"白矮星、中子星、黑洞、超新星","desc":"恒星最终命运由质量决定：白矮星、中子星或黑洞。超新星是大质量恒星的壮丽终局。","sections":[
      {"name":"2.1 致密星与超新星","color":"#7c3aed","desc":"简并压、坍缩","items":[
        item("la-k2-1","钱德拉塞卡极限与白矮星",["def","thm","his"],"白矮星最大质量 $M_{Ch}\\simeq1.44M_\\odot$。","<p>白矮星靠电子简并压支撑。超过钱德拉塞卡极限，电子简并压不足，恒星坍缩。Ia 型超新星即白矮星达钱德拉塞卡极限后的热核爆炸，是标准烛光，用于测距（暗能量发现）。</p>"),
        item("la-k2-2","中子星与黑洞",["def","thm","app"],"中子星由中子简并压支撑；更大质量坍缩为黑洞。","<p>核心坍缩超新星（II 型）留下中子星或黑洞。中子星密度达核密度，半径约 10 km，强磁场产生脉冲星。质量约 $2-3M_\\odot$ 以上形成黑洞。中子星并合产生引力波和短伽马暴（GW170817）。</p>"),
      ]},
    ]},
    {"id":"la-ch3","num":"第三章","title":"星系与活动星系核","en":"GALAXIES & AGN","sub":"星系动力学、超大质量黑洞","desc":"星系由恒星、气体和暗物质构成。活动星系核由中心超大质量黑洞吸积驱动。","sections":[
      {"name":"3.1 星系动力学与 AGN","color":"#0f766e","desc":"旋转曲线、吸积盘","items":[
        item("la-k3-1","星系旋转曲线与暗物质",["def","thm","his"],"观测到平坦旋转曲线，暗示暗物质晕的存在。","<p>星系旋转曲线在可见物质外应按 $v\\propto r^{-1/2}$ 下降，但观测到几乎平坦。这表明存在不可见的暗物质晕提供额外引力。暗物质占宇宙物质约 85%。</p>"),
        item("la-k3-2","活动星系核（AGN）",["def","thm","app"],"超大质量黑洞吸积产生强烈辐射与喷流。","<p>AGN 由中心超大质量黑洞（$10^6-10^{10}M_\\odot$）吸积气体驱动，吸积盘将引力能转化为辐射。类星体是最亮的 AGN。射电星系有相对论性喷流。AGN 反馈调节星系演化。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 57. 等离子体物理 plasma-physics
# ============================================================
SUBJECTS.append({
  "filename":"plasma-physics.html",
  "title":"等离子体物理",
  "eyebrow":"PLASMA PHYSICS",
  "subtitle":"等离子体 · 德拜屏蔽 · 朗缪尔波 · 磁约束 · 不稳定性",
  "meta_desc":"等离子体物理知识体系：德拜长度、等离子体频率、朗缪尔波、阿尔文波、磁约束、等离子体不稳定性、聚变等离子体",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"等离子体基本性质","en":"PLASMA BASICS","sub":"德拜长度、等离子体频率、准中性","desc":"等离子体是电离气体，是物质第四态，占宇宙可见物质 99%。本章讨论其集体行为与基本参数。","sections":[
      {"name":"1.1 德拜屏蔽与等离子体振荡","color":"#2563eb","desc":"集体效应","items":[
        item("la-k1-1","德拜长度与准中性",["def","thm"],"$\\lambda_D=\\sqrt{\\varepsilon_0 kT_e/(ne^2)}$，$\\lambda_D\\ll L$ 为准中性条件。","<p>等离子体在大于德拜长度的尺度上呈准中性（$n_e\\approx Zn_i$）。单个电荷被屏蔽，库仑势变为 Yukawa 型 $\\propto e^{-r/\\lambda_D}/r$。德拜球内含大量粒子（$n\\lambda_D^3\\gg1$）是等离子体判据之一。</p>"),
        item("la-k1-2","等离子体频率与朗缪尔波",["def","thm"],"$\\omega_p=\\sqrt{ne^2/(\\varepsilon_0 m_e)}$，朗缪尔波色散 $\\omega^2=\\omega_p^2+3k^2v_{Te}^2$。","<p>等离子体频率是高频静电振荡频率。电子密度扰动产生朗缪尔波（电子等离子体波）。离子等离子体振荡频率为 $\\omega_{pi}=\\sqrt{Zn_ie^2/(\\varepsilon_0 m_i)}$。电磁波在等离子体中传播需 $\\omega>\\omega_p$（截止频率）。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"磁化等离子体与不稳定性","en":"MAGNETIZED PLASMA & INSTABILITIES","sub":"磁流体力学、阿尔文波、不稳定性","desc":"磁化等离子体中电磁与流体耦合，产生丰富的波动与不稳定性。磁流体力学（MHD）是核心框架。","sections":[
      {"name":"2.1 MHD 与等离子体不稳定性","color":"#7c3aed","desc":"阿尔文波、撕裂模","items":[
        item("la-k2-1","磁流体力学与阿尔文波",["def","thm"],"阿尔文速度 $v_A=B/\\sqrt{\\mu_0\\rho}$，阿尔文波沿磁场传播。","<p>MHD 方程将等离子体视为导电流体，耦合 Navier-Stokes 与 Maxwell 方程。阿尔文波是磁场张力驱动的横波，沿磁力线传播。磁声波是快/慢模式。MHD 在托卡马克和空间等离子体中广泛应用。</p>"),
        item("la-k2-2","等离子体不稳定性",["def","thm","app"],"撕裂模、漂移波、气球模等约束等离子体的主要挑战。","<p>等离子体中存在多种不稳定性：撕裂模破坏磁面形成磁岛；漂移波由密度梯度驱动，是反常输运的主因；气球模在坏曲率区增长。控制不稳定性是磁约束聚变的核心难题。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 58. 生物物理 biophysics
# ============================================================
SUBJECTS.append({
  "filename":"biophysics.html",
  "title":"生物物理",
  "eyebrow":"BIOPHYSICS",
  "subtitle":"蛋白质折叠 · DNA力学 · 分子马达 · 膜生物物理",
  "meta_desc":"生物物理知识体系：蛋白质折叠与能量地形、DNA弹性与拓扑、分子马达与布朗棘轮、生物膜与离子通道",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"生物大分子物理","en":"BIOMACROMOLECULES","sub":"蛋白质、DNA、RNA","desc":"用物理方法研究生物大分子的结构、动力学与功能。生物物理是物理与生命科学的交叉。","sections":[
      {"name":"1.1 蛋白质折叠","color":"#2563eb","desc":"能量地形、Anfinsen","items":[
        item("la-k1-1","蛋白质折叠与能量地形",["def","thm","his"],"氨基酸序列决定三维结构（Anfinsen 原理）；折叠沿能量漏斗进行。","<p>蛋白质从随机卷曲折叠到天然态。能量地形漏斗模型：大量构象态汇聚到低能天然态。折叠是热力学（疏水作用、氢键）与动力学协同的过程。分子伴侣协助折叠，错误折叠（如淀粉样蛋白）导致阿尔茨海默病等。</p>"),
        item("la-k1-2","DNA 力学与拓扑",["def","thm","app"],"持久长度 $\\xi_p\\approx50$ nm；扭转与超螺旋。","<p>DNA 是半柔性聚合物，蠕虫链模型（WLC）描述其弹性。DNA 双螺旋的扭转导致超螺旋，拓扑异构酶调节超螺旋度。单分子技术（光镊、磁镊）可测量 DNA 的拉伸和扭转响应。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"分子马达与生物膜","en":"MOLECULAR MOTORS & MEMBRANES","sub":"布朗棘轮、脂质双层","desc":"分子马达将化学能转化为机械功；生物膜是选择性渗透的脂质双层。","sections":[
      {"name":"2.1 分子马达与膜","color":"#7c3aed","desc":"ATP 酶、离子通道","items":[
        item("la-k2-1","分子马达与布朗棘轮",["def","thm","app"],"马达蛋白沿轨道定向运动，将 ATP 水解能转化为功。","<p>分子马达（如肌球蛋白、驱动蛋白、动力蛋白）在热噪声背景下实现定向运动。布朗棘轮模型用非对称势与能量输入解释定向输运。F₁F₀-ATP 合酶是旋转马达，效率近 100%。</p>"),
        item("la-k2-2","生物膜与离子通道",["def","thm"],"脂质双层流动性；离子通道实现选择性跨膜运输。","<p>生物膜由磷脂双分子层构成，具有流动性（Singer-Nicolson 流体镶嵌模型）。膜蛋白（离子通道、泵）维持跨膜电位。Hodgkin-Huxley 模型描述神经动作电位。膜融合与囊泡运输是细胞生物学核心过程。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 59. 辐射过程 radiation-processes
# ============================================================
SUBJECTS.append({
  "filename":"radiation-processes.html",
  "title":"辐射过程",
  "eyebrow":"RADIATION PROCESSES",
  "subtitle":"同步辐射 · 轫致辐射 · 切伦科夫辐射 · 黑体辐射 · 逆康普顿",
  "meta_desc":"辐射过程知识体系：李纳-维谢尔势、同步辐射、轫致辐射、切伦科夫辐射、逆康普顿散射、黑体辐射",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"带电粒子辐射","en":"RADIATION BY CHARGED PARTICLES","sub":"李纳-维谢尔势、辐射功率","desc":"加速的带电粒子必然辐射电磁波。本章从李纳-维谢尔势出发讨论各种辐射机制。","sections":[
      {"name":"1.1 辐射基本理论","color":"#2563eb","desc":"加速电荷辐射","items":[
        item("la-k1-1","李纳-维谢尔势与辐射场",["def","thm"],"$\\mathbf{E}_{rad}\\propto \\mathbf{n}\\times(\\mathbf{n}\\times\\dot\\boldsymbol\\beta)$，辐射场 $\\propto1/r$。","<p>加速电荷的电磁场分为速度场（$\\propto1/r^2$，非辐射）和加速度场（$\\propto1/r$，辐射）。李纳-维谢尔势给出推迟势。辐射方向图由加速度决定：非相对论为 $\\sin^2\\theta$ 分布，相对论集中于前向锥角 $1/\\gamma$。</p>"),
        item("la-k1-2","拉莫尔公式与相对论推广",["def","thm"],"$P=\\frac{q^2a^2}{6\\pi\\varepsilon_0 c^3}$（非相对论），$P=\\frac{q^2\\gamma^4}{6\\pi\\varepsilon_0 c}(\\dot\\beta^2+\\gamma^2(\\boldsymbol\\beta\\cdot\\dot\\boldsymbol\\beta)^2)$。","<p>拉莫尔公式给出非相对论加速电荷的总辐射功率。相对论推广中，横向加速度辐射功率 $\\propto\\gamma^4$，纵向 $\\propto\\gamma^6$。同步辐射即相对论电子在磁场中做圆周运动（横向加速）的辐射。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"主要辐射机制","en":"MAJOR RADIATION MECHANISMS","sub":"同步、轫致、切伦科夫、逆康普顿","desc":"天体物理和实验室中常见的辐射机制包括同步辐射、轫致辐射、切伦科夫辐射和逆康普顿散射。","sections":[
      {"name":"2.1 各类辐射机制","color":"#7c3aed","desc":"天体辐射、光源","items":[
        item("la-k2-1","同步辐射",["def","thm","app"],"相对论电子在磁场中辐射，功率 $P\\propto\\gamma^2B^2\\sin^2\\alpha$。","<p>同步辐射谱宽、高偏振、高亮度，是重要的第三代光源（如上海光源）。在天体物理中，射电星系、超新星遗迹的射电辐射即同步辐射。曲率辐射是类似机制（沿弯曲磁力线运动）。</p>"),
        item("la-k2-2","轫致辐射与切伦科夫辐射",["def","thm"],"轫致：电荷在库仑场中减速；切伦科夫：$v>c/n$ 时的锥形辐射。","<p>轫致辐射（制动辐射）是带电粒子经过原子核库仑场时减速产生的连续谱，X 射线管的主要机制。切伦科夫辐射是粒子在介质中超光速（$v>c/n$）时产生的锥形辐射，角度 $\\cos\\theta_c=1/(\\beta n)$，用于粒子探测（如中微子探测器）。</p>"),
        item("la-k2-3","逆康普顿散射与黑体辐射",["def","thm"],"光子被相对论电子散射获得能量 $\\sim\\gamma^2$；黑体辐射由普朗克定律描述。","<p>逆康普顿散射：低能光子被相对论电子散射后能量提升 $\\sim\\gamma^2$，是天体 X 射线/伽马射线的重要来源。黑体辐射谱由普朗克公式 $B_\\nu(T)=\\frac{2h\\nu^3}{c^2}\\frac1{e^{h\\nu/kT}-1}$ 描述，宇宙微波背景是完美黑体谱。</p>"),
      ]},
    ]},
  ]
})

# ============================================================
# 60. 核聚变物理 fusion-physics
# ============================================================
SUBJECTS.append({
  "filename":"fusion-physics.html",
  "title":"核聚变物理",
  "eyebrow":"FUSION PHYSICS",
  "subtitle":"聚变反应 · 劳逊判据 · 托卡马克 · 仿星器 · 惯性约束",
  "meta_desc":"核聚变物理知识体系：聚变反应、库仑势垒、劳逊判据、三重积、托卡马克、仿星器、惯性约束聚变、等离子体约束",
  "chapters":[
    {"id":"la-ch1","num":"第一章","title":"聚变原理","en":"FUSION PRINCIPLES","sub":"D-T反应、库仑势垒、劳逊判据","desc":"轻核聚变释放巨大能量，是太阳的能量来源。本章讨论聚变反应、条件与功率平衡。","sections":[
      {"name":"1.1 聚变反应与条件","color":"#2563eb","desc":"高温、高密度、长约束","items":[
        item("la-k1-1","聚变反应与库仑势垒",["def","thm"],"D-T：$\\text{D}+\\text{T}\\to\\alpha(3.5\\text{MeV})+n(14.1\\text{MeV})$，$Q=17.6$ MeV。","<p>轻核需克服库仑势垒才能聚变，量子隧穿使聚变在低于势垒能量下发生。反应率 $\\langle\\sigma v\\rangle$ 在 $T\\sim10-20$ keV 时最大。D-T 是最易实现的反应，D-D、D-He³ 是先进燃料。质量亏损转化为能量（$E=\\Delta mc^2$）。</p>"),
        item("la-k1-2","劳逊判据与三重积",["def","thm"],"$n\\tau_E\\ge 10^{14}\\,\\text{cm}^{-3}\\cdot\\text{s}$（D-T，$T\\sim10^8$ K）。","<p>劳逊判据给出聚变能量得失相当的密度-约束时间乘积。三重积 $nT\\tau_E$ 是聚变装置的核心指标，需达到 $\\sim10^{21}\\,\\text{keV}\\cdot\\text{s}/\\text{m}^3$。ITER 目标实现 $Q>10$（聚变功率/输入功率）。</p>"),
      ]},
    ]},
    {"id":"la-ch2","num":"第二章","title":"磁约束与惯性约束","en":"MAGNETIC & INERTIAL CONFINEMENT","sub":"托卡马克、仿星器、激光聚变","desc":"实现受控聚变需约束高温等离子体。磁约束（托卡马克、仿星器）和惯性约束（激光）是两大途径。","sections":[
      {"name":"2.1 约束方案","color":"#7c3aed","desc":"托卡马克、仿星器、ICF","items":[
        item("la-k2-1","托卡马克与仿星器",["def","thm","app"],"托卡马克用环向场+极向场约束；仿星器用非轴对称线圈。","<p>托卡马克（Tokamak）是最先进的磁约束方案，环形真空室加环向磁场，等离子体电流产生极向磁场形成嵌套磁面。ITER 是国际热核聚变实验堆。仿星器（Stellarator，如 W7-X）用外部线圈产生全部磁场，无等离子体电流，稳态运行。</p>"),
        item("la-k2-2","惯性约束聚变（ICF）",["def","thm","app"],"激光压缩靶丸实现聚变，NIF 2022 年实现点火。","<p>惯性约束用高能激光（或离子束）瞬间压缩氘氚靶丸，靠惯性在飞散前完成聚变。2022 年美国国家点火装置（NIF）首次实现科学点火（输出能量>输入聚变能）。快点火（fast ignition）是改进方案。</p>"),
      ]},
    ]},
  ]
})

print("Total subjects defined:", len(SUBJECTS))

# 补充 index.html 引用但原列表缺失的 4 个学科
SUBJECTS.append({"filename":"linear-algebra.html","title":"线性代数","eyebrow":"LINEAR ALGEBRA","subtitle":"行列式 · 矩阵 · 向量空间 · 特征值 · 二次型","meta_desc":"线性代数知识体系","chapters":[]})
SUBJECTS.append({"filename":"newtonian-mechanics.html","title":"牛顿力学","eyebrow":"NEWTONIAN MECHANICS","subtitle":"运动学 · 牛顿定律 · 动量能量 · 刚体振动","meta_desc":"牛顿力学知识体系","chapters":[]})
SUBJECTS.append({"filename":"engineering-optics.html","title":"工程光学","eyebrow":"ENGINEERING OPTICS","subtitle":"几何光学 · 像差 · 光学系统","meta_desc":"工程光学知识体系","chapters":[]})
SUBJECTS.append({"filename":"quantum-information.html","title":"量子信息","eyebrow":"QUANTUM INFORMATION","subtitle":"量子比特 · 纠缠 · 量子通信","meta_desc":"量子信息知识体系","chapters":[]})

# 用 build_subjects 生成的扩展章节替换原章节（每科≥300知识点）
from build_subjects import expand_subject, SUBJECT_MAP
for s in SUBJECTS:
    fn = s["filename"]
    if fn in SUBJECT_MAP:
        prefix = fn.replace("-","_").replace(".html","")
        s["chapters"] = expand_subject(fn, SUBJECT_MAP[fn], prefix)

for s in SUBJECTS:
    write_subject(s)
print(f"\nDone! Generated {len(SUBJECTS)} subject pages.")
