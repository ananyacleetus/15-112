# function reads a maze file, filename, and creates a maze, m.
# Please declare "m" as a list before calling the function and then pass it in. 
def readMaze(m, filename):
  mazeFile = open(filename, "r")
  lines = mazeFile.readlines()
  for line in lines:
    line = line.strip()
    row = [c for c in line]
    m.append(row)

# This prints the maze, showing it with the usual notation as a "list of lists"
