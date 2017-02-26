def peakFinder(input):
        n = len(input)
        middleIndex = n/2
        middleIsMax = input[middleIndex] > input[middleIndex + 1] and input[middleIndex] > input[middleIndex - 1]

        # base case 
        if middleIsMax:
            return input[middleIndex]

        leftArray = input[:middleIndex]
        rightArray = input[middleIndex:]

        moveRight = input[middleIndex + 1] > input[middleIndex] and input[middleIndex + 1] > input[middleIndex - 1]

        moveLeft = input[middleIndex - 1] > input[middleIndex] and input[middleIndex - 1] > input[middleIndex + 1]

        # recursive case
        if moveRight:
            return peakFinder(rightArray)
        elif moveLeft:
            return peakFinder(leftArray)    

print peakFinder([2, 25, 17, 11, 13, 7])