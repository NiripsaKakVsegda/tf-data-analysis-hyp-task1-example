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
    err1 = sqrt(p1*(1-p1)/x_cnt)
    err2 = sqrt(p2*(1-p2)/y_cnt)
    z_score = (p2 - p1) / sqrt(err1**2+err2**2)
    t_critical = stats.t.ppf(1-alpha/2, x_cnt+y_cnt-2)
    return z_score > t_critical
