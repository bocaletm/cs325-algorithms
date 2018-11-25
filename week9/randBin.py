import random
f = open("bin2.txt","w+")
testCases = 20
f.write(str(testCases))
f.write("\n")
for i in range(testCases):
        #generate capacity
    capacity = random.randint(1,1000)
    f.write(str(capacity))
    f.write("\n")
        #generate number of items
    itemCount = random.randint(1,100)
    f.write(str(itemCount))
    f.write("\n")
        #generate item weights
    for j in range(itemCount):
        f.write(str(random.randint(1,capacity)))
        f.write(" ")
    f.write("\n")
