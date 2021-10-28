import numpy as np

dataset = np.load('RAW/pems8janfeb_all.npy')
filters = np.load('Filtered/PeMSD8/sensors_to_keep.npy')
ids = np.load('RAW/sensor_ids_pems8.npy')[:, 0]

mask = []
for i in ids:
    mask.append(i not in filters)

filtered = np.delete(dataset, mask, 1)

np.save('PeMSD8/pems8janfeb_206', filtered)
print(filtered.shape)
