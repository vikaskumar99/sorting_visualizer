import time

def mergeSort(data, draw, speed):
    mergeSortAlgo(data, 0 , len(data)-1, draw, speed)

def mergeSortAlgo(data, left, right, draw, speed):
    if left<right:
        middle = (left + right) // 2
        mergeSortAlgo(data, left, middle, draw, speed)
        mergeSortAlgo(data, middle+1, right, draw, speed)

        merge(data, left, middle, right, draw, speed)

def merge(data, left, middle, right, draw, speed):
    draw(data, getColorArray(len(data), left, middle, right))
    time.sleep((2.0-speed)*0.1)

    leftpart = data[left:middle+1]
    rightpart = data[middle+1:right+1]

    leftidx= rightidx = 0
    for i in range(left, right+1):
        if leftidx<len(leftpart) and rightidx<len(rightpart):
            if leftpart[leftidx] <= rightpart[rightidx]:
                data[i] = leftpart[leftidx]
                leftidx+=1
            else:
                data[i] = rightpart[rightidx]
                rightidx+=1
        elif leftidx<len(leftpart):
            data[i] = leftpart[leftidx]
            leftidx+=1
        else:
            data[i] = rightpart[rightidx]
            rightidx+=1
    draw(data, ['green' if x>=left and x<=right else 'red' for x in range(len(data))])
    time.sleep((2.0-speed)*0.1)

def getColorArray(length, left, middle, right):
    colorArray=[]
    for i in range(length):
        if i>=left and i<=right:
            if i>=left and i<=middle:
                colorArray.append('blue')
            else:
                colorArray.append('orange')
        else:
            colorArray.append('red')
    return colorArray