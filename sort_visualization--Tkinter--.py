from tkinter import *
from tkinter import ttk
import random
import time

root = Tk()
root.title("Bubble Sort Visualizer")
root.maxsize(1000, 600)
root.config(bg="Black")
select_case = StringVar()
data = []

def generate():
	global data
	data = []
	if casemenu.get() == "worst-case":
		data = [i for i in range(20,0,-1)] # --> worst case
	#----------------------------------------------------------------
	if casemenu.get() == "average-case":
		# without repetition
		while True:
			r = random.randrange(1,21,1)
			if r not in data:
				data.append(r)
			if len(data) == 20:
				break
										# # --> average case
		# # with repetition
		# for i in range(20):
		# 	data.append(random.randrange(1,21))
	#----------------------------------------------------------------
	if casemenu.get() == "best-case":
		data = [i for i in range(0,21)] # --> best case

	drawData(data, ['Red' for x in range(len(data))])




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


def bubble(data, drawData):
	n = len(data)
	
	start = time.time()

	for i in range(n):
		for j in range(0, n-i-1):
	
			if data[j] > data[j+1]:
				data[j], data[j+1] = data[j+1], data[j]
	
				# if swapped then color becomes Green else stays Red
				drawData(data, ['Green' if x == j + 1 else 'Red' for x in range(len(data))])

				time.sleep(0.05) # Sorting speed

	end = time.time()
	duration = "Duration Time: " + str(end - start) + " seconds"


	lable= Label(Mainframe, text=duration, bg="Red")
	lable.grid(row=2, columnspan=4, padx=5, pady=5)

	# sorted elements generated with Green color
	drawData(data, ['Green' for x in range(len(data))])


def start_algorithm():
	global data
	bubble(data, drawData)




Mainframe = Frame(root, width=900, height=100, bg="Grey")
Mainframe.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=900, height=480, bg="Grey")
canvas.grid(row=1, column=0, padx=10, pady=5)

Button(Mainframe, text="Generate", bg="Red", command=generate).grid(row=1, column=2, padx=5, pady=5)

Button(Mainframe, text="START", bg="Blue", command=start_algorithm).grid(row=1, column=3, padx=5, pady=5)

casemenu = ttk.Combobox(Mainframe, textvariable=select_case, values=["average-case","best-case","worst-case"])
casemenu.grid(row=0, columnspan=4, padx=5, pady=5)
casemenu.current(0)



root.mainloop()