import time
def bubbleSort(data, draw, speed):
    if len(data)>20:
        speed = 0
    colorArr = []
    i=0
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                colorArr=['yellow' if x==j or x==j+1 else 'red' for x in range(len(data))]
                for x in range(len(data)-1,len(data)-i-1,-1):
                    colorArr[x]='green'
                draw(data, colorArr)
                time.sleep((2.0-speed)*0.1)
        i+=1
    draw(data, ['green' for x in range(len(data))])

