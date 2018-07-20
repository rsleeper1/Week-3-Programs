#Reverse A List
#Ryan Sleeper
#This program will reverse a list.

def swapItem(item, list, itemCount):      #This method swaps items in a list. It takes three parameters, an item, the list with the included items and 
    if itemCount == len(list):            #an itemCount which keeps track of the number of items we have swapped in the list.
        return list                       #This is my base case. My function will call itself until the itemCount is equal to the length of the list.
    else:
        list.insert(len(list) - itemCount, item)
        list.remove(item)
        itemCount = itemCount + 1
        return swapItem(list[0], list, itemCount)  #This is where the method calls itself until it has gone through the entire list.
    
def main():
    list = ["apples","berries","bananas","watermelons"]   #This is a random list I made. Feel free to change it and use other words or numbers.
    print("Original List: {}".format(list))      #I wanted to print out the original to make it easier to see that the program does in fact
    itemCount = 0                                #reverse the items.
    swapItem(list[0], list, itemCount)
    print("Reversed List: {}".format(list))
        
main()
    



    
    
        
        
        