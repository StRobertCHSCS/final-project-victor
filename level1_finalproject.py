# ------------------------------------------------------------------------
# Name: final_project.py
#
# Purpose: Create a two-level puzzle game where the player needs to go
# from one end of a maze to the other
#
# Author: Victor Lisita
#
# Date: 06-18-2019
# ------------------------------------------------------------------------
# import the arcade system
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
# create variables for the keys
key_get_1 = 0
key_get_2 = 0
key_get_3 = 0
key_get_4 = 0
# create variables for whether or not the gates are open
gate_open_1 = 0
gate_open_2 = 0
gate_open_3 = 0
gate_open_4 = 0
#create a variable for when the player beats the level
win = 0

# create a variable that determines which level the game is on the timer between levels
level2 = 0
timer = 0

def player():
    """Defines the abilities of the player for the first level"""
    # assign global variables
    global GRID, x, y, color, row, column, player_row, player_column, open1, open2, gate_open_1, gate_open_2, win, level2, key_get_1, key_get_2, timer, HEIGHT, WIDTH, MARGIN
        # assign this code to run only if it is in the first level
        if level2 == 0:
            # make the player have a unique grid variable to identify where it is
            row = player_row
            column = player_column
            GRID[row][column] = 2
            arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
            # tell the code that the level has been beaten when the player reaches a certain point
            if player_column == 14 and player_row == 13:
                win += 1
            # create code that allows the player to interact with the gates, keys, and teleporters
            if win == 0:
                # code for the teleporter interaction
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

                # code for the gate interaction so that the gate square becomes the appropriate colour when the player crosses it
                # yellow gate
                if open1 == True and gate_open_1 == 0:
                    GRID[9][3] = 2
                    GRID[11][7] = 0
                if open1 == True and gate_open_1 > 0:
                    GRID[11][7] = 2
                    GRID[9][3] = 2
                # green gate
                if open2 == True and gate_open_2 == 0:
                    GRID[10][9] = 2
                    GRID[13][12] = 0
                if open2 == True and gate_open_2 > 0:
                    GRID[10][9] = 2
                    GRID[13][12] = 2

                # code that moves the player when it grabs a key so that the key sound will not constantly play
                # yellow key
                if (player_row == 9 and player_column == 3) and GRID[player_row-1][player_column] == 2:
                    player_row = 10
                    row = player_row
                if (player_row == 9 and player_column == 3) and GRID[player_row+1][player_column] == 2:
                    player_row = 8
                    row = player_row
                # green key
                if (player_row == 10 and player_column == 9) and GRID[player_row][player_column+1] == 2:
                    player_column = 8
                    column = player_column
                if (player_row == 10 and player_column == 9) and GRID[player_row][player_column-1] == 2:
                    player_column = 10
                    column = player_column
            # create code for when the player does finish the level
            if win == 1:
                # reset the player position
                player_row = 1
                player_column = 0
                # remove the player path
                for i in range(len(grid_row)):
                    for j in range(len(grid_column)):
                        GRID[grid_row[i]][grid_column[j]] = 0
                if GRID[row][column] == 2:
                    GRID[row][column] = 0
                # reset the keys and gates and their relative functions
                GRID[9][3] = 6
                GRID[10][9] = 8
                open1 = False
                key_get_1 = 0
                key_get_2 = 0
                gate_open_1 = 0
                gate_open_2 = 0
                GRID[11][7] = 5
                GRID[13][12] = 7
                # change the height, width and margin of the grid squares for the next level
                HEIGHT = 23.1
                WIDTH = 23.1
                MARGIN = 1
                # reset the grid values
                grid_reset()
                # create a large square to cover up the previous level
                arcade.draw_rectangle_filled(400, 300, 1200, 600, arcade.color.BLACK)
                # play a victory sound
                arcade.play_sound(complete)
                # activate the setup of the next level
                level2setup()
                timer = 0
                level2 = 1

