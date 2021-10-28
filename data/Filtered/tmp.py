import numpy as np

kept = np.load('PeMSD4/sensors_to_keep.npy')

removed = np.load('PeMSD4/removed_sensors.npy')

print(kept, removed)

np.save('PeMSD4/sensors_to_keep.npy', kept)
