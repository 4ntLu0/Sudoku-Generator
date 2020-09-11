import turtle
from random import randint, shuffle
from time import sleep

# initialize empty 9x9 grid

grid = []
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])

lTrace = turtle.Turtle()
#lTrace.tracer(0)
lTrace.speed(0)
lTrace.color("#000000")
lTrace.hideturtle()
limTopLeft_x = -150
limTopLeft_y = 150


def text(message, x, y, size):
    '''
    writes message at location
    :param message:
    :param x:
    :param y:
    :param size:
    :return:
    '''

    lFont = ("Garamond", size, "normal")
    lTrace.penup()
    lTrace.goto(x, y)
    lTrace.write(message, align="left", font=lFont)


def drawGrid(grid):
    '''
    draws the grid!
    :param grid:
    :return:
    '''

    intDim = 35
    for row in range(0, 10):
        if (row % 3) == 0:
            lTrace.pensize(3)
        else:
            lTrace.pensize(1)
        lTrace.penup()
        lTrace.goto(limTopLeft_x, limTopLeft_y - row * intDim)
        lTrace.pendown()
        lTrace.goto(limTopLeft_x + 9 * intDim, limTopLeft_y - row * intDim)

    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] != 0:
                text(grid[row][col], limTopLeft_y + col * intDim + 9, limTopLeft_y - row * intDim - intDim + 8, 18)


def checkGrid(grid):
    '''
    checks if grid is full
    :param grid:
    :return:
    '''
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False

    return True  # complete grid


def solveGrid(grid):
    '''
    backtracking/recursive function to check all combinations of numbers to find solution.
    :param grid:
    :return:
    '''
    global counter

    for i in range(0, 81):
        row = i // 9
        col = i % 9
        if grid[row][col] == 0:
            for value in range(1, 10):
                if not (value in grid[row]):  # check value not already sued
                    if not value in (
                            grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col],
                            grid[6][col],
                            grid[7][col], grid[8][col]):
                        # Identify which of the 9 squares we are working on
                        square = []
                        if row < 3:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(0, 3)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(0, 3)]
                            else:
                                square = [grid[i][6:9] for i in range(0, 3)]
                        elif row < 6:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(3, 6)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(3, 6)]
                            else:
                                square = [grid[i][6:9] for i in range(3, 6)]
                        else:
                            if col < 3:
                                square = [grid[i][0:3] for i in range(6, 9)]
                            elif col < 6:
                                square = [grid[i][3:6] for i in range(6, 9)]
                            else:
                                square = [grid[i][6:9] for i in range(6, 9)]
                        # Check that this value has not already be used on this 3x3 square
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col] = value
                            if checkGrid(grid):
                                counter += 1
                                break
                            else:
                                if solveGrid(grid):
                                    return True


numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(numberList)


def fillGrid(grid):
    '''
    backtracing=recursive fn to check all possible combos until solution.
    :param grid: 
    :return: 
    '''
    global counter

    for i in range(0, 81):
        row = i // 9
    col = i % 9
    if grid[row][col] == 0:
        shuffle(numberList)
        for value in numberList:
            # Check that this value has not already be used on this row
            if not (value in grid[row]):
                # Check that this value has not already be used on this column
                if not value in (
                grid[0][col], grid[1][col], grid[2][col], grid[3][col], grid[4][col], grid[5][col], grid[6][col],
                grid[7][col], grid[8][col]):
                    # Identify which of the 9 squares we are working on
                    square = []
                    if row < 3:
                        if col < 3:
                            square = [grid[i][0:3] for i in range(0, 3)]
                        elif col < 6:
                            square = [grid[i][3:6] for i in range(0, 3)]
                        else:
                            square = [grid[i][6:9] for i in range(0, 3)]
                    elif row < 6:
                        if col < 3:
                            square = [grid[i][0:3] for i in range(3, 6)]
                        elif col < 6:
                            square = [grid[i][3:6] for i in range(3, 6)]
                        else:
                            square = [grid[i][6:9] for i in range(3, 6)]
                    else:
                        if col < 3:
                            square = [grid[i][0:3] for i in range(6, 9)]
                        elif col < 6:
                            square = [grid[i][3:6] for i in range(6, 9)]
                        else:
                            square = [grid[i][6:9] for i in range(6, 9)]
                    # Check that this value has not already be used on this 3x3 square
                    if not value in (square[0] + square[1] + square[2]):
                        grid[row][col] = value
                        if checkGrid(grid):
                            return True
                        else:
                            if fillGrid(grid):
                                return True
            break
    grid[row][col] = 0


    #time for number deletion!

attempts=5 #change this number for more difficult puzzles.
counter = 1

while attempts>0:
    row = randint(0,8)
    col = randint(0,8)

    reset = grid[row][col]
    grid[row][col] = 0

    lGridCopy = []
    for r in range(0,9):
        lGridCopy.append([])
        for c in range(0,9):
            lGridCopy[r].append(grid[r][c])

    counter = 0
    solveGrid(lGridCopy)

    if counter !=1:
        grid[row][col] = reset
        attempts -= 1

    lTrace.clear()
    drawGrid(grid)
    lTrace.getscreen().update()


print("grid ready")