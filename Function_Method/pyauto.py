from msvcrt import putch
import pyautogui

for i in range(1,1000):
    pyautogui.write("I love python",interval=0.1)
    pyautogui.press('enter')
