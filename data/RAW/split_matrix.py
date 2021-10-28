import numpy as np

file = np.load('distance_matrix_pems8.npy')

half = int(len(file) / 2)
np.save('distance_matrix_pems8_1', file[:half])
np.save('distance_matrix_pems8_2', file[half:])
