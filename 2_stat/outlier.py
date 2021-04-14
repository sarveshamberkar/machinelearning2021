import numpy as np
import matplotlib.pyplot as plt

#formula z = (X — μ) / σ

def z_score(data:list):
    threshold = 3
    outlier = []
    mean = np.mean(data)
    standard_deviation = np.std(data)
    for i in data:
        z = (i-mean)/standard_deviation
        if np.abs(z) > threshold:
            outlier.append(i)
    return outlier

def iqr(data:list):
    sorted_data = sorted(data)

if __name__ == '__main__':
    # custom dataset for example for outlier
    dataset = [11, 10, 12, 14, 12, 15, 14, 13, 15, 102, 12, 14, 17, 19, 107, 10, 13, 12, 14, 12, 108, 12, 11, 14, 13,
               15,
               10, 15, 12, 10, 14, 13, 15, 10]
    # Z-Score
    print(z_score(dataset))