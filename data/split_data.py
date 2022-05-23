import os
import pandas as pd
#import sklearn
from sklearn.model_selection import train_test_split

DATA_DIRECTORY = 'all'

def split_data(datadir):
    train_frac = 0.8 #of all data
    test_frac = 0.5  #of remaining

    labels = pd.read_csv(os.path.join(datadir, 'label.txt'), header=None)
    inputs = pd.read_csv(os.path.join(datadir, 'seq.in'), header=None)
    tagging = pd.read_csv(os.path.join(datadir, 'seq.out'), header=None)

    
    # split into training and remaining
    inputs_train, inputs_test, tagging_train, tagging_test, labels_train, labels_test = train_test_split(
        inputs, tagging, labels, train_size=train_frac, random_state=6)

    # then split remaining into dev and test
    inputs_dev, inputs_test, tagging_dev, tagging_test, labels_dev, labels_test = train_test_split(
        inputs_test, tagging_test, labels_test, test_size=test_frac, random_state=6)


    # create and write files to train directory
    os.mkdir("train")
    labels_train.to_csv('train/label.txt', header=None, index=False)
    inputs_train.to_csv('train/seq.in', header=None, index=False)
    tagging_train.to_csv('train/seq.out', header=None, index=False)

    # create and write files to test directory
    os.mkdir("test")
    labels_test.to_csv('test/label.txt', header=None, index=False)
    inputs_test.to_csv('test/seq.in', header=None, index=False)
    tagging_test.to_csv('test/seq.out', header=None, index=False)

    # create and write files in dev directory
    os.mkdir("dev")
    labels_dev.to_csv('dev/label.txt', header=None, index=False)
    inputs_dev.to_csv('dev/seq.in', header=None, index=False)
    tagging_dev.to_csv('dev/seq.out', header=None, index=False)

if __name__ == "__main__":
    split_data(DATA_DIRECTORY)