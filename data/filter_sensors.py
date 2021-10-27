import gc

import numpy as np

ids = np.load('RAW/sensor_ids.npy')
file = np.load('RAW/distance_matrix.npy')
sensors = np.c_[ids[:, 0], file]


def get_most_redundant_sensor():
    print('Sensors remaining:', len(sensors))
    amount_of_short_distances_per_sensor = {}
    for a in sensors:

        short_distances_per_sensor = []
        for x in a:
            if 5.6327 >= x > 0:  # 3.5 miles is 5.6327 km
                short_distances_per_sensor.append(x)
        amount_of_short_distances_per_sensor[a[0]] = len(short_distances_per_sensor)

    return not amount_of_short_distances_per_sensor or \
           max(amount_of_short_distances_per_sensor.items(), key=lambda k: k[1])[0]


sensor = True
while sensor:
    print(gc.get_count())
    sensors = np.delete(sensors, (np.searchsorted(sensors[:, 0], sensor)), 0)
    sensor = get_most_redundant_sensor()
    gc.collect()
    print(gc.get_count())

print(len(sensors))
print(sensors)
