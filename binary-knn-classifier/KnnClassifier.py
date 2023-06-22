import numpy as np
import pandas as pd


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
            raise Exception("Klasyfikator nie został jeszcze wytrenowany")  # nie wolno rzucać Exception - zbyt szeroki typ

        if self.distance_type == 'euclidean':  # a czemu to jest string, a nie już funkcja?
            distances = self.euclidean_distance(x)
        elif self.distance_type == 'taxi':
            distances = self.taxi_distance(x)
        elif self.distance_type == 'max':
            distances = self.maximum_distance(x)
        elif self.distance_type == 'cos':
            distances = self.cosinus_distance(x)
        else:
            raise Exception("Błędne określenie funkcji odległości")  # jw.

        y_predicted = []
        for element in distances:
            sorted_nearest_neighbor_indexes = np.argsort(element)
            nearest_neighbor_indexes = sorted_nearest_neighbor_indexes[:self.k]
            nearest_labels = self.y_train[nearest_neighbor_indexes]
            unique_labels, label_counts = np.unique(nearest_labels, return_counts=True)
            predicted_label = unique_labels[np.argmax(label_counts)]
            y_predicted.append(predicted_label)

        return y_predicted

    # sqrt((x2 - x1)^2 + (y2 - y1)^2) odległość w linii prostej między dwoma punktami
    def euclidean_distance(self, x_test):
        x_test = np.array(x_test)
        num_train = self.x_train.shape[0]
        num_test = x_test.shape[0]
        distances = np.zeros((num_test, num_train))

        for i in range(num_test):  # bardzo niewydajne
            squared_diff = np.square(self.x_train - x_test[i])
            sum_squared_diff = np.sum(squared_diff, axis=1)
            distances[i] = np.sqrt(sum_squared_diff)

        return distances

    # |x2 - x1| + |y2 - y1|
    def taxi_distance(self, x_test):
        x_test = np.array(x_test)  # ten kod się powtarza we wszystkich odległościach
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

    # iloczyn skalarny obu wektorów podzielony przez iloczyn ich rozmiarów,
    # jeśli dobrze rozumiem, ze źródła: https://tinyurl.com/metrykakosinusowa
    def cosinus_distance(self, x_test):
        x_test = np.array(x_test)
        num_train = self.x_train.shape[0]
        num_test = x_test.shape[0]
        distances = np.zeros((num_test, num_train))

        for i in range(num_test):
            dot_product = np.dot(self.x_train, x_test[i])
            vector_length_a = np.linalg.norm(self.x_train, axis=1)
            vector_length_b = np.linalg.norm(x_test[i])
            distances[i] = 1 - (dot_product / (vector_length_a * vector_length_b))

        return distances


# Ściąga funkcji odleglości:
# euclidean -> funkcja euklidesowa
# taxi -> funkcja taksówkowa
# max -> funkcja maximum
# cos -> funkcja cosinusowa


dataset_file = "dataset2.csv"
k_neighbor = 3
distance_function = "euclidean"

x_test_vectors = [[82.18524265650146, 78.41780024806185, 35.10949458470073, 30.03053626819411]]

knn = KnnClassifier(k_neighbor, distance_function)
data = pd.read_csv(f'data/{dataset_file}', header=None, delimiter=" ")

x_train = data.iloc[:, :-1].values
y_train = data.iloc[:, -1].values

# TRAIN
knn.train(x_train, y_train)

# PREDICTED
predicted = knn.predict(x_test_vectors)

for pred, test in zip(predicted, x_test_vectors):
    print("Predicted:", pred)
    print("Test Vector:", test)
    print("---")
