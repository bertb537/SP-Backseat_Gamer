from tkinter import *
from tkinter.ttk import *
import pyautogui
from PIL import Image, ImageTk

import app
import styles as st


def screen_capture():
    screenshot = pyautogui.screenshot()
    screenshot = ImageTk.PhotoImage(screenshot)

    return screenshot


def init_homescreen(window: Tk):
    frame = Frame(window)
    frame.pack()

    Label(frame, text=app.APP_TITLE, style="Title.Label").grid(row=0, column=0)

    while True:
        screenshot = screen_capture()
        screenViewer = Label(frame, image=screenshot)
        screenViewer.grid(row=1, column=0)
        screenViewer.image = screenshot
        window.update_idletasks()
        window.update()
