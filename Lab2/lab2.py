from tkinter import *
root =Tk()
canv = Canvas(root, width= 540, height=960, bg="white", cursor="pencil")
canv.pack()

f = open('DS5.txt')
for line in f:
    lcoor = line.split(' ')
    x = int(lcoor[0])
    y = int(lcoor[1])
    canv.create_line(x,y,x+1,y)
    
canv.mainloop()
