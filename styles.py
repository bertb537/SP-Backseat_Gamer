from tkinter import *
from tkinter.ttk import *

FONT = 'Arial'
DEFAULT_BTN_COLOR = 1


def apply_styles(frame):
    style = Style(frame)
    global FONT
    style.configure("Title.Label", font=(FONT, 32))

