from PyQt5.QtWidgets import (
    QStackedWidget,
    QDialog,
)
from PyQt5.uic import loadUi


class MainWindow(QStackedWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Add the screens
        self.setWindowTitle("Backseat Gamer")
        self.addWidget(HomeScreen(self))


class HomeScreen(QDialog):
    def __init__(self, mainWindow: MainWindow, user: str = "", BattlenetID: str = ""):
        super(HomeScreen, self).__init__()
        loadUi('ScreenViews/HomeScreen.ui', self)

        self._user = user
        self._BattlenetID = BattlenetID
        self._main_window = mainWindow

        self.trackingNavBtn.clicked.connect(self.__start_tracking_click)
        self.statsNavBtn.clicked.connect(self.__view_stats_click)

    def __start_tracking_click(self):
        self._main_window.addWidget(DataTracking(self._main_window, self._user, self._BattlenetID))
        self._main_window.setCurrentIndex(self._main_window.currentIndex()+1)

    def __view_stats_click(self):
        self._main_window.addWidget(StatScreen(self._main_window, self._user, self._BattlenetID))
        self._main_window.setCurrentIndex(self._main_window.currentIndex()+1)


class DataTracking(QDialog):
    def __init__(self, mainWindow: MainWindow, user: str = "", BattlenetID: str = ""):
        super(DataTracking, self).__init__()
        loadUi('ScreenViews/TrackingScreen.ui', self)

        self._user = user
        self._BattlenetID = BattlenetID
        self._main_window = mainWindow

        self.returnNavBtn.clicked.connect(self.__back_click)

    def __back_click(self):
        self._main_window.addWidget(HomeScreen(self._main_window, self._user, self._BattlenetID))
        self._main_window.setCurrentIndex(self._main_window.currentIndex()+1)


class StatScreen(QDialog):
    def __init__(self, mainWindow, user: str = "", BattlenetID: str = ""):
        super(StatScreen, self).__init__()
        loadUi('ScreenViews/StatisticsScreen.ui', self)

        self._user = user
        self._BattlenetID = BattlenetID
        self._main_window = mainWindow

        self.returnNavBtn.clicked.connect(self.__back_click)

    def __back_click(self):
        self._main_window.addWidget(HomeScreen(self._main_window, self._user, self._BattlenetID))
        self._main_window.setCurrentIndex(self._main_window.currentIndex()+1)
