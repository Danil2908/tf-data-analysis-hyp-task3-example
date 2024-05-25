import pandas as pd
import numpy as np


chat_id = 1527061415 # Ваш chat ID, не меняйте название переменной

def solution(control_npv: np.array, test_npv: np.array) -> bool: 
    mean_control = sum(control_npv) / len(control_npv)
    mean_test = sum(test_npv) / len(test_npv)
    
    # t тестт для сравнения средних двух выборок 
    z_score, p_value = stats.ttest_ind(control_npv, test_npv)
    
    alpha = 0.03
    
    return p_value < alpha
