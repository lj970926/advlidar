import torch


def check_intersection(u, v, w):
    return u >= 0 and u <= 1 and v >= 0 and v <= 1 and w >= 0 and w <= 1

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

    pvec = v1 - orig
    intersec = torch.empty(size=(3,))
    intersec[0] = torch.dot(pvec, torch.cross(edge1, edge2))
    intersec[1] = torch.dot(pvec, torch.cross(d, edge2))
    intersec[2] = torch.dot(pvec, torch.cross(edge1, d))
    intersec /= torch.dot(d, torch.cross(edge1, edge2))
    is_intersec = check_intersection(intersec[1], intersec[2], 1 - intersec[1] - intersec[2])
    return is_intersec, intersec
    
    
