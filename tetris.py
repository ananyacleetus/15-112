#!/usr/bin/python
#acleetus

from Tkinter import *
import random

def run(rows,cols): 
    global canvas
    root = Tk()
    root.title("Tetris")
    #starting Tetris board
    canvas = Canvas(root, width=0, height=0, bg="blue")
    #setting blue background
    canvas.pack()
    canvas.canvas = root.canvas = canvas
    root.resizable(width=0, height=0)
    root.bind("<Key>", keyPress)
    timerFired()
    init(rows,cols)
    root.mainloop()

def init(rows,cols):    
    canvas.ROWSIZE = 30
    canvas.COLSIZE = 30
    #setting size of both rows and columns
    canvas.ROWS = rows
    canvas.COLS = cols
    #sets number of rows and columns

    canvas.BORDERSIZE = 2
    #sets border 

    canvas.XOFF = 0
    canvas.YOFF = 100
    #sets x and y offsets

    canvas.data.score = 0
    canvas.data.isGameOver = False
    
    canvas.config(width=canvas.COLS*canvas.COLSIZE+canvas.XOFF, height=canvas.ROWS*canvas.ROWSIZE+canvas.YOFF)
    #width is columns x column size x x-offset 
    #height is rows x rows size x y-offset
    
    canvas.emptyColor = "blue" #empty is bluee
    canvas.gridColor = "black" #grid is blackkkkk   


    canvas.board[0][0] = "red" # TL = red
    canvas.board[0][cols-1] = "white" # TR = white
    canvas.board[rows-1][0] = "green" # BL = green
    canvas.board[rows-1][cols-1] = "gray" # BR = gray

    boardPieces()
    newFallingPiece()
    redrawAll()

def timerFired():
    removeRows()
    redrawAll()
    if (canvas.data.isGameOver == False):
        if moveFallingPiece(1,0) == False:
            placeFallingPiece()
            removeRows()
            #removes rows for redraw
            newFallingPiece()
            if fallingPieceIsLegal(canvas.data.fallingPieceRow, canvas.data.fallingPieceCol) == False:
                    canvas.data.isGameOver = True
    canvas.after(canvas.data.delay, timerFired) 

def keyPress(event):
    if (event.keysym == "r"):
        #if use hits r, game restarts
        init()
    elif event.keysym == "Left":
        moveFallingPiece(0,-1)
        #reacts to left key
    elif event.keysym == "Right":
        moveFallingPiece(0,+1)
        #reacts to left key
    elif event.keysym == "Up":
        rotateFallingPiece()
        #reacts to up key
        #calls rotatefallingpiece
    elif event.keysym == "Down":
        moveFallingPiece(+1,0)
        #reacts to down key
    else:
        newFallingPiece()
        #canvas = event.widget.canvas
        #newFallingPiece(canvas)
    redrawAll()

def drawScore():
    #draws the current score
    #called in redraw so it can update
    canvas.create_text(canvas.data.canvasWidth/2, canvas.data.margin/2, text="Score: " + str(canvas.data.score), fill="black", font="Purisa 22")

def boardPieces():
    #all of the pieces in tetris
    iPiece = [
        [ True,  True,  True,  True]
        ]

    jPiece = [
        [ True, False, False ],
        [ True, True,  True]
        ]

    lPiece = [
        [ False, False, True],
        [ True,  True,  True]   
        ]
    
    oPiece = [
        [ True, True],
        [ True, True]
        ]
    
    sPiece = [
        [ False, True, True],
        [ True,  True, False ]
        ]
    
    tPiece = [
        [ False, True, False ],
        [ True,  True, True]
        ]

    zPiece = [
        [ True,  True, False ],
        [ False, True, True]
        ]

    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", "orange" ]
    canvas.data["tetrisPieces"] = tetrisPieces
    #not sure if this should be in init... hmmm
    canvas.data["tetrisPieceColors"] = tetrisPieceColors

