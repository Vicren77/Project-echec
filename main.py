# -*- coding: utf-8 -*-

import piece as pc
import plateau as pt
import jeu
import copy

a = jeu.Jeu()
print(u"a ..... :")
print(a.__str__())

B = a.actionsDisponibles(pc.blanc)
N = a.actionsDisponibles(pc.noir)
M = a.move 
"""
L = a.actionsDisponibles(pc.blanc)
for action in L:
    b = copy.deepcopy(a)
    b.move(action)
    M = b.actionsDisponibles(pc.noir)
    for action2 in M:
        c = copy.deepcopy(b)
        c.move(action2)
        (score_blanc, score_noir) = jeu.score1(c)
        print(score_blanc, score_noir)
"""