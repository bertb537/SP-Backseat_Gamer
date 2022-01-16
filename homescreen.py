from PyQt5 import QtGui as Gui
import pyautogui
from PIL import Image, ImageTk

import app
import styles as st


def screen_capture():
    screenshot = pyautogui.screenshot()
    screenshot = ImageTk.PhotoImage(screenshot)

    return screenshot


def init_homescreen(application: Gui.QGuiApplication, window: Gui.QWidget):
    title = Gui.QLabel(window)
    title

    while True:
        screenshot = screen_capture()
        screenViewer = Label(frame, image=screenshot)
        screenViewer.grid(row=1, column=0)
        screenViewer.image = screenshot
        window.update_idletasks()
        window.update()
