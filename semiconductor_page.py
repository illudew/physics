"""复用微积分的章节、卡片、弹窗和公式速查版式。"""
import re
from gen_calc import gen_html
from semiconductor_textbook import CHAPTERS

def render():
    formulas = []
    # 每小节选一条核心公式；在速查项注明适用前提见对应知识卡。
    for ch in CHAPTERS:
        for sec in ch['sections']:
            for item in sec['items']:
                match = re.search(r'\$\$(.*?)\$\$', item['body'], re.S)
                if match:
                    formulas.append((item['name'],match[1],sec['name']+'；符号和适用条件见该节知识卡。'))
                    break
    page = gen_html(CHAPTERS, formulas)
    page = page.replace('微积分 · 知识体系','半导体物理 · 知识体系')
    page = page.replace('CALCULUS · KNOWLEDGE MAP','SEMICONDUCTOR PHYSICS · KNOWLEDGE MAP')
    page = page.replace('微积分知识体系：一元微分、微分定理、一元积分、微分方程、多元微分、重积分、积分定理、无穷级数','半导体物理知识体系：能带、统计、输运、结与界面、光电、热电、磁效应与非晶态')
    page = page.replace('一元微分 · 微分定理 · 一元积分 · 微分方程 · 多元微分 · 重积分 · 积分定理 · 无穷级数','能带 · 统计 · 输运 · 结与界面 · 光电与热电 · 非晶态')
    page = page.replace('基于同济大学《高等数学》知识体系整理','依据刘恩科等《半导体物理学》第8版（电子工业出版社，2023）整理 · 记号统一，按主题重组')
    page = page.replace('>定 理</span>','>规 律</span>')
    # 数学表达较长时只在公式区域滚动，保持移动端弹窗宽度。
    page = page.replace('</style>', '.la-fml{overflow-x:auto;max-width:100%}.la-modal-body svg{max-width:100%;height:auto}\n</style>')
    return page
