import arcade
WIDTH = 30
HEIGHT= 30
MARGIN = 2
ROW_COUNT = 15
COLUMN_COUNT = 16
GRID = []
player_row = 1
player_column = 0
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN + 200
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN

grid_row = []
grid_column = []
key_get_1 = 0
key_get_2 = 0
gate_open_1 = 0
gate_open_2 = 0
win = 0

level2 = 0
timer = 0

def player():
    global GRID, x, y, color, row, column, player_row, player_column, open, gate_open_1, gate_open_2, win, open2, level2, key_get_1, key_get_2, timer
    if level2 == 0:
        row = player_row
        column = player_column
        GRID[row][column] = 2
        arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
        if player_column == 14 and player_row == 13:
            win += 1
        if win == 1:
            arcade.draw_text("YOU WIN", 566, 300, arcade.color.WHITE, 12)
            player_row = 1
            player_column = 0
            for i in range(len(grid_row)):
                for j in range(len(grid_column)):
                    GRID[grid_row[i]][grid_column[j]] = 0
            if GRID[row][column] == 2:
                GRID[row][column] = 0
            GRID[9][3] = 6
            GRID[10][9] = 8
            open = False
            key_get_1 = 0
            key_get_2 = 0
            gate_open_1 = 0
            gate_open_2 = 0
            GRID[11][7] = 5
            GRID[13][12] = 7
            grid_reset()
            arcade.draw_rectangle_filled(400, 300, 1200, 600, arcade.color.BLACK)
            level2setup()
            timer = 0
            level2 = 1

        if win == 0:
            # teleporters
            if player_column == 7 and player_row == 3:
                player_column = 3
                player_row = 4
                GRID[3][3] = 1
                GRID[3][7] = 1
            if player_column == 3 and player_row == 3:
                player_column = 7
                player_row = 4
                GRID[3][3] = 1
                GRID[3][7] = 1

            # key and gate
            if GRID[9][3] == 2:
                open = True
            if open == True and gate_open_1 == 0:
                GRID[9][3] = 2
                GRID[11][7] = 0
            if open == True and gate_open_1 > 0:
                GRID[11][7] = 2
                GRID[9][3] = 2
            if GRID[10][9] == 2:
                open2 = True
            if open2 == True and gate_open_2 == 0:
                GRID[10][9] = 2
                GRID[13][12] = 0
            if open2 == True and gate_open_2 > 0:
                GRID[10][9] = 2
                GRID[13][12] = 2

def player2():
    global level2, player_column, player_row, row, column, GRID
    if level2 == 1:
        row = player_row
        column = player_column
        GRID[row][column] = 2
        arcade.draw_rectangle_filled(x, y, 23.1, 23.1, color)

        #teleporters
        if win == 2:
            # teleporter 1
            if player_row == 1 and player_column == 18:
                player_row = 18
                player_column = 2
                GRID[1][18] = 1
                GRID[18][1] = 1
            # teleporter 2
            if player_row == 5 and player_column == 1:
                player_row = 9
                player_column = 1
                GRID[5][1] = 1
                GRID[10][1] = 1
            if player_row == 10 and player_column == 1:
                player_row = 5
                player_column = 2
                GRID[5][1] = 1
                GRID[10][1] = 1
            # teleporter 3
            if player_row == 5 and player_column == 18:
                player_row = 3
                player_column = 17
                GRID[5][18] = 1
                GRID[3][18] = 1
            if player_row == 3 and player_column == 18:
                player_row = 5
                player_column = 17
                GRID[5][18] = 1
                GRID[3][18] = 1
            # teleporter 4
            if player_row == 16 and player_column == 1:
                player_row = 16
                player_column = 17
                GRID[16][1] = 1
                GRID[16][18] = 1
            if player_row == 16 and player_column == 18:
                player_row = 16
                player_column = 2
                GRID[16][1] = 1
                GRID[16][18] = 1

def grid_reset():
    global GRID, grid_row, grid_column, row
    GRID = []
    grid_row = []
    grid_column = []


