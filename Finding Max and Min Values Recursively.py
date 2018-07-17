#Finding Max and Min Values
#Ryan Sleeper

def findMaxAndMin(sequence):         #This method finds the max and min values of a sequence of numbers.
    if len(sequence) < 2:            #This catches a sequence that doesn't have enough numbers to compare (less than 2).
        print("Please create a sequence of at least 2 numbers.")
    
    elif len(sequence) == 2:           #This is my base case. Once the sequence gets down to two numbers we have found the max and min.
        sequence.sort()
        return sequence[0], sequence[1]
    else:
        if sequence[0] <= sequence[1]:     #This if statement initializes the minimum number and the maximum number.
            minNum = sequence[0]
            maxNum = sequence[1]
        else:
            minNum = sequence[1]
            maxNum = sequence[0]
            
        if minNum < sequence[2]:               #Once we have a minimum and maximum, the method checks the next number and compares it to the
            if maxNum > sequence[2]:           #minimum value and the maximum value. If it is less than the minimum, then it becomes the new
                sequence.remove(sequence[2])   #minimum value. If it is greater than the maximum value then it becomes the new max value. If 
                return findMaxAndMin(sequence) #it is neither than it gets removed from the list.
            else:
                sequence.remove(maxNum)
                maxNum = sequence[1]
                return findMaxAndMin(sequence)
        else:
            sequence.remove(minNum)
            minNum = sequence[1]
            return findMaxAndMin(sequence)
        
def main():
    sequence = [54, 79, 8, 0, 9, 9, 23, 120, 40]     #This is my sequence, feel free to change it to see different results.
    minNum, maxNum = findMaxAndMin(sequence)
    print("The minimum number is: {}".format(minNum))   #I had the program print out the results to make sure it was producing the correct answers.
    print("The maximum number is: {}".format(maxNum))
    
main()
            
            