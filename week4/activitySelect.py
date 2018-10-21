#################
# Mario Bocaletti
# cs325 - week3
# 10/18/18
# activity
#################

#ideal items class
class activity:
    def _init_(self, num, start, finish):
        self.num = num
        self.start = start
        self.finish = finish

#read single int 
def readOne(data):
    num = data.pop(0)
    return num

############
# schedule()
# calculate and print schedule
############
def schedule(activities):
        #sort by last to start
    activities.sort(key=lambda x: x.start, reverse=True)
    sched = []
        #add activity number to schedule
    sched.append(activities[0])
    for i in range(1,len(activities)):
        if (activities[i].finish <= sched[-1].start): 
            sched.append(activities[i])
        #print schedule
    print("Number of activities selected = %d" % (len(sched)))
    print("Activities:", end=" ")
    sched.reverse()
    for i in range(len(sched)):
        print(sched[i].num,end=" ")
    print("\n")

############
# main
############

#read file
inputFile = open("act.txt", "r")
data = []
for line in inputFile:
    data.extend(line.split())
inputFile.close()

    #typecast to int
data = list(map(int,data))


activities = []
count = 0
while(data):
    count += 1
    print("Set %d" % count)
        #triage file data
    activitySets = readOne(data) 
    for i in range(activitySets):
        act = activity()
        act.num = readOne(data)
        act.start = readOne(data)
        act.finish = readOne(data)
        activities.append(act)
            #calculate and print results
    schedule(activities)
    #for i in range(len(activities)):
   #     print(vars(activities[i]))
    activities[:] = []
