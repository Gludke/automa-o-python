from pyautogui import moveTo, click
import pyautogui
import time
# import keyboard
import random
# import win32api, win32con

# pyautogui.keyDown('alt')
# #Aperta e solta a tecla:
# pyautogui.press(['tab'])
# pyautogui.keyUp('alt')

#clicar no círculo
# pyautogui.click('circle.png')

while 1 :
    if (pyautogui.locateOnScreen('circle.png', confidence=0.9)):
        print('Imagem encontrada')
        pyautogui.moveTo('circle.png')
        time.sleep(0.7)
    else:
        print('Imagem não encontrada...')
        time.sleep(0.7)
        pyautogui.moveTo(500, 500)


