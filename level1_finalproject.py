import arcade
# create the dimensions of all elements of the grid for the first level
WIDTH = 30
HEIGHT= 30
MARGIN = 2
ROW_COUNT = 15
COLUMN_COUNT = 16
GRID = []
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN + 200
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
# create variables based on the player's progress in the level
player_row = 1
player_column = 0
grid_row = []
grid_column = []
key_get_1 = 0
key_get_2 = 0
key_get_3 = 0
key_get_4 = 0
gate_open_1 = 0
gate_open_2 = 0
gate_open_3 = 0
gate_open_4 = 0
win = 0
# create a variable that determines which level the game is on the timer between levels
level2 = 0
timer = 0
# create a function for the player for the first level
def player():
    global GRID, x, y, color, row, column, player_row, player_column, open1, open2, gate_open_1, gate_open_2, win, level2, key_get_1, key_get_2, timer, HEIGHT, WIDTH, MARGIN
    if level2 == 0:
        row = player_row
        column = player_column
        GRID[row][column] = 2
        arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
        if player_column == 14 and player_row == 13:
            win += 1

        if win == 0:
            # teleporters
            if player_column == 7 and player_row == 3:
                player_column = 3
                player_row = 4
                arcade.play_sound(teleport_sound)
                GRID[3][3] = 1
                GRID[3][7] = 1
            if player_column == 3 and player_row == 3:
                player_column = 7
                player_row = 4
                arcade.play_sound(teleport_sound)
                GRID[3][3] = 1
                GRID[3][7] = 1

            # gates
            if open1 == True and gate_open_1 == 0:
                GRID[9][3] = 2
                GRID[11][7] = 0
            if open1 == True and gate_open_1 > 0:
                GRID[11][7] = 2
                GRID[9][3] = 2
            if open2 == True and gate_open_2 == 0:
                GRID[10][9] = 2
                GRID[13][12] = 0
            if open2 == True and gate_open_2 > 0:
                GRID[10][9] = 2
                GRID[13][12] = 2

            # key grabbing
            if (player_row == 9 and player_column == 3) and GRID[player_row-1][player_column] == 2:
                player_row = 10
                row = player_row
            if (player_row == 9 and player_column == 3) and GRID[player_row+1][player_column] == 2:
                player_row = 8
                row = player_row
            if (player_row == 10 and player_column == 9) and GRID[player_row][player_column+1] == 2:
                player_column = 8
                column = player_column
            if (player_row == 10 and player_column == 9) and GRID[player_row][player_column-1] == 2:
                player_column = 10
                column = player_column

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
            open1 = False
            key_get_1 = 0
            key_get_2 = 0
            gate_open_1 = 0
            gate_open_2 = 0
            GRID[11][7] = 5
            GRID[13][12] = 7
            HEIGHT = 23.1
            WIDTH = 23.1
            MARGIN = 1
            grid_reset()
            arcade.draw_rectangle_filled(400, 300, 1200, 600, arcade.color.BLACK)
            arcade.play_sound(complete)
            level2setup()
            timer = 0
            level2 = 1

