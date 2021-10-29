import numpy as np

dataset = np.load('RAW/pems4julaug_cleaned.npy')
filters = np.load('Filtered/PeMSD4/sensors_to_keep.npy')
ids = np.load('RAW/d04_sensors.npy')

mask = []
for i in ids:
    mask.append(i not in filters)

print(len(mask))
filtered = np.delete(dataset, mask, 1)

np.save('PeMSD4_julaug/pems04julaug', filtered)
print(filtered.shape)
