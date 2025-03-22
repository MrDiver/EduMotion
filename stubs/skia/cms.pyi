from __future__ import annotations
__all__ = ['ICCProfile', 'Matrix3x3', 'TransferFunction']
class ICCProfile:
    buffer: int
    data_color_space: int
    has_A2B: bool
    has_toXYZD50: bool
    has_trc: bool
    pcs: int
    size: int
    tag_count: int
    def __init__(self) -> None:
        ...
class Matrix3x3:
    """
    
        A row-major 3x3 matrix (ie vals[row][col])
        
    """
    def __init__(self, v: list[float]) -> None:
        ...
class TransferFunction:
    """
    
        A transfer function mapping encoded values to linear values,
        represented by this 7-parameter piecewise function:
    
          linear = sign(encoded) *  (c*|encoded| + f)       , 0 <= |encoded| < d
                 = sign(encoded) * ((a*|encoded| + b)^g + e), d <= |encoded|
    
        (A simple gamma transfer function sets g to gamma and a to 1.)
        
    """
    def __init__(self, v: list[float]) -> None:
        ...