def on_draw():
    global GRID, color, column, row, x, y, win, row2, column2, GRID2, level2, timer
    if level2 == 0:
        if win == 0:
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    if row == 0 or row == 14 or (column == 0 and row != 1) or (column == 14 and row != 13):
                        GRID[row][column] = 1
                    if column == 15:
                        GRID[row][column] = 3

                    if GRID[row][column] == 0:
                        color = arcade.color.BLACK
                    elif GRID[row][column] == 1:
                        color = arcade.color.PURPLE
                    elif GRID[row][column] == 2:
                        color = arcade.color.BLUE
                    elif GRID[row][column] == 3:
                        color = arcade.color.BLACK
                    elif GRID[row][column] == 4:
                        color = arcade.color.BLUEBERRY
                    elif GRID[row][column] == 5:
                        color = arcade.color.YELLOW
                    elif GRID[row][column] == 6:
                        color = arcade.color.DARK_YELLOW
                    elif GRID[row][column] == 7:
                        color = arcade.color.GREEN
                    elif GRID[row][column] == 8:
                        color = arcade.color.BOTTLE_GREEN




                    x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                    y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                    arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)


                    for r in range(2, 6):
                        GRID[r][2] = 1
                    for r in range(7, 13):
                        GRID[r][2] = 1
                    for c in range(2, 5):
                        GRID[7][c] = 1
                    for r in range(2, 7):
                        GRID[r][4] = 1
                    for c in range(2, 5):
                        GRID[2][c] = 1
                    for r in range(2, 12):
                        GRID[r][12] = 1
                    for r in range(2, 10):
                        GRID[r][10] = 1
                    for r in range(9, 12):
                        GRID[r][4] = 1
                    for c in range(8, 12):
                        GRID[11][c] = 1
                    for r in range(9, 12):
                        GRID[r][6] = 1
                    for c in range(6, 10):
                        GRID[9][c] = 1
                    for r in range(2, 8):
                        GRID[r][6] = 1
                        GRID[r][8] = 1
                    for c in range(6, 9):
                        GRID[2][c] = 1
                    for c in range(12, 14):
                        GRID[12][c] = 1
                    GRID[3][7] = 4
                    GRID[3][3] = 4
        if win == 0:
            key()
            gate()
            player()

        arcade.draw_rectangle_filled(525, 100, 30, 30, arcade.color.DARK_YELLOW)
        arcade.draw_rectangle_filled(675, 100, 30, 30, arcade.color.YELLOW)
        arcade.draw_text("unlocks", 567, 95, arcade.color.WHITE, 13)

        arcade.draw_rectangle_filled(525, 150, 30, 30, arcade.color.BOTTLE_GREEN)
        arcade.draw_rectangle_filled(675, 150, 30, 30, arcade.color.GREEN)
        arcade.draw_text("unlocks", 567, 145, arcade.color.WHITE, 13)

        arcade.draw_rectangle_filled(525, 50, 30, 30, arcade.color.BLUEBERRY)
        arcade.draw_rectangle_filled(675, 50, 30, 30, arcade.color.BLUEBERRY)
        arcade.draw_text("teleporters", 555, 45, arcade.color.WHITE, 13)

        arcade.draw_text("LEVEL 1", 545, 400, arcade.color.RED, 20)

        arcade.draw_line(500, 75, 700, 75, arcade.color.WHITE, 7)
        arcade.draw_line(500, 210, 700, 210, arcade.color.WHITE, 7)

        arcade.draw_text("Keys:", 505, 180, arcade.color.WHITE, 12)
        arcade.draw_text("Gates:", 650, 180, arcade.color.WHITE, 12)

        arcade.draw_text("W: Move Up", 545, 340, arcade.color.WHITE, 12)
        arcade.draw_text("A: Move Left", 545, 320, arcade.color.WHITE, 12)
        arcade.draw_text("S: Move Down", 545, 300, arcade.color.WHITE, 12)
        arcade.draw_text("D: Move Right", 545, 280, arcade.color.WHITE, 12)
        arcade.draw_text("K: Reset Level", 545, 260, arcade.color.WHITE, 12)

    if level2 == 1:
        arcade.draw_rectangle_filled(400, 300, 1200, 600, arcade.color.BLACK)
        arcade.draw_text("LEVEL 1 COMPLETE!!!", 135, 250, arcade.color.WHITE, 30)
        if timer > 4:
            win = 2
            arcade.draw_rectangle_filled(400, 300, 1200, 600, arcade.color.BLACK)
            second_draw()


