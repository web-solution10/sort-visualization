import time

def bubble_sort(data, drawData):
    global start
    global end
    n = len(data)

    start = time.time()

    for i in range(n):
        for j in range(0, n-i-1):

            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

                # if swapped then color becomes Green else stays Red
                drawData(data, ['Green' if x == j + 1 else '#F4D35E' for x in range(len(data))])

                time.sleep(0.05) # Sorting speed

    end = time.time()
    # sorted elements generated with Green color
    drawData(data, ['Green' for x in range(len(data))])


def duration_time():
    duration = "Duration Time: " + str(end - start) + " seconds"
    return duration


    





