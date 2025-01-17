import os

import numpy as np


def load_st_dataset(dataset):
    #output B, N, D
    if dataset == 'PEMSD4':
        data_path = os.path.join('../data/PeMSD4/pems04.npz')
        data = np.load(data_path)['data'][:, :, 0]  #onley the first dimension, traffic flow data
    elif dataset == 'PEMSD8':
        data_path = os.path.join('../data/PeMSD8/pems08.npz')
        data = np.load(data_path)['data'][:, :, 0]  #onley the first dimension, traffic flow data
    elif dataset == 'PEMSD4JULAUG':
        data_path = os.path.join('../data/PeMSD4_julaug/pems04julaug.npy')
        data = np.load(data_path)
    elif dataset == 'PEMSD8JANFEB':
        data_path = os.path.join('../data/PeMSD8_janfeb/pems08janfeb.npy')
        data = np.load(data_path)
    else:
        raise ValueError
    if len(data.shape) == 2:
        data = np.expand_dims(data, axis=-1)
    print('Load %s Dataset shaped: ' % dataset, data.shape, data.max(), data.min(), data.mean(), np.median(data))
    return data
