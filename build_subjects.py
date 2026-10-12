# -*- coding: utf-8 -*-
"""构建脚本：将 content_topics.py 中的主题展开为完整学科数据。
每个主题生成一个知识点（分组集中展示），不做数量膨胀。"""
from content_bank import build_section, T
from content_topics import *

# 文件名到主题变量的映射
SUBJECT_MAP = {
    # 数学类 7
    "elementary-math.html": ELEMENTARY_MATH,
    "advanced-math.html": ADVANCED_MATH,
    "probability-statistics.html": PROBABILITY_STATISTICS,
    "group-theory.html": GROUP_THEORY,
    "mathematical-methods.html": MATHEMATICAL_METHODS,
    "special-functions.html": SPECIAL_FUNCTIONS,
    "vector-analysis.html": VECTOR_ANALYSIS,
    # 计算
    "computational-physics.html": COMPUTATIONAL_PHYSICS,
    # 力学 4
    "theoretical-mechanics.html": THEORETICAL_MECHANICS,
    "fluid-mechanics.html": FLUID_MECHANICS,
    "solid-mechanics.html": SOLID_MECHANICS,
    "cfd.html": CFD,
    # 电磁电子 6
    "electromagnetism.html": ELECTROMAGNETISM,
    "electrodynamics.html": ELECTRODYNAMICS,
    "circuits.html": CIRCUITS,
    "analog-electronics.html": ANALOG_ELECTRONICS,
    "digital-electronics.html": DIGITAL_ELECTRONICS,
    "integrated-circuits.html": INTEGRATED_CIRCUITS,
    # 热学统计 2
    "thermal-physics.html": THERMODYNAMICS,
    "statistical-mechanics.html": STATISTICAL_PHYSICS,
    # 光学 5
    "optics.html": OPTICS,
    "optical-design.html": OPTICAL_DESIGN,
    "laser-principles.html": LASER_PHYSICS,
    "nonlinear-optics.html": NONLINEAR_OPTICS,
    "luminescence.html": LUMINESCENCE,
    # 声学 1
    "acoustics.html": ACOUSTICS,
    # 量子原子核 4
    "atomic-physics.html": ATOMIC_PHYSICS,
    "quantum-mechanics.html": QUANTUM_MECHANICS,
    "quantum-computing.html": QUANTUM_COMPUTING,
    "nuclear-physics.html": NUCLEAR_PHYSICS,
    # 实验 2
    "basic-physics-lab.html": EXPERIMENTAL_PHYSICS,
    "modern-physics-lab.html": MODERN_PHYSICS_EXPERIMENTS,
    # 凝聚态材料 9
    "solid-state-physics.html": SOLID_STATE_PHYSICS,
    "materials-physics.html": MATERIALS_SCIENCE,
    "superconductivity.html": SUPERCONDUCTIVITY,
    "nanophysics.html": NANOPHYSICS,
    "topological-matter.html": TOPOLOGICAL_MATTER,
    "2d-materials.html": TWO_D_MATERIALS,
    "low-temperature-physics.html": LOW_TEMPERATURE_PHYSICS,
    "materials-preparation.html": MATERIALS_PREPARATION,
    "materials-characterization.html": MATERIALS_CHARACTERIZATION,
    # 半导体 4
    "semiconductor-physics.html": SEMICONDUCTOR_PHYSICS,
    "semiconductor-materials.html": SEMICONDUCTOR_MATERIALS,
    "semiconductor-devices.html": SEMICONDUCTOR_DEVICES,
    "semiconductor-process.html": MICROELECTRONICS,
    # 相对论宇宙 4
    "relativity.html": RELATIVITY,
    "cosmology.html": COSMOLOGY,
    "black-hole-physics.html": BLACK_HOLE_PHYSICS,
    "astrophysics.html": ASTROPHYSICS,
    # 粒子场论 7
    "particle-physics.html": PARTICLE_PHYSICS,
    "gauge-theory.html": GAUGE_THEORY,
    "quantum-field-theory.html": QUANTUM_FIELD_THEORY,
    "string-theory.html": STRING_THEORY,
    "quantum-gravity.html": QUANTUM_GRAVITY,
    "conformal-field-theory.html": CONFORMAL_FIELD_THEORY,
    "tqft.html": TQFT,
    # 交叉 4
    "plasma-physics.html": PLASMA_PHYSICS,
    "biophysics.html": BIOPHYSICS,
    "radiation-processes.html": RADIATION_PROCESSES,
    "fusion-physics.html": FUSION_PHYSICS,
    # 其他
    "electroweak-theory.html": ELECTROWEAK,
    "quantum-electrodynamics.html": QUANTUM_ELECTRODYNAMICS,
    "quantum-chromodynamics.html": QUANTUM_CHROMODYNAMICS,
    "medical-physics.html": MEDICAL_PHYSICS,
    "econophysics.html": ECONOPHYSICS,
    "geophysics.html": GEOPHYSICS,
    "crystallography.html": CRYSTALLOGRAPHY,
    "microelectronics.html": MICROELECTRONICS,
    "optoelectronics.html": OPTOELECTRONICS,
    "magnetism.html": MAGNETISM,
    "dielectrics.html": DIELECTRICS,
    "fiber-optics.html": FIBER_OPTICS,
    "photonics.html": PHOTONICS,
    "linear-algebra.html": LINEAR_ALGEBRA,
    "newtonian-mechanics.html": NEWTONIAN_MECHANICS,
    "engineering-optics.html": ENGINEERING_OPTICS,
    "quantum-information.html": QUANTUM_INFORMATION,
}

def expand_subject(filename, topic_data, prefix):
    """将主题数据展开为章节结构。每个主题 = 一个知识点（分组展示）。"""
    chapters = []
    for ci, ch in enumerate(topic_data, 1):
        sections = []
        for si, sec in enumerate(ch["sections"], 1):
            sec_prefix = f"{prefix}-c{ci}s{si}"
            sections.append(build_section(sec_prefix, sec["name"], sec["color"],
                             sec.get("desc",""), sec["topics"]))
        chapters.append({"id": f"{prefix}-ch{ci}", "num": ch["ch"], "title": ch["title"],
                         "en": ch["en"], "sub": ch["sub"], "desc": ch.get("desc",""),
                         "sections": sections})
    return chapters

def count_items(chapters):
    return sum(len(s["items"]) for c in chapters for s in c["sections"])

if __name__ == "__main__":
    for fn, data in SUBJECT_MAP.items():
        prefix = fn.replace("-","_").replace(".html","")
        chs = expand_subject(fn, data, prefix)
        n = count_items(chs)
        print(f"{fn}: {n} items")