def player2():
    global level2, player_column, player_row, row, column, GRID, win, open1, open2, open3, open4, gate_open_1, gate_open_2, gate_open_3, gate_open_4, key_get_1, key_get_2, key_get_3, key_get_4
    if level2 == 1:
        row = player_row
        column = player_column
        GRID[row][column] = 2
        arcade.draw_rectangle_filled(x, y, 23.1, 23.1, color)

        if win == 2:
            # teleporter 1
            if player_row == 1 and player_column == 18:
                player_row = 18
                player_column = 2
                arcade.play_sound(teleport_sound)
                GRID[1][18] = 1
                GRID[18][1] = 1
            # teleporter 2
            if player_row == 5 and player_column == 1:
                player_row = 9
                player_column = 1
                arcade.play_sound(teleport_sound)
                GRID[5][1] = 1
                GRID[10][1] = 1
            if player_row == 10 and player_column == 1:
                player_row = 5
                player_column = 2
                arcade.play_sound(teleport_sound)
                GRID[5][1] = 1
                GRID[10][1] = 1
            # teleporter 3
            if player_row == 5 and player_column == 18:
                player_row = 3
                player_column = 17
                arcade.play_sound(teleport_sound)
                GRID[5][18] = 1
                GRID[3][18] = 1
            if player_row == 3 and player_column == 18:
                player_row = 5
                player_column = 17
                arcade.play_sound(teleport_sound)
                GRID[5][18] = 1
                GRID[3][18] = 1
            # teleporter 4
            if player_row == 16 and player_column == 1:
                player_row = 16
                player_column = 17
                arcade.play_sound(teleport_sound)
                GRID[16][1] = 1
                GRID[16][18] = 1
            if player_row == 16 and player_column == 18:
                player_row = 16
                player_column = 2
                arcade.play_sound(teleport_sound)
                GRID[16][1] = 1
                GRID[16][18] = 1

            # gates
            if open1 == True and gate_open_1 == 0:
                GRID[3][15] = 2
                GRID[1][11] = 0
            if open1 == True and gate_open_1 > 0:
                GRID[3][15] = 2
                GRID[1][11] = 2
            if open2 == True and gate_open_2 == 0:
                GRID[5][8] = 2
                GRID[10][8] = 0
            if open2 == True and gate_open_2 > 0:
                GRID[5][8] = 2
                GRID[10][8] = 2
            if open3 == True and gate_open_3 == 0:
                GRID[11][13] = 2
                GRID[6][15] = 0
            if open3 == True and gate_open_3 > 0:
                GRID[11][13] = 2
                GRID[6][15] = 2
            if open4 == True and gate_open_4 == 0:
                GRID[16][14] = 2
                GRID[13][17] = 0
            if open4 == True and gate_open_4 > 0:
                GRID[16][14] = 2
                GRID[13][17] = 2

            # key grabbing as to not cause key audio to play on repeat
            # key 1
            if (player_row == 3 and player_column == 15) and GRID[player_row][player_column-1] == 2:
                player_column = 16
                column = player_column
            if (player_row == 3 and player_column == 15) and GRID[player_row][player_column+1] == 2:
                player_column = 14
                column = player_column
            # key 2
            if (player_row == 5 and player_column == 8) and GRID[player_row][player_column-1] == 2:
                player_column = 9
                column = player_column
            if (player_row == 5 and player_column == 8) and GRID[player_row][player_column+1] == 2:
                player_column = 7
                column = player_column
            # key 3
            if (player_row == 11 and player_column == 13) and GRID[player_row+1][player_column] == 2:
                player_row = 10
                row = player_row
            if (player_row == 11 and player_column == 13) and GRID[player_row-1][player_column] == 2:
                player_row = 12
                row = player_row
            # key 4
            if (player_row == 16 and player_column == 14) and GRID[player_row][player_column-1] == 2:
                player_column = 15
                column = player_column
            if (player_row == 16 and player_column == 14) and GRID[player_row][player_column+1] == 2:
                player_column = 13
                column = player_column

        if player_column == 19 and player_row == 18:
            arcade.play_sound(complete)
            player_row = 19

        if player_column == 19 and player_row == 19:
            win = 3


def grid_reset():
    global GRID, grid_row, grid_column, row
    GRID = []
    grid_row = []
    grid_column = []

