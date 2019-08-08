from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QAction
from Browser import Browser


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setCentralWidget(Browser())
        self._setup_actions()
        self._setup_menu_bar()

    def _setup_actions(self):
        self._print_action = QAction('print')
        self._print_action.setShortcut('Ctrl+P')
        self._print_action.triggered.connect(self._print)

    def _setup_menu_bar(self):
        self._menu_bar = self.menuBar()
        self._print_menu = self._menu_bar.addMenu('print')
        self._print_menu.addAction(self._print_action)

    def _print(self):
        print('printing...')