from tkinter import *
from tkinter.ttk import *

import app
from homescreen import init_homescreen
import styles as st


def init_mainwindow():
    window = Tk()
    window.title(app.APP_TITLE)
    window.resizable
    st.apply_styles(window)

    # Initialize Homescreen
    init_homescreen(window)


if __name__ == '__main__':
    init_mainwindow()


