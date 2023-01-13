#importing pygame module as py
import pygame as py
from pygame.locals import *
from math import pi
import random

py.init()
#chheck if display modules initialized or not if 1 else 0
#print(py.display.get_init())
width,height=200,400
pixel=64
#setting display
screen=py.display.set_mode(
(width,height)
)

#image loading part
py.display.set_caption("MonkeyBan")
loc=py.image.load('Logo.png')
py.display.set_icon(loc)
dustbin=py.image.load("monkey.png")
fruit_1=py.image.load("banana.png")

#Variable creation part
x,y=width/2,height-100
fruit_x,fruit_y=random.randint(0,width),50
score=0
delay=250
compare=5

#music loading part
background_music=py.mixer.music.load("background.mp3")
py.mixer.music.play(-1)

#collector monkey position function
def collector(w,v):
    screen.blit(dustbin,(w,v))

#fruits falling position
def fruits(a,b):
    screen.blit(fruit_1,(a,b))

#main loop
Exit=True
while Exit: 
#delay time to speed up the fruit
    py.time.delay(delay)
#screen colour 
    screen.fill((240,220,234))
#grtting event menas which key pressing
    for event in py.event.get():
        if (event.type == py.QUIT):
            Exit=False
        if (event.type==py.KEYDOWN):
            if (event.key == py.K_LEFT)and(x>0 and x<(width-pixel+9)):
                x-=10
            if(event.key==py.K_RIGHT)and(x>-1 and x<(width-pixel)):
                x+=10
        if (event.type==py.KEYUP):
            if (event.key==py.K_RIGHT) or (event.key == py.K_LEFT):
                pass
#collector function calling by executing event function              
    collector(x,y)
#increasing fruit position to create falling moment
    fruit_y+=10
#calling fruit image position fun
    fruits(fruit_x,fruit_y)
#to check monkey catched the banana or not if not game quit
    if((x-32)<fruit_x) and ((x+32)>fruit_x) and ((y-32)<fruit_y) and ((y+32)>fruit_y):
       # print("Catched")
        fruit_y=50
        fruit_x=random.randint(0,width-62)
        score+=1
    elif(fruit_y>(height-32) and fruit_y<(height+32)):
        Exit=False
        print("your score is ")
        print(score)
#to increase the speed of the banana 
    if(score>compare) and (delay>100):
        delay-=30
        compare+=5
#everything must be update
    py.display.update()
#uninitializing all modules to quit from game
py.display.quit()

