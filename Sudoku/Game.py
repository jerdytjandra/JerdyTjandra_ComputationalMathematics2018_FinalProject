from assets import *
from Solver import *

def create_visual_map(grid):
    temp_grid = []
    temp_grid_group = Group()

    for row in range(9):
        temp_row = []

        for col in range(9):
            if grid[row][col][2] == 0:
                # print(grid[row][col][2])
                temp_value = Value(grid[row][col][0], grid[row][col][1], "  ")
                temp_row.append(temp_value)
                temp_grid_group.add(temp_value)
            else:
                # print(grid[row][col][2])
                temp_value = Value(grid[row][col][0], grid[row][col][1], grid[row][col][2])
                # print("Initialize value")
                temp_row.append(temp_value)
                # print("Appending to temp_row")
                temp_grid_group.add(temp_value)
                # print("Appending to group")

        temp_grid.append(temp_row)

    return temp_grid, temp_grid_group

def check_answer(comp_grid, visual_grid):
    win = True
    for row in range(9):
        for col in range(9):
            if visual_grid[row][col].score != comp_grid[row][col][2] and visual_grid[row][col].score != "  ":
                print("Grid[%s][%s]: %s" % (row,col,visual_grid[row][col].score))
                print("Comp grid[%s][%s]: %s" % (row,col,comp_grid[row][col][2]))
                visual_grid[row][col].answer_false()
                win = False
    if win == True:
        return False
    else:
        return True


def game(screen, screen_width, screen_height):

    #Background
    imagefile = "map.jpg"
    bg1 = Background([0,0], imagefile)

    #Sudoku data
    grid=[[[30,30,3],[90,30,0],[150,30,6],[210,30,5],[270,30,0],[330,30,8],[390,30,4],[450,30,0],[510,30,0]],
          [[30,90,5],[90,90,2],[150,90,0],[210,90,0],[270,90,0],[330,90,0],[390,90,0],[450,90,0],[510,90,0]],
          [[30,150,0],[90,150,8],[150,150,7],[210,150,0],[270,150,0],[330,150,0],[390,150,0],[450,150,3],[510,150,1]],
          [[30,210,0],[90,210,0],[150,210,3],[210,210,0],[270,210,1],[330,210,0],[390,210,0],[450,210,8],[510,210,0]],
          [[30,270,9],[90,270,0],[150,270,0],[210,270,8],[270,270,6],[330,270,3],[390,270,0],[450,270,0],[510,270,5]],
          [[30,330,0],[90,330,5],[150,330,0],[210,330,0],[270,330,9],[330,330,0],[390,330,6],[450,330,0],[510,330,0]],
          [[30,390,1],[90,390,3],[150,390,0],[210,390,0],[270,390,0],[330,390,0],[390,390,2],[450,390,5],[510,390,0]],
          [[30,450,0],[90,450,0],[150,450,0],[210,450,0],[270,450,0],[330,450,0],[390,450,0],[450,450,7],[510,450,4]],
          [[30,510,0],[90,510,0],[150,510,5],[210,510,2],[270,510,0],[330,510,6],[390,510,3],[450,510,0],[510,510,0]]]
    solve_sudoku(grid)
    # Grid sprites
    visual_grid, visual_grid_group = create_visual_map(grid)

    #Sudoku solver


    running = True
    while running:
        screen.blit(bg1.image, bg1.rect)
        visual_grid_group.draw(screen)

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                print("Mouse down")
                for row in range(9):
                    for col in range(9):
                        # print("Grid[%s][%s]: %s" % (row,col,visual_grid[row][col].score))
                        if visual_grid[row][col].rect.collidepoint(mouse.get_pos()):
                            print("grid[%s][%s] is clicked" % (row,col))
                            visual_grid[row][col].renew()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_c:
                    running = check_answer(grid,visual_grid)

            if event.type == QUIT:
                running = False
                pygame.quit()

        display.update()
