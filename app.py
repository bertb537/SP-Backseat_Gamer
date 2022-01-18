from PyQt5.QtWidgets import (
    QStackedWidget,
)

from ScreenViews.homescreen import HomeScreen
from ScreenViews.datatracking import DataTracking
from ScreenViews.statscreen import StatScreen


APP_TITLE = "Backseat Gamer"
APP_DEFAULT_SCREEN_SIZE = [800, 500]


class MainWindow(QStackedWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Add the screens
        self.addWidget(HomeScreen())
