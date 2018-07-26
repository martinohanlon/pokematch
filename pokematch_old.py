import os
import sys
from guizero import App, Box, Text, Picture, PushButton
from random import choice, randint, shuffle
from time import sleep
if sys.platform == "darwin":
    from PIL import Image

def match(chosen):
    if chosen:
        # correct
        score.value = int(score.value) + 1
        show_message("Correct", "green")
        app.after(1000, clear_message)
    else:
        # incorrect
        score.value = int(score.value) - 1
        show_message("Incorrect", "red")
        app.after(1000, clear_message)

    destroy_board()
    setup_board()

def show_message(message, color):
    player_message.text_color = color
    player_message.value = message

def clear_message():
    player_message.value = "Match the pokemon"
    player_message.text_color = "black"

def countdown():
    timer.value = int(timer.value) - 1
    if timer.value == "9":
        timer.text_color = "red"
    elif timer.value == "0":
        timer.cancel(countdown)
        game_over()

def game_over():
    game_window.hide()
    result.value = "Game over, you scored {}".format(score.value)
    results_window.show()
    app.after(2000, return_to_menu)

def destroy_board():
    for picture in pictures:
        picture.destroy()

    for button in buttons:
        button.destroy()

def setup_board():

    pictures = []
    buttons = []

    for x in range(0,3):
        for y in range(0,3):

            picture = Picture(picture_grid, image = get_random_sprite(), grid = [x,y])
            picture.bg = "royal blue"
            picture.tk.config(height = 100)
            picture.tk.config(width = 100)
            pictures.append(picture)

    button_number = 0
    for x in range(0,3):
        for y in range(0,3):
            button = PushButton(button_grid, command = match, args = [False], grid = [x,y])
            button.width = 100
            button.height = 100
            button.icon(get_random_sprite())
            button.bg = "dodger blue"
            button_number += 1
            buttons.append(button)

    chosen_one = get_random_sprite()

    winning_button = randint(0,8)
    buttons[winning_button].icon(chosen_one)
    buttons[winning_button].update_command(match, args = [True])
    pictures[randint(0,8)].value = chosen_one

    app.display()

def get_random_sprite():
    sprite_path = os.path.join(sprites_dir, sprites.pop())
    # if its macos convert it to a gif
    if sys.platform == "darwin":
        sprite_path_gif = sprite_path + ".gif"
        Image.open(sprite_path).save(sprite_path_gif)
        sprite_path = sprite_path_gif
    return sprite_path

def start_game():
    timer.value = "60"
    timer.repeat(1000, countdown)
    score.value = "0"
    menu_window.hide()
    game_window.show()

def return_to_menu():
    menu_window.show()
    game_window.hide()
    results_window.hide()
    
app = App("PokeMatch", width=700, layout="grid")

# this is the menu window
menu_window = Box(app, grid=[0,0])

title = Text(menu_window, "PokeMatch", size=24, color="dodger blue")
instructions = Text(menu_window, "Its so simple...  Just find the pokemon on the right that matches one on the left.")
instructions.font = "Verdana"
start = PushButton(menu_window, command=start_game, text="Start")
start.bg = "dodger blue"

# this is the playing window
game_window = Box(app, layout="grid", grid=[0,1])
game_window.hide()

player_message = Text(game_window, "Match the pokemon", grid=[0,0,3,1], size=16)
timer = Text(game_window, grid=[0,1], size=16)
score = Text(game_window, grid=[2,1], size=16)

picture_grid = Box(game_window, layout="grid", grid=[0,2])
picture_grid.bg = "royal blue"

seperator = Text(game_window, text = ">", size=24, color = "dodger blue", grid=[1,2])

button_grid = Box(game_window, layout="grid", grid=[2,2] )
button_grid.bg = "dodger blue"

# this is the results window
results_window = Box(app, grid=[0,2])
result = Text(results_window)
result.font = "Verdana"

# load the sprites
sprites_dir = "pokemon"
sprites = [f for f in os.listdir(sprites_dir) if os.path.isfile(os.path.join(sprites_dir, f))]
shuffle(sprites)

# create
pictures = []
buttons = []

setup_board()

app.display()