# -*- coding: utf-8 -*-
"""原子物理章节（依据手写讲义六章）。"""
from qcii_common import C, S, q  # noqa: F401
import qap_1, qap_2, qap_3


def chapters():
    return qap_1.chapters() + qap_2.chapters() + qap_3.chapters()
