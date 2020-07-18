import time

def selectionSort(data, draw, speed):
    colorArr=[]
    idx=0
    for i in range(len(data)): 
        min_idx = i 
        for j in range(i+1, len(data)): 
            if data[min_idx] > data[j]: 
                min_idx = j  
        colorArr=['yellow' if x==i or x==min_idx else 'red' for x in range(len(data))]
        for x in range(idx):
            colorArr[x]='green'
        idx+=1
        draw(data, colorArr)
        time.sleep((2.0-speed)*0.1)
        data[i], data[min_idx] = data[min_idx], data[i]
    draw(data,['green' for x in range(len(data))])

