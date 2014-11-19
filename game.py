#!/usr/bin/python
#acleetus

from Tkinter import *
import random

#what i want to accomplish: 
#create timer to regular pipes 
#use timer for bird to move 
#user input up arrow moves bird up a certain increment 
#if bird overlaps part of pipe, bird dies--> loss 
#if bird goes through, score goes up

def run():
    global canvas
    global data
    data = {}
    root = Tk()
    root.title("Flappy Kesden")
    #starting Flappy Kesden board
    h = 500
    w = 500
    canvas = Canvas(root, width=w, height=h, bg="blue")
    #setting blue background
    canvas.pack()
    data["canvas"] = canvas
    data["height"] = h
    data ["width"] = w
    root.resizable(width=0, height=0)
    root.bind("<Key>", keyPress)
    init()
    timerFired()
    root.mainloop()

def draw_Pipe():
    canvas.create_rectangle(pipe_top, fill = "red", tag = "pipe")
    canvas.create_rectangle(pipe_bot, fill = "red", tag = "pipe")
    if pipe_top[2] <=-5:
        data["score"] +=1 
        make_Pipe()

def make_Pipe():
    global pipe_top
    global pipe_bot
    global old_pipe_top
    global old_pipe_bot
    gap = random.randrange(150, data["height"]-150)
    pipe_top = [data ["width"]-50, 0, data ["width"], gap]
    pipe_bot = [data ["width"]-50, pipe_top[3] +135, data ["width"], data["height"]]
    old_pipe_top = pipe_top[:]
    old_pipe_bot = pipe_bot[:]
    draw_Pipe()

def init():    
    global data 
    data["isGameOver"] = False
    data ["score"] = 0
    data["player_x"] = data["height"]/2
    data["player_y"] = data["width"]/2
   # data["kesden"] = PhotoImage(file = "kesden_bird.png")

def timerFired():
    global data
    canvas = data["canvas"]
    if [data["isGameOver"] == False]:
        redrawAll()
        make_Pipe()
        draw_Pipe()
        move_Pipe()
        check()
        delay = 2000
        canvas.after(delay, timerFired)

def move_Pipe():
    canvas.move("pipe", -150, 0)

def draw_Kesden():
    canvas.create_oval( data["player_x"]+ 10, data["player_y"] +10,  data["player_x"]-10 , data["player_y"] -10, fill = "black", tag = "birdie")



def redrawAll():    
    if (data["isGameOver"] == True):
        #adds game over and restart text
        #r is in keypress
        global pipe_bottom, pipe_pos
        canvas.insert(canvas.create_text(data["width"] / 2, data["height"] / 2, 0, "Game Over! Press 'r' to start a new game")
    else:
        canvas.delete("score")
        drawScore()


def keyPress(event):
    if (event.keysym == "r"):
        #if use hits r, game restarts
        run()
        redrawAll()
    if (event.keysym == "Down"):
        canvas.move("birdie",0,10)
        data["player_y"]+=10
        draw_Kesden()
    if (event.keysym == "Up"):
        canvas.move("birdie",0,-10)
        data["player_y"]-=10
        draw_Kesden()

def check():
    if data["player_y"] +10 < pipe_top[3]:
        data["isGameOver"] = True
    else:data["score"] +=1
    if data["player_y"]-10 > pipe_bot[1]:
        data["isGameOver"] = True
    else:data["score"] +=1
def drawScore():
    #draws the current score
    #called in redraw so it can update
    canvas.create_text(data["width"]/2, 20, text="Score: " + str(data["score"]), fill="black", font="Purisa 22", tag = "score")


run()