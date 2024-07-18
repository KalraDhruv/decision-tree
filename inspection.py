# module inspection
import argparse
import pandas as pd
import math
from collections import Counter

def inspection(input_train):

    input = pd.read_csv(input_train, sep='\t')
    labels = input.iloc[:, input.shape[1]-1]

    # Initializing counter for calculating the count for unique labels
    label_counter = Counter(labels)
    total_count = len(labels)

    entropy = 0
    for count in label_counter.values():

        probability_unique_label = count / total_count
        entropy -= probability_unique_label * math.log2(probability_unique_label)

    return entropy
def inspection_common(labels):

    # Initializing counter for calculating the count for unique labels
    label_counter = Counter(labels)
    total_count = len(labels)

    entropy = 0
    for count in label_counter.values():
        probability_unique_label = count / total_count
        entropy -= probability_unique_label * math.log2(probability_unique_label)

    return entropy

if __name__ == '__main__':
    print("hello")
    dataset = './dataset/small_train.tsv'
    value = inspection(dataset)
    print(f"The entropy of labels is: {value}")
