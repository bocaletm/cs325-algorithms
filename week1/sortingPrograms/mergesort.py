# Mario Bocaletti
# CS325 Fall 2018
# 09/22/18
# Merge Sort


##################
# merge()
##################
def merge(leftSide = [], rightSide = []):
    if not leftSide:
        return rightSide
    if not rightSide:
        return leftSide

    mergedSubData = []

    while leftSide and rightSide:
        if leftSide[0] <= rightSide[0]:
            mergedSubData.append(leftSide.pop(0))
        else:
            mergedSubData.append(rightSide.pop(0))
            
    if leftSide:
        mergedSubData.extend(leftSide)
    if rightSide:
        mergedSubData.extend(rightSide)

    return mergedSubData

##################
# mergeSort()
##################
def mergeSort(data = []):
    if len(data) <= 1:
        return data
    else:
        half = len(data)//2
        leftHalf = mergeSort(data[:half])
        rightHalf = mergeSort(data[half:])
        return merge(leftHalf,rightHalf)

#############
# main
#############
    #read data from file
inputFile = open("data.txt", "r")
data = [] 
rawData = inputFile.readlines()
for i in range(len(rawData)):
    data.extend(rawData[i].split())
inputFile.close()

    #remove first item
data.pop(0);

    #typecast to int
data = list(map(int,data))

    #call merge sort 
data = mergeSort(data)
    
    #print data to file
with open("merge.out","w") as f:
    for i in range(len(data)):
        f.write("%s " % data[i])