def on_draw():
    global GRID, color, column, row, x, y, win, level2, timer
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
                    for r in range(2, 7):
                        GRID[r][4] = 1
                    for r in range(2, 8):
                        GRID[r][6] = 1
                        GRID[r][8] = 1
                    for r in range(2, 10):
                        GRID[r][10] = 1
                    for r in range(2, 12):
                        GRID[r][12] = 1
                    for r in range(7, 13):
                        GRID[r][2] = 1
                    for r in range(9, 12):
                        GRID[r][4] = 1
                        GRID[r][6] = 1
                    for c in range(2, 5):
                        GRID[2][c] = 1
                        GRID[7][c] = 1
                    for c in range(6, 9):
                        GRID[2][c] = 1
                    for c in range(6, 10):
                        GRID[9][c] = 1
                    for c in range(8, 12):
                        GRID[11][c] = 1
                    for c in range(12, 14):
                        GRID[12][c] = 1

                    GRID[3][7] = 4
                    GRID[3][3] = 4
        if win == 0:
            key()
            gate()
            player()

    arcade.draw_rectangle_filled(525, 150, 30, 30, arcade.color.BOTTLE_GREEN)
    arcade.draw_rectangle_filled(675, 150, 30, 30, arcade.color.GREEN)
    arcade.draw_text("unlocks", 567, 145, arcade.color.WHITE, 13)

    arcade.draw_rectangle_filled(525, 100, 30, 30, arcade.color.DARK_YELLOW)
    arcade.draw_rectangle_filled(675, 100, 30, 30, arcade.color.YELLOW)
    arcade.draw_text("unlocks", 567, 95, arcade.color.WHITE, 13)

    arcade.draw_rectangle_filled(525, 50, 30, 30, arcade.color.BLUEBERRY)
    arcade.draw_rectangle_filled(675, 50, 30, 30, arcade.color.BLUEBERRY)
    arcade.draw_text("teleporters", 555, 45, arcade.color.WHITE, 13)

    arcade.draw_text("LEVEL 1", 550, 420, arcade.color.RED, 20)

    arcade.draw_line(500, 75, 700, 75, arcade.color.WHITE, 7)
    arcade.draw_line(500, 210, 700, 210, arcade.color.WHITE, 7)

    arcade.draw_text("Keys:", 505, 180, arcade.color.WHITE, 12)
    arcade.draw_text("Gates:", 650, 180, arcade.color.WHITE, 12)

    arcade.draw_text("W: Move Up", 545, 340, arcade.color.WHITE, 12)
    arcade.draw_text("A: Move Left", 545, 320, arcade.color.WHITE, 12)
    arcade.draw_text("S: Move Down", 545, 300, arcade.color.WHITE, 12)
    arcade.draw_text("D: Move Right", 545, 280, arcade.color.WHITE, 12)
    arcade.draw_text("K: Reset Level", 545, 260, arcade.color.WHITE, 12)

    arcade.draw_rectangle_filled(550, 385, 30, 30, arcade.color.BLUE)
    arcade.draw_text("Player", 580, 382, arcade.color.WHITE, 12)

    arcade.draw_text("You can't move past your own line", 495, 230, arcade.color.YELLOW, 12)

    if level2 == 1:
        arcade.draw_rectangle_filled(400, 300, 1200, 600, arcade.color.BLACK)
        arcade.draw_text("LEVEL 1 COMPLETE!!!", 135, 250, arcade.color.WHITE, 30)
        if timer > 4:
            win = 2
            arcade.draw_rectangle_filled(400, 300, 1200, 600, arcade.color.BLACK)
            second_draw()

def second_draw():
    global GRID, row, column, color, level2, x, y, win
    for row in range(20):
        for column in range(21):
            if row == 0 or row == 19 or (column == 0 and row != 1) or (column == 19 and row != 18):
                GRID[row][column] = 1
            if column == 20:
                GRID[row][column] = 3

            # list all possible variables and the corresponding color
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
                color = arcade.color.RUBY_RED
            elif GRID[row][column] == 14:
                color = arcade.color.DARK_GRAY
            elif GRID[row][column] == 15:
                color = arcade.color.GRAY

            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
            y = (MARGIN + WIDTH) * row + MARGIN + WIDTH // 2
            arcade.draw_rectangle_filled(x, y, HEIGHT, WIDTH, color)

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

    key()
    gate()
    player2()

    arcade.draw_text("LEVEL 2", 545, 400, arcade.color.RED, 25)

    arcade.draw_rectangle_filled(525, 310, 20, 20, arcade.color.BOTTLE_GREEN)
    arcade.draw_rectangle_filled(675, 310, 20, 20, arcade.color.GREEN)
    arcade.draw_text("unlocks", 570, 307, arcade.color.WHITE, 12)

    arcade.draw_rectangle_filled(525, 280, 20, 20, arcade.color.DARK_YELLOW)
    arcade.draw_rectangle_filled(675, 280, 20, 20, arcade.color.YELLOW)
    arcade.draw_text("unlocks", 570, 277, arcade.color.WHITE, 12)

    arcade.draw_rectangle_filled(525, 250, 20, 20, arcade.color.RUBY_RED)
    arcade.draw_rectangle_filled(675, 250, 20, 20, arcade.color.RED)
    arcade.draw_text("unlocks", 570, 247, arcade.color.WHITE, 12)

    arcade.draw_rectangle_filled(525, 220, 20, 20, arcade.color.GRAY)
    arcade.draw_rectangle_filled(675, 220, 20, 20, arcade.color.DARK_GRAY)
    arcade.draw_text("unlocks", 570, 217, arcade.color.WHITE, 12)

    arcade.draw_rectangle_filled(525, 175, 25, 25, arcade.color.BLUEBERRY)
    arcade.draw_rectangle_filled(675, 175, 25, 25, arcade.color.BLUEBERRY)

    arcade.draw_rectangle_filled(525, 140, 25, 25, arcade.color.VIOLET_RED)
    arcade.draw_rectangle_filled(675, 140, 25, 25, arcade.color.VIOLET_RED)

    arcade.draw_rectangle_filled(525, 105, 25, 25, arcade.color.INDIGO)
    arcade.draw_rectangle_filled(675, 105, 25, 25, arcade.color.INDIGO)

    arcade.draw_rectangle_filled(525, 70, 25, 25, arcade.color.PURPLE_PIZZAZZ)
    arcade.draw_rectangle_filled(675, 70, 25, 25, arcade.color.PURPLE_PIZZAZZ)

    arcade.draw_text("teleporters", 560, 120, arcade.color.WHITE, 13)

    arcade.draw_line(500, 200, 700, 200, arcade.color.WHITE, 7)
    arcade.draw_line(500, 350, 700, 350, arcade.color.WHITE, 7)

    arcade.draw_text("Keys:", 512, 330, arcade.color.WHITE, 10)
    arcade.draw_text("Gates:", 660, 330, arcade.color.WHITE, 10)

    if win == 3:
        arcade.draw_rectangle_filled(400, 300, 1200, 1200, arcade.color.BLACK)
        arcade.draw_text("CONGRATULATIONS!", 120, 250, arcade.color.WHITE, 40)


