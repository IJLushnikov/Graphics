from tkinter import *
from math import sin,cos,pi
root =Tk()
canv = Canvas(root, width= 960, height=960, bg="white", cursor="pencil")
canv.pack()
    

a = 10 * (5+1)
radangle = (pi/180)*a

f = open('DS5.txt')
for line in f:
    lcoor = line.split(' ')
    x = int(lcoor[0])
    y = int(lcoor[1])
    x-=480
    y-=480
    x = x*cos(radangle)-y*sin(radangle)
    y = x*sin(radangle)+y*cos(radangle)
    x+=480
    y+=480
    canv.create_line(x,y,x+1,y,fill= "blue")
    
canv.mainloop()