def second_draw():
    global GRID, row, column, color, level2, x, y
    for row in range(20):
        for column in range(21):
            if row == 0 or row == 19 or (column == 0 and row != 1) or (column == 19 and row != 18):
                GRID[row][column] = 1
            if column == 20:
                GRID[row][column] = 3

            if GRID[row][column] == 0:
                color = arcade.color.BLACK
            elif GRID[row][column] == 1:
                color = arcade.color.PURPLE
            elif GRID[row][column] == 2:
                color = arcade.color.BLUE
            elif GRID[row][column] == 3:
                color = arcade.color.BLACK
            elif GRID[row][column] == 4:
                color = arcade.color.BLUEBERRY
            elif GRID[row][column] == 5:
                color = arcade.color.VIOLET_RED
            elif GRID[row][column] == 6:
                color = arcade.color.INDIGO
            elif GRID[row][column] == 7:
                color = arcade.color.PURPLE_PIZZAZZ
            elif GRID[row][column] == 8:
                color = arcade.color.YELLOW
            elif GRID[row][column] == 9:
                color = arcade.color.DARK_YELLOW
            elif GRID[row][column] == 10:
                color = arcade.color.GREEN
            elif GRID[row][column] == 11:
                color = arcade.color.BOTTLE_GREEN
            elif GRID[row][column] == 12:
                color = arcade.color.RED
            elif GRID[row][column] == 13:
                color = arcade.color.BRICK_RED
            elif GRID[row][column] == 14:
                color = arcade.color.DARK_GRAY
            elif GRID[row][column] == 15:
                color = arcade.color.GRAY

            x = (1 + 23.1) * column + 1 + 23.1 // 2
            y = (1 + 23.1) * row + 1 + 23.1 // 2
            arcade.draw_rectangle_filled(x, y, 23.1, 23.1, color)

            #rows
            for c in range(1,4):
                GRID[2][c] = 1
            for c in range(5,9):
                GRID[2][c] = 1
            for c in range(10,20):
                GRID[2][c] = 1
            for c in range(1,3):
                GRID[4][c] = 1
            for c in range(4,13):
                GRID[4][c] = 1
            for c in range(14,20):
                GRID[4][c] = 1
            for c in range(3,13):
                GRID[6][c] = 1
            for c in range(16,20):
                GRID[6][c] = 1
            for c in range(1,17):
                GRID[8][c] = 1
            for c in range(1,10):
                GRID[11][c] = 1
            for c in range(11,13):
                GRID[11][c] = 1
            for c in range(14,19):
                GRID[11][c] = 1
            for c in range(3,6):
                GRID[13][c] = 1
            for c in range(7,17):
                GRID[13][c] = 1
            for c in range(1,3):
                GRID[15][c] = 1
            for c in range(4,11):
                GRID[15][c] = 1
            for c in range(12,19):
                GRID[15][c] = 1
            for c in range(1,19):
                GRID[17][c] = 1

            # single blocks
            GRID[3][7] = 1
            GRID[5][14] = 1
            GRID[6][1] = 1
            GRID[6][14] = 1
            GRID[8][18] = 1
            GRID[9][4] = 1
            GRID[9][8] = 1
            GRID[9][11] = 1
            GRID[9][16] = 1
            GRID[10][2] = 1
            GRID[10][6] = 1
            GRID[10][14] = 1
            GRID[12][11] = 1
            GRID[13][1] = 1
            GRID[13][18] = 1
            GRID[14][4] = 1

            # teleporter blocks
            GRID[1][18] = 4
            GRID[18][1] = 4
            GRID[5][1] = 5
            GRID[10][1] = 5
            GRID[5][18] = 6
            GRID[3][18] = 6
            GRID[16][1] = 7
            GRID[16][18] = 7

        player2()
        gate()
        key()

    arcade.draw_text("LEVEL 2", 545, 400, arcade.color.RED, 20)

def on_update(delta_time):
    global timer
    timer += delta_time

def gate():
    global GRID, row, column, player_column, player_row, key_get_1, gate_open_1, gate_open_2, key_get_2, level2
    if level2 == 0:
        # level 1 gates
        if key_get_1 > 0 and player_column == 7 and player_row == 11:
            GRID[11][7] = 2
            gate_open_1 += 1
        if gate_open_1 > 0:
            GRID[11][7] = 2
        else:
            GRID[11][7] = 5
        if key_get_2 > 0 and player_column == 12 and player_row == 13:
            GRID[13][12] = 2
            gate_open_2 += 1
        if gate_open_2 > 0:
            GRID[13][12] = 2
        else:
            GRID[13][12] = 7

    if level2 == 1:
        # level 2 gates
        GRID[1][11] = 8
        GRID[10][8] = 10
        GRID[6][15] = 12
        GRID[13][17] = 14