def on_update(delta_time):
    global timer
    timer += delta_time

def gate():
    global GRID, row, column, player_column, player_row, key_get_1, key_get_2, key_get_3, key_get_4, gate_open_1, gate_open_2, gate_open_3, gate_open_4, level2
    if level2 == 0:
        # level 1 gates
        if key_get_1 > 0 and player_column == 7 and player_row == 11:
            gate_open_1 += 1
        if gate_open_1 > 0:
            GRID[11][7] = 2
        else:
            GRID[11][7] = 5
        if key_get_2 > 0 and player_column == 12 and player_row == 13:
            gate_open_2 += 1
        if gate_open_2 > 0:
            GRID[13][12] = 2
        else:
            GRID[13][12] = 7

    if level2 == 1:
        # level 2 gates
        if key_get_1 > 0 and player_column == 11 and player_row == 1:
            gate_open_1 += 1
        if gate_open_1 > 0:
            GRID[1][11] = 2
        else:
            GRID[1][11] = 8
        if key_get_2 > 0 and player_column == 8 and player_row == 10:
            gate_open_2 += 1
        if gate_open_2 > 0:
            GRID[10][8] = 2
        else:
            GRID[10][8] = 10
        if key_get_3 > 0 and player_column == 15 and player_row == 6:
            gate_open_3 += 1
        if gate_open_3 > 0:
            GRID[6][15] = 2
        else:
            GRID[6][15] = 12
        if key_get_4 > 0 and player_column == 17 and player_row == 13:
            gate_open_4 += 1
        if gate_open_4 > 0:
            GRID[13][17] = 2
        else:
            GRID[13][17] = 14

def key():
    global GRID, row, column, open1, open2, open3, open4, player_column, player_row, key_get_1, key_get_2, key_get_3, key_get_4, key_sound
    if level2 == 0:
        GRID[9][3] = 6
        GRID[10][9] = 8
        open1 = False
        open2 = False

        if player_column == 3 and player_row == 9:
            GRID[9][3] = 2
            key_get_1 += 1
            arcade.play_sound(key_sound)
        if key_get_1 > 0:
            open1 = True

        if player_column == 9 and player_row == 10:
            GRID[10][9] = 2
            key_get_2 += 1
            arcade.play_sound(key_sound)
        if key_get_2 > 0:
            open2 = True

    if level2 == 1:
        GRID[3][15] = 9
        GRID[5][8] = 11
        GRID[11][13] = 13
        GRID[16][14] = 15
        open1 = False
        open2 = False
        open3 = False
        open4 = False

        if player_row == 3 and player_column == 15:
            GRID[3][15] = 2
            key_get_1 += 1
            arcade.play_sound(key_sound)
        if key_get_1 > 0:
            open1 = True

        if player_row == 5 and player_column == 8:
            GRID[5][8] = 2
            key_get_2 += 1
            arcade.play_sound(key_sound)
        if key_get_2 > 0:
            open2 = True

        if player_row == 11 and player_column == 13:
            GRID[11][13] = 2
            key_get_3 += 1
            arcade.play_sound(key_sound)
        if key_get_3 > 0:
            open3 = True

        if player_row == 16 and player_column == 14:
            GRID[16][14] = 2
            key_get_4 += 1
            arcade.play_sound(key_sound)
        if key_get_4 > 0:
            open4 = True

