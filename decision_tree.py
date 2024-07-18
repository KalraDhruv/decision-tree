import argparse
import math
from collections import Counter, defaultdict
from inspection import *
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.attr = None
        self.vote = None

def mutualInformation(label, feature, train_input):
    # Using Zip to combine the lists element wise
    combined_list = Counter(zip(feature, label))
    # Obtaining the probability for each unique pair of x & y
    unique_label_count = defaultdict(Counter)
    # Initializing variable for storing mutualInformation
    i_y_x = inspection(train_input)
    # Total count of all features/labels
    total_count_data = len(feature)

    for(x_val, y_val), count in combined_list.items():
        unique_label_count[x_val][y_val] = count

    for x_val, counter in unique_label_count.items():

        countLabel = 0
        probabilities = [];
        for x_val, y_val in counter.items():
            countLabel+=y_val
        for x_val, y_val in counter.items():
            probabilities.append(y_val/countLabel)
        for probability in probabilities:
            i_y_x -= (countLabel/total_count_data) * (-1) * (probability * math.log2(probability))

    return i_y_x





if __name__ == '__main__':
    value = mutualInformation([1,0,0,1,1,0,0,1],[0,0,1,0,0,1,1,0],'dataset/small_train.tsv')
    print(f"The entropy is: {value}")

    '''
    parser = argparse.ArgumentParser()
    parser.add_argument("train_input", type=str, help='path to training input .tsv file')
    parser.add_argument("test_input", type=str, help='path to the test input .tsv file')
    parser.add_argument("max_depth", type=int,
                        help='maximum depth to which the tree should be built')
    parser.add_argument("train_out", type=str,
                        help='path to output .txt file to which the feature extractions on the training data should be written')
    parser.add_argument("test_out", type=str,
                        help='path to output .txt file to which the feature extractions on the test data should be written')
    parser.add_argument("metrics_out", type=str,
                        help='path of the output .txt file to which metrics such as train and test error should be written')
    parser.add_argument("print_out", type=str,
                        help='path of the output .txt file to which the printed tree should be written')
    args = parser.parse_args()
    '''






