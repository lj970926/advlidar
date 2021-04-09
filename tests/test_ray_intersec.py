import sys
sys.path.append("..")

import torch

from render.utils.intersection import get_intersection

def test_intersection_1():
    orig = torch.tensor([0., 0., 1.])
    d = torch.tensor([0., 0., 2.])
    v1 = torch.tensor([0., 0., 0.])
    v2 = torch.tensor([1., 0., 0.])
    v3 = torch.tensor([0., 1., 0.])
    is_intersec, (t, u ,v) = get_intersection(orig, d, v1, v2, v3)
    print(is_intersec, t, u, v)
    assert(is_intersec == False)

test_intersection_1()