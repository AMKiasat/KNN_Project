import matplotlib.pyplot as plt
import numpy as np
import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

if __name__ == '__main__':
    a = [[1, 6], [2, 6], [2, 7], [3, 7], [3, 8], [4, 9], [6, 1], [7, 2], [7, 3], [8, 3], [8, 4], [9, 4]]
    data = np.array(a)
    label = [-1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1]

    # for k in range(1, len(data), 2):
    for i in range(len(data)):
        new_data = np.delete(data, i, axis=0)
        # print(new_data)
        distances = []
        for j in range(len(new_data)):
            distances.append(calculate_distance(data[i], new_data[j]))
        print(distances)

    # plt.plot(data.T[0], data.T[1], 'o', color='blue')

    plt.show()
