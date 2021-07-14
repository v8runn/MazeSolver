# define stack to keep track
# visited set
# end x and y coordinates
# def solver(x, y):
# if the x and y coordinates are the same as end then true
# else if on a wall or already here then false
# appended to set
# if x!=0: then solve for left, correct path is true and return


maze = [[0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 1]]

visited= [[0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0]]

correctPath = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]]

startX = 0
startY = 0

endX = 4
endY = 5

def solve (x, y):
    if (x, y) == (endX, endY):
        return True
    if (maze[x][y] == 1) or (visited[x][y] == 1):
        return False
    
    visited[x][y] = 1

    if (x!=0):
        if (solve(x-1, y)):
            correctPath[x][y] = "*"
            return True
    if (x!=5):
        if (solve(x+1, y)):
            correctPath[x][y] = "*"
            return True
    if (y!=0):
        if (solve(x, y-1)):
            correctPath[x][y] = "*"
            return True
    if (y!=5):
        if (solve(x, y+1)):
            correctPath[x][y] = "*"
            return True
    
    return False



