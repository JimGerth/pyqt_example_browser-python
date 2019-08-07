from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import re


class Browser(QWidget):

    def __init__(self):
        super().__init__()

        self._web_view = QWebEngineView()
        self._menu_bar = QWidget()
        self._back_button = QPushButton(text="back")
        self._load_button = QPushButton(text="load")
        self._search_bar = SearchBar('enter search or address')

        self._init_menu_bar()
        self._init_web_view()
        self._init_self()

    def _init_menu_bar(self):
        layout = QHBoxLayout()
        layout.addWidget(self._back_button)
        layout.addWidget(self._load_button)
        layout.addWidget(self._search_bar)
        self._menu_bar.setLayout(layout)

    def _init_web_view(self):
        pass

    def _init_self(self):
        layout = QVBoxLayout()
        layout.addWidget(self._web_view)
        layout.addWidget(self._menu_bar)
        self.setLayout(layout)


class SearchBar(QLineEdit):
    def keyPressEvent(self, e):
        super().keyPressEvent(e)
        if e.key() == 0x01000004:
            print('enter pressed')
            is_url = re.match('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', self.text())
            if not is_url:
                print('enter a valid url!')
            else:
                print(f'loading {self.text()}...')

app = QApplication([])

browser = Browser()
browser.show()

app.exec_()