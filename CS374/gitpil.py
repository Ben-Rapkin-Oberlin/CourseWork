import numpy

def arrays(arr):
    print(type(arr))
    # complete this function
    # use numpy.array
    a=numpy.empty(shape=(len(arr),1),dtype=numpy.float)
    for i in arr:
        #print (i)
        a.append(i)
    a = a[::-1]
    print(a)
        


arr = [1, 2, 3, 4, 5, 6, 7]
arrays(arr)
