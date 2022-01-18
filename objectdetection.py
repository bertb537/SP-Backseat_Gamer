import pyautogui
from PIL import ImageTk


def screen_capture():
    screenshot = pyautogui.screenshot()
    screenshot = ImageTk.PhotoImage(screenshot)

    return screenshot


class ObjectDetection:
    def __init__(self, userID: str, username: str):
        super().__init__()

        self._userID = userID
        self._username = username
