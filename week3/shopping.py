#################
# Mario Bocaletti
# cs325 - week3
# 10/12/18
# shopping
#################

#ideal items class
class shoppingCart:
    def _init_(self, items, total):
        self.items = items
        self.total = total

#read single int 
def readOne(data):
    num = data.pop(0)
    return num

#read two int into a list
def readList(items,data,times):
    itemList = []
    timesList = []
    for i in range(items):
        for j in range(times):
            timesList.insert(len(timesList),data.pop(0))
        itemList.append(list(timesList))
        timesList[:] = []
    return itemList
        
#knapsack function returns max value and items
def knapsack(limit,items,priceWeight):
    itemsInCart = []
        #create table
#    table = []
#    for row in range(items+1):
#        table += [[0]*(limit+1)]
    table = [[0 for l in range(limit+1)]
                for i in range(items+1)]
    for i in range(items+1):
        for l in range(limit+1):
            if i == 0 or l == 0:
                table[i][l] = 0
                    #check item weight against column limit
            elif priceWeight[i-1][1] <= l:
                    #use item
                if (priceWeight[i-1][0] + table[i-1][l-priceWeight[i-1][1]]) > table[i-1][l]:
                    table[i][l] = priceWeight[i-1][0] + table[i-1][l-priceWeight[i-1][1]]                        
                else:
                    #discard item
                    table[i][l] =  table[i-1][l]
            else:
                table[i][l] = table[i-1][l]
        #get the sequence of added item weights   
        #Reference: https://stackoverflow.com/questions/49715583/get-the-element-of-a-list-in-knapsack-0-1
    tmpW = limit
    total = table[items][limit]
    for i in range(items,0,-1):
        if total <= 0:
            break
        if total == table[i-1][tmpW]:
            continue
        else:
            #itemsInCart.append(priceWeight[i-1][1])
            itemsInCart.insert(0,i)
            total -= priceWeight[i-1][0] 
            tmpW -= priceWeight[i-1][1]
                
                #wrap cart items and max in object
    cart = shoppingCart()
    cart.items = itemsInCart
    cart.total = table[items][limit]
   # for i in range(items+1):
   #     print(table[i])
   # print()
    return cart

    
#calculate and print results
def shopping(items,priceWeight,familyMembers,familyWeights):
    #print(items)
    #print(priceWeight)
    #print(familyMembers)
    #print(familyWeights)
    familyCarts = []
    price = 0
    for i in range(familyMembers):
       familyCarts.append(knapsack(int(familyWeights[i][0]),items,priceWeight))
       price += familyCarts[i].total
    print("Total Price: ", price, file=open("shopping.out","a"))
    print("Member Items: ", file=open("shopping.out","a"))
    for j in range(familyMembers):
        print(j+1,"->", familyCarts[j].items,file=open("shopping.out","a"))

############
# main
############
import os
#read file
inputFile = open("shopping.txt", "r")
data = []
for line in inputFile:
    data.extend(line.split())
inputFile.close()

    #typecast to int
data = list(map(int,data))

#triage file data
testCases = readOne(data) 

priceWeight = []
familyWeights = []
os.remove("shopping.out")
for i in range(testCases):
    items = readOne(data)
    priceWeight.extend(readList(items,data,2))
    familyMembers = readOne(data)
    familyWeights.extend(readList(familyMembers,data,1))
        #calculate and print results
    print("Test Case:", i+1,file=open("shopping.out","a"))
    shopping(items,priceWeight,familyMembers,familyWeights)
    priceWeight[:] = []
    familyWeights[:] = []
