from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
    QGridLayout
)

import styles as st


class HomeScreen(QWidget):
    def __init__(self, switchStats, switchTracking, user: str = "", BattlenetID: str = ""):
        super().__init__()

        self._user = user
        self._BattlenetID = BattlenetID

        self._funct_switch_tracking = switchTracking
        self._funct_switch_stats = switchStats

        # Init Widgets
        header = QLabel("Backseat Gamer")
        userIDLabel = QLabel("User:")
        userIDLineEdit = QLineEdit()
        usernameLabel = QLabel("Battlenet ID:")
        usernameLineEdit = QLineEdit()
        statsBtn = QPushButton("View Stats")
        trackingBtn = QPushButton("Start Tracking")

        # Style Widgets
        header.setStyleSheet(st.h1)
        userIDLabel.setStyleSheet(st.body)
        userIDLineEdit.setStyleSheet(st.lineEdit)
        usernameLabel.setStyleSheet(st.body)
        usernameLineEdit.setStyleSheet(st.lineEdit)
        statsBtn.setStyleSheet(st.forwardNavBtn)
        trackingBtn.setStyleSheet(st.forwardNavBtn)

        # Apply Click listeners
        trackingBtn.clicked.connect(self.__start_tracking_click)

        # Create UI
        layout = QGridLayout()

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setColumnStretch(2, 1)
        layout.setColumnStretch(3, 1)

        layout.addWidget(header, 0, 0, 1, 0, Qt.AlignCenter)

        layout.addWidget(userIDLabel, 1, 0, 1, 1, Qt.AlignLeft)
        layout.addWidget(userIDLineEdit, 1, 1, 1, 3)
        layout.addWidget(usernameLabel, 2, 0, 1, 1, Qt.AlignLeft)
        layout.addWidget(usernameLineEdit, 2, 1, 1, 3)
        layout.addWidget(statsBtn, 3, 0, 1, 2, Qt.AlignLeft)
        layout.addWidget(trackingBtn, 3, 2, 1, 2, Qt.AlignRight)

        # Set layout and central widget
        self.setLayout(layout)

        self.setFixedSize(400, 150)

    def __start_tracking_click(self):
        self._funct_switch_tracking(self._user, self._BattlenetID)
