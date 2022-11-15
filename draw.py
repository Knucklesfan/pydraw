from PIL import Image
import pyautogui
import time

gap = 2;
pyautogui.PAUSE = 0
im = Image.open("waltuh.png")
px = im.load()
width, height = im.size
time.sleep(4)
mousex,mousey = pyautogui.position()
pyautogui.moveTo(mousex, mousey, duration=0)

for x in range(width):
    for y in range(height):
        pyautogui.moveTo(mousex+(x*gap), mousey+(y*gap), duration=0)
        if px[x, y] != 1:
            pyautogui.click()