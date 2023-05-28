import numpy as np


class KnnClassifier:
    def __init__(self, k, distance_type):
        self.k = k
        self.distance_type = distance_type
        self.x_train = None  # tablica wektorów
        self.y_train = None  # tablica etykiet

    def train(self, x, y):
        x = np.array(x)
        y = np.array(y)
        if self.x_train is not None:
            # Po to, aby rozszerzać zbiór przypadków uczących, gdy train uruchomimy kilka razy.
            self.x_train = np.concatenate([self.x_train, x])
            self.y_train = np.concatenate([self.y_train, y])
        else:
            self.x_train = x
            self.y_train = y

    def predict(self, x):
        if self.x_train is None or self.y_train is None:
            print("Klasyfikator nie został jeszcze wytrenowany")

        if self.distance == 'euclidean':
            distances = self.euclidean_distance(x)
        elif self.distance == 'taxi':
            distances = self.taxi_distance(x)
        elif self.distance == 'max':
            distances = self.maximum_distance(x)
        elif self.distance == 'cos':
            distances = self.cosinus_distance(x)
        else:
            print("Błędne określenie funkcji odległości")

        y_predicted = []
        for element in distances:
            sorted_nearest_neighbor_indexes = np.argsort(element)
            nearest_neighbor_indexes = sorted_nearest_neighbor_indexes[:self.k]
            nearest_labels = self.y_train[nearest_neighbor_indexes]
            unique_labels, label_counts = np.unique(nearest_labels, return_counts=True)
            predicted_label = unique_labels[np.argmax(label_counts)]
            y_predicted.append(predicted_label)

        return np.array(y_predicted)

    # sqrt((x2 - x1)^2 + (y2 - y1)^2) odległość w linii prostej między dwoma punktami
    def euclidean_distance(self, x_test):
        x_test = np.array(x_test)
        num_train = self.x_train.shape[0]
        num_test = x_test.shape[0]
        distances = np.zeros((num_test, num_train))

        for i in range(num_test):
            squared_diff = np.square(self.x_train - x_test[i])
            sum_squared_diff = np.sum(squared_diff, axis=1)
            distances[i] = np.sqrt(sum_squared_diff)

        return distances

    # |x2 - x1| + |y2 - y1|
    def taxi_distance(self, x_test):
        x_test = np.array(x_test)
        num_train = self.x_train.shape[0]
        num_test = x_test.shape[0]
        distances = np.zeros((num_test, num_train))

        for i in range(num_test):
            abs_diff = np.abs(self.x_train - x_test[i])
            sum_abs_diff = np.sum(abs_diff, axis=1)
            distances[i] = sum_abs_diff

        return distances

    # max(|x2 - x1|, |y2 - y1|)
    def maximum_distance(self, x_test):
        x_test = np.array(x_test)
        num_train = self.x_train.shape[0]
        num_test = x_test.shape[0]
        distances = np.zeros((num_test, num_train))

        for i in range(num_test):
            abs_diff = np.abs(self.x_train - x_test[i])
            max_abs_diff = np.max(abs_diff, axis=1)
            distances[i] = max_abs_diff

        return distances
