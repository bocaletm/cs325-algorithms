#ideal items class
class shoppingCart:
    def _init_(self, items, total):
        self.items = items
        self.total = total

#knapsack function returns max value and items
def knapsack(limit,items,priceWeight):
    itemsInCart = []
        #create table
    table = []
    for row in range(items+1):
        table += [[0]*(limit+1)]
    for i in range(1,items+1):
        for l in range(1,limit+1):
                    #check item weight against column limit
            if priceWeight[i-1][0] <= l:
                    #use item
                if (priceWeight[i-1][1] + table[i-1][l-priceWeight[i-1][0]]) > table[i-1][l]:
                    table[i][l] = priceWeight[i-1][1] + table[i-1][l-priceWeight[i-1][0]]                        #add used item index to cart
                else:
                    #discard item
                    table[i][l] =  table[i-1][l]
            else:
                table[i][l] = table[i-1][l]
        #get the sequence of added item weights    
    count = 0
    for i in range(items+1):
        if table[i][limit] > count:
            itemsInCart.append(table[i][limit] - count)
            count += table[i][limit]
                
                #wrap cart items and max in object
    cart = shoppingCart()
    cart.items = (itemsInCart)
    cart.total = table[items][limit]
    return cart

priceWeight = [[32,16],[43,12],[26,4],[50,8],[20,3],[27,9]]
limit = 25
items = 6
shopping = knapsack(limit,items,priceWeight)
print(shopping.items)
print(shopping.total)
limit = 23
shopping = knapsack(limit,items,priceWeight)
print(shopping.items)
print(shopping.total)
limit = 21
shopping = knapsack(limit,items,priceWeight)
print(shopping.items)
print(shopping.total)
limit = 19
shopping = knapsack(limit,items,priceWeight)
print(shopping.items)
print(shopping.total)

