import pandas as pd
import numpy as np
import scipy.stats as stats
from math import sqrt

chat_id = 440047378

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.05
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    err1 = p1*(1-p1)/x_cnt
    err2 = p2*(1-p2)/y_cnt
    z_score = (p2 - p1) / sqrt(err1+err2)
    p_value = stats.norm.sf(z_score)
    return p_value < alpha
