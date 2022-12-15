import time

def partition(data, head, tail, drawData):
    border = head
    pivot = data[tail]

    global start
    global end
    start = time.time()
    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(0.05)

    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(0.05)

            data[border], data[j] = data[j], data[border]
            border += 1

        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(0.05)


    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(0.05)

    data[border], data[tail] = data[tail], data[border]
    
    end = time.time()
    return border

def quick_sort(data, head, tail, drawData):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData)

        #LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawData, )

        #RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawData, )



def getColorArray(dataLen, head, tail, border, currIdx, swaping = False):
    colorArray = []
    for i in range(dataLen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('#F4D35E')
        else:
            colorArray.append('#F95738')

        if i == tail:
            colorArray[i] = '#D90429'
        elif i == border:
            colorArray[i] = '#2B2D42'
        elif i == currIdx:
            colorArray[i] = '#B04AFA'

        if swaping:
            if i == border or i == currIdx:
                colorArray[i] = '#1b998b'

    return colorArray


def duration_time():
    duration = "Duration Time: " + str(end - start) + " seconds"
    return duration