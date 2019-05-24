import arcade
WIDTH = 30
HEIGHT= 30
MARGIN = 2
ROW_COUNT = 15
COLUMN_COUNT = 15
GRID = []

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN + 200
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


def on_update(delta_time):
    pass

def player(row, column):
    row = 1
    column = 0
    GRID[row][column] = 2

def on_draw():

    for row in range(ROW_COUNT):
        for column in range(COLUMN_COUNT):
            if row == 0 or row == 14 or (column == 0 and row != 1) or (column == 14 and row != 13):
                GRID[row][column] = 1

            if GRID[row][column] == 0:
                color = arcade.color.WHITE
            elif GRID[row][column] == 1:
                color = arcade.color.PURPLE
            elif GRID[row][column] == 2:
                color = arcade.color.BLUE


            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
            y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
            arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    arcade.draw_rectangle_filled(513, 434, 62, 62, arcade.color.WHITE)



def on_key_press(arcade_key_d, modifiers):
    pass


def setup():
    global GRID


    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.BLACK)
    arcade.schedule(on_update, 1 / 60)

    arcade.start_render()
    window = arcade.get_window()
    window.player = player
    window.on_draw = on_draw


    for row in range(ROW_COUNT):
        GRID.append([])
        for column in range(COLUMN_COUNT):
            GRID[row].append(0)
    arcade.run()

if __name__ == '__main__':
    setup()