def rotateFallingPiece():
    #rotating the current piece that is falling
    print "before:",(canvas.fallingPieceRow,canvas.fallingPieceCol)
    oldPiece = canvas.fallingPiece
    oldRow = canvas.fallingPieceRow
    oldCol = canvas.fallingPieceCol
    canvas.fallingPieceRow -= abs(len(canvas.fallingPiece) - len(oldPiece))
    canvas.fallingPieceCol -= abs(len(canvas.fallingPiece[0]) - len(oldPiece[0]))
    print "after:",(canvas.fallingPieceRow,canvas.fallingPieceCol)
    if not fallingPieceisLegal():
        canvas.fallingPiece = oldPiece
        canvas.fallingPieceRow = oldRow
        canvas.fallingPieceCol = oldCol

def moveFallingPiece(drow,dcol):
    #moving based on change (Delta) in rows and columns
    canvas.fallingPieceRow += drow
    canvas.fallingPieceCol += dcol
    if not fallingPieceisLegal():
        canvas.fallingPieceRow -= drow
        canvas.fallingPieceCol -= dcol

def fallingPieceisLegal():
    #repeatedly checks if the current piece's place is valid
    for row in xrange(len(canvas.fallingPiece)):
        for col in xrange(len(canvas.fallingPiece[row])):
            if canvas.fallingPiece[row][col] == True:
                newRow = canvas.fallingPieceRow + row
                newCol = canvas.fallingPieceCol + col
                if (newRow < 0 or newCol < 0
                    or newRow > canvas.ROWS-1
                    or newCol > canvas.COLS-1
                    or canvas.board[newRow][newCol] != canvas.emptyColor):
                    return False
    return True

def newFallingPiece():
    index = random.randint(0,len(canvas.tetrisPieces)-1)
    canvas.fallingPiece = canvas.tetrisPieces[index]
    canvas.fallingPieceColor = canvas.tetrisPieceColors[index]
    canvas.fallingPieceRow = 0
    canvas.fallingPieceCol = canvas.COLS/2 - len(canvas.fallingPiece[0])/2

def drawFallingPiece():
    drow = dcol = 0
    for line in canvas.fallingPiece:
        for block in line:
            if block == True:
                drawCell(canvas.fallingPieceRow+drow,canvas.fallingPieceCol+dcol,canvas.fallingPieceColor)
            dcol += 1
        drow += 1
        dcol = 0
    

def drawCell(row,col,color):
    sizes = [canvas.ROWSIZE,canvas.COLSIZE]
    canvas.create_rectangle(col*sizes[0],row*sizes[1],
                    (col+1)*sizes[0],(row+1)*sizes[1], fill=canvas.gridColor)
    canvas.create_rectangle(col*sizes[0]+canvas.BORDERSIZE,row*sizes[1]+canvas.BORDERSIZE,
                    (col+1)*sizes[0]-canvas.BORDERSIZE,(row+1)*sizes[1]-canvas.BORDERSIZE, 
                    fill=color)

def drawBoard():
    for row in xrange(canvas.ROWS):
        for col in xrange(canvas.COLS):
             drawCell(row,col,canvas.board[row][col])
    drawFallingPiece()

def isFull(row):
    #referenced when removing rows 
    #used to check individual rows
    for col in canvas.data.board[row]:
        if col == canvas.data.emptyColor:
            return False
    return True

def removeRows():
    rows = len(canvas.data.board)
    x = 0
    r = fallingPieceisLegal
    for row in range(rows):
        if isFull(row):
            #removes rows from stack
            canvas.data.board.pop(row)
            canvas.data.board.insert(0, [canvas.data.emptyColor] * canvas.data.cols)
            x += 1
            r = True
    if r:
        canvas.data.score += x
       

def redrawAll():    
    if (canvas.data.isGameOver == True):
        drawBoard()
        #adds game over and restart text
        #r is in keypress
        canvas.create_text(canvas.data.canvasWidth/2, canvas.data.canvasHeight*2/5, text="Game Over!",fill="black", font="Purisa 22")
        canvas.create_text(canvas.data.canvasWidth/2,canvas.data.canvasHeight*3/5, text="Press 'r' to reset", fill="black",font="Purisa 22")
    else:
        #else redraws as current
        drawBoard()
        drawFallingPiece()
        drawScore()

run(15,10)
