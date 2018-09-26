# Mario Bocaletti
# CS325 Fall 2018
# 09/22/18

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

    #insert sort algorithm
for i in range(1,len(data)):
    key = data[i]
    j = i

    while j>0 and data[j-1]>key:
        data[j] = data[j-1]
        j = j - 1

    data[j] = key 
    
    #print data to file
with open("insert.out","w") as f:
    for i in range(len(data)):
        f.write("%s " % data[i])


