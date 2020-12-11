from PIL import ImageGrab as ig
import pyautogui
import time

# enemy color: 172, 172, 172
X = 270.0

def screen():
    screen_print = ig.grab()
    return screen_print

def enemy(screen_print):
    for x in range(int(X), int(X+80)):
        for y in range(410, 465):
            enemy_color = screen_print.getpixel((x, y))
            if enemy_color == (172, 172, 172):
                return True

def jump():
    global X
    pyautogui.press('space')
    X += 0.8

print('Iniciando em 3 segundos')
time.sleep(3)

while True:
    screen_print = screen()
    if enemy(screen_print):
        jump()
    print(enemy(screen_print))