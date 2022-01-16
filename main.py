import sys

from PyQt5 import QtWidgets

from homescreen import HomeScreen


if __name__ == '__main__':
    # Create the application and its main window
    app = QtWidgets.QApplication(sys.argv)

    # Initialize Homescreen
    window = HomeScreen()
    window.show()
    sys.exit(app.exec_())
