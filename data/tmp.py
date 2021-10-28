import numpy as np

file = np.load('RAW/pemsd4_all_ids.npy')
file2 = np.load('RAW/sensor_ids.npy')[:, 0].tolist()

for f in file2:
    if f not in file:
        print(f)

print(len(file), len(file2))
