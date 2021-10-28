import numpy as np

dataset = np.load('RAW/pems4julaug_all.npy')
filters = np.load('Filtered/PeMSD4/sensors_to_keep.npy')
ids = np.load('RAW/sensor_ids.npy')

mask = []
for i in ids:
    mask.append(not i[0] in filters)

filtered = np.delete(dataset, mask, 1)

print(filtered)
