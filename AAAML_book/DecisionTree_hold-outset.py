"""While explaining about Over-fitting, I decided to divide the data into two parts.
 I trained the model on one part and checked its performance on the other part. Well,
 this is also a kind of cross-validation commonly known as a hold-outset"""

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import metrics
from sklearn import tree


def single_depth_decision_tree(depth: int):
    df = pd.read_csv('data/winequality-red.csv', sep=';')

    # how to change/map the labels
    quality_mapping = {
        3: 0,
        4: 1,
        5: 2,
        6: 3,
        7: 4,
        8: 5

    }
    # you can use the map function of pandas with
    # any dictionary to convert the values in a given
    # column to values in the dictionary

    df['quality'] = df.quality.map(quality_mapping)

    # use sample with frac=1 to shuffle the dataframe
    # we reset the indices since they change after
    # shuffling the dataframe
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    df_train = df.head(1000)
    df_test = df.tail(599)

    clf = tree.DecisionTreeClassifier(max_depth=depth)
    cols = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide',
            'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol']
    # train the model on the provided features
    # and mapped quality from before
    clf.fit(df_train[cols], df_train.quality)

    train_predict = clf.predict(df_train[cols])
    test_predict = clf.predict(df_test[cols])

    train_acc = metrics.accuracy_score(df_train.quality, train_predict)
    test_acc = metrics.accuracy_score(df_test.quality, test_predict)

    return [train_acc * 100, test_acc * 100]


def multiple_depth_decision_tree(maximum_depth: int):
    train_accuracy = []
    test_accuracy = []
    for i in range(1, maximum_depth):
        result = single_depth_decision_tree(i)
        train_accuracy.append(result[0])
        test_accuracy.append(result[1])
    return [train_accuracy, test_accuracy]


if __name__ == '__main__':
    accuracies = multiple_depth_decision_tree(25)
    plt.plot(list(range(len(accuracies[0]))), accuracies[0])
    plt.plot(list(range(len(accuracies[1]))), accuracies[1])
    plt.savefig('results/DicisionTreeAccracy.jpg')