def player2():
    """Defines the abilities of the player in the second level"""
    # define global variables
    global level2, player_column, player_row, row, column, GRID, win, open1, open2, open3, open4, gate_open_1, gate_open_2, gate_open_3, gate_open_4, key_get_1, key_get_2, key_get_3, key_get_4
    # set to code to run only when the second level is being played
    if level2 == 1:
        row = player_row
        column = player_column
        GRID[row][column] = 2
        arcade.draw_rectangle_filled(x, y, 23.1, 23.1, color)

        # create code for how the player interacts with teleporters, key and gates
        if win == 2:
            # blue teleporter interaction
            if player_row == 1 and player_column == 18:
                player_row = 18
                player_column = 2
                arcade.play_sound(teleport_sound)
                GRID[1][18] = 1
                GRID[18][1] = 1
            # pink teleporter interaction
            # lower entrance
            if player_row == 5 and player_column == 1:
                player_row = 9
                player_column = 1
                arcade.play_sound(teleport_sound)
                GRID[5][1] = 1
                GRID[10][1] = 1
            # upper entrance
            if player_row == 10 and player_column == 1:
                player_row = 5
                player_column = 2
                arcade.play_sound(teleport_sound)
                GRID[5][1] = 1
                GRID[10][1] = 1
            # indigo teleporter interaction
            # upper entrance
            if player_row == 5 and player_column == 18:
                player_row = 3
                player_column = 17
                arcade.play_sound(teleport_sound)
                GRID[5][18] = 1
                GRID[3][18] = 1
            # lower entrance
            if player_row == 3 and player_column == 18:
                player_row = 5
                player_column = 17
                arcade.play_sound(teleport_sound)
                GRID[5][18] = 1
                GRID[3][18] = 1
            # lavender teleporter interaction
            # left entrance
            if player_row == 16 and player_column == 1:
                player_row = 16
                player_column = 17
                arcade.play_sound(teleport_sound)
                GRID[16][1] = 1
                GRID[16][18] = 1
            # right entrance
            if player_row == 16 and player_column == 18:
                player_row = 16
                player_column = 2
                arcade.play_sound(teleport_sound)
                GRID[16][1] = 1
                GRID[16][18] = 1

            # interaction with gates to have the appropriate color when the player crosses it
            # yellow gate
            if open1 == True and gate_open_1 == 0:
                GRID[3][15] = 2
                GRID[1][11] = 0
            if open1 == True and gate_open_1 > 0:
                GRID[3][15] = 2
                GRID[1][11] = 2
            # green gate
            if open2 == True and gate_open_2 == 0:
                GRID[5][8] = 2
                GRID[10][8] = 0
            if open2 == True and gate_open_2 > 0:
                GRID[5][8] = 2
                GRID[10][8] = 2
            # red gate
            if open3 == True and gate_open_3 == 0:
                GRID[11][13] = 2
                GRID[6][15] = 0
            if open3 == True and gate_open_3 > 0:
                GRID[11][13] = 2
                GRID[6][15] = 2
            # gray gate
            if open4 == True and gate_open_4 == 0:
                GRID[16][14] = 2
                GRID[13][17] = 0
            if open4 == True and gate_open_4 > 0:
                GRID[16][14] = 2
                GRID[13][17] = 2

            # interaction with keys to make the player move forward afterwards as to not cause the key sound to constantly play
            # yellow key
            if (player_row == 3 and player_column == 15) and GRID[player_row][player_column-1] == 2:
                player_column = 16
                column = player_column
            if (player_row == 3 and player_column == 15) and GRID[player_row][player_column+1] == 2:
                player_column = 14
                column = player_column
            # green key
            if (player_row == 5 and player_column == 8) and GRID[player_row][player_column-1] == 2:
                player_column = 9
                column = player_column
            if (player_row == 5 and player_column == 8) and GRID[player_row][player_column+1] == 2:
                player_column = 7
                column = player_column
            # red key
            if (player_row == 11 and player_column == 13) and GRID[player_row+1][player_column] == 2:
                player_row = 10
                row = player_row
            if (player_row == 11 and player_column == 13) and GRID[player_row-1][player_column] == 2:
                player_row = 12
                row = player_row
            # gray key
            if (player_row == 16 and player_column == 14) and GRID[player_row][player_column-1] == 2:
                player_column = 15
                column = player_column
            if (player_row == 16 and player_column == 14) and GRID[player_row][player_column+1] == 2:
                player_column = 13
                column = player_column

        # have the player complete the level when reaching a certain point
        if player_column == 19 and player_row == 18:
            arcade.play_sound(complete)
            player_row = 19
        # create a change of the player's position to prevent the completion sound from constantly playing
        if player_column == 19 and player_row == 19:
            win = 3


