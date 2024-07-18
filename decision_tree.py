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

def mutualInformation(feature, label):
    # Using Zip to combine the lists element wise
    combined_list = Counter(zip(feature, label))
    # Obtaining the probability for each unique pair of x & y
    unique_label_count = defaultdict(Counter)
    # Initializing variable for storing mutualInformation
    i_y_x = inspection_common(label)
    # Total count of all features/labels
    total_count_data = len(feature)

    for(x_val, y_val), count in combined_list.items():
        unique_label_count[x_val][y_val] = count

    for x_val, counter in unique_label_count.items():
        countLabel = 0
        probabilities = []
        for x_val, y_val in counter.items():
            countLabel += y_val
        for x_val, y_val in counter.items():
            probabilities.append(y_val/countLabel)
        for probability in probabilities:
            i_y_x -= (countLabel/total_count_data) * (-1) * (probability * math.log2(probability))

    return i_y_x

def train(train_input):
    input = pd.read_csv(train_input, sep='\t')
    label = input.iloc[:, input.shape[1] - 1]
    feature = input.drop(input.columns[input.shape[1] - 1], axis=1)
    root = tree_recurse(feature, label)
    return root

def tree_recurse(feature, label):
    # Root node for the tree
    root = Node()
    split = mutualInfoSplitter(feature, label)

    if split == None:
        majority_vote = 'label'
        # This works fine
        # Return the majority vote classifier for the leaf.
        return majority_vote

    else:
        root.attr = split

        # The below code goes through all the values(V) of the best attribute
        # and takes a subset of value = v, where v belongs to V
        unique_values_feature = Counter(feature[split])
        new_input = pd.concat([feature,label], axis=1)
        
        for x_val, y_val in unique_values_feature.items():
            new_input = new_input[new_input[split] == x_val]

            # Only valid for 2 label values for multiple values
            # This must be changed to root children and must loop through
            # the whole list to find the corresponding splitting node.

            new_input = new_input.drop(split, axis=1)

            new_label = new_input.iloc[:,new_input.shape[1] -1]
            new_feature = new_input.drop(new_input.columns[new_input.shape[1] - 1], axis=1)

            if x_val == 0:
                root.left = tree_recurse(new_feature, new_label)

            else:
                root.right = tree_recurse(new_feature, new_label)

        return root

def mutualInfoSplitter(feature, label):
    list_mutual_info = []

    for column in feature.columns:
        list_mutual_info.append(mutualInformation(feature[column].values, label))

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
        return None
    else:
        # Use this to extract the corresponding values from the dataframe
        unique_values_feature= Counter(feature[feature.columns[i_y_x_index]])
        for x_val, y_val in unique_values_feature.items():
            new_input= feature[feature[feature.columns[i_y_x_index]] == x_val]
            print(new_input)

        return feature.columns[i_y_x_index]




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
    train('dataset/heart_test.tsv')



