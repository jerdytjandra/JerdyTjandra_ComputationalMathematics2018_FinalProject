def find_empty_location(grid, current):
    for row in range(9):
        for col in range(9):
            if(grid[row][col][2] == 0):
                current[0] = row
                current[1] = col
                return True
    return False

def used_in_row(grid, row , num):
    for i in range(9):
        if(grid[row][i][2] == num):
            return True
    return False

def used_in_col(grid , col, num):
    for i in range(9):
        if(grid[i][col][2] == num):
            return True
    return False

def used_in_box(grid, row, col, num):
    for i in range(3):
        for j in range(3):
            if(grid[i+row][j+col][2] == num):
                return True
    return False

def check_location_is_safe(grid,row,col,num):

    return not used_in_row(grid,row,num) and not used_in_col(grid,col,num) and not used_in_box(grid,row - row%3,col - col%3,num)

def solve_sudoku(grid):

    # 'current' is a list variable that keeps the record of row and col in find_empty_location Function
    current = [0,0]

    # If there is no unassigned location, we are done
    if(not find_empty_location(grid, current)):
        return True

    # Assigning list values to row and col that we got from the above Function
    row = current[0]
    col = current[1]

    # consider digits 1 to 9
    for num in range(1,10):

        # if looks promising
        if(check_location_is_safe(grid,row,col,num)):

            # make tentative assignment
            grid[row][col][2] = num

            # return, if sucess, ya!
            if(solve_sudoku(grid)):
                return True

            # failure, unmake & try again
            grid[row][col][2] = 0

    # this triggers backtracking
    return False
