from tkinter import *
from tkinter import ttk
import random
import time
import quicksort
import bubblesort

root = Tk()
root.title("Bubble Sort Visualizer")
root.maxsize(1000, 700)
root.config(bg="Black")
data = []

def generate():
	global data
	data = []
	if casemenu.get() == "worst-case":
		data = [i for i in range(20,0,-1)] # --> worst case
	#----------------------------------------------------------------
	if casemenu.get() == "average-case(without repitition)":
		# without repetition
		while True:
			r = random.randrange(1,21,1)
			if r not in data:
				data.append(r)
			if len(data) == 20:
				break
													# # --> average case
	if casemenu.get() == "average-case(with repitition)":
		# # with repetition
		for i in range(20):
			data.append(random.randrange(1,21))
	#----------------------------------------------------------------
	if casemenu.get() == "best-case":
		data = [i for i in range(0,21)] # --> best case

	drawData(data, ['#F4D35E' for x in range(len(data))])




def drawData(data, colorlist):
	canvas.delete("all")
	can_height = 480
	can_width = 900
	x_width = can_width/(len(data) + 1)
	offset = 17.5
	spacing = 10

	# normalizing data for rescaling real-valued numeric data within the
	# given range
	normalized_data = [i / max(data) for i in data]

	for i, height in enumerate(normalized_data):
		# top left corner
		x0 = i*x_width + offset + spacing
		y0 = can_height - height*340

		# bottom right corner
		x1 = ((i+1)*x_width) + offset
		y1 = can_height

		canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
		canvas.create_text(x0+10, y0, anchor=SW, text=str(data[i]))
	root.update_idletasks()


def quick_colors():
    colors_list = ['#F4D35E','#F95738','#D90429','#2B2D42','#B04AFA','#1b998b']
    name_list = ['unsorted:' , 'sorted:' ,'tail:' , 'index:' , 'pivot:' ,'swap:']
    x = 1
    for i in range (len(colors_list)):

        colors = Frame(colors_key, width=25, height=25, bg=colors_list[i])
        colors.grid(row=2, column=x, padx=10, pady=5)
        
        names1 = Label(colors_key, text=name_list[i], bg='#FAF0CA')
        names1.grid(row=2, column=x-1,padx=10,pady=5)
        i = i+1
        x = x+5



def sort_algorithm():
	global data
	if not data:
		return
	
	if sortmenu.get() == "quick_sort":
		quick_colors()
		quicksort.quick_sort(data, 0, len(data)-1, drawData)

		label= Label(timeFrame, text=quicksort.duration_time(), bg="Red", font="Times 12 bold")
		label.grid(row=0, column=0, padx=5, pady=5)
		if casemenu.get() == "worst-case":
			complexity = "Time Complexity: O(n²)"
		elif casemenu.get() == "best-case":
			complexity = "Time Complexity: Ω(n*log(n))"
		else:
			complexity = "Time Complexity: Θ(n*log(n))"

		timeComplexity= Label(timeFrame, text=complexity, bg="Green",font="Times 12 bold")
		timeComplexity.grid(row=0, column=1, padx=5, pady=5)


	if sortmenu.get() == 'bubble_sort':
		bubblesort.bubble_sort(data, drawData)
		label= Label(timeFrame, text=bubblesort.duration_time(), bg="Red", font="Times 12 bold")
		label.grid(row=0, column=0, padx=5, pady=5)
		if casemenu.get() == "worst-case":
			complexity = "Time Complexity: O(n²)"
		elif casemenu.get() == "best-case":
			complexity = "Time Complexity: Ω(n)"
		else:
			complexity = "Time Complexity: Θ(n²)"

		timeComplexity= Label(timeFrame, text=complexity, bg="Green",font="Times 12 bold")
		timeComplexity.grid(row=0, column=1, padx=5, pady=5)





Mainframe = Frame(root, width=900, height=100, bg="Grey")
Mainframe.grid(row=0, column=0, padx=10, pady=5)

timeFrame = Frame(root, width=900, height=30, bg="Grey")
timeFrame.grid(row=1, column=0, padx=10, pady=5)

colors_key = Frame(root, width=900, height=35, bg="Grey")
colors_key.grid(row=2, column=0, padx=10, pady=5)

canvas = Canvas(root, width=900, height=480, bg="Grey")
canvas.grid(row=3, column=0, padx=10, pady=5)

Button(Mainframe, text="Generate", bg="Red", command=generate).grid(row=0, column=5, padx=5, pady=5)

Button(Mainframe, text="SORT!", bg="Yellow", command=sort_algorithm).grid(row=1, column=5, padx=5, pady=5)

sortmenu = ttk.Combobox(Mainframe, textvariable=StringVar(), values=["bubble_sort","insertion_sort","merge_sort","quick_sort"])
sortmenu.grid(row=0, columnspan=4, padx=5, pady=5)
sortmenu.current(3)

casemenu = ttk.Combobox(Mainframe, textvariable=StringVar(), values=["best-case","average-case(without repitition)","average-case(with repitition)","worst-case"])
casemenu.grid(row=1, columnspan=4, padx=5, pady=5)
casemenu.current(1)


root.mainloop()