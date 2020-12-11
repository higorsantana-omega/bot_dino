from PIL import ImageGrab as ig

# enemy color: 172, 172, 172

def screen():
    screen_print = ig.grab()
    return screen_print

def enemy(screen_print):
    enemy_color = screen_print.getpixel()


while True:
    screen_print = screen()
    print(screen_print)