def grid_reset():
    """Resets all grid-related variables"""
    # create global variables
    global GRID, grid_row, grid_column, row
    # reset grid-related variables
    GRID = []
    grid_row = []
    grid_column = []

def on_draw():
    """Draws the main level and the transition to the second level"""
    # create global variables
    global GRID, color, column, row, x, y, win, level2, timer
    # set the code for it only to run during the first level and before the player has won
    if level2 == 0:
        if win == 0:
            # create code that allows every square in the grid to be changed
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    # set variables for the walls in the grid
                    if row == 0 or row == 14 or (column == 0 and row != 1) or (column == 14 and row != 13):
                        GRID[row][column] = 1
                    if column == 15:
                        GRID[row][column] = 3
                    # set each variable to a specific color
                    # floor
                    if GRID[row][column] == 0:
                        color = arcade.color.BLACK
                    # walls
                    elif GRID[row][column] == 1:
                        color = arcade.color.PURPLE
                    # player and its trail
                    elif GRID[row][column] == 2:
                        color = arcade.color.BLUE
                    # invisible wall past the finishing point
                    elif GRID[row][column] == 3:
                        color = arcade.color.BLACK
                    # teleporter
                    elif GRID[row][column] == 4:
                        color = arcade.color.BLUEBERRY
                    # yellow gate
                    elif GRID[row][column] == 5:
                        color = arcade.color.YELLOW
                    # yellow key
                    elif GRID[row][column] == 6:
                        color = arcade.color.DARK_YELLOW
                    # green gate
                    elif GRID[row][column] == 7:
                        color = arcade.color.GREEN
                    # green key
                    elif GRID[row][column] == 8:
                        color = arcade.color.BOTTLE_GREEN

                    # set a size for each square in the grid
                    x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                    y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                    arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

                    # set up the columns of walls within the grid
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
                    # set up the rows of walls within the grid
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
                    # identify the teleporter entrance and exit
                    GRID[3][7] = 4
                    GRID[3][3] = 4
        # create an if statement to activate keys, gates, and the player to run before the player has beaten the level
        if win == 0:
            key()
            gate()
            player()

    # create information text to assist the player
    # green key and gate info
    arcade.draw_rectangle_filled(525, 150, 30, 30, arcade.color.BOTTLE_GREEN)
    arcade.draw_rectangle_filled(675, 150, 30, 30, arcade.color.GREEN)
    arcade.draw_text("unlocks", 567, 145, arcade.color.WHITE, 13)
    # yellow key and gate info
    arcade.draw_rectangle_filled(525, 100, 30, 30, arcade.color.DARK_YELLOW)
    arcade.draw_rectangle_filled(675, 100, 30, 30, arcade.color.YELLOW)
    arcade.draw_text("unlocks", 567, 95, arcade.color.WHITE, 13)
    # teleporter info
    arcade.draw_rectangle_filled(525, 50, 30, 30, arcade.color.BLUEBERRY)
    arcade.draw_rectangle_filled(675, 50, 30, 30, arcade.color.BLUEBERRY)
    arcade.draw_text("teleporters", 555, 45, arcade.color.WHITE, 13)
    # level 1 sign
    arcade.draw_text("LEVEL 1", 550, 420, arcade.color.RED, 20)
    # separating line
    arcade.draw_line(500, 75, 700, 75, arcade.color.WHITE, 7)
    arcade.draw_line(500, 210, 700, 210, arcade.color.WHITE, 7)
    # differentiate the key spaces from the gates
    arcade.draw_text("Keys:", 505, 180, arcade.color.WHITE, 12)
    arcade.draw_text("Gates:", 650, 180, arcade.color.WHITE, 12)
    # player controls
    arcade.draw_text("W: Move Up", 545, 340, arcade.color.WHITE, 12)
    arcade.draw_text("A: Move Left", 545, 320, arcade.color.WHITE, 12)
    arcade.draw_text("S: Move Down", 545, 300, arcade.color.WHITE, 12)
    arcade.draw_text("D: Move Right", 545, 280, arcade.color.WHITE, 12)
    arcade.draw_text("K: Reset Level", 545, 260, arcade.color.WHITE, 12)
    # player info
    arcade.draw_rectangle_filled(550, 385, 30, 30, arcade.color.BLUE)
    arcade.draw_text("Player", 580, 382, arcade.color.WHITE, 12)
    # additional gameplay information
    arcade.draw_text("You can't move past your own line", 495, 230, arcade.color.YELLOW, 12)

    # create code for the transition after the player has beaten the level
    if level2 == 1:
        # create a victory screen that covers the old grid
        arcade.draw_rectangle_filled(400, 300, 1200, 600, arcade.color.BLACK)
        arcade.draw_text("LEVEL 1 COMPLETE!!!", 135, 250, arcade.color.WHITE, 30)
        # use the timer to give the player a few seconds before switching levels
        if timer > 4:
            win = 2
            arcade.draw_rectangle_filled(400, 300, 1200, 600, arcade.color.BLACK)
            # launch the code for the second level
            second_draw()

