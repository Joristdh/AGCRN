import gc
from datetime import datetime

import numpy as np

ids = np.load('RAW/sensor_ids.npy')
file = np.load('RAW/distance_matrix.npy')
sensors = np.c_[ids[:, 0], file]
clean = np.load('RAW/d04_sensors.npy').tolist()

mask = []
for i in ids:
    mask.append(i[0] not in clean)

sensors = np.delete(sensors, mask, 0)


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
    if len(amount_of_short_distances_per_sensor) > 0:
        return max(amount_of_short_distances_per_sensor.items(), key=lambda k: k[1])[0]
    else:
        return False


removed_sensors = []
sensor = get_most_redundant_sensor()
while sensor and sensor > 0:
    nr = np.searchsorted(sensors[:, 0], sensor)
    print(datetime.now(), 'Deleting node:', int(sensor), 'at:', nr)
    try:
        sensors = np.delete(np.delete(sensors, nr, 0), nr + 1, 1)
        removed_sensors.append(sensor)
        sensor = get_most_redundant_sensor()
        gc.collect()
    except:
        np.save('Filtered/remaining_sensors', sensors)
        np.save('Filtered/removed_sensors', removed_sensors)

np.save('Filtered/sensors_to_keep', sensors[:, 0])
np.save('Filtered/removed_sensors', removed_sensors)
print(len(sensors))
