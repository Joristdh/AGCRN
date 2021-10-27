import numpy as np

ids = np.load('RAW/sensor_ids.npy')
file = np.load('RAW/distance_matrix.npy')
file_with_id = np.c_[ids[:, 0], file]


def get_most_redundant_sensor(sensors):
    print('Sensors remaining:', len(sensors))
    amount_of_short_distances_per_sensor = {}
    for i, a in enumerate(sensors):

        short_distances_per_sensor = []
        for x in range(i + 2, len(a)):
            if a[x] <= 5.6327:  # 3.5 miles is 5.6327 km
                short_distances_per_sensor.append(a[x])
        amount_of_short_distances_per_sensor[a[0]] = len(short_distances_per_sensor)

    return not amount_of_short_distances_per_sensor or \
           max(amount_of_short_distances_per_sensor.items(), key=lambda k: k[1])[0]


def delete_most_redundant_sensor_from_list(sensors):
    sensor = get_most_redundant_sensor(sensors)
    if sensor:
        delete_most_redundant_sensor_from_list(np.delete(sensors, (np.searchsorted(sensors[:, 0], sensor)), 0))
    else:
        return sensors


print(delete_most_redundant_sensor_from_list(file_with_id))
