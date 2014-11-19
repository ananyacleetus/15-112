#!/usr/bin/python
#acleetus

from readMaze import readMaze   

def begin(maze):
    x = -1
    y= -1
    #starting right outside maze
    for row in maze:
        y += 1
        for char in row:
            x += 1
            #goes through each letter
            if (char == 'S'):
                #print "I found the start!"
                #print x
                #print y
                return [x,y]
        x = -1  
  #  print "Lol jk, returning bad start"
    return [-1,-1]
    #out of range

def throughMaze(maze, solution, x, y):
    #goes through maze
    if y < 0 or x < 0 or y > len(maze)-1 or x > len(maze[y])-1:
       #print "This is out of bounds"
        return False
    elif (maze[y][x] == "F"):
        solution.append("(" + str(x) + "," + str(y) + ")")
        #print "You found an F"
        return True
        #for 'F's in maze
    elif (maze[y][x] == "*" or maze[y][x] == "W"):
        #print "You found a W"
        return False
        #for 'W's in maze
    maze[y][x] = "*"
    solution.append("(" + str(x) + "," + str(y) + ")")
    if (throughMaze(maze,solution,x,y-1) or throughMaze(maze,solution,x+1,y) or throughMaze(maze,solution,x,y+1) or throughMaze(maze,solution,x-1,y)):
        #print "Muawhahah this works"
        return True
    solution.pop()
    #removes last one from stack
    return False

def solveMaze(maze, solution):
    start = begin(maze)
    #finds start of the maze
    return throughMaze(maze,solution,start[0],start[1])

def mazeSolver():
    mazeFile = "sampleMaze.txt"
    maze = []
    mazeSolution = []
    m= []
    readMaze(m, mazeFile)
    if (solveMaze(m, mazeSolution)):
        print mazeSolution
    else:
        print "No solution found."

mazeSolver()