def second_draw():
    """The on_draw function for the second level"""
    # set global variables
    global GRID, row, column, color, level2, x, y, win
    # set up the grid so that every square can be given a variable
    for row in range(20):
        for column in range(21):
            # set up the walls in the grid
            if row == 0 or row == 19 or (column == 0 and row != 1) or (column == 19 and row != 18):
                GRID[row][column] = 1
            if column == 20:
                GRID[row][column] = 3

            # list all possible variables and the corresponding color
            # floor
            if GRID[row][column] == 0:
                color = arcade.color.BLACK
            # walls
            elif GRID[row][column] == 1:
                color = arcade.color.PURPLE
            # player
            elif GRID[row][column] == 2:
                color = arcade.color.BLUE
            # invisible wall at the end of the level
            elif GRID[row][column] == 3:
                color = arcade.color.BLACK
            # blue teleporter
            elif GRID[row][column] == 4:
                color = arcade.color.BLUEBERRY
            # pink teleporter
            elif GRID[row][column] == 5:
                color = arcade.color.VIOLET_RED
            # indigo teleporter
            elif GRID[row][column] == 6:
                color = arcade.color.INDIGO
            # lavendar teleporter
            elif GRID[row][column] == 7:
                color = arcade.color.PURPLE_PIZZAZZ
            # yellow gate
            elif GRID[row][column] == 8:
                color = arcade.color.YELLOW
            # yellow key
            elif GRID[row][column] == 9:
                color = arcade.color.DARK_YELLOW
            # green gate
            elif GRID[row][column] == 10:
                color = arcade.color.GREEN
            # green key
            elif GRID[row][column] == 11:
                color = arcade.color.BOTTLE_GREEN
            # red gate
            elif GRID[row][column] == 12:
                color = arcade.color.RED
            # red key
            elif GRID[row][column] == 13:
                color = arcade.color.RUBY_RED
            # gray gate
            elif GRID[row][column] == 14:
                color = arcade.color.DARK_GRAY
            # gray key
            elif GRID[row][column] == 15:
                color = arcade.color.GRAY

            # create a size for each square in the grid
            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
            y = (MARGIN + WIDTH) * row + MARGIN + WIDTH // 2
            arcade.draw_rectangle_filled(x, y, HEIGHT, WIDTH, color)

            # set up all the rows of walls in the grid
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

            # set up all the individual wall blocks in the grid
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

            # set up all the teleporter blocks
            # blue tele
            GRID[1][18] = 4
            GRID[18][1] = 4
            # pink tele
            GRID[5][1] = 5
            GRID[10][1] = 5
            # indigo tele
            GRID[5][18] = 6
            GRID[3][18] = 6
            # lavendar tele
            GRID[16][1] = 7
            GRID[16][18] = 7

    # activate the functions for the keys, gates, and the level 2 player
    key()
    gate()
    player2()

    # create informative text at the side to aid the player
    # level 2 sign
    arcade.draw_text("LEVEL 2", 545, 400, arcade.color.RED, 25)
    # green key and gate
    arcade.draw_rectangle_filled(525, 310, 20, 20, arcade.color.BOTTLE_GREEN)
    arcade.draw_rectangle_filled(675, 310, 20, 20, arcade.color.GREEN)
    arcade.draw_text("unlocks", 570, 307, arcade.color.WHITE, 12)
    # yellow key and gate
    arcade.draw_rectangle_filled(525, 280, 20, 20, arcade.color.DARK_YELLOW)
    arcade.draw_rectangle_filled(675, 280, 20, 20, arcade.color.YELLOW)
    arcade.draw_text("unlocks", 570, 277, arcade.color.WHITE, 12)
    # red key and gate
    arcade.draw_rectangle_filled(525, 250, 20, 20, arcade.color.RUBY_RED)
    arcade.draw_rectangle_filled(675, 250, 20, 20, arcade.color.RED)
    arcade.draw_text("unlocks", 570, 247, arcade.color.WHITE, 12)
    # gray key and gate
    arcade.draw_rectangle_filled(525, 220, 20, 20, arcade.color.GRAY)
    arcade.draw_rectangle_filled(675, 220, 20, 20, arcade.color.DARK_GRAY)
    arcade.draw_text("unlocks", 570, 217, arcade.color.WHITE, 12)
    # blue teleporters
    arcade.draw_rectangle_filled(525, 175, 25, 25, arcade.color.BLUEBERRY)
    arcade.draw_rectangle_filled(675, 175, 25, 25, arcade.color.BLUEBERRY)
    # pink teleporters
    arcade.draw_rectangle_filled(525, 140, 25, 25, arcade.color.VIOLET_RED)
    arcade.draw_rectangle_filled(675, 140, 25, 25, arcade.color.VIOLET_RED)
    # indigo teleporters
    arcade.draw_rectangle_filled(525, 105, 25, 25, arcade.color.INDIGO)
    arcade.draw_rectangle_filled(675, 105, 25, 25, arcade.color.INDIGO)
    # lavendar teleporters
    arcade.draw_rectangle_filled(525, 70, 25, 25, arcade.color.PURPLE_PIZZAZZ)
    arcade.draw_rectangle_filled(675, 70, 25, 25, arcade.color.PURPLE_PIZZAZZ)
    arcade.draw_text("teleporters", 560, 120, arcade.color.WHITE, 13)
    # draw separating lines
    arcade.draw_line(500, 200, 700, 200, arcade.color.WHITE, 7)
    arcade.draw_line(500, 350, 700, 350, arcade.color.WHITE, 7)
    # differentiate between the keys and gates
    arcade.draw_text("Keys:", 512, 330, arcade.color.WHITE, 10)
    arcade.draw_text("Gates:", 660, 330, arcade.color.WHITE, 10)
    # set up a screen to be placed when the player beats the second level
    if win == 3:
        arcade.draw_rectangle_filled(400, 300, 1200, 1200, arcade.color.BLACK)
        arcade.draw_text("CONGRATULATIONS!", 120, 250, arcade.color.WHITE, 40)


