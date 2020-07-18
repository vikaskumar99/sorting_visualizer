#required imports
from tkinter import *
from tkinter import ttk
import random
from bubbleSort import bubbleSort
from mergeSort import mergeSort
from selectionSort import selectionSort
from insertionSort import insertionSort
from quickSort import quick_sort

root = Tk()
root.title("Sorting Visualizer")
root.maxsize(900, 900)
root.config(bg="black")
selected_alg=StringVar()

#array to hold the items generated
data=[]

def Generate():
    global data
    #print('Algo selected: '+ selected_alg.get())
    #data=[100,20,30,40,50,60]
    '''minval = int(minEntry.get())
    maxval = int(maxEntry.get())
    size = int(sizeEntry.get())'''
    #initialized to empty array
    data = []
    #get size from the scale bar
    length = size.get()
    #if length is zero
    if(length==0):
        length=5
    #random elements in the array
    for i in range(length):
        data.append(random.randrange(10, 100))
    
    #initially the array is unsorted, so color it Red.
    draw(data,['red' for i in range(len(data))])

#method for drawing the canvas
def draw(data, colorArray):
    #clear canvas
    canvas.delete("all")
    c_height=380
    c_width=800
    #the width of each bar is total_width / size_of_array
    x_width = c_width / len(data)
    offset = 0      #space after which bars has to be drawn
    spacing = 5     #spacing between each bar
    normalized_data = [i/max(data) for i in data]   #normalizing the data array

    if(len(data)<=20):      #if size of array is less than 20, then items value can be seen over the bar
        for i, height in enumerate(normalized_data):
            x0 = i*x_width + offset + spacing
            y0 = c_height - height * 340

            x1 = (i+1) * x_width +offset
            y1 = c_height
            #drawing the bars
            canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline=colorArray[i])
            canvas.create_text(x0+2, y0, anchor = SW, text = str(data[i]))  #write the value of each bar
    else:
        for i, height in enumerate(normalized_data):
            x0 = i*x_width + offset + spacing
            y0 = c_height - height * 340

            x1 = (i+1) * x_width +offset
            y1 = c_height
            #drawing bars
            canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline=colorArray[i])
    root.update_idletasks()

def startAlgorithm():
    global data
    #check which algorithm is selected
    if algoMenu.get()=='Bubble Sort':
        bubbleSort(data, draw, speed.get())
    elif algoMenu.get()=='Merge Sort':
        mergeSort(data,draw,speed.get())
    elif algoMenu.get()=='Selection Sort':
        selectionSort(data,draw,speed.get())
    elif algoMenu.get()=='Insertion Sort':
        insertionSort(data, draw, speed.get())
    elif algoMenu.get()=='Quick Sort':
        quick_sort(data,0, len(data)-1, draw, speed.get())
        draw(data, ['green' for x in range(len(data))])



UI_frame = Frame(root, width=800, height = 200, bg="grey")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

#creating the canvas where the bars are to be drawn
canvas = Canvas(root, width=800, height=380, bg="white")
canvas.grid(row=1, column=0, padx=10, pady=5)

#Creating Label UI
Label(UI_frame, text="Algorithms", bg="grey").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algoMenu = ttk.Combobox(UI_frame, textvariable = selected_alg, values=["Bubble Sort","Merge Sort","Selection Sort","Insertion Sort","Quick Sort"])
algoMenu.grid(row=0, column=1, padx=5, pady=5)
algoMenu.current(0)
Button(UI_frame, text="Generate", command = Generate, bg="red").grid(row=0, column=2, padx=5, pady=5)

Label(UI_frame, text="Size", bg="grey").grid(row=1, column=0, padx=5, pady=5, sticky=W)
size = Scale(master=UI_frame, from_=0, to=200, length=200,orient=HORIZONTAL)
size.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(UI_frame, text="Speed", bg="grey").grid(row=1, column=2, padx=5, pady=5, sticky=W)
speed = Scale(master=UI_frame, from_=0.1, to=2.0, length=200, digits=2, showvalue=1.0, resolution = 0.2, orient=HORIZONTAL)
speed.grid(row=1, column=3, padx=5, pady=5, sticky=W)
speed.set(1.0)

Button(UI_frame, text="Start", command = startAlgorithm, bg="red").grid(row=1, column=4, padx=5, pady=5)

#size.pack()
#sizeEntry.grid(row=1, column=1, padx=5,pady=5, sticky=W)


'''Label(UI_frame, text="MinValue", bg="grey").grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(UI_frame)
minEntry.grid(row=1, column=3, padx=5,pady=5, sticky=W)

Label(UI_frame, text="MaxValue", bg="grey").grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(UI_frame)
maxEntry.grid(row=1, column=5, padx=5,pady=5, sticky=W)'''

root.mainloop()

