#Install -> python from microsoft store
#Install -> pip install pygame==2.1.3.dev8
#Run cd command for project folder location
# Run python Dustbin.py

#importing pygame module as py
import pygame as py
#from pygame.locals import *
from math import pi
import random
from tkinter import *
root = Tk()

py.init()

#music loading part
background_music=py.mixer.music.load("background.mp3")
py.mixer.music.play(-1)

def play():
#main loop
    #image loading part
    width,height=200,300
    pixel=64
#setting display
    screen=py.display.set_mode(
    (width,height))
    py.display.set_caption("MonkeyBan")
    loc=py.image.load('Logo.png')
    py.display.set_icon(loc)
#Variable creation part
    x,y=width/2,height-100        #collector bin coordinates
    dustbin=py.image.load("monkey.png")
    fruit_1=py.image.load("banana.png")
    Exit=True
    count=0
    score=0
    check=-1
    compare=2
    speed=7

    while Exit: 
#screen colour &
        screen.fill((240,220,234))
        py.time.delay(80)
        if score>check:
            fruit_x,fruit_y=random.randint(0,width-60),50
            check=score
#grtting event menas which key pressing
        key=py.key.get_pressed()
        for event in py.event.get():
            if (event.type == py.QUIT):
                Exit=False
        if (key[py.K_LEFT]) and (x>0 and x<(width-pixel+9)):
            x-=10
        if(key[py.K_RIGHT]) and (x>-1 and x<(width-pixel)):
            x+=10
#collector moving function blit()              
        screen.blit(dustbin,(x,y))        
#calling fruit image position fun
        if count == speed:
            fruit_y+=10
            count=0
            screen.blit(fruit_1,(fruit_x,fruit_y))
        else:
            screen.blit(fruit_1,(fruit_x,fruit_y))
#to check monkey catched the banana or not if not game quit
        if((x-32)<fruit_x) and ((x+32)>fruit_x) and ((y-32)<fruit_y) and ((y+32)>fruit_y):
            score+=1  
        elif(fruit_y>(height-32) and fruit_y<(height+32)):
            Exit=False
            print("your score is ")
            print(score)
#to increase the speed of the banana 
        if(score>compare) and (speed>1):
            speed-=1
            compare+=compare
#everything must be update
        py.display.update()
        count+=1
    py.display.quit()

button_1=Button(root,text='Play',command=play,bg='blue')
button_1.pack()
root.mainloop()
#uninitializing all modules to quit from game


