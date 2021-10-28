import gc
from datetime import datetime

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
        if len(short_distances_per_sensor) > 0:
            amount_of_short_distances_per_sensor[a[0]] = len(short_distances_per_sensor)

    print(datetime.now(), 'Adjacent sensors remaining:', len(amount_of_short_distances_per_sensor))
    return not amount_of_short_distances_per_sensor or \
           max(amount_of_short_distances_per_sensor.items(), key=lambda k: k[1])[0]


removed_sensors = []
sensor = get_most_redundant_sensor()
while sensor:
    nr = np.searchsorted(sensors[:, 0], sensor)
    print(datetime.now(), 'Deleting node:', int(sensor), 'at:', nr)
    try:
        sensors = np.delete(np.delete(sensors, nr, 0), nr + 1, 1)
        removed_sensors.append(sensor)
        sensor = get_most_redundant_sensor()
        gc.collect()
    except:
        np.save('remaining_sensors', sensors)
        np.save('removed_sensors', removed_sensors)

np.save('sensors_to_keep', sensors)
np.save('removed_sensors', removed_sensors)
print(len(sensors))
