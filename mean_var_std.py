import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
        
    npList = np.array(list).reshape(3,3) 
    
    mean_row = np.mean(npList, axis=0).tolist() 
    mean_col = np.mean(npList, axis=1).tolist()
    mean_flat = np.mean(npList).tolist()

    var_row = np.var(npList, axis=0).tolist()
    var_col = np.var(npList, axis=1).tolist()
    var_flat = np.var(npList).tolist()

    std_row = np.std(npList, axis=0).tolist()
    std_col = np.std(npList, axis=1).tolist()
    std_flat = np.std(npList).tolist()

    max_row = np.max(npList, axis=0).tolist()
    max_col = np.max(npList, axis=1).tolist()
    max_flat = np.max(npList).tolist()
    
    min_row = np.min(npList, axis=0).tolist()
    min_col = np.min(npList, axis=1).tolist()
    min_flat = np.min(npList).tolist()
    
    sum_row = np.sum(npList, axis=0).tolist()
    sum_col = np.sum(npList, axis=1).tolist()
    sum_flat = np.sum(npList).tolist()
    
    result_dict = {
        'mean': [mean_row, mean_col, mean_flat],
        'variance': [var_row, var_col, var_flat],
        'standard deviation': [std_row, std_col, std_flat],
        'max': [max_row, max_col, max_flat],
        'min': [min_row, min_col, min_flat],
        'sum': [sum_row, sum_col, sum_flat],
        }
    return result_dict





    return calculations