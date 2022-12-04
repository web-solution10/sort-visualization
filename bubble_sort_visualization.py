from graphics import *
import time
import random

win = GraphWin('bubble_sort_visualization', 1000, 500)
win.setCoords(0, 0, 200, 200)

# Generating Random List
heights = []
while True:
    r = random.randrange(10,210,10)
    if r not in heights:
        heights.append(r)
    if len(heights) == 20:
        break

# Destructuring The List Values With The Rectangles' Heights
x = 0
for i in range(len(heights)):
    heights[i] = Rectangle(Point(x,0),Point(x+10,heights[i]))
    heights[i].setFill("white")
    heights[i].draw(win)
    x += 10



def foo():
    ent = Entry(Point(100,180),50)
    ent.setText("bubblesort")
    ent.draw(win)
    text = Text(Point(100,170),"Type! Then, do a mouse-click 🖱👆")
    text.setStyle("bold")
    text.draw(win)
    
    win.getMouse()
    if ent.getText() == "bubblesort":
        ent.undraw()
        text.undraw()
        # Bubble Sort Visualization
        n = len(heights)
        for i in range(n):
            for j in range(0,n-i-1):
                bigger = int(heights[j].getP2().getY())
                smaller = int(heights[j+1].getP2().getY())
                if bigger > smaller:
                    heights[j].setFill("red")
                    heights[j+1].setFill("yellow")
                    # The Animation-----------
                    for i in range(5):
                        time.sleep(0.05)
                        heights[j].move(2,0)
                        heights[j+1].move(-2,0)
                    #-------------------------
                    heights[j].setFill("white")
                    heights[j+1].setFill("white")
                    heights[j], heights[j+1] = heights[j+1], heights[j]

    # elif ent.getText() == "insertionsort":
    #     for i in range(1, len(heights)):
    #         key = heights[i]

    #         j = i-1
    #         while j >= 0 and int(key.getP2().getY()) < int(heights[j].getP2().getY()) :

    #                 for i in range(5):
    #                     time.sleep(0.05)
    #                     heights[j+1].move(-2,0)

    #                 heights[j + 1] = heights[j]
    #                 j -= 1

    #         for i in range(5):
    #             time.sleep(0.05)
    #             heights[j+1].move(2,0)
    #             key.move(2,0)

    #         heights[j + 1] = key




foo()



win.getMouse()

