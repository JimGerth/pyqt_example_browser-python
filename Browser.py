from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class Browser(QWidget):

    def __init__(self):
        super().__init__()

        self._web_view = QWebEngineView()
        self._search_bar = QWidget()

        self._back_button = QPushButton(text="back")
        self._back_button.clicked.connect(self._back)

        self._load_button = QPushButton(text="load")
        self._load_button.clicked.connect(self._load)

        self._search_text_field = QLineEdit('enter search or address')
        self._search_text_field.returnPressed.connect(self._load)


        self._setup_menu_bar()
        self._setup_web_view()
        self._setup_actions()
        self._setup_self()

    def _setup_menu_bar(self):
        layout = QHBoxLayout()
        layout.addWidget(self._back_button)
        layout.addWidget(self._load_button)
        layout.addWidget(self._search_text_field)
        layout.setSpacing(5)
        layout.setContentsMargins(10, 10, 10, 10)
        self._search_bar.setLayout(layout)

    def _setup_web_view(self):
        pass

    def _setup_self(self):
        layout = QVBoxLayout()
        layout.addWidget(self._web_view)
        layout.addWidget(self._search_bar)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def _setup_actions(self):
        printAction = QAction('print')
        printAction.setShortcut('Ctrl+P')
        printAction.triggered.connect(self._print)

    def _load(self):
        self._web_view.load(QUrl(self._search_text_field.text()))
        if not self._web_view.url().url(): # check if web view recognized the url as valid
            self._web_view.load(QUrl('https://www.google.com/search?q=' + self._search_text_field.text()))

    def _back(self):
        self._web_view.back()

    def _print(self):
        print('printing...')