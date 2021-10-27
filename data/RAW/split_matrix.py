import numpy as np

file = np.load('distance_matrix.npy')

half = int(len(file) / 2)
np.save('distance_matrix1', file[:half])
np.save('distance_matrix2', file[half:])
