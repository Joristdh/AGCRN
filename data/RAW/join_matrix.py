import numpy as np

file1 = np.load('distance_matrix1.npy')
file2 = np.load('distance_matrix2.npy')

np.save('distance_matrix2', np.concatenate(file1, file2))
