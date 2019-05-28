import arcade
WIDTH = 30
HEIGHT= 30
MARGIN = 2
ROW_COUNT = 15
COLUMN_COUNT = 15
GRID = []

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN + 200
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


def player():
    global GRID, x, y, color, row, column, player_row, player_column
    row = 1
    column = 0
    player_row = row
    player_column = column
    GRID[row][column] = 2
    arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

def on_draw():
    global GRID, color, column, row, x, y
    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            if row == 0 or row == 14 or (column == 0 and row != 1) or (column == 14 and row != 13):
                GRID[row][column] = 1

            if GRID[row][column] == 0:
                color = arcade.color.WHITE
            if GRID[row][column] == 1:
                color = arcade.color.PURPLE
            if GRID[row][column] == 2:
                color = arcade.color.BLUE

            arcade.draw_rectangle_filled(513, 434, 62, 62, arcade.color.WHITE)
            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
            y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
            arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
    player()

def on_update(delta_time):
    pass


def on_key_press(arcade_key_d, modifiers):
    global column, row, player_row, player_column
    player()
    player_column += 1
    column += 1
    GRID[row][column] = 2

def on_key_release(arcade_key_d, modifiers):
    player()
    player_column


def setup():
    global GRID


    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1 / 60)

    arcade.start_render()
    window = arcade.get_window()
    window.on_draw = on_draw
    window.player = player
    window.on_key_press = on_key_press
    window.on_update = on_update



    for row in range(ROW_COUNT):
        GRID.append([])
        for column in range(COLUMN_COUNT):
            GRID[row].append(0)
    arcade.run()

if __name__ == '__main__':
    setup()