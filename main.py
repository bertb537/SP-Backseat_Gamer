import sys

from PyQt5 import QtWidgets

from ScreenViews.screens import MainWindow

if __name__ == '__main__':
    # Create the application and its main window
    application = QtWidgets.QApplication(sys.argv)

    # Initialize Homescreen
    window = MainWindow()
    window.show()
    sys.exit(application.exec_())
