#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 16:06:43 2023

@author: jordanconey
"""

# example/refraction.py

import numpy as np


def snell(theta_inc, n1, n2):
    """
    Compute the refraction angle using Snell's Law.

    See https://en.wikipedia.org/wiki/Snell%27s_law

    Parameters
    ----------
    theta_inc : float
        Incident angle in radians.
    n1, n2 : float
        The refractive index of medium of origin and destination medium.

    Returns
    -------
    theta : float
        refraction angle

    Examples
    --------
    A ray enters an air--water boundary at pi/4 radians (45 degrees).
    Compute exit angle.

    >>> snell(np.pi/4, 1.00, 1.33)
    0.5605584137424605
    """
    breakpoint()
    
    return np.arcsin(n1 / n2 * np.sin(theta_inc)) # comment

