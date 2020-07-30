import numpy as np
from sys import exit
import os

"""
1. average number of non-zero pixels
2. average number of zero pixels
3. ratio of non-zero to zero
4. max/min non-zero
5. max/min zero
"""

"""
The geometrical featues:

Number of black pixels in the window.
Position of the uppermost black pixel.
Position of the lowermost black pixel.
Deviation of the uppermost pixel.
Deviation of the lowermost pixel.
Pixel density between upper and lower contour.
Number of black-to-white transitions in vertical direction.
Center of gravity.
The second derivative of the moment in vertical direction.
"""
class feature_finder:


    def __init__(self):
