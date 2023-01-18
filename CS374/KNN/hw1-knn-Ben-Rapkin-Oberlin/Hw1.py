# Ben Rapkin
# 1 read command line args
# 2 To begin execution, the program should read in the data set as a set of instances
# 3 Then, the instances should be randomly split into training and test sets (using the
#   percentage and random seed input to the program)
# 4 Next, predictions should be made for each instance in the test set created in Step 3, using
#   the training set as the instances to compare to in the k-Nearest Neighbors algorithm.
# 5 A confusion matrix should be created based on the predictions made during Step 4, then
#   the confusion matrix should be output as a file with its name following the pattern:
#   results-<DataSet>-<k>-<Seed>.csv (e.g., results-mnist_100-1-12345.csv).

import sys
import random
import math
import csv
import time
# arg list
# program name, The path to data set, The name of the distance function,
# The value of k, The percentage of the data set to use for training, The random seed to use for splitting the data set into training and test sets
# 6 total args

def most_frequent(List):
    #from https://www.geeksforgeeks.org/python-find-most-frequent-element-in-a-list/
    return max(List, key = List.count)

def readData():
    # read data from file
    # return data
    with open(sys.argv[1], 'r') as f:
        first_line = f.readline()
        ncol = first_line.count(',') + 1
        data = []
        all_data = f.readlines()
        labels = []
        for line in all_data:
            line = line.replace('\n', '')
            line = line.split(',')
            if line[0] not in labels:
                labels.append(line[0])
            temp=[float(x) for x in line[1:]]
            temp.insert(0, line[0])
            data.append(temp)
            
    return data, labels

def euclidean_distance(instance1, instance2,length):
    #euclidean distance
    #return math.dist([float(x) for x in instance1], [float(x) for x in instance2])
    return math.dist([x for x in instance1], [x for x in instance2])

def hamming_distance(instance1, instance2, length):
    #hamming distance
    distance = 0
    for x in range(1, length):
        if instance1[x] != instance2[x]:
            distance += 1
    return distance

def kNN(train_data, classifyData, labels,distfunc):
    # takes in the training data, the data to classify, the labels, and the distance function for the kNN algorithm
    k = int(sys.argv[3])
    #prime list of neighbors to avoid if statement each  for len(neighbors) < k
    starting_point = []
    for i in range (k):
            starting_point.append(([i],sys.maxsize))
    for classifyData_instance in classifyData:
        #for each data point to classify, finds the k nearest neighbors
        neighbors = [*starting_point]
        max_neighbor=(max(neighbors, key=lambda x: x[1])) 
        for train_data_instance in train_data:
            #where the distance function is called
            dist = distfunc(classifyData_instance[1:], train_data_instance[1:], len(classifyData_instance)-1)
            if dist < max_neighbor[1]:
                #if the distance is less than the max neighbor, replace it
                neighbors.remove(max_neighbor)
                neighbors.append((train_data_instance, dist))
                max_neighbor=(max(neighbors, key=lambda x: x[1]))
        #find the most common label among the neighbors
        classifyData_instance.append(most_frequent([x[0][0] for x in neighbors]))
    return classifyData

def evaluate(results):
    #calculates accuracy
    correct = 0
    wrong = 0
    for a in results:
        if a[0] == a[-1]:
            correct += 1
        else:
            wrong += 1
   # print("Yes,No")
   # print(correct, wrong)
   # print("seed:",sys.argv[5],"Accuracy: ", correct/(correct+wrong))
    #print(correct/(correct+wrong))

def writeResults(results, labels):
    # write results to file
    with open('results-'+sys.argv[1]+'-'+sys.argv[3]+'-'+sys.argv[5]+'.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        labels.append('')
        writer.writerow(labels)
        labels=labels[:-1]
        # get all instances that are originally of class label
        for label in labels:
            # print("big loop")
            applicable = []
            for instance in result:
                # get all instances that are originally of class label
                if instance[0] == label:
                    applicable.append(instance)
            allcol = []
            for label2 in labels:
                acoppy = applicable.copy()
                c = 0
                for instance in acoppy:
                    # count how many of these instances are classified as each label
                    if instance[len(instance)-1] == label2:
                        c += 1
                        applicable.remove(instance)
                allcol.append(c)
            # write to file
            writer.writerow(allcol)

#print("#"*50)
#print("#"*50)
st = time.process_time()
data, labels = readData()  # data is a 2 dimensional list of strings
random.seed(sys.argv[5])
random.shuffle(data)
# split data based on percentage
trainingData = data[:math.floor(len(data)*float(sys.argv[4]))]
classifyData = data[math.floor(len(data)*float(sys.argv[4])):]
#use distance function based on input
if (sys.argv[2] == 'E'):
    result = kNN(trainingData, classifyData, labels, euclidean_distance)
elif (sys.argv[2] == 'H'):
    result = kNN(trainingData, classifyData, labels, hamming_distance)
#find accuracy
evaluate(result)
#write results to file
writeResults(result, labels)
#et = time.process_time()
#print("Time: ", (et-st))
