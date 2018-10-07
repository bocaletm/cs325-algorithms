# Mario Bocaletti
# CS325 Fall 2018
# 10/7/18
# Stooge Sort

import math
#############
# stoogeSort
#############
def stoogeSort(data,lo,hi):
    size = hi - lo + 1
    if size == 2 and data[lo] > data[lo+1]:
        temp = data[lo]
        data[lo] = data[lo+1]
        data[lo+1] = temp

    elif size > 2:
        m = math.ceil((2 * size)/3)
        stoogeSort(data, lo, lo+m-1)
        stoogeSort(data,hi-m+1,hi)
        stoogeSort(data, lo, lo+m-1)

    return data

#############
# main
#############
    #read data from file
inputFile = open("data.txt", "r")
data = []
for line in inputFile:
    extraNum = len(data)
    data.extend(line.split())
    data.pop(extraNum)
inputFile.close()

    #typecast to int
data = list(map(int,data))

    #call stooge sort 
data = stoogeSort(data,0,len(data)-1)
    
    #print data to file
with open("stooge.out","w") as f:
    for i in range(len(data)):
        f.write("%s " % data[i])
