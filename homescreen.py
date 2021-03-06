from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)
import pyautogui
from PIL import Image, ImageTk

import app
import styles as st


class HomeScreen(QMainWindow):
    def __init__(self, userID: str = "", username: str = ""):
        super().__init__()

        self._userID = userID
        self._username = username

        self.setWindowTitle(app.APP_TITLE)
