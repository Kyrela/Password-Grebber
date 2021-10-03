"""
The automatic password generation, without interface. Works only with the mode 0.
"""


from pyperclip import paste
from keyboard import write
from generator import generate

write(generate(paste()))
