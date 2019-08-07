from PyQt5.QtWidgets import *


class SearchBar(QLineEdit):

    def __init__(self, text):
        super().__init__(text)
        self._parent_browser = None

    def set_parent_browser(self, browser):
        self._parent_browser = browser

    def keyPressEvent(self, e):
        super().keyPressEvent(e)
        if e.key() == 0x01000004:
            self._parent_browser.request_search(self.text())