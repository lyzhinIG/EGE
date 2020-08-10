import pyperclip
from ctypes import windll

pyperclip.copy('The text to be copied to the clipboard.')
n = input() 
if windll.user32.OpenClipboard(None):
    windll.user32.EmptyClipboard()
    windll.user32.CloseClipboard()
n = input()
x = input()
