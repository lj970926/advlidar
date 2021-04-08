import torch

def get_intersection(orig: torch.Tensor, d: torch.Tensor, v1: torch.Tensor, v2: torch.Tensor, v3: torch.Tensor):
    r'''
    args:
        orig: coordination of the origin of the ray
        d: directional vector
        v1, v2, v3: three vertices of the triangle
    return value

    '''
    edge1 = v2 - v1
    edge2 = v3 - v1
    
    
