import numpy as np

file1 = np.load('distance_matrix_pems8_1.npy')
file2 = np.load('distance_matrix_pems8_2.npy')

np.save('distance_matrix', np.concatenate((file1, file2)))
