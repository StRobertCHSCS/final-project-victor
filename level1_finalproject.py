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
key_get = 0
gate_open_1 = 0
gate_open_2 = 0
win = 0

def player():
    global GRID, x, y, color, row, column, player_row, player_column, open, gate_open_1, gate_open_2, win
    row = player_row
    column = player_column
    GRID[row][column] = 2
    arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
    if player_column == 14 and player_row == 13:
        win += 1
    if win == 1:
        arcade.draw_text("YOU WIN", 550, 200, arcade.color.WHITE, 12)

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
    if open == True and gate_open_2 == 0:
        GRID[9][3] = 2
        GRID[13][12] = 0
    if open == True and gate_open_2 > 0:
        GRID[11][7] = 2
        GRID[13][12] = 2



def on_draw():
    global GRID, color, column, row, x, y
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            if row == 0 or row == 14 or (column == 0 and row != 1) or (column == 14 and row != 13):
                GRID[row][column] = 1
            if column == 15:
                GRID[row][column] = 3

            if GRID[row][column] == 0:
                color = arcade.color.WHITE
            elif GRID[row][column] == 1:
                color = arcade.color.PURPLE
            elif GRID[row][column] == 5:
                color = arcade.color.YELLOW
            elif GRID[row][column] == 6:
                color = arcade.color.DARK_YELLOW
            elif GRID[row][column] == 2:
                color = arcade.color.BLUE
            elif GRID[row][column] == 3:
                color = arcade.color.BLACK
            elif GRID[row][column] == 4:
                color = arcade.color.BLUEBERRY




            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
            y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
            arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

            for r in range(2, 5):
                GRID[r][2] = 1
            for r in range(6, 13):
                GRID[r][2] = 1
            for c in range(2, 5):
                GRID[6][c] = 1
            for r in range(2, 7):
                GRID[r][4] = 1
            for c in range(2, 5):
                GRID[2][c] = 1
            for r in range(2, 12):
                GRID[r][12] = 1
            for r in range(2, 10):
                GRID[r][10] = 1
            for r in range(8, 12):
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
    key()
    gate()
    player()


def on_update(delta_time):
    pass

def gate():
    global GRID, row, column, player_colum, player_row, key_get, gate_open_1, gate_open_2
    GRID[11][7] = 5
    GRID[13][12] = 5
    if key_get > 0 and player_column == 7 and player_row == 11:
        GRID[11][7] = 2
        gate_open_1 += 1
    if key_get > 0 and player_column == 12 and player_row == 13:
        GRID[13][12] = 2
        gate_open_2 += 1
    if gate_open_1 > 0:
        GRID[11][7] = 2
    if gate_open_2 > 0:
        GRID[13][12] = 2

def key():
    global GRID, row, column, open, player_column, player_row, key_get
    GRID[9][3] = 6
    open = False
    if player_column == 3 and player_row == 9:
        GRID[9][3] = 2
        key_get += 1
    if key_get > 0:
        open = True

def on_key_press(key, modifiers):
    global column, row, player_row, player_column, key_get, win
    if key == arcade.key.D and GRID[row][column+1] != 1 and column != 14 and GRID[row][column+1] != 2:
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
        key_get = 0
        GRID[11][7] = 5
        win = 0

def on_key_release(arcade_key_d, modifiers):
    global column, row, player_row, player_column
    pass


def setup():
    global GRID


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