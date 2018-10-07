# Mario Bocaletti
# CS325 Fall 2018
# 09/22/18
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
thirtyFiveTime = 0

    #create lists
fiveK = []
tenK = []
fifteenK = []
twentyK = []
twentyFiveK = []
thirtyK = []
thirtyFiveK = []
    #fill lists with random numbers
for i in range(50):
    fiveK.append(random.randint(randBot,randTop))
for i in range(100):
    tenK.append(random.randint(randBot,randTop))
for i in range(150):
    fifteenK.append(random.randint(randBot,randTop))
for i in range(200):
    twentyK.append(random.randint(randBot,randTop))
for i in range(250):
    twentyFiveK.append(random.randint(randBot,randTop))
for i in range(300):
    thirtyK.append(random.randint(randBot,randTop))
for i in range(350):
    thirtyFiveK.append(random.randint(randBot,randTop))
   
    #sort the lists and record time
startTime = time.time()
fiveK = stoogeSort(fiveK,0,len(fiveK)-1)
endTime = time.time()
fiveTime = endTime - startTime

startTime = time.time()
tenK = stoogeSort(tenK,0,len(tenK)-1)
endTime = time.time()
tenTime = endTime - startTime

startTime = time.time()
fifteenK = stoogeSort(fifteenK,0,len(fifteenK)-1)
endTime = time.time()
fifteenTime = endTime - startTime

startTime = time.time()
twentyK = stoogeSort(twentyK,0,len(twentyK)-1)
endTime = time.time()
twentyTime = endTime - startTime

startTime = time.time()
twentyFiveK = stoogeSort(twentyFiveK,0,len(twentyFiveK)-1)
endTime = time.time()
twentyFiveTime = endTime - startTime

startTime = time.time()
thirtyK = stoogeSort(thirtyK,0,len(thirtyK)-1)
endTime = time.time()
thirtyTime = endTime - startTime

startTime = time.time()
thirtyFiveK = stoogeSort(thirtyFiveK,0,len(thirtyFiveK)-1)
endTime = time.time()
thirtyFiveTime = endTime - startTime

with open("stoogeTimes.txt","w") as fi:
    fi.write("Input (n)\tTime\n")
    fi.write("50\t%s\n" % fiveTime)
    fi.write("100\t%s\n" % tenTime)
    fi.write("150\t%s\n" % fifteenTime)
    fi.write("200\t%s\n" % twentyTime)
    fi.write("250\t%s\n" % twentyFiveTime)
    fi.write("300\t%s\n" % thirtyTime)
    fi.write("350\t%s\n" % thirtyFiveTime)

print("Input (n)\tTime\n")
print("50\t%s\n" % fiveTime)
print("100\t%s\n" % tenTime)
print("150\t%s\n" % fifteenTime)
print("200\t%s\n" % twentyTime)
print("250\t%s\n" % twentyFiveTime)
print("300\t%s\n" % thirtyTime)
print("350\t%s\n" % thirtyFiveTime)
