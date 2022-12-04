from graphics import *
import time
import random




win = GraphWin('movingEmoji', 1000, 500)
win.setCoords(0, 0, 200, 200)


rec = Rectangle(Point(10,10),Point(40,20))
rec.draw(win)
print(rec.getP2().getY())

win.getMouse()


