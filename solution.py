import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 424771681 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
     alpha = 0.02
    
    stat, p_value = ks_2samp(x, y)
    return p_value < alpha
