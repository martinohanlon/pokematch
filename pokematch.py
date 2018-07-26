import os
from guizero import App, Box, Text, Picture, PushButton
from random import shuffle, randint

def get_random_sprite():
    sprite_path = os.path.join(sprites_dir, sprites.pop())
    return sprite_path

def setup_round():
    instructions.value = "Match the pokemon"
    instructions.text_color = "black"

    # set random pokemon for the buttons and pictures
    for picture in pictures:
        picture.image = get_random_sprite()
        picture.width = 100
        picture.height = 100
        picture.update_command(match_picture, args=[False])
    
    for button in buttons:
        button.image = get_random_sprite()
        button.width = 100
        button.height = 100
        button.update_command(match_picture, args=[False])

    # get a random sprite to be matched
    matched_sprite = get_random_sprite()

    # place the matched sprite on a random location
    random_picture = randint(0,8)
    pictures[random_picture].image = matched_sprite
    pictures[random_picture].update_command(match_picture, args=[True])

    random_button = randint(0,8)
    buttons[random_button].image = matched_sprite
    buttons[random_button].update_command(match_picture, args=[True])
    
def match_picture(matched):
    if matched:
        instructions.value = "well done"
        instructions.text_color = "green"
        score.value = int(score.value) + 1
    else:
        instructions.value = "incorrect"
        instructions.text_color = "red"
        score.value = int(score.value) - 1

    app.after(1000, setup_round)

def start_game():
    score.value = "0"
    picture.hide()
    play.hide()
    pictures_box.show()
    buttons_box.show()
    score.show()
    time_left.show()
    time_left.value = "30"
    time_left.repeat(1000, timer)
    setup_round()

def timer():
    time_left.value = int(time_left.value) - 1
    if time_left.value == "0":
        pictures_box.hide()
        buttons_box.hide()
        score.hide()
        time_left.hide()
        picture.show()
        play.show()
        instructions.value = "Time out - score = " + score.value
        time_left.cancel(timer)

# load the sprites
sprites_dir = "pokemon"
sprites = [f for f in os.listdir(sprites_dir) if os.path.isfile(os.path.join(sprites_dir, f))]
shuffle(sprites)

app = App(title="Pokematch", layout="grid", width=650, height=400)

instructions = Text(app, grid=[0,0], text="Get ready...")

time_left = Text(app, grid=[1,0])

# create the boxes for the pictures and the buttons
pictures_box = Box(app, layout="grid", grid=[0,1], visible=False)
pictures_box.bg = "dodger blue"

buttons_box = Box(app, layout="grid", grid=[1,1], visible=False)
buttons_box.bg = "royal blue"

# create the buttons and pictures
pictures = []
buttons = []
for x in range(0,3):
        for y in range(0,3):
            picture = PushButton(pictures_box, grid=[x,y])
            pictures.append(picture)
            
            button = PushButton(buttons_box, grid=[x,y])
            buttons.append(button)

# score
score = Text(app, grid=[0,2,2,1], visible=False)

picture = Picture(app, grid=[0,3,2,1], image=get_random_sprite())

# play button
play = PushButton(app, text="Play", grid=[0,4,2,1], command=start_game)

app.display()