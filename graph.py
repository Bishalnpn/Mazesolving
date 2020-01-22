# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:11:44 2019

@author: Bisha
"""
from tkinter import *

w = Tk()
w.title("Mazesolver")
canvas = Canvas(w, width=750, height=750, background='black')
canvas.grid(row=0, column=0)
canvas.create_line(100,650,100,275,fill="white",width=4)
canvas.create_line(100,275,425,275,fill="white",width=4)
canvas.create_line(425,275,425,300,fill="white",width=4)
canvas.create_line(425,325,425,650,fill="white",width=4)
canvas.create_line(425,650,125,650,fill="white",width=4)
#1
canvas.create_line(100,600,175,600,fill="white")
canvas.create_line(175,600,175,525,fill="white")
canvas.create_line(175,525,225,525,fill="white")
canvas.create_line(225,525,225,475,fill="white")
canvas.create_line(225,475,250,475,fill="white")
canvas.create_line(225,475,150,475,fill="white")
canvas.create_line(150,475,150,425,fill="white")
canvas.create_line(150,425,175,425,fill="white")

canvas.create_rectangle(175,425,200,450,outline="white")
#2
canvas.create_line(200,425,200,375,fill="white")
canvas.create_line(200,375,175,375,fill="white")
canvas.create_line(175,375,175,325,fill="white")
canvas.create_line(175,325,175,400,fill="white")
canvas.create_line(175,400,125,400,fill="white")
canvas.create_line(125,400,125,575,fill="white")
canvas.create_line(125,575,150,575,fill="white")
canvas.create_line(150,575,150,500,fill="white")
canvas.create_line(150,500,200,500,fill="white")
#3
canvas.create_line(125,400,125,275,fill="white")
canvas.create_line(125,275,225,275,fill="white")
canvas.create_line(225,275,225,325,fill="white")
canvas.create_line(225,325,250,325,fill="white")
canvas.create_line(250,325,250,350,fill="white")

#4
canvas.create_line(150,375,150,300,fill="white")
canvas.create_line(150,300,200,300,fill="white")
canvas.create_line(200,300,200,350,fill="white")
canvas.create_line(200,350,225,350,fill="white")
canvas.create_line(225,350,225,375,fill="white")
#5
canvas.create_line(225,375,225,450,fill="white")
canvas.create_line(225,450,350,450,fill="white")
canvas.create_line(350,450,350,500,fill="white")
canvas.create_line(350,500,400,500,fill="white")
canvas.create_line(400,500,400,525,fill="white")
canvas.create_line(400,525,325,525,fill="white")
canvas.create_line(325,525,325,475,fill="white")
canvas.create_line(325,475,275,475,fill="white")

#6
canvas.create_line(125,650,125,625,fill="white")
canvas.create_line(125,625,275,625,fill="white")
canvas.create_line(275,625,275,600,fill="white")
canvas.create_line(275,600,225,600,fill="white")
canvas.create_line(225,600,225,575,fill="white")
canvas.create_line(225,575,275,575,fill="white")
canvas.create_line(275,575,275,525,fill="white")
#7
canvas.create_line(200,625,200,575,fill="white")

#8
canvas.create_line(275,550,325,550,fill="white")
canvas.create_line(325,550,325,625,fill="white")
canvas.create_line(325,625,425,625,fill="white")
canvas.create_line(425,625,425,600,fill="white")
canvas.create_line(425,600,350,600,fill="white")
canvas.create_line(350,600,350,550,fill="white")
canvas.create_line(350,550,425,550,fill="white")
canvas.create_line(425,550,425,475,fill="white")
canvas.create_line(425,475,375,475,fill="white")
canvas.create_line(375,475,375,425,fill="white")

#9
canvas.create_rectangle(250,400,375,425,outline="white")
#10
canvas.create_line(375,400,425,400,fill="white")
canvas.create_line(425,425,425,325,fill="white")
canvas.create_line(425,325,375,325,fill="white")
canvas.create_line(375,325,375,375,fill="white")
canvas.create_line(325,375,400,375,fill="white")
canvas.create_line(400,375,400,350,fill="white")
#11
canvas.create_line(325,625,425,625,fill="white")
canvas.create_line(325,625,425,625,fill="white")
canvas.create_line(325,625,425,625,fill="white")

#12
canvas.create_line(225,375,300,375,fill="white")
canvas.create_line(300,375,300,350,fill="white")
canvas.create_line(300,350,350,350,fill="white")
canvas.create_line(350,350,350,300,fill="white")
canvas.create_line(350,300,425,300,fill="white")
canvas.create_line(425,300,425,275,fill="white")
canvas.create_line(425,275,325,275,fill="white")
canvas.create_line(325,275,250,275,fill="white")
canvas.create_line(250,275,250,300,fill="white")
canvas.create_line(250,300,300,300,fill="white")

#13
canvas.create_line(325,275,325,325,fill="white")
canvas.create_line(325,325,275,325,fill="white")
canvas.create_line(275,325,275,350,fill="white")

#14
canvas.create_line(425,450,400,450,fill="white")
canvas.create_line(400,450,400,425,fill="white")

#15
canvas.create_line(425,575,375,575,fill="white")

#16
canvas.create_line(175,550,250,550,fill="white")
canvas.create_line(250,550,250,500,fill="white")
canvas.create_line(250,500,300,500,fill="white")

#17
canvas.create_line(300,650,300,575,fill="white")

canvas.create_line(110,650,120,650,fill="white",width=4)


w.mainloop()

