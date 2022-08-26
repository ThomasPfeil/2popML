import numpy as np
import matplotlib.pyplot as plt

def scale(data):
    return np.sign(data) * np.abs(data)**0.1

def de_scale(data):
    return np.sign(data) * np.abs(data)**10.0

def normalize(data, offset, data_min, data_max):
    return (data - data_min[:,None]) / (data_max[:, None] - data_min[:, None]) + offset

def normalize_one(data, data_min, data_max, offset):
    return (data - data_min) / (data_max - data_min) + offset

def de_normalize(data_norm, data_min, data_max, offset):
    return (data_norm - offset) * (data_max[:] - data_min[:]) + data_min[:]