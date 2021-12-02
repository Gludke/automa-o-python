import pyautogui

pyautogui.keyDown('alt')
#Aperta e solta a tecla:
pyautogui.press(['tab'])
pyautogui.keyUp('alt')

pyautogui.write('1, 2, 3')
#Pode receber lista de tecla a ser pressionada:
pyautogui.press(['left', 'left', 'left'])



