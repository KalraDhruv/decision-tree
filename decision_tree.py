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

def train(train_input):
    root = tree_recurse(train_input)

def tree_recurse(train_input):
    q = Node()
    i = 0
    if i == 10:
        i= 1

    else:
        split = mutualInfoSplitter(train_input)
        print(f"The column selected for spliting is: {split}")

def mutualInfoSplitter(train_input):
    input = pd.read_csv(train_input, sep='\t')
    labels = input.iloc[:, input.shape[1] - 1]
    input = input.drop(input.columns[input.shape[1] - 1], axis=1)
    list_mutual_info = []

    for column in input.columns:
        list_mutual_info.append(mutualInformation(labels, input[column].values, train_input))

    print(list_mutual_info)
    i_y_x_index = -1
    index_count = 0
    i_y_x = 0

    for new_i in list_mutual_info:

       if new_i > i_y_x and new_i != 0:
            i_y_x = new_i
            i_y_x_index = index_count
       index_count += 1

    if i_y_x_index == -1:
        return 'none'
    else:
        return input.columns[i_y_x_index]




if __name__ == '__main__':
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
split = mutualInfoSplitter('dataset/small_train.tsv')
print(f"The column selected for spliting is: {split}")


