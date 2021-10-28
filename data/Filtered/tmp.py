import numpy as np

kept = np.load('sensors_to_keep.npy')[:, 0]

removed = np.load('removed_sensors.npy')

print(kept, removed)

np.save('sensors_to_keep.npy', kept)
