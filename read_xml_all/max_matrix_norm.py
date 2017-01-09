# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:55:45 2016

@author: wang
"""

import numpy as np

def max_matrix_norm(y):
    max_matrix_value=np.amax(y)
    percentage = 100.0/max_matrix_value
    matrix_nom = y*percentage
    return matrix_nom
    