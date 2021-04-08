import torch
from render.utils.intersection import get_intersection

def test_intersection_1():
    orig = torch.tensor([0, 0, 0])
    d = torch.tensor()