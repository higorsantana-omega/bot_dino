from PIL import ImageGrab as ig
import pyautogui
import time

# enemy color: 172, 172, 172
x = 220.0

def screen():
    screen_print = ig.grab()
    return screen_print

def enemy(screen_print):
    for x in range(int(x), int(x+80)):
        for y in range(410, 465):
            enemy_color = screen_print.getpixel((x, y))
            if enemy_color == (172, 172, 172):
                return True

print('Iniciando em 3 segundos')
time.sleep(3)

while True:
    screen_print = screen()
    if enemy(screen_print):
        global x
        pyautogui.press('space')
        x += 0.5
    print(enemy(screen_print))