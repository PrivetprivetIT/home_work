from logging import fatal

from tank import Tank
from tkinter import*
import world
import tanks_collection
import texture

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68

KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37, 39, 38, 40

SPACE = 32

FPS = 60

def update():
    tanks_collection.update()

    player = tanks_collection.get_player()

    world.set_camera_xy(player.get_x() - world.SCREEN_WIDTH // 2 + player.get_size() // 2,
                        player.get_y() - world.SCREEN_HEIGHT // 2 + player.get_size() // 2)

    world.update_map()
    w.after(1000//FPS, update)

def key_press(event):

    player = tanks_collection.get_player()

    if event.keycode == KEY_W:
        player.forward()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()

    elif event.keycode == KEY_UP:
        world.move_camera(delta_x = 0, delta_y = -5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(delta_x = 0, delta_y = 5)
    elif event.keycode == KEY_LEFT:
        world.move_camera(delta_x = -5, delta_y = 0)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(delta_x = 5, delta_y = 0)

    elif event.keycode == SPACE:
        tanks_collection.spawn()

def load_textures():
    texture.load('tank_up', '../img/tank_up.png')
    texture.load('tank_down', '../img/tank_down.png')
    texture.load('tank_left', '../img/tank_left.png')
    texture.load('tank_right', '../img/tank_right.png')
    texture.load(world.BRICK, '../img/brick.png')
    texture.load(world.WATER, '../img/water.png')
    texture.load(world.CONCRETE, '../img/wall.png')
    print(texture._frames)

w = Tk()

load_textures()

w.title('Танки на минималках 2.0')
canv = Canvas(w, width = world.SCREEN_WIDTH, height = world.SCREEN_HEIGHT,
              bg = '#8ccb5e')
canv.pack()

world.initialaze(canv)

tanks_collection.initialaze(canv)

w.bind('<KeyPress>', key_press)

update()
w.mainloop()