def key():
    global GRID, row, column, open, player_column, player_row, key_get_1, gate_open_1, open2, key_get_2
    if level2 == 0:
        GRID[9][3] = 6
        GRID[10][9] = 8
        open = False
        open2 = False
        if player_column == 3 and player_row == 9:
            GRID[9][3] = 2
            key_get_1 += 1
        if key_get_1 > 0:
            open = True

        if player_column == 9 and player_row == 10:
            GRID[10][9] = 2
            key_get_2 += 1
        if key_get_2 > 0:
            open2 = True

    if level2 == 1:
        GRID[3][14] = 9
        GRID[5][8] = 11
        GRID[11][13] = 13
        GRID[16][14] = 15



def on_key_press(key, modifiers):
    global column, row, player_row, player_column, key_get_1, win, gate_open_1, key_get_2, gate_open_2, row2, column2, GRID, level2
    if level2 == 0:
        if key == arcade.key.D and GRID[row][column+1] != 1 and column != 14 and GRID[row][column+1] != 2 and GRID[row][column+1] != 7:
            player_column += 1
            column += 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row][column-1] = 2
        if key == arcade.key.W and GRID[row+1][column] != 1 and GRID[row+1][column] != 5 and GRID[row+1][column] != 2:
            player_row += 1
            row += 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row-1][column] = 2
        if key == arcade.key.S and GRID[row-1][column] != 1 and GRID[row-1][column] != 5 and GRID[row-1][column] != 2:
            player_row -= 1
            row -= 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row+1][column] = 2
        if (key == arcade.key.A and GRID[row][column-1] != 1) and GRID[row][column-1] != 2 and not (key == arcade.key.A and player_row == 1 and player_column == 0):
            player_column -= 1
            column -= 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row][column+1] = 2
        if key == arcade.key.K:
            player_row = 1
            player_column = 0
            for i in range(len(grid_row)):
                for j in range(len(grid_column)):
                    GRID[grid_row[i]][grid_column[j]] = 0
            if GRID[row][column] == 2:
                GRID[row][column] = 0
            GRID[9][3] = 6
            GRID[10][9] = 8
            key_get_1 = 0
            key_get_2 = 0
            gate_open_1 = 0
            gate_open_2 = 0
            GRID[11][7] = 5
            GRID[13][12] = 7
            win = 0
        if key == arcade.key.P:
            player_row = 13
            player_column = 13

    if level2 == 1 and win == 2:
        if key == arcade.key.D and GRID[row][column+1] != 1 and column != 19 and GRID[row][column+1] != 2:
            player_column += 1
            column += 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row][column-1] = 2
        if key == arcade.key.W and GRID[row+1][column] != 1 and GRID[row+1][column] != 2:
            player_row += 1
            row += 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row-1][column] = 2
        if key == arcade.key.S and GRID[row-1][column] != 1 and GRID[row-1][column] != 2:
            player_row -= 1
            row -= 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row+1][column] = 2
        if (key == arcade.key.A and GRID[row][column-1] != 1) and GRID[row][column-1] != 2 and not (key == arcade.key.A and player_row == 1 and player_column == 0):
            player_column -= 1
            column -= 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row][column+1] = 2
        if key == arcade.key.K:
            player_row = 1
            player_column = 0
            for i in range(len(grid_row)):
                for j in range(len(grid_column)):
                    GRID[grid_row[i]][grid_column[j]] = 0
            if GRID[row][column] == 2:
                GRID[row][column] = 0


def on_key_release(arcade_key_d, modifiers):
    global column, row, player_row, player_column
    pass

def level2setup():
    global row, column, GRID
    print("help")
    for row in range(20):
        GRID.append([])
        for column in range(21):
             GRID[row].append(0)

def setup():
    global GRID, row, column, row2, column2


    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)

    arcade.schedule(on_update, 1 / 60)

    arcade.start_render()
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_update = on_update


    for row in range(ROW_COUNT):
        GRID.append([])
        for column in range(COLUMN_COUNT):
            GRID[row].append(0)
    arcade.run()

if __name__ == '__main__':
    setup()