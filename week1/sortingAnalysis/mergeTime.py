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

###################
# main method
###################

import random;
import time;
randTop = 10000
randBot = 0

    #time vars
startTime = 0
endTime = 0

fiveTime = 0
tenTime = 0
fifteenTime = 0
twentyTime = 0
twentyFiveTime = 0
thirtyTime = 0

    #create lists
fiveK = []
tenK = []
fifteenK = []
twentyK = []
twentyFiveK = []
thirtyK = []
    #fill lists with random numbers
for i in range(5000):
    fiveK.append(random.randint(randBot,randTop))
for i in range(10000):
    tenK.append(random.randint(randBot,randTop))
for i in range(15000):
    fifteenK.append(random.randint(randBot,randTop))
for i in range(20000):
    twentyK.append(random.randint(randBot,randTop))
for i in range(25000):
    twentyFiveK.append(random.randint(randBot,randTop))
for i in range(30000):
    thirtyK.append(random.randint(randBot,randTop))
    
    #sort the lists and record time
startTime = time.time()
fiveK = mergeSort(fiveK)
endTime = time.time()
fiveTime = endTime - startTime

startTime = time.time()
tenK = mergeSort(tenK)
endTime = time.time()
tenTime = endTime - startTime

startTime = time.time()
fifteenK = mergeSort(fifteenK)
endTime = time.time()
fifteenTime = endTime - startTime

startTime = time.time()
twentyK = mergeSort(twentyK)
endTime = time.time()
twentyTime = endTime - startTime

startTime = time.time()
twentyFiveK = mergeSort(twentyFiveK)
endTime = time.time()
twentyFiveTime = endTime - startTime

startTime = time.time()
thirtyK = mergeSort(thirtyK)
endTime = time.time()
thirtyTime = endTime - startTime

#with open("mergeTimes.txt","w") as fi:
#    fi.write("Input (n)\tTime\n")
#    fi.write("5000\t%s\n" % fiveTime)
#    fi.write("10000\t%s\n" % tenTime)
#    fi.write("15000\t%s\n" % fifteenTime)
#    fi.write("20000\t%s\n" % twentyTime)
#    fi.write("25000\t%s\n" % twentyFiveTime)
#    fi.write("30000\t%s\n" % thirtyTime)

print("Input (n)\tTime\n")
print("5000\t%s\n" % fiveTime)
print("10000\t%s\n" % tenTime)
print("15000\t%s\n" % fifteenTime)
print("20000\t%s\n" % twentyTime)
print("25000\t%s\n" % twentyFiveTime)
print("30000\t%s\n" % thirtyTime)
