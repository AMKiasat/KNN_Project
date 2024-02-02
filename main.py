import matplotlib.pyplot as plt
import numpy as np
import math


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def calculate_best_k(x, y):
    error_accuracy = []
    for k in range(1, len(x), 2):
        predicts = []
        for i in range(len(x)):
            new_data = np.delete(x, i, axis=0)
            new_label = np.delete(y, i, axis=0)
            distances = []
            for j in range(len(new_data)):
                distances.append(calculate_distance(x[i], new_data[j]))
            sorted_indices = np.argsort(distances)
            sorted_labels = new_label[sorted_indices]
            if np.cumsum(sorted_labels[:k])[-1] > 0:
                predicts.append(1)
            else:
                predicts.append(-1)
        correct = 0
        for i in range(len(y)):
            if predicts[i] == y[i]:
                correct += 1
        error_accuracy.append([(len(y) - correct) / len(y), k])
        print("for k =", k, "\terror=", len(y) - correct, "\t/", len(y), "\t= ", error_accuracy[-1][0])
    return np.array(error_accuracy)


def plot_data(x, y):
    blue = data[label == 1]
    red = data[label == -1]
    plt.scatter(blue[:, 0], blue[:, 1], c='blue', label='Label 1')
    plt.scatter(red[:, 0], red[:, 1], c='red', label='Label -1')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.title('Scatter Plot with Different Colored Points for Labels')
    plt.show()


def plot_for_k(error_a):
    plt.bar(error_a.T[1], error_a.T[0])
    plt.xlabel('k')
    plt.ylabel('Error Accuracy')

    # Adding a title to the chart
    plt.title('Bar Chart')
    plt.show()


if __name__ == '__main__':
    data = np.array([[1, 6], [2, 6], [2, 7], [3, 7], [3, 8], [4, 9], [6, 1], [7, 2], [7, 3], [8, 3], [8, 4], [9, 4]])
    label = np.array([-1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1])

    plot_data(data, label)
    error_acc = calculate_best_k(data, label)
    plot_for_k(error_acc)
