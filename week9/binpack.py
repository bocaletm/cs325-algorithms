##################
# Mario Bocaletti
# cs325 - week6
# 11/22/18
# binpack
##################
#bin class to implement bins
class Bin:
    def __init__(self,cap):
        self.cap = cap

    def setCap(self,cap):
        self.cap = cap

#read single item 
def readOne(data):
    item = data.pop(0)
    return item

#first fit algorithm
def firstFit(capacity,itemCount,weights):
    bins = []
    newBin = Bin(capacity)
    bins.append(newBin)
    binCount = 1
    #go through each item
    for i in range(itemCount):
        placed = False
        for j in range(binCount):
                #if the item fits in the bin, remove its capacity from the bin
            if bins[j].cap >= weights[i]:
                bins[j].cap -= weights[i]
                placed = True
                break
        if not placed:
            #if the item did not fit in the bin, move to the next bin 
            #and set its capacity removing the current item
            newBin = Bin(capacity - weights[i])
            bins.append(newBin)
            binCount += 1
    return binCount

#first fit decreasing
def firstFitDecreasing(capacity,itemCount,weights):
    #sort in reverse order
    sortedWeights = weights.copy()
    sortedWeights.sort(reverse=True)
    #call firstFit on the sorted weights
    return firstFit(capacity,itemCount,sortedWeights)

#best fit algorithm
def bestFit(capacity,itemCount,weights):
    bins = []
    newBin = Bin(capacity)
    bins.append(newBin)
    room = capacity
    for i in range(itemCount):
        putHere = 0
        for eachBin in bins:
            if eachBin.cap >= weights[i]:
                if (eachBin.cap - weights[i]) < room:
                    room = eachBin.cap - weights[i]
                    putHere = eachBin
        if putHere == 0:
            newBin = Bin(capacity - weights[i])
            bins.append(newBin)
        else:
            putHere.cap =- weights[i]
    return len(bins)

####################
# main
####################
#get data from file
filename = "bin.txt"
inputFile = open(filename,"r")
data = []
for line in inputFile:
    data.extend(line.split())
inputFile.close()
data = list(map(int,data))
#process data into variables
capacity = 0
itemCount = 0
weights = []
testCases = readOne(data)
for i in range(testCases):
    capacity = readOne(data)
    itemCount = readOne(data)
    for j in range(itemCount):
        weights.append(readOne(data))
        #call each function
    print("Test Case ", i+1)
    print("\tFirst Fit: ", firstFit(capacity,itemCount,weights))
    print("\tFirst Fit Decreasing: ", firstFitDecreasing(capacity,itemCount,weights))
    print("\tBest Fit: ", bestFit(capacity,itemCount,weights))

