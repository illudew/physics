# -*- coding: utf-8 -*-
"""Generate vector-analysis.html with 7 chapters: 矢量运算/矢量微积分/梯度散度旋度/曲线坐标系/并矢与张量运算/并矢与张量分析/算符运算法则."""
import json

FIG = {
"vector_add": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="120" x2="180" y2="120" stroke="#2563eb" stroke-width="2"/>
<polygon points="180,120 170,115 170,125" fill="#2563eb"/>
<line x1="30" y1="120" x2="100" y2="50" stroke="#7c3aed" stroke-width="2"/>
<polygon points="100,50 90,55 95,65" fill="#7c3aed"/>
<line x1="30" y1="120" x2="200" y2="50" stroke="#16a34a" stroke-width="2" stroke-dasharray="5 3"/>
<polygon points="200,50 190,54 194,63" fill="#16a34a"/>
<line x1="100" y1="50" x2="200" y2="50" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<line x1="180" y1="120" x2="200" y2="50" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 3"/>
<text x="100" y="140" font-size="11" fill="#2563eb">a</text>
<text x="48" y="78" font-size="11" fill="#7c3aed">b</text>
<text x="156" y="74" font-size="11" fill="#16a34a">a+b</text>
</svg>''',
"dot_product": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="40" y1="110" x2="200" y2="110" stroke="#2563eb" stroke-width="2"/>
<polygon points="200,110 190,105 190,115" fill="#2563eb"/>
<line x1="40" y1="110" x2="130" y2="50" stroke="#7c3aed" stroke-width="2"/>
<polygon points="130,50 120,55 125,65" fill="#7c3aed"/>
<line x1="130" y1="50" x2="130" y2="110" stroke="#ef4444" stroke-width="1.3" stroke-dasharray="4 3"/>
<text x="48" y="100" font-size="11" fill="#2563eb">a</text>
<text x="76" y="72" font-size="11" fill="#7c3aed">b</text>
<text x="134" y="84" font-size="10" fill="#ef4444">|b|cosθ</text>
<text x="66" y="124" font-size="10" fill="#475569">θ</text>
</svg>''',
"cross_product": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="120" x2="180" y2="120" stroke="#2563eb" stroke-width="2"/>
<polygon points="180,120 170,115 170,125" fill="#2563eb"/>
<line x1="30" y1="120" x2="80" y2="50" stroke="#7c3aed" stroke-width="2"/>
<polygon points="80,50 70,55 75,65" fill="#7c3aed"/>
<line x1="105" y1="120" x2="105" y2="30" stroke="#16a34a" stroke-width="2"/>
<polygon points="105,30 100,40 110,40" fill="#16a34a"/>
<text x="100" y="140" font-size="11" fill="#2563eb">a</text>
<text x="48" y="78" font-size="11" fill="#7c3aed">b</text>
<text x="110" y="60" font-size="11" fill="#16a34a">a×b</text>
<path d="M 60 120 A 45 45 0 0 0 105 80" fill="none" stroke="#475569" stroke-width="1" stroke-dasharray="3 2"/>
</svg>''',
"curl": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 120 40 A 50 50 0 1 1 119 40" fill="none" stroke="#2563eb" stroke-width="2"/>
<polygon points="119,40 124,50 113,49" fill="#2563eb"/>
<circle cx="120" cy="80" r="4" fill="#ef4444"/>
<line x1="120" y1="80" x2="120" y2="30" stroke="#ef4444" stroke-width="1.8"/>
<polygon points="120,30 115,40 125,40" fill="#ef4444"/>
<text x="128" y="36" font-size="11" fill="#ef4444">curl F</text>
<text x="60" y="80" font-size="10" fill="#2563eb">F 场</text>
</svg>''',
"gauss": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="120" cy="80" rx="70" ry="50" fill="#eef4fb" stroke="#2563eb" stroke-width="2"/>
<line x1="120" y1="30" x2="120" y2="20" stroke="#16a34a" stroke-width="1.8"/>
<polygon points="120,20 115,30 125,30" fill="#16a34a"/>
<line x1="190" y1="80" x2="205" y2="80" stroke="#16a34a" stroke-width="1.8"/>
<polygon points="205,80 195,75 195,85" fill="#16a34a"/>
<line x1="50" y1="80" x2="35" y2="80" stroke="#16a34a" stroke-width="1.8"/>
<polygon points="35,80 45,75 45,85" fill="#16a34a"/>
<line x1="120" y1="130" x2="120" y2="140" stroke="#16a34a" stroke-width="1.8"/>
<polygon points="120,140 115,130 125,130" fill="#16a34a"/>
<text x="100" y="86" font-size="11" fill="#2563eb">V</text>
<text x="126" y="24" font-size="9" fill="#16a34a">dS</text>
</svg>''',
"coords": '''<svg viewBox="0 0 260 160" xmlns="http://www.w3.org/2000/svg">
<line x1="30" y1="130" x2="230" y2="130" stroke="#94a3b8" stroke-width="1.5"/>
<polygon points="230,130 220,125 220,135" fill="#94a3b8"/>
<line x1="30" y1="130" x2="30" y2="30" stroke="#94a3b8" stroke-width="1.5"/>
<polygon points="30,30 25,40 35,40" fill="#94a3b8"/>
<line x1="30" y1="130" x2="140" y2="80" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3 2"/>
<polygon points="140,80 132,76 133,86" fill="#94a3b8"/>
<circle cx="120" cy="90" r="4" fill="#2563eb"/>
<line x1="120" y1="130" x2="120" y2="90" stroke="#7c3aed" stroke-width="1.5"/>
<line x1="30" y1="130" x2="120" y2="130" stroke="#7c3aed" stroke-width="1.5"/>
<line x1="120" y1="90" x2="155" y2="55" stroke="#7c3aed" stroke-width="1.5"/>
<text x="234" y="134" font-size="11" fill="#94a3b8">x</text>
<text x="18" y="28" font-size="11" fill="#94a3b8">z</text>
<text x="142" y="78" font-size="11" fill="#94a3b8">y</text>
<text x="124" y="86" font-size="10" fill="#2563eb">P</text>
<text x="70" y="124" font-size="10" fill="#7c3aed">r</text>
<text x="124" y="114" font-size="10" fill="#7c3aed">z</text>
<text x="150" y="68" font-size="10" fill="#7c3aed">r</text>
</svg>''',
"flux": '''<svg viewBox="0 0 240 160" xmlns="http://www.w3.org/2000/svg">
<path d="M 40 40 L 200 40 L 200 120 L 40 120 Z" fill="#eef4fb" stroke="#2563eb" stroke-width="2"/>
<line x1="120" y1="40" x2="120" y2="120" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2"/>
<line x1="80" y1="80" x2="110" y2="80" stroke="#16a34a" stroke-width="1.8"/>
<polygon points="110,80 100,75 100,85" fill="#16a34a"/>
<line x1="160" y1="80" x2="195" y2="80" stroke="#16a34a" stroke-width="1.8"/>
<polygon points="195,80 185,75 185,85" fill="#16a34a"/>
<line x1="120" y1="80" x2="120" y2="30" stroke="#ef4444" stroke-width="1.8"/>
<polygon points="120,30 115,40 125,40" fill="#ef4444"/>
<text x="124" y="28" font-size="10" fill="#ef4444">n</text>
<text x="90" y="72" font-size="10" fill="#16a34a">F</text>
<text x="170" y="72" font-size="10" fill="#16a34a">F</text>
<text x="110" y="90" font-size="11" fill="#2563eb">dS</text>
</svg>'''
}

TAG_LABEL = {"def":"定 义","thm":"定 理","der":"推 导","exa":"例 子","app":"应 用","note":"备 注"}

CORE_FORMULAS = [
    ("向量加法", "\\vec{a}+\\vec{b} = (a_x+b_x,\\ a_y+b_y,\\ a_z+b_z)", "对应分量相加"),
    ("向量数乘", "\\lambda\\vec{a} = (\\lambda a_x,\\ \\lambda a_y,\\ \\lambda a_z)", "数乘向量等于数乘各分量"),
    ("向量模长", "|\\vec{a}|=\\sqrt{a_x^2+a_y^2+a_z^2}", "向量的大小"),
    ("单位向量", "\\vec{a}^0 = \\dfrac{\\vec{a}}{|\\vec{a}|}", "模为 1 的向量"),
    ("点积定义", "\\vec{a}\\cdot\\vec{b} = |\\vec{a}||\\vec{b}|\\cos\\theta", "点积结果为标量"),
    ("点积分量", "\\vec{a}\\cdot\\vec{b} = a_xb_x+a_yb_y+a_zb_z", "分量形式的点积"),
    ("向量投影", "\\mathrm{proj}_{\\vec{a}}\\vec{b} = \\dfrac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}|^2}\\vec{a}", "b 在 a 方向的投影向量"),
    ("叉积定义", "\\vec{a}\\times\\vec{b} = |\\vec{a}||\\vec{b}|\\sin\\theta\\ \\vec{n}", "叉积为向量，方向由右手定则"),
    ("叉积分量", "\\vec{a}\\times\\vec{b} = \\begin{vmatrix}\\vec{i}&\\vec{j}&\\vec{k}\\\\a_x&a_y&a_z\\\\b_x&b_y&b_z\\end{vmatrix}", "叉积的行列式表示"),
    ("叉积模长", "|\\vec{a}\\times\\vec{b}| = |a||b|\\sin\\theta", "等于平行四边形面积"),
    ("叉积反交换律", "\\vec{a}\\times\\vec{b} = -\\vec{b}\\times\\vec{a}", "叉积不满足交换律"),
    ("混合积定义", "[\\vec{a}\\ \\vec{b}\\ \\vec{c}] = (\\vec{a}\\times\\vec{b})\\cdot\\vec{c}", "混合积为标量"),
    ("混合积分量", "[\\vec{a}\\ \\vec{b}\\ \\vec{c}]=\\begin{vmatrix}a_x&a_y&a_z\\\\b_x&b_y&b_z\\\\c_x&c_y&c_z\\end{vmatrix}", "混合积的行列式表示"),
    ("混合积轮换对称", "(\\vec{a}\\times\\vec{b})\\cdot\\vec{c} = (\\vec{b}\\times\\vec{c})\\cdot\\vec{a} = (\\vec{c}\\times\\vec{a})\\cdot\\vec{b}", "轮换不变"),
    ("三向量共面条件", "(\\vec{a}\\times\\vec{b})\\cdot\\vec{c}=0 \\iff \\vec{a},\\vec{b},\\vec{c}\\text{共面}", "混合积为零即共面"),
    ("BAC-CAB 公式", "\\vec{a}\\times(\\vec{b}\\times\\vec{c}) = \\vec{b}(\\vec{a}\\cdot\\vec{c})-\\vec{c}(\\vec{a}\\cdot\\vec{b})", "二重叉积展开"),
    ("拉格朗日恒等式", "(\\vec{a}\\times\\vec{b})\\cdot(\\vec{c}\\times\\vec{d}) = (\\vec{a}\\cdot\\vec{c})(\\vec{b}\\cdot\\vec{d})-(\\vec{a}\\cdot\\vec{d})(\\vec{b}\\cdot\\vec{c})", "四向量恒等式"),
    ("矢量函数导数", "\\dfrac{d\\vec{A}}{dt} = \\lim_{\\Delta t\\to 0}\\dfrac{\\vec{A}(t+\\Delta t)-\\vec{A}(t)}{\\Delta t}", "矢量函数对参数求导"),
    ("矢量求导分量", "\\dfrac{d\\vec{A}}{dt} = \\dfrac{dA_x}{dt}\\vec{i}+\\dfrac{dA_y}{dt}\\vec{j}+\\dfrac{dA_z}{dt}\\vec{k}", "分量分别求导"),
    ("点积求导", "\\dfrac{d}{dt}(\\vec{A}\\cdot\\vec{B}) = \\dfrac{d\\vec{A}}{dt}\\cdot\\vec{B}+\\vec{A}\\cdot\\dfrac{d\\vec{B}}{dt}", "点积的乘积法则"),
    ("叉积求导", "\\dfrac{d}{dt}(\\vec{A}\\times\\vec{B}) = \\dfrac{d\\vec{A}}{dt}\\times\\vec{B}+\\vec{A}\\times\\dfrac{d\\vec{B}}{dt}", "叉积的乘积法则，顺序不可换"),
    ("第一型线积分", "\\int_L f(x,y,z)\\,ds = \\int_\\alpha^\\beta f(x(t),y(t),z(t))\\sqrt{x'^2+y'^2+z'^2}\\,dt", "对弧长的线积分"),
    ("第二型线积分", "\\int_L \\vec{F}\\cdot d\\vec{r} = \\int_\\alpha^\\beta \\vec{F}(\\vec{r}(t))\\cdot\\vec{r}'(t)\\,dt", "对坐标的线积分"),
    ("方向导数", "\\dfrac{\\partial f}{\\partial l} = \\nabla f\\cdot\\vec{l}^0 = |\\nabla f|\\cos\\theta", "沿方向 l 的方向导数"),
    ("梯度直角坐标", "\\nabla f = \\dfrac{\\partial f}{\\partial x}\\vec{i}+\\dfrac{\\partial f}{\\partial y}\\vec{j}+\\dfrac{\\partial f}{\\partial z}\\vec{k}", "标量场的梯度"),
    ("梯度的散度（拉普拉斯）", "\\nabla^2 f = \\dfrac{\\partial^2 f}{\\partial x^2}+\\dfrac{\\partial^2 f}{\\partial y^2}+\\dfrac{\\partial^2 f}{\\partial z^2}", "拉普拉斯算子"),
    ("通量定义", "\\Phi = \\oiint_S \\vec{F}\\cdot d\\vec{S} = \\oiint_S \\vec{F}\\cdot\\vec{n}\\,dS", "穿过闭合曲面的通量"),
    ("散度定义", "\\nabla\\cdot\\vec{F} = \\lim_{\\Delta V\\to 0}\\dfrac{1}{\\Delta V}\\oiint_{\\Delta S}\\vec{F}\\cdot d\\vec{S}", "单位体积通量"),
    ("散度直角坐标", "\\nabla\\cdot\\vec{F} = \\dfrac{\\partial F_x}{\\partial x}+\\dfrac{\\partial F_y}{\\partial y}+\\dfrac{\\partial F_z}{\\partial z}", "散度的分量形式"),
    ("旋度定义", "\\nabla\\times\\vec{F} = \\begin{vmatrix}\\vec{i}&\\vec{j}&\\vec{k}\\\\ \\partial_x&\\partial_y&\\partial_z\\\\ F_x&F_y&F_z\\end{vmatrix}", "旋度的行列式形式"),
    ("旋度分量", "(\\nabla\\times\\vec{F})_x = \\dfrac{\\partial F_z}{\\partial y}-\\dfrac{\\partial F_y}{\\partial z}", "旋度的 x 分量"),
    ("高斯公式", "\\oiint_{\\partial V}\\vec{F}\\cdot d\\vec{S} = \\iiint_V (\\nabla\\cdot\\vec{F})\\,dV", "散度定理"),
    ("斯托克斯公式", "\\oint_{\\partial S}\\vec{F}\\cdot d\\vec{l} = \\iint_S (\\nabla\\times\\vec{F})\\cdot d\\vec{S}", "环量等于旋度通量"),
    ("梯度的旋度为零", "\\nabla\\times(\\nabla f) = 0", "梯度场必无旋"),
    ("旋度的散度为零", "\\nabla\\cdot(\\nabla\\times\\vec{F}) = 0", "旋度场必无源"),
    ("拉梅系数", "h_i = \\sqrt{\\left(\\dfrac{\\partial x}{\\partial u_i}\\right)^2+\\left(\\dfrac{\\partial y}{\\partial u_i}\\right)^2+\\left(\\dfrac{\\partial z}{\\partial u_i}\\right)^2}", "曲线坐标的拉梅系数"),
    ("弧长元", "ds^2 = h_1^2du_1^2+h_2^2du_2^2+h_3^2du_3^2", "正交曲线坐标弧长元"),
    ("体积元", "dV = h_1h_2h_3\\,du_1du_2du_3", "正交曲线坐标体积元"),
    ("柱坐标拉梅系数", "h_r=1,\\quad h_\\varphi=r,\\quad h_z=1", "柱坐标拉梅系数"),
    ("柱坐标梯度", "\\nabla f = \\dfrac{\\partial f}{\\partial r}\\vec{e}_r+\\dfrac{1}{r}\\dfrac{\\partial f}{\\partial \\varphi}\\vec{e}_\\varphi+\\dfrac{\\partial f}{\\partial z}\\vec{e}_z", "柱坐标梯度"),
    ("柱坐标散度", "\\nabla\\cdot\\vec{F} = \\dfrac{1}{r}\\dfrac{\\partial(rF_r)}{\\partial r}+\\dfrac{1}{r}\\dfrac{\\partial F_\\varphi}{\\partial \\varphi}+\\dfrac{\\partial F_z}{\\partial z}", "柱坐标散度"),
    ("柱坐标旋度", "\\nabla\\times\\vec{F} = \\dfrac{1}{r}\\begin{vmatrix}\\vec{e}_r&r\\vec{e}_\\varphi&\\vec{e}_z\\\\ \\partial_r&\\partial_\\varphi&\\partial_z\\\\ F_r&rF_\\varphi&F_z\\end{vmatrix}", "柱坐标旋度"),
    ("球坐标拉梅系数", "h_r=1,\\quad h_\\theta=r,\\quad h_\\varphi=r\\sin\\theta", "球坐标拉梅系数"),
    ("球坐标梯度", "\\nabla f = \\dfrac{\\partial f}{\\partial r}\\vec{e}_r+\\dfrac{1}{r}\\dfrac{\\partial f}{\\partial\\theta}\\vec{e}_\\theta+\\dfrac{1}{r\\sin\\theta}\\dfrac{\\partial f}{\\partial\\varphi}\\vec{e}_\\varphi", "球坐标梯度"),
    ("球坐标散度", "\\nabla\\cdot\\vec{F} = \\dfrac{1}{r^2}\\dfrac{\\partial(r^2F_r)}{\\partial r}+\\dfrac{1}{r\\sin\\theta}\\dfrac{\\partial(\\sin\\theta F_\\theta)}{\\partial\\theta}+\\dfrac{1}{r\\sin\\theta}\\dfrac{\\partial F_\\varphi}{\\partial\\varphi}", "球坐标散度"),
    ("球坐标拉普拉斯", "\\nabla^2 f = \\dfrac{1}{r^2}\\dfrac{\\partial}{\\partial r}\\left(r^2\\dfrac{\\partial f}{\\partial r}\\right)+\\dfrac{1}{r^2\\sin\\theta}\\dfrac{\\partial}{\\partial \\theta}\\left(\\sin\\theta\\dfrac{\\partial f}{\\partial \\theta}\\right)+\\dfrac{1}{r^2\\sin^2\\theta}\\dfrac{\\partial^2 f}{\\partial \\varphi^2}", "球坐标拉普拉斯"),
    ("正交坐标梯度通式", "\\nabla f = \\sum_{i=1}^3 \\dfrac{1}{h_i}\\dfrac{\\partial f}{\\partial u_i}\\vec{e}_i", "梯度通式"),
    ("正交坐标散度通式", "\\nabla\\cdot\\vec{F} = \\dfrac{1}{h_1h_2h_3}\\sum_i\\dfrac{\\partial(h_1h_2h_3 F_i/h_i)}{\\partial u_i}", "散度通式"),
    ("并矢定义", "\\vec{a}\\vec{b} = \\sum_{i,j} a_i b_j \\vec{e}_i\\vec{e}_j", "并矢有 9 个分量"),
    ("并矢双点积", "\\vec{a}\\vec{b}:\\vec{c}\\vec{d} = (\\vec{a}\\cdot\\vec{c})(\\vec{b}\\cdot\\vec{d})", "双点积为标量"),
    ("二阶张量矩阵", "\\mathbf{T} = \\begin{pmatrix}T_{11}&T_{12}&T_{13}\\\\T_{21}&T_{22}&T_{23}\\\\T_{31}&T_{32}&T_{33}\\end{pmatrix}", "二阶张量的矩阵表示"),
    ("单位张量", "\\mathbf{I} = \\vec{e}_1\\vec{e}_1+\\vec{e}_2\\vec{e}_2+\\vec{e}_3\\vec{e}_3", "克罗内克 delta 张量"),
    ("张量缩并", "C = \\sum_i T_{ii} = \\mathrm{tr}(\\mathbf{T})", "张量的迹（一次缩并）"),
    ("张量点积", "(\\mathbf{T}\\cdot\\vec{a})_i = \\sum_j T_{ij}a_j", "张量与矢量的点积"),
    ("张量坐标变换", "T'_{ij} = \\sum_{k,l} R_{ik}R_{jl}T_{kl}", "二阶张量变换法则"),
    ("梯度乘积规则", "\\nabla(uv) = v\\nabla u + u\\nabla v", "标量乘积的梯度"),
    ("散度乘积规则", "\\nabla\\cdot(u\\vec{F}) = u(\\nabla\\cdot\\vec{F})+\\nabla u\\cdot\\vec{F}", "标量乘矢量的散度"),
    ("旋度乘积规则", "\\nabla\\times(u\\vec{F}) = u(\\nabla\\times\\vec{F})+\\nabla u\\times\\vec{F}", "标量乘矢量的旋度"),
    ("叉积散度恒等式", "\\nabla\\cdot(\\vec{F}\\times\\vec{G}) = \\vec{G}\\cdot(\\nabla\\times\\vec{F})-\\vec{F}\\cdot(\\nabla\\times\\vec{G})", "叉积的散度"),
    ("叉积旋度恒等式", "\\nabla\\times(\\vec{F}\\times\\vec{G}) = \\vec{F}(\\nabla\\cdot\\vec{G})-\\vec{G}(\\nabla\\cdot\\vec{F})+(\\vec{G}\\cdot\\nabla)\\vec{F}-(\\vec{F}\\cdot\\nabla)\\vec{G}", "叉积的旋度"),
    ("点积梯度恒等式", "\\nabla(\\vec{F}\\cdot\\vec{G}) = (\\vec{F}\\cdot\\nabla)\\vec{G}+(\\vec{G}\\cdot\\nabla)\\vec{F}+\\vec{F}\\times(\\nabla\\times\\vec{G})+\\vec{G}\\times(\\nabla\\times\\vec{F})", "点积的梯度"),
    ("矢量拉普拉斯", "\\nabla^2\\vec{F} = \\nabla(\\nabla\\cdot\\vec{F})-\\nabla\\times(\\nabla\\times\\vec{F})", "矢量拉普拉斯恒等式"),
    ("亥姆霍兹分解", "\\vec{F} = -\\nabla\\phi+\\nabla\\times\\vec{A}", "任意矢量场可分解为无旋+无源"),
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

# ============ 第一章 矢量运算 ============
ch1_sections = [
{"name":"1.1 向量的基本运算","color":"#2563eb","desc":"向量的概念、表示、加法、数乘与线性相关性",
"items":[
{"id":"v1s1-1","name":"向量的概念与表示","tags":["def","exa"],"brief":"既有大小又有方向的量，用分量或几何有向线段表示。",
"body":wrap(
 defn("向量",p("既有大小又有方向的量称为<strong>向量</strong>（矢量）。在直角坐标系中，向量 $\\vec{a}$ 可表示为：")+
 fml("\\vec{a} = a_x\\vec{i} + a_y\\vec{j} + a_z\\vec{k} = (a_x, a_y, a_z)")+
 p("其模（大小）为 $|\\vec{a}|=\\sqrt{a_x^2+a_y^2+a_z^2}$。"))+
 note(p("只有大小没有方向的量称为标量。向量与起点无关，可自由平移（自由向量）。单位向量 $\\vec{a}^0 = \\dfrac{\\vec{a}}{|\\vec{a}|}$。"))+
 der(p("<strong>由模长公式推导单位向量：</strong>设 $\\vec{a}^0 = \\lambda\\vec{a}$ 且 $|\\vec{a}^0|=1$，则 $|\\lambda\\vec{a}|=|\\lambda||\\vec{a}|=1$，取 $\\lambda>0$ 得 $\\lambda=1/|\\vec{a}|$，故 $\\vec{a}^0=\\vec{a}/|\\vec{a}|$。"))
)},
{"id":"v1s1-2","name":"向量的加法与数乘","tags":["def","thm","der"],"brief":"平行四边形法则、三角形法则与数乘运算律。",
"fig":"vector_add","figCap":"向量加法的平行四边形法则：a+b 为平行四边形对角线",
"body":wrap(
 defn("向量加法",p("两向量 $\\vec{a},\\vec{b}$ 相加满足<strong>平行四边形法则</strong>（或三角形法则）：将 $\\vec{b}$ 平移使其起点与 $\\vec{a}$ 终点重合，则从 $\\vec{a}$ 起点到 $\\vec{b}$ 终点的向量为 $\\vec{a}+\\vec{b}$。分量形式：")+
 fml("\\vec{a}+\\vec{b} = (a_x+b_x,\\ a_y+b_y,\\ a_z+b_z)"))+
 defn("数乘向量",p("实数 $\\lambda$ 与向量 $\\vec{a}$ 的乘积 $\\lambda\\vec{a}$ 仍为向量：")+
 fml("\\lambda\\vec{a} = (\\lambda a_x,\\ \\lambda a_y,\\ \\lambda a_z),\\quad |\\lambda\\vec{a}|=|\\lambda||\\vec{a}|")+
 p("方向：$\\lambda>0$ 时与 $\\vec{a}$ 同向，$\\lambda<0$ 时反向。"))+
 thm("运算律",p("加法满足交换律、结合律；数乘满足结合律与分配律：")+
 fml("\\vec{a}+\\vec{b}=\\vec{b}+\\vec{a},\\quad (\\vec{a}+\\vec{b})+\\vec{c}=\\vec{a}+(\\vec{b}+\\vec{c})")+
 fml("\\lambda(\\mu\\vec{a})=(\\lambda\\mu)\\vec{a},\\quad \\lambda(\\vec{a}+\\vec{b})=\\lambda\\vec{a}+\\lambda\\vec{b}"))+
 der(p("<strong>交换律推导：</strong>分量形式中 $a_i+b_i=b_i+a_i$（实数加法交换律），故各分量相等，向量相等。平行四边形法则中对角线与选取起点无关，几何上亦成立。"))
)},
{"id":"v1s1-3","name":"线性相关与无关","tags":["def","thm","der"],"brief":"判断向量组是否可互相线性表示。",
"body":wrap(
 defn("线性组合",p("对向量 $\\vec{a}_1,\\vec{a}_2,\\ldots,\\vec{a}_n$，表达式 $k_1\\vec{a}_1+k_2\\vec{a}_2+\\cdots+k_n\\vec{a}_n$ 称为它们的<strong>线性组合</strong>。"))+
 defn("线性相关",p("若存在不全为零的数 $k_1,\\ldots,k_n$ 使 $\\sum k_i\\vec{a}_i=\\vec{0}$，则称向量组<strong>线性相关</strong>；否则称<strong>线性无关</strong>。"))+
 thm("判定定理",p("① 两个向量线性相关 $\\iff$ 它们平行；<br>② 三个向量线性相关 $\\iff$ 它们共面；<br>③ $n$ 维空间中 $n+1$ 个向量必线性相关。"))+
 der(p("<strong>三向量共面推导：</strong>若 $\\vec{a},\\vec{b},\\vec{c}$ 线性相关，存在不全为零的 $k_1,k_2,k_3$ 使 $k_1\\vec{a}+k_2\\vec{b}+k_3\\vec{c}=\\vec{0}$。不妨 $k_3\\neq 0$，则 $\\vec{c}=-(k_1/k_3)\\vec{a}-(k_2/k_3)\\vec{b}$，即 $\\vec{c}$ 可由 $\\vec{a},\\vec{b}$ 线性表示，故三向量共面。反之，若共面，$\\vec{c}$ 可表为 $\\vec{a},\\vec{b}$ 的线性组合，即存在相关关系。"))
)}
]},
{"name":"1.2 点积","color":"#3b82f6","desc":"点积的定义、几何意义、性质与投影",
"items":[
{"id":"v1s2-1","name":"点积（标量积）","tags":["def","thm","der"],"brief":"a·b=|a||b|cosθ，结果为标量，几何上是投影。",
"fig":"dot_product","figCap":"点积 a·b = |a|(|b|cosθ)，即 |a| 乘以 b 在 a 上的投影",
"body":wrap(
 defn("点积",p("两向量 $\\vec{a},\\vec{b}$ 的<strong>点积</strong>（内积、标量积）定义为：")+
 fml("\\vec{a}\\cdot\\vec{b} = |\\vec{a}||\\vec{b}|\\cos\\theta")+
 p("其中 $\\theta$ 为 $\\vec{a}$ 与 $\\vec{b}$ 的夹角（$0\\le\\theta\\le\\pi$）。分量形式：")+
 fml("\\vec{a}\\cdot\\vec{b} = a_xb_x + a_yb_y + a_zb_z"))+
 thm("性质",p("① $\\vec{a}\\cdot\\vec{a}=|\\vec{a}|^2$；<br>② $\\vec{a}\\perp\\vec{b}\\iff\\vec{a}\\cdot\\vec{b}=0$；<br>③ 交换律 $\\vec{a}\\cdot\\vec{b}=\\vec{b}\\cdot\\vec{a}$；<br>④ 分配律 $\\vec{a}\\cdot(\\vec{b}+\\vec{c})=\\vec{a}\\cdot\\vec{b}+\\vec{a}\\cdot\\vec{c}$。"))+
 der(p("<strong>几何意义推导：</strong>$\\vec{b}$ 在 $\\vec{a}$ 方向上的投影长度为 $|\\vec{b}|\\cos\\theta$，故 $\\vec{a}\\cdot\\vec{b}=|\\vec{a}|(|\\vec{b}|\\cos\\theta)$。当 $\\vec{a}$ 为单位向量时，点积即为投影长度。由此可定义投影向量 $\\mathrm{proj}_{\\vec{a}}\\vec{b}=\\dfrac{\\vec{a}\\cdot\\vec{b}}{|\\vec{a}|^2}\\vec{a}$。"))+
 der(p("<strong>分量形式推导：</strong>利用 $\\vec{i}\\cdot\\vec{i}=\\vec{j}\\cdot\\vec{j}=\\vec{k}\\cdot\\vec{k}=1$，$\\vec{i}\\cdot\\vec{j}=\\vec{j}\\cdot\\vec{k}=\\vec{k}\\cdot\\vec{i}=0$，将 $\\vec{a}=a_x\\vec{i}+a_y\\vec{j}+a_z\\vec{k}$，$\\vec{b}=b_x\\vec{i}+b_y\\vec{j}+b_z\\vec{k}$ 展开点积，交叉项为零，得 $\\vec{a}\\cdot\\vec{b}=a_xb_x+a_yb_y+a_zb_z$。"))
)}
]},
{"name":"1.3 叉积与混合积","color":"#1d4ed8","desc":"叉积的定义、右手定则、行列式计算，以及混合积",
"items":[
{"id":"v1s3-1","name":"叉积（矢量积）","tags":["def","thm","der"],"brief":"a×b 为垂直于 a,b 的向量，模为 |a||b|sinθ。",
"fig":"cross_product","figCap":"叉积 a×b 方向垂直于 a,b 平面，满足右手定则",
"body":wrap(
 defn("叉积",p("两向量 $\\vec{a},\\vec{b}$ 的<strong>叉积</strong>（外积、矢量积）定义为一个向量：")+
 fml("\\vec{a}\\times\\vec{b} = |\\vec{a}||\\vec{b}|\\sin\\theta\\ \\vec{n}")+
 p("其中 $\\vec{n}$ 为垂直于 $\\vec{a},\\vec{b}$ 所在平面的单位向量，方向由<strong>右手定则</strong>确定。分量形式：")+
 fml("\\vec{a}\\times\\vec{b} = \\begin{vmatrix}\\vec{i}&\\vec{j}&\\vec{k}\\\\a_x&a_y&a_z\\\\b_x&b_y&b_z\\end{vmatrix}")+
 p("展开得 $(a_yb_z-a_zb_y,\\ a_zb_x-a_xb_z,\\ a_xb_y-a_yb_x)$。"))+
 thm("性质",p("① 反交换律：$\\vec{a}\\times\\vec{b}=-\\vec{b}\\times\\vec{a}$；<br>② $\\vec{a}\\parallel\\vec{b}\\iff\\vec{a}\\times\\vec{b}=0$；<br>③ $|\\vec{a}\\times\\vec{b}|$ 等于以 $\\vec{a},\\vec{b}$ 为邻边的平行四边形面积；<br>④ 分配律：$\\vec{a}\\times(\\vec{b}+\\vec{c})=\\vec{a}\\times\\vec{b}+\\vec{a}\\times\\vec{c}$。"))+
 der(p("<strong>反交换律推导：</strong>由定义，$\\vec{b}\\times\\vec{a}=|\\vec{b}||\\vec{a}|\\sin\\theta\\ \\vec{n}'$，其中 $\\vec{n}'$ 由右手定则从 $\\vec{b}$ 转向 $\\vec{a}$ 确定，与从 $\\vec{a}$ 转向 $\\vec{b}$ 的 $\\vec{n}$ 方向相反，故 $\\vec{n}'=-\\vec{n}$，因此 $\\vec{b}\\times\\vec{a}=-\\vec{a}\\times\\vec{b}$。"))+
 der(p("<strong>模长=面积推导：</strong>平行四边形面积 = 底 $\\times$ 高 = $|\\vec{a}|\\times(|\\vec{b}|\\sin\\theta)=|\\vec{a}||\\vec{b}|\\sin\\theta=|\\vec{a}\\times\\vec{b}|$。"))
)},
{"id":"v1s3-2","name":"混合积与多重积","tags":["def","thm","der"],"brief":"(a×b)·c 的几何意义为平行六面体体积，以及 BAC-CAB 公式。",
"body":wrap(
 defn("混合积",p("三向量 $\\vec{a},\\vec{b},\\vec{c}$ 的<strong>混合积</strong>定义为：")+
 fml("[\\vec{a}\\ \\vec{b}\\ \\vec{c}] = (\\vec{a}\\times\\vec{b})\\cdot\\vec{c}")+
 p("其绝对值等于以 $\\vec{a},\\vec{b},\\vec{c}$ 为棱的平行六面体体积。"))+
 thm("轮换对称性",p("混合积具有轮换对称性：")+
 fml("(\\vec{a}\\times\\vec{b})\\cdot\\vec{c} = (\\vec{b}\\times\\vec{c})\\cdot\\vec{a} = (\\vec{c}\\times\\vec{a})\\cdot\\vec{b}")+
 p("且三向量共面 $\\iff (\\vec{a}\\times\\vec{b})\\cdot\\vec{c}=0$。"))+
 thm("BAC-CAB 公式",p("二重叉积满足：")+
 fml("\\vec{a}\\times(\\vec{b}\\times\\vec{c}) = \\vec{b}(\\vec{a}\\cdot\\vec{c})-\\vec{c}(\\vec{a}\\cdot\\vec{b})"))+
 der(p("<strong>体积意义推导：</strong>$|\\vec{a}\\times\\vec{b}|$ 为底面积，$\\vec{c}$ 在垂直于底面方向的投影高为 $|\\vec{c}\\cos\\phi|$（$\\phi$ 为 $\\vec{c}$ 与法向夹角），故体积 $V=|\\vec{a}\\times\\vec{b}||\\vec{c}\\cos\\phi|=|(\\vec{a}\\times\\vec{b})\\cdot\\vec{c}|$。"))+
 der(p("<strong>BAC-CAB 推导（分量法）：</strong>记 $\\vec{D}=\\vec{b}\\times\\vec{c}$，则 $D_x=b_yc_z-b_zc_y$。$\\vec{a}\\times\\vec{D}$ 的 $x$ 分量为 $a_yD_z-a_zD_y=a_y(b_zc_x-b_xc_z)-a_z(b_xc_y-b_yc_x)=b_x(a_yc_y+a_zc_z)-c_x(a_yb_y+a_zb_z)$。加减 $a_xb_xc_x$ 项，整理得 $b_x(\\vec{a}\\cdot\\vec{c})-c_x(\\vec{a}\\cdot\\vec{b})$。同理 $y,z$ 分量，合并即得 BAC-CAB。"))
)}
]}
]

# ============ 第二章 矢量微积分 ============
ch2_sections = [
{"name":"2.1 矢量函数的导数与积分","color":"#0d9488","desc":"矢量函数的求导法则、几何意义与线积分",
"items":[
{"id":"v2s1-1","name":"矢量函数的导数","tags":["def","thm","der"],"brief":"矢量函数对参数求导，几何上是切向量。",
"body":wrap(
 defn("矢量函数",p("若对参数 $t$ 的每个值都对应一个向量 $\\vec{A}(t)$，则称 $\\vec{A}(t)$ 为<strong>矢量函数</strong>。分量表示：$\\vec{A}(t)=A_x(t)\\vec{i}+A_y(t)\\vec{j}+A_z(t)\\vec{k}$。"))+
 defn("导数定义",p("矢量函数 $\\vec{A}(t)$ 的导数定义为：")+
 fml("\\dfrac{d\\vec{A}}{dt} = \\lim_{\\Delta t\\to 0}\\dfrac{\\vec{A}(t+\\Delta t)-\\vec{A}(t)}{\\Delta t}")+
 p("分量形式：$\\dfrac{d\\vec{A}}{dt} = \\dfrac{dA_x}{dt}\\vec{i}+\\dfrac{dA_y}{dt}\\vec{j}+\\dfrac{dA_z}{dt}\\vec{k}$。"))+
 thm("求导法则",p("① $\\dfrac{d}{dt}(\\vec{A}\\pm\\vec{B})=\\dfrac{d\\vec{A}}{dt}\\pm\\dfrac{d\\vec{B}}{dt}$；<br>② $\\dfrac{d}{dt}(\\lambda\\vec{A})=\\dfrac{d\\lambda}{dt}\\vec{A}+\\lambda\\dfrac{d\\vec{A}}{dt}$；<br>③ $\\dfrac{d}{dt}(\\vec{A}\\cdot\\vec{B})=\\dfrac{d\\vec{A}}{dt}\\cdot\\vec{B}+\\vec{A}\\cdot\\dfrac{d\\vec{B}}{dt}$；<br>④ $\\dfrac{d}{dt}(\\vec{A}\\times\\vec{B})=\\dfrac{d\\vec{A}}{dt}\\times\\vec{B}+\\vec{A}\\times\\dfrac{d\\vec{B}}{dt}$。"))+
 der(p("<strong>几何意义推导：</strong>$\\vec{r}(t)$ 为空间曲线的位置矢量，$\\Delta\\vec{r}=\\vec{r}(t+\\Delta t)-\\vec{r}(t)$ 为割线方向向量。当 $\\Delta t\\to 0$ 时，割线趋近于切线，故 $\\dfrac{d\\vec{r}}{dt}=\\lim\\dfrac{\\Delta\\vec{r}}{\\Delta t}$ 沿曲线切线方向，即<strong>切向量</strong>。若 $t$ 为弧长 $s$，则 $\\dfrac{d\\vec{r}}{ds}$ 为单位切向量。"))+
 der(p("<strong>点积求导推导：</strong>$\\dfrac{d}{dt}(\\vec{A}\\cdot\\vec{B})=\\lim\\dfrac{(\\vec{A}+\\Delta\\vec{A})\\cdot(\\vec{B}+\\Delta\\vec{B})-\\vec{A}\\cdot\\vec{B}}{\\Delta t}=\\lim\\left(\\dfrac{\\Delta\\vec{A}}{\\Delta t}\\cdot\\vec{B}+\\vec{A}\\cdot\\dfrac{\\Delta\\vec{B}}{\\Delta t}+\\dfrac{\\Delta\\vec{A}\\cdot\\Delta\\vec{B}}{\\Delta t}\\right)=\\dfrac{d\\vec{A}}{dt}\\cdot\\vec{B}+\\vec{A}\\cdot\\dfrac{d\\vec{B}}{dt}$（最后一项为高阶无穷小）。"))
)},
{"id":"v2s1-2","name":"矢量函数的积分（线积分）","tags":["def","thm","der"],"brief":"第一型与第二型曲线积分的定义与计算。",
"body":wrap(
 defn("第一型线积分（对弧长）",p("设 $f(x,y,z)$ 在曲线 $L$ 上连续，$L$ 由 $\\vec{r}(t)=(x(t),y(t),z(t)),\\alpha\\le t\\le\\beta$ 给出，则：")+
 fml("\\int_L f(x,y,z)\\,ds = \\int_\\alpha^\\beta f(x(t),y(t),z(t))\\sqrt{x'(t)^2+y'(t)^2+z'(t)^2}\\,dt"))+
 defn("第二型线积分（对坐标）",p("设 $\\vec{F}=(P,Q,R)$，则沿曲线 $L$ 的第二型线积分为：")+
 fml("\\int_L \\vec{F}\\cdot d\\vec{r} = \\int_L Pdx+Qdy+Rdz = \\int_\\alpha^\\beta \\vec{F}(\\vec{r}(t))\\cdot\\vec{r}'(t)\\,dt"))+
 thm("两型线积分关系",p("第二型线积分可化为第一型：$\\int_L\\vec{F}\\cdot d\\vec{r}=\\int_L(\\vec{F}\\cdot\\vec{\\tau})\\,ds$，其中 $\\vec{\\tau}$ 为曲线单位切向量。"))+
 der(p("<strong>弧长元推导：</strong>由弧长微分 $ds=\\sqrt{(dx)^2+(dy)^2+(dz)^2}$，代入 $dx=x'(t)dt$ 等，得 $ds=\\sqrt{x'(t)^2+y'(t)^2+z'(t)^2}\\,dt$。第一型线积分即把曲线分成微元 $ds$，每点乘以函数值后求和取极限。"))+
 der(p("<strong>第二型线积分物理意义：</strong>质点在力场 $\\vec{F}$ 中沿曲线 $L$ 运动，力所做的功 $W=\\int_L\\vec{F}\\cdot d\\vec{r}$。将位移微元 $d\\vec{r}=\\vec{r}'(t)dt$ 代入即得计算公式。功的正负取决于力与位移方向夹角。"))
)}
]},
{"name":"2.2 场与方向导数","color":"#14b8a6","desc":"标量场、矢量场、方向导数与链式法则",
"items":[
{"id":"v2s2-1","name":"标量场与矢量场","tags":["def","exa"],"brief":"空间中点对应标量或矢量的分布。",
"body":wrap(
 defn("标量场",p("若空间区域 $V$ 内每一点 $M$ 都对应一个标量 $u(M)$，则称在 $V$ 上定义了一个<strong>标量场</strong> $u=u(x,y,z)$。如温度场、密度场、电势场。"))+
 defn("矢量场",p("若空间区域 $V$ 内每一点 $M$ 都对应一个矢量 $\\vec{F}(M)$，则称在 $V$ 上定义了一个<strong>矢量场</strong> $\\vec{F}=\\vec{F}(x,y,z)=(P,Q,R)$。如力场、速度场、电场。"))+
 exa(p("<strong>例：</strong>静电场中电势 $\\phi(x,y,z)$ 是标量场，电场强度 $\\vec{E}=-\\nabla\\phi$ 是矢量场。不可压缩流体的速度场 $\\vec{v}(x,y,z)$ 是矢量场。"))+
 der(p("<strong>场的等值面/矢量线：</strong>标量场用等值面 $u=C$ 描述；矢量场用矢量线（积分曲线满足 $\\dfrac{dx}{P}=\\dfrac{dy}{Q}=\\dfrac{dz}{R}$）描述。等值面与矢量线分别刻画场的空间分布形态。"))
)},
{"id":"v2s2-2","name":"方向导数与链式法则","tags":["def","thm","der"],"brief":"方向导数是梯度在该方向的投影。",
"body":wrap(
 defn("方向导数",p("标量场 $u(x,y,z)$ 在点 $M$ 沿方向 $\\vec{l}$ 的<strong>方向导数</strong>定义为：")+
 fml("\\dfrac{\\partial u}{\\partial l} = \\lim_{\\rho\\to 0}\\dfrac{u(M')-u(M)}{\\rho}")+
 p("计算公式：$\\dfrac{\\partial u}{\\partial l} = \\dfrac{\\partial u}{\\partial x}\\cos\\alpha+\\dfrac{\\partial u}{\\partial y}\\cos\\beta+\\dfrac{\\partial u}{\\partial z}\\cos\\gamma$。"))+
 defn("梯度",p("标量场 $u$ 的<strong>梯度</strong>定义为矢量：")+
 fml("\\nabla u = \\left(\\dfrac{\\partial u}{\\partial x},\\dfrac{\\partial u}{\\partial y},\\dfrac{\\partial u}{\\partial z}\\right)"))+
 thm("梯度与方向导数关系",p("")+
 fml("\\dfrac{\\partial u}{\\partial l} = \\nabla u \\cdot \\vec{l}^0 = |\\nabla u|\\cos\\theta")+
 p("梯度方向是函数增长最快的方向，梯度的模是最大方向导数。"))+
 thm("复合函数链式法则",p("若 $u=u(x,y,z)$，而 $x=x(t),y=y(t),z=z(t)$，则：")+
 fml("\\dfrac{du}{dt} = \\dfrac{\\partial u}{\\partial x}\\dfrac{dx}{dt}+\\dfrac{\\partial u}{\\partial y}\\dfrac{dy}{dt}+\\dfrac{\\partial u}{\\partial z}\\dfrac{dz}{dt} = \\nabla u\\cdot\\dfrac{d\\vec{r}}{dt}"))+
 der(p("<strong>方向导数推导：</strong>设 $\\vec{l}^0=(\\cos\\alpha,\\cos\\beta,\\cos\\gamma)$，沿 $\\vec{l}$ 方向动点坐标为 $x+x_0+\\rho\\cos\\alpha$ 等。由全微分 $du=u_xdx+u_ydy+u_zdz$，除以 $\\rho$ 取极限得 $\\dfrac{\\partial u}{\\partial l}=u_x\\cos\\alpha+u_y\\cos\\beta+u_z\\cos\\gamma=\\nabla u\\cdot\\vec{l}^0$。"))+
 der(p("<strong>链式法则推导：</strong>由全微分 $du=u_xdx+u_ydy+u_zdz$，两边除以 $dt$，因 $dx=x'(t)dt$ 等，得 $\\dfrac{du}{dt}=u_xx'+u_yy'+u_zz'=\\nabla u\\cdot\\dfrac{d\\vec{r}}{dt}$。几何上表示沿轨道 $\\vec{r}(t)$ 函数的变化率等于梯度与速度的点积。"))
)},
{"id":"v2s2-3","name":"梯度的运算性质","tags":["thm","der","app"],"brief":"梯度的四则运算与复合函数梯度规则。",
"body":wrap(
 thm("梯度运算规则",p("设 $u,v$ 为标量场：<br>① $\\nabla(u\\pm v)=\\nabla u\\pm\\nabla v$；<br>② $\\nabla(uv)=v\\nabla u+u\\nabla v$；<br>③ $\\nabla\\left(\\dfrac{u}{v}\\right)=\\dfrac{v\\nabla u-u\\nabla v}{v^2}\\ (v\\neq 0)$；<br>④ $\\nabla f(u)=f'(u)\\nabla u$（复合函数）。"))+
 der(p("<strong>商的梯度推导：</strong>$\\nabla\\left(\\dfrac{u}{v}\\right)$ 的 $i$ 分量为 $\\dfrac{\\partial}{\\partial x_i}\\left(\\dfrac{u}{v}\\right)=\\dfrac{v\\dfrac{\\partial u}{\\partial x_i}-u\\dfrac{\\partial v}{\\partial x_i}}{v^2}=\\dfrac{v(\\nabla u)_i-u(\\nabla v)_i}{v^2}$，故 $\\nabla\\left(\\dfrac{u}{v}\\right)=\\dfrac{v\\nabla u-u\\nabla v}{v^2}$。"))+
 der(p("<strong>复合函数梯度推导：</strong>$\\nabla f(u)$ 的 $i$ 分量为 $\\dfrac{\\partial f(u)}{\\partial x_i}=f'(u)\\dfrac{\\partial u}{\\partial x_i}=f'(u)(\\nabla u)_i$，故 $\\nabla f(u)=f'(u)\\nabla u$。例如 $\\nabla(u^n)=n u^{n-1}\\nabla u$。"))+
 app(p("<strong>应用：</strong>点电荷电势 $\\varphi=\\dfrac{q}{4\\pi\\varepsilon_0 r}$，电场 $\\vec{E}=-\\nabla\\varphi=\\dfrac{q}{4\\pi\\varepsilon_0 r^2}\\vec{e}_r$（利用 $\\nabla r=\\vec{e}_r$，$\\nabla(1/r)=-\\vec{e}_r/r^2$）。"))
)}
]}
]

# ============ 第三章 梯度 散度 旋度 ============
ch3_sections = [
{"name":"3.1 梯度与散度","color":"#c2410c","desc":"梯度的几何意义、散度的通量定义与物理意义",
"items":[
{"id":"v3s1-1","name":"梯度","tags":["def","thm","der"],"brief":"梯度垂直等值面，指向函数增大方向。",
"body":wrap(
 defn("梯度",p("标量场 $u(x,y,z)$ 的<strong>梯度</strong>为矢量：")+
 fml("\\nabla u = \\dfrac{\\partial u}{\\partial x}\\vec{i}+\\dfrac{\\partial u}{\\partial y}\\vec{j}+\\dfrac{\\partial u}{\\partial z}\\vec{k}"))+
 thm("几何意义",p("梯度 $\\nabla u$ 在点 $M$ 处垂直于过该点的等值面 $u=C$，且指向 $u$ 增大的方向。梯度的模是该点最大方向导数。"))+
 der(p("<strong>垂直等值面推导：</strong>等值面 $u(x,y,z)=C$ 上任一曲线 $\\vec{r}(t)=(x(t),y(t),z(t))$ 满足 $u(x(t),y(t),z(t))=C$。对 $t$ 求导：$u_x\\dot{x}+u_y\\dot{y}+u_z\\dot{z}=0$，即 $\\nabla u\\cdot\\dot{\\vec{r}}=0$。因 $\\dot{\\vec{r}}$ 为等值面任意切向量，故 $\\nabla u$ 垂直于等值面。"))+
 der(p("<strong>指向增大方向推导：</strong>沿梯度方向 $\\vec{l}^0=\\nabla u/|\\nabla u|$，方向导数 $\\dfrac{\\partial u}{\\partial l}=\\nabla u\\cdot\\vec{l}^0=|\\nabla u|>0$，故函数沿梯度方向增大，梯度指向增大方向。"))
)},
{"id":"v3s1-2","name":"散度","tags":["def","thm","der"],"brief":"散度是单位体积的通量，描述源汇强度。",
"fig":"gauss","figCap":"闭合曲面 S 包围体积 V，矢量场 F 穿过 S 的通量",
"body":wrap(
 defn("通量",p("矢量场 $\\vec{F}$ 穿过曲面 $S$ 的<strong>通量</strong>为：")+
 fml("\\Phi = \\iint_S \\vec{F}\\cdot d\\vec{S} = \\iint_S \\vec{F}\\cdot\\vec{n}\\,dS")+
 p("其中 $\\vec{n}$ 为曲面法向量。对闭合曲面，$\\vec{n}$ 取外法向。"))+
 defn("散度",p("矢量场 $\\vec{F}$ 在点 $M$ 的<strong>散度</strong>定义为单位体积的通量：")+
 fml("\\nabla\\cdot\\vec{F} = \\lim_{\\Delta V\\to 0}\\dfrac{1}{\\Delta V}\\oiint_{\\Delta S}\\vec{F}\\cdot d\\vec{S}")+
 p("直角坐标系中：$\\nabla\\cdot\\vec{F} = \\dfrac{\\partial F_x}{\\partial x}+\\dfrac{\\partial F_y}{\\partial y}+\\dfrac{\\partial F_z}{\\partial z}$。"))+
 thm("物理意义",p("散度 $\\nabla\\cdot\\vec{F}>0$ 表示该点有<strong>源</strong>（流出），$<0$ 表示有<strong>汇</strong>（流入），$=0$ 表示无源。若处处 $\\nabla\\cdot\\vec{F}=0$，则称 $\\vec{F}$ 为<strong>无源场</strong>（管形场）。"))+
 der(p("<strong>直角坐标公式推导：</strong>取中心在 $(x,y,z)$、边长 $\\Delta x,\\Delta y,\\Delta z$ 的小长方体。右面（$x+\\Delta x/2$）通量约为 $F_x(x+\\Delta x/2)\\Delta y\\Delta z\\approx[F_x+\\frac{\\partial F_x}{\\partial x}\\frac{\\Delta x}{2}]\\Delta y\\Delta z$；左面通量为 $-F_x(x-\\Delta x/2)\\Delta y\\Delta z\\approx-[F_x-\\frac{\\partial F_x}{\\partial x}\\frac{\\Delta x}{2}]\\Delta y\\Delta z$。两面之和为 $\\frac{\\partial F_x}{\\partial x}\\Delta x\\Delta y\\Delta z$。三对面相加后除以体积 $\\Delta V=\\Delta x\\Delta y\\Delta z$，得散度公式。"))
)}
]},
{"name":"3.2 旋度","color":"#ea580c","desc":"环量、旋度的定义与物理意义",
"items":[
{"id":"v3s2-1","name":"环量与旋度","tags":["def","thm","der"],"brief":"旋度描述矢量场的旋转特性。",
"fig":"curl","figCap":"旋度 curl F 的方向沿右手螺旋，垂直于矢量场旋转平面",
"body":wrap(
 defn("环量",p("矢量场 $\\vec{F}$ 沿闭合曲线 $L$ 的<strong>环量</strong>为：")+
 fml("\\Gamma = \\oint_L \\vec{F}\\cdot d\\vec{l}"))+
 defn("旋度",p("矢量场 $\\vec{F}$ 在点 $M$ 的<strong>旋度</strong>是一个矢量，其方向沿使环量面密度最大的法向，大小为该最大环量面密度。直角坐标系中：")+
 fml("\\nabla\\times\\vec{F} = \\begin{vmatrix}\\vec{i}&\\vec{j}&\\vec{k}\\\\ \\dfrac{\\partial}{\\partial x}&\\dfrac{\\partial}{\\partial y}&\\dfrac{\\partial}{\\partial z}\\\\ F_x&F_y&F_z\\end{vmatrix}")+
 p("分量：$\\left(\\dfrac{\\partial F_z}{\\partial y}-\\dfrac{\\partial F_y}{\\partial z},\\ \\dfrac{\\partial F_x}{\\partial z}-\\dfrac{\\partial F_z}{\\partial x},\\ \\dfrac{\\partial F_y}{\\partial x}-\\dfrac{\\partial F_x}{\\partial y}\\right)$。"))+
 thm("物理意义",p("旋度 $\\nabla\\times\\vec{F}\\neq 0$ 表示场有<strong>涡旋</strong>（旋转），若处处 $\\nabla\\times\\vec{F}=0$，则称 $\\vec{F}$ 为<strong>无旋场</strong>（保守场），可表示为某标量场的梯度 $\\vec{F}=\\nabla u$。"))+
 der(p("<strong>旋度分量推导（z 分量）：</strong>取 $xy$ 平面内中心在 $(x,y)$、边长 $\\Delta x,\\Delta y$ 的小矩形，逆时针环量为 $\\oint\\vec{F}\\cdot d\\vec{l}\\approx F_x\\Delta x+(F_y+\\frac{\\partial F_y}{\\partial x}\\Delta x)\\Delta y-(F_x+\\frac{\\partial F_x}{\\partial y}\\Delta y)\\Delta x-F_y\\Delta y=(\\frac{\\partial F_y}{\\partial x}-\\frac{\\partial F_x}{\\partial y})\\Delta x\\Delta y$。除以面积 $\\Delta x\\Delta y$ 得 z 分量 $\\frac{\\partial F_y}{\\partial x}-\\frac{\\partial F_x}{\\partial y}$。其余分量同理。"))
)}
]},
{"name":"3.3 高斯公式、斯托克斯公式与恒等式","color":"#f59e0b","desc":"散度定理、环量定理、零恒等式与拉普拉斯算子",
"items":[
{"id":"v3s3-1","name":"高斯公式（散度定理）","tags":["thm","der","app"],"brief":"闭合曲面通量等于散度的体积分。",
"body":wrap(
 thm("高斯公式",p("设空间闭区域 $V$ 由分片光滑闭合曲面 $S$ 围成，$\\vec{F}$ 在 $V$ 上有连续偏导数，则：")+
 fml("\\oiint_S \\vec{F}\\cdot d\\vec{S} = \\iiint_V (\\nabla\\cdot\\vec{F})\\,dV"))+
 der(p("<strong>证明思路：</strong>将 $V$ 分割为无数小体积元。每个小体积元的通量等于其散度乘以体积（散度定义）。相邻小体积元的公共面通量相互抵消（法向相反），最终只剩下外表面 $S$ 的通量，即得高斯公式。严格证明需用多元函数积分中值定理与极限。"))+
 app(p("<strong>电磁学应用：</strong>电场高斯定理 $\\oiint_S\\vec{E}\\cdot d\\vec{S}=\\dfrac{q}{\\varepsilon_0}$，写成微分形式为 $\\nabla\\cdot\\vec{E}=\\dfrac{\\rho}{\\varepsilon_0}$，其中 $\\rho$ 为电荷密度。磁场 $\\nabla\\cdot\\vec{B}=0$ 表明磁场无源（无磁单极子）。"))
)},
{"id":"v3s3-2","name":"斯托克斯公式","tags":["thm","der","app"],"brief":"闭合曲线环量等于旋度穿过曲面的通量。",
"body":wrap(
 thm("斯托克斯公式",p("设光滑曲面 $S$ 的边界为分段光滑闭合曲线 $L$，$\\vec{F}$ 在 $S$ 上有连续偏导数，则：")+
 fml("\\oint_L \\vec{F}\\cdot d\\vec{l} = \\iint_S (\\nabla\\times\\vec{F})\\cdot d\\vec{S}")+
 p("其中 $L$ 的正向与 $S$ 的法向满足右手定则。"))+
 der(p("<strong>证明思路：</strong>将曲面 $S$ 分割为无数小面元。每个小面元边界的环量等于旋度在该面元法向的投影乘以面积（旋度定义）。相邻面元公共边界的环量相互抵消（方向相反），最终只剩下外边界 $L$ 的环量。"))+
 app(p("<strong>电磁学应用：</strong>法拉第电磁感应定律的微分形式 $\\nabla\\times\\vec{E}=-\\dfrac{\\partial\\vec{B}}{\\partial t}$，由斯托克斯公式可得积分形式 $\\oint_L\\vec{E}\\cdot d\\vec{l}=-\\dfrac{d}{dt}\\iint_S\\vec{B}\\cdot d\\vec{S}$，即感应电动势等于磁通量变化率的负值。"))
)},
{"id":"v3s3-3","name":"零恒等式与拉普拉斯算子","tags":["thm","der"],"brief":"旋度的散度为零，梯度的旋度为零。",
"body":wrap(
 thm("零恒等式",p("对任意有二阶连续偏导数的标量场 $u$ 和矢量场 $\\vec{F}$：")+
 fml("\\nabla\\times(\\nabla u) = 0,\\quad \\nabla\\cdot(\\nabla\\times\\vec{F}) = 0")+
 p("即：<strong>梯度场必无旋，旋度场必无源</strong>。"))+
 defn("拉普拉斯算子",p("梯度的散度称为<strong>拉普拉斯算子</strong>：")+
 fml("\\nabla^2 u = \\nabla\\cdot(\\nabla u) = \\dfrac{\\partial^2 u}{\\partial x^2}+\\dfrac{\\partial^2 u}{\\partial y^2}+\\dfrac{\\partial^2 u}{\\partial z^2}"))+
 der(p("<strong>第一式证明：</strong>$\\nabla\\times(\\nabla u)$ 的 $x$ 分量为 $\\dfrac{\\partial}{\\partial y}\\left(\\dfrac{\\partial u}{\\partial z}\\right)-\\dfrac{\\partial}{\\partial z}\\left(\\dfrac{\\partial u}{\\partial y}\\right)=u_{zy}-u_{yz}=0$（混合偏导连续时相等，克莱罗定理）。$y,z$ 分量同理为零。"))+
 der(p("<strong>第二式证明：</strong>$\\nabla\\cdot(\\nabla\\times\\vec{F})=\\dfrac{\\partial}{\\partial x}(F_{z,y}-F_{y,z})+\\dfrac{\\partial}{\\partial y}(F_{x,z}-F_{z,x})+\\dfrac{\\partial}{\\partial z}(F_{y,x}-F_{x,y})$。每一项如 $\\dfrac{\\partial F_{z,y}}{\\partial x}=F_{z,yx}$ 与 $-\\dfrac{\\partial F_{z,x}}{\\partial y}=-F_{z,xy}$ 抵消（$F_{z,yx}=F_{z,xy}$），总和为零。"))+
 note(p("满足拉普拉斯方程 $\\nabla^2u=0$ 的函数称为调和函数。静电场中无电荷区域的电势 $\\varphi$ 满足 $\\nabla^2\\varphi=0$。"))
)}
]}
]

# ============ 第四章 曲线坐标系 ============
ch4_sections = [
{"name":"4.1 正交曲线坐标系与拉梅系数","color":"#7c3aed","desc":"曲线坐标、拉梅系数、弧长元与体积元",
"items":[
{"id":"v4s1-1","name":"正交曲线坐标与拉梅系数","tags":["def","thm","der"],"brief":"正交曲线坐标中弧长元、体积元与拉梅系数。",
"fig":"coords","figCap":"空间点 P 在柱坐标 (r,φ,z) 与直角坐标中的位置关系",
"body":wrap(
 defn("曲线坐标",p("设 $u_1,u_2,u_3$ 为空间点的曲线坐标，与直角坐标的变换关系为 $x=x(u_1,u_2,u_3),y=y(u_1,u_2,u_3),z=z(u_1,u_2,u_3)$。若三族坐标面处处正交，则称为<strong>正交曲线坐标系</strong>。"))+
 defn("拉梅系数",p("沿坐标曲线 $u_i$ 方向的弧长元 $ds_i=h_i\\,du_i$，其中 $h_i$ 称为<strong>拉梅系数</strong>：")+
 fml("h_i = \\sqrt{\\left(\\dfrac{\\partial x}{\\partial u_i}\\right)^2+\\left(\\dfrac{\\partial y}{\\partial u_i}\\right)^2+\\left(\\dfrac{\\partial z}{\\partial u_i}\\right)^2}"))+
 thm("弧长元与体积元",p("空间弧长元 $ds^2=h_1^2du_1^2+h_2^2du_2^2+h_3^2du_3^2$，体积元 $dV=h_1h_2h_3\\,du_1du_2du_3$。"))+
 der(p("<strong>拉梅系数推导：</strong>坐标曲线 $u_i$（其余坐标固定）的切向量为 $\\dfrac{\\partial\\vec{r}}{\\partial u_i}=\\left(\\dfrac{\\partial x}{\\partial u_i},\\dfrac{\\partial y}{\\partial u_i},\\dfrac{\\partial z}{\\partial u_i}\\right)$，其模长即为 $h_i$。弧长微分 $ds_i=\\left|\\dfrac{\\partial\\vec{r}}{\\partial u_i}\\right|du_i=h_i\\,du_i$。"))+
 der(p("<strong>体积元推导：</strong>正交曲线坐标中，三个坐标方向互相垂直，体积元等于三边弧长元乘积 $dV=ds_1ds_2ds_3=h_1h_2h_3\\,du_1du_2du_3$。柱坐标 $dV=r\\,dr d\\varphi dz$，球坐标 $dV=r^2\\sin\\theta\\,dr d\\theta d\\varphi$。"))
)},
{"id":"v4s1-2","name":"正交曲线坐标中的梯度散度旋度通式","tags":["thm","der"],"brief":"用拉梅系数表示的梯度、散度、旋度一般公式。",
"body":wrap(
 thm("梯度通式",p("")+
 fml("\\nabla f = \\dfrac{1}{h_1}\\dfrac{\\partial f}{\\partial u_1}\\vec{e}_1+\\dfrac{1}{h_2}\\dfrac{\\partial f}{\\partial u_2}\\vec{e}_2+\\dfrac{1}{h_3}\\dfrac{\\partial f}{\\partial u_3}\\vec{e}_3"))+
 thm("散度通式",p("")+
 fml("\\nabla\\cdot\\vec{F} = \\dfrac{1}{h_1h_2h_3}\\left[\\dfrac{\\partial(h_2h_3F_1)}{\\partial u_1}+\\dfrac{\\partial(h_1h_3F_2)}{\\partial u_2}+\\dfrac{\\partial(h_1h_2F_3)}{\\partial u_3}\\right]"))+
 thm("旋度通式",p("")+
 fml("\\nabla\\times\\vec{F} = \\dfrac{1}{h_1h_2h_3}\\begin{vmatrix}h_1\\vec{e}_1&h_2\\vec{e}_2&h_3\\vec{e}_3\\\\ \\dfrac{\\partial}{\\partial u_1}&\\dfrac{\\partial}{\\partial u_2}&\\dfrac{\\partial}{\\partial u_3}\\\\ h_1F_1&h_2F_2&h_3F_3\\end{vmatrix}"))+
 der(p("<strong>梯度通式推导：</strong>沿 $u_i$ 方向的方向导数 $\\dfrac{\\partial f}{\\partial s_i}=\\dfrac{1}{h_i}\\dfrac{\\partial f}{\\partial u_i}$（因 $ds_i=h_i\\,du_i$），梯度在 $\\vec{e}_i$ 方向分量即为该方向导数，故 $\\nabla f=\\sum_i\\dfrac{1}{h_i}\\dfrac{\\partial f}{\\partial u_i}\\vec{e}_i$。"))+
 der(p("<strong>散度通式推导：</strong>取由 $u_1,u_1+du_1$ 等六个坐标面围成的小体积元，其体积 $dV=h_1h_2h_3\\,du_1du_2du_3$。沿 $u_1$ 方向两面通量差为 $\\dfrac{\\partial}{\\partial u_1}(F_1\\cdot h_2h_3\\,du_2du_3)\\,du_1=\\dfrac{\\partial(h_2h_3F_1)}{\\partial u_1}du_1du_2du_3$。三方向通量和除以体积即得散度通式。"))
)}
]},
{"name":"4.2 柱坐标系","color":"#8b5cf6","desc":"(r,φ,z) 坐标下的梯度、散度、旋度",
"items":[
{"id":"v4s2-1","name":"柱坐标系中的矢量微分","tags":["def","thm","der"],"brief":"柱坐标拉梅系数与梯度、散度、旋度公式。",
"body":wrap(
 defn("柱坐标",p("柱坐标 $(r,\\varphi,z)$ 与直角坐标的关系：$x=r\\cos\\varphi,\\ y=r\\sin\\varphi,\\ z=z$。拉梅系数：")+
 fml("h_r=1,\\quad h_\\varphi=r,\\quad h_z=1"))+
 thm("柱坐标中的梯度",p("")+
 fml("\\nabla f = \\dfrac{\\partial f}{\\partial r}\\vec{e}_r+\\dfrac{1}{r}\\dfrac{\\partial f}{\\partial \\varphi}\\vec{e}_\\varphi+\\dfrac{\\partial f}{\\partial z}\\vec{e}_z"))+
 thm("柱坐标中的散度",p("")+
 fml("\\nabla\\cdot\\vec{F} = \\dfrac{1}{r}\\dfrac{\\partial(rF_r)}{\\partial r}+\\dfrac{1}{r}\\dfrac{\\partial F_\\varphi}{\\partial \\varphi}+\\dfrac{\\partial F_z}{\\partial z}"))+
 thm("柱坐标中的旋度",p("")+
 fml("\\nabla\\times\\vec{F} = \\dfrac{1}{r}\\begin{vmatrix}\\vec{e}_r&r\\vec{e}_\\varphi&\\vec{e}_z\\\\ \\partial_r&\\partial_\\varphi&\\partial_z\\\\ F_r&rF_\\varphi&F_z\\end{vmatrix}"))+
 der(p("<strong>拉梅系数推导：</strong>$x=r\\cos\\varphi$，$\\dfrac{\\partial x}{\\partial r}=\\cos\\varphi$，$\\dfrac{\\partial y}{\\partial r}=\\sin\\varphi$，$\\dfrac{\\partial z}{\\partial r}=0$，故 $h_r=\\sqrt{\\cos^2\\varphi+\\sin^2\\varphi}=1$。$\\dfrac{\\partial x}{\\partial \\varphi}=-r\\sin\\varphi$，$\\dfrac{\\partial y}{\\partial \\varphi}=r\\cos\\varphi$，故 $h_\\varphi=\\sqrt{r^2\\sin^2\\varphi+r^2\\cos^2\\varphi}=r$。$h_z=1$。"))+
 der(p("<strong>散度公式推导：</strong>代入通式 $h_1h_2h_3=1\\cdot r\\cdot 1=r$，$\\dfrac{\\partial(h_2h_3F_1)}{\\partial u_1}=\\dfrac{\\partial(r\\cdot 1\\cdot F_r)}{\\partial r}$，$\\dfrac{\\partial(h_1h_3F_2)}{\\partial u_2}=\\dfrac{\\partial(1\\cdot 1\\cdot F_\\varphi)}{\\partial \\varphi}$，$\\dfrac{\\partial(h_1h_2F_3)}{\\partial u_3}=\\dfrac{\\partial(1\\cdot r\\cdot F_z)}{\\partial z}$，除以 $r$ 即得柱坐标散度公式。"))
)},
{"id":"v4s2-2","name":"柱坐标中的拉普拉斯与应用","tags":["thm","der","app"],"brief":"柱坐标拉普拉斯公式及轴对称问题应用。",
"body":wrap(
 thm("柱坐标拉普拉斯",p("由 $\\nabla^2 f=\\nabla\\cdot(\\nabla f)$，代入柱坐标梯度与散度公式，得：")+
 fml("\\nabla^2 f = \\dfrac{1}{r}\\dfrac{\\partial}{\\partial r}\\left(r\\dfrac{\\partial f}{\\partial r}\\right)+\\dfrac{1}{r^2}\\dfrac{\\partial^2 f}{\\partial \\varphi^2}+\\dfrac{\\partial^2 f}{\\partial z^2}"))+
 app(p("<strong>应用：</strong>轴对称问题中 $f$ 与 $\\varphi$ 无关，拉普拉斯方程简化为 $\\dfrac{1}{r}\\dfrac{\\partial}{\\partial r}\\left(r\\dfrac{\\partial f}{\\partial r}\\right)+\\dfrac{\\partial^2 f}{\\partial z^2}=0$。无限长直导线电场、圆柱波导中场分布均用柱坐标求解。"))+
 der(p("<strong>拉普拉斯推导：</strong>梯度为 $\\left(\\dfrac{\\partial f}{\\partial r},\\dfrac{1}{r}\\dfrac{\\partial f}{\\partial\\varphi},\\dfrac{\\partial f}{\\partial z}\\right)$。代入柱坐标散度公式：第一项 $\\dfrac{1}{r}\\dfrac{\\partial}{\\partial r}\\left(r\\cdot\\dfrac{\\partial f}{\\partial r}\\right)$，第二项 $\\dfrac{1}{r}\\dfrac{\\partial}{\\partial\\varphi}\\left(\\dfrac{1}{r}\\dfrac{\\partial f}{\\partial\\varphi}\\right)=\\dfrac{1}{r^2}\\dfrac{\\partial^2 f}{\\partial\\varphi^2}$，第三项 $\\dfrac{\\partial}{\\partial z}\\left(\\dfrac{\\partial f}{\\partial z}\\right)=\\dfrac{\\partial^2 f}{\\partial z^2}$。合并得柱坐标拉普拉斯。"))
)}
]},
{"name":"4.3 球坐标系","color":"#a78bfa","desc":"(r,θ,φ) 坐标下的梯度、散度、旋度与拉普拉斯",
"items":[
{"id":"v4s3-1","name":"球坐标系中的矢量微分","tags":["def","thm","der"],"brief":"球坐标拉梅系数与梯度、散度、旋度、拉普拉斯公式。",
"body":wrap(
 defn("球坐标",p("球坐标 $(r,\\theta,\\varphi)$ 与直角坐标关系：$x=r\\sin\\theta\\cos\\varphi,\\ y=r\\sin\\theta\\sin\\varphi,\\ z=r\\cos\\theta$。拉梅系数：")+
 fml("h_r=1,\\quad h_\\theta=r,\\quad h_\\varphi=r\\sin\\theta"))+
 thm("球坐标中的梯度",p("")+
 fml("\\nabla f = \\dfrac{\\partial f}{\\partial r}\\vec{e}_r+\\dfrac{1}{r}\\dfrac{\\partial f}{\\partial\\theta}\\vec{e}_\\theta+\\dfrac{1}{r\\sin\\theta}\\dfrac{\\partial f}{\\partial\\varphi}\\vec{e}_\\varphi"))+
 thm("球坐标中的散度",p("")+
 fml("\\nabla\\cdot\\vec{F} = \\dfrac{1}{r^2}\\dfrac{\\partial(r^2F_r)}{\\partial r}+\\dfrac{1}{r\\sin\\theta}\\dfrac{\\partial(\\sin\\theta F_\\theta)}{\\partial\\theta}+\\dfrac{1}{r\\sin\\theta}\\dfrac{\\partial F_\\varphi}{\\partial\\varphi}"))+
 thm("球坐标中的拉普拉斯",p("")+
 fml("\\nabla^2 f = \\dfrac{1}{r^2}\\dfrac{\\partial}{\\partial r}\\left(r^2\\dfrac{\\partial f}{\\partial r}\\right)+\\dfrac{1}{r^2\\sin\\theta}\\dfrac{\\partial}{\\partial \\theta}\\left(\\sin\\theta\\dfrac{\\partial f}{\\partial \\theta}\\right)+\\dfrac{1}{r^2\\sin^2\\theta}\\dfrac{\\partial^2 f}{\\partial \\varphi^2}"))+
 der(p("<strong>拉梅系数推导：</strong>$\\dfrac{\\partial x}{\\partial r}=\\sin\\theta\\cos\\varphi$，$\\dfrac{\\partial y}{\\partial r}=\\sin\\theta\\sin\\varphi$，$\\dfrac{\\partial z}{\\partial r}=\\cos\\theta$，故 $h_r=\\sqrt{\\sin^2\\theta(\\cos^2\\varphi+\\sin^2\\varphi)+\\cos^2\\theta}=1$。$\\dfrac{\\partial x}{\\partial \\theta}=r\\cos\\theta\\cos\\varphi$，$\\dfrac{\\partial y}{\\partial \\theta}=r\\cos\\theta\\sin\\varphi$，$\\dfrac{\\partial z}{\\partial \\theta}=-r\\sin\\theta$，故 $h_\\theta=r$。$\\dfrac{\\partial x}{\\partial \\varphi}=-r\\sin\\theta\\sin\\varphi$，$\\dfrac{\\partial y}{\\partial \\varphi}=r\\sin\\theta\\cos\\varphi$，故 $h_\\varphi=r\\sin\\theta$。"))+
 der(p("<strong>拉普拉斯推导：</strong>$\\nabla^2f=\\nabla\\cdot(\\nabla f)$。梯度为 $\\left(\\dfrac{\\partial f}{\\partial r},\\dfrac{1}{r}\\dfrac{\\partial f}{\\partial\\theta},\\dfrac{1}{r\\sin\\theta}\\dfrac{\\partial f}{\\partial\\varphi}\\right)$。代入球坐标散度公式：$F_r=\\dfrac{\\partial f}{\\partial r}$，$F_\\theta=\\dfrac{1}{r}\\dfrac{\\partial f}{\\partial\\theta}$，$F_\\varphi=\\dfrac{1}{r\\sin\\theta}\\dfrac{\\partial f}{\\partial\\varphi}$。第一项 $\\dfrac{1}{r^2}\\dfrac{\\partial(r^2 f_r)}{\\partial r}$，第二项 $\\dfrac{1}{r\\sin\\theta}\\dfrac{\\partial(\\sin\\theta\\cdot\\frac{1}{r}f_\\theta)}{\\partial\\theta}$，第三项 $\\dfrac{1}{r\\sin\\theta}\\dfrac{\\partial(\\frac{1}{r\\sin\\theta}f_\\varphi)}{\\partial\\varphi}$，整理即得。"))
)},
{"id":"v4s3-2","name":"球坐标中的旋度与球对称应用","tags":["thm","der","app"],"brief":"球坐标旋度公式及球对称场的简化。",
"body":wrap(
 thm("球坐标旋度",p("代入旋度通式得球坐标旋度：")+
 fml("\\nabla\\times\\vec{F} = \\dfrac{1}{r^2\\sin\\theta}\\begin{vmatrix}\\vec{e}_r&r\\vec{e}_\\theta&r\\sin\\theta\\vec{e}_\\varphi\\\\ \\partial_r&\\partial_\\theta&\\partial_\\varphi\\\\ F_r&rF_\\theta&r\\sin\\theta F_\\varphi\\end{vmatrix}"))+
 thm("球对称场",p("若场具有球对称性，$F_r=F_r(r)$，$F_\\theta=F_\\varphi=0$，则：")+
 fml("\\nabla\\cdot\\vec{F}=\\dfrac{1}{r^2}\\dfrac{d(r^2 F_r)}{dr},\\quad \\nabla\\times\\vec{F}=0")+
 p("球对称矢量场必无旋，可表为标量势的梯度。"))+
 app(p("<strong>应用：</strong>点电荷电场 $\\vec{E}=\\dfrac{q}{4\\pi\\varepsilon_0 r^2}\\vec{e}_r$ 球对称，$\\nabla\\times\\vec{E}=0$（静电场无旋），$\\nabla\\cdot\\vec{E}=\\dfrac{q}{\\varepsilon_0}\\delta(\\vec{r})$（除原点外散度为零）。引力场、热流等球对称场均用此简化。"))+
 der(p("<strong>球对称场无旋推导：</strong>旋度 $r$ 分量为 $\\dfrac{1}{r\\sin\\theta}\\left(\\dfrac{\\partial(\\sin\\theta F_\\varphi)}{\\partial\\theta}-\\dfrac{\\partial F_\\theta}{\\partial\\varphi}\\right)$，因 $F_\\theta=F_\\varphi=0$ 而为零；$\\theta$ 分量为 $\\dfrac{1}{r}\\left(\\dfrac{1}{\\sin\\theta}\\dfrac{\\partial F_r}{\\partial\\varphi}-\\dfrac{\\partial(rF_\\varphi)}{\\partial r}\\right)=0$；$\\varphi$ 分量为 $\\dfrac{1}{r}\\left(\\dfrac{\\partial(rF_\\theta)}{\\partial r}-\\dfrac{\\partial F_r}{\\partial\\theta}\\right)=0$。故 $\\nabla\\times\\vec{F}=0$。"))
)}
]}
]

# ============ 第五章 并矢与张量运算 ============
ch5_sections = [
{"name":"5.1 并矢与二阶张量","color":"#be185d","desc":"并矢（张量积）的定义、分量与二阶张量概念",
"items":[
{"id":"v5s1-1","name":"并矢（张量积）","tags":["def","thm","der"],"brief":"并矢 ab 有 9 个分量 a_i b_j，是二阶张量的基础。",
"body":wrap(
 defn("并矢",p("两个矢量 $\\vec{a},\\vec{b}$ 的<strong>并矢</strong>（张量积、外积）记作 $\\vec{a}\\vec{b}$（或 $\\vec{a}\\otimes\\vec{b}$），定义为具有 9 个分量 $a_i b_j$ 的量：")+
 fml("\\vec{a}\\vec{b} = \\sum_{i,j=1}^3 a_i b_j \\vec{e}_i\\vec{e}_j = \\begin{pmatrix}a_1b_1&a_1b_2&a_1b_3\\\\a_2b_1&a_2b_2&a_2b_3\\\\a_3b_1&a_3b_2&a_3b_3\\end{pmatrix}"))+
 thm("并矢的运算",p("① 并矢与矢量点积：$(\\vec{a}\\vec{b})\\cdot\\vec{c}=\\vec{a}(\\vec{b}\\cdot\\vec{c})$；<br>② $\\vec{c}\\cdot(\\vec{a}\\vec{b})=(\\vec{c}\\cdot\\vec{a})\\vec{b}$；<br>③ 双点积：$(\\vec{a}\\vec{b}):(\\vec{c}\\vec{d})=(\\vec{a}\\cdot\\vec{c})(\\vec{b}\\cdot\\vec{d})$。"))+
 der(p("<strong>并矢分量推导：</strong>$\\vec{a}=\\sum_i a_i\\vec{e}_i$，$\\vec{b}=\\sum_j b_j\\vec{e}_j$，张量积 $\\vec{a}\\vec{b}=\\sum_{i,j}a_i b_j(\\vec{e}_i\\vec{e}_j)$。基并矢 $\\vec{e}_i\\vec{e}_j$ 共 9 个线性无关，构成二阶张量空间的基，故并矢由 9 个分量 $a_i b_j$ 完全确定。"))+
 der(p("<strong>并矢点积推导：</strong>$(\\vec{a}\\vec{b})\\cdot\\vec{c}=\\sum_{i,j}a_i b_j\\vec{e}_i(\\vec{e}_j\\cdot\\vec{c})=\\sum_{i,j}a_i b_j\\vec{e}_i c_j=\\vec{a}(\\sum_j b_j c_j)=\\vec{a}(\\vec{b}\\cdot\\vec{c})$。注意并矢点积不满足交换律：$(\\vec{a}\\vec{b})\\cdot\\vec{c}\\neq\\vec{c}\\cdot(\\vec{a}\\vec{b})$。"))
)},
{"id":"v5s1-2","name":"二阶张量的定义与矩阵表示","tags":["def","thm"],"brief":"二阶张量是具有 9 个分量并满足变换法则的量。",
"body":wrap(
 defn("二阶张量",p("二阶张量 $\\mathbf{T}$ 是这样的量：在坐标系中由 9 个分量 $T_{ij}$ 表示，且满足坐标变换法则。几何上，二阶张量可视为将矢量线性映射为矢量的算子。"))+
 defn("矩阵形式",p("二阶张量的分量可排成 3×3 矩阵：")+
 fml("\\mathbf{T} = \\begin{pmatrix}T_{11}&T_{12}&T_{13}\\\\T_{21}&T_{22}&T_{23}\\\\T_{31}&T_{32}&T_{33}\\end{pmatrix}")+
 p("张量作用于矢量：$(\\mathbf{T}\\cdot\\vec{a})_i=\\sum_j T_{ij}a_j$，即矩阵乘列向量。"))+
 thm("张量与矢量",p("矢量是一阶张量（3 个分量），标量是零阶张量（1 个分量）。并矢是特殊的二阶张量（但并非所有二阶张量都可表为单个并矢）。"))+
 der(p("<strong>从线性映射理解：</strong>设 $\\mathbf{T}$ 是矢量空间到自身的线性映射，$\\mathbf{T}(\\vec{a})$ 线性依赖于 $\\vec{a}$。取基底 $\\vec{e}_i$，$\\mathbf{T}(\\vec{e}_j)=\\sum_i T_{ij}\\vec{e}_i$，则 $\\mathbf{T}(\\vec{a})=\\sum_j a_j\\mathbf{T}(\\vec{e}_j)=\\sum_{i,j}T_{ij}a_j\\vec{e}_i$。系数 $T_{ij}$ 即为张量分量。"))
)}
]},
{"name":"5.2 张量的代数运算","color":"#db2777","desc":"加法、数乘、张量积、缩并、内积",
"items":[
{"id":"v5s2-1","name":"张量的加法、数乘与张量积","tags":["def","thm"],"brief":"张量的基本代数运算。",
"body":wrap(
 defn("加法",p("两个同阶张量 $\\mathbf{T},\\mathbf{S}$ 相加，分量对应相加：$(\\mathbf{T}+\\mathbf{S})_{ij}=T_{ij}+S_{ij}$。"))+
 defn("数乘",p("标量 $\\lambda$ 与张量 $\\mathbf{T}$ 的乘积：$(\\lambda\\mathbf{T})_{ij}=\\lambda T_{ij}$。"))+
 defn("张量积",p("$m$ 阶张量 $\\mathbf{T}$ 与 $n$ 阶张量 $\\mathbf{S}$ 的张量积为 $m+n$ 阶张量：$(\\mathbf{T}\\otimes\\mathbf{S})_{i_1\\cdots i_m j_1\\cdots j_n}=T_{i_1\\cdots i_m}S_{j_1\\cdots j_n}$。"))+
 thm("运算律",p("加法满足交换律、结合律；数乘满足结合律、分配律；张量积满足结合律、对加法的分配律，但不满足交换律。"))+
 der(p("<strong>张量积阶数推导：</strong>一阶张量（矢量）$\\vec{a}$ 有 3 个分量，$\\vec{b}$ 有 3 个分量，张量积 $\\vec{a}\\vec{b}$ 有 $3\\times 3=9$ 个分量 $a_i b_j$，是二阶张量。同理 $n$ 阶张量有 $3^n$ 个分量。张量积使阶数相加。"))
)},
{"id":"v5s2-2","name":"缩并与内积（点积）","tags":["def","thm","der"],"brief":"缩并降低张量阶数，内积是缩并的一种。",
"body":wrap(
 defn("缩并",p("对二阶张量 $T_{ij}$，令两指标相同并求和，称为<strong>缩并</strong>：")+
 fml("C = \\sum_{i=1}^3 T_{ii} = T_{11}+T_{22}+T_{33} = \\mathrm{tr}(\\mathbf{T})")+
 p("缩并将二阶张量变为标量（零阶张量），即张量的迹。"))+
 defn("内积（点积）",p("两个二阶张量 $\\mathbf{T},\\mathbf{S}$ 的双点积（内积）为标量：")+
 fml("\\mathbf{T}:\\mathbf{S} = \\sum_{i,j} T_{ij}S_{ij}")+
 p("张量与矢量的点积：$(\\mathbf{T}\\cdot\\vec{a})_i=\\sum_j T_{ij}a_j$，结果为矢量。"))+
 thm("缩并的阶数变化",p("$n$ 阶张量缩并一次（对两个指标求和）变为 $n-2$ 阶张量。如三阶张量 $T_{ijk}$ 缩并 $j,k$ 得一阶张量 $\\sum_j T_{ijj}$。"))+
 der(p("<strong>缩并降阶推导：</strong>二阶张量有 $3^2=9$ 个分量 $T_{ij}$。缩并后 $i=j$，求和 $\\sum_i T_{ii}$ 仅剩一个数，故从二阶（9 分量）降为零阶（1 分量）。一般地，缩并将两个自由指标化为哑指标求和，独立指标数减少 2，阶数降低 2。"))+
 der(p("<strong>内积与双点积关系：</strong>$\\mathbf{T}:\\mathbf{S}=\\sum_{ij}T_{ij}S_{ij}$ 可视为 $\\mathbf{T}$ 的转置与 $\\mathbf{S}$ 矩阵乘积的迹：$\\mathrm{tr}(\\mathbf{T}^T\\mathbf{S})=\\sum_i(\\mathbf{T}^T\\mathbf{S})_{ii}=\\sum_{i,j}T_{ji}S_{ij}$。当 $\\mathbf{T}$ 对称时与 $\\sum T_{ij}S_{ij}$ 一致。"))
)}
]},
{"name":"5.3 特殊张量与坐标变换","color":"#ec4899","desc":"单位张量、转置、对称反对称张量与变换法则",
"items":[
{"id":"v5s3-1","name":"单位张量、转置、对称与反对称张量","tags":["def","thm","der"],"brief":"单位张量、转置操作、对称性及其分解。",
"body":wrap(
 defn("单位张量",p("<strong>单位张量</strong> $\\mathbf{I}$ 的分量为克罗内克 delta：$I_{ij}=\\delta_{ij}$，矩阵形式为单位矩阵。对任意矢量 $\\vec{a}$，$\\mathbf{I}\\cdot\\vec{a}=\\vec{a}$。"))+
 defn("转置张量",p("二阶张量 $\\mathbf{T}$ 的<strong>转置</strong> $\\mathbf{T}^T$ 定义为 $(\\mathbf{T}^T)_{ij}=T_{ji}$。若 $\\mathbf{T}^T=\\mathbf{T}$，称<strong>对称张量</strong>；若 $\\mathbf{T}^T=-\\mathbf{T}$，称<strong>反对称张量</strong>。"))+
 thm("对称-反对称分解",p("任意二阶张量可唯一分解为对称部分与反对称部分之和：")+
 fml("\\mathbf{T} = \\dfrac{1}{2}(\\mathbf{T}+\\mathbf{T}^T)+\\dfrac{1}{2}(\\mathbf{T}-\\mathbf{T}^T) = \\mathbf{T}_S+\\mathbf{T}_A")+
 p("其中 $\\mathbf{T}_S$ 对称，$\\mathbf{T}_A$ 反对称。反对称张量只有 3 个独立分量，等价于一个轴矢量。"))+
 der(p("<strong>分解唯一性推导：</strong>设 $\\mathbf{T}=\\mathbf{S}+\\mathbf{A}$，$\\mathbf{S}$ 对称、$\\mathbf{A}$ 反对称。转置得 $\\mathbf{T}^T=\\mathbf{S}-\\mathbf{A}$。两式相加 $\\mathbf{T}+\\mathbf{T}^T=2\\mathbf{S}$，故 $\\mathbf{S}=\\frac{1}{2}(\\mathbf{T}+\\mathbf{T}^T)$；相减得 $\\mathbf{A}=\\frac{1}{2}(\\mathbf{T}-\\mathbf{T}^T)$。分解唯一。"))+
 der(p("<strong>反对称张量等价于轴矢量：</strong>反对称张量 $\\mathbf{A}$ 形如 $\\begin{pmatrix}0&-A_3&A_2\\\\A_3&0&-A_1\\\\-A_2&A_1&0\\end{pmatrix}$，对任意 $\\vec{a}$，$\\mathbf{A}\\cdot\\vec{a}=\\vec{\\omega}\\times\\vec{a}$，其中 $\\vec{\\omega}=(A_1,A_2,A_3)$。故反对称张量与轴矢量一一对应。"))
)},
{"id":"v5s3-2","name":"张量的坐标变换法则","tags":["def","thm","der"],"brief":"二阶张量在正交变换下的分量变换规律。",
"body":wrap(
 defn("正交变换",p("设新坐标系基矢 $\\vec{e}'_i=\\sum_j R_{ij}\\vec{e}_j$，其中 $\\mathbf{R}=(R_{ij})$ 为正交矩阵（$\\mathbf{R}^T\\mathbf{R}=\\mathbf{I}$）。矢量分量变换：$a'_i=\\sum_j R_{ij}a_j$。"))+
 defn("二阶张量变换法则",p("二阶张量分量在坐标变换下满足：")+
 fml("T'_{ij} = \\sum_{k,l} R_{ik}R_{jl}T_{kl}")+
 p("此为二阶张量的<strong>协变变换法则</strong>（笛卡尔张量）。"))+
 thm("标量不变性",p("标量（零阶张量）在坐标变换下数值不变：$u'=u$。矢量的模长 $|\\vec{a}|$ 是标量，故不变。"))+
 der(p("<strong>张量变换法则推导：</strong>张量 $\\mathbf{T}$ 将矢量 $\\vec{a}$ 映射为 $\\vec{b}=\\mathbf{T}\\cdot\\vec{a}$，即 $b_i=\\sum_j T_{ij}a_j$。在新坐标系中 $b'_i=\\sum_k R_{ik}b_k=\\sum_k R_{ik}\\sum_l T_{kl}a_l$。而 $a_l=\\sum_j R_{jl}a'_j$（逆变换 $\\mathbf{R}^{-1}=\\mathbf{R}^T$），代入得 $b'_i=\\sum_{k,l}R_{ik}T_{kl}\\sum_j R_{jl}a'_j=\\sum_j\\left(\\sum_{k,l}R_{ik}R_{jl}T_{kl}\\right)a'_j$。但 $b'_i=\\sum_j T'_{ij}a'_j$，比较系数得 $T'_{ij}=\\sum_{k,l}R_{ik}R_{jl}T_{kl}$。"))
)}
]}
]

# ============ 第六章 并矢与张量分析 ============
ch6_sections = [
{"name":"6.1 张量场与张量微分","color":"#8b5cf6","desc":"张量场的概念、张量的梯度与散度运算",
"items":[
{"id":"v6s1-1","name":"张量场的概念","tags":["def","exa"],"brief":"空间中每点对应一个张量的分布。",
"body":wrap(
 defn("张量场",p("若空间区域 $V$ 内每一点 $M$ 都对应一个张量 $\\mathbf{T}(M)$，则称在 $V$ 上定义了一个<strong>张量场</strong>。二阶张量场表示为 $T_{ij}=T_{ij}(x,y,z)$。"))+
 defn("张量场的连续性与可微性",p("若张量的每个分量 $T_{ij}(x,y,z)$ 都是连续（可微）函数，则称该张量场连续（可微）。张量场的微分运算归结为各分量的偏导数运算。"))+
 exa(p("<strong>例：</strong>连续介质中的应力张量场 $\\sigma_{ij}(x,y,z)$，每点的应力状态由一个二阶张量描述；电磁场中的麦克斯韦应力张量也是二阶张量场。"))+
 der(p("<strong>标量场→矢量场→张量场：</strong>标量场 $u$ 是零阶张量场；梯度 $\\nabla u$ 是一阶张量场（矢量场）；梯度的梯度 $\\nabla\\nabla u$ 是二阶张量场，分量为 $\\dfrac{\\partial^2 u}{\\partial x_i\\partial x_j}$，即二阶导数构成的 Hessian 矩阵。"))
)},
{"id":"v6s1-2","name":"张量的梯度与散度","tags":["def","thm","der"],"brief":"张量场的梯度升阶，散度降阶。",
"body":wrap(
 defn("张量的梯度",p("二阶张量场 $\\mathbf{T}$ 的梯度 $\\nabla\\mathbf{T}$ 是三阶张量，分量为：")+
 fml("(\\nabla\\mathbf{T})_{ijk} = \\dfrac{\\partial T_{jk}}{\\partial x_i}")+
 p("标量场的梯度是矢量（一阶升为一阶），矢量场的梯度是二阶张量，依此类推。"))+
 defn("张量的散度",p("二阶张量场 $\\mathbf{T}$ 的散度 $\\nabla\\cdot\\mathbf{T}$ 是矢量，分量为：")+
 fml("(\\nabla\\cdot\\mathbf{T})_i = \\sum_j \\dfrac{\\partial T_{ij}}{\\partial x_j}")+
 p("散度运算使张量阶数降低 1（对第一个指标求导并缩并）。"))+
 thm("散度定理的张量形式",p("对二阶张量场 $\\mathbf{T}$，有张量形式的高斯公式：")+
 fml("\\oiint_S \\mathbf{T}\\cdot d\\vec{S} = \\iiint_V (\\nabla\\cdot\\mathbf{T})\\,dV")+
 p("其中 $\\mathbf{T}\\cdot d\\vec{S}$ 的分量为 $\\sum_j T_{ij}dS_j$。"))+
 der(p("<strong>张量散度降阶推导：</strong>$\\nabla$ 是一阶矢量算子（分量 $\\partial_i$），与二阶张量 $T_{jk}$ 先做张量积得三阶 $\\partial_i T_{jk}$，再对 $i$ 与某一指标缩并。通常定义 $\\nabla\\cdot\\mathbf{T}$ 对第一个指标缩并：$\\sum_j\\partial_j T_{ij}$，结果自由指标只剩 $i$，故为一阶张量（矢量），阶数从 2 降为 1。"))+
 der(p("<strong>张量散度定理推导：</strong>对 $\\mathbf{T}$ 的每个列矢量 $\\vec{T}_j=(T_{1j},T_{2j},T_{3j})$ 应用矢量高斯公式：$\\oiint_S\\vec{T}_j\\cdot d\\vec{S}=\\iiint_V(\\nabla\\cdot\\vec{T}_j)dV$，即 $\\oiint_S\\sum_i T_{ij}dS_i=\\iiint_V\\sum_i\\dfrac{\\partial T_{ij}}{\\partial x_i}dV$。对每个 $j$ 成立，合并为张量形式。"))
)}
]},
{"name":"6.2 应力张量简介","color":"#a78bfa","desc":"连续介质力学中的应力张量及其平衡方程",
"items":[
{"id":"v6s2-1","name":"应力张量","tags":["def","thm","der"],"brief":"描述连续介质内力的二阶对称张量。",
"body":wrap(
 defn("应力矢量",p("在外法线为 $\\vec{n}$ 的面元上，单位面积所受的内力称为<strong>应力矢量</strong> $\\vec{t}_n$。它不仅与位置有关，还与面元方向 $\\vec{n}$ 有关。"))+
 defn("应力张量",p("存在二阶对称张量 $\\boldsymbol{\\sigma}$，使得任意法向 $\\vec{n}$ 的应力矢量满足：")+
 fml("\\vec{t}_n = \\boldsymbol{\\sigma}\\cdot\\vec{n},\\quad \\text{即}\\quad t_{n,i} = \\sum_j \\sigma_{ij}n_j")+
 p("$\\sigma_{ij}$ 表示作用在垂直于 $x_j$ 轴的面上、沿 $x_i$ 方向的应力分量。$\\sigma_{ii}$ 为正应力，$\\sigma_{ij}(i\\neq j)$ 为剪应力。"))+
 thm("应力张量对称性",p("由力矩平衡可证应力张量对称：$\\sigma_{ij}=\\sigma_{ji}$，故只有 6 个独立分量。"))+
 der(p("<strong>应力张量存在性推导（柯西公式）：</strong>取四面体微元，三个面垂直坐标轴（法向 $-\\vec{e}_j$），斜面法向 $\\vec{n}=(n_1,n_2,n_3)$。斜面面积 $dS$，三个坐标面面积 $dS_j=n_j dS$。力平衡 $\\vec{t}_n dS+\\sum_j \\vec{t}_{-e_j}n_j dS=0$（体力为高阶小量）。由牛顿第三定律 $\\vec{t}_{-e_j}=-\\vec{t}_{e_j}$，得 $\\vec{t}_n=\\sum_j\\vec{t}_{e_j}n_j$。定义 $\\sigma_{ij}=(\\vec{t}_{e_j})_i$，则 $t_{n,i}=\\sum_j\\sigma_{ij}n_j$。"))+
 der(p("<strong>对称性推导：</strong>取微小正六面体，考虑对中心轴的力矩平衡。剪应力 $\\sigma_{ij}$ 与 $\\sigma_{ji}$ 产生的力矩必须相等反向（无体力矩），故 $\\sigma_{ij}=\\sigma_{ji}$。"))
)},
{"id":"v6s2-2","name":"应变张量","tags":["def","thm","der"],"brief":"描述连续介质变形的二阶对称张量。",
"body":wrap(
 defn("位移场",p("设介质中质点的位移矢量为 $\\vec{u}=(u_1,u_2,u_3)$，依赖于位置坐标。变形由位移场的梯度描述。"))+
 defn("应变张量",p("<strong>无穷小应变张量</strong>定义为位移梯度的对称部分：")+
 fml("\\varepsilon_{ij} = \\dfrac{1}{2}\\left(\\dfrac{\\partial u_i}{\\partial x_j}+\\dfrac{\\partial u_j}{\\partial x_i}\\right)")+
 p("$\\varepsilon_{ii}$ 为正应变（沿 $x_i$ 方向的相对伸长），$\\varepsilon_{ij}(i\\neq j)$ 为剪应变（夹角变化的一半）。"))+
 thm("应变张量对称性",p("由定义显然 $\\varepsilon_{ij}=\\varepsilon_{ji}$，应变张量是对称二阶张量，有 6 个独立分量。体积应变（膨胀）为 $\\varepsilon_{kk}=\\nabla\\cdot\\vec{u}$。"))+
 der(p("<strong>正应变推导：</strong>沿 $x_1$ 方向取微元 $dx_1$，变形后两端点位移差为 $\\dfrac{\\partial u_1}{\\partial x_1}dx_1$，相对伸长为 $\\dfrac{\\partial u_1}{\\partial x_1}=\\varepsilon_{11}$。体积膨胀 $\\Delta V/V\\approx\\varepsilon_{11}+\\varepsilon_{22}+\\varepsilon_{33}=\\varepsilon_{kk}=\\nabla\\cdot\\vec{u}$（散度的几何意义）。"))+
 der(p("<strong>剪应变推导：</strong>沿 $x_1$ 方向的线段变形后偏转角度约为 $\\dfrac{\\partial u_2}{\\partial x_1}$，沿 $x_2$ 方向的线段偏转为 $\\dfrac{\\partial u_1}{\\partial x_2}$，两线段夹角变化为 $\\dfrac{\\partial u_2}{\\partial x_1}+\\dfrac{\\partial u_1}{\\partial x_2}=2\\varepsilon_{12}$，故剪应变 $\\varepsilon_{12}$ 为夹角变化的一半。"))
)}
]},
{"name":"6.3 各向同性张量与应用","color":"#c084fc","desc":"各向同性张量的概念及其在力学、电磁学中的应用",
"items":[
{"id":"v6s3-1","name":"各向同性张量","tags":["def","thm"],"brief":"在任意坐标变换下分量不变的张量。",
"body":wrap(
 defn("各向同性张量",p("若一个张量在任意正交坐标变换下其分量保持不变，则称为<strong>各向同性张量</strong>。物理上表示材料性质与方向无关。"))+
 thm("各向同性张量的形式",p("① 零阶：任意标量都是各向同性的；<br>② 一阶：只有零矢量是各向同性的；<br>③ 二阶：$\\mathbf{T}=\\lambda\\mathbf{I}$（只有单位张量的倍数）；<br>④ 四阶：$C_{ijkl}=\\lambda\\delta_{ij}\\delta_{kl}+\\mu(\\delta_{ik}\\delta_{jl}+\\delta_{il}\\delta_{jk})$。"))+
 app(p("<strong>力学应用：</strong>各向同性线弹性材料的本构关系（广义胡克定律）$\\sigma_{ij}=\\lambda\\varepsilon_{kk}\\delta_{ij}+2\\mu\\varepsilon_{ij}$，由四阶各向同性弹性张量 $C_{ijkl}$ 与应变张量 $\\varepsilon_{ij}$ 缩并得到，仅含两个独立常数 $\\lambda,\\mu$（拉梅常数）。"))+
 der(p("<strong>二阶各向同性张量推导：</strong>设 $\\mathbf{T}$ 各向同性，对绕 $x_3$ 轴转 $\\theta$ 的变换，$T'_{11}=T_{11}\\cos^2\\theta+2T_{12}\\sin\\theta\\cos\\theta+T_{22}\\sin^2\\theta=T_{11}$。对任意 $\\theta$ 成立要求 $T_{12}=0$ 且 $T_{11}=T_{22}$。同理所有对角元相等、非对角元为零，故 $\\mathbf{T}=\\lambda\\mathbf{I}$。"))
)},
{"id":"v6s3-2","name":"张量分析的应用","tags":["app","der"],"brief":"连续介质力学与电磁学中的张量应用。",
"body":wrap(
 app(p("<strong>连续介质力学：</strong>运动方程由应力张量散度给出：$\\rho\\dfrac{d\\vec{v}}{dt}=\\nabla\\cdot\\boldsymbol{\\sigma}+\\vec{f}$，其中 $\\rho$ 为密度，$\\vec{f}$ 为体力。分量形式：$\\rho\\dfrac{dv_i}{dt}=\\sum_j\\dfrac{\\partial\\sigma_{ij}}{\\partial x_j}+f_i$。"))+
 app(p("<strong>电磁学：</strong>电磁场的动量流由麦克斯韦应力张量描述：$\\sigma_{ij}=\\varepsilon_0 E_iE_j+\\dfrac{1}{\\mu_0}B_iB_j-\\dfrac{1}{2}(\\varepsilon_0 E^2+\\dfrac{1}{\\mu_0}B^2)\\delta_{ij}$。其散度给出电磁力密度。"))+
 app(p("<strong>流体力学：</strong>Navier-Stokes 方程中的粘性应力张量 $\\tau_{ij}=\\mu\\left(\\dfrac{\\partial v_i}{\\partial x_j}+\\dfrac{\\partial v_j}{\\partial x_i}\\right)+\\lambda(\\nabla\\cdot\\vec{v})\\delta_{ij}$，是对称二阶张量。"))+
 der(p("<strong>运动方程推导：</strong>对介质中任意体积 $V$，动量变化率等于面力与体力之和：$\\dfrac{d}{dt}\\iiint_V\\rho\\vec{v}\\,dV=\\oiint_S\\boldsymbol{\\sigma}\\cdot d\\vec{S}+\\iiint_V\\vec{f}\\,dV$。左端由雷诺输运定理化为 $\\iiint_V\\rho\\dfrac{d\\vec{v}}{dt}\\,dV$；右端面积分由张量散度定理化为 $\\iiint_V(\\nabla\\cdot\\boldsymbol{\\sigma})\\,dV$。因 $V$ 任意，被积函数相等，得运动方程。"))
)}
]}
]

# ============ 第七章 算符运算法则 ============
ch7_sections = [
{"name":"7.1 梯度算符的代数性质与乘积规则","color":"#0891b2","desc":"∇ 算符的微分性与矢量性，标量乘矢量的三个乘积规则",
"items":[
{"id":"v7s1-1","name":"梯度算符 ∇ 的代数性质","tags":["def","thm","der"],"brief":"∇ 既是微分算子又是矢量，具有双重性质。",
"body":wrap(
 defn("∇ 算符",p("哈密顿算子（nabla）定义为：")+
 fml("\\nabla = \\dfrac{\\partial}{\\partial x}\\vec{i}+\\dfrac{\\partial}{\\partial y}\\vec{j}+\\dfrac{\\partial}{\\partial z}\\vec{k}")+
 p("它具有<strong>双重性</strong>：既是微分算子（对后面的量求导），又是矢量（参与点积、叉积）。"))+
 thm("∇ 的三种作用",p("① 作用于标量 $u$：$\\nabla u$（梯度，矢量）；<br>② 点乘矢量 $\\vec{F}$：$\\nabla\\cdot\\vec{F}$（散度，标量）；<br>③ 叉乘矢量 $\\vec{F}$：$\\nabla\\times\\vec{F}$（旋度，矢量）。"))+
 der(p("<strong>双重性推导：</strong>将 $\\nabla$ 视为矢量 $\\vec{A}=(\\partial_x,\\partial_y,\\partial_z)$，则 $\\nabla u$ 是数乘（各分量乘 $u$），$\\nabla\\cdot\\vec{F}$ 是点积 $\\sum\\partial_i F_i$，$\\nabla\\times\\vec{F}$ 是叉积。但 $\\nabla$ 不是普通矢量，因为它作为微分算子时要作用于其后的函数，且不满足交换律（$\\nabla\\cdot\\vec{F}\\neq\\vec{F}\\cdot\\nabla$，后者是标量微分算子 $\\sum F_i\\partial_i$）。"))+
 der(p("<strong>$\\vec{F}\\cdot\\nabla$ 的意义：</strong>$\\vec{F}\\cdot\\nabla=\\sum_i F_i\\dfrac{\\partial}{\\partial x_i}$ 是一个标量微分算子，作用于标量得标量，作用于矢量得分量分别求导。例如 $(\vec{F}\\cdot\\nabla)\\vec{G}$ 表示沿 $\\vec{F}$ 方向的方向导数乘以 $|\\vec{F}|$。"))
)},
{"id":"v7s1-2","name":"乘积规则","tags":["thm","der"],"brief":"∇(uv)、∇·(uF)、∇×(uF) 三个乘积公式。",
"body":wrap(
 thm("标量乘积的梯度",p("")+
 fml("\\nabla(uv) = v\\nabla u + u\\nabla v"))+
 thm("标量乘矢量的散度",p("")+
 fml("\\nabla\\cdot(u\\vec{F}) = u(\\nabla\\cdot\\vec{F})+\\nabla u\\cdot\\vec{F}"))+
 thm("标量乘矢量的旋度",p("")+
 fml("\\nabla\\times(u\\vec{F}) = u(\\nabla\\times\\vec{F})+\\nabla u\\times\\vec{F}"))+
 der(p("<strong>梯度乘积推导：</strong>$\\nabla(uv)$ 的 $i$ 分量为 $\\dfrac{\\partial(uv)}{\\partial x_i}=v\\dfrac{\\partial u}{\\partial x_i}+u\\dfrac{\\partial v}{\\partial x_i}=v(\\nabla u)_i+u(\\nabla v)_i$，故 $\\nabla(uv)=v\\nabla u+u\\nabla v$。这是多元函数乘积求导法则的直接结果。"))+
 der(p("<strong>散度乘积推导：</strong>$\\nabla\\cdot(u\\vec{F})=\\sum_i\\dfrac{\\partial(uF_i)}{\\partial x_i}=\\sum_i\\left(F_i\\dfrac{\\partial u}{\\partial x_i}+u\\dfrac{\\partial F_i}{\\partial x_i}\\right)=\\sum_i F_i(\\nabla u)_i+u\\sum_i\\dfrac{\\partial F_i}{\\partial x_i}=\\nabla u\\cdot\\vec{F}+u(\\nabla\\cdot\\vec{F})$。"))+
 der(p("<strong>旋度乘积推导：</strong>$\\nabla\\times(u\\vec{F})$ 的 $i$ 分量为 $\\sum_{j,k}\\varepsilon_{ijk}\\partial_j(uF_k)=\\sum_{j,k}\\varepsilon_{ijk}(F_k\\partial_j u+u\\partial_j F_k)=\\sum_{j,k}\\varepsilon_{ijk}(\\partial_j u)F_k+u\\sum_{j,k}\\varepsilon_{ijk}\\partial_j F_k=(\\nabla u\\times\\vec{F})_i+u(\\nabla\\times\\vec{F})_i$，其中 $\\varepsilon_{ijk}$ 为 Levi-Civita 符号。"))
)}
]},
{"name":"7.2 矢量恒等式","color":"#06b6d4","desc":"叉积的散度、叉积的旋度、点积的梯度展开",
"items":[
{"id":"v7s2-1","name":"叉积的散度与旋度恒等式","tags":["thm","der"],"brief":"∇·(F×G) 与 ∇×(F×G) 的展开。",
"body":wrap(
 thm("叉积的散度",p("")+
 fml("\\nabla\\cdot(\\vec{F}\\times\\vec{G}) = \\vec{G}\\cdot(\\nabla\\times\\vec{F})-\\vec{F}\\cdot(\\nabla\\times\\vec{G})"))+
 thm("叉积的旋度",p("")+
 fml("\\nabla\\times(\\vec{F}\\times\\vec{G}) = \\vec{F}(\\nabla\\cdot\\vec{G})-\\vec{G}(\\nabla\\cdot\\vec{F})+(\\vec{G}\\cdot\\nabla)\\vec{F}-(\\vec{F}\\cdot\\nabla)\\vec{G}"))+
 der(p("<strong>叉积散度推导：</strong>利用 $\\nabla$ 的双重性，形式上 $\\nabla\\cdot(\\vec{F}\\times\\vec{G})$ 中 $\\nabla$ 分别作用于 $\\vec{F}$ 和 $\\vec{G}$。当 $\\nabla$ 作用于 $\\vec{F}$ 时（$\\vec{G}$ 视为常矢），由矢量恒等式 $\\vec{A}\\cdot(\\vec{B}\\times\\vec{C})=\\vec{B}\\cdot(\\vec{C}\\times\\vec{A})$，得 $(\\nabla\\times\\vec{F})\\cdot\\vec{G}$；当作用于 $\\vec{G}$ 时，得 $\\vec{F}\\cdot(\\vec{G}\\times\\nabla)$，轮换为 $-\\vec{F}\\cdot(\\nabla\\times\\vec{G})$。相加即得。"))+
 der(p("<strong>叉积旋度推导：</strong>用 BAC-CAB 公式 $\\vec{A}\\times(\\vec{B}\\times\\vec{C})=\\vec{B}(\\vec{A}\\cdot\\vec{C})-\\vec{C}(\\vec{A}\\cdot\\vec{B})$，将 $\\vec{A}$ 视为 $\\nabla$。$\\nabla\\times(\\vec{F}\\times\\vec{G})$ 中 $\\nabla$ 分别作用于 $\\vec{F}$ 和 $\\vec{G}$：<br>① $\\nabla$ 作用于 $\\vec{G}$：$\\vec{F}(\\nabla\\cdot\\vec{G})-(\\vec{F}\\cdot\\nabla)\\vec{G}$；<br>② $\\nabla$ 作用于 $\\vec{F}$：$(\\vec{G}\\cdot\\nabla)\\vec{F}-\\vec{G}(\\nabla\\cdot\\vec{F})$（注意符号因 $\\nabla$ 在 $\\vec{F}$ 前而调整）。<br>合并即得四元恒等式。"))
)},
{"id":"v7s2-2","name":"点积的梯度展开","tags":["thm","der"],"brief":"∇(F·G) 的四元展开式。",
"body":wrap(
 thm("点积的梯度",p("")+
 fml("\\nabla(\\vec{F}\\cdot\\vec{G}) = (\\vec{F}\\cdot\\nabla)\\vec{G}+(\\vec{G}\\cdot\\nabla)\\vec{F}+\\vec{F}\\times(\\nabla\\times\\vec{G})+\\vec{G}\\times(\\nabla\\times\\vec{F})"))+
 der(p("<strong>推导：</strong>利用恒等式 $\\vec{A}\\times(\\vec{B}\\times\\vec{C})=\\vec{B}(\\vec{A}\\cdot\\vec{C})-(\\vec{A}\\cdot\\vec{B})\\vec{C}$，解出 $\\vec{B}(\\vec{A}\\cdot\\vec{C})=\\vec{A}\\times(\\vec{B}\\times\\vec{C})+(\\vec{A}\\cdot\\vec{B})\\vec{C}$。<br>取 $\\vec{A}=\\nabla$，$\\vec{B}=\\vec{F}$，$\\vec{C}=\\vec{G}$，则 $\\nabla$ 作用于 $\\vec{G}$ 时：$\\vec{F}(\\nabla\\cdot\\vec{G})=\\nabla\\times(\\vec{F}\\times\\vec{G})+(\\vec{F}\\cdot\\nabla)\\vec{G}$，其中 $\\vec{F}$ 为常矢，$(\\nabla\\times(\\vec{F}\\times\\vec{G}))$ 项处理后得 $\\vec{F}\\times(\\nabla\\times\\vec{G})$ 的贡献。<br>同理 $\\nabla$ 作用于 $\\vec{F}$ 得 $\\vec{G}\\times(\\nabla\\times\\vec{F})+(\\vec{G}\\cdot\\nabla)\\vec{F}$。<br>两部分相加即得完整展开。"))+
 note(p("此式可记忆为：梯度点积 = 方向导数项 + 旋度耦合项。当 $\\vec{F}=\\vec{G}$ 时，$\\nabla(F^2)=2(\\vec{F}\\cdot\\nabla)\\vec{F}+2\\vec{F}\\times(\\nabla\\times\\vec{F})$，常用于流体力学。"))
)}
]},
{"name":"7.3 拉普拉斯算子与亥姆霍兹分解","color":"#22d3ee","desc":"拉普拉斯作用于矢量、矢量拉普拉斯恒等式与场的分解定理",
"items":[
{"id":"v7s3-1","name":"拉普拉斯算子","tags":["def","thm","der"],"brief":"标量与矢量的拉普拉斯，矢量拉普拉斯恒等式。",
"body":wrap(
 defn("标量拉普拉斯",p("标量场 $u$ 的拉普拉斯为梯度的散度：")+
 fml("\\nabla^2 u = \\nabla\\cdot(\\nabla u) = \\dfrac{\\partial^2 u}{\\partial x^2}+\\dfrac{\\partial^2 u}{\\partial y^2}+\\dfrac{\\partial^2 u}{\\partial z^2}"))+
 defn("矢量拉普拉斯",p("矢量场 $\\vec{F}$ 的拉普拉斯定义为各分量分别求标量拉普拉斯：")+
 fml("\\nabla^2\\vec{F} = (\\nabla^2 F_x,\\ \\nabla^2 F_y,\\ \\nabla^2 F_z)"))+
 thm("矢量拉普拉斯恒等式",p("")+
 fml("\\nabla^2\\vec{F} = \\nabla(\\nabla\\cdot\\vec{F})-\\nabla\\times(\\nabla\\times\\vec{F})"))+
 der(p("<strong>矢量拉普拉斯恒等式推导：</strong>计算右端 $x$ 分量。$\\nabla(\\nabla\\cdot\\vec{F})$ 的 $x$ 分量为 $\\partial_x(\\partial_x F_x+\\partial_y F_y+\\partial_z F_z)=\\partial_x^2 F_x+\\partial_x\\partial_y F_y+\\partial_x\\partial_z F_z$。<br>$\\nabla\\times\\vec{F}$ 的分量为 $(\\partial_y F_z-\\partial_z F_y,\\ \\partial_z F_x-\\partial_x F_z,\\ \\partial_x F_y-\\partial_y F_x)$。<br>$\\nabla\\times(\\nabla\\times\\vec{F})$ 的 $x$ 分量为 $\\partial_y(\\nabla\\times\\vec{F})_z-\\partial_z(\\nabla\\times\\vec{F})_y=\\partial_y(\\partial_x F_y-\\partial_y F_x)-\\partial_z(\\partial_z F_x-\\partial_x F_z)=\\partial_x\\partial_y F_y-\\partial_y^2 F_x-\\partial_z^2 F_x+\\partial_x\\partial_z F_z$。<br>相减得 $\\partial_x^2 F_x+\\partial_y^2 F_x+\\partial_z^2 F_x=\\nabla^2 F_x$。同理 $y,z$ 分量，恒等式成立。"))
)},
{"id":"v7s3-2","name":"亥姆霍兹分解","tags":["thm","der"],"brief":"任意矢量场可分解为无旋部分与无源部分之和。",
"body":wrap(
 thm("亥姆霍兹分解定理",p("在有限区域内，任意足够光滑的矢量场 $\\vec{F}$ 可唯一分解为<strong>无旋场</strong>与<strong>无源场</strong>之和：")+
 fml("\\vec{F} = -\\nabla\\phi + \\nabla\\times\\vec{A}")+
 p("其中 $\\phi$ 为标量势（使 $-\\nabla\\phi$ 无旋），$\\vec{A}$ 为矢量势（使 $\\nabla\\times\\vec{A}$ 无源）。"))+
 thm("势的方程",p("对分解式取散度：$\\nabla\\cdot\\vec{F}=-\\nabla^2\\phi$（因 $\\nabla\\cdot(\\nabla\\times\\vec{A})=0$），故 $\\phi$ 满足泊松方程 $\\nabla^2\\phi=-\\nabla\\cdot\\vec{F}$。<br>取旋度：$\\nabla\\times\\vec{F}=\\nabla\\times(\\nabla\\times\\vec{A})=\\nabla(\\nabla\\cdot\\vec{A})-\\nabla^2\\vec{A}$。取库仑规范 $\\nabla\\cdot\\vec{A}=0$，则 $\\nabla^2\\vec{A}=-\\nabla\\times\\vec{F}$。"))+
 der(p("<strong>分解推导：</strong>① 无旋部分：若 $\\vec{F}$ 的无旋部分为 $-\\nabla\\phi$，则由 $\\nabla\\times(-\\nabla\\phi)=0$ 自然满足无旋。取散度得 $\\nabla\\cdot\\vec{F}=-\\nabla^2\\phi$，解此泊松方程得 $\\phi$。<br>② 无源部分：令 $\\vec{F}+\\nabla\\phi=\\nabla\\times\\vec{A}$，需验证 $\\nabla\\cdot(\\vec{F}+\\nabla\\phi)=\\nabla\\cdot\\vec{F}+\\nabla^2\\phi=0$（由 $\\phi$ 的方程），故 $\\vec{F}+\\nabla\\phi$ 无源，可表为某矢量场的旋度（庞加莱引理）。<br>③ 取规范 $\\nabla\\cdot\\vec{A}=0$，解 $\\nabla^2\\vec{A}=-\\nabla\\times\\vec{F}$ 得 $\\vec{A}$。分解成立。"))+
 app(p("<strong>电磁学应用：</strong>电场 $\\vec{E}$ 可分解为库仑场（无旋，$-\\nabla\\phi$）和感生电场（无源，$-\\partial\\vec{A}/\\partial t$）。磁场 $\\vec{B}=\\nabla\\times\\vec{A}$ 天然无源。亥姆霍兹分解是电磁势方法的数学基础。"))
)}
]}
]

CHAPTERS = [
{"id":"ch1","num":"第一章","title":"矢量运算","en":"VECTOR ALGEBRA","desc":"向量的加减、数乘、点积、叉积、混合积与多重积，是矢量分析的代数基础。","sections":ch1_sections},
{"id":"ch2","num":"第二章","title":"矢量微积分","en":"VECTOR CALCULUS","desc":"矢量函数的导数与积分、线积分、标量场与矢量场、方向导数与链式法则。","sections":ch2_sections},
{"id":"ch3","num":"第三章","title":"梯度 散度 旋度","en":"GRADIENT · DIVERGENCE · CURL","desc":"梯度、散度、旋度的定义与推导，高斯公式、斯托克斯公式，零恒等式与拉普拉斯算子。","sections":ch3_sections},
{"id":"ch4","num":"第四章","title":"曲线坐标系","en":"CURVILINEAR COORDINATES","desc":"正交曲线坐标、拉梅系数、柱坐标与球坐标系中的梯度、散度、旋度与拉普拉斯算子。","sections":ch4_sections},
{"id":"ch5","num":"第五章","title":"并矢与张量运算","en":"DYADICS & TENSOR ALGEBRA","desc":"并矢（张量积）、二阶张量、张量代数运算、特殊张量与坐标变换法则。","sections":ch5_sections},
{"id":"ch6","num":"第六章","title":"并矢与张量分析","en":"TENSOR ANALYSIS","desc":"张量场、张量的梯度与散度、应力张量、各向同性张量及其在力学与电磁学中的应用。","sections":ch6_sections},
{"id":"ch7","num":"第七章","title":"算符运算法则","en":"OPERATOR IDENTITIES","desc":"∇ 算符的代数性质、乘积规则、矢量恒等式、拉普拉斯算子与亥姆霍兹分解。","sections":ch7_sections},
]


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
  .la-nav-tab.c2{color:#0d9488;border-color:#99f6e4}
  .la-nav-tab.c3{color:#c2410c;border-color:#fed7aa}
  .la-nav-tab.c4{color:#7c3aed;border-color:#ddd6fe}
  .la-nav-tab.c5{color:#be185d;border-color:#fbcfe8}
  .la-nav-tab.c6{color:#8b5cf6;border-color:#ddd6fe}
  .la-nav-tab.c7{color:#0891b2;border-color:#a5f3fc}
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
  .la-phase-title.ch1::before{background:#2563eb}
  .la-phase-title.ch2::before{background:#0d9488}
  .la-phase-title.ch3::before{background:#c2410c}
  .la-phase-title.ch4::before{background:#7c3aed}
  .la-phase-title.ch5::before{background:#be185d}
  .la-phase-title.ch6::before{background:#8b5cf6}
  .la-phase-title.ch7::before{background:#0891b2}
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
<meta name="description" content="矢量与张量分析知识体系：矢量运算、矢量微积分、梯度散度旋度、曲线坐标系、并矢与张量、算符运算法则">
<title>矢量与张量分析 · 知识体系</title>
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
    <div class="la-eyebrow">VECTOR & TENSOR ANALYSIS · KNOWLEDGE MAP</div>
    <h1>矢量与张量分析 · 知识体系</h1>
    <p class="la-subtitle">矢量运算 · 矢量微积分 · 梯度散度旋度 · 曲线坐标系 · 并矢与张量 · 算符运算法则</p>
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
    <div>矢量与张量分析 · 知识体系可视化 · MathJax + SVG</div>
    <div style="margin-top:8px">基于矢量分析与张量分析核心知识体系整理</div>
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
    with open("/workspace/vector-analysis.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated vector-analysis.html ({len(html)} chars)")