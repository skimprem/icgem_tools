"""
ICGEM Tools - Python library for working with ICGEM format files.

This library provides tools for reading, writing, and processing ICGEM format files,
which are used in geodesy for representing gravitational models and spherical harmonic
coefficients.
"""

__version__ = "0.1.0"
__author__ = "Roman Sermiagin"
__email__ = "roman.sermiagin@gmail.com"

from .points import ICGEMTable
from .grids import ICGEMGrid
# from .coeffs import ICGEMCoeff

__all__ = [
    "ICGEMTable",
    "ICGEMGrid",
    # "ICGEMCoeff",
]