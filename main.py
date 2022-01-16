import sys

from PyQt5 import QtGui as Gui

import app
from homescreen import init_homescreen
import styles as st


def init_application():
    # Create the application and its main window
    application = Gui.QGuiApplication(sys.argv)
    main_window = Gui.QWidget()
    main_window.setGeometry(0, 0, 800, 500)
    main_window.setWindowTitle(app.APP_TITLE)

    # Initialize Homescreen
    init_homescreen(application, main_window)


if __name__ == '__main__':
    init_application()