def on_update(delta_time):
    """Make a timer to use for the level transition"""
    # define global variables
    global timer
    # create a functioning timer
    timer += delta_time

def gate():
    """create code that tells the gates to open when a key has been collected"""
    # define global variables
    global GRID, row, column, player_column, player_row, key_get_1, key_get_2, key_get_3, key_get_4, gate_open_1, gate_open_2, gate_open_3, gate_open_4, level2
    # make this specific code run when the player is on the first level
    if level2 == 0:
        # make cases for when the grid spot each gate is on should have a certain variable
        # yellow gate
        if key_get_1 > 0 and player_column == 7 and player_row == 11:
            gate_open_1 += 1
        if gate_open_1 > 0:
            GRID[11][7] = 2
        else:
            GRID[11][7] = 5
        # green gate
        if key_get_2 > 0 and player_column == 12 and player_row == 13:
            gate_open_2 += 1
        if gate_open_2 > 0:
            GRID[13][12] = 2
        else:
            GRID[13][12] = 7

    # make this specific code run when the player is on the second level
    if level2 == 1:
        # make cases for when the grid spot each gate is on should have a certain variable
        # yellow gate
        if key_get_1 > 0 and player_column == 11 and player_row == 1:
            gate_open_1 += 1
        if gate_open_1 > 0:
            GRID[1][11] = 2
        else:
            GRID[1][11] = 8
        # green gate
        if key_get_2 > 0 and player_column == 8 and player_row == 10:
            gate_open_2 += 1
        if gate_open_2 > 0:
            GRID[10][8] = 2
        else:
            GRID[10][8] = 10
        # red gate
        if key_get_3 > 0 and player_column == 15 and player_row == 6:
            gate_open_3 += 1
        if gate_open_3 > 0:
            GRID[6][15] = 2
        else:
            GRID[6][15] = 12
        # gray gate
        if key_get_4 > 0 and player_column == 17 and player_row == 13:
            gate_open_4 += 1
        if gate_open_4 > 0:
            GRID[13][17] = 2
        else:
            GRID[13][17] = 14

