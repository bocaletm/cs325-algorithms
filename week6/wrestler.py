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
        self.team = ""

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

#triage wrestlers
def triageWrestlers(wrestlers,firstName):
    Q = []
    Q.append(firstName)
    sortedList = []
    invalid=False
    while len(Q) > 0:
        w = Q.pop(0)
        if wrestlers[w].team == "baby":
            rivalTeam = "heels"
            sortedList.append(w)
        else:
            rivalTeam = "baby"
            sortedList.append(w)
        for r in wrestlers[w].rivals:
            if wrestlers[r].team == "":
                wrestlers[r].team = rivalTeam
                Q.append(r)
            elif wrestlers[r].team == wrestlers[w].team:
                invalid=True
                break
        if invalid==True:
            break
    unsorted = set(wrestlers.keys()).difference(sortedList)
    if unsorted and not invalid:
            #recursively process separate trees in forest
        wrestlerSubset = dict((u,wrestlers[u]) for u in unsorted)
        newName = next(iter(unsorted))
        wrestlerSubset[newName].team = "baby"
        invalid = triageWrestlers(wrestlerSubset,newName)
    return invalid


#calculate and print the results
def babyHeel(wrestlers,firstName):
    heels = []
    babyFaces = []
    invalid=False
        #add first wrestler to babyFaces
    wrestlers[firstName].team = "baby"
        #sort the rest of the list
    invalid = triageWrestlers(wrestlers,firstName)
        #print results
    if invalid:
        print("No")
    else:
        print("Yes")
        for w in wrestlers.keys():
            if wrestlers[w].team == "baby":
                babyFaces.append(w)
            elif wrestlers[w].team=="heels":
                heels.append(w)
        print("Babyfaces: ", babyFaces)
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
