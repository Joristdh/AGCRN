import numpy as np

dataset = np.load('RAW/pems4julaug_all.npy')
filters = np.load('Filtered/PeMSD4/sensors_to_keep.npy')
ids = np.load('RAW/pemsd4_all_ids.npy')

mask = []
for i in ids:
    mask.append(i not in filters)

filtered = np.delete(dataset, mask, 1)

np.save('PeMSD4_julaug', filtered)
print(filtered.shape)