def key():
    """
    Create code that assigns keys to a spot and
    activates certain commands when said key is picked up
    """
    # define global variables
    global GRID, row, column, open1, open2, open3, open4, player_column, player_row, key_get_1, key_get_2, key_get_3, key_get_4, key_sound
    # make this specific code run when the player is on the first level
    if level2 == 0:
        # set up the variables for the grid locations that the keys are on
        GRID[9][3] = 6
        GRID[10][9] = 8
        # set up variables for the gates opening
        open1 = False
        open2 = False
        # set up code so that picking up a key cause a variable to be set up
        # yellow key
        if player_column == 3 and player_row == 9:
            GRID[9][3] = 2
            key_get_1 += 1
            arcade.play_sound(key_sound)
        if key_get_1 > 0:
            open1 = True
        # green key
        if player_column == 9 and player_row == 10:
            GRID[10][9] = 2
            key_get_2 += 1
            arcade.play_sound(key_sound)
        if key_get_2 > 0:
            open2 = True
    # make this specific code run when the player is on the second level
    if level2 == 1:
        GRID[3][15] = 9
        GRID[5][8] = 11
        GRID[11][13] = 13
        GRID[16][14] = 15
        # set up variables for the gates
        open1 = False
        open2 = False
        open3 = False
        open4 = False
        # set up code so that picking up a key cause a variable to be set up
        # yellow key
        if player_row == 3 and player_column == 15:
            GRID[3][15] = 2
            key_get_1 += 1
            arcade.play_sound(key_sound)
        if key_get_1 > 0:
            open1 = True
        # green key
        if player_row == 5 and player_column == 8:
            GRID[5][8] = 2
            key_get_2 += 1
            arcade.play_sound(key_sound)
        if key_get_2 > 0:
            open2 = True
        # red key
        if player_row == 11 and player_column == 13:
            GRID[11][13] = 2
            key_get_3 += 1
            arcade.play_sound(key_sound)
        if key_get_3 > 0:
            open3 = True
        # gray key
        if player_row == 16 and player_column == 14:
            GRID[16][14] = 2
            key_get_4 += 1
            arcade.play_sound(key_sound)
        if key_get_4 > 0:
            open4 = True

