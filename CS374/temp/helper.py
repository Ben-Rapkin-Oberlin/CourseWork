import numpy as np
import datasets.mnist.loader as mnist

def get_binary_dataset():
    train_x_orig, train_y_orig, test_x_orig, test_y_orig = mnist.get_data()
 
    index_5 = np.where(train_y_orig == 5)
    index_8 = np.where(train_y_orig == 8)
 
    index = np.concatenate([index_5[0], index_8[0]])
    np.random.seed(1)
    np.random.shuffle(index)
 
    train_y = train_y_orig[index]
    train_x = train_x_orig[index]
 
    train_y[np.where(train_y == 5)] = 0
    train_y[np.where(train_y == 8)] = 1
 
    index_5 = np.where(test_y_orig == 5)
    index_8 = np.where(test_y_orig == 8)
 
    index = np.concatenate([index_5[0], index_8[0]])
    np.random.shuffle(index)
 
    test_y = test_y_orig[index]
    test_x = test_x_orig[index]
 
    test_y[np.where(test_y == 5)] = 0
    test_y[np.where(test_y == 8)] = 1
 
    return train_x, train_y, test_x, test_y
 
def pre_process_data(train_x, test_x):
    # Normalize
    train_x = train_x / 255.
    test_x = test_x / 255.
 
    return train_x, test_x