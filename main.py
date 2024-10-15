import time
from engine.graphics.graphics import window
from engine.graphics.gui import gui, UIdim, frame, line, text_box
from engine.types.color import color

from random import randint
from threading import Thread
from time import sleep

w = window(43,43,(100,100,100))
w.update()
w.render()

guiroot = gui(w)

element1 = frame(UIdim(0,0.49,0,0.49),UIdim(0,0.3,0,0.2),UIdim(0,0.5,0,0.5),10,color(100,100,100))
element2 = frame(UIdim(0,0,0,0),UIdim(1,0,0,1),UIdim(0,0,0,0),11,color(80,80,100))
element3 = frame(UIdim(-1,1,0,0),UIdim(1,0,1,0),UIdim(0,0,0,0),100,color(255,100,100))
text_icon1 = text_box("X]",UIdim(0,0,0,0),UIdim(2,1,2,1),UIdim(0,0,0,0),0)
element3.append(text_icon1)

element4 = frame(UIdim(-2,1,0,0),UIdim(1,0,1,0),UIdim(0,0,0,0),100,color(80,80,255))
text_icon2 = text_box("# ",UIdim(0,0,0,0),UIdim(2,1,2,1),UIdim(0,0,0,0),0)
element4.append(text_icon2)

element5 = frame(UIdim(-3,1,0,0),UIdim(1,0,1,0),UIdim(0,0,0,0),100,color(120,120,120))
text_icon3 = text_box("- ",UIdim(0,0,0,0),UIdim(2,1,2,1),UIdim(0,0,0,0),0)
element5.append(text_icon3)


text = text_box("Supercalifragilisticexpialidocious hello world lorum ipsum foo boo bar zoot loot shoot python goes kapoot",UIdim(1,0,1,0),UIdim(-1,1,-1,1),UIdim(0,0,0,0),2)


element1.append(element2)
element1.append(element3)
element1.append(element4)
element1.append(element5)
element1.append(text)

blanker = frame(UIdim(0,0.5,0,0.5),UIdim(0,1,0,1),UIdim(0,0.5,0,0.5),0,color(0,0,0))

bg = frame(UIdim(0,0.5,0,0.5),UIdim(0,1,0,1),UIdim(0,0.5,0,0.5),0,color(100,100,255))
bg.append(element1)
blanker.append(bg)

guiroot.append(blanker)

guiroot.decend_tree_and_plot()
guiroot.decend_tree_and_plot()

w.update()
w.render()

def tempfunc():
  while True:
    bg.size.ypercent = randint(50,100) / 100
    bg.size.xpercent = randint(50,100) / 100
    element1.position.xpercent = randint(12,88) / 100
    element1.position.ypercent = randint(12,88) / 100
    #element1.size.xpercent += 0.01
    #element1.size.ypercent += 0.007
    #if element1.size.xpercent > 0.9: element1.size.xpercent = 0.2
    #if element1.size.ypercent > 0.9: element1.size.ypercent = 0.2
    input("press enter to continue")
    guiroot.decend_tree_and_plot()
  #guiroot.decend_tree_and_plot()
    w.update()
    w.render()




t = Thread(target=tempfunc)
t.start()
sleep(0.5)
