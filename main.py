import sys

from PyQt5.QtCore import Qt

from homescreen import HomeScreen


if __name__ == '__main__':
    # Create the application and its main window
    application = Qt.QGuiApplication(sys.argv)

    # Initialize Homescreen
    window = HomeScreen()
