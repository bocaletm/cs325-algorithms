# Mario Bocaletti
# CS325 Fall 2018
# 09/22/18

###################
# insertSort method
###################
def insertSort(data = []):
    #insert sort algorithm
    for i in range(1,len(data)):
        key = data[i]
        j = i

        while j>0 and data[j-1]>key:
            data[j] = data[j-1]
            j = j - 1

        data[j] = key

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

    #create lists
fiveK = []
tenK = []
fifteenK = []
twentyK = []
twentyFiveK = []
thirtyK = []
thirtyFiveK = []
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
for i in range(35000):
    thirtyFiveK.append(random.randint(randBot,randTop))
   
    #sort the lists and record time
startTime = time.time()
fiveK = insertSort(fiveK)
endTime = time.time()
fiveTime = endTime - startTime

startTime = time.time()
tenK = insertSort(tenK)
endTime = time.time()
tenTime = endTime - startTime

startTime = time.time()
fifteenK = insertSort(fifteenK)
endTime = time.time()
fifteenTime = endTime - startTime

startTime = time.time()
twentyK = insertSort(twentyK)
endTime = time.time()
twentyTime = endTime - startTime

startTime = time.time()
twentyFiveK = insertSort(twentyFiveK)
endTime = time.time()
twentyFiveTime = endTime - startTime

startTime = time.time()
thirtyK = insertSort(thirtyK)
endTime = time.time()
thirtyTime = endTime - startTime

startTime = time.time()
thirtyFiveK = insertSort(thirtyFiveK)
endTime = time.time()
thirtyFiveTime = endTime - startTime

#with open("insertTimes.txt","w") as fi:
#    fi.write("Input (n)\tTime\n")
#    fi.write("5000\t%s\n" % fiveTime)
#    fi.write("10000\t%s\n" % tenTime)
#    fi.write("15000\t%s\n" % fifteenTime)
#    fi.write("20000\t%s\n" % twentyTime)
#    fi.write("25000\t%s\n" % twentyFiveTime)
#    fi.write("30000\t%s\n" % thirtyTime)
#    fi.write("35000\t%s\n" % thirtyFiveTime)

print("Input (n)\tTime\n")
print("5000\t%s\n" % fiveTime)
print("10000\t%s\n" % tenTime)
print("15000\t%s\n" % fifteenTime)
print("20000\t%s\n" % twentyTime)
print("25000\t%s\n" % twentyFiveTime)
print("30000\t%s\n" % thirtyTime)
print("35000\t%s\n" % thirtyFiveTime)