def on_key_press(key, modifiers):
    global column, row, player_row, player_column, key_get_1, key_get_2, key_get_3, key_get_4, win, gate_open_1, gate_open_2, gate_open_3, gate_open_4, level2
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
        # reset button
        if key == arcade.key.K:
            # reset player position
            player_row = 1
            player_column = 0
            # resetting around the keys
            GRID[10][3] = 0
            GRID[8][3] = 0
            GRID[10][8] = 0
            GRID[10][10] = 0
            # resetting the path of the player
            for i in range(len(grid_row)):
                for j in range(len(grid_column)):
                    GRID[grid_row[i]][grid_column[j]] = 0
            if GRID[row][column] == 2:
                GRID[row][column] = 0
            # resetting all key and gate values
            key_get_1 = 0
            key_get_2 = 0
            gate_open_1 = 0
            gate_open_2 = 0
            GRID[9][3] = 6
            GRID[10][9] = 8
            GRID[11][7] = 5
            GRID[13][12] = 7
            win = 0

    if level2 == 1 and win == 2:
        if key == arcade.key.D and GRID[row][column+1] != 1 and column != 19 and GRID[row][column+1] != 2 and GRID[row][column+1] != 8 and GRID[row][column+1] != 10:
            player_column += 1
            column += 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row][column-1] = 2
        if key == arcade.key.W and GRID[row+1][column] != 1 and GRID[row+1][column] != 2 and GRID[row+1][column] != 12 and GRID[row+1][column] != 14:
            player_row += 1
            row += 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row-1][column] = 2
        if key == arcade.key.S and GRID[row-1][column] != 1 and GRID[row-1][column] != 2 and GRID[row-1][column] != 12 and GRID[row-1][column] != 14:
            player_row -= 1
            row -= 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row+1][column] = 2
        if (key == arcade.key.A and GRID[row][column-1] != 1) and GRID[row][column-1] != 2 and GRID[row][column-1] != 8 and GRID[row][column-1] != 10 and not (key == arcade.key.A and player_row == 1 and player_column == 0):
            player_column -= 1
            column -= 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row][column+1] = 2
        if key == arcade.key.K:
            player_row = 1
            player_column = 0
            # resetting keys
            GRID[3][14] = 0
            GRID[3][16] = 0
            GRID[5][7] = 0
            GRID[5][9] = 0
            GRID[10][13] = 0
            GRID[12][13] = 0
            GRID[16][13] = 0
            GRID[16][15] = 0
            for i in range(len(grid_row)):
                for j in range(len(grid_column)):
                    GRID[grid_row[i]][grid_column[j]] = 0
            if GRID[row][column] == 2:
                GRID[row][column] = 0
            key_get_1 = 0
            key_get_2 = 0
            key_get_3 = 0
            key_get_4 = 0
            gate_open_1 = 0
            gate_open_2 = 0
            gate_open_3 = 0
            gate_open_4 = 0
            GRID[3][15] = 9
            GRID[5][8] = 11
            GRID[11][13] = 13
            GRID[16][14] = 15
            GRID[1][11] = 8
            GRID[10][8] = 10
            GRID[6][15] = 12
            GRID[13][17] = 14

def level2setup():
    global row, column, GRID, timer, background_sound
    for row in range(20):
        GRID.append([])
        for column in range(21):
             GRID[row].append(0)

def setup():
    global GRID, row, column, key_sound, teleport_sound, complete

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Game")
    # level 1 setup
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

    key_sound = arcade.load_sound("sounds/keysound.wav")
    teleport_sound = arcade.load_sound("sounds/teleport.wav")
    complete = arcade.load_sound("sounds/complete.wav")

    arcade.run()

if __name__ == '__main__':
    setup()
