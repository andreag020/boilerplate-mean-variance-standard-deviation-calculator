import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert list to array
    a = np.array(list).reshape(3,3)
    
    # Get mean in both axis
    mean1 = a.mean(axis=0)
    mean2 = a.mean(axis=1)

    # Get variance in both axis
    var1 = a.var(axis=0)
    var2 = a.var(axis=1)

    # Get standard deviation in both axis
    sd1 = a.std(axis=0)
    sd2 = a.std(axis=1)

    # Get max in both axis
    max1 = a.max(axis=0)
    max2 = a.max(axis=1)

    # Get min in both axis
    min1 = a.min(axis=0)
    min2 = a.min(axis=1)

    # Get sum in both axis
    sum1 = a.sum(axis=0)
    sum2 = a.sum(axis=1)

    calculations = {
        'mean': [mean1.tolist(), mean2.tolist(), a.mean().tolist()],
        'variance': [var1.tolist(), var2.tolist(), a.var().tolist()],
        'standard deviation': [sd1.tolist(), sd2.tolist(), a.std().tolist()],
        'max': [max1.tolist(), max2.tolist(), a.max().tolist()],
        'min': [min1.tolist(), min2.tolist(), a.min().tolist()],
        'sum': [sum1.tolist(), sum2.tolist(), a.sum().tolist()]
    }
    return calculations