import gc

import numpy as np

ids = np.load('RAW/sensor_ids.npy')
file = np.load('RAW/distance_matrix.npy')
sensors = np.c_[ids[:, 0], file]


def get_most_redundant_sensor():
    amount_of_short_distances_per_sensor = {}
    for a in sensors:

        short_distances_per_sensor = []
        for x in a:
            if 5.6327 >= x > 0:  # 3.5 miles is 5.6327 km
                short_distances_per_sensor.append(x)
        amount_of_short_distances_per_sensor[a[0]] = len(short_distances_per_sensor)

    print('Adjacent sensors remaining:', len(amount_of_short_distances_per_sensor))
    return not amount_of_short_distances_per_sensor or \
           max(amount_of_short_distances_per_sensor.items(), key=lambda k: k[1])[0]


sensor = True
while sensor:
    sensors = np.delete(sensors, (np.searchsorted(sensors[:, 0], sensor)), 0)
    sensor = get_most_redundant_sensor()
    gc.collect()

np.save('sensors_to_keep', sensors)
print(len(sensors))
