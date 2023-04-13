import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 626925789 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.09
    t, p = ttest_ind(x, y)
    return bool(p.mean() < alpha)
