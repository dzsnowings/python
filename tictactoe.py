from turtle import *
import turtle as t

setup(width =750, height = 750, startx = -100, starty = 0)

def drawBoard():
	ht()
	speed(0)
	pd()
	forward(300)
	pu()

def getPos(x, y):
	print("(", x, "," ,y,")")
	return

def main():
    t.onscreenclick(getPos)
    t.mainloop()

goto(-150, 0)
drawBoard()
goto(-150, -100)
drawBoard()
goto(-150, 100)
drawBoard()
goto(-150, -200)
drawBoard()
goto(-150, 100)
right(90)
drawBoard()
goto(-50, 100)
drawBoard()
goto(50, 100)
drawBoard()
goto(150, 100)
drawBoard()

print("Let's play Tic-Tac-Toe!")

main()
for i in range(100):
	if (x>-150 or x<-50) and (y>0 or y<100):
		circle(75)



#color('red', 'yellow')
#begin_fill()
#while True:
#    forward(200)
#    left(170)
#    if abs(pos()) < 1:
#       break
#end_fill()
#done()
