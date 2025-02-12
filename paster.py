import pyautogui
from pynput import keyboard
from pynput.keyboard import Controller
from pynput.keyboard import Key
import clipboard as c
 

screenWidth, screenHeight = pyautogui.size()
keyBoard = Controller()


def type_string(string):
    string=string
    keyBoard.release(Key.ctrl_l)
    keyBoard.release(Key.ctrl_r)
    print(string)
    for character in string:  
        keyBoard.type(character)  
    return  

def on_activate():
    type_string(c.paste())

with keyboard.GlobalHotKeys({'<ctrl>+`':on_activate}) as h:
    h.join()


    