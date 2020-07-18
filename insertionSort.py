import time

def insertionSort(data, draw, speed):
    colorArr=[]
    for i in range(1, len(data)): 
  
        key = data[i]  
        j = i-1
        while j >= 0 and key < data[j] : 
                data[j + 1] = data[j] 
                j -= 1
        colorArr = ['yellow' if x==i else 'red' for x in range(len(data))]
        for x in range(i-1,j,-1):
            colorArr[x] = 'black'
        draw(data,colorArr)
        time.sleep((2.0-speed)*0.1)
        data[j + 1] = key
        
    draw(data,['green' for x in range(len(data))])