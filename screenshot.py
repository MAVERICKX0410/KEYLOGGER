import pyautogui
import time

time.sleep(2)
p = 1

while True:
    print(p)
    x ="Screenshot"+ str(p) +".png"
    print(x)
    screenshot = pyautogui.screenshot()
    screenshot.save(r"C:\Users\Khawa\Desktop\PYLOGGY\SCREENSHOT" + x)
    p = p + 1
    time.sleep(2)
    pass
