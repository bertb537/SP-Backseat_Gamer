import sys

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

import app
import styles as st


class DataTracking(QWidget):
    def __init__(self, switchBack, user: str = "", BattlenetID: str = ""):
        super().__init__()

        self._funct_switch_back = switchBack
        self._user = user
        self._BattlenetID = BattlenetID

        backBtn = QPushButton("Back")

        backBtn.setStyleSheet(st.backwardNavBtn)

        backBtn.clicked.connect(self.__back_click())

        layout = QVBoxLayout()
        layout.addWidget(backBtn)

        self.setLayout(layout)

    def __back_click(self):
        self._funct_switch_back(self._user, self._BattlenetID)