from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
import math


def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def calculate_distance_iris(point1, point2):
    distance = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2 + (
                point1[3] - point2[3]) ** 2)
    return distance


def calculate_error(x, y):
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
    blue = x[y == 1]
    red = x[y == -1]
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
    plt.title('Error Chart')
    plt.show()


def q8():
    data = np.array([[1, 6], [2, 6], [2, 7], [3, 7], [3, 8], [4, 9], [6, 1], [7, 2], [7, 3], [8, 3], [8, 4], [9, 4]])
    label = np.array([-1, 1, -1, 1, -1, -1, 1, 1, -1, 1, -1, 1])

    plot_data(data, label)
    error_acc = calculate_error(data, label)
    plot_for_k(error_acc)



def iris_db():
    iris = datasets.load_iris()
    data = iris.data
    label = iris.target
    k = int(input("Please insert an odd number for k in knn algorithm: "))
    predicts = []
    for i in range(len(data)):
        new_data = np.delete(data, i, axis=0)
        new_label = np.delete(label, i, axis=0)
        distances = []
        for j in range(len(new_data)):
            distances.append(calculate_distance_iris(data[i], new_data[j]))
        sorted_indices = np.argsort(distances)
        sorted_labels = new_label[sorted_indices]
        count = [sum(1 for element in sorted_labels[:k] if element == 0),
                 sum(1 for element in sorted_labels[:k] if element == 1),
                 sum(1 for element in sorted_labels[:k] if element == 2)]
        # print(count)
        predicts.append(np.argmax(np.array(count)))
    correct = 0
    for i in range(len(label)):
        if predicts[i] == label[i]:
            correct += 1
    error_accuracy = [(len(label) - correct) / len(label), k]
    print("for k =", k, "error=", len(label) - correct, "/", len(label), "=", error_accuracy[0])


if __name__ == '__main__':
    which_one = input("which question? ")
    if which_one == '1':
        q8()
    if which_one == '2':
        iris_db()