def on_key_press(key, modifiers):
    """Assigns a variable "key" that allows certain keyboard keys to perform certain operations"""
    # assign global variables
    global column, row, player_row, player_column, key_get_1, key_get_2, key_get_3, key_get_4, win, gate_open_1, gate_open_2, gate_open_3, gate_open_4, level2
    # set this specific code to run only when the player is in the first level
    if level2 == 0:
        # set up the "d" key so that it moves the player to the right unless blocked by a gate or wall
        if key == arcade.key.D and GRID[row][column+1] != 1 and column != 14 and GRID[row][column+1] != 2 and GRID[row][column+1] != 7:
            player_column += 1
            column += 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row][column-1] = 2
        # set up the "w" key so that it moves the player up unless blocked by a gate or wall
        if key == arcade.key.W and GRID[row+1][column] != 1 and GRID[row+1][column] != 5 and GRID[row+1][column] != 2:
            player_row += 1
            row += 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row-1][column] = 2
        # set up the "s" key so that it moves the player down unless blocked by a gate or wall
        if key == arcade.key.S and GRID[row-1][column] != 1 and GRID[row-1][column] != 5 and GRID[row-1][column] != 2:
            player_row -= 1
            row -= 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row+1][column] = 2
        # set up the "a" key so that it moves the player to the left unless blocked by a gate or wall
        if (key == arcade.key.A and GRID[row][column-1] != 1) and GRID[row][column-1] != 2 and not (key == arcade.key.A and player_row == 1 and player_column == 0):
            player_column -= 1
            column -= 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row][column+1] = 2
        # create a button that resets the level if the player gets stuck
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
    # make this specific code run when the player is on the second level
    if level2 == 1 and win == 2:
        # set up the "d" key so that it moves the player to the right unless blocked by a gate or wall
        if key == arcade.key.D and GRID[row][column+1] != 1 and column != 19 and GRID[row][column+1] != 2 and GRID[row][column+1] != 8 and GRID[row][column+1] != 10:
            player_column += 1
            column += 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row][column-1] = 2
        # set up the "w" key so that it moves the player up unless blocked by a gate or wall
        if key == arcade.key.W and GRID[row+1][column] != 1 and GRID[row+1][column] != 2 and GRID[row+1][column] != 12 and GRID[row+1][column] != 14:
            player_row += 1
            row += 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row-1][column] = 2
        # set up the "s" key so that it moves the player down unless blocked by a gate or wall
        if key == arcade.key.S and GRID[row-1][column] != 1 and GRID[row-1][column] != 2 and GRID[row-1][column] != 12 and GRID[row-1][column] != 14:
            player_row -= 1
            row -= 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row+1][column] = 2
        # set up the "a" key so that it moves the player to the left unless blocked by a gate or wall
        if (key == arcade.key.A and GRID[row][column-1] != 1) and GRID[row][column-1] != 2 and GRID[row][column-1] != 8 and GRID[row][column-1] != 10 and not (key == arcade.key.A and player_row == 1 and player_column == 0):
            player_column -= 1
            column -= 1
            grid_row.append(row)
            grid_column.append(column)
            GRID[row][column] = 2
            GRID[row][column+1] = 2
        # set up a key that resets the whole level if the player gets stuck
        if key == arcade.key.K:
            # reset player position
            player_row = 1
            player_column = 0
            # resetting the area around the keys
            GRID[3][14] = 0
            GRID[3][16] = 0
            GRID[5][7] = 0
            GRID[5][9] = 0
            GRID[10][13] = 0
            GRID[12][13] = 0
            GRID[16][13] = 0
            GRID[16][15] = 0
            # resetting the player path
            for i in range(len(grid_row)):
                for j in range(len(grid_column)):
                    GRID[grid_row[i]][grid_column[j]] = 0
            if GRID[row][column] == 2:
                GRID[row][column] = 0
            # resetting all key and gate values
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
    """Creates the setup for the grid of the second level"""
    # define global variables
    global row, column, GRID, timer, background_sound
    # set up the grid for the second level
    for row in range(20):
        GRID.append([])
        for column in range(21):
             GRID[row].append(0)

def setup():
    """
    Sets up the screen, the main grid for the first level
    and all functions that allow the game to run
    """
    # define global variables
    global GRID, row, column, key_sound, teleport_sound, complete, background
    # set up the screen width and length using the variables at the beginning alongside the background
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "No Turning Back (Final Project)")
    arcade.set_background_color(arcade.color.BLACK)
    # create a system that constantly updates the game
    arcade.schedule(on_update, 1 / 60)
    # render the first level and the player function
    arcade.start_render()
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_update = on_update
    # create the grid for the first level
    for row in range(ROW_COUNT):
        GRID.append([])
        for column in range(COLUMN_COUNT):
            GRID[row].append(0)
    #load in all necessary sound files that will be used
    background = arcade.load_sound("sounds/background.wav")
    key_sound = arcade.load_sound("sounds/keysound.wav")
    teleport_sound = arcade.load_sound("sounds/teleport.wav")
    complete = arcade.load_sound("sounds/complete.wav")
    # start playing the background music
    arcade.play_sound(background)
    # run the program
    arcade.run()
# run the setup for the game
if __name__ == '__main__':
    setup()
