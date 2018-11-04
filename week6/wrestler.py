##################
# Mario Bocaletti
# cs325 - week6
# 11/4/18
# wrestler
##################

# wrestler class has a list of rivals
class Wrestler:
    def __init__(self):
        self.rivals = set()

    def addRival(self,rival):
        self.rivals.add(rival)
    
    def hasRival(self,rival):
        if rival in self.rivals:
            return True
        else:
            return False

#read single item 
def readOne(data):
    item = data.pop(0)
    return item

#calculate and print the results
def babyHeel(wrestlers,firstName):
    heels = set() 
    babyFaces = set()
        #add first wrestler to babyFaces
        #and its rivals to the heels
    babyFaces.add(firstName)
    heels = wrestlers[firstName].rivals
    wrestlers.pop(firstName)
    #wrestlers.pop(wrestlers[firstName])
    for w in wrestlers.keys():
        if w not in heels:
            babyFaces.add(w)
            heels = heels.union(wrestlers[w].rivals)
        else:
            heels.add(w)
            babyFaces = babyFaces.union(wrestlers[w].rivals)
    invalid = heels.intersection(babyFaces)
    if invalid:
        print("No")
    else:
        print("Babyfaces: ",  babyFaces)
        print("Heels: ", heels)

        
################
# main
################
import sys
#read file
filename = sys.argv[1]
inputFile = open(filename, "r")

data = []
for line in inputFile:
    data.extend(line.split())
inputFile.close()

#create dictionary of wrestler objects
wrestlers = {}
wrestlerCount = int(readOne(data))
for i in range(wrestlerCount):
    name = readOne(data)
    #just to start the babyface list with the first name provided
    if i == 0:
        firstName = name
    wrestlers[name] = Wrestler()

#add rivals to wrestlers
rivalries = int(readOne(data))
for r in range(rivalries):
    redCorner = readOne(data)
    blueCorner = readOne(data)
    wrestlers[redCorner].addRival(blueCorner)
    wrestlers[blueCorner].addRival(redCorner)

#get results
babyHeel(wrestlers,firstName)
